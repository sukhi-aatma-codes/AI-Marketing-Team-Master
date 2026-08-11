---
name: decision-council
description: >
  Use this skill to pressure-test a single high-stakes marketing decision from multiple
  adversarial perspectives before it gets locked in — pricing calls, positioning angles,
  channel bets, offer structure, market entry choices, or crisis-response stances. Trigger
  on explicit requests like "council this", "pressure-test this", "war room this", or
  "stress-test this decision". Also trigger on a genuine fork-in-the-road question with
  real stakes and no obvious right answer ("should we do X or Y", "which of these three
  angles is strongest", "am I wrong to pivot from X to Y"). Do NOT trigger on requests for
  content creation, factual lookups, single-right-answer questions, or routine choices with
  low downside (e.g. "should this email subject line be shorter" is not a council question).
  This skill does not produce marketing deliverables itself — it evaluates a decision that
  another skill or agent has already scoped (e.g. a campaign-strategist brief, an
  abm-account-plan tier call, a crisis-response stance).
---

# Decision Council

Runs one decision through five independent advisors, each committed to a different
thinking style, then has them anonymously review each other's arguments before a
chairman synthesizes a final verdict. The value is the structured disagreement — a
single continuous train of reasoning (which is what every other skill in this workspace
produces) tends to converge early and miss the angle nobody on the team thought to raise.

Methodology adapted from Andrej Karpathy's LLM Council concept (multiple models,
anonymized peer review, chairman synthesis) — implemented here with sub-agents instead
of separate models.

## When to run this

Good candidates: a pricing decision with real revenue risk, choosing between two
positioning angles, deciding whether to enter a new segment, picking a crisis-response
stance, validating an ABM tier assignment for a flagship account, deciding whether a
campaign bet is worth the spend.

Bad candidates: anything with one correct answer, routine copy choices, content creation
requests, decisions already made where the user just wants the deliverable written.

If the request doesn't clearly name a decision with two or more real options and real
stakes, ask one clarifying question before proceeding rather than guessing.

## Before starting

Read whatever `_context\` files are relevant to the decision at hand — do not guess brand
specifics and do not carry over assumptions from a different brand or a prior session:

- `_context/Brand_Growth_Marketing_Context.md` — funnel stage, channel goals, targets
- `_context/Brand_Product_Offerings.md` — relevant service line, ICP, pricing context
- `_context/Brand_Insights_Ledger.md` — validated personas, objections, past performance
  patterns relevant to this call
- The specific brief, plan, or manifest the decision came from, if one exists (e.g. a
  campaign brief, an ABM account plan, a webinar plan)

Spend no more than a minute on this. The goal is enough grounding that advisors argue
from real constraints instead of generic takes — not an exhaustive context dump.

## Workflow

### Step 1 — Frame the question

Combine the user's raw question with the context gathered above into one neutral framed
question that:
1. States the core decision and the real options on the table
2. Includes the relevant brand/campaign context (audience, funnel stage, numbers, prior
   results) that bears on the call
3. States what's at stake — why getting this wrong is costly

Do not add your own opinion or steer the framing. If the question is too vague to frame
("council this: our strategy"), ask one clarifying question, then proceed. Save the framed
question — it goes in the transcript.

### Step 2 — Convene the council (5 sub-agents, single message, parallel)

Spawn all five advisors as `general-purpose` agents via the Agent tool, all in one message
so they run in parallel. Each gets the framed question and one assigned lens:

1. **The Contrarian** — assumes the plan has a hidden flaw and hunts for it. Not a
   pessimist by disposition — plays the role of the person who asks the question everyone
   else is avoiding.
2. **The First Principles Thinker** — ignores the surface question and asks what problem
   is actually being solved. Will sometimes conclude the question itself is wrong.
3. **The Expansionist** — looks for the upside nobody scoped. What's this worth if it
   works better than planned? What adjacent opportunity is being left on the table?
4. **The Outsider** — has no context on the brand, the industry, or prior history. Reacts
   only to what's in the framed question. Exists to catch what's obvious to the team but
   opaque to a cold prospect or new hire.
5. **The Executor** — cares only about whether this can actually ship and what the first
   concrete step is. Flags ideas that sound right but have no clear Monday-morning action.

Each advisor prompt should instruct: respond independently, do not hedge, do not try to
be balanced, argue the assigned lens as strongly as the evidence allows, 150–300 words,
no preamble.

### Step 3 — Peer review (5 sub-agents, single message, parallel)

Collect the five responses. Anonymize them as Response A–E in randomized order so no
reviewer knows which advisor said what. Spawn five new `general-purpose` agents (one per
original advisor persona), each given all five anonymized responses and three questions:

1. Which response is strongest, and why?
2. Which response has the biggest blind spot, and what is it?
3. What did all five responses miss that the council should have caught?

Cap each review at 200 words, direct, referencing responses by letter.

### Step 4 — Chairman synthesis

One final agent call gets everything: the framed question, all five de-anonymized advisor
responses, and all five peer reviews. It produces the verdict in this exact structure:

```
## Where the Council Agrees
[Points multiple advisors converged on independently — high-confidence signals]

## Where the Council Clashes
[Genuine disagreements, both sides stated, why reasonable advisors differ]

## Blind Spots the Council Caught
[What only surfaced through peer review — not visible in any single response]

## The Recommendation
[A direct, specific recommendation — never "it depends." The chairman may side with a
minority advisor if the reasoning is strongest, and should say so explicitly.]

## The One Thing to Do First
[A single concrete next action — not a list]
```

### Step 5 — Save outputs

**HTML report** — self-contained, inline CSS, clean/scannable:
1. The framed question at the top
2. The chairman's verdict, prominent
3. A simple agree/clash visual (grid or spectrum showing where advisors aligned/diverged)
4. Collapsed-by-default sections for each advisor's full response
5. Collapsed-by-default section for peer review highlights
6. Footer with date and what was counciled

Save as `output/reports/decision-council-<topic-slug>-<yyyy-mm-dd>.html`

**Markdown transcript** — framed question, all five advisor responses, all five peer
reviews (anonymization mapping revealed), full chairman synthesis.

Save as `output/reports/decision-council-<topic-slug>-<yyyy-mm-dd>.md`

If the decision belongs to a named campaign with a manifest at
`output\campaigns\<campaign-slug>.md`, append a row for both files (date, asset, type,
path, produced by, status).

## Quality checklist

- [ ] Framed question is grounded in real `_context\` facts, not invented brand details
- [ ] All 5 advisors spawned in parallel (single message), not sequentially
- [ ] Peer review is genuinely anonymized — reviewers never see advisor names
- [ ] Chairman verdict follows the exact 5-section structure and gives a real answer, not
      "it depends"
- [ ] The one first action is a single concrete step, not a list
- [ ] Both `.html` and `.md` saved to `output/reports/`
- [ ] Campaign manifest updated if this decision belongs to a named campaign
