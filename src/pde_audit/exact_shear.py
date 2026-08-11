"""Exact formulas for the periodic Navier--Stokes shear calibration.

We normalize spatial integration by torus volume, so <cos(k y)^2> = 1/2.
For odd k_m=2m-1,

    u_N(y,t) = N^{-1/2} sum_m exp(-nu k_m^2 t) cos(k_m y) e_x

is an exact 3D periodic Navier--Stokes solution with constant pressure because
(u_N . grad) u_N vanishes identically.
"""
from __future__ import annotations

import math


def odd_wavenumbers(N: int) -> list[int]:
    if N <= 0:
        raise ValueError("N must be positive")
    return [2 * m - 1 for m in range(1, N + 1)]


def horizon(N: int, nu: float, c: float) -> float:
    return c / (nu * N * N)


def circulation_traffic_integral(N: int, nu: float, c: float) -> float:
    """Integral_0^T <|u_N|^2> dt, exactly in the normalized torus measure."""
    T = horizon(N, nu, c)
    return sum(
        (1.0 - math.exp(-2.0 * nu * k * k * T)) / (4.0 * nu * N * k * k)
        for k in odd_wavenumbers(N)
    )


def hodge_green_bank_initial(N: int) -> float:
    """(1/2)<u_N,(-Delta)^(-1)u_N> at t=0 in normalized torus measure."""
    return sum(1.0 / (k * k) for k in odd_wavenumbers(N)) / (4.0 * N)


def gaussian_cos_mean(a: float) -> float:
    return math.exp(-0.5 * a * a)


def gaussian_cos_product_mean(a: float, b: float) -> float:
    return 0.5 * (
        math.exp(-0.5 * (a - b) * (a - b))
        + math.exp(-0.5 * (a + b) * (a + b))
    )


def kelvin_terminal_moments(N: int, c: float, L: float = 1.0) -> tuple[float, float, float]:
    """Exact E[X_N], E[X_N^2], Var(X_N) for the rectangular circulation.

    X_N = (2L/sqrt(N)) sum_m cos(k_m sqrt(2c) Z / N), Z~N(0,1).
    No Monte Carlo is used.
    """
    ks = odd_wavenumbers(N)
    scale = math.sqrt(2.0 * c) / N
    coeff = 2.0 * L / math.sqrt(N)
    alphas = [k * scale for k in ks]
    mean = coeff * sum(gaussian_cos_mean(a) for a in alphas)
    second = coeff * coeff * sum(
        gaussian_cos_product_mean(a, b) for a in alphas for b in alphas
    )
    var = second - mean * mean
    # Roundoff may produce a tiny negative value only at machine epsilon.
    if var < 0.0 and abs(var) < 1e-12:
        var = 0.0
    return mean, second, var



def kelvin_anchor_moments(
    N: int, c: float, anchor: float, L: float = 1.0
) -> tuple[float, float, float]:
    """Exact Gaussian moments for the rectangular circulation at anchor ``anchor``.

    X_N(a)=(2L/sqrt(N)) sum_m cos(k_m(a+sqrt(2c) Z/N)), Z~N(0,1).
    """
    ks = odd_wavenumbers(N)
    scale = math.sqrt(2.0 * c) / N
    coeff = 2.0 * L / math.sqrt(N)
    mean = coeff * sum(
        math.cos(k * anchor) * math.exp(-0.5 * (k * scale) ** 2) for k in ks
    )
    second = coeff * coeff * sum(
        0.5
        * (
            math.cos(k * anchor - ell * anchor)
            * math.exp(-0.5 * ((k - ell) * scale) ** 2)
            + math.cos(k * anchor + ell * anchor)
            * math.exp(-0.5 * ((k + ell) * scale) ** 2)
        )
        for k in ks
        for ell in ks
    )
    var = second - mean * mean
    if var < 0.0 and abs(var) < 1e-12:
        var = 0.0
    return mean, second, var


def kelvin_anchor_covariance(
    N: int, c: float, anchor_a: float, anchor_b: float, L: float = 1.0
) -> float:
    """Exact covariance of two rectangular Kelvin payoffs at anchors a,b."""
    ks = odd_wavenumbers(N)
    scale = math.sqrt(2.0 * c) / N
    coeff = 2.0 * L / math.sqrt(N)
    mean_a = coeff * sum(
        math.cos(k * anchor_a) * math.exp(-0.5 * (k * scale) ** 2) for k in ks
    )
    mean_b = coeff * sum(
        math.cos(k * anchor_b) * math.exp(-0.5 * (k * scale) ** 2) for k in ks
    )
    cross = coeff * coeff * sum(
        0.5
        * (
            math.cos(k * anchor_a - ell * anchor_b)
            * math.exp(-0.5 * ((k - ell) * scale) ** 2)
            + math.cos(k * anchor_a + ell * anchor_b)
            * math.exp(-0.5 * ((k + ell) * scale) ** 2)
        )
        for k in ks
        for ell in ks
    )
    return cross - mean_a * mean_b


def kelvin_increment_variance(
    N: int, c: float, anchor_a: float, anchor_b: float, L: float = 1.0
) -> float:
    """Var(X_b-X_a), reconstructed only from exact covariance data."""
    va = kelvin_anchor_moments(N, c, anchor_a, L)[2]
    vb = kelvin_anchor_moments(N, c, anchor_b, L)[2]
    cab = kelvin_anchor_covariance(N, c, anchor_a, anchor_b, L)
    return va + vb - 2.0 * cab
