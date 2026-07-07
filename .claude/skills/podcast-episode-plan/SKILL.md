---
name: podcast-episode-plan
description: >
  Use this skill whenever the user wants to prepare a plan, script, outline, or research briefing for a
  podcast episode. Trigger on requests like "plan our next podcast episode with Guest X", "write a script
  for our upcoming solo podcast on Y", "create a research briefing sheet for our host", or "outline interview
  questions for a guest on automation". Coordinates guest profiling, episode timing segments, open-ended questions,
  and host scripting.
---

# Podcast Episode Planner

Creates detailed guest research dossiers, structured interview blueprints, and high-impact episode scripts for hosts. Produces a structured outline in `.md` and a formatted Word document (`.docx`) in `output/podcasts/` for easy sharing with hosts and guests.

## Before starting

Read these context files every time — do not rely on prior session memory:
- `_context/Brand_Voice_Guide.md` — conversational tone rules (podcast outlines and script segments must sound natural, professional, and engaging when spoken aloud).
- `_context/Brand_Product_Offerings.md` — service lines and value propositions (essential to align interview themes with soft brand opportunities).
- `_context/Brand_Insights_Ledger.md` — Section 9 (Podcast Intelligence) and Section 1 (Buyer Personas & Objections) for topic resonance and audience alignment.

## Clarify inputs first

Confirm with the user (unless specified):
1. **Episode Format:** Interview with a guest, solo host episode, or co-hosted panel discussion.
2. **Guest Name & Profile:** Who is the guest? (Name, title, company, bio, areas of expertise, links to recent articles).
3. **Episode Topic / Goal:** What is the primary theme? What value should the listener walk away with?
4. **Target Audience (ICP):** Who is the primary listener?
5. **Call to Action:** What is the soft CTA for the episode? (e.g. Subscribe, visit landing page, download checklist).
6. **Host Name & Bio:** (If not already documented in `Brand_Context.md`).

## Scripting & Question Principles

1. **Write for the Ear:** Text intended to be read aloud must use short sentences, contractions ("don't", "we're"), and natural speech cadences. Avoid long, complex passive sentences.
2. **Value-First Hook:** The intro script must capture attention within the first 30 seconds. Do not start with dry definitions; start with a bold quote, a massive industry challenge, or a compelling tease of what the guest will reveal.
3. **Open-Ended, Non-Obvious Questions:** Avoid generic questions (e.g. "Tell us about your background"). Instead, write questions that probe specific, contrarian stances, real-world examples, and actionable processes (e.g., "In your recent article, you said X is dead. Why is that?").
4. **Natural Transitions:** Draft guiding prompts or transition scripts for the host to steer the conversation smoothly between segment topics.
5. **No Invented Guest Quotes/Opinions:** Do not assume guest opinions. Frame questions to invite their thoughts rather than declaring what they think.

## Workflow

### Step 1 — Guest Dossier & Topic Research
* Research and summarize the guest's background, past speaking points, and unique viewpoints.
* Frame the episode's strategic angle: What makes this topic unique compared to other podcasts in this space?

### Step 2 — Episode Segment Structure
Map the timeline blocks (default 30-45 minutes):
* **00:00 - 02:00 | Intro Hook:** High-impact host intro, guest intro, and summary of the episode value.
* **02:00 - 05:00 | Icebreaker:** A warm, light questions anchoring the guest's expertise.
* **05:00 - 15:00 | Part 1: The Context & Status Quo:** Establishing the problem.
* **15:00 - 30:00 | Part 2: The Solution & Actionable Steps:** Strategic and tactical changes.
* **30:00 - 38:00 | Part 3: Future Outlook & Predictions:** What's next in the next 12-24 months.
* **38:00 - 40:00 | Outro & CTA:** Summarizing lessons, host sign-off, guest links, sponsor messages, and CTA.

### Step 3 — Draft Script & Questions
* Write verbatim scripts for the Intro Hook and the Outro.
* Write 8–10 structured questions for the body, grouping them under clear H2 segment banners. Provide brief "Host guidance notes" explaining *why* each question is being asked.

## Output structure (`.md`)

Save as `output/podcasts/episode-plan-<topic-or-guest>-<date>.md` with this structure:

```markdown
# Podcast Episode Plan: [Topic or Guest Name]
Host: [Host Name] | Guest: [Guest Name, Title, Company]
Target Length: [e.g. 40 minutes] | Format: [e.g. Guest Interview]
Date: [yyyy-mm-dd]

---

## 1. Episode Brief & Guest Profile
* **Core Theme:** [Summary of topic]
* **Target Audience ICP:** [Who is the listener?]
* **Episode Goal:** [Key listener takeaway]
* **Guest Bio Summary:** [Short professional profile]
* **Guest Unique POV Angles:** [2-3 strategic talking points]

---

## 2. Master Run of Show (Timeline)
| Time | Segment | Focus | Format |
|---|---|---|---|
| 00:00 | Intro Hook | Episode overview & Guest intro | Scripted (Host) |
| 02:00 | Icebreaker | Warm-up question | Guided Q&A |
| 05:00 | Part 1: The Status Quo | Mapping current challenges | Guided Q&A |
| 15:00 | Part 2: Actionable Strategy| Solutions & processes | Guided Q&A |
| 30:00 | Part 3: Future Outlook | Predictions | Guided Q&A |
| 38:00 | Outro & CTA | Soft pitch & Closing details | Scripted (Host) |

---

## 3. Host Scripts (Verbatim)

### Intro Hook Script
"Welcome back to [Show Name]... Today, we're diving into a challenge that almost every B2B leader is facing... To help us unpack this, I'm joined by..."

### Outro Script
"A huge thank you to [Guest Name] for sharing... You can find links to everything we discussed in the show notes at... Don't forget to subscribe and..."

---

## 4. Interview Blueprint (Questions & Guides)

### Icebreaker Segment
#### Question 1: [Question text]
* **Host Guide:** [Why ask this? What response to look for?]

### Part 1: The Status Quo [Topic]
#### Question 2: [Question text]
* **Host Guide:** [Prompt to probe deeper on X]

#### Question 3: [Question text]
* **Host Guide:** [Ensure they cover the impact on ICP]

### Part 2: Actionable Solutions [Topic]
...
```

## Rich deliverable

After saving the `.md`, invoke `document-skills:docx` to export the plan as a Word document for the host's recording screen or guest review.
Save as `output/podcasts/episode-plan-<topic-or-guest>-<date>.docx`.

## Quality checklist

- [ ] Verbatim scripts for Intro and Outro are written for the ear (short, punchy).
- [ ] Guest biography and unique points of view are researched.
- [ ] Timeline table maps out timing blocks clearly.
- [ ] Questions are open-ended and designed to prompt storytelling.
- [ ] Soft CTA is clearly integrated into the outro script.
- [ ] Output files saved to `output/podcasts/` folder.
