"""Gauge-normal finite-event form for reconstructed Kelvin residual lineage.

The physical event datum is the reconstructed residual synthesis map A.  Raw
orientation blocks are coordinate representatives relative to parent/child area
frames.  Sequential event maps compose on one-current state, their tensor-square
pair maps compose functorially, and intermediate spectral projector resolutions
sum out exactly.  Scalar endpoint channel lists alone are not compositional because
they discard cross-channel coherence.
"""
from __future__ import annotations

from collections.abc import Sequence
import sympy as sp

from .frame_aware_kelvin_residual_refinement import (
    frame_aware_physical_synthesis_block,
    codeforming_synthesis_block,
)

Matrix = sp.MatrixBase


def raw_block_from_physical_synthesis(
    parent_area_frame: Matrix,
    child_area_frame: Matrix,
    physical_block: Matrix,
) -> Matrix:
    if not (
        parent_area_frame.shape == child_area_frame.shape == physical_block.shape
        and parent_area_frame.rows == parent_area_frame.cols
    ):
        raise ValueError("parent/child frames and physical block must be equal square matrices")
    return sp.simplify(
        parent_area_frame.T * physical_block * child_area_frame.inv().T
    )


def physical_raw_normal_form_residual(
    parent_area_frame: Matrix,
    child_area_frame: Matrix,
    raw_block: Matrix,
) -> Matrix:
    A=frame_aware_physical_synthesis_block(parent_area_frame,child_area_frame,raw_block)
    recovered=raw_block_from_physical_synthesis(parent_area_frame,child_area_frame,A)
    return sp.simplify(recovered-raw_block)


def raw_block_from_codeforming_synthesis(
    parent_line_frame: Matrix,
    child_line_frame: Matrix,
    codeforming_block: Matrix,
) -> Matrix:
    Jp=sp.det(parent_line_frame); Ji=sp.det(child_line_frame)
    if Jp == 0 or Ji == 0:
        raise ValueError("line frames must be invertible")
    return sp.simplify(Jp/Ji*codeforming_block)


def codeforming_raw_normal_form_residual(
    parent_line_frame: Matrix,
    child_line_frame: Matrix,
    raw_block: Matrix,
) -> Matrix:
    B=codeforming_synthesis_block(parent_line_frame,child_line_frame,raw_block)
    recovered=raw_block_from_codeforming_synthesis(parent_line_frame,child_line_frame,B)
    return sp.simplify(recovered-raw_block)


def frame_aware_event_composition_residual(
    parent_area_frame: Matrix,
    middle_area_frame: Matrix,
    child_area_frame: Matrix,
    parent_from_middle_raw: Matrix,
    middle_from_child_raw: Matrix,
) -> Matrix:
    A_pm=frame_aware_physical_synthesis_block(
        parent_area_frame,middle_area_frame,parent_from_middle_raw
    )
    A_mc=frame_aware_physical_synthesis_block(
        middle_area_frame,child_area_frame,middle_from_child_raw
    )
    A_pc=frame_aware_physical_synthesis_block(
        parent_area_frame,child_area_frame,
        sp.simplify(parent_from_middle_raw*middle_from_child_raw),
    )
    return sp.simplify(A_pm*A_mc-A_pc)


def codeforming_event_composition_residual(
    parent_line_frame: Matrix,
    middle_line_frame: Matrix,
    child_line_frame: Matrix,
    parent_from_middle_raw: Matrix,
    middle_from_child_raw: Matrix,
) -> Matrix:
    B_pm=codeforming_synthesis_block(
        parent_line_frame,middle_line_frame,parent_from_middle_raw
    )
    B_mc=codeforming_synthesis_block(
        middle_line_frame,child_line_frame,middle_from_child_raw
    )
    B_pc=codeforming_synthesis_block(
        parent_line_frame,child_line_frame,
        sp.simplify(parent_from_middle_raw*middle_from_child_raw),
    )
    return sp.simplify(B_pm*B_mc-B_pc)


def second_moment_event_composition_residual(
    child_second_moment: Matrix,
    first_event_map: Matrix,
    second_event_map: Matrix,
) -> Matrix:
    if child_second_moment.rows != child_second_moment.cols:
        raise ValueError("child second moment must be square")
    if first_event_map.cols != child_second_moment.rows or second_event_map.cols != first_event_map.rows:
        raise ValueError("event map dimensions do not compose")
    mid=sp.simplify(first_event_map*child_second_moment*first_event_map.T)
    via_mid=sp.simplify(second_event_map*mid*second_event_map.T)
    total=sp.simplify(second_event_map*first_event_map)
    direct=sp.simplify(total*child_second_moment*total.T)
    return sp.simplify(via_mid-direct)


def pair_functor_event_composition_residual(
    first_event_map: Matrix,
    second_event_map: Matrix,
) -> Matrix:
    if second_event_map.cols != first_event_map.rows:
        raise ValueError("event map dimensions do not compose")
    lhs=sp.kronecker_product(second_event_map,second_event_map)*sp.kronecker_product(first_event_map,first_event_map)
    total=sp.simplify(second_event_map*first_event_map)
    rhs=sp.kronecker_product(total,total)
    return sp.simplify(lhs-rhs)


def intermediate_projector_telescope_residual(
    child_second_moment: Matrix,
    first_event_map: Matrix,
    second_event_map: Matrix,
    parent_eigenvalue: sp.Expr,
    parent_projector: Matrix,
    intermediate_projectors: Sequence[Matrix],
) -> sp.Expr:
    if not intermediate_projectors:
        raise ValueError("nonempty intermediate projector family required")
    total=sp.simplify(second_event_map*first_event_map)
    direct=sp.simplify(
        parent_eigenvalue*sp.trace(
            parent_projector*total*child_second_moment*total.T
        )
    )
    resolved=sp.Integer(0)
    for Pb in intermediate_projectors:
        for Pg in intermediate_projectors:
            resolved += parent_eigenvalue*sp.trace(
                parent_projector
                *second_event_map*Pb*first_event_map
                *child_second_moment
                *first_event_map.T*Pg*second_event_map.T
            )
    return sp.simplify(direct-resolved)


def intermediate_degenerate_basis_telescope_residual(
    child_second_moment: Matrix,
    first_event_map: Matrix,
    second_event_map: Matrix,
    parent_eigenvalue: sp.Expr,
    parent_projector: Matrix,
    intermediate_family_a: Sequence[Matrix],
    intermediate_family_b: Sequence[Matrix],
) -> sp.Expr:
    ra=intermediate_projector_telescope_resolved_value(
        child_second_moment,first_event_map,second_event_map,parent_eigenvalue,
        parent_projector,intermediate_family_a
    )
    rb=intermediate_projector_telescope_resolved_value(
        child_second_moment,first_event_map,second_event_map,parent_eigenvalue,
        parent_projector,intermediate_family_b
    )
    return sp.simplify(ra-rb)


def intermediate_projector_telescope_resolved_value(
    child_second_moment: Matrix,
    first_event_map: Matrix,
    second_event_map: Matrix,
    parent_eigenvalue: sp.Expr,
    parent_projector: Matrix,
    intermediate_projectors: Sequence[Matrix],
) -> sp.Expr:
    total=sp.Integer(0)
    for Pb in intermediate_projectors:
        for Pg in intermediate_projectors:
            total += parent_eigenvalue*sp.trace(
                parent_projector
                *second_event_map*Pb*first_event_map
                *child_second_moment
                *first_event_map.T*Pg*second_event_map.T
            )
    return sp.simplify(total)


def channel_diagonal_readout(second_moment: Matrix, projectors: Sequence[Matrix]) -> tuple[sp.Expr,...]:
    return tuple(sp.simplify(sp.trace(P*second_moment)) for P in projectors)


def channel_only_composition_counterexample(parameter: sp.Expr = sp.Rational(1,2)) -> dict[str,sp.Expr|Matrix|tuple[sp.Expr,...]]:
    """Two PSD mid-state tensors with identical diagonal channels but different
    coherence give different parent channels after the same finite event map.
    """
    c=parameter
    Qplus=sp.Matrix([[1,c,0],[c,1,0],[0,0,0]])
    Qminus=sp.Matrix([[1,-c,0],[-c,1,0],[0,0,0]])
    P=[sp.diag(1,0,0),sp.diag(0,1,0),sp.diag(0,0,1)]
    A=sp.Matrix([[1,1,0],[0,1,0],[0,0,1]])
    Pout=P[0]
    Eplus=sp.simplify(sp.trace(Pout*A*Qplus*A.T))
    Eminus=sp.simplify(sp.trace(Pout*A*Qminus*A.T))
    return {
        "Q_plus":Qplus,
        "Q_minus":Qminus,
        "input_channels_plus":channel_diagonal_readout(Qplus,P),
        "input_channels_minus":channel_diagonal_readout(Qminus,P),
        "event_map":A,
        "parent_channel_plus":Eplus,
        "parent_channel_minus":Eminus,
        "parent_channel_difference":sp.simplify(Eplus-Eminus),
        "cross_coherence_plus":Qplus[0,1],
        "cross_coherence_minus":Qminus[0,1],
    }


def symmetric_second_moment_from_event_probes(second_moment: Matrix) -> Matrix:
    """Reconstruct a symmetric second moment from coordinate and pair-sum probes.

    Probe e_i returns e_i^T Q e_i.  Probe e_i+e_j and polarization recover Q_ij.
    This models exact quadratic readout after a one-row linear event synthesis.
    """
    if second_moment.rows != second_moment.cols:
        raise ValueError("second moment must be square")
    d=second_moment.rows
    e=[sp.eye(d)[:,i] for i in range(d)]
    diag=[sp.simplify((v.T*second_moment*v)[0]) for v in e]
    out=sp.zeros(d)
    for i in range(d):
        out[i,i]=diag[i]
        for j in range(i+1,d):
            pair=sp.simplify(((e[i]+e[j]).T*second_moment*(e[i]+e[j]))[0])
            qij=sp.simplify((pair-diag[i]-diag[j])/2)
            out[i,j]=qij; out[j,i]=qij
    return sp.simplify(out)


def symmetric_event_probe_reconstruction_residual(second_moment: Matrix) -> Matrix:
    reconstructed=symmetric_second_moment_from_event_probes(second_moment)
    target=sp.simplify((second_moment+second_moment.T)/2)
    return sp.simplify(reconstructed-target)
