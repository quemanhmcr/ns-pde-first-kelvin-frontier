"""Exact Navier--Stokes calibrations for intrinsic curvature--support grammar."""
from __future__ import annotations
import sympy as sp
from .first_bad_candidate_exclusions import gradient
from .local_enstrophy_kelvin_growth_gate import enstrophy_balance_faces
from .intrinsic_curvature_support_grammar import (
    critical_curvature_covariant_residual_at,
    intrinsic_curvature_tensor,
    kernel_normalization_face_residual,
    kernel_quadratic_opening,
    normalized_source_curvature_tensor,
)
Matrix = sp.MatrixBase

def three_mode_kernel_birth_velocity_scalar(z, time, nu):
    s = nu * time
    return sp.simplify(5*sp.exp(1-s)*sp.sin(z)+sp.Rational(1,2)*sp.exp(4-4*s)*sp.sin(2*z)-sp.Rational(1,3)*sp.exp(9-9*s)*sp.sin(3*z))

def three_mode_kernel_birth_vorticity_scalar(z, time, nu):
    return sp.simplify(sp.diff(three_mode_kernel_birth_velocity_scalar(z,time,nu),z))

def three_mode_kernel_birth_velocity(coords, time, nu):
    _,_,z=coords
    return sp.Matrix([three_mode_kernel_birth_velocity_scalar(z,time,nu),0,0])

def three_mode_kernel_birth_ns_residual(coords, time, nu):
    u=three_mode_kernel_birth_velocity(coords,time,nu)
    A=gradient(u,coords)
    adv=sp.simplify(A*u)
    lap=sp.Matrix([sum(sp.diff(u[i],q,2) for q in coords) for i in range(3)])
    return sp.simplify(sp.diff(u,time)+adv-nu*lap)

def three_mode_kernel_birth_global_polynomial(cosine):
    c=cosine
    return sp.expand(-4*c**3+2*c**2+8*c-1)

def three_mode_kernel_birth_global_certificate(cosine):
    c=cosine
    q=three_mode_kernel_birth_global_polynomial(c)
    return {"q":q,"upper_factor":sp.factor(5-q),"derivative_factor":sp.factor(sp.diff(q,c)),"value_at_one":sp.simplify(q.subs(c,1)),"value_at_minus_one":sp.simplify(q.subs(c,-1)),"value_at_internal_critical":sp.simplify(q.subs(c,sp.Rational(-2,3))),"lower_margin_at_internal_critical":sp.simplify(5+q.subs(c,sp.Rational(-2,3)))}

def three_mode_kernel_birth_calibration(coords,time,nu):
    x,y,z=coords
    T=sp.simplify(1/nu)
    u=three_mode_kernel_birth_velocity(coords,time,nu)
    q=three_mode_kernel_birth_vorticity_scalar(z,time,nu)
    omega=sp.Matrix([0,q,0])
    faces=enstrophy_balance_faces(u,omega,coords,time,nu)
    e=sp.simplify(faces["enstrophy"])
    M=sp.Rational(25,2)
    point={x:0,y:0,z:0,time:T}
    max_rate=sp.simplify(sp.diff(e,time).subs(point))
    g=sp.simplify(e/M)
    R=sp.simplify(faces["stretching"]-faces["kelvin_bulk"]+faces["curvature_diffusion"])
    Phi=sp.simplify(R/M-(max_rate/M)*g)
    Q=intrinsic_curvature_tensor(g,coords)
    K=normalized_source_curvature_tensor(Phi,coords)
    Q0=sp.simplify(sp.trigsimp(Q.subs(point)))
    K0=sp.simplify(sp.trigsimp(K.subs(point)))
    stretch_K=sp.simplify(-sp.hessian(faces["stretching"]/M,coords).subs(point))
    bulk_K=sp.simplify(sp.hessian(faces["kelvin_bulk"]/M,coords).subs(point))
    curvature_K=sp.simplify(-sp.hessian(faces["curvature_diffusion"]/M,coords).subs(point))
    zdir=sp.Matrix([0,0,1])
    raw_growth_hessian=sp.simplify(sp.hessian(R,coords).subs(point))
    return {
        "time":T,"velocity":u,"vorticity":omega,"enstrophy":e,"max_enstrophy":M,"max_rate":max_rate,
        "normalized_enstrophy_event":sp.simplify(g.subs(time,T)),"normalized_source_event":sp.simplify(Phi.subs(time,T)),
        "curvature":Q0,"source_curvature":K0,"stretch_source_curvature":stretch_K,
        "kelvin_bulk_source_curvature":bulk_K,"curvature_diffusion_source_curvature":curvature_K,
        "source_face_residual":sp.simplify(K0-stretch_K-bulk_K-curvature_K),
        "quartic_enstrophy_derivative":sp.simplify(sp.diff(e,z,4).subs(point)),
        "z_curvature_opening_rate":sp.simplify(-sp.diff(sp.diff(e,z,2),time).subs(point)/M),
        "z_kernel_opening":kernel_quadratic_opening(K0,zdir),
        "kernel_normalization_residual":kernel_normalization_face_residual(raw_growth_hessian,Q0,M,max_rate,zdir,K0),
        "covariant_residual":critical_curvature_covariant_residual_at(g,Phi,u,coords,time,point),
        "ns_residual":three_mode_kernel_birth_ns_residual(coords,time,nu),
        "enstrophy_balance_residual":sp.simplify(sp.trigsimp(faces["balance_residual"])),
    }
