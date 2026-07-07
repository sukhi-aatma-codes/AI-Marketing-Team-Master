# Standard Operating Procedure: Webinar Program Pipeline (SOP-WBN-05)

**Version:** 1.0
**Owner:** `webinar-strategist`
**Collaborators:** `content-creator`, `social-strategist`, `creative-designer` (conditional)

This SOP governs running a webinar program end-to-end: plan, registration assets, promotion, live-event readiness, and post-event follow-up. It enforces the core rule: **plan before promote** — no promotional post or registration page gets written until the webinar plan defines the concept, timeline, and follow-up tracks they serve.

---

## Webinar Program Pipeline Checklist

### Phase 1: Webinar Plan
*Owner: `webinar-strategist`*
- [ ] **1.1 Load brand context:** `Brand_Voice_Guide.md`, `Brand_Product_Offerings.md`, and `Brand_Context.md` (all mandatory). Read `Brand_Insights_Ledger.md` Sections 1 (Buyer Personas) and 11 (Webinar Intelligence) for topic resonance and past registration/attendance patterns.
- [ ] **1.2 Invoke `webinar-plan`:** Produces `output\webinars\webinar-plan-<topic>-<date>.md`. Do not draft the plan inline.
- [ ] **1.3 Completeness check:** The plan must include concept, agenda, speaker brief, promotion timeline, registration brief, and BOTH follow-up tracks (attendee and no-show — no-shows are often the larger group).
- [ ] **1.4 Reality checks:** Topic ties to a real ICP pain point and the brand's actual credibility area; speaker credentials are sourced from `_context\` or user-confirmed (never invented); promotion touchpoint density fits the actual lead time to event day.

### Phase 2: Registration Assets
*Owner: `content-creator`, briefed by the webinar plan*
- [ ] **2.1 Registration page:** Invoke `lp-builder` against the plan's registration brief → `.md` + `.html` in `output\pages\`. The H1 leads with the attendee outcome, not the event title.
- [ ] **2.2 Visuals (conditional):** Registration page graphics and promo creative → `creative-designer` (`social-creative-designer` / `image` skills), styled per `Brand_Style.md`.

### Phase 3: Promotion
*Owners: `social-strategist` (program), `content-creator` (email)*
- [ ] **3.1 Social promotion program:** The promotion timeline is a multi-piece planned program — per the social routing rule it goes to `social-strategist`, which sequences the touchpoints from the plan and invokes `social-copy` (and `social-creative-designer`) per piece. Outputs land in `output\social\`.
- [ ] **3.2 Email invite sequence:** Invoke `email-copy` for the invite + reminder sequence mapped to the plan's timeline → `output\email\`.
- [ ] **3.3 Message match:** Every promotional piece points to the registration page and mirrors its core promise — one value proposition across social, email, and page.

### Phase 4: Event Readiness
*Owner: `webinar-strategist`*
- [ ] **4.1 Speaker brief delivered:** Speaker(s) have the brief and run-of-show from the plan with enough lead time to prepare.
- [ ] **4.2 Final checks:** Registration page live and correct, reminder emails scheduled per the timeline, and the follow-up sequences (Phase 5) drafted BEFORE the event — follow-up speed matters most in the first 24 hours after.

### Phase 5: Follow-up & Wrap
*Owners: `content-creator` (email), `webinar-strategist` (wrap)*
- [ ] **5.1 Execute both tracks:** Invoke `email-copy` for the attendee track (recording + next-step CTA) and the no-show track (recording + re-engagement) as defined in the plan → `output\email\`.
- [ ] **5.2 Repurposing handoff (conditional):** If the recording feeds other content (blog recap, social clips), hand off to `content-creator` / `social-strategist` with the plan and recording as inputs.
- [ ] **5.3 Ledger update (conditional):** Write to `Brand_Insights_Ledger.md` Section 11 only with validated results — registration/attendance patterns, follow-up conversion differences, speaker formats that resonated. Not at planning time.
