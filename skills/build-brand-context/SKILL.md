---
name: build-brand-context
description: >
  Use this skill to refresh or rebuild the Brand_Context.md file only — without running a
  full brand onboarding. Trigger when: company positioning has changed, a new vertical or ICP
  has been added, the value proposition needs updating, or Brand_Context.md is stale or missing
  but the other context files are still valid. Accepts a URL, uploaded materials, or user-provided
  text as input. Does NOT touch any other _context\ file.
---

# Build Brand Context

Refreshes `_context/Brand_Context.md` — the company overview, positioning, and ICP file.
Use this when the brand's positioning, verticals, or differentiators have changed, but a full
re-onboarding is not warranted.

## Scope — what this skill writes

This skill writes ONE file: `_context/Brand_Context.md`.
It does NOT modify `Brand_Voice_Guide.md`, `Brand_Style.md`, `Brand_Product_Offerings.md`,
`Brand_Growth_Marketing_Context.md`, or `Brand_Insights_Ledger.md`.

## Before starting

If `_context/Brand_Context.md` already exists, read it first.
Note which sections are outdated or missing — those are the primary update targets.
Do not discard accurate existing content: merge and update, don't wholesale replace, unless the
user explicitly asks for a full rewrite.

## Clarify inputs

Ask the user:
1. **Source material:** URL to scrape, uploaded deck/doc, or will the user provide information directly?
2. **Scope of change:** What has changed? (e.g., new ICP, repositioned product, new market, rebrand)
3. **Rewrite or update?** Should this be a targeted update to specific sections, or a full rewrite?

If the user can't answer, default to: scrape the provided URL, compare against the existing file, and update only the sections where the scraped content conflicts with or extends the current content.

## Research phase

If a URL is provided:
- Scrape: homepage, About Us, product/service pages, case studies, any "Who we serve" sections
- Extract: company description, mission/vision statements, named customer segments, explicit pain points addressed, differentiators claimed, any named verticals or geographies

If materials are uploaded (deck, PDF, brief):
- Extract the same signals from the uploaded content
- Cross-reference against the existing `Brand_Context.md` to identify gaps and conflicts

If neither: work from what the user provides directly in the conversation.

## File structure to produce

Write `_context/Brand_Context.md` with these sections:

```
# Brand Context — [Company Name]

## Company Overview
[2–3 sentences. What the company does, who it serves, and what category it operates in.
Concrete, not generic — name the industry, the buyer type, and the outcome delivered.]

## Positioning Statement
[One sentence. Format: "For [target buyer] who [need/problem], [Company] is the [category]
that [key differentiator]. Unlike [alternative], we [proof of differentiation]."
If a formal positioning statement doesn't exist in the source, synthesize one from the research.
Mark it: [SYNTHESIZED — confirm with client]]

## Target Verticals
[Bulleted list of the industries or sectors the brand serves. Name them specifically —
not "enterprise" but "mid-market insurance carriers" or "Series B SaaS companies".]

## Buyer Profiles (ICPs)
[Per ICP: role title, company size/type, primary pain point they hire this brand to solve,
buying trigger (what causes them to start searching), and key decision criterion.
Mark any inferred buyer profiles with [ASSUMPTION — confirm with client].]

## Core Differentiators
[3–5 bullets. What makes this brand distinctly different from alternatives in their category.
Grounded in the source material — not inferred from generic category claims.]

## Competitive Positioning
[Brief landscape note: which alternatives buyers typically consider, and how this brand
positions against them. If not in source material, mark as [TBD — competitive research needed].]

## Brand Maturity & Market Presence
[Founding year (if available), team size or scale signal, notable clients or logos (if public),
geographic reach. Mark any unknown fields as [TBD].]
```

## Quality rules

- No invented company facts. If a stat or claim isn't in the source material, use `[TBD]`.
- No generic filler (e.g., "a leading provider of innovative solutions"). Write concrete specifics.
- If you synthesize the positioning statement because one doesn't exist, mark it clearly.
- Every ICP must name a specific role and a specific pain point — not "decision makers" or "businesses".
- Do not paste marketing copy verbatim. Translate it into operational brand intelligence.

## Output

Save to: `_context/Brand_Context.md`

After saving, report to the user:
- What sections were updated vs. left unchanged
- Any fields marked `[TBD]` or `[ASSUMPTION]` that need user validation
- Whether the file is ready for downstream agents or has gaps that block execution
