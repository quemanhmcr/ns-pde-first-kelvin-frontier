"""Directional and refinement/event balance for the physical Kelvin residual.

The literal physical residual energy is bilinear in the primal line metric M=L^T L
and residual second moment Q.  This module keeps geometry, residual/current content,
and random-frame metric--residual correlation as separate physical faces.

No first-bad threshold, future-bank, restart, continuation, or regularity claim is
made here.
"""
from __future__ import annotations

from collections.abc import Sequence
import sympy as sp

from .weighted_codeforming_kelvin_residual import (
    asymmetric_rectangle_shear_error_from_velocity,
    primal_line_metric,
    quadratic_heat_shear,
)

Matrix = sp.MatrixBase


def weighted_energy(metric: Matrix, residual_second_moment: Matrix) -> sp.Expr:
    if metric.shape != residual_second_moment.shape or metric.rows != metric.cols:
        raise ValueError("metric and second moment must be equal square matrices")
    return sp.simplify(sp.trace(metric * residual_second_moment))


def spectral_metric(principal_vectors: Matrix, squared_line_scales: Sequence[sp.Expr]) -> Matrix:
    n = principal_vectors.rows
    if principal_vectors.cols != n or len(squared_line_scales) != n:
        raise ValueError("principal frame and line scales must have common dimension")
    return sp.simplify(
        principal_vectors * sp.diag(*squared_line_scales) * principal_vectors.T
    )


def directional_weighted_terms(
    residual_second_moment: Matrix,
    principal_vectors: Matrix,
    squared_line_scales: Sequence[sp.Expr],
) -> list[sp.Expr]:
    n = principal_vectors.rows
    if residual_second_moment.shape != (n, n) or principal_vectors.shape != (n, n):
        raise ValueError("directional data dimension mismatch")
    if len(squared_line_scales) != n:
        raise ValueError("one squared line scale per principal direction is required")
    out=[]
    for i,s2 in enumerate(squared_line_scales):
        v=principal_vectors[:,i]
        out.append(sp.simplify(s2 * (v.T * residual_second_moment * v)[0]))
    return out


def directional_weighted_energy_residual(
    residual_second_moment: Matrix,
    principal_vectors: Matrix,
    squared_line_scales: Sequence[sp.Expr],
) -> sp.Expr:
    metric=spectral_metric(principal_vectors,squared_line_scales)
    return sp.simplify(
        weighted_energy(metric,residual_second_moment)
        - sum(directional_weighted_terms(residual_second_moment,principal_vectors,squared_line_scales))
    )


def directional_bias_spread_terms(
    mean_residual: Matrix,
    covariance: Matrix,
    principal_vectors: Matrix,
    squared_line_scales: Sequence[sp.Expr],
) -> list[sp.Expr]:
    n=mean_residual.rows
    if mean_residual.shape != (n,1) or covariance.shape != (n,n):
        raise ValueError("mean/covariance dimension mismatch")
    if principal_vectors.shape != (n,n) or len(squared_line_scales) != n:
        raise ValueError("principal data dimension mismatch")
    out=[]
    for i,s2 in enumerate(squared_line_scales):
        v=principal_vectors[:,i]
        bias=sp.simplify((v.T*mean_residual)[0]**2)
        spread=sp.simplify((v.T*covariance*v)[0])
        out.append(sp.simplify(s2*(bias+spread)))
    return out


def midpoint_revaluation_faces(
    metric_minus: Matrix,
    second_moment_minus: Matrix,
    metric_plus: Matrix,
    second_moment_plus: Matrix,
) -> tuple[sp.Expr,sp.Expr]:
    """Return exact geometry and state/current midpoint faces."""
    if not (
        metric_minus.shape == second_moment_minus.shape == metric_plus.shape == second_moment_plus.shape
    ):
        raise ValueError("all event tensors must have equal shape")
    Mbar=sp.simplify((metric_plus+metric_minus)/2)
    Qbar=sp.simplify((second_moment_plus+second_moment_minus)/2)
    dM=sp.simplify(metric_plus-metric_minus)
    dQ=sp.simplify(second_moment_plus-second_moment_minus)
    geometry=sp.simplify(sp.trace(Qbar*dM))
    state=sp.simplify(sp.trace(dQ*Mbar))
    return geometry,state


def midpoint_revaluation_residual(
    metric_minus: Matrix,
    second_moment_minus: Matrix,
    metric_plus: Matrix,
    second_moment_plus: Matrix,
) -> sp.Expr:
    geometry,state=midpoint_revaluation_faces(
        metric_minus,second_moment_minus,metric_plus,second_moment_plus
    )
    jump=sp.simplify(
        weighted_energy(metric_plus,second_moment_plus)
        - weighted_energy(metric_minus,second_moment_minus)
    )
    return sp.simplify(jump-geometry-state)


def right_refinement_metric_residual(
    line_frame: Matrix,
    refinement: Matrix,
) -> Matrix:
    """Audit M(LR)=R^T M(L) R for the repo's physical right-refinement convention."""
    if line_frame.shape != refinement.shape or line_frame.rows != line_frame.cols:
        raise ValueError("line frame/refinement must be equal square matrices")
    lhs=primal_line_metric(sp.simplify(line_frame*refinement))
    rhs=sp.simplify(refinement.T*primal_line_metric(line_frame)*refinement)
    return sp.simplify(lhs-rhs)


def passive_reparameterized_second_moment(
    second_moment: Matrix,
    refinement: Matrix,
) -> Matrix:
    if second_moment.shape != refinement.shape or refinement.rows != refinement.cols:
        raise ValueError("second moment/refinement must be equal square matrices")
    Rinv=sp.simplify(refinement.inv())
    return sp.simplify(Rinv*second_moment*Rinv.T)


def passive_reparameterization_energy_residual(
    metric: Matrix,
    second_moment: Matrix,
    refinement: Matrix,
) -> sp.Expr:
    metric_plus=sp.simplify(refinement.T*metric*refinement)
    Qplus=passive_reparameterized_second_moment(second_moment,refinement)
    return sp.simplify(
        weighted_energy(metric_plus,Qplus)-weighted_energy(metric,second_moment)
    )


def passive_midpoint_face_sum_residual(
    metric: Matrix,
    second_moment: Matrix,
    refinement: Matrix,
) -> sp.Expr:
    metric_plus=sp.simplify(refinement.T*metric*refinement)
    Qplus=passive_reparameterized_second_moment(second_moment,refinement)
    geometry,state=midpoint_revaluation_faces(metric,second_moment,metric_plus,Qplus)
    return sp.simplify(geometry+state)


def ensemble_energy(mean_metric: Matrix, mean_second_moment: Matrix, mixed_correlation: sp.Expr) -> sp.Expr:
    return sp.simplify(weighted_energy(mean_metric,mean_second_moment)+mixed_correlation)


def ensemble_event_three_faces(
    mean_metric_minus: Matrix,
    mean_second_moment_minus: Matrix,
    mixed_correlation_minus: sp.Expr,
    mean_metric_plus: Matrix,
    mean_second_moment_plus: Matrix,
    mixed_correlation_plus: sp.Expr,
) -> tuple[sp.Expr,sp.Expr,sp.Expr]:
    geometry,state=midpoint_revaluation_faces(
        mean_metric_minus,mean_second_moment_minus,
        mean_metric_plus,mean_second_moment_plus,
    )
    correlation=sp.simplify(mixed_correlation_plus-mixed_correlation_minus)
    return geometry,state,correlation


def ensemble_event_three_face_residual(
    mean_metric_minus: Matrix,
    mean_second_moment_minus: Matrix,
    mixed_correlation_minus: sp.Expr,
    mean_metric_plus: Matrix,
    mean_second_moment_plus: Matrix,
    mixed_correlation_plus: sp.Expr,
) -> sp.Expr:
    faces=ensemble_event_three_faces(
        mean_metric_minus,mean_second_moment_minus,mixed_correlation_minus,
        mean_metric_plus,mean_second_moment_plus,mixed_correlation_plus,
    )
    jump=sp.simplify(
        ensemble_energy(mean_metric_plus,mean_second_moment_plus,mixed_correlation_plus)
        - ensemble_energy(mean_metric_minus,mean_second_moment_minus,mixed_correlation_minus)
    )
    return sp.simplify(jump-sum(faces))


def scale_shape_smooth_rate_residual(
    residual_second_moment: Matrix,
    second_moment_rate: Matrix,
    rho: sp.Expr,
    rho_rate: sp.Expr,
    anisotropy_metric: Matrix,
    anisotropy_rate: Matrix,
) -> sp.Expr:
    """Product-rule split: scale + anisotropy + residual/current content."""
    if not (
        residual_second_moment.shape == second_moment_rate.shape
        == anisotropy_metric.shape == anisotropy_rate.shape
    ):
        raise ValueError("all smooth-rate tensors must have equal shape")
    M=sp.simplify(rho**2*anisotropy_metric)
    Mdot=sp.simplify(2*rho*rho_rate*anisotropy_metric+rho**2*anisotropy_rate)
    full=sp.simplify(sp.trace(second_moment_rate*M+residual_second_moment*Mdot))
    scale=sp.simplify(2*rho_rate/rho*weighted_energy(M,residual_second_moment))
    shape=sp.simplify(rho**2*sp.trace(residual_second_moment*anisotropy_rate))
    content=sp.simplify(sp.trace(second_moment_rate*M))
    return sp.simplify(full-scale-shape-content)


def reverse_material_metric_rate(grad_u: Matrix, line_frame: Matrix) -> Matrix:
    """For Ldot=-A L, Mdot=-L^T(A^T+A)L."""
    if grad_u.shape != line_frame.shape or grad_u.rows != grad_u.cols:
        raise ValueError("grad_u/line_frame must be equal square matrices")
    return sp.simplify(-line_frame.T*(grad_u.T+grad_u)*line_frame)


def reverse_material_weighted_energy_rate_residual(
    grad_u: Matrix,
    line_frame: Matrix,
    residual_second_moment: Matrix,
    codeforming_noise: Matrix,
    nu: sp.Expr,
) -> sp.Expr:
    """Metric strain work plus q.v. content equals physical residual-energy drift."""
    M=primal_line_metric(line_frame)
    Mdot=reverse_material_metric_rate(grad_u,line_frame)
    Qdot=sp.simplify(2*nu*codeforming_noise*codeforming_noise.T)
    lhs=sp.simplify(sp.trace(Qdot*M+residual_second_moment*Mdot))
    S=sp.simplify((grad_u+grad_u.T)/2)
    physical_Q=sp.simplify(line_frame*residual_second_moment*line_frame.T)
    strain=sp.simplify(-2*sp.trace(S*physical_Q))
    qv=sp.simplify(2*nu*sp.trace(codeforming_noise*codeforming_noise.T*M))
    return sp.simplify(lhs-strain-qv)


def homogeneous_isotropic_refinement_residual(
    metric: Matrix,
    second_moment: Matrix,
    scale_factor: sp.Expr,
    degree: int,
) -> sp.Expr:
    """M+=lambda^2 M, Q+=lambda^(2p-4)Q => E+=lambda^(2p-2)E."""
    if degree < 2:
        raise ValueError("nonaffine degree must be at least two")
    Mplus=sp.simplify(scale_factor**2*metric)
    Qplus=sp.simplify(scale_factor**(2*degree-4)*second_moment)
    return sp.simplify(
        weighted_energy(Mplus,Qplus)
        - scale_factor**(2*degree-2)*weighted_energy(metric,second_moment)
    )


def quadratic_long_support_calibration(
    anchor_y: sp.Symbol,
    time: sp.Expr,
    nu: sp.Expr,
    rho: sp.Expr,
) -> dict[str,sp.Expr | Matrix]:
    """Exact quadratic NS with L=diag(1,rho,rho): residual shrinks but support does not."""
    U=quadratic_heat_shear(anchor_y,time,nu)
    eps=asymmetric_rectangle_shear_error_from_velocity(U,anchor_y,sp.Integer(1),rho)
    L=sp.diag(1,rho,rho)
    J=sp.det(L)
    chi_z=sp.simplify(eps/J)
    chi=sp.Matrix([0,0,chi_z])
    r=sp.simplify(L*chi)
    energy=sp.simplify(r.dot(r))
    return {
        "line_frame":L,
        "epsilon_z":sp.simplify(eps),
        "chi":chi,
        "physical_residual":r,
        "physical_energy":energy,
        "long_x_line_squared":sp.Integer(1),
    }
