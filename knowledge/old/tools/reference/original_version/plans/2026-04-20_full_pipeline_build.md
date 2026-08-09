# Plan: Full Pipeline Build — Weekly Knowledge Base Workflow

**Date:** 2026-04-20  
**Input:** `build.md` task + `DESIGN_DOC.md` + `REQ_knowledge_base_system.md`  
**Status:** Validated

---

## Scope

Build all missing pipeline components across Stages 0–3. Deliverables are prompt files (`.prompt.md`) and Python code (`.py`) within `knowledge/tools/`.

---

## Files to Create

| # | File Path | Type | Stage | Purpose |
|---|-----------|------|-------|---------|
| 1 | `code/batch_convert.py` | Python | 0 | Orchestrates batch `.docx` → `.md` with idempotency |
| 2 | `code/parse_weekly_report.py` | Python | 1 | Parses raw `.md` into structured JSON blocks per person/area |
| 3 | `code/deduplicate_updates.py` | Python | 1 | Compares current vs. prior week tagged output, flags duplicates |
| 4 | `code/generate_changelog.py` | Python | 2 | Produces changelog `.md` from entity diffs |
| 5 | `code/validate_knowledge_base.py` | Python | 3 | YAML, wikilink, required-field validation |
| 6 | `code/generate_pr_summary.py` | Python | 3 | Produces PR description from changelog |
| 7 | `prompts/parse_weekly_report.prompt.md` | Prompt | 1 | Instructions for splitting raw report into tagged blocks |
| 8 | `prompts/deduplicate_updates.prompt.md` | Prompt | 1 | Instructions for prior-week dedup |
| 9 | `prompts/update_person_entity.prompt.md` | Prompt | 2 | Instructions for editing person overview files |
| 10 | `prompts/update_project_entity.prompt.md` | Prompt | 2 | Instructions for editing project overview files |
| 11 | `prompts/update_business_area_entity.prompt.md` | Prompt | 2 | Instructions for editing business area overview files |
| 12 | `prompts/generate_changelog.prompt.md` | Prompt | 2 | Instructions for changelog formatting |

## Files to Modify

| File | Change |
|------|--------|
| `DESIGN_DOC.md` | Add Stage 0 orchestration, Stage 1 parser, Stage 2 entity prompts, Stage 3 validation to implementation phases |
| `README.md` | Add all new files to the file map |

## Dependencies

```
batch_convert.py (Stage 0)
       │
       ▼
parse_weekly_report.py (Stage 1) ← reads master_team_roster.md, business_areas_master.md, business_active_projects_master.md
       │
       ▼
deduplicate_updates.py (Stage 1) ← reads prior week's tagged output
       │
       ▼
executive_summary.prompt.md + evp_highlights.prompt.md (Stage 1 — existing)
       │
       ▼
update_person_entity.prompt.md + update_project_entity.prompt.md + update_business_area_entity.prompt.md (Stage 2)
       │
       ▼
generate_changelog.py (Stage 2)
       │
       ▼
validate_knowledge_base.py (Stage 3)
       │
       ▼
generate_pr_summary.py (Stage 3)
```

## Validation Checklist

- [x] All code reads entity data from master `.md` files — nothing hardcoded (R2.2.8)
- [x] Parser handles variability: first-name-only, multi-person blocks, inconsistent delimiters (build.md)
- [x] Dedup compares against prior week (R2.2.7)
- [x] Entity updates append to tracking tables, never overwrite (R2.3.2, R2.3.3, R2.3.4)
- [x] Changelog cites source text for status changes (R2.3.7)
- [x] Validation checks YAML, wikilinks, required fields (R6.1.*)
- [x] All files created within `knowledge/tools/` scope (build.md constraint)
- [x] All Python code produces execution logs (R3.1.3)
