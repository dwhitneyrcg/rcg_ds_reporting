# Knowledge Prompts — File Map

This directory contains all prompt definitions, requirements, code, and plans for the PR-gated knowledge base pipeline. See [DESIGN_DOC.md](../DESIGN_DOC.md) for the full system architecture.

---

## Directory Structure

```
tools/
├── README.md                          ← You are here
├── DESIGN_DOC.md                      ← System design document (copy)
├── agents/                            ← Agent definitions (planner, validator, executor)
├── requirements/                      ← Validated requirements
├── plans/                             ← Planner agent output
├── prompts/                           ← Prompt definitions (.prompt.md) + original .docx
├── code/                              ← Python scripts + execution logs
└── reusable/                          ← (Reserved) Shared prompt fragments
```

---

## 1. Requirements (`requirements/`)

| File | Description |
|------|-------------|
| `REQ_knowledge_base_system.md` | Complete requirements document (R1–R7) covering system-level, pipeline, agent, content/formatting, classification, and validation requirements. Every requirement has a traceable ID. |

---

## 2. Prompt Definitions (`prompts/`)

### Converted Prompt Files (`.docx` → `.prompt.md`)

| File | Stage | Description |
|------|-------|-------------|
| `executive_summary.prompt.md` | Step 1 | INSTRUCT_BASE logic — generates per-area executive weekly report, parameterized to read mappings from master files |
| `evp_highlights.prompt.md` | Step 1 | INSTRUCT_HIGHLIGHTS logic — produces exactly 3 achievements + 3-4 focus areas with selection criteria and headline rules |
| `classification_rules.prompt.md` | Shared | Business area classification system — maps raw update text to one of 17 canonical business areas |
| `style_guide_executive.prompt.md` | Shared | Formatting and tone rules for executive summaries (do/don't table, structural rules, example output) |
| `build_business_areas_and_projects.prompt.md` | Step 2 | Entity creation/update templates for propagating weekly updates to people, project, and business area overview files |

### Pipeline Prompt Files

| File | Stage | Description |
|------|-------|-------------|
| `parse_weekly_report.prompt.md` | Step 1 | Defines the 5-step process: split into blocks, classify area, match projects, separate status, output tagged markdown |
| `deduplicate_updates.prompt.md` | Step 1 | Rules for comparing current vs. prior week tagged reports to remove duplicate content (≥75% similarity threshold) |
| `update_person_entity.prompt.md` | Step 2 | Instructions for updating person overview files — tracking table, active projects, frontmatter |
| `update_project_entity.prompt.md` | Step 2 | Instructions for updating project overview files — tracking table, delivery status, milestones |
| `update_business_area_entity.prompt.md` | Step 2 | Instructions for updating business area overview files — current status narrative, project/team lists |
| `generate_changelog.prompt.md` | Step 2 | Rules for producing the auditable changelog with per-entity change tables |

### Converted Instruction Files (`.docx` → `.md`)

| File | Source | Description |
|------|--------|-------------|
| `20251031 - Instruction Files (Business Area Summarization).md` | `.docx` | Original per-area summarization instructions (converted to markdown) |
| `20251031 - Instructions Files (Generate Business Area Mappings).md` | `.docx` | Original business area classification instructions (converted to markdown) |
| `20260323 - Build Business Areas and Projects (Updated).md` | `.docx` | Original entity-building instructions (converted to markdown) |

### Original `.docx` Files (`prompts/docx/`)

| File | Description |
|------|-------------|
| `20251031 - Instruction Files (Business Area Summarization).docx` | Original summarization instructions |
| `20251031 - Instructions Files (Generate Business Area Mappings).docx` | Original classification instructions |
| `20260323 - Build Business Areas and Projects (Original).docx` | Original entity-building instructions (v1) |
| `20260323 - Build Business Areas and Projects (Updated).docx` | Updated entity-building instructions |

### Pending Conversion (`.docx` — not yet converted to `.prompt.md`)

| File | Description |
|------|-------------|
| `20260323 - Build People Information (Updated v2).docx` | Instructions for building people entity files |
| `20260324 - Format Weekly Updates into Markdown (Updated).docx` | Instructions for converting weekly report format |

---

## 3. Python Code (`code/`)

### Pipeline Scripts

| File | Stage | Description |
|------|-------|-------------|
| `batch_convert.py` | Stage 0 | Orchestrates batch `.docx` → `.md` conversion with idempotency (skips existing `.md` files). Wraps `docx_to_markdown.py`. |
| `parse_weekly_report.py` | Stage 1 | Parses raw weekly reports into tagged markdown. Reads team roster, business areas, and projects from master `.md` files at runtime. ~350 lines. |
| `deduplicate_updates.py` | Stage 1 | Compares current vs. prior week tagged reports; removes items with ≥75% text similarity. Logs all removals. |
| `generate_changelog.py` | Stage 2 | Reads tagged report, compares against entity state, produces `CHANGELOG.md` with person/area/project change tables. |
| `validate_knowledge_base.py` | Stage 3 | Validates YAML frontmatter, wikilink resolution, required sections, orphan detection. Returns exit code 0/1. |
| `generate_pr_summary.py` | Stage 3 | Reads changelog + validation report to produce a PR description with summary stats, review checklist, and embedded changelog. |
| `docx_to_markdown.py` | Utility | Converts individual `.docx` files to Markdown preserving bold/italic, headings, tables, and lists. Produces timestamped execution logs. |

### Execution Logs (`code/logs/`)

| File | Description |
|------|-------------|
| `docx_to_markdown_20260419_234511.log` | Conversion run: 3 instruction `.docx` files → `.md` |
| `docx_to_markdown_20260419_234521.log` | Conversion run: 49 raw weekly reports → `.md` in `reporting/weekly_updates_raw_md/` |

---

## 4. Plans (`plans/`)

| File | Description |
|------|-------------|
| `2026-04-19_initial_agent_setup.md` | Initial setup plan documenting all Phase 1 deliverables and defining Phase 2 next steps |

---

## 5. Agent Definitions (`agents/`)

| File | Role | Description |
|------|------|-------------|
| `agents/kb-planner.agent.md` | Planner | Read-only analysis — produces structured plans, iterates with Validator |
| `agents/kb-validator.agent.md` | Validator | Reviews plans/output against requirements, returns pass/fail verdicts |
| `agents/kb-executor.agent.md` | Executor | Implements validated plans, creates/edits files, logs all actions |

The agents are invocable from VS Code's agent picker. Start with `@kb-planner` to plan a weekly cycle — it will automatically engage `@kb-validator`, and then you hand the validated plan to `@kb-executor`.

---

## 6. Reserved (`reusable/`)

Placeholder for shared prompt fragments that can be composed across multiple prompt files. Currently empty.
