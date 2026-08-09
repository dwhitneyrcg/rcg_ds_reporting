---
name: deduplicate_updates
description: >
  Compare the current week's tagged report against the prior week's to
  identify and remove duplicate content. Ensures the executive summary
  only contains genuinely new information.
stage: step1_summarize_and_classify
inputs:
  current_tagged: "This week's tagged .md (output of parse_weekly_report)"
  prior_tagged: "Prior week's tagged .md"
output: "Deduplicated tagged .md with duplicate items removed"
code: "code/deduplicate_updates.py"
---

## System Instructions

You are comparing two consecutive weekly tagged reports to remove content that was already reported the prior week. The goal is to ensure executive summaries contain only new information.

## Deduplication Rules

1. **Similarity threshold:** Items with ≥75% text similarity to a prior-week item are flagged as duplicates
2. **Scope:** Compare within the same business area first, then across areas for the same person
3. **Action:** Remove duplicate items from the current week's output
4. **Logging:** Record every removed item with the prior-week match and similarity score

## What Counts as Duplicate

- Same achievement restated with minor wording changes
- Ongoing work items carried forward verbatim from last week
- Status updates that haven't changed (same milestone, same status)

## What is NOT Duplicate

- A follow-up to last week's work (e.g., "Completed testing" after last week's "Started testing")
- Same project but different deliverable
- New context added to an ongoing item
- Status changes (e.g., "In Progress" → "Completed")

## Output

The deduplicated file maintains the same YAML frontmatter and structure as the input, with duplicate bullet items removed. If an entire person block becomes empty after dedup, remove the block entirely.
