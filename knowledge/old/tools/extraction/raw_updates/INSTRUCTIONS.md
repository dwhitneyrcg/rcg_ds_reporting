# Raw Weekly Update Extraction

Extract structured **PEOPLE / BIZ-PROJECT / UPDATE** blocks from raw weekly `.docx` reports.

## Files

| File | Purpose |
|------|---------|
| `extract_raw_updates.py` | Main extraction script (CLI + importable API) |
| `roster.py` | Team roster and nickname/alias mappings |
| `INSTRUCTIONS.md` | This file |

## Prerequisites

```
pip install python-docx
```

## Quick Start

### Single file

```powershell
python extract_raw_updates.py "path/to/20260424 - Weekly Matt and Rafeh Update (Raw).docx"
```

This writes a `.md` file next to the `.docx` with the same name.

### Single file with custom output path

```powershell
python extract_raw_updates.py "path/to/report.docx" --output "path/to/output.md"
```

### Single file with output directory

```powershell
python extract_raw_updates.py "path/to/report.docx" --output-dir "path/to/output_dir"
```

### Batch mode (all .docx files in a directory)

```powershell
python extract_raw_updates.py --batch "path/to/weekly_updates_raw" --output-dir "path/to/reporting"
```

- Processes all `.docx` files in the directory
- Skips files that already have a corresponding `.md` in the output directory
- If `--output-dir` is omitted, `.md` files are written next to the `.docx` files

## Example Commands

Using the project's standard paths:

```powershell
# Single file → knowledge/reporting/
python extract_raw_updates.py ^
  "knowledge/reporting/weekly_updates_raw/20260424 - Weekly Matt and Rafeh Update (Raw).docx" ^
  --output-dir "knowledge/reporting"

# Batch all raw files → knowledge/reporting/
python extract_raw_updates.py ^
  --batch "knowledge/reporting/weekly_updates_raw" ^
  --output-dir "knowledge/reporting"
```

## Output Format

Each `.md` file contains sequentially numbered update blocks:

```markdown
# 20260424 - Weekly Matt and Rafeh Update (Raw)
**Source date:** 2026-04-24

## Update 1

**PEOPLE:** Mireille Pascaline Feudjio Tsague
**BIZ/PROJECT:** Contact Center
**UPDATE:**
Call Volume Forecasting...

---

## Update 2

**PEOPLE:** Carlos Gonzalez Andarcio, Bao Le
**BIZ/PROJECT:** E-Commerce Targeting
**UPDATE:**
Added more features...

---

_Source: 20260424 - Weekly Matt and Rafeh Update (Raw).docx_
```

## How the Parser Works

### 1. Paragraph extraction
The DOCX is read using `python-docx`. Each paragraph's text is split on embedded `\n` characters (Word soft returns / Shift+Enter) so that merged name+project paragraphs become separate lines.

### 2. Block splitting
Lines are grouped into blocks, separated by 1+ consecutive blank lines.

### 3. Orphan block merging
Any block whose first line does NOT look like a person name is merged into the previous block. This handles:
- Jira ticket sub-items that follow a parent block
- Date-prefixed entries (e.g., "Apr 20, 2026 -- ...")
- Continuation sections (e.g., "1:1 Web UI Requirements:")

### 4. Block parsing
Each block is split into three parts:
- **Line 0 → PEOPLE**: Split on ` & `, ` and `, `,` delimiters; each token resolved against the roster
- **Line 1 (+ maybe line 2) → BIZ/PROJECT**: Captured as-is from the document
- **Remaining lines → UPDATE**: Raw content preserved verbatim

### 5. Name resolution
Names are resolved via `roster.py`:
- Direct first-name lookup (e.g., `Ben` → `Benjamin Fowler`)
- Last-initial disambiguation (e.g., `David M.` → `David Martinez`)
- Unresolved names are flagged with `[?]` (e.g., `Santiago [?]`)

## BIZ/PROJECT Heuristics

The parser applies these rules to separate the BIZ/PROJECT label from UPDATE content:

| Scenario | Example | Handling |
|----------|---------|----------|
| Clean label on line 1 | `Contact Center` | BIZ = line 1, UPDATE starts at line 2 |
| Label with trailing colon | `Supply Chain IBP:` | Colon stripped, BIZ = `Supply Chain IBP` |
| Long text after colon (>50 chars) | `Track Optimization: Both projects are running...` | BIZ = text before colon, rest → UPDATE |
| Short label on line 2 (<=5 words) | Line 1: `Supply Chain IBP:`, Line 2: `Supply Name Ratio` | BIZ = `Supply Chain IBP / Supply Name Ratio` |

## Maintaining the Roster

When new team members join or new nicknames appear:

1. Open `roster.py`
2. Add the first-name (lowercase) → full name mapping to `ROSTER`
3. If the first name is ambiguous (e.g., two "David"s), add entries to `LAST_INITIAL_MAP`
4. Unresolved names show up as `Name [?]` in the output -- use these to find what needs adding

## Programmatic Usage

```python
from extract_raw_updates import process_docx

# Returns the path of the written .md file
md_path = process_docx("path/to/report.docx", "path/to/output.md")
```

## Known Limitations

- **Person detection is heuristic-based**: Short capitalized lines without a roster match may be misidentified as person names. Review the output for the first run of any new report author.
- **BIZ/PROJECT is captured as-is**: No canonical business-area classification is applied at this stage. That happens in Step 1 (Summarize & Classify).
- **Embedded tables in DOCX are not extracted**: `python-docx` paragraph iteration skips table content. If updates contain tables, they will be missing from the output.
