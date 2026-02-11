# tests/power/power_function.py
from __future__ import annotations

from typing import Iterable, Callable


def power_at(
    model_alt,
    rejection_region,
) -> float:
    """
    Power an einem alternativen Modell.

    Definition:
        Power = P_{model_alt}(X ∈ K)

    - model_alt: alternatives Modell (z. B. Binomial(n, p))
    - rejection_region: festgelegter Ablehnungsbereich K
      (inkl. aller Setzungen wie alpha, zweiseitig, ...)

    Rückgabe:
        Wahrscheinlichkeit der Verwerfung unter model_alt
    """
    return sum(
        model_alt.pmf(x)
        for x in rejection_region.K
    )


def power_curve(
    model_factory: Callable[[float], object],
    p_values: Iterable[float],
    rejection_region,
):
    """
    Power-Funktion als Abbildung p ↦ Power(p).

    - model_factory(p): erzeugt ein alternatives Modell
      (z. B. Binomial(n, p))
    - p_values: Iterable von wahren Parametern p
    - rejection_region: festgelegter Ablehnungsbereich K

    Rückgabe:
        Liste von Tupeln (p, Power(p))
    """
    result = []

    for p in p_values:
        model_alt = model_factory(p)
        power = power_at(model_alt, rejection_region)
        result.append((p, power))

    return result
