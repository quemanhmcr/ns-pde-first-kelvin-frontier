"""Exact physical typing of the metric-whitened finite Kelvin remainder.

For a coherent line frame L let H=cof(L).  The codeforming nonaffinity one-form
beta=(L^T L)N satisfies

    curl_xi beta = H^T [omega(X+L xi)-omega(X)].

Thus H^{-T} is not an artificial normalization at the pointwise density level: it
exactly reconstructs the physical vorticity defect.  At finite scale, applying the
same map to the vector of three face circulation residuals produces a reconstructed
finite-face physical residual; it is generally not a pointwise field value because
the three components sample three different surfaces.

For random payoffs X_H=H^T zeta+epsilon, whitening gives zeta+r with
r=H^{-T}epsilon.  Covariance therefore contains residual and mandatory local/residual
cross blocks.  This module keeps that exact algebra before any L2 estimate.
"""
from __future__ import annotations

from collections.abc import Sequence

import sympy as sp

from .codeforming_surface_moment_tower import (
    codeforming_nonaffinity_field,
    codeforming_nonaffinity_one_form,
    cofactor_map,
    curl3,
)
from .kelvin_packet_locality import metric_from_area_frame

Matrix = sp.MatrixBase


def pointwise_orientation_density(field_defect: Matrix, area_frame: Matrix) -> sp.Matrix:
    """g=H^T delta_zeta, the three orientation flux-density coefficients."""
    if area_frame.rows != area_frame.cols or field_defect.shape != (area_frame.rows, 1):
        raise ValueError("field defect and area frame dimensions must match")
    return sp.simplify(area_frame.T * field_defect)


def whitened_face_reconstruction(face_residual: Matrix, area_frame: Matrix) -> sp.Matrix:
    """r_H=H^{-T} epsilon_H, a reconstructed physical residual vector."""
    if area_frame.rows != area_frame.cols or face_residual.shape != (area_frame.rows, 1):
        raise ValueError("face residual and area frame dimensions must match")
    return sp.simplify(area_frame.inv().T * face_residual)


def pointwise_whitening_residual(field_defect: Matrix, area_frame: Matrix) -> sp.Matrix:
    """Residual H^{-T}(H^T delta_zeta)-delta_zeta."""
    density = pointwise_orientation_density(field_defect, area_frame)
    return sp.simplify(whitened_face_reconstruction(density, area_frame) - field_defect)


def codeforming_beta_whitened_curl_residual(
    beta: Matrix,
    codeforming_coords: Sequence[sp.Symbol],
    area_frame: Matrix,
    physical_field_defect: Matrix,
) -> sp.Matrix:
    """Residual H^{-T} curl_xi beta - delta_omega."""
    if beta.shape != physical_field_defect.shape:
        raise ValueError("beta and physical defect dimensions must match")
    return sp.simplify(
        area_frame.inv().T * curl3(beta, codeforming_coords) - physical_field_defect
    )


def whitened_energy_residual(face_residual: Matrix, area_frame: Matrix) -> sp.Expr:
    """Residual |H^-T eps|^2-eps^T(H^T H)^-1 eps."""
    reconstructed = whitened_face_reconstruction(face_residual, area_frame)
    metric = metric_from_area_frame(area_frame)
    return sp.simplify(
        reconstructed.dot(reconstructed)
        - (face_residual.T * metric * face_residual)[0]
    )


def whitened_covariance(face_covariance: Matrix, area_frame: Matrix) -> sp.Matrix:
    """Cov(H^-T epsilon)=H^-T Cov(epsilon) H^-1 for fixed H."""
    if face_covariance.shape != area_frame.shape or area_frame.rows != area_frame.cols:
        raise ValueError("covariance and area frame must have equal square shape")
    return sp.simplify(area_frame.inv().T * face_covariance * area_frame.inv())


def whitened_covariance_trace_residual(face_covariance: Matrix, area_frame: Matrix) -> sp.Expr:
    """Residual tr(Cov(reconstruction))-tr(C_eps (H^T H)^-1)."""
    return sp.simplify(
        sp.trace(whitened_covariance(face_covariance, area_frame))
        - sp.trace(face_covariance * metric_from_area_frame(area_frame))
    )


def passive_orientation_reparameterization_residual(
    face_residual: Matrix,
    area_frame: Matrix,
    orientation_map: Matrix,
) -> sp.Matrix:
    """Residual for H+=H R, eps+=R^T eps: physical reconstruction is invariant."""
    if area_frame.shape != orientation_map.shape or face_residual.shape != (area_frame.rows, 1):
        raise ValueError("orientation dimensions must match")
    before = whitened_face_reconstruction(face_residual, area_frame)
    after = whitened_face_reconstruction(
        sp.simplify(orientation_map.T * face_residual),
        sp.simplify(area_frame * orientation_map),
    )
    return sp.simplify(after - before)


def face_error_qv_tensor(noise_coefficients: Sequence[Matrix], nu: sp.Expr) -> sp.Matrix:
    """Gamma_eps=2nu sum_mu q_mu q_mu^T for an orientation-complete error vector."""
    if not noise_coefficients:
        return sp.zeros(0)
    n = noise_coefficients[0].rows
    if any(q.shape != (n, 1) for q in noise_coefficients):
        raise ValueError("all noise coefficients must be equal column vectors")
    return sp.simplify(
        2 * nu * sum((q * q.T for q in noise_coefficients), sp.zeros(n))
    )


def whitened_face_error_qv_residual(
    noise_coefficients: Sequence[Matrix],
    area_frame: Matrix,
    nu: sp.Expr,
) -> sp.Matrix:
    """Residual H^-T Gamma_eps H^-1 - 2nu sum r_mu r_mu^T."""
    gamma = face_error_qv_tensor(noise_coefficients, nu)
    if gamma.shape != area_frame.shape:
        raise ValueError("noise dimension and area frame must match")
    lhs = whitened_covariance(gamma, area_frame)
    reconstructed = [whitened_face_reconstruction(q, area_frame) for q in noise_coefficients]
    rhs = sp.simplify(
        2 * nu * sum((q * q.T for q in reconstructed), sp.zeros(area_frame.rows))
    )
    return sp.simplify(lhs - rhs)


def whitened_full_covariance_from_blocks(
    local_covariance: Matrix,
    residual_covariance: Matrix,
    local_residual_cross: Matrix,
) -> sp.Matrix:
    """Cov(zeta+r)=C_zeta+C_r+C_zr+C_zr^T; cross blocks are mandatory."""
    if not (
        local_covariance.shape == residual_covariance.shape == local_residual_cross.shape
        and local_covariance.rows == local_covariance.cols
    ):
        raise ValueError("all covariance blocks must have equal square shape")
    return sp.simplify(
        local_covariance
        + residual_covariance
        + local_residual_cross
        + local_residual_cross.T
    )


def equal_two_state_covariance(v1: Matrix, v2: Matrix) -> sp.Matrix:
    """Exact covariance of a two-state equal-probability vector: (v1-v2)(...)^T/4."""
    if v1.shape != v2.shape or v1.cols != 1:
        raise ValueError("two-state values must be equal column vectors")
    d = sp.simplify(v1 - v2)
    return sp.simplify(d * d.T / 4)


def equal_two_state_cross_covariance(
    x1: Matrix,
    x2: Matrix,
    y1: Matrix,
    y2: Matrix,
) -> sp.Matrix:
    """Exact Cov(X,Y) for equal two-state coupled samples."""
    if x1.shape != x2.shape or y1.shape != y2.shape or x1.cols != 1 or y1.cols != 1:
        raise ValueError("two-state values must be column vectors")
    return sp.simplify((x1 - x2) * (y1 - y2).T / 4)


def homogeneous_beta_scale_shape_residual(
    physical_homogeneous_residual: Matrix,
    degree: int,
    physical_relative_coords: Sequence[sp.Symbol],
    scale: sp.Expr,
    unit_det_shape: Matrix,
    codeforming_coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    """Residual beta_{rho S}^{(p)}-rho^(p+1) S^T U_p(S xi)."""
    if degree < 2:
        raise ValueError("nonaffine homogeneous degree must be at least two")
    n = len(physical_relative_coords)
    if unit_det_shape.shape != (n, n):
        raise ValueError("shape dimension mismatch")
    L = sp.simplify(scale * unit_det_shape)
    N = codeforming_nonaffinity_field(
        physical_homogeneous_residual,
        sp.zeros(n),
        physical_relative_coords,
        L,
        codeforming_coords,
    )
    beta = codeforming_nonaffinity_one_form(N, L)
    xi = sp.Matrix(codeforming_coords)
    substitution = {
        physical_relative_coords[i]: (unit_det_shape * xi)[i]
        for i in range(n)
    }
    expected = sp.simplify(
        scale ** (degree + 1)
        * unit_det_shape.T
        * physical_homogeneous_residual.subs(substitution, simultaneous=True)
    )
    return sp.simplify(beta - expected)


def coordinate_face_flux_vector(
    codeforming_flux_density: Matrix,
    codeforming_coords: Sequence[sp.Symbol],
    half_widths: Sequence[sp.Expr],
) -> sp.Matrix:
    """Integrate component i over the centered coordinate face xi_i=0.

    The density components are already reference-orientation flux coefficients (for
    example curl_xi beta=H^T delta omega).  Each component is therefore integrated
    over a different coordinate face.  The resulting vector is a finite-face object,
    not the value of one pointwise vector field.
    """
    if codeforming_flux_density.shape != (3, 1) or len(codeforming_coords) != 3 or len(half_widths) != 3:
        raise ValueError("coordinate face flux vector is three-dimensional")
    out = []
    for i in range(3):
        expr = sp.simplify(codeforming_flux_density[i].subs(codeforming_coords[i], 0))
        for j in range(3):
            if j == i:
                continue
            expr = sp.integrate(
                expr,
                (codeforming_coords[j], -half_widths[j], half_widths[j]),
            )
        out.append(sp.simplify(expr))
    return sp.Matrix(out)
