---
name: blog-writer
description: >
  Use this skill whenever the user wants to write a blog post, article, or long-form piece
  of content. Trigger on requests like "write a blog post about X", "draft an article on Y",
  "create content for our blog on Z", "write a thought leadership piece", "create a post
  about industry trends in our vertical", or any request for a written article intended for
  publication. This skill produces a fully upload-ready output — slug, all CMS meta fields,
  HTML file, and Word doc — nothing left to do before publishing. It performs SERP research
  before writing and optimizes for SEO, AEO (AI answer engines), and GEO (generative engine
  optimization). Use it after keyword-research if a keyword brief exists.
---

# Blog Writer

Writes fully upload-ready, SEO/AEO/GEO-optimized blog posts in the brand's voice. Performs
SERP research before writing. Produces: structured `.md` with all CMS meta fields, `.html`
for direct upload, and `.docx` for editorial review. Nothing is left for the user to add
before publishing.

## Before starting

Read these context files every time:
- `_context/Brand_Voice_Guide.md` — voice pillars, tone, banned words, power verbs
- `_context/Brand_Product_Offerings.md` — service lines, ICPs, proof points to reference

If a keyword research file exists for this topic (in `output/seo/`), read it first. It contains
the SERP analysis and People Also Ask data that shapes the outline and FAQ section.

## Clarify inputs first

Confirm with the user:
1. **Topic:** What is the post about?
2. **Primary keyword:** The main search term to rank for
3. **Target ICP:** Who is the reader? (Shapes depth, language, and proof points used)
4. **Service line:** Which service line is this post supporting?
5. **Target word count:** Default is 1,200–1,500 words. Longer if topic demands depth.
6. **CTA target:** What should the reader do at the end? (Service page, lead magnet, contact)

## Research phase (before writing)

Do this research before touching the outline. Real research, real sources — no invented data.

**SERP research:**
- Search the primary keyword. What content types dominate page 1?
- What angle do the top 3 results take? (Educational, service-led, data-led, listicle)
- Is there a featured snippet? What format (paragraph, list, table)?
- What are the People Also Ask questions? (These become the FAQ section)
- What content gaps exist — what do the top results miss that the brand could own?

**Source research:**
- Search for supporting statistics, recent data, and industry research (Gartner, Forrester,
  McKinsey, plus the analyst firms and trade publications specific to the brand's vertical)
- Find 3–5 citable external sources with URLs
- Find 2–3 internal linking targets: brand service pages or blog posts to link to naturally

Document all research findings before writing. Every stat in the post must have a source.

## CMS meta block

Every post starts with this block (goes into `.md` front-matter AND top of `.html` as an HTML
comment block for the publisher to copy into the CMS):

```
<!-- CMS META — copy these fields into your CMS before publishing -->
Slug:              /blog/<url-friendly-slug-max-60-chars>
Meta title:        <60 chars max — include primary keyword, ideally near the start>
Meta description:  <150–155 chars — benefit-led sentence, include primary keyword>
Canonical URL:     https://www.[brand-domain]/blog/<slug>  ← load domain from Brand_Context.md
OG title:          <same as meta title or a tested variation>
OG description:    <same as meta description>
Focus keyword:     <primary keyword>
Secondary keywords: <2–3 supporting terms, comma-separated>
Schema type:       Article
Author:            [brand editorial team name — from Brand_Context.md]
Estimated read time: X min read
```

## Post structure

Write in this exact order:

**1. H1** — Keyword-led. Matches the SERP intent identified in research. Aim for 55–65 chars.
Example pattern: "[Number/Adjective] [Topic] [Outcome/Promise]"

**2. TL;DR block** (immediately below H1, before intro)
A clearly labelled "TL;DR" or "Key Takeaways" block with 3–5 bullet points summarizing the
post's main arguments. Purpose: serves AI answer engines (AEO/GEO) and scanners who won't
read the full post. Format as a `<ul>` in HTML. Each bullet = one complete thought, 15–25 words.

**3. Introduction** (100–150 words)
- Hook: an unexpected stat, a provocative question, or a scene-setting scenario
- Problem context: name the pain the ICP recognizes
- Promise: what this post will answer or give the reader

**4. Body sections (3–5 H2s)**
- One idea per section — do not pack multiple arguments into one H2
- Each section: claim → evidence (cited) → implication for the reader
- Work in 2–3 internal links to brand pages naturally within body text
- Work in external citations as inline links (e.g., "according to [Gartner, 2024]")
- Keep paragraphs short: 2–4 sentences maximum

**5. FAQ section** (H2: "Frequently Asked Questions")
- 4–6 Q&A pairs based on People Also Ask questions and related searches from SERP research
- Format: `<h3>` for each question, paragraph answer immediately below
- Each answer: 40–60 words — long enough to be useful, short enough for featured snippet capture
- Answers must be self-contained (readable without the full post context) — this is how AI
  answer engines will cite them

**6. Conclusion** (75–100 words)
- Restate the key takeaway (not the intro — a new synthesis)
- Soft CTA: natural, not salesy. Use the primary CTA from `Brand_Voice_Guide.md` — never "Click Here" or "Learn More" with no context

## AEO/GEO rules

- TL;DR and FAQ use question + direct concise answer format — this is what AI answer engines index
- H2s must be able to stand alone as complete thoughts (not "Why This Matters" — instead
  "Why Mid-Market Teams Lose 30% of Their Week to Manual Reporting")
- No filler transitions or padding paragraphs — every sentence carries information
- Avoid "In this article, we will discuss..." — get to the point immediately

## Brand voice rules

Load `Brand_Voice_Guide.md` and apply throughout:
- Lead with transformation outcomes, not service descriptions
- Use the power verbs defined in `Brand_Voice_Guide.md` — do not substitute a generic list
- Ground every claim: pair any outcome statement with a specific proof point from `_context\` (or flag `[SOURCE NEEDED]`)
- Write to "you" (the reader) — never "the client" or "organizations"
- Apply the banned-words list from `Brand_Voice_Guide.md` — no exceptions

## Output files

**1. Structured markdown** `output/pages/blog-<slug>-<date>.md`
Contains: CMS meta block in YAML front-matter + full post content in markdown

**2. HTML file** `output/pages/blog-<slug>-<date>.html`
Self-contained HTML with:
- `<head>` with meta tags, OG tags, canonical, JSON-LD Article schema
- Google Fonts link for brand font (load typeface name from Brand_Style.md)
- Minimal inline CSS (body max-width 720px, brand colors for links and accents)
- Full structured post content in semantic HTML (h1, h2, h3, ul, p, blockquote, a)
- FAQ section marked up with FAQ schema (JSON-LD) for featured snippet eligibility

**3. Word document** `output/pages/blog-<slug>-<date>.docx`
Invoke `document-skills:docx` to produce a formatted Word doc for editorial review.
Include: meta block as a styled table at top, then the full post content.

## Quality checklist

- [ ] SERP research completed before writing — not inferred
- [ ] Every stat has an inline citation with a real URL
- [ ] TL;DR block present and contains 3–5 complete-thought bullets
- [ ] FAQ section present with 4–6 Q&As from People Also Ask data
- [ ] 2–3 internal links to brand pages woven into body text
- [ ] CMS meta block complete: slug, meta title (≤60 chars), meta description (≤155 chars),
      canonical, focus keyword, schema type, read time
- [ ] No banned words from Brand_Voice_Guide.md
- [ ] All three output files saved: `.md`, `.html`, `.docx`
