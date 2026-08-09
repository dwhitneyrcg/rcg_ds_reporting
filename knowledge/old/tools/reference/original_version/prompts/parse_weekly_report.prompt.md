---
name: parse_weekly_report
description: >
  Parse a raw weekly .md report into structured, tagged blocks grouped by
  person and business area. This is the first processing step after .docx
  conversion and before executive summarization.
stage: step1_summarize_and_classify
inputs:
  raw_report: "A raw weekly .md file from reporting/weekly_updates_raw_md/"
  master_team_roster: "Read from knowledge/people/master_team_roster.md"
  business_areas_master: "Read from knowledge/biz_areas/business_areas_master.md"
  active_projects_master: "Read from knowledge/biz_areas/business_active_projects_master.md"
output: "A tagged .md file with YAML frontmatter listing all people, areas, and projects referenced"
code: "code/parse_weekly_report.py"
---

## System Instructions

You are parsing a raw weekly team report into structured, classified update blocks. The raw report is a flat document containing updates from multiple team members, each covering one or more business areas and projects.

## Input Format

The raw report follows this general pattern (with significant variability):

```
<Person Name(s)>
<Business Area / Brand>: <Project Name>
- Bullet point work items
- More bullets
```

## Processing Steps

### Step 1: Split into Person Blocks

Identify where each person's update begins and ends:
- Person headers are standalone lines containing a known team member name
- Names may be first-name-only, full name, or multi-person (`Ben & Camila`)
- Resolve all names against `master_team_roster.md`
- Everything between one person header and the next belongs to that person's block

### Step 2: Classify Business Area

For each person block, determine the canonical business area:
- Check the first few lines for explicit area headers (text before `:` or `|`)
- Match against known business area names and aliases from `business_areas_master.md`
- Use brand prefixes (`RCI |`, `CEL |`, `SSC |`) as disambiguation signals
- If no match, classify as "Unclassified"
- Each block maps to exactly ONE area

### Step 3: Match Active Projects

For each block, identify which active projects from `business_active_projects_master.md` are referenced:
- Match project names against the block text
- Use word overlap scoring for fuzzy matching
- A block may reference zero or more projects

### Step 4: Separate Completed vs. In-Progress

Split each block's content into:
- **Completed**: past-tense items, explicitly labeled "Completed/Delivered" sections
- **In Progress**: present-tense work, explicitly labeled "In Progress/Working On" sections
- **Next Steps**: forward-looking items, explicitly labeled "Next Steps/Upcoming" sections

### Step 5: Output Tagged Markdown

Produce a `.md` file with:
- **YAML frontmatter** containing: date, source file, tags (all areas as slugs), people list, business_areas list, projects list
- **Body** organized by business area (H2), then person (H3), with Completed/In Progress/Next Steps subsections

## Output Format

```markdown
---
date: YYYY-MM-DD
source: <original filename>
tags:
  - weekly_update
  - <area_slug_1>
  - <area_slug_2>
people:
  - Person Name 1
  - Person Name 2
business_areas:
  - "Business Area 1"
  - "Business Area 2"
projects:
  - "Project Name 1"
---

# Weekly Update — YYYY-MM-DD

## Business Area Name

### Person Name

**Completed:**
- Item 1
- Item 2

**In Progress:**
- Item 1

**Next Steps:**
- Item 1
```

## Key Constraints

- All entity lookups (people, areas, projects) must use the master markdown files — not hardcoded values
- Person names in the output must be the canonical display name from `master_team_roster.md`
- Business areas must match the 17 canonical labels in `business_areas_master.md`
- If a person cannot be resolved, log a warning and use the raw name
