# MCP Tool Setup

This workspace integrates external tools via MCP (Model Context Protocol) servers configured in
`.mcp.json`. None of them are required to produce output — every capability category degrades
gracefully to a baseline that works with zero setup. Paid/configured tools improve quality and
depth; they are never gates.

## The tiered fallback principle

Every skill or agent that touches an external tool is written to try the best available option
first and fall back automatically — it should never block a deliverable because a tool isn't
configured. If you read a skill file and it says "if X isn't available, fall back to Y," that's
this principle in practice, not an apology.

| Capability | Best (configured) | Better (configured) | Always available (zero setup) |
|---|---|---|---|
| Image generation | Ideogram / Flux / Nano Banana / GPT Image (whichever has a key set) | Unsplash / Pexels stock photography | A detailed, ready-to-paste image prompt/creative brief for manual generation |
| Web research | Exa (semantic search) | Firecrawl (clean page extraction) | Claude's built-in `WebSearch` / `WebFetch` tools — no MCP, no key, works today |
| Analytics / marketing data | Windsor.ai (350+ connectors) | GA4 official server (narrower, more setup) | User-pasted CSV/export data — `data-analyst` already supports this |
| Broad/long-tail tool access | Composio (500+ tools, manual setup) | Windsor.ai already covers most marketing-specific long tail | Native MCP servers below, or ask the user to paste the data manually |

## Servers configured in `.mcp.json`

### Image generation

| Server | What it does | Auth tier | Env var |
|---|---|---|---|
| `ideogram` | Photorealistic/illustrative image generation, used by `social-creative-designer` | Official, API key | `IDEOGRAM_API_KEY` |
| `flux` | Black Forest Labs FLUX models — official hosted MCP | Official, OAuth (browser sign-in on first use, no key) | none |
| `nano-banana` | Google Gemini 2.5 Flash Image ("Nano Banana") generation/editing | Community package, API key | `GEMINI_API_KEY` |
| `gpt-image` | OpenAI `gpt-image-1` generation/editing | Community package, API key | `OPENAI_API_KEY` |
| `unsplash` | Stock photo search | Community package, API key | `UNSPLASH_ACCESS_KEY` |
| `pexels` | Stock photo/video search | Community package, API key | `PEXELS_API_KEY` |

Used by: `.claude/skills/image/SKILL.md`, `.claude/skills/social-creative-designer/SKILL.md`, `.claude/skills/ad-creative/SKILL.md`.

### Design assembly

| Server | What it does | Auth tier | Env var |
|---|---|---|---|
| `canva` | Typography, layout assembly, brand-kit templates, final export | Official, hosted, OAuth | none |

### Web research

| Server | What it does | Auth tier | Env var |
|---|---|---|---|
| `exa` | Neural/semantic web search, content/competitor discovery | Official, API key | `EXA_API_KEY` |
| `firecrawl` | Clean page → markdown extraction, structured scraping | Official, API key | `FIRECRAWL_API_KEY` |

Used by: `market-researcher`, `seo-specialist`, `ai-citation-strategist`. Claude's built-in
`WebSearch`/`WebFetch` tools work without either of these — they're an upgrade for structured
results and semantic matching, not a prerequisite.

### Analytics / marketing data

| Server | What it does | Auth tier | Env var |
|---|---|---|---|
| `windsor` | 350+ marketing/ads/analytics/CRM/commerce connectors (GA4, Meta Ads, Google Ads, LinkedIn Ads, HubSpot, Salesforce, Shopify, Stripe, and more) via one server, including write actions | Official, hosted, OAuth | none |

Used by: `data-analyst`. Prefer this over a standalone GA4 server unless you need GA4-specific
depth Windsor's pass-through doesn't cover (see "Documented but not configured" below).

### Document research

| Server | What it does | Auth tier | Env var |
|---|---|---|---|
| `notebooklm` | Multi-document analysis and synthesis | Official, hosted | none |

## Setting environment variables (Windows)

`.mcp.json` references credentials as `${VAR_NAME}` — Claude Code expands these from your real
OS environment variables. It does not auto-load a `.env` file (not supported yet). Set each one
you intend to use:

**PowerShell (persists across sessions):**
```powershell
setx IDEOGRAM_API_KEY "your-key-here"
setx EXA_API_KEY "your-key-here"
setx FIRECRAWL_API_KEY "your-key-here"
setx GEMINI_API_KEY "your-key-here"
setx OPENAI_API_KEY "your-key-here"
setx UNSPLASH_ACCESS_KEY "your-key-here"
setx PEXELS_API_KEY "your-key-here"
```

`setx` only takes effect in **new** terminal sessions — close and reopen your terminal (and
restart Claude Code) after running it. For the current session only, use `$env:VAR_NAME = "..."`
instead, but that won't persist.

You only need to set variables for the tools you actually plan to use — an unset variable means
that one server fails to start, not that the workspace breaks. Skills route around it per the
fallback table above.

## Documented but not configured

These three need a setup step only you can complete (interactive OAuth or account-specific
values), so they're documented here rather than pre-filled into `.mcp.json` with placeholders
that would just fail silently.

### Composio (broad connector, 500+ tools)
Run this yourself in a terminal:
```bash
npx @composio/mcp@latest setup
```
This opens a browser for OAuth and walks you through tool selection. Once complete, it tells you
what to add to `.mcp.json` — bring that back and it can be added in a follow-up pass. Given
Windsor.ai already covers most of the marketing-specific long tail with simpler auth, only do
this if you need a tool outside marketing/ads/CRM/commerce (e.g. Slack, Notion, Google Sheets).

### GA4 official server (if you want GA4-specific depth beyond Windsor.ai)
The Google-maintained server is Python-based, not `npx`-based, and needs a GCP service account:
1. Create or use a GCP project, enable the Google Analytics Data API
2. Create a service account, grant it Viewer access on the GA4 property in question
3. Download the service account JSON key
4. Set `GOOGLE_APPLICATION_CREDENTIALS` to the key file's path and `GA4_PROPERTY_ID` to the
   property ID
5. Install and run via `pipx` per the official server's own instructions — this one isn't a
   single `npx` line like the others, so it's not pre-added to `.mcp.json`

### Windsor.ai via claude.ai connector
Separate from the `windsor` entry in `.mcp.json` above (which works independently). If you also
want it available through claude.ai's own connector system (useful outside this project),
authorize it at claude.ai → Settings → Connectors. You don't need to do this for the
project-level `.mcp.json` entry to work.

## Adding more tools later

Follow the pattern above: verify the package/URL actually exists and is current (don't trust
training-data assumptions about npm package names — search), prefer official servers over
community ones when both exist, use `${VAR_NAME}` for any credential, and document the new
server's fallback tier here before wiring it into a skill.
