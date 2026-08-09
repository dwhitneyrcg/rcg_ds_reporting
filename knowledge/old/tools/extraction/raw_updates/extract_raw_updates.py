"""
extract_raw_updates.py
----------------------
Parse a raw weekly update DOCX file into a structured markdown file
with PEOPLE / BIZ-PROJECT / UPDATE blocks.

Usage:
    python extract_raw_updates.py <input.docx>
    python extract_raw_updates.py <input.docx> --output <output.md>
    python extract_raw_updates.py <input.docx> --output-dir <dir>
    python extract_raw_updates.py --batch <directory_of_docx_files>

If --output is omitted, the .md file is written alongside the .docx
with the same base name.

If --batch is used, all .docx files in the directory are processed
and .md files are written to --output-dir (or the same directory).

Requirements:
    pip install python-docx
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from datetime import date
from pathlib import Path

try:
    from docx import Document
except ImportError:
    print("python-docx is required. Install with: pip install python-docx")
    sys.exit(1)

try:
    from rapidfuzz import fuzz, process as rf_process
    _HAS_FUZZY = True
except ImportError:
    _HAS_FUZZY = False

# Import roster data from sibling module
_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR))
from roster import ROSTER, LAST_INITIAL_MAP

# Build the set of unique full names for fuzzy matching.
# Keys are lowered full names, values are canonical display names.
_FULL_NAMES: dict[str, str] = {v.lower(): v for v in ROSTER.values()}
_FUZZY_THRESHOLD = 75  # minimum similarity score to suggest a match


# ─────────────────────────────────────────────────────────
# Name Resolution
# ─────────────────────────────────────────────────────────

def resolve_name(raw: str) -> str | None:
    """Resolve a raw name token (e.g. 'Ben', 'Erick A.') to a full roster name.

    Returns None for empty input, or 'RawName [?]' if unresolved.
    """
    raw = raw.strip().rstrip(".").rstrip(":")
    if not raw:
        return None

    parts = raw.split()

    # Try last-initial disambiguation first  ("David M." → David Martinez)
    if len(parts) >= 2:
        first = parts[0].lower()
        last_init = parts[-1].rstrip(".").lower()
        if len(last_init) == 1:
            key = (first, last_init)
            if key in LAST_INITIAL_MAP:
                return LAST_INITIAL_MAP[key]

    # Direct first-name / nickname lookup
    first_lower = parts[0].lower() if parts else raw.lower()
    if first_lower in ROSTER:
        return ROSTER[first_lower]

    # Fuzzy fallback — suggest closest roster match
    if _HAS_FUZZY and _FULL_NAMES:
        raw_lower = raw.lower()
        result = rf_process.extractOne(
            raw_lower, _FULL_NAMES.keys(), scorer=fuzz.WRatio,
            score_cutoff=_FUZZY_THRESHOLD,
        )
        if result:
            matched_key, score, _ = result
            canonical = _FULL_NAMES[matched_key]
            return f"{raw} [?~{canonical},{int(score)}%]"

    # Fully unresolved — no close match
    return f"{raw} [?]"


def split_name_line(line: str) -> list[str]:
    """Split a people line into individual name tokens.

    Handles patterns like:
        'Ben & Camila'
        'Erick A., Danusio G., Rodrigo B'
        'Kevin D. & Glen-Erik C., Erick G.'
        'Carlos and Bao'
    """
    line = line.replace("**", "").replace("*", "").strip()
    # Strip leading BIZ prefix separated by en-dash/em-dash (e.g. "Loyalty – Carlos:")
    line = re.sub(r"^[A-Za-z\s]+\s*[\u2013\u2014]\s*", "", line)
    # Split on ' & ' or ' and '
    parts = re.split(r"\s+&\s+|\s+and\s+", line)
    names: list[str] = []
    for part in parts:
        sub = [s.strip() for s in part.split(",") if s.strip()]
        names.extend(sub)
    return names


# ─────────────────────────────────────────────────────────
# DOCX → Block Extraction
# ─────────────────────────────────────────────────────────

def extract_blocks(docx_path: str) -> list[list[str]]:
    """Read a DOCX file and return paragraph blocks split on blank lines.

    Soft returns (embedded \\n) within a single paragraph are treated
    as separate lines so that merged name+biz paragraphs are handled.
    """
    doc = Document(docx_path)
    lines: list[str] = []
    for p in doc.paragraphs:
        for sub in p.text.split("\n"):
            lines.append(sub)

    blocks: list[list[str]] = []
    current: list[str] = []
    for text in lines:
        stripped = text.strip()
        if not stripped or stripped == "\xa0":
            if current:
                blocks.append(current)
                current = []
        else:
            current.append(stripped)
    if current:
        blocks.append(current)
    return blocks


def is_person_line(line: str) -> bool:
    """Heuristic: does this line look like a person-name header?

    Returns False for lines that start with known non-person patterns
    (project IDs, dates, URLs, numbered items, long sentences).
    """
    clean = line.replace("**", "").replace("*", "").strip()

    # Reject known non-person prefixes
    if re.match(
        r"^(Project:|[\[\(]|DOE-|\d{4}[-/]"
        r"|Jan |Feb |Mar |Apr |May |Jun |Jul |Aug |Sep |Oct |Nov |Dec "
        r"|1:1 |http)",
        clean,
    ):
        return False

    # Too long for a name line
    if len(clean) > 80:
        return False

    # Starts with a list number
    if re.match(r"^\d+\.?\s", clean):
        return False

    # Contains a known first name → accept
    name_tokens = re.split(r"[,&]+|\band\b", clean.lower())
    for token in name_tokens:
        first = token.strip().split()[0] if token.strip().split() else ""
        if first in ROSTER:
            return True

    # Short, title-cased line (1-5 words, each < 20 chars) → likely a name
    words = clean.split()
    if 1 <= len(words) <= 5 and words[0][0:1].isupper():
        if all(len(w) < 20 for w in words):
            return True

    return False


def merge_orphan_blocks(blocks: list[list[str]]) -> list[list[str]]:
    """Merge blocks whose first line is NOT a person name into the previous block."""
    if not blocks:
        return blocks
    merged = [blocks[0]]
    for block in blocks[1:]:
        if not is_person_line(block[0]):
            merged[-1].extend([""] + block)
        else:
            merged.append(block)
    return merged


# ─────────────────────────────────────────────────────────
# Block → Structured Dict
# ─────────────────────────────────────────────────────────
# Delimiters that reliably separate a BIZ area from a PROJECT name in raw text.
_BIZ_PROJECT_SPLITTERS = re.compile(
    r"\s*/\s*"       # "E-Commerce / Booking Propensity Model"
    r"|\s*\|\s*"     # "CEL Rev Mgmt | Europe Actual Price Paid"
    r"|\s*>\s*"      # rare but possible
)


def split_biz_project(raw: str) -> tuple[str, str]:
    """Attempt to separate a combined BIZ/PROJECT string into (biz, project).

    Heuristic:
      - Split on  /  |  >  delimiters.
      - If the first segment is short (<= 6 words) and looks like an area label,
        treat it as BIZ and the rest as PROJECT.
      - Otherwise return ("", raw) -- the whole thing is labeled PROJECT
        and flagged for manual curation.

    Returns (biz, project).  biz may be empty string.
    """
    raw = raw.strip()
    if not raw:
        return ("", "")

    # Try splitting on known delimiters
    parts = _BIZ_PROJECT_SPLITTERS.split(raw, maxsplit=1)
    if len(parts) == 2:
        candidate_biz = parts[0].strip()
        candidate_proj = parts[1].strip()
        # Accept if the BIZ part is a short label (not a full sentence)
        if len(candidate_biz.split()) <= 6 and candidate_proj:
            return (candidate_biz, candidate_proj)

    # Try splitting on colon only if the part before it is short
    if ":" in raw:
        colon_idx = raw.index(":")
        before = raw[:colon_idx].strip()
        after = raw[colon_idx + 1:].strip()
        if len(before.split()) <= 6 and after and len(after) < 80:
            return (before, after)

    # Cannot split -- default entire string to PROJECT
    return ("", raw)


def format_update_text(raw_text: str) -> str:
    """Format raw update text into readable lines.

    - Each non-empty line becomes a bullet point (if not already one).
    - Blank lines within the block are removed.
    """
    result = []
    for line in raw_text.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        # Already a bullet / numbered item -- keep as-is
        if re.match(r"^[-*]\s|^\d+[.)]\s", stripped):
            result.append(stripped)
        else:
            result.append(f"- {stripped}")
    return "\n".join(result)
def parse_block(block: list[str]) -> dict | None:
    """Parse a raw text block into {people, biz, project, update}.

    Returns None for degenerate blocks (< 2 lines).
    """
    if len(block) < 2:
        return None

    # --- PEOPLE (line 0) ---
    raw_names = split_name_line(block[0])
    resolved = [r for r in (resolve_name(n) for n in raw_names) if r]

    # --- BIZ/PROJECT (line 1, maybe line 2) ---
    biz_line = block[1]
    content_start = 2

    # Handle content leaking after a colon
    if ":" in biz_line:
        colon_idx = biz_line.index(":")
        before = biz_line[:colon_idx].strip()
        after = biz_line[colon_idx + 1 :].strip()

        if "\n" in biz_line:
            first_line = biz_line.split("\n")[0].rstrip(":")
            rest = "\n".join(biz_line.split("\n")[1:])
            biz, project = split_biz_project(first_line)
            return {
                "people": resolved,
                "biz": biz,
                "project": project,
                "update": format_update_text("\n".join([rest] + block[content_start:])),
            }

        if len(after) > 50:
            biz, project = split_biz_project(before)
            return {
                "people": resolved,
                "biz": biz,
                "project": project,
                "update": format_update_text("\n".join([after] + block[content_start:])),
            }

    biz_project = biz_line.rstrip(":")

    # Try merging a short label-like line 2 into the BIZ/PROJECT field
    if len(block) > 2:
        line2 = block[2]
        if (
            block[1].rstrip().endswith(":")
            and len(line2) < 60
            and not line2[0].isdigit()
        ):
            if len(line2.split()) <= 5 and not line2.rstrip().endswith("."):
                biz_project = block[1].rstrip(":") + " / " + line2
                content_start = 3

    # --- Split BIZ from PROJECT ---
    biz, project = split_biz_project(biz_project)

    # --- UPDATE (remaining lines) ---
    update_text = format_update_text("\n".join(block[content_start:]))

    return {"people": resolved, "biz": biz, "project": project, "update": update_text}


# ─────────────────────────────────────────────────────────
# Write Markdown Output
# ─────────────────────────────────────────────────────────

def extract_date_from_filename(filename: str) -> str | None:
    """Try to pull a YYYYMMDD date from the filename and return YYYY-MM-DD."""
    m = re.search(r"(\d{8})", filename)
    if m:
        d = m.group(1)
        return f"{d[:4]}-{d[4:6]}-{d[6:8]}"
    return None


_SEPARATOR = "############################################################################"


def build_markdown(parsed_blocks: list[dict | None], source_filename: str) -> str:
    """Return the full markdown string for the structured output file."""
    stem = Path(source_filename).stem
    date_str = extract_date_from_filename(source_filename) or "Unknown"

    lines = [f"# {stem}", f"**Source date:** {date_str}", ""]

    for block_data in parsed_blocks:
        if block_data is None:
            continue
        people_str = ", ".join(block_data["people"])
        biz = block_data.get("biz", "")
        project = block_data.get("project", "")

        lines.append("")
        lines.append(_SEPARATOR)

        lines.append(f"PEOPLE:    {people_str}")
        if biz:
            lines.append(f"BIZ:       {biz}")
            lines.append(f"PROJECT:   {project}")
        else:
            # Could not identify BIZ area -- label as PROJECT, flag for curation
            lines.append(f"PROJECT:   {project}  [curation needed]")

        lines.append(_SEPARATOR)
        lines.append("")

        # Update content -- each line is already bulleted by format_update_text
        if block_data["update"]:
            lines.append(block_data["update"])

        lines.append("")  # single blank line after content

    lines.append(f"_Source: {source_filename}_")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────
# Review CSV
# ─────────────────────────────────────────────────────────

# Centralized review log -- single CSV across all extractions
_REVIEW_LOG_DIR = Path(__file__).resolve().parents[3] / "reporting" / "weekly_updates_raw_md"
_REVIEW_LOG_PATH = _REVIEW_LOG_DIR / "review_log.csv"

_REVIEW_COLUMNS = [
    "date_logged",
    "source_file",
    "output_file",
    "block_id",
    "people",
    "issue_type",
    "current_value",
    "suggestion",
    "resolution",
    "status",
]

# Known BIZ area labels for fuzzy suggestion (derived from biz_areas/ folder names).
_BIZ_AREAS_DIR = Path(__file__).resolve().parents[3] / "biz_areas"

def _load_biz_labels() -> dict[str, str]:
    """Build {lowered_label: display_label} from biz_areas/ subdirectory names."""
    labels: dict[str, str] = {}
    if _BIZ_AREAS_DIR.is_dir():
        for child in _BIZ_AREAS_DIR.iterdir():
            if child.is_dir():
                # Convert folder name to display label:
                #   "pcp_pricing_automation_(rci_cel)" -> "PCP Pricing Automation (RCI/CEL)"
                raw = child.name.replace("_", " ").replace(",", ", ")
                labels[raw.lower()] = raw
    return labels

_BIZ_LABELS: dict[str, str] = _load_biz_labels()


def _suggest_biz(project_text: str) -> str:
    """Fuzzy-match a project label against known BIZ areas. Return suggestion or ''."""
    if not _HAS_FUZZY or not _BIZ_LABELS:
        return ""
    result = rf_process.extractOne(
        project_text.lower(), _BIZ_LABELS.keys(), scorer=fuzz.WRatio,
        score_cutoff=50,
    )
    if result:
        matched_key, score, _ = result
        return f"{_BIZ_LABELS[matched_key]} ({int(score)}%)"
    return ""


def build_review_rows(
    parsed_blocks: list[dict | None],
    source_filename: str,
    output_filename: str,
) -> list[dict]:
    """Scan parsed blocks for issues and return review-log rows.

    Issue types emitted:
      - biz_missing      : BIZ could not be identified (curation needed)
      - fuzzy_match       : A person name was resolved via fuzzy matching
      - name_unresolved   : A person name could not be resolved at all
    """
    rows: list[dict] = []
    block_id = 0
    today = date.today().isoformat()

    for block_data in parsed_blocks:
        if block_data is None:
            continue
        block_id += 1

        people_str = ", ".join(block_data["people"])
        biz = block_data.get("biz", "")
        project = block_data.get("project", "")

        # --- name issues ---
        for name in block_data["people"]:
            if "[?~" in name:
                m = re.search(r"\[\?~(.+?),(\d+)%\]", name)
                suggestion = m.group(1) if m else ""
                rows.append({
                    "date_logged": today,
                    "source_file": source_filename,
                    "output_file": output_filename,
                    "block_id": block_id,
                    "people": people_str,
                    "issue_type": "fuzzy_match",
                    "current_value": name,
                    "suggestion": suggestion,
                    "resolution": "",
                    "status": "open",
                })
            elif name.endswith("[?]"):
                rows.append({
                    "date_logged": today,
                    "source_file": source_filename,
                    "output_file": output_filename,
                    "block_id": block_id,
                    "people": people_str,
                    "issue_type": "name_unresolved",
                    "current_value": name,
                    "suggestion": "",
                    "resolution": "",
                    "status": "open",
                })

        # --- BIZ missing ---
        if not biz:
            rows.append({
                "date_logged": today,
                "source_file": source_filename,
                "output_file": output_filename,
                "block_id": block_id,
                "people": people_str,
                "issue_type": "biz_missing",
                "current_value": project,
                "suggestion": _suggest_biz(project),
                "resolution": "",
                "status": "open",
            })

    return rows


def write_review_csv(rows: list[dict], csv_path: str | None = None) -> str:
    """Append review rows to the centralized review log CSV.

    Creates the file with headers if it does not exist; appends otherwise.
    Returns the path written.
    """
    csv_path = csv_path or str(_REVIEW_LOG_PATH)
    os.makedirs(os.path.dirname(csv_path) or ".", exist_ok=True)

    file_exists = os.path.exists(csv_path)
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=_REVIEW_COLUMNS)
        if not file_exists:
            writer.writeheader()
        writer.writerows(rows)
    return csv_path


# ─────────────────────────────────────────────────────────
# Public API
# ─────────────────────────────────────────────────────────

def process_docx(docx_path: str, output_path: str | None = None) -> str:
    """End-to-end: DOCX → structured markdown file.

    Args:
        docx_path:   Path to the input .docx file.
        output_path: Path for the output .md file.
                     If None, replaces .docx with .md in the same directory.

    Returns:
        The path of the written markdown file.
    """
    docx_path = str(Path(docx_path).resolve())
    if output_path is None:
        output_path = str(Path(docx_path).with_suffix(".md"))
    output_path = str(Path(output_path).resolve())

    # Extract & merge
    blocks = extract_blocks(docx_path)
    print(f"  [{Path(docx_path).name}] {len(blocks)} raw blocks", end="")
    blocks = merge_orphan_blocks(blocks)
    print(f" → {len(blocks)} after merge")

    # Parse
    parsed = [parse_block(b) for b in blocks]
    valid = [p for p in parsed if p is not None]

    # Write markdown
    md_text = build_markdown(parsed, Path(docx_path).name)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_text)

    # Write review CSV (append to centralized log)
    review_rows = build_review_rows(parsed, Path(docx_path).name, Path(output_path).name)
    review_csv_path = None
    if review_rows:
        review_csv_path = write_review_csv(review_rows)

    # Summary
    all_people = set()
    unresolved = set()
    fuzzy_matches = set()
    needs_curation = 0
    for p in valid:
        for name in p["people"]:
            all_people.add(name)
            if "[?~" in name:
                fuzzy_matches.add(name)
            elif name.endswith("[?]"):
                unresolved.add(name)
        if not p.get("biz"):
            needs_curation += 1

    print(f"  -> {len(valid)} updates | {len(all_people)} people | {needs_curation} need BIZ curation", end="")
    if fuzzy_matches or unresolved:
        total = len(fuzzy_matches) + len(unresolved)
        print(f" | {total} unresolved names:")
        for name in sorted(fuzzy_matches):
            print(f"       {name}  (fuzzy suggestion)")
        for name in sorted(unresolved):
            print(f"       {name}  (no close match -- new person?)")
    else:
        print()
    print(f"  -> Wrote: {output_path}")
    if review_rows:
        print(f"  -> Review log: {review_csv_path} ({len(review_rows)} issues appended)")
    return output_path


# ─────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Extract structured PEOPLE / BIZ-PROJECT / UPDATE blocks from raw weekly DOCX files."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("input", nargs="?", help="Path to a single .docx file.")
    group.add_argument(
        "--batch",
        metavar="DIR",
        help="Process all .docx files in DIR.",
    )
    parser.add_argument(
        "--output", "-o", metavar="PATH", help="Output .md file path (single-file mode only)."
    )
    parser.add_argument(
        "--output-dir",
        metavar="DIR",
        help="Directory for output .md files (batch mode). Defaults to same dir as input.",
    )

    args = parser.parse_args()

    if args.batch:
        src_dir = Path(args.batch).resolve()
        if not src_dir.is_dir():
            print(f"Error: {src_dir} is not a directory.")
            sys.exit(1)
        out_dir = Path(args.output_dir).resolve() if args.output_dir else src_dir
        os.makedirs(out_dir, exist_ok=True)

        docx_files = sorted(src_dir.glob("*.docx"))
        if not docx_files:
            print(f"No .docx files found in {src_dir}")
            sys.exit(0)

        print(f"Processing {len(docx_files)} files from {src_dir}")
        print(f"Output directory: {out_dir}\n")
        for docx_file in docx_files:
            out_file = out_dir / (docx_file.stem + ".md")
            if out_file.exists():
                print(f"  [SKIP] {docx_file.name} → .md already exists")
                continue
            process_docx(str(docx_file), str(out_file))
        print("\nDone.")
    else:
        docx_file = Path(args.input).resolve()
        if not docx_file.exists():
            print(f"Error: {docx_file} not found.")
            sys.exit(1)
        out_path = args.output
        if args.output_dir:
            os.makedirs(args.output_dir, exist_ok=True)
            out_path = str(Path(args.output_dir) / (docx_file.stem + ".md"))
        process_docx(str(docx_file), out_path)


if __name__ == "__main__":
    main()
