"""Shared plot styling for Credit-Card-Risk-Detection (UIbit)."""

import matplotlib.pyplot as plt
import seaborn as sns

# UIbit brand palette
COLORS = {
    "primary": "#2563EB",
    "secondary": "#1E40AF",
    "accent": "#0EA5E9",
    "legit": "#10B981",
    "fraud": "#EF4444",
    "neutral": "#64748B",
    "background": "#F8FAFC",
    "text": "#0F172A",
}

PALETTE = [COLORS["primary"], COLORS["fraud"], COLORS["legit"], COLORS["accent"], COLORS["secondary"]]


def apply_uibit_theme():
    """Apply consistent matplotlib/seaborn styling across notebooks."""
    sns.set_theme(
        style="whitegrid",
        palette=PALETTE,
        font_scale=1.05,
        rc={
            "figure.facecolor": COLORS["background"],
            "axes.facecolor": "#FFFFFF",
            "axes.edgecolor": COLORS["neutral"],
            "axes.labelcolor": COLORS["text"],
            "axes.titleweight": "bold",
            "axes.titlesize": 14,
            "grid.color": "#E2E8F0",
            "grid.linestyle": "--",
            "grid.alpha": 0.7,
            "text.color": COLORS["text"],
            "xtick.color": COLORS["text"],
            "ytick.color": COLORS["text"],
            "legend.frameon": True,
            "legend.facecolor": "#FFFFFF",
            "legend.edgecolor": "#E2E8F0",
        },
    )
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.rcParams["figure.dpi"] = 110
