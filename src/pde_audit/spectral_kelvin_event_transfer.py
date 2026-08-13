"""Exact spectral-projector transfer of frame-aware Kelvin residual events.

Finite refinement/reselection need not identify individual principal axes across an
event.  Given the physical residual synthesis blocks A_i and spectral projector
resolutions at the child/parent endpoints, the parent weighted channel is exactly the
sum of signed ordered child-pair / child-spectral-block traffic.  The formula uses
projectors, so it remains regular at eigenvalue degeneracy.
"""
from __future__ import annotations

from collections.abc import Sequence
import sympy as sp

from .frame_aware_kelvin_residual_refinement import block_synthesis_second_moment
from .selected_principal_kelvin_lineage import library_block

Matrix = sp.MatrixBase


def projector_resolution_residual(projectors: Sequence[Matrix]) -> Matrix:
    if not projectors:
        raise ValueError("nonempty projector family required")
    d=projectors[0].rows
    if any(P.shape != (d,d) for P in projectors):
        raise ValueError("projector dimensions must match")
    return sp.simplify(sum(projectors,sp.zeros(d))-sp.eye(d))


def projector_family_algebra_residuals(projectors: Sequence[Matrix]) -> list[Matrix]:
    if not projectors:
        raise ValueError("nonempty projector family required")
    d=projectors[0].rows
    out=[]
    for i,P in enumerate(projectors):
        if P.shape != (d,d):
            raise ValueError("projector dimensions must match")
        out.append(sp.simplify(P.T-P))
        out.append(sp.simplify(P*P-P))
        for j,Q in enumerate(projectors):
            if i != j:
                out.append(sp.simplify(P*Q))
    out.append(projector_resolution_residual(projectors))
    return out


def parent_spectral_channel(
    library_second_moment: Matrix,
    synthesis_blocks: Sequence[Matrix],
    parent_eigenvalue: sp.Expr,
    parent_projector: Matrix,
) -> sp.Expr:
    Qp=block_synthesis_second_moment(library_second_moment,synthesis_blocks)
    return sp.simplify(parent_eigenvalue*sp.trace(parent_projector*Qp))


def spectral_event_transfer_term(
    library_second_moment: Matrix,
    synthesis_blocks: Sequence[Matrix],
    parent_eigenvalue: sp.Expr,
    parent_projector: Matrix,
    child_projector_families: Sequence[Sequence[Matrix]],
    left_child: int,
    left_channel: int,
    right_child: int,
    right_channel: int,
) -> sp.Expr:
    n=len(synthesis_blocks)
    if len(child_projector_families) != n:
        raise ValueError("one child projector family per synthesis block required")
    Ai=synthesis_blocks[left_child]; Aj=synthesis_blocks[right_child]
    d=Ai.rows
    if Ai.shape != (d,d) or Aj.shape != (d,d) or parent_projector.shape != (d,d):
        raise ValueError("all physical synthesis/projector blocks must be equal square matrices")
    Pi=child_projector_families[left_child][left_channel]
    Pj=child_projector_families[right_child][right_channel]
    Qij=library_block(library_second_moment,left_child,right_child,d)
    return sp.simplify(
        parent_eigenvalue
        * sp.trace(parent_projector*Ai*Pi*Qij*Pj*Aj.T)
    )


def spectral_event_transfer_sum(
    library_second_moment: Matrix,
    synthesis_blocks: Sequence[Matrix],
    parent_eigenvalue: sp.Expr,
    parent_projector: Matrix,
    child_projector_families: Sequence[Sequence[Matrix]],
) -> sp.Expr:
    total=sp.Integer(0)
    for i,fami in enumerate(child_projector_families):
        for beta in range(len(fami)):
            for j,famj in enumerate(child_projector_families):
                for gamma in range(len(famj)):
                    total += spectral_event_transfer_term(
                        library_second_moment,synthesis_blocks,parent_eigenvalue,
                        parent_projector,child_projector_families,
                        i,beta,j,gamma,
                    )
    return sp.simplify(total)


def spectral_event_transfer_residual(
    library_second_moment: Matrix,
    synthesis_blocks: Sequence[Matrix],
    parent_eigenvalue: sp.Expr,
    parent_projector: Matrix,
    child_projector_families: Sequence[Sequence[Matrix]],
) -> sp.Expr:
    exact=parent_spectral_channel(
        library_second_moment,synthesis_blocks,parent_eigenvalue,parent_projector
    )
    transfer=spectral_event_transfer_sum(
        library_second_moment,synthesis_blocks,parent_eigenvalue,parent_projector,
        child_projector_families,
    )
    return sp.simplify(exact-transfer)


def full_parent_spectral_energy_residual(
    library_second_moment: Matrix,
    synthesis_blocks: Sequence[Matrix],
    parent_eigenvalues: Sequence[sp.Expr],
    parent_projectors: Sequence[Matrix],
    parent_metric: Matrix,
) -> sp.Expr:
    if len(parent_eigenvalues) != len(parent_projectors):
        raise ValueError("one parent eigenvalue per spectral projector required")
    Qp=block_synthesis_second_moment(library_second_moment,synthesis_blocks)
    spectral=sum(
        (lam*sp.trace(P*Qp) for lam,P in zip(parent_eigenvalues,parent_projectors)),
        sp.Integer(0),
    )
    return sp.simplify(sp.trace(parent_metric*Qp)-spectral)


def transfer_sector_sums(
    library_second_moment: Matrix,
    synthesis_blocks: Sequence[Matrix],
    parent_eigenvalue: sp.Expr,
    parent_projector: Matrix,
    child_projector_families: Sequence[Sequence[Matrix]],
) -> tuple[sp.Expr,sp.Expr,sp.Expr,sp.Expr]:
    """Return same-child/same-channel, same-child/cross-channel,
    cross-child/same-index-channel, cross-child/cross-index-channel sectors.

    Channel index equality is only a bookkeeping label; the projector formula itself
    does not identify physical axes across children.
    """
    ss=sc=cs=cc=sp.Integer(0)
    for i,fami in enumerate(child_projector_families):
        for beta in range(len(fami)):
            for j,famj in enumerate(child_projector_families):
                for gamma in range(len(famj)):
                    term=spectral_event_transfer_term(
                        library_second_moment,synthesis_blocks,parent_eigenvalue,
                        parent_projector,child_projector_families,i,beta,j,gamma
                    )
                    if i==j and beta==gamma: ss += term
                    elif i==j: sc += term
                    elif beta==gamma: cs += term
                    else: cc += term
    return tuple(sp.simplify(x) for x in (ss,sc,cs,cc))


def degenerate_block_internal_basis_residual(
    library_second_moment: Matrix,
    synthesis_blocks: Sequence[Matrix],
    parent_eigenvalue: sp.Expr,
    parent_projector: Matrix,
    child_index: int,
    fixed_other_families: Sequence[Sequence[Matrix]],
    basis_family_a: Sequence[Matrix],
    basis_family_b: Sequence[Matrix],
) -> sp.Expr:
    """Internal rank-one resolutions of the same degenerate projector block give the
    same total event transfer after all child channels are summed.
    """
    fam_a=[list(f) for f in fixed_other_families]
    fam_b=[list(f) for f in fixed_other_families]
    fam_a[child_index]=list(basis_family_a)
    fam_b[child_index]=list(basis_family_b)
    return sp.simplify(
        spectral_event_transfer_sum(
            library_second_moment,synthesis_blocks,parent_eigenvalue,parent_projector,fam_a
        )
        - spectral_event_transfer_sum(
            library_second_moment,synthesis_blocks,parent_eigenvalue,parent_projector,fam_b
        )
    )


def two_child_opposite_residual_transfer_calibration(amplitude: sp.Expr) -> dict[str,sp.Expr|Matrix]:
    """Signed cross-child projector traffic for two opposite z residuals.

    This is the algebraic core of the exact half-period one-mode NS calibration.
    """
    v=sp.Matrix([0,0,amplitude,0,0,-amplitude])
    Q=sp.simplify(v*v.T)
    A=[sp.eye(3),sp.eye(3)]
    P=[sp.diag(1,0,0),sp.diag(0,1,0),sp.diag(0,0,1)]
    fam=[P,P]
    Pz=P[2]
    channel=parent_spectral_channel(Q,A,sp.Integer(1),Pz)
    same_child,cross_channel,cross_child_same,cross_child_cross=transfer_sector_sums(
        Q,A,sp.Integer(1),Pz,fam
    )
    return {
        "library_second_moment":Q,
        "parent_channel":channel,
        "same_child_same_channel":same_child,
        "same_child_cross_channel":cross_channel,
        "cross_child_same_channel":cross_child_same,
        "cross_child_cross_channel":cross_child_cross,
        "transfer_residual":spectral_event_transfer_residual(Q,A,1,Pz,fam),
    }
