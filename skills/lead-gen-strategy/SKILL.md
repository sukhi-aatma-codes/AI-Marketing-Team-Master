---
name: lead-gen-strategy
description: >
  Use this skill when the user needs the architecture of a lead generation funnel —
  channel mix, lead qualification criteria, scoring model, and nurture flow — rather
  than a single content asset. Trigger on requests like "design our lead gen funnel
  for X", "what's our MQL/SQL criteria", "build a lead scoring model", "map our nurture
  flow for this offer", or "how should we generate and qualify leads for Y". Produces
  the strategic funnel architecture; does not write the gated asset, landing page, or
  email copy itself — those are built afterward via lead-magnet, lp-builder, and
  email-copy using this document as the brief.
---

# Lead Generation Strategy

Produces the funnel architecture beneath a lead generation push: which channels source
leads, how leads get qualified and scored, how they route, and how the nurture sequence
is structured stage by stage. This is a planning document, not the gated asset or the
copy — those get built afterward by other skills against this brief.

## Before starting

Read these context files every time:
- `_context/Brand_Growth_Marketing_Context.md` — current channels, funnel stages, goals, benchmarks
- `_context/Brand_Product_Offerings.md` — service lines, ICPs, differentiators
- `_context/Brand_Insights_Ledger.md` Section 1 — confirmed buyer personas and objections

## Clarify inputs first

Confirm:
1. **Target offer or topic**: What the funnel is built around (a specific service line, a gated asset topic, or a broader program)
2. **Target ICP**: Who this funnel needs to qualify and convert
3. **Funnel scope**: Standalone funnel build, or part of a broader campaign already defined by `campaign-strategist` (if the latter, request the Campaign Strategy Document as input rather than re-deriving audience/positioning)
4. **Existing channels**: What's already live (check `Brand_Growth_Marketing_Context.md`) vs. what needs to be stood up
5. **Lead volume expectations**: Realistic monthly/quarterly target if known, or flag as TBD

## Workflow

### Step 1 — Channel mix
Recommend channels realistic given current capability (per `Brand_Growth_Marketing_Context.md`). For each channel:
- Role (top-of-funnel source vs. mid-funnel nurture vs. conversion)
- Expected lead quality vs. volume tradeoff
- Priority: P1 (must-have) / P2 (high value) / P3 (nice-to-have)

Do not recommend a channel with no existing presence unless explicitly flagged as a new investment requiring setup.

### Step 2 — Qualification & scoring model
Define:
- **MQL criteria**: firmographic fit (from `Brand_Product_Offerings.md` ICP) + minimum engagement threshold
- **SQL criteria**: buying-intent signals that justify sales handoff
- **Scoring model**: simple point system across fit signals (title, company size, industry) and behavior signals (content downloads, page visits, email engagement) — weight fit higher than behavior for B2B unless the brand context indicates otherwise
- **Disqualification criteria**: what excludes a lead regardless of score (e.g. wrong company size, competitor, student/job-seeker noise)

### Step 3 — Lead routing
- Where MQLs go (marketing nurture vs. immediate sales notification)
- Where SQLs go (sales handoff — note this is a handoff point only; this skill does not own CRM/sales process)
- SLA expectations if known, or flag as TBD

### Step 4 — Nurture flow map
Map the funnel stage by stage:
- Stage name (e.g. ToFu capture → MoFu nurture → BoFu conversion)
- Trigger that moves a lead into this stage
- Content type needed at this stage (gated asset, email, retargeting ad, webinar — note which downstream skill produces it)
- Exit criteria (what moves them to the next stage or disqualifies them)

### Step 5 — Conversion benchmarks
Per stage, note an expected conversion rate range if industry/brand benchmarks exist in `Brand_Growth_Marketing_Context.md`; otherwise flag as `[TBD — no benchmark available, recommend a baseline test]`.

### Step 6 — Execution handoff
List which skill produces which downstream asset. Do not write this copy here:
- Gated asset (checklist/whitepaper/guide) → `lead-magnet` (owned by `content-creator`)
- Landing page → `lp-builder` (owned by `content-creator`)
- Nurture email sequence → `email-copy` (owned by `content-creator`)
- Paid amplification → `ad-creative`

## Output structure (`.md`)

Save as `output/reports/lead-gen-strategy-<topic>-<date>.md`:

```
# Lead Generation Strategy: [Topic/Offer]
Target ICP: [...]
Scope: [standalone / part of campaign — name campaign if applicable]
Date: [yyyy-mm-dd]

## Channel Mix
| Channel | Role | Quality/Volume tradeoff | Priority |
|---------|------|--------------------------|----------|

## Qualification & Scoring
MQL criteria: [...]
SQL criteria: [...]
Scoring model: [point table — fit signals, behavior signals]
Disqualification criteria: [...]

## Lead Routing
MQL routes to: [...]
SQL routes to: [...]
SLA: [...] or [TBD]

## Nurture Flow Map
| Stage | Trigger | Content type | Owning skill | Exit criteria |
|-------|---------|---------------|---------------|----------------|

## Conversion Benchmarks
| Stage | Expected conversion | Source |
|-------|----------------------|--------|

## Execution Handoff
| Asset | Skill to invoke |
|-------|------------------|
| Gated asset | lead-magnet |
| Landing page | lp-builder |
| Nurture sequence | email-copy |
| Paid amplification | ad-creative |
```

## Quality checklist

- [ ] Channel recommendations match current capability in `Brand_Growth_Marketing_Context.md` — new-channel investments explicitly flagged
- [ ] MQL/SQL criteria and scoring model trace to `Brand_Product_Offerings.md` ICP definitions, not invented
- [ ] Nurture flow map covers every stage from capture to conversion with no gaps
- [ ] Conversion benchmarks sourced or explicitly flagged `[TBD]`
- [ ] Execution handoff table correctly routes to `content-creator`-owned skills, not duplicated inline
- [ ] `.md` saved to `output/reports/`
