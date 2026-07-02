"""
Brand Chart Template
--------------------
Base template for generating branded static charts (PNG) using matplotlib.
CONFIGURE before use: update BRAND_PRIMARY, BRAND_ACCENT, BRAND_FONT below
with values from _context/Brand_Style.md for the active brand.

Usage:
  Adapt the DATA and CONFIG sections below for your specific chart.
  Run: python chart_template.py
  Output: chart_output.png in the same directory
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import rcParams
import numpy as np
import os

# ─── BRAND COLORS — load from _context/Brand_Style.md before use ───────────────
BRAND_PRIMARY   = "#REPLACE_WITH_BRAND_PRIMARY"    # main series color
BRAND_ACCENT    = "#REPLACE_WITH_BRAND_ACCENT"     # highlight / secondary series
WHITE           = "#FFFFFF"
CHARCOAL        = "#1A1A1A"
LIGHT_GREY      = "#E8E8E8"

# Color palette for multi-series charts (extend as needed)
PALETTE = [BRAND_PRIMARY, BRAND_ACCENT, CHARCOAL, "#D4D4D4", "#6B7280"]

# ─── TYPOGRAPHY ────────────────────────────────────────────────────────────────
# Try to load Montserrat; fall back gracefully if not installed
try:
    rcParams["font.family"] = "Montserrat"
except Exception:
    rcParams["font.family"] = "DejaVu Sans"

rcParams["font.size"] = 11
rcParams["axes.labelcolor"] = CHARCOAL
rcParams["xtick.color"] = CHARCOAL
rcParams["ytick.color"] = CHARCOAL
rcParams["text.color"] = CHARCOAL

# ─── DATA — REPLACE THIS SECTION ───────────────────────────────────────────────
# Example: bar chart of CPL by channel
CHART_TITLE = "Cost Per Lead by Channel — Q1 2026"
X_LABEL     = "Channel"
Y_LABEL     = "Cost Per Lead (USD)"
SOURCE      = "Source: Campaign Analytics, Q1 2026"

# Categories and values (replace with your actual data)
categories = ["LinkedIn Ads", "Google Search", "Email", "Display", "Organic"]
values     = [320, 185, 45, 210, 0]  # 0 for organic = no paid cost
colors     = [NAVY, RED, NAVY, RED, LIGHT_GREY]  # per-bar color override

# ─── CHART CONFIG ──────────────────────────────────────────────────────────────
CHART_TYPE    = "bar"        # "bar" | "barh" | "line" | "multiline" | "doughnut"
FIGURE_SIZE   = (10, 6)      # width, height in inches
DPI           = 150          # output resolution
OUTPUT_FILE   = "chart_output.png"

SHOW_DATA_LABELS = True      # show values on top of bars
SHOW_GRID        = True      # horizontal grid lines
SHOW_LEGEND      = False     # set True for multi-series charts

# ─── CHART BUILDER ─────────────────────────────────────────────────────────────

def apply_brand_style(ax, fig):
    """Apply brand styling to any matplotlib axes object."""
    fig.patch.set_facecolor(WHITE)
    ax.set_facecolor(WHITE)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(LIGHT_GREY)
    ax.spines["bottom"].set_color(LIGHT_GREY)
    if SHOW_GRID:
        ax.yaxis.grid(True, color=LIGHT_GREY, linewidth=0.8, zorder=0)
        ax.set_axisbelow(True)
    ax.tick_params(axis="both", which="both", length=0)


def add_data_labels_bar(ax, bars, fmt="{:.0f}"):
    """Add value labels above each bar."""
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.annotate(
                fmt.format(height),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 6),
                textcoords="offset points",
                ha="center", va="bottom",
                fontsize=10, color=CHARCOAL, fontweight="bold"
            )


def add_source_annotation(fig, source_text):
    """Add a source attribution line at the bottom of the figure."""
    fig.text(
        0.02, 0.01, source_text,
        ha="left", va="bottom",
        fontsize=8, color="#6B7280", style="italic"
    )


def build_bar_chart():
    fig, ax = plt.subplots(figsize=FIGURE_SIZE, dpi=DPI)
    apply_brand_style(ax, fig)

    bars = ax.bar(
        categories, values,
        color=colors if len(colors) == len(categories) else NAVY,
        width=0.55, zorder=3, edgecolor=WHITE, linewidth=0.5
    )

    if SHOW_DATA_LABELS:
        add_data_labels_bar(ax, bars)

    ax.set_title(CHART_TITLE, fontsize=14, fontweight="bold", color=CHARCOAL,
                 loc="left", pad=16)
    ax.set_xlabel(X_LABEL, fontsize=11, labelpad=10)
    ax.set_ylabel(Y_LABEL, fontsize=11, labelpad=10)
    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels(categories, fontsize=10)

    add_source_annotation(fig, SOURCE)
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return fig


def build_barh_chart():
    fig, ax = plt.subplots(figsize=FIGURE_SIZE, dpi=DPI)
    apply_brand_style(ax, fig)

    y_pos = np.arange(len(categories))
    bars = ax.barh(y_pos, values, color=NAVY, height=0.55, zorder=3)

    for bar in bars:
        width = bar.get_width()
        ax.annotate(f"{width:.0f}",
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(6, 0), textcoords="offset points",
                    ha="left", va="center", fontsize=10, color=CHARCOAL, fontweight="bold")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, fontsize=10)
    ax.invert_yaxis()
    ax.set_title(CHART_TITLE, fontsize=14, fontweight="bold", color=CHARCOAL, loc="left", pad=16)
    ax.set_xlabel(Y_LABEL, fontsize=11, labelpad=10)
    ax.xaxis.grid(True, color=LIGHT_GREY, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    add_source_annotation(fig, SOURCE)
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return fig


def build_line_chart():
    """For single-series line chart. For multi-series, edit to pass a dict of {label: values}."""
    fig, ax = plt.subplots(figsize=FIGURE_SIZE, dpi=DPI)
    apply_brand_style(ax, fig)

    ax.plot(categories, values, color=NAVY, linewidth=2.5, marker="o",
            markersize=7, markerfacecolor=RED, markeredgecolor=WHITE, markeredgewidth=1.5,
            zorder=3)

    if SHOW_DATA_LABELS:
        for x, y in zip(categories, values):
            ax.annotate(f"{y:.0f}", xy=(x, y), xytext=(0, 10),
                        textcoords="offset points", ha="center", fontsize=9, color=CHARCOAL)

    ax.set_title(CHART_TITLE, fontsize=14, fontweight="bold", color=CHARCOAL, loc="left", pad=16)
    ax.set_xlabel(X_LABEL, fontsize=11, labelpad=10)
    ax.set_ylabel(Y_LABEL, fontsize=11, labelpad=10)

    add_source_annotation(fig, SOURCE)
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    return fig


def build_doughnut_chart():
    """For proportion charts (use 2–4 segments only)."""
    fig, ax = plt.subplots(figsize=(7, 7), dpi=DPI)
    fig.patch.set_facecolor(WHITE)

    wedge_colors = [NAVY, RED, "#1A1A2E", LIGHT_GREY][:len(categories)]
    wedges, texts, autotexts = ax.pie(
        values, labels=None,
        colors=wedge_colors,
        autopct="%1.0f%%", pctdistance=0.75,
        startangle=90, wedgeprops=dict(width=0.55, edgecolor=WHITE, linewidth=2)
    )
    for autotext in autotexts:
        autotext.set_fontsize(11)
        autotext.set_fontweight("bold")
        autotext.set_color(WHITE)

    legend_patches = [mpatches.Patch(color=wedge_colors[i], label=categories[i])
                      for i in range(len(categories))]
    ax.legend(handles=legend_patches, loc="lower center", bbox_to_anchor=(0.5, -0.12),
              ncol=2, fontsize=10, frameon=False)

    ax.set_title(CHART_TITLE, fontsize=14, fontweight="bold", color=CHARCOAL, pad=20)
    add_source_annotation(fig, SOURCE)
    plt.tight_layout()
    return fig


# ─── MAIN ──────────────────────────────────────────────────────────────────────

CHART_BUILDERS = {
    "bar":      build_bar_chart,
    "barh":     build_barh_chart,
    "line":     build_line_chart,
    "multiline": build_line_chart,  # extend build_line_chart for multi-series
    "doughnut": build_doughnut_chart,
}

if __name__ == "__main__":
    builder = CHART_BUILDERS.get(CHART_TYPE)
    if not builder:
        raise ValueError(f"Unknown CHART_TYPE '{CHART_TYPE}'. Choose from: {list(CHART_BUILDERS.keys())}")

    fig = builder()
    output_path = os.path.join(os.path.dirname(__file__), OUTPUT_FILE)
    fig.savefig(output_path, dpi=DPI, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print(f"Chart saved to: {output_path}")
