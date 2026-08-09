---
name: generate_changelog
description: >
  Produce a structured CHANGELOG.md that lists every entity change
  proposed by this pipeline run. The changelog is appended to the PR
  for reviewer audit.
stage: step2_propagate_to_entities
inputs:
  tagged_report: "Deduplicated tagged weekly summary"
output: "CHANGELOG.md with tables of person, area, and project changes"
code: "code/generate_changelog.py"
---

## System Instructions

You are generating an auditable changelog that lists every entity change this pipeline run proposes. The changelog will be included in the PR description so a reviewer can quickly assess scope and correctness.

## Changelog Structure

```
# Changelog — YYYY-MM-DD

## Person Entity Updates
| Person | Area | Items | File Exists |
| ...

### Details
#### <Person Name> (<Area>)
Action: Append tracking row for YYYY-MM-DD
- <item 1>
- <item 2>

## Business Area Updates
- **<Area>** — file exists
  - Action: Update Current Status narrative, append tracking row

## Project References
- `<wikilink path>`

## Summary
- People updated: N
- Areas updated: N
- Projects referenced: N
```

## Rules

1. Every changed entity must appear in the changelog
2. List the specific action taken (append row, update status, add project)
3. Flag missing entity files with bold markers so the reviewer can decide whether to create them
4. Include the source text from the weekly report that justifies each change
5. Sort entries alphabetically within each section
