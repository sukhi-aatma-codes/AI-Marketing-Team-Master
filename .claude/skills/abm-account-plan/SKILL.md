---
name: abm-account-plan
description: >
  Use this skill when a campaign is account-based (ABM) rather than broad-audience —
  targeting a named list of accounts or a tight account segment instead of a general ICP.
  Trigger on requests like "build an ABM plan for these 20 accounts", "we need account
  tiering for our enterprise target list", "map stakeholders at [account]", or when
  campaign-strategist's Campaign Brief Summary sets campaign type = ABM. Produces account
  tiering, fit/opportunity/accessibility scoring, a stakeholder map template, and
  tier-specific messaging angles. Does not write execution copy — hands off to
  ad-creative, social-copy, email-copy, and lp-builder for that.
---

# ABM Account Plan

Produces the account-level targeting layer that sits beneath a broader campaign strategy:
which accounts to target, how to tier them, who the stakeholders are, and what messaging
angle each tier gets. This is a planning document — personalized execution assets (ads,
emails, landing pages) are built afterward by other skills using this plan as the brief.

## Before starting

Read these context files every time:
- `_context/Brand_Product_Offerings.md` — ICPs, service lines, differentiators (defines account fit criteria)
- `_context/Brand_Context.md` — positioning, company overview
- `_context/Brand_Insights_Ledger.md` Section 1 — confirmed buyer personas, objections, and any prior ABM learnings

## Clarify inputs first

Confirm:
1. **Target list or segment**: A named account list, or a segment definition (industry + size + signal) to build a list against
2. **Account count**: Determines tiering approach — under ~10 accounts can go 1:1, 10–50 suits 1:few clustering, 50+ needs 1:many systemization
3. **Primary objective**: New logo acquisition, expansion within existing accounts, or competitive displacement
4. **Known relationships**: Any existing contacts, referral paths, or sales conversations already in motion at these accounts
5. **Timeline**: When personalized campaigns need to be live

## Workflow

### Step 1 — Account tiering
Classify the account list (or segment) into one of:
- **1:1** — fully bespoke campaigns per account (reserve for highest-value, lowest-count targets)
- **1:few** — clustered personalization for accounts sharing industry/use-case/size characteristics
- **1:many** — systemized personalization (dynamic fields, segment-level messaging) for the broader list

State the tiering rationale per account or cluster — don't default to 1:1 just because the user asked for ABM.

### Step 2 — Fit, opportunity, and accessibility scoring
For each account or cluster, score against:
- **Fit**: ICP alignment from `Brand_Product_Offerings.md` (industry, size, technographic signals)
- **Opportunity**: Revenue/expansion potential, strategic value
- **Accessibility**: Existing relationships, referral paths, known champions
- **Timing**: Any known buying signals, budget cycles, or active initiatives

Flag accounts that score low on fit despite being on the target list — note as `[ASSUMPTION — confirm this account belongs in scope]`.

### Step 3 — Stakeholder map
For each account or representative account-per-cluster, map:
- **Decision maker(s)**: budget authority
- **Influencer(s)**: technical/functional evaluators
- **Champion(s)**: internal advocate, if known
- **Blocker(s)**: likely resistance points, if known

If stakeholder names/titles aren't known, provide a role-based template the user can fill in rather than inventing names.

### Step 4 — Tier-specific messaging angles
For each tier (or cluster), define:
- The hero message angle for that tier (must trace back to `Brand_Product_Offerings.md` positioning — no invented differentiators)
- Why this angle fits this tier specifically (not generic campaign messaging)
- Proof points to use, sourced from `_context\` — mark any gap as `[TBD — proof point needed]`

### Step 5 — Execution handoff
List, per tier, which skill produces which asset. Do not write this copy here:
- Account-targeted ad copy → `ad-creative`
- Account-targeted LinkedIn/social content → `social-copy`
- Account email sequences → `email-copy`
- Account-specific landing pages → `lp-builder`

## Output structure (`.md`)

Save as `output/reports/abm-account-plan-<segment>-<date>.md`:

```
# ABM Account Plan: [Segment/List Name]
Objective: [new logo / expansion / displacement]
Account count: [N]
Date: [yyyy-mm-dd]

## Tiering Summary
| Tier | Accounts/Clusters | Personalization level | Rationale |
|------|-------------------|------------------------|-----------|

## Account Scoring
| Account/Cluster | Fit | Opportunity | Accessibility | Timing | Priority |
|------------------|-----|-------------|----------------|--------|----------|

## Stakeholder Map — [Account or Cluster]
| Role | Title/Function | Influence | Notes |
|------|-----------------|-----------|-------|

## Tier Messaging
### Tier [name]
Hero angle: [...]
Why it fits: [...]
Proof points: [...] or [TBD]

## Execution Handoff
| Asset | Tier(s) | Skill to invoke |
|-------|---------|------------------|
| Account ad copy | ... | ad-creative |
| Account social content | ... | social-copy |
| Account email sequence | ... | email-copy |
| Account landing page | ... | lp-builder |
```

## Quality checklist

- [ ] Tiering rationale stated per account/cluster — not a blanket 1:1 default
- [ ] Every fit/opportunity score traces to `Brand_Product_Offerings.md`, not assumption
- [ ] Stakeholder maps use role templates where names aren't confirmed — no invented names
- [ ] Every messaging angle and proof point is sourced or flagged `[TBD]`
- [ ] Execution handoff table lists the correct owning skill for every asset type
- [ ] `.md` saved to `output/reports/`
