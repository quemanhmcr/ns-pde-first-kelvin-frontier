"""Literal first-bad selector semantics for reconstructed Kelvin residual libraries.

A hysteretic first-bad selector is a readout on a persistent germ/fiber library, not
in general a physical map from the previously selected residual to the newly
selected residual.  This module records the exact one-current and second-moment
consequences, preserving the full pair blocks required at selector switches.
"""
from __future__ import annotations

import sympy as sp

from .selected_principal_kelvin_lineage import germ_extraction_map

Matrix = sp.MatrixBase


def selected_residual(library_state: Matrix, germ_count: int, index: int, fiber_dim: int = 3) -> Matrix:
    E=germ_extraction_map(germ_count,index,fiber_dim)
    if library_state.shape != (germ_count*fiber_dim,1):
        raise ValueError("library state dimension does not match germ/fiber data")
    return sp.simplify(E*library_state)


def selector_switch_universal_factorization_residual(
    germ_count: int,
    old_index: int,
    new_index: int,
    transition: Matrix,
    fiber_dim: int = 3,
) -> Matrix:
    """Return E_new - T E_old.  For distinct coordinate germs this cannot vanish."""
    if transition.shape != (fiber_dim,fiber_dim):
        raise ValueError("transition must act on one residual fiber")
    Eold=germ_extraction_map(germ_count,old_index,fiber_dim)
    Enew=germ_extraction_map(germ_count,new_index,fiber_dim)
    return sp.simplify(Enew-transition*Eold)


def selector_switch_unavoidable_new_block(
    germ_count: int,
    old_index: int,
    new_index: int,
    transition: Matrix,
    fiber_dim: int = 3,
) -> Matrix:
    residual=selector_switch_universal_factorization_residual(
        germ_count,old_index,new_index,transition,fiber_dim
    )
    cs=slice(new_index*fiber_dim,(new_index+1)*fiber_dim)
    return residual[:,cs]


def same_selector_factorization_residual(
    germ_count: int,
    index: int,
    transition: Matrix,
    fiber_dim: int = 3,
) -> Matrix:
    E=germ_extraction_map(germ_count,index,fiber_dim)
    return sp.simplify(transition*E-transition*E)


def selector_switch_state_counterexample(
    germ_count: int = 2,
    old_index: int = 0,
    new_index: int = 1,
    fiber_dim: int = 3,
) -> dict[str,Matrix]:
    if old_index == new_index:
        raise ValueError("counterexample requires a genuine selector switch")
    if germ_count < 2:
        raise ValueError("at least two germs required")
    v=sp.Matrix([sp.Integer(i+1) for i in range(fiber_dim)])
    w=sp.Matrix([sp.Integer(fiber_dim-i) for i in range(fiber_dim)])
    X1=sp.zeros(germ_count*fiber_dim,1)
    X2=sp.zeros(germ_count*fiber_dim,1)
    X1[old_index*fiber_dim:(old_index+1)*fiber_dim,0]=v
    X2[old_index*fiber_dim:(old_index+1)*fiber_dim,0]=v
    X2[new_index*fiber_dim:(new_index+1)*fiber_dim,0]=w
    Eold=germ_extraction_map(germ_count,old_index,fiber_dim)
    Enew=germ_extraction_map(germ_count,new_index,fiber_dim)
    return {
        "state_1":X1,
        "state_2":X2,
        "old_readout_1":sp.simplify(Eold*X1),
        "old_readout_2":sp.simplify(Eold*X2),
        "new_readout_1":sp.simplify(Enew*X1),
        "new_readout_2":sp.simplify(Enew*X2),
    }


def selected_second_moment(
    library_second_moment: Matrix,
    germ_count: int,
    index: int,
    fiber_dim: int = 3,
) -> Matrix:
    n=germ_count*fiber_dim
    if library_second_moment.shape != (n,n):
        raise ValueError("library second moment dimension mismatch")
    E=germ_extraction_map(germ_count,index,fiber_dim)
    return sp.simplify(E*library_second_moment*E.T)


def selector_second_moment_jump_terms(
    library_second_moment: Matrix,
    germ_count: int,
    old_index: int,
    new_index: int,
    fiber_dim: int = 3,
) -> tuple[Matrix,Matrix,Matrix]:
    Eold=germ_extraction_map(germ_count,old_index,fiber_dim)
    Enew=germ_extraction_map(germ_count,new_index,fiber_dim)
    dE=sp.simplify(Enew-Eold)
    left=sp.simplify(dE*library_second_moment*Eold.T)
    right=sp.simplify(Eold*library_second_moment*dE.T)
    quad=sp.simplify(dE*library_second_moment*dE.T)
    return left,right,quad


def selector_second_moment_jump_residual(
    library_second_moment: Matrix,
    germ_count: int,
    old_index: int,
    new_index: int,
    fiber_dim: int = 3,
) -> Matrix:
    Qold=selected_second_moment(library_second_moment,germ_count,old_index,fiber_dim)
    Qnew=selected_second_moment(library_second_moment,germ_count,new_index,fiber_dim)
    left,right,quad=selector_second_moment_jump_terms(
        library_second_moment,germ_count,old_index,new_index,fiber_dim
    )
    return sp.simplify(Qnew-Qold-left-right-quad)


def selector_switch_second_moment_counterexample(fiber_dim: int = 3) -> dict[str,Matrix]:
    """Two PSD full-library second moments share the old selected block but differ after switch."""
    v=sp.Matrix([sp.Integer(i+1) for i in range(fiber_dim)])
    w=sp.Matrix([sp.Integer(fiber_dim-i) for i in range(fiber_dim)])
    X1=sp.Matrix.vstack(v,sp.zeros(fiber_dim,1))
    X2=sp.Matrix.vstack(v,w)
    Q1=sp.simplify(X1*X1.T)
    Q2=sp.simplify(X2*X2.T)
    return {
        "Q_full_1":Q1,
        "Q_full_2":Q2,
        "old_Q_1":selected_second_moment(Q1,2,0,fiber_dim),
        "old_Q_2":selected_second_moment(Q2,2,0,fiber_dim),
        "new_Q_1":selected_second_moment(Q1,2,1,fiber_dim),
        "new_Q_2":selected_second_moment(Q2,2,1,fiber_dim),
    }


def hidden_reset_faces_from_blocks(
    library_second_moment: Matrix,
    fiber_dim: int = 3,
) -> dict[str,Matrix]:
    """Two-germ 0->1 reset faces, exposing which full-library blocks are needed."""
    if library_second_moment.shape != (2*fiber_dim,2*fiber_dim):
        raise ValueError("expected a two-germ second-moment library")
    Q00=library_second_moment[:fiber_dim,:fiber_dim]
    Q01=library_second_moment[:fiber_dim,fiber_dim:]
    Q10=library_second_moment[fiber_dim:,:fiber_dim]
    Q11=library_second_moment[fiber_dim:,fiber_dim:]
    left,right,quad=selector_second_moment_jump_terms(library_second_moment,2,0,1,fiber_dim)
    return {
        "Q00":Q00,"Q01":Q01,"Q10":Q10,"Q11":Q11,
        "left":left,"right":right,"quadratic":quad,
        "jump":sp.simplify(Q11-Q00),
    }


def selector_switch_factorization_on_subspace_residual(
    old_extraction: Matrix,
    new_extraction: Matrix,
    admissible_embedding: Matrix,
    transition: Matrix,
) -> Matrix:
    """Conditional bridge: E_new S = T E_old S on a specified admissible subspace."""
    if old_extraction.cols != admissible_embedding.rows or new_extraction.cols != admissible_embedding.rows:
        raise ValueError("embedding domain mismatch")
    if transition.cols != old_extraction.rows or transition.rows != new_extraction.rows:
        raise ValueError("transition readout dimensions mismatch")
    return sp.simplify(new_extraction*admissible_embedding-transition*old_extraction*admissible_embedding)


def selected_after_physical_event(
    full_event_map: Matrix,
    post_germ_count: int,
    post_index: int,
    fiber_dim: int = 3,
) -> Matrix:
    """Literal old-library -> post-event selected readout map E_post A_full."""
    Epost=germ_extraction_map(post_germ_count,post_index,fiber_dim)
    if Epost.cols != full_event_map.rows:
        raise ValueError("post selector/event output dimensions mismatch")
    return sp.simplify(Epost*full_event_map)


def selected_physical_event_factorization_residual(
    full_event_map: Matrix,
    pre_germ_count: int,
    pre_index: int,
    post_germ_count: int,
    post_index: int,
    selected_transition: Matrix,
    fiber_dim: int = 3,
) -> Matrix:
    """Test E_post A_full = T E_pre.  Generic selector changes fail this factorization."""
    Epre=germ_extraction_map(pre_germ_count,pre_index,fiber_dim)
    lhs=selected_after_physical_event(full_event_map,post_germ_count,post_index,fiber_dim)
    if full_event_map.cols != Epre.cols or selected_transition.shape != (fiber_dim,fiber_dim):
        raise ValueError("pre selector/event transition dimensions mismatch")
    return sp.simplify(lhs-selected_transition*Epre)
