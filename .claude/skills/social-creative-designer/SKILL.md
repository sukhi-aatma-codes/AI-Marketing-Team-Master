---
name: social-creative-designer
description: >
  Use this skill whenever the user wants to create LinkedIn carousel posts, social media slides,
  single social graphics, or any branded visual content for social channels. Trigger on requests
  like "create a carousel", "make a LinkedIn post visual", "design social slides", "generate a
  carousel about X", "create a graphic for our Instagram", or any mention of social graphics,
  carousel slides, or branded visuals for LinkedIn, Instagram, Facebook, or other platforms.
  This skill manages the full workflow from style selection through image generation and export,
  using a two-tool architecture: Ideogram for visual/photo elements and Canva for all typography
  and layout assembly. Use it even if the user doesn't explicitly say "carousel" — any request
  for a social post visual or slide series belongs here.
---

# Social Creative Designer

Generates LinkedIn carousels, single social graphics, and branded visual content using a
two-tool architecture. **Ideogram** owns the visual/photo layer. **Canva** owns all typography,
layout composition, and final export. These roles never overlap.

## Before starting

Always read `_context/Brand_Style_Reference.md` first, unless the user has explicitly named a
style. Use it to select the most appropriate style for the content type and to load the exact
creative direction, color values, prompt starters, and do-not rules for that style. If this file
doesn't exist yet for the active brand, run `build-brand-style-reference` first — do not invent
style codes or fall back to generic stock-AI-image aesthetics.

## Defaults

| Setting | Default |
|---------|---------|
| Slides per carousel | 5 |
| Aspect ratio | 4:5 (LinkedIn portrait) |
| Platform | LinkedIn |
| Single image | 1:1 square |

Also support: 1:1, 3:4, 1.91:1. Platforms: Instagram, Facebook. Adjust when the user specifies.

## Carousel structure

Every carousel follows this arc regardless of style:

- **Slide 1 — Hook:** Bold attention-stopping headline, minimal text. Scroll-stopping entry point.
  Apply the hook slide spec from Brand_Style_Reference.md for the active style.
- **Slides 2 to N-1 — Value:** One idea per slide — a stat, insight, or teaching point. Never
  crowd a slide with more than one idea.
- **Slide N — CTA:** Key takeaway or offer. Primary proof point (from Brand_Product_Offerings.md) + brand domain (from Brand_Context.md) + primary CTA (from Brand_Voice_Guide.md).

For a single static image: apply the same style to one frame. The hook/value/CTA structure
doesn't apply — focus the single frame on the strongest idea.

---

## Two-tool architecture

The two tools have distinct, non-overlapping responsibilities. Confusing them causes text
hallucination (Ideogram) or missing visuals (Canva-only for photo styles).

| Tool | What it does | What it never does |
|------|--------------|--------------------|
| **Ideogram** | Generates photographic backgrounds, atmospheric scenes, abstract art, illustration, textured environments — any image where the visual element is primary | Renders text, headlines, labels, numbers, or any typography |
| **Canva** | Handles all typography, text hierarchy, brand colour fills, layout composition, and exports the final PNG | Generates photographic or illustrative backgrounds |

**Critical rule:** Never include text, words, numbers, or labels in an Ideogram prompt. If the
style spec calls for a number or headline, that always goes to Canva — not Ideogram.

### Style → tool routing

Style codes and names are brand-specific and live in `_context/Brand_Style_Reference.md` — do
not hardcode any brand's actual style names here. Instead, read each style's "Look" description
and classify it into one of these archetypes to decide the Ideogram/Canva split:

| Archetype | Ideogram role | Canva role |
|-----------|---------------|-----------|
| **Typographic-only** (solid brand-color fill, no photo/illustration element) | Not used | Full slide: brand fill, headline, rule/marker accents per spec, wordmark, export |
| **Photo-blend** (a generated or abstract visual element occupies part of the frame, blended with text) | Generates the visual element per the style's Ideogram prompt starter — no text, no typography | Headline, sub-copy, CTA overlay, brand-color framing, export |
| **Full-photo-bleed** (a photograph or photorealistic generation fills the entire frame) | Full-bleed visual per the style's Ideogram prompt starter — no text, no typography | Gradient/overlay treatment per spec, text legibility layer, CTA, export |
| **Diagram/framework** (explanatory shapes, no photography) | Not used | Full diagram: shapes, labels, connecting lines per spec, export |

For each requested style, read its `_context/Brand_Style_Reference.md` entry, determine which
archetype it matches from the "Look" description, and apply the corresponding tool split above
using that style's own colors, prompt starters, and do-not rules — never another brand's.

---

## Ideogram workflow (when needed)

Use `mcp__ideogram__generate_image`.

**Rules:**
- Add "no text, no typography, no lettering, no words, no numbers" to every prompt explicitly.
- Use the Ideogram prompt starter from Brand_Style_Reference.md as the creative base, then adapt
  it to the specific subject matter.
- Aspect ratio: `4x5` for LinkedIn portrait default. Also supported: `1x1`, `3x4`.
- Style mode: `DESIGN` for graphic design outputs; `REALISTIC` for photography; `AUTO` when unsure.
- Outputs save to `output/ideogram_output/` per the MCP config. Note the file path — Canva needs it.

---

## Canva workflow (every slide)

Every slide — including pure typographic slides with no Ideogram element — goes through Canva
for final assembly and export. Typography is never generated any other way.

**Step 1 — Get brand kit (once per session)**
```
mcp__canva__list-brand-kits
```
Retrieve the brand kit ID. Reuse this ID for all slides in the same session.

**Step 2 — Generate design**
```
mcp__canva__generate-design
```
Describe the slide fully: background colour (exact hex), font (the brand typeface from Brand_Style.md, exact weight), all
text content and hierarchy, layout structure, and any Ideogram-generated visual to incorporate.
Reference the style spec from Brand_Style_Reference.md for spacing, rule placement, and do-nots.
Include: brand primary color, brand accent color, and brand font at the correct weight (all from Brand_Style.md).

**Step 3 — Confirm candidate**
```
mcp__canva__create-design-from-candidate
```
Select and finalise the design candidate.

**Step 4 — Export PNG**
```
mcp__canva__export-design
```
Export at the target resolution. Save to `output/social/` folder using the naming convention below.

---

## Output naming

```
output/social/social-<topic-slug>-slide-<N>-<yyyy-mm-dd>.png
```

Example: `output/social/social-q3-launch-slide-1-2026-05-09.png`

For single images: `output/social/social-<topic-slug>-<yyyy-mm-dd>.png`

---

## Tool unavailability

Handle each tool's failure independently — they are separate systems.

**If Ideogram is unavailable:**
- Tell the user clearly which of the requested styles are affected (any photo-blend or
  full-photo-bleed archetype per `Brand_Style_Reference.md`).
- Offer to continue: typographic-only and diagram/framework styles can be completed fully
  through Canva alone. Photo-dependent styles are blocked until Ideogram is restored.

**If Canva is unavailable:**
- Tell the user clearly. Canva handles all text and export — this is a full blocker for every style.
- Offer to: generate any needed visual backgrounds through Ideogram, and deliver a written text
  brief (headline, body, CTA, hex values, font spec, layout notes) the user can apply manually.

**If both are unavailable:**
- Tell the user clearly. Offer to deliver the complete slide content as a written brief: exact
  copy per slide, hex colours, font weights, layout description, and style spec — ready for a
  designer or the user's own design tool.

---

## Quality checklist before delivering

For each finished slide, confirm before reporting completion:

- [ ] Background colour matches the style spec exactly
- [ ] Headline text is readable and not garbled
- [ ] Font is the brand typeface (per Brand_Style.md) at the correct weight for the style
- [ ] Brand wordmark is present (position per Brand_Style_Reference.md)
- [ ] Only one idea per slide — not crowded
- [ ] File is saved to `output/social/` with the correct filename and date
