---
name: press-release
description: >
  Use this skill whenever the user wants to draft an AP-style press release or media alert
  for wire distribution or journalist pitching. Trigger on requests like "write a press
  release about X", "draft a media announcement for our launch", "create a PR alert for Y",
  "we need a press release for this new service", or "write an AP-style corporate announcement".
  This skill handles structured corporate copy, boilerplate generation, and executive quotes.
  Produces review-ready output files in output/pr/.
---

# Press Release

Drafts structured, AP-style press releases for wire distribution, media distribution, and direct pitching.
Ensures factual precision and clean formatting. Produces a structured `.md` file and a formatted Word
document (`.docx`) for client and legal sign-off.

## Before starting

Read these context files every time — do not rely on prior session memory:
- `_context/Brand_Context.md` — company profile, standard boilerplate information, brand domain
- `_context/Brand_Voice_Guide.md` — corporate tone rules and banned vocabulary (PR requires strict corporate tone, not promotional marketing copy)

## Clarify inputs first

Confirm with the user:
1. **News Angle / Hook:** What is the primary announcement? (Product launch, funding, partnership, executive hire)
2. **Key Facts / Data:** Any specific numbers, release dates, or facts that must be included.
3. **Quotes:** Executive quotes (or draft quotes reflecting specific points).
4. **Embargo Status:** Is the news immediate (FOR IMMEDIATE RELEASE) or embargoed until a specific date/time?
5. **Media Contact:** Name, email, and phone number for the PR representative.

If the user's request makes these inputs clear, skip asking and proceed.

## Workflow

### Step 1 — News Hook & Structure Check
Verify the news is structured in the standard "inverted pyramid" style:
- **Headline (Hook):** Direct, active voice, summary of the news, under 100 characters.
- **Subheadline:** Expands the hook with context or a secondary key fact.
- **Dateline:** City, State (or Country) — Month DD, YYYY.
- **Lead Paragraph (The Hook):** Who, what, when, where, and why in the first 2-3 sentences.
- **Body Paragraphs:** Factual context, supporting quotes, details of the release.
- **Boilerplate:** Standard "About [Company]" paragraph from `Brand_Context.md`.
- **Media Contact Block:** Name, role, email, phone.

### Step 2 — Draft the Release
Write the release in full, adhering to AP style. Apply this house AP contract exactly — do not rely on a general sense of "AP style":
- **Numerals:** spell out one through nine; figures for 10 and above. Always figures for percentages, money, and ages.
- **Percent:** use the % sign with a figure ("25%", not "25 percent").
- **Dateline:** `CITY, State/Country — Month D, YYYY —` in front of the lead sentence, city in all caps.
- **Dates:** Month Day, Year. Abbreviate Jan., Feb., Aug., Sept., Oct., Nov., Dec. only with a specific date.
- **Titles:** capitalize formal titles only directly before a name ("CEO Jane Doe"); lowercase after ("Jane Doe, chief executive officer,").
- **Series commas:** no Oxford comma in simple series.
- **Attribution:** use "said" — never "stated", "shared", "enthused", or "exclaimed".
- **Company references:** a company is singular ("it"), never "they".
- Avoid promotional marketing adjectives (e.g. "revolutionary", "best-in-class", "seamless").
- Use active voice and third-person pronoun perspectives.
- Ground all corporate claims in verifiable facts.
- Include `###` symbols or `### ENDS ###` at the bottom of the content body before the boilerplate.

### Step 3 — Editorial Review & Compliance Check
Review spelling, datelines, and quote attributes:
- Verify that every direct quote is attributed to a named executive with their correct title.
- Place brackets around draft assumptions that need client confirmation: `[DRAFT - confirm quote/metric]`.

## Output structure (`.md`)

Save as `output/pr/press-release-<topic>-<date>.md` with this exact section structure:

```
# Press Release: [Short Title]
Embargo Status: [FOR IMMEDIATE RELEASE / EMBARGOED UNTIL yyyy-mm-dd]
Topic: [Announcement type]
Date: [yyyy-mm-dd]

## CMS Meta Block
Slug: /news/press-release-[slug]
Meta Title: [AP Headline]
Meta Description: [Subheadline or summary, max 155 chars]

---

FOR IMMEDIATE RELEASE

**[DATELINE - CITY, STATE] — [Month Day, Year]** — [Lead paragraph: Who, what, when, where, why. Make it highly factual and direct.]

[Body Paragraph 1: Explaining the announcement in detail. Insert context, data, or product capabilities.]

"Insert executive quote here," said [Executive Name], [Title] at [Company]. "Ensure the quote sounds natural and focuses on strategic vision, customer value, or industry shift."

[Body Paragraph 2: Secondary details, partnerships, integration specifics, or product features.]

"Insert secondary partner/customer quote if applicable," said [Name], [Title] at [Partner Company].

[Conclusion Paragraph: Wrap up details, launch timelines, or product availability.]

###

**About [Company Name]**
[Standard corporate boilerplate text from Brand_Context.md]

**Media Contact**
Name: [Representative Name]
Title: [Representative Title]
Email: [Representative Email]
Phone: [Representative Phone]
Domain: [brand domain URL]
```

## Rich deliverable

After saving the `.md`, invoke `document-skills:docx` to export as a Word document for PR distribution and legal sign-off.
Save as `output/pr/press-release-<topic>-<date>.docx`.

## Quality checklist

- [ ] Headline is in active voice, under 100 characters, and states the news clearly
- [ ] Dateline present in the exact format `CITY, State/Country — Month D, YYYY —` and every rule of the house AP contract above applied
- [ ] Quotes sound like spoken commentary, not written brochures
- [ ] Zero promotional hyperbole (no "seamless", "next-gen", or "disruptive")
- [ ] Media contact block complete with name, title, email, and phone
- [ ] Standard boilerplate text appended at the bottom
- [ ] `.md` and `.docx` saved to `output/pr/`
