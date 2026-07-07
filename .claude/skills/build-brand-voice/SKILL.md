---
name: build-brand-voice
description: >
  Use this skill to refresh or rebuild Brand_Voice_Guide.md only — without running a full brand
  onboarding. Trigger when: the brand's tone has shifted, a new writing style guide has been
  shared, voice rules are outdated after a rebrand, or the file is missing while other context
  files are still valid. Accepts a URL, uploaded style guide, sample copy, or user-provided
  direction as input. Does NOT touch any other _context\ file.
---

# Build Brand Voice

Refreshes `_context/Brand_Voice_Guide.md` — the tone, voice rules, and writing standards file.
Use this when the brand's communication style has evolved, a formal style guide has been shared,
or the current voice guide no longer reflects how the brand writes.

## Scope — what this skill writes

This skill writes ONE file: `_context/Brand_Voice_Guide.md`.
It does NOT modify `Brand_Context.md`, `Brand_Style.md`, `Brand_Product_Offerings.md`,
`Brand_Growth_Marketing_Context.md`, or `Brand_Insights_Ledger.md`.

## Before starting

Read `_context/Brand_Context.md` to ground yourself in who the brand is and who they write for —
voice rules must match the audience and category, not exist in a vacuum.

If `_context/Brand_Voice_Guide.md` already exists, read it first.
Note which rules are stale or missing — those are the update targets.
Merge and update unless the user asks for a full rewrite.

## Clarify inputs

Ask the user:
1. **Source material:** URL to scrape, uploaded style guide or copy samples, or direct guidance from the user?
2. **What's changed:** New brand voice direction? Rebrand? A specific writing issue to fix?
3. **Sample copy:** Can the user share 2–3 examples of copy they consider "on-brand"? These are the most reliable voice signal.
4. **Rewrite or update?** Targeted section update or full rebuild?

If no material is provided, work from the existing `Brand_Context.md` to infer a coherent voice
for the brand's category and audience, and mark all inferences with `[INFERRED — confirm with client]`.

## Research phase

If a URL is provided:
- Read: homepage hero, About Us, blog posts, case study intros, social bios, ad copy (if visible)
- Identify: sentence length patterns, use of active vs. passive voice, formality level, use of "you" vs. "we", industry jargon vs. plain language, use of data/stats to support claims

If sample copy is provided:
- Analyze 3+ examples for consistent patterns across all the signals above
- Identify what makes each example feel "on-brand" — and abstract the rule behind it

If a formal style guide is uploaded:
- Extract the applicable rules and translate them into the operational format below
- Style guides often describe intent ("warm but professional") — translate that into concrete constraints

## File structure to produce

Write `_context/Brand_Voice_Guide.md` with these sections:

```
# Brand Voice Guide — [Company Name]

## Voice Character
[3–5 adjectives that define the brand's personality in writing — but pair each with a constraint.
Not "professional" alone. Instead: "Professional: we never use slang, but we avoid jargon that
alienates non-specialist readers."]

## Tone Spectrum
[Describe where the brand sits across 3 axes — and where it must not go:
- Formal ←→ Conversational: [position + hard limit]
- Technical ←→ Accessible: [position + hard limit]
- Assertive ←→ Modest: [position + hard limit]]

## Sentence & Paragraph Rules
[Specific structural rules. Examples:
- Max sentence length: [X words — or "two clauses max"]
- Paragraph length: [X sentences max]
- Lead sentence: always a claim or question — never a subordinate clause
- Oxford comma: yes/no
- Numbers: spell out under [X], use numerals above]

## Active Voice Rules
[Is passive voice banned entirely, or only discouraged in certain contexts?
Give a "do this / not that" example pair.]

## Power Verbs (use these)
[List 10–15 action verbs the brand favors in headlines, CTAs, and body copy.]

## Banned Words & Phrases
[List words/phrases to never use — with a brief reason for each.
Examples: "seamless", "leverage", "world-class", "cutting-edge", "synergy"
Add brand-specific bans based on what you found in the source material.]

## POV & Pronouns
[How does the brand address the reader? "You" / "they" / "we"?
Does the brand write in first-person plural ("we help teams") or does it center the reader
("you can reduce costs by X")?]

## Claim Grounding Rules
[Does the brand back every assertion with data? Anecdote? Customer quote?
What's the standard for making a claim without a citation?]

## CTA Style
[What does an on-brand CTA look like? Examples of strong vs. weak CTAs for this brand.
Tone of urgency: assertive / gentle / question-led?]

## Writing Examples
[2–3 "Write this / not that" pairs pulled from or modelled on real brand copy.
These are the most operational part of the file — downstream agents use them directly.]
```

## Quality rules

- Describe voice in constraints, not aspirations. "We write short sentences" is useful. "We write with clarity and impact" is not.
- Every rule must be actionable: a content writer should be able to apply it without asking what it means.
- If the source material is sparse, write conservative rules and mark inferences with `[INFERRED — confirm]`.
- Never describe what the brand "is" generically. Describe what it does and does not write.

## Output

Save to: `_context/Brand_Voice_Guide.md`

After saving, report to the user:
- What sections were updated vs. left unchanged
- Any rules marked `[INFERRED]` that need validation
- Any gaps (e.g., no CTA examples found) that block content agents from using the file immediately
