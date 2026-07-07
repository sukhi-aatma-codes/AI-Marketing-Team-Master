# Standard Operating Procedure: Campaign Launch Pipeline (SOP-CMP-02)

**Version:** 1.0  
**Owner:** `campaign-strategist`  
**Collaborators:** `market-researcher`, `content-creator`, `creative-designer`, `data-analyst`

This SOP governs the end-to-end execution of designing, drafting, and preparing B2B tech campaigns. It ensures consistent messaging, correct visual layout specifications, and clear metric targets across all channels.

---

## Campaign Execution Pipeline Checklist

### Phase 1: Landscape Research & Demand Audit
*Owner: `market-researcher`*
- [ ] **1.1 Competitive Audit:** Analyze competitor positioning and active channels. Identify positioning gaps or white space.
- [ ] **1.2 Search Demand Audit:** Run keyword research to discover high-value search terms and user-intent patterns.
- [ ] **1.3 Handover:** Output research data to `output\seo\` and notify the `campaign-strategist`.

### Phase 2: Strategic Scaffolding & Messaging
*Owner: `campaign-strategist`*
- [ ] **2.1 Load Brand Context:** Read the onboarded files in `_context\`.
- [ ] **2.2 Formulate Positioning:** Define the campaign's hero positioning statement and messaging pillars.
- [ ] **2.3 Structure Channels:** List required deliverables across organic, paid, and search channels.
- [ ] **2.4 Handover:** Save the master Campaign Strategy Document in `output\reports\` and brief the execution team.
- [ ] **2.5 Campaign Manifest:** Create `output\campaigns\<campaign-slug>.md` seeded with the planned deliverables (per the campaign-strategist manifest format). All downstream asset filenames use the campaign slug as their `<topic>` segment.

### Phase 3: Copywriting & Design Production
*Owners: `content-creator` (Copy), `creative-designer` (Visuals)*
- [ ] **3.1 Production Sequence:** Always draft the landing page copy first to anchor the campaign, followed by supporting blog posts and social graphics.
- [ ] **3.2 Copy Compliance:** Ensure all copy strictly follows rules in `Brand_Voice_Guide.md`.
- [ ] **3.3 Design Specs:** Create platform-compliant specs (dimensions, color hex codes from `Brand_Style.md`, typography, logo rules).
- [ ] **3.4 Review & Save:** Save creative briefs and ad copy to `output\ads\` or `output\social\` as appropriate.
- [ ] **3.5 Manifest Update:** For each saved asset, append its row to `output\campaigns\<campaign-slug>.md` (or flip its seeded row to `done`).

### Phase 4: Analytics Scaffolding
*Owner: `data-analyst`*
- [ ] **4.1 Metric Alignment:** Map the campaign objectives to measurable KPIs (Awareness → Conversion).
- [ ] **4.2 Set Baselines:** Define targets based on previous growth channel context in `Brand_Growth_Marketing_Context.md`.
- [ ] **4.3 Report Structure:** Save an initial analytics framework report to `output\reports\`.
