import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from intervals.config import (
    CIModelConfig,
    CIGeometryConfig,
    CIStyle,
)


def plot_ci_ellipse(
    model: CIModelConfig,
    geometry: CIGeometryConfig,
    style: CIStyle,
    *,
    save: str | None = None,
):
    p = np.linspace(geometry.p_min, geometry.p_max, 3000)
    z = norm.ppf((1 + model.gamma) / 2)

    def f(p):
        return p + z * np.sqrt(p * (1 - p) / model.n)

    def g(p):
        return p - z * np.sqrt(p * (1 - p) / model.n)

    fig, ax = plt.subplots(figsize=style.figsize)

    # Grenzkurven
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

    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(geometry.p_min, geometry.p_max)
    ax.set_ylim(geometry.p_min, geometry.p_max)

    ax.set_xlabel(r"$p$",fontsize=12)
    ax.set_ylabel(r"$h$",fontsize=12)

    if style.grid:
        ax.grid(True, alpha=0.8)

    if style.ticks == "fine":
        ax.minorticks_on()
        ax.tick_params(which="major", length=6)

    ax.set_title(
        rf"$n={model.n},\; \gamma={model.gamma}$",
        y=1.02
    )

    if save is not None:
        fig.savefig(save, bbox_inches="tight")

    plt.show()
