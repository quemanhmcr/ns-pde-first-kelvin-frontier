"""Hybrid selected-residual semimartingale law.

A persistent same-replica residual library evolves continuously by common Brownian
motion.  A hysteretic selector is piecewise constant and changes by finite readout
jumps.  The selected process therefore has a continuous Brownian bracket plus
finite jump squares in its optional quadratic variation.  The jump squares are
observer/reset path variation, not a new continuous stochastic producer or a
monotone covariance bank.
"""
from __future__ import annotations

from collections.abc import Sequence
import sympy as sp

from .selected_principal_kelvin_lineage import germ_extraction_map, one_mode_half_period_lineage_calibration
from .same_replica_residual_library_dynamics import same_replica_library_qv, stacked_common_noise

Matrix = sp.MatrixBase


def selected_continuous_noise(
    noise_blocks: Sequence[Matrix],
    index: int,
) -> Matrix:
    d=noise_blocks[0].rows
    E=germ_extraction_map(len(noise_blocks),index,d)
    return sp.simplify(E*stacked_common_noise(noise_blocks))


def selected_continuous_qv_rate(
    noise_blocks: Sequence[Matrix],
    index: int,
    nu: sp.Expr,
) -> Matrix:
    d=noise_blocks[0].rows
    E=germ_extraction_map(len(noise_blocks),index,d)
    G=same_replica_library_qv(noise_blocks,nu)
    return sp.simplify(E*G*E.T)


def selected_continuous_qv_factorization_residual(
    noise_blocks: Sequence[Matrix],
    index: int,
    nu: sp.Expr,
) -> Matrix:
    Q=selected_continuous_noise(noise_blocks,index)
    return sp.simplify(selected_continuous_qv_rate(noise_blocks,index,nu)-2*nu*Q*Q.T)


def selector_readout_jump(
    library_state: Matrix,
    germ_count: int,
    old_index: int,
    new_index: int,
    fiber_dim: int = 3,
) -> Matrix:
    Eold=germ_extraction_map(germ_count,old_index,fiber_dim)
    Enew=germ_extraction_map(germ_count,new_index,fiber_dim)
    if library_state.shape != (germ_count*fiber_dim,1):
        raise ValueError("library state dimension mismatch")
    return sp.simplify((Enew-Eold)*library_state)


def selector_jump_optional_qv(
    library_state: Matrix,
    germ_count: int,
    old_index: int,
    new_index: int,
    fiber_dim: int = 3,
) -> Matrix:
    jump=selector_readout_jump(library_state,germ_count,old_index,new_index,fiber_dim)
    return sp.simplify(jump*jump.T)


def selector_jump_dyad_faces(
    library_state: Matrix,
    germ_count: int,
    old_index: int,
    new_index: int,
    fiber_dim: int = 3,
) -> tuple[Matrix,Matrix,Matrix]:
    Eold=germ_extraction_map(germ_count,old_index,fiber_dim)
    Yold=sp.simplify(Eold*library_state)
    dY=selector_readout_jump(library_state,germ_count,old_index,new_index,fiber_dim)
    left=sp.simplify(dY*Yold.T)
    right=sp.simplify(Yold*dY.T)
    quadratic=sp.simplify(dY*dY.T)
    return left,right,quadratic


def selector_jump_dyad_residual(
    library_state: Matrix,
    germ_count: int,
    old_index: int,
    new_index: int,
    fiber_dim: int = 3,
) -> Matrix:
    Eold=germ_extraction_map(germ_count,old_index,fiber_dim)
    Enew=germ_extraction_map(germ_count,new_index,fiber_dim)
    Yold=sp.simplify(Eold*library_state)
    Ynew=sp.simplify(Enew*library_state)
    left,right,quadratic=selector_jump_dyad_faces(
        library_state,germ_count,old_index,new_index,fiber_dim
    )
    return sp.simplify(Ynew*Ynew.T-Yold*Yold.T-left-right-quadratic)


def hybrid_optional_qv(
    continuous_qv_increments: Sequence[Matrix],
    jump_vectors: Sequence[Matrix],
) -> Matrix:
    if not continuous_qv_increments and not jump_vectors:
        raise ValueError("at least one continuous or jump contribution required")
    if continuous_qv_increments:
        d=continuous_qv_increments[0].rows
    else:
        d=jump_vectors[0].rows
    out=sp.zeros(d)
    for G in continuous_qv_increments:
        if G.shape != (d,d):
            raise ValueError("continuous qv dimensions must match")
        out += G
    for J in jump_vectors:
        if J.shape != (d,1):
            raise ValueError("jump vector dimensions must match")
        out += J*J.T
    return sp.simplify(out)


def selector_closed_excursion(
    library_state: Matrix,
    germ_count: int,
    index_path: Sequence[int],
    fiber_dim: int = 3,
) -> dict[str,Matrix]:
    if len(index_path) < 2:
        raise ValueError("selector path must contain at least one switch")
    jumps=[]
    for old,new in zip(index_path,index_path[1:]):
        jumps.append(selector_readout_jump(library_state,germ_count,old,new,fiber_dim))
    Estart=germ_extraction_map(germ_count,index_path[0],fiber_dim)
    Eend=germ_extraction_map(germ_count,index_path[-1],fiber_dim)
    state_change=sp.simplify((Eend-Estart)*library_state)
    jump_sum=sp.simplify(sum(jumps,sp.zeros(fiber_dim,1)))
    optional_qv=sp.simplify(sum((J*J.T for J in jumps),sp.zeros(fiber_dim)))
    return {
        "state_change":state_change,
        "jump_sum":jump_sum,
        "jump_optional_qv":optional_qv,
    }


def one_mode_selector_excursion_calibration(
    t: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> dict[str,sp.Expr|Matrix]:
    """Exact NS selector excursion on the two half-period residual packets."""
    c=one_mode_half_period_lineage_calibration(t,nu,k)
    chi0=sp.simplify(c["chi0"])
    chi1=sp.simplify(c["chi1"])
    X=sp.Matrix([0,0,chi0,0,0,chi1])
    excursion=selector_closed_excursion(X,2,[0,1,0],3)
    jump01=selector_readout_jump(X,2,0,1,3)
    jump10=selector_readout_jump(X,2,1,0,3)
    return {
        "chi0":chi0,
        "chi1":chi1,
        "jump_01":jump01,
        "jump_10":jump10,
        "state_change":excursion["state_change"],
        "jump_sum":excursion["jump_sum"],
        "jump_optional_qv":excursion["jump_optional_qv"],
        "jump_optional_qv_trace":sp.simplify(sp.trace(excursion["jump_optional_qv"])),
    }
