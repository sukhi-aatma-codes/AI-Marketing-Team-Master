# Reference Examples — Not Live Brand Data

The files in this folder are **worked examples**, not data for any currently active brand.
They demonstrate the expected output quality and format for two skills:

- **`cogneesol-deck-analysis.md`** (source: `cogneesol-deck.pptx`) — shows the depth of
  extraction expected from the deck-analysis workflow inside `build-brand-style`: exact hex
  codes pulled from slide XML, font usage, a full layout breakdown, decorative-element
  vocabulary, and a reproducibility verdict.
- **`cogneesol-brand-style-reference.md`** — shows the expected output format for the
  `build-brand-style-reference` skill: a generative visual style library with per-style
  energy/look/color-usage descriptions and ready-to-use Flux and Ideogram prompt starters.
- **`cogneesol-deck.pptx`** also doubles as a worked example of what a finished
  `_templates/Brand_Deck_Template.pptx` should look like (the artifact `build-brand-deck-template`
  produces) — it was already 100% reproducible from native shapes with zero embedded media,
  which is exactly the standard a generated template should hit.

**Do not read these as input when onboarding or updating the active brand.** They belong to
a past demo engagement (Cogneesol) and are kept here purely as a quality bar / format
reference for the skills that generate the real, per-brand equivalents: `_context/Brand_Style.md`,
`_context/Brand_Style_Reference.md`, and `_templates/Brand_Deck_Template.pptx`.
