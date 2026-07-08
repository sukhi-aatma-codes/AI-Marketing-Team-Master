---
name: build-brand-deck-template
description: >
  Use this skill to build or refresh the active brand's reusable .pptx deck template —
  the actual binary file branded-deck assembles new presentations from. Trigger when: a
  style-source deck has just been analyzed by build-brand-style's deck-extraction workflow
  and no template exists yet for this brand, branded-deck reports its template is missing,
  or the brand's visual identity has changed enough that the existing template is stale.
  Produces a real .pptx file, not a markdown description — that's build-brand-style's job.
  Does NOT touch _context\ — this skill writes to _templates\ only.
---

# Build Brand Deck Template

Produces `_templates/Brand_Deck_Template.pptx` — the actual reusable presentation file
`branded-deck` duplicates and adapts for every new deck — plus its companion analysis file.
This is the construction step. The extraction/analysis step belongs to `build-brand-style`'s
deck-extraction workflow; this skill consumes that output rather than redoing it.

## Scope — what this skill writes

This skill writes to `_templates\` only: `Brand_Deck_Template.pptx` and
`Brand_Deck_Template_Analysis.md`. It does not modify any `_context\` file.

## Before starting

Read `_context/Brand_Style.md` first — the template must use the brand's actual hex codes,
typography, and grid principles, never invented ones.

Check whether a style-source deck has already been analyzed (either earlier in this
conversation or recorded in `_samples\INDEX.md` as a deck-type source). If `build-brand-style`
hasn't run its deck-extraction workflow on that source yet, run it first — this skill needs
those specs, not the raw deck file.

If `_templates/Brand_Deck_Template.pptx` already exists, ask the user whether this is a
refresh (visual identity changed) or the file is fine as-is before overwriting it.

See `_samples/_reference-examples/cogneesol-deck.pptx` and its companion
`cogneesol-deck-analysis.md` for the expected output quality — a worked example, not data for
the active brand. Note that file is itself proof of the standard to hit: 11 layouts built
entirely from native shapes and text, zero embedded media, fully reproducible from spec alone.

## Two modes

### Mode A — deck-derived (preferred when a source deck was provided)
Use the layout inventory from `build-brand-style`'s deck-extraction output: the named layout
patterns (title, agenda, section divider, etc.), their exact composition, the decorative
shape vocabulary, and recurring elements (wordmark position, footer treatment). Reproduce each
layout as one slide in the new template, built from native shapes (rectangles, ellipses, lines)
and text boxes — using the brand's real extracted hex codes and fonts, not the source deck's
embedded media (there should be none to extract if the source deck is itself reproducible;
if it isn't, flag which elements can't be faithfully reproduced and why).

### Mode B — style-derived only (no source deck available)
If `_context/Brand_Style.md` exists but no deck was ever analyzed, propose a default layout
set using the brand's established colors/fonts/grid:
- Title slide
- Agenda / table of contents
- Section divider
- Two-column insight (heading + stat callout)
- Capabilities/services grid
- Stat/metrics callout ("by the numbers")
- Testimonial / social proof
- Process timeline
- Case study
- Generic content (open layout for charts/tables/text)
- Closing / thank you

Mark every slide in this mode with a note in the analysis file that these are **proposed
defaults**, not extracted from real brand history — the user should treat them as a starting
point to refine, not a faithful reproduction of anything that already exists.

## Workflow

1. Confirm mode (A or B) based on what's available.
2. Build each layout slide using `document-skills:pptx` — native shapes and text only, exact
   hex codes and font names from `Brand_Style.md` (or the deck extraction), placeholder text
   in every text element (e.g. "Section Title Goes Here", `[IMAGE PLACEHOLDER]` where a photo
   slot is needed) so `branded-deck` can find-and-replace cleanly.
3. Write the companion analysis file — same structure as `build-brand-style`'s deck-extraction
   output (color table, typography hierarchy, layout inventory, decorative vocabulary,
   reproducibility notes), adapted to describe *this* template file specifically so
   `branded-deck` has one authoritative spec to read alongside the binary.
4. QA pass: confirm every color/font used in the built `.pptx` matches `Brand_Style.md` exactly
   — no off-palette colors, no substituted fonts. Confirm no embedded media was introduced.

## Output

Save to:
- `_templates/Brand_Deck_Template.pptx`
- `_templates/Brand_Deck_Template_Analysis.md`

After saving, report to the user:
- Which mode was used (deck-derived vs. style-derived defaults)
- How many layouts the template includes and what each is for
- Any elements flagged as not faithfully reproducible (Mode A) or proposed rather than
  extracted (Mode B)

## Completion checklist

- [ ] Both files saved: `_templates/Brand_Deck_Template.pptx` and `_templates/Brand_Deck_Template_Analysis.md` — nothing written to `_context\`
- [ ] Every color and font in the `.pptx` matches `Brand_Style.md` (or the deck extraction) exactly
- [ ] Every text element carries find-and-replace placeholder text; no embedded media introduced
- [ ] Analysis file covers: color table, typography hierarchy, layout inventory, decorative vocabulary, reproducibility notes
- [ ] Report delivered to the user: mode used, layout count and purposes, non-reproducible or proposed elements
