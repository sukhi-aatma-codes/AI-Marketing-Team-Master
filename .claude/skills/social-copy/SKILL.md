---
name: social-copy
description: >
  Use this skill whenever the user wants to write text copy for social media posts — the
  written content that accompanies a social image or stands alone as a text post. Trigger
  on requests like "write a LinkedIn post about X", "draft captions for this campaign",
  "create social copy for our product launch", "write 3 LinkedIn post variants",
  "give me post copy for Y", or any request for social media text, captions, or post copy.
  This skill handles the written layer only — for the visual layer, use social-creative-designer.
  Works well in combination: social-copy for text, social-creative-designer for the image.
  Produces variants for A/B testing plus a Word doc for approval workflows.
---

# Social Copy

Writes platform-specific social post copy: hook, body, CTA, and hashtags. Produces 2–3
variants per post for A/B testing. Complements `social-creative-designer` (which handles
visuals). The `.md` is the working file; the `.docx` is for sharing with approvers.

## Before starting

Read this context file:
- `_context/Brand_Voice_Guide.md` — tone, voice pillars, banned words, power verbs, channel-specific
  tone guidance (LinkedIn company vs. LinkedIn executive vs. other platforms)

## Clarify inputs first

Confirm:
1. **Content to promote:** What is the post about? (Blog post, case study, event, stat, product, award)
2. **Platform(s):** LinkedIn (company page or executive voice), Instagram, Facebook, Twitter/X, or multiple
3. **Post objective:** Awareness, engagement, traffic, lead gen, or brand building
4. **Tone intent:** Thought leadership, educational, celebratory, urgency-driven, conversational
5. **Key message:** The single most important thing the reader should take away

## Platform defaults and constraints

| Platform | Optimal length | Tone | Format notes |
|----------|---------------|------|--------------|
| LinkedIn (company) | 150–300 words | Professional thought leadership | Start with hook; use line breaks for readability; 3–5 hashtags |
| LinkedIn (executive) | 100–250 words | First-person, insightful, personal | More conversational than company voice; story-led openings work well |
| Instagram | 125–150 words visible above fold | Warm, visual-context-dependent | Lead with the hook in first 2 lines; emoji used sparingly |
| Facebook | 100–200 words | Approachable, community-oriented | Shorter than LinkedIn; question-based CTAs perform well |
| Twitter/X | 240 chars max | Sharp, punchy, one idea | No room for body — hook + link + 1–2 hashtags only |

## Post structure

Every post follows: **Hook → Body → CTA → Hashtags**

**Hook (first 1–2 lines — most important)**
The hook must stop the scroll before the "see more" truncation. Options:
- A bold stat: "60% of marketing budgets go to channels no one is measuring."
- A counterintuitive claim: "Your biggest churn risk isn't your product."
- A direct question to the ICP: "Can your team tell leadership what a qualified lead actually costs?"
- A short declarative: "Your funnel is leaking more than you think. Here's the proof."

(These are hook *shapes* — pull the actual stats, claims, and ICP language from `_context\`.)

Never open with "We are excited to announce" or "Check out our latest..." — these are hook killers.

**Body (2–5 short paragraphs or a short list)**
- One idea per paragraph; short paragraphs (2–3 lines max)
- Work in the key message with a proof point from `Brand_Voice_Guide.md` or `_context/`
- Use line breaks between paragraphs for LinkedIn readability
- If using a list, max 3–4 items (more than 4 becomes a wall of text on mobile)

**CTA (last line before hashtags)**
- Must be specific: "Read the full guide: [link]" / "Book a 30-min call" / "Swipe through for all 5 signs"
- Match the brand CTA voice — use the primary CTAs defined in `Brand_Voice_Guide.md`
- Never: "Click Here" / "Learn More" without context

**Hashtags**
- LinkedIn: 3–5 tags. Mix: vertical (e.g. #B2BSaaS), function (e.g. #MarketingAutomation), brand hashtag (from Brand_Context.md if defined)
- Instagram: 5–10 tags. Add broader reach tags (e.g. #B2B, #DigitalTransformation, plus the brand's vertical tags)
- Facebook: 1–3 tags or none

## Produce 2–3 variants

For each post, produce variants that test different angles:
- **Variant A:** Stat-led hook (authority, grounded approach)
- **Variant B:** Question-led hook (engagement, challenges the reader)
- **Variant C:** Story or scenario hook (relatability, if appropriate for platform)

Label variants clearly. Note which angle each is testing and which to try first.

## Brand voice rules

From `Brand_Voice_Guide.md` — apply throughout:
- Lead with outcomes and transformation, not services (what the reader gets, not what the brand does)
- Every claim needs a proof anchor — or mark it as aspirational clearly
- Write to "you" — never "clients" or "businesses" in third person
- Apply the banned-words list from `Brand_Voice_Guide.md` — no exceptions

## Output structure (`.md`)

Save as `output/social/copy-<topic>-<date>.md`:

```
# Social Copy: [Topic]
Platform: [platform(s)]
Post objective: [awareness / engagement / traffic / lead gen]
Date: [yyyy-mm-dd]

## Variant A — [Hook type: stat-led / question-led / story-led]
[Full post copy]
Hashtags: #tag1 #tag2 #tag3
Note: [What this variant tests; recommended for first test]

## Variant B — [Hook type]
[Full post copy]
Hashtags: ...
Note: ...

## Variant C — [Hook type] (if applicable)
[Full post copy]
Hashtags: ...
Note: ...

## Usage notes
[Which variant to test first; platform-specific formatting tips; any claims to source before posting]
```

## Rich deliverable

After saving the `.md`, invoke `document-skills:docx` to produce a Word document for approval
workflows (team review, client sign-off, legal/compliance check if needed).
Save as `output/social/copy-<topic>-<date>.docx`

## Quality checklist

- [ ] Hook is in the first 1–2 lines and doesn't start with "We are..." or "Check out..."
- [ ] 2–3 variants produced, each testing a different hook angle
- [ ] Every claim has a proof point from `_context/` or is clearly marked aspirational
- [ ] No banned words from Brand_Voice_Guide.md
- [ ] Hashtags present and correctly sized for the platform
- [ ] CTA is specific — not "Learn More" without context
- [ ] `.md` and `.docx` both saved to `output/social/`
