---
name: build-brand-growth
description: >
  Use this skill to refresh or rebuild Brand_Growth_Marketing_Context.md only — without running
  a full brand onboarding. Trigger when: marketing channels, goals, or funnel metrics have
  changed, a new quarter's targets have been set, a channel has been added or dropped, or the
  file is missing while other context files are still valid. Accepts current performance data,
  a strategy brief, or user-provided direction as input. Does NOT touch any other _context\ file.
---

# Build Brand Growth

Refreshes `_context/Brand_Growth_Marketing_Context.md` — the marketing channels, funnel stages,
active goals, and performance baselines file. Use this when channel mix, targets, or funnel
benchmarks have changed and the growth context needs to reflect the current state.

## Scope — what this skill writes

This skill writes ONE file: `_context/Brand_Growth_Marketing_Context.md`.
It does NOT modify `Brand_Context.md`, `Brand_Voice_Guide.md`, `Brand_Style.md`,
`Brand_Product_Offerings.md`, or `Brand_Insights_Ledger.md`.

## Before starting

Read `_context/Brand_Context.md` for the brand's target verticals and ICPs — channel strategy
must be calibrated to where those buyers actually are.

Read `_context/Brand_Product_Offerings.md` for the product portfolio — different products often
have different channels, funnel shapes, and conversion benchmarks.

If `_context/Brand_Growth_Marketing_Context.md` already exists, read it first. Identify which
sections are stale (old targets, dropped channels, outdated metrics). Merge and update unless
the user requests a full rewrite.

## Clarify inputs

Ask the user:
1. **Current period:** What quarter/period does this growth context cover?
2. **Active channels:** Which channels are currently live? (SEO, LinkedIn, Google Ads, email, partnerships, events, etc.)
3. **Goals:** What are the primary marketing KPIs for this period? (MQLs, demo requests, pipeline value, traffic)
4. **Baselines:** Are there performance benchmarks available? (Current CTR, CPL, MQL volume, conversion rates)
5. **Funnel shape:** What does the funnel look like — stages, hand-off points to sales, average deal cycle?
6. **Budget context:** Is there a channel budget split to document? (Optional — mark as `[INTERNAL]` if sensitive)

If the user can't provide all of this, work from what's available and mark unknown fields as `[TBD]`.

## File structure to produce

Write `_context/Brand_Growth_Marketing_Context.md` with these sections:

```
# Brand Growth Marketing Context — [Company Name]
# Period: [Q? YYYY]

---

## Growth Objectives

| Objective | Target | Timeframe | Owner |
|-----------|--------|-----------|-------|
| [e.g., MQL volume] | [X per month] | [Q? YYYY] | [Marketing / SDR] |
| [e.g., Demo requests] | [X per month] | [Q? YYYY] | [Marketing] |
| [e.g., Organic traffic] | [X sessions/month] | [Q? YYYY] | [SEO / Content] |

Primary growth motion: [Inbound / Outbound / PLG / Partnership-led / Event-led — choose the dominant one]

---

## Funnel Architecture

### Funnel Stages
| Stage | Definition | Key Action | Owner |
|-------|-----------|-----------|-------|
| Awareness | [How prospects first encounter the brand] | [e.g., blog visit, ad impression] | Marketing |
| Interest | [How they signal interest] | [e.g., email sign-up, webinar register] | Marketing |
| Consideration | [How they enter the buying process] | [e.g., demo request, trial start] | Marketing / Sales |
| Decision | [How they convert] | [e.g., proposal reviewed, contract signed] | Sales |

### Funnel Benchmarks
| Stage Transition | Current Rate | Target Rate |
|-----------------|-------------|------------|
| Visitor → Lead | [X%] | [X%] |
| Lead → MQL | [X%] | [X%] |
| MQL → SQL | [X%] | [X%] |
| SQL → Closed Won | [X%] | [X%] |

Mark any unknown benchmarks as `[TBD — pull from CRM/analytics]`

### Average Deal Metrics
- Sales cycle length: [X days / weeks]
- Average contract value: [$ — mark as [INTERNAL] if sensitive]
- Lead-to-close time: [X days]

---

## Active Channels

For each active channel, write a block:

### Channel: [Name — e.g., LinkedIn Paid]

| Field | Value |
|-------|-------|
| Status | Active / Paused / Testing |
| Primary goal | [Awareness / Lead gen / Retargeting] |
| Target ICP | [Role @ company type] |
| Current CPL | [$ — or [TBD]] |
| Current CTR | [% — or [TBD]] |
| Monthly spend | [$ — or [INTERNAL]] |
| Top performing format | [Carousel / Single image / Video / Document] |
| Key message tested | [Headline or angle that has performed best] |
| Notes | [What's working, what's not, what to test next] |

---

Repeat the channel block for every active channel. Common channels to cover:
- SEO / Organic Search
- LinkedIn Paid
- Google Search Ads
- Google Display
- Email / Newsletter
- Content Marketing (blog, gated assets)
- Webinars / Events
- Partnerships / Affiliates
- Social Organic (LinkedIn, X, Instagram)
- Outbound / SDR-led

---

## Content & SEO Foundation

### Target keyword clusters
[3–5 topic clusters the brand is building content authority around.
Format: [Cluster name] — [primary keyword] — [monthly search volume estimate or TBD]]

### Content types in rotation
[Blog, case studies, whitepapers, webinars, video — list what is currently produced and at what cadence]

### Top performing content
[If known: title, URL, what makes it work. Otherwise: [TBD — pull from analytics]]

---

## CRM & Attribution

- CRM platform: [e.g., HubSpot, Salesforce]
- Marketing automation: [e.g., HubSpot, Marketo, ActiveCampaign]
- Attribution model: [First touch / Last touch / Multi-touch / Linear]
- Lead scoring in place: [Yes / No — brief description if yes]
- MQL definition: [The exact criteria that qualifies a lead as an MQL]

---

## Competitive Spend Context

[Brief note on what is known about competitor ad presence or content volume in the same channels.
If unknown: [TBD — run competitive research via market-researcher agent]]

---

## Open Questions & Gaps

[List any fields that are TBD, any channel hypothesis not yet tested, any funnel leak identified
but not yet addressed. This section is for the strategist reading this file to know what intelligence is still missing.]
```

## Quality rules

- Targets must be specific numbers, not ranges or vague goals. "20 MQLs/month" is useful. "More MQLs" is not.
- Mark any benchmark that hasn't been validated from actual data as `[UNVERIFIED — confirm from CRM/analytics]`.
- The MQL definition is mandatory — without it, campaign-strategist and data-analyst agents cannot set proper success criteria.
- Channel blocks must include "what's working / what to test next" — this is what the campaign-strategist consumes when planning the next quarter.

## Output

Save to: `_context/Brand_Growth_Marketing_Context.md`

After saving, report to the user:
- Which sections were updated vs. left unchanged
- How many `[TBD]` fields remain — and which ones block strategy or campaign planning
- Whether the funnel benchmarks are complete enough for the data-analyst agent to use

## Completion checklist

- [ ] File saved to exactly `_context/Brand_Growth_Marketing_Context.md` — no other `_context\` file modified
- [ ] Every target is a specific number — no ranges or vague goals
- [ ] MQL definition present (mandatory for campaign-strategist and data-analyst)
- [ ] Unvalidated benchmarks marked `[UNVERIFIED — confirm from CRM/analytics]`
- [ ] Every channel block includes "what's working / what to test next"
- [ ] Report delivered to the user: updates, remaining `[TBD]` count and which block planning, benchmark completeness
