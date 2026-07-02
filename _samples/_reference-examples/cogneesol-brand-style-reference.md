# Cogneesol — Brand Style Reference Guide

A visual style library for content creation across digital, social, print, and event formats.
Each style is described using directional creative language so Claude and image generation
models (Flux, Ideogram) can interpret and produce on-brand variations with flexibility.

**Brand constants that apply to ALL styles:**
- Primary Blue: `#112C7D`
- Primary Red: `#AB2828`
- Font: Montserrat (all weights)
- Tone: Authoritative, transformation-forward, partner-not-vendor
- Never: clip art, gradients not grounded in brand blue, overly cheerful stock photography

---

## EXISTING STYLES
*Documented from live website assets. Use these for website banners, service pages, and on-site feature imagery.*

---

### E1: Constellation Banner

**Format:** 1440×420px (wide hero banner). Website hero sections, service page headers, event landing pages.

**Best for:** Any wide-format banner where the left half carries headline text and the right half provides visual context. Vertical pages, service overviews, solution pages.

**Energy:** Quiet authority. The blue feels deep and intelligent — like looking at a control room or a live data network at night. Professional without being cold. The photo grounds it in the real world without competing with the text.

**Look:** The entire background is a deep navy blue `#112C7D` that darkens toward the top corners and right edge, creating a natural vignette. Across the left 55% of the image, a geometric constellation network of thin cyan-to-teal lines (`~#00D4FF` at low opacity, ~15%) connects seven to ten glowing node points — small radiant circles with a soft cyan glow and subtle halo. The lines are irregular, not grid-based — they feel organic and data-driven rather than decorative. The right 45% transitions from the pure blue into a dark-tinted, desaturated photograph that bleeds into the network — the photo has a navy color-graded overlay at ~70% opacity so it reads as part of the composition, not a separate element. The photo subject is always a human or object directly relevant to the service (e.g., a robotic hand touching a digital surface for D.A.T., insurance professional for insurance, city skyline for real estate). No text is embedded in the generated image — text is overlaid in the design tool.

**Color usage:** 80% deep navy blue. 15% dark-tinted photography. 5% cyan glow accents.

**Flux prompt starter:**
> Wide cinematic banner, deep navy blue `#112C7D` background, geometric constellation network of thin glowing cyan lines with small radiant teal node points on the left half, seamlessly blending into a dark navy-tinted photograph of [SUBJECT] on the right side, professional B2B technology aesthetic, no text, ultra-wide aspect ratio, photorealistic, dark moody lighting, subtle lens glow on nodes —ar 16:4 —style raw

**Ideogram prompt starter:**
> Wide format graphic design banner, deep navy blue background, abstract neural network constellation pattern with thin teal glowing lines and bright node points on left side, dark professional photograph of [SUBJECT] color-graded navy blue on right side, seamless blend between illustration and photo, B2B enterprise technology brand, no text or typography, horizontal banner composition

**Do not:** Use bright or warm photography. Add white or light backgrounds. Use the constellation on a non-blue base. Let the photo overpower the left text zone.

---

### E2: Diagonal Slash Card

**Format:** 625×625px (square card). Service vertical feature images, vertical solution thumbnails, blog featured images, LinkedIn single-image posts.

**Best for:** When a single image needs to represent a specific service or vertical (Insurance, Pharma, Finance, Legal, Real Estate). The diagonal creates energy and forward momentum.

**Energy:** Precise and dynamic. The diagonal cut feels like transformation in progress — something being divided and reimagined. The corner triangles function as a visual signature, grounding the image in the Cogneesol brand without a logo present.

**Look:** White or very light neutral background taking up approximately 25% of the frame on the left side and bottom-left corner. The main photograph occupies the dominant portion of the image, entering from the upper right and filling 70-75% of the frame. A clean, sharp diagonal white slash cuts across the image from lower-left to upper-right at approximately 45–50 degrees — this is a solid white bar, 15-20px wide, creating a hard graphic separation between the white margin and the photograph. In the bottom-left corner, two geometric triangles are stacked: a large right-pointing triangle in brand red `#AB2828` (approximately 55px tall) and a smaller right-pointing triangle in brand navy `#112C7D` (approximately 30px tall) positioned just below and slightly right of the red triangle, creating a layered arrow-like mark. The photograph is full color, sharp, professional — subject matter relates to the relevant service vertical (e.g., lab technician with digital health overlay for Pharma, digital wallet with fintech icons for Finance).

**Color usage:** White background margins. Full-color photography. Red `#AB2828` and navy `#112C7D` geometric corner mark only.

**Flux prompt starter:**
> Square format, professional stock photograph of [SUBJECT] filling three-quarters of the frame from upper right, sharp diagonal white slash line cutting across at 45 degrees from lower-left to upper-right, white background visible in lower-left corner, small red and navy geometric right-pointing triangles stacked in lower-left corner as brand mark, clean modern B2B design, natural studio lighting, no text —ar 1:1

**Ideogram prompt starter:**
> Square graphic design composition, professional photograph of [SUBJECT] dominating upper-right, bold diagonal white stripe slashing across from lower-left to upper-right, white negative space lower-left, two small stacked right-pointing triangles in red and dark navy in bottom-left corner, modern enterprise brand visual, clean minimal design, no text

**Do not:** Round the corners on the diagonal. Make the triangles too large (they are an accent, not a hero). Use dark or moody photography — the photo should be well-lit and professional.

---

### E3: Dark Navy Overlay Card

**Format:** 380×240px (horizontal card) or 340×200px. Success story cards, case study thumbnails, blog article cards, event recap posts.

**Best for:** When a real photograph needs to carry brand weight — client outcomes, case studies, event photos, industry verticals in context.

**Energy:** Grounded and credible. The dark overlay transforms any photograph into a brand asset. It signals "this is a real result, not an illustration."

**Look:** Full-bleed professional photograph covers the entire card. A dark navy-to-transparent gradient overlay sits over the bottom 50-60% of the image, starting from near-transparent at the mid-point and reaching approximately 85% opacity `#112C7D` at the bottom edge. This creates a dark shelf where white headline text and a small red arrow → CTA sit cleanly. The top of the image remains visible and shows the photograph clearly. The overall effect reads like a premium editorial magazine card. An optional thin red `#AB2828` top border (3px) can be applied to reinforce brand identity. No constellation or geometric elements — the photograph is the hero.

**Color usage:** Full-color photography. Navy gradient overlay. White text. Red arrow/CTA accent.

**Flux prompt starter:**
> Horizontal editorial card, full-bleed professional photograph of [SUBJECT], dark navy blue gradient overlay covering the bottom half fading to transparent at top, moody cinematic color grade, B2B enterprise editorial style, no text, photorealistic —ar 16:10

**Ideogram prompt starter:**
> Horizontal card design, full-bleed corporate photography of [SUBJECT], dark navy blue translucent gradient overlay on lower half, clean editorial layout, professional enterprise brand aesthetic, no text or typography

**Do not:** Apply the constellation network on top. Use a light overlay. Use illustrated or stock-clip photography — must feel documentary/real.

---

## ASPIRATIONAL STYLES
*These styles do not yet exist in Cogneesol's asset library. Build toward them for LinkedIn, thought leadership, reports, events, and social content.*

---

### A1: Executive Insight — Dark

**Format:** 1080×1080px (LinkedIn carousel slide, Instagram square). LinkedIn carousel posts, thought leadership series, weekly industry stat posts, conference speaker content.

**Best for:** Sharing a single powerful insight, statistic, or expert perspective. The content type that builds authority with CFOs, COOs, and VPs. Each slide in a carousel should carry one idea only.

**Energy:** The feel of a premium analyst report — Gartner meets McKinsey but with a human voice. Confident without being cold. The reader should feel like they're receiving privileged intelligence, not a sales pitch.

**Look:** Deep navy `#112C7D` full-bleed background. A single large statistic or short declarative statement in white Montserrat Bold (48–64pt) dominates the upper two-thirds. A thin red horizontal rule `#AB2828` (2px, spanning 60px) sits just above the headline as a visual anchor — not decorating the bottom of the text but introducing it from above. Supporting context text in Montserrat Regular white at 14–16pt sits below the headline. A subtle geometric texture — very faint diagonal grid lines or dot matrix at 4% white opacity — adds depth to the background without distraction. Bottom of the slide carries the Cogneesol wordmark in white (small, ~14pt) left-aligned, and a source citation in Montserrat Light grey-white right-aligned. Cover slide of any carousel uses a red `#AB2828` full-bleed background instead of navy, with white Montserrat Black headline — this creates a scroll-stopping entry point before settling into the navy interior slides.

**Color usage:** 90% navy. Red rule accent. White typography. Cover slide: 90% red, white type.

**Flux prompt starter:**
> Square format dark navy background `#112C7D`, large bold white sans-serif statistic text centered upper half, thin red horizontal accent line above the text, subtle dot-matrix texture at very low opacity on background, clean minimal graphic design, B2B executive intelligence aesthetic, no decorative photography, professional and premium —ar 1:1 —style raw

**Ideogram prompt starter:**
> Square LinkedIn carousel slide design, deep navy blue `#112C7D` solid background, large white bold Montserrat statistic headline centered, thin red `#AB2828` horizontal rule above headline, faint diagonal grid texture in background, small brand wordmark bottom left, minimal premium B2B design, McKinsey-style analytical aesthetic, no images or photography

**Carousel structure:**
- Slide 1 (Cover): Red background, white bold hook headline, "Swipe →" micro-label
- Slides 2–6 (Insight): Navy background, one stat or insight per slide, red rule anchor
- Slide 7 (CTA): Navy background, brief offer + cogneesol.com + "Talk to Our Team"

**Do not:** Crowd a slide with more than one idea. Use imagery or photography. Apply the constellation network. Mix light and dark backgrounds within interior slides.

---

### A2: Executive Insight — Editorial Break

**Format:** 1080×1080px. LinkedIn carousel posts targeting broader audiences (not just C-suite), HR/talent content, culture posts, award announcements, partnership reveals.

**Best for:** Content that needs to reach beyond the core buyer persona. Lighter, more approachable posts that expand the audience without abandoning brand credibility. Think: IWD posts, team milestones, ESG content, Everest Group recognition announcements.

**Energy:** A premium business magazine — like HBR or Fast Company. Intelligent but inviting. The whitespace signals confidence. The brand is present but not imposing. Someone who isn't actively buying should still feel this is worth reading.

**Look:** Clean white `#FFFFFF` background with generous whitespace. Navy `#112C7D` Montserrat Bold headline (36–44pt) left-aligned, not centered. A red `#AB2828` vertical bar (4px wide, 40px tall) sits to the left of the headline as a typographic accent — like a blockquote marker. Body text in Montserrat Regular at 13pt in dark charcoal `#1A1A2E`. A single photograph or graphic element occupies the right 40% of the slide in a clean rectangular crop — full color, well-lit, human or contextual (no network graphics, no tech overlays). Bottom strip: thin light grey rule, then small Cogneesol logo left and subtle page number or topic label right. The overall composition breathes — there is no element in every corner.

**Color usage:** 70% white. Navy and charcoal typography. Red left-bar accent. Single photo element.

**Flux prompt starter:**
> Square format editorial layout, clean white background, professional photograph of [SUBJECT] in right 40% rectangular crop, generous whitespace left side, minimal B2B magazine aesthetic, soft natural lighting on subject, premium business editorial feel, no text —ar 1:1

**Ideogram prompt starter:**
> Square editorial graphic design, white background, navy bold headline left-aligned with thin red vertical bar accent to left, rectangular photograph right side, clean minimal business magazine layout, HBR Harvard Business Review aesthetic, Montserrat typography, B2B professional brand, generous whitespace

**Do not:** Use the constellation network. Center-align body text. Use more than one photograph. Make the red accent too large — it is a typographic mark, not a shape.

---

### A3: Data Signal

**Format:** 1080×1080px (square) or 1200×628px (LinkedIn link preview / Twitter card). Whitepaper pull-quotes, industry data posts, D.A.T. framework explainer slides, research stat announcements.

**Best for:** Sharing Cogneesol's analytical credibility. Any post where the content is a number, a trend, a finding, or a framework insight. This is the style that makes Cogneesol look like a research firm, not just a BPO.

**Energy:** The premium research aesthetic of Deloitte Insights or McKinsey Quarterly — but in Cogneesol's exact palette. Deliberate, unhurried, precise. Every element justifies its presence. The reader should feel the data is trustworthy before they even read it.

**Look:** Very deep navy — almost black navy `#0C1F5C` — full-bleed background. A single large data visualization element occupies the center: either an oversized percentage/number in white Montserrat Black (96–120pt) with a smaller red superscript label, OR a minimal bar/line chart rendered in white and red on the dark background. Thin white horizontal rules (1px, 20% opacity) divide the slide into thirds — subtle, structural, not decorative. A small Cogneesol red `#AB2828` square marker (8×8px) introduces the source attribution text in the bottom-left. The top carries a short all-caps category label in Montserrat SemiBold tracked wide (`INSURANCE OPERATIONS · 2025`) in light grey-white. No photography. No illustration. No texture. The visual weight is entirely in the data and typography.

**Color usage:** Deep navy background. White for primary data. Red for highlights and markers. Zero photography.

**Flux prompt starter:**
> Square format minimal data visualization design, very deep navy blue almost black background, single large white bold percentage or number centered, thin horizontal white rule lines as background structure, small red accent square bottom left, clean premium research report aesthetic, no photography no illustration, typographic-led design —ar 1:1 —style raw

**Ideogram prompt starter:**
> Square data visualization graphic, deep near-black navy `#0C1F5C` background, enormous white bold Montserrat statistic centered, thin white horizontal structural lines, small red `#AB2828` square accent mark, all-caps grey category label top, minimal premium research design, Deloitte Insights McKinsey aesthetic, B2B data intelligence brand, no images

**Do not:** Add photographs or illustrative elements. Use more than two data points per slide. Use a lighter background — the depth of the navy is critical to the premium feel.

---

### A4: Framework Explainer

**Format:** 1080×1080px (carousel) or 1200×900px (presentation slide export). D.A.T. framework posts, process explainer carousels, methodology breakdowns, "how we work" content.

**Best for:** Making Cogneesol's intellectual property visible. The D.A.T. framework, the 5-step delivery process, the ADIS framework — these need visual form to build perceived expertise. This style turns a concept into a shareable, credible diagram.

**Energy:** Clear, structured, intelligent. The feeling of a well-designed McKinsey slide — the kind that makes a complex idea look simple. Should feel like it took expertise to simplify, not like a template was applied.

**Look:** White `#FFFFFF` background. A central diagram occupies the middle 70% of the slide — this could be a horizontal process flow (numbered circles in alternating navy/red connected by thin navy lines), a hub-and-spoke model, or a layered pyramid. Primary shapes use brand navy `#112C7D` filled circles or rectangles. Active/highlighted elements use brand red `#AB2828`. Connecting lines are thin navy, 1.5px. Labels inside or below shapes in Montserrat SemiBold white (inside navy shapes) or Montserrat SemiBold navy (on white background). Each node carries a 1–2 word label only — no full sentences inside the diagram. A supporting sentence in Montserrat Regular 12pt charcoal sits below the diagram as context. Top of slide: Montserrat Bold navy headline 28pt, left-aligned, with red left-bar accent. Bottom: Cogneesol wordmark small, right-aligned.

**Color usage:** White background. Navy shapes. Red highlights/active nodes. Charcoal body text.

**Ideogram prompt starter:**
> Square infographic design, white background, clean process flow diagram with navy blue `#112C7D` numbered circles connected by thin navy lines, one red `#AB2828` highlighted active circle, Montserrat bold labels inside shapes, minimal enterprise framework diagram, McKinsey slide aesthetic, B2B professional design, no photographs, structured and clear

**Flux prompt starter:**
> Square format clean infographic, white background, minimal process flow diagram with deep navy blue circles and connecting lines, single red accent circle highlighted, bold white labels inside circles, corporate B2B presentation aesthetic, flat design, no photography, professional enterprise brand —ar 1:1 —style raw

**Do not:** Use more than 6 nodes in a single diagram. Add drop shadows, gradients, or 3D effects. Include full sentences inside diagram shapes. Use illustration-style icons.

---

### A5: Report & Whitepaper Cover

**Format:** A4 portrait 2480×3508px (print-ready) or 816×1056px (digital screen). Whitepaper covers, CFO guides, industry reports, gated content PDFs.

**Best for:** Any piece of long-form content Cogneesol publishes — "Data is the Spinal Cord of Insurance", CFO's Guide to IRM, Finance Automation Trends, etc. The cover must signal premium research quality before the first word is read.

**Energy:** The feeling of picking up a Deloitte Insights report or an Everest Group PEAK Matrix publication. Heavy, considered, valuable. The kind of document someone saves to their desktop rather than skimming and closing.

**Look:** Deep navy `#112C7D` occupies the top 65% of the cover as a solid field. A large, abstract geometric element — a partial circle arc, a diagonal plane, or a fragmented grid of thin white lines — sits in the top-right quadrant at approximately 8% white opacity, providing visual depth without competing. The report title in Montserrat ExtraBold white sits at top-left, large (36–44pt), spanning up to two lines. Below the title, a red `#AB2828` horizontal rule (60px wide, 3px tall) introduces a two-line subtitle in Montserrat Regular white 16pt. A bold red rectangle `#AB2828` (full width, 32px tall) creates a dividing band between the navy top and the white bottom section — this is a signature structural element of the Cogneesol report cover. The bottom 35% is white: this carries the author name(s) in Montserrat Medium navy 12pt, a small report category tag in red all-caps 9pt, the Cogneesol logo bottom-left, and the year bottom-right. An optional thumbnail photograph (industry-relevant, square crop) can be inset in the lower-right of the white section with a navy border.

**Color usage:** 65% deep navy. Red band divider. White bottom section. White typography on navy. Navy typography on white.

**Ideogram prompt starter:**
> Portrait A4 report cover design, deep navy blue `#112C7D` top two-thirds, bold white Montserrat report title top-left, thin red `#AB2828` horizontal rule below title, subtitle text white, full-width red horizontal band dividing navy top from white bottom section, white bottom third with author names and small logo, faint abstract geometric arc in top-right corner at very low opacity, premium Deloitte-style research report cover, no photography in main area

**Flux prompt starter:**
> Portrait format premium report cover, dark navy blue upper section, large bold white title typography upper left, thin red accent rule, full-width red stripe dividing the cover horizontally, clean white lower section, subtle abstract geometric pattern in background at low opacity, professional B2B research publication aesthetic, Montserrat typography, no people —ar 3:4 —style raw

**Cover series consistency:** Once a cover system is established, vary only the title text, the optional inset photograph, and the abstract geometric element (arc vs. grid vs. diagonal). The red band, logo placement, and color split remain fixed.

**Do not:** Use the constellation network on report covers — too web-native, not print-authoritative. Use photography as the dominant element. Change the red band position between covers in a series.

---

### A6: Event Presence

**Format:** Multiple: 1080×1080px (social announcement), 1920×1080px (digital signage/expo screen), 400×500px (speaker bio card). Conference announcements, expo booth graphics, speaking engagement cards, event recap posts.

**Best for:** Any time Cogneesol appears at an industry event — Vertafore AccelerateNOW, UAC-Xceedance, APCIA, industry forums. Also for announcing participation before the event and sharing highlights after.

**Energy:** Energetic, present, confident. The feeling of a brand that belongs on the conference floor alongside the big players. Not loud — but unmistakably there.

**Look:** Full-bleed brand red `#AB2828` background — this is the only style where red dominates at full bleed, creating maximum scroll-stopping impact in a social feed. White Montserrat ExtraBold event name or headline large (52–64pt) centered or left-aligned. A navy `#112C7D` diagonal band cuts across the lower 30% of the image at a 10–12 degree angle — this echoes the diagonal slash from E2 but at a macro scale, used as a structural color block rather than a graphic detail. Within the navy band: event details or booth number in Montserrat SemiBold white 18pt. Cogneesol wordmark in white top-left. An optional small event logo badge top-right. For speaker cards, a circular portrait photograph (headshot, professional) sits center-right with the navy band carrying the speaker's name and title. No constellation. No data elements.

**Color usage:** Red primary background. Navy diagonal band. White typography throughout. Optional headshot photo.

**Ideogram prompt starter:**
> Square social media graphic, bold red `#AB2828` full-bleed background, large white bold Montserrat headline centered, navy blue `#112C7D` diagonal band cutting across lower third at slight angle, white details text in navy band, small white logo top-left, energetic professional B2B event announcement design, no photography in background

**Flux prompt starter:**
> Square format bold event announcement graphic, vivid red background, large white bold typography headline, deep navy blue diagonal geometric band lower third, white text within navy band, clean professional B2B conference brand aesthetic, no photographs —ar 1:1 —style raw

**Do not:** Use the constellation on a red background. Add more than two colors beyond red, navy, and white. Use this style outside of event contexts — the red dominance would conflict with authority content.

---

### A7: Social Proof

**Format:** 1080×1080px (square), 1080×1350px (portrait for Instagram/LinkedIn). Client testimonial posts, award announcements (Everest Group, ISO), client win callouts, employee milestones.

**Best for:** Converting credibility into content. Cogneesol has strong proof points — 500+ clients, Everest Group recognition, real client quotes — but these are underused as visual social content. This style gives them visual form.

**Energy:** Warm confidence. The feeling of a trusted firm that lets results speak. Not boastful — quietly powerful. The reader should feel reassured, not sold to.

**Look:** White background, clean layout. A large opening quotation mark in brand red `#AB2828` Montserrat Black (~120pt) sits in the top-left as a decorative anchor — large enough to be a visual element, not just punctuation. The quote text in Montserrat SemiBold navy `#112C7D` (20–24pt) occupies the center, max three lines, generous line height. A thin red rule (2px, 80px wide) sits below the quote before the attribution. Attribution line: client name bold navy, then title and company in Montserrat Regular charcoal 12pt. For award/recognition posts instead of quotes: a clean badge or certification mark sits center with supporting context text. Bottom: Cogneesol wordmark small navy left, optional industry tag right (e.g., "INSURANCE · CLIENT STORY"). The composition always has 20%+ whitespace — nothing crowds the quote.

**Color usage:** White background. Navy for quote text. Red quotation mark and rule. Charcoal attribution.

**Ideogram prompt starter:**
> Square testimonial card design, white background, large red `#AB2828` opening quotation mark upper-left as decorative element, navy `#112C7D` bold quote text centered, thin red horizontal rule below quote, client attribution text in charcoal below rule, small logo bottom-left, clean minimal premium B2B testimonial design, generous whitespace, no photography

**Flux prompt starter:**
> Square format clean quote card, white background, oversized red quotation mark upper-left, navy blue bold testimonial text center, thin red accent line below quote, minimal premium corporate design aesthetic, no images or photography —ar 1:1 —style raw

**Variant — Award Callout:** Replace quote with centered award badge graphic (e.g., Everest Group PEAK Matrix logo), large navy headline above ("Recognized. Again."), brief context text below, red rule accent. Same whitespace rules apply.

**Do not:** Use more than 35 words in the quote. Add photography behind the quote text. Use the full-bleed navy background — white is critical to differentiate this from A1.

---

## Style Selection Guide

| Content type | Recommended style |
|---|---|
| Website hero / service page banner | E1 Constellation Banner |
| Service vertical thumbnail / blog feature image | E2 Diagonal Slash Card |
| Case study card / success story thumbnail | E3 Dark Navy Overlay |
| LinkedIn thought leadership carousel (C-suite) | A1 Executive Insight Dark |
| LinkedIn culture / award / ESG post | A2 Executive Insight Editorial |
| Industry stat / D.A.T. data post | A3 Data Signal |
| Framework / process explainer carousel | A4 Framework Explainer |
| Whitepaper / report / gated content cover | A5 Report & Whitepaper Cover |
| Event announcement / expo / conference | A6 Event Presence |
| Client quote / award / recognition | A7 Social Proof |

---

## Prompt Assembly Pattern

When asking Claude or an image gen model to create a new asset, use this structure:

```
Style: [Style code and name, e.g. A1 Executive Insight Dark]
Format: [Exact dimensions, e.g. 1080×1080px]
Subject: [What the image or slide is about]
Content: [The specific stat, quote, headline, or message]
Model: [Flux / Ideogram]
Variation: [Any departure from the standard look]
```

**Example:**
```
Style: A3 Data Signal
Format: 1080×1080px
Subject: Insurance processing efficiency stat
Content: "79% of mid-market CFOs reported attempted payments fraud in 2024"
Model: Ideogram
Variation: Use the source citation "Association of Finance Professionals, 2025"
```

---

## What This System Is Not

- Not a logo usage guide (see Brand_Style.md for logo rules)
- Not a web UI component system (see Brand_Style.md for digital standards)
- Not final approved assets — all outputs from image gen models require human review before publishing
- Not exhaustive — new styles can be added as content needs evolve
