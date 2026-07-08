---
name: aeo-foundations
description: >
  Use this skill whenever the user wants to inspect, audit, or implement the foundational infrastructure
  for Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO). Trigger on requests like
  "audit our AI crawl readiness", "check robots.txt for AI bots", "create an llms.txt file for our site",
  "audit token budgets for AI search", "set up robots rules for Claude and ChatGPT", or "inspect our site's
  parsability for citation engines". Use this skill to make sure AI engines and browsing agents can discover,
  read, and parse site content before pursuing brand recommendations.
---

# AEO Foundations

Audits and designs the technical infrastructure required for AI engines, search-augmented crawlers,
and agentic crawlers to parse and access your site. Recommends configurations for robots.txt, creates
structured llms.txt maps, and calculates token budgets for key pages. Produces a structured AEO foundations
audit report saved as `output/seo/aeo-foundations-audit-<date>.md`.

## Before starting

Read these context files every time — do not rely on prior session memory:
- `_context/Brand_Context.md` — brand overview and primary domains
- `_context/Brand_Growth_Marketing_Context.md` — target channels and content priority

## Clarify inputs first

Confirm with the user:
1. **Target URL/Domain:** The domain to check (e.g. acme.com)
2. **AI Crawl Policy:** Does the business want to opt-in to model training (GPTBot/ClaudeBot) or restrict crawling to search-retrieval engines only (PerplexityBot)?
3. **Sitemap Availability:** URL to current sitemap.xml
4. **Primary Content Pages:** The 3–5 most critical pages (pricing, product overview, documentation) to assess for token budgets.

If the user's request makes these inputs clear, skip asking and proceed.

## Workflow

### Step 1 — robots.txt AI Crawler Audit
Inspect or design the site's robots.txt configurations to handle specialized AI user-agents:
- **Search-Augmented Bots (Allow):** Ensure bots that feed real-time responses and user citations (e.g., PerplexityBot) are allowed.
- **Model-Training Bots (Strategic Business Choice):** Document rules for crawler options like GPTBot, ClaudeBot, Google-Extended, and Applebot-Extended. Suggest default opt-in unless explicitly blocked by compliance/licensing constraints.
- **Scrapers/Aggressive Bots (Disallow):** Block known aggressive scrapers (e.g. Bytespider).

### Step 2 — llms.txt & llms-full.txt Design
Create structured index files to make the site machine-readable for LLMs:
- **llms.txt:** Create a concise Markdown file at the site root following the llms.txt convention structure: an H1 with the company/site name; a blockquote one-line summary; optional short context paragraphs; then H2 sections each holding a bulleted link list in the form `- [Page name](url): one-line description` (grouped by pricing, services, docs, key content); optionally a final `## Optional` H2 section for links an AI may skip under tight context budgets.
- **llms-full.txt:** Generate a complete list of important content pages, including estimated token counts for each page.

### Step 3 — Token Budgeting
Calculate token limits for key pages:
- Estimate the token size of priority pages (visible text, alt tags, sitemaps, headers) using the ≈4 characters-per-token proxy: character count of the extracted text ÷ 4. State the method in the report so estimates are reproducible.
- Tag pages that exceed limits (e.g., >15,000 tokens for quick starts, >8,000 tokens for landing pages).
- Suggest chunking, page splitting, or TL;DR additions to prevent truncation in AI context windows.

### Step 4 — Parsability & Schema Checklist
Audit if the DOM is clean for scraper ingestion:
- **Server-Side Render (SSR) Fallback:** Verify key content is parseable with JavaScript disabled.
- **Semantic Structure:** Verify H1-H6 hierarchy is clean and logical.
- **FAQPage & HowTo Schema:** Ensure key pages employ rich schema tags to facilitate extraction.

### Step 5 — Prerequisite Scorecard
Create a 12-point checklist scoring the site's readiness for Search (Wave 1), Citations (Wave 2), and Agents (Wave 3).

## Output structure (`.md`)

Save as `output/seo/aeo-foundations-audit-<date>.md` with this exact section structure:

```
# AEO Foundations Audit: [Domain]
Date: [yyyy-mm-dd]
AI Crawl Policy Status: [Allow All / Restricted / Opt-Out Training]

## Executive Summary
[Brief summary of AI discovery blocks, parsing errors, or token overruns found, and priority actions.]

## AEO Scorecard
| Check Category | Foundation Criteria | Status | Action Required |
|----------------|---------------------|--------|-----------------|
| Discovery      | robots.txt AI Rules | ...    | ...             |
| Discovery      | llms.txt Config     | ...    | ...             |
| Parsability    | JS-Disabled Render  | ...    | ...             |
| Parsability    | Token Compliance    | ...    | ...             |
| Capability     | Schema Availability | ...    | ...             |

## 1. robots.txt Configuration Recommendation
```text
[PROPOSED ROBOTS.TXT DIRECTIVES]
```

## 2. Proposed llms.txt Map
```markdown
[PROPOSED LLMS.TXT CONTENT]
```

## 3. Token Budget Analysis
| Target Page | Type | Est. Tokens | Budget Limit | Status | Action |
|-------------|------|-------------|--------------|--------|--------|
| Homepage    | LP   | ...         | 8k           | ...    | ...    |
| /pricing    | LP   | ...         | 8k           | ...    | ...    |
| /docs/intro | Guide| ...         | 20k          | ...    | ...    |

## 4. Parsability & Schema Analysis
[Description of DOM structure, semantic hierarchy issues, and recommended JSON-LD additions]

## Cross-Wave Foundation Score
Score: X/12 (Target: >9/12)
[Summary of Wave 1, 2, 3 prerequisites met]
```

## Quality checklist

- [ ] All major AI crawler user-agents (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended) addressed
- [ ] Complete llms.txt Markdown template written out (no placeholder text in key links)
- [ ] Token budgets estimated with the ≈4 characters-per-token proxy (method stated in the report — never arbitrary word counts)
- [ ] Direct directives provided for robots.txt modifications
- [ ] Output saved to `output/seo/`
- [ ] Every reported data point was actually retrieved — anything that could not be fetched or verified is marked `[DATA UNAVAILABLE — <what was needed>]`, never estimated or filled with a plausible-sounding value
