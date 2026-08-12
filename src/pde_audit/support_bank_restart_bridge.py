"""Exact support x total-bank tensor factorization for the physical Kelvin core.

On the ideal full physical backward-Kelvin state write

    omega = F eta,
    Q_tot = eta eta^T + C_tilde,  C_tilde >= 0,
    P_nu = 2 nu tau F F^T.

No norm estimate is introduced here.  The main identity decomposes a physical
vorticity envelope into three positive-semidefinite physical sectors whenever the
corresponding Loewner envelopes hold:

    p q I - 2 nu tau omega omega^T
      = q (p I-P_nu)
        + 2 nu tau F(q I-Q_tot)F^T
        + 2 nu tau F(Q_tot-eta eta^T)F^T.

The last term is unresolved/future covariance.  This module does not prove the
programme-specific uniform envelopes or a continuation theorem.
"""
from __future__ import annotations

import sympy as sp

Matrix = sp.MatrixBase


def codeforming_total_second_moment(mean: Matrix, covariance: Matrix) -> sp.Matrix:
    if mean.cols != 1 or covariance.rows != covariance.cols or covariance.rows != mean.rows:
        raise ValueError("mean/covariance dimension mismatch")
    return sp.simplify(mean * mean.T + covariance)


def physical_vorticity_from_codeforming(deformation: Matrix, mean: Matrix) -> sp.Matrix:
    return sp.simplify(deformation * mean)


def physical_total_second_moment(deformation: Matrix, total: Matrix) -> sp.Matrix:
    return sp.simplify(deformation * total * deformation.T)


def parabolic_support_tensor(
    deformation: Matrix,
    nu: sp.Expr,
    remaining_horizon: sp.Expr,
) -> sp.Matrix:
    return sp.simplify(2 * nu * remaining_horizon * deformation * deformation.T)


def resolved_unresolved_factorization_residual(
    deformation: Matrix,
    mean: Matrix,
    covariance: Matrix,
) -> sp.Matrix:
    Q = codeforming_total_second_moment(mean, covariance)
    T = physical_total_second_moment(deformation, Q)
    omega = physical_vorticity_from_codeforming(deformation, mean)
    return sp.simplify(T - omega * omega.T - deformation * covariance * deformation.T)


def support_bank_three_face_residual(
    deformation: Matrix,
    mean: Matrix,
    covariance: Matrix,
    p_star: sp.Expr,
    q_star: sp.Expr,
    nu: sp.Expr,
    remaining_horizon: sp.Expr,
) -> sp.Matrix:
    """Residual of the exact three-positive-sector decomposition."""
    n = deformation.rows
    if deformation.cols != n or mean.shape != (n, 1) or covariance.shape != (n, n):
        raise ValueError("all state tensors must have one common square dimension")
    I = sp.eye(n)
    Q = codeforming_total_second_moment(mean, covariance)
    P = parabolic_support_tensor(deformation, nu, remaining_horizon)
    omega = physical_vorticity_from_codeforming(deformation, mean)
    lhs = sp.simplify(p_star * q_star * I - 2 * nu * remaining_horizon * omega * omega.T)
    rhs = sp.simplify(
        q_star * (p_star * I - P)
        + 2 * nu * remaining_horizon * deformation * (q_star * I - Q) * deformation.T
        + 2 * nu * remaining_horizon * deformation * (Q - mean * mean.T) * deformation.T
    )
    return sp.simplify(lhs - rhs)


def total_bank_support_factorization_residual(
    deformation: Matrix,
    total: Matrix,
    q_star: sp.Expr,
    nu: sp.Expr,
    remaining_horizon: sp.Expr,
) -> sp.Matrix:
    """q P_nu - 2 nu tau T_tot = 2 nu tau F(q I-Q_tot)F^T."""
    n = deformation.rows
    I = sp.eye(n)
    P = parabolic_support_tensor(deformation, nu, remaining_horizon)
    T = physical_total_second_moment(deformation, total)
    return sp.simplify(
        q_star * P
        - 2 * nu * remaining_horizon * T
        - 2 * nu * remaining_horizon * deformation * (q_star * I - total) * deformation.T
    )


def scalar_vorticity_rate_square_bound(
    p_star: sp.Expr,
    q_star: sp.Expr,
    nu: sp.Expr,
    remaining_horizon: sp.Expr,
) -> sp.Expr:
    """Scalar RHS p*q/(2 nu tau) implied by the tensor Loewner envelope."""
    return sp.simplify(p_star * q_star / (2 * nu * remaining_horizon))


def time_integrated_vorticity_rate_bound(
    product_bound: sp.Expr,
    nu: sp.Expr,
    epsilon: sp.Expr,
) -> sp.Expr:
    """Integral of sqrt(M/(2nu tau)) from tau=0 to epsilon."""
    return sp.simplify(sp.sqrt(2 * product_bound * epsilon / nu))


def parabolic_support_dynamics_residual(
    grad_u: Matrix,
    deformation: Matrix,
    nu: sp.Expr,
    remaining_horizon: sp.Expr,
) -> sp.Matrix:
    """Physical-time law Pdot=A P+P A^T-P/tau for tau=Theta-t."""
    B = sp.simplify(deformation * deformation.T)
    P = sp.simplify(2 * nu * remaining_horizon * B)
    Bdot = sp.simplify(grad_u * B + B * grad_u.T)
    Pdot_direct = sp.simplify(-2 * nu * B + 2 * nu * remaining_horizon * Bdot)
    Pdot_rhs = sp.simplify(grad_u * P + P * grad_u.T - P / remaining_horizon)
    return sp.simplify(Pdot_direct - Pdot_rhs)


def isotropic_diagonal_envelope_gap(
    p_star: sp.Expr,
    q_star: sp.Expr,
    support_diagonal: tuple[sp.Expr, ...],
    total_diagonal: tuple[sp.Expr, ...],
    resolved_diagonal: tuple[sp.Expr, ...],
    nu: sp.Expr,
    tau: sp.Expr,
) -> sp.Matrix:
    """Diagonal witness of the three-sector PSD gap.

    resolved_diagonal are eta_i^2, so Q_i-resolved_i is covariance content.
    """
    if not (len(support_diagonal) == len(total_diagonal) == len(resolved_diagonal)):
        raise ValueError("diagonal lengths must match")
    return sp.diag(*[
        sp.simplify(
            q_star * (p_star - support_diagonal[i])
            + (q_star * support_diagonal[i] - support_diagonal[i] * total_diagonal[i])
            + support_diagonal[i] * (total_diagonal[i] - resolved_diagonal[i])
        )
        for i in range(len(support_diagonal))
    ])
