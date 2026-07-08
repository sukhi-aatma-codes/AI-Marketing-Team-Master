---
name: build-brand-style-reference
description: >
  Use this skill to build or refresh Brand_Style_Reference.md — the generative visual style
  library that social-creative-designer, ad-creative, campaign-brief, and lead-magnet read for
  image-generation direction. Trigger when: image creative samples (social graphics, ad
  visuals, banners) are provided for a brand, the active brand has no Brand_Style_Reference.md
  yet, or existing visual assets need to be re-analyzed after a style update. Accepts uploaded
  images, a folder of creative samples, or URLs to existing brand visuals as input. Does NOT
  touch Brand_Style.md or any other _context\ file — this is a distinct, image-generation-
  specific deliverable with its own format.
---

# Build Brand Style Reference

Refreshes `_context/Brand_Style_Reference.md` — a directional style library written so Claude
and image-generation models (Flux, Ideogram) can interpret and reproduce on-brand visuals. This
is not a copy of `Brand_Style.md`'s color/typography rules; it's a working library of named,
reusable visual *styles*, each with a concrete prompt starter.

## Scope — what this skill writes

This skill writes ONE file: `_context/Brand_Style_Reference.md`.
It does NOT modify `Brand_Style.md`, `Brand_Context.md`, `Brand_Voice_Guide.md`,
`Brand_Product_Offerings.md`, `Brand_Growth_Marketing_Context.md`, or `Brand_Insights_Ledger.md`.

## Before starting

Read `_context/Brand_Style.md` first if it exists — every style entry must use the brand's
actual hex codes and typography, not invented ones. If `Brand_Style.md` doesn't exist yet, run
`build-brand-style` first; a style reference without a grounded color/type system will drift.

If `_context/Brand_Style_Reference.md` already exists, read it first. Merge new styles in
rather than discarding ones the user hasn't asked to replace.

See `_samples/_reference-examples/cogneesol-brand-style-reference.md` for the expected depth
and format of the output — it is a worked example, not data for the active brand.

## Clarify inputs

Ask the user:
1. **Source material**: Uploaded images, a folder/archive of past creative (check
   `_samples\INDEX.md` if `sample-archive-index` has already run), or a URL to existing brand
   visuals (website, social profile)?
2. **Coverage**: Should this cover one campaign's visuals, or build a full library across
   formats (social, ads, presentations, events)?
3. **Aspirational styles**: Should the library also propose new directions to build toward
   (clearly labeled as not-yet-real), or strictly document what already exists?

## Workflow

### Step 1 — Visual analysis, per source image
For each image provided, analyze:
- **Composition**: framing, focal areas, how text/photo/graphic zones divide the frame
- **Color usage**: which brand colors appear and in what proportion (e.g. "80% navy, 15%
  photography, 5% accent")
- **Energy/mood**: the feeling the style conveys and why (e.g. "quiet authority," "scroll-
  stopping urgency") — this is what lets Claude pick the right style for a given brief later
- **Recurring marks**: logo placement, geometric signatures, consistent decorative elements

### Step 2 — Name and group styles
Give each distinct style a short code and name (e.g. "E1: Constellation Banner"). Group into:
- **Existing Styles** — documented directly from real assets the user provided
- **Aspirational Styles** (optional, only if requested) — new directions extrapolated from the
  brand's established visual language, clearly labeled as not-yet-real so they aren't mistaken
  for documented brand history

### Step 3 — Write prompt starters
For each style, write both a **Flux prompt starter** and an **Ideogram prompt starter** —
concrete, reusable prompt text with a `[SUBJECT]` placeholder for the variable content, written
so `social-creative-designer` and `ad-creative` can drop it in directly.

### Step 4 — Do-not rules
For each style, state what breaks it (e.g. "don't use warm/bright photography," "don't round
the corners on the diagonal cut") — these prevent downstream drift toward generic AI-image
aesthetics.

## File structure to produce

Write `_context/Brand_Style_Reference.md`:

```
# [Company Name] — Brand Style Reference Guide

A visual style library for content creation across digital, social, print, and event formats.
Each style is described using directional creative language so Claude and image generation
models (Flux, Ideogram) can interpret and produce on-brand variations with flexibility.

**Brand constants that apply to ALL styles:**
- [Primary color]: `#XXXXXX`
- [Secondary color]: `#XXXXXX`
- Font: [Typeface] (from Brand_Style.md)
- Tone: [from Brand_Voice_Guide.md]
- Never: [hard brand-wide visual exclusions]

---

## EXISTING STYLES
*Documented from real brand assets.*

---

### [Code]: [Style Name]

**Format:** [dimensions]px ([orientation]). [Where this format is used.]

**Best for:** [Content types/placements this style fits.]

**Energy:** [The feeling this style conveys and why.]

**Look:** [Detailed prose description — precise enough that someone could redraw it from
the description alone: layout proportions, color placement, treatment of photography/
illustration, decorative elements and their exact position.]

**Color usage:** [Percentage breakdown of color/photography/accent.]

**Flux prompt starter:**
> [Concrete prompt text with [SUBJECT] placeholder]

**Ideogram prompt starter:**
> [Concrete prompt text with [SUBJECT] placeholder]

**Do not:** [What breaks this style.]

---

## ASPIRATIONAL STYLES
*(Only include this section if the user asked for new directions, not just documentation of
existing assets.) These styles do not yet exist in the brand's asset library.*

[Same structure as above, per style.]
```

## Quality rules

- Every hex code must trace back to `Brand_Style.md` — never invent a color not in the brand's
  established palette.
- "Look" descriptions must be specific enough to function as a generation brief — vague language
  ("modern, clean design") is not acceptable; describe exact proportions, placements, and
  treatments.
- Prompt starters must be platform-agnostic prompt text, not chat instructions — they get pasted
  directly into image-generation tools.
- Aspirational styles must be clearly separated from existing ones — never blend them in the
  same section.
- If insufficient source images are available to extract a real style, do not invent one; tell
  the user more samples are needed.

## Output

Save to: `_context/Brand_Style_Reference.md`

After saving, report to the user:
- How many distinct styles were documented and from how many source images
- Any style gaps (e.g. "no event/presentation visuals provided — that format isn't covered yet")
- Whether aspirational styles were included or this is existing-only

## Completion checklist

- [ ] File saved to exactly `_context/Brand_Style_Reference.md` — no other `_context\` file modified
- [ ] Every hex code traces back to `Brand_Style.md` — no invented colors
- [ ] Every style's "Look" description is specific enough to function as a generation brief on its own
- [ ] Prompt starters are paste-ready prompt text, not chat instructions
- [ ] Aspirational styles clearly separated from existing ones; no style invented from insufficient samples
- [ ] Report delivered to the user: style count and source count, format gaps, aspirational inclusion
