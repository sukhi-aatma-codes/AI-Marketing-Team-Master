---
name: lead-magnet
description: >
  Use this skill whenever the user wants to create or strategize gated content for demand
  generation — guides, checklists, toolkits, self-assessments, templates, or any content asset
  that a prospect would exchange their contact details to receive. Covers format selection by
  buyer stage, gating strategy, distribution planning, and measurement — not just writing the
  asset. Trigger on requests like "create a lead magnet on X", "build a guide for our
  prospects", "write a checklist for CFOs", "make a toolkit for Y", "create gated content about
  Z", "we need a whitepaper outline on X", "what should we give away for emails", or any
  mention of downloadable content, gated assets, or demand gen content pieces. Produces a
  fully written content file in `.md`, plus a premium branded PDF using the brand template.
---

# Lead Magnet

Creates lead magnet content — guides, checklists, toolkits, and self-assessments — for
demand gen and gated content programs. Produces a fully written `.md` content file plus a
premium branded PDF via `branded-deck`.

## Before starting

Read these context files every time:
- `_context/Brand_Voice_Guide.md` — voice, tone, banned words, proof point rules
- `_context/Brand_Product_Offerings.md` — service lines, ICPs, pain points, proof points

## Clarify inputs first

Confirm:
1. **Target ICP:** Who is this for? (Role, vertical, company size — shapes language and depth)
2. **Pain point / trigger event:** What problem or decision moment does this address?
3. **Buyer stage:** Awareness, consideration, or decision — drives both format and gating choice (see below)
4. **Format:** See format selection guide below
5. **Gating approach:** Full gate, partial preview, ungated, or content upgrade — see Gating Strategy below
6. **Service line:** Which service line does this support?
7. **CTA destination:** Where should the reader go after consuming it? (Service page, demo booking, contact)
8. **Existing proof points:** Ask the user for any real case study outcomes or client data to include

## Format selection guide

Choose the format that matches the ICP's mindset at their current stage:

| Format | Best for | Reader mindset | Typical length | Effort |
|--------|---------|----------------|---------------|--------|
| **Checklist** | Early awareness or action-ready practitioners | "Give me something I can use today" | 1–2 pages | Low |
| **Guide** | Education-first, mid-funnel prospects | "Help me understand this problem and how to solve it" | 8–15 pages | High |
| **Toolkit** | Practitioners who need templates and frameworks | "Give me the tools, I'll apply them" | 5–10 pages + templates | Medium |
| **Self-assessment** | Prospects evaluating their own situation | "Help me diagnose where I stand" | 3–6 pages + scoring | Medium |
| **Report / whitepaper** | Senior buyers who want data and analyst-level depth | "Show me the research and implications" | 12–20 pages | High |

If the user hasn't specified a format, recommend the best fit based on ICP and pain point.

### Matching format to buyer stage

- **Awareness** (doesn't know you yet, needs education): checklist, guide
- **Consideration** (evaluating solutions, building trust): toolkit, self-assessment, report/whitepaper
- **Decision** (ready to act, removing friction): toolkit (implementation-focused), short checklist ("get started in 10 minutes")

Don't default to "guide" for everything — a decision-stage prospect wants an implementation
aid, not another education piece.

## Gating Strategy

| Approach | When to use | Trade-off |
|----------|-------------|-----------|
| **Full gate** | High-value content, decision-stage offers | Maximum capture, lower reach |
| **Partial gate** | Preview + full version behind the form | Balances reach and capture |
| **Ungated** | Top-of-funnel education, brand awareness | Maximum reach, no lead capture |
| **Content upgrade** | Bonus tied to a specific blog post | Contextual, high-intent — converts 2–5x better than generic gates |

**Form fields — ask for the minimum needed.** Every extra field reduces conversion meaningfully:
- Email only → highest conversion, lowest qualification
- Email + name → light personalization, minor friction increase
- Email + company/role → better lead qualification, more friction — justify this for
  decision-stage or high-value offers only

**Framing the exchange:** state the value plainly ("Get the full 20-page guide free"), show a
preview (table of contents or first page), and reduce risk ("No spam. Unsubscribe anytime.").

## Distribution Plan

Don't treat the asset as done once written — plan how it reaches the ICP:

- **Blog CTAs / content upgrades:** inline and end-of-post CTAs on related content; a
  topic-specific content upgrade converts better than a generic sidebar offer
- **Social promotion:** hand off to `social-strategist` (or invoke `social-copy` directly) for
  platform-specific posts and carousel teasers built from this asset's key points
- **Paid amplification:** hand off to `creative-designer` (`ad-creative`) for LinkedIn/Google
  promotion of high-intent assets (toolkits, templates, reports)
- **Email nurture:** hand off to `email-copy` (via `content-creator`) for the post-capture
  sequence — don't leave a new lead with no follow-up plan
- **PR / partner co-promotion:** for report/whitepaper-tier assets with original data, consider
  `pr-comms` for media pitching or partner newsletter placement

## Measurement Plan

| Metric | What it tells you | Rough benchmark |
|--------|--------------------|-----------------|
| Landing page conversion rate | Offer attractiveness | 20–40% warm traffic, 5–15% cold |
| Cost per lead | Acquisition efficiency | Varies by channel — track against `Brand_Growth_Marketing_Context.md` baselines |
| Lead-to-customer rate | Lead quality, not just volume | 1–5% typical B2B, varies widely |
| Email engagement post-capture | Content/offer relevance | 30–50% open, 2–5% click as a rough floor |

Flag benchmarks without a real source as directional only — never present them as the brand's
actual performance data.

**What to A/B test first:** headline framing (benefit vs. curiosity), gate level (full vs.
partial preview), form fields (email-only vs. email+role).

## Content workflow

### Step 1 — Title and premise
Title formula options:
- Problem-led: "The Hidden Cost of Manual Claims Processing: A CFO's Guide"
- Outcome-led: "From Back-Office Bottleneck to Operational Advantage: 5 Strategies for Insurance COOs"
- Diagnostic: "Is Your Insurance Back-Office Ready for 2026? A Self-Assessment for Operations Leaders"
- Number-led: "7 Signs Your Finance Function Is Ready for Intelligent Automation"

Write a 2–3 sentence premise statement: the problem this piece addresses, why it matters now,
and what the reader will be able to do after reading it.

### Step 2 — Structure and outline
Map the content to a logical arc:
- **Checklist:** Introduction (why this matters) → checklist items (grouped by theme) → scoring/next steps
- **Guide:** Problem framing → Root causes → Framework / approach → Implementation steps → Results / proof → CTA
- **Toolkit:** Introduction → Template 1 → Template 2 → How to use each → Next steps
- **Self-assessment:** Introduction → Assessment questions (by section) → Scoring guide → What your score means → CTA

### Step 3 — Write the full content
Write every section in full — not placeholders, not outlines. This is the complete text.

Apply brand voice rules:
- Write to "you" (the reader) — never "the reader" or "organizations" in third person
- Ground every claim with a proof point from `_context/` or a cited external source
- If a stat or case study is needed and not available from `_context/`, flag it clearly:
  `[DRAFT — confirm this data point before publishing: ...]`
- Lead with outcomes and transformation, not service features
- No banned words from `Brand_Voice_Guide.md`

### Step 4 — CTA page / final section
Every lead magnet ends with a dedicated CTA section:
- Restate the problem the piece addressed
- Bridge to how the brand solves it (1–2 sentences, outcome-led)
- Primary CTA: [use primary CTA from Brand_Voice_Guide.md]
- Proof anchor: [use primary proof point from Brand_Product_Offerings.md]

### Step 5 — Design brief for branded PDF
Add a design brief section to the `.md` recommending how to render this as a premium PDF:
- **Visual style:** Recommend from `_context/Brand_Style_Reference.md` (if it doesn't exist
  yet, run `build-brand-style-reference` first) — match by content type:
  - Guides and reports → a report/cover-style entry (title-forward, structured cover treatment)
  - Data-heavy pieces → a data/stat-forward style for charts and stats pages
  - Checklists → a clean, typographic-only style for an authority look
- **Cover:** Title, subtitle, ICP-targeted headline, brand logo, year
- **Interior pages:** Consistent use of brand heading color, accent color, brand font, white backgrounds (all from Brand_Style.md)
- **Footer:** brand wordmark, page numbers, brand domain (from Brand_Context.md)

## Output structure (`.md`)

Save as `output/pages/lead-magnet-<topic>-<date>.md`:

```
# [Lead Magnet Title]
Format: [Checklist / Guide / Toolkit / Self-assessment / Report]
Target ICP: [Role, vertical]
Service line: [from Brand_Product_Offerings.md]
Date: [yyyy-mm-dd]

## Premise
[2–3 sentences: problem, why now, what the reader gains]

## [Section 1 title]
[Full written content]

## [Section 2 title]
[Full written content]

... (repeat for all sections)

## Next Steps
[CTA section: problem recap → brand bridge → CTA → proof anchor]

## Design Brief for PDF
Style: [A5 / A3 / A1 recommendation]
Cover: [title, subtitle, logo placement]
Interior: [color and typography notes]
[Any data visualization pages — note which charts to build]

## Data Points to Confirm
[Any flagged DRAFT data points that need user verification before publishing]
```

## Rich deliverable

### Production tool decision table

| Lead magnet format | Production tool | Output | Reason |
|---|---|---|---|
| Checklist | ReportLab (Python) | `.pdf` | Document layout — flowing text, no slides |
| Guide | ReportLab (Python) | `.pdf` | Document layout — multi-page narrative |
| Toolkit | ReportLab (Python) | `.pdf` | Document layout — templates + frameworks |
| Self-assessment | ReportLab (Python) | `.pdf` | Document layout — scored questionnaire |
| Report / whitepaper | ReportLab (Python) | `.pdf` | Document layout — long-form, data-heavy |

**Rule: never use `branded-deck` for lead magnet documents.** `branded-deck` is a slide/PPTX tool — it produces presentations, not document-formatted PDFs. All lead magnet formats above are documents. Use ReportLab for all of them.

`branded-deck` is only appropriate if the deliverable is explicitly a slide deck (e.g. a sales deck or pitch deck) — which is not a lead magnet format.

### Execution

After the `.md` is complete, run `generate_pdf.py` (ReportLab) to produce the branded PDF.
Apply the visual style recommended in the design brief (Step 5).

Save as `output/pages/lead-magnet-<topic>-<date>.pdf`

## Quality checklist

- [ ] Buyer stage identified and format matched to it — not a default "guide" for everything
- [ ] Gating approach chosen deliberately (full/partial/ungated/content upgrade) with a stated reason
- [ ] Form fields minimized to what's actually needed for qualification
- [ ] Distribution plan included — at minimum, which agent/skill owns promotion and nurture follow-up
- [ ] Format selection justified based on ICP and stage — not arbitrary
- [ ] Full content written in every section — no placeholders except flagged data gaps
- [ ] All proof points sourced from `_context/` — nothing invented
- [ ] Flagged data gaps clearly marked `[DRAFT — confirm before publishing]`
- [ ] CTA page present with proof anchor and specific action
- [ ] Design brief section included with style recommendation
- [ ] `.md` and `.pdf` both saved to `output/pages/`

## Related skills

- **`email-copy`** (via `content-creator`) — nurture sequence after lead capture
- **`social-copy`** / **`social-strategist`** — promotion and teaser content
- **`ad-creative`** (via `creative-designer`) — paid amplification of high-intent assets
- **`lp-builder`** — the landing page/form this asset is gated behind
