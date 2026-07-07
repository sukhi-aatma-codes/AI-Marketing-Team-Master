---
name: image
description: >
  Use this skill when the user wants to create, generate, edit, or optimize a marketing image
  that isn't a LinkedIn carousel or paid ad creative — blog hero images, OG/social preview
  images, profile or directory banners, product mockups, or brand asset exploration. Trigger
  on phrases like "generate a blog hero image", "create an OG image for this page", "make a
  LinkedIn banner", "I need a product mockup", "optimize our images for page speed", or any
  general image generation/editing/optimization request. For paid ad image creative, see
  ad-creative. For LinkedIn carousels and platform social graphics, see social-creative-designer.
---

# Image

Produces general-purpose marketing images and image-optimization guidance — the asset types
that don't fit `ad-creative` (paid ad specs) or `social-creative-designer` (LinkedIn carousels,
platform social graphics): blog heroes, OG/social preview images, profile and directory
banners, product mockups, and exploratory brand asset concepts.

## Before starting

Read these context files every time:
- `_context/Brand_Style.md` — hex colors, typography, imagery direction (photography vs.
  illustration, treatment style)
- `_context/Brand_Style_Reference.md`, if it exists — reuse a named style and its prompt
  starter rather than freelancing a new look for every image. If it doesn't exist yet and the
  task calls for a recognizable visual style, run `build-brand-style-reference` first.

## Tools available — tiered fallback, not a hard dependency

No tool here is required to deliver. Work down this chain; whichever tier is actually
configured (the user may not have set up every key — see `MCP_SETUP.md`), use it. Never block
the deliverable on a missing tool — if nothing below is available, the final fallback (a
detailed image prompt/brief) is always a complete, valid deliverable on its own.

**Tier 1 — generation (try whichever is configured, in this order if multiple are):**
- **Ideogram** (`mcp__ideogram__generate_image`) — photographic/illustrative/abstract generation
- **Flux** (`mcp__flux__*`) — Black Forest Labs FLUX models, strong photorealism/brand consistency
- **Nano Banana** (`mcp__nano-banana__*`) — Gemini 2.5 Flash Image, good general-purpose + editing
- **GPT Image** (`mcp__gpt-image__*`) — OpenAI `gpt-image-1`, good general-purpose + text rendering

Never include text, headlines, or numbers in a generation prompt for any of these — that's
always Canva's job (Tier 2).

**Tier 2 — assembly (always try this for the typography/layout layer):**
- **Canva** (`mcp__canva__*`) — all typography, text overlay, layout assembly, brand-kit
  templates, final export

**Tier 3 — stock photography (when generation isn't available, or real-world authenticity
matters more than uniqueness):**
- **Unsplash** (`mcp__unsplash__*`) — search and retrieve stock photos
- **Pexels** (`mcp__pexels__*`) — search and retrieve stock photos/video

**Tier 4 — final fallback, always available, no setup required:**
- Produce the full image concept as a detailed, ready-to-paste prompt (per the prompting basics
  below) plus the exact dimensions/format needed. Tell the user which tool to paste it into.
  This is a complete deliverable, not a degraded one — say so plainly, don't apologize for it.

If a configured tool call fails (expired key, rate limit, service error), don't retry
indefinitely or fail the task — drop to the next tier and note in your response which tier you
ended up using and why, so the user knows whether to fix a credential.

## Choosing your approach

| Approach | Best for | When to use |
|----------|----------|-------------|
| **AI generation** (Tier 1: Ideogram / Flux / Nano Banana / GPT Image — whichever is configured) | Original images from text prompts | Blog heroes, social graphics, lifestyle/abstract scenes |
| **AI editing** (Nano Banana or GPT Image support in-place editing; Flux Kontext for in-image edits if available) | Modifying an existing image | Background removal, style changes, variations |
| **Canva templates** | Templated, brand-consistent assets | Profile banners, OG image templates, presentations |
| **Screenshot + overlay** | Product UI showcases | Product mockups, feature announcements — AI models hallucinate UI, never generate one |
| **Stock photography** (Tier 3: Unsplash / Pexels) | Generic business/lifestyle scenes | When speed matters more than uniqueness, generation tools aren't configured, or no brand style is established yet |

## Decision tree

```
Need text/headlines in the image?
├── Yes → Canva (typography layer) — never Ideogram for text
└── No ↓

Need product UI in the image?
├── Yes → real screenshot + Canva overlay — never AI-generate a UI
└── No ↓

Need brand-consistent visual style?
├── Yes, a style already exists → Brand_Style_Reference.md prompt starter via Ideogram
├── Yes, no style exists yet → run build-brand-style-reference first, or propose one inline
│    for a one-off if the task doesn't warrant a full style library
└── No → freeform Ideogram generation, grounded in Brand_Style.md colors/imagery direction
```

## Prompting basics (Ideogram)

A strong prompt follows: **Subject + Setting + Style + Lighting + Composition + Technical**

```
A laptop on a minimal white desk showing a dashboard UI silhouette, soft directional
lighting from the left, shallow depth of field, clean commercial photography style,
brand navy color grade, 16:9 aspect ratio
```

Always add "no text, no typography, no lettering, no words, no numbers" explicitly — Ideogram
will attempt to render text from contextual cues otherwise, and it reads as off-brand noise.

**Common mistakes:** too vague ("a business image" — add specifics); no aspect ratio; asking
for embedded text instead of using the Canva overlay step; no style direction
("photorealistic," "flat illustration," "3D render" drastically change output).

## Workflows by asset type

### Blog & article hero images
1. Define the visual concept — what metaphor represents the post's topic?
2. Generate with Ideogram (or note: source from stock photography if no AI budget/time for
   iteration).
3. Standard size: 1200×630 (doubles as the OG image) or 1920×1080 for full-width heroes.
4. Optimize per the checklist below before publishing.
5. Save alongside the blog post it belongs to.

### OG & social preview images
The image shown when a URL is shared on social/Slack/Discord. Required meta tags:
```html
<meta property="og:image" content="https://yoursite.com/og/page-name.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="https://yoursite.com/og/page-name.jpg" />
```
Reuse the blog hero at 1200×630 where one exists rather than generating a separate asset.

### Profile & directory banners
| Platform | Size | Notes |
|----------|------|-------|
| LinkedIn personal cover | 1584×396 | 4:1, safe zone center |
| LinkedIn company cover | 1128×191 | 5.9:1; LinkedIn allows up to 4200×700 |
| Twitter/X header | 1500×500 | 3:1, partially obscured by avatar |
| GitHub social preview | 1280×640 | 2:1, shows in link cards |

Keep text minimal (seen small on mobile), center critical content (edges crop differently per
device), match brand colors/fonts exactly per `Brand_Style.md`.

### Product mockups & screenshots
AI models hallucinate UI — never generate one. Capture a real screenshot at 2x resolution,
frame in a device mockup (browser/laptop/phone), add callout arrows or feature labels via Canva.

### Brand asset exploration
| Asset | AI generation | Canva/manual | Notes |
|-------|:-:|:-:|-------|
| Logo | Poor — inconsistent, not vector | Yes | Always finalize logos manually; AI for concept exploration only |
| Illustrations | Good for style exploration | Depends | AI for concepts, finalize in a design tool |
| Icons | No | Yes | Use platform-provided or licensed icon sets |

## Image optimization checklist

- [ ] Served as WebP with JPEG/PNG fallback
- [ ] Resized to actual display size — don't ship a 4000px image in an 800px container
- [ ] Compressed: target 75-85% quality for photos, near-lossless for screenshots
- [ ] Lazy-loaded below the fold
- [ ] Explicit `width`/`height` attributes set (prevents layout shift)
- [ ] Descriptive, keyword-relevant alt text — not stuffed

## Output routing

Save by asset type, not a single folder:
- Blog hero / OG image → `output\pages\` (alongside the page or post it belongs to)
- Social graphic, profile/directory banner → `output\social\`
- Brand asset exploration / presentation imagery → `output\presentations\` if deck-bound, otherwise `output\social\`
- Raw Ideogram outputs are intermediate working files → `output\ideogram_output\`, finals move to the
  folder above per workspace convention

Filename format: `<type>-<topic>-<yyyy-mm-dd>.<ext>`

## Quality rules

- Never generate a fabricated product UI — screenshot the real thing.
- Every color/font used must trace to `Brand_Style.md` — no off-palette colors, no substituted fonts.
- If `Brand_Style_Reference.md` exists, prefer its named styles over freelancing a new visual
  direction for routine assets — reserve net-new styles for genuinely new formats.
- No fabricated social proof or stats rendered into images — same rule as written copy.

## Related skills

- **`ad-creative`** — paid ad image specs and copy variant matrices
- **`social-creative-designer`** — LinkedIn carousels and platform-specific social graphics
- **`build-brand-style-reference`** — builds the style library this skill reads from
