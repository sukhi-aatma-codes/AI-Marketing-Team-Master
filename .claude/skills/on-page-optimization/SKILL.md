---
name: on-page-optimization
description: >
  Use this skill whenever the user wants to optimize a specific webpage, landing page,
  or blog post for on-page SEO signals, keyword alignment, content depth, readability,
  and featured snippet capture. Trigger on requests like "optimize our homepage for search",
  "do an on-page audit of this URL", "improve meta tags for X", "check this draft's on-page SEO",
  "format this content for keyword Y", or "align this landing page copy with search intent".
  Use this skill after keyword-research and before blog-writer or lp-builder to review and
  optimize specific pages.
---

# On-Page Optimization

Analyzes and optimizes a specific webpage's content, structure, and meta tags for target
keywords, readability, search intent, and featured snippet capture. Checks for keyword cannibalization
before proposing modifications. Produces a structured `.md` optimization document and a Word doc (`.docx`)
for editorial review.

## Before starting

Read these context files every time — do not rely on prior session memory:
- `_context/Brand_Voice_Guide.md` — brand voice and copywriting constraints
- `_context/Brand_Product_Offerings.md` — target services, ICPs, and proof points to anchor copy

If a keyword research file exists in `output/seo/` for this topic, read it first to align the target primary and secondary keywords.

## Clarify inputs first

Confirm with the user:
1. **Target URL or Text Draft:** The page URL to optimize or the draft copy text to audit.
2. **Primary Keyword:** The main keyword we want the page to rank for.
3. **Secondary Keywords:** 2–3 supporting keywords or semantic variants.
4. **Target ICP:** Who is reading the page (shapes content tone, vocabulary, and CTAs).
5. **Objective:** Conversion (landing page), education (blog post), or awareness (homepage).

If the user's request makes these inputs clear, skip asking and proceed.

## Optimization workflow

### Step 1 — Cannibalization Pre-Check
Before proposing any metadata or content changes:
- Check Google Search Console or search results to see if another page on the brand's domain already ranks or matches the target keyword.
- Ensure the primary keyword is not owned by a stronger pillar page.
- Assign keyword ownership clearly to avoid split rankings.

### Step 2 — Metadata Optimization
Design high-performance search tags:
- **Title Tag:** Must be 50–60 characters. Place primary keyword near the start. Use unique branding suffix.
- **Meta Description:** Must be 150–155 characters. Benefit-led, uses primary keyword, and includes a clear call to action (CTA).
- **Header Structure:** Verify a single `<h1>` containing the primary keyword. Outline `<h2>` and `<h3>` tags that align with related search terms and user pain points.

### Step 3 — Content Depth & Keyword Alignment
Audit the visible page copy:
- **Keyword Density:** Check for natural keyword integration in the first 100 words, body copy, and conclusion. Avoid keyword stuffing.
- **Semantic Coverage:** Identify related topics, synonyms, and sub-questions searchers ask.
- **E-E-A-T Compliance** (Experience, Expertise, Authoritativeness, Trustworthiness — Google's page-quality framework): evidence each on-page — first-hand experience signals (original data, screenshots, "we tested" language); an author bio with relevant credentials; links to authoritative external citations; trust elements (contact/about links, specific brand proof points, no unverifiable claims). Check and add all four.
- **Paragraph Length:** Break down long text blocks into readable 2–4 sentence paragraphs.

### Step 4 — Media & Rich Elements
Enhance interactive elements:
- **Image Alt Text:** Propose descriptive, keyword-rich alt text for all major visual elements.
- **Tables and Bullet Lists:** Format data or steps into lists and tables to target featured snippets and Perplexity citations.
- **FAQs:** Build a structured FAQ section utilizing People Also Ask questions found in SERP research.

### Step 5 — Internal/External Linking
Audit URL linkages:
- **Internal Links:** Identify 2–3 contextual internal link targets from the page to other cluster/pillar pages.
- **External Citations:** Add links to authoritative external studies or industry stats.

## Output structure (`.md`)

Save as `output/seo/on-page-<page-slug>-<date>.md` with this exact section structure:

```
# On-Page SEO Optimization: [Page Title]
Date: [yyyy-mm-dd]
Target Page: [URL or Description]
Primary Keyword: [Keyword]
Secondary Keywords: [Keywords]
Target ICP: [ICP from Offerings]

## Cannibalization Verification
[Summary of the cross-page cannibalization audit — confirming no overlapping keywords with other pages]

## Metadata Recommendations
### Current vs. Optimized Tags
| Element | Current | Recommended | Chars | Notes |
|---------|---------|-------------|-------|-------|
| Title   | ...     | ...         | ...   | ...   |
| Meta    | ...     | ...         | ...   | ...   |
| H1      | ...     | ...         | ...   | ...   |

## Content Structure & Hierarchy
[Outline of the optimized header structure: H1, H2s, H3s]

## Recommended Copy Changes
### Section: [e.g. Hero Section / Introduction]
- **Current Copy:**
  > [Text]
- **Optimized Copy:**
  > [Text]
- **SEO Rationale:** [Why the change was made — intent matching, keyword placement, styling]

[Repeat for other major body sections]

## FAQ & Snippet Capture Recommendations
### Question 1: [PAA question]
- **Proposed Answer:** [40-60 word concise paragraph answer]
- **Schema Format:** FAQPage JSON-LD recommendation

## Linking & Anchor Text Plan
- **Internal Links to add:**
  - Link to `/url-1` using anchor text "..."
- **External Sources to cite:**
  - Source: [Name] - [URL]
```

## Rich deliverable

After saving the `.md`, invoke `document-skills:docx` to export as a Word document for editorial review.
Save as `output/seo/on-page-<page-slug>-<date>.docx`.

## Quality checklist

- [ ] Cannibalization pre-check completed and documented in the output
- [ ] Recommended Title and Meta Description character limits verified
- [ ] Single `<h1>` tag enforced with primary keyword present
- [ ] Word-for-word copy changes (before vs. after) provided for major sections
- [ ] FAQ answers are self-contained and formatted for featured snippet capture
- [ ] `.md` and `.docx` saved to `output/seo/`
- [ ] Every reported data point was actually retrieved — anything that could not be fetched or verified is marked `[DATA UNAVAILABLE — <what was needed>]`, never estimated or filled with a plausible-sounding value
