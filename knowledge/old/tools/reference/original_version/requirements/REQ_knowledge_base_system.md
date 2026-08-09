# Requirements: PR-Gated Knowledge Base System

**Version:** 1.0  
**Date:** April 19, 2026  
**Source:** DESIGN_DOC.md + stakeholder discussions  
**Status:** Active

---

## R1. System-Level Requirements

### R1.1 Knowledge Base Scope
The knowledge base tracks four entity types:
- **People** — individual team members, their roles, leaders, assigned business areas, and project contributions
- **Projects** — active initiatives with goals, milestones, delivery status, and weekly progress
- **Business Areas** — organizational groupings of projects with strategic goals, dollar-impact targets, OKRs, and team assignments
- **Weekly Reports** — timestamped summaries of team activity, classified by business area and project

### R1.2 Single Entry Point
All new knowledge enters the system through weekly reports. Entity files (people, projects, business areas) are updated programmatically — not manually edited — to ensure consistency and auditability.

### R1.3 Audit Trail via Git
Every change to the knowledge base must be committed to git and reviewed via pull request before merging. This provides:
- Full traceability of who approved what change
- Rollback capability for incorrect updates
- Diff-based review of all proposed changes
- Accountability for knowledge quality

### R1.4 Feedback Loop
The knowledge base provides context for generating the next week's report (business area definitions, project lists, prior week summaries). The weekly report then feeds new knowledge back into entity files. This is a closed loop.

---

## R2. Pipeline Requirements

### R2.1 Stage 0: Input Conversion
- **R2.1.1** All `.docx` input files must be converted to Markdown before any processing
- **R2.1.2** The converter must preserve: paragraph text, table structures, list formatting, and bold/italic emphasis
- **R2.1.3** Converted files are saved alongside originals as `.md` files for version control
- **R2.1.4** The converter must be idempotent — re-running on the same `.docx` produces identical `.md` output

### R2.2 Stage 1: Summarize & Classify
- **R2.2.1** Parse raw weekly report content (one report per team member per week)
- **R2.2.2** Classify each update block to exactly one canonical business area using mapping rules derived from `business_areas_master.md`
- **R2.2.3** Match updates to specific active projects listed in `business_active_projects_master.md`
- **R2.2.4** Resolve person names to canonical identifiers using `master_team_roster.md`, with disambiguation by business area context
- **R2.2.5** Separate content into achievements (completed work) and focus areas (forward-looking work)
- **R2.2.6** Produce two output formats:
  - Executive summary (per-area bullet points for weekly distribution)
  - EVP highlights (3 achievements + 3-4 focus areas for senior leadership)
- **R2.2.7** Remove duplicates from prior week's report
- **R2.2.8** All mapping data (business area aliases, project lists, person rosters) must be read from master markdown files at runtime — not hardcoded

### R2.3 Stage 2: Propagate to Entities
- **R2.3.1** Parse the tagged weekly summary to extract per-entity updates
- **R2.3.2** Update person overview files: append weekly tracking entry, update active project list
- **R2.3.3** Update project overview files: update delivery status, add milestones, append weekly progress
- **R2.3.4** Update business area overview files: update current quarter narrative, cascade project status changes
- **R2.3.5** Generate a changelog summarizing all proposed edits with justification for each change
- **R2.3.6** Every wikilink created must resolve to an existing entity file (no orphan references)
- **R2.3.7** Status field changes must cite the source update that triggered the change
- **R2.3.8** All modified files must pass YAML frontmatter validation and wikilink syntax checks

### R2.4 Stage 3: PR Generation
- **R2.4.1** Create a feature branch named `weekly-update/YYYY-MM-DD`
- **R2.4.2** Commit all new and modified files
- **R2.4.3** Include the changelog in the PR description
- **R2.4.4** Stage 1 output (weekly summary) is reviewed and approved separately from Stage 2 entity updates
- **R2.4.5** Stage 2 entity updates may be split into multiple smaller PRs for manageable review

---

## R3. Agent System Requirements

### R3.1 Agent Roles

Three agents collaborate to execute the pipeline:

#### R3.1.1 Planner Agent
- Analyzes the current state of the knowledge base and incoming weekly reports
- Produces a structured plan specifying: which files to create/modify, what content to extract, which entities are affected
- Saves plans as Markdown files in `knowledge/prompts/plans/`
- Iterates with the Validator until the plan meets all requirements
- Must reference the DESIGN_DOC.md and current requirements when producing plans

#### R3.1.2 Validator Agent
- Reviews Planner output against DESIGN_DOC.md requirements and user instructions
- Checks for: completeness (all entities covered), consistency (no conflicting updates), compliance (meets formatting and linking conventions)
- Documents any gaps or requirement clarifications in `knowledge/prompts/requirements/`
- Returns structured feedback to the Planner with specific pass/fail verdicts per requirement
- Must validate that all proposed wikilinks resolve and all YAML frontmatter is well-formed

#### R3.1.3 Executor Agent
- Takes the validated plan and produces outputs:
  - **Prompt files** (`.prompt.md`) saved to `knowledge/prompts/prompts/`
  - **Python code** saved to `knowledge/prompts/code/`
- All Python code execution must be logged (input, output, errors)
- Executor does not make architectural decisions — it implements exactly what the validated plan specifies
- Must follow existing conventions (wikilink syntax, YAML frontmatter structure, file naming)

### R3.2 Agent Interaction Protocol
1. **Planner** reads the knowledge base state + incoming data → produces a plan
2. **Validator** reviews the plan against requirements → returns pass/fail with feedback
3. If fail: **Planner** revises the plan based on feedback → re-submits to Validator
4. If pass: **Executor** implements the plan → produces code and/or prompt files
5. **Validator** reviews Executor output for correctness → final approval or revision request

### R3.3 Artifact Storage

| Artifact | Location | Format |
|----------|----------|--------|
| Plans | `knowledge/prompts/plans/` | Markdown |
| Requirements & feedback | `knowledge/prompts/requirements/` | Markdown |
| Prompt definitions | `knowledge/prompts/prompts/` | `.prompt.md` |
| Python code | `knowledge/prompts/code/` | `.py` |
| Execution logs | `knowledge/prompts/code/logs/` | `.log` or `.md` |

---

## R4. Content & Formatting Requirements

### R4.1 Executive Summary Style (Stage 1 — INSTRUCT_BASE)
- **R4.1.1** Each business area gets one bullet point
- **R4.1.2** Format: `**[Business Area]:** accomplishments then *ongoing work*`
- **R4.1.3** Accomplishments: 2-3 sentences with strategic context
- **R4.1.4** Ongoing work: 1 sentence, italicized, no strategic context needed
- **R4.1.5** No team member names — use "Team" collectively
- **R4.1.6** No mention of "OKRs" — describe the actual objectives being addressed
- **R4.1.7** Pithy, executive-grade language — no fluffy phrasing
- **R4.1.8** Dollar amounts must be exact
- **R4.1.9** Alphabetical ordering by business area name
- **R4.1.10** No projects mentioned that aren't in the weekly reports
- **R4.1.11** Areas with no updates get "No Relevant Update"

### R4.2 EVP Highlights Style (Stage 1 — INSTRUCT_HIGHLIGHTS)
- **R4.2.1** Section 1: Exactly 3 "Key AI Achievements" — tangible outcomes, not activities
- **R4.2.2** Section 2: Exactly 3-4 "Focus Areas" — forward momentum, not work-in-progress
- **R4.2.3** Headlines start with a noun or outcome, not a verb
- **R4.2.4** Headlines must be understandable without acronyms
- **R4.2.5** Each headline followed by 1 tight explanatory sentence
- **R4.2.6** No team names, no activity logs, no concerns/blockers
- **R4.2.7** Must be copy-paste ready for executive distribution
- **R4.2.8** Must read as outcomes, not activities — an EVP should understand in under 30 seconds

### R4.3 Entity File Formatting
- **R4.3.1** All entity overview files must have YAML frontmatter with `tags` array
- **R4.3.2** All cross-references use Obsidian wikilink syntax: `[[path/to/note|Display Name]]`
- **R4.3.3** File and folder names are lowercase with underscores or hyphens
- **R4.3.4** Project tracking tables use consistent column headers across all entity types
- **R4.3.5** Invalid characters in wikilinks: `# | ^ : %% [[ ]]` (per wikilink_conventions.md)

---

## R5. Business Area Classification Requirements

### R5.1 Canonical Business Areas
The following 17 areas are the valid classification targets:

1. PCP Pricing Automation (RCI/CEL)
2. Revenue Management Automation (RCI)
3. Revenue Management Automation (CEL)
4. Revenue Management Automation (SSC)
5. PROPEL Targeted Offers (CEL)
6. Contact Center Optimization & Automation (RCI/CEL)
7. AXIOM: Generative-AI SEATs (Hotel Ops, Consumer Insights, Legal)
8. Marine Insights Analytics Platform (Marine Operations)
9. Supply Chain Optimization
10. Win-on-Waste (Hotel Operations)
11. Customer Lifetime Value (Corporate Planning)
12. Customer Targeting (E-Commerce)
13. Hybris Product Recommendations (Digital)
14. Loyalty Program Redesign
15. RoyalOne Community (Digital)
16. NewBuild
17. HR

### R5.2 Classification Rules
- **R5.2.1** Each update block maps to exactly one business area
- **R5.2.2** The business area is typically stated before the first `:` in each update block
- **R5.2.3** If a person is mentioned, their typical business area association provides context but the actual content determines classification
- **R5.2.4** If no category matches, classify as "Unclassified"
- **R5.2.5** Each business area has associated: strategic goal, OKR, team members, and active projects (defined in master files)
- **R5.2.6** Classification mappings must be maintained in `business_areas_master.md` and read at runtime

---

## R6. Validation & Quality Requirements

### R6.1 Structural Validation
- **R6.1.1** All `.md` files with frontmatter must have parseable YAML
- **R6.1.2** All wikilinks must resolve to existing files in the knowledge base
- **R6.1.3** No entity file may have empty required fields (tags, status, leader for people)
- **R6.1.4** Person files must reference only projects in `business_active_projects_master.md`
- **R6.1.5** Each weekly cycle PR must include a changelog file

### R6.2 Content Validation
- **R6.2.1** No team member names in executive summaries — only "Team"
- **R6.2.2** No duplicate content from prior week's report
- **R6.2.3** All dollar amounts carried forward accurately
- **R6.2.4** Status changes must be justified by source weekly update text

### R6.3 Pipeline Validation
- **R6.3.1** Converter must be idempotent
- **R6.3.2** Pipeline must not modify files outside `knowledge/` and `reporting/`
- **R6.3.3** All Python code execution must produce logs
- **R6.3.4** Failed pipeline runs must not leave partial/corrupt state

---

## R7. Open Requirements (Pending Decision)

| ID | Question | Current Status |
|----|----------|----------------|
| R7.1 | Rolling window or archival strategy for entity tracking tables | Retain everything for now; revisit when file sizes become unwieldy |
| R7.2 | CODEOWNERS mapping for business area review routing | TBD — define per-area reviewers |
| R7.3 | Execution engine selection (Azure OpenAI, Databricks FM, VS Code Copilot) | TBD — evaluate cost and automation profiles |
| R7.4 | Input format migration timeline | `.docx` → Markdown accepted; converter bridges the gap |
