# Plan: Initial Agent System Setup & Prompt Migration

**Date:** 2026-04-19  
**Input:** Design discussion + DESIGN_DOC.md + stakeholder requirements  
**Status:** Validated

## Objective

Bootstrap the agent-based knowledge pipeline by:
1. Converting all existing `.docx` instruction files to `.prompt.md` format
2. Converting all raw weekly `.docx` reports to Markdown
3. Establishing the Planner → Validator → Executor agent workflow
4. Documenting requirements traceably

## What Was Completed

### Files Created

| File Path | Type | Purpose |
|-----------|------|---------|
| `knowledge/prompts/requirements/REQ_knowledge_base_system.md` | Requirements | Complete requirements document (R1–R7) |
| `knowledge/prompts/prompts/executive_summary.prompt.md` | Prompt | INSTRUCT_BASE converted to parameterized markdown |
| `knowledge/prompts/prompts/evp_highlights.prompt.md` | Prompt | INSTRUCT_HIGHLIGHTS converted to parameterized markdown |
| `knowledge/prompts/prompts/classification_rules.prompt.md` | Prompt | Business area mapping rules (shared) |
| `knowledge/prompts/prompts/style_guide_executive.prompt.md` | Prompt | Formatting & tone rules (shared) |
| `knowledge/prompts/prompts/build_business_areas_and_projects.prompt.md` | Prompt | Entity creation/update instructions for Step 2 |
| `knowledge/prompts/code/docx_to_markdown.py` | Code | Reusable .docx → .md converter with logging |
| `.github/agents/kb-planner.agent.md` | Agent | Planner agent definition |
| `.github/agents/kb-validator.agent.md` | Agent | Validator agent definition |
| `.github/agents/kb-executor.agent.md` | Agent | Executor agent definition |

### Conversions Executed

| Source | Target | Count |
|--------|--------|-------|
| `knowledge/prompts/prompts/*.docx` | `knowledge/prompts/prompts/*.md` | 3 instruction files |
| `knowledge/reporting/weekly_updates_raw/*.docx` | `knowledge/reporting/weekly_updates_raw_md/*.md` | 49 weekly reports |

### Agent Architecture

```
User Request
     │
     ▼
┌─────────────┐     ┌──────────────┐
│  kb-planner  │◄───►│ kb-validator  │
│  (plans)     │     │  (reviews)    │
└──────┬──────┘     └──────────────┘
       │ validated plan
       ▼
┌─────────────┐
│ kb-executor  │
│ (implements) │
└─────────────┘
```

## Next Steps (Phase 2)

1. Design Step 2 entity propagation prompts (how to update person/project/area files from a tagged weekly summary)
2. Build the changelog generator
3. Implement YAML frontmatter and wikilink validation checks
4. Test the full pipeline on 2-3 historical weekly reports end-to-end

## Validation Notes

Reviewed against REQ_knowledge_base_system.md sections R1–R6. All structural requirements are met for Phase 1 deliverables.
