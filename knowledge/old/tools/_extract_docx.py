"""Parse 20260424 DOCX into structured PEOPLE / BIZ-PROJECT / UPDATE blocks."""
from docx import Document
import re, json

DOCX_PATH = r"C:\Users\133486\OneDrive - Royal Caribbean Group\LocalDatabricks\rcg_ds_reporting\knowledge\reporting\weekly_updates_raw\20260424 - Weekly Matt and Rafeh Update (Raw).docx"
OUTPUT_PATH = r"C:\Users\133486\OneDrive - Royal Caribbean Group\LocalDatabricks\rcg_ds_reporting\knowledge\reporting\20260424 - Weekly Matt and Rafeh Update (Raw).md"

# --- Name resolution roster ---
ROSTER = {
    "aagam": "Aagam Shah",
    "arya": "Arya Cheeti",
    "ayon": "Ayon Ghosh",
    "bao": "Bao Le",
    "ben": "Benjamin Fowler",
    "benjamin": "Benjamin Fowler",
    "caleb": "Caleb Sharkey",
    "camila": "Camila Aichele",
    "carlos": "Carlos Gonzalez Andarcio",
    "cihan": "Cihan Ulus",
    "cristian": "Cristian Villamarin-Villamil",
    "danusio": "Danusio Guimares",
    "david m": "David Martinez",
    "david w": "David Whitney",
    "douglas": "Douglas Bedell",
    "edward": "Edward Baffa",
    "erick": "Erick Alfaro",
    "evan": "Evan McFall",
    "eswar": "Thokala Eswar",
    "glen-erik": "Glen-Erik Cortez",
    "gourish": "Gourish Pisal",
    "ignacio": "Ignacio Villasmil",
    "javier": "Nelson Javier Buitrago-Aza",
    "jesse": "Jesse Bausell",
    "kartik": "Kartik Ullal",
    "kevin": "Kevin Diaz",
    "lamis": "Lamis Amer",
    "luis": "Luis Vargas",
    "mahshad": "Mahshad Shariatnasab",
    "mehdi": "Mehdi Assefi",
    "mert": "Mert Ersoz",
    "michelle": "Michelle Manfrini",
    "mirielle": "Mireille Pascaline Feudjio Tsague",
    "mireille": "Mireille Pascaline Feudjio Tsague",
    "osvaldo": "Osvaldo Velazquez",
    "parimala": "Parimala Kettymuthu",
    "reza": "Reza Bahadori",
    "rodrigo": "Rodrigo Briguido",
    "srilekha": "Srilekha Reddy Madupu",
    "william": "William Borges",
    "santiago": "Santiago [?]",
    "doug": "Douglas Bedell",
    "douglas": "Douglas Bedell",
    "neila": "Neila [?]",
    "lekha": "Srilekha Reddy Madupu",
    "anand": "Anand [?]",
    "nicolas": "Nicolas [?]",
}

# Last-initial disambiguation for ambiguous first names
LAST_INITIAL_MAP = {
    ("carlos", "a"): "Carlos Gonzalez Andarcio",
    ("carlos", "g"): "Carlos Gonzalez Andarcio",
    ("david", "m"): "David Martinez",
    ("david", "w"): "David Whitney",
    ("erick", "a"): "Erick Alfaro",
    ("erick", "g"): "Erick Alfaro",  # likely typo - flag
    ("danusio", "g"): "Danusio Guimares",
    ("rodrigo", "b"): "Rodrigo Briguido",
    ("glen-erik", "c"): "Glen-Erik Cortez",
    ("kevin", "d"): "Kevin Diaz",
    ("mirielle", "t"): "Mireille Pascaline Feudjio Tsague",
    ("osvaldo", "v"): "Osvaldo Velazquez",
    ("cristian", "v"): "Cristian Villamarin-Villamil",
    ("evan", "m"): "Evan McFall",
    ("ayon", "g"): "Ayon Ghosh",
}


def resolve_name(raw: str) -> str:
    """Resolve a raw name token to a full roster name."""
    raw = raw.strip().rstrip(".")
    if not raw:
        return None

    # Try last-initial disambiguation first
    parts = raw.split()
    if len(parts) >= 2:
        first = parts[0].lower()
        last_init = parts[-1].rstrip(".").lower()
        if len(last_init) == 1:
            key = (first, last_init)
            if key in LAST_INITIAL_MAP:
                return LAST_INITIAL_MAP[key]

    # Try direct first-name lookup
    first_lower = parts[0].lower() if parts else raw.lower()
    # Handle hyphenated names like Glen-Erik
    if "-" in raw and len(parts) >= 1:
        first_lower = parts[0].lower()
    if first_lower in ROSTER:
        return ROSTER[first_lower]

    # Return raw if unresolved
    return f"{raw} [?]"


def split_name_line(line: str) -> list:
    """Split a people line like 'Ben & Camila' or 'Erick A., Danusio G., Rodrigo B' into individual names."""
    # Remove bold markers
    line = line.replace("**", "").replace("*", "").strip()
    # Split on ' & ', ' and '
    parts = re.split(r'\s+&\s+|\s+and\s+', line)
    # Further split on ', ' within each part
    names = []
    for part in parts:
        sub = [s.strip() for s in part.split(",") if s.strip()]
        names.extend(sub)
    return names


def extract_blocks(docx_path: str) -> list:
    """Extract paragraph blocks from DOCX, split on empty lines.
    Also splits paragraphs that contain embedded newlines (soft returns).
    """
    doc = Document(docx_path)
    # Flatten: split each paragraph on embedded \n to get true lines
    lines = []
    for p in doc.paragraphs:
        for sub in p.text.split("\n"):
            lines.append(sub)

    blocks = []
    current = []
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
    """Heuristic: does this line look like a person name header (vs. project/date/content)?"""
    clean = line.replace("**", "").replace("*", "").strip()
    # Reject lines starting with known non-person patterns
    if re.match(r'^(Project:|[\[\(]|DOE-|\d{4}[-/]|Apr |May |Jun |Jul |Aug |Sep |Oct |Nov |Dec |Jan |Feb |Mar |1:1 |http)', clean):
        return False
    # Reject lines that are too long to be a name header (>80 chars)
    if len(clean) > 80:
        return False
    # Reject lines starting with numbers (like "1. something")
    if re.match(r'^\d+\.?\s', clean):
        return False
    # Accept if it contains a known first name
    name_tokens = re.split(r'[,&]+|\band\b', clean.lower())
    for token in name_tokens:
        first = token.strip().split()[0] if token.strip().split() else ""
        if first in ROSTER:
            return True
    # Accept if it looks like "FirstName" or "FirstName L." (short, 1-3 words)
    words = clean.split()
    if 1 <= len(words) <= 5 and words[0][0].isupper():
        # Check if all words look name-like (capitalized, short)
        if all(len(w) < 20 for w in words):
            return True
    return False


def merge_orphan_blocks(blocks: list) -> list:
    """Merge blocks whose first line is not a person name into the previous block."""
    if not blocks:
        return blocks
    merged = [blocks[0]]
    for block in blocks[1:]:
        if not is_person_line(block[0]):
            # Merge into the previous block
            merged[-1].extend([""] + block)
        else:
            merged.append(block)
    return merged


def parse_block(block: list) -> dict:
    """Parse a block into PEOPLE, BIZ/PROJECT, UPDATE."""
    if len(block) < 2:
        return None  # skip degenerate blocks

    # Line 0: People
    raw_names = split_name_line(block[0])
    resolved = [resolve_name(n) for n in raw_names]
    resolved = [r for r in resolved if r]

    # Line 1 (and maybe 2): BIZ/PROJECT
    biz_line = block[1]
    content_start = 2

    # Check if the biz line has content after a colon (e.g., "RCI Revenue Management - Track Optimization:\nBoth projects...")
    # If the text after the colon is long (>30 chars), it's likely content, not a project qualifier
    if ":" in biz_line:
        colon_idx = biz_line.index(":")
        before_colon = biz_line[:colon_idx].strip()
        after_colon = biz_line[colon_idx + 1:].strip()
        # If there's a newline in the biz line, split it
        if "\n" in biz_line:
            first_line = biz_line.split("\n")[0].rstrip(":")
            rest = "\n".join(biz_line.split("\n")[1:])
            biz_project = first_line
            # Prepend the rest to the update content
            update_lines = [rest] + block[content_start:]
            update_text = "\n".join(update_lines)
            return {
                "people": resolved,
                "biz_project": biz_project,
                "update": update_text,
            }
        elif len(after_colon) > 50:
            # Long content after colon - it's likely the update content leaked into biz
            biz_project = before_colon
            update_lines = [after_colon] + block[content_start:]
            update_text = "\n".join(update_lines)
            return {
                "people": resolved,
                "biz_project": biz_project,
                "update": update_text,
            }

    biz_project = biz_line.rstrip(":")

    # If line 1 looks like it's part of a multi-line biz header
    # (ends with colon and line 2 is a short label, not a sentence)
    if len(block) > 2:
        line2 = block[2]
        if block[1].rstrip().endswith(":") and len(line2) < 60 and not line2[0].isdigit():
            # Only merge if line2 looks label-like (few words, no period at end, short)
            words_in_line2 = len(line2.split())
            if words_in_line2 <= 5 and not line2.rstrip().endswith("."):
                biz_project = block[1].rstrip(":") + " / " + line2
                content_start = 3

    # Rest: UPDATE
    update_lines = block[content_start:]
    update_text = "\n".join(update_lines)

    return {
        "people": resolved,
        "biz_project": biz_project,
        "update": update_text,
    }


def write_markdown(blocks: list, output_path: str):
    """Write structured blocks to markdown file."""
    lines = ["# 20260424 - Weekly Matt and Rafeh Update (Raw)", ""]

    for i, block_data in enumerate(blocks, 1):
        if block_data is None:
            continue
        people_str = ", ".join(block_data["people"])
        lines.append(f"## Update {i}")
        lines.append("")
        lines.append(f"**PEOPLE:** {people_str}")
        lines.append(f"**BIZ/PROJECT:** {block_data['biz_project']}")
        lines.append(f"**UPDATE:**")
        lines.append(block_data["update"])
        lines.append("")
        lines.append("---")
        lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Wrote {len([b for b in blocks if b])} updates to {output_path}")


# --- Main ---
blocks = extract_blocks(DOCX_PATH)
print(f"Found {len(blocks)} raw blocks (before merge)")

blocks = merge_orphan_blocks(blocks)
print(f"Found {len(blocks)} blocks (after merging orphans)")

parsed = [parse_block(b) for b in blocks]

# Debug: print summary
for i, p in enumerate(parsed, 1):
    if p:
        print(f"  Block {i}: PEOPLE={p['people']}  BIZ={p['biz_project'][:50]}")
    else:
        print(f"  Block {i}: SKIPPED (too short)")

write_markdown(parsed, OUTPUT_PATH)
