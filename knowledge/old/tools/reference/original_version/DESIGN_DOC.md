# Design Document: PR-Gated Knowledge Base System

**Author:** David Whitney  
**Date:** April 19, 2026  
**Status:** Draft  
**Repository:** `rcg_ds_reporting`

---

## 1. Purpose

Build and maintain an auditable, interlinked markdown knowledge base that tracks the Data Science organization's people, projects, business areas, and weekly progress. The system uses weekly reports as the sole ingestion point for new knowledge, with all updates vetted through the pull request review process.

## 2. Design Principles

| Principle | Rationale |
|-----------|-----------|
| **PR-gated ingestion** | Every knowledge update flows through a code commit and PR review, providing traceability, rollback capability, and content validation by human reviewers. |
| **Weekly report as single entry point** | All new knowledge enters through structured weekly reports. No ad-hoc edits to entity files — the pipeline is the only writer. |
| **Knowledge feedback loop** | The knowledge base provides context for generating the next week's report; the report then feeds back to update the knowledge base. Quality compounds over time. |
| **Entities are dynamic, not static** | People, project, and business area overviews are living documents updated programmatically each cycle — not reference pages maintained by hand. |
| **Separation of compression and integration** | Summarizing raw reports (Step 1) and propagating updates to entity files (Step 2) are distinct pipeline stages with different failure modes and validation needs. |

## 3. System Architecture

### 3.1 High-Level Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                        WEEKLY CYCLE                                 │
│                                                                     │
│  ┌──────────┐    ┌──────────────┐    ┌──────────────────────────┐   │
│  │ Raw Team │    │   STEP 1:    │    │       STEP 2:            │   │
│  │ Reports  │───▶│  Summarize   │───▶│  Propagate to Entities  │  │
│  │ (.docx)  │    │  & Classify  │    │  (People, Projects,      │  │
│  └──────────┘    └──────┬───────┘    │   Business Areas)        │  │
│                         │            └────────────┬─────────────┘  │
│                         │                         │                │
│                         ▼                         ▼                │
│                  ┌─────────────┐          ┌─────────────────┐      │
│                  │  Tagged     │          │ Entity File     │      │
│                  │  Weekly     │          │ Edits (diffs)   │      │
│                  │  Summary    │          │ + Changelog     │      │
│                  │  (.md)      │          └────────┬────────┘      │
│                  └─────────────┘                   │               │
│                                                    ▼               │
│                                           ┌────────────────┐       │
│                                           │   PR Created   │       │
│                                           │  for Review    │       │
│                                           └────────┬───────┘       │
│                                                    │               │
│                                                    ▼               │
│                                           ┌────────────────┐       │
│                                           │  Human Review  │       │
│                                           │  & Merge       │       │
│                                           └────────┬───────┘       │
│                                                    │               │
│                                                    ▼               │
│                                           ┌────────────────┐       │
│                                           │ Updated        │       │
│  ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│ Knowledge Base │       │
│  │  Context fed into next week's Step 1   └────────────────┘       │
│  └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─         │
└────────────────────────────────────────────────────────────────────┘
```

### 3.2 Knowledge Base Structure

```
knowledge/
├── knowledge_context.md                  # Base path and global context
├── conventions/
│   └── wiki_links/
│       └── wikilink_conventions.md       # Linking standards
├── people/
│   ├── master_team_roster.md             # Active/inactive team index
│   └── <person_name>/
│       └── overview_<name>.md            # Role, leader, areas, project tracking
├── biz_areas/
│   ├── business_areas_master.md          # All business areas index
│   ├── business_active_projects_master.md# All active projects index
│   └── <business_area>/
│       ├── overview_<area>.md            # Goal, impact, OKRs, team, status
│       └── <project>/
│           └── overview_<project>.md     # Project details, milestones, status
├── okrs/                                 # Quarterly OKR tracking
├── repositories/                         # Code repository documentation
│   └── <system>/
│       ├── OVERVIEW_<repo>.md            # Architecture docs
│       └── DIAGRAM_<repo>.md             # Mermaid diagrams
├── reporting/
│   ├── weekly_updates_raw/               # Source .docx files
│   ├── weekly_updates_raw_md/            # Parsed raw reports (.md)
│   ├── weekly_updates_summarized/        # Summarized .docx files
│   ├── weekly_updates_summarized_md/     # Parsed summaries (.md)
│   └── changelogs/                       # Per-cycle change summaries
└── tools/                                # AI prompt definitions & code (→ skills)
    ├── step1_summarize_and_classify/
    └── step2_propagate_to_entities/
    └── agents/
    └── code/
    └── prompts/
    └── planning/
    └── requirements/

```

### 3.3 Entity File Conventions

All entity overview files follow a standard structure:

- **YAML frontmatter** with tags for discoverability and cross-referencing
- **Obsidian wikilinks** (`[[path/to/note|Label]]`) for bidirectional navigation
- **Structured sections** for both static metadata and dynamic tracking tables
- **Canonical naming** — folder and file names are lowercase, hyphen/underscore-delimited

Linking conventions are defined in `conventions/wiki_links/wikilink_conventions.md`.

## 4. Pipeline Stages

### 4.1 Step 1: Summarize & Classify

**Input:** Raw weekly team reports (`.docx`)  
**Context:** Current knowledge base (business areas, projects, people, prior week's report)  
**Output:** Tagged weekly summary (`.md`) with structured sections per business area

**Responsibilities:**
1. Parse raw `.docx` content
2. Classify each update to a canonical business area using alias mappings
3. Match updates to specific active projects
4. Resolve person names with disambiguation
5. Separate achievements (past-tense accomplishments) from focus areas (forward-looking work)
6. Generate two output formats:
   - **Executive summary** (`INSTRUCT_BASE`) — per-area bullet points for weekly distribution
   - **EVP highlights** (`INSTRUCT_HIGHLIGHTS`) — 3 achievements + 3-4 focus areas for senior leadership

**Mapping Strategy:**
- Business area aliases and project lists should be **read from master markdown files** at runtime, not hardcoded in Python. This ensures the pipeline always reflects the current state of the knowledge base.
- Person resolution should read from `master_team_roster.md` and individual overview files.

### 4.2 Step 2: Propagate to Entities

**Input:** Tagged weekly summary from Step 1  
**Context:** Current state of all entity files to be updated  
**Output:** Modified entity files + changelog

**Responsibilities:**
1. Parse the tagged weekly summary to extract per-entity updates
2. For each referenced **person**: update their project tracking table with the week's work
3. For each referenced **project**: update delivery status, latest progress, milestone dates
4. For each referenced **business area**: update current status, active work summary
5. Generate a **changelog** summarizing all proposed edits and rationale

**Edit Strategy:**

| Entity Type | What Gets Updated | How |
|-------------|-------------------|-----|
| Person overview | Weekly tracking table, active project list | Append row to tracking table; add/remove project wikilinks |
| Project overview | Delivery status, latest milestones, weekly tracking | Update status field in frontmatter; append to milestone log |
| Business area overview | Current quarter summary, project statuses | Update narrative summary; cascade project status changes |

**Guardrails for Step 2:**
- **No orphan references** — every wikilink created must point to an existing entity file
- **No destructive overwrites without justification** — if a status field changes (e.g., "On Track" → "At Risk"), the changelog must state the source update that triggered it
- **Validation pass** — after edits, verify all modified files have valid YAML frontmatter and intact wikilink syntax
- **Diff preview** — generate a human-readable summary of all changes before committing

### 4.3 Changelog Generation

Each weekly cycle produces a changelog file at `reporting/changelogs/YYYY-MM-DD.md`:

```markdown
# Weekly Knowledge Update — 2026-04-17

## Summary
- 12 person files updated
- 8 project files updated
- 5 business area files updated

## Changes by Entity

### People
- **Benjamin Fowler** — Added weekly tracking entry for Supply Chain (Beverage Optimization, HVAC Diagnostics)
- **Camila Aichele** — Updated active project list: added "New Initiative X"

### Projects
- **PRE 4.0** — Status changed: "In Development" → "UAT". Source: "PRE 4.0 entered user acceptance testing this week"
- **SPI Track Optimization** — Added milestone: "v2 model deployed to staging"

### Business Areas
- **Revenue Management Automation (RCI)** — Updated Q2 progress narrative
```

This changelog is included in the PR to reduce reviewer burden — reviewers scan intent here, then spot-check diffs.

## 5. PR Review Process

### 5.1 Branch Strategy

Each weekly cycle creates a branch:

```
weekly-update/YYYY-MM-DD
```

The branch contains:
1. New tagged weekly summary file(s) in `reporting/`
2. Modified entity files (people, projects, business areas)
3. Changelog file

### 5.2 Review Scope

| Reviewer Role | Reviews | Focus |
|---------------|---------|-------|
| Pipeline owner (you) | Changelog + spot-check diffs | Factual accuracy, no regressions |
| Business area lead (optional) | Their area's diffs only | Domain accuracy |
| Automated checks | All modified files | YAML validity, wikilink integrity, no orphan references |

### 5.3 Automated Validation (CI)

Pre-merge checks to implement:

- [ ] All `.md` files with frontmatter have valid YAML
- [ ] All wikilinks resolve to existing files
- [ ] No entity file has an empty/missing required field (status, tags, leader)
- [ ] Person files reference only projects that exist in `business_active_projects_master.md`
- [ ] Changelog file exists for the weekly cycle
- [ ] No files outside `knowledge/` and `reporting/` are modified by the pipeline

## 6. Prompt Architecture

### 6.1 Current State

Prompts are stored as `.md` files in `knowledge/tools/`. 
Raw Prompts are stored as '.docx' files. This creates friction:
- Binary files produce opaque git diffs
- Require `extract_docx.py` to read programmatically
- Cannot be parameterized or composed
- Cannot be version-controlled meaningfully

### 6.2 Target State: Markdown-Based Prompts → Skills

Convert prompt definitions to markdown files with YAML frontmatter for metadata. These become composable, version-controlled, and git-diffable.

**Proposed structure:**

```
knowledge/prompts/
├── step1_summarize_and_classify/
│   ├── executive_summary.prompt.md       # INSTRUCT_BASE logic
│   └── evp_highlights.prompt.md          # INSTRUCT_HIGHLIGHTS logic
├── step2_propagate_to_entities/
│   ├── update_person.prompt.md           # How to edit person files
│   ├── update_project.prompt.md          # How to edit project files
│   └── update_business_area.prompt.md    # How to edit business area files
└── shared/
    ├── classification_rules.prompt.md    # Business area mapping rules
    └── style_guide.prompt.md             # Formatting and tone rules
```

**Prompt file format:**

```markdown
---
name: executive_summary
description: Generate executive weekly report from raw team updates
inputs:
  - raw_updates: "This week's raw team reports"
  - prior_report: "Last week's executive summary"
  - business_areas: "Current business area list from master file"
  - active_projects: "Current active project list from master file"
output: "Formatted executive weekly report with per-area summaries"
---

## System Instructions
...

## Classification Rules
{{classification_rules}}

## Output Format
...
```

### 6.3 Migration Path

1. Extract current `.docx` prompt content to `.prompt.md` files
2. Parameterize — replace hardcoded lists with template variables that read from master files
3. Validate — run both old and new prompts on the same input, compare outputs
4. Deprecate `.docx` files once markdown versions are proven
5. Optionally convert to VS Code skills (`.github/copilot/skills/`) if using Copilot as the execution engine

## 7. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Step 2 makes incorrect edits to entity files | High (early) | Medium | PR review gate; changelog with justifications; automated validation |
| PR review becomes rubber-stamp as volume grows | Medium | High | Changelog summaries; scoped reviews by area; automated validation catches structural errors |
| Step 1 mis-classifies update to wrong business area | Medium | Medium | Mapping data read from master files (single source of truth); classification confidence scores |
| Knowledge base context biases AI with stale info | Medium | Medium | Step 2 must update entities comprehensively each cycle; periodic full-base audits |
| Cascading errors (Step 1 error → Step 2 propagation) | Medium | High | Step 1 output reviewed before Step 2 runs; two-PR approach (one per step) if needed |
| .docx parsing fragility | Low | Medium | Migrate input format to structured markdown or form-based submission |
| Single-person review bottleneck | High | Medium | Delegate area-level reviews to team leads; invest in CI validation |

## 8. Implementation Phases

### Phase 1: Foundation (Complete)
- [x] Knowledge base structure (people, projects, business areas)
- [x] Master index files with wikilinks
- [x] Weekly report parsing (`process_weekly_updates.py`)
- [x] AI prompt definitions for Step 1
- [x] Convert prompts from `.docx` to `.prompt.md`
- [x] Extract mapping dictionaries from Python code to master `.md` files

### Phase 2: Full Pipeline (Complete)
- [x] Stage 0: Batch `.docx` → `.md` conversion (`code/batch_convert.py`)
- [x] Stage 1: Parse & tag weekly reports (`code/parse_weekly_report.py`)
- [x] Stage 1: Deduplicate vs. prior week (`code/deduplicate_updates.py`)
- [x] Stage 2: Entity update prompts (person, project, business area)
- [x] Stage 2: Changelog generation (`code/generate_changelog.py`)
- [x] Stage 3: Knowledge base validation (`code/validate_knowledge_base.py`)
- [x] Stage 3: PR summary generation (`code/generate_pr_summary.py`)
- [ ] Test on 2-3 weekly cycles manually before automating

### Phase 3: Automation & CI
- [ ] Automate branch creation and PR generation per weekly cycle
- [ ] Add CI validation checks (pre-merge) using `validate_knowledge_base.py`
- [ ] Implement scoped review routing (by business area)
- [ ] Build diff preview / changelog summary for PR descriptions

### Phase 4: Scale & Harden
- [ ] Populate OKR tracking and tie to business area quarterly reviews
- [ ] Add repository documentation updates to the pipeline (code changes → architecture docs)
- [ ] Periodic knowledge base audits (quarterly review of entity accuracy)
- [ ] Metrics: track review time, error rate, knowledge freshness

## 9. Open Questions

1. **Input format migration:** Can team members submit weekly updates as markdown or a structured form instead of `.docx`? This would eliminate parsing complexity.
2. **Two-PR vs. one-PR per cycle:** Should Step 1 output be reviewed and merged before Step 2 runs, or should the full cycle be a single PR? Two PRs add process overhead but prevent cascading errors.
3. **Granularity of entity updates:** How much history should entity files retain? Append-only tracking tables will grow indefinitely — define a rolling window or archival strategy.
4. **Multi-reviewer routing:** Who reviews which areas? Define the CODEOWNERS mapping for `knowledge/biz_areas/<area>/`.
5. **Execution engine:** Should prompts be executed via Azure OpenAI API, Databricks Foundation Models, or VS Code Copilot skills? Each has different automation and cost profiles.
