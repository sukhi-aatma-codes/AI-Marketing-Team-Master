# How to Use Foundry Collective

A practical reference for everything this workspace can do: 13 agents, 37 skills, one example
prompt for each. If you've never used this workspace before, read **Orientation** first. If
you already know the system and just need a prompt to copy, jump straight to the **Agent
Catalog** or **Skill Catalog** below.

---

## Orientation

**Foundry Collective** is the user's personal marketing operating system — it functions as their
marketing department wherever they work. (The workspace directory/path is still named
`AI Marketing Team Master` — that's the technical folder name; Foundry Collective is what the
system is called in conversation.) It does nothing employer-specific until `_context\` is
populated — six `Brand_*.md` files plus a shared `Brand_Insights_Ledger.md` define who the
employer/brand is, how it talks, what it sells, who it sells to, and what its visuals look like.
Every agent and skill reads those files at runtime instead of assuming a brand identity.

**If `_context\` is empty or you're starting at a new organization**, your first prompt is
always to `brand-onboarder` — nothing else in this guide works correctly until that's done.

**For bulk raw materials** (a folder of 20+ ads, decks, or images), drop them in `_samples\`
and run `sample-archive-index` first — it triages files to the right deep-extraction skill
(`build-brand-style` for decks, `build-brand-style-reference` for image creative) instead of
reading everything blind.

**The one rule that decides where to start:**

> **Single, bounded deliverable with a clear brief → invoke a skill directly.**
> **Open-ended, multi-step, or needs judgment across formats → delegate to an agent.**

"Write a blog post on X" is a skill call (`blog-writer`). "We're launching X and need a content
push" is an agent call (`content-creator`, which decides which skills to run and in what order).
When in doubt, start with the agent — agents invoke the right skills for you.

---

## Workflow Diagram

### 1. System layers

```
┌──────────────────────────────────────────────────────────────────┐
│  _context\  —  the brand's "brain", read at runtime               │
│  Brand_Context · Brand_Voice_Guide · Brand_Style ·                 │
│  Brand_Product_Offerings · Brand_Growth_Marketing_Context ·        │
│  Brand_Style_Reference  (visual style library + prompt starters,   │
│  built once real creative samples exist) ·                        │
│  Brand_Insights_Ledger  (shared cross-agent memory, grows over     │
│  time as agents confirm what works)                                │
└───────────────────────────────┬────────────────────────────────────┘
                                 │ loaded by every agent/skill before
                                 │ producing anything brand-facing
                                 ▼
┌──────────────────────────────────────────────────────────────────┐
│  13 AGENTS  (.claude/agents\)  —  orchestration + judgment         │
│                                                                      │
│  brand-onboarder      campaign-strategist     market-researcher    │
│  content-creator      creative-designer       data-analyst         │
│  seo-specialist       ai-citation-strategist  pr-comms              │
│  social-strategist    podcast-strategist                            │
│  lead-generation-engine                webinar-strategist           │
└───────────────────────────────┬────────────────────────────────────┘
                                 │ invokes via the Skill tool
                                 ▼
┌──────────────────────────────────────────────────────────────────┐
│  37 SKILLS  (.claude\skills\)  —  single-purpose execution modules │
│  blog-writer · social-copy · ad-creative · lp-builder ·             │
│  lead-magnet · email-copy · keyword-research · market-research ·    │
│  campaign-brief · branded-deck · abm-account-plan ·                 │
│  lead-gen-strategy · webinar-plan · technical-seo-audit ·           │
│  on-page-optimization · aeo-foundations · citation-audit ·          │
│  press-release · media-pitch · crisis-response ·                    │
│  executive-thought-leadership · social-strategy ·                   │
│  social-creative-designer · podcast-episode-plan ·                  │
│  podcast-show-notes · campaign-report · data-visualization ·        │
│  build-brand-context · build-brand-voice · build-brand-style ·      │
│  build-brand-products · build-brand-growth ·                        │
│  build-brand-style-reference · sample-archive-index ·               │
│  build-brand-deck-template · image · copy-editing  (37 total)       │
└───────────────────────────────┬────────────────────────────────────┘
                                 │ writes finished, deliverable files
                                 ▼
┌──────────────────────────────────────────────────────────────────┐
│  OUTPUT DIRECTORIES  —  under output\, organized by type         │
│  output\ads\           output\pages\          output\presentations\│
│  output\reports\       output\seo\            output\social\       │
│  output\pr\            output\email\          output\podcasts\     │
│  output\webinars\      output\ideogram_output\                     │
└──────────────────────────────────────────────────────────────────┘
```

### 2. Common pipelines (agent → agent / skill → output)

```
NEW BRAND
  brand-onboarder ──→ _context\ (6 files + ledger) ──→ everything else unlocked

BULK SAMPLE DROP (20+ files in _samples\)
  sample-archive-index ──→ _samples\INDEX.md
       ├─→ decks tagged for style ──→ build-brand-style (deck-extraction) ──→ _context\
       │                                  └─→ build-brand-deck-template  ──→ _templates\
       └─→ image creative tagged  ──→ build-brand-style-reference        ──→ _context\

CAMPAIGN LAUNCH (full)
  campaign-strategist ──┬─→ content-creator ────→ output\pages\ output\social\ output\email\
                         └─→ creative-designer ──→ output\ads\ output\social\

ABM CAMPAIGN
  campaign-strategist (+ abm-account-plan skill) ──→ output\reports\
       │
       └─→ creative-designer + content-creator (personalized assets) ──→ output\ads\ output\social\ output\email\ output\pages\

LEAD-GEN FUNNEL BUILD
  lead-generation-engine ──→ output\reports\ (funnel architecture)
       │
       └─→ content-creator (lead magnet + landing page + nurture) ──→ output\pages\ output\email\

WEBINAR PROGRAM
  webinar-strategist ──→ output\webinars\ (plan)
       │
       ├─→ content-creator (promotion + follow-up) ──→ output\social\ output\email\ output\pages\
       └─→ social-strategist (promotion calendar slotting)

SEO CONTENT PUSH
  market-researcher ──→ content-creator (blog-writer + lp-builder) ──→ output\pages\

SEO OVERHAUL → AI VISIBILITY PUSH
  seo-specialist ──→ content-creator (gap execution) ──→ output\pages\
  seo-specialist (aeo-foundations) ──→ ai-citation-strategist ──→ output\seo\

PR CAMPAIGN
  pr-comms ──┬─→ content-creator ──→ output\pages\ output\social\
             └─→ social-strategist (amplification) ──→ output\social\

PODCAST LAUNCH
  podcast-strategist ──┬─→ content-creator (repurpose) ──→ output\pages\ output\social\
                        └─→ social-strategist (promote)

PERFORMANCE REVIEW
  data-analyst ──→ output\reports\ ──→ feeds next campaign-strategist cycle
```

---

## The Example Brand

Every prompt below appears in two forms: a **concrete version** using a fictional B2B SaaS
brand, and a **generic version** with bracketed placeholders you can drop your real brand
into. The fictional brand:

> **Veloxa** — a cloud cost optimization (FinOps) platform for engineering and finance teams
> managing $1M+ in annual cloud spend. ICP: VP Engineering, Head of Platform/Infrastructure,
> and CFO/Finance Ops leaders at mid-market to enterprise companies (200–5,000 employees).

This is illustrative only — Veloxa has no `_context\` files in this workspace. To run these
prompts for real, either onboard Veloxa with `brand-onboarder` first, or substitute your own
brand (already onboarded) wherever you see "Veloxa."

---

## Agent Catalog (13)

Each entry: what it does, when to delegate vs. use a skill directly, what it owns/hands off to,
where output lands, and an example prompt pair.

### 1. `brand-onboarder` 🩵
**Does:** Scrapes a brand URL or materials and builds all six `_context\` files plus seeds the
Brand Insights Ledger. If `_samples\` has raw materials, triages them first via
`sample-archive-index` and routes decks/images to the deep-extraction skills. Runs once per
brand engagement — not a recurring tool.
**Delegate when:** Onboarding a new brand from scratch, or switching the active brand entirely.
**Don't delegate when:** Only one context file needs a partial refresh — use the relevant
`build-brand-*` skill instead.
**Output:** `_context\` (all 6 files + ledger)
> 🟦 *"We just signed Veloxa (veloxa.io) as a new client. Onboard them and build out the full brand context."*
> ⬜ *"We're starting work with a new brand at [URL]. Onboard them and set up all the context files."*

### 2. `campaign-strategist` 🟣
**Does:** Turns an objective, audience, or product brief into a full Campaign Strategy
Document — positioning, messaging hierarchy, channel plan, paid media plan, deliverable specs,
KPIs. Owns ABM account planning internally (no separate ABM agent).
**Delegate when:** A campaign, launch, or demand-gen program needs to be mapped end to end.
**Don't delegate when:** The strategy already exists and you just need one asset — go straight
to `content-creator`/`creative-designer`, or the `campaign-brief` skill for a standalone brief doc.
**Owns:** `campaign-brief`, `branded-deck`, `abm-account-plan` · **Hands off to:** `content-creator`,
`creative-designer`, `seo-specialist`, `ai-citation-strategist`, `pr-comms`, `social-strategist`,
`podcast-strategist`, `lead-generation-engine` · **Output:** `output\reports\`
> 🟦 *"We're launching Veloxa's new Kubernetes cost-anomaly detection feature next quarter, targeting VP Engineering at mid-market SaaS companies. Build the campaign strategy."*
> ⬜ *"We're launching [new feature] for [ICP] next quarter. Build the campaign strategy."*

### 3. `market-researcher` 🔵
**Does:** Combines competitive intelligence and keyword/search-demand research into one
structured intelligence pass.
**Delegate when:** You need competitive positioning AND search demand together, before a
campaign or content strategy.
**Don't delegate when:** You only need one or the other — invoke `market-research` or
`keyword-research` directly.
**Owns:** `market-research`, `keyword-research` · **Hands off to:** `campaign-strategist`,
`content-creator`, `seo-specialist` · **Output:** `output\reports\`
> 🟦 *"Who's competing with Veloxa in the cloud cost optimization space, and what are engineering leaders actually searching for around 'cloud cost management'?"*
> ⬜ *"Who's competing with us in [category], and what is [ICP] actually searching for around [topic]?"*

### 4. `content-creator` 🟢
**Does:** Produces publish-ready content across formats — blog, social, lead magnets, landing
pages, email — with brand voice compliance and platform-correct formatting.
**Delegate when:** Multiple formats are needed for one campaign/topic, or the brief is open
enough to need format judgment.
**Don't delegate when:** You want one specific format with a clear brief — go straight to
`blog-writer`, `social-copy`, `lp-builder`, `lead-magnet`, or `copy-editing` (to edit existing copy).
**Owns:** `blog-writer`, `social-copy`, `lead-magnet`, `lp-builder`, `email-copy`, `copy-editing` ·
**Hands off to:** `creative-designer`, `social-strategist`, `seo-specialist`, `pr-comms` ·
**Output:** `output\pages\`, `output\social\`, `output\email\`
> 🟦 *"We're launching the cost-anomaly detection feature next week. I need a blog post, a LinkedIn post, and a landing page for it."*
> ⬜ *"We're launching [feature] next week. I need a blog post, a LinkedIn post, and a landing page for it."*

### 5. `creative-designer` 🟡
**Does:** Turns a campaign brief into visual direction and platform-specific creative specs —
ad creatives, social graphics — with copy and visual layer coordinated.
**Delegate when:** Visual direction needs defining across multiple platforms/formats together.
**Don't delegate when:** One specific graphic with a clear brief is needed — use
`social-creative-designer` directly; copy-only ad text — use `ad-creative` directly; a
general-purpose image (blog hero, OG image, banner, mockup) — use `image` directly.
**Owns:** `ad-creative`, `social-creative-designer`, `image` · **Output:** `output\ads\`, `output\social\`, `output\pages\`
> 🟦 *"We're launching cost-anomaly detection on LinkedIn and Google Display. I need ad creatives across both platforms."*
> ⬜ *"We're launching [feature] on [platforms]. I need ad creatives across both."*

### 6. `data-analyst` 🟠
**Does:** Turns raw or multi-source campaign data into insights, anomaly analysis, and
executive-ready visual reports.
**Delegate when:** The analysis goal is open-ended ("make sense of this," "what's driving the
drop") or both analysis and visualization are needed.
**Don't delegate when:** You already know what chart you want from interpreted data — use
`data-visualization` directly; or you want a formatted report with no analysis judgment — use
`campaign-report` directly.
**Owns:** `campaign-report`, `data-visualization` · **Output:** `output\reports\`
> 🟦 *"Here's the export from Veloxa's Q2 LinkedIn and Google Ads campaigns. What's driving the cost-per-lead increase?"*
> ⬜ *"Here's our Q2 campaign data export. What's driving [the anomaly]?"*

### 7. `seo-specialist` 🔵
**Does:** Manages technical SEO health, on-page optimization, and AI-crawler foundations
(robots.txt, llms.txt).
**Delegate when:** Auditing technical SEO health, fixing crawl/indexation issues, or optimizing
a specific page.
**Don't delegate when:** Only keyword research is needed — use `keyword-research` directly; or
general competitor messaging is in scope — use `market-researcher`.
**Owns:** `technical-seo-audit`, `on-page-optimization`, `aeo-foundations` · **Hands off to:**
`content-creator` · **Output:** `output\seo\`
> 🟦 *"Veloxa's organic traffic has been flat for two months. Audit our technical SEO and tell us what to fix."*
> ⬜ *"Our organic traffic has been flat. Audit our technical SEO and tell us what to fix."*

### 8. `ai-citation-strategist` 🟣
**Does:** Audits brand visibility and citation patterns across ChatGPT, Claude, Gemini, and
Perplexity; produces fix packs to improve recommendation likelihood.
**Delegate when:** You need to know why AI engines recommend competitors instead of you, or
want a citation share-of-voice scorecard.
**Don't delegate when:** The issue is traditional crawl/indexation/Core Web Vitals — use
`seo-specialist`.
**Owns:** `citation-audit` (also uses `aeo-foundations`) · **Output:** `output\seo\`
> 🟦 *"I asked ChatGPT for the best cloud cost optimization tool for enterprise and it only mentioned our competitors. Why, and how do we fix it?"*
> ⬜ *"I asked ChatGPT for [category] and it only mentioned competitors. Why, and how do we fix it?"*

### 9. `pr-comms` 🔵
**Does:** Coordinates earned media — AP-style press releases, journalist pitches, crisis
playbooks, executive thought leadership.
**Delegate when:** Drafting a wire-ready press release, a media pitch, a crisis response plan,
or ghostwriting executive content.
**Don't delegate when:** It's customer-facing blog/social/landing page copy — use `content-creator`.
**Owns:** `press-release`, `media-pitch`, `crisis-response`, `executive-thought-leadership` ·
**Output:** `output\pr\`
> 🟦 *"Veloxa just closed a $20M Series B. Draft a press release and a pitch for the top 5 cloud infrastructure journalists."*
> ⬜ *"We just closed [milestone]. Draft a press release and a pitch for [target journalists]."*

### 10. `social-strategist` 🔵
**Does:** Plans multi-platform organic social growth — content calendars, channel
prioritization, visual spec sheets.
**Delegate when:** Designing a content calendar or cross-platform growth play.
**Don't delegate when:** You want copy for one specific post — use `social-copy` directly; or a
single visual layout spec — use `social-creative-designer` directly.
**Owns:** `social-strategy` (also uses `social-copy`, `social-creative-designer`) ·
**Hands off to:** `creative-designer`, `content-creator` · **Output:** `output\social\`
> 🟦 *"Plan Veloxa's social calendar for next month — we want to highlight our new cost-anomaly detection customers."*
> ⬜ *"Plan our social calendar for next month — we want to highlight [theme]."*

### 11. `podcast-strategist` 🟣
**Does:** Plans podcast episodes end to end — guest research, run-of-show, scripts, show notes,
repurposing.
**Delegate when:** Structuring a guest interview, drafting an episode plan, or synthesizing a
transcript into show notes.
**Don't delegate when:** It's a standard blog post from a general topic — use `content-creator`.
**Owns:** `podcast-episode-plan`, `podcast-show-notes` · **Hands off to:** `content-creator` ·
**Output:** `output\podcasts\`
> 🟦 *"We have the VP of Infrastructure at a major fintech coming on the show next week to talk cloud cost governance. Research her and draft the questions."*
> ⬜ *"We have [guest], [title] at [company], coming on the show to talk about [topic]. Research them and draft the questions."*

### 12. `lead-generation-engine` 🟦 (indigo)
**Does:** Designs the architecture of a lead-gen funnel — channel mix, MQL/SQL qualification,
scoring model, nurture flow map. Does not write the gated asset/landing page/emails itself.
**Delegate when:** Building a funnel from scratch, or fixing a qualification problem ("we're
getting leads but they're junk").
**Don't delegate when:** A funnel/qualification model already exists and you just need one
asset — go to `content-creator` directly.
**Owns:** `lead-gen-strategy` · **Hands off to:** `content-creator`, `campaign-strategist` (if
part of a larger campaign) · **Output:** `output\reports\`
> 🟦 *"We need a lead gen funnel for Veloxa's new mid-market tier — right now we just have a contact form and no qualification process."*
> ⬜ *"We need a lead gen funnel for [offer/tier] — right now we just have a contact form and no qualification process."*

### 13. `webinar-strategist` 🔴 (crimson)
**Does:** Plans a webinar program end to end — concept, agenda, speaker brief, promotion
timeline, registration brief, attendee/no-show follow-up.
**Delegate when:** Planning a webinar from concept through follow-up, or structuring
post-event follow-up for an already-run event.
**Don't delegate when:** A webinar plan already exists and you just need promotion copy or a
registration page — go to `content-creator` directly.
**Owns:** `webinar-plan` · **Hands off to:** `content-creator`, `social-strategist`, `creative-designer` ·
**Output:** `output\webinars\`
> 🟦 *"We want to run a webinar on cutting Kubernetes spend by 30% for mid-market platform teams next month. Plan it out."*
> ⬜ *"We want to run a webinar on [topic] for [ICP] next month. Plan it out."*

---

## Skill Catalog (34)

Grouped by the agent that primarily owns each skill. Invoke any of these directly when you
have a single, bounded deliverable and a clear brief.

### Brand Foundation Maintenance *(invoked directly — no owning agent; use `brand-onboarder` only for a full rebuild)*

**`sample-archive-index`** — Triage manifest for bulk `_samples\` drops (20+ files); routes
each to the right deep-extraction skill. Produces no brand truth itself.
> 🟦 *"I just dropped 40 old Veloxa ad creatives and a few decks into _samples. Index them."*
> ⬜ *"I just dropped a folder of old ads and decks into _samples. Index them."*
Output: `_samples\INDEX.md`

**`build-brand-context`** — Refreshes `Brand_Context.md` (positioning, ICPs, company overview).
> 🟦 *"Veloxa just repositioned around FinOps governance, not just cost visibility. Update our brand context."*
> ⬜ *"We repositioned around [new angle]. Update our brand context file."*
Output: `_context\Brand_Context.md`

**`build-brand-voice`** — Refreshes `Brand_Voice_Guide.md` (tone, banned jargon, writing rules).
> 🟦 *"Veloxa's new CMO wants a sharper, less corporate tone. Update our voice guide."*
> ⬜ *"Our tone is shifting — update our brand voice guide."*
Output: `_context\Brand_Voice_Guide.md`

**`build-brand-style`** — Refreshes `Brand_Style.md` (colors, typography, visual grid). When a
source deck is provided, extracts exact colors/fonts/layout from the slide XML rather than
visually skimming.
> 🟦 *"Veloxa just rebranded — here's the new style guide PDF. Update our brand style file."*
> ⬜ *"We just updated our visual identity — here's the style guide. Rebuild our brand style file."*
Output: `_context\Brand_Style.md`

**`build-brand-style-reference`** — Generates/refreshes `Brand_Style_Reference.md`, the
generative visual style library (named styles + Flux/Ideogram prompt starters) consumed by
`social-creative-designer`, `ad-creative`, `campaign-brief`, and `lead-magnet`.
> 🟦 *"Here are 15 of Veloxa's past LinkedIn graphics. Build our brand style reference from them."*
> ⬜ *"Here are our past social/ad creative samples. Build our brand style reference from them."*
Output: `_context\Brand_Style_Reference.md`

**`build-brand-deck-template`** — Builds/refreshes the actual reusable `.pptx` deck template
`branded-deck` assembles new presentations from (not just a markdown description).
> 🟦 *"We just analyzed Veloxa's sales deck for style — now build the real template file from it."*
> ⬜ *"We just analyzed our sales deck for style — now build the real template file from it."*
Output: `_templates\Brand_Deck_Template.pptx` + `_templates\Brand_Deck_Template_Analysis.md`

**`build-brand-products`** — Refreshes `Brand_Product_Offerings.md` (services, ICPs, pain points).
> 🟦 *"Veloxa just launched a new Kubernetes cost-anomaly detection tier. Add it to our product offerings."*
> ⬜ *"We just launched [new product/tier]. Add it to our product offerings file."*
Output: `_context\Brand_Product_Offerings.md`

**`build-brand-growth`** — Refreshes `Brand_Growth_Marketing_Context.md` (channels, funnel, goals).
> 🟦 *"Veloxa's Q3 targets and channel mix changed — update our growth marketing context."*
> ⬜ *"Our quarterly targets and channel mix changed — update our growth context file."*
Output: `_context\Brand_Growth_Marketing_Context.md`

### Campaign Strategy *(owned by `campaign-strategist`)*

**`campaign-brief`** — Standalone stakeholder-facing campaign brief document.
> 🟦 *"Create a standalone campaign brief for Veloxa's cost-anomaly detection launch I can send to our agency."*
> ⬜ *"Create a standalone campaign brief for [launch] I can send to [stakeholder]."*
Output: `output\reports\campaign-brief-<campaign>-<date>.md` + `.docx`

**`branded-deck`** — On-brand presentation deck (strategy, sales, internal). Builds from
`_templates/Brand_Deck_Template.pptx` — if that's missing, run `build-brand-deck-template` first.
> 🟦 *"Turn Veloxa's Q3 campaign strategy into a 10-slide deck for the leadership review."*
> ⬜ *"Turn this campaign strategy into a [N]-slide deck for [audience]."*
Output: `output\presentations\<topic>-<date>.pptx` (+ `.pdf`)

**`abm-account-plan`** — Account tiering, fit/opportunity scoring, stakeholder maps for ABM.
> 🟦 *"Build an ABM plan for our top 20 target accounts in fintech infrastructure."*
> ⬜ *"Build an ABM plan for [target account list/segment]."*
Output: `output\reports\abm-account-plan-<segment>-<date>.md`

### Market Research

**`market-research`** — Competitive landscape analysis, buyer signals, strategic implications.
> 🟦 *"Research the cloud cost optimization / FinOps competitive landscape for Veloxa."*
> ⬜ *"Research the competitive landscape for [category]."*
Output: `output\reports\research-<topic>-<date>.md` + `.pdf`

**`keyword-research`** — Keyword identification, SERP analysis, journey-stage mapping. *(also
used by `seo-specialist`)*
> 🟦 *"Do keyword research for 'cloud cost optimization' and 'FinOps platform.'"*
> ⬜ *"Do keyword research for [topic/category]."*
Output: `output\seo\keywords-<topic>-<date>.md` + `.docx`

### Content Creation *(owned by `content-creator`)*

**`blog-writer`** — Fully SEO/AEO-optimized, upload-ready blog posts.
> 🟦 *"Write a 1,200-word blog post on why platform teams are switching from manual tagging to automated cloud cost anomaly detection."*
> ⬜ *"Write a [N]-word blog post on [topic] for [ICP]."*
Output: `output\pages\blog-<slug>-<date>.md` + `.html` + `.docx`

**`social-copy`** — Platform-specific post copy with hook/body/CTA variants. *(also used by
`social-strategist`)*
> 🟦 *"Write 3 LinkedIn posts and 3 X posts promoting Veloxa's new cost-anomaly detection feature."*
> ⬜ *"Write [N] LinkedIn posts and [N] X posts promoting [asset/feature]."*
Output: `output\social\copy-<topic>-<date>.md` + `.docx`

**`lead-magnet`** — Format/buyer-stage/gating strategy + content for gated assets: checklists,
guides, toolkits, self-assessments. Now includes a distribution and measurement plan, not just
the written piece.
> 🟦 *"Create a lead magnet — a Kubernetes cost-audit checklist — for platform engineering leads."*
> ⬜ *"Create a lead magnet — a [format] — on [topic] for [ICP]."*
Output: `output\pages\lead-magnet-<topic>-<date>.md` + `.pdf`

**`lp-builder`** — Conversion-focused landing pages.
> 🟦 *"Build a landing page for our free cloud cost audit offer targeting platform engineering teams."*
> ⬜ *"Build a landing page for [offer] targeting [ICP]."*
Output: `output\pages\lp-<slug>-<date>.md` + `.html`

**`email-copy`** — Welcome, nurture, promotional, or cold outreach sequences.
> 🟦 *"Write a 5-email nurture sequence for people who downloaded our Kubernetes cost-audit checklist."*
> ⬜ *"Write a [N]-email nurture sequence for [lead magnet/offer] downloaders."*
Output: `output\email\sequence-<topic>-<date>.md` + `.docx`

**`copy-editing`** — Seven Sweeps edit pass (Clarity → Voice/Tone → So What → Prove It →
Specificity → Heightened Emotion → Zero Risk) plus expert panel scoring for high-stakes copy.
For editing copy that already exists, not writing new copy.
> 🟦 *"Review and tighten up our cost-anomaly detection landing page copy — it reads a bit flat."*
> ⬜ *"Review and tighten up [existing page/copy] — it reads a bit flat."*
Output: `edit-<topic>-<date>.md`, saved to the source content's folder

### Creative Design *(owned by `creative-designer`)*

**`ad-creative`** — Character-count-verified ad copy variant matrices (Google, LinkedIn, display).
> 🟦 *"Write Google Search and LinkedIn ad copy for our cost-anomaly detection landing page."*
> ⬜ *"Write [platform] ad copy for [landing page/offer]."*
Output: `output\ads\ad-creative-<campaign>-<date>.md`

**`image`** — General-purpose marketing images: blog heroes, OG/social preview images,
profile/directory banners, product mockups, image optimization. Distinct from
`social-creative-designer` (LinkedIn carousels) and `ad-creative` (paid ad specs).
> 🟦 *"Generate a hero image for our blog post on Kubernetes cost anomalies, and an OG image for the same page."*
> ⬜ *"Generate a hero image for [blog post], and an OG image for the same page."*
Output: `output\pages\` (blog hero/OG), `output\social\` (banners), routed by asset type per the skill's table

**`social-creative-designer`** — Social graphics and LinkedIn carousels (Ideogram + Canva).
*(also used by `social-strategist`)*
> 🟦 *"Create a LinkedIn carousel explaining how cloud cost anomalies get missed without automated detection."*
> ⬜ *"Create a [carousel/graphic] explaining [concept] for [platform]."*
Output: `output\social\social-<topic>-slide-<N>-<date>.png`

### Data & Reporting *(owned by `data-analyst`)*

**`campaign-report`** — Performance reports with insights, benchmarking, recommendations.
> 🟦 *"Pull together a performance report on Veloxa's Q2 paid campaigns."*
> ⬜ *"Pull together a performance report on [campaign/period]."*
Output: `output\reports\campaign-report-<name>-<date>.md` + `.xlsx` + `.pptx` + `.pdf`

**`data-visualization`** — Branded interactive charts and static visualizations.
> 🟦 *"Turn this funnel conversion data into a visualization for the leadership deck."*
> ⬜ *"Turn this [data] into a visualization for [audience]."*
Output: `output\reports\dataviz-<topic>-<date>.html` + `.py`

### SEO & AEO *(owned by `seo-specialist`)*

**`technical-seo-audit`** — Crawlability, indexation, Core Web Vitals, structured data audit.
> 🟦 *"Run a technical SEO audit on veloxa.io — we suspect crawl issues."*
> ⬜ *"Run a technical SEO audit on [domain] — we suspect [issue]."*
Output: `output\seo\technical-seo-audit-<date>.md` + `.pdf`

**`on-page-optimization`** — Page-specific copy/HTML optimization for a target keyword.
> 🟦 *"Optimize our /cloud-cost-optimization page for the keyword 'cloud cost optimization platform.'"*
> ⬜ *"Optimize [page] for the keyword [target keyword]."*
Output: `output\seo\on-page-<page-slug>-<date>.md` + `.docx`

**`aeo-foundations`** — AI crawler rules, robots.txt, llms.txt maps. *(also used by
`ai-citation-strategist`)*
> 🟦 *"Audit veloxa.io's readiness for AI crawlers and build us an llms.txt."*
> ⬜ *"Audit [domain]'s readiness for AI crawlers and build an llms.txt."*
Output: `output\seo\aeo-foundations-audit-<date>.md`

### AI Citation *(owned by `ai-citation-strategist`)*

**`citation-audit`** — Brand visibility/citation scorecard across ChatGPT, Claude, Gemini, Perplexity.
> 🟦 *"Run a citation audit — are we showing up when people ask AI tools for the best cloud cost optimization platform?"*
> ⬜ *"Run a citation audit for [category] across the major AI engines."*
Output: `output\seo\citation-audit-<date>.md`

### PR & Comms *(owned by `pr-comms`)*

**`press-release`** — AP-style wire-ready press releases.
> 🟦 *"Write a press release announcing Veloxa's $20M Series B."*
> ⬜ *"Write a press release announcing [milestone/news]."*
Output: `output\pr\press-release-<topic>-<date>.md` + `.docx`

**`media-pitch`** — Personalized journalist pitch emails.
> 🟦 *"Draft a pitch to the lead infrastructure reporter at TechCrunch about our Series B."*
> ⬜ *"Draft a pitch to [reporter/outlet] about [news]."*
Output: `output\pr\media-pitch-<topic>-<date>.md`

**`crisis-response`** — Holding statements, press responses, internal talking points.
> 🟦 *"We had a 4-hour platform outage that hit billing dashboards. Draft a crisis communication playbook."*
> ⬜ *"We had [incident]. Draft a crisis communication playbook."*
Output: `output\pr\crisis-playbook-<topic>-<date>.md`

**`executive-thought-leadership`** — CEO/exec op-eds and LinkedIn thought pieces.
> 🟦 *"Draft a LinkedIn article for Veloxa's CEO on why FinOps is becoming a board-level concern."*
> ⬜ *"Draft a LinkedIn article for our [exec title] on [topic]."*
Output: `output\pr\thought-leadership-<exec>-<date>.md` + `.docx`

### Social Media *(owned by `social-strategist`)*

**`social-strategy`** — Cross-platform organic content calendars and campaigns.
> 🟦 *"Design a 4-week LinkedIn content calendar around Veloxa's customer cost-savings stories."*
> ⬜ *"Design a [N]-week content calendar around [theme]."*
Output: `output\social\calendar-<topic>-<date>.md` + `.docx`

### Podcast *(owned by `podcast-strategist`)*

**`podcast-episode-plan`** — Guest research dossier, run-of-show, host script, questions.
> 🟦 *"Plan our next episode — we have the Head of Cloud Infra at a fintech unicorn as a guest, topic is multi-cloud cost governance."*
> ⬜ *"Plan our next episode — guest is [name/title], topic is [topic]."*
Output: `output\podcasts\episode-plan-<topic-or-guest>-<date>.md` + `.docx`

**`podcast-show-notes`** — Show notes, timestamps, takeaways, promo blurbs from a transcript.
> 🟦 *"Here's the transcript from our episode on cloud cost governance — write show notes, timestamps, and 2 promo posts."*
> ⬜ *"Here's the transcript from our episode on [topic] — write show notes, timestamps, and promo posts."*
Output: `output\podcasts\show-notes-<topic-or-guest>-<date>.md` + `.docx`

### Lead Generation *(owned by `lead-generation-engine`)*

**`lead-gen-strategy`** — Channel mix, MQL/SQL scoring model, nurture flow map.
> 🟦 *"Design our lead gen funnel for the new mid-market tier — we need MQL/SQL criteria and a nurture flow."*
> ⬜ *"Design our lead gen funnel for [offer/tier] — we need qualification criteria and a nurture flow."*
Output: `output\reports\lead-gen-strategy-<topic>-<date>.md`

### Webinar *(owned by `webinar-strategist`)*

**`webinar-plan`** — Concept, agenda, speaker brief, promotion timeline, follow-up outline.
> 🟦 *"Build a webinar plan on cutting Kubernetes spend 30% — speaker is our Head of Product, date is in 3 weeks."*
> ⬜ *"Build a webinar plan on [topic] — speaker is [name], date is [timeframe]."*
Output: `output\webinars\webinar-plan-<topic>-<date>.md`

---

## End-to-End Scenario Walkthroughs

Realistic multi-step sequences, all using Veloxa, showing how agents hand off to each other.

### Scenario 1 — New feature launch
1. **`campaign-strategist`**: *"We're launching Kubernetes cost-anomaly detection for VP Engineering at mid-market SaaS companies. Build the campaign strategy."* → `output\reports\strategy-...md`
2. **`content-creator`** (parallel): *"Using this campaign strategy, build the blog post, landing page, and LinkedIn posts for the launch."* → `output\pages\`, `output\social\`
3. **`creative-designer`** (parallel): *"Using this campaign strategy, build the LinkedIn and display ad creatives."* → `output\ads\`, `output\social\`

### Scenario 2 — ABM push into enterprise accounts
1. **`campaign-strategist`**: *"We want to run an ABM campaign targeting our top 20 enterprise fintech accounts for cost-anomaly detection. Build the campaign strategy — campaign type is ABM."* → `output\reports\strategy-...md`, then `output\reports\abm-account-plan-...md`
2. **`creative-designer`**: *"Using the ABM account plan, build personalized ad creative for our Tier 1 accounts."* → `output\ads\`
3. **`content-creator`**: *"Using the ABM account plan, build account-specific landing pages and email sequences for Tier 1."* → `output\pages\`, `output\email\`

### Scenario 3 — Lead-gen funnel for a new tier
1. **`lead-generation-engine`**: *"Design a lead gen funnel for our new mid-market tier — right now we just have a contact form."* → `output\reports\lead-gen-strategy-...md`
2. **`content-creator`**: *"Using this funnel strategy, build the gated checklist, landing page, and nurture sequence."* → `output\pages\`, `output\email\`

### Scenario 4 — Webinar program
1. **`webinar-strategist`**: *"Plan a webinar on cutting Kubernetes spend 30%, targeting platform engineering leads, 3 weeks out."* → `output\webinars\webinar-plan-...md`
2. **`content-creator`**: *"Using this webinar plan, write the registration page and the promotion + follow-up emails."* → `output\pages\`, `output\email\`
3. **`social-strategist`**: *"Slot the webinar promotion into next month's social calendar."* → `output\social\`

### Scenario 5 — SEO + AI visibility push
1. **`seo-specialist`**: *"Audit our technical SEO and on-page optimization for our /cloud-cost-optimization page."* → `output\seo\`
2. **`content-creator`**: *"Close the content gaps identified in the SEO audit."* → `output\pages\`
3. **`seo-specialist`** (`aeo-foundations`): *"Audit and fix our AI crawler readiness — robots.txt and llms.txt."* → `output\seo\`
4. **`ai-citation-strategist`**: *"Now run a citation audit — are we showing up when people ask AI tools for the best cloud cost platform?"* → `output\seo\`
