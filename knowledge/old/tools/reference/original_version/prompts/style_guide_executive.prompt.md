---
name: style_guide_executive
description: >
  Formatting and tone rules for per-area summaries in the executive
  weekly report. Referenced by executive_summary.prompt.md.
stage: shared
---

## Summary Paragraph Rules

For each business area, produce a single paragraph following this structure:

1. **Lead with deliveries:** Start with any important meetings or new business deliveries.
2. **Add context:** Provide supporting strategic context where necessary (2-3 sentences max).
3. **Close with active work:** Summarize active work not yet delivered in a single sentence (no strategic context needed).

## Tone & Language

| Do | Don't |
|----|-------|
| "Delivered PRE" | "Between March and April our Revenue Management team delivered PRE" |
| "Teams are focusing on" | "Building on recent achievements, teams are focused on" |
| Use specific dollar amounts | Use vague "significant revenue" language |
| Be explicit about objectives addressed | Say "in support of OKRs" |
| Replace names with "Team" | Mention individual team members |
| State project outcomes | Describe project activities |

## Structural Rules

- Each sentence must be internally complete: `what was done + why it matters`
- Do not front-load all work then explain significance at the end
- No line separators between business area bullets
- No newline break between accomplishments and ongoing work within a bullet
- Order alphabetically by business area name
- If no updates exist for an area: "No Relevant Update"
- Eliminate all citations from final output
- Do not over-abbreviate — details must not be lost

## Example Output

```
• **PCP Pricing Automation:** Teams delivered a PoC optimization model for Beverage packages, addressing key factors such as price elasticity and dilution concerns. Positive feedback from business teams underscores its importance in mitigating revenue risks tied to secular decline and advancing high-margin product performance. *Teams are now working on refining the optimization model for Beverage packages and integrating the product recommendations engine API with backend systems to enable QA testing during test sailings.*
```
