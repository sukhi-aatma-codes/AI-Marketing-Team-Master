---
name: copy-editing
description: >
  Use this skill when the user wants to edit, review, refresh, or improve existing marketing
  copy rather than write something new. Trigger on phrases like "edit this copy", "review my
  copy", "polish this", "tighten this up", "this reads awkwardly", "clean up this text", "too
  wordy", "sharpen the messaging", "refresh this content", "this page is outdated", or "content
  audit". For writing new copy from scratch, see blog-writer, lp-builder, social-copy, or
  email-copy instead — this skill edits copy that already exists.
---

# Copy Editing

Systematically improves existing marketing copy through focused editing passes, preserving the
core message rather than rewriting from scratch. Good copy editing enhances; it doesn't replace.

## Before starting

Read `_context/Brand_Voice_Guide.md` every time — every edit gets checked against the brand's
actual tone rules and banned words, not generic "good writing" instincts. If the copy being
edited references services or proof points, also read `_context/Brand_Product_Offerings.md` to
verify claims are accurate, not just well-written.

## Core philosophy

- Don't change the core message — enhance it
- Multiple focused passes beat one unfocused review
- Each edit needs a clear reason, traceable to a specific sweep
- Preserve the author's voice while improving clarity

## The Seven Sweeps

Edit through seven sequential passes, each focused on one dimension. After each sweep, loop
back to confirm earlier sweeps weren't compromised by the new edits.

### Sweep 1 — Clarity
Can the reader understand what's being said? Check: confusing sentence structures, unclear
pronoun references, jargon, ambiguous statements, missing context. Read through once marking
problem areas without correcting yet, then recommend specific edits.

### Sweep 2 — Voice and Tone
Is the copy consistent in how it sounds, and does it match `Brand_Voice_Guide.md`? Check:
shifts between formal/casual, inconsistent personality, jarring mood changes, word choices that
don't match brand vocabulary or violate the banned-words list. Read aloud to catch
inconsistencies a silent read misses. **Return to Sweep 1** after editing.

### Sweep 3 — So What
Does every claim answer "why should I care?" For every statement, literally ask "so what?" — if
the copy doesn't answer with a deeper benefit, it needs a bridge.

❌ "Our platform uses AI-powered analytics"
✅ "Our AI-powered analytics surface insights you'd miss manually — so you can decide faster"

**Return to Sweeps 2, then 1.**

### Sweep 4 — Prove It
Is every claim supported with evidence? Check for unsubstantiated claims, missing social proof,
"best"/"leading" without evidence. **Every proof point added during this sweep must come from
`_context/Brand_Product_Offerings.md` or a verifiable external source — never invented to make
a sweep pass.** If a claim needs proof that doesn't exist in `_context\`, flag it
`[DRAFT — confirm this data point before publishing: ...]` rather than fabricating a stat or
quote. This is the same no-invented-proof-points rule that governs every other skill in this
workspace. **Return to Sweeps 3, 2, 1.**

### Sweep 5 — Specificity
Is the copy concrete enough to be compelling? Replace vague language with numbers, timeframes,
examples:

| Vague | Specific |
|-------|----------|
| Save time | Save 4 hours every week |
| Many customers | 2,847 teams |
| Fast results | Results in 14 days |
| Great support | Response within 2 hours |

Only add specificity that's real — a fabricated number is a Sweep 4 violation, not a Sweep 5 win.
**Return to Sweeps 4, 3, 2, 1.**

### Sweep 6 — Heightened Emotion
Does the copy make the reader feel something? Check for flat, purely informational language;
pain points stated but not felt; aspirations named but not evoked. Paint the "before" state
vividly, use sensory language, ask questions that prompt reflection — without manufacturing
emotion that misrepresents the brand's actual tone (`Brand_Voice_Guide.md` governs how far this
can go; a clinical, technical brand voice shouldn't suddenly read as breathless). **Return to
Sweeps 5, 4, 3, 2, 1.**

### Sweep 7 — Zero Risk
Have all barriers to action been removed? Check friction near CTAs, unanswered objections,
missing trust signals, unclear next steps. Only cite risk reducers (guarantees, trial terms,
cancellation policy) that are real and confirmed — never invent a guarantee that doesn't exist
to make copy more persuasive. **Return through all six previous sweeps one final time.**

## Expert panel scoring (for high-stakes copy)

After the Seven Sweeps, run a multi-persona review for landing pages, launch emails, or sales
copy — a single perspective misses things a panel catches.

1. Assemble 3-4 expert personas relevant to the copy type (e.g. for a landing page: conversion
   copywriter, UX writer, the target ICP persona, brand strategist)
2. Each persona scores 1-10 on their area of expertise with specific critiques, not just a number
3. Revise based on the lowest-scoring areas first
4. Re-score after revisions — iterate until every persona scores 7+, average 8+

| Score | Meaning |
|-------|---------|
| 9-10 | Publish-ready |
| 7-8 | Strong, minor tweaks only |
| 5-6 | Functional but has clear gaps — needs another pass |
| 3-4 | Significant issues — major revision needed |
| 1-2 | Fundamentally broken — rethink approach |

**When to run this:** always for launch copy and high-traffic landing pages; recommended for
email sequences and ad copy; optional for blog posts and social content; skip for quick edits.

## Quick-pass checks (when a full seven-sweep isn't warranted)

**Cut:** very/really/extremely (weak intensifiers), just/actually/basically (filler), "in order
to" (use "to"), unnecessary "that."

**Replace:** utilize→use, leverage→use, facilitate→help, robust→strong, seamless→smooth,
cutting-edge→new/modern, delve→look/investigate, testament→proof, revolutionize→improve/change — unless one of these terms is explicitly part of the brand's
established vocabulary in `Brand_Voice_Guide.md`.

**AI artifacts:** Remove generic AI transitions (e.g. *In conclusion, It is important to note, Furthermore, It is worth noting*) and structural templates.

**Punctuation:** Ban all em dashes (—) used for dramatic parenthetical statements (overused by AI models). Replace them with standard commas, colons, parentheses, or break the clause into a new sentence.

**Watch for:** unnecessary adverbs, passive voice, nominalizations ("make a decision" → "decide").

**Structure:** one idea per sentence, vary sentence length, front-load important information,
short paragraphs (2-4 sentences for web), strong opening sentences.

## Content refresh mode

Copy editing isn't only for new drafts — existing pages decay: outdated stats, stale examples,
drifted voice as `Brand_Voice_Guide.md` evolves. Use this mode when traffic is declining, data
is stale, or the underlying product/offering has changed. Run the same Seven Sweeps, with
particular attention to Sweep 4 (Prove It) — anything that read as current six months ago may
now need a `[DRAFT — confirm before publishing]` flag.

## Common copy problems & fixes

| Problem | Symptom | Fix |
|---------|---------|-----|
| Wall of features | Lists what the product does, not why it matters | Add "which means…" after each feature |
| Corporate speak | "Leverage synergies to optimize outcomes" | Ask "how would a human say this?" |
| Weak opening | Starts with company history or vague statements | Lead with the reader's problem |
| Buried CTA | The ask comes too late or isn't clear | Make it obvious, early, repeated |
| No proof | "Customers love us" with no evidence | Add specific testimonials/numbers — or flag `[DRAFT]` |
| Generic claims | "We help businesses grow" | Specify who, how, by how much |
| Mixed audiences | Copy tries to speak to everyone | Pick one ICP and write directly to them |

## Working process

1. Run a sweep and present findings — show what was found and why it's an issue
2. Recommend specific edits, don't just flag problems
3. Present the revised copy for the user's review — they own final decisions
4. After each round of edits, re-check earlier sweeps per the backward-check instructions above
5. Repeat until a full sweep finds no new issues

## Output

Produce an edit report containing: sweep-by-sweep findings, the revised copy in full, and any
`[DRAFT]`-flagged items needing confirmation. Save alongside the source content's natural
location — if the original lives in `output\pages\`, `output\social\`, `output\email\`, `output\ads\`, or `output\pr\`, save the
edit report to that same folder. If the source location isn't obvious, ask the user.

Filename: `edit-<topic>-<yyyy-mm-dd>.md`

## Quality checklist

- [ ] All seven sweeps completed, with backward re-checks after each
- [ ] Every proof point added or kept traces to `_context\` or is flagged `[DRAFT]` — none invented
- [ ] Voice/tone changes checked against `Brand_Voice_Guide.md`, not generic style preference
- [ ] Expert panel scoring run for high-stakes copy (landing pages, launch emails, sales copy)
- [ ] Revised copy presented in full, not just a list of suggested changes
- [ ] Edit report saved to the correct output folder matching the source content type

## Related skills

- **`blog-writer`**, **`lp-builder`**, **`social-copy`**, **`email-copy`**, **`ad-creative`** —
  for writing new copy from scratch; use this skill to edit the result afterward
- **`build-brand-voice`** — if edits keep surfacing the same voice drift, the
  `Brand_Voice_Guide.md` itself may need refreshing rather than every piece individually
