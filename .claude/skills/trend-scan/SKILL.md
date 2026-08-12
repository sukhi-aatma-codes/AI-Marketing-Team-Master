---
name: trend-scan
description: >
  Use this skill whenever the user wants a fast, engagement-ranked pulse check on what's
  trending around a topic right now — using only free, keyless sources (Hacker News, GitHub,
  Reddit, general web search). Trigger on requests like "what's trending in X right now",
  "scan Reddit and HN for chatter about Y", "what's getting engagement on this topic lately",
  "pull recent buzz on Z", or any request for a dated, cited trend snapshot rather than a full
  market analysis. Produces a raw evidence feed that can optionally inform market-research —
  it does not replace it.
---

# Trend Scan

Produces a dated, cited, engagement-ranked snapshot of what's currently being discussed around
a topic across free, keyless sources. This is raw evidence, not analysis — synthesis, brand
opportunity framing, and recommendations belong to `market-research`, not this skill. The `.md`
output is a machine-readable handoff other skills and agents can fold in as supporting evidence.

## Before starting

No `_context\` file is required — this is a brand-agnostic scan tool that works on any topic.
If the topic maps to the active brand's service lines or ICP, optionally read
`_context/Brand_Product_Offerings.md` for seed terms, but never require it.

## Clarify scope/inputs first

Confirm with the user if not already clear from the request:
1. **Topic or query terms** — what to scan for
2. **Timeframe** — default: last 30 days, unless stated otherwise
3. **Sources to include/exclude** — default: all four (Hacker News, GitHub, Reddit, web)
4. **Depth** — quick scan (top 5–10 results per source) or deep scan (multiple query variants per source)

If the request already states these clearly, skip asking and proceed.

## Workflow

### Step 1 — Hacker News
Query the HN Algolia Search API (keyless, no auth required):
- `https://hn.algolia.com/api/v1/search?query=<topic>&tags=story` for stories
- `https://hn.algolia.com/api/v1/search?query=<topic>&tags=comment` for discussion volume

Fetch via WebFetch. This endpoint is reliable — no fallback needed. Record points, comment
count, story URL, and post date for each result.

### Step 2 — GitHub
Query the unauthenticated GitHub REST search endpoint:
- `https://api.github.com/search/repositories?q=<topic>&sort=updated`

Fetch via WebFetch. This endpoint is rate-limited to roughly 10 requests/minute unauthenticated —
if it returns a 403, fall back to the public search UI
(`https://github.com/search?q=<topic>&type=repositories`) via WebSearch or WebFetch. Record star
count, fork count, last-push date, and repo URL for each result.

### Step 3 — Reddit
Attempt `https://www.reddit.com/search.json?q=<topic>&sort=top` via WebFetch first. Reddit
frequently blocks non-browser requests (403/429) — treat this as expected, not exceptional.
On any failure, immediately fall back to `WebSearch("site:reddit.com <topic>")` and read
whatever thread titles, upvote counts, and comment counts are visible in the results or on
fetched thread pages. Never block the scan waiting on Reddit to succeed. If both the JSON
endpoint and the WebSearch fallback return nothing usable, log Reddit as a zero-result source
(see Output rules, Law 3).

### Step 4 — General web
Run a WebSearch pass for the topic to catch anything the platform-specific searches missed
(news coverage, forum threads, industry blogs). If `exa` or `firecrawl` MCP tools happen to be
configured with a working key, they may be used as optional accelerants — but never assume
they're present; WebSearch is the guaranteed baseline every environment has.

### Out of scope, by design
X/Twitter, YouTube, TikTok, and Polymarket are explicitly not covered — all require paid APIs
or browser cookie authentication, which this skill intentionally avoids. State this in the
output rather than silently omitting these platforms.

## Engagement scoring

Do not compute a unified numeric score across sources — comparing Reddit upvotes to GitHub
stars to HN points as one number is false precision. Instead:
- Report each finding's **native metric as-is** (e.g., "1,204 HN points / 340 comments", "2.3k
  GitHub stars, pushed 3 days ago").
- Assign a qualitative **High / Medium / Low tier**, computed relative to that source's own
  result set for this scan run (top result this run = High, bottom quartile = Low) — not
  against a fixed global threshold.
- Separately flag **cross-source corroboration**: a finding appearing independently on 2+
  sources is the real trend-strength signal, distinct from engagement tier.

## Output rules (non-negotiable)

1. **Never fabricate an engagement number.** If a count could not be directly read from a
   fetched response, mark it `[not visible]` — never estimate a plausible-sounding figure.
2. **Never invent or guess a source URL.** Only cite URLs actually returned by a fetch or
   search call.
3. **Report a zero-result source explicitly, on its own line.** Never silently omit a
   platform that returned nothing or failed — a thin-looking scan that's honest beats a
   full-looking one that isn't.
4. **Distinguish "cross-source trend" from "single high-engagement outlier."** Only mark a
   finding as corroborated if it independently appears on 2+ sources; one loud thread on one
   platform is a signal, not a trend.
5. **Date-stamp every finding** (post date + date scanned), not just the report header —
   "last 30 days" content ages fast and a brief can go stale within the same week.
6. **State findings as reported, not editorialized.** Summarize what the source said or
   showed; do not add unstated implications ("this proves demand is exploding"). Synthesis
   belongs to `market-research`, not this skill.
7. **If a source returns blocked/403/429, name it explicitly** rather than presenting a thin
   result as if the platform was fully checked.

## Save output

Save as `output/trend-scan/trend-scan-<topic>-<yyyy-mm-dd>.md`.

## Output structure (`.md`)

```
# Trend Scan: [Topic]
Scan window: [start date] to [end date] (default: last 30 days)
Date scanned: [yyyy-mm-dd]
Sources attempted: Hacker News, GitHub, Reddit, Web search
Sources with results: [list] | Sources with zero results or blocked: [list, with reason]

## Findings

### Finding 1: [Short claim/topic label]
- Source: [Hacker News / GitHub / Reddit / Web]
- Engagement: [native metric] — Tier: [High/Medium/Low, relative to this source's results this run]
- URL: [exact URL fetched]
- Posted: [yyyy-mm-dd or "unknown — not visible"]
- Cross-source corroboration: [Trending — also seen on: <sources> / Single-source signal]
- Summary: [1–3 sentences, description only, no editorializing]

[Repeat per finding, ordered by corroboration then engagement tier]

## Zero-Result / Blocked Sources
[Source, query attempted, what happened, fallback used]

## Cross-Source Trend Summary
[Bullet list of only findings that hit 2+ sources]

## Sources
[Every URL cited above, plus access date]
```

## Quality checklist

- [ ] All four sources attempted and logged, even if zero-result or blocked
- [ ] Every engagement number traceable to a fetched response — none estimated
- [ ] Every URL was actually returned by a fetch or search call — none guessed
- [ ] Cross-source corroboration flag only set where 2+ independent sources confirm it
- [ ] Every finding has both a posted date and the date scanned
- [ ] Out-of-scope platforms (X, YouTube, TikTok, Polymarket) noted as intentionally excluded, not silently missing
- [ ] Saved to `output/trend-scan/` with the correct filename convention
- [ ] Every reported data point was actually retrieved — anything that could not be fetched or verified is marked `[DATA UNAVAILABLE — <what was needed>]`, never estimated or filled with a plausible-sounding value
