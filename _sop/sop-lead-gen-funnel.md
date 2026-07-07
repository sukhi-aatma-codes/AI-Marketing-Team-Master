# Standard Operating Procedure: Lead Generation Funnel Build (SOP-LGF-04)

**Version:** 1.0
**Owner:** `lead-generation-engine`
**Collaborators:** `content-creator`, `creative-designer` (conditional), `data-analyst`

This SOP governs building a lead generation funnel from architecture through executable assets. It enforces the core rule: **architecture before assets** — no gated asset, gate page, or nurture sequence gets written until a funnel document defines where it fits, how leads are qualified, and what happens after conversion.

---

## Lead Gen Funnel Pipeline Checklist

### Phase 1: Scope & Context
*Owner: `lead-generation-engine`*
- [ ] **1.1 Standalone or campaign component?** If this funnel is part of a larger campaign being scoped, `campaign-strategist` owns the campaign and this SOP runs as a sub-task feeding funnel specifics into the Campaign Strategy Document. If standalone (e.g. fixing qualification on an existing form), proceed directly.
- [ ] **1.2 Load brand context:** `Brand_Growth_Marketing_Context.md` (channels, goals, benchmarks) and `Brand_Product_Offerings.md` (ICPs, service lines) — both mandatory. Read `Brand_Insights_Ledger.md` Sections 1 (Buyer Personas & Objections) and 10 (Lead Generation Intelligence) for validated qualification and channel history.
- [ ] **1.3 Confirm the offer and ICP:** Which offer gates the funnel, which ICP it targets, and what volume/quality expectation the user has. Ask if ambiguous.

### Phase 2: Funnel Architecture
*Owner: `lead-generation-engine`*
- [ ] **2.1 Invoke `lead-gen-strategy`:** Produces `output\reports\lead-gen-strategy-<topic>-<date>.md`. Do not draft the architecture inline.
- [ ] **2.2 Completeness check:** The document must define the channel mix, MQL/SQL qualification criteria, a scoring model, and the nurture flow map. Scoring must weight ICP-fit signals at least as heavily as behavioral signals — high-volume, low-fit funnels create the junk-leads problem this SOP exists to prevent.
- [ ] **2.3 Honest benchmarks:** Conversion assumptions come from `Brand_Growth_Marketing_Context.md` or are flagged `[TBD — recommend a baseline test]`. Channels with no existing brand presence are flagged as new-channel investments, not assumed live.

### Phase 3: Asset Execution
*Owner: `content-creator`, briefed by the funnel document*
- [ ] **3.1 Hand off with the funnel doc as the brief:** `lead-generation-engine` does not write assets. Pass `output\reports\lead-gen-strategy-<topic>-<date>.md` to `content-creator`.
- [ ] **3.2 Build in dependency order:** `lead-magnet` (gated asset: `.md` + branded PDF) → `lp-builder` (gate/landing page: `.md` + `.html` in `output\pages\`) → `email-copy` (nurture sequence: `.md` + `.docx` in `output\email\`). Each asset must reference the funnel stage and qualification triggers defined in Phase 2.
- [ ] **3.3 Output verification:** Confirm each skill's full output contract exists before reporting the phase complete.
- [ ] **3.4 Campaign manifest (conditional):** If this funnel belongs to a named campaign, append one row per asset (funnel doc included) to `output\campaigns\<campaign-slug>.md` and use the campaign slug as the `<topic>` segment of asset filenames.

### Phase 4: Amplification (conditional)
*Owner: `creative-designer`*
- [ ] **4.1 Paid promotion:** If any funnel stage gets paid traffic, hand off to `creative-designer` (`ad-creative` for copy variants, `social-creative-designer` for visuals). Ad copy must message-match the gate page H1.

### Phase 5: Measurement Scaffolding
*Owner: `data-analyst`*
- [ ] **5.1 KPI mapping:** Map each funnel stage to a measurable KPI (visits → form fills → MQL → SQL) with baselines from `Brand_Growth_Marketing_Context.md` where they exist.
- [ ] **5.2 Review cadence:** Define when qualification accuracy gets reviewed against real sales feedback (e.g. after the first 50 leads).
- [ ] **5.3 Ledger update (conditional):** Write to `Brand_Insights_Ledger.md` Section 10 only when qualification criteria or channel performance is validated by real-world results — not at build time.
