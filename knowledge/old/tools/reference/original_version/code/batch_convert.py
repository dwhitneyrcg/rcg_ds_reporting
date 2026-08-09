"""
batch_convert.py
Orchestrates batch conversion of .docx weekly reports to .md files.
Adds idempotency: skips files that already have a corresponding .md output.

Usage:
    python batch_convert.py <input_dir> <output_dir>
    python batch_convert.py  (uses default paths)

Requires: python-docx (pip install python-docx)
"""

import sys
import logging
from pathlib import Path
from datetime import datetime

# Import the converter from the same directory
sys.path.insert(0, str(Path(__file__).parent))
from docx_to_markdown import convert_file

# Logging
LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / f"batch_convert_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

# Default paths relative to knowledge base root
KNOWLEDGE_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_INPUT = KNOWLEDGE_ROOT / "reporting" / "weekly_updates_raw"
DEFAULT_OUTPUT = KNOWLEDGE_ROOT / "reporting" / "weekly_updates_raw_md"


def batch_convert(input_dir: Path, output_dir: Path) -> dict:
    """Convert all .docx files in input_dir to .md in output_dir, skipping existing."""
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    docx_files = sorted(input_dir.glob("*.docx"))
    if not docx_files:
        logger.warning(f"No .docx files found in {input_dir}")
        return {"converted": 0, "skipped": 0, "failed": 0}

    logger.info(f"Found {len(docx_files)} .docx files in {input_dir}")

    stats = {"converted": 0, "skipped": 0, "failed": 0, "files": []}

    for docx_file in docx_files:
        md_name = docx_file.with_suffix(".md").name
        md_path = output_dir / md_name

        # Idempotency: skip if .md already exists and is non-empty
        if md_path.exists() and md_path.stat().st_size > 0:
            logger.info(f"SKIP (exists): {md_name}")
            stats["skipped"] += 1
            continue

        try:
            convert_file(docx_file, md_path)
            stats["converted"] += 1
            stats["files"].append(str(md_path))
            logger.info(f"CONVERTED: {docx_file.name} → {md_name}")
        except Exception as e:
            stats["failed"] += 1
            logger.error(f"FAILED: {docx_file.name} — {e}")

    logger.info(
        f"Batch complete: {stats['converted']} converted, "
        f"{stats['skipped']} skipped, {stats['failed']} failed"
    )
    return stats


def main():
    if len(sys.argv) >= 3:
        input_dir = Path(sys.argv[1])
        output_dir = Path(sys.argv[2])
    else:
        input_dir = DEFAULT_INPUT
        output_dir = DEFAULT_OUTPUT
        logger.info(f"Using default paths: {input_dir} → {output_dir}")

    if not input_dir.exists():
        logger.error(f"Input directory does not exist: {input_dir}")
        sys.exit(1)

    stats = batch_convert(input_dir, output_dir)
    print(f"\nResults: {stats['converted']} converted, {stats['skipped']} skipped, {stats['failed']} failed")


if __name__ == "__main__":
    main()
