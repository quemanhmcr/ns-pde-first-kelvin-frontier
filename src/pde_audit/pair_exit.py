"""Exact physical-exit formulas for killed one-dimensional diffusion.

For dX=sqrt(2 nu)dW on x>0 with absorption at x=0, the survival probability is
S(x,t)=erf(x/sqrt(4 nu t)).  Two independent future replicas from the same fixed
ancestor have pair survival S^2, and the loss rate is the sum of the two physical
exit faces.
"""
from __future__ import annotations

import math


def survival_probability(x: float, nu: float, t: float) -> float:
    if x <= 0.0 or nu <= 0.0 or t <= 0.0:
        raise ValueError("x, nu, t must be positive")
    return math.erf(x / math.sqrt(4.0 * nu * t))


def first_exit_density(x: float, nu: float, t: float) -> float:
    """Positive density -dS/dt, equal to the absorbing heat flux at x=0."""
    if x <= 0.0 or nu <= 0.0 or t <= 0.0:
        raise ValueError("x, nu, t must be positive")
    return x * math.exp(-(x * x) / (4.0 * nu * t)) / (
        2.0 * math.sqrt(math.pi * nu) * t ** 1.5
    )


def pair_survival_probability(x: float, nu: float, t: float) -> float:
    s = survival_probability(x, nu, t)
    return s * s


def pair_exit_rate(x: float, nu: float, t: float) -> float:
    """Positive loss rate -d(S^2)/dt = 2 S f_exit from the two exit faces."""
    s = survival_probability(x, nu, t)
    f = first_exit_density(x, nu, t)
    return 2.0 * s * f
