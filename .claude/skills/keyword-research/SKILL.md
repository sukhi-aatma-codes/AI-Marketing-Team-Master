---
name: keyword-research
description: >
  Use this skill whenever the user wants to identify, cluster, or prioritize keywords for SEO
  or SEM — including SERP analysis to understand what's currently ranking and what gaps exist.
  Trigger on requests like "do keyword research for X", "what keywords should we target for Y",
  "find me SEO keywords for our services page", "what's ranking for Z", "build a
  keyword strategy for this topic", or any mention of search terms, rankings, SEO strategy,
  or content gaps. Use this after market-research and before blog-writer or lp-builder — it
  sits in the middle of the content pipeline.
---

# Keyword Research

Identifies and prioritizes keywords for SEO/SEM with SERP analysis — what's currently ranking,
what content format dominates, and where the gaps are. Maps keywords to content types and buyer
journey stages. The `.md` output feeds directly into `blog-writer` and `lp-builder`. The `.docx`
is for sharing with stakeholders or SEO teams.

## Before starting

Read these context files every time:
- `_context/Brand_Product_Offerings.md` — service lines, ICPs, pain points (generates seed keywords)
- `_context/Brand_Growth_Marketing_Context.md` — channel mix and current growth focus

## Clarify inputs first

Confirm with the user:
1. **Topic or service line:** What to build the keyword list around
2. **Target ICP:** Who is searching (shapes intent and language)
3. **Seed keywords:** Any terms the user already knows they want to target
4. **Scope:** Single-page focus, topic cluster, or full vertical keyword map

## Workflow

### Step 1 — Seed keyword generation
From `Brand_Product_Offerings.md`, extract:
- Service line names and synonyms
- ICP job titles and pain point language
- Industry terminology buyers use (not internal jargon)

Generate an initial seed list of 15–25 terms.

### Step 2 — Cluster by search intent
Group seeds and related terms into three intent buckets:

| Intent | Description | Content type match |
|--------|-------------|-------------------|
| **Informational** | "What is / how does / why does" — research phase | Blog, guide, FAQ page |
| **Commercial investigation** | Comparing options, evaluating solutions | Comparison page, case study, whitepaper |
| **Transactional** | Ready to buy or engage | Landing page, service page, contact page |

For each seed, identify 3–5 related variants (long-tail, question-form, modifier-based).

### Step 3 — SERP analysis (run for each priority cluster)

For each cluster's primary keyword, search and document:

**Content type audit:**
- What appears on page 1? (blog posts, service pages, comparison pages, Reddit/Quora, news)
- Is there a featured snippet? If yes, what format (paragraph, list, table)?
- Are there People Also Ask boxes? List the questions.
- Any image packs, local packs, or video carousels?

**Top 3 results analysis:**
- What angle does each take? (educational / service-led / data-led / opinionated)
- Approximate word count and content depth
- What they cover well vs. what they miss

**Content gap:**
- What would a better answer look like that the brand could own?
- Is there an angle no one has taken that matches the brand's positioning?

### Step 4 — Content type mapping
For each cluster, recommend the content type the brand should create and why:
- Blog post → informational, long-tail, education-first
- Landing page → transactional or commercial, service-specific
- Case study → commercial investigation, proof-heavy
- FAQ page → informational, People Also Ask dominance

### Step 5 — Prioritization
Score each cluster on:
- **Intent value:** How close to a buying decision
- **Topical authority fit:** Does the brand have existing content or expertise here
- **Competition level:** How hard is page 1 to crack (qualitative from SERP scan)
- **Quick-win potential:** Low-competition terms where the brand could rank fast

Flag top 5 clusters as **Priority** and bottom clusters as **Long-term**.

## Output structure (`.md`)

Save as `output/seo/keywords-<topic>-<date>.md` with this exact structure:

```
# Keyword Research: [Topic]
Date: [yyyy-mm-dd]
Target ICP: [who is searching]
Service line: [from Brand_Product_Offerings.md]

## Seed Keywords
[List of 15–25 seeds]

## Keyword Clusters
### Cluster 1: [Cluster name] — [Intent type]
Primary keyword: ...
Related variants: ...
SERP summary: [what's ranking, featured snippet Y/N, PAA questions]
Content gap: ...
Recommended content type: ...
Priority: High / Medium / Low

[Repeat for each cluster]

## Priority Matrix
[Table: Cluster | Intent value | Authority fit | Competition | Priority tier]

## Recommended Content Plan
[Ordered list of what to create first, with rationale]
```

## Rich deliverable

After saving the `.md`, invoke `document-skills:docx` to export as a Word document.
Save as `output/seo/keywords-<topic>-<date>.docx`.

## Quality checklist

- [ ] SERP analysis run for every Priority cluster — not inferred, actually searched
- [ ] People Also Ask questions documented (these feed directly into blog FAQ sections)
- [ ] Content gaps are specific and actionable, not generic
- [ ] Priority matrix populated — user can see what to tackle first vs. later
- [ ] `.md` section headings match the structure above (blog-writer reads this file)
- [ ] `.docx` generated and saved to `output/seo/`
- [ ] Every reported data point was actually retrieved — anything that could not be fetched or verified is marked `[DATA UNAVAILABLE — <what was needed>]`, never estimated or filled with a plausible-sounding value
