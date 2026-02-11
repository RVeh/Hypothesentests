"""
CI – Confidence Intervals

Geometric representation, calculations, and simulations.
"""

from .ellipse import plot_ci_ellipse
from .plot import plot_ci
from .simulation import simulate_ci

__all__ = [
    "plot_ci_ellipse",
    "plot_ci",
    "simulate_ci",
]

