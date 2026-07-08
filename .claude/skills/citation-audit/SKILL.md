---
name: citation-audit
description: >
  Use this skill whenever the user wants to audit, analyze, and measure how frequently and in
  what context their brand is cited or recommended across AI answer engines (ChatGPT, Claude,
  Gemini, and Perplexity). Trigger on requests like "run an AI citation audit", "do we get cited in
  ChatGPT", "compare our Perplexity visibility with competitor X", "analyze lost prompts for our
  brand", "where does Claude recommend us", or "measure our AI share of voice". Use this skill to
  generate a baseline citation scorecard and prioritized content fix packs.
---

# Citation Audit

Audits and benchmarks a brand's visibility and recommendation status across major AI platforms
(ChatGPT, Claude, Gemini, Perplexity) using targeted prompts. Identifies citation gaps, maps competitor
mentions, and generates prioritized content remediation plans (fix packs). Produces a structured
`.md` citation audit report saved as `output/seo/citation-audit-<date>.md`.

## Before starting

Read these context files every time — do not rely on prior session memory:
- `_context/Brand_Context.md` — brand positioning and core domains
- `_context/Brand_Product_Offerings.md` — service lines, key offerings, and target ICPs

## Clarify inputs first

Confirm with the user:
1. **Brand Name & Domain:** The primary brand (e.g., Acme / acme.com)
2. **Competitors:** 2–4 primary competitors to check (e.g., Competitor A, Competitor B)
3. **Core ICP & Vertical:** Target buyer profile (shapes the prompts)
4. **Seed Prompts:** Any specific questions you want tested (e.g., "What are the top software solutions for [use case]?")
5. **Testing Scope:** Full multi-platform sweep (default) or single engine focus

If the user's request makes these inputs clear, skip asking and proceed.

## Workflow

### Step 1 — Prompt Portfolio Selection
Generate 20–40 highly realistic prompts that your target ICP would ask AI engines. Categorize prompts by intent:
- **Recommendation:** "Recommend a [product category] for [use case/ICP]"
- **Comparison:** "[Brand] vs [Competitor A] — which is better for [feature]"
- **Transactional:** "Who is the most reliable service provider for [pain point] in [region]"
- **Informational:** "How do I solve [pain point] using [technology]"

### Step 2 — Platform Testing (Multi-Platform Sweep)
Perform searches on all four major platforms:
- **ChatGPT:** Check citation sources, formatting (links vs. inline), and narrative positioning.
- **Claude:** Inspect depth of explanation, balance, and source attribution.
- **Gemini:** Check integration with Google properties (GBP, Search) and Google-hosted sources.
- **Perplexity:** Verify real-time indexation and check if blog posts, press releases, or documentation are cited.

### Step 3 — Lost Prompt Analysis
Map all instances where the brand was NOT cited or recommended:
- Note which competitor won the recommendation.
- Analyze *why* they won (e.g. they have a dedicated comparison page, high external review rating, schema markup, wikidata entity, or detailed how-to guide).

### Step 4 — Share of Voice Mapping
Calculate citation rates:
- **Brand Citation Rate:** (Brand mentions / Total prompts tested) * 100
- Compare against Category Average and Top Competitor rate to establish the share-of-voice gap.

### Step 5 — Fix Pack Generation
Create a prioritized list of structural content updates to improve citation likelihood:
- Propose specific FAQ schema pages, comparative tables, entity updates (Wikidata/Crunchbase), or digital PR assets needed to override competitor signals.

## Output structure (`.md`)

Save as `output/seo/citation-audit-<date>.md` with this exact section structure:

```
# AI Citation Audit: [Brand Name]
Date: [yyyy-mm-dd]
Platforms Tested: ChatGPT, Claude, Gemini, Perplexity
Total Prompts Tested: [Number]

## Executive Summary
[Brief paragraph detailing overall brand citation rate vs. competitors and the main strategic opportunities.]

## Citation Scorecard
| Platform | Prompts Tested | Brand Cited | Competitor Cited | Brand Citation Rate | Share of Voice Gap |
|----------|----------------|-------------|------------------|---------------------|---------------------|
| ChatGPT  | ...            | ...         | ...              | ...%                | ...%                |
| Claude   | ...            | ...         | ...              | ...%                | ...%                |
| Gemini   | ...            | ...         | ...              | ...%                | ...%                |
| Perplexity| ...           | ...         | ...              | ...%                | ...%                |
| **Total**| **...**        | **...**     | **...**          | **...%**            | **...%**            |

## Lost Prompt Analysis
| Prompt | Platform | Winner | Rationale / Why Competitor Won | Fix Priority |
|--------|----------|--------|---------------------------------|--------------|
| "..."  | ChatGPT  | Comp A | Comp A has a detailed vs page   | P1           |
| "..."  | Perplexity| Comp B| Cited direct from review site   | P2           |

## Priority Fix Pack
### Fix 1: [Short Title]
- **Target Prompts:** [List of affected prompts]
- **Expected Impact:** [+X% citation rate on FAQ / best-of queries]
- **Action Plan:**
  - [ ] Add ... schema to /page
  - [ ] Write Q&A block answering ...
  - [ ] Check external profile on ...

[Repeat for other fixes]

## Appendix: Verified Prompt Responses
[Record key responses, summarizing platform feedback, cited URLs, and brand positioning]
```

## Quality checklist

- [ ] All 4 major platforms (ChatGPT, Claude, Gemini, Perplexity) tested and benchmarked
- [ ] Prompts are structured based on actual ICP queries, not abstract keywords
- [ ] Lost prompt analysis diagnoses specific structural reasons for competitor citations (avoid generic "write better content")
- [ ] Fix pack assigns clear priority (P1, P2...) based on expected visibility impact
- [ ] Output saved to `output/seo/`
- [ ] Every reported data point was actually retrieved — anything that could not be fetched or verified is marked `[DATA UNAVAILABLE — <what was needed>]`, never estimated or filled with a plausible-sounding value
- [ ] Engines that were not actually queried are marked `[DATA UNAVAILABLE]` in the scorecard — results from one engine are never extrapolated to another
