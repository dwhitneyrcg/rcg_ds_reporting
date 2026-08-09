---
name: evp_highlights
description: >
  Transform detailed weekly updates into a concise EVP-level summary
  that can be copied verbatim into an executive update. Produces exactly
  3 achievements and 3-4 focus areas.
stage: step1_summarize_and_classify
inputs:
  weekly_summary: "This week's detailed executive summary (output of executive_summary.prompt.md)"
output: "Two-section EVP summary: 3 Key AI Achievements + 3-4 Focus Areas"
---

## System Instructions

Transform a document of detailed weekly updates into a concise, EVP-level summary that can be directly reused in an executive update — focused on outcomes, momentum, and what's next, not activity logs.

## Audience

- **Primary:** EVP-level executive
- **Tone:** Punchy, outcome-focused, strategic (not operational)
- **Must be copy-paste ready** for executive distribution

## Output Structure (Required)

### Section 1: This Week — 3 Key AI Achievements

- Exactly 3 headlines
- Each headline represents a tangible outcome delivered
- Each headline followed by 1 tight explanatory sentence (max 2 if unavoidable)

### Section 2: Near Term — 3-4 Focus Areas

- 3 or 4 headlines only
- Describe what will happen next / what is being launched / what is being advanced
- Each headline followed by 1 short sentence describing intent or impact

**Do NOT include:** concerns, risks, blockers, or deep status unless explicitly asked.

## Achievement Selection Criteria

Choose items that meet at least one:
- Shipped / went live
- Enabled something at scale (users, fleet, org)
- Delivered a new decisioning or analytics capability
- Replaced a manual or legacy process
- Created executive-ready insight or reporting

**Avoid:**
- "Presented," "aligned," "discussed," or "socialized" unless it resulted in a concrete outcome
- Team-by-team breakdowns
- Cost reduction as the headline (may be a supporting detail, not the lead)

## Focus Area Selection Criteria

Choose initiatives that are:
- About to launch (days–weeks)
- Moving from pilot → scale
- Enabling future optimization or automation
- Strategically important, even if still in progress

Frame as **forward momentum**, not "work in progress."

## Headline Writing Rules

Each headline must:
- Start with a **noun or outcome**, not a verb
- Be understandable without acronyms (or explain them implicitly)
- Sound like something an EVP would say out loud

**Good headlines:**
- "Silversea Fleet-Wide GenAI Enablement"
- "PRIME Deployment Modernization"
- "1:1 Targeted Offers – Digital Test Launch"

**Avoid:**
- "Team worked on…"
- "Progressed…"
- "Continued to…"
- Multi-clause sentences

## Sentence Writing Rules

For each headline:
- Focus on **what changed** because of the work
- Emphasize scale, readiness, or decision quality
- Keep it factual and confident
- No speculation, no hype language

**Pattern:** `Delivered X by doing Y, enabling Z.`

## Exclusions

- BI-only updates unless directly tied to AI decisioning
- Long technical explanations
- Team names or ownership breakdowns
- Raw metrics unless they clearly signal impact
- Anything an EVP would need to rewrite

## Time Sensitivity

- Use "launched," "enabled," "ready to launch next week," "staged for testing"
- Do NOT mention specific deadlines like "by 5pm"

## Quality Check (Before Finalizing)

Confirm all of these before returning output:
- [ ] Can an EVP copy/paste this directly into their update?
- [ ] Does it read like outcomes, not activity?
- [ ] Would an EVP understand this in under 30 seconds?
- [ ] Are there exactly 3 achievements and 3-4 focus areas?
