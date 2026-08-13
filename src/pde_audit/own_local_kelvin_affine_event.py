"""Exact own-local affine Kelvin residual event algebra.

The old frame-aware A/B synthesis is exact for a common local target.  Packet-specific
anchors add an exact target/reanchoring coboundary.  This module keeps the current,
frame, target, selector, and Brownian-source faces separate before any estimate.
"""
from __future__ import annotations
from collections.abc import Sequence
import sympy as sp
from .codeforming_surface_moment_tower import cofactor_map
from .frame_aware_kelvin_residual_refinement import (
    codeforming_synthesis_map, compatible_parent_packet,
    frame_aware_physical_synthesis_map, raw_orientation_error,
)
Matrix = sp.MatrixBase


def own_local_target_face(child_frames: Sequence[Matrix], raw_blocks: Sequence[Matrix],
                          child_targets: Sequence[Matrix], parent_target: Matrix) -> Matrix:
    if not child_frames or not (len(child_frames) == len(raw_blocks) == len(child_targets)):
        raise ValueError("matching nonempty child frame/block/target data required")
    d = parent_target.rows
    out = sp.zeros(d, 1)
    for H, R, w in zip(child_frames, raw_blocks, child_targets):
        if H.shape != (d,d) or R.shape != (d,d) or w.shape != (d,1):
            raise ValueError("own-local packet dimensions must agree")
        out += R * H.T * (w - parent_target)
    return sp.simplify(out)


def own_local_raw_error_refinement_residual(child_circulations: Sequence[Matrix],
        child_frames: Sequence[Matrix], raw_blocks: Sequence[Matrix],
        child_targets: Sequence[Matrix], parent_target: Matrix) -> Matrix:
    Kp, Hp = compatible_parent_packet(child_circulations, child_frames, raw_blocks)
    lhs = raw_orientation_error(Kp, Hp, parent_target)
    rhs = sp.zeros(parent_target.rows, 1)
    for K, H, R, w in zip(child_circulations, child_frames, raw_blocks, child_targets):
        rhs += R * raw_orientation_error(K, H, w)
    rhs += own_local_target_face(child_frames, raw_blocks, child_targets, parent_target)
    return sp.simplify(lhs-rhs)


def own_local_physical_affine_data(parent_frame: Matrix, child_frames: Sequence[Matrix],
        raw_blocks: Sequence[Matrix], child_targets: Sequence[Matrix],
        parent_target: Matrix) -> tuple[Matrix,Matrix]:
    A = frame_aware_physical_synthesis_map(parent_frame, child_frames, raw_blocks)
    delta = own_local_target_face(child_frames, raw_blocks, child_targets, parent_target)
    return A, sp.simplify(parent_frame.inv().T * delta)


def own_local_physical_refinement_residual(child_circulations: Sequence[Matrix],
        child_frames: Sequence[Matrix], raw_blocks: Sequence[Matrix],
        child_targets: Sequence[Matrix], parent_target: Matrix) -> Matrix:
    Kp, Hp = compatible_parent_packet(child_circulations, child_frames, raw_blocks)
    rp = sp.simplify(Hp.inv().T * raw_orientation_error(Kp, Hp, parent_target))
    child_r = [sp.simplify(H.inv().T*raw_orientation_error(K,H,w))
               for K,H,w in zip(child_circulations, child_frames, child_targets)]
    A,d = own_local_physical_affine_data(Hp, child_frames, raw_blocks, child_targets, parent_target)
    return sp.simplify(rp - A*sp.Matrix.vstack(*child_r) - d)


def own_local_codeforming_affine_data(parent_line_frame: Matrix,
        child_line_frames: Sequence[Matrix], raw_blocks: Sequence[Matrix],
        child_targets: Sequence[Matrix], parent_target: Matrix) -> tuple[Matrix,Matrix]:
    child_H = [cofactor_map(L) for L in child_line_frames]
    B = codeforming_synthesis_map(parent_line_frame, child_line_frames, raw_blocks)
    delta = own_local_target_face(child_H, raw_blocks, child_targets, parent_target)
    return B, sp.simplify(delta/sp.det(parent_line_frame))


def affine_target_coboundary(A: Matrix, omega_before: Matrix, omega_after: Matrix) -> Matrix:
    return sp.simplify(A*omega_before - omega_after)


def affine_composition_residuals(A1: Matrix, A2: Matrix, omega0: Matrix,
        omega1: Matrix, omega2: Matrix, x0: Matrix) -> tuple[Matrix,Matrix]:
    d1 = affine_target_coboundary(A1, omega0, omega1)
    d2 = affine_target_coboundary(A2, omega1, omega2)
    A20 = sp.simplify(A2*A1)
    d20 = affine_target_coboundary(A20, omega0, omega2)
    sequential = sp.simplify(A2*(A1*x0+d1)+d2)
    direct = sp.simplify(A20*x0+d20)
    return sp.simplify(sequential-direct), sp.simplify(A2*d1+d2-d20)


def affine_pathwise_second_moment_residual(A: Matrix, x: Matrix, d: Matrix) -> Matrix:
    y = sp.simplify(A*x+d); Q = sp.simplify(x*x.T)
    rhs = sp.simplify(A*Q*A.T + A*x*d.T + d*x.T*A.T + d*d.T)
    return sp.simplify(y*y.T-rhs)


def selected_affine_jump(x: Matrix, A: Matrix, d: Matrix, Eminus: Matrix, Eplus: Matrix) -> Matrix:
    return sp.simplify((Eplus*A-Eminus)*x + Eplus*d)


def selected_affine_jump_square_residual(x: Matrix, A: Matrix, d: Matrix,
        Eminus: Matrix, Eplus: Matrix) -> Matrix:
    D = sp.simplify(Eplus*A-Eminus); b = sp.simplify(Eplus*d); Q = sp.simplify(x*x.T)
    jump = sp.simplify(D*x+b)
    rhs = sp.simplify(D*Q*D.T + D*x*b.T + b*x.T*D.T + b*b.T)
    return sp.simplify(jump*jump.T-rhs)


def target_gradient_coboundary(A: Matrix, Gminus: Matrix, Gplus: Matrix) -> Matrix:
    return sp.simplify(A*Gminus-Gplus)


def affine_noise_response(A: Matrix, Nminus: Matrix, Gminus: Matrix, Gplus: Matrix) -> Matrix:
    return sp.simplify(A*Nminus + target_gradient_coboundary(A,Gminus,Gplus))


def affine_noise_gram_residual(A: Matrix, Nminus: Matrix, Gminus: Matrix, Gplus: Matrix) -> Matrix:
    Nt = target_gradient_coboundary(A,Gminus,Gplus)
    Np = affine_noise_response(A,Nminus,Gminus,Gplus)
    rhs = sp.simplify(A*Nminus*Nminus.T*A.T + A*Nminus*Nt.T + Nt*Nminus.T*A.T + Nt*Nt.T)
    return sp.simplify(Np*Np.T-rhs)


def cubic_heat_shear_reanchoring_calibration(anchor: sp.Expr, target: sp.Expr,
        half_width: sp.Expr, x_length: sp.Expr, time: sp.Expr, nu: sp.Expr) -> dict[str,sp.Expr]:
    a,p,b,ell,t = anchor,target,half_width,x_length,time
    K = sp.simplify(2*b*ell*(-3*a**2-b**2-6*nu*t)); H = sp.simplify(2*b*ell)
    omega = sp.simplify(-(3*p**2+6*nu*t)); eps = sp.simplify(K-H*omega)
    q = sp.simplify(-12*a*b*ell + 12*b*ell*p)
    y = sp.symbols('y', real=True); U = y**3+6*nu*t*y
    return {"circulation":K, "area":H, "raw_error":eps, "residual_noise_y":q,
            "heat_equation_residual":sp.simplify(sp.diff(U,t)-nu*sp.diff(U,y,2))}


def cubic_two_child_own_local_mismatch(center: sp.Expr, half_width: sp.Expr,
        x_length: sp.Expr, time: sp.Expr, nu: sp.Expr) -> dict[str,sp.Expr]:
    a,b,ell = center,half_width,x_length
    plus = cubic_heat_shear_reanchoring_calibration(a,a,b,ell,time,nu)
    minus = cubic_heat_shear_reanchoring_calibration(-a,-a,b,ell,time,nu)
    pplus = cubic_heat_shear_reanchoring_calibration(a,0,b,ell,time,nu)
    pminus = cubic_heat_shear_reanchoring_calibration(-a,0,b,ell,time,nu)
    child_sum = sp.simplify(plus["raw_error"]+minus["raw_error"])
    parent_error = sp.simplify(pplus["raw_error"]+pminus["raw_error"])
    mismatch = sp.simplify(parent_error-child_sum)
    return {"child_sum":child_sum, "parent_error":parent_error, "mismatch":mismatch,
            "expected_mismatch":sp.simplify(-12*a**2*b*ell)}
