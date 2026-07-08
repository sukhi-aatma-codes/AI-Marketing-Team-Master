---
name: branded-deck
description: Build on-brand strategy and campaign presentation decks by extending the official pptx skill. Use whenever the user asks for a deck, slides, presentation, pitch, strategy doc, or campaign plan in slide form. Picks layouts from a bundled brand template, matches its colors/fonts/spacing exactly, and produces a `.pptx` file. Trigger on phrases like "make a deck", "build a presentation", "branded slides", "campaign deck", "strategy deck", or any request for a `.pptx`.
---

# branded-deck

Builds **on-brand presentation decks** by composing layouts from a bundled brand template. Extends the official `document-skills:pptx` skill — that skill handles the `.pptx` mechanics; this skill handles brand fidelity, layout selection, and storytelling structure.

## Inputs (read these first, every time)

This skill is brand-agnostic. All brand-specific design rules live in two swappable files in
`_templates\`. **Always read them at the start of every run** — never rely on memory of past
sessions, and never reuse a template left over from a different brand:

1. **Brand template (binary):** `_templates/Brand_Deck_Template.pptx`. This is the visual source of truth — the deck you produce must look like it could have been made from this file.
2. **Template analysis (markdown):** `_templates/Brand_Deck_Template_Analysis.md`. Contains the exact color hex codes, font, font-size hierarchy, layout inventory, decorative vocabulary, and recurring elements. Treat its specs as **non-negotiable**.

If either file is missing, run `build-brand-deck-template` first — don't improvise a brand from
scratch, and don't fall back to any other brand's template.

Also load the brand voice/style files from the project's `_context/` folder when writing slide copy (voice guide for tone, product offerings for accurate service language). The analysis governs **visuals**; `_context/` governs **words**.

## Workflow

### 1. Clarify the brief (skip only if the user has already given all of these)

Before writing any code, confirm:
- **Purpose** — sales pitch, internal strategy, campaign plan, board update, etc.
- **Audience** — who's in the room, what they care about
- **Length** — target slide count (default 10–14 if unspecified)
- **Must-include content** — stats, case studies, products, timelines the user wants surfaced
- **Output filename and folder** — default to `output/presentations/` with `<topic>-<yyyy-mm-dd>.pptx`

Don't ask all of these if context already answers them. Do ask if the brief is vague — generic decks waste a re-render cycle.

### 2. Outline the storyline before touching code

Sketch the slide-by-slide flow as a short bulleted list and confirm with the user. For each slide, choose the layout from the template's inventory (see analysis file) that best fits the storytelling beat:

| Storytelling beat | Pick this layout |
|---|---|
| Open the deck, set context | Title slide (dark) |
| Show the agenda / table of contents | Agenda |
| Mark a major section transition | Section divider (dark, giant numeral) |
| Make a single argument with one supporting stat | Two-column insight |
| Show a portfolio of services / pillars / options | Capabilities grid (3×2 or similar) |
| Prove credibility with metrics | By the Numbers (dark) |
| Show social proof / a quote | Testimonial (cool gray) |
| Walk through a process or methodology | Process timeline (numbered horizontal flow) |
| Tell a customer story | Case study |
| Anything that doesn't fit a specialised layout | Generic content |
| Close the deck | Thank You / closing (dark) |

**Rules of thumb:**
- **Sandwich structure**: open dark → light content slides → close dark. Use section dividers (dark) to break up long light stretches.
- **Don't repeat the same layout back-to-back** — vary cards, columns, timelines, stat callouts.
- **Every slide needs a visual element.** No plain bullet-list slides.
- **Use the brand's accent color sparingly** — only on numerals, key stats, and the wordmark, exactly as the analysis describes. Never on body copy or large fills.

### 3. Build the deck

Hand off `.pptx` mechanics to the official pptx skill. Two viable paths:

- **Edit the brand template** (preferred when the template is well-built): unpack `_templates/Brand_Deck_Template.pptx`, duplicate the layout slides you need, replace placeholder text and stats, repack. Inherits exact styling for free.
- **Generate from scratch with `pptxgenjs`** (use when the structure differs significantly): re-create each chosen layout using the exact specs from the analysis file — same hex codes, same font, same size hierarchy, same decorative shape vocabulary (rectangles, ellipses, lines only, unless the analysis says otherwise).

Whichever path: **read the analysis file's specs verbatim** when setting colors, fonts, sizes, and positions. Do not approximate "a similar navy" — use the exact hex.

### 4. Required QA pass

Follow the official pptx skill's QA workflow. In addition, verify against the brand template:

- **Color check**: every fill, stroke, and text color appears in the analysis's palette table. No off-palette colors.
- **Font check**: only the typeface(s) named in the analysis. No Arial/Calibri sneaking in.
- **Layout check**: each slide matches a named layout from the analysis (or is a deliberate, justified composite).
- **Recurring elements**: wordmark in the position the analysis specifies, footer band on the slides the analysis specifies, page numbers correct.
- **Placeholder check**: no leftover `[IMAGE PLACEHOLDER]`, `XXXX`, lorem ipsum, or "Section Title Goes Here" text.
- **Visual subagent pass**: render to images and have a fresh-eyes subagent inspect for overlap, overflow, and brand drift.

Do not declare done until at least one fix-and-verify cycle has run.

## Output

- The `.pptx` file, saved to the folder agreed in step 1 (default `output/presentations/`).
- **If the calling skill requires a PDF** (e.g. `lead-magnet`): export the `.pptx` to PDF immediately after saving it. Use PowerPoint COM automation via `comtypes` on Windows — open the file with `comtypes.client.CreateObject('Powerpoint.Application')`, call `presentation.SaveAs(pdf_path, 32)` (32 = ppSaveAsPDF), then close PowerPoint. Save the PDF to the same folder and base filename as the `.pptx`. Confirm the PDF file exists and its size is non-zero before declaring done.
- A short note back to the user: which layouts were used, which slides need their data confirmed, and any open questions.

## What NOT to do

- Don't invent a different brand palette or font because it "looks better."
- Don't skip the analysis file — it's the contract.
- Don't add icons, illustrations, gradients, or background patterns unless the analysis explicitly permits them.
- Don't fill slides with bullet lists. Use the visual layouts the template offers.
- Don't fabricate stats, case studies, or quotes. If the brief is missing proof points, ask the user.

## Completion checklist

- [ ] `.pptx` saved to the agreed folder (default `output/presentations/`) — and PDF exported alongside it if the calling skill requires one (non-zero file size confirmed)
- [ ] Every fill, stroke, and text color appears in the analysis file's palette table — no off-palette colors
- [ ] Only the typeface(s) named in the analysis used — no Arial/Calibri substitutions
- [ ] Every slide matches a named layout from the analysis (or is a deliberate, justified composite)
- [ ] Wordmark, footer band, and page numbers placed per the analysis's recurring-elements spec
- [ ] Zero leftover placeholder text (`[IMAGE PLACEHOLDER]`, `XXXX`, lorem ipsum, "Section Title Goes Here")
- [ ] At least one fix-and-verify cycle run after the visual inspection pass
- [ ] Summary note delivered: layouts used, slides needing data confirmation, open questions
