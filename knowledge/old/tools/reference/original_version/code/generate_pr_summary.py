"""
generate_pr_summary.py
Reads the CHANGELOG.md and validation report to produce a human-readable
PR description for the knowledge base update.

Usage:
    python generate_pr_summary.py <changelog.md> <validation_report.md> <output_pr_summary.md>

The output is ready to paste into a GitHub/Azure DevOps PR description.
"""

import sys
import logging
import re
from pathlib import Path
from datetime import datetime

LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / f"pr_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def extract_summary_stats(changelog_text: str) -> dict:
    """Extract summary stats from the changelog."""
    stats = {}
    for line in changelog_text.splitlines():
        match = re.match(r"- \*\*(.+?):\*\*\s*(\d+)", line)
        if match:
            stats[match.group(1).lower()] = int(match.group(2))
    return stats


def extract_validation_status(validation_text: str) -> dict:
    """Extract validation pass/fail and counts."""
    result = {"errors": 0, "warnings": 0, "files_checked": 0}
    for line in validation_text.splitlines():
        if "Errors:" in line:
            match = re.search(r"Errors:\s*(\d+)", line)
            if match:
                result["errors"] = int(match.group(1))
        elif "Warnings:" in line:
            match = re.search(r"Warnings:\s*(\d+)", line)
            if match:
                result["warnings"] = int(match.group(1))
        elif "Files checked:" in line:
            match = re.search(r"Files checked:\s*(\d+)", line)
            if match:
                result["files_checked"] = int(match.group(1))
    return result


def generate_pr_body(changelog_path: Path, validation_path: Path | None) -> str:
    """Generate the PR description markdown."""
    changelog = changelog_path.read_text(encoding="utf-8")
    stats = extract_summary_stats(changelog)

    validation = None
    if validation_path and validation_path.exists():
        val_text = validation_path.read_text(encoding="utf-8")
        validation = extract_validation_status(val_text)

    # Extract report date from changelog title
    date_match = re.search(r"Changelog — (\S+)", changelog)
    report_date = date_match.group(1) if date_match else datetime.now().strftime("%Y-%m-%d")

    lines = [
        f"## Knowledge Base Update — {report_date}",
        "",
        "### Summary",
        "",
        f"Weekly report ingested and propagated to knowledge base entities.",
        "",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| People updated | {stats.get('people updated', 0)} |",
        f"| Areas updated | {stats.get('areas updated', 0)} |",
        f"| Projects referenced | {stats.get('projects referenced', 0)} |",
        "",
    ]

    # Validation status
    if validation:
        status = "PASSED" if validation["errors"] == 0 else "FAILED"
        emoji = "white_check_mark" if validation["errors"] == 0 else "x"
        lines.extend([
            f"### Validation: {status}",
            "",
            f"- Files checked: {validation['files_checked']}",
            f"- Errors: {validation['errors']}",
            f"- Warnings: {validation['warnings']}",
            "",
        ])
    else:
        lines.extend([
            "### Validation: Not Run",
            "",
        ])

    # Pipeline steps
    lines.extend([
        "### Pipeline Steps",
        "",
        "1. Raw `.docx` converted to `.md` (batch_convert.py)",
        "2. Weekly report parsed and tagged by person/area/project (parse_weekly_report.py)",
        "3. Duplicate content removed vs. prior week (deduplicate_updates.py)",
        "4. Entity files updated with tracking entries (manual review of prompt outputs)",
        "5. Changelog generated (generate_changelog.py)",
        "6. Knowledge base validated (validate_knowledge_base.py)",
        "",
        "### Review Checklist",
        "",
        "- [ ] Changelog entries are accurate — weekly report items map to correct people/areas",
        "- [ ] No unintended overwrites of existing entity content",
        "- [ ] New wikilinks resolve to existing files",
        "- [ ] Frontmatter `last_updated` dates are correct",
        "- [ ] No PII or sensitive content in tracking entries",
        "",
        "<details>",
        "<summary>Full Changelog</summary>",
        "",
        changelog,
        "",
        "</details>",
    ])

    return "\n".join(lines)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    changelog_path = Path(sys.argv[1])
    validation_path = Path(sys.argv[2]) if len(sys.argv) >= 3 else None
    output_path = Path(sys.argv[3]) if len(sys.argv) >= 4 else Path("pr_summary.md")

    if not changelog_path.exists():
        logger.error(f"Changelog not found: {changelog_path}")
        sys.exit(1)

    pr_body = generate_pr_body(changelog_path, validation_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(pr_body, encoding="utf-8")
    logger.info(f"PR summary written to {output_path}")
    print(pr_body)


if __name__ == "__main__":
    main()
