---
name: media-pitch
description: >
  Use this skill whenever the user wants to draft a personalized media pitch email targeting
  journalists, editors, or podcasters. Trigger on requests like "write a pitch to a reporter",
  "draft a media email for TechCrunch", "create a journalist outreach message", "write a pitch for
  our press release", or "draft an email pitching our spokesperson". This skill handles hook
  personalization, value proposition alignment, and follow-up strategy mapping.
---

# Media Pitch

Drafts highly targeted, personalized email pitches designed to capture a journalist's or editor's
attention. Aligns news hooks with a reporter's specific beat or recent coverage history. Produces a
structured `.md` outreach file saved in `output/pr/`.

## Before starting

Read these context files every time — do not rely on prior session memory:
- `_context/Brand_Context.md` — brand positioning and core domains
- `_context/Brand_Voice_Guide.md` — writing style guidelines (pitches must be concise, professional, and value-focused)

## Clarify inputs first

Confirm with the user:
1. **Target Outlet & Journalist:** The publication and writer's name (e.g. Jane Doe at TechCrunch).
2. **Journalist's Beat / Recent Coverage:** A brief note on what the reporter writes about or a recent article to reference.
3. **Primary News Hook:** The story we are pitching (usually linked to a press release or asset in `output/pr/`).
4. **Pitch Angle:** Why this story is relevant to *their* readers *today* (timeliness, trend, data).
5. **Spokesperson & Offer:** Who is available for interview, or what exclusive data we are offering.

If the user's request makes these inputs clear, skip asking and proceed.

## Workflow

### Step 1 — Hook Personalization
Identify the connection between the brand's news and the journalist's work:
- Search or inspect the journalist's recent articles.
- Draft an opening line that references their specific coverage: "I read your piece on [Topic] and..."
- Avoid generic flattery (e.g. "I love your work!"). Be specific and relevant.

### Step 2 — The Pitch Structure
Keep the pitch brief, punchy, and structured for quick scanning:
- **Subject Line:** Max 60 characters, hook-first, clear value indicator (e.g. "PITCH: [Short Hook] for [Outlet]").
- **Intro (1-2 sentences):** The personalized connection hook.
- **The News (2-3 sentences):** The core announcement or story idea. State the conflict or problem first, then the solution.
- **Why It Matters (2-3 bullet points):** Citable facts, trends, or data that validate the pitch.
- **The Offer / CTA (1-2 sentences):** An interview with a spokesperson, exclusive data access, or a product trial.
- **Sign-off:** Professional closing.

### Step 3 — Follow-up Strategy
Include a short, structured plan for following up if the journalist does not respond (timing, channel, alternative angle).

## Output structure (`.md`)

Save as `output/pr/media-pitch-<topic>-<date>.md` with this exact structure:

```
# Media Pitch: [Story Title]
Target Journalist: [Name]
Target Publication: [Outlet Name]
Recent Reference: [Article title/link referenced in the pitch]
Date: [yyyy-mm-dd]

## Email Subject Line Options
- Option 1 (Data-led): PITCH: [Hook with stat] for [Outlet]
- Option 2 (Trend-led): PITCH: [Hook referencing trend]
- Option 3 (Direct): Story Idea: [Announcment summary]

---

Hi [Journalist Name],

[Personalized intro referencing their recent coverage or beat focus - e.g., "I saw your recent coverage of the growing API security gap among mid-market banks, and wanted to share an update on this front."]

[The Hook: Core announcement summary. Match the pitch angle to their audience's primary interest.]

Here are a few reasons why this is relevant to [Outlet] readers right now:
- **[Bullet Point 1 - Trend/Fact]:** [Description and metric proving timeliness]
- **[Bullet Point 2 - Differentiation]:** [How this approach differs from standard alternatives]
- **[Bullet Point 3 - Impact]:** [What the real-world outcome is]

I can offer you:
- An exclusive interview with [Spokesperson Name], [Title] at [Company] (available [dates/times])
- Pre-release access to the full data report/product platform
- Under-embargo draft details (embargo lifts: [Date/Time])

Would you be open to a quick chat or receiving an embargoed copy of the full announcement?

Best regards,

[Sender Name]
[Sender Title]
[Company Name]
[Media Contact Email/Phone]
[Brand URL]

---

## Pitch Strategy & Follow-up Plan
### Target Follow-up Timeline
- **Follow-up 1 (Day 3-4):** Brief check-in email modifying the hook (e.g., "Hi [Name], just following up to see if you have any questions on the data...").
- **Follow-up 2 (Day 7):** Alternative angle or phone check-in (if appropriate).
- **If ignored:** Move to [Alternative Outlet/Journalist Name].
```

## Quality checklist

- [ ] Email body copy is under 200 words (excluding contact info and follow-up plan)
- [ ] Subject line is under 60 characters and clearly marked as PITCH or Story Idea
- [ ] Opening line references specific recent work or beat focus of the journalist
- [ ] Pitch focuses on the conflict/outcome value, not product features
- [ ] Clear call to action offering a specific interview or asset (not just "what do you think?")
- [ ] Output saved to `output/pr/`
