"""
parse_weekly_report.py
Parses a raw weekly .md report into structured JSON blocks per person/business area.

Reads entity data from master markdown files at runtime — nothing hardcoded.
Outputs a tagged .md file with YAML frontmatter listing all entities referenced.

Usage:
    python parse_weekly_report.py <raw_report.md> <output_tagged.md>
    python parse_weekly_report.py <raw_report.md>  (outputs to stdout as JSON)

Requires: pyyaml (pip install pyyaml)
"""

import json
import re
import sys
import logging
from pathlib import Path
from datetime import datetime

LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / f"parse_weekly_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

KNOWLEDGE_ROOT = Path(__file__).resolve().parent.parent.parent


# ---------------------------------------------------------------------------
# 1. Load master data from markdown support files
# ---------------------------------------------------------------------------

def load_team_roster(roster_path: Path) -> dict:
    """Parse master_team_roster.md → dict mapping lowercase first names, full names,
    and slug variants to canonical entries {name, slug, status}."""
    text = roster_path.read_text(encoding="utf-8")
    roster = {}
    status = "active"
    for line in text.splitlines():
        if "## Inactive" in line:
            status = "inactive"
        # Match wikilink pattern: [[slug/overview_slug|Display Name]]
        m = re.search(r"\[\[([^|]+)\|([^\]]+)\]\]", line)
        if m:
            slug = m.group(1).split("/")[0]
            display_name = m.group(2).strip()
            entry = {"name": display_name, "slug": slug, "status": status}
            # Index by multiple keys for fuzzy matching
            roster[display_name.lower()] = entry
            first = display_name.split()[0].lower()
            roster[first] = entry
            # Also index by slug
            roster[slug.replace("_", " ")] = entry
    logger.info(f"Loaded {len(roster)} roster entries from {roster_path.name}")
    return roster


def load_business_areas(areas_path: Path) -> list[dict]:
    """Parse business_areas_master.md → list of {name, slug, folder}."""
    text = areas_path.read_text(encoding="utf-8")
    areas = []
    for line in text.splitlines():
        m = re.search(r"\[\[([^|]+)\|([^\]]+)\]\]", line)
        if m:
            link_path = m.group(1)
            display_name = m.group(2).strip()
            folder = link_path.split("/")[0]
            areas.append({"name": display_name, "slug": folder, "folder": folder})
    logger.info(f"Loaded {len(areas)} business areas from {areas_path.name}")
    return areas


def load_active_projects(projects_path: Path) -> list[dict]:
    """Parse business_active_projects_master.md → list of {name, slug, area}."""
    text = projects_path.read_text(encoding="utf-8")
    projects = []
    current_area = None
    for line in text.splitlines():
        # Area headers are typically ## or bold text
        area_match = re.match(r"^#{1,3}\s+(.+)", line)
        if area_match:
            current_area = area_match.group(1).strip()
            continue
        # Bold area headers
        bold_match = re.match(r"^\*\*(.+?)\*\*", line)
        if bold_match and not re.search(r"\[\[", line):
            current_area = bold_match.group(1).strip()
            continue
        m = re.search(r"\[\[([^|]+)\|([^\]]+)\]\]", line)
        if m:
            link_path = m.group(1)
            display_name = m.group(2).strip()
            projects.append({
                "name": display_name,
                "slug": link_path.split("/")[-1] if "/" in link_path else link_path,
                "area": current_area,
            })
    logger.info(f"Loaded {len(projects)} active projects from {projects_path.name}")
    return projects


def build_area_aliases(areas: list[dict]) -> dict:
    """Build a lookup mapping common aliases/abbreviations to canonical area names."""
    alias_map = {}
    for area in areas:
        name = area["name"]
        alias_map[name.lower()] = name
        # Generate common abbreviations
        # e.g., "Marine Insights Analytics Platform (Marine Operations)" → "miap", "marine"
        # e.g., "Contact Center Optimization & Automation (RCI/CEL)" → "contact center"
        words = name.lower()
        alias_map[words] = name
        # Parenthetical content
        paren = re.search(r"\((.+?)\)", name)
        if paren:
            alias_map[paren.group(1).lower()] = name
        # Acronyms from capitals
        caps = "".join(c for c in name if c.isupper())
        if len(caps) >= 2:
            alias_map[caps.lower()] = name
        # Key words
        for keyword_map in [
            ("miap", "Marine Insights Analytics Platform (Marine Operations)"),
            ("marine", "Marine Insights Analytics Platform (Marine Operations)"),
            ("contact center", "Contact Center Optimization & Automation (RCI/CEL)"),
            ("ivr", "Contact Center Optimization & Automation (RCI/CEL)"),
            ("workforce planning", "Contact Center Optimization & Automation (RCI/CEL)"),
            ("cresta", "Contact Center Optimization & Automation (RCI/CEL)"),
            ("lead scoring", "Contact Center Optimization & Automation (RCI/CEL)"),
            ("cti", "Contact Center Optimization & Automation (RCI/CEL)"),
            ("bktocx", "Contact Center Optimization & Automation (RCI/CEL)"),
            ("bk2cx", "Contact Center Optimization & Automation (RCI/CEL)"),
            ("wow", "Win-on-Waste (Hotel Operations)"),
            ("win on waste", "Win-on-Waste (Hotel Operations)"),
            ("win-on-waste", "Win-on-Waste (Hotel Operations)"),
            ("fpms", "Win-on-Waste (Hotel Operations)"),
            ("cltv", "Customer Lifetime Value (Corporate Planning)"),
            ("clv", "Customer Lifetime Value (Corporate Planning)"),
            ("customer lifetime", "Customer Lifetime Value (Corporate Planning)"),
            ("propel", "PROPEL Targeted Offers (CEL)"),
            ("targeted offers", "PROPEL Targeted Offers (CEL)"),
            ("axiom", "AXIOM: Generative-AI SEATs (Hotel Ops, Consumer Insights, Legal)"),
            ("seat", "AXIOM: Generative-AI SEATs (Hotel Ops, Consumer Insights, Legal)"),
            ("medallia", "AXIOM: Generative-AI SEATs (Hotel Ops, Consumer Insights, Legal)"),
            ("genai", "AXIOM: Generative-AI SEATs (Hotel Ops, Consumer Insights, Legal)"),
            ("supply chain", "Supply Chain Optimization"),
            ("ibp", "Supply Chain Optimization"),
            ("uniforms", "Supply Chain Optimization"),
            ("hf&b", "Supply Chain Optimization"),
            ("cococay", "Supply Chain Optimization"),
            ("pcp", "PCP Pricing Automation (RCI/CEL)"),
            ("pricing automation", "PCP Pricing Automation (RCI/CEL)"),
            ("shorex", "PCP Pricing Automation (RCI/CEL)"),
            ("beverage package", "PCP Pricing Automation (RCI/CEL)"),
            ("hybris", "Hybris Product Recommendations (Digital)"),
            ("product recommendations", "Hybris Product Recommendations (Digital)"),
            ("recommender", "Hybris Product Recommendations (Digital)"),
            ("mycruise", "Hybris Product Recommendations (Digital)"),
            ("loyalty", "Loyalty Program Redesign"),
            ("royalone", "RoyalOne Community (Digital)"),
            ("app engagement", "RoyalOne Community (Digital)"),
            ("newbuild", "NewBuild"),
            ("new build", "NewBuild"),
            ("pre", "Revenue Management Automation (RCI)"),
            ("spi", "Revenue Management Automation (RCI)"),
            ("gty", "Revenue Management Automation (RCI)"),
            ("dart", "Revenue Management Automation (RCI)"),
            ("elasticity", "Revenue Management Automation (RCI)"),
            ("e-commerce", "Customer Targeting (E-Commerce)"),
            ("uplift model", "Customer Targeting (E-Commerce)"),
            ("booking propensity", "Customer Targeting (E-Commerce)"),
            ("epsilon", "Customer Targeting (E-Commerce)"),
            ("genie", "Customer Targeting (E-Commerce)"),
        ]:
            alias_map[keyword_map[0]] = keyword_map[1]
    return alias_map


# ---------------------------------------------------------------------------
# 2. Parse the raw weekly report into person blocks
# ---------------------------------------------------------------------------

def split_into_person_blocks(text: str, roster: dict) -> list[dict]:
    """Split raw report text into blocks, each attributed to a person."""
    lines = text.splitlines()
    blocks = []
    current_block = None

    # Build a set of known names for detection
    known_names = set()
    for entry in roster.values():
        known_names.add(entry["name"].lower())
        known_names.add(entry["name"].split()[0].lower())

    def is_person_line(line: str) -> str | None:
        """Check if a line is a person header. Returns the matched name or None."""
        stripped = line.strip().rstrip(":")
        stripped = re.sub(r"^\*\*(.+?)\*\*$", r"\1", stripped)  # Remove bold
        stripped = re.sub(r"^#+\s*", "", stripped)  # Remove heading markers
        stripped = stripped.strip()

        if not stripped or len(stripped) > 100:
            return None
        # Skip lines that are clearly bullet points or content
        if stripped.startswith(("-", "•", "*", "1.", "2.", "3.")):
            return None

        # Check if line matches a known person
        lower = stripped.lower()
        # Handle multi-person: "Ben & Camila", "Glen-Erik & Alejandro"
        for part in re.split(r"\s*[&,]\s*", lower):
            part = part.strip().rstrip(":").rstrip(".")
            # Remove parenthetical context
            part = re.sub(r"\s*\(.*?\)\s*", "", part).strip()
            if part in known_names:
                return stripped

        # Check if it looks like a name (2-4 capitalized words, no bullets)
        words = stripped.split()
        if 1 <= len(words) <= 5:
            # Check first word is capitalized and not a common non-name word
            non_names = {"completed", "delivered", "in", "working", "update", "status",
                         "next", "key", "this", "the", "a", "and", "or", "rci", "cel",
                         "ssc", "miap", "week", "project", "overview"}
            if words[0].lower() not in non_names and words[0][0].isupper():
                # Check against roster more carefully
                for part in re.split(r"\s*[&,]\s*", stripped.lower()):
                    part = re.sub(r"\s*\(.*?\)\s*", "", part).strip()
                    if part in known_names:
                        return stripped
        return None

    for line in lines:
        person = is_person_line(line)
        if person is not None:
            if current_block:
                blocks.append(current_block)
            current_block = {"person_raw": person, "lines": []}
        elif current_block is not None:
            current_block["lines"].append(line)
        # Skip lines before first person block

    if current_block:
        blocks.append(current_block)

    logger.info(f"Split report into {len(blocks)} person blocks")
    return blocks


# ---------------------------------------------------------------------------
# 3. Classify and structure each block
# ---------------------------------------------------------------------------

def resolve_person(person_raw: str, roster: dict) -> list[dict]:
    """Resolve a raw person string to canonical roster entries."""
    resolved = []
    # Split multi-person: "Ben & Camila", "Glen-Erik & Javier"
    parts = re.split(r"\s*[&,]\s*", person_raw)
    for part in parts:
        part = part.strip().rstrip(":").rstrip(".")
        part = re.sub(r"\s*\(.*?\)\s*", "", part).strip()
        lower = part.lower()
        if lower in roster:
            resolved.append(roster[lower])
        else:
            # Try first word
            first = lower.split()[0] if lower.split() else lower
            if first in roster:
                resolved.append(roster[first])
            else:
                resolved.append({"name": part, "slug": part.lower().replace(" ", "_"), "status": "unknown"})
                logger.warning(f"Could not resolve person: '{part}'")
    return resolved


def classify_business_area(text: str, area_aliases: dict) -> str:
    """Determine the business area from block text using alias matching."""
    text_lower = text.lower()

    # Strategy 1: Check first few lines for explicit area headers
    first_lines = text_lower.split("\n")[:5]
    header_text = " ".join(first_lines)

    # Look for brand prefixes: "RCI |", "CEL |", "SSC |"
    brand_match = re.search(r"\b(rci|cel|ssc)\s*[\|:]", header_text)

    # Check for area keywords in header — longest match first
    sorted_aliases = sorted(area_aliases.keys(), key=len, reverse=True)
    for alias in sorted_aliases:
        if alias in header_text:
            return area_aliases[alias]

    # Strategy 2: Check full text for area keywords
    for alias in sorted_aliases:
        if len(alias) >= 3 and alias in text_lower:
            return area_aliases[alias]

    # Strategy 3: Brand-based inference
    if brand_match:
        brand = brand_match.group(1).upper()
        if brand == "SSC":
            return "Revenue Management Automation (SSC)"
        elif brand == "CEL":
            return "Revenue Management Automation (CEL)"
        elif brand == "RCI":
            return "Revenue Management Automation (RCI)"

    return "Unclassified"


def match_projects(text: str, projects: list[dict], area: str) -> list[str]:
    """Find which active projects are referenced in the text."""
    matched = []
    text_lower = text.lower()
    for proj in projects:
        proj_name_lower = proj["name"].lower()
        # Check exact name match or key words from project name
        words = [w for w in proj_name_lower.split() if len(w) > 3]
        if proj_name_lower in text_lower:
            matched.append(proj["name"])
        elif len(words) >= 2 and all(w in text_lower for w in words[:3]):
            matched.append(proj["name"])
    return list(set(matched))


def classify_status(lines: list[str]) -> dict:
    """Split lines into completed, in_progress, and next_steps."""
    result = {"completed": [], "in_progress": [], "next_steps": [], "raw": []}
    current_section = "raw"

    for line in lines:
        stripped = line.strip().lower()
        # Detect section headers
        if re.match(r"^(completed|delivered|done|accomplishments?)\s*:?\s*$", stripped):
            current_section = "completed"
            continue
        elif re.match(r"^(in\s*progress|working\s*on|ongoing|current)\s*:?\s*$", stripped):
            current_section = "in_progress"
            continue
        elif re.match(r"^(next\s*(steps?|week)|upcoming|planned|pending)\s*:?\s*$", stripped):
            current_section = "next_steps"
            continue
        elif re.match(r"^(key\s*dates?)\s*:?\s*$", stripped):
            current_section = "next_steps"
            continue

        # Heuristic: past tense verbs → completed, future/present → in_progress
        if current_section == "raw" and line.strip():
            if re.match(r"^\s*[-•*]\s*", line):
                content = re.sub(r"^\s*[-•*]\s*", "", line).strip()
                if re.match(r"(completed|delivered|finished|fixed|resolved|deployed|created|built|added|updated|implemented|achieved)", content.lower()):
                    result["completed"].append(line)
                    continue
                elif re.match(r"(working|will|need|planning|next|ongoing|continue|investigating)", content.lower()):
                    result["in_progress"].append(line)
                    continue

        result[current_section].append(line)

    return result


# ---------------------------------------------------------------------------
# 4. Main parsing pipeline
# ---------------------------------------------------------------------------

def parse_report(report_path: Path, roster: dict, areas: list[dict],
                 projects: list[dict], area_aliases: dict) -> list[dict]:
    """Full pipeline: raw .md → structured tagged blocks."""
    text = report_path.read_text(encoding="utf-8")
    # Remove Python string wrappers if present
    text = re.sub(r'^raw_monthly_text\s*=\s*"""', "", text)
    text = re.sub(r'"""\s*$', "", text)

    blocks = split_into_person_blocks(text, roster)
    parsed = []

    for block in blocks:
        block_text = "\n".join(block["lines"])
        people = resolve_person(block["person_raw"], roster)
        area = classify_business_area(block["person_raw"] + "\n" + block_text, area_aliases)
        matched_projects = match_projects(block_text, projects, area)
        status = classify_status(block["lines"])

        parsed.append({
            "person_raw": block["person_raw"],
            "people": [p["name"] for p in people],
            "people_slugs": [p["slug"] for p in people],
            "business_area": area,
            "projects": matched_projects,
            "completed": [l.strip() for l in status["completed"] if l.strip()],
            "in_progress": [l.strip() for l in status["in_progress"] if l.strip()],
            "next_steps": [l.strip() for l in status["next_steps"] if l.strip()],
            "raw_text": block_text.strip(),
        })

    logger.info(f"Parsed {len(parsed)} blocks from {report_path.name}")
    return parsed


def extract_date_from_filename(filename: str) -> str:
    """Extract YYYYMMDD date from filename like '20260313 - Weekly...'."""
    m = re.match(r"(\d{8})", filename)
    if m:
        d = m.group(1)
        return f"{d[:4]}-{d[4:6]}-{d[6:8]}"
    return datetime.now().strftime("%Y-%m-%d")


def blocks_to_tagged_markdown(blocks: list[dict], report_date: str, source_file: str) -> str:
    """Convert structured blocks to a tagged .md file with YAML frontmatter."""
    # Collect all unique entities
    all_people = sorted(set(p for b in blocks for p in b["people"]))
    all_areas = sorted(set(b["business_area"] for b in blocks if b["business_area"] != "Unclassified"))
    all_projects = sorted(set(p for b in blocks for p in b["projects"]))

    # Build YAML frontmatter
    lines = ["---"]
    lines.append(f"date: {report_date}")
    lines.append(f"source: {source_file}")
    lines.append("tags:")
    lines.append("  - weekly_update")
    for area in all_areas:
        slug = area.lower().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_").replace(":", "").replace("&", "and")
        lines.append(f"  - {slug}")
    lines.append("people:")
    for p in all_people:
        lines.append(f"  - {p}")
    lines.append("business_areas:")
    for a in all_areas:
        lines.append(f'  - "{a}"')
    lines.append("projects:")
    for p in all_projects:
        lines.append(f'  - "{p}"')
    lines.append("---")
    lines.append("")
    lines.append(f"# Weekly Update — {report_date}")
    lines.append("")

    # Group blocks by business area
    by_area = {}
    for block in blocks:
        area = block["business_area"]
        by_area.setdefault(area, []).append(block)

    for area in sorted(by_area.keys()):
        lines.append(f"## {area}")
        lines.append("")
        for block in by_area[area]:
            people_str = ", ".join(block["people"])
            lines.append(f"### {people_str}")
            lines.append("")
            if block["completed"]:
                lines.append("**Completed:**")
                for item in block["completed"]:
                    lines.append(f"- {item}")
                lines.append("")
            if block["in_progress"]:
                lines.append("**In Progress:**")
                for item in block["in_progress"]:
                    lines.append(f"- {item}")
                lines.append("")
            if block["next_steps"]:
                lines.append("**Next Steps:**")
                for item in block["next_steps"]:
                    lines.append(f"- {item}")
                lines.append("")
            if not (block["completed"] or block["in_progress"] or block["next_steps"]):
                # Fall back to raw text
                lines.append(block["raw_text"])
                lines.append("")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    report_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    roster_path = KNOWLEDGE_ROOT / "people" / "master_team_roster.md"
    areas_path = KNOWLEDGE_ROOT / "biz_areas" / "business_areas_master.md"
    projects_path = KNOWLEDGE_ROOT / "biz_areas" / "business_active_projects_master.md"

    roster = load_team_roster(roster_path)
    areas = load_business_areas(areas_path)
    projects = load_active_projects(projects_path)
    area_aliases = build_area_aliases(areas)

    blocks = parse_report(report_path, roster, areas, projects, area_aliases)
    report_date = extract_date_from_filename(report_path.name)

    if output_path:
        md = blocks_to_tagged_markdown(blocks, report_date, report_path.name)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(md, encoding="utf-8")
        logger.info(f"Tagged output written to {output_path}")
    else:
        print(json.dumps(blocks, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
