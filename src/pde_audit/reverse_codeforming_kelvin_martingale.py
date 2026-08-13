"""Reverse-age co-deforming martingale core of finite Kelvin residual dynamics.

On the literal incompressible reverse-age state let the local line frame satisfy

    Ldot = -A L,      tr A = 0,

and let H=cof(L)=J L^-T, J=det L (constant under incompressible material motion).
For the orientation-complete actual circulation vector K define

    eta   = L^-1 omega,
    kappa = K / J,
    chi   = L^-1 r = kappa-eta = epsilon/J,

where epsilon=K-H^T omega and r=H^-T epsilon.

Because K and H^T omega are driftless reverse-age Kelvin martingales, eta, chi and
kappa are all driftless in the co-deforming frame.  All affine strain is therefore
coordinate work in the pushforward chi -> r=L chi.  The joint eta/chi second-moment
law is one full Gram matrix of anchor noise responses, with mandatory signed cross
blocks.

This is a same-clock full-state theorem.  It is not the future-remaining covariance
bank and does not establish reduced covariance closure or regularity.
"""
from __future__ import annotations

import sympy as sp

from .codeforming_surface_moment_tower import cofactor_map

Matrix = sp.MatrixBase


def line_frame_volume_rate(grad_u_anchor: Matrix, line_frame: Matrix) -> sp.Expr:
    """d det(L)/ds for Ldot=-A L."""
    if grad_u_anchor.shape != line_frame.shape or line_frame.rows != line_frame.cols:
        raise ValueError("gradient and line frame must be equal square matrices")
    Ldot = sp.simplify(-grad_u_anchor * line_frame)
    return sp.simplify(sp.det(line_frame) * sp.trace(line_frame.inv() * Ldot))


def incompressible_volume_rate_residual(grad_u_anchor: Matrix, line_frame: Matrix) -> sp.Expr:
    """Residual Jdot + tr(A)J = 0; vanishes with tr(A)=0."""
    J = sp.det(line_frame)
    return sp.simplify(line_frame_volume_rate(grad_u_anchor, line_frame) + sp.trace(grad_u_anchor) * J)


def inverse_line_frame_rate(grad_u_anchor: Matrix, line_frame: Matrix) -> Matrix:
    """d(L^-1)/ds=L^-1 A for Ldot=-A L."""
    Linv = line_frame.inv()
    Ldot = sp.simplify(-grad_u_anchor * line_frame)
    return sp.simplify(-Linv * Ldot * Linv)


def reverse_codeforming_vorticity_drift_residual(
    grad_u_anchor: Matrix,
    line_frame: Matrix,
    local_vorticity: Matrix,
) -> Matrix:
    """Residual d(L^-1 omega)_FV=0 for domega_FV=-A omega."""
    if local_vorticity.shape != (line_frame.rows, 1):
        raise ValueError("vorticity dimension mismatch")
    Linv = line_frame.inv()
    return sp.simplify(
        inverse_line_frame_rate(grad_u_anchor, line_frame) * local_vorticity
        + Linv * (-grad_u_anchor * local_vorticity)
    )


def reverse_codeforming_vorticity_noise(line_frame: Matrix, grad_omega: Matrix) -> Matrix:
    """G~=L^-1 grad(omega), the reverse-age co-deforming local noise matrix."""
    if grad_omega.shape != line_frame.shape or line_frame.rows != line_frame.cols:
        raise ValueError("gradient and line frame must have equal square shape")
    return sp.simplify(line_frame.inv() * grad_omega)


def orientation_error_to_codeforming_residual_residual(
    line_frame: Matrix,
    orientation_error: Matrix,
) -> Matrix:
    """Residual L^-1 H^-T epsilon - epsilon/det(L), H=cof(L)."""
    if orientation_error.shape != (line_frame.rows, 1):
        raise ValueError("orientation error dimension mismatch")
    H = cofactor_map(line_frame)
    lhs = sp.simplify(line_frame.inv() * H.inv().T * orientation_error)
    rhs = sp.simplify(orientation_error / sp.det(line_frame))
    return sp.simplify(lhs - rhs)


def normalized_circulation_local_residual_identity_residual(
    line_frame: Matrix,
    circulation: Matrix,
    local_vorticity: Matrix,
    orientation_error: Matrix,
) -> Matrix:
    """Residual epsilon/J - [K/J-L^-1 omega], assuming epsilon=K-H^T omega."""
    if not (
        circulation.shape == local_vorticity.shape == orientation_error.shape
        == (line_frame.rows, 1)
    ):
        raise ValueError("circulation, vorticity and error dimensions must match frame")
    J = sp.det(line_frame)
    eta = sp.simplify(line_frame.inv() * local_vorticity)
    return sp.simplify(orientation_error / J - (circulation / J - eta))


def reverse_codeforming_residual_noise(
    orientation_error_noise: Matrix,
    line_frame: Matrix,
) -> Matrix:
    """Q_chi=Q_epsilon/J for incompressible material J=det L constant."""
    if orientation_error_noise.rows != line_frame.rows or line_frame.rows != line_frame.cols:
        raise ValueError("error-noise rows must match square frame")
    return sp.simplify(orientation_error_noise / sp.det(line_frame))


def reverse_codeforming_circulation_noise(
    actual_kelvin_noise: Matrix,
    line_frame: Matrix,
) -> Matrix:
    """A~=A_K/J for kappa=K/J with constant incompressible J."""
    if actual_kelvin_noise.rows != line_frame.rows:
        raise ValueError("Kelvin-noise rows must match frame")
    return sp.simplify(actual_kelvin_noise / sp.det(line_frame))


def reverse_codeforming_noise_decomposition_residual(
    actual_kelvin_noise: Matrix,
    orientation_error_noise: Matrix,
    line_frame: Matrix,
    grad_omega: Matrix,
) -> Matrix:
    """Residual A~/J? Precisely A_K/J - [L^-1 grad omega + Q_epsilon/J]."""
    full = reverse_codeforming_circulation_noise(actual_kelvin_noise, line_frame)
    local = reverse_codeforming_vorticity_noise(line_frame, grad_omega)
    residual = reverse_codeforming_residual_noise(orientation_error_noise, line_frame)
    return sp.simplify(full - local - residual)


def qv_tensor(noise_matrix: Matrix, nu: sp.Expr) -> Matrix:
    """2nu Q Q^T."""
    return sp.simplify(2 * nu * noise_matrix * noise_matrix.T)


def cross_qv_tensor(left_noise: Matrix, right_noise: Matrix, nu: sp.Expr) -> Matrix:
    """2nu Q_left Q_right^T, generally signed/non-symmetric."""
    if left_noise.cols != right_noise.cols:
        raise ValueError("Brownian dimensions must match")
    return sp.simplify(2 * nu * left_noise * right_noise.T)


def joint_local_residual_noise(local_noise: Matrix, residual_noise: Matrix) -> Matrix:
    """Vertical stack [G~;Q_chi] carrying the complete local/residual response."""
    if local_noise.cols != residual_noise.cols:
        raise ValueError("Brownian dimensions must match")
    return local_noise.col_join(residual_noise)


def joint_local_residual_qv(local_noise: Matrix, residual_noise: Matrix, nu: sp.Expr) -> Matrix:
    """One full Gram tensor 2nu [G;Q][G;Q]^T."""
    joint = joint_local_residual_noise(local_noise, residual_noise)
    return qv_tensor(joint, nu)


def joint_qv_block_residual(local_noise: Matrix, residual_noise: Matrix, nu: sp.Expr) -> Matrix:
    """Residual of full Gram against local/residual/cross block assembly."""
    n = local_noise.rows
    m = residual_noise.rows
    local = qv_tensor(local_noise, nu)
    residual = qv_tensor(residual_noise, nu)
    cross = cross_qv_tensor(local_noise, residual_noise, nu)
    assembled = local.row_join(cross).col_join(cross.T.row_join(residual))
    return sp.simplify(joint_local_residual_qv(local_noise, residual_noise, nu) - assembled)


def full_circulation_qv_decomposition_residual(
    local_noise: Matrix,
    residual_noise: Matrix,
    nu: sp.Expr,
) -> Matrix:
    """Gamma_kappa-[Gamma_eta+Gamma_chi+Gamma_eta,chi+transpose]."""
    full_noise = sp.simplify(local_noise + residual_noise)
    return sp.simplify(
        qv_tensor(full_noise, nu)
        - qv_tensor(local_noise, nu)
        - qv_tensor(residual_noise, nu)
        - cross_qv_tensor(local_noise, residual_noise, nu)
        - cross_qv_tensor(residual_noise, local_noise, nu)
    )


def martingale_dyad_drift(noise_matrix: Matrix, nu: sp.Expr) -> Matrix:
    """Drift of YY^T for driftless dY=sqrt(2nu)Q dW."""
    return qv_tensor(noise_matrix, nu)


def martingale_cross_dyad_drift(left_noise: Matrix, right_noise: Matrix, nu: sp.Expr) -> Matrix:
    """Drift of Y Z^T for two driftless same-anchor martingales."""
    return cross_qv_tensor(left_noise, right_noise, nu)


def codeforming_residual_energy_drift(residual_noise: Matrix, nu: sp.Expr) -> sp.Expr:
    """Drift of |chi|^2/2: nu ||Q_chi||_F^2, with no strain term."""
    return sp.simplify(nu * sum(e**2 for e in residual_noise))


def physical_pushforward_energy_drift_residual(
    grad_u_anchor: Matrix,
    line_frame: Matrix,
    codeforming_residual: Matrix,
    codeforming_noise: Matrix,
    nu: sp.Expr,
) -> sp.Expr:
    """Residual recovering physical -r.S.r+nu||L Qchi||^2 from r=L chi."""
    if codeforming_residual.shape != (line_frame.rows, 1):
        raise ValueError("residual dimension mismatch")
    r = sp.simplify(line_frame * codeforming_residual)
    S = sp.simplify((grad_u_anchor + grad_u_anchor.T) / 2)
    physical = sp.simplify(-(r.T * S * r)[0] + nu * sum(e**2 for e in line_frame * codeforming_noise))
    Ldot = sp.simplify(-grad_u_anchor * line_frame)
    metric_work = sp.simplify((codeforming_residual.T * line_frame.T * Ldot * codeforming_residual)[0])
    qv_work = sp.simplify(nu * sum(e**2 for e in line_frame * codeforming_noise))
    return sp.simplify(metric_work + qv_work - physical)


def constant_mean_bias_rate() -> sp.Integer:
    """Drift rate of E[chi] for a driftless reverse-age co-deforming martingale."""
    return sp.Integer(0)


def second_moment_minus_covariance_source_residual(
    noise_matrix: Matrix,
    nu: sp.Expr,
) -> Matrix:
    """With constant mean, second-moment and centered-covariance rates both equal Gamma."""
    gamma = qv_tensor(noise_matrix, nu)
    return sp.simplify(martingale_dyad_drift(noise_matrix, nu) - gamma)


def reverse_age_vs_backward_operator_source_residual(
    reverse_age_dyad_source: Matrix,
    backward_physical_time_source: Matrix,
) -> Matrix:
    """Residual source_sigma + source_backward_time=0 for sigma=t-s orientation."""
    if reverse_age_dyad_source.shape != backward_physical_time_source.shape:
        raise ValueError("source shapes must match")
    return sp.simplify(reverse_age_dyad_source + backward_physical_time_source)
