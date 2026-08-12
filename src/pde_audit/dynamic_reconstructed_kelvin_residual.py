"""Exact reverse-age dynamics of the orientation-reconstructed finite Kelvin residual.

Let K be the vector of actual closed-current circulations for an orientation-complete
packet and let H be the *local reverse cofactor frame*, Hdot=A(X)^T H.  Define

    Phi = H^T omega(X),
    epsilon_lin = K-Phi,
    W = H^{-T} K,
    r = H^{-T} epsilon_lin = W-omega.

Closed-current Kelvin drift and the local Nanson/vorticity stretching drift both
vanish exactly in reverse age.  Hence epsilon_lin is a pure anchor martingale.  The
reconstructed vectors W and r acquire the physical line connection -A solely from
H^{-T}dot=-A H^{-T}.

This is distinct from the earlier actual-area error K-omega.h_R.  That error has the
finite-variation drift -omega.R_A; adding the exact geometry mismatch
omega.(h_R-h) contributes +omega.R_A and transfers the drift away in epsilon_lin.
No term is discarded.

No future-clock, ancestry, restart, continuation, or regularity identification is
made here.
"""
from __future__ import annotations

from collections.abc import Sequence

import sympy as sp

Matrix = sp.MatrixBase


def reverse_local_area_frame_rate(grad_u_anchor: Matrix, area_frame: Matrix) -> Matrix:
    """Hdot=A^T H for the actual local reverse cofactor frame."""
    if grad_u_anchor.rows != grad_u_anchor.cols or area_frame.shape != grad_u_anchor.shape:
        raise ValueError("grad_u_anchor and area_frame must be equal square matrices")
    return sp.simplify(grad_u_anchor.T * area_frame)


def inverse_transpose_frame_rate(grad_u_anchor: Matrix, area_frame: Matrix) -> Matrix:
    """d(H^-T)/ds=-A H^-T, the reconstructed physical-vector connection."""
    Hdot = reverse_local_area_frame_rate(grad_u_anchor, area_frame)
    Q = area_frame.inv().T
    # Written by product rule rather than hard-coding the result.
    return sp.simplify(-Q * Hdot.T * Q)


def inverse_transpose_connection_residual(grad_u_anchor: Matrix, area_frame: Matrix) -> Matrix:
    """Residual d(H^-T)/ds + A H^-T."""
    Q = area_frame.inv().T
    return sp.simplify(inverse_transpose_frame_rate(grad_u_anchor, area_frame) + grad_u_anchor * Q)


def local_vorticity_flux_noise_matrix(area_frame: Matrix, grad_omega: Matrix) -> Matrix:
    """Columns are H^T partial_mu omega, the local reverse-age flux noise coefficients."""
    if area_frame.rows != area_frame.cols or grad_omega.shape != area_frame.shape:
        raise ValueError("area_frame and grad_omega must have equal square shape")
    return sp.simplify(area_frame.T * grad_omega)


def local_vorticity_flux_drift_residual(
    grad_u_anchor: Matrix,
    area_frame: Matrix,
    local_vorticity: Matrix,
) -> Matrix:
    """Residual of drift d(H^T omega)=0 using Hdot=A^T H and domega=-A omega ds."""
    if local_vorticity.shape != (grad_u_anchor.rows, 1):
        raise ValueError("vorticity dimension mismatch")
    Hdot = reverse_local_area_frame_rate(grad_u_anchor, area_frame)
    return sp.simplify(Hdot.T * local_vorticity + area_frame.T * (-grad_u_anchor * local_vorticity))


def local_frame_kelvin_error_noise(
    actual_kelvin_noise_matrix: Matrix,
    area_frame: Matrix,
    grad_omega: Matrix,
) -> Matrix:
    """Q_K=a_finite-H^T grad omega for epsilon_lin=K-H^T omega."""
    local = local_vorticity_flux_noise_matrix(area_frame, grad_omega)
    if actual_kelvin_noise_matrix.shape != local.shape:
        raise ValueError("actual and local Kelvin noise matrices must have equal shape")
    return sp.simplify(actual_kelvin_noise_matrix - local)


def reconstructed_kelvin_noise(noise_matrix: Matrix, area_frame: Matrix) -> Matrix:
    """H^-T times an orientation-coordinate noise matrix."""
    if noise_matrix.rows != area_frame.rows or area_frame.rows != area_frame.cols:
        raise ValueError("noise rows must match square area frame")
    return sp.simplify(area_frame.inv().T * noise_matrix)


def reconstructed_payoff_drift(grad_u_anchor: Matrix, reconstructed_payoff: Matrix) -> Matrix:
    """Pathwise drift of W=H^-T K: -A W."""
    if reconstructed_payoff.shape != (grad_u_anchor.rows, 1):
        raise ValueError("payoff dimension mismatch")
    return sp.simplify(-grad_u_anchor * reconstructed_payoff)


def reconstructed_residual_drift(grad_u_anchor: Matrix, reconstructed_residual: Matrix) -> Matrix:
    """Pathwise drift of r=W-omega: -A r."""
    return reconstructed_payoff_drift(grad_u_anchor, reconstructed_residual)


def actual_area_mismatch_rate(
    grad_u_anchor: Matrix,
    actual_area: Matrix,
    local_area: Matrix,
    shape_residual: Matrix,
) -> Matrix:
    """delta hdot=A^T delta h+R_A, where delta h=h_R-h."""
    if actual_area.shape != local_area.shape or actual_area.shape != shape_residual.shape:
        raise ValueError("area and shape-residual dimensions must match")
    if actual_area.shape != (grad_u_anchor.rows, 1):
        raise ValueError("area dimension mismatch")
    delta = sp.simplify(actual_area - local_area)
    return sp.simplify(grad_u_anchor.T * delta + shape_residual)


def geometry_mismatch_flux_drift(
    grad_u_anchor: Matrix,
    local_vorticity: Matrix,
    actual_area: Matrix,
    local_area: Matrix,
    shape_residual: Matrix,
) -> sp.Expr:
    """Drift of omega.(h_R-h), exactly +omega.R_A after stretching cancellation."""
    delta = sp.simplify(actual_area - local_area)
    delta_dot = actual_area_mismatch_rate(
        grad_u_anchor, actual_area, local_area, shape_residual
    )
    omega_dot = sp.simplify(-grad_u_anchor * local_vorticity)
    return sp.simplify((omega_dot.T * delta)[0] + (local_vorticity.T * delta_dot)[0])


def shape_drift_transfer_residual(
    grad_u_anchor: Matrix,
    local_vorticity: Matrix,
    actual_area: Matrix,
    local_area: Matrix,
    shape_residual: Matrix,
) -> sp.Expr:
    """Residual (-omega.R_A)+d[omega.(h_R-h)]/ds=0."""
    actual_area_error_drift = sp.simplify(-(local_vorticity.T * shape_residual)[0])
    mismatch_drift = geometry_mismatch_flux_drift(
        grad_u_anchor, local_vorticity, actual_area, local_area, shape_residual
    )
    return sp.simplify(actual_area_error_drift + mismatch_drift)


def geometry_mismatch_noise_matrix(
    grad_omega: Matrix,
    actual_area: Matrix,
    local_area: Matrix,
) -> sp.Matrix:
    """Rows/orientation? Return noise vector over Brownian directions: delta h^T grad omega."""
    if actual_area.shape != local_area.shape or grad_omega.rows != actual_area.rows:
        raise ValueError("geometry/gradient dimensions do not match")
    delta = sp.simplify(actual_area - local_area)
    return sp.simplify(delta.T * grad_omega)


def local_error_noise_transfer_residual(
    actual_kelvin_noise_row: Matrix,
    grad_omega: Matrix,
    actual_area: Matrix,
    local_area: Matrix,
) -> Matrix:
    """Scalar-face noise transfer: q_actualarea + q_geometry = q_localframe.

    Each argument represents one physical finite surface/current.  Rows index Brownian
    directions.  This is the noise counterpart of the deterministic shape-drift transfer.
    """
    if actual_kelvin_noise_row.rows != 1:
        raise ValueError("actual Kelvin noise for one face must be a row vector")
    q_actual = sp.simplify(actual_kelvin_noise_row - actual_area.T * grad_omega)
    q_geom = geometry_mismatch_noise_matrix(grad_omega, actual_area, local_area)
    q_local = sp.simplify(actual_kelvin_noise_row - local_area.T * grad_omega)
    return sp.simplify(q_actual + q_geom - q_local)


def noise_qv_tensor(noise_matrix: Matrix, nu: sp.Expr) -> Matrix:
    """2nu Q Q^T when columns are Brownian noise directions."""
    return sp.simplify(2 * nu * noise_matrix * noise_matrix.T)


def reconstructed_residual_qv(
    local_error_noise_matrix: Matrix,
    area_frame: Matrix,
    nu: sp.Expr,
) -> Matrix:
    """Gamma_r=2nu Qhat Qhat^T, Qhat=H^-T Q_K."""
    qhat = reconstructed_kelvin_noise(local_error_noise_matrix, area_frame)
    return noise_qv_tensor(qhat, nu)


def reconstructed_residual_dyad_drift(
    grad_u_anchor: Matrix,
    residual: Matrix,
    reconstructed_noise: Matrix,
    nu: sp.Expr,
) -> Matrix:
    """Drift of rr^T: -A rr^T-rr^T A^T+2nu Qhat Qhat^T."""
    R = sp.simplify(residual * residual.T)
    return sp.simplify(
        -grad_u_anchor * R
        - R * grad_u_anchor.T
        + noise_qv_tensor(reconstructed_noise, nu)
    )


def reconstructed_residual_energy_drift(
    grad_u_anchor: Matrix,
    residual: Matrix,
    reconstructed_noise: Matrix,
    nu: sp.Expr,
) -> sp.Expr:
    """Drift of |r|^2/2: -r.S.r + nu ||Qhat||_F^2."""
    S = sp.simplify((grad_u_anchor + grad_u_anchor.T) / 2)
    qsq = sp.simplify(sum(e**2 for e in reconstructed_noise))
    return sp.simplify(-(residual.T * S * residual)[0] + nu * qsq)


def local_residual_cross_qv(
    grad_omega: Matrix,
    reconstructed_residual_noise: Matrix,
    nu: sp.Expr,
) -> Matrix:
    """d[omega,r]/ds=2nu (grad omega) Qhat^T."""
    if grad_omega.cols != reconstructed_residual_noise.cols:
        raise ValueError("local/residual Brownian dimensions must match")
    return sp.simplify(2 * nu * grad_omega * reconstructed_residual_noise.T)


def local_residual_cross_dyad_drift(
    grad_u_anchor: Matrix,
    local_vorticity: Matrix,
    residual: Matrix,
    grad_omega: Matrix,
    reconstructed_residual_noise: Matrix,
    nu: sp.Expr,
) -> Matrix:
    """Drift of omega r^T with mandatory cross q.v. source."""
    M = sp.simplify(local_vorticity * residual.T)
    return sp.simplify(
        -grad_u_anchor * M
        - M * grad_u_anchor.T
        + local_residual_cross_qv(grad_omega, reconstructed_residual_noise, nu)
    )


def full_reconstructed_noise_decomposition_residual(
    actual_kelvin_noise_matrix: Matrix,
    area_frame: Matrix,
    grad_omega: Matrix,
) -> Matrix:
    """Residual H^-T a_finite - [grad omega + H^-T(a_finite-H^T grad omega)]."""
    full = reconstructed_kelvin_noise(actual_kelvin_noise_matrix, area_frame)
    qerr = local_frame_kelvin_error_noise(actual_kelvin_noise_matrix, area_frame, grad_omega)
    qhat = reconstructed_kelvin_noise(qerr, area_frame)
    return sp.simplify(full - grad_omega - qhat)


def connected_vector_dyad_drift(
    grad_u_anchor: Matrix,
    vector: Matrix,
    noise_matrix: Matrix,
    nu: sp.Expr,
) -> Matrix:
    """Drift of vv^T for dv=-A v ds+sqrt(2nu)Q dW."""
    if vector.shape != (grad_u_anchor.rows, 1) or noise_matrix.rows != vector.rows:
        raise ValueError("vector/noise dimensions must match connection")
    V = sp.simplify(vector * vector.T)
    return sp.simplify(
        -grad_u_anchor * V - V * grad_u_anchor.T + noise_qv_tensor(noise_matrix, nu)
    )


def full_dyad_block_decomposition_residual(
    grad_u_anchor: Matrix,
    local_vorticity: Matrix,
    residual: Matrix,
    grad_omega: Matrix,
    reconstructed_residual_noise: Matrix,
    nu: sp.Expr,
) -> Matrix:
    """Dynamic dyad residual for W=omega+r including both cross blocks.

    The full reconstructed noise is grad_omega+Qhat.  The identity is
      drift(WW^T)=drift(omega omega^T)+drift(rr^T)
                  +drift(omega r^T)+transpose.
    """
    W = sp.simplify(local_vorticity + residual)
    full_noise = sp.simplify(grad_omega + reconstructed_residual_noise)
    full = connected_vector_dyad_drift(grad_u_anchor, W, full_noise, nu)
    local = connected_vector_dyad_drift(grad_u_anchor, local_vorticity, grad_omega, nu)
    res = connected_vector_dyad_drift(
        grad_u_anchor, residual, reconstructed_residual_noise, nu
    )
    cross = local_residual_cross_dyad_drift(
        grad_u_anchor, local_vorticity, residual, grad_omega, reconstructed_residual_noise, nu
    )
    return sp.simplify(full - local - res - cross - cross.T)


def full_qv_block_decomposition_residual(
    actual_kelvin_noise_matrix: Matrix,
    area_frame: Matrix,
    grad_omega: Matrix,
    nu: sp.Expr,
) -> Matrix:
    """Gamma_W-[Gamma_omega+Gamma_r+Gamma_or+Gamma_or^T]."""
    full_noise = reconstructed_kelvin_noise(actual_kelvin_noise_matrix, area_frame)
    qerr = local_frame_kelvin_error_noise(actual_kelvin_noise_matrix, area_frame, grad_omega)
    qhat = reconstructed_kelvin_noise(qerr, area_frame)
    gamma_full = noise_qv_tensor(full_noise, nu)
    gamma_local = noise_qv_tensor(grad_omega, nu)
    gamma_r = noise_qv_tensor(qhat, nu)
    gamma_cross = local_residual_cross_qv(grad_omega, qhat, nu)
    return sp.simplify(gamma_full - gamma_local - gamma_r - gamma_cross - gamma_cross.T)
