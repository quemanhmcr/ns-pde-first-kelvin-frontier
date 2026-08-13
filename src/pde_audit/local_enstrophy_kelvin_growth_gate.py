"""Literal local enstrophy growth law and its Kelvin q.v. interpretation.

The purpose is physical typing, not a singularity criterion.  For incompressible NS
vorticity omega,

  (d_t + u.grad - nu Delta)(|omega|^2/2)
    = omega.S.omega - nu |grad omega|_F^2.

At a spatial critical point the advection face vanishes.  At a local maximum the
curvature face nu Delta e is nonpositive, so positive time growth requires positive
stretching-minus-Kelvin-bulk margin.  This is a necessary instantaneous growth gate,
not a continuation-failure theorem.
"""
from __future__ import annotations

from collections.abc import Sequence
import sympy as sp

from .first_bad_candidate_exclusions import (
    abc_pressure,
    abc_velocity,
    curl3,
    gradient,
    laplacian,
    navier_stokes_residual,
)
from .kelvin_packet_locality import (
    affine_vortex_stretch_gradient,
    affine_vortex_stretch_ns_residual,
    affine_vortex_stretch_vorticity,
)
from .orientation_packet import metric_bulk_reconstruction_residual

Matrix = sp.MatrixBase


def strain_from_gradient(grad_u: Matrix) -> Matrix:
    return sp.simplify((grad_u+grad_u.T)/2)


def enstrophy_density(omega: Matrix) -> sp.Expr:
    return sp.simplify(omega.dot(omega)/2)


def vorticity_equation_residual(
    velocity: Matrix,
    omega: Matrix,
    coords: Sequence[sp.Symbol],
    time: sp.Symbol,
    nu: sp.Expr,
) -> Matrix:
    """Residual omega_t+(u.grad)omega-(omega.grad)u-nu Delta omega."""
    Gu=gradient(velocity,coords)
    Go=gradient(omega,coords)
    return sp.simplify(
        sp.diff(omega,time)+Go*velocity-Gu*omega-nu*laplacian(omega,coords)
    )


def enstrophy_balance_faces(
    velocity: Matrix,
    omega: Matrix,
    coords: Sequence[sp.Symbol],
    time: sp.Symbol,
    nu: sp.Expr,
) -> dict[str,sp.Expr|Matrix]:
    """Return literal time/advection/stretch/Kelvin-bulk/curvature faces."""
    Gu=gradient(velocity,coords)
    Go=gradient(omega,coords)
    S=strain_from_gradient(Gu)
    e=enstrophy_density(omega)
    grad_e=sp.Matrix([sp.diff(e,q) for q in coords])
    lap_e=sp.simplify(sum(sp.diff(e,q,2) for q in coords))
    time_face=sp.simplify(sp.diff(e,time))
    advection=sp.simplify((grad_e.T*velocity)[0])
    stretching=sp.simplify((omega.T*S*omega)[0])
    bulk=sp.simplify(nu*sum(Go[i,j]**2 for i in range(Go.rows) for j in range(Go.cols)))
    curvature=sp.simplify(nu*lap_e)
    residual=sp.simplify(time_face+advection-stretching+bulk-curvature)
    vort_res=vorticity_equation_residual(velocity,omega,coords,time,nu)
    contraction=sp.simplify((omega.T*vort_res)[0])
    return {
        "enstrophy":e,
        "gradient":sp.simplify(grad_e),
        "laplacian":lap_e,
        "time":time_face,
        "advection":advection,
        "stretching":stretching,
        "kelvin_bulk":bulk,
        "curvature_diffusion":curvature,
        "balance_residual":residual,
        "vorticity_residual_contraction":contraction,
        "balance_minus_vorticity_contraction":sp.simplify(residual-contraction),
    }


def critical_point_growth_residual(
    time_derivative: sp.Expr,
    stretching: sp.Expr,
    kelvin_bulk: sp.Expr,
    laplacian_enstrophy: sp.Expr,
    nu: sp.Expr,
) -> sp.Expr:
    """Residual e_t-[stretch-bulk+nu Delta e] at grad e=0."""
    return sp.simplify(time_derivative-(stretching-kelvin_bulk+nu*laplacian_enstrophy))


def growth_gate_margin(stretching: sp.Expr, kelvin_bulk: sp.Expr) -> sp.Expr:
    return sp.simplify(stretching-kelvin_bulk)


def kelvin_bulk_packet_residual(
    grad_omega: Matrix,
    area_frame: Matrix,
    nu: sp.Expr,
) -> sp.Expr:
    """Metric-normalized orientation-complete Kelvin q.v. bulk minus nu|grad omega|^2."""
    return metric_bulk_reconstruction_residual(grad_omega,area_frame,nu)


def abc_beltrami_enstrophy_stretching_calibration(
    amplitude: sp.Expr,
    nu: sp.Expr,
    time: sp.Symbol,
    coords: Sequence[sp.Symbol],
) -> dict[str,sp.Expr|Matrix]:
    """Global ABC identity: at every enstrophy critical point stretching is zero."""
    u=abc_velocity(amplitude,nu,time,coords)
    omega=curl3(u,coords)
    e=enstrophy_density(omega)
    grad_e=sp.Matrix([sp.diff(e,q) for q in coords])
    S=strain_from_gradient(gradient(u,coords))
    stretching=sp.simplify((omega.T*S*omega)[0])
    transport=sp.simplify((u.T*grad_e)[0])
    p=abc_pressure(u)
    return {
        "beltrami_residual":sp.simplify(sp.trigsimp(omega-u)),
        "stretching":sp.simplify(sp.trigsimp(stretching)),
        "enstrophy_gradient":sp.simplify(sp.trigsimp(grad_e)),
        "stretching_minus_enstrophy_transport":sp.simplify(sp.trigsimp(stretching-transport)),
        "ns_residual":sp.simplify(sp.trigsimp(navier_stokes_residual(u,p,coords,time,nu))),
    }


def affine_vortex_local_growth_calibration(
    a: sp.Expr,
    r0: sp.Expr,
    time: sp.Symbol,
    coords: tuple[sp.Symbol,sp.Symbol,sp.Symbol],
    nu: sp.Expr,
) -> dict[str,sp.Expr|Matrix]:
    """Exact affine NS mechanism: spatially uniform enstrophy grows by stretching alone.

    This is a local mechanism calibration, not a periodic/finite-energy target-class
    counterexample.
    """
    A=affine_vortex_stretch_gradient(a,r0,time)
    xvec=sp.Matrix(coords)
    u=sp.simplify(A*xvec)
    omega=affine_vortex_stretch_vorticity(a,r0,time)
    faces=enstrophy_balance_faces(u,omega,coords,time,nu)
    ns_res,p=affine_vortex_stretch_ns_residual(a,r0,time,coords,nu)
    shift=sp.Matrix([2*sp.pi,0,0])
    periodicity_defect=sp.simplify(A*shift)
    return {
        **faces,
        "velocity":u,
        "vorticity":omega,
        "ns_residual":ns_res,
        "pressure":p,
        "periodicity_defect_x_2pi":periodicity_defect,
    }
