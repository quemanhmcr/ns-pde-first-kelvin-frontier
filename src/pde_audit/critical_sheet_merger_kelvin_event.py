"""Exact Kelvin-packet event calibration at a smooth NS critical-sheet merger.

The physical Navier--Stokes field is the periodic heat shear

    u=(U(y,t),0,0),
    U=-e^{-nu t} sin y -(e^3/8)e^{-4 nu t} sin(2y).

Because u is x-independent and has only an x component, the nonlinear transport
term vanishes exactly and the 3D NSE reduce to the literal heat equation for U.
The enstrophy critical sheets y=pi+-d(t), cos d=e^{3(nu t-1)}, merge into the
persistent sheet y=pi at t*=1/nu while the NSE field stays analytic.

This module then attaches an orientation-complete *physical* Kelvin box packet to
a critical-sheet anchor.  The xy face is intentionally one-sided in y, [a,a+s],
so the finite-current Brownian anchor response remains nonzero at the merger.  This
lets the merger referee target, affine reanchoring, and same-replica cross blocks
without hiding them behind a symmetric zero-noise packet.

The critical-sheet geometry fixes the anchor a but not the box shape (s,l,m).  Thus
same-shape translated packets coalesce in every instantaneous physical component,
whereas different admissible shapes at the same merged sheet need not.  This is a
no-go against inferring full packet-state coalescence from scalar/critical geometry
alone.  Branch/ancestry labels remain separate data even when instantaneous packet
states coincide.
"""
from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Sequence
import sympy as sp

from .codeforming_surface_moment_tower import cofactor_map
from .same_replica_residual_library_dynamics import same_replica_library_qv

Matrix = sp.MatrixBase


@dataclass(frozen=True)
class KelvinPacketState:
    anchor_y: sp.Expr
    line_frame: Matrix
    area_frame: Matrix
    circulation: Matrix
    target_vorticity: Matrix
    raw_error: Matrix
    physical_residual: Matrix
    codeforming_residual: Matrix
    target_gradient: Matrix
    residual_noise: Matrix
    full_codeforming_noise: Matrix


def merger_time(nu: sp.Expr) -> sp.Expr:
    return sp.simplify(1 / nu)


def merger_ratio(t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """r(t)=exp(3(nu t-1)); side sheets exist for 0<r<1."""
    return sp.exp(3 * (nu * t - 1))


def merger_half_separation(t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """d(t)=acos r(t), so side sheets are pi+-d."""
    return sp.acos(merger_ratio(t, nu))


def merger_side_anchors(t: sp.Expr, nu: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
    d = merger_half_separation(t, nu)
    return sp.pi - d, sp.pi + d


def merger_shear_scalar(y: sp.Expr, t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    return sp.simplify(
        -sp.exp(-nu * t) * sp.sin(y)
        - sp.exp(3) * sp.exp(-4 * nu * t) * sp.sin(2 * y) / 8
    )


def merger_shear_velocity(
    coords: tuple[sp.Symbol, sp.Symbol, sp.Symbol],
    t: sp.Expr,
    nu: sp.Expr,
) -> Matrix:
    _, y, _ = coords
    return sp.Matrix([merger_shear_scalar(y, t, nu), 0, 0])


def merger_shear_vorticity_scalar(y: sp.Expr, t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    return sp.simplify(
        sp.exp(-nu * t) * sp.cos(y)
        + sp.exp(3) * sp.exp(-4 * nu * t) * sp.cos(2 * y) / 4
    )


def merger_shear_vorticity(
    coords: tuple[sp.Symbol, sp.Symbol, sp.Symbol],
    t: sp.Expr,
    nu: sp.Expr,
) -> Matrix:
    _, y, _ = coords
    return sp.Matrix([0, 0, merger_shear_vorticity_scalar(y, t, nu)])


def merger_shear_ns_residual(
    coords: tuple[sp.Symbol, sp.Symbol, sp.Symbol],
    t: sp.Symbol,
    nu: sp.Expr,
) -> tuple[Matrix, sp.Expr, sp.Expr]:
    """Return (momentum residual, divergence, pressure) for the exact shear."""
    u = merger_shear_velocity(coords, t, nu)
    p = sp.Integer(0)
    adv = sp.Matrix([
        sum(u[j] * sp.diff(u[i], coords[j]) for j in range(3))
        for i in range(3)
    ])
    lap = sp.Matrix([
        sum(sp.diff(u[i], q, 2) for q in coords)
        for i in range(3)
    ])
    residual = sp.simplify(sp.diff(u, t) + adv - nu * lap)
    div = sp.simplify(sum(sp.diff(u[i], coords[i]) for i in range(3)))
    return residual, div, p


def merger_enstrophy(y: sp.Expr, t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    q = merger_shear_vorticity_scalar(y, t, nu)
    return sp.simplify(q**2 / 2)


def merger_vorticity_gradient_factor(y: sp.Expr, t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Exact q_y; critical side sheets use the non-sin factor."""
    return sp.factor(sp.diff(merger_shear_vorticity_scalar(y, t, nu), y))


def reduced_side_vorticity(alpha: sp.Expr, ratio: sp.Expr) -> sp.Expr:
    """q on cos y=-r, with alpha=e^{-nu t}."""
    r = ratio
    return sp.simplify(-alpha * (2 * r**2 + 1) / (4 * r))


def reduced_side_transverse_hessian(alpha: sp.Expr, ratio: sp.Expr) -> sp.Expr:
    """e_yy on either side sheet, expressed only through alpha=e^{-nu t}, r."""
    r = ratio
    return sp.simplify(-alpha**2 * (2 * r**2 + 1) * (1 - r**2) / (4 * r**2))


def merger_quartic_transverse_derivative() -> sp.Expr:
    """e_yyyy(pi,t*) for the exact periodic merger."""
    return sp.simplify(-sp.Rational(9, 4) * sp.exp(-2))


def critical_sheet_speed_product(d: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """d |d_dot| after writing r=cos d and r_dot=3 nu r."""
    return sp.simplify(3 * nu * d * sp.cos(d) / sp.sin(d))


def critical_sheet_speed_product_limit(nu: sp.Expr) -> sp.Expr:
    d = sp.symbols("d_merger", positive=True)
    return sp.simplify(sp.limit(critical_sheet_speed_product(d, nu), d, 0, dir="+"))


def asymmetric_box_line_frame(
    y_span: sp.Expr,
    x_length: sp.Expr,
    z_length: sp.Expr,
) -> Matrix:
    """Diagonal line frame for the one-sided box packet [a,a+s] in y."""
    return sp.diag(x_length, y_span, z_length)


def asymmetric_box_circulation_z(
    anchor_y: sp.Expr,
    y_span: sp.Expr,
    x_length: sp.Expr,
    t: sp.Expr,
    nu: sp.Expr,
) -> sp.Expr:
    """Exact Kelvin circulation of the xy face with +z orientation."""
    a, s, ell = anchor_y, y_span, x_length
    return sp.simplify(
        ell
        * (
            sp.exp(-nu * t) * (sp.sin(a + s) - sp.sin(a))
            + sp.exp(3) * sp.exp(-4 * nu * t)
            * (sp.sin(2 * (a + s)) - sp.sin(2 * a))
            / 8
        )
    )


def asymmetric_box_packet_state(
    anchor_y: sp.Expr,
    y_span: sp.Expr,
    x_length: sp.Expr,
    z_length: sp.Expr,
    t: sp.Expr,
    nu: sp.Expr,
) -> KelvinPacketState:
    """Orientation-complete finite Kelvin packet attached to a sheet anchor.

    The yz and zx faces have zero vorticity flux for this shear.  The xy face has
    exact circulation through the finite y interval [a,a+s].  The local target is
    the vorticity at the anchor a, not a face average.
    """
    a, s, ell, m = anchor_y, y_span, x_length, z_length
    L = asymmetric_box_line_frame(s, ell, m)
    H = cofactor_map(L)
    q = merger_shear_vorticity_scalar(a, t, nu)
    K = sp.Matrix([0, 0, asymmetric_box_circulation_z(a, s, ell, t, nu)])
    omega = sp.Matrix([0, 0, q])
    eps = sp.simplify(K - H.T * omega)
    r = sp.simplify(H.inv().T * eps)
    J = sp.det(L)
    chi = sp.simplify(eps / J)

    # Differentiate before substituting a possibly constant anchor (for example a=pi).
    aa = sp.symbols("a_packet", real=True)
    qy_general = sp.diff(merger_shear_vorticity_scalar(aa, t, nu), aa)
    qy = sp.simplify(qy_general.subs(aa, a))
    grad_omega = sp.zeros(3)
    grad_omega[2, 1] = qy
    local_noise = sp.simplify(L.inv() * grad_omega)

    K_general = sp.Matrix([0, 0, asymmetric_box_circulation_z(aa, s, ell, t, nu)])
    omega_general = sp.Matrix([0, 0, merger_shear_vorticity_scalar(aa, t, nu)])
    eps_general = sp.simplify(K_general - H.T * omega_general)
    chi_general = sp.simplify(eps_general / J)
    residual_noise = sp.zeros(3)
    residual_noise[2, 1] = sp.simplify(sp.diff(chi_general[2], aa).subs(aa, a))
    full_noise = sp.simplify(local_noise + residual_noise)
    return KelvinPacketState(
        anchor_y=a,
        line_frame=L,
        area_frame=H,
        circulation=K,
        target_vorticity=omega,
        raw_error=eps,
        physical_residual=r,
        codeforming_residual=chi,
        target_gradient=grad_omega,
        residual_noise=residual_noise,
        full_codeforming_noise=full_noise,
    )


def merger_packet_residual_z(y_span: sp.Expr) -> sp.Expr:
    """Exact physical r_z at a=pi,t*=1/nu; independent of nu,l,m."""
    s = y_span
    return sp.simplify(
        sp.exp(-1) * (6 * s - 8 * sp.sin(s) + sp.sin(2 * s)) / (8 * s)
    )


def merger_packet_noise_zy(y_span: sp.Expr, z_length: sp.Expr) -> sp.Expr:
    """Exact codeforming anchor-noise coefficient N_zy at the merger."""
    s, m = y_span, z_length
    return sp.simplify(sp.exp(-1) * (1 - sp.cos(s))**2 / (2 * s * m))


def merger_packet_anchor_residual_derivative(y_span: sp.Expr) -> sp.Expr:
    """partial_a r_z at the merger; nonzero for a generic one-sided packet."""
    s = y_span
    return sp.simplify(sp.exp(-1) * (1 - sp.cos(s))**2 / (2 * s))


def merger_packet_cusp_coefficient(y_span: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Limit d*|d/dt r_z(side)| from the singular anchor speed face."""
    return sp.simplify(3 * nu * merger_packet_anchor_residual_derivative(y_span))


def collision_embedding(packet_count: int, fiber_dim: int = 3) -> Matrix:
    """S=1_N tensor I, embedding one coalesced packet into an N-label library."""
    if packet_count <= 0 or fiber_dim <= 0:
        raise ValueError("positive packet/fiber dimensions required")
    return sp.kronecker_product(sp.ones(packet_count, 1), sp.eye(fiber_dim))


def branch_extraction(packet_count: int, index: int, fiber_dim: int = 3) -> Matrix:
    if not (0 <= index < packet_count):
        raise ValueError("packet index out of range")
    E = sp.zeros(fiber_dim, packet_count * fiber_dim)
    E[:, index * fiber_dim:(index + 1) * fiber_dim] = sp.eye(fiber_dim)
    return E


def normalized_collision_quotient(weights: Sequence[sp.Expr], fiber_dim: int = 3) -> Matrix:
    if not weights:
        raise ValueError("nonempty collision weights required")
    return sp.Matrix.hstack(*[sp.simplify(w) * sp.eye(fiber_dim) for w in weights])


def normalized_collision_quotient_residual(
    weights: Sequence[sp.Expr], fiber_dim: int = 3
) -> Matrix:
    C = normalized_collision_quotient(weights, fiber_dim)
    S = collision_embedding(len(weights), fiber_dim)
    return sp.simplify(C * S - sum(weights) * sp.eye(fiber_dim))


def collision_affine_event_data(
    event_map: Matrix,
    common_target: Matrix,
    common_target_gradient: Matrix,
    packet_count: int,
) -> tuple[Matrix, Matrix]:
    """Return (d,N_target) for a collision library with identical local targets."""
    S = collision_embedding(packet_count, common_target.rows)
    omega_minus = sp.simplify(S * common_target)
    grad_minus = sp.simplify(S * common_target_gradient)
    d = sp.simplify(event_map * omega_minus - common_target)
    ntarget = sp.simplify(event_map * grad_minus - common_target_gradient)
    return d, ntarget


def coalesced_noise_stack(noise_block: Matrix, packet_count: int) -> Matrix:
    return sp.simplify(collision_embedding(packet_count, noise_block.rows) * noise_block)


def coalesced_same_replica_qv(noise_block: Matrix, packet_count: int, nu: sp.Expr) -> Matrix:
    return same_replica_library_qv([noise_block] * packet_count, nu)


def quotient_qv_residual(
    noise_block: Matrix,
    weights: Sequence[sp.Expr],
    nu: sp.Expr,
) -> Matrix:
    C = normalized_collision_quotient(weights, noise_block.rows)
    G = coalesced_same_replica_qv(noise_block, len(weights), nu)
    target = sp.simplify(2 * nu * noise_block * noise_block.T)
    return sp.simplify(C * G * C.T - sum(weights)**2 * target)


def diagonal_only_quotient_defect(
    noise_block: Matrix,
    weights: Sequence[sp.Expr],
    nu: sp.Expr,
) -> Matrix:
    """Counterfactual defect after deleting same-replica cross-label q.v. blocks."""
    block = sp.simplify(2 * nu * noise_block * noise_block.T)
    diagonal = sp.diag(*([block] * len(weights)))
    C = normalized_collision_quotient(weights, noise_block.rows)
    target = sp.simplify(sum(weights)**2 * block)
    return sp.simplify(C * diagonal * C.T - target)


def collision_selector_jump_residual(
    packet_state: Matrix,
    left_index: int,
    right_index: int,
    packet_count: int = 3,
) -> Matrix:
    """(E_right-E_left) S x: label switch has no physical jump on collision subspace."""
    S = collision_embedding(packet_count, packet_state.rows)
    El = branch_extraction(packet_count, left_index, packet_state.rows)
    Er = branch_extraction(packet_count, right_index, packet_state.rows)
    return sp.simplify((Er - El) * S * packet_state)


def different_shape_packet_no_go_witness() -> dict[str, sp.Expr | Matrix]:
    """Two legitimate packet shapes at the same merged critical sheet disagree."""
    s1 = sp.pi / 2
    s2 = sp.pi / 3
    r1 = merger_packet_residual_z(s1)
    r2 = merger_packet_residual_z(s2)
    n1 = merger_packet_noise_zy(s1, sp.Integer(1))
    n2 = merger_packet_noise_zy(s2, sp.Integer(1))
    H1 = cofactor_map(asymmetric_box_line_frame(s1, sp.Integer(1), sp.Integer(1)))
    H2 = cofactor_map(asymmetric_box_line_frame(s2, sp.Integer(1), sp.Integer(1)))
    return {
        "span_1": s1,
        "span_2": s2,
        "area_frame_1": H1,
        "area_frame_2": H2,
        "residual_1": r1,
        "residual_2": r2,
        "residual_difference": sp.simplify(r1 - r2),
        "noise_1": n1,
        "noise_2": n2,
        "noise_difference": sp.simplify(n1 - n2),
    }
