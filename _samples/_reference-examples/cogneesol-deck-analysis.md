# Cogneesol Enterprise Template — Analysis

**Source:** [cogneesol-deck.pptx](cogneesol-deck.pptx) — 11 slides, no embedded raster images, no logo files. Everything is built from native PowerPoint shapes (rectangles, ellipses, lines) and text. **The entire template is reproducible from scratch — nothing needs to be extracted.**

---

## 1. Color System

**Exact palette (sampled from slide XML, ordered by frequency of use):**

| Hex | Role | Where it shows up |
|---|---|---|
| `#FFFFFF` | White | Body text on dark slides; card/panel fills on light slides |
| `#AB2828` | **Brand red accent** | Section numbers (01, 02, 03…), key stat digits ("99%"), "COGNEESOL" wordmark |
| `#112C7D` | **Primary navy** | Dark slide background, primary headings on light slides |
| `#0C1F5C` / `#162F8A` | Deeper / lighter navy | Layered rectangles, gradient-like depth on dark slides |
| `#1A1A2E` | Near-black navy | Deep accent rectangles |
| `#A8BCEF` / `#7A93C9` / `#9BAACC` | Light-blue tints | Subtitles and supporting text on dark navy slides |
| `#E4E7F0` / `#F4F5F8` | Off-white / cool gray | Light card backgrounds, testimonial slide background |
| `#4A5568` | Slate gray | Body copy on light backgrounds |
| `#000000` | Black | Occasional text |
| `#FFBBBB` | Pale pink | Used once — likely a one-off accent |

**Pattern:**
- **Dark slides (`#112C7D`)** = title, agenda, section dividers, by-the-numbers, thank-you (slides 1, 3, 6, 11). Used to bookend the deck and mark transitions.
- **Light slides (`#FFFFFF`)** = content, capabilities, process, case study (slides 4, 5, 8, 9, 10).
- **One cool-gray slide (`#F4F5F8`)** = testimonial (slide 7) — sits between dark and light to feel softer.
- **Red (`#AB2828`)** is the disciplined accent: only used for numerals, key stats, and the wordmark. Never used for body text or large fills.

---

## 2. Typography

- **Single typeface across the entire deck: Montserrat** (510 references, no other font used). Headers and body share the family — weight and size do the work.
- **Size hierarchy (in pt):**
  - Mega-numerals: **180–210pt** (huge "01", "02" section numbers behind text on slides 3 and 7)
  - Hero titles: **44–62pt** (slide 1 title, slide 11 "Thank You")
  - Slide titles: **22–28pt**
  - Sub-headings: **15–19pt**
  - Body: **11–13pt**
  - Captions / footers: **6–10pt**
- **Style patterns:**
  - "COGNEESOL" wordmark and section labels (e.g., "AGENDA", "CASE STUDY", "OUTCOMES") are rendered **uppercase with letter-spacing** — small caps look.
  - Numerals (`01`, `02`, `99`, `%`) are styled as oversized display elements in red, often paired with a smaller label below.
  - Body copy is sentence case, regular weight; titles use bold/semibold.

---

## 3. Layout Patterns

11 distinct layouts identified:

| # | Layout | Composition |
|---|---|---|
| 1 | **Title slide** (dark navy) | Wordmark top-left; large title + subtitle stack centered-left; presenter/date strip at bottom; small red ellipse decorative dot |
| 2 | **Agenda** (white) | "AGENDA" eyebrow top-left; "What we'll cover today" pull-quote left; 5 numbered items in a 2-column grid right (red "01"–"05" + title + one-line description); 8 thin connecting lines |
| 3 | **Section divider** (dark navy) | Giant `02`-style numeral (~210pt) ghosted in background; "SECTION TWO / Section Title Goes Here" stacked center-left; brief description; right column lists key focus areas |
| 4 | **Two-column insight** (white) | Slide title bar; left = primary heading + 3 bullet points; right = oversized stat callout (`99` + `%` + label) over supporting paragraph |
| 5 | **Capabilities grid** (white) | Title + intro line; **3×2 grid of cards**, each with red number, bold service name, short description |
| 6 | **By the Numbers** (dark navy) | Title; **4 stat blocks in a row** — large red number with `+` or `%` superscript, label below, micro-context line; certification strip at bottom |
| 7 | **Testimonial** (cool gray) | Giant red `"` quote mark (180pt); pull-quote in dark text; outcomes row (4 metrics) at bottom; attribution line |
| 8 | **Process timeline** (white) | Title + intro; **5-step horizontal flow** — numbered circles `01`–`05` connected by line, each with phase name + description below; framework footer band |
| 9 | **Case study** (white) | Title; left = `[IMAGE PLACEHOLDER]` + Challenge/Solution stack; right = "CASE STUDY" eyebrow + 3 stat tiles + client/industry strip |
| 10 | **Generic content** (white) | Title bar; section label badge; large open content area for charts/tables/text |
| 11 | **Thank You / closing** (dark navy) | Large "Thank You" + tagline center; contact lines (email/phone/web); address strip; wordmark |

**Recurring positional pattern:** On nearly every slide, the **"COGNEESOL" wordmark sits top-left** and the **page footer** ("The Partner in Your Transformation Journey" + page number) sits **bottom-center / bottom-right** on content slides 4–10.

---

## 4. Decorative Elements

The template uses a **deliberately minimal vocabulary** of 3 shape primitives:
- **Rectangles** — used as panels, cards, dividers, footer bands, content backgrounds
- **Ellipses** — used as numbered circles in process flows, decorative dots, the "99%" frame, and stat backgrounds
- **Thin lines** — connectors in the agenda and process timeline, divider rules in footer strips

There are **no icons, no illustrations, no photographs, no background graphics, no gradients, no patterns**. The visual interest comes entirely from:
1. Strong dark-vs-light slide contrast
2. Oversized red numerals as the recurring motif
3. Disciplined whitespace and grid alignment

**Reproducibility: 100%.** Every decorative element is a native PPTX preset shape with a solid fill. Nothing needs to be extracted from the original — a regenerated template using the same hex codes and Montserrat will be visually identical.

---

## 5. Recurring Elements

**On every slide:**
- "COGNEESOL" wordmark, **top-left corner**, ~10–15pt, white on dark slides / navy on light slides. (No bitmap logo — it's set in Montserrat with letter-spacing as type, not an image.)

**On content slides 4–10 (not on title/agenda/section dividers/closing):**
- Footer band at bottom containing "COGNEESOL — The Partner in Your Transformation Journey" + page number, ~6–8pt
- Small red decorative ellipse near the wordmark or footer

**Not present:**
- No image-based logo file in `/ppt/media/` (the folder is empty)
- No recurring background graphic, watermark, or pattern

---

## What can vs. can't be reproduced

| Element | Reproducible from scratch? |
|---|---|
| All colors (10 hex codes above) | Yes — verified from XML |
| Montserrat typography + size hierarchy | Yes — Montserrat is a free Google Font |
| All 11 layouts | Yes — pure shape + text composition |
| Wordmark "COGNEESOL" | Yes — it's typeset, not an image |
| Decorative shapes (rects, ellipses, lines) | Yes — native preset geometries |
| `[IMAGE PLACEHOLDER]` on case study slide | Reproducible as a placeholder; if a real client logo or photo is needed later, it must be supplied separately |

**Nothing in this template requires extraction-and-reembed.** The original `.pptx` contains zero binary media. A full rebuild using Montserrat + the palette above will reproduce the deck faithfully.
