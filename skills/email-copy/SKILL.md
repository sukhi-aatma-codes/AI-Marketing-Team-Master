---
name: email-copy
description: >
  Use this skill whenever the user wants to draft email welcome sequences, lead-magnet nurture sequences,
  newsletter drip sequences, promotional broadcasts, or cold outreach emails. Trigger on requests like
  "write a welcome sequence for our new trial users", "draft a nurture sequence for our lead magnet",
  "write our monthly newsletter", "create a promotional email sequence for our product launch", or "draft
  a cold outreach email targeting operations managers". Handles subject line variation, preview text
  calibration, merge tag injection, and conversion-focused copy.
---

# Email Copywriter

Drafts highly engaging, conversion-focused B2B email sequences, nurture campaigns, and newsletters in the brand's voice. Produces a structured `.md` draft and a formatted Word document (`.docx`) in `output/email/` for review and upload.

## Before starting

Read these context files every time — do not rely on prior session memory:
- `_context/Brand_Voice_Guide.md` — specific voice pillars, tone, banned words, power verbs (B2B email copy should remain professional but leaning conversational and personal, avoiding overly dense corporate jargon).
- `_context/Brand_Product_Offerings.md` — service lines, ICPs, differentiators, and value propositions.
- `_context/Brand_Growth_Marketing_Context.md` — active marketing channels, funnel benchmarks, and lead acquisition contexts.
- `_context/Brand_Insights_Ledger.md` — Section 3 (Copywriting & Voice Preferences) and Section 1 (Buyer Personas & Objections) for messaging angles and feedback.

## Clarify inputs first

Confirm with the user (unless already specified in the prompt):
1. **Campaign Type:** Welcome sequence, nurture campaign, promotional broadcast, newsletter, or cold outreach.
2. **Target Audience (ICP):** Who is receiving this email? (e.g. CTOs, Ops Managers, Trial Users).
3. **Offer / Lead Magnet:** What asset, product trial, or event is being delivered or promoted?
4. **Sequence Length:** Default is 3–5 emails for sequences. For newsletters/broadcasts, it is 1 email.
5. **Primary CTA:** What is the specific conversion goal? (e.g. Book a demo, download report, activate trial).
6. **Key Message / Angles:** Are there specific pain points or features to highlight in each email?

## Sequence Design Guidelines

When writing a nurture sequence, follow a logical value-driven progression:
* **Email 1: The Delivery & Immediate Value (Day 0)**
  * Deliver the requested resource or welcome the user. Keep it short, helpful, and set expectations for future emails.
* **Email 2: Problem Amplification & The Shift (Day 2)**
  * Contrast the status quo with the desired state. Highlight a common industry problem the recipient faces, backing it up with a stat or insight.
* **Email 3: The Solution & Case Study / Social Proof (Day 4)**
  * Introduce the brand's unique approach. Share a case study or anonymized client result showing how the problem was resolved.
* **Email 4: Objection Handling & FAQ (Day 6)**
  * Address the top reasons people hesitate (e.g., migration effort, cost, security, time-to-value). Use a Q&A or bulleted list format.
* **Email 5: The Direct Offer / Urgent CTA (Day 8)**
  * Pivot to a direct, low-friction invitation (e.g., a personalized 15-minute operational audit, trial check-in).

## Copywriting & Formatting Rules

1. **One-to-One Conversational Tone:** Emails must read like they were written by a human colleague, not a marketing department. Use simple, clear language. Avoid bulk marketing words (e.g., "revolutionary", "groundbreaking", "hurry").
2. **Subject Line Iteration:** Provide 3 distinct subject line options (Benefit-led, Curiosity-led, Question) and corresponding preview text (max 80 chars) for each email.
3. **Merge Tags:** Incorporate merge tags like `{{first_name}}`, `{{company}}`, and `{{job_title}}` naturally.
4. **Scannable Layout:** Keep paragraphs to 1–3 sentences max. Use bulleted lists for key benefits or objections. Use white space to draw the reader down the page.
5. **Clear CTA Anchor:** Do not use generic links (e.g., "click here"). Make CTA links highly context-driven (e.g., "See the full automation checklist" or "Schedule a 15-minute setup call with our team"). Include the link in its own line for mobile scannability.

## Output structure (`.md`)

Save as `output/email/sequence-<topic>-<date>.md` with this structure:

```markdown
# Email Sequence: [Campaign Name / Topic]
Target Audience: [ICP]
Funnel Stage: [e.g. Consideration / Warm Lead]
Primary CTA: [e.g. Book a Demo]
Date: [yyyy-mm-dd]

---

## Campaign Summary Table
| Email | Goal | Timing | Subject Line (Selected) | CTA |
|---|---|---|---|---|
| #1 | Welcome & Deliver Asset | Day 0 | [Subject] | Download Resource |
| #2 | Problem & Value Shift | Day 2 | [Subject] | Read Case Study |
| ... | | | | |

---

## Email 1: [Goal/Timing]

### Subject Line Options
- **Option A (Benefit):** [Subject line]
- **Option B (Curiosity):** [Subject line]
- **Option C (Question):** [Subject line]

**Preview Text:** [Preview text - max 80 chars]

### Body Copy

Hi {{first_name}},

[Hook / Delivery - immediate value.]

[Body - context, setting expectations, or introducing the core value.]

[Bulleted list of key details or takeaways.]

[Clear, contextual CTA link]

Best,

[Sender Name]  
[Title / Company Name]

---

## Email 2: [Goal/Timing]
...
```

## Rich deliverable

After saving the `.md`, invoke `document-skills:docx` to export the email copies as a Word document for review, styling, or uploading.
Save as `output/email/sequence-<topic>-<date>.docx`.

## Quality checklist

- [ ] Written in a conversational, human, one-to-one voice.
- [ ] Incorporates standard merge tags (`{{first_name}}`, etc.) naturally.
- [ ] 3 subject line options (Benefit, Curiosity, Question) and preview text provided per email.
- [ ] Paragraphs are short (1-3 sentences) with clean formatting.
- [ ] CTA links are descriptive and placed on their own line.
- [ ] No fake or invented customer data or metrics used.
- [ ] Output files saved to `output/email/` folder.
