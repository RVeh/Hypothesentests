from dataclasses import dataclass

@dataclass
class PIConfig:
    p: float
    n: int
    gamma: float = 0.95

    p_min: float = 0.0
    p_max: float = 1.0
    figsize: tuple = (4, 4)


import numpy as np
from scipy.stats import norm

def prediction_interval(p, n, gamma):
    z = norm.ppf((1 + gamma) / 2)
    radius = z * np.sqrt(p * (1 - p) / n)
    return p - radius, p + radius


@dataclass
class CIStyle:
    curve_upper: str = "black"
    curve_lower: str = "green"
    interval_bar: str = "blue"
    helper_lines: str = "gray"

    grid: bool = True
    ticks: str = "normal"   # "normal" | "fine"


import matplotlib.pyplot as plt
import numpy as np

def plot_pi(cfg, style=None, save=None, show_info=True):
    if style is None:
        style = CIStyle()

    x = np.linspace(cfg.p_min, cfg.p_max, 3000)
    z = norm.ppf((1 + cfg.gamma) / 2)

    def f(x): return x + z * np.sqrt(x * (1 - x) / cfg.n)
    def g(x): return x - z * np.sqrt(x * (1 - x) / cfg.n)

    li, re = prediction_interval(cfg.p, cfg.n, cfg.gamma)

    fig, ax = plt.subplots(figsize=cfg.figsize)

    # Grenzkurven
    ax.plot(x, f(x), color=style.curve_upper)
    ax.plot(x, g(x), color=style.curve_lower)

    # Prognoseintervall
    ax.vlines(0, li, re, linewidth=5, color=style.interval_bar)
    ax.vlines(cfg.p, li, re, linewidth=2, color=style.helper_lines)

    # Hilfslinien
    ax.hlines([li, re], 0, cfg.p, linestyle=":", color=style.helper_lines)
    ax.vlines(cfg.p, 0, re, linestyle=":", color=style.helper_lines)

    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(cfg.p_min, cfg.p_max)
    ax.set_ylim(cfg.p_min, cfg.p_max)

    ax.set_xlabel(r"$p$",fontsize=12)
    ax.set_ylabel(r"$h$",fontsize=12)
    
    if style.grid:
        ax.grid(True, alpha=0.8)

    if style.ticks == "fine":
        ax.minorticks_on()
        ax.tick_params(which="major", length=6)

    ax.set_title(
        rf"$n={cfg.n},\; p={cfg.p},\; \gamma={cfg.gamma}$",
        y=1.02
    )

    if show_info:
        ax.text(
            cfg.p_min + 0.01,
            0.92 * cfg.p_max,
            rf"{cfg.gamma*100:.0f}%-PI$\approx$[{li:.3f};{re:.3f}]"
        )

    if save is not None:
        fig.savefig(save, bbox_inches="tight")

    plt.show()
    return li, re
