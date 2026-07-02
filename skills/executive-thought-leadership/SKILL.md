---
name: executive-thought-leadership
description: >
  Use this skill whenever the user wants to draft thought leadership articles, LinkedIn posts,
  opinion pieces (op-eds), speaking briefs, or panel talking points for company executives.
  Trigger on requests like "write a LinkedIn article for our CEO", "draft a thought leadership
  piece on Y", "write an op-ed about industry trends for our founder", or "create talking points
  for a panel discussion". Handles tone calibration, executive voice matching, and trend-focused
  storytelling.
---

# Executive Thought Leadership

Drafts industry-leading thought leadership content (articles, social posts, op-eds, panel scripts)
on behalf of company executives. Blends corporate expertise with human insight, personal anecdote,
and visionary perspective. Produces a structured `.md` draft and a formatted Word document (`.docx`) in `output/pr/`.

## Before starting

Read these context files every time — do not rely on prior session memory:
- `_context/Brand_Context.md` — company mission, target industry verticals, market presence
- `_context/Brand_Voice_Guide.md` — specific tone rules for executives (executive voice is typically more conversational, opinionated, first-person, and storytelling-driven than the main company voice)

## Clarify inputs first

Confirm with the user:
1. **Executive Profile:** Who is the author? (CEO, founder, CTO — their name, title, and specific areas of expertise/personality traits).
2. **Topic & Core Message:** What industry trend, problem, or vision is the piece addressing? What is their unique point of view (POV)?
3. **Target Platform / Format:** LinkedIn article, LinkedIn post, trade publication (e.g. Forbes Tech Council), op-ed, or speaking notes.
4. **Anecdote / Story:** Any personal experiences, client stories, or company lessons they want to reference.
5. **Call to Action:** Soft, industry-level CTA (e.g. "We need to change how we think about X", not "Buy our software").

If the user's request makes these inputs clear, skip asking and proceed.

## Workflow

### Step 1 — Executive Stance & Tone Calibration
Identify the executive's voice and strategic stance:
- **Founder/CEO:** Visionary, leadership-focused, story-driven, strategic, industry-advocate.
- **CTO/Technical Leader:** Analytical, future-focused, problem-solving, developer-empathetic, detail-oriented.
- Use first-person pronoun perspective ("I", "we", "our team").
- Inject specific experience anchors: "Over the past 15 years in [industry], I've seen..."

### Step 2 — Storytelling & Narrative Structure
Build a compelling, non-salesy narrative arc:
- **The Hook:** A bold statement, personal reflection, or contrarian view.
- **The Shift:** Explain how the industry is changing or why the status quo is failing.
- **The Lesson:** Introduce 3–4 actionable insights or principles derived from experience (not product pitches).
- **The Vision:** Detail what a better future looks like and how the industry can build it.
- **The Call to Action:** Challenge the reader, ask a question, or recommend a shift in perspective.

### Step 3 — Draft the Content
Write the article in full, ensuring it remains educational and inspiring. If drafting supporting social posts, write 2–3 variants testing different hook angles.

## Output structure (`.md`)

Save as `output/pr/thought-leadership-<exec>-<date>.md` with this exact structure:

```
# Thought Leadership: [Article Title]
Author: [Executive Name], [Title]
Topic: [Story POV / Trend]
Target Format: [e.g. LinkedIn Article / Op-Ed]
Date: [yyyy-mm-dd]

## Executive Persona Profile
- **Tone parameters:** [e.g. Conversational, highly analytical, first-person narrative]
- **Key positioning focus:** [e.g. Champion of operations efficiency / cybersecurity compliance]

---

## 1. Master Article Copy
*Word Count: [Number] | Target Publication: [Forbes/Medium/LinkedIn]*

# [Headline - Visionary and outcome-led]

[Lead Hook: Personal story, bold metric, or contrarian hook in first person.]

[Problem framing: Why standard practices are holding companies back. Map this to the target ICP's operational pain points without selling the brand.]

[Subsection: H2 - Principle 1 / Actionable Insight]
[Paragraph 1-2 details]

[Subsection: H2 - Principle 2 / Actionable Insight]
[Paragraph 1-2 details]

[Subsection: H2 - Principle 3 / Actionable Insight]
[Paragraph 1-2 details]

[Conclusion: The Vision. Challenge the industry, summarize key points, and end on a soft CTA.]

---

## 2. Supporting Social Promotion Posts
*Designed for the executive's personal LinkedIn/Twitter profiles to drive engagement to the article.*

### Social Variant A: Story-led Hook
[First-person narrative hook. Bulleted takeaways. CTA link to article.]

### Social Variant B: Question-led Hook
[Direct question to peers/ICP. Key insight from article. CTA link.]

---

## 3. Background Notes & confirmed Anecdotes
- **Verified stats used:** [Citations and links]
- **Client references:** [Confirmed/anonymized details]
```

## Rich deliverable

After saving the `.md`, invoke `document-skills:docx` to export as a Word document for executive review and editing.
Save as `output/pr/thought-leadership-<exec>-<date>.docx`.

## Quality checklist

- [ ] Written in the first person ("I", "we") from the perspective of the named executive
- [ ] Stance is visionary and opinionated, not a neutral corporate summary
- [ ] Zero direct sales pitches for the brand's services/products (rely on soft positioning)
- [ ] At least one personal anecdote or company lesson included
- [ ] Supporting social media posts included for promo
- [ ] `.md` and `.docx` saved to `output/pr/`
