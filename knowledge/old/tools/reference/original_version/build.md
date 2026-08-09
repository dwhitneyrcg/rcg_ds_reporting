# Build: Knowledge Base Pipeline Workflow

**Date:** April 20, 2026  
**Status:** Active  
**Scope:** `C:\Users\133486\OneDrive - Royal Caribbean Group\LocalDatabricks\rcg_ds_reporting\knowledge\tools\`

---

## Task

Build a set of prompts and code that implement the full weekly knowledge base pipeline as defined in [DESIGN_DOC.md](DESIGN_DOC.md). The pipeline ingests raw weekly `.docx` reports, converts them to `.md`, classifies and summarizes updates, and propagates changes to entity files (people, projects, business areas). When complete, update `DESIGN_DOC.md` and `README.md` to reflect all additions.

---

## Constraints

1. **Architecture target:** Use `DESIGN_DOC.md` and `README.md` in this folder as the authoritative specification.
2. **File scope:** You are ONLY allowed to add, modify, or delete files within:
   ```
   C:\Users\133486\OneDrive - Royal Caribbean Group\LocalDatabricks\rcg_ds_reporting\knowledge\tools\
   ```
3. **No hardcoding:** Do NOT hardcode people, business areas, or active projects. Instead, read from the markdown support files listed below at runtime.
4. **Agent workflow:** Use the Planner → Validator → Executor process. Document all work in the designated locations per agent.

---

## Markdown Support Files (Read-Only References)

These files are the single source of truth. All classification, resolution, and entity lookups must reference them — never embed their contents as literals.

| Data | Path |
|------|------|
| Business Areas | `C:\Users\133486\OneDrive - Royal Caribbean Group\LocalDatabricks\rcg_ds_reporting\knowledge\biz_areas\business_areas_master.md` |
| Active Projects | `C:\Users\133486\OneDrive - Royal Caribbean Group\LocalDatabricks\rcg_ds_reporting\knowledge\biz_areas\business_active_projects_master.md` |
| People | `C:\Users\133486\OneDrive - Royal Caribbean Group\LocalDatabricks\rcg_ds_reporting\knowledge\people\master_team_roster.md` |

---

## Agent Roles & Artifact Locations

### Planner (`agents/kb-planner.agent.md`)

Analyzes the codebase and architects a solution. Works with the Validator to revise the plan until it passes all requirements.

**Output location:** `knowledge/tools/plans/`  
**Output format:** Markdown plan documents

### Validator (`agents/kb-validator.agent.md`)

Reviews the Planner's suggestions against the requirements in `DESIGN_DOC.md`, `requirements/REQ_knowledge_base_system.md`, and user instructions. Documents any new or clarified requirements.

**Output location:** `knowledge/tools/requirements/`  
**Output format:** Markdown requirement and validation documents

### Executor (`agents/kb-executor.agent.md`)

Takes the validated plan and creates prompt files or Python code. All Python code execution must be logged.

**Output locations:**

| Artifact | Location |
|----------|----------|
| Prompt files | `knowledge/tools/prompts/` |
| Python code | `knowledge/tools/code/` |
| Execution logs | `knowledge/tools/code/logs/` |

---

## Raw Weekly Report Pattern

Raw weekly reports are `.docx` files converted to `.md`. They follow a consistent structural pattern that the pipeline must parse:

### Document-Level Structure
- One flat document per week containing updates from all reporting team members
- No YAML frontmatter in raw files
- No consistent document-level header

### Per-Person Block Structure

Each report is a sequence of person-level blocks:

```
<Person Name(s)> [optional: (Business Area context)]
<Business Area / Brand>: <Project Name>
[Optional status section headers: Completed, In Progress, Next Steps, Key Dates]
- Bullet point work items
- More bullets
```

### Classification Signals

| Signal | Location | Example |
|--------|----------|---------|
| **Person name** | First line of each block | `Mert`, `Ben & Camila`, `Mirielle T.` |
| **Business area** | Text before the first `:` or `\|` in the project header | `Contact Center:`, `RCI \| SPI Factor` |
| **Brand prefix** | Pipe-delimited prefix on project headers | `RCI \|`, `CEL \|`, `SSC \|` |
| **Project name** | Text after the area/brand prefix | `GTY-LEAD 3.0`, `PRE`, `BKTOCX` |
| **Completed vs. ongoing** | Section headers or verb tense | `Completed:`, `In Progress:`, `Next Steps:` |

### Variability to Handle

- Person names are inconsistent: first name only, full name, multiple people (`Ben & Camila`)
- Business area labels vary: `MIAP`, `Marine`, `Contact Center`, `IBP: Supply Chain`
- Project delimiters vary: `|`, `#`, `:`, bold text, plain text
- Some blocks lack explicit business area headers — context must be inferred from content
- The same person may appear in multiple blocks for different business areas
- Updates from multiple people on the same project may not be adjacent

---

## Pipeline Stages to Build

### Stage 0: Convert `.docx` → `.md`

**Existing:** `code/docx_to_markdown.py` — already functional.

**What's needed:**
- Prompt or script to orchestrate batch conversion of new weekly `.docx` files
- Idempotency check: skip files that already have a corresponding `.md`

### Stage 1: Summarize & Classify

**Existing prompts:** `executive_summary.prompt.md`, `evp_highlights.prompt.md`, `classification_rules.prompt.md`, `style_guide_executive.prompt.md`

**What's needed:**
- A **parsing prompt/code** that takes a raw `.md` weekly report and splits it into structured per-person, per-business-area update blocks
- The parser must:
  1. Identify person name boundaries (where one person's block ends and the next begins)
  2. Extract the business area label from each block using `classification_rules.prompt.md`
  3. Resolve person names to canonical identifiers by reading `master_team_roster.md`
  4. Match update content to active projects by reading `business_active_projects_master.md`
  5. Separate completed work from in-progress/next-steps items
  6. Output a structured tagged `.md` file with YAML frontmatter listing all entities referenced
- The existing `executive_summary.prompt.md` and `evp_highlights.prompt.md` then consume this structured output to produce the two report formats
- A **deduplication prompt/code** that compares against the prior week's report to flag repeated content

### Stage 2: Propagate to Entities

**Existing prompt:** `build_business_areas_and_projects.prompt.md`

**What's needed:**
- A **person update prompt** that takes the tagged weekly summary and generates edits for each referenced person's overview file:
  - Append a row to their weekly tracking table
  - Update their active project list if changed
  - Update `last_updated` in frontmatter
- A **project update prompt** that updates each referenced project's overview:
  - Append weekly progress to tracking table
  - Update delivery status if the weekly report indicates a status change
  - Add new milestones if mentioned
- A **business area update prompt** that updates each referenced area's overview:
  - Update the current quarter narrative summary
  - Cascade any project status changes
- A **changelog generator** that produces a `reporting/changelogs/YYYY-MM-DD.md` file listing all entity changes with justifications

### Stage 3: Validation & PR Preparation

**What's needed:**
- A **validation script** (`code/validate_knowledge_base.py`) that checks:
  - All `.md` files with frontmatter have valid YAML
  - All wikilinks resolve to existing files
  - No required fields are empty
  - Person files reference only projects in `business_active_projects_master.md`
  - No orphan references
- A **PR summary generator** that produces a human-readable description of all changes for the PR body

---

## Execution Sequence

```
1. Planner reads this build.md + DESIGN_DOC.md + existing prompts/code
         │
         ▼
2. Planner produces a plan in plans/ detailing:
   - What new prompts to create
   - What new code to write
   - What existing files to modify
   - Execution order and dependencies
         │
         ▼
3. Validator reviews the plan against:
   - DESIGN_DOC.md architecture
   - requirements/REQ_knowledge_base_system.md
   - This build.md constraints
   - Returns PASS/FAIL with feedback
         │
         ▼
4. If FAIL → Planner revises and resubmits
   If PASS → Executor implements
         │
         ▼
5. Executor creates prompts in prompts/ and code in code/
   Executor logs all actions in code/logs/
         │
         ▼
6. Validator reviews Executor output
   - Structural validation (files exist, correct format)
   - Content validation (meets prompt requirements)
         │
         ▼
7. If PASS → Update DESIGN_DOC.md and README.md
```

---

## Completion Criteria

This build is complete when:

- [ ] Stage 0 has an orchestration script or prompt for batch `.docx` → `.md` conversion with idempotency
- [ ] Stage 1 has a parser that splits raw weekly `.md` into structured tagged blocks
- [ ] Stage 1 has a deduplication mechanism against prior week
- [ ] Stage 1 produces structured output consumable by `executive_summary.prompt.md` and `evp_highlights.prompt.md`
- [ ] Stage 2 has prompts for updating person, project, and business area entity files
- [ ] Stage 2 has a changelog generator
- [ ] Stage 3 has a validation script for YAML, wikilinks, and required fields
- [ ] Stage 3 has a PR summary generator
- [ ] All Python code has execution logs in `code/logs/`
- [ ] All prompts reference support files dynamically (no hardcoded entity data)
- [ ] `DESIGN_DOC.md` is updated to reflect the implemented pipeline
- [ ] `README.md` is updated with a complete file map of all new artifacts
