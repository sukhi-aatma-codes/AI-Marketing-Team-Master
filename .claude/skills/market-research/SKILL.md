---
name: market-research
description: >
  Use this skill whenever the user wants to research a market, industry vertical, competitor,
  or topic to inform a marketing or business strategy decision. Trigger on requests like
  "research the HR tech market", "who are our competitors in X", "what's happening
  in the supply chain software space", "do a market analysis of Y", "give me a competitive
  landscape for Z", or any request for market intelligence, competitor analysis, or industry
  sizing. Always use this skill before campaign briefs, keyword research, or content strategy
  work on a new vertical — it should be the first step in any new market or topic exploration.
---

# Market Research

Researches a market, vertical, competitor, or topic using web search and produces a structured
intelligence report with strategic implications. The `.md` output is the machine-readable
handoff for downstream skills (keyword-research, campaign-brief, blog-writer). The PDF is
the human-ready deliverable for stakeholders.

## Before starting

Read these context files every time — do not rely on prior session memory:
- `_context/Brand_Context.md` — brand positioning and proof points
- `_context/Brand_Product_Offerings.md` — service lines and ICPs
- `_context/Brand_Growth_Marketing_Context.md` — channels, growth vectors, current focus

## Clarify scope first

Before searching, confirm with the user:
1. **Topic:** What market, vertical, or company to research
2. **Depth:** Quick scan (key signals only, ~30 min) or deep dive (full analysis)
3. **Competitors:** Any specific companies to profile, or should you identify them?
4. **Purpose:** What decision will this research inform? (shapes what to prioritise)

If the user's request makes all four clear, skip asking and proceed.

## Research workflow

### Step 1 — Market landscape
Search for:
- Market size, growth rate, and forecast (cite source and year)
- Key trends reshaping the market in the past 12–24 months
- Regulatory or macro forces affecting buyers
- Dominant players and their market share where available

### Step 2 — Competitor profiling
For each relevant competitor (up to 5):
- Positioning and value proposition
- Target segments and geographies
- Known differentiators and weaknesses
- Pricing model if publicly available
- Recent news, funding, or product launches

### Step 3 — Buyer signals
Search for:
- What buyers in this market are searching for (intent signals)
- Common pain points appearing in reviews, forums, or industry publications
- Analyst commentary on buyer priorities (Gartner, Forrester, McKinsey, plus analysts specific to the brand's vertical)

### Step 4 — Brand opportunity mapping
Using the brand context files, identify:
- Where the brand's positioning matches unmet needs
- Where competitors are weak that the brand can exploit
- Which growth vectors from `Brand_Growth_Marketing_Context.md` this market supports
- Content and messaging angles with the most traction potential

## Output structure (`.md`)

Save as `output/reports/research-<topic>-<date>.md` with this exact section structure so downstream skills can parse it:

```
# Market Research: [Topic]
Date: [yyyy-mm-dd]
Prepared for: [purpose the user stated]

## Market Landscape
[Market size, growth, trends, macro forces]

## Competitor Profiles
[One subsection per competitor: positioning, segments, differentiators, weaknesses, news]

## Buyer Signals
[Pain points, intent signals, analyst commentary]

## Brand Opportunity Map
[Gap analysis, positioning angles, which growth vectors apply]

## Strategic Implications
[3–5 bullet recommendations: what to prioritize, what to avoid, what to watch]

## Sources
[All sources cited with URLs and access dates]
```

## Rich deliverable

After saving the `.md`, invoke `document-skills:pdf` to render it as a formatted PDF.
Save as `output/reports/research-<topic>-<date>.pdf`.

Tell the user: the `.md` is ready for use by keyword-research or campaign-brief skills; the PDF is ready to share with stakeholders.

## Quality checklist

- [ ] All claims are cited — no unsourced statistics or assertions
- [ ] At least 3 competitors profiled (or user confirmed fewer exist)
- [ ] Brand opportunity map references `Brand_Context.md` proof points, not invented ones
- [ ] `.md` section headings match the structure above (for agent handoff compatibility)
- [ ] PDF generated and saved to `output/reports/`
- [ ] Sources section populated with URLs and access dates
- [ ] Every reported data point was actually retrieved — anything that could not be fetched or verified is marked `[DATA UNAVAILABLE — <what was needed>]`, never estimated or filled with a plausible-sounding value
