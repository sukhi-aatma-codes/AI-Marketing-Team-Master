---
name: podcast-show-notes
description: >
  Use this skill whenever the user wants to draft podcast show notes, summaries, timestamp breakdowns, or
  promotional descriptions for a recorded podcast episode. Trigger on requests like "write show notes for episode 5
  with Guest X", "create an episode summary and timestamps", "draft description copy for our podcast player", or
  "compile resources and promotional copy for the recorded podcast". Coordinates summaries, takeaway logs,
  timestamps, resource listings, and social promotion blurbs.
---

# Podcast Show Notes Creator

Drafts high-engagement podcast show notes, chronological timestamp logs, guest resource listings, and platform-specific promotional blurbs for recorded episodes. Produces structured deliverables in `.md` and formatted Word documents (`.docx`) in `output/podcasts/` for CMS uploading and player description distribution.

## Before starting

Read these context files every time — do not rely on prior session memory:
- `_context/Brand_Voice_Guide.md` — copywriting voice rules (show notes must remain scannable, outcome-led, and benefit-driven).
- `_context/Brand_Style.md` — typographic/linking style (links must be descriptive, not naked URLs).
- `_context/Brand_Insights_Ledger.md` — Section 9 (Podcast Intelligence) and Section 3 (Copywriting & Voice Preferences).

## Clarify inputs first

Confirm with the user (unless specified):
1. **Episode Audio Draft / Transcript / Outline:** What actually occurred in the episode? (If unavailable, request bulleted topics and guest answers).
2. **Guest Name & Title:** (Verify correct spelling).
3. **Episode Title:** (Format preference, e.g., guest name, topic headline).
4. **Resources Mentioned:** Books, websites, reports, profiles, or tools mentioned during the recording.
5. **Primary CTA:** (e.g., download an associated lead magnet, sign up for newsletter, book a demo).

## Writing & Structuring Rules

1. **Intriguing Episode Summary:** The opening summary (100–150 words) must highlight the *stakes* and the *value* of the conversation. Focus on the core transformation or problem solved. Avoid dry logs like "In this episode we talk to X about Y." Instead, use: "Host [Name] sits down with [Guest Name] to uncover why B2B firms lose margin..."
2. **Key Takeaway Logs:** List 3–5 bulleted key takeaways. Each bullet should represent a complete, actionable thought of 15-25 words.
3. **Structured Timestamps:** Map key discussion pivots with timestamps in `[MM:SS]` or `[HH:MM:SS]` format. Make timestamps descriptive (e.g. `[12:45] The shift from spreadsheets to automation` instead of `[12:45] Part 2`).
4. **Descriptive Link Anchor Text:** All mentioned resources must be formatted as descriptive links (e.g. [Read the Gartner 2024 Automation Report](http://...) rather than [here](http://...) or just the raw URL).
5. **Platform-Native Promotional Copy:** Include 1–2 social promotion post templates (e.g. LinkedIn hook-style, Twitter/X thread starter) to drive audience traffic to the episode player.

## Workflow

### Step 1 — Review Transcript or Recording Highlights
* Extract the critical points, stats, and quotes mentioned by the guest and host.
* Identify the exact timing signatures of key topic shifts.

### Step 2 — Draft the Show Notes Sections
Draft the Summary, Key Takeaways, Timestamps, and Resources sections in order.

### Step 3 — Draft Social Promo Copies
Write B2B-native promotional social copy promoting the episode launch. Ensure character compliance.

## Output structure (`.md`)

Save as `output/podcasts/show-notes-<topic-or-guest>-<date>.md` with this structure:

```markdown
# Podcast Show Notes: [Episode Title]
Show: [Show Name] | Episode: [Number]
Guest: [Guest Name, Title, Company]
Date: [yyyy-mm-dd]

---

## 1. Episode Summary
[Compelling, benefit-led summary. Write 2 short paragraphs outlining the challenge, the guest's unique response, and what listeners will walk away with.]

---

## 2. Key Takeaways
From this conversation, you'll learn:
* **[Core takeaway title]:** [1-2 sentences expanding on the takeaway and why it matters.]
* **[Core takeaway title]:** [1-2 sentences expanding on the takeaway.]
* **[Core takeaway title]:** [1-2 sentences expanding on the takeaway.]

---

## 3. Episode Timestamps
* **[00:00]** Intro & Guest Welcome.
* **[02:15]** [Icebreaker topic and guest's background hook.]
* **[06:40]** [Segment Topic: The status quo challenge.]
* **[15:10]** [Segment Topic: Step-by-step solution.]
* **[30:50]** [Segment Topic: Predictions for the next 12 months.]
* **[38:20]** Host Outro & Sponsor details.

---

## 4. Mentioned Resources & Links
* **Connect with the guest:** [[Guest Name] on LinkedIn]([URL])
* **Connect with the host:** [[Host Name] on LinkedIn]([URL])
* **Resources Mentioned:**
  * [[Title of Tool/Report]]([URL]) — [Short description of what the tool does or why it's referenced]
* **Episode CTA:** [Associated Lead Magnet / Landing Page Link]

---

## 5. Social Promotion Copy

### LinkedIn Post Copy
[Attention hook. Bulleted takeaways from the episode. Call to action directing to the podcast player link.]

### Twitter/X Post Copy
[Short tweet teaser (max 280 chars) + hashtags.]
```

## Rich deliverable

After saving the `.md`, invoke `document-skills:docx` to export the show notes as a Word document.
Save as `output/podcasts/show-notes-<topic-or-guest>-<date>.docx`.

## Quality checklist

- [ ] Opening summary is engaging and outlines the value of the conversation.
- [ ] 3-5 key takeaways are structured as complete thoughts.
- [ ] Timestamp log is chronologically accurate and descriptive.
- [ ] Resources list has descriptive, clickable links (no naked URLs).
- [ ] Social promo copy is included and customized for LinkedIn and Twitter/X.
- [ ] Output files saved to `output/podcasts/` folder.
