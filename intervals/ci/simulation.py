from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from intervals.ci.calculations import wilson_ci
from intervals.config import (
    CISimModelConfig,
    CISimControlConfig,
    CISimGeometryConfig,
    CISimStyle,
)


def simulate_ci(
    model: CISimModelConfig,
    control: CISimControlConfig,
    geometry: CISimGeometryConfig,
    style: CISimStyle,
    *,
    save: str | None = None,
):
    # --- Zufallsquelle ---
    rng = np.random.default_rng(control.seed)
    X = rng.binomial(model.n, model.p_true, size=control.m)

    intervals = np.empty((control.m, 2))
    cover = np.empty(control.m, dtype=bool)

    # --- Simulation ---
    for i, k in enumerate(X):
        h = k / model.n
        L, R = wilson_ci(h, model.n, model.gamma)
        intervals[i] = (L, R)
        cover[i] = (L <= model.p_true <= R)

    coverage_rate = cover.mean()

    # --- Plot ---
    fig, ax = plt.subplots(figsize=style.figsize)
    y = np.arange(1, control.m + 1)

    for i, (L, R) in enumerate(intervals):
        color = style.color_cover if cover[i] else style.color_miss
        ax.hlines(y[i], L, R, linewidth=1.2, color=color)

    ax.axvline(model.p_true, linewidth=1.0, color="gray")

    ax.set_ylim(0, control.m + 1)
    ax.set_xlim(geometry.x_min, geometry.x_max)
    ax.set_xlabel(r"$p$", fontsize=12)
    ax.set_ylabel("Realisierung", fontsize=12)

    if style.show_stats:
        ax.set_title(
            rf"{control.m} Intervalle (Wilson), "
            rf"$n={model.n}, \gamma={model.gamma}$" "\n"
            rf"Trefferquote $\approx {coverage_rate:.2f}$ | Seed {control.seed}"
        )
    else:
        ax.set_title(rf"$n={model.n}, \gamma={model.gamma}$")

    fig.tight_layout()

    if save is not None:
        fig.savefig(save, bbox_inches="tight")

    plt.show()
    plt.close(fig)

    return float(coverage_rate)
