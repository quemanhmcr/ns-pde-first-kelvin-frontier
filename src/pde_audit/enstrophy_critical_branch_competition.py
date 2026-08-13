"""Exact competition and value-crossing algebra for smooth enstrophy critical branches.

A selector/ranking switch between two already-existing smooth critical branches is a
different event from critical-Hessian degeneracy.  If branch values e_1(t), e_2(t)
cross transversally, the active winner can switch while both branches remain smooth
and nondegenerate.

For Navier--Stokes enstrophy critical branches, each branch value derivative is the
literal three-face rate stretching - Kelvin_bulk + nu Delta e.  Hence the crossing
gap derivative is the difference of those physical branch rates.
"""
from __future__ import annotations

import sympy as sp

from .first_bad_candidate_exclusions import gradient, laplacian, navier_stokes_residual
from .local_enstrophy_kelvin_growth_gate import enstrophy_balance_faces, enstrophy_density

Matrix = sp.MatrixBase


def branch_value_gap(value_1: sp.Expr,value_2: sp.Expr) -> sp.Expr:
    return sp.simplify(value_1-value_2)


def branch_value_gap_rate(rate_1: sp.Expr,rate_2: sp.Expr) -> sp.Expr:
    return sp.simplify(rate_1-rate_2)


def branch_growth_rate_from_faces(
    stretching: sp.Expr,
    kelvin_bulk: sp.Expr,
    curvature_diffusion: sp.Expr,
) -> sp.Expr:
    return sp.simplify(stretching-kelvin_bulk+curvature_diffusion)


def crossing_gap_rate_face_difference_residual(
    gap_rate: sp.Expr,
    stretch_1: sp.Expr,
    bulk_1: sp.Expr,
    curvature_1: sp.Expr,
    stretch_2: sp.Expr,
    bulk_2: sp.Expr,
    curvature_2: sp.Expr,
) -> sp.Expr:
    rhs=branch_growth_rate_from_faces(stretch_1,bulk_1,curvature_1)-branch_growth_rate_from_faces(
        stretch_2,bulk_2,curvature_2
    )
    return sp.simplify(gap_rate-rhs)


def transverse_crossing_orientation(gap_rate_at_crossing: sp.Expr) -> int:
    """Return +1 for branch 2 -> branch 1 winner switch, -1 for the reverse.

    Used only in exact numeric/calibration contexts where sign is decidable.
    """
    v=sp.simplify(gap_rate_at_crossing)
    if v.is_positive:
        return 1
    if v.is_negative:
        return -1
    if v.is_zero:
        raise ValueError("crossing is not transverse")
    fv=float(sp.N(v))
    if fv > 0:
        return 1
    if fv < 0:
        return -1
    raise ValueError("crossing is not transverse")


def two_branch_max_envelope_at_crossing(
    common_value: sp.Expr,
    left_winner_rate: sp.Expr,
    right_winner_rate: sp.Expr,
) -> dict[str,sp.Expr]:
    """Continuous max envelope with generally different one-sided derivatives."""
    return {
        "value_left":sp.simplify(common_value),
        "value_right":sp.simplify(common_value),
        "left_derivative":sp.simplify(left_winner_rate),
        "right_derivative":sp.simplify(right_winner_rate),
        "derivative_jump":sp.simplify(right_winner_rate-left_winner_rate),
    }


def selector_scalar_jump_at_tie(
    common_value: sp.Expr,
    pre_selector: Matrix,
    post_selector: Matrix,
) -> sp.Expr:
    """Selector changes branch index, but selected scalar value has zero jump at a tie."""
    x=sp.Matrix([common_value,common_value])
    if pre_selector.shape != (1,2) or post_selector.shape != (1,2):
        raise ValueError("selectors must be 1x2 branch readouts")
    return sp.simplify((post_selector*x)[0]-(pre_selector*x)[0])


def nondegenerate_value_crossing_geometry_calibration(time: sp.Symbol) -> dict[str,object]:
    """Pure geometry: equal branch values can cross while both Hessians stay negative definite.

    This is not an NS calibration.  It proves only that the value-crossing condition
    and Hessian-degeneracy condition are mathematically independent event surfaces.
    """
    H1=-2*sp.eye(3)
    H2=-4*sp.eye(3)
    v1=time
    v2=-time
    return {
        "value_1":v1,
        "value_2":v2,
        "gap":sp.simplify(v1-v2),
        "gap_rate":sp.simplify(sp.diff(v1-v2,time)),
        "crossing_time":sp.Integer(0),
        "hessian_1":H1,
        "hessian_2":H2,
        "det_hessian_1":sp.det(H1),
        "det_hessian_2":sp.det(H2),
    }


def three_mode_heat_shear(
    y: sp.Symbol,
    t: sp.Symbol,
    nu: sp.Expr,
) -> sp.Expr:
    """Periodic exact shear velocity U(y,t) with a designed critical-value crossing."""
    return sp.simplify(
        -sp.exp(-nu*t)*sp.sin(y)
        -sp.Rational(3,2)*sp.exp(3)*sp.exp(-4*nu*t)*sp.sin(2*y)
        +sp.Rational(1,3)*sp.exp(8)*sp.exp(-9*nu*t)*sp.sin(3*y)
    )


def three_mode_heat_shear_velocity(
    x: sp.Symbol,
    y: sp.Symbol,
    z: sp.Symbol,
    t: sp.Symbol,
    nu: sp.Expr,
) -> Matrix:
    del x,z
    return sp.Matrix([three_mode_heat_shear(y,t,nu),0,0])


def three_mode_heat_shear_vorticity(
    y: sp.Symbol,
    t: sp.Symbol,
    nu: sp.Expr,
) -> Matrix:
    U=three_mode_heat_shear(y,t,nu)
    return sp.Matrix([0,0,sp.simplify(-sp.diff(U,y))])


def three_mode_branch_crossing_calibration(
    x: sp.Symbol,
    y: sp.Symbol,
    z: sp.Symbol,
    t: sp.Symbol,
    nu: sp.Expr,
) -> dict[str,object]:
    """Exact periodic NS: two persistent critical sheets exchange the larger enstrophy value.

    At t*=1/nu the y=0 and y=pi sheets have equal value and strictly negative,
    nonzero transverse y-curvature.  Translation symmetry leaves flat x/z directions,
    so this is a critical-sheet calibration, not a full isolated-Hessian calibration.
    The ranking crosses while both values are decreasing and neither critical sheet
    is created or destroyed.
    """
    coords=(x,y,z)
    u=three_mode_heat_shear_velocity(x,y,z,t,nu)
    omega=three_mode_heat_shear_vorticity(y,t,nu)
    e=enstrophy_density(omega)
    tstar=sp.simplify(1/nu)
    p0={y:0,t:tstar}
    ppi={y:sp.pi,t:tstar}
    w=omega[2]
    wy=sp.diff(w,y)
    eyy=sp.diff(e,y,2)
    e0=sp.simplify(e.subs(p0))
    epi=sp.simplify(e.subs(ppi))
    eyy0=sp.simplify(eyy.subs(p0))
    eyy_pi=sp.simplify(eyy.subs(ppi))
    et0=sp.simplify(sp.diff(e,t).subs(p0))
    etpi=sp.simplify(sp.diff(e,t).subs(ppi))
    gap=sp.simplify(e.subs(y,0)-e.subs(y,sp.pi))
    gapdot=sp.simplify(sp.diff(gap,t))
    gapdot_star=sp.simplify(gapdot.subs(t,tstar))
    faces=enstrophy_balance_faces(u,omega,coords,t,nu)
    def face_at(name: str, point: dict[sp.Symbol,sp.Expr]) -> sp.Expr:
        return sp.simplify(faces[name].subs(point))
    rate0=branch_growth_rate_from_faces(
        face_at("stretching",p0),face_at("kelvin_bulk",p0),face_at("curvature_diffusion",p0)
    )
    ratepi=branch_growth_rate_from_faces(
        face_at("stretching",ppi),face_at("kelvin_bulk",ppi),face_at("curvature_diffusion",ppi)
    )
    # Periodic shear solves NS with p=0: U_t=nu U_yy and advection vanishes.
    ns=sp.simplify(navier_stokes_residual(u,sp.Integer(0),coords,t,nu))
    before=sp.simplify(gap.subs(t,sp.Rational(1,2)/nu))
    after=sp.simplify(gap.subs(t,sp.Rational(3,2)/nu))
    pre_selector=sp.Matrix([[0,1]])
    post_selector=sp.Matrix([[1,0]])
    envelope=two_branch_max_envelope_at_crossing(e0,etpi,et0)
    return {
        "velocity":u,
        "vorticity":omega,
        "enstrophy":e,
        "ns_residual":ns,
        "t_cross":tstar,
        "critical_y_derivative_0":sp.simplify(sp.diff(e,y).subs(p0)),
        "critical_y_derivative_pi":sp.simplify(sp.diff(e,y).subs(ppi)),
        "vorticity_y_derivative_0":sp.simplify(wy.subs(p0)),
        "vorticity_y_derivative_pi":sp.simplify(wy.subs(ppi)),
        "value_0":e0,
        "value_pi":epi,
        "hessian_yy_0":eyy0,
        "hessian_yy_pi":eyy_pi,
        "time_rate_0":et0,
        "time_rate_pi":etpi,
        "growth_rate_from_faces_0":rate0,
        "growth_rate_from_faces_pi":ratepi,
        "stretching_0":face_at("stretching",p0),
        "stretching_pi":face_at("stretching",ppi),
        "kelvin_bulk_0":face_at("kelvin_bulk",p0),
        "kelvin_bulk_pi":face_at("kelvin_bulk",ppi),
        "curvature_0":face_at("curvature_diffusion",p0),
        "curvature_pi":face_at("curvature_diffusion",ppi),
        "gap":gap,
        "gap_before":before,
        "gap_after":after,
        "gap_rate_at_crossing":gapdot_star,
        "gap_rate_face_residual":crossing_gap_rate_face_difference_residual(
            gapdot_star,
            face_at("stretching",p0),face_at("kelvin_bulk",p0),face_at("curvature_diffusion",p0),
            face_at("stretching",ppi),face_at("kelvin_bulk",ppi),face_at("curvature_diffusion",ppi),
        ),
        "selector_scalar_jump_at_tie":selector_scalar_jump_at_tie(e0,pre_selector,post_selector),
        "envelope":envelope,
    }
