---
name: campaign-brief
description: >
  Use this skill whenever the user wants to create a campaign brief, plan a marketing campaign,
  or align stakeholders on a campaign strategy before execution begins. Trigger on requests
  like "create a campaign brief for X", "plan a campaign around Y", "brief out this campaign",
  "we need a campaign plan for Z", "build a campaign strategy for our insurance content push",
  or any request to document a campaign's goals, audience, channels, messaging, creative
  direction, and KPIs in one place. This is the starting point for any planned campaign —
  run this before ad-creative, blog-writer, social-copy, or lp-builder when launching
  something coordinated. Produces a structured `.md` and a `.docx` for stakeholder distribution.
---

# Campaign Brief

Creates the strategic campaign brief — the source-of-truth document that aligns all
stakeholders before a campaign is built. Covers goals, audience, channels, messaging,
creative direction, KPIs, and timeline. The `.md` feeds directly into downstream skills
(ad-creative, blog-writer, social-copy, lp-builder). The `.docx` is for distribution.

## Before starting

Read these context files every time:
- `_context/Brand_Growth_Marketing_Context.md` — active channels, funnel stages, campaign types,
  current growth focus areas
- `_context/Brand_Product_Offerings.md` — service lines, ICPs, differentiators, proof points
- `_context/Brand_Voice_Guide.md` — messaging principles, tone per channel, banned words

## Gather inputs

Ask the user for:
1. **Campaign goal:** What is this campaign trying to achieve? (Be specific — "increase MQLs from insurance COOs by 20%" not "generate leads")
2. **Service line:** Which product or service does this campaign support?
3. **Target ICP:** Who is the primary audience? (Role, vertical, company size, geography)
4. **Channels:** Which channels are in scope? (LinkedIn, Google, email, content, events, etc.)
5. **Timeline:** When does it launch? How long does it run?
6. **Budget:** Total and/or per-channel allocation (if known — optional)
7. **Existing assets:** Any content, case studies, or creative that already exists and can be used

If the user provides a market research or keyword research file, read it first — it informs
the audience, messaging, and channel strategy sections.

## Brief structure

### Section 1 — Campaign overview
One paragraph summary: what this campaign is, who it's for, what it's trying to achieve,
and why now. This is the "campaign in one breath" — anyone should be able to read this section
and understand the full intent.

### Section 2 — SMART goal
State the goal in SMART format:
- **Specific:** What exactly will this campaign produce?
- **Measurable:** What metric(s) will be tracked?
- **Achievable:** Is this realistic given the channel and timeline?
- **Relevant:** How does this goal connect to the business growth vectors in `Brand_Growth_Marketing_Context.md`?
- **Time-bound:** By when?

Example: "Generate 50 MQLs from insurance carriers (COO/VP Ops titles) in Australia and the
UK via LinkedIn Sponsored Content and Google Search, within 60 days of launch."

### Section 3 — Audience
Pull the ICP profile from `Brand_Product_Offerings.md`. Document:
- Primary ICP: role, company type, size, geography
- Pain points: what they're struggling with right now
- Buying triggers: what events or moments make them search for a solution
- Where they spend time: which channels and content types reach them
- What they need to believe before engaging: the key perception shifts this campaign must drive

### Section 4 — Channel strategy
For each channel in scope:
- **What it does in this campaign:** Awareness / consideration / conversion / retargeting
- **Why this channel for this ICP:** One sentence rationale
- **Funnel stage:** Top / middle / bottom
- **Content or asset needed:** What needs to be created for this channel
- **How it connects to other channels:** How does this channel hand off to the next step

Example channel table:

| Channel | Role | Funnel stage | Asset needed | Hands off to |
|---------|------|-------------|-------------|-------------|
| LinkedIn Sponsored Content | Awareness | Top | Carousel + 3 post variants | Google retargeting |
| Google Search | Capture intent | Bottom | 3 ad groups + landing page | Email nurture |
| Email nurture | Conversion | Bottom | 3-email sequence | Sales call |

### Section 5 — Messaging hierarchy
Document the messaging in order of priority:
1. **Primary message:** The single most important thing the audience must take away
2. **Supporting proof point 1:** The stat or credential that grounds the primary message
3. **Supporting proof point 2:** A second proof point (ideally different type — e.g., client outcome + analyst recognition)
4. **Supporting proof point 3:** A third if available
5. **CTA:** The specific action the audience is being asked to take at each funnel stage

All proof points must come from `_context/Brand_Product_Offerings.md` or user-provided data.

### Section 6 — Creative direction
Specify the creative approach for each asset type:
- **Visual style:** Recommend from `_context/Brand_Style_Reference.md`
  (select the style whose description best matches the content type and campaign tone; if the
  file doesn't exist yet, run `build-brand-style-reference` first)
- **Tone per channel:** Reference `Brand_Voice_Guide.md` tone table
- **Key visual concepts:** What should the imagery communicate (not the specific design, but the concept)
- **What not to do:** Any creative directions to avoid based on the audience and objective

### Section 7 — KPI framework
For each goal, specify:
- **Primary KPI:** The single number that determines if this campaign succeeded
- **Supporting metrics:** 2–3 metrics that explain the primary KPI (e.g., CTR, CPL, landing page CVR)
- **How it's measured:** Tool, attribution model, reporting frequency
- **Target values:** What does success look like numerically?

| KPI | Target | Measurement tool | Reporting cadence |
|-----|--------|-----------------|-------------------|

### Section 8 — Timeline and phases

| Phase | Activities | Duration | Owner |
|-------|-----------|----------|-------|
| Pre-launch | Asset creation, ad setup, audience build | [X weeks] | [team] |
| Launch | Go live, monitor daily, optimize bids | [X weeks] | [team] |
| Optimization | A/B test results, creative refresh if needed | [X weeks] | [team] |
| Wrap | Performance report, learnings, next campaign input | [X days] | [team] |

### Section 9 — Budget (if provided)
| Channel | Budget allocation | % of total |
|---------|-----------------|-----------|

If budget is not provided, note: "Budget TBD — allocate after channel strategy is confirmed."

### Section 10 — Assets needed
List every deliverable that needs to be created for this campaign, with which skill produces it:

| Asset | Skill to use | Priority | Status |
|-------|-------------|----------|--------|
| LinkedIn carousel | social-creative-designer | High | To do |
| Blog post | blog-writer | High | To do |
| Landing page | lp-builder | High | To do |
| Ad copy | ad-creative | Medium | To do |
| Social post copy | social-copy | Medium | To do |

## Output structure (`.md`)

Save as `output/reports/campaign-brief-<campaign>-<date>.md` with all 10 sections in order.

## Rich deliverable

After saving the `.md`, invoke `document-skills:docx` to produce a formatted Word document
for stakeholder distribution (team briefing, client sign-off, agency handoff).

The Word doc should use the same section structure. Invoke `branded-deck` if a presentation
version of the brief is also needed.

Save as `output/reports/campaign-brief-<campaign>-<date>.docx`

## Quality checklist

- [ ] SMART goal is specific, measurable, and time-bound — not vague ("generate awareness")
- [ ] Channel table explains why each channel is used — not just a list
- [ ] All proof points in messaging hierarchy sourced from `_context/` — nothing invented
- [ ] Assets needed table is complete — downstream skills know exactly what to build
- [ ] KPI targets are numeric — not "improve performance"
- [ ] Creative direction references specific styles from `_context/Brand_Style_Reference.md`
- [ ] Both `.md` and `.docx` saved to `output/reports/`
