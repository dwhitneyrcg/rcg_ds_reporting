"""
generate_changelog.py
Produces a CHANGELOG.md summarizing every entity change made during
this pipeline run. Used by the PR summary and for audit.

Usage:
    python generate_changelog.py <tagged_report.md> <output_changelog.md>

Reads the tagged report, compares against current entity state,
and lists all pending changes grouped by entity type.
"""

import re
import sys
import logging
import yaml
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[2]  # knowledge/
LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / f"changelog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def read_frontmatter(filepath: Path) -> dict:
    """Read YAML frontmatter from a markdown file."""
    text = filepath.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                return yaml.safe_load(parts[1]) or {}
            except yaml.YAMLError:
                return {}
    return {}


def parse_tagged_report(filepath: Path) -> dict:
    """Parse tagged report into structured sections."""
    text = filepath.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    body = parts[2] if len(parts) >= 3 else text
    frontmatter = {}
    if len(parts) >= 3:
        try:
            frontmatter = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError:
            pass

    result = {
        "report_date": frontmatter.get("report_date", "unknown"),
        "areas": {},
    }

    current_area = None
    current_person = None

    for line in body.splitlines():
        area_match = re.match(r"^##\s+(.+)", line)
        person_match = re.match(r"^###\s+(.+)", line)
        if area_match:
            current_area = area_match.group(1).strip()
            result["areas"].setdefault(current_area, {"people": {}})
        elif person_match and current_area:
            current_person = person_match.group(1).strip()
            result["areas"][current_area]["people"].setdefault(current_person, [])
        elif current_area and current_person:
            stripped = line.strip()
            if re.match(r"^[-•*]\s+", stripped):
                content = re.sub(r"^[-•*]\s+", "", stripped).strip()
                if content:
                    result["areas"][current_area]["people"][current_person].append(content)

    return result


def find_entity_file(entity_type: str, name: str) -> Path | None:
    """Locate the overview file for a person, project, or area."""
    slug = name.lower().replace(" ", "_").replace("-", "_")
    if entity_type == "person":
        pattern = ROOT / "people" / slug / f"overview_{slug}.md"
        if pattern.exists():
            return pattern
        # Try partial match
        people_dir = ROOT / "people"
        if people_dir.exists():
            for d in people_dir.iterdir():
                if d.is_dir() and slug in d.name:
                    overview = d / f"overview_{d.name}.md"
                    if overview.exists():
                        return overview
    elif entity_type == "area":
        areas_dir = ROOT / "biz_areas"
        if areas_dir.exists():
            for d in areas_dir.iterdir():
                if d.is_dir() and slug in d.name:
                    overview = d / f"overview_{d.name}.md"
                    if overview.exists():
                        return overview
    return None


def generate_changelog(tagged_path: Path) -> str:
    """Generate a changelog markdown string."""
    report = parse_tagged_report(tagged_path)
    report_date = report["report_date"]

    lines = [
        f"# Changelog — {report_date}",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"Source: `{tagged_path.name}`",
        "",
    ]

    # Track changes by entity type
    person_changes = []
    area_changes = []
    project_mentions = set()

    for area_name, area_data in report["areas"].items():
        area_changes.append(area_name)
        for person_name, items in area_data["people"].items():
            if items:
                person_changes.append({
                    "name": person_name,
                    "area": area_name,
                    "items": items,
                    "file_exists": find_entity_file("person", person_name) is not None,
                })
                # Extract project mentions from wikilinks in items
                for item in items:
                    wikilinks = re.findall(r"\[\[([^\]|]+)", item)
                    project_mentions.update(wikilinks)

    # Person changes
    lines.append("## Person Entity Updates")
    lines.append("")
    if person_changes:
        lines.append(f"| Person | Area | Items | File Exists |")
        lines.append(f"|--------|------|-------|-------------|")
        for pc in sorted(person_changes, key=lambda x: x["name"]):
            count = len(pc["items"])
            exists = "Yes" if pc["file_exists"] else "**No**"
            lines.append(f"| {pc['name']} | {pc['area']} | {count} | {exists} |")
        lines.append("")
        lines.append("### Details")
        lines.append("")
        for pc in sorted(person_changes, key=lambda x: x["name"]):
            lines.append(f"#### {pc['name']} ({pc['area']})")
            lines.append(f"Action: Append tracking row for {report_date}")
            for item in pc["items"]:
                lines.append(f"- {item}")
            lines.append("")
    else:
        lines.append("_No person updates this week._")
        lines.append("")

    # Area changes
    lines.append("## Business Area Updates")
    lines.append("")
    if area_changes:
        for area in sorted(area_changes):
            area_file = find_entity_file("area", area)
            status = "exists" if area_file else "**not found**"
            lines.append(f"- **{area}** — file {status}")
            lines.append(f"  - Action: Update Current Status narrative, append tracking row")
        lines.append("")
    else:
        lines.append("_No area updates this week._")
        lines.append("")

    # Project mentions
    lines.append("## Project References")
    lines.append("")
    if project_mentions:
        for proj in sorted(project_mentions):
            lines.append(f"- `{proj}`")
        lines.append("")
    else:
        lines.append("_No project wikilinks found in tagged report._")
        lines.append("")

    # Summary stats
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **People updated:** {len(person_changes)}")
    lines.append(f"- **Areas updated:** {len(area_changes)}")
    lines.append(f"- **Projects referenced:** {len(project_mentions)}")
    lines.append("")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    tagged_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not tagged_path.exists():
        logger.error(f"Tagged report not found: {tagged_path}")
        sys.exit(1)

    changelog = generate_changelog(tagged_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(changelog, encoding="utf-8")
    logger.info(f"Changelog written to {output_path}")


if __name__ == "__main__":
    main()
