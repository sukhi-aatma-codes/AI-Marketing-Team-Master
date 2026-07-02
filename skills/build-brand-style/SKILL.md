---
name: build-brand-style
description: >
  Use this skill to refresh or rebuild Brand_Style.md only — without running a full brand
  onboarding. Trigger when: visual identity has been updated (new colors, fonts, logo), a formal
  brand style guide has been shared, or Brand_Style.md is missing while other context files are
  still valid. Accepts a URL, uploaded style guide, image samples, or user-provided specs as input.
  Does NOT touch any other _context\ file.
---

# Build Brand Style

Refreshes `_context/Brand_Style.md` — the visual identity file covering colors, typography,
grid, imagery style, and logo rules. Use this when the brand has rebranded, a new style guide
has been shared, or the visual rules need updating before a design sprint.

## Scope — what this skill writes

This skill writes ONE file: `_context/Brand_Style.md`.
It does NOT modify `Brand_Context.md`, `Brand_Voice_Guide.md`, `Brand_Product_Offerings.md`,
`Brand_Growth_Marketing_Context.md`, or `Brand_Insights_Ledger.md`.

## Before starting

Read `_context/Brand_Context.md` to understand the brand's category and audience — visual style
must be appropriate to the market (B2B enterprise vs. B2C consumer vs. tech startup all have
different visual conventions).

If `_context/Brand_Style.md` already exists, read it first. Identify which sections are
outdated or missing. Merge and update unless the user requests a full rewrite.

## Clarify inputs

Ask the user:
1. **Source material:** URL to inspect, uploaded style guide (PDF, Figma export, image files), or user-provided specs?
2. **What's changed:** Full rebrand? Color update only? New typography?
3. **Asset access:** Are logo files, brand guidelines PDFs, or Figma/Canva links available?
4. **Priority use cases:** What will this style file primarily drive — social graphics, landing pages, ad creatives, presentations?

## Research phase

If a URL is provided:
- Inspect: homepage, product pages, and blog for visual signals
- Extract: dominant background colors, primary accent colors, button/CTA colors, link colors
- Identify: font families used in headings and body (visible via page source or font inspector)
- Note: image treatment style (photography vs. illustration vs. abstract), use of whitespace,
  border radius on UI elements (sharp/square vs. rounded), icon style (line vs. filled)

If a style guide or images are uploaded:
- Extract all defined values (hex codes, font names, type scale, spacing rules)
- Note any usage rules (logo clearspace, color combinations to avoid, dark mode variants)

If a presentation deck (`.pptx` or similar) is provided as a style source, extract at the
**structural level**, not by visually skimming rendered slides:
- **Colors:** Pull exact hex codes directly from the file's underlying slide XML (unzip the
  `.pptx` and inspect `ppt/slides/slideN.xml` and `ppt/theme/theme1.xml`), ordered by frequency
  of use. Do not approximate from a rendered screenshot when the source XML is available.
- **Typography:** Identify every typeface referenced in the XML and its usage count; derive the
  size hierarchy (display/hero/heading/body/caption) from the font-size attributes actually used.
- **Layout patterns:** Catalog each distinct slide layout as a named pattern (e.g. "title slide,"
  "two-column insight," "process timeline") with its composition described concretely enough to
  rebuild.
- **Decorative vocabulary:** List the shape primitives used (rectangles, ellipses, lines, icons,
  photography) and where they recur (e.g. wordmark position, footer treatment).
- **Reproducibility verdict:** State plainly what's rebuildable from this spec alone (native
  shapes, type, color) vs. what requires extracting embedded media (logos, photos) from the
  original file.
- See `_samples/_reference-examples/cogneesol-deck-analysis.md` for the expected depth and
  format of this extraction — it is a worked example, not data for the active brand.
- For complex decks, you may write this full extraction as a standalone working file in
  `_samples\` before distilling it into `_context/Brand_Style.md`'s structured sections below —
  optional for simple decks, useful for traceability on larger ones.

If neither is available:
- Work from the brand's name, category, and ICP (from `Brand_Context.md`) to propose a
  coherent, professional palette and typeface appropriate for the market
- Mark all proposed values as `[PROPOSED — confirm with client]`

## File structure to produce

Write `_context/Brand_Style.md` with these sections:

```
# Brand Style Guide — [Company Name]

## Color Palette

### Primary Colors
| Name | Hex | Usage |
|------|-----|-------|
| [Color name] | #XXXXXX | [Primary CTA buttons, links, key accents] |
| [Color name] | #XXXXXX | [Secondary brand color — headers, dividers] |

### Supporting Colors
| Name | Hex | Usage |
|------|-----|-------|
| [Color name] | #XXXXXX | [Background fills, section dividers] |
| [Color name] | #XXXXXX | [Body text] |
| [Color name] | #XXXXXX | [Light background, cards] |

### Accessibility Notes
[Confirm primary text/background combinations meet WCAG AA contrast (4.5:1 for body text).
Flag any combinations that fail.]

## Typography

### Typeface Stack
| Role | Font Family | Weight(s) | Fallback |
|------|------------|-----------|---------|
| Display / H1 | [Font name] | [700, 800] | [serif/sans-serif] |
| Heading / H2–H4 | [Font name] | [600, 700] | [serif/sans-serif] |
| Body | [Font name] | [400, 500] | [serif/sans-serif] |
| Caption / Meta | [Font name] | [400] | [serif/sans-serif] |

### Type Scale (Desktop)
| Level | Size | Line Height | Weight |
|-------|------|------------|--------|
| H1 | [Xpx / Xrem] | [X] | [X] |
| H2 | [Xpx / Xrem] | [X] | [X] |
| H3 | [Xpx / Xrem] | [X] | [X] |
| Body | [Xpx / Xrem] | [X] | [X] |
| Caption | [Xpx / Xrem] | [X] | [X] |

### Typography Rules
[Max line length for body text, alignment rules (left-aligned body, centered headlines?),
use of all-caps, italic, or bold for emphasis.]

## Logo Usage

### Variants
[List available logo variants: full color, reversed (white), dark, icon-only]

### Clearspace
[Minimum whitespace around the logo — expressed as a multiple of a logo element, e.g., "1× the height of the wordmark on all sides"]

### Prohibited Uses
[Don't stretch, recolor, add drop shadow, use on a conflicting background, etc.]

## Imagery Style

### Photography Direction
[Documentary / aspirational / product-focused? People or abstract? Warm/cool tones?
Include or avoid: stock-photo aesthetic, faces, office settings, etc.]

### Illustration Style
[Flat / isometric / line-art / none? Color range within palette?]

### Icon Style
[Line icons / filled icons / mixed? Stroke weight? Rounded or sharp corners?]

## Layout & Grid Principles

### Spacing System
[Base unit (e.g., 8px grid). Common spacing increments.]

### Border Radius
[Sharp (0px) / subtle (4px) / rounded (8–12px) / pill (9999px)?]

### Shadow / Elevation
[No shadows / subtle drop shadows / card elevation system?]

### Content Max Width
[Max container width for web: e.g., 1200px, 1440px]

## Platform-Specific Notes

### Social (LinkedIn, Instagram, X)
[Dominant color usage, safe zones for text, aspect ratio preferences]

### Paid Display Ads
[Brand color dominance rules, button style, headline text treatment]

### Presentations
[Slide background: white / brand primary / dark mode? Header treatment.]
```

## Quality rules

- Hex codes must be exact — do not approximate. If a hex cannot be extracted, use `[TBD — hex needed]`.
- Font names must be the exact Google Fonts or licensed font name — not "a sans-serif that looks like Helvetica".
- Mark any value that is proposed (not extracted from source) with `[PROPOSED — confirm with client]`.
- Platform-specific notes are mandatory — downstream skills (`social-creative-designer`, `ad-creative`) consume this section directly.

## Output

Save to: `_context/Brand_Style.md`

After saving, report to the user:
- What was extracted from source vs. proposed
- Any `[TBD]` or `[PROPOSED]` fields that need confirmation before design work can begin
- Any accessibility concerns flagged in the color palette
