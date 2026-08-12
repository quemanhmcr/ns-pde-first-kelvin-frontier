"""Exact full current-shape anchor covariance and deformation--Kelvin cross laws.

The physical backward Kelvin current is written in anchor/relative-shape coordinates.
In reverse age the only Brownian directions are the spatial anchor coordinates.  The
relative shape and the Cauchy deformation are finite-variation state coordinates.
Consequently every same-ancestor covariance source on the full state is an anchor
carre-du-champ.  This module keeps that source separate from first-order shape and
deformation transport and records the mixed deformation--Kelvin block forced by the
same noisy anchor.

No restart, continuation, singular-time, or regularity statement is made here.
"""
from __future__ import annotations

from typing import Sequence

import sympy as sp

from .stochastic_cauchy_deformation import (
    column_vectorize,
    vectorized_deformation_covariance_leading_tensor,
    vectorized_horizon_connection,
)

Matrix = sp.MatrixBase


def reverse_age_current_shape_diffusion_covariance(
    relative_count: int,
    spatial_dim: int,
    deformation_matrix_dim: int,
    nu: sp.Expr,
) -> sp.Matrix:
    """Full-state covariance for (X,R_1,...,R_N,vec D): only X is noisy.

    The physical time coordinate r=t-sigma, if carried explicitly, has zero row and
    column and can be adjoined separately.  Relative shape and D have zero direct
    martingale covariance.
    """
    if relative_count < 0 or spatial_dim <= 0 or deformation_matrix_dim <= 0:
        raise ValueError("invalid state dimensions")
    size = spatial_dim * (1 + relative_count) + deformation_matrix_dim**2
    out = sp.zeros(size)
    out[:spatial_dim, :spatial_dim] = 2 * nu * sp.eye(spatial_dim)
    return out


def reverse_age_current_shape_drift(
    anchor_velocity: Matrix,
    point_velocities: Sequence[Matrix],
    deformation: Matrix,
    grad_u_anchor: Matrix,
) -> sp.Matrix:
    """Reverse-age drift for (X,R_1,...,R_N,vec D), excluding rdot=-1.

      Xdot = -u(X),
      R_p dot = -[u(X+R_p)-u(X)],
      Ddot = D (grad u(X))^T.

    The first two signs are the reverse-age form of the physical backward-Kelvin
    current-shape generator; the D convention is the stochastic Cauchy convention
    already audited in ``stochastic_cauchy_deformation``.
    """
    dim = anchor_velocity.rows
    if anchor_velocity.shape != (dim, 1):
        raise ValueError("anchor_velocity must be a column vector")
    if any(v.shape != (dim, 1) for v in point_velocities):
        raise ValueError("point velocity dimension mismatch")
    if deformation.rows != deformation.cols or grad_u_anchor.shape != deformation.shape:
        raise ValueError("deformation and grad_u_anchor must be equal square matrices")
    blocks: list[sp.Matrix] = [-anchor_velocity]
    blocks.extend([sp.simplify(-(v - anchor_velocity)) for v in point_velocities])
    blocks.append(column_vectorize(sp.simplify(deformation * grad_u_anchor.T)))
    return sp.Matrix.vstack(*blocks)


def anchor_cross_carre_du_champ(
    left_mean: Matrix,
    right_mean: Matrix,
    anchor_coords: Sequence[sp.Symbol],
    nu: sp.Expr,
) -> sp.Matrix:
    """2 nu sum_mu (d_Xmu left)(d_Xmu right)^T on the full current-shape state."""
    if left_mean.cols != 1 or right_mean.cols != 1:
        raise ValueError("means must be column vectors")
    out = sp.zeros(left_mean.rows, right_mean.rows)
    for x in anchor_coords:
        dl = left_mean.diff(x)
        dr = right_mean.diff(x)
        out += 2 * nu * dl * dr.T
    return sp.simplify(out)


def full_state_carre_du_champ(
    mean: Matrix,
    state_coords: Sequence[sp.Symbol],
    diffusion_covariance: Matrix,
) -> sp.Matrix:
    """J a J^T, exposed here to audit that only the anchor block contributes."""
    if mean.cols != 1:
        raise ValueError("mean must be a column vector")
    if diffusion_covariance.shape != (len(state_coords), len(state_coords)):
        raise ValueError("diffusion covariance/state dimension mismatch")
    J = sp.Matrix([[sp.diff(mean[i], x) for x in state_coords] for i in range(mean.rows)])
    return sp.simplify(J * diffusion_covariance * J.T)


def one_form_lie_derivative(
    one_form: Matrix,
    vector_field: Matrix,
    coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    """Coordinate Lie derivative (L_v beta)_i=v^j d_j beta_i+beta_j d_i v^j."""
    n = len(coords)
    if one_form.shape != (n, 1) or vector_field.shape != (n, 1):
        raise ValueError("one_form/vector_field dimension mismatch")
    return sp.Matrix([
        sp.simplify(
            sum(vector_field[j] * sp.diff(one_form[i], coords[j]) for j in range(n))
            + sum(one_form[j] * sp.diff(vector_field[j], coords[i]) for j in range(n))
        )
        for i in range(n)
    ])


def navier_stokes_kelvin_gauge_residual(
    velocity: Matrix,
    pressure: sp.Expr,
    time: sp.Symbol,
    coords: Sequence[sp.Symbol],
    nu: sp.Expr,
) -> sp.Matrix:
    """Audit (d_t+L_u-nu Delta)u^flat=d(1/2|u|^2-p) for incompressible NS.

    The returned residual is exactly the velocity-form Navier--Stokes residual in
    Kelvin/Cartan typing.  On a closed material current the right-hand exact form has
    zero circulation, so the finite-variation Kelvin drift vanishes.
    """
    n = len(coords)
    if velocity.shape != (n, 1):
        raise ValueError("velocity dimension mismatch")
    lie = one_form_lie_derivative(velocity, velocity, coords)
    lap = sp.Matrix([
        sum(sp.diff(velocity[i], x, 2) for x in coords) for i in range(n)
    ])
    kelvin_drift = sp.simplify(sp.diff(velocity, time) + lie - nu * lap)
    gauge_scalar = sp.simplify(sp.Rational(1, 2) * (velocity.T * velocity)[0] - pressure)
    gauge = sp.Matrix([sp.diff(gauge_scalar, x) for x in coords])
    return sp.simplify(kelvin_drift - gauge)


def translation_cartan_residual(
    one_form: Matrix,
    coords: Sequence[sp.Symbol],
    direction_index: int,
) -> sp.Matrix:
    """Audit d_mu beta = i_{e_mu} d beta + d(beta_mu) in a constant frame."""
    n = len(coords)
    if one_form.shape != (n, 1) or not 0 <= direction_index < n:
        raise ValueError("one_form/direction dimension mismatch")
    mu = direction_index
    contraction = sp.Matrix([
        sp.diff(one_form[i], coords[mu]) - sp.diff(one_form[mu], coords[i])
        for i in range(n)
    ])
    exact = sp.Matrix([sp.diff(one_form[mu], x) for x in coords])
    translation = sp.Matrix([sp.diff(one_form[i], coords[mu]) for i in range(n)])
    return sp.simplify(translation - contraction - exact)


def closed_current_cartan_noise_residual(
    boundary: Matrix,
    current: Matrix,
    curvature_contraction: Matrix,
    scalar_potential: Matrix,
) -> sp.Expr:
    """Closed-current Cartan residual for L_e beta=i_e d beta+d(i_e beta).

    Finite-chain typing uses ``d potential = boundary.T * potential``.  The
    translation derivative cochain is therefore ``curvature_contraction+B.T*p``.
    For a closed current B Z=0 its circulation equals the curvature-contraction
    circulation exactly.
    """
    if current.cols != 1 or curvature_contraction.cols != 1 or scalar_potential.cols != 1:
        raise ValueError("current/cochains must be column vectors")
    if boundary.cols != current.rows or curvature_contraction.rows != current.rows:
        raise ValueError("chain dimensions do not match")
    if boundary.rows != scalar_potential.rows:
        raise ValueError("potential dimension does not match boundary")
    translation_derivative = sp.simplify(curvature_contraction + boundary.T * scalar_potential)
    return sp.simplify(
        (translation_derivative.T * current)[0]
        - (curvature_contraction.T * current)[0]
    )


def kelvin_pair_anchor_source(
    left_noise_coefficients: Sequence[sp.Expr],
    right_noise_coefficients: Sequence[sp.Expr],
    nu: sp.Expr,
) -> sp.Expr:
    """Polarized Kelvin anchor source 2 nu sum_mu a_mu(Z) a_mu(Z')."""
    if len(left_noise_coefficients) != len(right_noise_coefficients):
        raise ValueError("noise coefficient lists must have equal length")
    return sp.simplify(
        2 * nu * sum(a * b for a, b in zip(left_noise_coefficients, right_noise_coefficients))
    )


def deformation_kelvin_cross_carre_du_champ(
    mean_deformation_spatial_derivatives: Sequence[Matrix],
    kelvin_mean_spatial_derivatives: Sequence[sp.Expr],
    nu: sp.Expr,
) -> sp.Matrix:
    """Anchor source 2nu sum vec(d_mu Dbar) (d_mu Kbar) for Cov(vec D,K)."""
    if not mean_deformation_spatial_derivatives:
        raise ValueError("at least one spatial derivative is required")
    if len(mean_deformation_spatial_derivatives) != len(kelvin_mean_spatial_derivatives):
        raise ValueError("deformation/Kelvin derivative lists must have equal length")
    n = mean_deformation_spatial_derivatives[0].rows
    if any(G.shape != (n, n) for G in mean_deformation_spatial_derivatives):
        raise ValueError("deformation derivatives must be equal square matrices")
    out = sp.zeros(n * n, 1)
    for G, g in zip(mean_deformation_spatial_derivatives, kelvin_mean_spatial_derivatives):
        out += 2 * nu * column_vectorize(G) * g
    return sp.simplify(out)


def deformation_kelvin_cross_covariance_horizon_residual(
    cross_covariance: Matrix,
    horizon_operator_cross_covariance: Matrix,
    grad_u: Matrix,
    mean_deformation_spatial_derivatives: Sequence[Matrix],
    kelvin_mean_spatial_derivatives: Sequence[sp.Expr],
    nu: sp.Expr,
) -> sp.Matrix:
    """H C_DK - B C_DK - Gamma_DK for scalar Kelvin payoff K."""
    B = vectorized_horizon_connection(grad_u)
    source = deformation_kelvin_cross_carre_du_champ(
        mean_deformation_spatial_derivatives,
        kelvin_mean_spatial_derivatives,
        nu,
    )
    if cross_covariance.shape != source.shape:
        raise ValueError("cross covariance dimension mismatch")
    return sp.simplify(horizon_operator_cross_covariance - B * cross_covariance - source)


def deformation_kelvin_cross_covariance_leading_tensor(
    grad_u_spatial_derivatives: Sequence[Matrix],
    kelvin_anchor_derivatives: Sequence[sp.Expr],
    nu: sp.Expr,
    horizon: sp.Expr,
) -> sp.Matrix:
    """Leading Cov(vec D,K)=nu h^2 sum vec((d_mu A)^T) d_mu K_0 + O(h^3)."""
    if len(grad_u_spatial_derivatives) != len(kelvin_anchor_derivatives):
        raise ValueError("gradient/Kelvin derivative lists must have equal length")
    n = grad_u_spatial_derivatives[0].rows
    out = sp.zeros(n * n, 1)
    for G, g in zip(grad_u_spatial_derivatives, kelvin_anchor_derivatives):
        if G.shape != (n, n):
            raise ValueError("grad_u derivatives must be equal square matrices")
        out += column_vectorize(G.T) * g
    return sp.simplify(nu * horizon**2 * out)


def kelvin_variance_leading(
    kelvin_anchor_derivatives: Sequence[sp.Expr],
    nu: sp.Expr,
    horizon: sp.Expr,
) -> sp.Expr:
    """Leading scalar Kelvin variance 2 nu h sum_mu (d_mu K_0)^2."""
    return sp.simplify(2 * nu * horizon * sum(g**2 for g in kelvin_anchor_derivatives))


def joint_deformation_kelvin_leading_covariance(
    grad_u_spatial_derivatives: Sequence[Matrix],
    kelvin_anchor_derivatives: Sequence[sp.Expr],
    nu: sp.Expr,
    horizon: sp.Expr,
) -> sp.Matrix:
    """Leading joint covariance of (vec D,K), keeping the forced cross block."""
    Sigma_D = vectorized_deformation_covariance_leading_tensor(
        grad_u_spatial_derivatives, nu, horizon
    )
    C_DK = deformation_kelvin_cross_covariance_leading_tensor(
        grad_u_spatial_derivatives, kelvin_anchor_derivatives, nu, horizon
    )
    V_K = kelvin_variance_leading(kelvin_anchor_derivatives, nu, horizon)
    top = Sigma_D.row_join(C_DK)
    bottom = C_DK.T.row_join(sp.Matrix([[V_K]]))
    return sp.simplify(top.col_join(bottom))


def joint_deformation_kelvin_leading_gramian(
    grad_u_spatial_derivatives: Sequence[Matrix],
    kelvin_anchor_derivatives: Sequence[sp.Expr],
    nu: sp.Expr,
    horizon: sp.Expr,
) -> sp.Matrix:
    """Exact Gram-integral representation of the leading joint block.

      2 nu sum_mu int_0^h [s v_mu; g_mu][s v_mu; g_mu]^T ds,

    v_mu=vec((d_mu A)^T), g_mu=d_mu K_0.  This makes PSD and the h^3/h^2/h
    hierarchy literal rather than an inequality estimate.
    """
    if len(grad_u_spatial_derivatives) != len(kelvin_anchor_derivatives):
        raise ValueError("gradient/Kelvin derivative lists must have equal length")
    s = sp.Symbol("s_joint", nonnegative=True)
    n = grad_u_spatial_derivatives[0].rows
    out = sp.zeros(n * n + 1)
    for G, g in zip(grad_u_spatial_derivatives, kelvin_anchor_derivatives):
        v = column_vectorize(G.T)
        response = (s * v).col_join(sp.Matrix([g]))
        out += 2 * nu * response * response.T
    return sp.simplify(out.applyfunc(lambda entry: sp.integrate(entry, (s, 0, horizon))))


def joint_deformation_kelvin_leading_gramian_residual(
    grad_u_spatial_derivatives: Sequence[Matrix],
    kelvin_anchor_derivatives: Sequence[sp.Expr],
    nu: sp.Expr,
    horizon: sp.Expr,
) -> sp.Matrix:
    return sp.simplify(
        joint_deformation_kelvin_leading_covariance(
            grad_u_spatial_derivatives, kelvin_anchor_derivatives, nu, horizon
        )
        - joint_deformation_kelvin_leading_gramian(
            grad_u_spatial_derivatives, kelvin_anchor_derivatives, nu, horizon
        )
    )


def one_mode_shear_kelvin_mean(
    y: sp.Expr,
    current_time: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """Normalized x-cycle Kelvin mean U(y,t) for u=exp(-nu k^2 t) cos(ky)e_x."""
    return sp.simplify(sp.exp(-nu * k**2 * current_time) * sp.cos(k * y))


def one_mode_shear_kelvin_variance(
    y: sp.Expr,
    current_time: sp.Expr,
    horizon: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """Exact Var(K_h) for K_h=e^{-alpha(t-h)} cos(kY_h)."""
    alpha = sp.simplify(nu * k**2)
    mean = one_mode_shear_kelvin_mean(y, current_time, nu, k)
    second = sp.simplify(
        sp.Rational(1, 2)
        * sp.exp(-2 * alpha * (current_time - horizon))
        * (1 + sp.exp(-4 * alpha * horizon) * sp.cos(2 * k * y))
    )
    return sp.simplify(second - mean**2)


def one_mode_shear_deformation_kelvin_cross_covariance(
    y: sp.Expr,
    current_time: sp.Expr,
    horizon: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """Exact Cov(c_h,K_h) for the same reverse Brownian anchor in one-mode shear.

    c_h=int_0^h U_y(Y_s,t-s)ds and
    K_h=exp[-alpha(t-h)] cos(kY_h), alpha=nu k^2.
    """
    alpha = sp.simplify(nu * k**2)
    return sp.simplify(
        k
        * sp.exp(-2 * alpha * current_time)
        * sp.sin(2 * k * y)
        / (4 * alpha)
        * (2 * alpha * horizon - 1 + sp.exp(-2 * alpha * horizon))
    )


def one_mode_shear_deformation_kelvin_cross_leading_residual(
    y: sp.Expr,
    current_time: sp.Expr,
    horizon: sp.Symbol,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """Audit Cov(c_h,K_h)=nu h^2 U_yy U_y+O(h^3)."""
    U = one_mode_shear_kelvin_mean(y, current_time, nu, k)
    leading = sp.simplify(nu * horizon**2 * sp.diff(U, y, 2) * sp.diff(U, y))
    exact = one_mode_shear_deformation_kelvin_cross_covariance(
        y, current_time, horizon, nu, k
    )
    return sp.trigsimp(sp.simplify(sp.series(exact, horizon, 0, 3).removeO() - leading))
