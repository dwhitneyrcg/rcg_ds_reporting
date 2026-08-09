# Design Document: LLM-Managed Wiki for Data Science Team

**Author:** David Whitney
**Date:** May 10, 2026
**Status:** Draft v2
**Repository:** `rcg_ds_reporting`
**Supersedes:** `DESIGN_DOC.md` (April 19, 2026)

---

## 0. Change Summary from Prior Design

| Area | Prior Design | This Design | Rationale |
|------|-------------|-------------|-----------|
| Schema layer | Implicit (scattered conventions) | Explicit AGENTS.md hierarchy | Adopts the open standard; any agent can read it |
| Entity discovery | Python code held entity lists | Python reads wiki master files at runtime | Eliminates drift between code and wiki (Constraint 4) |
| Initial bootstrap | LLM-driven ad-hoc extraction | Deterministic Python extraction + LLM enrichment | Reproducible first pass; LLM only fills judgment gaps |
| Agent framework | Planner/Validator/Executor (soft) | Planner/Validator/Executor with hard gates | Validator rejects by default unless all checks pass |
| Business hierarchy | 17 fixed "business areas" | Generic Program/Project two-tier model | Reusable across teams with different vocabulary |
| LLM usage in code | LLM generated and maintained Python | Reusable Python utilities; LLM does content only | Minimizes LLM-generated code drift (Constraint 3) |
| Purpose/direction | Implicit in design doc | Explicit `purpose.md` file | Borrowed from nashsu/llm_wiki pattern |

---

## 1. Purpose

Build and maintain a persistent, compounding, interlinked markdown wiki that tracks the Data Science organization's people, programs, projects, OKRs, repositories, and weekly progress. The wiki is the compiled knowledge layer between raw sources and human consumers -- following Karpathy's LLM Wiki pattern where the LLM writes and maintains all content, and humans curate sources, ask questions, and review.

### 1.1 What This Is

An internal team wiki maintained by LLM agents, fed by weekly reports, meeting notes, and project documents. Humans remain in the loop through PR review. The wiki stays current because the LLM does the maintenance that no one on the team has time for.

### 1.2 What This Is Not

- Not a RAG system (knowledge is compiled, not re-derived per query)
- Not a static documentation site (every page is a living document)
- Not a replacement for human judgment (the LLM proposes; humans approve)

---

## 2. Design Principles

| # | Principle | Rationale |
|---|-----------|-----------|
| P1 | **Wiki as persistent artifact** | Knowledge compounds over time. Cross-references, contradictions, and synthesis are built once and kept current -- not re-derived on every query. (Karpathy: "the wiki is a persistent, compounding artifact") |
| P2 | **Three-layer architecture** | Raw sources (immutable) -> Wiki (LLM-maintained) -> Schema/AGENTS.md (co-evolved). Clear ownership at each layer. |
| P3 | **PR-gated ingestion** | Every knowledge update flows through a code commit and PR review. Traceability, rollback, and human validation. |
| P4 | **Wiki is the single source of truth for entities** | Python code, prompts, and agents read entity lists from wiki master files at runtime. Never hardcode names, projects, or business areas in Python functions or prompt files. If the wiki does not list it, it does not exist. |
| P5 | **Separation of deterministic and generative work** | Python handles parsing, validation, diffing, wikilink checking. LLMs handle summarization, classification, narrative synthesis. Each does what it is best at. |
| P6 | **Two-step ingest** | Analyze first (what entities are affected, what changed), generate second (write/update wiki pages). This prevents false certainty from one-shot ingestion. (Borrowed from nashsu/llm_wiki) |
| P7 | **Programs and projects are generic containers** | The hierarchy is "Program > Project" with configurable labels. One team's "Business Area" is another's "Pillar" or "Function". The architecture does not assume a fixed vocabulary. |
| P8 | **Agents do not rubber-stamp** | The Validator rejects by default. Every check must explicitly pass. If ambiguous, the Validator flags for human review rather than approving. |

---

## 3. Architecture

### 3.1 The Three Layers (Karpathy Model Adapted)

```
+------------------------------------------------------------------+
|                          LAYER 3: SCHEMA                          |
|                                                                   |
|  AGENTS.md (root)        purpose.md        conventions/           |
|  Tells agents HOW        Tells agents WHY   Tells agents WHAT     |
|  to operate              the wiki exists     standards to follow   |
|                                                                   |
+------------------------------------------------------------------+
|                          LAYER 2: WIKI                            |
|                                                                   |
|  people/     programs/     okrs/     repositories/    reporting/  |
|  Entity pages maintained by LLM pipeline                          |
|  Interlinked with wikilinks, YAML frontmatter, tracking tables    |
|                                                                   |
+------------------------------------------------------------------+
|                       LAYER 1: RAW SOURCES                        |
|                                                                   |
|  reporting/weekly_updates_raw/     (immutable .docx inputs)       |
|  reporting/weekly_updates_raw_md/  (deterministic .md conversions)|
|  Any future source: Slack exports, meeting transcripts, etc.      |
|                                                                   |
+------------------------------------------------------------------+
```

**Layer 1 (Raw Sources)** is immutable. The LLM reads from it but never modifies it. These are the source of truth for what was actually said.

**Layer 2 (Wiki)** is LLM-maintained. The LLM creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent. Humans read it; the pipeline writes it.

**Layer 3 (Schema)** is co-evolved by human and LLM. It tells agents how the wiki is structured, what the conventions are, and what workflows to follow. This is the key configuration layer.

### 3.2 AGENTS.md Hierarchy

Adopting the [AGENTS.md](https://agents.md/) open standard. The closest AGENTS.md to the edited file takes precedence.

```
rcg_ds_reporting/
  AGENTS.md                           # Root: repo-level build, test, conventions
  knowledge/
    AGENTS.md                         # Wiki-level: entity conventions, linking rules
    tools/
      AGENTS.md                       # Pipeline-level: how to run the pipeline
      agents/
        kb-planner.agent.md           # Planner agent definition
        kb-validator.agent.md         # Validator agent definition
        kb-executor.agent.md          # Executor agent definition
```

**Root AGENTS.md** contains:
- Python environment setup (`requirements.txt`, venv activation)
- Test commands (`python -m pytest tests/`)
- Global conventions (encoding rules, file naming, no hardcoded entities)
- Security: no credentials in committed files

**knowledge/AGENTS.md** contains:
- Wiki structure and entity types
- YAML frontmatter requirements
- Wikilink syntax rules (referencing `conventions/wiki_links/`)
- Master file locations (the canonical sources for entity lookups)
- Naming conventions for folders and files

**knowledge/tools/AGENTS.md** contains:
- Pipeline execution sequence
- Python script inventory and usage
- Prompt file inventory
- Agent workflow (Planner -> Validator -> Executor)
- Output locations for each artifact type

### 3.3 purpose.md

A dedicated file at `knowledge/purpose.md` that explains why the wiki exists. This gives agents a compass for judging what knowledge is worth preserving.

```markdown
# Purpose

This wiki exists to help the Data Science team:

1. Track weekly progress across all programs and projects
2. Maintain living documentation of every team member's contributions
3. Generate executive summaries and EVP highlights from raw reports
4. Preserve institutional knowledge that would otherwise exist only
   in chat history or individual memory
5. Provide context for the next week's report generation, creating
   a compounding knowledge feedback loop

The intended consumers are:
- DS leadership (weekly summaries, program status)
- Individual contributors (their own project history, cross-team context)
- New team members (onboarding context)
- LLM agents (context for generating future reports)
```

---

## 4. Knowledge Base Structure

### 4.1 Directory Layout

```
knowledge/
  purpose.md                              # Why this wiki exists
  AGENTS.md                               # Wiki-level agent instructions
  knowledge_context.md                    # Base path and global context
  index.md                                # Wiki-wide page catalog (NEW)
  log.md                                  # Chronological operation log (NEW)
  conventions/
    wiki_links/
      wikilink_conventions.md             # Linking standards
    naming/
      naming_conventions.md               # Folder/file naming rules (NEW)
  people/
    master_team_roster.md                 # Active/inactive team index
    <person_slug>/
      overview_<person_slug>.md           # Role, leader, programs, tracking
  programs/                               # RENAMED from biz_areas/
    programs_master.md                    # All programs index (RENAMED)
    active_projects_master.md             # All active projects index (RENAMED)
    <program_slug>/
      overview_<program_slug>.md          # Goal, impact, OKRs, team, status
      <project_slug>/
        overview_<project_slug>.md        # Project details, milestones, status
  okrs/                                   # Quarterly OKR tracking
  repositories/                           # Code repository documentation
    <system_slug>/
      OVERVIEW_<repo>.md
      DIAGRAM_<repo>.md
  reporting/
    weekly_updates_raw/                   # Source .docx files (IMMUTABLE)
    weekly_updates_raw_md/                # Deterministic .md conversions
    weekly_updates_summarized/            # LLM-generated summaries
    weekly_updates_summarized_md/         # Parsed summaries
    changelogs/                           # Per-cycle change summaries
  tools/                                  # Pipeline code, prompts, agents
    AGENTS.md                             # Pipeline-level agent instructions
    purpose.md                            # Pipeline purpose (optional)
    agents/                               # Agent definitions (.agent.md)
    code/                                 # Python utility scripts
      logs/                               # Execution logs
    prompts/                              # Prompt definitions (.prompt.md)
    reference/                            # Literature, prior versions
    requirements/                         # Requirements documents
    plans/                                # Planner output
```

### 4.2 Renaming: biz_areas -> programs

**Rationale:** The user's team thinks in terms of "programs" (a collection of related projects under a business sponsor) and "projects" (specific deliverables). The name "business areas" is too specific to one team's vocabulary and couples the architecture to a particular organizational structure.

**Generic model:**

| This Team's Term | Generic Term | Definition |
|-----------------|-------------|------------|
| Business Area | **Program** | A sustained capability or function with a business sponsor, strategic goal, and OKR targets. Contains one or more projects. |
| Project | **Project** | A discrete initiative with a defined scope, delivery timeline, and measurable outcome. Lives under exactly one program. |

**Why this matters for reusability:** Another team might call their programs "Pillars", "Functions", "Workstreams", or "Capabilities". The folder is called `programs/` but the display labels are configurable in `programs_master.md`. The Python code never assumes a specific name -- it reads whatever the master file contains.

**Migration path:** Rename `biz_areas/` to `programs/`, update all wikilinks. This is a one-time operation executed as a dedicated PR.

### 4.3 index.md and log.md (New)

Borrowed directly from Karpathy's LLM Wiki pattern:

**index.md** -- Content-oriented catalog of every page in the wiki. Organized by category (people, programs, projects, repositories). Each entry has a wikilink and a one-line summary. Updated on every ingest cycle. Agents read this first to find relevant pages.

**log.md** -- Chronological append-only record. Each entry uses a parseable prefix:

```markdown
## [2026-05-10] ingest | Weekly Report 2026-05-09
- 14 person files updated
- 6 project files updated
- 3 program files updated
- Changelog: [[reporting/changelogs/2026-05-10|2026-05-10]]

## [2026-05-10] lint | Weekly health check
- 2 orphan pages detected
- 1 broken wikilink found
- Review items created: 2
```

### 4.4 Entity File Conventions

All entity overview files follow a standard structure:

- **YAML frontmatter** with `tags`, `status`, `last_updated`, and entity-specific metadata
- **Obsidian wikilinks** (`[[path/to/note|Label]]`) for bidirectional navigation
- **Structured sections** for both static metadata and dynamic tracking tables
- **Canonical naming** -- folder and file names are lowercase, underscore-delimited

Linking conventions defined in `conventions/wiki_links/wikilink_conventions.md`.
Naming conventions defined in `conventions/naming/naming_conventions.md`.

### 4.5 Review Items (New)

Borrowed from nashsu/llm_wiki. A `review/` folder (or section within changelogs) for items that the pipeline cannot auto-decide:

- A new project mentioned in a weekly report that does not match any existing project
- A person name that cannot be resolved against the roster
- A status change that contradicts the prior week's status
- A classification that the LLM has low confidence on
- A metric or dollar amount that should be verified by a human

Review items are structured as individual markdown files:

```markdown
---
tags: [review]
status: open | resolved
created: 2026-05-10
source: weekly_update_2026-05-09.md
---

# Review: Unresolved person name "Alex H."

## Context
The weekly report for 2026-05-09 references "Alex H." in the
Contact Center section. The roster contains "Alexander Hu" but
no alias "Alex H." is registered.

## Suggested Resolution
Add alias "Alex H." -> "Alexander Hu" to master_team_roster.md

## Resolution
[To be filled by human reviewer]
```

---

## 5. The Program/Project Hierarchy -- Design Rationale

### 5.1 The Problem

The prior design used 17 hardcoded "business areas", each with a flat list of projects underneath. This created several issues:

1. **Vocabulary coupling** -- The label "business area" is meaningful only to this team. Another DS team might call the same concept a "pillar", "capability", or "workstream."
2. **Flat hierarchy** -- Some "projects" are really sub-projects of a larger initiative. There is no way to express that a program has phases or workstreams.
3. **Static list** -- The 17 areas were captured at a point in time. Programs get added, merged, sunset. The architecture should accommodate this naturally.
4. **Classification rigidity** -- The classification rules hardcoded 17 labels. When a new program appears, the classification rules must be manually updated.

### 5.2 The Solution: Two-Tier Generic Containers

```
programs/
  programs_master.md                    # Index of all programs
  active_projects_master.md             # Index of all active projects
  <program_slug>/
    overview_<program_slug>.md          # Program-level overview
    <project_slug>/
      overview_<project_slug>.md        # Project-level overview
```

**Program** = a sustained capability area with a business sponsor and strategic goal. Examples from this team: "Revenue Management Automation (RCI)", "Contact Center Optimization & Automation", "Supply Chain Optimization".

**Project** = a discrete deliverable under a program. Examples: "PRE 4.0", "Beverage Package Optimization", "Conversational IVR".

### 5.3 How Classification Works Without Hardcoding

The classification pipeline reads `programs_master.md` at runtime to get the list of valid programs. It reads each program's `overview_<program>.md` to get:
- Aliases (alternative names the program is known by in reports)
- Active project names
- Team members typically associated with this program

This means:
- Adding a new program = creating a folder + overview file + adding to `programs_master.md`
- No Python code changes required
- No prompt file changes required
- The classification adapts automatically on the next pipeline run

### 5.4 When a New Program or Project Appears

The pipeline should handle this as a **review item**, not an automatic creation:

1. During ingest, if an update references work that does not match any known program or project
2. The pipeline creates a review item: "Potential new program/project detected"
3. A human reviews and either:
   - Maps it to an existing program/project (adding an alias)
   - Approves creation of a new program/project (triggers entity file creation)
4. Only after human approval does the new entity enter the wiki

This prevents the wiki from accumulating phantom entities from mis-parsed reports.

### 5.5 Reusability for Other Teams

Another team adopting this system would:

1. Replace the contents of `programs_master.md` with their own programs
2. Create program folders with their own project structures
3. Update `purpose.md` to reflect their team's goals
4. The Python code, agent definitions, and pipeline scripts work unchanged

The architecture explicitly avoids coupling to any specific team's organizational vocabulary.

---

## 6. Pipeline Stages

### 6.1 High-Level Flow

```
+-----------------------------------------------------------------------+
|                         WEEKLY CYCLE                                    |
|                                                                        |
|  +----------+     +-------------+     +--------------+                 |
|  | Raw .docx| --> | Stage 0:    | --> | Stage 1a:    |                 |
|  | Reports  |     | DOCX to MD  |     | Parse & Tag  |                 |
|  | (Layer 1)|     | (Python)    |     | (Python)     |                 |
|  +----------+     +------+------+     +------+-------+                 |
|                          |                   |                          |
|                          v                   v                          |
|                   +------+------+     +------+-------+                 |
|                   | Raw .md     |     | Tagged .md   |                 |
|                   | (Layer 1)   |     | with YAML    |                 |
|                   +-------------+     +------+-------+                 |
|                                              |                          |
|                          +-------------------+-------------------+     |
|                          |                                       |     |
|                          v                                       v     |
|                   +------+-------+                       +------+--+   |
|                   | Stage 1b:    |                       | Stage 2: |   |
|                   | Summarize    |                       | Propagate|   |
|                   | (LLM)       |                       | to Wiki  |   |
|                   +--------------+                       | (LLM)   |   |
|                          |                               +----+----+   |
|                          v                                    |         |
|                   +--------------+                            v         |
|                   | Exec Summary |                    +-------+------+ |
|                   | EVP Highlights|                   | Entity edits | |
|                   +--------------+                    | + Changelog  | |
|                                                       +-------+------+ |
|                                                               |         |
|           +------+------+          +--------------+           |         |
|           | Stage 3:    | <--------| Stage 2      | <---------+         |
|           | Validate    |          | output files |                     |
|           | (Python)    |          +--------------+                     |
|           +------+------+                                               |
|                  |                                                       |
|                  v                                                       |
|           +------+------+                                               |
|           | PR Created  |                                               |
|           | for Review  |                                               |
|           +------+------+                                               |
|                  |                                                       |
|                  v                                                       |
|           +------+------+                                               |
|           | Human Review|                                               |
|           | & Merge     |                                               |
|           +------+------+                                               |
|                  |                                                       |
|                  v                                                       |
|           +------+----------+                                           |
|           | Updated Wiki    |----> Context for next week's Stage 1      |
|           | (Layer 2)       |                                           |
|           +-----------------+                                           |
+-----------------------------------------------------------------------+
```

### 6.2 Stage 0: DOCX to Markdown (Python -- Deterministic)

**Input:** Raw `.docx` files in `reporting/weekly_updates_raw/`
**Output:** `.md` files in `reporting/weekly_updates_raw_md/`
**Tool:** `code/batch_convert.py` wrapping `code/docx_to_markdown.py`

This is purely deterministic. No LLM involvement. The Python script:
1. Reads the `.docx` using `python-docx`
2. Converts paragraphs, tables, bold/italic to markdown
3. Splits embedded soft-returns into separate lines
4. Writes UTF-8 markdown with no YAML frontmatter
5. Idempotent: skips files that already have a `.md` counterpart

**No entity data in this script.** It is a format converter only.

### 6.3 Stage 1a: Parse & Tag (Python -- Deterministic)

**Input:** Raw `.md` from Stage 0
**Output:** Tagged `.md` with YAML frontmatter listing all entities
**Tool:** `code/parse_weekly_report.py`

**Data sources read at runtime (never hardcoded):**
- `people/master_team_roster.md` -- for name resolution
- `programs/programs_master.md` -- for program classification
- `programs/active_projects_master.md` -- for project matching

The Python script:
1. Splits the raw report into person-level blocks (using blank-line delimiters)
2. Resolves person names against the roster (with alias/nickname lookup)
3. Classifies each block to a program using text matching against program names and aliases
4. Matches updates to specific projects using the active projects list
5. Separates completed work from in-progress/next-steps
6. Outputs a structured tagged `.md` with YAML frontmatter

**Critical constraint:** The script contains ZERO hardcoded entity names. All entity lookups go through the master markdown files. If a name or program is not in the wiki, the script flags it as unresolved with a `[?]` marker and creates a review item.

**Name resolution strategy:**
- The script reads aliases from the roster file
- A nickname table (e.g., "Ben" -> "Benjamin Fowler") lives in `people/master_team_roster.md` as an aliases section, NOT in Python code
- Unresolved names create review items, not errors

### 6.4 Stage 1b: Summarize & Classify (LLM -- Generative)

**Input:** Tagged `.md` from Stage 1a + current wiki context
**Output:** Executive summary, EVP highlights
**Tools:** Prompt files consumed by LLM agent

This is where the LLM adds value that Python cannot:
1. Summarize updates into pithy executive language
2. Select the 3 most impactful achievements for EVP highlights
3. Synthesize multiple team members' updates on the same project into a unified narrative
4. Apply tone and style rules from `style_guide_executive.prompt.md`

The LLM reads:
- The tagged output from Stage 1a
- The prior week's executive summary (for deduplication)
- Program overview files (for strategic context)

**What the LLM does NOT do:**
- Parse raw reports (Python did that)
- Resolve names (Python did that)
- Classify to programs (Python did that)
- Generate Python code

### 6.5 Stage 2: Propagate to Wiki Entities (LLM -- Generative)

**Input:** Tagged `.md` from Stage 1a
**Context:** Current state of all entity files to be updated
**Output:** Modified entity files + changelog

The LLM:
1. Reads the tagged weekly summary
2. For each referenced **person**: updates their tracking table, active project list
3. For each referenced **project**: updates delivery status, milestones, tracking
4. For each referenced **program**: updates current status narrative
5. Generates a **changelog** with per-entity change tables and justifications

**Edit strategy:**

| Entity Type | What Gets Updated | How |
|-------------|-------------------|-----|
| Person overview | Weekly tracking table, active project list | Append row; add/remove project wikilinks |
| Project overview | Delivery status, milestones, weekly tracking | Update frontmatter status; append to logs |
| Program overview | Current quarter summary, project statuses | Update narrative; cascade project changes |

**Guardrails:**
- No orphan references -- every wikilink must resolve to an existing file
- No destructive overwrites without justification cited in changelog
- Status changes must cite the source text that triggered them
- New entities are flagged as review items, not auto-created

### 6.6 Stage 3: Validate & PR Preparation (Python -- Deterministic)

**Tool:** `code/validate_knowledge_base.py`

Automated checks (all Python, no LLM):
- All `.md` files with frontmatter have valid YAML
- All wikilinks resolve to existing files
- No required fields are empty (status, tags, last_updated)
- Person files reference only projects in `active_projects_master.md`
- Changelog file exists for the weekly cycle
- No files outside `knowledge/` were modified
- No duplicate tracking table entries (same week, same entity)

**Output:** Validation report + PR summary with change statistics

### 6.7 Stage 4: Lint (Python + LLM -- Periodic)

Not part of the weekly cycle but run periodically (e.g., monthly):

**Python checks:**
- Orphan pages (in wiki but not linked from any master file)
- Broken wikilinks (link target does not exist)
- Stale pages (not updated in > 4 weeks)
- Missing pages (referenced in master files but no file on disk)
- Duplicate tags or inconsistent frontmatter

**LLM checks:**
- Contradictions between pages
- Stale claims that newer sources have superseded
- Important concepts mentioned but lacking their own page
- Suggested new questions to investigate

---

## 7. Agent Framework

### 7.1 Architecture: Planner -> Validator -> Executor

```
+--------------------+
|    Human Input     |  (weekly report, ad-hoc request)
+---------+----------+
          |
          v
+---------+----------+       +-----------------------+
|   PLANNER AGENT    | <---> |    VALIDATOR AGENT     |
|                    |       |                        |
| - Reads wiki state |       | - Checks plan against  |
| - Analyzes input   |       |   requirements         |
| - Produces plan    |       | - REJECTS by default   |
| - Revises on       |       | - Returns PASS/FAIL    |
|   feedback         |       |   with actionable      |
|                    |       |   feedback             |
+---------+----------+       +-----------+-----------+
          |                               |
          | (validated plan)              |
          v                               |
+---------+----------+                    |
|   EXECUTOR AGENT   |                    |
|                    |                    |
| - Implements plan  | ---- output -----> |
| - Runs Python code |   (post-execution  |
| - Edits wiki files |    validation)     |
| - Logs all actions |                    |
+--------------------+                    |
                                          v
                              +-----------+-----------+
                              |   HUMAN REVIEWER      |
                              |   (PR review)         |
                              +-----------------------+
```

### 7.2 Anti-Rubber-Stamping Measures

The prior agent framework had the right structure but lacked mechanisms to prevent the Validator from becoming a formality. This design adds:

**1. Reject-by-default posture:** The Validator starts every review with FAIL and must find evidence to upgrade each check to PASS. This is the opposite of "scan for problems" -- it is "confirm every requirement is met."

**2. Specific, measurable checks (not subjective):**

| Check Category | Example Checks | Pass Criteria |
|---------------|---------------|---------------|
| Completeness | All entities in input accounted for in plan | Count matches |
| File paths | All paths match existing conventions | Regex validation |
| Wikilink syntax | All links use `[[path\|label]]` format | Pattern match |
| Entity existence | All referenced entities exist in master files | File-system check |
| No hardcoded data | Plan does not introduce entity literals in code | Code scan |
| Changelog coverage | Every proposed change has a changelog entry | Count matches |

**3. Separate pre-execution and post-execution validation:**
- Pre-execution: Validates the plan (does it make sense? does it follow conventions?)
- Post-execution: Validates the output (did the executor follow the plan? are files valid?)

**4. Escalation path:** If the Validator encounters ambiguity, it creates a review item for human judgment rather than making a judgment call itself.

### 7.3 Agent Definitions (AGENTS.md-Compatible)

Agent files live at `knowledge/tools/agents/` and use the VS Code `.agent.md` format for IDE integration. They also conform to AGENTS.md conventions for cross-platform compatibility.

**kb-planner.agent.md:**
- Tools: read, search, agent (can invoke validator), todo
- Reads wiki state, analyzes input, produces structured plans
- Plans saved to `knowledge/tools/plans/`
- Cannot create or edit wiki files directly

**kb-validator.agent.md:**
- Tools: read, search (read-only)
- Reviews plans and executor output against requirements
- Cannot modify plans or wiki files
- Returns structured PASS/FAIL report

**kb-executor.agent.md:**
- Tools: read, edit, search, execute, todo
- Implements exactly what the validated plan specifies
- Cannot make architectural decisions
- All actions logged to `knowledge/tools/code/logs/`

### 7.4 When the Agent Framework Might Fail

| Risk | Why It Could Fail | Mitigation |
|------|-------------------|------------|
| Validator approves bad plans | LLM may not catch semantic errors | Use Python for structural checks; reserve LLM for judgment calls |
| Planner produces plans that are too vague | "Update person files" is not actionable | Plan format requires specific file paths, section names, and content snippets |
| Executor deviates from plan | LLM may "improve" things | Post-execution validation compares output against plan |
| Circular revision loops | Planner and Validator disagree indefinitely | Max 3 revision cycles; escalate to human after that |
| Context window overflow | Wiki grows too large for a single LLM call | Agents read index.md first, then drill into specific files |
| Agent invocation overhead | Three agents per operation is slow | Only use full pipeline for weekly cycles; ad-hoc edits can skip planning |

---

## 8. Python Utility Layer

### 8.1 Design Philosophy

Python code is the **deterministic backbone** of the pipeline. It handles everything that does not require judgment:

| Python Does | LLM Does |
|------------|----------|
| DOCX to markdown conversion | Summarization and narrative synthesis |
| Report splitting into blocks | Classification confidence decisions |
| Name resolution against roster | Writing entity update prose |
| Wikilink syntax validation | Selecting EVP highlight achievements |
| YAML frontmatter validation | Generating changelog justifications |
| File diffing and change detection | Detecting contradictions |
| Orphan/broken link detection | Suggesting new pages to create |

### 8.2 Script Inventory

| Script | Stage | What It Does | Entity Data? |
|--------|-------|-------------|-------------|
| `batch_convert.py` | 0 | Orchestrates DOCX -> MD conversion | None |
| `docx_to_markdown.py` | 0 | Converts individual DOCX files | None |
| `parse_weekly_report.py` | 1a | Parses raw reports into tagged blocks | Reads from wiki master files at runtime |
| `deduplicate_updates.py` | 1b | Removes duplicate content vs. prior week | None (text comparison only) |
| `validate_knowledge_base.py` | 3 | Validates wiki structural integrity | Reads from wiki master files at runtime |
| `generate_changelog.py` | 2 | Generates changelog from entity diffs | Reads from wiki entity files at runtime |
| `generate_pr_summary.py` | 3 | Produces PR description | Reads from changelog |

### 8.3 The "No Hardcoded Entities" Rule

This is the single most important constraint on the Python layer. It is stated explicitly because prior implementations violated it:

**RULE:** No Python file may contain any of the following as string literals:
- Person names (e.g., `"Benjamin Fowler"`)
- Program names (e.g., `"Revenue Management Automation (RCI)"`)
- Project names (e.g., `"PRE 4.0"`)
- Business department names
- OKR text
- Team structure information

**WHERE THIS DATA LIVES:** In wiki markdown files (master roster, programs master, active projects master). Python reads these files at runtime via parsing functions.

**EXCEPTION:** A nickname/alias table for name resolution MAY exist, but it MUST live in `people/master_team_roster.md` as a structured section (e.g., an Aliases table), not in Python code. The Python script reads the alias table from the markdown file.

**WHY:** When entity data is embedded in Python, it drifts from the wiki. The Python says one thing; the wiki says another. The wiki is the single source of truth. The Python is a pipeline tool that reads from the source of truth.

**VALIDATION:** `validate_knowledge_base.py` should include a check that scans all `.py` files in `tools/code/` for potential hardcoded entity names by comparing against the current roster and program list. This is a lint rule, not a hard gate, because some string matches may be coincidental.

---

## 9. Initial Bootstrap Process

### 9.1 The Cold-Start Problem

When the wiki is first created, there are no master files to read from. The pipeline depends on files that do not yet exist. The bootstrap process creates these files.

### 9.2 Bootstrap Stages

**Stage B1: Extract entities from raw sources (Python)**

Use Python to scan all historical `.docx` reports and extract:
- Every unique person name mentioned
- Every unique program/business area label mentioned
- Every unique project name mentioned

This produces three plain-text lists. No wiki files yet.

**Tool:** A dedicated `bootstrap_extract.py` script that:
1. Reads all `.docx` files in `reporting/weekly_updates_raw/`
2. Splits each into blocks using the same heuristics as `parse_weekly_report.py`
3. Extracts candidate person names (first line of each block)
4. Extracts candidate program names (text before first `:` on line 2)
5. Extracts candidate project names (text after first `:` on line 2)
6. Deduplicates and outputs sorted lists to `tools/plans/bootstrap_entities.md`

**Stage B2: Human review of extracted entities**

A human reviews `bootstrap_entities.md` and:
- Merges duplicates (e.g., "MIAP" and "Marine Insights Analytics Platform")
- Assigns canonical names
- Maps nicknames to full names
- Marks any entities to exclude

**Stage B3: Create master files (Python)**

A `bootstrap_create_masters.py` script reads the reviewed entity list and creates:
- `people/master_team_roster.md` with wikilinks for each person
- `programs/programs_master.md` with wikilinks for each program
- `programs/active_projects_master.md` with projects grouped by program

**Stage B4: Create entity files (LLM)**

The LLM reads the master files and the original `.docx` reports to create:
- One overview file per person (`people/<slug>/overview_<slug>.md`)
- One overview file per program (`programs/<slug>/overview_<slug>.md`)
- One overview file per project (`programs/<slug>/<project_slug>/overview_<project_slug>.md`)

The LLM uses the prompt templates in `tools/prompts/build_business_areas_and_projects.prompt.md` to populate these files with content from the raw reports.

**Stage B5: Create index.md and log.md**

The LLM (or Python) creates `index.md` cataloging all pages, and `log.md` recording the bootstrap operation.

### 9.3 Bootstrap vs. Steady-State

| Aspect | Bootstrap | Steady-State |
|--------|-----------|-------------|
| Entity source | Raw `.docx` files | Wiki master files |
| Entity creation | Human-reviewed extraction | Review items from pipeline |
| Content source | Historical reports | Current week's report |
| Validation | Manual spot-check | Automated `validate_knowledge_base.py` |
| LLM role | Populate entity files with historical content | Update entity files with incremental changes |

---

## 10. Weekly Cycle Runbook

### 10.1 Sequence

```
1. Receive raw .docx report
2. Stage 0: batch_convert.py --> raw .md
3. Stage 1a: parse_weekly_report.py --> tagged .md
4. Stage 1b: LLM summarize (exec summary + EVP highlights)
5. Stage 2: LLM propagate to entities + generate changelog
6. Stage 3: validate_knowledge_base.py --> validation report
7. Generate PR summary
8. Create branch: weekly-update/YYYY-MM-DD
9. Commit all changes
10. Open PR for human review
11. Human reviews changelog, spot-checks diffs
12. Merge --> wiki updated
13. Update index.md and log.md
```

### 10.2 Variables

```powershell
$REPORT_DATE = "YYYY-MM-DD"
$ROOT = "C:\Users\133486\OneDrive - Royal Caribbean Group\LocalDatabricks\rcg_ds_reporting"
$TOOLS = "$ROOT\knowledge\tools"
$CODE = "$TOOLS\code"
$PYTHON = "$ROOT\.venv\Scripts\python.exe"
```

### 10.3 Error Handling

| Error | Action |
|-------|--------|
| Stage 0 fails (DOCX parsing) | Manual DOCX cleanup, retry |
| Stage 1a: unresolved person name | Review item created; pipeline continues with `[?]` marker |
| Stage 1a: unresolved program | Review item created; update classified as "Unclassified" |
| Stage 1b: LLM produces poor summary | Human edits summary before Stage 2 |
| Stage 2: LLM creates orphan wikilink | Caught by Stage 3 validation |
| Stage 3: validation fails | PR blocked until issues resolved |

---

## 11. Changelog and PR Review

### 11.1 Changelog Format

Each weekly cycle produces `reporting/changelogs/YYYY-MM-DD.md`:

```markdown
# Weekly Knowledge Update -- YYYY-MM-DD

## Summary
- X person files updated
- Y project files updated
- Z program files updated
- N review items created

## Changes by Entity

### People
- **Person A** -- Added weekly tracking entry for Program X (Project Y, Project Z)

### Projects
- **Project A** -- Status changed: "In Development" -> "UAT".
  Source: "Project A entered user acceptance testing this week"

### Programs
- **Program A** -- Updated Q2 progress narrative

## Review Items
- [Unresolved name] "Alex H." in Contact Center section
- [New project?] "Fare Integrity Monitor" not in active projects list
```

### 11.2 PR Review Process

| Reviewer Role | Reviews | Focus |
|---------------|---------|-------|
| Pipeline owner | Changelog + spot-check diffs | Factual accuracy, no regressions |
| Program lead (optional) | Their program's diffs only | Domain accuracy |
| Automated (CI) | All modified files | YAML, wikilinks, required fields, orphans |

### 11.3 Branch Strategy

```
weekly-update/YYYY-MM-DD
```

Contains: new tagged summary, modified entity files, changelog, updated index.md and log.md.

---

## 12. Prompt Architecture

### 12.1 Prompt File Format

All prompts are markdown files with YAML frontmatter:

```markdown
---
name: prompt_identifier
description: >
  What this prompt does
stage: step1 | step2 | shared
inputs:
  - input_name: "Description of input"
output: "Description of expected output"
---

## System Instructions
...

## Rules
...

## Output Format
...
```

### 12.2 Prompt Inventory

| File | Stage | LLM Role |
|------|-------|----------|
| `executive_summary.prompt.md` | 1b | Summarize weekly updates per program |
| `evp_highlights.prompt.md` | 1b | Select top achievements + focus areas |
| `classification_rules.prompt.md` | 1b | Disambiguate program classification (fallback) |
| `style_guide_executive.prompt.md` | 1b | Tone and formatting rules |
| `update_person_entity.prompt.md` | 2 | Update person overview files |
| `update_project_entity.prompt.md` | 2 | Update project overview files |
| `update_program_entity.prompt.md` | 2 | Update program overview files |
| `deduplicate_updates.prompt.md` | 1b | Remove duplicate content vs. prior week |
| `generate_changelog.prompt.md` | 2 | Generate changelog with justifications |
| `build_business_areas_and_projects.prompt.md` | bootstrap | Entity creation templates |

### 12.3 How Prompts Avoid Hardcoded Data

Every prompt that references entities uses template variables that are filled at runtime by reading wiki master files:

```markdown
## Classification Rules

Read the current program list from `programs/programs_master.md`.
For each program, read its overview file to get aliases and project lists.

DO NOT assume any fixed list of programs. The wiki is the source of truth.
```

No prompt file contains a numbered list of program names. If the wiki changes, the prompts automatically reflect the change.

---

## 13. Operations Beyond Weekly Ingest

### 13.1 Query

Users can ask questions against the wiki. The agent:
1. Reads `index.md` to find relevant pages
2. Reads the relevant pages
3. Synthesizes an answer with wikilink citations
4. Optionally files the answer back into the wiki as a new page

Example queries:
- "What has the Contact Center team delivered this quarter?"
- "Which projects is Camila Aichele working on?"
- "What is the current status of PRE 4.0?"

### 13.2 Lint

Periodic health check (see Stage 4 above). Produces a lint report and optionally creates review items for issues found.

### 13.3 Ad-Hoc Entity Updates

Not every update comes through the weekly report pipeline. Sometimes:
- A new team member joins (add to roster + create person file)
- A project is completed (update status + move to completed section)
- OKRs change (update program overview)

These follow a simplified flow: human provides the update -> Executor creates/edits files -> Validator checks -> PR review. No Planner needed for simple entity CRUD.

---

## 14. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| LLM makes incorrect entity edits | High (early) | Medium | PR gate + changelog + validation + review items |
| PR review becomes rubber-stamp | Medium | High | Changelog summaries; scoped reviews; CI validation |
| Classification misses new program | Medium | Medium | Review items for unmatched updates; periodic lint |
| Entity data drifts from code | Previously High | High | **Eliminated by design** -- code reads from wiki |
| Wiki grows too large for LLM context | Medium | Medium | index.md navigation; drill-into specific files; future: search tool |
| Bootstrap extracts wrong entities | Medium | Medium | Human review stage (B2) before wiki creation |
| Cascading errors (Stage 1 -> Stage 2) | Medium | High | Stage 1 output reviewed before Stage 2; two-PR option |
| DOCX parsing fragility | Low | Medium | Migrate to markdown/form input over time |
| Single reviewer bottleneck | High | Medium | Delegate program-level reviews; invest in CI |
| Agents produce inconsistent formatting | Medium | Low | Templates in prompts; validation in Stage 3 |

---

## 15. Implementation Phases

### Phase 0: Migration (New)
- [ ] Rename `biz_areas/` to `programs/` with wikilink updates
- [ ] Create `purpose.md`
- [ ] Create `index.md` and `log.md`
- [ ] Create AGENTS.md hierarchy (root, knowledge/, tools/)
- [ ] Move alias/nickname table from Python to `master_team_roster.md`
- [ ] Create `conventions/naming/naming_conventions.md`
- [ ] Add hardcoded-entity lint check to `validate_knowledge_base.py`

### Phase 1: Foundation (Complete -- from prior design)
- [x] Knowledge base structure (people, programs, projects)
- [x] Master index files with wikilinks
- [x] Weekly report parsing (`parse_weekly_report.py`)
- [x] AI prompt definitions for Stage 1
- [x] Prompts converted from `.docx` to `.prompt.md`

### Phase 2: Full Pipeline (Complete -- from prior design)
- [x] Stage 0: Batch DOCX -> MD conversion
- [x] Stage 1: Parse, tag, deduplicate
- [x] Stage 2: Entity update prompts + changelog generation
- [x] Stage 3: Validation + PR summary generation

### Phase 3: Hardening (New)
- [ ] Run pipeline on 3 historical weekly cycles end-to-end
- [ ] Verify no hardcoded entities in any `.py` file
- [ ] Verify all prompts read from wiki master files
- [ ] Review and tighten Validator checks
- [ ] Create bootstrap scripts (`bootstrap_extract.py`, `bootstrap_create_masters.py`)
- [ ] Write integration tests for each pipeline stage

### Phase 4: Automation & CI
- [ ] Automate branch creation and PR generation
- [ ] Add CI validation checks (pre-merge)
- [ ] Implement scoped review routing by program
- [ ] Build diff preview for PR descriptions
- [ ] Add Stage 4 lint as scheduled job

### Phase 5: Scale & Extend
- [ ] Populate OKR tracking
- [ ] Add repository documentation pipeline
- [ ] Add non-DOCX source ingestion (Slack, meeting transcripts)
- [ ] Implement search tool (qmd or custom) when wiki exceeds ~200 pages
- [ ] Metrics: track review time, error rate, knowledge freshness
- [ ] Evaluate Databricks Foundation Models as execution engine

---

## 16. Pros and Cons of This Architecture

### 16.1 Pros

| Advantage | Detail |
|-----------|--------|
| **Knowledge compounds** | Every weekly cycle makes the wiki more complete. Cross-references and synthesis are built once, not re-derived. |
| **Auditable** | Every change goes through a PR. Full git history. Changelogs explain why. |
| **No entity drift** | Python reads from wiki, not from hardcoded lists. Adding a program requires zero code changes. |
| **Reusable across teams** | The Program/Project model and Python utilities are team-agnostic. Another team can adopt by changing content, not code. |
| **LLM does what it is good at** | Summarization, synthesis, narrative -- not parsing, validation, or file management. |
| **Python does what it is good at** | Deterministic, testable, reproducible. No LLM variability in structural operations. |
| **Three-agent separation** | Planning mistakes are caught before execution. Execution mistakes are caught before merge. |
| **Open standards** | AGENTS.md works with any agent platform. Markdown + YAML + wikilinks work with any editor. |

### 16.2 Cons

| Disadvantage | Detail | Mitigation |
|--------------|--------|------------|
| **Complexity** | Three agents, four pipeline stages, multiple file types. Steep learning curve for new maintainers. | Detailed runbook (Section 10); AGENTS.md files explain everything in-situ |
| **LLM cost** | Stages 1b and 2 require LLM calls per weekly cycle. At ~30 team members and 17 programs, this could be significant. | Prompt caching; batch similar updates; use cheaper models for routine updates |
| **Context window limits** | As the wiki grows, a single LLM call may not be able to hold all relevant context. | index.md as navigation layer; drill-into strategy; future: embedding-based search |
| **DOCX dependency** | The pipeline starts with DOCX, which is fragile to parse and opaque to diff. | Migrate to markdown or structured form input over time (Phase 5) |
| **Three-agent overhead** | Planner -> Validator -> Executor adds latency to every operation. | Use full pipeline only for weekly cycles; skip planning for simple CRUD |
| **Human review bottleneck** | One person reviewing all PRs will become overwhelmed. | Scoped reviews by program; invest in CI to catch structural issues |
| **Bootstrap effort** | Creating 100+ entity files from scratch is labor-intensive even with LLM help. | Bootstrap scripts automate extraction; human only reviews entity lists |
| **PR-gated = slower** | PR review adds delay between report ingestion and wiki update. | Most delay is acceptable (wiki updates are not time-critical); urgent fixes can bypass |

### 16.3 Key Trade-offs

**Accuracy vs. Speed:** The PR gate, validation, and review items all slow the pipeline down. But for a team knowledge base, accuracy matters more than speed. A wrong update to an entity file is worse than a delayed update.

**Automation vs. Control:** The pipeline could auto-merge if all validation checks pass. But the PR review keeps humans in the loop for judgment calls that validation cannot catch (factual accuracy, strategic context, tone).

**Generality vs. Specificity:** The Program/Project model is generic enough for any team but does not capture deep domain structure (e.g., "this project has three workstreams, each with milestones"). Adding a third tier (Program > Workstream > Project) is possible but adds complexity. Start with two tiers; add a third only if needed.

---

## 17. Open Questions

1. **Rename migration:** Should `biz_areas/` -> `programs/` happen as a big-bang PR or incremental migration? Big-bang is cleaner but riskier.

2. **Alias table format:** What is the best markdown format for storing person name aliases in `master_team_roster.md`? Options: YAML frontmatter, a dedicated `## Aliases` section with a table, or inline markers per person entry.

3. **Context window strategy:** When the wiki exceeds the LLM's context window, should we adopt embedding-based search (qmd), a summarization cascade, or a hierarchical context strategy? This is not urgent at ~200 pages but should be planned.

4. **Execution engine:** Azure OpenAI API vs. Databricks Foundation Models vs. VS Code Copilot skills? Each has different cost, latency, and automation profiles. Current implementation uses VS Code Copilot; scaling may require a headless API.

5. **Input format migration:** Can team members submit weekly updates as markdown instead of DOCX? This eliminates Stage 0 and reduces parsing fragility. Timeline and adoption barriers need assessment.

6. **Two-PR vs. one-PR per cycle:** Should Stage 1 output be merged before Stage 2 runs? Two PRs prevent cascading errors but add process overhead.

7. **Third tier:** If programs need workstreams/sub-programs, how should the folder hierarchy extend? `programs/<program>/<workstream>/<project>/` or a flat structure with tags?

---

## 18. Glossary

| Term | Definition |
|------|-----------|
| **Program** | A sustained capability or function with a business sponsor and strategic goal. Contains one or more projects. (Previously "Business Area") |
| **Project** | A discrete initiative with defined scope and timeline, living under one program. |
| **Entity** | Any wiki-tracked object: person, program, project, OKR, repository. |
| **Master file** | An index markdown file listing all entities of a type with wikilinks. The single source of truth for what entities exist. |
| **Review item** | A flagged issue requiring human judgment before the pipeline can proceed. |
| **Ingest** | Processing a new source document into the wiki (Stages 0-3). |
| **Lint** | A periodic health check of the wiki's structural integrity and content freshness. |
| **Bootstrap** | The initial creation of the wiki from historical raw sources. |
| **AGENTS.md** | The schema layer -- a markdown file telling LLM agents how to operate on the codebase. |
| **Tagged report** | The output of Stage 1a: a raw report annotated with resolved person names, program classifications, and project matches. |
| **Changelog** | A per-cycle summary of all entity changes with justifications, included in the PR. |

---

## Appendix A: AGENTS.md Template (Root)

```markdown
# AGENTS.md

## Project Overview
This repository maintains an LLM-managed wiki for the Data Science team.
The wiki tracks people, programs, projects, OKRs, and weekly progress.

## Setup
- Python 3.12+ required
- Install deps: `pip install -r requirements.txt`
- Activate venv: `.venv\Scripts\activate` (Windows)

## Key Commands
- Convert DOCX to MD: `python knowledge/tools/code/batch_convert.py <input_dir> <output_dir>`
- Parse weekly report: `python knowledge/tools/code/parse_weekly_report.py <raw.md> <tagged.md>`
- Validate wiki: `python knowledge/tools/code/validate_knowledge_base.py`

## Critical Conventions
- **No hardcoded entities.** All entity lookups read from wiki master files at runtime.
- **YAML frontmatter** on all entity overview files.
- **Wikilinks** for all cross-references: `[[path/to/note|Label]]`
- **Lowercase underscore naming** for all folders and files.
- **ASCII-safe content** -- see encoding rules in user memory.

## Agent Workflow
Use the Planner -> Validator -> Executor pipeline for all non-trivial changes.
See `knowledge/tools/agents/` for agent definitions.

## File Ownership
- `knowledge/` -- Wiki content. Modified only by the pipeline or approved PRs.
- `knowledge/tools/` -- Pipeline infrastructure. Modified by developers.
- `knowledge/reporting/weekly_updates_raw/` -- Immutable source files.
```

## Appendix B: Program Overview Template

```markdown
---
tags:
  - program
  - <program_slug>
status: active | completed | sunset
last_updated: YYYY-MM-DD
aliases:
  - "Alternative Name 1"
  - "Short Name"
---

# [Program Name]

## Strategic Goal
[Dollar-value impact target and strategic objective]

## Current OKR (Q# YYYY)
[Quarterly objectives and key results]

## Team Members
- [[people/<person>/overview_<person>|Name]] -- Role

## Active Projects
- [[programs/<program>/<project>/overview_<project>|Project Name]]

## Completed Projects
- [Listed with completion date]

## Current Status
[Updated weekly from pipeline]

## Weekly Tracking

| Week | Key Updates | Source |
|------|-------------|--------|
```

## Appendix C: Project Overview Template

```markdown
---
tags:
  - project
  - <program_slug>
  - <project_slug>
status: active | completed | on_hold
last_updated: YYYY-MM-DD
---

# [Project Name]

## Program
[[programs/<program>/overview_<program>|Program Name]]

## Overview
[What this project does]

## Goal
[Specific measurable objective]

## Impact
[Expected business value]

## Milestones
| Milestone | Target Date | Status | Actual Date |
|-----------|-------------|--------|-------------|

## Delivery Status
[Current phase]

## Weekly Tracking

| Week | Key Updates | Source |
|------|-------------|--------|
```

## Appendix D: Person Overview Template

```markdown
---
tags:
  - person
  - <person_slug>
status: active | inactive
last_updated: YYYY-MM-DD
aliases:
  - "Nickname"
  - "First Initial"
leader: <leader_slug>
---

# [Full Name]

## Role
[Title and responsibilities]

## Leader
[[people/<leader>/overview_<leader>|Leader Name]]

## Active Programs
- [[programs/<program>/overview_<program>|Program Name]]

## Active Projects
- [[programs/<program>/<project>/overview_<project>|Project Name]]

## Weekly Tracking

| Week | Program | Project | Key Updates | Source |
|------|---------|---------|-------------|--------|
```
