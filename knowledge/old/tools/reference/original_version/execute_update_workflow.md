# Execute Weekly Knowledge Base Update

**Purpose:** Step-by-step runbook for processing a new weekly report through the full pipeline (Stage 0 → Stage 3). Follow each stage in order — each stage depends on the output of the previous one.

---

## Prerequisites

- Python 3.12+ with `python-docx` and `pyyaml` installed
- Activate the venv: `.venv\Scripts\activate`
- Working directory: `C:\Users\133486\OneDrive - Royal Caribbean Group\LocalDatabricks\rcg_ds_reporting\`
- A new weekly report `.docx` file in `knowledge/reporting/weekly_updates_raw/`

## Variables

Set these once at the start. Replace the date with the current report date.

```powershell
$REPORT_DATE = "2026-04-20"
$ROOT = "C:\Users\133486\OneDrive - Royal Caribbean Group\LocalDatabricks\rcg_ds_reporting"
$TOOLS = "$ROOT\knowledge\tools"
$CODE = "$TOOLS\code"
$RAW_DOCX = "$ROOT\knowledge\reporting\weekly_updates_raw"
$RAW_MD = "$ROOT\knowledge\reporting\weekly_updates_raw_md"
$CHANGELOGS = "$ROOT\knowledge\reporting\changelogs"
$PYTHON = "$ROOT\.venv\Scripts\python.exe"
```

---

## Stage 0 — Convert `.docx` → `.md`

**Script:** `code/batch_convert.py`  
**Input:** Raw `.docx` files in `weekly_updates_raw/`  
**Output:** Corresponding `.md` files in `weekly_updates_raw_md/`  
**Idempotency:** Skips files that already have a `.md` counterpart.

### Run

```powershell
& $PYTHON "$CODE\batch_convert.py" "$RAW_DOCX" "$RAW_MD"
```

### Verify

- Check `code/logs/batch_convert_*.log` for conversion results
- Confirm the new `.md` file exists in `$RAW_MD`
- Open the `.md` file and spot-check that headings, bullets, and tables converted cleanly

### Troubleshooting

| Symptom | Fix |
|---------|-----|
| `ModuleNotFoundError: python-docx` | `& $PYTHON -m pip install python-docx` |
| `.md` already exists, skipped | Expected if this report was already converted. Delete the `.md` to force re-conversion. |
| Garbled table formatting | Open the `.docx` in Word and check for merged cells or nested tables — these require manual cleanup. |

---

## Stage 1a — Parse & Tag Weekly Report

**Script:** `code/parse_weekly_report.py`  
**Input:** The raw `.md` report from Stage 0  
**Output:** A tagged `.md` file with YAML frontmatter, structured by business area and person  
**Data sources read at runtime:** `master_team_roster.md`, `business_areas_master.md`, `business_active_projects_master.md`

### Identify the input file

```powershell
$RAW_FILE = Get-ChildItem "$RAW_MD" -Filter "*$REPORT_DATE*" | Select-Object -First 1
Write-Host "Input: $($RAW_FILE.FullName)"
```

If no file matches the date, list available files and pick the correct one:

```powershell
Get-ChildItem "$RAW_MD" -Filter "*.md" | Sort-Object Name -Descending | Select-Object -First 10 Name
```

### Run

```powershell
$TAGGED_FILE = "$RAW_MD\tagged_$REPORT_DATE.md"
& $PYTHON "$CODE\parse_weekly_report.py" "$($RAW_FILE.FullName)" "$TAGGED_FILE"
```

### Verify

- Check `code/logs/parse_weekly_report_*.log` for warnings (unresolved names, unknown areas)
- Open `$TAGGED_FILE` and confirm:
  - YAML frontmatter lists all people and areas referenced
  - Each `## Business Area` section has `### Person` subsections
  - Bullet items are classified under the correct area
  - No person block is empty

### Troubleshooting

| Symptom | Fix |
|---------|-----|
| Person name not resolved | Add an alias to `master_team_roster.md` or update the person's overview file. Re-run. |
| Wrong business area classification | Check `classification_rules.prompt.md` and `business_areas_master.md` for missing aliases. |
| `ModuleNotFoundError: pyyaml` | `& $PYTHON -m pip install pyyaml` |

---

## Stage 1b — Deduplicate vs. Prior Week

**Script:** `code/deduplicate_updates.py`  
**Input:** This week's tagged `.md` + prior week's tagged `.md`  
**Output:** Deduplicated tagged `.md` (same structure, duplicate items removed)  
**Threshold:** Items with ≥75% text similarity to a prior-week item are removed.

### Identify the prior week's tagged file

```powershell
$PRIOR_DATE = (Get-Date $REPORT_DATE).AddDays(-7).ToString("yyyy-MM-dd")
$PRIOR_FILE = "$RAW_MD\tagged_$PRIOR_DATE.md"

if (Test-Path $PRIOR_FILE) {
    Write-Host "Prior week file found: $PRIOR_FILE"
} else {
    Write-Host "No prior week file — dedup will pass through unchanged"
}
```

### Run

```powershell
$DEDUPED_FILE = "$RAW_MD\deduped_$REPORT_DATE.md"
& $PYTHON "$CODE\deduplicate_updates.py" "$TAGGED_FILE" "$PRIOR_FILE" "$DEDUPED_FILE"
```

### Verify

- Check console output for duplicate count
- Check `code/logs/deduplicate_*.log` for each removed item and its similarity score
- Open `$DEDUPED_FILE` and confirm no genuine new content was removed
- If this is the first week (no prior file), the output should be identical to the tagged input

### Troubleshooting

| Symptom | Fix |
|---------|-----|
| Too many items removed | Lower `SIMILARITY_THRESHOLD` in `deduplicate_updates.py` (default: 0.75). |
| Follow-up items incorrectly flagged | These should be kept — if removed, the similarity threshold is too aggressive. |
| Prior file path wrong | Verify `$PRIOR_FILE` points to the correct tagged file. Adjust `$PRIOR_DATE` manually if the prior report wasn't exactly 7 days earlier. |

---

## Stage 2a — Update Entity Files

This stage uses the entity update prompts to propagate changes from the deduplicated tagged report into person, project, and business area overview files. **This step requires agent assistance or manual editing** — the prompts define _what_ to change, the agent or human applies the edits.

**Prompts:**
- `prompts/update_person_entity.prompt.md` — appends tracking rows, updates active project lists
- `prompts/update_project_entity.prompt.md` — appends tracking rows, updates delivery status and milestones
- `prompts/update_business_area_entity.prompt.md` — updates current status narrative, project/team lists

### Process

1. **Open** `$DEDUPED_FILE` (the deduplicated tagged report)
2. **For each person** mentioned in the report:
   - Read their overview file: `knowledge/people/<name>/overview_<name>.md`
   - Follow `update_person_entity.prompt.md` to append a tracking table row and update project lists
   - Update `last_updated` in frontmatter to `$REPORT_DATE`
3. **For each project** referenced:
   - Read its overview file: `knowledge/biz_areas/<area>/<project>/overview_<project>.md`
   - Follow `update_project_entity.prompt.md` to append progress and update status if warranted
4. **For each business area** with updates:
   - Read its overview file: `knowledge/biz_areas/<area>/overview_<area>.md`
   - Follow `update_business_area_entity.prompt.md` to update the Current Status narrative

### Using the KB Executor Agent

Instead of manual editing, invoke the executor agent:

```
@kb-executor Apply the deduplicated weekly report at <path to deduped file>
to all referenced entity files following the update prompts.
```

The executor will read the three update prompts and apply changes to each entity file, logging all actions.

---

## Stage 2b — Generate Changelog

**Script:** `code/generate_changelog.py`  
**Input:** The deduplicated tagged `.md`  
**Output:** `reporting/changelogs/YYYY-MM-DD.md`

### Run

```powershell
$CHANGELOG = "$CHANGELOGS\$REPORT_DATE.md"
New-Item -ItemType Directory -Path "$CHANGELOGS" -Force | Out-Null
& $PYTHON "$CODE\generate_changelog.py" "$DEDUPED_FILE" "$CHANGELOG"
```

### Verify

- Open `$CHANGELOG` and confirm:
  - Person Entity Updates table lists all people from the tagged report
  - Business Area Updates lists all areas
  - "File Exists" column shows **No** for any missing entity files (these need to be created)
  - Summary stats match your expectations
- Check `code/logs/generate_changelog_*.log`

---

## Stage 3a — Validate Knowledge Base

**Script:** `code/validate_knowledge_base.py`  
**Input:** Reads the entire `knowledge/` directory  
**Output:** Validation report at `code/logs/validation_report.md` + exit code 0 (pass) or 1 (fail)

### Run

```powershell
& $PYTHON "$CODE\validate_knowledge_base.py"
$exitCode = $LASTEXITCODE
Write-Host "Validation exit code: $exitCode"
```

### Interpret Results

| Result | Meaning | Action |
|--------|---------|--------|
| Exit 0, 0 errors | All checks passed | Proceed to PR summary |
| Exit 1, errors listed | Structural issues found | Fix each error before proceeding |
| Warnings only | Non-blocking issues | Review warnings; fix if time allows |

### Common Errors and Fixes

| Error | Fix |
|-------|-----|
| Missing YAML frontmatter | Add `---\nname: ...\nstatus: ...\nlast_updated: ...\n---` to the top of the file |
| Broken wikilink `[[path]]` | Verify the target file exists; fix the path or create the missing file |
| Missing required section | Add the section heading (e.g., `## Weekly Tracking`) to the entity overview |
| Orphan overview file | Add a wikilink to the file from the appropriate master list |

---

## Stage 3b — Generate PR Summary

**Script:** `code/generate_pr_summary.py`  
**Input:** Changelog from Stage 2b + validation report from Stage 3a  
**Output:** `pr_summary.md` ready to paste into a PR description

### Run

```powershell
$VALIDATION_REPORT = "$CODE\logs\validation_report.md"
$PR_SUMMARY = "$TOOLS\pr_summary_$REPORT_DATE.md"
& $PYTHON "$CODE\generate_pr_summary.py" "$CHANGELOG" "$VALIDATION_REPORT" "$PR_SUMMARY"
```

### Verify

- Open `$PR_SUMMARY` and confirm:
  - Summary table shows correct counts
  - Validation status matches Stage 3a result
  - Review checklist is present
  - Full changelog is embedded in the `<details>` block

---

## Final Steps — Commit & PR

Once all stages pass:

1. **Create a branch:**
   ```powershell
   git checkout -b weekly-update/$REPORT_DATE
   ```

2. **Stage all changed knowledge files:**
   ```powershell
   git add knowledge/
   ```

3. **Commit with a descriptive message:**
   ```powershell
   git commit -m "knowledge: weekly update $REPORT_DATE"
   ```

4. **Push and create PR:**
   ```powershell
   git push -u origin weekly-update/$REPORT_DATE
   ```

5. **Use the PR summary** (`$PR_SUMMARY`) as the PR description body.

6. **Review checklist** (from the PR summary):
   - [ ] Changelog entries are accurate
   - [ ] No unintended overwrites of existing entity content
   - [ ] New wikilinks resolve to existing files
   - [ ] Frontmatter `last_updated` dates are correct
   - [ ] No PII or sensitive content in tracking entries

---

## Quick Reference — Full Pipeline in One Block

```powershell
# --- Set variables ---
$REPORT_DATE = "2026-04-20"
$ROOT = "C:\Users\133486\OneDrive - Royal Caribbean Group\LocalDatabricks\rcg_ds_reporting"
$TOOLS = "$ROOT\knowledge\tools"
$CODE = "$TOOLS\code"
$RAW_DOCX = "$ROOT\knowledge\reporting\weekly_updates_raw"
$RAW_MD = "$ROOT\knowledge\reporting\weekly_updates_raw_md"
$CHANGELOGS = "$ROOT\knowledge\reporting\changelogs"
$PYTHON = "$ROOT\.venv\Scripts\python.exe"

# --- Stage 0: Convert ---
& $PYTHON "$CODE\batch_convert.py" "$RAW_DOCX" "$RAW_MD"

# --- Stage 1a: Parse & Tag ---
$RAW_FILE = (Get-ChildItem "$RAW_MD" -Filter "*$REPORT_DATE*" | Select-Object -First 1).FullName
$TAGGED_FILE = "$RAW_MD\tagged_$REPORT_DATE.md"
& $PYTHON "$CODE\parse_weekly_report.py" "$RAW_FILE" "$TAGGED_FILE"

# --- Stage 1b: Deduplicate ---
$PRIOR_DATE = (Get-Date $REPORT_DATE).AddDays(-7).ToString("yyyy-MM-dd")
$PRIOR_FILE = "$RAW_MD\tagged_$PRIOR_DATE.md"
$DEDUPED_FILE = "$RAW_MD\deduped_$REPORT_DATE.md"
& $PYTHON "$CODE\deduplicate_updates.py" "$TAGGED_FILE" "$PRIOR_FILE" "$DEDUPED_FILE"

# --- Stage 2a: Entity updates (agent-assisted) ---
# @kb-executor processes the deduped file against entity prompts

# --- Stage 2b: Changelog ---
$CHANGELOG = "$CHANGELOGS\$REPORT_DATE.md"
New-Item -ItemType Directory -Path "$CHANGELOGS" -Force | Out-Null
& $PYTHON "$CODE\generate_changelog.py" "$DEDUPED_FILE" "$CHANGELOG"

# --- Stage 3a: Validate ---
& $PYTHON "$CODE\validate_knowledge_base.py"

# --- Stage 3b: PR Summary ---
$PR_SUMMARY = "$TOOLS\pr_summary_$REPORT_DATE.md"
& $PYTHON "$CODE\generate_pr_summary.py" "$CHANGELOG" "$CODE\logs\validation_report.md" "$PR_SUMMARY"

# --- Commit ---
git checkout -b weekly-update/$REPORT_DATE
git add knowledge/
git commit -m "knowledge: weekly update $REPORT_DATE"
git push -u origin weekly-update/$REPORT_DATE
```
