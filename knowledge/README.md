# Knowledge Base — process flow

An auditable markdown wiki of the team's **people**, **projects**, and
**programs**, rebuilt from weekly reports through a pipeline where **nothing
reaches the wiki without a human approving it.**

- **program** — a broad, ongoing initiative (the container; e.g. *Revenue Management Automation*).
- **project** — a concrete deliverable inside one program (e.g. *Track Optimization*).
- **person** — a team member who works across projects/programs.

Entity templates: [pipeline/SCHEMA.md](pipeline/SCHEMA.md). Extraction rules the
agent follows: [pipeline/EXTRACT.md](pipeline/EXTRACT.md).

---

## The flow at a glance

Each box names **who does it**: 🧑 human · ⚙️ script (`kb.py`) · 🤖 Claude Code agent.

```
  ┌────────────────────────┐
  │ reporting/raw/*.docx    │  source weekly reports — segregated, READ-ONLY
  └───────────┬────────────┘
              │  ⚙️  kb.py parse                         (mechanical: docx → text)
              ▼
  ┌────────────────────────┐
  │ reporting/parsed/*.md   │  plain text, NO classification
  └───────────┬────────────┘
              │  🤖  agent follows EXTRACT.md            (the ONLY judgment step)
              │        reads parsed report + current indexes
              ▼
  ┌──────────────────────────────────────────────┐
  │ _staging/<cycle>/                              │  PROPOSED changes — not live
  │   proposed/{people,projects,programs}/…        │
  │   proposed/indexes/…                           │
  │   NOVELTY_REPORT.md   ◄── what a human reviews  │
  └───────────┬──────────────────────────────────┘
              │  ⚙️  kb.py validate                      (YAML + wikilinks must pass)
              │  🧑  read NOVELTY_REPORT.md  ◄── THE GATE
              │  ⚙️  kb.py accept <cycle>                (promote approved files)
              ▼
  ┌────────────────────────┐      ┌─────────────────────────────┐
  │ people/ projects/       │      │ reporting/changelogs/<cycle> │
  │ programs/ indexes/      │      │   .md  (audit trail)         │
  │   ← the live wiki       │      └─────────────────────────────┘
  └────────────────────────┘
              │
              └─► the updated wiki becomes the "current state" the agent reads
                  next week, so it knows what already exists (novel vs routine).
```

The loop is deliberately split so the **only** place machine judgment happens
(extraction) is sandwiched between a dumb mechanical parse and a human-gated
accept. The old pipeline did classification with 450 lines of regex and
misfiled updates silently — that is gone.

---

## Stage by stage (with the real 2026-04-24 run)

### 1. `parse` — docx → plain text  ·  ⚙️ script
```bash
python pipeline/kb.py parse reporting/raw
```
Converts each `.docx` to markdown text under `reporting/parsed/`. Formatting
only, **no classification**. Raw files are never modified.
> *2026-04-24:* one report → [reporting/parsed/20260424 - Weekly Matt and Rafeh Update.md](reporting/parsed/20260424%20-%20Weekly%20Matt%20and%20Rafeh%20Update.md).

### 2. `extract` — text → staged proposals  ·  🤖 agent
A Claude Code agent follows [pipeline/EXTRACT.md](pipeline/EXTRACT.md): it reads
the parsed report **and** the current `indexes/` (to know what already exists),
then writes proposed entity files into `_staging/<cycle>/proposed/` plus a
`NOVELTY_REPORT.md`. It classifies by **meaning**, not keyword overlap, and only
writes entities the report actually touches. Nothing here is live.
> *2026-04-24:* 13 programs + 13 projects + 2 index updates staged. People left
> empty — the report has no per-person attribution (flagged as Unresolved).

### 3. `validate` — structural safety check  ·  ⚙️ script
```bash
python pipeline/kb.py validate 2026-04-24
```
Fails the cycle if any staged entity has broken YAML frontmatter, a missing
required field (`type`, `name`, `status`), or a wikilink that resolves to
nothing in the wiki *or* the staged set (no orphans). Indexes are exempt from
frontmatter but their links are still checked.

### 4. Review the novelty report  ·  🧑 THE GATE
Open `_staging/<cycle>/NOVELTY_REPORT.md`. It sorts every proposal into:

| Section | Meaning | What you do |
|---------|---------|-------------|
| **NOVEL** | New entity, status change, new person↔project link, first-time dollar/deadline, or anything contradicting the wiki — each with the **source sentence**. | Scrutinize these. |
| **ROUTINE** | Appended progress, no status change. | Skim. |
| **Unresolved** | The agent couldn't classify it confidently. | Decide. |

> *2026-04-24:* cold start, so every entity was NEW. The report still
> singled out the items worth a closer look — e.g. Contact Center hitting
> `status: Live`, the HR sub-$750K/yr commitment + the stakeholder decision that
> narrowed scope, and the Rev-Mgmt methodology decision — each quoting the report.

### 5. `accept` — promote into the wiki  ·  ⚙️ script (only on your say-so)
```bash
python pipeline/kb.py accept 2026-04-24 --dry-run   # preview what lands
python pipeline/kb.py accept 2026-04-24             # promote everything
python pipeline/kb.py accept 2026-04-24 --only projects/cam_car_planning/overview_cam_car_planning.md
```
`accept` re-runs `validate` and **refuses if anything fails**, copies the
approved files into the live wiki, and appends `reporting/changelogs/<cycle>.md`.
Use `--only` to promote some proposals and hold others for revision.

---

## Directory layout

```
knowledge/
├── README.md                     ← you are here
├── people/    <slug>/overview_<slug>.md     live wiki
├── projects/  <slug>/overview_<slug>.md     live wiki
├── programs/  <slug>/overview_<slug>.md     live wiki
├── indexes/   {people,projects,programs}.md "what exists" — the agent's source of truth
├── reporting/
│   ├── raw/          source .docx weekly reports     (READ-ONLY input)
│   ├── parsed/       docx → text                     (kb.py parse output)
│   └── changelogs/   <cycle>.md per accepted cycle   (audit trail)
├── _staging/<cycle>/ proposed changes awaiting accept (the gate's holding area)
└── pipeline/
    ├── kb.py         the only code: parse · seed · validate · accept
    ├── EXTRACT.md    instructions the agent follows (step 2)
    ├── SCHEMA.md     entity frontmatter + section templates
    └── test_kb.py    self-check for the gate: `python pipeline/test_kb.py`
```

---

## Running a full weekly cycle

```bash
cd knowledge

# 1. mechanical parse
python pipeline/kb.py parse reporting/raw

# 2. extraction — in Claude Code, ask the agent to follow pipeline/EXTRACT.md
#    for the parsed report; it writes _staging/<cycle>/

# 3-4. check structure, then read the novelty report (the human gate)
python pipeline/kb.py validate <cycle>
#    open _staging/<cycle>/NOVELTY_REPORT.md

# 5. approve
python pipeline/kb.py accept <cycle>
```

## Seeding the baseline from a spreadsheet

Weekly reports carry *progress*, but a roster spreadsheet is the authoritative
source for *who and what exists*. Use `seed` to bootstrap (or re-baseline)
people, projects, and programs from one workbook — it's deterministic (no LLM)
and lands in the **same staging → validate → accept gate** as a weekly cycle.

```bash
# 1. get a blank template (3 tabs: programs, projects, people)
python pipeline/kb.py seed --template reporting/seed/roster_template.xlsx
#    fill it in (delete the "e.g." example rows or leave them — they're skipped)

# 2. stage proposals from the filled sheet
python pipeline/kb.py seed reporting/seed/roster.xlsx --cycle seed-initial
#    seed first validates the sheet's internal references (every project's
#    program, every person's projects/programs must exist) and refuses if not.

# 3. review, then promote through the normal gate
#    _staging/seed-initial/NOVELTY_REPORT.md shows NEW vs already-in-wiki, and
#    which wiki entities are NOT in the sheet (candidates to retire)
python pipeline/kb.py validate seed-initial
python pipeline/kb.py accept   seed-initial
```

Spreadsheet schema:

| Tab (in order) | Columns |
|-----|---------|
| `people` | `name`, `aliases`, `role`, `leader`, `status`, `programs` (`;`-sep), `projects` (`;`-sep) |
| `programs` | `program`, `aliases`, `status`, `goal` |
| `projects` | `project`, `aliases`, `program`, `status`, `summary` |

Slugs are derived from names automatically.

**Aliases (all three types)** are the mapping backbone. `aliases` is `;`-separated
(`RMA; Rev Mgmt`) and does double duty: it becomes the entity's Obsidian
`aliases:` frontmatter, **and** it is written into the index line as `(aka: …)`
so the index *is* the alias lookup table the weekly extract reads to map
shorthand in reports — `RMA`→Revenue Management Automation (program),
`PRE`→Pricing Recommendation Engine (project), `Will`→William (person). `seed`
warns if one alias is ambiguous (used by two entities of the same type), since
that would misroute the mapping. **Seed is the canonical baseline:
accepting it overwrites matching entities** (and replaces their progress-log
history) — so seed first, then run weekly extracts to layer progress on top.

## Design principles

- **One judgment step, fenced in.** Parse is dumb, accept is gated; only
  extraction reasons, and its output is staged for human review before it lands.
- **No regex classifier.** Classification is semantic (the agent), not
  word-overlap. The old approach misfiled silently; this surfaces uncertainty in
  the Unresolved section instead of guessing.
- **The wiki only changes via `accept`.** Raw reports are read-only; the agent
  only writes to `_staging/`. Every promotion leaves a changelog.
- **Indexes are the source of truth for "what exists,"** so the agent can tell a
  genuinely new entity (NOVEL) from a routine weekly update.
- **No new dependencies** beyond `python-docx` + `pyyaml` (already installed).
