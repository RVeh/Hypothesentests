import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from intervals.config import (
    PIModelConfig,
    PIGeometryConfig,
    PIStyle,
)


def prediction_interval(p: float, n: int, gamma: float):
    z = norm.ppf((1 + gamma) / 2)
    radius = z * np.sqrt(p * (1 - p) / n)
    return p - radius, p + radius


def plot_pi(
    model: PIModelConfig,
    geometry: PIGeometryConfig,
    style: PIStyle,
    *,
    save: str | None = None,
    show_info: bool = False,
):
    # ----- Geometrie -----
    p = np.linspace(geometry.p_min, geometry.p_max, 3000)

    # ----- Modell --------
    z = norm.ppf((1 + model.gamma) / 2)

    def f(p):
        return p + z * np.sqrt(p * (1 - p) / model.n)

    def g(x):
        return p - z * np.sqrt(p * (1 - p) / model.n)

    # Prognoseintervall am Punkt p
    li, re = prediction_interval(model.p, model.n, model.gamma)

    # ----- Plot -----
    fig, ax = plt.subplots(figsize=style.figsize)

    # Grenzkurven
    ax.plot(p, f(p), color=style.curve_upper)
    ax.plot(p, g(p), color=style.curve_lower)

    ax.fill_between(
    p,
    g(p),
    f(p),
    color=style.area_color,
    alpha=style.area_alpha,
    zorder=0,
)
 
    # Prognoseintervall
    ax.vlines(0, li, re, linewidth=5, color=style.interval_bar)
    ax.vlines(model.p, li, re, linewidth=2, color=style.helper_lines)

    # Hilfslinien
    ax.hlines([li, re], 0, model.p, linestyle=":", color=style.helper_lines)
    ax.vlines(model.p, 0, re, linestyle=":", color=style.helper_lines)

    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(geometry.p_min, geometry.p_max)
    ax.set_ylim(geometry.p_min, geometry.p_max)

    ax.set_xlabel(r"$p$", fontsize=12)
    ax.set_ylabel(r"$h$", fontsize=12)

    if style.grid:
        ax.grid(True, alpha=0.8)

    if style.ticks == "fine":
        ax.minorticks_on()
        ax.tick_params(which="major", length=6)

    ax.set_title(
        rf"$n={model.n},\; p={model.p},\; \gamma={model.gamma}$",
        y=1.02
    )

    if show_info:
        ax.text(
            geometry.p_min + 0.02,
            0.92 * geometry.p_max,
            rf"${model.gamma*100:.0f}\%\text{{-PI}}\approx[{li:.3f};{re:.3f}]$"
        )

    if save is not None:
        fig.savefig(save, bbox_inches="tight")

    plt.show()
    return li, re
