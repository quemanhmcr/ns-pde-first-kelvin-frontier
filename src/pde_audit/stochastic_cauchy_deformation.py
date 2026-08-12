"""Fixed-past stochastic Cauchy-invariant second-moment geometry.

For a causal backward stochastic flow from current (x,t) to a fixed past time s<t,
write the stochastic Cauchy contribution as

    Y = D w_s,

where w_s is vorticity sampled at the stochastic past position and D is the
stochastic deformation matrix.  Then

    m = E[Y] = omega(x,t),
    Q = E[Y Y^T],
    C = Q - m m^T >= 0.

If |w_s|^2 <= W_s samplewise, define R=E[D D^T].  The exact two-face identity

    W_s R - m m^T = (W_s R-Q) + C

separates terminal directional headroom from stochastic covariance.  The first gap
has samplewise factorization D(W_s I-w_s w_s^T)D^T.

The deformation evolves by D_sigma=D (grad u)^T in reverse age, so
(D D^T)_sigma=2 D S D^T.  This finite-variation deformation moment is a physical
stretching channel and is not centered covariance or quadratic variation.

No global deformation bound, restart theorem, or regularity conclusion is encoded.
"""
from __future__ import annotations

from typing import Sequence

import sympy as sp

Matrix = sp.MatrixBase


def cauchy_sample(deformation: Matrix, past_vorticity: Matrix) -> sp.Matrix:
    return sp.simplify(deformation * past_vorticity)


def sample_terminal_headroom_residual(
    deformation: Matrix,
    past_vorticity: Matrix,
    terminal_square_bound: sp.Expr,
) -> sp.Matrix:
    """Residual of W DD^T - YY^T = D(WI-ww^T)D^T."""
    n = deformation.rows
    if deformation.cols != n or past_vorticity.shape != (n, 1):
        raise ValueError("dimension mismatch")
    Y = cauchy_sample(deformation, past_vorticity)
    lhs = sp.simplify(terminal_square_bound * deformation * deformation.T - Y * Y.T)
    rhs = sp.simplify(
        deformation
        * (terminal_square_bound * sp.eye(n) - past_vorticity * past_vorticity.T)
        * deformation.T
    )
    return sp.simplify(lhs - rhs)


def weighted_second_moment(samples: Sequence[Matrix], weights: Sequence[sp.Expr]) -> sp.Matrix:
    if not samples or len(samples) != len(weights):
        raise ValueError("nonempty equally-sized samples/weights required")
    shape = samples[0].shape
    if any(sample.shape != shape for sample in samples):
        raise ValueError("sample shapes must match")
    return sp.simplify(sum((w * sample for w, sample in zip(weights, samples)), sp.zeros(*shape)))


def ensemble_cauchy_moments(
    deformations: Sequence[Matrix],
    past_vorticities: Sequence[Matrix],
    weights: Sequence[sp.Expr],
) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    """Return mean m, second moment Q, covariance C, deformation moment R."""
    if not deformations or not (
        len(deformations) == len(past_vorticities) == len(weights)
    ):
        raise ValueError("nonempty equally-sized ensemble data required")
    Ys = [cauchy_sample(D, w) for D, w in zip(deformations, past_vorticities)]
    m = weighted_second_moment(Ys, weights)
    Q = weighted_second_moment([Y * Y.T for Y in Ys], weights)
    C = sp.simplify(Q - m * m.T)
    R = weighted_second_moment([D * D.T for D in deformations], weights)
    return m, Q, C, R


def ensemble_terminal_headroom_residual(
    deformations: Sequence[Matrix],
    past_vorticities: Sequence[Matrix],
    weights: Sequence[sp.Expr],
    terminal_square_bound: sp.Expr,
) -> sp.Matrix:
    """Residual of W R-Q = E[D(WI-ww^T)D^T]."""
    m, Q, C, R = ensemble_cauchy_moments(deformations, past_vorticities, weights)
    n = R.rows
    rhs_terms = [
        D * (terminal_square_bound * sp.eye(n) - w * w.T) * D.T
        for D, w in zip(deformations, past_vorticities)
    ]
    rhs = weighted_second_moment(rhs_terms, weights)
    return sp.simplify(terminal_square_bound * R - Q - rhs)


def cauchy_two_face_envelope_residual(
    mean: Matrix,
    second_moment: Matrix,
    deformation_moment: Matrix,
    terminal_square_bound: sp.Expr,
) -> sp.Matrix:
    """Residual W R-mm^T - [(W R-Q)+(Q-mm^T)]."""
    lhs = sp.simplify(terminal_square_bound * deformation_moment - mean * mean.T)
    rhs = sp.simplify(
        (terminal_square_bound * deformation_moment - second_moment)
        + (second_moment - mean * mean.T)
    )
    return sp.simplify(lhs - rhs)


def deformation_reverse_age_residual(
    deformation: Matrix,
    deformation_dot: Matrix,
    grad_u: Matrix,
) -> sp.Matrix:
    """D_sigma-D (grad u)^T."""
    return sp.simplify(deformation_dot - deformation * grad_u.T)


def deformation_gram_rate_residual(
    deformation: Matrix,
    deformation_dot: Matrix,
    grad_u: Matrix,
) -> sp.Matrix:
    """(DD^T)_sigma - 2 D S D^T."""
    Gdot = sp.simplify(deformation_dot * deformation.T + deformation * deformation_dot.T)
    S = sp.simplify((grad_u + grad_u.T) / 2)
    return sp.simplify(Gdot - 2 * deformation * S * deformation.T)


def incompressible_deformation_determinant_log_rate(grad_u: Matrix) -> sp.Expr:
    """d_sigma log det D = tr(grad u)."""
    return sp.simplify(sp.trace(grad_u))


def ensemble_deformation_rate_residual(
    deformations: Sequence[Matrix],
    grad_us: Sequence[Matrix],
    weights: Sequence[sp.Expr],
    R_dot: Matrix,
) -> sp.Matrix:
    """R_sigma = 2 E[D S D^T], an exact generally unclosed hierarchy law."""
    if not (len(deformations) == len(grad_us) == len(weights)):
        raise ValueError("ensemble lengths must match")
    terms = []
    for D, A in zip(deformations, grad_us):
        S = sp.simplify((A + A.T) / 2)
        terms.append(2 * D * S * D.T)
    rhs = weighted_second_moment(terms, weights)
    return sp.simplify(R_dot - rhs)


def affine_vortex_z_deformation(a: sp.Expr, past_time: sp.Expr, current_time: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.exp(2 * a * (current_time - past_time)))


def affine_vortex_z_vorticity(a: sp.Expr, r0: sp.Expr, time: sp.Expr) -> sp.Expr:
    return sp.simplify(2 * r0 * sp.exp(2 * a * time))


def affine_vortex_cauchy_z_residual(
    a: sp.Expr,
    r0: sp.Expr,
    past_time: sp.Expr,
    current_time: sp.Expr,
) -> sp.Expr:
    D = affine_vortex_z_deformation(a, past_time, current_time)
    ws = affine_vortex_z_vorticity(a, r0, past_time)
    wt = affine_vortex_z_vorticity(a, r0, current_time)
    return sp.simplify(D * ws - wt)


def affine_vortex_total_bank_envelope_residual(
    a: sp.Expr,
    r0: sp.Expr,
    past_time: sp.Expr,
    current_time: sp.Expr,
) -> sp.Expr:
    """W_s R_zz-|omega_t|^2; exact zero for uniform affine vortex."""
    D = affine_vortex_z_deformation(a, past_time, current_time)
    ws = affine_vortex_z_vorticity(a, r0, past_time)
    wt = affine_vortex_z_vorticity(a, r0, current_time)
    return sp.simplify(ws**2 * D**2 - wt**2)


def one_mode_shear_terminal_supremum(
    past_time: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    return sp.simplify(k**2 * sp.exp(-2 * nu * k**2 * past_time))


def one_mode_shear_second_moment(
    y: sp.Expr,
    current_time: sp.Expr,
    past_time: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    h = sp.simplify(current_time - past_time)
    W = one_mode_shear_terminal_supremum(past_time, nu, k)
    return sp.simplify(
        W / 2 * (1 - sp.exp(-4 * nu * k**2 * h) * sp.cos(2 * k * y))
    )


def one_mode_shear_terminal_headroom(
    y: sp.Expr,
    current_time: sp.Expr,
    past_time: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    W = one_mode_shear_terminal_supremum(past_time, nu, k)
    Q = one_mode_shear_second_moment(y, current_time, past_time, nu, k)
    return sp.simplify(W - Q)
