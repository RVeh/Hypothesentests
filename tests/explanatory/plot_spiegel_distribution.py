# tests/explanatory/plot_spiegel_distribution.py
from __future__ import annotations

import matplotlib.pyplot as plt

from tests.plots.plot_model import ModelPlotStyle


def plot_spiegel_distribution(
    *,
    model_alt,
    model_null,
    rejection_region,
    style: ModelPlotStyle,
    save: str | None = None,
):
    """
    Explanatory plot (kein Referenzplot).

    Darstellung:
    - H0-Verteilung oberhalb der x-Achse (fix)
      * rot: Ablehnung unter H0 (α)
    - H1-Verteilung gespiegelt unterhalb der x-Achse (beweglich)
      * grün: Masse von H1 in K (Power)
      * hellblau: restliche Masse
    - x-Achse ist Spiegelachse
    """

    fig, ax = plt.subplots(figsize=style.figsize)

    # -------------------------------------------------
    # x-Bereich: sigma-basiert (jetzt wirksam!)
    # -------------------------------------------------
    mu = model_null.n * model_null.p
    sigma = (model_null.n * model_null.p * (1 - model_null.p)) ** 0.5

    xmin = max(0, int(mu - style.sigma_range * sigma))
    xmax = min(model_null.n, int(mu + style.sigma_range * sigma))

    ax.set_xlim(xmin, xmax)

    # -------------------------------------------------
    # H0-Verteilung (oben, fix)
    # -------------------------------------------------
    for k in model_null.support:
        if k < xmin or k > xmax:
            continue

        if k in rejection_region.K:
            color = style.reject_color      # rot: Ablehnung unter H0
        else:
            color = style.model_color       # blau: akzeptiert

        ax.bar(
            k,
            model_null.pmf(k),
            width=style.bar_width,
            color=color,
            edgecolor="black",
            linewidth=0.5,
            zorder=2,
        )

    # -------------------------------------------------
    # H1-Verteilung gespiegelt (unten, beweglich)
    # -------------------------------------------------
    for k in model_alt.support:
        if k < xmin or k > xmax:
            continue

        if k in rejection_region.K:
            color = style.power_pstar_color   # grün: Power-Masse
        else:
            color = "lightblue"               # nicht verworfen

        ax.bar(
            k,
            -model_alt.pmf(k),   # echte Spiegelung
            width=style.bar_width,
            color=color,
            edgecolor="black",
            linewidth=0.3,
            zorder=2,
        )

    # -------------------------------------------------
    # Spiegelachse & y-Achse
    # -------------------------------------------------
    ax.axhline(0, color="black", linewidth=1)

    ymax = max(model_null.pmf(k) for k in range(xmin, xmax + 1))
    ax.set_ylim(-1.2 * ymax, 1.2 * ymax)

    ax.set_xlabel(r"Anzahl der Erfolge $k$")
    ax.set_ylabel(r"$P(X = k)$")

    ax.tick_params(labelsize=style.tick_fontsize)

    # -------------------------------------------------
    # Dezente Orientierung rechts (keine Legende!)
    # -------------------------------------------------
    ax.text(
        0.8,
        0.90,
        rf"$H_0:\ p={model_null.p}$",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=style.tick_fontsize,
        color="gray",
    )

    ax.text(
        0.8,
        0.84,
        rf"$H_1:\ p={model_alt.p}$",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=style.tick_fontsize,
        color="gray",
    )

    # Kein Titel, kein Subtitel, kein Textblock
    # (Teil einer erklärenden Sequenz)

    if save is not None:
        fig.savefig(save, bbox_inches="tight")

    return ax
