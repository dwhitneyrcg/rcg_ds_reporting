---
name: update_person_entity
description: >
  Update a person's overview file based on tagged weekly report data.
  Appends tracking table entries and updates active project lists.
stage: step2_propagate_to_entities
inputs:
  tagged_report: "Structured tagged weekly summary with per-person blocks"
  person_overview: "Current content of the person's overview_<name>.md file"
  active_projects_master: "Read from knowledge/biz_areas/business_active_projects_master.md"
output: "Updated person overview file with new tracking entry and project list changes"
---

## System Instructions

You are updating a person's knowledge base overview file based on their contributions reported in this week's tagged summary. You append new information — you never overwrite existing tracking entries.

## What to Update

### 1. Weekly Tracking Table

Append a new row to the person's `## Weekly Tracking` table:

```markdown
| YYYY-MM-DD | <summary of this week's work> | <business area(s)> | <project(s)> |
```

- **Date:** The date of the weekly report
- **Summary:** 1-2 sentence summary of what this person did (combine all their blocks)
- **Business Area:** Which area(s) they contributed to
- **Projects:** Which specific projects they worked on

### 2. Active Projects List

Check the person's `## Active Projects` section:
- If they worked on a project not currently listed, **add it** with a wikilink
- If a project is marked as completed in the weekly report, **move it** to the Completed Projects section with the completion date
- Use wikilink format: `[[biz_areas/<area>/<project>/overview_<project>|Project Name]]`
- Verify the project exists in `business_active_projects_master.md` before adding

### 3. Frontmatter

- Update `last_updated: YYYY-MM-DD` to the report date

## What NOT to Update

- Do NOT change: name, leader, employee type, resource role, business area assignment
- Do NOT overwrite existing tracking table rows
- Do NOT remove projects from the active list unless explicitly marked completed
- Do NOT modify the person's static metadata

## Wikilink Format

All project references must use the Obsidian wikilink format:
```
[[biz_areas/<area_folder>/<project_folder>/overview_<project>|Display Name]]
```

## Output Format

Return the complete updated overview file content, ready to write directly to disk.
