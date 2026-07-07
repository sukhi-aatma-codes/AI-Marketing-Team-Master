---
name: sample-archive-index
description: >
  Use this skill when the user drops a large batch of raw brand materials into _samples\ (20+
  files — ad archives, old decks, social creative, copy sheets) and the next step needs to know
  what's there before reading anything in full. Trigger on requests like "index everything in
  _samples", "I just dropped a folder of old ads, build an index", or run it automatically as a
  first step by brand-onboarder, build-brand-style, and build-brand-style-reference whenever
  _samples\ is non-empty. Produces a cheap triage manifest only — it does not analyze or
  synthesize content itself; that's the job of the deeper skills it routes to.
---

# Sample Archive Index

Scans `_samples\` and produces a one-entry-per-file manifest so downstream skills can decide
what's worth a full read instead of blind-scanning a large folder. This is a triage layer, not
an analysis layer — it classifies and routes, it does not extract brand truth.

## Workflow

### Step 1 — Scan
Recursively list every file under `_samples\`, excluding `_reference-examples\` (those are
worked examples, never live input — see that folder's own README).

### Step 2 — Classify each file
For each file, determine:
- **Type**: deck (`.pptx`/`.key`/`.pdf` slides), image creative (social graphics, ad visuals,
  banners), document (style guide, brief, copy sheet), other
- **Likely use**: which downstream skill this should feed —
  - Decks with visual design content → `build-brand-style` (deck-extraction workflow)
  - Image creative (social posts, ad visuals, banners) → `build-brand-style-reference`
  - Style guides, brand docs → `build-brand-style` or `build-brand-context` depending on content
  - Copy sheets, old ad text, sales decks with messaging → `build-brand-voice` or
    `build-brand-products` depending on content
- **One-line description**: what the file actually contains (not a guess from the filename
  alone — open it enough to confirm)

### Step 3 — Write the manifest
Group entries by likely use so a downstream skill can scan straight to its relevant section.

## Output structure (`.md`)

Save as `_samples\INDEX.md`:

```
# Sample Archive Index
Last updated: [yyyy-mm-dd]
Files scanned: [N]

## Visual Style Sources (→ build-brand-style-reference)
| File | Type | Description |
|------|------|--------------|
| social-creatives/banner-01.png | image | LinkedIn banner, navy background, constellation motif |

## Deck Style Sources (→ build-brand-style)
| File | Type | Description |
|------|------|--------------|
| pitch-deck-2024.pptx | deck | 14-slide sales deck, dark theme, red accent numerals |

## Voice / Messaging Sources (→ build-brand-voice / build-brand-products)
| File | Type | Description |
|------|------|--------------|
| old-ad-copy.docx | document | 12 past Google Ads headlines and descriptions |

## Unclassified
| File | Type | Description |
|------|------|--------------|
| [file] | [type] | [why it didn't fit a category above] |
```

## Quality rules

- This skill never writes brand truth — it does not populate any `_context\` file. Its only
  output is the index.
- Re-running this skill should refresh the manifest for new or changed files, not duplicate
  entries for files already indexed and unchanged.
- If a file can't be classified confidently, put it in "Unclassified" with a note rather than
  guessing — a wrong route wastes the downstream skill's effort.
- Skip `_reference-examples\` entirely — those are worked examples, never live brand input.

## Output

Save to: `_samples\INDEX.md`

After saving, report to the user a one-line summary per category (e.g. "12 visual style
sources, 3 deck sources, 5 voice/messaging sources, 1 unclassified") and recommend which
downstream skill(s) to run next.
