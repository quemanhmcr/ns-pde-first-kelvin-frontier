"""Clock, parabolic-covariance, and moving-cut compatibility identities.

This module records three distinctions that are proof-critical for the Kelvin
restart programme:

1. physical Navier--Stokes time is not silently the same clock as a terminal
   ancestry/backward-martingale horizon;
2. a second-order Doob/Dynkin equation is not an ordinary de Rham exact one-form;
3. a moving quantile/shell cut has a time/boundary-speed face in addition to its
   static spatial boundary commutator.

No continuation or regularity statement is made here.
"""
from __future__ import annotations

from typing import Sequence

import sympy as sp

Matrix = sp.MatrixBase


def one_mode_mean(a: sp.Expr, tau: sp.Expr, nu: sp.Expr, k: sp.Expr) -> sp.Expr:
    """Conditional mean for the canonical one-mode Brownian/Kelvin calibration."""
    return sp.exp(-nu * k**2 * tau) * sp.cos(k * a)


def one_mode_second_moment(a: sp.Expr, tau: sp.Expr, nu: sp.Expr, k: sp.Expr) -> sp.Expr:
    r = nu * k**2 * tau
    return sp.Rational(1, 2) * (1 + sp.exp(-4 * r) * sp.cos(2 * k * a))


def one_mode_future_variance(a: sp.Expr, tau: sp.Expr, nu: sp.Expr, k: sp.Expr) -> sp.Expr:
    m = one_mode_mean(a, tau, nu, k)
    return sp.simplify(one_mode_second_moment(a, tau, nu, k) - m**2)


def one_mode_gamma(a: sp.Expr, tau: sp.Expr, nu: sp.Expr, k: sp.Expr) -> sp.Expr:
    m = one_mode_mean(a, tau, nu, k)
    return sp.simplify(2 * nu * sp.diff(m, a) ** 2)


def one_mode_horizon_dynkin_residual(a: sp.Symbol, tau: sp.Symbol, nu: sp.Expr, k: sp.Expr) -> sp.Expr:
    """Residual of (partial_tau - nu partial_aa)V = gamma."""
    V = one_mode_future_variance(a, tau, nu, k)
    gamma = one_mode_gamma(a, tau, nu, k)
    return sp.simplify(sp.diff(V, tau) - nu * sp.diff(V, a, 2) - gamma)


def one_mode_ordinary_spacetime_defect(a: sp.Symbol, tau: sp.Symbol, nu: sp.Expr, k: sp.Expr) -> sp.Expr:
    """Defect in the false ordinary one-form claim after s=Theta-tau.

    If ordinary de Rham exactness were valid, partial_s V + gamma would vanish.
    Because partial_s=-partial_tau, the actual coefficient is

        -partial_tau V + gamma = -nu partial_aa V.
    """
    V = one_mode_future_variance(a, tau, nu, k)
    gamma = one_mode_gamma(a, tau, nu, k)
    return sp.simplify(-sp.diff(V, tau) + gamma)


def forward_brownian_shear_residual(a: sp.Symbol, t: sp.Symbol, nu: sp.Expr, k: sp.Expr) -> sp.Expr:
    """(partial_t + nu partial_aa)u for u=e^{-nu k^2 t}cos(ka)."""
    u = sp.exp(-nu * k**2 * t) * sp.cos(k * a)
    return sp.simplify(sp.diff(u, t) + nu * sp.diff(u, a, 2))


def backward_kelvin_shear_residual(a: sp.Symbol, t: sp.Symbol, nu: sp.Expr, k: sp.Expr) -> sp.Expr:
    """(partial_t - nu partial_aa)u for the same one-mode NS shear."""
    u = sp.exp(-nu * k**2 * t) * sp.cos(k * a)
    return sp.simplify(sp.diff(u, t) - nu * sp.diff(u, a, 2))


def forward_future_terminal_mean(
    a: sp.Expr,
    s: sp.Expr,
    Theta: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """E[u(A_Theta,Theta)|A_s=a] for forward Brownian A with variance 2nu."""
    return sp.simplify(sp.exp(-nu * k**2 * (2 * Theta - s)) * sp.cos(k * a))


def normalized_variance_current_residual_1d(
    f: sp.Expr,
    phi: sp.Expr,
    w: sp.Expr,
    V: sp.Expr,
    x: sp.Symbol,
    s: sp.Symbol,
    nu: sp.Expr,
    K: sp.Expr,
    gamma: sp.Expr,
) -> sp.Expr:
    """Exact divergence-form covariance balance residual.

    q=f phi, j=w-nu K partial_x log f, and
    L V = w V_x + nu phi^{-1} partial_x(phi K V_x).
    With q_s=-partial_x(qj), V_s=-L V-gamma, the exact balance is

      partial_s(qV)+partial_x(qjV+nu q K V_x)=-q gamma.
    """
    q = sp.simplify(f * phi)
    j = sp.simplify(w - nu * K * sp.diff(sp.log(f), x))
    L_V = sp.simplify(w * sp.diff(V, x) + nu / phi * sp.diff(phi * K * sp.diff(V, x), x))
    q_s = -sp.diff(q * j, x)
    V_s = -L_V - gamma
    return sp.simplify(
        sp.expand(
            q_s * V
            + q * V_s
            + sp.diff(q * j * V + nu * q * K * sp.diff(V, x), x)
            + q * gamma
        ).doit()
    )


def two_clock_quadratic_rate(
    C: Matrix,
    C_t: Matrix,
    C_tau: Matrix,
    a: Matrix,
    a_t: Matrix,
    tau_t: sp.Expr,
) -> sp.Expr:
    """Exact chain rule for a(t)^T C(t,tau(t)) a(t)."""
    if C.rows != C.cols or C_t.shape != C.shape or C_tau.shape != C.shape:
        raise ValueError("C, C_t and C_tau must be same-size square matrices")
    if a.shape != (C.rows, 1) or a_t.shape != a.shape:
        raise ValueError("a and a_t must be compatible column vectors")
    return sp.simplify(
        (a.T * (C_t + tau_t * C_tau) * a)[0]
        + 2 * (a.T * C * a_t)[0]
    )


def moving_cut_operator_face(v_boundary: sp.Expr, a_t: sp.Expr) -> sp.Expr:
    """Coefficient of delta_{x=a(t)} in G_Q for Q=1_{x<a(t)}.

    Q_t contributes +a_t delta and [v partial_x,Q] contributes -v delta,
    so G_Q=(a_t-v) delta.
    """
    return sp.simplify(a_t - v_boundary)


def moving_halfline_mass_rate(q_boundary: sp.Expr, v_boundary: sp.Expr, a_t: sp.Expr) -> sp.Expr:
    """Reynolds rate for mass in (-infinity,a(t))."""
    return sp.simplify(q_boundary * moving_cut_operator_face(v_boundary, a_t))


def moving_halfline_static_flux(q_boundary: sp.Expr, v_boundary: sp.Expr) -> sp.Expr:
    return sp.simplify(-q_boundary * v_boundary)


def moving_halfline_boundary_speed_face(q_boundary: sp.Expr, a_t: sp.Expr) -> sp.Expr:
    return sp.simplify(q_boundary * a_t)


def pair_moving_cut_mass_rate(
    face_densities: Sequence[sp.Expr],
    face_velocities: Sequence[sp.Expr],
    a_t: sp.Expr,
) -> sp.Expr:
    """Two-replica Reynolds rate: one moving-boundary face per replica."""
    if len(face_densities) != 2 or len(face_velocities) != 2:
        raise ValueError("ordered pair requires exactly two face densities and velocities")
    return sp.simplify(
        sum(
            face_densities[i] * moving_cut_operator_face(face_velocities[i], a_t)
            for i in range(2)
        )
    )
