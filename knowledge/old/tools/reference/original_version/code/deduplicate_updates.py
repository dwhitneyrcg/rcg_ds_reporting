"""
deduplicate_updates.py
Compares the current week's tagged report against the prior week's tagged report
and flags duplicate content. Outputs a deduplicated version.

Usage:
    python deduplicate_updates.py <current_tagged.md> <prior_tagged.md> <output.md>

Reads YAML frontmatter from both files to compare update blocks.
"""

import re
import sys
import logging
from pathlib import Path
from datetime import datetime
from difflib import SequenceMatcher

LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / f"deduplicate_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

SIMILARITY_THRESHOLD = 0.75  # Lines above this similarity ratio are flagged as duplicates


def extract_bullet_items(text: str) -> list[str]:
    """Extract all bullet-point items from markdown text."""
    items = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.match(r"^[-•*]\s+", stripped):
            content = re.sub(r"^[-•*]\s+", "", stripped).strip()
            if content:
                items.append(content)
    return items


def parse_tagged_sections(filepath: Path) -> dict:
    """Parse a tagged .md file into {area: {person: [items]}}."""
    text = filepath.read_text(encoding="utf-8")
    # Strip YAML frontmatter
    parts = text.split("---", 2)
    body = parts[2] if len(parts) >= 3 else text

    sections = {}
    current_area = None
    current_person = None

    for line in body.splitlines():
        area_match = re.match(r"^##\s+(.+)", line)
        person_match = re.match(r"^###\s+(.+)", line)
        if area_match:
            current_area = area_match.group(1).strip()
            sections.setdefault(current_area, {})
        elif person_match and current_area:
            current_person = person_match.group(1).strip()
            sections[current_area].setdefault(current_person, [])
        elif current_area and current_person:
            stripped = line.strip()
            if re.match(r"^[-•*]\s+", stripped):
                content = re.sub(r"^[-•*]\s+", "", stripped).strip()
                if content:
                    sections[current_area][current_person].append(content)

    return sections


def find_duplicates(current_items: list[str], prior_items: list[str]) -> list[tuple[str, str, float]]:
    """Find items in current that are similar to items in prior."""
    duplicates = []
    for curr in current_items:
        for prev in prior_items:
            ratio = SequenceMatcher(None, curr.lower(), prev.lower()).ratio()
            if ratio >= SIMILARITY_THRESHOLD:
                duplicates.append((curr, prev, ratio))
                break  # One match is enough
    return duplicates


def deduplicate_report(current_path: Path, prior_path: Path) -> tuple[str, list[dict]]:
    """Compare current vs. prior tagged reports. Returns (cleaned text, duplicate log)."""
    current_text = current_path.read_text(encoding="utf-8")
    current_sections = parse_tagged_sections(current_path)
    prior_sections = parse_tagged_sections(prior_path)

    duplicate_log = []
    lines_to_remove = set()

    for area, people in current_sections.items():
        prior_people = prior_sections.get(area, {})
        for person, items in people.items():
            prior_items = prior_people.get(person, [])
            if not prior_items:
                # Check all prior people in this area
                all_prior = [i for items_list in prior_people.values() for i in items_list]
                prior_items = all_prior

            dupes = find_duplicates(items, prior_items)
            for curr_item, prev_item, ratio in dupes:
                duplicate_log.append({
                    "area": area,
                    "person": person,
                    "current": curr_item,
                    "prior_match": prev_item,
                    "similarity": round(ratio, 3),
                })
                lines_to_remove.add(curr_item)

    # Remove duplicates from the text
    output_lines = []
    for line in current_text.splitlines():
        stripped = line.strip()
        content = re.sub(r"^[-•*]\s+", "", stripped).strip()
        if content in lines_to_remove:
            logger.info(f"REMOVED duplicate: {content[:80]}...")
            continue
        output_lines.append(line)

    logger.info(f"Found {len(duplicate_log)} duplicates, removed from output")
    return "\n".join(output_lines), duplicate_log


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)

    current_path = Path(sys.argv[1])
    prior_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])

    if not prior_path.exists():
        logger.warning(f"Prior week file not found: {prior_path}. Skipping dedup.")
        output_path.write_text(current_path.read_text(encoding="utf-8"), encoding="utf-8")
        return

    cleaned_text, dupe_log = deduplicate_report(current_path, prior_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(cleaned_text, encoding="utf-8")
    logger.info(f"Deduplicated output written to {output_path}")

    if dupe_log:
        print(f"\nDuplicates found: {len(dupe_log)}")
        for d in dupe_log:
            print(f"  [{d['area']}] {d['person']}: {d['current'][:60]}... (similarity: {d['similarity']})")


if __name__ == "__main__":
    main()
