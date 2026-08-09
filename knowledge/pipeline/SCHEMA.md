# Entity schema & templates

Canonical structure for every entity overview. `kb.py validate` enforces the
three required frontmatter fields (`type`, `name`, `status`); the rest is
convention. Keep frontmatter minimal — it is metadata, not content.

Files live at `<entity_dir>/<slug>/overview_<slug>.md`.

---

## program

```markdown
---
type: program
name: "Revenue Management Automation"
aliases: ["RMA", "Rev Mgmt"]   # abbreviations used in reports; powers name-mapping
status: Active            # Active | Paused | Completed
tags: [program]
---

# Revenue Management Automation

## Goal
One or two sentences: what this initiative exists to do.

## Projects
- [[projects/<slug>/overview_<slug>|Project Name]]

## Current Status
Narrative of where the program stands this quarter. Updated as projects move.
```

---

## project

```markdown
---
type: project
name: "Pricing Recommendation Engine"
aliases: ["PRE", "PRE 4.0"]    # abbreviations used in reports; powers name-mapping
status: In Development    # Planned | In Development | UAT | Live | Completed | At Risk | Paused
program: "[[programs/revenue_management_automation/overview_revenue_management_automation|Revenue Management Automation]]"
tags: [project]
---

# Pricing Recommendation Engine

## Summary
What the deliverable is and who it serves.

## People
- [[people/<slug>/overview_<slug>|Person Name]]

## Progress Log
| Date | Update | Status |
|------|--------|--------|
| 2026-04-24 | <one-line progress> | In Development |
```

Append a row to **Progress Log** each cycle; never overwrite prior rows. Change
the `status` frontmatter field only when the report justifies it — that is a
NOVEL change (see EXTRACT.md) and the changelog/novelty report must cite why.

---

## person

```markdown
---
type: person
name: "David Whitney"
aliases: ["Dave"]         # optional nicknames; help resolve names in weekly reports
status: Active            # Active | Inactive
tags: [person]
---

# David Whitney

## Role
Title / function (if known from reports).

## Active Projects
- [[projects/<slug>/overview_<slug>|Project Name]]

## Weekly Progress
| Date | Project | Activity |
|------|---------|----------|
| 2026-04-24 | [[projects/<slug>/overview_<slug>|Project Name]] | <one-line> |
```

Append to **Weekly Progress** each cycle. Add/remove **Active Projects** links as
the person's involvement changes (a new person↔project link is NOVEL).

---

## Indexes

`indexes/{people,projects,programs}.md` are flat lists of every entity, used by
EXTRACT as the "what already exists" source of truth **and the alias lookup
table** for name-mapping. Each line is a wikilink plus any aliases in `(aka: …)`:

```markdown
# Programs
- [[programs/revenue_management_automation/overview_revenue_management_automation|Revenue Management Automation]]  (aka: RMA, Rev Mgmt)
```

When `accept` promotes a *new* entity, add its line (with its aliases) to the
matching index in the same cycle. When the extract step learns a new alias for
an existing entity, update both the entity's `aliases:` and its index line.
