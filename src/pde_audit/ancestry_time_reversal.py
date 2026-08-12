"""Exact weighted-diffusion forward/backward drift algebra for the ancestry law.

For the repository's normalized ancestry operator

    L psi = w.grad psi + nu/phi div(phi K grad psi),
    q = f phi,

with symmetric diffusion tensor K, the expanded forward Ito drift is not w when K
or phi varies.  This module derives the forward drift b_+, the time-reversed drift
b_-, and proves that the stored current velocity j=w-nu K grad log f is exactly
their midpoint.

This is generator/time-orientation algebra only.  It does not identify the ancestry
state with the physical backward Kelvin current-shape state.
"""
from __future__ import annotations

from typing import Sequence

import sympy as sp

Matrix = sp.MatrixBase


def gradient(expr: sp.Expr, coords: Sequence[sp.Symbol]) -> sp.Matrix:
    return sp.Matrix([sp.diff(expr, x) for x in coords])


def weighted_diffusion_connection(
    K: Matrix,
    phi: sp.Expr,
    coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    """c_phi with component j = phi^-1 sum_i partial_i(phi K_ij)."""
    n = len(coords)
    if K.shape != (n, n):
        raise ValueError("K must match the coordinate dimension")
    return sp.Matrix([
        sp.simplify(sum(sp.diff(phi * K[i, j], coords[i]) for i in range(n)) / phi)
        for j in range(n)
    ])


def expanded_forward_drift(
    w: Matrix,
    K: Matrix,
    phi: sp.Expr,
    coords: Sequence[sp.Symbol],
    nu: sp.Expr,
) -> sp.Matrix:
    """Ito drift b_+=w+nu c_phi of the weighted backward operator."""
    return sp.simplify(w + nu * weighted_diffusion_connection(K, phi, coords))


def diffusion_divergence_density(
    K: Matrix,
    q: sp.Expr,
    coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    """Column divergence with component j = sum_i partial_i(K_ij q)."""
    n = len(coords)
    if K.shape != (n, n):
        raise ValueError("K must match the coordinate dimension")
    return sp.Matrix([
        sp.simplify(sum(sp.diff(K[i, j] * q, coords[i]) for i in range(n)))
        for j in range(n)
    ])


def forward_probability_current(
    w: Matrix,
    K: Matrix,
    phi: sp.Expr,
    f: sp.Expr,
    coords: Sequence[sp.Symbol],
    nu: sp.Expr,
) -> sp.Matrix:
    """Fokker-Planck current q b_+ - nu div(K q), q=f phi."""
    q = sp.simplify(f * phi)
    bplus = expanded_forward_drift(w, K, phi, coords, nu)
    return sp.simplify(q * bplus - nu * diffusion_divergence_density(K, q, coords))


def repository_current_velocity(
    w: Matrix,
    K: Matrix,
    f: sp.Expr,
    coords: Sequence[sp.Symbol],
    nu: sp.Expr,
) -> sp.Matrix:
    """j=w-nu K grad log f, assuming symmetric K as in the diffusion tensor."""
    return sp.simplify(w - nu * K * gradient(sp.log(f), coords))


def reversed_drift(
    w: Matrix,
    K: Matrix,
    phi: sp.Expr,
    f: sp.Expr,
    coords: Sequence[sp.Symbol],
    nu: sp.Expr,
) -> sp.Matrix:
    """Backward/time-reversed Ito drift b_-=b_+-2nu q^-1 div(Kq)."""
    q = sp.simplify(f * phi)
    bplus = expanded_forward_drift(w, K, phi, coords, nu)
    return sp.simplify(
        bplus - 2 * nu * diffusion_divergence_density(K, q, coords) / q
    )


def midpoint_current_residual(
    w: Matrix,
    K: Matrix,
    phi: sp.Expr,
    f: sp.Expr,
    coords: Sequence[sp.Symbol],
    nu: sp.Expr,
) -> sp.Matrix:
    """Residual of j=(b_++b_-)/2."""
    bplus = expanded_forward_drift(w, K, phi, coords, nu)
    bminus = reversed_drift(w, K, phi, f, coords, nu)
    j = repository_current_velocity(w, K, f, coords, nu)
    return sp.simplify((bplus + bminus) / 2 - j)


def probability_current_residual(
    w: Matrix,
    K: Matrix,
    phi: sp.Expr,
    f: sp.Expr,
    coords: Sequence[sp.Symbol],
    nu: sp.Expr,
) -> sp.Matrix:
    """Residual of physical Fokker-Planck current J=q j."""
    q = sp.simplify(f * phi)
    J = forward_probability_current(w, K, phi, f, coords, nu)
    j = repository_current_velocity(w, K, f, coords, nu)
    return sp.simplify(J - q * j)


def forward_drift_required_for_backward_kelvin(
    u_backward: Matrix,
    K: Matrix,
    phi: sp.Expr,
    f: sp.Expr,
    coords: Sequence[sp.Symbol],
    nu: sp.Expr,
) -> sp.Matrix:
    """w required so that the time-reversed drift b_- equals physical backward drift u."""
    cphi = weighted_diffusion_connection(K, phi, coords)
    return sp.simplify(u_backward + nu * cphi + 2 * nu * K * gradient(sp.log(f), coords))


def backward_kelvin_matching_residual(
    u_backward: Matrix,
    K: Matrix,
    phi: sp.Expr,
    f: sp.Expr,
    coords: Sequence[sp.Symbol],
    nu: sp.Expr,
) -> sp.Matrix:
    """Residual b_--u after choosing the exact required forward ancestry drift w."""
    w = forward_drift_required_for_backward_kelvin(u_backward, K, phi, f, coords, nu)
    return sp.simplify(reversed_drift(w, K, phi, f, coords, nu) - u_backward)


def naive_w_equals_u_mismatch(
    u_backward: Matrix,
    K: Matrix,
    phi: sp.Expr,
    f: sp.Expr,
    coords: Sequence[sp.Symbol],
    nu: sp.Expr,
) -> sp.Matrix:
    """Physical mismatch b_--u if one silently sets the ancestry symbol w equal to u."""
    return sp.simplify(reversed_drift(u_backward, K, phi, f, coords, nu) - u_backward)


def backward_state_map_diffusion(
    map_components: Matrix,
    K: Matrix,
    coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    """Pushforward diffusion tensor DPi K DPi^T for a proposed state map Pi."""
    J = sp.Matrix([[sp.diff(map_components[a], x) for x in coords] for a in range(map_components.rows)])
    if K.shape != (len(coords), len(coords)):
        raise ValueError("K must match the ancestry coordinate dimension")
    return sp.simplify(J * K * J.T)


def backward_state_map_drift(
    map_components: Matrix,
    backward_drift: Matrix,
    K: Matrix,
    coords: Sequence[sp.Symbol],
    nu: sp.Expr,
) -> sp.Matrix:
    """Backward-Ito drift of Pi(Y): DPi b_- - nu K:Hess(Pi)."""
    n = len(coords)
    if backward_drift.shape != (n, 1) or K.shape != (n, n):
        raise ValueError("ancestry drift/diffusion dimensions do not match coordinates")
    out = []
    for a in range(map_components.rows):
        first = sum(backward_drift[i] * sp.diff(map_components[a], coords[i]) for i in range(n))
        second = nu * sum(
            K[i, j] * sp.diff(map_components[a], coords[i], coords[j])
            for i in range(n)
            for j in range(n)
        )
        out.append(sp.simplify(first - second))
    return sp.Matrix(out)


def backward_state_map_residuals(
    map_components: Matrix,
    backward_drift: Matrix,
    K: Matrix,
    coords: Sequence[sp.Symbol],
    nu: sp.Expr,
    target_drift: Matrix,
    target_K: Matrix,
) -> tuple[sp.Matrix, sp.Matrix]:
    """Drift and diffusion residuals for ancestry -> physical backward state descent."""
    drift = backward_state_map_drift(map_components, backward_drift, K, coords, nu)
    diffusion = backward_state_map_diffusion(map_components, K, coords)
    if target_drift.shape != drift.shape or target_K.shape != diffusion.shape:
        raise ValueError("target state dimensions do not match the proposed map")
    return sp.simplify(drift - target_drift), sp.simplify(diffusion - target_K)
