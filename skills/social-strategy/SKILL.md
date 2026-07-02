---
name: social-strategy
description: >
  Use this skill whenever the user wants to plan a social media campaign, build an organic content calendar,
  or define platform-specific strategies (LinkedIn, Twitter/X, etc.). Trigger on requests like "create a
  social media calendar for next month", "plan a LinkedIn push for our new whitepaper", "design an organic
  social campaign for product X", or "develop a B2B platform strategy". Coordinates content pillars, visual
  specs, post copy hook guidelines, and scheduling patterns.
---

# Social Media Strategist

Designs comprehensive cross-platform organic social media campaigns, thematic content calendars, and channel strategies. Produces structured social calendar layouts in `.md` and formatted Word documents (`.docx`) in `output/social/` for marketing alignment and scheduling.

## Before starting

Read these context files every time — do not rely on prior session memory:
- `_context/Brand_Voice_Guide.md` — platform-specific tone rules (LinkedIn is typically authoritative, professional, and insight-led; Twitter/X is conversational, concise, and real-time oriented).
- `_context/Brand_Style.md` — visual themes, colors, and typography rules (crucial for defining design specs for graphics/carousels).
- `_context/Brand_Insights_Ledger.md` — Section 8 (Social Media Intelligence) and Section 2 (Creative & Formatting Insights) for historical performance benchmarks.
- `_context/Brand_Product_Offerings.md` — service lines and buyer personas.

## Clarify inputs first

Confirm with the user (unless specified):
1. **Campaign Objective:** Is the goal awareness, lead generation, website traffic, event registration, or thought leadership?
2. **Target Platform(s):** LinkedIn (Company / Personal profiles), Twitter/X, or other platforms.
3. **Hero Content / Topic:** What core topic, blog post, report, or announcement is the campaign promoting?
4. **Duration & Frequency:** How long is the campaign (e.g., 2 weeks, 4 weeks) and how many posts per platform (e.g., 3 posts per week)?
5. **Creative Format Preference:** Text-only, single image, graphic card, PDF document slide/carousel, or short video.

## Platform Strategy Rules

### LinkedIn (B2B Authority Builder)
* Focus on professional value, insights, and lessons learned.
* Post formats: Long-form text with a hook (the "Click to see more" line is critical), PDF document slides (carousels), or single graphic cards.
* Keep formatting clean. Use emojis sparingly as bullet points. Do not post links in the main text body (place in the first comment to avoid platform reach penalties, indicating: `[Link in first comment]`).

### Twitter/X (Industry Conversation Engine)
* Focus on conciseness, commentary on industry trends, and short actionable tips.
* Post formats: Single-concept posts (max 280 chars) or multi-post threads (the first post must have an engaging hook and a thread marker, e.g. `🧵 1/5`).
* Tag relevant accounts and use active, industry-specific hashtags (max 2 per tweet).

## Workflow

### Step 1 — Theme Mapping & Pillars
Select weekly themes or daily pillars to vary content types:
- **Thought Leadership:** Opinion pieces, market trends, or executive stance.
- **Actionable Value:** Step-by-step guides, quick fixes, or bulleted tips.
- **Social Proof / Credibility:** Case studies, client wins, metrics, or quotes.
- **Engagement / Question:** Polls, direct questions to the community, or debates.

### Step 2 — Visual Specification Design
For posts requiring creative support, draft detailed briefs for the design team matching `Brand_Style.md`:
* Spec dimensions (e.g., LinkedIn vertical 1080x1350, Twitter 1200x675).
* Hero text headline copy.
* Color hex selections and layout guidelines.

### Step 3 — Calendar Construction & Copywriting
Write the copy for all posts. Ensure every post has an attention-stopping hook, formatted body text, visual assets brief, and a clear call to action.

## Output structure (`.md`)

Save as `output/social/calendar-<topic>-<date>.md` with this structure:

```markdown
# Social Content Calendar: [Topic / Campaign Name]
Target Platforms: [e.g. LinkedIn and Twitter/X]
Campaign Duration: [e.g. 2 Weeks]
Date: [yyyy-mm-dd]

---

## Strategic Summary
* **Campaign Objective:** [Objective]
* **Target ICP:** [Persona profile]
* **Primary CTA Destination:** [Link]

---

## 1. Content Calendar Matrix
| Post ID | Platform | Date | Topic Pillar | Content Format | Visual Spec Summary | CTA |
|---|---|---|---|---|---|---|
| P-01 | LinkedIn | Mon | Thought Leadership | Long-text + PDF Slide | "3 Steps to..." | Download Report |
| P-02 | Twitter/X | Tue | Actionable Tip | Single text post | None | None |
| ... | | | | | | |

---

## 2. Post Copy & Specifications

### Post P-01: LinkedIn — [Thematic Hook Title]
* **Date / Time:** [Day, Hour]
* **Format:** Long-text + PDF Document Slider (Carousel)
* **Design Brief (For Creative Team):**
  * **Size:** 1080x1080 (1:1 Ratio)
  * **Number of Slides:** 4 Slides
  * **Colors:** Brand Primary Hex, Accents
  * **Slide 1:** Title: [Headline]
  * **Slide 2:** [Points/Body]
  * **Slide 3:** [Points/Body]
  * **Slide 4:** CTA: [Call to Action Text]

**Post Copy:**

[Attention Hook - Bold, direct statement or controversial insight. Must make reader click "...see more"]

[Paragraph 1 - Explaining the problem]

[Bulleted list of takeaways]

[Contextual CTA link indicator: (Link in first comment)]

---

### Post P-02: Twitter/X — [Topic]
* **Date / Time:** [Day, Hour]
* **Format:** Text Post (Max 280 characters)

**Post Copy:**

[Engaging Hook]

[Actionable tip or question]

[Hashtags (Max 2)]

---
```

## Rich deliverable

After saving the `.md`, invoke `document-skills:docx` to export the social calendar as a Word document.
Save as `output/social/calendar-<topic>-<date>.docx`.

## Quality checklist

- [ ] Clear campaign objective and ICP defined at top.
- [ ] Posting matrix table included with all required fields.
- [ ] Post hooks are engaging and designed for the platform (scrolling stops).
- [ ] Creative specs are explicit, including slide contents for LinkedIn carousels.
- [ ] Main copy is free of direct body links for LinkedIn posts.
- [ ] Character counts for Twitter/X posts are validated (≤280 chars).
- [ ] Output files saved to `output/social/` folder.
