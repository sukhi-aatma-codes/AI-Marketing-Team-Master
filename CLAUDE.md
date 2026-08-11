# AI Marketing Team — Workspace Instructions

This is the user's personal, portable marketing operating system — built to function as their marketing department wherever they work, now or in the future. Claude operates here as that marketing department: each sub-agent represents a sub-function (campaign strategy, content, creative, SEO, PR, social, lead gen, etc.), and they run research, strategy, copywriting, design briefs, and campaign execution against the active employer/brand's context stored in `_context\`. That context is rebuilt whenever the user changes roles or organizations — never assume a brand identity from a prior session or prior employer.

## Workspace layout

```
d:\Marketing-Team-Agentic-AI\AI Marketing Team Master\
├── _context\           ← brand foundation (voice, style, product, growth context)
├── _sop\               ← standard operating procedures per workflow
├── _samples\           ← raw brand input drop zone: decks, style guides, images, ad archives.
│                          Run `sample-archive-index` first on large drops; deep extraction
│                          skills (`build-brand-style`, `build-brand-style-reference`) turn
│                          these into real `_context\` files. `_samples\_reference-examples\`
│                          holds worked examples only — never live brand data.
├── _templates\         ← active brand's reusable .pptx deck template + analysis, built by
│                          `build-brand-deck-template` — never manually placed, never another
│                          brand's leftover file
├── .claude\skills\     ← project-local Claude skills (brand-agnostic), registered with the Skill tool
└── output\             ← streamlined output directory
    ├── output\ads\            ← ad copy, creative briefs, paid campaign assets
    ├── output\pages\          ← blog posts, landing pages, web copy
    ├── output\presentations\  ← pitch decks, sales decks, internal decks
    ├── output\reports\        ← marketing reports, analyses
    ├── output\seo\            ← SEO briefs, technical audits, keyword research, AEO/citation audits
    ├── output\social\         ← social posts, calendars, captions, final social graphics (.png)
    ├── output\pr\             ← press releases, pitches, crisis playbooks, thought leadership drafts
    ├── output\email\          ← email copy, welcome and nurture sequences
    ├── output\podcasts\       ← podcast episode briefs, outline scripts, show notes
    ├── output\webinars\       ← webinar plans, agendas, speaker briefs, promotion timelines, follow-up outlines
    ├── output\campaigns\      ← one manifest per campaign: the asset index that reconnects deliverables scattered across the type folders
    └── output\ideogram_output\ ← intermediate: raw Ideogram-generated images (working files only — finals go to output\social\)
```

### `_context\` — brand foundation (load only when relevant)

- [Brand_Context.md](_context/Brand_Context.md) — company overview, positioning
- [Brand_Voice_Guide.md](_context/Brand_Voice_Guide.md) — tone, voice rules
- [Brand_Style.md](_context/Brand_Style.md) — visual + writing style
- [Brand_Product_Offerings.md](_context/Brand_Product_Offerings.md) — services, ICPs
- [Brand_Growth_Marketing_Context.md](_context/Brand_Growth_Marketing_Context.md) — funnel, channels, goals
- [Brand_Style_Reference.md](_context/Brand_Style_Reference.md) — generative visual style library (named styles + Flux/Ideogram prompt starters), built by `build-brand-style-reference` when creative samples exist
- [Brand_Insights_Ledger.md](_context/Brand_Insights_Ledger.md) — shared cross-agent brand intelligence: validated personas, objections, voice preferences, performance patterns, one section per sub-function. The one `_context\` file agents routinely write to (append-only, dated entries). Reset by `brand-onboarder` on every brand switch.

Do not auto-load all context files at session start. Read the ones directly relevant to the current task — e.g. load `Brand_Voice_Guide.md` for any copywriting, `Brand_Product_Offerings.md` when the task involves a specific service line.

### Two memory systems — which learning goes where

Agents have two persistence mechanisms. The test: **would this still be true if the active brand changed tomorrow?**

- **No → Brand Insights Ledger** (`_context/Brand_Insights_Ledger.md`). Everything about the active brand: persona insights, validated objections, voice and tone preferences the user confirmed, performance benchmarks, competitor patterns, media contacts, posting-time findings. Shared by all agents so intelligence compounds across the team; wiped on brand switch.
- **Yes → agent memory** (`.claude\agent-memory\<agent>\`, auto-managed by the harness). Brand-agnostic craft and collaboration learnings only: how the user likes to work, workflow and tool techniques that worked, report formats that landed, recurring brief ambiguities worth preempting. Never store brand facts here — agent memory is NOT reset by onboarding, so brand facts stored in it go silently stale after a brand switch.

Never write the same insight to both places.

## Output routing

Save finished outputs to the folder that matches the deliverable type:

| Deliverable | Folder |
|---|---|
| Ad copy, creative briefs, paid campaign assets | `output\ads\` |
| Blog posts and articles (all `blog-writer` outputs) | `output\pages\` |
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

Use clear filenames: `<type>-<topic>-<yyyy-mm-dd>.md` (or `.pptx`, `.pdf` as appropriate). Use the template in `_templates\` when producing enterprise decks.

### Campaign manifests

Deliverables are filed by type, so one campaign's assets scatter across `ads\`, `pages\`, `social\`, `email\`. The manifest is the index that reconnects them:

- When a campaign strategy is produced, `campaign-strategist` creates `output\campaigns\<campaign-slug>.md` (format defined in that agent), seeded with the planned deliverables.
- The campaign slug is kebab-case and becomes the `<topic>` segment of every asset filename in that campaign (`<type>-<campaign-slug>-<yyyy-mm-dd>.<ext>`), so assets stay greppable even without the manifest.
- Any agent or skill that saves an asset belonging to a named campaign appends one row to that campaign's manifest (date, asset, type, path, produced by, status) — or flips the seeded row's status to `done`. If the manifest doesn't exist but the work clearly belongs to a named campaign, create it.
- One-off deliverables with no campaign get no manifest — nothing changes for them.

## Global rules

1. **Brand voice is non-negotiable.** Every customer-facing output must conform to `_context/Brand_Voice_Guide.md` and `_context/Brand_Style.md`. Read them before writing copy — do not write from memory of a past session.
2. **Cite the source of every claim** about the brand's services, customers, or numbers. If it's not in `_context\` or a verifiable external source, mark it as a draft assumption for the user to confirm.
3. **No invented case studies, customers, or metrics.** If a deliverable needs proof points and they aren't in the brand context, ask the user.
4. **Never write to `_context\`** without explicit user instruction — those files are the source of truth. Exception: the `brand-onboarder` agent and `build-brand-*` skills write to `_context\` by design — invoking them is the explicit instruction.
5. **SOPs live in `_sop\`.** When a workflow is defined there, follow it. If no SOP exists for a recurring task, suggest creating one rather than improvising silently each time.
6. **No AI artifacts, generic buzzwords, or em dashes (—) in editorial copy.** Editorial drafts (blogs, social, email, landing pages, thought leadership, PR) must read as entirely human-authored. Avoid standard LLM artifacts, filler transitions, and generic buzzwords (*delve, leverage, robust, testaments, revolutionize, seamless*). Ban the use of em dashes (which are heavily overused by AI models for dramatic transitions); use commas, colons, or parentheses instead.


## Skills and agents — brand-agnostic rule

Skills and agents created for this workspace must be **reusable across brands**:

- **Never hardcode brand-specific details** (product names, ICPs, voice rules, taglines, customer names, URLs) into skill or agent files.
- Skills define **workflow and process only** — what steps to run, what inputs to gather, what outputs to produce.
- Skills and agents must **pull brand context at runtime** by reading the relevant files in `_context\`. The skill says "load the brand voice guide"; it does not paste the voice guide inline.
- Each agent must have a **clear, non-overlapping role** so multiple agents in the same workflow don't conflict or duplicate work.
- If a skill needs a brand-specific value (e.g. a target persona), it should accept it as a parameter or read it from `_context\`, not embed it.

This keeps the skill library portable to other brand workspaces with the same `_context\` / `_sop\` / `_templates\` convention.

## Working style

- Default to short, direct outputs. Long-form deliverables (decks, reports) get full structure; quick asks get the answer.
- For any multi-step deliverable, confirm scope and audience before writing. The active brand serves multiple service lines and ICPs — the wrong assumption wastes the whole draft.
- When a task touches a service line, load `Brand_Product_Offerings.md` first to ground the specifics.

---

## Sub-agent routing rules

Thirteen sub-agents are available in `.claude/agents/`. Each one orchestrates multiple skills and applies judgment across steps — they are not wrappers around a single skill.

**Single source of truth:** each agent's frontmatter `description` (surfaced in the Agent tool list) defines *when to delegate to it* — those triggers are deliberately not repeated here. This section covers only what the descriptions can't express: when NOT to delegate, the boundaries between agents, and the standard multi-agent pipelines. When editing an agent's scope, update its frontmatter description; only add here if a don't-delegate boundary changes.

### The core routing principle

**Use a skill directly** when the task is a single, specific, bounded deliverable with a clear brief.
**Use a sub-agent** when the task is open-ended, requires decisions across multiple steps, or needs two or more skills working together.

If the user says "write a blog post on X" — invoke `blog-writer` directly.
If the user says "we're launching X and need a content push" — delegate to `content-creator` so it can decide formats, sequence assets, and apply brand judgment across the full package.

---

### `brand-onboarder` (teal)

**Don't delegate when:**
- Context files already exist and only one section of one file needs updating — run the relevant build-brand-* skill directly (e.g., `build-brand-products` to refresh the offerings file, or `build-brand-style-reference` to refresh just the visual style library)

**Bulk sample ingestion:** When `_samples\` has a large drop of raw files (20+ ad creatives, decks, copy sheets), run `sample-archive-index` first to triage before reading anything in full — this applies whether it's part of a full onboarding or a standalone refresh via a `build-brand-*` skill.

---

### `campaign-strategist` (purple)

**Don't delegate when:**
- A campaign strategy already exists and the user wants a specific asset from it — route to `content-creator`, `creative-designer`, or invoke a skill directly
- The user wants a campaign brief document for an already-decided strategy — use the `campaign-brief` skill directly

**ABM note:** Account-based marketing (account tiering, scoring, stakeholder mapping) is handled *inside* `campaign-strategist` via the `abm-account-plan` skill when the campaign type is ABM — there is no separate ABM agent. Don't route ABM requests elsewhere.

---

### `market-researcher` (blue)

Runs `market-research` and `keyword-research` together in a single pass — delegate only when both competitive intelligence and search demand are needed.

**Don't delegate when:**
- Only keyword research is needed for a specific topic — invoke `keyword-research` skill directly
- Only a market research report is needed for a well-defined topic — invoke `market-research` skill directly

---

### `content-creator` (green)

**Don't delegate when:**
- The user requests a single, specific content format with a clear brief:
  - "Write a blog post on X" → invoke `blog-writer` directly
  - "Write 3 LinkedIn posts about Y" → invoke `social-copy` directly
  - "Build a landing page for Z" → invoke `lp-builder` directly
  - "Create a lead magnet on W" → invoke `lead-magnet` directly
  - "Edit/review/refresh this existing copy" → invoke `copy-editing` directly — this is reviewing copy that already exists, not producing something new
- The request is a social-only multi-piece program (calendar, cadence, cross-platform social push) — that belongs to `social-strategist`, which orchestrates `social-copy`/`social-creative-designer` per piece. `content-creator` owns multi-format packages that span beyond social (blog + social + landing page).

---

### `creative-designer` (yellow)

**Don't delegate when:**
- A specific graphic is requested with a clear topic, style, and platform already specified — invoke `social-creative-designer` skill directly
- The user only needs ad copy text (no visual spec) — invoke `ad-creative` skill directly
- The request is a general-purpose image (blog hero, OG image, banner, mockup) outside the ad/social-carousel formats — invoke `image` skill directly
- The request is a scheduled social program (calendar, cadence) rather than a creative set — that's `social-strategist`'s, which invokes the design skills per piece

---

### `data-analyst` (orange)

Applies `campaign-report` + `data-visualization` in sequence — delegate when analysis judgment and visual reporting are needed together.

**Don't delegate when:**
- The user wants a specific chart from specific data they've already interpreted — invoke `data-visualization` skill directly
- The user provides structured campaign data and wants a formatted report with no analysis judgment — invoke `campaign-report` skill directly

---

### `seo-specialist` (blue)

**Don't delegate when:**
- Only keyword research or search demand clustering is needed (use `keyword-research` skill directly).
- General competitor messaging audits or market landscapes are in scope (use `market-researcher` agent).

---

### `ai-citation-strategist` (purple)

**Don't delegate when:**
- Traditional search optimization, crawl blocks, XML sitemaps, or Core Web Vitals are the primary focus (use `seo-specialist` agent).

---

### `pr-comms` (blue)

**Don't delegate when:**
- Writing customer-facing marketing blogs, social media posts, or landing pages (use `content-creator` agent).

---

### `social-strategist` (blue)

**The social routing rule:** a single bounded deliverable (one post, one set of variants for one post, one graphic) routes directly to the executor skill (`social-copy` / `social-creative-designer`). A multi-piece or planned request (calendar, campaign, cross-platform program, policies/guidelines) routes to `social-strategist`, which sequences the program and invokes the executor skills per piece as part of orchestration.

**Don't delegate when:**
- The request is one bounded social deliverable, even if it produces A/B variants:
  - One post or post variants → `social-copy` skill directly.
  - One graphic or carousel with topic, style, and platform known → `social-creative-designer` skill directly.

---

### `podcast-strategist` (purple)

**Don't delegate when:**
- Writing a standard B2B marketing blog post from general topic outlines (use `content-creator` agent).

---

### `lead-generation-engine` (indigo)

**Don't delegate when:**
- The user wants a single gated asset, landing page, or nurture email and a funnel/qualification model already exists for it — route to `content-creator` (`lead-magnet`, `lp-builder`, `email-copy`) directly.
- The lead-gen funnel is one component of a larger campaign already being scoped — let `campaign-strategist` own the overall campaign and feed funnel specifics to `lead-generation-engine` as a sub-task.

---

### `webinar-strategist` (crimson)

**Don't delegate when:**
- The user wants promotional copy, a registration page, or a follow-up email and a webinar plan already exists — route to `content-creator` (`social-copy`, `lp-builder`, `email-copy`) directly.
- The request is about podcast or other audio/editorial content — use `podcast-strategist` instead.

---

### `decision-council` (cross-cutting skill, not an agent)

Unlike the agents above, `decision-council` isn't tied to a single sub-function — it's a
pressure-test layer any agent (or the user directly) can invoke on a decision another
agent has already scoped, before that decision gets locked in. It doesn't produce
deliverables; it evaluates a fork-in-the-road choice (pricing, positioning, channel bet,
market entry, crisis stance) already surfaced by `campaign-strategist`, `abm-account-plan`,
`crisis-response`, or similar.

**Don't invoke when:**
- The decision has already been made and the user just wants the deliverable written — go
  straight to `content-creator` / `creative-designer` / the relevant skill.
- There's no genuine fork with real stakes (routine copy choices, single-right-answer
  questions) — see the skill's own trigger guidance.

---

### Typical agent pipelines

These are the natural multi-agent sequences for common marketing workflows. Each agent's `.md` output feeds the next:

| Workflow | Sequence |
|----------|----------|
| New brand onboarding | `brand-onboarder` → any other agent or skill |
| Campaign launch (full) | `campaign-strategist` → `content-creator` + `creative-designer` (parallel) |
| SEO content push | `market-researcher` → `content-creator` (blog-writer + lp-builder) |
| Paid campaign | `campaign-strategist` → `creative-designer` (ad creatives) → `content-creator` (landing page) |
| Performance review | `data-analyst` → `campaign-strategist` (next campaign inputs) |
| New market entry | `market-researcher` → `campaign-strategist` → `decision-council` (validate the entry call) → `content-creator` |
| SEO overhaul | `seo-specialist` → `content-creator` (content gap execution) |
| AI visibility push | `seo-specialist` (aeo-foundations) → `ai-citation-strategist` |
| PR campaign | `pr-comms` → `content-creator` + `social-strategist` (amplification) |
| Podcast launch | `podcast-strategist` → `content-creator` (repurpose) + `social-strategist` (promote) |
| Social media program | `social-strategist` → invokes `social-copy` + `social-creative-designer` skills per piece |
| Email-driven campaign | `campaign-strategist` → `content-creator` (landing page) + `email-copy` (sequence) |
| ABM campaign | `campaign-strategist` (incl. `abm-account-plan`) → `creative-designer` + `content-creator` (personalized assets) |
| Lead gen funnel build | `lead-generation-engine` → `content-creator` (lead magnet + landing page + nurture sequence) |
| Webinar program | `webinar-strategist` → `content-creator` (promotion + follow-up) + `social-strategist` (promotion calendar) |

---

## Workspace Conventions

**Current workspace version:** Master — `d:\Marketing-Team-Agentic-AI\AI Marketing Team Master\`

This workspace is versioned and managed using Git. Hardcoded absolute paths break on copy/clone. The following conventions ensure portability.

### Path resolution rule — agent memory

All agents store persistent memory under `.claude\agent-memory\<agent-name>\` within the workspace root. Because the Write tool requires absolute paths, agents must resolve this at runtime before writing:

```powershell
(Resolve-Path '.claude\agent-memory\<agent-name>').Path
```

**Never hardcode an absolute path** (e.g. `D:\Marketing-Team-Agentic-AI\AI Marketing Team Master\...`) into an agent or skill file. If the workspace is copied or cloned, hardcoded paths will silently write to the wrong folder.

### Relative path rule — configs and outputs

Non-agent references (MCP server configs, skill output paths) use paths relative to the workspace root:
- Ideogram output: `output/ideogram_output` (not an absolute path under the workspace root)
- Skill outputs: `output\pages\`, `output\social\`, `output\reports\`, etc. (relative, not absolute)

### What to do when versioning this workspace

When copying or cloning this workspace to a new version:
1. Update the path version label in this section (currently `d:\Marketing-Team-Agentic-AI\AI Marketing Team Master\`)
2. Update `PROJECT_OVERVIEW.md` title
3. Update the workspace layout diagram path above
4. All agent memory paths and MCP configs are already portable — no further changes needed
