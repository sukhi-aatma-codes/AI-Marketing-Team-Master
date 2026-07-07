---
name: campaign-report
description: >
  Use this skill whenever the user wants to analyze marketing campaign performance, generate
  a campaign report, review results from a paid or organic campaign, or summarize what worked
  and what to do next. Trigger on requests like "analyze our Q2 campaign", "report on this
  campaign data", "how did our LinkedIn ads perform", "pull together our campaign results",
  "what's our CPL looking like", or any time the user shares campaign metrics and wants
  analysis, insights, or recommendations. Produces three outputs: Excel data file, PowerPoint
  deck, and PDF — plus the structured markdown for agent handoffs.
---

# Campaign Report

Analyzes marketing campaign performance from data the user provides. Surfaces insights,
benchmarks against targets, and produces prioritized recommendations. Outputs: structured
`.md` (agent handoff), `.xlsx` (data + pivot-ready tables), `.pptx` (executive summary deck),
`.pdf` (send-ready version of the deck).

## Before starting

Read this context file:
- `_context/Brand_Growth_Marketing_Context.md` — channel benchmarks, funnel targets, active
  campaign types and goals

## Gather inputs first

Ask the user to provide:
1. **Campaign data:** Paste a metrics table, share a CSV, or describe the numbers by channel
2. **Campaign context:** What was the goal? What channels ran? What was the spend? What period?
3. **Success metrics:** What were the targets (CPL, ROAS, MQLs, reach, etc.)?
4. **Audience:** Who will see this report? (Shapes depth — internal team vs. executive vs. client)

If the user has already provided all of this, skip asking and proceed.

## Analysis workflow

### Step 1 — Data validation
Before analysing, check:
- Are all key metrics present? Flag any gaps (e.g., no conversion data, no spend breakdown)
- Are the metrics comparable across channels, or do different channels measure different things?
- What is the attribution model? Note any limitations this creates in the analysis

### Step 2 — Performance summary
Calculate and document:
- Total spend, total impressions, total clicks, total conversions (or MQLs)
- Overall CPL / ROAS / CTR — whatever the primary KPI is
- Funnel conversion rates: Impression → Click → Landing page → Conversion

### Step 3 — Channel-by-channel breakdown
For each channel in the campaign:
- Spend, impressions, clicks, conversions
- Channel-specific KPIs (e.g., LinkedIn: CTR + CPL; Google: Quality Score + ROAS; Email: Open rate + CTR)
- Performance vs. target: over/under, by how much, what it means

### Step 4 — Insight extraction (3–5 insights)
Go beyond the numbers. For each insight:
- **What happened** (the data)
- **Why it likely happened** (the interpretation)
- **What it means for future campaigns** (the implication)

Avoid generic insights ("CTR was low"). Make them specific and actionable ("LinkedIn Sponsored
Content CTR was 0.3% vs. 0.5% benchmark — the vertical-specific creative outperformed the
generic service ad by 2x, suggesting vertical-specific creative should be the default").

### Step 5 — Recommendations
Produce 3–5 prioritized recommendations:
- Rank by impact (high/medium/low) and effort (high/medium/low)
- Each recommendation links back to a specific insight
- Include a suggested next test or action

## Output structure (`.md`)

Save as `output/reports/campaign-report-<campaign-name>-<date>.md`:

```
# Campaign Report: [Campaign Name]
Period: [start – end date]
Prepared for: [audience]
Date: [yyyy-mm-dd]

## Campaign Overview
[Goal, channels, total spend, period summary]

## Performance Summary
[Top-line KPIs vs. targets — table format]

## Channel Breakdown
[One subsection per channel with metrics table + narrative]

## Key Insights
1. [Insight: what + why + implication]
2. ...

## Recommendations
| # | Recommendation | Impact | Effort | Links to insight |
|---|---------------|--------|--------|-----------------|
...

## Data Notes
[Attribution model, gaps, caveats]
```

## Rich deliverables

After saving the `.md`, produce three outputs:

**1. Excel data file**
Invoke `document-skills:xlsx` to build:
- Sheet 1: Raw data table (all metrics, all channels, all periods)
- Sheet 2: Channel comparison table (pivot-ready)
- Sheet 3: Actuals vs. targets summary

Save as `output/reports/campaign-report-<name>-<date>.xlsx`

**2. PowerPoint executive deck**
Invoke `document-skills:pptx` to build a 5–8 slide branded deck:
- Slide 1: Campaign overview (goal, period, spend)
- Slide 2: Performance summary (top KPIs vs. targets — visual)
- Slides 3–5: Channel breakdown (one slide per major channel)
- Slide 6: Key insights (3–5 bullets, one per insight)
- Slide 7: Recommendations (prioritized table)
- Slide 8 (optional): Appendix / data notes

Use the brand deck template via `branded-deck` skill.
Save as `output/reports/campaign-report-<name>-<date>.pptx`

**3. PDF**
Invoke `document-skills:pdf` to export the deck as a send-ready PDF.
Save as `output/reports/campaign-report-<name>-<date>.pdf`

## Quality checklist

- [ ] Every metric in the report is from the user's data — no estimated or invented numbers
- [ ] Each insight is specific (names channel, creative, or audience) — not generic
- [ ] Recommendations are prioritized by impact × effort, not just listed
- [ ] Data notes flag any attribution gaps or measurement limitations
- [ ] All three rich formats (`.xlsx`, `.pptx`, `.pdf`) generated and saved
- [ ] `.md` section headings match the structure above
