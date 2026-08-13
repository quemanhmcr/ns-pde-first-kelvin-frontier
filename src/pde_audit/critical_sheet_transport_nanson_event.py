"""Exact transport anatomy of a Kelvin packet attached to the NS critical-sheet merger.

This module continues ``critical_sheet_merger_kelvin_event`` without freezing packet
shape by hand.  It distinguishes three pieces that coincide only if one simplifies
too early:

* the Eulerian enstrophy critical sheet, whose normal speed is fixed by the PDE;
* the physical Kelvin/material transport, whose common-noise relative shape has no
  Brownian motion and whose deterministic shear has zero y velocity;
* a sheet-attached local Nanson frame, which can be reanchored along the critical
  sheet but then retains the integrated velocity-gradient history of that branch.

For the exact periodic two-mode heat shear, these pieces give a rigid no-go.  The
side critical sheets move in y whereas material trajectories do not.  A literal
Kelvin stochastic anchor also has y quadratic variation 2 nu, whereas the critical
sheet path has zero quadratic variation.  Thus a sheet-attached packet is an
Eulerian moving-cut/readout, not the same object as a Kelvin ancestry trajectory.

If one nevertheless transports a local frame by the forward Nanson connection
Ldot=(grad u)L along each reanchored critical branch, the central and side histories
accumulate different finite shears.  They reach the same anchor and local vorticity
at the merger but not the same frame/support state.  The singular derivative of the
one-sided packet found in the previous milestone is identified exactly as the
moving-cut circulation flux; the viscous face stays finite.

No first-bad identification, restart, continuation, or regularity theorem is made.
"""
from __future__ import annotations

from dataclasses import dataclass
import sympy as sp

from .codeforming_surface_moment_tower import cofactor_map
from .critical_sheet_merger_kelvin_event import (
    asymmetric_box_circulation_z,
    merger_packet_cusp_coefficient,
    merger_ratio,
    merger_shear_scalar,
    merger_shear_vorticity_scalar,
    merger_side_anchors,
    merger_time,
)

Matrix = sp.MatrixBase
_VALID_BRANCHES = {"central", "minus", "plus", "side"}


@dataclass(frozen=True)
class TransportedMergerPacketState:
    branch: str
    anchor_y: sp.Expr
    shear_history: sp.Expr
    line_frame: Matrix
    area_frame: Matrix
    circulation: Matrix
    target_vorticity: Matrix
    raw_error: Matrix
    physical_residual: Matrix
    codeforming_residual: Matrix


@dataclass(frozen=True)
class MovingCutCirculationFaces:
    diffusion: sp.Expr
    moving_cut: sp.Expr
    total: sp.Expr


def _check_branch(branch: str) -> None:
    if branch not in _VALID_BRANCHES:
        raise ValueError(f"unknown critical branch: {branch}")


def critical_branch_anchor(branch: str, t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Eulerian y-coordinate of the central/minus/plus critical sheet."""
    _check_branch(branch)
    if branch == "central":
        return sp.pi
    minus, plus = merger_side_anchors(t, nu)
    if branch in {"minus", "side"}:
        return minus
    return plus


def critical_branch_normal_speed(branch: str, t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Exact physical-time y speed of the critical sheet.

    The fluid has u_y=0.  Hence this is also the normal reanchoring velocity of a
    sheet-attached Eulerian packet relative to material transport.
    """
    _check_branch(branch)
    if branch == "central":
        return sp.Integer(0)
    r = merger_ratio(t, nu)
    speed = sp.simplify(3 * nu * r / sp.sqrt(1 - r**2))
    if branch in {"minus", "side"}:
        return speed
    return -speed


def central_critical_vorticity(t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    return sp.simplify(-sp.exp(-nu * t) + sp.exp(3 - 4 * nu * t) / 4)


def side_critical_vorticity(t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """q on either side sheet, after using cos(y)=-r(t)."""
    return sp.simplify(-sp.exp(2 * nu * t - 3) / 2 - sp.exp(3 - 4 * nu * t) / 4)


def critical_vorticity_gap_side_minus_central(t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Exact q_side-q_central, strictly negative before the merger."""
    r = merger_ratio(t, nu)
    alpha = sp.exp(-nu * t)
    return sp.simplify(-alpha * (1 - r) ** 2 / (2 * r))


def branch_nanson_shear_history(branch: str, t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Forward local-Nanson shear gamma(t) from common identity data at t=0.

    With A=(partial_y U) E_xy=-q E_xy and L=(I+gamma E_xy)L0, one has
    gamma_dot=partial_y U=-q.  The two side branches have the same q history.
    """
    _check_branch(branch)
    if branch == "central":
        return sp.simplify(
            (1 - sp.exp(-nu * t)) / nu
            - sp.exp(3) * (1 - sp.exp(-4 * nu * t)) / (16 * nu)
        )
    return sp.simplify(
        sp.exp(-3) * (sp.exp(2 * nu * t) - 1) / (4 * nu)
        + sp.exp(3) * (1 - sp.exp(-4 * nu * t)) / (16 * nu)
    )


def nanson_history_gap(t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Delta gamma=gamma_central-gamma_side for common initialization at t=0."""
    return sp.simplify(
        branch_nanson_shear_history("central", t, nu)
        - branch_nanson_shear_history("side", t, nu)
    )


def nanson_history_gap_rate(t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Delta gamma_dot=q_side-q_central<0 for every pre-merger time."""
    return critical_vorticity_gap_side_minus_central(t, nu)


def merger_nanson_history_gap(nu: sp.Expr) -> sp.Expr:
    """Nonzero central-minus-side Nanson shear memory at t*=1/nu."""
    return sp.simplify(nanson_history_gap(merger_time(nu), nu))


def shear_nanson_line_frame(
    shear_history: sp.Expr,
    y_span: sp.Expr,
    x_length: sp.Expr,
    z_length: sp.Expr,
) -> Matrix:
    """L=(I+gamma E_xy) diag(ell,s,m)."""
    gamma, s, ell, m = shear_history, y_span, x_length, z_length
    return sp.Matrix([[ell, gamma * s, 0], [0, s, 0], [0, 0, m]])


def shear_nanson_area_frame(
    shear_history: sp.Expr,
    y_span: sp.Expr,
    x_length: sp.Expr,
    z_length: sp.Expr,
) -> Matrix:
    return cofactor_map(
        shear_nanson_line_frame(shear_history, y_span, x_length, z_length)
    )


def merger_history_line_comparison(nu: sp.Expr) -> Matrix:
    """L_c L_s^{-1}=I+Delta gamma E_xy at the merger (scale cancels)."""
    dg = merger_nanson_history_gap(nu)
    return sp.Matrix([[1, dg, 0], [0, 1, 0], [0, 0, 1]])


def merger_history_area_comparison(nu: sp.Expr) -> Matrix:
    """cof(L_c L_s^{-1})=I-Delta gamma E_yx."""
    return cofactor_map(merger_history_line_comparison(nu))


def transported_merger_packet_state(
    branch: str,
    y_span: sp.Expr,
    x_length: sp.Expr,
    z_length: sp.Expr,
    nu: sp.Expr,
) -> TransportedMergerPacketState:
    """Endpoint packet built from branch Nanson history and the common merger anchor.

    The affine shear changes support/frame geometry but leaves the xy oriented area
    vector unchanged.  For this z-vorticity heat shear, circulation and the own-local
    reconstructed residual therefore coincide across branches even though L and H do
    not.  This makes the hidden geometry memory explicit rather than projecting it
    away into the residual fiber.
    """
    _check_branch(branch)
    T = merger_time(nu)
    gamma = branch_nanson_shear_history(branch, T, nu)
    L = shear_nanson_line_frame(gamma, y_span, x_length, z_length)
    H = cofactor_map(L)
    q = merger_shear_vorticity_scalar(sp.pi, T, nu)
    K = sp.Matrix(
        [0, 0, asymmetric_box_circulation_z(sp.pi, y_span, x_length, T, nu)]
    )
    omega = sp.Matrix([0, 0, q])
    eps = sp.simplify(K - H.T * omega)
    r = sp.simplify(H.inv().T * eps)
    chi = sp.simplify(eps / sp.det(L))
    return TransportedMergerPacketState(
        branch=branch,
        anchor_y=sp.pi,
        shear_history=gamma,
        line_frame=L,
        area_frame=H,
        circulation=K,
        target_vorticity=omega,
        raw_error=eps,
        physical_residual=r,
        codeforming_residual=chi,
    )


def finite_shear_nonaffinity_x(
    anchor_y: sp.Expr,
    relative_y: sp.Expr,
    t: sp.Expr,
    nu: sp.Expr,
) -> sp.Expr:
    """Delta U-U_y(a) r_y: exact finite-support nonaffinity of the shear."""
    a, ry = anchor_y, relative_y
    U = merger_shear_scalar(a, t, nu)
    U_shift = merger_shear_scalar(a + ry, t, nu)
    aa = sp.symbols("a_transport", real=True)
    Uy = sp.diff(merger_shear_scalar(aa, t, nu), aa).subs(aa, a)
    return sp.simplify(U_shift - U - Uy * ry)


def sheet_attached_affine_grid_slip(
    anchor_y: sp.Expr,
    anchor_speed_y: sp.Expr,
    relative_y: sp.Expr,
    t: sp.Expr,
    nu: sp.Expr,
) -> Matrix:
    """Packet-grid velocity minus actual fluid velocity.

    If c_dot=u(c)+a_dot e_y and Ldot=A(c)L, then for a point with relative y=r_y

        V_grid-u(c+r) = -N_a(r_y) e_x + a_dot e_y.

    The two defects are orthogonal in this exact shear: finite nonaffinity is x-like,
    while critical-sheet reanchoring is y-like.  They cannot cancel each other.
    """
    nonaff = finite_shear_nonaffinity_x(anchor_y, relative_y, t, nu)
    return sp.Matrix([-nonaff, anchor_speed_y, 0])


def kelvin_anchor_y_qv_rate(nu: sp.Expr) -> sp.Expr:
    """Physical common-noise Kelvin anchor y quadratic-variation rate."""
    return sp.simplify(2 * nu)


def critical_sheet_path_y_qv_rate() -> sp.Expr:
    """A deterministic smooth/Hölder critical-sheet coordinate has zero q.v. here."""
    return sp.Integer(0)


def literal_sheet_kelvin_ancestry_qv_defect(nu: sp.Expr) -> sp.Expr:
    """Q.v. mismatch excluding literal identification of critical path with Kelvin anchor."""
    return sp.simplify(kelvin_anchor_y_qv_rate(nu) - critical_sheet_path_y_qv_rate())


def moving_cut_circulation_rate_faces(
    anchor_y: sp.Expr,
    anchor_speed_y: sp.Expr,
    y_span: sp.Expr,
    x_length: sp.Expr,
    t: sp.Expr,
    nu: sp.Expr,
) -> MovingCutCirculationFaces:
    """Exact Reynolds/heat split for K=ell int_a^{a+s} q(y,t)dy.

    q_t=nu q_yy gives

      Kdot = ell nu [q_y(a+s)-q_y(a)]
             + ell a_dot [q(a+s)-q(a)].

    The first face is viscous diffusion through the fixed endpoints; the second is
    the moving-cut/reanchoring flux created by the critical-sheet selector motion.
    """
    a, v, s, ell = anchor_y, anchor_speed_y, y_span, x_length
    yy = sp.symbols("y_cut", real=True)
    qy = sp.diff(merger_shear_vorticity_scalar(yy, t, nu), yy)
    q = merger_shear_vorticity_scalar
    diffusion = sp.simplify(
        ell * nu * (qy.subs(yy, a + s) - qy.subs(yy, a))
    )
    moving = sp.simplify(ell * v * (q(a + s, t, nu) - q(a, t, nu)))
    return MovingCutCirculationFaces(
        diffusion=diffusion,
        moving_cut=moving,
        total=sp.simplify(diffusion + moving),
    )


def moving_cut_chain_rule_residual(
    anchor_y: sp.Expr,
    anchor_speed_y: sp.Expr,
    y_span: sp.Expr,
    x_length: sp.Expr,
    t: sp.Symbol,
    nu: sp.Expr,
) -> sp.Expr:
    """Residual of (partial_t+a_dot partial_a)K against the two physical faces."""
    a, v = anchor_y, anchor_speed_y
    aa = sp.symbols("a_cut", real=True)
    K = asymmetric_box_circulation_z(aa, y_span, x_length, t, nu)
    chain = sp.simplify(sp.diff(K, t) + v * sp.diff(K, aa))
    faces = moving_cut_circulation_rate_faces(a, v, y_span, x_length, t, nu)
    return sp.simplify(chain.subs(aa, a) - faces.total)


def merger_support_vorticity_jump(y_span: sp.Expr) -> sp.Expr:
    """q(pi+s,t*)-q(pi,t*) for the one-sided packet."""
    s = y_span
    return sp.simplify(sp.exp(-1) * (1 - sp.cos(s)) ** 2 / 2)


def merger_viscous_circulation_face(
    y_span: sp.Expr,
    x_length: sp.Expr,
    nu: sp.Expr,
) -> sp.Expr:
    """Finite diffusion face at a=pi,t*=1/nu."""
    s, ell = y_span, x_length
    return sp.simplify(
        ell * nu * sp.exp(-1) * sp.sin(s) * (1 - sp.cos(s))
    )


def merger_moving_cut_flux_distance_product_limit(
    y_span: sp.Expr,
    x_length: sp.Expr,
    nu: sp.Expr,
) -> sp.Expr:
    """d*|moving-cut circulation rate| as either side sheet reaches merger."""
    return sp.simplify(
        3 * nu * x_length * merger_support_vorticity_jump(y_span)
    )


def merger_residual_cusp_from_moving_cut(
    y_span: sp.Expr,
    nu: sp.Expr,
) -> sp.Expr:
    """Area-normalized moving-cut singular coefficient; equals prior residual cusp."""
    s = y_span
    return sp.simplify(
        merger_moving_cut_flux_distance_product_limit(s, sp.Integer(1), nu) / s
    )


def merger_residual_cusp_identification_residual(
    y_span: sp.Expr,
    nu: sp.Expr,
) -> sp.Expr:
    return sp.simplify(
        merger_residual_cusp_from_moving_cut(y_span, nu)
        - merger_packet_cusp_coefficient(y_span, nu)
    )


def side_cut_total_variation_to_merger(t0: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Total y variation of either monotone side cut from t0 to t*=1/nu."""
    return sp.simplify(sp.acos(merger_ratio(t0, nu)))
