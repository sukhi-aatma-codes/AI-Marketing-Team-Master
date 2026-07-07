---
name: webinar-plan
description: >
  Use this skill when planning a webinar as a lead-gen or audience-education program —
  concept, agenda, speaker brief, promotion timeline, registration brief, and follow-up
  sequence outline. Trigger on requests like "plan a webinar on X", "we need a run-of-show
  for our webinar with [speaker]", "build our webinar promotion and follow-up plan", or
  "design the registration-to-follow-up flow for this webinar". Produces the planning
  document only — promotion copy, the registration landing page, and follow-up emails
  are built afterward via social-copy, lp-builder, and email-copy using this plan as brief.
---

# Webinar Plan

Produces the end-to-end plan for a single webinar: concept, agenda, speaker brief,
promotion cadence, registration page brief, and the post-event follow-up structure.
This is a planning document — the actual promotion copy, landing page, and follow-up
emails are written afterward by other skills against this plan.

## Before starting

Read these context files every time:
- `_context/Brand_Voice_Guide.md` — tone rules for promotional and registration copy direction
- `_context/Brand_Product_Offerings.md` — service lines and ICPs the webinar should support
- `_context/Brand_Context.md` — company overview, positioning

## Clarify inputs first

Confirm:
1. **Topic and angle**: What the webinar covers and why it's timely/relevant now
2. **Target ICP**: Who this webinar needs to attract and qualify
3. **Speaker(s)**: Internal expert, external guest, or panel — and their availability/role
4. **Format**: Live Q&A, structured presentation, panel discussion, or fireside chat
5. **Date and promotion window**: When it runs and how much lead time exists for promotion
6. **Primary CTA**: What attendees should do next (demo request, content download, sales conversation)

## Workflow

### Step 1 — Concept and title
Define a title and one-paragraph concept statement. The angle must tie to a real pain point or interest from `Brand_Product_Offerings.md` ICP definitions — not a generic industry topic with no connection to the brand's expertise.

### Step 2 — Agenda / run-of-show
Build a timed agenda (recommend 30–45 minutes total unless the user specifies otherwise):
- Opening hook (first 2 minutes — why attendees should stay)
- Core content blocks with timing
- Q&A window
- Closing CTA moment

### Step 3 — Speaker brief
For each speaker:
- Role in the session (host, presenter, panelist)
- Key talking points to prepare (not a script — bullet points)
- What makes them credible on this topic (ties to proof points in `_context\`)

### Step 4 — Promotion timeline
Map the promotion cadence across the lead time window (e.g. 3 weeks out, 1 week out, day-of, day-after):
- Channel and format needed at each touchpoint (email, social post, paid ad)
- Which downstream skill produces it — do not write the copy here

### Step 5 — Registration page brief
Define the brief for `lp-builder`: offer framing, what's promised, form fields needed, urgency/scarcity angle if applicable.

### Step 6 — Follow-up sequence outline
Map the post-event flow as two tracks:
- **Attendees**: thank-you + recording/resources + primary CTA follow-up
- **No-shows**: recording offer + re-engagement CTA

For each touch, note timing (e.g. "same day," "+2 days") and purpose — not the copy itself.

### Step 7 — Execution handoff
List, per deliverable, which skill produces it:
- Promotion social posts → `social-copy`
- Promotion email reminders → `email-copy`
- Registration landing page → `lp-builder`
- Post-event follow-up sequence → `email-copy`

## Output structure (`.md`)

Save as `output/webinars/webinar-plan-<topic>-<date>.md`:

```
# Webinar Plan: [Title]
Topic/Angle: [...]
Target ICP: [...]
Format: [...]
Date: [yyyy-mm-dd] | Promotion window: [start date]–[event date]
Primary CTA: [...]

## Agenda / Run-of-Show
| Time | Segment | Notes |
|------|---------|-------|

## Speaker Brief
### [Speaker name/role]
Talking points: [...]
Credibility angle: [...]

## Promotion Timeline
| Touchpoint | Channel | Format | Owning skill |
|------------|---------|--------|----------------|

## Registration Page Brief (for lp-builder)
Offer framing: [...]
Form fields: [...]
Urgency angle: [...]

## Follow-Up Sequence Outline
### Attendee track
| Timing | Purpose |
|--------|---------|

### No-show track
| Timing | Purpose |
|--------|---------|

## Execution Handoff
| Asset | Skill to invoke |
|-------|------------------|
| Promotion social posts | social-copy |
| Promotion email reminders | email-copy |
| Registration landing page | lp-builder |
| Follow-up sequence | email-copy |
```

## Quality checklist

- [ ] Concept ties to a real ICP pain point in `Brand_Product_Offerings.md` — not a generic topic
- [ ] Agenda is timed and includes an opening hook and a clear closing CTA moment
- [ ] Speaker credibility angle is sourced from `_context\`, not invented
- [ ] Promotion timeline covers the full lead-time window with no gaps
- [ ] Follow-up sequence covers both attendee and no-show tracks
- [ ] Execution handoff table routes every asset to the correct owning skill
- [ ] `.md` saved to `output/webinars/`
