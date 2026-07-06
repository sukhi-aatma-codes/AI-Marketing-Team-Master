# 🧠 Foundry Collective — Project Overview

## What This Project Is

**Foundry Collective** is a **personal, portable marketing operating system** built for Claude (Anthropic's AI) — designed to function as the user's marketing department wherever they work, now or at a future employer. Each sub-agent represents a sub-function within that marketing department (campaign strategy, content, creative, SEO, PR, social, lead gen, podcast/webinar programs, etc.), and together they produce everything a marketing org needs: strategy, content, ads, visuals, research, and reports.

The workspace directory and internal file paths still read `AI Marketing Team Master` (see Workspace Conventions in `CLAUDE.md`) — that's the technical/folder name. **Foundry Collective** is the name of the system itself, the one used in conversation and in any materials describing it to others.

It's designed to move with the user across employers — just swap the `_context\` files when changing organizations and every agent and skill adapts automatically. No hardcoded employer/brand info anywhere.

---

## 🏗️ Architecture Overview

```
AI Marketing Team Master
├── _context\         ← Active brand's "brain" (6 files)
├── _sop\             ← Standard operating procedures
├── _samples\         ← Raw brand input drop zone (PDFs, decks, images, ad archives)
├── _templates\       ← Active brand's reusable .pptx deck template + analysis
├── skills\           ← 37 reusable execution modules
└── .claude\agents\   ← 13 AI sub-agents with specialized roles
```

---

## 👥 The 13 Sub-Agents (The "Team")

| Agent | Color | Role |
|-------|-------|------|
| `brand-onboarder` | 🩵 Teal | Scrapes a brand URL → builds all 6 `_context\` files from scratch |
| `campaign-strategist` | 🟣 Purple | Turns marketing goals into full campaign strategies (now including paid media & email) |
| `market-researcher` | 🔵 Blue | Competitive intelligence + keyword research combined |
| `content-creator` | 🟢 Green | Multi-format content packages (blog + social + landing page + email) |
| `creative-designer` | 🟡 Yellow | Visual direction, social graphics, ad creative specs |
| `data-analyst` | 🟠 Orange | Campaign performance analysis + visual reporting |
| `seo-specialist` | 🔵 Blue | Technical site health + on-page search engine optimization & strategy |
| `ai-citation-strategist` | 🟣 Purple | Generative/Answer Engine Optimization (GEO/AEO) & citation scorecarding |
| `pr-comms` | 🔵 Blue | Earned media relations, AP-style press releases, crisis response, thought leadership |
| `social-strategist` | 🔵 Blue | Social channel growth playbook, content calendar planning, and platform strategy |
| `podcast-strategist` | 🟣 Purple | Podcast concept positioning, guest research, scripting, and show notes planning |
| `lead-generation-engine` | 🟦 Indigo | Lead funnel architecture — channel mix, MQL/SQL scoring, nurture flow design |
| `webinar-strategist` | 🔴 Crimson | Webinar program planning — concept, agenda, promotion, registration-to-follow-up |

---

## 🔧 The 37 Skills (Atomic Execution Modules)

Skills are single-purpose, reusable tasks agents can call:

| Skill | Output |
|-------|--------|
| `ad-creative` | Ad copy + paid creative briefs |
| `blog-writer` | Long-form SEO blog posts |
| `branded-deck` | Pitch / sales / internal decks |
| `campaign-brief` | Source-of-truth campaign brief docs |
| `campaign-report` | Formatted performance reports |
| `data-visualization` | Charts and visual data outputs |
| `keyword-research` | SEO keyword research reports |
| `lead-magnet` | Gated asset strategy (format/buyer-stage/gating/distribution) + content, checklists, whitepapers |
| `copy-editing` | Seven Sweeps edit pass + expert panel scoring for existing copy |
| `image` | Blog heroes, OG images, banners, mockups, image optimization |
| `lp-builder` | Landing page copy and structure |
| `market-research` | Competitive landscape reports |
| `social-copy` | Social media captions and posts |
| `social-creative-designer` | Visual specs for social graphics |
| `build-brand-context` | Refreshed Brand_Context.md file |
| `build-brand-voice` | Refreshed Brand_Voice_Guide.md file |
| `build-brand-style` | Refreshed Brand_Style.md file |
| `build-brand-products` | Refreshed Brand_Product_Offerings.md file |
| `build-brand-growth` | Refreshed Brand_Growth_Marketing_Context.md file |
| `build-brand-style-reference` | Refreshed Brand_Style_Reference.md — generative visual style library + prompt starters |
| `build-brand-deck-template` | Built/refreshed `_templates/Brand_Deck_Template.pptx` — the real reusable deck `branded-deck` builds from |
| `sample-archive-index` | Triage manifest for bulk `_samples\` drops, routing files to the right deep-extraction skill |
| `technical-seo-audit` | Structured technical SEO audit reports |
| `on-page-optimization` | Copy & HTML on-page optimization checks |
| `aeo-foundations` | AI crawler rules, robots.txt, and llms.txt maps |
| `citation-audit` | AI recommendation engine scorecard and fix pack |
| `press-release` | AP-style press releases for wire distribution |
| `media-pitch` | Personalized email pitches for journalists |
| `crisis-response` | Incident playbooks & holding statements |
| `executive-thought-leadership` | Opinion articles & CEO LinkedIn thought pieces |
| `email-copy` | Email welcome sequences & drip newsletters |
| `social-strategy` | Social platform calendars and campaigns |
| `podcast-episode-plan` | Podcast scripting & research sheets |
| `podcast-show-notes` | Podcast episode show notes & summaries |
| `abm-account-plan` | Account tiering, scoring, stakeholder maps for ABM campaigns |
| `lead-gen-strategy` | Lead funnel architecture, MQL/SQL scoring, nurture flow maps |
| `webinar-plan` | Webinar concept, agenda, promotion, and follow-up plans |

---

## 🔄 How the Flow Works

### Step 1 — Brand Onboarding (always first)

```
User provides URL or brand materials
        ↓
brand-onboarder agent scrapes & analyzes
        ↓
Produces 6 _context\ files:
  • Brand_Context.md                    ← positioning, ICPs, differentiators
  • Brand_Voice_Guide.md                ← tone rules, banned jargon, writing style
  • Brand_Style.md                      ← hex colors, fonts, visual grid
  • Brand_Product_Offerings.md          ← services, buyer personas, pain points
  • Brand_Growth_Marketing_Context.md   ← channels, funnel, goals, benchmarks
  • Brand_Style_Reference.md            ← generative visual style library + prompt starters
                                           (only when real creative samples exist — see below)
```

> No marketing execution (campaigns, content, ads) may begin until the first 5 context files
> exist. `Brand_Style_Reference.md` is the exception — it requires real visual samples to
> ground it, so it's built (via `build-brand-style-reference`) whenever samples are available,
> not invented from nothing.

**Bulk sample drops:** If the user has dozens of raw files (ad archives, decks, social
creative) to onboard from, run `sample-archive-index` first — it scans `_samples\` and routes
each file to the right deep-extraction skill (`build-brand-style` for decks, `build-brand-
style-reference` for image creative) instead of reading everything blind.

---

### Step 2 — Common Agent Pipelines

| Workflow | Agent Sequence |
|----------|----------------|
| **New campaign launch (full)** | `campaign-strategist` → `content-creator` + `creative-designer` *(parallel)* |
| **SEO content push** | `market-researcher` → `content-creator` *(blog + landing page)* |
| **Paid campaign** | `campaign-strategist` → `creative-designer` → `content-creator` *(landing page)* |
| **Performance review** | `data-analyst` → `campaign-strategist` *(feeds next campaign)* |
| **New market entry** | `market-researcher` → `campaign-strategist` → `content-creator` |
| **New brand onboarding** | `brand-onboarder` → any other agent or skill |
| **SEO overhaul** | `seo-specialist` → `content-creator` *(content gap execution)* |
| **AI visibility push** | `seo-specialist` *(aeo-foundations)* → `ai-citation-strategist` |
| **PR campaign** | `pr-comms` → `content-creator` + `social-strategist` *(amplification)* |
| **Podcast launch** | `podcast-strategist` → `content-creator` *(repurpose)* + `social-strategist` *(promote)* |
| **Social media program** | `social-strategist` → `content-creator` + `creative-designer` |
| **Email-driven campaign** | `campaign-strategist` → `content-creator` *(landing page)* + `email-copy` *(sequence)* |

---

### Step 3 — Skill vs. Agent Decision Rule

| Situation | What to do |
|-----------|-----------|
| Single, specific, bounded deliverable with a clear brief | Invoke a **skill** directly |
| Open-ended, multi-step, or requires decisions across formats | Delegate to an **agent** |

**Examples:**
- `"Write a blog post on X"` → invoke `blog-writer` skill directly
- `"We're launching X and need a content push"` → delegate to `content-creator` agent

---

## 📂 Output Routing

Finished outputs are saved to the folder matching the deliverable type:

| Deliverable | Folder |
|-------------|--------|
| Ad copy, creative briefs, paid campaign assets | `output\ads\` |
| Landing pages, web/site copy | `output\pages\` |
| Decks (sales, pitch, internal) | `output\presentations\` |
| Marketing reports, analyses, audits | `output\reports\` |
| SEO briefs, technical audits, keyword research, AEO/citation audits | `output\seo\` |
| Social posts, calendars, captions | `output\social\` |
| Press releases, pitches, crisis playbooks, thought leadership drafts | `output\pr\` |
| Email copy, welcome and nurture sequences | `output\email\` |
| Podcast episode briefs, outline scripts, show notes | `output\podcasts\` |
| Webinar plans, agendas, speaker briefs, promotion timelines, follow-up outlines | `output\webinars\` |
| ABM account plans, lead generation funnel strategy | `output\reports\` |
| Raw Ideogram-generated images (working files) | `output\ideogram_output\` |

---

## 🔌 External Integrations

All MCP integrations are **tiered, not required** — every capability they support has a
zero-setup fallback built into the relevant skill/agent (built-in `WebSearch`/`WebFetch`,
user-pasted data, or a manual creative brief). See `MCP_SETUP.md` for full setup instructions
and the fallback chain per capability.

| Integration | Purpose | Auth |
|-------------|---------|------|
| **Ideogram MCP** | AI image generation — raw outputs to `output\ideogram_output\`, finals move to `output\social\` | API key |
| **Flux MCP** | Black Forest Labs FLUX image generation, official hosted server | OAuth |
| **Nano Banana MCP** | Gemini 2.5 Flash Image generation/editing | API key |
| **GPT Image MCP** | OpenAI `gpt-image-1` generation/editing | API key |
| **Unsplash MCP** | Stock photo search | API key |
| **Pexels MCP** | Stock photo/video search | API key |
| **Canva MCP** | Typography, layout assembly, brand-kit templates, final export | OAuth |
| **Exa MCP** | Neural/semantic web search for research and competitive discovery | API key |
| **Firecrawl MCP** | Clean page-to-markdown extraction for audits and research | API key |
| **Windsor MCP** | 350+ marketing/ads/analytics/CRM/commerce connectors in one server | OAuth |
| **NotebookLM MCP** | Multi-document analysis and synthesis | hosted |

---

## 📋 Shared Memory: Brand Insights Ledger

`_context\Brand_Insights_Ledger.md` is a **cross-agent shared memory** file. Every agent reads and writes to it, accumulating intelligence over time:

| Section | Updated By |
|---------|-----------|
| Core Buyer Personas & Objections | `market-researcher`, `campaign-strategist` |
| Creative & Formatting Insights | `creative-designer` |
| Copywriting & Voice Preferences | `content-creator` |
| Performance & Anomaly Analytics | `data-analyst` |
| Lead Generation Intelligence | `lead-generation-engine` |
| Webinar Intelligence | `webinar-strategist` |

This means **the team gets smarter over time** as campaigns run and user feedback is captured.

---

## ⚙️ Global Rules

1. **Brand voice is non-negotiable** — every customer-facing output must conform to `Brand_Voice_Guide.md` and `Brand_Style.md`.
2. **Cite every claim** — if it's not in `_context\` or a verifiable source, mark it as a draft assumption.
3. **No invented proof points** — no fake case studies, customers, or metrics. Use `[TBD]` placeholders.
4. **Never write to `_context\`** without explicit user instruction (exception: `brand-onboarder` agent and the `build-brand-*` skills, including `build-brand-style-reference`, by design).
5. **SOPs are law** — when a workflow SOP exists in `_sop\`, follow it. If none exists for a recurring task, suggest creating one.
6. **Skills and agents must be brand-agnostic** — no hardcoded brand details, ever. Pull context from `_context\` at runtime.
7. **No AI artifacts, generic buzzwords, or em dashes (—) in editorial copy** — editorial drafts (blogs, social, email, landing pages, thought leadership, PR) must read as entirely human-authored. Avoid standard LLM artifacts, generic buzzwords (*delve, leverage, robust, testaments, revolutionize, seamless*), and ban em dashes (replace with commas, colons, or parentheses).


---

---

## 📝 Changelog

### v3.7 — 2026-07-06

#### Named the project — Foundry Collective

The system now has a name the user calls it by in conversation and shares with colleagues:
**Foundry Collective**. This is a naming/branding update only — no change to the workspace
directory name, agent/skill files, or `_context\` mechanics. `AI Marketing Team Master` remains
the technical folder/path name (see Workspace Conventions in `CLAUDE.md`); Foundry Collective is
the name used when describing the system to people rather than to the filesystem.

### v3.6 — 2026-06-30

#### Reframing + 2 new skills + 1 enriched, from coreyhaines31/marketingskills

**Framing correction**: this was described throughout the top-level docs as a "brand-agnostic AI marketing agency workspace" serving external clients. That was never accurate — it's the user's personal, portable marketing operating system, built to function as their marketing department at whatever organization they work for, now or in the future. Each sub-agent represents a sub-function within that one marketing org, not a separate client engagement. The swappable `_context\` mechanism is unchanged — it's how the system moves with the user to a new employer — only the framing language in `CLAUDE.md`, this file, and `HOW_TO_USE.md` was corrected. Agent/skill files were untouched since their internal "brand-agnostic, read `_context\` at runtime" instructions were already accurate.

**Skill review**: evaluated `github.com/coreyhaines31/marketingskills` (40 PLG/SaaS-focused skills). Most were out of scope — anything assuming ownership of the product/app itself (paywalls, signup flows, in-app onboarding, churn dunning, ASO) doesn't fit a marketing function that doesn't own the product, consistent with excluding sales/CRM/revops when the b2b-agents repo was reviewed earlier. Three items made the cut:

- **New skill**: `image` — general-purpose marketing image production and optimization (blog heroes, OG images, profile/directory banners, product mockups, image format/compression guidance), distinct from `social-creative-designer` (LinkedIn carousels specifically) and `ad-creative` (paid ad specs). Owned by `creative-designer`.
- **Enriched `lead-magnet`** (not a new skill): the source repo's `lead-magnets` skill was pure strategy (format-by-buyer-stage matching, gating trade-offs, distribution plan, conversion benchmarks) with no content-writing capability — the inverse of our existing skill, which wrote content with no strategic framework first. Merged the strategy sections into our existing skill rather than replacing it, preserving its branded-PDF/`Brand_Style_Reference.md` integration.
- **New skill**: `copy-editing` — the Seven Sweeps framework (Clarity → Voice/Tone → So What → Prove It → Specificity → Heightened Emotion → Zero Risk, each with backward re-checks) plus expert panel scoring for high-stakes copy. Closes a real gap — every existing skill writes new copy, nothing reviews/refreshes what already exists. Owned by `content-creator`.
- Also fixed two small pre-existing staleness bugs found while wiring these in: `creative-designer.md`'s skill table still referenced the old hardcoded Cogneesol style codes (`A1–A7 / E1–E3`) instead of pointing at `Brand_Style_Reference.md`; `content-creator.md` said `lead-magnet` produces PDFs "via branded-deck," which `lead-magnet`'s own skill file explicitly forbids (it uses ReportLab — `branded-deck` is for slide decks, not documents).

### v3.5 — 2026-06-30

#### Bug fix — Same hardcoded-template bug, one layer over, in decks

The v3.4 fix addressed `Brand_Style_Reference.md` being hardcoded to a stale demo brand's file. The same bug class existed in `branded-deck`: `skills/branded-deck/assets/Cogneesol_Enterprise_Template.pptx` was a byte-identical copy (verified by MD5) of the Cogneesol reference deck, bundled directly inside the skill folder, with no skill ever producing a fresh template per brand. Every deck `branded-deck` built was still styled off Cogneesol's literal template file — and `_templates\`, which `CLAUDE.md` already documented as the intended convention, never actually existed.

This also confirmed something the user had done manually once before: a sample deck was shared, the system produced an analysis (`cogneesol-deck-analysis.md`) and a matching template (`Cogneesol_Enterprise_Template.pptx`), and that became `branded-deck`'s baseline. This release formalizes that one-off manual sequence into a repeatable skill.

- **New skill**: `build-brand-deck-template` — builds the actual reusable `_templates/Brand_Deck_Template.pptx` (+ companion analysis file), not just markdown. Two modes: deck-derived (reproduces a real source deck's layouts using `build-brand-style`'s extraction) or style-derived defaults (a sensible layout set styled from `Brand_Style.md` alone, when no source deck exists).
- **Fix**: `branded-deck` now reads its template from `_templates/Brand_Deck_Template.pptx` + `_templates/Brand_Deck_Template_Analysis.md` instead of skill-bundled `assets/`/`references/` paths. The hardcoded Cogneesol files were deleted from the skill folder entirely.
- **New folder**: `_templates\` now actually exists, populated only by `build-brand-deck-template` — never manually, never left over from a different brand (brand-onboarder now clears it on brand switch, same as `Brand_Style_Reference.md`).
- `_samples/_reference-examples/cogneesol-deck.pptx` does double duty as a worked example of both "a good source deck" and "what a finished template should look like," since it was already 100% reproducible from native shapes with zero embedded media.

### v3.4 — 2026-06-30

#### Bug fix + new capability — Real per-brand visual style extraction

Investigated whether to add RAG (vector embeddings + retrieval) for bulk sample ingestion (dropping a folder of 20+ ads/decks/images). Decided against it: this workspace has no scripting/database infrastructure today and is wholesale-copied between versions, making a vector index a portability and staleness liability. Built a lightweight alternative instead — and in the process found and fixed a real bug.

- **Bug found**: `_context/Brand_Style_Reference.md` — the generative visual style library read by `social-creative-designer`, `ad-creative`, `campaign-brief`, and `lead-magnet` — was hardcoded to `_samples/social-creatives/Brand_Style_Reference.md` in all four skills, and nothing ever generated or refreshed it. Every onboarded brand was silently inheriting a past demo brand's (Cogneesol's) visual style library, including its specific style codes (A1, E1, etc.) hardcoded inline in `social-creative-designer`'s tool-routing table. This violated the "never assume a brand identity from a prior session" rule everywhere else in the workspace.
- **Fix**: All 4 consumer skills now point to `_context/Brand_Style_Reference.md` (the correct per-brand location). `social-creative-designer`'s routing table was generalized from hardcoded style codes to brand-agnostic visual archetypes (typographic-only / photo-blend / full-photo-bleed / diagram), with the skill reading the active brand's actual style names from `Brand_Style_Reference.md` at runtime.
- **New skill**: `build-brand-style-reference` — generates/refreshes `_context/Brand_Style_Reference.md` from real image creative samples (named styles, energy/look descriptions, Flux + Ideogram prompt starters), following the same depth as the original hand-made Cogneesol example.
- **Extended**: `build-brand-style` now has a deck-extraction workflow — when a `.pptx` style source is provided, it parses the slide XML directly for exact hex codes, font usage, and layout patterns rather than visually skimming rendered slides.
- **New skill**: `sample-archive-index` — a lightweight triage manifest for bulk `_samples\` drops (20+ files), classifying and routing each file to the right deep-extraction skill instead of blind-scanning everything.
- **Cleanup**: the original Cogneesol files (which inspired this whole investigation — they were hand-made proof this depth of extraction is achievable) were relocated to `_samples\_reference-examples\` with a README marking them as a worked-example quality bar, not live brand data.
- `Brand_Style_Reference.md` is now the 6th core `_context\` file (`brand-onboarder` builds 6 files, not 5) — built only when real creative samples exist, never invented from nothing.

### v3.3 — 2026-06-30

#### Expansion — ABM, Lead Generation, and Webinar Programs

Reviewed `github.com/vsevolodl/b2b-agents` (40 generic B2B commercial agent prompts) for adaptation. Nothing was copy-pasted — that repo's agents don't follow this workspace's conventions (no `_context\` grounding, no Skill tool invocation, no agent memory, no output routing). Scope was narrowed to capabilities the user actually owns personally (ABM, lead-gen funnel design, webinar programs); LinkedIn outreach and the other 37 repo agents (sales execution, revenue ops, customer lifecycle, partnerships) were excluded as out of scope for a marketing-only toolkit.

- **ABM** folded into `campaign-strategist` as a new skill (`abm-account-plan`) rather than a new agent — `campaign-strategist` already listed ABM as a campaign type but had no framework to execute it. A new agent would have mostly duplicated the existing strategy-layer agent.
- **New agent**: `lead-generation-engine` — owns lead funnel architecture (channel mix, MQL/SQL scoring model, nurture flow map) via the new `lead-gen-strategy` skill. Hands off gated-asset, landing-page, and email execution to `content-creator`'s existing skills rather than duplicating them.
- **New agent**: `webinar-strategist` — owns webinar program planning (concept, agenda, speaker brief, promotion timeline, registration brief, follow-up outline) via the new `webinar-plan` skill, mirroring why `podcast-strategist` exists as its own agent for the analogous content format. Hands off promotion/registration/follow-up copy execution to `content-creator`.
- **New folder**: `output\webinars\` for webinar plans (mirrors the `output\podcasts\` folder pattern). ABM and lead-gen strategy docs route to the existing `output\reports\` folder.
- **Ledger expansion**: `_context/Brand_Insights_Ledger.md` gets two new sections — Section 10 (Lead Generation Intelligence) and Section 11 (Webinar Intelligence). ABM insights fold into the existing Section 1 (Buyer Personas & Objections), already owned by `campaign-strategist`.

### v3.2 — 2026-06-30

#### Expansion — SEO, PR, Social, and Podcast Integration

Added 5 new specialized agents and 11 new skills to expand the marketing team's capabilities, entirely authored in the project's native format.
- **New Agents**: `seo-specialist`, `ai-citation-strategist`, `pr-comms`, `social-strategist`, `podcast-strategist`.
- **New Skills**: 11 skills added spanning SEO optimization, AI visibility, PR pitching, cross-platform social strategy, podcast episode planning, show notes, and email copy.
- **Agent Upgrades**: `campaign-strategist` updated to orchestrate the new downstream specialists. `content-creator` updated to utilize email and podcast-repurposing skills.

### v3.1 — 2026-06-29

#### Bug fixes (path portability)

The workspace was copy-pasted from v2. All hardcoded `D:\AI Marketing Team v2\` absolute paths were broken. Fixed across the board:

| File | Change |
|------|--------|
| All 6 agent files | Memory path changed from hardcoded `D:\AI Marketing Team v2\.claude\agent-memory\<name>\` to runtime-resolved pattern: `(Resolve-Path '.claude\agent-memory\<name>').Path` |
| `.mcp.json` | `IMAGE_OUTPUT_DIR` changed from `D:\\AI Marketing Team v2\\ideogram_output` to relative `output/ideogram_output` |
| `.claude\settings.json` | Removed 14 stale v2 session-specific allowed commands; replaced with empty `allow: []` |
| `CLAUDE.md` | Workspace layout diagram path updated `v2` → `Master`; new `## Workspace Conventions` section added (see below) |
| `PROJECT_OVERVIEW.md` | All "AI Marketing Team v2" references updated to Master |
| `_sop\sop-onboarding.md` | Step 3.2 updated from path-check instruction to runtime-resolution instruction |

**Convention documented in `CLAUDE.md`:** Agents must never hardcode absolute paths. Use `(Resolve-Path '.claude\agent-memory\<name>').Path` at runtime. MCP configs and skill output paths use workspace-relative paths. When versioning or cloning, only text references need updating — everything else is portable automatically.

#### Enhancement A — Brand Insights Ledger integration

`_context\Brand_Insights_Ledger.md` existed but was dead weight — no agent referenced it. All 6 agents were updated to actively read and write it:

| Agent | Reads | Writes |
|-------|-------|--------|
| `brand-onboarder` | — | Resets file on new onboarding; seeds Section 1 with initial ICP/persona intelligence |
| `campaign-strategist` | Section 1 (Buyer Personas & Objections) | Section 1 — ICP nuances, validated positioning angles |
| `market-researcher` | Section 1 | Section 1 — confirmed buyer pain points, competitor moves, underserved segments |
| `content-creator` | Sections 1 + 3 | Section 3 (Copywriting & Voice Preferences) — confirmed/corrected voice decisions |
| `creative-designer` | Sections 1 + 2 | Section 2 (Creative & Formatting Insights) — confirmed/rejected visual directions |
| `data-analyst` | Section 4 | Section 4 (Performance & Anomaly Analytics) — baselines, recurring anomalies |

Each agent now has explicit read instructions (which sections, why) and write instructions (section ownership, trigger conditions, entry format, do-not-write rules). The team now accumulates intelligence across sessions rather than starting from scratch each time.

#### Enhancement B — `build-brand-*` partial update skills

Five new skills created under `skills\`. These allow individual `_context\` files to be refreshed without triggering a full brand re-onboarding. Previously, `CLAUDE.md` routing rules referenced these skills but they did not exist.

| Skill | File Updated | Trigger |
|-------|-------------|---------|
| `build-brand-context` | `Brand_Context.md` | Positioning changed, new ICP added, company description stale |
| `build-brand-voice` | `Brand_Voice_Guide.md` | Tone shift, rebrand, new style guide shared |
| `build-brand-style` | `Brand_Style.md` | New colors/fonts, visual rebrand, style guide uploaded |
| `build-brand-products` | `Brand_Product_Offerings.md` | New product launched, pricing changed, ICP refined |
| `build-brand-growth` | `Brand_Growth_Marketing_Context.md` | New quarter targets, channel mix changed, funnel benchmarks updated |

Each skill: reads the existing context file first (merge, not replace by default), accepts URL/uploaded materials/user input, follows a structured output format, and reports `[TBD]` and `[ASSUMPTION]` fields that need user validation before downstream agents can use the file.

**Architectural note — onboarder vs. skills:**
`brand-onboarder` runs once per brand engagement (first-time setup, or switching to a new client). It is not a recurring tool. The `build-brand-*` skills are the ongoing maintenance path — they handle targeted updates to individual context files mid-engagement (new product launched, rebrand, updated quarterly targets) without forcing a full re-onboarding. Without these skills, any context change would require rebuilding all 5 files from scratch.

---

*Last updated: 2026-07-06*
