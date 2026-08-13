"""Combined physical packet event plus selector-switch algebra.

The persistent library changes by a specified linear physical map A, while the
hysteretic selector changes readout from E_- to E_+.  These are distinct typed
operations.  The post-event selected residual is E_+ A X, hence the selected jump
operator is D=E_+ A-E_-.  In a common library space A=I+dA and E_+=E_-+dE,

    D = E_- dA + dE A
      = dE + E_+ dA
      = E_- dA + dE + dE dA.

The mixed dE dA face is the finite physical-selector interaction.  It is not a
Brownian source and cannot be dropped from a simultaneous event ledger.
"""
from __future__ import annotations

import sympy as sp

from .selected_principal_kelvin_lineage import germ_extraction_map, one_mode_half_period_lineage_calibration

Matrix = sp.MatrixBase


def combined_post_readout_map(
    full_event_map: Matrix,
    post_germ_count: int,
    post_index: int,
    fiber_dim: int = 3,
) -> Matrix:
    """C=E_+ A: pre-library -> post-event selected residual."""
    Eplus=germ_extraction_map(post_germ_count,post_index,fiber_dim)
    if Eplus.cols != full_event_map.rows:
        raise ValueError("post selector/event dimensions mismatch")
    return sp.simplify(Eplus*full_event_map)


def combined_selected_jump_operator(
    full_event_map: Matrix,
    pre_germ_count: int,
    pre_index: int,
    post_germ_count: int,
    post_index: int,
    fiber_dim: int = 3,
) -> Matrix:
    """D=E_+ A-E_- on the pre-event persistent library."""
    Eminus=germ_extraction_map(pre_germ_count,pre_index,fiber_dim)
    C=combined_post_readout_map(full_event_map,post_germ_count,post_index,fiber_dim)
    if C.cols != Eminus.cols:
        raise ValueError("pre/post event input dimensions mismatch")
    return sp.simplify(C-Eminus)


def combined_selected_jump(
    library_state: Matrix,
    full_event_map: Matrix,
    pre_germ_count: int,
    pre_index: int,
    post_germ_count: int,
    post_index: int,
    fiber_dim: int = 3,
) -> Matrix:
    D=combined_selected_jump_operator(
        full_event_map,pre_germ_count,pre_index,post_germ_count,post_index,fiber_dim
    )
    if library_state.shape != (D.cols,1):
        raise ValueError("library state dimension mismatch")
    return sp.simplify(D*library_state)


def same_space_event_interaction_faces(
    full_event_map: Matrix,
    germ_count: int,
    pre_index: int,
    post_index: int,
    fiber_dim: int = 3,
) -> tuple[Matrix,Matrix,Matrix]:
    """Return (physical-old, selector-old, mixed) operator faces.

    For A=I+dA and dE=E_+-E_-,
      D = E_- dA + dE + dE dA.
    """
    n=germ_count*fiber_dim
    if full_event_map.shape != (n,n):
        raise ValueError("same-space interaction requires a square library event")
    Eminus=germ_extraction_map(germ_count,pre_index,fiber_dim)
    Eplus=germ_extraction_map(germ_count,post_index,fiber_dim)
    dA=sp.simplify(full_event_map-sp.eye(n))
    dE=sp.simplify(Eplus-Eminus)
    physical_old=sp.simplify(Eminus*dA)
    selector_old=dE
    mixed=sp.simplify(dE*dA)
    return physical_old,selector_old,mixed


def same_space_event_interaction_residual(
    full_event_map: Matrix,
    germ_count: int,
    pre_index: int,
    post_index: int,
    fiber_dim: int = 3,
) -> Matrix:
    D=combined_selected_jump_operator(
        full_event_map,germ_count,pre_index,germ_count,post_index,fiber_dim
    )
    p,s,m=same_space_event_interaction_faces(
        full_event_map,germ_count,pre_index,post_index,fiber_dim
    )
    return sp.simplify(D-p-s-m)


def same_space_sequential_product_rule_residuals(
    full_event_map: Matrix,
    germ_count: int,
    pre_index: int,
    post_index: int,
    fiber_dim: int = 3,
) -> tuple[Matrix,Matrix]:
    """Residuals for physical-first and selector-first finite product rules."""
    n=germ_count*fiber_dim
    if full_event_map.shape != (n,n):
        raise ValueError("same-space product rule requires a square library event")
    Eminus=germ_extraction_map(germ_count,pre_index,fiber_dim)
    Eplus=germ_extraction_map(germ_count,post_index,fiber_dim)
    dA=sp.simplify(full_event_map-sp.eye(n))
    dE=sp.simplify(Eplus-Eminus)
    D=sp.simplify(Eplus*full_event_map-Eminus)
    physical_first=sp.simplify(D-(Eminus*dA+dE*full_event_map))
    selector_first=sp.simplify(D-(dE+Eplus*dA))
    return physical_first,selector_first


def combined_selected_second_moment(
    library_second_moment: Matrix,
    full_event_map: Matrix,
    post_germ_count: int,
    post_index: int,
    fiber_dim: int = 3,
) -> Matrix:
    """Post-event selected second moment C Q C^T with C=E_+ A."""
    C=combined_post_readout_map(full_event_map,post_germ_count,post_index,fiber_dim)
    if library_second_moment.shape != (C.cols,C.cols):
        raise ValueError("library second moment dimension mismatch")
    return sp.simplify(C*library_second_moment*C.T)


def combined_second_moment_jump_faces(
    library_second_moment: Matrix,
    full_event_map: Matrix,
    pre_germ_count: int,
    pre_index: int,
    post_germ_count: int,
    post_index: int,
    fiber_dim: int = 3,
) -> tuple[Matrix,Matrix,Matrix]:
    """Left/right/quadratic full-pair faces for D=E_+A-E_-."""
    Eminus=germ_extraction_map(pre_germ_count,pre_index,fiber_dim)
    D=combined_selected_jump_operator(
        full_event_map,pre_germ_count,pre_index,post_germ_count,post_index,fiber_dim
    )
    if library_second_moment.shape != (D.cols,D.cols):
        raise ValueError("library second moment dimension mismatch")
    left=sp.simplify(D*library_second_moment*Eminus.T)
    right=sp.simplify(Eminus*library_second_moment*D.T)
    quadratic=sp.simplify(D*library_second_moment*D.T)
    return left,right,quadratic


def combined_second_moment_jump_residual(
    library_second_moment: Matrix,
    full_event_map: Matrix,
    pre_germ_count: int,
    pre_index: int,
    post_germ_count: int,
    post_index: int,
    fiber_dim: int = 3,
) -> Matrix:
    Eminus=germ_extraction_map(pre_germ_count,pre_index,fiber_dim)
    before=sp.simplify(Eminus*library_second_moment*Eminus.T)
    after=combined_selected_second_moment(
        library_second_moment,full_event_map,post_germ_count,post_index,fiber_dim
    )
    left,right,quadratic=combined_second_moment_jump_faces(
        library_second_moment,full_event_map,pre_germ_count,pre_index,
        post_germ_count,post_index,fiber_dim
    )
    return sp.simplify(after-before-left-right-quadratic)


def combined_jump_square(
    library_state: Matrix,
    full_event_map: Matrix,
    pre_germ_count: int,
    pre_index: int,
    post_germ_count: int,
    post_index: int,
    fiber_dim: int = 3,
) -> Matrix:
    jump=combined_selected_jump(
        library_state,full_event_map,pre_germ_count,pre_index,
        post_germ_count,post_index,fiber_dim
    )
    return sp.simplify(jump*jump.T)


def one_mode_hidden_germ_synthesis_calibration(
    t: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> dict[str,Matrix|sp.Expr|bool]:
    """Exact one-mode NS payload with a specified hidden-germ synthesis plus 0->1 switch.

    Start from the audited half-period residuals chi_1=-chi_0.  The specified
    orientation-preserving full-library event leaves germ 0 unchanged and replaces
    germ 1 by germ 1 + germ 0.  It is a literal linear current synthesis.  A
    simultaneous selector switch 0->1 then has a nonzero mixed dE dA face.
    """
    c=one_mode_half_period_lineage_calibration(t,nu,k)
    chi0=sp.simplify(c['chi0'])
    chi1=sp.simplify(c['chi1'])
    ez=sp.Matrix([0,0,1])
    X=sp.Matrix.vstack(chi0*ez,chi1*ez)
    I=sp.eye(3); Z=sp.zeros(3)
    A=sp.Matrix.vstack(
        sp.Matrix.hstack(I,Z),
        sp.Matrix.hstack(I,I),
    )
    p,s,m=same_space_event_interaction_faces(A,2,0,1,3)
    jump=combined_selected_jump(X,A,2,0,2,1,3)
    return {
        'chi0':chi0,
        'chi1':chi1,
        'library_state':X,
        'event_map':A,
        'physical_old_jump':sp.simplify(p*X),
        'selector_old_jump':sp.simplify(s*X),
        'mixed_jump':sp.simplify(m*X),
        'total_jump':jump,
        'post_selected':sp.simplify(combined_post_readout_map(A,2,1,3)*X),
        'pre_selected':sp.simplify(germ_extraction_map(2,0,3)*X),
    }
