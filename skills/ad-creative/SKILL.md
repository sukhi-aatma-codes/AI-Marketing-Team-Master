---
name: ad-creative
description: >
  Use this skill whenever the user wants to create paid advertising copy — headlines,
  descriptions, and CTAs for Google Ads, LinkedIn Ads, display ads, or retargeting.
  Trigger on requests like "write Google Ads for our insurance page", "create LinkedIn
  ad copy for X", "build an ad creative for this campaign", "write paid ads for Y",
  "give me ad headlines for Z", or any request for paid media copy. Produces a character-
  count-verified variant matrix ready for upload. Visual ad component direction is included
  as a brief for social-creative-designer — the visual layer is handled separately.
---

# Ad Creative

Generates character-count-compliant ad copy variant matrices for paid channels. Text layer
is fully produced; visual layer is documented as a brief for `social-creative-designer`.
The `.md` is the copy source of truth for upload and agent handoffs.

## Before starting

Read these context files every time:
- `_context/Brand_Voice_Guide.md` — voice pillars, outcome-led language, banned words
- `_context/Brand_Product_Offerings.md` — service lines, ICPs, differentiators, proof points

## Clarify inputs first

Confirm:
1. **Campaign objective:** Awareness, lead generation, retargeting, or event promotion
2. **Platform(s):** Google Search, LinkedIn Single Image, LinkedIn Sponsored Message, Display/Retargeting
3. **Service / offer:** What is being advertised?
4. **Target ICP:** Who sees this ad? (Role, vertical, pain point)
5. **Key message:** The one thing this ad must communicate
6. **Landing page URL:** Where does the ad send traffic?

## Platform character limits

These are hard limits. Every variant must be verified before delivery.

| Platform | Field | Limit | Notes |
|----------|-------|-------|-------|
| Google Search | Headline | 30 chars | Up to 3 headlines per ad |
| Google Search | Description | 90 chars | Up to 2 descriptions per ad |
| Google Search | Display URL path | 15 chars each | 2 optional path fields |
| LinkedIn Single Image | Intro text | 600 chars | Text above the image |
| LinkedIn Single Image | Headline | 70 chars | On the image card |
| LinkedIn Single Image | CTA button | 20 chars | From Canva button labels list |
| LinkedIn Sponsored Message | Subject | 60 chars | |
| LinkedIn Sponsored Message | Body | 500 chars | |
| LinkedIn Sponsored Message | CTA | 20 chars | |
| Display / Retargeting | Headline | 25–45 chars | Varies by network |
| Display / Retargeting | Description | 90 chars | |
| Display / Retargeting | CTA | 15–20 chars | |

## Copy workflow

### Guiding principles
- Lead with the outcome the ICP wants — not the service name
  ("Cut processing time by 30%" not "Our Outsourcing Services")
- Never lead with cost savings as the hook — lead with transformation, then anchor with efficiency
- Every headline or intro line must be able to stand alone — ads are scanned, not read
- Proof points outperform adjectives: "500+ clients" beats "experienced team"
- Match the ICP's language from `Brand_Product_Offerings.md` — use their terms, not internal ones

### Step 1 — Variant matrix
For each platform requested, produce:
- **3 headline variants** — each tests a different angle (outcome / proof / question / urgency)
- **2 description variants** — each expands on a different headline angle
- **2 CTA variants** — test action-oriented vs. value-oriented framing

Label each variant with its angle so the user knows what's being tested.

### Step 2 — Character count verification
After writing every variant, count characters and verify compliance.
Mark each field: ✓ (within limit) or ✗ N chars (over by N — must fix).
Fix all ✗ items before delivering.

### Step 3 — Recommended A/B test pairing
Suggest the first A/B test:
- Which headline × description × CTA combination to run first
- What hypothesis it tests (e.g., "outcome-led headline vs. proof-led headline")
- Which variant to hold back for the second test

## Visual ad component brief

The visual layer of image ads (LinkedIn Single Image, Display) is handled by `social-creative-designer`.
Include a visual brief at the bottom of the `.md` to pass to that skill:

```
## Visual Ad Brief (for social-creative-designer)

Platform: [LinkedIn Single Image / Display]
Dimensions: [1200×627px for LinkedIn; 300×250 / 728×90 / 160×600 for display]
Style recommendation: [select from `_context/Brand_Style_Reference.md` — match the style whose
"Best for" and "Energy" fit this ad's purpose, e.g. a typographic dark style for thought
leadership ads, a full-photo-bleed style for event ads, a photo-blend style for service
vertical ads. If that file doesn't exist yet, run `build-brand-style-reference` first.]
Visual subject: [what the image should show — not text, just the visual concept]
Text to overlay in Canva: [headline from the copy matrix that goes on the image]
Background: [brand primary / brand secondary / white — per Brand_Style.md]
```

## Output structure (`.md`)

Save as `output/ads/ad-creative-<campaign>-<date>.md`:

```
# Ad Creative: [Campaign Name]
Platform(s): [...]
Objective: [awareness / lead gen / retargeting]
Target ICP: [role, vertical]
Landing page: [URL]
Date: [yyyy-mm-dd]

## Google Search Ads
### Headline variants
| # | Headline | Chars | Angle | ✓/✗ |
|---|---------|-------|-------|-----|
| H1 | ... | 28 | Outcome-led | ✓ |
| H2 | ... | 30 | Proof-led | ✓ |
| H3 | ... | 27 | Question | ✓ |

### Description variants
| # | Description | Chars | Angle | ✓/✗ |
|---|------------|-------|-------|-----|
| D1 | ... | 88 | Expands H1 | ✓ |
| D2 | ... | 90 | Expands H2 | ✓ |

### Display URL paths
Path 1: [/Insurance] Path 2: [/Outsourcing]

### Recommended A/B test: H1 + D1 vs. H2 + D2
Hypothesis: [...]

---

## LinkedIn Single Image Ads
[Same table structure for Intro text, Headline, CTA button]
Recommended A/B test: [...]

---

## Visual Ad Brief (for social-creative-designer)
[Visual brief as specified above]

---
# TODO: Visual Components
The visual layer for image ads is handled by social-creative-designer using the brief above.
Run that skill separately with this brief as input to produce the ad creative images.
```

## Quality checklist

- [ ] Every variant character count verified — no ✗ items in the final output
- [ ] All 3 headline angles are genuinely different (not minor word swaps)
- [ ] No variant leads with "we" or with cost savings as the primary hook
- [ ] All proof points sourced from `_context/` or user-provided — nothing invented
- [ ] Recommended A/B test pairing included with a clear hypothesis
- [ ] Visual ad brief included for every image ad platform requested
- [ ] `.md` saved to `output/ads/`
