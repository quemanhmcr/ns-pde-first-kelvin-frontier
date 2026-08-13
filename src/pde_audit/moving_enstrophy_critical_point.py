"""Exact motion law for a differentiable nondegenerate enstrophy critical point.

If x_*(t) satisfies grad e(x_*(t),t)=0, differentiating the constraint gives

    Hess(e) xdot_* + grad(partial_t e) = 0.

Using the exact NS critical-point growth law

    partial_t e = -u.grad e + G + nu Delta e,
    G = omega.S.omega - nu |grad omega|^2,

and grad e=0 yields

    Hess(e)(xdot_*-u) + grad(G + nu Delta e) = 0.

For invertible Hessian this determines the critical-point velocity.  Degenerate
critical sets need not have a unique speed; the exact affine vortex provides a
Navier--Stokes calibration where Hess(e)=0 and every spatial path stays critical.
"""
from __future__ import annotations

from collections.abc import Sequence
import sympy as sp

from .first_bad_candidate_exclusions import abc_velocity, curl3, gradient
from .kelvin_packet_locality import affine_vortex_stretch_gradient, affine_vortex_stretch_vorticity
from .local_enstrophy_kelvin_growth_gate import enstrophy_balance_faces, enstrophy_density

Matrix = sp.MatrixBase


def scalar_hessian(scalar: sp.Expr, coords: Sequence[sp.Symbol]) -> Matrix:
    return sp.hessian(scalar,coords)


def critical_path_value_derivative_residual(
    total_derivative: sp.Expr,
    partial_time_derivative: sp.Expr,
    gradient_scalar: Matrix,
    critical_velocity: Matrix,
) -> sp.Expr:
    """Residual d/dt f(x_*(t),t)-[f_t+grad f . xdot]."""
    if gradient_scalar.shape != critical_velocity.shape or gradient_scalar.cols != 1:
        raise ValueError("gradient and critical velocity must be equal-size columns")
    return sp.simplify(total_derivative-partial_time_derivative-(gradient_scalar.T*critical_velocity)[0])


def scalar_critical_constraint_speed_residual_at(
    scalar: sp.Expr,
    coords: Sequence[sp.Symbol],
    time: sp.Symbol,
    point: dict[sp.Symbol,sp.Expr],
    critical_velocity: Matrix,
) -> Matrix:
    """Residual Hess(f) xdot + partial_t grad f at a supplied critical point."""
    H=sp.simplify(sp.trigsimp(sp.hessian(scalar,coords).subs(point)))
    grad_f=sp.Matrix([sp.diff(scalar,q) for q in coords])
    grad_ft=sp.simplify(sp.trigsimp(sp.diff(grad_f,time).subs(point)))
    return sp.simplify(H*critical_velocity+grad_ft)


def nondegenerate_scalar_critical_velocity_at(
    scalar: sp.Expr,
    coords: Sequence[sp.Symbol],
    time: sp.Symbol,
    point: dict[sp.Symbol,sp.Expr],
) -> Matrix:
    """xdot=-Hess(f)^-1 partial_t grad f for a nondegenerate critical branch."""
    H=sp.simplify(sp.trigsimp(sp.hessian(scalar,coords).subs(point)))
    if sp.simplify(H.det()) == 0:
        raise ValueError("critical Hessian is singular; no unique critical speed")
    grad_f=sp.Matrix([sp.diff(scalar,q) for q in coords])
    grad_ft=sp.simplify(sp.trigsimp(sp.diff(grad_f,time).subs(point)))
    return sp.simplify(-H.inv()*grad_ft)


def critical_growth_spatial_gradient(
    velocity: Matrix,
    omega: Matrix,
    coords: Sequence[sp.Symbol],
    time: sp.Symbol,
    nu: sp.Expr,
) -> tuple[sp.Expr,Matrix]:
    """R=stretching-Kelvin_bulk+nu Delta e and grad R."""
    faces=enstrophy_balance_faces(velocity,omega,coords,time,nu)
    R=sp.simplify(faces["stretching"]-faces["kelvin_bulk"]+faces["curvature_diffusion"])
    gradR=sp.simplify(sp.Matrix([sp.diff(R,q) for q in coords]))
    return R,gradR


def critical_point_speed_residual(
    velocity: Matrix,
    omega: Matrix,
    coords: Sequence[sp.Symbol],
    time: sp.Symbol,
    nu: sp.Expr,
    critical_velocity: Matrix,
) -> Matrix:
    """H_e(xdot-u)+grad(stretch-bulk+nu Delta e), evaluated before substitution."""
    if critical_velocity.shape != velocity.shape:
        raise ValueError("critical velocity and fluid velocity dimensions must match")
    e=enstrophy_density(omega)
    H=scalar_hessian(e,coords)
    _,gradR=critical_growth_spatial_gradient(velocity,omega,coords,time,nu)
    return sp.simplify(H*(critical_velocity-velocity)+gradR)


def nondegenerate_critical_velocity(
    velocity: Matrix,
    omega: Matrix,
    coords: Sequence[sp.Symbol],
    time: sp.Symbol,
    nu: sp.Expr,
) -> Matrix:
    """xdot=u-H_e^{-1} grad R; valid only where Hessian is invertible and grad e=0."""
    e=enstrophy_density(omega)
    H=scalar_hessian(e,coords)
    if sp.simplify(H.det()) == 0:
        raise ValueError("critical Hessian is singular; no unique inverse-Hessian speed")
    _,gradR=critical_growth_spatial_gradient(velocity,omega,coords,time,nu)
    return sp.simplify(velocity-H.inv()*gradR)


def nondegenerate_critical_velocity_at(
    velocity: Matrix,
    omega: Matrix,
    coords: Sequence[sp.Symbol],
    time: sp.Symbol,
    nu: sp.Expr,
    point: dict[sp.Symbol,sp.Expr],
) -> Matrix:
    """Local version: substitute the critical point before Hessian inversion."""
    e=enstrophy_density(omega)
    H=sp.simplify(sp.trigsimp(scalar_hessian(e,coords).subs(point)))
    if sp.simplify(H.det()) == 0:
        raise ValueError("critical Hessian is singular; no unique inverse-Hessian speed")
    _,gradR=critical_growth_spatial_gradient(velocity,omega,coords,time,nu)
    gradR0=sp.simplify(sp.trigsimp(gradR.subs(point)))
    u0=sp.simplify(sp.trigsimp(velocity.subs(point)))
    return sp.simplify(sp.trigsimp(u0-H.inv()*gradR0))


def critical_relative_velocity_faces_at(
    velocity: Matrix,
    omega: Matrix,
    coords: Sequence[sp.Symbol],
    time: sp.Symbol,
    nu: sp.Expr,
    point: dict[sp.Symbol,sp.Expr],
) -> tuple[Matrix,Matrix,Matrix]:
    """Local physical faces; substitute before inverse-Hessian contraction."""
    e=enstrophy_density(omega)
    H=sp.simplify(sp.trigsimp(scalar_hessian(e,coords).subs(point)))
    if sp.simplify(H.det()) == 0:
        raise ValueError("critical Hessian is singular; no unique inverse-Hessian speed")
    faces=enstrophy_balance_faces(velocity,omega,coords,time,nu)
    grad_stretch=sp.Matrix([sp.diff(faces["stretching"],q) for q in coords])
    grad_bulk=sp.Matrix([sp.diff(faces["kelvin_bulk"],q) for q in coords])
    grad_lap=sp.Matrix([sp.diff(faces["laplacian"],q) for q in coords])
    gs=sp.simplify(sp.trigsimp(grad_stretch.subs(point)))
    gb=sp.simplify(sp.trigsimp(grad_bulk.subs(point)))
    gl=sp.simplify(sp.trigsimp(grad_lap.subs(point)))
    return (
        sp.simplify(-H.inv()*gs),
        sp.simplify(H.inv()*gb),
        sp.simplify(-nu*H.inv()*gl),
    )


def critical_relative_velocity_faces(
    velocity: Matrix,
    omega: Matrix,
    coords: Sequence[sp.Symbol],
    time: sp.Symbol,
    nu: sp.Expr,
) -> tuple[Matrix,Matrix,Matrix]:
    """Relative speed faces from stretching, Kelvin bulk, and curvature gradients."""
    e=enstrophy_density(omega)
    H=scalar_hessian(e,coords)
    if sp.simplify(H.det()) == 0:
        raise ValueError("critical Hessian is singular; no unique inverse-Hessian speed")
    faces=enstrophy_balance_faces(velocity,omega,coords,time,nu)
    grad_stretch=sp.Matrix([sp.diff(faces["stretching"],q) for q in coords])
    grad_bulk=sp.Matrix([sp.diff(faces["kelvin_bulk"],q) for q in coords])
    grad_lap=sp.Matrix([sp.diff(faces["laplacian"],q) for q in coords])
    stretch_face=sp.simplify(-H.inv()*grad_stretch)
    bulk_face=sp.simplify(H.inv()*grad_bulk)
    curvature_face=sp.simplify(-nu*H.inv()*grad_lap)
    return stretch_face,bulk_face,curvature_face


def abc_fixed_critical_point_speed_calibration(
    amplitude: sp.Expr,
    nu: sp.Expr,
    time: sp.Symbol,
    coords: tuple[sp.Symbol,sp.Symbol,sp.Symbol],
) -> dict[str,sp.Expr|Matrix]:
    """Exact periodic ABC strict maximum is fixed although the fluid velocity is nonzero."""
    u=abc_velocity(amplitude,nu,time,coords)
    omega=curl3(u,coords)
    e=enstrophy_density(omega)
    H=scalar_hessian(e,coords)
    grad_e=sp.Matrix([sp.diff(e,q) for q in coords])
    point={q:sp.pi/4 for q in coords}
    H0=sp.simplify(sp.trigsimp(H.subs(point)))
    u0=sp.simplify(sp.trigsimp(u.subs(point)))
    grad0=sp.simplify(sp.trigsimp(grad_e.subs(point)))
    grad_et0=sp.simplify(sp.trigsimp(sp.diff(grad_e,time).subs(point)))
    xdot0=sp.zeros(3,1)
    predicted=nondegenerate_scalar_critical_velocity_at(e,coords,time,point)
    constraint_res=scalar_critical_constraint_speed_residual_at(e,coords,time,point,xdot0)
    # From the exact enstrophy PDE at grad e=0: grad R = grad e_t + H u.
    growth_gradient=sp.simplify(grad_et0+H0*u0)
    pde_speed_res=sp.simplify(H0*(xdot0-u0)+growth_gradient)
    relative=sp.simplify(-H0.inv()*growth_gradient)
    return {
        "point":sp.Matrix([sp.pi/4]*3),
        "gradient":grad0,
        "gradient_time_derivative":grad_et0,
        "hessian":H0,
        "hessian_det":sp.factor(H0.det()),
        "fluid_velocity":u0,
        "critical_velocity":xdot0,
        "predicted_critical_velocity":predicted,
        "relative_velocity":relative,
        "growth_gradient":growth_gradient,
        "constraint_speed_residual":constraint_res,
        "pde_speed_residual":pde_speed_res,
    }


def affine_degenerate_critical_speed_calibration(
    a: sp.Expr,
    r0: sp.Expr,
    time: sp.Symbol,
    coords: tuple[sp.Symbol,sp.Symbol,sp.Symbol],
    nu: sp.Expr,
) -> dict[str,sp.Expr|Matrix]:
    """Uniform-enstrophy affine NS: Hessian and growth gradient vanish, speed is undetermined."""
    A=affine_vortex_stretch_gradient(a,r0,time)
    u=sp.simplify(A*sp.Matrix(coords))
    omega=affine_vortex_stretch_vorticity(a,r0,time)
    e=enstrophy_density(omega)
    H=scalar_hessian(e,coords)
    grad_e=sp.Matrix([sp.diff(e,q) for q in coords])
    _,gradR=critical_growth_spatial_gradient(u,omega,coords,time,nu)
    v1=sp.Matrix([1,0,0])
    v2=sp.Matrix([0,2,-1])
    return {
        "gradient":sp.simplify(grad_e),
        "hessian":sp.simplify(H),
        "growth_gradient":sp.simplify(gradR),
        "speed_residual_v1":sp.simplify(H*(v1-u)+gradR),
        "speed_residual_v2":sp.simplify(H*(v2-u)+gradR),
    }
