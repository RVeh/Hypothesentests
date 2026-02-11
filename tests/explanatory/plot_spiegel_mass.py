 # tests/explanatory/plot_spiegel_mass.py
from __future__ import annotations

import matplotlib.pyplot as plt

from tests.plots.plot_model import plot_binomial_model, ModelPlotStyle


def plot_spiegel_mass(
    *,
    model_alt,
    rejection_region,
    style: ModelPlotStyle,
    save: str | None = None,
):
    """
    Explanatory plot (kein Referenzplot):

    Hebt die Masse im Ablehnungsbereich K hervor.
    Vorbereitung der Power-Idee.
    """

    fig, ax = plt.subplots(figsize=style.figsize)

    plot_binomial_model(
        model=model_alt,
        style=style,
        ax=ax,
    )

    # Masse in K hervorheben
    for k in rejection_region.K:
        ax.bar(
            k,
            model_alt.pmf(k),
            width=style.bar_width,
            color=style.power_pstar_color,
        )

    if save is not None:
        fig.savefig(save, bbox_inches="tight")

    return ax
