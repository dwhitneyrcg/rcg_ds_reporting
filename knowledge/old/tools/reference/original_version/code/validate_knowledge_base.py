"""
validate_knowledge_base.py
Validates the knowledge base for structural integrity:
  - YAML frontmatter presence and required fields
  - Wikilink target resolution (no broken links)
  - Required sections in entity overview files
  - Orphan detection (files not linked from any master list)

Usage:
    python validate_knowledge_base.py [--fix]

Returns exit code 0 if all checks pass, 1 if any fail.
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
LOG_FILE = LOG_DIR / f"validate_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


# Required frontmatter fields by entity type
REQUIRED_FRONTMATTER = {
    "person": ["name", "status", "last_updated"],
    "project": ["project_name", "status", "last_updated"],
    "area": ["area_name", "last_updated"],
}

# Required sections by entity type
REQUIRED_SECTIONS = {
    "person": ["## Weekly Tracking", "## Active Projects"],
    "project": ["## Weekly Tracking", "## Delivery Status"],
    "area": ["## Current Status", "## Active Projects", "## Team Members"],
}


class ValidationResult:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.info: list[str] = []
        self.files_checked = 0

    @property
    def passed(self) -> bool:
        return len(self.errors) == 0

    def error(self, msg: str):
        self.errors.append(msg)
        logger.error(msg)

    def warn(self, msg: str):
        self.warnings.append(msg)
        logger.warning(msg)

    def log_info(self, msg: str):
        self.info.append(msg)
        logger.info(msg)

    def summary(self) -> str:
        lines = [
            "# Validation Report",
            "",
            f"- Files checked: {self.files_checked}",
            f"- Errors: {len(self.errors)}",
            f"- Warnings: {len(self.warnings)}",
            "",
        ]
        if self.errors:
            lines.append("## Errors")
            lines.append("")
            for e in self.errors:
                lines.append(f"- {e}")
            lines.append("")
        if self.warnings:
            lines.append("## Warnings")
            lines.append("")
            for w in self.warnings:
                lines.append(f"- {w}")
            lines.append("")
        return "\n".join(lines)


def read_frontmatter(filepath: Path) -> dict | None:
    """Read YAML frontmatter, return None if missing or invalid."""
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception:
        return None

    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return None


def detect_entity_type(filepath: Path) -> str | None:
    """Detect whether a file is a person, project, or area overview."""
    rel = filepath.relative_to(ROOT)
    parts_list = list(rel.parts)
    if "people" in parts_list and filepath.name.startswith("overview_"):
        return "person"
    if "biz_areas" in parts_list:
        if filepath.name.startswith("overview_") and len(parts_list) >= 3:
            # Check depth: biz_areas/<area>/overview = area, biz_areas/<area>/<project>/overview = project
            idx = parts_list.index("biz_areas")
            depth = len(parts_list) - idx - 1  # depth from biz_areas
            if depth == 2:  # biz_areas/<area>/overview.md
                return "area"
            elif depth >= 3:  # biz_areas/<area>/<project>/overview.md
                return "project"
    return None


def extract_wikilinks(text: str) -> list[str]:
    """Extract all wikilink targets from text."""
    return re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", text)


def resolve_wikilink(target: str) -> Path:
    """Resolve a wikilink target to a filesystem path."""
    # Wikilinks are relative to the knowledge/ root
    clean = target.strip().replace("/", "\\")
    if not clean.endswith(".md"):
        clean += ".md"
    return ROOT / clean


def validate_frontmatter(filepath: Path, entity_type: str, result: ValidationResult):
    """Validate frontmatter presence and required fields."""
    fm = read_frontmatter(filepath)
    rel = filepath.relative_to(ROOT)

    if fm is None:
        result.error(f"{rel}: Missing or invalid YAML frontmatter")
        return

    required = REQUIRED_FRONTMATTER.get(entity_type, [])
    for field in required:
        if field not in fm:
            result.error(f"{rel}: Missing required frontmatter field '{field}'")


def validate_sections(filepath: Path, entity_type: str, result: ValidationResult):
    """Validate required markdown sections exist."""
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception:
        result.error(f"{filepath.relative_to(ROOT)}: Cannot read file")
        return

    required = REQUIRED_SECTIONS.get(entity_type, [])
    for section in required:
        if section not in text:
            result.warn(f"{filepath.relative_to(ROOT)}: Missing section '{section}'")


def validate_wikilinks(filepath: Path, result: ValidationResult):
    """Validate all wikilinks in a file resolve to existing targets."""
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception:
        return

    rel = filepath.relative_to(ROOT)
    links = extract_wikilinks(text)
    for target in links:
        resolved = resolve_wikilink(target)
        if not resolved.exists():
            # Check without .md extension (folder reference)
            folder = ROOT / target.strip()
            if not folder.exists():
                result.warn(f"{rel}: Broken wikilink [[{target}]]")


def find_orphan_overviews(result: ValidationResult):
    """Find overview files not linked from any master list."""
    master_files = [
        ROOT / "people" / "master_team_roster.md",
        ROOT / "biz_areas" / "business_areas_master.md",
        ROOT / "biz_areas" / "business_active_projects_master.md",
    ]

    # Collect all wikilink targets from master files
    all_targets = set()
    for mf in master_files:
        if mf.exists():
            text = mf.read_text(encoding="utf-8")
            for target in extract_wikilinks(text):
                all_targets.add(target.strip().lower())

    # Find all overview files
    for overview in ROOT.rglob("overview_*.md"):
        rel = overview.relative_to(ROOT)
        rel_str = str(rel).replace("\\", "/").replace(".md", "")
        # Check if any master target matches
        found = any(rel_str.lower() in t or t in rel_str.lower() for t in all_targets)
        if not found:
            result.warn(f"Orphan: {rel} — not linked from any master list")


def main():
    result = ValidationResult()
    logger.info(f"Validating knowledge base at {ROOT}")

    # Find all markdown overview files
    overview_files = list(ROOT.rglob("overview_*.md"))
    result.log_info(f"Found {len(overview_files)} overview files")

    for filepath in overview_files:
        result.files_checked += 1
        entity_type = detect_entity_type(filepath)
        if entity_type:
            validate_frontmatter(filepath, entity_type, result)
            validate_sections(filepath, entity_type, result)
        validate_wikilinks(filepath, result)

    # Also validate master files
    for master in ["people/master_team_roster.md",
                    "biz_areas/business_areas_master.md",
                    "biz_areas/business_active_projects_master.md"]:
        mpath = ROOT / master
        if mpath.exists():
            result.files_checked += 1
            validate_wikilinks(mpath, result)
        else:
            result.warn(f"Master file missing: {master}")

    # Check for orphans
    find_orphan_overviews(result)

    # Output report
    report = result.summary()
    print(report)

    report_path = Path(__file__).parent / "logs" / "validation_report.md"
    report_path.write_text(report, encoding="utf-8")
    logger.info(f"Validation report saved to {report_path}")

    if result.passed:
        logger.info("VALIDATION PASSED")
        return 0
    else:
        logger.error(f"VALIDATION FAILED — {len(result.errors)} error(s)")
        return 1


if __name__ == "__main__":
    sys.exit(main())
