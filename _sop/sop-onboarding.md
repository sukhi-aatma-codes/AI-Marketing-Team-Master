# Standard Operating Procedure: Brand Onboarding (SOP-ONB-01)

**Version:** 1.0  
**Owner:** `brand-onboarder`  
**Downstream Dependents:** All sub-agents  

This SOP governs the end-to-end execution of onboarding a new brand or client into this workspace. No brand-specific marketing execution (campaign strategy, content creation, design) may begin until this SOP is marked as **COMPLETED** and the first 5 context files reside in `_context\`. The 6th file, `Brand_Style_Reference.md`, is built whenever real creative samples exist (it cannot be invented from nothing) and is not a blocker for execution to begin.

---

## Onboarding Execution Checklist

### Phase 1: Ingestion & Analysis
- [ ] **1.1 Parse Raw Inputs:** Retrieve domain URL, style guides, decks, copy sheets, or briefs provided by the user. If the user has dropped a large batch of files (20+) into `_samples\`, run `sample-archive-index` first to triage before reading anything in full.
- [ ] **1.1b Deep Extraction (when applicable):** Route indexed files to the matching deep-extraction skill — decks with visual design content to `build-brand-style`'s deck-extraction workflow (exact hex codes and fonts from slide XML); image creative samples to `build-brand-style-reference` (style library + Flux/Ideogram prompt starters).
- [ ] **1.2 Analyze Branding Identity:**
  * Extract core taglines, positioning phrases, and mission statements.
  * Map the visual design (primary/secondary hex codes, font typography).
- [ ] **1.3 Analyze Product Suite:**
  * Document all product/service offerings.
  * Extract technical features and translate them into buyer-facing benefits.
  * Identify specific Ideal Customer Profiles (ICPs) and buying triggers.
- [ ] **1.4 Audit Current Growth Channels:**
  * Note organic channels (LinkedIn, Twitter, blog presence).
  * Check paid channels, active CTAs, and apparent funnel stages.

### Phase 2: Generating Core Context Files
Generate the source-of-truth files in `_context\` using structured templates:

- [ ] **2.1 `Brand_Context.md`:**
  * Include company category, positioning statements, core values, vertical targets, and competitive differentiators.
- [ ] **2.2 `Brand_Voice_Guide.md`:**
  * Define tone dimensions, writing style spectrum (e.g. conversational vs academic), list of banned jargon words, and writing rules.
- [ ] **2.3 `Brand_Style.md`:**
  * Define digital design hex codes, the brand's actual font pairing (as parsed from its site or style guide), grid spacing, safety boundaries, and approved image style patterns.
- [ ] **2.4 `Brand_Product_Offerings.md`:**
  * Categorize service lines, technical descriptions, price tiers, buyer persona targets, and specific pain points solved.
- [ ] **2.5 `Brand_Growth_Marketing_Context.md`:**
  * Define active goals, key channels, target metric baselines, and conversion metrics.
- [ ] **2.6 `Brand_Style_Reference.md` (conditional):** Only if real creative samples were provided — invoke `build-brand-style-reference` to produce the generative visual style library. If no samples exist, skip and flag as an open gap in Phase 4 rather than inventing styles.

### Phase 3: Integrity & Consistency Check
Perform cross-file compliance checks:
- [ ] **3.1 Voice Consistency:** Ensure tone guidelines defined in `Brand_Voice_Guide.md` are used to write the value propositions in `Brand_Product_Offerings.md`.
- [ ] **3.2 Path Verification:** Confirm all agent memory path instructions use runtime resolution (`.claude\agent-memory\<name>\` resolved via `(Resolve-Path '.claude\agent-memory\<name>').Path`) — no hardcoded absolute paths.
- [ ] **3.3 Flag Verification:** Verify all assumptions or unknown metrics are explicitly marked as `[ASSUMPTION — please confirm]`.

### Phase 4: Client Handover & Review
- [ ] **4.1 Synthesize Onboarding Summary:** Present the user with a brief covering visual identity, core value prop, and key differentiators.
- [ ] **4.2 Highlight Gaps:** Present a bulleted list of open questions, unconfirmed metrics, or missing visual elements for user feedback.
