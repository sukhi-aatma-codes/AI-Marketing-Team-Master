---
name: technical-seo-audit
description: >
  Use this skill whenever the user wants to audit a website's technical SEO health,
  crawlability, indexation, internal linking structure, structured data, mobile
  compatibility, or Core Web Vitals performance. Trigger on requests like "run a
  technical SEO audit", "check if our site is indexed properly", "audit our sitemaps
  and robots.txt", "check Core Web Vitals for acme.com", or "find technical search
  issues on our domain". Always use this skill at the beginning of an SEO engagement
  to establish the technical baseline before content or on-page optimization.
---

# Technical SEO Audit

Audits a website's technical search infrastructure and performance metrics, producing a
structured technical SEO audit report with prioritized recommendations. The `.md` output is the
machine-readable handoff for downstream agents and skills (on-page-optimization, campaign-strategist,
blog-writer). The PDF is the human-ready deliverable for stakeholders.

## Before starting

Read these context files every time — do not rely on prior session memory:
- `_context/Brand_Context.md` — company overview and primary domains
- `_context/Brand_Growth_Marketing_Context.md` — growth goals and priority channels

## Clarify scope first

Before auditing, confirm with the user:
1. **Target URL/Domain:** The domain to audit (e.g. acme.com)
2. **Crawl Depth:** Desktop only, mobile only, or both (Default: mobile-first)
3. **Analytics Access:** Do we have Google Search Console or Google Analytics exports to inspect? (if yes, prompt user to supply data)
4. **Focus Area:** General health check, or specific problem (e.g., indexation drop, Core Web Vitals failure)

If the user's request makes these clear, skip asking and proceed.

## Audit workflow

### Step 1 — Crawlability & Indexation
Search or inspect the target site's:
- **robots.txt:** Inspect directives, check for blocked critical resources or search paths.
- **XML Sitemaps:** Verify sitemap index locations, look for non-canonical URLs, redirects, or 404s in the sitemap.
- **Index Coverage:** Check status codes (200, 301, 302, 404, 5xx) of key pages, check for incorrect meta robots tags (noindex).
- **Crawl Budget:** Identify parameter-heavy URLs, faceted navigation waste, or duplicate folders that bleed crawl activity.

### Step 2 — Site Architecture & Internal Linking
Verify the URL hierarchy and internal link distribution:
- **URL Structure:** Verify clean, descriptive, lower-case, hyphen-separated slugs. Check directory depth (max 3-4 clicks from homepage).
- **Internal Link Equity:** Check for orphaned pages, broken links (404), redirect chains, and anchor text distribution (ensure descriptive anchor text, no generic "click here").
- **Canonicalization:** Ensure self-referencing canonicals are correctly configured across all unique content pages.

### Step 3 — Page Experience & Core Web Vitals
Inspect field or lab performance data:
- **Largest Contentful Paint (LCP):** Target < 2.5s
- **Interaction to Next Paint (INP):** Target < 200ms
- **Cumulative Layout Shift (CLS):** Target < 0.1
- **HTTPS & Security:** Verify SSL certificate and HTTPS redirection rules.

### Step 4 — Structured Data (Schema)
Inspect the site's rich result configuration:
- **Existing Schema:** Check for presence of Organization, Website, Article, Product, LocalBusiness, FAQPage, or Breadcrumb List markup.
- **Validation Errors:** Check validation logs or check markup manually for missing required fields.
- **Opportunities:** Identify template-level schema opportunities to capture rich snippets.

### Step 5 — Mobile Optimization
Analyze mobile-friendliness:
- **Viewport Config:** Verify correct viewport meta configuration.
- **Content Formatting:** Check font sizes, touch target sizes (>48x48px), and horizontal scrolling issues on standard mobile dimensions.

## Output structure (`.md`)

Save as `output/seo/technical-seo-audit-<date>.md` with this exact section structure:

```
# Technical SEO Audit: [Domain]
Date: [yyyy-mm-dd]
Prepared for: [client domain/purpose]

## Executive Summary
[Brief paragraph summarizing the overall technical health score (e.g. 82/100), major blockers found, and estimated impact of resolving them.]

## Priority Fix Matrix
| Priority | Issue | Category | Description | Estimated Impact |
|----------|-------|----------|-------------|------------------|
| Critical | ...   | Crawlability | ... | High |
| High     | ...   | CWV / UX | ... | Med-High |

## 1. Crawlability & Indexation
### robots.txt Analysis
[DIRECTIVES AND ISSUES FOUND]

### XML Sitemap Health
[SITEMAP URLS AND HEALTH STATUS]

### Status Code & Index Coverage
[INDEXATION ISSUES, NOINDEX CONFIRMATIONS]

## 2. Site Architecture & Internal Linking
### URL Slugs & Hierarchy
[URL ASSESSMENT]

### Link Distribution & Canonical Tags
[CANONICAL ISSUES, ORPHANED PAGES, REDIRECT CHAINS]

## 3. Page Experience & Core Web Vitals
| Metric | Mobile | Desktop | Status | Recommendation |
|--------|--------|---------|--------|----------------|
| LCP    | ...    | ...     | ...    | ...            |
| INP    | ...    | ...     | ...    | ...            |
| CLS    | ...    | ...     | ...    | ...            |

## 4. Structured Data (Schema)
[CURRENT SCHEMAS AND DEFICIENCIES]

## 5. Mobile Compatibility
[MOBILE-FRIENDLINESS FINDINGS]

## Sources & Tools Used
[List all tools, page speed reports, or documentation referenced]
```

## Rich deliverable

After saving the `.md`, invoke `document-skills:pdf` to render it as a formatted PDF.
Save as `output/seo/technical-seo-audit-<date>.pdf`.

## Quality checklist

- [ ] Every technical issue identified is paired with a clear, developer-actionable fix description
- [ ] Core Web Vitals metrics are populated with actual data or estimated tests (no placeholder guesses)
- [ ] Internal linking audit checks for both desktop and mobile crawl paths
- [ ] Schema analysis lists specific missing properties, not just missing schema types
- [ ] Priority Fix Matrix ranks items by true search visibility impact vs. implementation effort
- [ ] PDF generated and saved to `output/seo/`
- [ ] Every reported data point was actually retrieved — anything that could not be fetched or verified is marked `[DATA UNAVAILABLE — <what was needed>]`, never estimated or filled with a plausible-sounding value
