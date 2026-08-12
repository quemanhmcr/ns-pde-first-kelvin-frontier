"""Exact finite-shape -> local Kelvin/Stokes descent identities.

The full Kelvin current is kept as a material surface/current observable.  The
local comparison is the anchor vorticity paired with the *actual* oriented area
vector of that finite surface.  Their difference is therefore a literal
finite-support vorticity-inhomogeneity flux, not a norm remainder.

On the reverse-age common-noise Kelvin state, only the anchor has Brownian
quadratic variation.  The finite relative shape has finite variation.  Hence the
descent error has two physically distinct channels:

* finite-variation strain-gradient/shape drift;
* anchor-translation martingale noise from vorticity-gradient variation across
  the actual surface.

The Cauchy deformation D is also finite variation, so its *pathwise* cross q.v.
with the descent error is exactly zero.  Finite-horizon covariance can still be
created through common noisy-anchor sampling; that is a connected-covariance
source, not pathwise [D,error].

No restart, continuation, singular-time, or regularity statement is made here.
"""
from __future__ import annotations

from typing import Sequence

import sympy as sp

from .full_current_shape_covariance import (
    deformation_kelvin_cross_covariance_leading_tensor,
    joint_deformation_kelvin_leading_covariance,
    joint_deformation_kelvin_leading_gramian,
)

Matrix = sp.MatrixBase


def kelvin_flux_local_readout(local_vorticity: Matrix, area_vector: Matrix) -> sp.Expr:
    """Local Stokes readout omega(X) dot h for the actual finite-surface area vector."""
    if local_vorticity.cols != 1 or area_vector.shape != local_vorticity.shape:
        raise ValueError("local vorticity and area vector must be equal column vectors")
    return sp.simplify((local_vorticity.T * area_vector)[0])


def kelvin_descent_error(
    actual_kelvin_flux: sp.Expr,
    local_vorticity: Matrix,
    area_vector: Matrix,
) -> sp.Expr:
    """epsilon_K = K_{Z(R)} - omega(X) dot h_R."""
    return sp.simplify(
        actual_kelvin_flux - kelvin_flux_local_readout(local_vorticity, area_vector)
    )


def reverse_age_local_area_rate(
    grad_u_anchor: Matrix,
    area_vector: Matrix,
    reverse_shape_gradient_residual: Matrix,
) -> Matrix:
    """Reverse-age finite-area law hdot=A(X)^T h+R_A.

    R_A = int_Sigma [(A(X+r)-A(X))^T n] dA.
    This is the reverse-age sign of the forward material shape current already
    audited in ``kelvin_shape_generator``.
    """
    if grad_u_anchor.rows != grad_u_anchor.cols:
        raise ValueError("grad_u_anchor must be square")
    if area_vector.shape != (grad_u_anchor.rows, 1):
        raise ValueError("area vector dimension mismatch")
    if reverse_shape_gradient_residual.shape != area_vector.shape:
        raise ValueError("shape residual dimension mismatch")
    return sp.simplify(grad_u_anchor.T * area_vector + reverse_shape_gradient_residual)


def reverse_age_local_vorticity_flux_drift(
    local_vorticity: Matrix,
    reverse_shape_gradient_residual: Matrix,
) -> sp.Expr:
    """Finite-variation drift of omega(X,r) dot h_R under reverse-age NS.

    Reverse-age Ito gives d omega = -A omega ds + sqrt(2nu) grad omega dW,
    while hdot=A^T h+R_A.  The local stretching terms cancel exactly, leaving
    omega dot R_A.
    """
    if local_vorticity.shape != reverse_shape_gradient_residual.shape:
        raise ValueError("vorticity/shape residual dimension mismatch")
    return sp.simplify((local_vorticity.T * reverse_shape_gradient_residual)[0])


def reverse_age_kelvin_descent_error_drift(
    local_vorticity: Matrix,
    reverse_shape_gradient_residual: Matrix,
) -> sp.Expr:
    """Drift of actual Kelvin flux minus local flux: -omega(X) dot R_A.

    The actual moving closed-current Kelvin drift is pure NS gauge and therefore
    zero.  Only the local finite-area approximation carries this shape drift.
    """
    return sp.simplify(
        -reverse_age_local_vorticity_flux_drift(
            local_vorticity, reverse_shape_gradient_residual
        )
    )


def kelvin_descent_error_noise_coefficients(
    actual_kelvin_noise_coefficients: Sequence[sp.Expr],
    local_vorticity_spatial_derivatives: Sequence[Matrix],
    area_vector: Matrix,
) -> list[sp.Expr]:
    """q_mu^err=a_mu(Z)-partial_mu omega(X) dot h_R.

    In a constant Euclidean noise frame, Stokes/Cartan identifies a_mu(Z) with
    the finite-surface integral of partial_mu omega.  Thus q_mu^err is precisely
    the vorticity-gradient variation across the actual support.
    """
    if len(actual_kelvin_noise_coefficients) != len(local_vorticity_spatial_derivatives):
        raise ValueError("actual/local noise lists must have equal length")
    out: list[sp.Expr] = []
    for a_mu, G in zip(actual_kelvin_noise_coefficients, local_vorticity_spatial_derivatives):
        if G.shape != area_vector.shape:
            raise ValueError("vorticity derivative/area vector dimension mismatch")
        out.append(sp.simplify(a_mu - (G.T * area_vector)[0]))
    return out


def kelvin_descent_error_qv_rate(
    noise_residuals: Sequence[sp.Expr],
    nu: sp.Expr,
) -> sp.Expr:
    """Pathwise d[epsilon_K]/ds = 2 nu sum_mu (q_mu^err)^2."""
    return sp.simplify(2 * nu * sum(q * q for q in noise_residuals))


def deformation_descent_error_pathwise_cross_qv(
    deformation_matrix_dim: int,
) -> Matrix:
    """Pathwise d[vec D,epsilon_K]/ds=0 because D has finite variation."""
    if deformation_matrix_dim <= 0:
        raise ValueError("deformation_matrix_dim must be positive")
    return sp.zeros(deformation_matrix_dim**2, 1)


def deformation_descent_error_cross_carre_du_champ(
    mean_deformation_spatial_derivatives: Sequence[Matrix],
    mean_error_spatial_derivatives: Sequence[sp.Expr],
    nu: sp.Expr,
) -> Matrix:
    """Full-state horizon source 2nu sum vec(d_mu Dbar) d_mu epsbar.

    This is a finite-horizon connected-covariance source.  It must not be confused
    with pathwise [D,epsilon_K], which is zero.
    """
    if not mean_deformation_spatial_derivatives:
        raise ValueError("at least one deformation derivative is required")
    if len(mean_deformation_spatial_derivatives) != len(mean_error_spatial_derivatives):
        raise ValueError("deformation/error derivative lists must have equal length")
    n = mean_deformation_spatial_derivatives[0].rows
    out = sp.zeros(n * n, 1)
    from .stochastic_cauchy_deformation import column_vectorize
    for G, g in zip(mean_deformation_spatial_derivatives, mean_error_spatial_derivatives):
        if G.shape != (n, n):
            raise ValueError("deformation derivatives must be equal square matrices")
        out += 2 * nu * column_vectorize(G) * g
    return sp.simplify(out)


def deformation_descent_error_leading_cross_covariance(
    grad_u_spatial_derivatives: Sequence[Matrix],
    error_anchor_derivatives: Sequence[sp.Expr],
    nu: sp.Expr,
    horizon: sp.Expr,
) -> Matrix:
    """Leading Cov(vec D,eps)=nu h^2 sum vec((d_mu A)^T) d_mu eps_0."""
    return deformation_kelvin_cross_covariance_leading_tensor(
        grad_u_spatial_derivatives, error_anchor_derivatives, nu, horizon
    )


def descent_error_variance_leading(
    error_anchor_derivatives: Sequence[sp.Expr],
    nu: sp.Expr,
    horizon: sp.Expr,
) -> sp.Expr:
    """Leading Var(eps)=2nu h sum_mu (d_mu eps_0)^2."""
    return sp.simplify(2 * nu * horizon * sum(g * g for g in error_anchor_derivatives))


def joint_deformation_error_leading_covariance(
    grad_u_spatial_derivatives: Sequence[Matrix],
    error_anchor_derivatives: Sequence[sp.Expr],
    nu: sp.Expr,
    horizon: sp.Expr,
) -> Matrix:
    """Leading joint covariance of (vec D,epsilon_K)."""
    return joint_deformation_kelvin_leading_covariance(
        grad_u_spatial_derivatives, error_anchor_derivatives, nu, horizon
    )


def joint_deformation_error_leading_gramian(
    grad_u_spatial_derivatives: Sequence[Matrix],
    error_anchor_derivatives: Sequence[sp.Expr],
    nu: sp.Expr,
    horizon: sp.Expr,
) -> Matrix:
    """Same leading joint covariance as one literal response Gram integral."""
    return joint_deformation_kelvin_leading_gramian(
        grad_u_spatial_derivatives, error_anchor_derivatives, nu, horizon
    )


def xy_rectangle_shear_kelvin_flux(
    shear_derivative: sp.Expr,
    y: sp.Symbol,
    anchor_y: sp.Expr,
    half_x: sp.Expr,
    half_y: sp.Expr,
) -> sp.Expr:
    """Kelvin/Stokes flux through an xy rectangle, normal +e_z, for u=U(y)e_x.

    curl(u)_z=-U_y.  The rectangle uses relative y in [-half_y,half_y] about
    anchor_y and x-width 2*half_x.
    """
    s = sp.Symbol("s_shape", real=True)
    integrand = -shear_derivative.subs(y, anchor_y + s)
    return sp.simplify(2 * half_x * sp.integrate(integrand, (s, -half_y, half_y)))


def xy_rectangle_shear_local_flux(
    shear_derivative: sp.Expr,
    y: sp.Symbol,
    anchor_y: sp.Expr,
    half_x: sp.Expr,
    half_y: sp.Expr,
) -> sp.Expr:
    """Local anchor flux (-U_y(anchor))*area for the same rectangle."""
    area = 4 * half_x * half_y
    return sp.simplify(-shear_derivative.subs(y, anchor_y) * area)


def xy_rectangle_shear_descent_error(
    shear_derivative: sp.Expr,
    y: sp.Symbol,
    anchor_y: sp.Expr,
    half_x: sp.Expr,
    half_y: sp.Expr,
) -> sp.Expr:
    return sp.simplify(
        xy_rectangle_shear_kelvin_flux(
            shear_derivative, y, anchor_y, half_x, half_y
        )
        - xy_rectangle_shear_local_flux(
            shear_derivative, y, anchor_y, half_x, half_y
        )
    )


def one_mode_shear_rectangle_error_shape_factor(
    half_x: sp.Expr,
    half_y: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """C_b=4 a[sin(kb)-kb] in eps=C_b e^{-alpha r} sin(kY)."""
    return sp.simplify(4 * half_x * (sp.sin(k * half_y) - k * half_y))


def one_mode_shear_rectangle_error_mean(
    y: sp.Expr,
    current_time: sp.Expr,
    half_x: sp.Expr,
    half_y: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    Cb = one_mode_shear_rectangle_error_shape_factor(half_x, half_y, k)
    return sp.simplify(Cb * sp.exp(-nu * k**2 * current_time) * sp.sin(k * y))


def one_mode_shear_rectangle_error_variance(
    y: sp.Expr,
    current_time: sp.Expr,
    horizon: sp.Expr,
    half_x: sp.Expr,
    half_y: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """Exact Var(eps_h) for the material xy rectangle in one-mode shear."""
    alpha = sp.simplify(nu * k**2)
    Cb = one_mode_shear_rectangle_error_shape_factor(half_x, half_y, k)
    mean = one_mode_shear_rectangle_error_mean(
        y, current_time, half_x, half_y, nu, k
    )
    second = sp.simplify(
        Cb**2
        * sp.Rational(1, 2)
        * sp.exp(-2 * alpha * (current_time - horizon))
        * (1 - sp.exp(-4 * alpha * horizon) * sp.cos(2 * k * y))
    )
    return sp.simplify(second - mean**2)


def one_mode_shear_deformation_rectangle_error_cross_covariance(
    y: sp.Expr,
    current_time: sp.Expr,
    horizon: sp.Expr,
    half_x: sp.Expr,
    half_y: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """Exact Cov(c_h,epsilon_h) in one-mode shear for the same reverse Brownian anchor."""
    alpha = sp.simplify(nu * k**2)
    Cb = one_mode_shear_rectangle_error_shape_factor(half_x, half_y, k)
    c2 = sp.cos(2 * k * y)
    bracket = sp.simplify(
        sp.exp(2 * alpha * horizon) - 1
        - c2 * (1 - sp.exp(-2 * alpha * horizon))
        - 2 * alpha * horizon * (1 - c2)
    )
    base = sp.simplify(
        -k * sp.exp(-2 * alpha * current_time) * bracket / (4 * alpha)
    )
    return sp.simplify(Cb * base)


def one_mode_shear_deformation_rectangle_error_cross_leading_residual(
    y: sp.Expr,
    current_time: sp.Expr,
    horizon: sp.Symbol,
    half_x: sp.Expr,
    half_y: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """Audit Cov(c_h,eps_h)=nu h^2 U_yy partial_y eps_0+O(h^3)."""
    U = sp.exp(-nu * k**2 * current_time) * sp.cos(k * y)
    eps0 = one_mode_shear_rectangle_error_mean(
        y, current_time, half_x, half_y, nu, k
    )
    leading = sp.simplify(
        nu * horizon**2 * sp.diff(U, y, 2) * sp.diff(eps0, y)
    )
    exact = one_mode_shear_deformation_rectangle_error_cross_covariance(
        y, current_time, horizon, half_x, half_y, nu, k
    )
    return sp.trigsimp(
        sp.simplify(sp.series(exact, horizon, 0, 3).removeO() - leading)
    )


def abc_origin_xy_reverse_shape_residual(
    amplitude: sp.Expr,
    nu: sp.Expr,
    time: sp.Expr,
    halfwidth: sp.Expr,
) -> Matrix:
    """Exact R_A for the centered xy square, normal +e_z, in unit ABC flow at origin."""
    q = sp.simplify(4 * amplitude * sp.exp(-nu * time) * halfwidth * (sp.sin(halfwidth) - halfwidth))
    return sp.Matrix([0, q, 0])


def abc_origin_xy_local_vorticity(
    amplitude: sp.Expr,
    nu: sp.Expr,
    time: sp.Expr,
) -> Matrix:
    """ABC is Beltrami: omega(0)=A e^{-nu t}(1,1,1)."""
    q = sp.simplify(amplitude * sp.exp(-nu * time))
    return sp.Matrix([q, q, q])


def abc_origin_xy_kelvin_descent_error(
    amplitude: sp.Expr,
    nu: sp.Expr,
    time: sp.Expr,
    halfwidth: sp.Expr,
) -> sp.Expr:
    """Exact initial flux error through centered xy square, normal +e_z, at origin."""
    return sp.simplify(
        4 * amplitude * sp.exp(-nu * time) * halfwidth * (sp.sin(halfwidth) - halfwidth)
    )


def centered_kelvin_error_quadrupole_leading(
    omega_second_derivatives: Sequence[Sequence[Matrix]],
    oriented_second_moments: Sequence[Sequence[Matrix]],
) -> sp.Expr:
    """1/2 sum_kl (partial_kl omega) dot M_kl for a centered finite surface.

    M_kl = int r_k r_l n dA is a *vector-valued* oriented surface moment.  The
    linear first-moment term has already been removed by centering.
    """
    n = len(omega_second_derivatives)
    if n == 0 or len(oriented_second_moments) != n:
        raise ValueError("nonempty equal spatial dimensions required")
    out = sp.Integer(0)
    for k in range(n):
        if len(omega_second_derivatives[k]) != n or len(oriented_second_moments[k]) != n:
            raise ValueError("second-derivative/moment arrays must be square")
        for ell in range(n):
            d2w = omega_second_derivatives[k][ell]
            M = oriented_second_moments[k][ell]
            if d2w.shape != (n, 1) or M.shape != (n, 1):
                raise ValueError("derivative and oriented moment entries must be spatial vectors")
            out += sp.Rational(1, 2) * (d2w.T * M)[0]
    return sp.simplify(out)


def centered_reverse_shape_residual_quadrupole_leading(
    grad_u_second_derivatives: Sequence[Sequence[Matrix]],
    oriented_second_moments: Sequence[Sequence[Matrix]],
) -> Matrix:
    """1/2 sum_kl (partial_kl A)^T M_kl, the centered reverse shape-current jet."""
    n = len(grad_u_second_derivatives)
    if n == 0 or len(oriented_second_moments) != n:
        raise ValueError("nonempty equal spatial dimensions required")
    out = sp.zeros(n, 1)
    for k in range(n):
        if len(grad_u_second_derivatives[k]) != n or len(oriented_second_moments[k]) != n:
            raise ValueError("second-derivative/moment arrays must be square")
        for ell in range(n):
            d2A = grad_u_second_derivatives[k][ell]
            M = oriented_second_moments[k][ell]
            if d2A.shape != (n, n) or M.shape != (n, 1):
                raise ValueError("grad-u derivative must be matrix and moment must be vector")
            out += sp.Rational(1, 2) * d2A.T * M
    return sp.simplify(out)


def centered_error_noise_quadrupole_leading(
    omega_third_derivatives: Sequence[Sequence[Sequence[Matrix]]],
    oriented_second_moments: Sequence[Sequence[Matrix]],
) -> list[sp.Expr]:
    """Leading q_mu^err=1/2 sum_kl (partial_mu,kl omega) dot M_kl.

    Thus the centered error q.v. samples one more spatial derivative than the
    deterministic descent bias itself.
    """
    n = len(omega_third_derivatives)
    if n == 0 or len(oriented_second_moments) != n:
        raise ValueError("nonempty equal spatial dimensions required")
    out: list[sp.Expr] = []
    for mu in range(n):
        if len(omega_third_derivatives[mu]) != n:
            raise ValueError("third-derivative array must be cubic")
        q = sp.Integer(0)
        for k in range(n):
            if len(omega_third_derivatives[mu][k]) != n or len(oriented_second_moments[k]) != n:
                raise ValueError("third-derivative/moment arrays have wrong dimensions")
            for ell in range(n):
                d3w = omega_third_derivatives[mu][k][ell]
                M = oriented_second_moments[k][ell]
                if d3w.shape != (n, 1) or M.shape != (n, 1):
                    raise ValueError("derivative and moment entries must be spatial vectors")
                q += sp.Rational(1, 2) * (d3w.T * M)[0]
        out.append(sp.simplify(q))
    return out


def reverse_age_local_tangent_rate(grad_u_anchor: Matrix, tangent: Matrix) -> Matrix:
    """Actual backward-current differential tangent rate: ell_dot=-A ell."""
    if grad_u_anchor.rows != grad_u_anchor.cols or tangent.shape != (grad_u_anchor.rows, 1):
        raise ValueError("gradient/tangent dimension mismatch")
    return sp.simplify(-grad_u_anchor * tangent)


def cauchy_metric_dual_area_frame_rate(grad_u_anchor: Matrix, area_frame: Matrix) -> Matrix:
    """Rate of H_C=rho^2 D^{-1} when Ddot=D A^T: H_Cdot=-A^T H_C.

    H_C is the same-replica Cauchy packet-metric dual already audited elsewhere.
    It is *not* the oriented area frame of the current being marched backward in
    reverse age; that actual local backward-current area has +A^T connection.
    """
    if grad_u_anchor.rows != grad_u_anchor.cols or area_frame.rows != grad_u_anchor.rows:
        raise ValueError("gradient/area frame dimension mismatch")
    return sp.simplify(-grad_u_anchor.T * area_frame)
