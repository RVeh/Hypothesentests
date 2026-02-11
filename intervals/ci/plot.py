from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from intervals.pi.plot import prediction_interval

from intervals.config import (
    CIModelConfig,
    CIGeometryConfig,
    CIStyle,
)
from intervals.ci.calculations import wilson_ci


def plot_ci(
    model: CIModelConfig,
    geometry: CIGeometryConfig,
    style: CIStyle,
    *,
    save: str | None = None,
    show_info: bool = False,
):
    # --- Geometrie ---
    p = np.linspace(geometry.p_min, geometry.p_max, geometry.points)

    # --- Modell ---
    z = norm.ppf((1 + model.gamma) / 2)

    def f(x):
        return x + z * np.sqrt(x * (1 - x) / model.n)

    def g(x):
        return x - z * np.sqrt(x * (1 - x) / model.n)

    # Wilson-Intervall
    p_L, p_R = wilson_ci(model.h, model.n, model.gamma)


    # --- Plot ---
    fig, ax = plt.subplots(figsize=style.figsize)

    ax.plot(p, f(p), color=style.curve_lower)
    ax.plot(p, g(p), color=style.curve_upper)

    ax.fill_between(
    p,
    g(p),
    f(p),
    color=style.area_color,
    alpha=style.area_alpha,
    zorder=0,
)

    ax.hlines(0, p_L, p_R, linewidth=5, color=style.ci_bar)

    ax.hlines(model.h, 0, 1, linestyle=":", color=style.helper_lines)
    ax.hlines(model.h, p_L, p_R, linewidth=2, color=style.helper_lines)
    ax.vlines([p_L, p_R], 0, model.h, linestyle=":", color=style.helper_lines)

    if style.show_prediction_overlay:
        p_vals = np.linspace(p_L, p_R, style.prediction_steps)

        for p in p_vals:
            li_p, re_p = prediction_interval(p, model.n, model.gamma)
            ax.vlines(
                p,
                li_p,
                re_p,
                color=style.helper_lines,
                linewidth=1.2,
                alpha=style.prediction_alpha,
                zorder=3,
            )
    
    ax.set_xlim(geometry.p_min, geometry.p_max)
    ax.set_ylim(geometry.p_min, geometry.p_max)
    ax.set_aspect("equal", adjustable="box")

    ax.set_xlabel(r"$p$", fontsize=12)
    ax.set_ylabel(r"$h$", fontsize=12)

    ax.set_title(
        rf"$n={model.n},\; h={model.h},\; \gamma={model.gamma}$"
    )

    if style.grid:
        ax.grid(True, alpha=0.8)

    if style.ticks == "fine":
        ax.minorticks_on()
        ax.tick_params(which="major", length=6)

    if show_info:
        ax.text(
            geometry.p_min + 0.02,
            0.92 * geometry.p_max,
            rf"${model.gamma*100:.0f}\%\text{{-KI}}\approx[{p_L:.3f};{p_R:.3f}]$"
        )

    if save is not None:
        fig.savefig(save, bbox_inches="tight")

    plt.show()
    return p_L, p_R
