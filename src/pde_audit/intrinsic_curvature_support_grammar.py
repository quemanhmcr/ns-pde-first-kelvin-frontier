"""Intrinsic curvature--support grammar at max-normalized enstrophy critical points.

Let e=|omega|^2/2, M(t)>0 be a time-only normalization, g=e/M, and suppose

    D_t g = Phi,       D_t = partial_t + u.grad.

At a spatial critical point of g, Q=-Hess(g) obeys the exact covariant law

    D_t Q + A^T Q + Q A = K,       K=-Hess(Phi),   A=grad u.

A physical material line frame obeys D_t L=A L.  Therefore the deformation
connection cancels *matrix-wise* in the dimensionless curvature--support tensor

    C=L^T Q L,
    D_t C = L^T K L.

No inverse Hessian and no log-determinant are needed, so the law remains exact on
singular/degenerate maxima.  Along a differentiable critical branch with relative
speed c=xdot_*-u, the only extra face is the literal reanchoring term (c.grad)Q.

For Navier--Stokes max normalization,

    Phi = R/M - (Mdot/M) g,
    R = omega.S.omega - nu|grad omega|^2 + nu Delta e.

On ker Q the normalization face vanishes identically.  Hence the first-order law
that opens or preserves a flat direction is local NS source curvature (plus, on a
moving critical branch, the exact reanchoring face), not an externally supplied
badness score.

No first-bad identification, support-collapse theorem, restart, continuation, or
regularity theorem is asserted here.
"""
from __future__ import annotations

from collections.abc import Sequence
import sympy as sp

from .first_bad_candidate_exclusions import gradient
from .intrinsic_enstrophy_localization import (
    integer_scaled_one_mode_heat_shear,
    one_mode_intrinsic_localization_calibration,
)
from .local_enstrophy_kelvin_growth_gate import enstrophy_balance_faces
from .enstrophy_critical_hessian_evolution import directional_matrix_derivative

Matrix = sp.MatrixBase


def normalized_enstrophy_source(
    local_growth_rate: sp.Expr,
    max_enstrophy: sp.Expr,
    max_rate: sp.Expr,
    normalized_enstrophy: sp.Expr,
) -> sp.Expr:
    """Phi=R/M-(Mdot/M)g for max-normalized enstrophy."""
    return sp.simplify(
        local_growth_rate / max_enstrophy
        - max_rate * normalized_enstrophy / max_enstrophy
    )


def intrinsic_curvature_tensor(
    normalized_enstrophy: sp.Expr, coords: Sequence[sp.Symbol]
) -> Matrix:
    """Q=-Hess(g); Q is positive semidefinite at a smooth spatial maximum."""
    return sp.simplify(-sp.hessian(normalized_enstrophy, coords))


def normalized_source_curvature_tensor(
    normalized_source: sp.Expr, coords: Sequence[sp.Symbol]
) -> Matrix:
    """K=-Hess(Phi), the intrinsic curvature-creation tensor."""
    return sp.simplify(-sp.hessian(normalized_source, coords))


def critical_curvature_covariant_residual_at(
    normalized_enstrophy: sp.Expr,
    normalized_source: sp.Expr,
    velocity: Matrix,
    coords: Sequence[sp.Symbol],
    time: sp.Symbol,
    point: dict[sp.Symbol, sp.Expr],
) -> Matrix:
    """Residual of D_t Q + A^T Q + Q A = K at grad g=0."""
    Q = intrinsic_curvature_tensor(normalized_enstrophy, coords)
    K = normalized_source_curvature_tensor(normalized_source, coords)
    A = gradient(velocity, coords)
    material_Q = sp.diff(Q, time) + directional_matrix_derivative(Q, velocity, coords)
    residual = sp.simplify(material_Q + A.T * Q + Q * A - K)
    return sp.simplify(sp.trigsimp(residual.subs(point)))


def curvature_support_tensor(curvature: Matrix, line_frame: Matrix) -> Matrix:
    """C=L^T Q L, the dimensionless curvature measured in physical packet lines."""
    if curvature.shape != (3, 3) or line_frame.shape != (3, 3):
        raise ValueError("curvature and line frame must be 3x3")
    return sp.simplify(line_frame.T * curvature * line_frame)


def curvature_support_connection_cancellation_residual(
    grad_u: Matrix,
    curvature: Matrix,
    source_curvature: Matrix,
    line_frame: Matrix,
) -> Matrix:
    """Pure algebraic residual for Cdot=L^T K L under Qdot=-A^TQ-QA+K."""
    if any(M.shape != (3, 3) for M in (grad_u, curvature, source_curvature, line_frame)):
        raise ValueError("all tensors must be 3x3")
    Qdot = sp.simplify(-grad_u.T * curvature - curvature * grad_u + source_curvature)
    Ldot = sp.simplify(grad_u * line_frame)
    direct = sp.simplify(
        Ldot.T * curvature * line_frame
        + line_frame.T * Qdot * line_frame
        + line_frame.T * curvature * Ldot
    )
    return sp.simplify(direct - line_frame.T * source_curvature * line_frame)


def curvature_support_trace_connection_residual(
    grad_u: Matrix,
    curvature: Matrix,
    source_curvature: Matrix,
    support_tensor: Matrix,
) -> sp.Expr:
    """Residual of D_t tr(QB)=tr(KB), Bdot=A B+B A^T."""
    Qdot = sp.simplify(-grad_u.T * curvature - curvature * grad_u + source_curvature)
    Bdot = sp.simplify(grad_u * support_tensor + support_tensor * grad_u.T)
    direct = sp.simplify(sp.trace(Qdot * support_tensor) + sp.trace(curvature * Bdot))
    return sp.simplify(direct - sp.trace(source_curvature * support_tensor))


def moving_branch_effective_curvature_source(
    source_curvature: Matrix,
    curvature_field: Matrix,
    relative_critical_velocity: Matrix,
    coords: Sequence[sp.Symbol],
) -> Matrix:
    """K_* = K + ((xdot_*-u).grad)Q for a reanchored critical branch."""
    slip = directional_matrix_derivative(curvature_field, relative_critical_velocity, coords)
    return sp.simplify(source_curvature + slip)


def moving_branch_curvature_support_residual(
    grad_u: Matrix,
    curvature: Matrix,
    branch_curvature_rate: Matrix,
    effective_source: Matrix,
    line_frame: Matrix,
) -> Matrix:
    """Residual of d(L^TQL)/dt=L^T K_* L along local Nanson connection Ldot=A L."""
    Ldot = sp.simplify(grad_u * line_frame)
    direct = sp.simplify(
        Ldot.T * curvature * line_frame
        + line_frame.T * branch_curvature_rate * line_frame
        + line_frame.T * curvature * Ldot
    )
    return sp.simplify(direct - line_frame.T * effective_source * line_frame)


def kernel_quadratic_opening(source_curvature: Matrix, direction: Matrix) -> sp.Expr:
    """xi^T K xi, the first-order curvature opening of a Q-flat direction."""
    if source_curvature.shape != (3, 3) or direction.shape != (3, 1):
        raise ValueError("expected a 3x3 tensor and 3-vector")
    return sp.simplify((direction.T * source_curvature * direction)[0])


def kernel_normalization_face_residual(
    raw_growth_hessian: Matrix,
    curvature: Matrix,
    max_enstrophy: sp.Expr,
    max_rate: sp.Expr,
    kernel_direction: Matrix,
    normalized_source_curvature: Matrix,
) -> sp.Expr:
    """On Q xi=0, xi^T K xi=-(1/M) xi^T Hess(R) xi; Mdot normalization disappears."""
    lhs = kernel_quadratic_opening(normalized_source_curvature, kernel_direction)
    rhs = sp.simplify(
        -(kernel_direction.T * raw_growth_hessian * kernel_direction)[0] / max_enstrophy
        - (max_rate / max_enstrophy)
        * (kernel_direction.T * curvature * kernel_direction)[0]
    )
    return sp.simplify(lhs - rhs)


def one_mode_persistent_flat_kernel_calibration(
    amplitude: sp.Expr,
    mode: sp.Expr,
    coords: tuple[sp.Symbol, sp.Symbol, sp.Symbol],
    time: sp.Symbol,
    nu: sp.Expr,
) -> dict[str, sp.Expr | Matrix]:
    """Exact periodic one-mode NS: Q has two permanent flat directions and K=0."""
    _, y, _ = coords
    theta = sp.Rational(1, 2)
    cal = one_mode_intrinsic_localization_calibration(
        amplitude, mode, theta, coords, time, nu
    )
    g = sp.trigsimp(cal["normalized_enstrophy"])
    Q = intrinsic_curvature_tensor(g, coords)
    # g is stationary and u.grad g=0 in this x-shear, hence Phi=0 identically.
    Phi = sp.Integer(0)
    K = normalized_source_curvature_tensor(Phi, coords)
    point = {coords[0]: 0, y: 0, coords[2]: 0}
    Q0 = sp.simplify(Q.subs(point))
    return {
        "normalized_enstrophy": g,
        "curvature": Q0,
        "source_curvature": K,
        "x_flat_opening": kernel_quadratic_opening(K, sp.Matrix([1, 0, 0])),
        "z_flat_opening": kernel_quadratic_opening(K, sp.Matrix([0, 0, 1])),
        "covariant_residual": critical_curvature_covariant_residual_at(
            g, Phi, cal["velocity"], coords, time, point
        ),
    }


def psd_kernel_right_viability_quadratic(effective_source: Matrix, kernel_direction: Matrix) -> sp.Expr:
    """Quadratic form forced nonnegative by a right-persistent PSD maximum branch.

    If C(t)=L^T Q L is differentiable and positive semidefinite for t>=t0, with
    L z in ker Q at t0, then z^T C(t) z has a one-sided minimum zero.  The exact
    curvature--support grammar identifies its right derivative with this form.
    """
    return kernel_quadratic_opening(effective_source, kernel_direction)


def kernel_compression(projector: Matrix, tensor: Matrix) -> Matrix:
    """P0 T P0 on a supplied orthogonal projector P0 onto ker Q."""
    if projector.shape != (3, 3) or tensor.shape != (3, 3):
        raise ValueError("projector and tensor must be 3x3")
    return sp.simplify(projector * tensor * projector)


def coercive_curvature_support_trace_gap(
    curvature: Matrix, support_tensor: Matrix, coercivity: sp.Expr
) -> sp.Expr:
    """tr(QB)-kappa tr(B); nonnegative whenever Q-kappa I and B are PSD."""
    return sp.simplify(sp.trace(curvature * support_tensor) - coercivity * sp.trace(support_tensor))


def kernel_normalization_compression_residual(
    raw_growth_hessian: Matrix,
    curvature: Matrix,
    max_enstrophy: sp.Expr,
    max_rate: sp.Expr,
    kernel_projector: Matrix,
    normalized_source_curvature: Matrix,
) -> Matrix:
    """Matrix residual P0 K P0 + M^-1 P0 Hess(R) P0 on ker Q.

    The full source curvature is K=-Hess(R)/M-(Mdot/M)Q.  If P0 projects onto
    ker Q, the normalization term dies exactly after compression.
    """
    P = kernel_projector
    full_expected = sp.simplify(
        -raw_growth_hessian / max_enstrophy
        - (max_rate / max_enstrophy) * curvature
    )
    return sp.simplify(P * (normalized_source_curvature - full_expected) * P)
