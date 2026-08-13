"""Physical frame-weighted topology for the reverse codeforming Kelvin residual.

The reverse-age codeforming residual chi is a convenient material coordinate, but
the physical reconstructed residual is r=L chi.  Therefore raw chi bias or raw chi
covariance is not itself the finite-to-local Kelvin topology.  The physical metric
is M_L=L^T L, and the literal second moment is tr(Q_chi M_L), with
Q_chi=Cov(chi)+E[chi]E[chi]^T.

This module records exact identities and exact smooth Navier--Stokes calibrations.
It makes no first-bad, future-bank, restart, continuation, or regularity claim.
"""
from __future__ import annotations

import sympy as sp

Matrix = sp.MatrixBase


def primal_line_metric(line_frame: Matrix) -> Matrix:
    if line_frame.rows != line_frame.cols:
        raise ValueError("line_frame must be square")
    return sp.simplify(line_frame.T * line_frame)


def physical_residual(line_frame: Matrix, codeforming_residual: Matrix) -> Matrix:
    if codeforming_residual.shape != (line_frame.cols, 1):
        raise ValueError("residual/frame dimension mismatch")
    return sp.simplify(line_frame * codeforming_residual)


def weighted_bias_energy(mean_residual: Matrix, line_frame: Matrix) -> sp.Expr:
    if mean_residual.shape != (line_frame.cols, 1):
        raise ValueError("mean/frame dimension mismatch")
    M = primal_line_metric(line_frame)
    return sp.simplify((mean_residual.T * M * mean_residual)[0])


def weighted_spread_energy(covariance: Matrix, line_frame: Matrix) -> sp.Expr:
    if covariance.shape != (line_frame.cols, line_frame.cols):
        raise ValueError("covariance/frame dimension mismatch")
    return sp.simplify(sp.trace(covariance * primal_line_metric(line_frame)))


def residual_second_moment(mean_residual: Matrix, covariance: Matrix) -> Matrix:
    if covariance.shape != (mean_residual.rows, mean_residual.rows):
        raise ValueError("mean/covariance dimension mismatch")
    return sp.simplify(covariance + mean_residual * mean_residual.T)


def weighted_second_moment_energy(
    mean_residual: Matrix,
    covariance: Matrix,
    line_frame: Matrix,
) -> sp.Expr:
    Q = residual_second_moment(mean_residual, covariance)
    return sp.simplify(sp.trace(Q * primal_line_metric(line_frame)))


def weighted_bias_spread_residual(
    mean_residual: Matrix,
    covariance: Matrix,
    line_frame: Matrix,
) -> sp.Expr:
    """Residual E|L chi|^2 - (weighted bias + weighted spread)."""
    lhs = weighted_second_moment_energy(mean_residual, covariance, line_frame)
    rhs = weighted_bias_energy(mean_residual, line_frame) + weighted_spread_energy(
        covariance, line_frame
    )
    return sp.simplify(lhs - rhs)


def physical_qv_tensor(
    line_frame: Matrix,
    codeforming_noise: Matrix,
    nu: sp.Expr,
) -> Matrix:
    if codeforming_noise.rows != line_frame.cols:
        raise ValueError("noise/frame dimension mismatch")
    N = sp.simplify(line_frame * codeforming_noise)
    return sp.simplify(2 * nu * N * N.T)


def weighted_qv_trace_residual(
    line_frame: Matrix,
    codeforming_noise: Matrix,
    nu: sp.Expr,
) -> sp.Expr:
    """Physical q.v. trace equals 2nu tr(Q Q^T L^T L)."""
    physical = physical_qv_tensor(line_frame, codeforming_noise, nu)
    weighted = sp.simplify(
        2
        * nu
        * sp.trace(
            codeforming_noise
            * codeforming_noise.T
            * primal_line_metric(line_frame)
        )
    )
    return sp.simplify(sp.trace(physical) - weighted)



def two_state_weighted_energy(
    line_frame_1: Matrix,
    residual_1: Matrix,
    line_frame_2: Matrix,
    residual_2: Matrix,
) -> sp.Expr:
    """Equal-weight E[chi^T M_L chi] for two literal full-state replicas."""
    if line_frame_1.shape != line_frame_2.shape:
        raise ValueError("line frames must have equal shape")
    if residual_1.shape != residual_2.shape or residual_1.shape != (line_frame_1.cols, 1):
        raise ValueError("residual/frame dimension mismatch")
    M1 = primal_line_metric(line_frame_1)
    M2 = primal_line_metric(line_frame_2)
    Q1 = residual_1 * residual_1.T
    Q2 = residual_2 * residual_2.T
    return sp.simplify(
        sp.Rational(1, 2) * (sp.trace(M1 * Q1) + sp.trace(M2 * Q2))
    )


def two_state_mean_metric_mean_second_moment(
    line_frame_1: Matrix,
    residual_1: Matrix,
    line_frame_2: Matrix,
    residual_2: Matrix,
) -> sp.Expr:
    Mbar = sp.simplify(
        (primal_line_metric(line_frame_1) + primal_line_metric(line_frame_2)) / 2
    )
    Qbar = sp.simplify(
        (residual_1 * residual_1.T + residual_2 * residual_2.T) / 2
    )
    return sp.simplify(sp.trace(Mbar * Qbar))


def two_state_metric_residual_correlation(
    line_frame_1: Matrix,
    residual_1: Matrix,
    line_frame_2: Matrix,
    residual_2: Matrix,
) -> sp.Expr:
    """1/4 tr[(M1-M2)(Q1-Q2)], the missing full-state mixed face."""
    M1 = primal_line_metric(line_frame_1)
    M2 = primal_line_metric(line_frame_2)
    Q1 = residual_1 * residual_1.T
    Q2 = residual_2 * residual_2.T
    return sp.simplify(sp.trace((M1 - M2) * (Q1 - Q2)) / 4)


def two_state_metric_residual_decomposition_residual(
    line_frame_1: Matrix,
    residual_1: Matrix,
    line_frame_2: Matrix,
    residual_2: Matrix,
) -> sp.Expr:
    exact = two_state_weighted_energy(
        line_frame_1, residual_1, line_frame_2, residual_2
    )
    factorized = two_state_mean_metric_mean_second_moment(
        line_frame_1, residual_1, line_frame_2, residual_2
    )
    mixed = two_state_metric_residual_correlation(
        line_frame_1, residual_1, line_frame_2, residual_2
    )
    return sp.simplify(exact - factorized - mixed)

def quadratic_heat_shear(y: sp.Expr, t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Exact shear U=y^2+2 nu t solving U_t-nu U_yy=0."""
    return sp.expand(y**2 + 2 * nu * t)


def quadratic_heat_shear_residual(y: sp.Symbol, t: sp.Symbol, nu: sp.Expr) -> sp.Expr:
    U = quadratic_heat_shear(y, t, nu)
    return sp.simplify(sp.diff(U, t) - nu * sp.diff(U, y, 2))


def asymmetric_square_shear_error_from_velocity(
    shear_velocity: sp.Expr,
    anchor_y: sp.Symbol,
    side: sp.Expr,
) -> sp.Expr:
    """Kelvin local-frame error on [0,side]_x x [0,side]_y, normal +e_z.

    For x-shear u=(U(y),0,0), omega_z=-U_y.  Stokes gives
      epsilon = side*[U(Y)-U(Y+side)] + side^2 U_y(Y).
    """
    U0 = shear_velocity
    U1 = shear_velocity.subs(anchor_y, anchor_y + side)
    Uy0 = sp.diff(shear_velocity, anchor_y)
    return sp.simplify(side * (U0 - U1) + side**2 * Uy0)


def asymmetric_square_codeforming_residual(
    shear_velocity: sp.Expr,
    anchor_y: sp.Symbol,
    side: sp.Expr,
) -> sp.Expr:
    """chi_z=epsilon/det(rho I)=epsilon/rho^3 for an isotropic square packet."""
    return sp.simplify(
        asymmetric_square_shear_error_from_velocity(shear_velocity, anchor_y, side)
        / side**3
    )


def quadratic_asymmetric_square_exact_residual(
    anchor_y: sp.Symbol,
    t: sp.Expr,
    nu: sp.Expr,
    side: sp.Expr,
) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Return (epsilon_z, chi_z, r_z) for exact quadratic heat shear."""
    U = quadratic_heat_shear(anchor_y, t, nu)
    eps = asymmetric_square_shear_error_from_velocity(U, anchor_y, side)
    chi = sp.simplify(eps / side**3)
    r = sp.simplify(side * chi)
    return eps, chi, r


def one_mode_shear(
    anchor_y: sp.Expr,
    t: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    return sp.exp(-nu * k**2 * t) * sp.cos(k * anchor_y)


def one_mode_asymmetric_codeforming_residual(
    anchor_y: sp.Symbol,
    t: sp.Expr,
    side: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    U = one_mode_shear(anchor_y, t, nu, k)
    return asymmetric_square_codeforming_residual(U, anchor_y, side)


def one_mode_asymmetric_codeforming_noise(
    anchor_y: sp.Symbol,
    t: sp.Expr,
    side: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """The y-anchor Brownian coefficient of chi_z at fixed frame/shape."""
    return sp.simplify(
        sp.diff(
            one_mode_asymmetric_codeforming_residual(anchor_y, t, side, nu, k),
            anchor_y,
        )
    )


def isotropic_physical_residual_from_scalar_chi(
    scalar_chi: sp.Expr,
    side: sp.Expr,
) -> sp.Expr:
    return sp.simplify(side * scalar_chi)


def homogeneous_weighted_exponent_residual(
    rho: sp.Expr,
    degree: int,
    amplitude: sp.Expr,
) -> sp.Expr:
    """Audit rho^2*(rho^(p-2)a)^2 = rho^(2p-2)a^2."""
    if degree < 2:
        raise ValueError("nonaffine degree must be at least two")
    raw_chi = rho ** (degree - 2) * amplitude
    lhs = sp.simplify(rho**2 * raw_chi**2)
    rhs = sp.simplify(rho ** (2 * degree - 2) * amplitude**2)
    return sp.simplify(lhs - rhs)
