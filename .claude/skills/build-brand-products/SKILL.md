---
name: build-brand-products
description: >
  Use this skill to refresh or rebuild Brand_Product_Offerings.md only — without running a full
  brand onboarding. Trigger when: a new product or service line has launched, pricing or packaging
  has changed, ICPs have been refined, a new use case has been confirmed, or the file is missing
  while other context files are still valid. Accepts a URL, product brief, sales deck, or
  user-provided specs as input. Does NOT touch any other _context\ file.
---

# Build Brand Products

Refreshes `_context/Brand_Product_Offerings.md` — the service and product inventory file
covering capabilities, buyer personas, pain points, and use cases. Use this when product lines
have changed, new services have launched, or ICP definitions need updating.

## Scope — what this skill writes

This skill writes ONE file: `_context/Brand_Product_Offerings.md`.
It does NOT modify `Brand_Context.md`, `Brand_Voice_Guide.md`, `Brand_Style.md`,
`Brand_Growth_Marketing_Context.md`, or `Brand_Insights_Ledger.md`.

## Before starting

Read `_context/Brand_Context.md` to ground the product work in the brand's overall positioning,
target verticals, and known ICPs — product descriptions must align with the established framing.

If `_context/Brand_Product_Offerings.md` already exists, read it first. Identify which product
lines are outdated, newly added, or missing. Merge and update unless the user requests a full rewrite.

## Clarify inputs

Ask the user:
1. **Source material:** URL (product pages, pricing page), uploaded sales deck, product brief, or direct input?
2. **Scope of change:** New product added? Existing product repositioned? ICP update only? Full refresh?
3. **Pricing visibility:** Is pricing public? Should it be included or marked `[INTERNAL — do not publish]`?
4. **Proof points:** Are there customer case studies, ROI metrics, or testimonials available to include?

## Research phase

If a URL is provided:
- Scrape: all product/service pages, pricing page, use case pages, case study pages
- For each product/service, extract:
  - Product name and one-line description
  - Core capabilities (what it does, not just what it "enables")
  - Named target buyer roles and company profiles
  - Pain points the product explicitly solves (use the language on the page)
  - Differentiators claimed (vs. doing nothing, vs. alternatives, vs. DIY)
  - Proof points: named customers, metrics, case study outcomes

If a deck or product brief is uploaded:
- Extract the same fields from the uploaded material
- Note any discrepancies between the deck and the live website (mark them for user confirmation)

## File structure to produce

For each product or service line, write a dedicated block. Repeat the block for every offering.

Write `_context/Brand_Product_Offerings.md` with this structure:

```
# Brand Product Offerings — [Company Name]

---

## Product/Service Line: [Name]

### What It Is
[2–3 sentences. What this product does and what category it belongs to.
Concrete capability description — not a tagline. Name the mechanism, not just the outcome.]

### Core Capabilities
- [Specific feature or capability — one per bullet]
- [...]
- [...]

### Target Buyer

| Field | Details |
|-------|---------|
| Primary Role | [Job title(s) of the person who buys or uses this] |
| Company Profile | [Size, industry, maturity stage — be specific] |
| Buying Trigger | [What event causes them to start evaluating this?] |
| Key Pain Point | [The specific operational problem they're trying to solve] |
| Decision Criterion | [What does "good enough to buy" look like for them?] |

### Pain Points Solved
- **[Pain point label]:** [One sentence on how this product specifically addresses it]
- [...]

### Key Differentiators
- [What makes this distinct from the closest alternative — be specific]
- [...]

### Proof Points
- [Customer quote, ROI metric, or case study outcome — with source if public]
- Mark unavailable proof points as: [TBD — request from client]

### Pricing / Packaging
[Visible pricing tiers, model (per seat / per usage / retainer), or mark as:
[INTERNAL — do not use in public-facing copy] if confidential]

---
```

Repeat the block above for every product or service line found. If multiple products exist,
add a summary table at the top:

```
## Product Portfolio Summary

| Product/Service | Primary ICP | Core Use Case | Category |
|----------------|------------|--------------|---------|
| [Name] | [Role @ company type] | [What it solves] | [Category] |
| [...] | [...] | [...] | [...] |
```

## Quality rules

- Describe capabilities in operational terms, not marketing claims. "Automates invoice matching
  across ERP systems" is useful. "Transforms your finance operations" is not.
- Every ICP entry must name a specific role (not "decision makers") and a specific pain point
  (not "inefficiency"). Vague ICPs break downstream copy agents.
- Mark any proof point that is not publicly verified as `[ASSUMPTION — confirm with client]`.
- If pricing is not public, include the pricing model (per seat, retainer, etc.) but mark dollar
  amounts as `[INTERNAL]`.
- If a product was on the old file but not found in source material, flag it:
  `[NOT FOUND IN SOURCE — confirm if still active]`

## Output

Save to: `_context/Brand_Product_Offerings.md`

After saving, report to the user:
- Which product lines were updated, added, or flagged as unconfirmed
- Any `[TBD]` proof points that need client input before copy agents can use them
- Any ICPs that are still vague and need sharpening before content work begins
