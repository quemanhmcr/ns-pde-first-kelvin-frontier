"""Exact Hessian evolution along a moving scalar critical branch.

For a scalar e satisfying

    e_t + u.grad e = R,

and a differentiable critical path grad e(x_*,t)=0, the Hessian H=Hess(e) obeys

    d_* H
      = Hess(R) - (grad u)^T H - H grad u
        + ((xdot_*-u).grad) H.

For enstrophy, R is exactly stretching - Kelvin_bulk + nu Delta e.
The local linear-deformation face has log-determinant contribution -2 div u, hence
vanishes identically for incompressible Navier--Stokes.
"""
from __future__ import annotations

from collections.abc import Sequence
import sympy as sp

from .first_bad_candidate_exclusions import abc_velocity, gradient
from .moving_enstrophy_critical_point import abc_fixed_critical_point_speed_calibration

Matrix = sp.MatrixBase


def directional_matrix_derivative(
    matrix_field: Matrix,
    direction: Matrix,
    coords: Sequence[sp.Symbol],
) -> Matrix:
    if direction.shape != (len(coords),1):
        raise ValueError("direction must match coordinate dimension")
    out=sp.zeros(matrix_field.rows,matrix_field.cols)
    for k,q in enumerate(coords):
        out += direction[k]*matrix_field.diff(q)
    return sp.simplify(out)


def critical_hessian_evolution_faces_at(
    scalar: sp.Expr,
    velocity: Matrix,
    source: sp.Expr,
    coords: Sequence[sp.Symbol],
    time: sp.Symbol,
    point: dict[sp.Symbol,sp.Expr],
    critical_velocity: Matrix,
) -> dict[str,Matrix]:
    """Exact local faces for e_t+u.grad e=R, evaluated at a critical point."""
    H=sp.hessian(scalar,coords)
    Gu=gradient(velocity,coords)
    HessR=sp.hessian(source,coords)
    Hdot_path=sp.diff(H,time)+directional_matrix_derivative(H,critical_velocity,coords)
    connection=sp.simplify(-(Gu.T*H+H*Gu))
    relative=directional_matrix_derivative(H,sp.simplify(critical_velocity-velocity),coords)
    def at(M: Matrix) -> Matrix:
        return sp.simplify(sp.trigsimp(M.subs(point)))
    H0=at(H)
    Hdot0=at(Hdot_path)
    growth0=at(HessR)
    connection0=at(connection)
    relative0=at(relative)
    return {
        "hessian":H0,
        "path_derivative":Hdot0,
        "growth_hessian":growth0,
        "connection":connection0,
        "relative_transport":relative0,
        "residual":sp.simplify(Hdot0-growth0-connection0-relative0),
    }


def hessian_connection_strain_rotation_faces(grad_u: Matrix,hessian: Matrix) -> tuple[Matrix,Matrix]:
    """Connection split: -(S H+H S) + (W H-H W)."""
    if grad_u.shape != hessian.shape or hessian.rows != hessian.cols:
        raise ValueError("gradient and Hessian dimensions must match")
    S=sp.simplify((grad_u+grad_u.T)/2)
    W=sp.simplify((grad_u-grad_u.T)/2)
    strain=sp.simplify(-(S*hessian+hessian*S))
    rotation=sp.simplify(W*hessian-hessian*W)
    return strain,rotation


def hessian_connection_strain_rotation_residual(grad_u: Matrix,hessian: Matrix) -> Matrix:
    strain,rotation=hessian_connection_strain_rotation_faces(grad_u,hessian)
    connection=sp.simplify(-(grad_u.T*hessian+hessian*grad_u))
    return sp.simplify(connection-strain-rotation)


def hessian_strain_rotation_logdet_rates(grad_u: Matrix,hessian: Matrix) -> tuple[sp.Expr,sp.Expr]:
    if sp.simplify(hessian.det()) == 0:
        raise ValueError("Hessian is singular; log-determinant rate undefined")
    strain,rotation=hessian_connection_strain_rotation_faces(grad_u,hessian)
    Hinv=hessian.inv()
    return (
        sp.simplify(sp.trace(Hinv*strain)),
        sp.simplify(sp.trace(Hinv*rotation)),
    )


def hessian_connection_logdet_rate(grad_u: Matrix, hessian: Matrix) -> sp.Expr:
    """tr(H^-1[-Gu^T H-H Gu]); H must be invertible."""
    if hessian.rows != hessian.cols or grad_u.shape != hessian.shape:
        raise ValueError("gradient and Hessian dimensions must match")
    if sp.simplify(hessian.det()) == 0:
        raise ValueError("Hessian is singular; log-determinant rate undefined")
    connection=sp.simplify(-(grad_u.T*hessian+hessian*grad_u))
    return sp.simplify(sp.trace(hessian.inv()*connection))


def hessian_connection_logdet_divergence_residual(grad_u: Matrix,hessian: Matrix) -> sp.Expr:
    """Exact residual connection logdet rate + 2 div u."""
    return sp.simplify(hessian_connection_logdet_rate(grad_u,hessian)+2*sp.trace(grad_u))


def hessian_logdet_rate(hessian: Matrix,hessian_dot: Matrix) -> sp.Expr:
    if hessian.shape != hessian_dot.shape or hessian.rows != hessian.cols:
        raise ValueError("Hessian and derivative dimensions must match")
    if sp.simplify(hessian.det()) == 0:
        raise ValueError("Hessian is singular; log-determinant rate undefined")
    return sp.simplify(sp.trace(hessian.inv()*hessian_dot))


def determinant_jacobi_residual(hessian: Matrix,hessian_dot: Matrix,det_dot: sp.Expr) -> sp.Expr:
    """Residual detdot-det(H) tr(H^-1 Hdot)."""
    return sp.simplify(det_dot-sp.det(hessian)*hessian_logdet_rate(hessian,hessian_dot))


def hessian_logdet_face_rates(faces: dict[str,Matrix]) -> dict[str,sp.Expr]:
    """Trace H^-1 against growth/connection/relative Hessian-evolution faces."""
    H=faces["hessian"]
    if sp.simplify(H.det()) == 0:
        raise ValueError("Hessian is singular; face log-determinant rates undefined")
    return {
        "total":hessian_logdet_rate(H,faces["path_derivative"]),
        "growth":sp.simplify(sp.trace(H.inv()*faces["growth_hessian"])),
        "connection":sp.simplify(sp.trace(H.inv()*faces["connection"])),
        "relative":sp.simplify(sp.trace(H.inv()*faces["relative_transport"])),
    }


def nonzero_determinant_from_lograte(det_initial: sp.Expr,integrated_lograte: sp.Expr) -> sp.Expr:
    """Exact branch formula det H(t)=det H(t0) exp(int tr(H^-1 Hdot))."""
    return sp.simplify(det_initial*sp.exp(integrated_lograte))


def abc_hessian_logdet_calibration(
    amplitude: sp.Expr,
    nu: sp.Expr,
    time: sp.Symbol,
    coords: tuple[sp.Symbol,sp.Symbol,sp.Symbol],
) -> dict[str,sp.Expr|Matrix]:
    """Exact periodic ABC fixed strict maximum: Hdot=-2nu H and log|det H| rate=-6nu."""
    c=abc_fixed_critical_point_speed_calibration(amplitude,nu,time,coords)
    H=c["hessian"]
    Hdot=sp.simplify(sp.diff(H,time))
    detH=sp.simplify(H.det())
    detdot=sp.simplify(sp.diff(detH,time))
    u=abc_velocity(amplitude,nu,time,coords)
    point={q:sp.pi/4 for q in coords}
    Gu0=sp.simplify(sp.trigsimp(gradient(u,coords).subs(point)))
    return {
        "hessian":H,
        "hessian_dot":Hdot,
        "hessian_dot_plus_2nu_hessian":sp.simplify(Hdot+2*nu*H),
        "determinant":detH,
        "determinant_dot":detdot,
        "logdet_rate":hessian_logdet_rate(H,Hdot),
        "jacobi_residual":determinant_jacobi_residual(H,Hdot,detdot),
        "grad_u":Gu0,
        "divergence":sp.simplify(sp.trace(Gu0)),
        "connection_logdet_rate":hessian_connection_logdet_rate(Gu0,H),
        "connection_divergence_residual":hessian_connection_logdet_divergence_residual(Gu0,H),
    }
