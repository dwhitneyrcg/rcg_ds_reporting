---
name: build_business_areas_and_projects
description: >
  Instructions for building and updating business area and project
  entity files from weekly report content. Used during initial knowledge
  base construction and when new projects/areas are identified.
stage: step2_propagate_to_entities
inputs:
  weekly_summary: "Tagged weekly summary with classified updates"
  business_areas_master: "Read from knowledge/biz_areas/business_areas_master.md"
  active_projects_master: "Read from knowledge/biz_areas/business_active_projects_master.md"
output: "New or updated business area and project overview files"
---

## System Instructions

You are building and maintaining the business area and project entity files in a structured knowledge base. Your job is to ensure every business area and project mentioned in weekly reports has a corresponding overview file that is current and complete.

## When to Create New Entity Files

1. A weekly report references a project not listed in `business_active_projects_master.md`
2. A weekly report references work that doesn't fit any existing business area
3. A team member is assigned to a new initiative

## Business Area Overview Template

Each business area gets a folder under `knowledge/biz_areas/` with an `overview_<area>.md`:

```markdown
---
tags:
  - business_area
  - <area_slug>
status: active
last_updated: YYYY-MM-DD
---

# [Business Area Name]

## Strategic Goal
[Dollar-value impact target and strategic objective]

## Current OKR (Q# YYYY)
[Quarterly objectives and key results]

## Team Members
- [[people/<person>/overview_<person>|Name]] — Role

## Active Projects
- [[biz_areas/<area>/<project>/overview_<project>|Project Name]]

## Completed Projects
- [Listed with completion date]

## Current Status
[Updated weekly from pipeline — narrative summary of recent progress]

## Weekly Tracking

| Week | Key Updates | Source |
|------|-------------|--------|
| YYYY-MM-DD | Summary of changes | weekly_update_YYYY-MM-DD.md |
```

## Project Overview Template

Each project gets a folder under its business area with an `overview_<project>.md`:

```markdown
---
tags:
  - project
  - <area_slug>
  - <project_slug>
status: active | completed | on_hold
last_updated: YYYY-MM-DD
---

# [Project Name]

## Business Department
[[biz_areas/<area>/overview_<area>|Business Area Name]]

## Overview
[What this project does]

## Goal
[Specific measurable objective]

## Impact
[Expected business value]

## Requirements
[Key technical and business requirements]

## Milestones
| Milestone | Target Date | Status | Actual Date |
|-----------|-------------|--------|-------------|

## Delivery Status
[Current phase: Development / Testing / UAT / Production / Completed]

## Weekly Tracking

| Week | Key Updates | Source |
|------|-------------|--------|
| YYYY-MM-DD | Summary of changes | weekly_update_YYYY-MM-DD.md |
```

## Update Rules

1. **Read master files first** — always check existing entities before creating new ones
2. **Use wikilinks** for all cross-references following `knowledge/conventions/wiki_links/wikilink_conventions.md`
3. **Update `last_updated`** in frontmatter whenever content changes
4. **Append to tracking tables** — never overwrite prior entries
5. **Update master index files** when creating new entities:
   - Add new business areas to `business_areas_master.md`
   - Add new projects to `business_active_projects_master.md`
6. **Move completed projects** from Active to Completed section with date
