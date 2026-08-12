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


def forward_deformation_from_cauchy(deformation: Matrix) -> sp.Matrix:
    """F_C=D^T, the forward deformation dual to the backflow Cauchy matrix."""
    return sp.simplify(deformation.T)


def coherent_area_frame_from_cauchy(
    deformation: Matrix,
    reference_scale: sp.Expr,
) -> sp.Matrix:
    """H=rho^2 F_C^-T=rho^2 D^-1 for the same stochastic replica deformation."""
    F = forward_deformation_from_cauchy(deformation)
    return sp.simplify(reference_scale**2 * F.inv().T)


def packet_metric_from_area_frame(area_frame: Matrix) -> sp.Matrix:
    return sp.simplify((area_frame.T * area_frame).inv())


def cauchy_packet_metric_duality_residual(
    deformation: Matrix,
    reference_scale: sp.Expr,
) -> sp.Matrix:
    """DD^T-rho^4 M_H for H=rho^2(D^T)^-T."""
    H = coherent_area_frame_from_cauchy(deformation, reference_scale)
    M = packet_metric_from_area_frame(H)
    return sp.simplify(deformation * deformation.T - reference_scale**4 * M)


def cauchy_spatial_support_spectral_trace_residual(deformation: Matrix) -> sp.Expr:
    """tr(DD^T)-tr(F_C F_C^T)=0: material metric and spatial support share spectrum."""
    F = forward_deformation_from_cauchy(deformation)
    return sp.simplify(sp.trace(deformation * deformation.T) - sp.trace(F * F.T))


def packet_metric_rate_residual_from_cauchy(
    deformation: Matrix,
    grad_u: Matrix,
    reference_scale: sp.Expr,
) -> sp.Matrix:
    """rho^4 Mdot - 2 D S D^T for fixed rho on the same stochastic deformation."""
    Ddot = sp.simplify(deformation * grad_u.T)
    H = coherent_area_frame_from_cauchy(deformation, reference_scale)
    M = packet_metric_from_area_frame(H)
    # Differentiate M through the exact identity rho^4 M=DD^T rather than
    # introducing a coordinate derivative of symbolic matrix entries.
    Mdot_from_duality = sp.simplify(
        (Ddot * deformation.T + deformation * Ddot.T) / reference_scale**4
    )
    S = sp.simplify((grad_u + grad_u.T) / 2)
    return sp.simplify(reference_scale**4 * Mdot_from_duality - 2 * deformation * S * deformation.T)


def matrix_deformation_covariance(
    deformations: Sequence[Matrix],
    weights: Sequence[sp.Expr],
) -> sp.Matrix:
    """Row-Gram deformation covariance E[DD^T]-E[D]E[D]^T.

    This is the column partial trace of the full covariance of vec(D), not the
    full n^2 x n^2 deformation covariance itself.
    """
    if not deformations or len(deformations) != len(weights):
        raise ValueError("nonempty equally-sized deformation/weight lists required")
    Dbar = weighted_second_moment(deformations, weights)
    R = weighted_second_moment([D * D.T for D in deformations], weights)
    return sp.simplify(R - Dbar * Dbar.T)


def deformation_second_moment_split_residual(
    deformations: Sequence[Matrix],
    weights: Sequence[sp.Expr],
) -> sp.Matrix:
    """Residual R-[Dbar Dbar^T+C_D^Gram]."""
    Dbar = weighted_second_moment(deformations, weights)
    R = weighted_second_moment([D * D.T for D in deformations], weights)
    C_D_gram = matrix_deformation_covariance(deformations, weights)
    return sp.simplify(R - Dbar * Dbar.T - C_D_gram)


def one_mode_shear_deformation_mean_coefficient(
    y: sp.Expr,
    current_time: sp.Expr,
    horizon: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """E[c_h] for the exact one-mode shear Cauchy deformation coefficient."""
    return sp.simplify(-k * horizon * sp.exp(-nu * k**2 * current_time) * sp.sin(k * y))


def one_mode_shear_deformation_second_coefficient(
    y: sp.Expr,
    current_time: sp.Expr,
    horizon: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """Exact E[c_h^2] for reverse Brownian sampling of U_y in one-mode shear.

    c_h = int_0^h U_y(Y_sigma,t-sigma) d sigma, with
    Y_sigma=y+sqrt(2nu)W_sigma.  Nilpotence of the shear gradient makes this the
    exact matrix deformation coefficient.
    """
    alpha = sp.simplify(nu * k**2)
    prefactor = sp.simplify(k**2 * sp.exp(-2 * alpha * current_time) / (4 * alpha**2))
    bracket = sp.simplify(
        sp.exp(2 * alpha * horizon) - 1 - 2 * alpha * horizon
        - sp.cos(2 * k * y)
        * (sp.exp(-2 * alpha * horizon) - 1 + 2 * alpha * horizon)
    )
    return sp.simplify(prefactor * bracket)


def one_mode_shear_deformation_variance(
    y: sp.Expr,
    current_time: sp.Expr,
    horizon: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    mean = one_mode_shear_deformation_mean_coefficient(y, current_time, horizon, nu, k)
    second = one_mode_shear_deformation_second_coefficient(y, current_time, horizon, nu, k)
    return sp.simplify(second - mean**2)


def one_mode_shear_deformation_variance_at_symmetry(
    current_time: sp.Expr,
    horizon: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """At y=0 the deterministic/mean shear coefficient vanishes but variance is positive."""
    alpha = sp.simplify(nu * k**2)
    return sp.simplify(
        k**2 * sp.exp(-2 * alpha * current_time)
        / (2 * alpha**2)
        * (sp.sinh(2 * alpha * horizon) - 2 * alpha * horizon)
    )


def one_mode_shear_deformation_gram_from_moments(
    mean_coefficient: sp.Expr,
    second_coefficient: sp.Expr,
) -> sp.Matrix:
    """E[D D^T] for D=I+c E_21 in the shear plane."""
    return sp.Matrix([[1, mean_coefficient], [mean_coefficient, 1 + second_coefficient]])


def one_mode_shear_mean_deformation_gram(mean_coefficient: sp.Expr) -> sp.Matrix:
    """E[D]E[D]^T for D=I+c E_21."""
    return sp.Matrix([[1, mean_coefficient], [mean_coefficient, 1 + mean_coefficient**2]])


def one_mode_shear_deformation_dispersion_residual(
    y: sp.Expr,
    current_time: sp.Expr,
    horizon: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Matrix:
    """R-DbarDbar^T-Var(c)e_2e_2^T."""
    mean = one_mode_shear_deformation_mean_coefficient(y, current_time, horizon, nu, k)
    second = one_mode_shear_deformation_second_coefficient(y, current_time, horizon, nu, k)
    variance = sp.simplify(second - mean**2)
    R = one_mode_shear_deformation_gram_from_moments(mean, second)
    mean_gram = one_mode_shear_mean_deformation_gram(mean)
    dispersion = sp.diag(0, variance)
    return sp.simplify(R - mean_gram - dispersion)


def one_mode_shear_deformation_variance_leading_residual(
    y: sp.Expr,
    current_time: sp.Expr,
    horizon: sp.Symbol,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """Coefficient check: Var(c)=2nu/3 * |d_y U_y(y,t)|^2 h^3+O(h^4)."""
    var = one_mode_shear_deformation_variance(y, current_time, horizon, nu, k)
    leading = sp.simplify(
        sp.Rational(2, 3)
        * nu
        * k**4
        * sp.exp(-2 * nu * k**2 * current_time)
        * sp.cos(k * y)**2
        * horizon**3
    )
    series = sp.series(var, horizon, 0, 4).removeO()
    return sp.trigsimp(sp.simplify(series - leading))


def matrix_deformation_pair_covariance(
    deformations: Sequence[Matrix],
    weights: Sequence[sp.Expr],
) -> sp.Matrix:
    """1/2 sum_ij p_i p_j (D_i-D_j)(D_i-D_j)^T.

    Equals matrix_deformation_covariance when weights sum to one.
    """
    if not deformations or len(deformations) != len(weights):
        raise ValueError("nonempty equally-sized deformation/weight lists required")
    n, m = deformations[0].shape
    if n != m or any(D.shape != (n, n) for D in deformations):
        raise ValueError("square equal-sized deformation matrices required")
    out = sp.zeros(n)
    for i, Di in enumerate(deformations):
        for j, Dj in enumerate(deformations):
            delta = Di - Dj
            out += sp.Rational(1, 2) * weights[i] * weights[j] * delta * delta.T
    return sp.simplify(out)


def matrix_deformation_pair_covariance_residual(
    deformations: Sequence[Matrix],
    weights: Sequence[sp.Expr],
) -> sp.Matrix:
    return sp.simplify(
        matrix_deformation_pair_covariance(deformations, weights)
        - matrix_deformation_covariance(deformations, weights)
    )


def expected_packet_metric_split_residual(
    deformations: Sequence[Matrix],
    weights: Sequence[sp.Expr],
    reference_scale: sp.Expr,
) -> sp.Matrix:
    """rho^4 E[M_H] - [Dbar Dbar^T + C_D^Gram] on same-replica packet family."""
    metrics = []
    for D in deformations:
        H = coherent_area_frame_from_cauchy(D, reference_scale)
        metrics.append(packet_metric_from_area_frame(H))
    EM = weighted_second_moment(metrics, weights)
    Dbar = weighted_second_moment(deformations, weights)
    C_D_gram = matrix_deformation_covariance(deformations, weights)
    return sp.simplify(reference_scale**4 * EM - Dbar * Dbar.T - C_D_gram)



def column_vectorize(matrix: Matrix) -> sp.Matrix:
    """Column-major vec, so vec(XB)=(B^T kron I)vec(X)."""
    return sp.Matrix([matrix[i, j] for j in range(matrix.cols) for i in range(matrix.rows)])


def vectorized_reverse_age_path_connection(grad_u: Matrix) -> sp.Matrix:
    """Pathwise connection K_path=A kron I for D_sigma=D A^T."""
    if grad_u.rows != grad_u.cols:
        raise ValueError("grad_u must be square")
    return sp.kronecker_product(grad_u, sp.eye(grad_u.rows))


def vectorized_horizon_connection(grad_u: Matrix) -> sp.Matrix:
    """Current-end horizon connection B=I kron A^T for left multiplication A^T M."""
    if grad_u.rows != grad_u.cols:
        raise ValueError("grad_u must be square")
    return sp.kronecker_product(sp.eye(grad_u.rows), grad_u.T)


def reverse_age_path_vectorization_residual(
    deformation: Matrix,
    deformation_dot: Matrix,
    grad_u: Matrix,
) -> sp.Matrix:
    """vec(D_sigma)-(A kron I)vec(D), auditing the pathwise right action."""
    return sp.simplify(
        column_vectorize(deformation_dot)
        - vectorized_reverse_age_path_connection(grad_u) * column_vectorize(deformation)
    )


def horizon_connection_vectorization_residual(
    mean_deformation: Matrix,
    grad_u: Matrix,
) -> sp.Matrix:
    """(I kron A^T)vec(M)-vec(A^T M), auditing current-end horizon ordering."""
    return sp.simplify(
        vectorized_horizon_connection(grad_u) * column_vectorize(mean_deformation)
        - column_vectorize(grad_u.T * mean_deformation)
    )


def matrix_deformation_vectorized_covariance(
    deformations: Sequence[Matrix],
    weights: Sequence[sp.Expr],
) -> sp.Matrix:
    """Full covariance Sigma_D=Cov(vec(D)) in column-major coordinates."""
    if not deformations or len(deformations) != len(weights):
        raise ValueError("nonempty equally-sized deformation/weight lists required")
    shape = deformations[0].shape
    if shape[0] != shape[1] or any(D.shape != shape for D in deformations):
        raise ValueError("square equal-sized deformation matrices required")
    vecs = [column_vectorize(D) for D in deformations]
    mean = weighted_second_moment(vecs, weights)
    second = weighted_second_moment([v * v.T for v in vecs], weights)
    return sp.simplify(second - mean * mean.T)


def column_partial_trace_vectorized_covariance(
    vectorized_covariance: Matrix,
    matrix_dimension: int,
) -> sp.Matrix:
    """Partial trace over D's column index: Sigma_(ij,kj) -> C^Gram_(ik)."""
    n = matrix_dimension
    if vectorized_covariance.shape != (n * n, n * n):
        raise ValueError("vectorized covariance shape must be n^2 x n^2")
    return sp.Matrix(
        n,
        n,
        lambda i, k: sp.simplify(
            sum(
                vectorized_covariance[i + j * n, k + j * n]
                for j in range(n)
            )
        ),
    )


def deformation_covariance_projection_residual(
    deformations: Sequence[Matrix],
    weights: Sequence[sp.Expr],
) -> sp.Matrix:
    """ptr_col Cov(vec D) - [E(DD^T)-E(D)E(D)^T]."""
    n = deformations[0].rows
    full = matrix_deformation_vectorized_covariance(deformations, weights)
    return sp.simplify(
        column_partial_trace_vectorized_covariance(full, n)
        - matrix_deformation_covariance(deformations, weights)
    )


def vectorized_deformation_pair_covariance(
    deformations: Sequence[Matrix],
    weights: Sequence[sp.Expr],
) -> sp.Matrix:
    """1/2 E[(vec D1-vec D2)(vec D1-vec D2)^T] for independent replicas."""
    if not deformations or len(deformations) != len(weights):
        raise ValueError("nonempty equally-sized deformation/weight lists required")
    vecs = [column_vectorize(D) for D in deformations]
    dim = vecs[0].rows
    out = sp.zeros(dim)
    for i, vi in enumerate(vecs):
        for j, vj in enumerate(vecs):
            delta = vi - vj
            out += sp.Rational(1, 2) * weights[i] * weights[j] * delta * delta.T
    return sp.simplify(out)


def vectorized_deformation_pair_covariance_residual(
    deformations: Sequence[Matrix],
    weights: Sequence[sp.Expr],
) -> sp.Matrix:
    return sp.simplify(
        vectorized_deformation_pair_covariance(deformations, weights)
        - matrix_deformation_vectorized_covariance(deformations, weights)
    )


def vectorized_deformation_carre_du_champ(
    mean_spatial_derivatives: Sequence[Matrix],
    nu: sp.Expr,
) -> sp.Matrix:
    """2 nu sum_mu vec(d_mu M) vec(d_mu M)^T; no direct D pathwise q.v."""
    if not mean_spatial_derivatives:
        raise ValueError("at least one spatial derivative is required")
    shape = mean_spatial_derivatives[0].shape
    if shape[0] != shape[1] or any(G.shape != shape for G in mean_spatial_derivatives):
        raise ValueError("square equal-sized mean derivatives required")
    dim = shape[0] * shape[1]
    out = sp.zeros(dim)
    for G in mean_spatial_derivatives:
        v = column_vectorize(G)
        out += 2 * nu * v * v.T
    return sp.simplify(out)


def projected_deformation_carre_du_champ(
    mean_spatial_derivatives: Sequence[Matrix],
    nu: sp.Expr,
) -> sp.Matrix:
    """Row-Gram projection 2 nu sum_mu (d_mu M)(d_mu M)^T."""
    if not mean_spatial_derivatives:
        raise ValueError("at least one spatial derivative is required")
    n = mean_spatial_derivatives[0].rows
    out = sp.zeros(n)
    for G in mean_spatial_derivatives:
        if G.shape != (n, n):
            raise ValueError("square equal-sized mean derivatives required")
        out += 2 * nu * G * G.T
    return sp.simplify(out)


def deformation_carre_du_champ_projection_residual(
    mean_spatial_derivatives: Sequence[Matrix],
    nu: sp.Expr,
) -> sp.Matrix:
    n = mean_spatial_derivatives[0].rows
    full = vectorized_deformation_carre_du_champ(mean_spatial_derivatives, nu)
    return sp.simplify(
        column_partial_trace_vectorized_covariance(full, n)
        - projected_deformation_carre_du_champ(mean_spatial_derivatives, nu)
    )


def reverse_age_horizon_operator_matrix(
    field: Matrix,
    horizon: sp.Symbol,
    current_time: sp.Symbol,
    velocity: Matrix,
    nu: sp.Expr,
    coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    """H=partial_h+partial_t+u.grad-nu Delta for dX=-u ds+sqrt(2nu)dW."""
    if velocity.shape != (len(coords), 1):
        raise ValueError("velocity dimension must match coordinates")
    return sp.Matrix(
        field.rows,
        field.cols,
        lambda i, j: sp.simplify(
            sp.diff(field[i, j], horizon)
            + sp.diff(field[i, j], current_time)
            + sum(velocity[a] * sp.diff(field[i, j], coords[a]) for a in range(len(coords)))
            - nu * sum(sp.diff(field[i, j], x, 2) for x in coords)
        ),
    )


def deformation_mean_horizon_residual(
    mean_deformation: Matrix,
    horizon_operator_mean: Matrix,
    grad_u: Matrix,
) -> sp.Matrix:
    """H M-A^T M for the current-end reverse-age multiplicative semigroup."""
    return sp.simplify(horizon_operator_mean - grad_u.T * mean_deformation)


def deformation_second_moment_horizon_residual(
    second_moment: Matrix,
    horizon_operator_second_moment: Matrix,
    grad_u: Matrix,
) -> sp.Matrix:
    """H R-A^T R-R A for R=E[DD^T]."""
    return sp.simplify(
        horizon_operator_second_moment
        - grad_u.T * second_moment
        - second_moment * grad_u
    )


def vectorized_deformation_covariance_horizon_residual(
    covariance: Matrix,
    horizon_operator_covariance: Matrix,
    grad_u: Matrix,
    mean_spatial_derivatives: Sequence[Matrix],
    nu: sp.Expr,
) -> sp.Matrix:
    """H Sigma-B Sigma-Sigma B^T-Gamma_vec for Sigma=Cov(vec D)."""
    B = vectorized_horizon_connection(grad_u)
    Gamma = vectorized_deformation_carre_du_champ(mean_spatial_derivatives, nu)
    return sp.simplify(
        horizon_operator_covariance - B * covariance - covariance * B.T - Gamma
    )


def projected_deformation_covariance_horizon_residual(
    covariance: Matrix,
    horizon_operator_covariance: Matrix,
    grad_u: Matrix,
    mean_spatial_derivatives: Sequence[Matrix],
    nu: sp.Expr,
) -> sp.Matrix:
    """H C-A^T C-C A-Gamma_Gram for the row-Gram covariance projection."""
    Gamma = projected_deformation_carre_du_champ(mean_spatial_derivatives, nu)
    return sp.simplify(
        horizon_operator_covariance
        - grad_u.T * covariance
        - covariance * grad_u
        - Gamma
    )


def vectorized_deformation_covariance_leading_tensor(
    grad_u_spatial_derivatives: Sequence[Matrix],
    nu: sp.Expr,
    horizon: sp.Expr,
) -> sp.Matrix:
    """Leading Cov(vec D): (2 nu/3) h^3 sum vec((d_mu A)^T) outer itself."""
    transposed = [G.T for G in grad_u_spatial_derivatives]
    return sp.simplify(
        sp.Rational(1, 3)
        * horizon**3
        * vectorized_deformation_carre_du_champ(transposed, nu)
    )


def projected_deformation_covariance_leading_tensor(
    grad_u_spatial_derivatives: Sequence[Matrix],
    nu: sp.Expr,
    horizon: sp.Expr,
) -> sp.Matrix:
    """Leading row-Gram covariance: (2 nu/3)h^3 sum (d_mu A)^T(d_mu A)."""
    if not grad_u_spatial_derivatives:
        raise ValueError("at least one spatial derivative is required")
    n = grad_u_spatial_derivatives[0].rows
    out = sp.zeros(n)
    for G in grad_u_spatial_derivatives:
        if G.shape != (n, n):
            raise ValueError("square equal-sized grad_u derivatives required")
        out += G.T * G
    return sp.simplify(sp.Rational(2, 3) * nu * horizon**3 * out)


def deformation_covariance_leading_projection_residual(
    grad_u_spatial_derivatives: Sequence[Matrix],
    nu: sp.Expr,
    horizon: sp.Expr,
) -> sp.Matrix:
    n = grad_u_spatial_derivatives[0].rows
    full = vectorized_deformation_covariance_leading_tensor(
        grad_u_spatial_derivatives, nu, horizon
    )
    projected = projected_deformation_covariance_leading_tensor(
        grad_u_spatial_derivatives, nu, horizon
    )
    return sp.simplify(column_partial_trace_vectorized_covariance(full, n) - projected)
