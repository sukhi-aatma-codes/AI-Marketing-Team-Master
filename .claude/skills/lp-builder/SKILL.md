---
name: lp-builder
description: >
  Use this skill whenever the user wants to create a landing page, service page, campaign
  page, or any web page designed to convert visitors. Trigger on requests like "build a
  landing page for X", "write a service page for one of our service lines", "create a
  campaign LP for Y", "make a page for this paid campaign", "write copy for a landing page
  on Z", or any mention of landing pages, service pages, or conversion-focused web copy.
  Produces a structured `.md` with all copy organized by section, plus a fully coded HTML
  file ready to drop into a CMS or send to a dev team. Adjusts page length and directness
  based on traffic source (paid vs. organic vs. email).
---

# LP Builder

Writes and produces landing pages as a structured `.md` (agent-ready, section-by-section)
and a ready-to-deploy HTML file. Adjusts for traffic source: paid pages are shorter and more
direct; organic pages can be longer and education-first; email pages assume warm audiences.

## Before starting

Read these context files every time:
- `_context/Brand_Voice_Guide.md` — lead with transformation outcomes, tone rules, banned words
- `_context/Brand_Product_Offerings.md` — service lines, ICPs, differentiators, proof points

## Clarify inputs first

Confirm:
1. **Offer / service:** What does this page promote?
2. **Target ICP:** Who is arriving on this page? (Role, vertical, pain point)
3. **Traffic source:** Paid (Google/LinkedIn ads), organic (SEO), email, or direct
4. **Primary CTA:** What is the one action the visitor should take?
5. **Proof points:** Ask the user for any specific metrics, client names, or case study outcomes
   to include. Check `_context/Brand_Product_Offerings.md` for what's available.
6. **Primary keyword** (for organic pages): Provide if SEO optimization is needed

## Page architecture by traffic source

| Traffic source | Page length | Tone | Key priority |
|----------------|-------------|------|-------------|
| Paid (Google/LinkedIn) | Short — 400–700 words | Direct, outcome-first | Message match: headline must mirror the ad |
| Organic (SEO) | Long — 800–1,500 words | Educational, authority-building | Keyword placement; trust signals above fold |
| Email | Medium — 500–900 words | Warm, continuation of email conversation | Continuity: page must feel like the natural next step |
| Direct / retargeting | Medium — 500–800 words | Assumes familiarity | Proof and CTA heavy; less problem framing needed |

## Section-by-section workflow

Write all sections in order. Each section has a specific job — don't blend them.

### Hero section
**Job:** Stop the visitor, confirm they're in the right place, give them one reason to scroll.

- **H1:** Outcome-led, 55–65 chars. Names the ICP's problem or desired outcome.
  Never leads with the service name. "Cut Your Reporting Week in Half" not "Business Intelligence Services"
- **Subheadline:** 1–2 sentences expanding the H1. Specifies who this is for and what they get.
- **Primary CTA button:** Action verb + context. "Book a Free Assessment" / "Talk to Our Team" / "Get the Playbook"
- **Trust signals** (optional, below CTA): client count, geographies served, analyst or industry recognition — pull real ones from `Brand_Context.md` / `Brand_Product_Offerings.md`, never invent them

For paid pages: H1 must match or closely reflect the ad headline (message match).

### Problem section
**Job:** Name the pain the ICP recognizes. Make the reader feel seen.

- 2–4 short paragraphs or a 3–5 item problem list
- Write from the ICP's perspective — their language, their frustrations, their stakes
- Do not solve it yet — just name it clearly. The solution comes next.
- Avoid telling the reader their problem is their fault. Frame it as systemic or market-driven.

### Solution section
**Job:** Show how this service solves the problem. Process + differentiators, not feature lists.

- Lead with the transformation outcome — one sentence naming the specific result the ICP gets and the timeframe (pull from Brand_Product_Offerings.md)
- Explain the approach (briefly) — what makes this different
- 3 differentiators max. Each in bold label + 1–2 sentence explanation.
- Reference the brand's named methodology or framework where relevant
  (check `Brand_Product_Offerings.md` for the correct name and description)

### Proof section
**Job:** Remove doubt. Show that this has worked for people like the visitor.

- Use only proof points from `_context/Brand_Product_Offerings.md` or user-provided data
- Options: client metrics ("reduced processing time by 40%"), client quote (if provided),
  credential (analyst recognition, certifications), client logos (if user provides), case study teaser
- Flag any missing proof points as `[DRAFT — confirm before publishing: ...]`
- For paid pages: 1–2 proof elements above fold. For organic: can be a full social proof section.

### CTA block (closing)
**Job:** Remove friction and convert.

- Repeat the primary CTA — same button label as in the hero
- Add a secondary trust signal: privacy note, no-commitment language, or response time commitment
- One sentence of urgency or value framing: "Most teams see results within the first 90 days."

## Keyword optimization (organic pages only)

- Primary keyword in H1 (ideally near the start)
- Primary keyword in the first paragraph of the problem or intro section
- 1–2 secondary keywords in H2 subheadings
- Meta title (≤60 chars): primary keyword + brand modifier
- Meta description (≤155 chars): benefit-led, includes primary keyword
- Add these to the top of the `.md` and as `<meta>` tags in the HTML `<head>`

## Output files

**1. Structured markdown** `output/pages/lp-<slug>-<date>.md`

```
# Landing Page: [Page title]
Slug: /[page-url]
Traffic source: [paid / organic / email / retargeting]
Primary CTA: [action]
Target ICP: [role, vertical]
Date: [yyyy-mm-dd]
Meta title: [≤60 chars — organic pages only]
Meta description: [≤155 chars — organic pages only]

## Hero
H1: [headline]
Subheadline: [subheadline]
CTA: [button label]
Trust signals: [optional]

## Problem
[Full copy]

## Solution
[Full copy with 3 differentiators]

## Proof
[Full copy with sourced proof points]

## CTA Block
[Full copy]

## Draft Flags
[Any [DRAFT] items needing confirmation]
```

**2. HTML file** `output/pages/lp-<slug>-<date>.html`

Full semantic HTML with:
- `<head>`: meta title, meta description, canonical, OG tags (organic pages), Google Fonts (brand font from Brand_Style.md)
- Inline CSS: brand colors (hex values from Brand_Style.md), responsive layout, max-width 960px, clean section spacing
- CTA buttons: brand accent color, white text, brand font (all values from Brand_Style.md)
- Semantic sectioning: `<header>`, `<section>`, `<footer>` with clear IDs for each section
- No external JS dependencies — pure HTML/CSS, dev-team-ready

## Quality checklist

- [ ] H1 is outcome-led — does not lead with the service name or "we"
- [ ] Hero CTA and closing CTA use the same button label
- [ ] Proof section contains only sourced proof points — nothing invented
- [ ] All `[DRAFT]` flags noted for the user to resolve before publishing
- [ ] Traffic-source adjustments applied (length, directness, message match for paid)
- [ ] Organic pages: meta title, meta description, and keyword placement included
- [ ] HTML file is complete, self-contained, and uses brand colors and brand font from Brand_Style.md
- [ ] Both `.md` and `.html` saved to `output/pages/`
