"""Frame-aware descent of raw orientation-error refinement to physical/codeforming residuals.

Raw orientation-complete Kelvin errors live in the area-frame coefficient fiber.
If a compatible packet refinement is linear there, metric whitening forces an exact
physical residual synthesis map.  Cofactor geometry then collapses the corresponding
codeforming synthesis blocks to determinant ratios times the raw orientation maps.

No claim is made that the programme's actual moving first-bad refinement has already
supplied the required raw orientation-current blocks; that instantiation remains a
separate literal question.
"""
from __future__ import annotations

from collections.abc import Sequence
import sympy as sp

from .codeforming_surface_moment_tower import cofactor_map
from .codeforming_whitened_kelvin_remainder import whitened_face_reconstruction
from .selected_principal_kelvin_lineage import column_vectorize, library_block
from .weighted_codeforming_kelvin_residual import quadratic_asymmetric_square_exact_residual

Matrix = sp.MatrixBase


def raw_orientation_error(circulation: Matrix, area_frame: Matrix, local_field: Matrix) -> Matrix:
    if circulation.shape != local_field.shape or area_frame.shape != (local_field.rows, local_field.rows):
        raise ValueError("circulation, field, and area frame dimensions must match")
    return sp.simplify(circulation - area_frame.T * local_field)


def compatible_parent_packet(
    child_circulations: Sequence[Matrix],
    child_area_frames: Sequence[Matrix],
    raw_refinement_blocks: Sequence[Matrix],
) -> tuple[Matrix, Matrix]:
    if not child_circulations or not (
        len(child_circulations) == len(child_area_frames) == len(raw_refinement_blocks)
    ):
        raise ValueError("matching nonempty child packet data required")
    d = child_circulations[0].rows
    Kp = sp.zeros(d, 1)
    HpT = sp.zeros(d)
    for K, H, R in zip(child_circulations, child_area_frames, raw_refinement_blocks):
        if K.shape != (d,1) or H.shape != (d,d) or R.shape != (d,d):
            raise ValueError("all packet blocks must share one fiber dimension")
        Kp += R * K
        HpT += R * H.T
    return sp.simplify(Kp), sp.simplify(HpT.T)


def compatible_raw_error_refinement_residual(
    child_circulations: Sequence[Matrix],
    child_area_frames: Sequence[Matrix],
    raw_refinement_blocks: Sequence[Matrix],
    local_field: Matrix,
) -> Matrix:
    Kp, Hp = compatible_parent_packet(
        child_circulations, child_area_frames, raw_refinement_blocks
    )
    lhs = raw_orientation_error(Kp, Hp, local_field)
    rhs = sp.zeros(local_field.rows, 1)
    for K, H, R in zip(child_circulations, child_area_frames, raw_refinement_blocks):
        rhs += R * raw_orientation_error(K, H, local_field)
    return sp.simplify(lhs-rhs)


def frame_aware_physical_synthesis_block(
    parent_area_frame: Matrix,
    child_area_frame: Matrix,
    raw_refinement_block: Matrix,
) -> Matrix:
    if not (
        parent_area_frame.shape == child_area_frame.shape == raw_refinement_block.shape
        and parent_area_frame.rows == parent_area_frame.cols
    ):
        raise ValueError("parent/child frames and raw block must be equal square matrices")
    return sp.simplify(
        parent_area_frame.inv().T * raw_refinement_block * child_area_frame.T
    )


def frame_aware_physical_synthesis_map(
    parent_area_frame: Matrix,
    child_area_frames: Sequence[Matrix],
    raw_refinement_blocks: Sequence[Matrix],
) -> Matrix:
    if not child_area_frames or len(child_area_frames) != len(raw_refinement_blocks):
        raise ValueError("matching nonempty child frames/refinement blocks required")
    return sp.Matrix.hstack(*[
        frame_aware_physical_synthesis_block(parent_area_frame,H,R)
        for H,R in zip(child_area_frames,raw_refinement_blocks)
    ])


def physical_reconstruction_refinement_residual(
    child_raw_errors: Sequence[Matrix],
    child_area_frames: Sequence[Matrix],
    raw_refinement_blocks: Sequence[Matrix],
    parent_area_frame: Matrix,
) -> Matrix:
    if not child_raw_errors or not (
        len(child_raw_errors) == len(child_area_frames) == len(raw_refinement_blocks)
    ):
        raise ValueError("matching nonempty child error/frame/refinement data required")
    d = parent_area_frame.rows
    eps_parent = sp.zeros(d,1)
    physical_stack=[]
    for eps,H,R in zip(child_raw_errors,child_area_frames,raw_refinement_blocks):
        eps_parent += R*eps
        physical_stack.append(whitened_face_reconstruction(eps,H))
    lhs=whitened_face_reconstruction(sp.simplify(eps_parent),parent_area_frame)
    A=frame_aware_physical_synthesis_map(parent_area_frame,child_area_frames,raw_refinement_blocks)
    rhs=sp.simplify(A*sp.Matrix.vstack(*physical_stack))
    return sp.simplify(lhs-rhs)


def reparameterized_raw_refinement_block(
    raw_refinement_block: Matrix,
    parent_orientation_map: Matrix,
    child_orientation_map: Matrix,
) -> Matrix:
    """R' = S_P^T R S_i^{-T} for H->H S and epsilon->S^T epsilon."""
    if not (
        raw_refinement_block.shape == parent_orientation_map.shape == child_orientation_map.shape
        and raw_refinement_block.rows == raw_refinement_block.cols
    ):
        raise ValueError("raw/parent/child orientation maps must have equal square shape")
    return sp.simplify(
        parent_orientation_map.T
        * raw_refinement_block
        * child_orientation_map.inv().T
    )


def physical_synthesis_gauge_residual(
    parent_area_frame: Matrix,
    child_area_frame: Matrix,
    raw_refinement_block: Matrix,
    parent_orientation_map: Matrix,
    child_orientation_map: Matrix,
) -> Matrix:
    before=frame_aware_physical_synthesis_block(
        parent_area_frame,child_area_frame,raw_refinement_block
    )
    Rnew=reparameterized_raw_refinement_block(
        raw_refinement_block,parent_orientation_map,child_orientation_map
    )
    after=frame_aware_physical_synthesis_block(
        sp.simplify(parent_area_frame*parent_orientation_map),
        sp.simplify(child_area_frame*child_orientation_map),
        Rnew,
    )
    return sp.simplify(after-before)


def cofactor_physical_synthesis_residual(
    parent_line_frame: Matrix,
    child_line_frame: Matrix,
    raw_refinement_block: Matrix,
) -> Matrix:
    """A_i = (J_i/J_P) L_P R_i L_i^{-1} when H=cof(L)."""
    Hp=cofactor_map(parent_line_frame)
    Hi=cofactor_map(child_line_frame)
    exact=frame_aware_physical_synthesis_block(Hp,Hi,raw_refinement_block)
    expected=sp.simplify(
        sp.det(child_line_frame)/sp.det(parent_line_frame)
        * parent_line_frame*raw_refinement_block*child_line_frame.inv()
    )
    return sp.simplify(exact-expected)


def codeforming_synthesis_block(
    parent_line_frame: Matrix,
    child_line_frame: Matrix,
    raw_refinement_block: Matrix,
) -> Matrix:
    Hp=cofactor_map(parent_line_frame)
    Hi=cofactor_map(child_line_frame)
    A=frame_aware_physical_synthesis_block(Hp,Hi,raw_refinement_block)
    return sp.simplify(parent_line_frame.inv()*A*child_line_frame)


def codeforming_determinant_ratio_residual(
    parent_line_frame: Matrix,
    child_line_frame: Matrix,
    raw_refinement_block: Matrix,
) -> Matrix:
    exact=codeforming_synthesis_block(
        parent_line_frame,child_line_frame,raw_refinement_block
    )
    expected=sp.simplify(
        sp.det(child_line_frame)/sp.det(parent_line_frame)*raw_refinement_block
    )
    return sp.simplify(exact-expected)


def codeforming_synthesis_map(
    parent_line_frame: Matrix,
    child_line_frames: Sequence[Matrix],
    raw_refinement_blocks: Sequence[Matrix],
) -> Matrix:
    if not child_line_frames or len(child_line_frames) != len(raw_refinement_blocks):
        raise ValueError("matching nonempty child line frames/refinement blocks required")
    return sp.Matrix.hstack(*[
        codeforming_synthesis_block(parent_line_frame,L,R)
        for L,R in zip(child_line_frames,raw_refinement_blocks)
    ])


def codeforming_refinement_from_raw_error_residual(
    child_codeforming_residuals: Sequence[Matrix],
    parent_line_frame: Matrix,
    child_line_frames: Sequence[Matrix],
    raw_refinement_blocks: Sequence[Matrix],
) -> Matrix:
    if not child_codeforming_residuals or not (
        len(child_codeforming_residuals)==len(child_line_frames)==len(raw_refinement_blocks)
    ):
        raise ValueError("matching nonempty codeforming refinement data required")
    Jp=sp.det(parent_line_frame)
    eps_parent=sp.zeros(parent_line_frame.rows,1)
    for chi,L,R in zip(child_codeforming_residuals,child_line_frames,raw_refinement_blocks):
        eps_parent += R*(sp.det(L)*chi)
    lhs=sp.simplify(eps_parent/Jp)
    B=codeforming_synthesis_map(parent_line_frame,child_line_frames,raw_refinement_blocks)
    rhs=sp.simplify(B*sp.Matrix.vstack(*child_codeforming_residuals))
    return sp.simplify(lhs-rhs)


def block_synthesis_second_moment(
    library_second_moment: Matrix,
    synthesis_blocks: Sequence[Matrix],
) -> Matrix:
    if not synthesis_blocks:
        raise ValueError("at least one synthesis block required")
    A=sp.Matrix.hstack(*synthesis_blocks)
    if A.cols != library_second_moment.rows or library_second_moment.rows != library_second_moment.cols:
        raise ValueError("synthesis/library dimensions do not match")
    return sp.simplify(A*library_second_moment*A.T)


def block_synthesis_pair_functor_residual(
    library_second_moment: Matrix,
    synthesis_blocks: Sequence[Matrix],
) -> Matrix:
    A=sp.Matrix.hstack(*synthesis_blocks)
    lhs=column_vectorize(block_synthesis_second_moment(library_second_moment,synthesis_blocks))
    rhs=sp.kronecker_product(A,A)*column_vectorize(library_second_moment)
    return sp.simplify(lhs-rhs)


def block_synthesis_pair_expansion_residual(
    library_second_moment: Matrix,
    synthesis_blocks: Sequence[Matrix],
) -> Matrix:
    d=synthesis_blocks[0].rows
    exact=block_synthesis_second_moment(library_second_moment,synthesis_blocks)
    expanded=sp.zeros(d)
    for i,Ai in enumerate(synthesis_blocks):
        for j,Aj in enumerate(synthesis_blocks):
            expanded += Ai*library_block(library_second_moment,i,j,Ai.cols)*Aj.T
    return sp.simplify(exact-expanded)


def block_synthesis_spectral_channel_residual(
    library_second_moment: Matrix,
    synthesis_blocks: Sequence[Matrix],
    eigenvalue: sp.Expr,
    projector: Matrix,
) -> sp.Expr:
    d=projector.rows
    exact=sp.simplify(
        eigenvalue*sp.trace(projector*block_synthesis_second_moment(library_second_moment,synthesis_blocks))
    )
    expanded=sp.Integer(0)
    for i,Ai in enumerate(synthesis_blocks):
        for j,Aj in enumerate(synthesis_blocks):
            expanded += eigenvalue*sp.trace(
                projector*Ai*library_block(library_second_moment,i,j,Ai.cols)*Aj.T
            )
    return sp.simplify(exact-expanded)


def isotropic_frame_aware_scale_residuals(
    parent_scale: sp.Expr,
    child_scale: sp.Expr,
    coefficient: sp.Expr,
) -> tuple[Matrix,Matrix]:
    """Physical synthesis scales as (rho_i/rho_P)^2; codeforming as the cube ratio."""
    Lp=parent_scale*sp.eye(3); Li=child_scale*sp.eye(3); R=coefficient*sp.eye(3)
    A=frame_aware_physical_synthesis_block(cofactor_map(Lp),cofactor_map(Li),R)
    B=codeforming_synthesis_block(Lp,Li,R)
    Aexpected=coefficient*(child_scale/parent_scale)**2*sp.eye(3)
    Bexpected=coefficient*(child_scale/parent_scale)**3*sp.eye(3)
    return sp.simplify(A-Aexpected),sp.simplify(B-Bexpected)


def quadratic_isotropic_packet_refinement_calibration(
    child_scales: Sequence[sp.Expr],
    coefficients: Sequence[sp.Expr],
    time: sp.Expr,
    nu: sp.Expr,
) -> dict[str, sp.Expr | Matrix]:
    """Exact quadratic-heat-shear current synthesis at anchor y=0.

    Each isotropic child has H_i=rho_i^2 I, epsilon_i=-rho_i^3 e_z,
    chi_i=-e_z.  The parent is the formal orientation-complete current sum with
    scalar raw blocks a_i I, so H_P=(sum a_i rho_i^2)I exactly.
    """
    if not child_scales or len(child_scales) != len(coefficients):
        raise ValueError("matching nonempty child scales/coefficients required")
    Y=sp.symbols("Y_frame_ref", real=True)
    hp=sp.simplify(sum(a*rho**2 for a,rho in zip(coefficients,child_scales)))
    if hp == 0:
        raise ValueError("parent area scale must be nonzero")
    Hp=sp.simplify(hp*sp.eye(3))
    eps_children=[]; r_children=[]; chi_children=[]; Hchildren=[]; Rblocks=[]
    eps_parent=sp.zeros(3,1)
    for a,rho in zip(coefficients,child_scales):
        eps_z,chi_z,r_z=quadratic_asymmetric_square_exact_residual(Y,time,nu,rho)
        eps_z=sp.simplify(eps_z.subs(Y,0))
        chi_z=sp.simplify(chi_z.subs(Y,0))
        r_z=sp.simplify(r_z.subs(Y,0))
        eps=sp.Matrix([0,0,eps_z]); chi=sp.Matrix([0,0,chi_z]); rr=sp.Matrix([0,0,r_z])
        H=sp.simplify(rho**2*sp.eye(3)); R=sp.simplify(a*sp.eye(3))
        eps_children.append(eps); chi_children.append(chi); r_children.append(rr)
        Hchildren.append(H); Rblocks.append(R)
        eps_parent += R*eps
    eps_parent=sp.simplify(eps_parent)
    r_parent=sp.simplify(Hp.inv().T*eps_parent)
    A=frame_aware_physical_synthesis_map(Hp,Hchildren,Rblocks)
    r_pred=sp.simplify(A*sp.Matrix.vstack(*r_children))
    rho_parent=sp.sqrt(hp)
    Lp=sp.simplify(rho_parent*sp.eye(3))
    child_L=[sp.simplify(rho*sp.eye(3)) for rho in child_scales]
    B=codeforming_synthesis_map(Lp,child_L,Rblocks)
    chi_parent=sp.simplify(eps_parent/sp.det(Lp))
    chi_pred=sp.simplify(B*sp.Matrix.vstack(*chi_children))
    naive_physical=sp.simplify(sum(
        (a*rr for a,rr in zip(coefficients,r_children)), sp.zeros(3,1)
    ))
    return {
        "parent_area_frame":Hp,
        "parent_line_frame":Lp,
        "parent_raw_error":eps_parent,
        "parent_physical_residual":r_parent,
        "frame_aware_physical_prediction":r_pred,
        "parent_codeforming_residual":chi_parent,
        "determinant_weighted_codeforming_prediction":chi_pred,
        "naive_common_fiber_physical_sum":naive_physical,
        "physical_prediction_residual":sp.simplify(r_parent-r_pred),
        "codeforming_prediction_residual":sp.simplify(chi_parent-chi_pred),
        "parent_area_scale":hp,
    }


def orientation_preserving_scalar_refinement_blocks(
    weights: Sequence[sp.Expr],
    fiber_dim: int = 3,
) -> list[Matrix]:
    if not weights or fiber_dim <= 0:
        raise ValueError("nonempty weights and positive fiber dimension required")
    I=sp.eye(fiber_dim)
    return [sp.simplify(w*I) for w in weights]


def scalar_refinement_pair_block_residual(
    weights: Sequence[sp.Expr],
    fiber_dim: int = 3,
) -> list[Matrix]:
    blocks=orientation_preserving_scalar_refinement_blocks(weights,fiber_dim)
    I2=sp.eye(fiber_dim**2)
    out=[]
    for i,Ri in enumerate(blocks):
        for j,Rj in enumerate(blocks):
            out.append(sp.simplify(sp.kronecker_product(Ri,Rj)-weights[i]*weights[j]*I2))
    return out


def orientation_complete_chain_refinement_residual(
    fine_boundary: Matrix,
    coarse_boundary: Matrix,
    edge_refinement: Matrix,
    vertex_refinement: Matrix,
    fiber_dim: int = 3,
) -> Matrix:
    """Lift B_f R1=R0 B_c to the independent orientation fiber."""
    if fiber_dim <= 0:
        raise ValueError("fiber dimension must be positive")
    I=sp.eye(fiber_dim)
    Bf=sp.kronecker_product(fine_boundary,I)
    Bc=sp.kronecker_product(coarse_boundary,I)
    R1=sp.kronecker_product(edge_refinement,I)
    R0=sp.kronecker_product(vertex_refinement,I)
    return sp.simplify(Bf*R1-R0*Bc)
