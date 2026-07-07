# Standard Operating Procedure: Content Production Pipeline (SOP-CNT-03)

**Version:** 1.0
**Owner:** `content-creator`
**Collaborators:** `market-researcher` (conditional), `seo-specialist` (conditional), `copy-editing` skill

This SOP governs the production of multi-format content packages (e.g. blog + social + landing page) and SEO-driven content pushes. It ensures every package is grounded in the brand context, produced in the correct dependency order, and edited before handover. It does NOT apply to single bounded deliverables — per the CLAUDE.md routing rules, "write a blog post on X" with a clear brief goes straight to the `blog-writer` skill with no SOP overhead.

---

## Content Production Pipeline Checklist

### Phase 1: Brief & Scope Confirmation
*Owner: `content-creator`*
- [ ] **1.1 Routing check:** Confirm this is a multi-format package or an open brief. A single, specific format with a clear brief routes directly to its skill (`blog-writer`, `social-copy`, `lp-builder`, `lead-magnet`, `email-copy`, `copy-editing`) — this SOP ends here.
- [ ] **1.2 Confirm the master brief:** One shared target ICP, funnel stage (ToFu/MoFu/BoFu), campaign theme, and one primary CTA across all formats. If any of these are ambiguous, ask before writing — a wrong assumption wastes the whole package.
- [ ] **1.3 Load brand context:** `Brand_Voice_Guide.md` and `Brand_Style.md` (mandatory), `Brand_Product_Offerings.md` when a service line is involved, `Brand_Insights_Ledger.md` Sections 1 (Buyer Personas) and 3 (Copywriting & Voice Preferences).
- [ ] **1.4 List the deliverables:** Name every asset, its format, its channel, and the skill that will produce it.

### Phase 2: Research (conditional — SEO-driven packages)
*Owner: `content-creator`, with `market-researcher` / `seo-specialist` when needed*
- [ ] **2.1 Reuse before researching:** Check `output\seo\` for an existing keyword or market research brief covering this topic. If one exists, read it — do not re-run research.
- [ ] **2.2 Keyword research:** If the package is SEO-driven and no brief exists, invoke `keyword-research` (output lands in `output\seo\`). If both competitive intelligence AND search demand are missing, delegate that pass to `market-researcher` instead.
- [ ] **2.3 Cannibalization check (conditional):** If the brand already ranks for adjacent topics, have `seo-specialist` confirm the new content targets a distinct keyword/intent before drafting.

### Phase 3: Production
*Owner: `content-creator`*
- [ ] **3.1 Production sequence:** Destination before traffic driver — landing page (`lp-builder`) first, then blog (`blog-writer`), then social (`social-copy`) and email (`email-copy`). Gated assets (`lead-magnet`) are produced before the emails that promote them.
- [ ] **3.2 Invoke skills, never write inline:** Every format goes through its skill via the Skill tool per the agent's Skill Invocation Protocol.
- [ ] **3.3 Message consistency:** Same core value proposition across formats, adapted per platform — not copy-pasted between formats.
- [ ] **3.4 Grounding rules:** No invented stats, case studies, or customer names. Claims without a `_context\` or verifiable external source get `[DRAFT ASSUMPTION — confirm before publishing]` or `[SOURCE NEEDED]` flags.

### Phase 4: Edit Pass
*Owner: `content-creator`, via the `copy-editing` skill*
- [ ] **4.1 Edit every long-form draft:** Run `copy-editing` on the blog, landing page, and lead magnet drafts before delivery (quick pass minimum; full seven-sweep for cornerstone pieces).
- [ ] **4.2 Editorial compliance:** No banned words from `Brand_Voice_Guide.md`, no em dashes, no AI artifacts or generic buzzwords — drafts must read as entirely human-authored.
- [ ] **4.3 Flag audit:** Every `[DRAFT ASSUMPTION]` and `[SOURCE NEEDED]` flag is still visible and listed for the user — none silently resolved.

### Phase 5: Handover & Routing
*Owner: `content-creator`*
- [ ] **5.1 Output verification:** Confirm every skill produced its full output contract (e.g. `blog-writer` → `.md` + `.html` + `.docx` in `output\pages\`; `social-copy` → `.md` + `.docx` in `output\social\`; `email-copy` → `.md` + `.docx` in `output\email\`). Missing files mean the skill did not complete — do not report done.
- [ ] **5.2 Summary table:** Deliver a table listing each asset, format, channel, file path, and CTA.
- [ ] **5.3 Campaign manifest (conditional):** If the package belongs to a named campaign, append one row per asset to `output\campaigns\<campaign-slug>.md` (or flip seeded rows to `done`), and use the campaign slug as the `<topic>` segment of every filename.
- [ ] **5.4 Ledger update (conditional):** Write to `Brand_Insights_Ledger.md` Section 3 only if the user confirmed or corrected something new this run — never routine completions.
