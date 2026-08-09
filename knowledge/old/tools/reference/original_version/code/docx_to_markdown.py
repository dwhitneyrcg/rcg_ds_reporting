"""
docx_to_markdown.py
Converts .docx files to Markdown format preserving:
- Paragraph text with bold/italic emphasis
- Headings (mapped to Markdown heading levels)
- Tables (converted to Markdown pipe tables)
- Bulleted and numbered lists

Usage:
    python docx_to_markdown.py <input.docx> [output.md]
    python docx_to_markdown.py <input_directory> [output_directory]

If output path is omitted, .md files are created alongside the .docx files.
"""

import os
import sys
import re
import logging
from pathlib import Path
from datetime import datetime

try:
    from docx import Document
    from docx.oxml.ns import qn
except ImportError:
    print("python-docx is required. Install with: pip install python-docx")
    sys.exit(1)

# Configure logging
LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / f"docx_to_markdown_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def get_heading_level(paragraph) -> int | None:
    """Return the heading level (1-6) or None if not a heading."""
    style_name = paragraph.style.name if paragraph.style else ""
    if style_name.startswith("Heading"):
        try:
            return int(style_name.split()[-1])
        except (ValueError, IndexError):
            return None
    return None


def is_list_item(paragraph) -> tuple[bool, bool]:
    """Check if paragraph is a list item. Returns (is_list, is_numbered)."""
    pPr = paragraph._element.find(qn("w:pPr"))
    if pPr is not None:
        numPr = pPr.find(qn("w:numPr"))
        if numPr is not None:
            ilvl = numPr.find(qn("w:ilvl"))
            level = int(ilvl.get(qn("w:val"))) if ilvl is not None else 0
            numId = numPr.find(qn("w:numId"))
            # Heuristic: numId > 1 is often numbered lists
            is_numbered = numId is not None and numId.get(qn("w:val"), "0") != "0"
            return True, is_numbered
    # Fallback: check if text starts with bullet-like chars
    text = paragraph.text.strip()
    if text and text[0] in ("•", "·", "-", "–", "►"):
        return True, False
    return False, False


def get_list_indent(paragraph) -> int:
    """Get indent level for list items (0-based)."""
    pPr = paragraph._element.find(qn("w:pPr"))
    if pPr is not None:
        numPr = pPr.find(qn("w:numPr"))
        if numPr is not None:
            ilvl = numPr.find(qn("w:ilvl"))
            if ilvl is not None:
                return int(ilvl.get(qn("w:val")))
    return 0


def runs_to_markdown(paragraph) -> str:
    """Convert paragraph runs to markdown with bold/italic formatting."""
    parts = []
    for run in paragraph.runs:
        text = run.text
        if not text:
            continue
        is_bold = run.bold
        is_italic = run.italic

        if is_bold and is_italic:
            text = f"***{text}***"
        elif is_bold:
            text = f"**{text}**"
        elif is_italic:
            text = f"*{text}*"

        parts.append(text)

    result = "".join(parts)
    # Clean up adjacent formatting markers: **text****more text** -> **text more text**
    result = re.sub(r"\*\*\*\*", " ", result)
    result = re.sub(r"\*\*\s+\*\*", " ", result)
    return result


def table_to_markdown(table) -> str:
    """Convert a docx table to a Markdown pipe table."""
    rows = []
    for row in table.rows:
        cells = []
        for cell in row.cells:
            cell_text = cell.text.strip().replace("|", "\\|").replace("\n", " ")
            cells.append(cell_text)
        rows.append(cells)

    if not rows:
        return ""

    # Normalize column count
    max_cols = max(len(r) for r in rows)
    for r in rows:
        while len(r) < max_cols:
            r.append("")

    lines = []
    # Header row
    lines.append("| " + " | ".join(rows[0]) + " |")
    # Separator
    lines.append("| " + " | ".join("---" for _ in rows[0]) + " |")
    # Data rows
    for row in rows[1:]:
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)


def convert_docx_to_markdown(docx_path: str | Path) -> str:
    """Convert a .docx file to Markdown string."""
    docx_path = Path(docx_path)
    logger.info(f"Converting: {docx_path.name}")

    doc = Document(str(docx_path))
    md_lines: list[str] = []
    numbered_counter = 0

    # Interleave paragraphs and tables in document order
    body = doc.element.body
    for child in body:
        tag = child.tag.split("}")[-1] if "}" in child.tag else child.tag

        if tag == "p":
            # Find matching paragraph object
            para = None
            for p in doc.paragraphs:
                if p._element is child:
                    para = p
                    break
            if para is None:
                continue

            text = runs_to_markdown(para)
            raw_text = para.text.strip()

            if not raw_text:
                md_lines.append("")
                numbered_counter = 0
                continue

            # Check heading
            heading_level = get_heading_level(para)
            if heading_level:
                md_lines.append("")
                md_lines.append(f"{'#' * heading_level} {raw_text}")
                md_lines.append("")
                numbered_counter = 0
                continue

            # Check list
            is_list, is_numbered = is_list_item(para)
            if is_list:
                indent_level = get_list_indent(para)
                indent = "  " * indent_level
                # Strip leading bullet chars from text
                clean_text = re.sub(r"^[•·\-–►]\s*", "", text).strip()
                if is_numbered:
                    numbered_counter += 1
                    md_lines.append(f"{indent}{numbered_counter}. {clean_text}")
                else:
                    md_lines.append(f"{indent}- {clean_text}")
                continue

            # Regular paragraph
            numbered_counter = 0
            md_lines.append(text)

        elif tag == "tbl":
            # Find matching table object
            tbl = None
            for t in doc.tables:
                if t._element is child:
                    tbl = t
                    break
            if tbl is not None:
                md_lines.append("")
                md_lines.append(table_to_markdown(tbl))
                md_lines.append("")

    # Clean up excessive blank lines
    result = "\n".join(md_lines)
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip() + "\n"


def convert_file(input_path: Path, output_path: Path | None = None) -> Path:
    """Convert a single .docx to .md. Returns the output path."""
    if output_path is None:
        output_path = input_path.with_suffix(".md")

    md_content = convert_docx_to_markdown(input_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(md_content, encoding="utf-8")
    logger.info(f"Output: {output_path}")
    return output_path


def convert_directory(input_dir: Path, output_dir: Path | None = None) -> list[Path]:
    """Convert all .docx files in a directory. Returns list of output paths."""
    if output_dir is None:
        output_dir = input_dir

    docx_files = sorted(input_dir.glob("*.docx"))
    if not docx_files:
        logger.warning(f"No .docx files found in {input_dir}")
        return []

    logger.info(f"Found {len(docx_files)} .docx files in {input_dir}")
    outputs = []
    for docx_file in docx_files:
        out_path = output_dir / docx_file.with_suffix(".md").name
        outputs.append(convert_file(docx_file, out_path))

    logger.info(f"Converted {len(outputs)} files")
    return outputs


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    if input_path.is_file():
        if not input_path.suffix.lower() == ".docx":
            logger.error(f"Not a .docx file: {input_path}")
            sys.exit(1)
        convert_file(input_path, output_path)
    elif input_path.is_dir():
        convert_directory(input_path, output_path)
    else:
        logger.error(f"Path does not exist: {input_path}")
        sys.exit(1)


if __name__ == "__main__":
    main()
