# EXTRACT — weekly report → staged knowledge-base proposals

This is the **reasoning** step of the pipeline. A Claude Code agent (you)
follows it. There is intentionally **no regex classifier** — read the parsed
report and the current wiki, then use judgment. The old pipeline failed because
it tried to do this with word-overlap scoring; do not reintroduce that.

## Inputs

1. **One parsed weekly report** — `reporting/parsed/<file>.md` (plain text, no
   classification; produced by `kb.py parse`).
2. **Current wiki state** — the indexes are the source of truth for "what
   already exists":
   - `indexes/people.md`
   - `indexes/projects.md`
   - `indexes/programs.md`
   Read the individual `overview_*.md` files only for entities the report touches.

## Output

Write proposals into `_staging/<cycle>/` (cycle = the report date, `YYYY-MM-DD`):

```
_staging/<cycle>/
  proposed/
    people/<slug>/overview_<slug>.md      # only entities this report changes
    projects/<slug>/overview_<slug>.md
    programs/<slug>/overview_<slug>.md
  NOVELTY_REPORT.md                        # the human-in-the-loop summary
```

Write a proposed file **only for entities the report actually touches.** Never
restage an unchanged entity. For an entity that already exists, copy its current
overview from the wiki, apply the week's change, and save the full updated file
to staging (accept overwrites the live copy with this version).

Nothing here is live yet. A human reviews `NOVELTY_REPORT.md`, then runs
`kb.py accept <cycle>` (optionally `--only <relpath>`) to promote.

## Taxonomy

| Entity | Is | Slug example |
|--------|----|--------------|
| **program** | A broad, ongoing initiative or workstream (the container; replaces the old "business area"). | `revenue_management_automation` |
| **project** | A concrete deliverable inside one program. | `gty_lead_fare_optimization` |
| **person** | A team member. Works across one or more projects/programs. | `david_whitney` |

Slugs are lowercase, words joined by `_`, no spaces or `[ ] | # : %`
(see `conventions/wiki_links/wikilink_conventions.md`). A project lives under
exactly one program; record that link in its frontmatter.

## Entity templates

See `pipeline/SCHEMA.md` for the canonical frontmatter + section templates for
each type. Required frontmatter on every entity: `type`, `name`, `status`
(`kb.py validate` rejects the cycle if any is missing). Use Obsidian wikilinks
`[[path/to/overview|Label]]` for every cross-reference; every link must resolve
to a file that exists in the wiki or is staged in the same cycle (no orphans).

## Resolving names with aliases (read this first)

Reports use shorthand: "RMA" for Revenue Management Automation, "PRE" for
Pricing Recommendation Engine, "Will" for William. The three index files are
your **alias lookup table** — each line carries the canonical name plus known
aliases:

```
- [[programs/revenue_management_automation/overview_...|Revenue Management Automation]]  (aka: RMA, Rev Mgmt)
- [[people/william_borges/overview_...|William Borges]]  (aka: Will, Bill)
```

To resolve any name/abbreviation in the report:
1. Match it (case-insensitive) against canonical names **and** the `(aka: …)`
   aliases in the relevant index. A hit resolves to that entity's slug.
2. No hit → it is either a genuinely new entity (novel) or an unknown alias for
   an existing one. Decide from context; if unsure, put it in **Unresolved**.
3. **Learn aliases.** If the report clearly uses a new shorthand for an existing
   entity (e.g. text says "PRE (Pricing Recommendation Engine)"), add that
   shorthand to the entity's `aliases:` frontmatter **and** its index line. Treat
   this as a NOVEL change (a "new alias learned") so the human confirms it — this
   is how the alias map grows over time.

Aliases must stay unambiguous: never give the same alias to two entities of the
same type. If the report's shorthand could mean two things, flag it, don't pick.

## Classification — how to decide

1. **Program** — match the update's initiative to an existing program in
   `indexes/programs.md` (by name or alias, above). If none fits, it is a
   *new program* (novel). Do not force-fit; "no clear program" is valid.
2. **Project** — match to an existing project under that program. Prefer the
   project the text is actually about, not keyword overlap. New deliverable →
   *new project* (novel).
3. **People** — resolve names against `indexes/people.md` (canonical or alias).
   Disambiguate by program/project context (e.g. two "David"s on different
   programs). If a name is genuinely ambiguous or unknown, flag it.
4. **Achievements vs focus** — split by meaning, not by trigger words:
   - *Achievement* = something done/delivered this week (past tense, completed).
   - *Focus* = forward-looking / in-progress / next steps.
   A sentence that is clearly future work is focus even if it starts with an
   unusual verb. (The old regex only knew a fixed verb list — ignore that.)

## Novelty — what the human must approve

`NOVELTY_REPORT.md` separates changes a reviewer must scrutinize from routine
ones. Classify each proposed change:

**NOVEL (needs human judgment):**
- A new person, project, or program (entity not in the indexes).
- A status change on an existing entity (e.g. `On Track` → `At Risk`,
  `In Development` → `UAT`, `Active` → `Completed`).
- A first-time person↔project relationship.
- A dollar figure, deadline, or commitment stated for the first time.
- Anything the report says that contradicts the current wiki.

**ROUTINE (likely fine, still staged):**
- Appending a weekly progress line to an existing entity with no status change.
- Rewording an existing narrative without changing facts.

For every NOVEL item, state the **source sentence** from the parsed report that
triggered it, so the reviewer can verify without hunting.

## NOVELTY_REPORT.md format

```markdown
# Novelty Report — <cycle>

**Source report:** reporting/parsed/<file>.md
**Proposed files:** <N>  (<n_new> new entities, <n_status> status changes)

## NOVEL — review before accepting
| Staged file | Change | Source sentence |
|-------------|--------|-----------------|
| proposed/programs/foo/overview_foo.md | NEW program | "<quote>" |
| proposed/projects/bar/overview_bar.md | status In Dev → UAT | "<quote>" |

## ROUTINE — appended progress, no status change
| Staged file | Change |
|-------------|--------|
| proposed/people/jane_doe/overview_jane_doe.md | +weekly line: Supply Chain |

## Unresolved — could not classify (needs a human decision)
- "<quote>" — ambiguous person "David"; could be [[people/...]] or [[people/...]].
```

If there is nothing unresolved, keep the section with `- none`.

## Guardrails

- Never write outside `_staging/<cycle>/`. The wiki only changes via `kb.py accept`.
- Never invent a fact not in the parsed report. If the report is vague, the
  entry is vague — do not embellish.
- Raw reports under `reporting/raw/` are read-only source. Never edit them.
- When unsure whether something is novel, treat it as NOVEL. Over-flagging costs
  a glance; under-flagging slips an unreviewed change into the wiki.
