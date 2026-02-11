# tests/utils/format_K.py
from __future__ import annotations

from typing import Iterable


def format_rejection_region_intervals(K: Iterable[int], n: int) -> str:
    """
    Formatiert K ⊂ {0,...,n} in Rand-Intervall-Schreibweise.

    Fälle:
    - beide Ränder:  K = {0,...,l} ∪ {r,...,n}
    - nur links:     K = {0,...,l}
    - nur rechts:    K = {r,...,n}
    - leer:          K = ∅
    """
    Kset = set(K)
    if not Kset:
        return r"$K=\emptyset$"

    # Linker Rand: muss bei 0 beginnen, sonst gibt es keinen linken Tail.
    l = None
    if 0 in Kset:
        l = 0
        while (l + 1) in Kset:
            l += 1

    # Rechter Rand: muss bei n beginnen, sonst gibt es keinen rechten Tail.
    r = None
    if n in Kset:
        r = n
        while (r - 1) in Kset:
            r -= 1

    if l is not None and r is not None:
        return rf"$K=\{{0,\dots,{l}\}}\cup\{{{r},\dots,{n}\}}$"
    if l is not None:
        return rf"$K=\{{0,\dots,{l}\}}$"
    if r is not None:
        return rf"$K=\{{{r},\dots,{n}\}}$"

    # Wenn weder 0 noch n in K sind, ist es kein Randbereich (hier selten).
    # Dann lieber kompakt als Liste: min..max als Hinweis.
    return rf"$K\subseteq\{{0,\dots,{n}\}},\;\min(K)={min(Kset)},\;\max(K)={max(Kset)}$"
