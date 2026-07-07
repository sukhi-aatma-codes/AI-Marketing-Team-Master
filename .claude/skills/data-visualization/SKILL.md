---
name: data-visualization
description: >
  Use this skill whenever the user wants to turn data into a chart, graph, visual table,
  or interactive visualization. Trigger on requests like "visualize this data", "make a
  chart of these numbers", "create a graph showing X", "plot this", "turn this table into
  a visualization", "show me a trend chart for Y", or any time the user shares a dataset
  and wants it displayed visually. Also trigger when another skill (campaign-report,
  keyword-research, market-research) produces data that would benefit from a visual.
  Produces an interactive HTML file (Chart.js) — works in any browser with no server needed.
  Also produces a Python script for static PNG output when needed.
---

# Data Visualization

Converts raw data into branded interactive charts and visual tables. Primary output is a
self-contained HTML file with Chart.js — embeds data inline, renders in browser with hover,
zoom, and tooltips. No server or dependencies required. Also produces a Python script for
static PNG output. Both use brand colors loaded at runtime from `_context/Brand_Style.md`.

## Before starting

Read this context file:
- `_context/Brand_Style.md` — exact hex values, typography, visual standards

Read the brand color values and font name from `Brand_Style.md` before generating any chart. Apply them consistently across all outputs. Do not default to any hardcoded values.

## Chart type selection guide

Choose based on what the data needs to communicate:

| Chart type | Use when |
|-----------|---------|
| Bar (vertical) | Comparing discrete categories (e.g., CPL by channel) |
| Bar (horizontal) | Many categories, long labels (e.g., keyword rankings) |
| Line | Showing trends over time (e.g., monthly leads) |
| Multi-line | Comparing trends across 2–3 series |
| Stacked bar | Part-to-whole over time or across categories |
| Scatter | Correlation between two variables |
| Doughnut / Pie | Simple proportion (2–4 segments only — more than 4 use bars) |
| Table (styled) | Precise numbers matter more than pattern — use for KPI dashboards |
| Funnel | Conversion stages (impression → click → MQL → deal) |

If the user hasn't specified a type, recommend the best fit and explain why in one sentence.

## Workflow

### Step 1 — Understand the data
- What are the dimensions (categories, time periods, groups)?
- What is the key message this chart needs to communicate?
- How many data series? (more than 3 series on one chart rarely works)

### Step 2 — Write structured `.md`
Save as `output/reports/dataviz-<topic>-<date>.md` including:
- Data table (exact numbers the chart uses)
- Chart type selected and rationale
- Key message / headline the chart should communicate
- Source attribution

### Step 3 — Generate interactive HTML (Chart.js)
Produce a self-contained HTML file:
- Embed the data inline as a JavaScript JSON object (no external data file needed)
- Use Chart.js loaded from CDN
- Apply brand colors from `Brand_Style.md` — primary color for main series, accent for highlights
- Load brand font from Google Fonts (font name from `Brand_Style.md`); use for all labels and title
- Include chart title, axis labels, data source annotation
- Enable tooltips with hover; enable legend if multiple series
- Add a thin navy border radius on bar charts for polish
- The HTML file must work by double-clicking — no server, no Python, no build step

Save as `output/reports/dataviz-<topic>-<date>.html`

Example Chart.js color config structure (populate hex values from `Brand_Style.md`):
```javascript
backgroundColor: ['<brand-primary>', '<brand-accent>', '<brand-neutral-dark>', '<brand-neutral-light>'],
borderColor: ['<brand-primary>', '<brand-accent>', '<brand-neutral-dark>', '<brand-neutral-light>'],
```

### Step 4 — Generate Python script (optional, for static PNG)
Use the bundled `scripts/chart_template.py` as the base. Adapt it to the specific data and
chart type. The script produces a PNG with identical brand styling.

Save the adapted script as `output/reports/dataviz-<topic>-<date>.py`

Only produce this if the user asks for a static image, or if the visualization is destined
for `social-creative-designer` (the brand's data-focused style from `Brand_Style_Reference.md`).

### Step 5 — Social handoff (optional)
If the user wants a social-ready version of the chart, pass the chart spec and data to
`social-creative-designer`, using the data/stat-focused style defined in the active brand's
`Brand_Style_Reference.md`. The social-creative-designer skill handles the branded
carousel/single-image output — this skill handles the data layer only.

## Bundled script

`.claude/skills/data-visualization/scripts/chart_template.py` — matplotlib + Plotly starter with:
- Brand color and font placeholders — set them from `_context/Brand_Style.md` before running
- Falls back to system sans-serif if the brand font isn't installed
- Brand grid style (light grey horizontal rules, white background)
- Standard figure size, DPI, tight layout

Read this file and adapt it rather than writing chart code from scratch.

## Quality checklist

- [ ] Chart type matches the data story — rationale stated in `.md`
- [ ] Brand colors applied correctly (navy primary, red accent)
- [ ] HTML file is self-contained — opens in browser without any server or extra files
- [ ] Chart has title, axis labels, and source annotation
- [ ] Data in the `.md` matches data in the chart exactly — no rounding differences
- [ ] Python script generated if static PNG was requested
