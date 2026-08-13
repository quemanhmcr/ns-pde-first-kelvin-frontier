"""Exact Kelvin/Nanson support lift of the intrinsic max-enstrophy chamber.

For the exact periodic one-mode heat shear, max-normalized enstrophy is
``g=cos^2(n y)``.  The connected chamber at y=0 with level
``theta=cos^2(alpha)`` is the slab ``|y|<=alpha/n``.  This module places an
orientation-complete coherent packet inside that same chamber and keeps scalar
compatibility, Kelvin current, Nanson support geometry, finite-shape drift and
ancestry flux as distinct physical faces.

The audited no-go is that alpha->0 can collapse the chamber thickness, packet
volume, gauge-correct Kelvin residual, anchor q.v. and finite-shape nonaffinity
while transverse support remains nonzero.  The missing geometry is the tangential
support tensor induced by the intrinsic level-set tangent plane, not a new score.

No first-bad identification, restart, continuation or regularity theorem is made.
"""
from __future__ import annotations

from dataclasses import dataclass
import sympy as sp

from .intrinsic_enstrophy_localization import (
    ancestry_superlevel_flux_faces,
    integer_scaled_one_mode_heat_shear,
    one_mode_intrinsic_localization_calibration,
)
from .kelvin_packet_locality import (
    cofactor_area_frame,
    coherent_three_face_normalized_quadrupoles,
    material_line_frame_rhs,
    two_sided_stretch_action,
)
from .orientation_packet import orientation_qv_matrix

Matrix = sp.MatrixBase


@dataclass(frozen=True)
class IntrinsicChamberPacketState:
    level: sp.Expr
    half_width_y: sp.Expr
    y_span: sp.Expr
    line_frame: Matrix
    area_frame: Matrix
    support_tensor: Matrix
    level_normal: Matrix
    tangential_projector: Matrix
    tangential_support_tensor: Matrix
    face_quadrupoles: tuple[Matrix, Matrix, Matrix]
    quadrupole_sum: Matrix
    circulation: Matrix
    target_vorticity: Matrix
    raw_error: Matrix
    physical_residual: Matrix
    codeforming_residual: Matrix
    target_gradient: Matrix
    residual_noise: Matrix
    full_codeforming_noise: Matrix
    orientation_qv: Matrix
    nanson_line_rate: Matrix
    support_tensor_rate: Matrix
    tangential_support_rate: Matrix
    endpoint_nonaffinity: Matrix
    compatibility_defect: sp.Expr
    uniform_ancestry_flux: sp.Expr


def intrinsic_chamber_level(alpha: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.cos(alpha) ** 2)


def intrinsic_chamber_half_width(alpha: sp.Expr, mode: sp.Expr) -> sp.Expr:
    return sp.simplify(alpha / mode)


def intrinsic_chamber_y_span(alpha: sp.Expr, mode: sp.Expr) -> sp.Expr:
    return sp.simplify(2 * alpha / mode)


def chamber_boundary_level_residual(alpha: sp.Expr, mode: sp.Expr) -> sp.Expr:
    h = intrinsic_chamber_half_width(alpha, mode)
    return sp.simplify(sp.cos(mode * h) ** 2 - intrinsic_chamber_level(alpha))


def centered_chamber_line_frame(
    alpha: sp.Expr, mode: sp.Expr, x_length: sp.Expr, z_length: sp.Expr
) -> Matrix:
    return sp.diag(x_length, intrinsic_chamber_y_span(alpha, mode), z_length)


def centered_one_mode_circulation_z(
    amplitude: sp.Expr,
    mode: sp.Expr,
    alpha: sp.Expr,
    anchor_y: sp.Expr,
    x_length: sp.Expr,
    t: sp.Expr,
    nu: sp.Expr,
) -> sp.Expr:
    decay = sp.exp(-nu * mode**2 * t)
    return sp.simplify(
        -2 * amplitude * mode * decay * x_length
        * sp.cos(mode * anchor_y) * sp.sin(alpha)
    )


def centered_one_mode_physical_residual_z(
    amplitude: sp.Expr, mode: sp.Expr, alpha: sp.Expr, t: sp.Expr, nu: sp.Expr
) -> sp.Expr:
    decay = sp.exp(-nu * mode**2 * t)
    return sp.simplify(amplitude * mode**2 * decay * (1 - sp.sin(alpha) / alpha))


def centered_one_mode_endpoint_nonaffinity(
    amplitude: sp.Expr, mode: sp.Expr, alpha: sp.Expr, t: sp.Expr, nu: sp.Expr
) -> Matrix:
    """U(h)-U(0)-U_y(0)h at h=alpha/n."""
    decay = sp.exp(-nu * mode**2 * t)
    return sp.Matrix([
        sp.simplify(amplitude * mode * decay * (sp.sin(alpha) - alpha)), 0, 0
    ])


def tangential_support_projector(level_normal: Matrix) -> Matrix:
    if level_normal.shape != (3, 1):
        raise ValueError("level normal must be a 3-vector")
    return sp.simplify(sp.eye(3) - level_normal * level_normal.T)


def packet_tangential_support_tensor(line_frame: Matrix, level_normal: Matrix) -> Matrix:
    if line_frame.shape != (3, 3):
        raise ValueError("line frame must be 3x3")
    P = tangential_support_projector(level_normal)
    B = sp.simplify(line_frame * line_frame.T)
    return sp.simplify(P * B * P)


def packet_tangential_support_rate(
    grad_u_anchor: Matrix, support_tensor: Matrix, level_normal: Matrix
) -> Matrix:
    if grad_u_anchor.shape != (3, 3) or support_tensor.shape != (3, 3):
        raise ValueError("grad u and support tensor must be 3x3")
    P = tangential_support_projector(level_normal)
    return sp.simplify(P * two_sided_stretch_action(grad_u_anchor, support_tensor) * P)


def intrinsic_chamber_packet_state(
    amplitude: sp.Expr,
    mode: sp.Expr,
    alpha: sp.Expr,
    x_length: sp.Expr,
    z_length: sp.Expr,
    coords: tuple[sp.Symbol, sp.Symbol, sp.Symbol],
    t: sp.Expr,
    nu: sp.Expr,
) -> IntrinsicChamberPacketState:
    _, y, _ = coords
    theta = intrinsic_chamber_level(alpha)
    h = intrinsic_chamber_half_width(alpha, mode)
    s = sp.simplify(2 * h)
    L = centered_chamber_line_frame(alpha, mode, x_length, z_length)
    H = cofactor_area_frame(L)
    B = sp.simplify(L * L.T)
    normal = sp.Matrix([0, 1, 0])
    P = tangential_support_projector(normal)
    Bt = sp.simplify(P * B * P)
    face_q = tuple(coherent_three_face_normalized_quadrupoles(L))
    qsum = sp.simplify(sum(face_q, sp.zeros(3)))
    decay = sp.exp(-nu * mode**2 * t)
    q0 = sp.simplify(-amplitude * mode**2 * decay)
    K = sp.Matrix([0, 0, centered_one_mode_circulation_z(
        amplitude, mode, alpha, 0, x_length, t, nu
    )])
    omega = sp.Matrix([0, 0, q0])
    eps = sp.simplify(K - H.T * omega)
    r = sp.simplify(H.inv().T * eps)
    J = sp.simplify(sp.det(L))
    chi = sp.simplify(eps / J)
    aa = sp.symbols("a_intrinsic_packet", real=True)
    q_general = sp.simplify(-amplitude * mode**2 * decay * sp.cos(mode * aa))
    qy_general = sp.diff(q_general, aa)
    grad_omega = sp.zeros(3)
    grad_omega[2, 1] = sp.simplify(qy_general.subs(aa, 0))
    local_noise = sp.simplify(L.inv() * grad_omega)
    K_general = sp.Matrix([0, 0, centered_one_mode_circulation_z(
        amplitude, mode, alpha, aa, x_length, t, nu
    )])
    omega_general = sp.Matrix([0, 0, q_general])
    eps_general = sp.simplify(K_general - H.T * omega_general)
    chi_general = sp.simplify(eps_general / J)
    residual_coeff = sp.simplify(sp.diff(chi_general[2], aa).subs(aa, 0))
    residual_noise = sp.Matrix([[0, 0, 0], [0, 0, 0], [0, residual_coeff, 0]])
    full_noise = sp.simplify(local_noise + residual_noise)
    gamma = orientation_qv_matrix(grad_omega, sp.eye(3), nu)
    U = integer_scaled_one_mode_heat_shear(amplitude, mode, y, t, nu)
    Uy0 = sp.simplify(sp.diff(U, y).subs(y, 0))
    Gu0 = sp.zeros(3)
    Gu0[0, 1] = Uy0
    Ldot = material_line_frame_rhs(Gu0, L)
    Bdot = sp.simplify(two_sided_stretch_action(Gu0, B))
    Btdot = packet_tangential_support_rate(Gu0, B, normal)

    calibration = one_mode_intrinsic_localization_calibration(
        amplitude, mode, theta, coords, t, nu
    )
    compatibility = sp.simplify(calibration["compatibility_defect"])
    grad_e_boundary = sp.simplify(
        amplitude**2 * mode**5 * decay**2 * sp.sqrt(theta * (1 - theta))
    )
    ancestry_faces = ancestry_superlevel_flux_faces(
        sp.Rational(1, 2) / sp.pi,
        0,
        0,
        compatibility,
        grad_e_boundary,
    )
    state_kwargs = {
        "level": theta,
        "half_width_y": h,
        "y_span": s,
        "line_frame": L,
        "area_frame": H,
        "support_tensor": B,
        "level_normal": normal,
        "tangential_projector": P,
        "tangential_support_tensor": Bt,
        "face_quadrupoles": face_q,
        "quadrupole_sum": qsum,
        "circulation": K,
        "target_vorticity": omega,
        "raw_error": eps,
        "physical_residual": r,
        "codeforming_residual": chi,
        "target_gradient": grad_omega,
        "residual_noise": residual_noise,
        "full_codeforming_noise": full_noise,
        "orientation_qv": gamma,
        "nanson_line_rate": Ldot,
        "support_tensor_rate": Bdot,
        "tangential_support_rate": Btdot,
        "endpoint_nonaffinity": centered_one_mode_endpoint_nonaffinity(amplitude, mode, alpha, t, nu),
        "compatibility_defect": compatibility,
        "uniform_ancestry_flux": sp.simplify(ancestry_faces["total"]),
    }
    return IntrinsicChamberPacketState(**state_kwargs)


def unit_transverse_intrinsic_support_no_go(
    amplitude: sp.Expr,
    mode: sp.Expr,
    alpha: sp.Symbol,
    coords: tuple[sp.Symbol, sp.Symbol, sp.Symbol],
    t: sp.Expr,
    nu: sp.Expr,
) -> dict[str, sp.Expr | Matrix]:
    """Nested-chamber limit with x and z line lengths fixed equal to one."""
    state = intrinsic_chamber_packet_state(amplitude, mode, alpha, 1, 1, coords, t, nu)
    J = sp.simplify(sp.det(state.line_frame))
    diameter_sq = sp.simplify(sp.trace(state.support_tensor))
    condition_ratio = sp.simplify(mode / (2 * alpha))
    persistent_area = sp.simplify(state.area_frame[1, 1])
    out = {
        "level": state.level,
        "boundary_level_residual": chamber_boundary_level_residual(alpha, mode),
        "compatibility_defect": state.compatibility_defect,
        "uniform_ancestry_flux": state.uniform_ancestry_flux,
        "line_frame": state.line_frame,
        "area_frame": state.area_frame,
        "packet_volume": J,
        "support_tensor": state.support_tensor,
        "tangential_support_tensor": state.tangential_support_tensor,

        "diameter_squared": diameter_sq,
        "condition_ratio": condition_ratio,
        "persistent_transverse_area": persistent_area,
    }
    out["volume_limit"] = sp.limit(J, alpha, 0, dir="+")
    out["residual_limit"] = sp.limit(state.physical_residual[2], alpha, 0, dir="+")
    out["diameter_limit"] = sp.limit(diameter_sq, alpha, 0, dir="+")
    out["condition_limit"] = sp.limit(condition_ratio, alpha, 0, dir="+")
    return out
