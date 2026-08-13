"""Selected/refined lineage algebra for physical Kelvin residual channels.

A first-bad selector acts on the germ factor while line/spectral geometry acts on
the physical 3-fiber.  Finite selector changes and linear refinements are therefore
handled by literal fiber-synthesis maps and their full tensor-square pair lifts.
Endpoint spectral channels are canonical; channel labels across an event are not
identified without an explicit physical transport map.

No first-bad threshold, moving-cut law, future-bank identification, restart,
continuation, or regularity claim is made here.
"""
from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
import sympy as sp

from .orientation_packet import packet_selector
from .weighted_codeforming_kelvin_residual import (
    one_mode_asymmetric_codeforming_residual,
)

Matrix = sp.MatrixBase


def block_diagonal_fiber_operator(blocks: Sequence[Matrix]) -> Matrix:
    if not blocks:
        raise ValueError("at least one fiber block is required")
    d = blocks[0].rows
    if any(B.shape != (d, d) for B in blocks):
        raise ValueError("all fiber blocks must be equal square matrices")
    return sp.diag(*blocks)


def first_bad_spectral_commutator(
    germ_selector: Matrix,
    fiber_blocks: Sequence[Matrix],
) -> Matrix:
    """[M_fb tensor I, blockdiag(P_g)] on the joint germ/fiber state."""
    if germ_selector.rows != germ_selector.cols or len(fiber_blocks) != germ_selector.rows:
        raise ValueError("one fiber block per germ is required")
    d = fiber_blocks[0].rows
    S = packet_selector(germ_selector, d)
    P = block_diagonal_fiber_operator(fiber_blocks)
    return sp.simplify(S * P - P * S)


def first_bad_pair_spectral_commutator(
    germ_selector: Matrix,
    fiber_blocks: Sequence[Matrix],
) -> Matrix:
    S = packet_selector(germ_selector, fiber_blocks[0].rows)
    P = block_diagonal_fiber_operator(fiber_blocks)
    S2 = sp.kronecker_product(S, S)
    P2 = sp.kronecker_product(P, P)
    return sp.simplify(S2 * P2 - P2 * S2)


def selected_library_weighted_energy(
    library_second_moment: Matrix,
    germ_selector: Matrix,
    metric_blocks: Sequence[Matrix],
) -> sp.Expr:
    """Endpoint selected physical energy on the joint germ/fiber library."""
    if germ_selector.rows != germ_selector.cols or len(metric_blocks) != germ_selector.rows:
        raise ValueError("one metric block per germ is required")
    d = metric_blocks[0].rows
    S = packet_selector(germ_selector, d)
    M = block_diagonal_fiber_operator(metric_blocks)
    if library_second_moment.shape != M.shape:
        raise ValueError("library second moment does not match germ/fiber metric")
    return sp.simplify(sp.trace(S * M * S * library_second_moment))


def selected_library_spectral_decomposition_residual(
    library_second_moment: Matrix,
    germ_selector: Matrix,
    metric_blocks: Sequence[Matrix],
    projector_families: Sequence[Sequence[Matrix]],
    eigenvalue_families: Sequence[Sequence[sp.Expr]],
) -> sp.Expr:
    """Selected endpoint energy equals the sum of per-germ spectral-block channels."""
    n = germ_selector.rows
    if not (
        germ_selector.cols == n
        and len(metric_blocks) == len(projector_families) == len(eigenvalue_families) == n
    ):
        raise ValueError("one spectral family per germ is required")
    d = metric_blocks[0].rows
    S = packet_selector(germ_selector, d)
    exact = selected_library_weighted_energy(library_second_moment, germ_selector, metric_blocks)
    total = sp.Integer(0)
    for g in range(n):
        if len(projector_families[g]) != len(eigenvalue_families[g]):
            raise ValueError("one eigenvalue per spectral projector is required")
        Eg = sp.zeros(n)
        Eg[g, g] = 1
        for P, lam in zip(projector_families[g], eigenvalue_families[g]):
            if P.shape != (d, d):
                raise ValueError("spectral projector block dimension mismatch")
            Pg = sp.kronecker_product(Eg, P)
            total += lam * sp.trace(S * Pg * S * library_second_moment)
    return sp.simplify(exact - total)


def coefficient_synthesis_map(
    coefficients: Sequence[sp.Expr],
    fiber_dim: int = 3,
) -> Matrix:
    """A=[a_1 I ... a_N I], mapping a fiber library to one physical fiber."""
    if not coefficients or fiber_dim <= 0:
        raise ValueError("nonempty coefficients and positive fiber dimension required")
    I = sp.eye(fiber_dim)
    return sp.Matrix.hstack(*[sp.simplify(a * I) for a in coefficients])


def germ_extraction_map(germ_count: int, index: int, fiber_dim: int = 3) -> Matrix:
    if germ_count <= 0 or fiber_dim <= 0 or not 0 <= index < germ_count:
        raise ValueError("invalid germ extraction data")
    coeffs = [sp.Integer(0)] * germ_count
    coeffs[index] = sp.Integer(1)
    return coefficient_synthesis_map(coeffs, fiber_dim)


def synthesized_second_moment(
    library_second_moment: Matrix,
    synthesis: Matrix,
) -> Matrix:
    if library_second_moment.rows != library_second_moment.cols:
        raise ValueError("library second moment must be square")
    if synthesis.cols != library_second_moment.rows:
        raise ValueError("synthesis/library dimensions do not match")
    return sp.simplify(synthesis * library_second_moment * synthesis.T)


def column_vectorize(M: Matrix) -> Matrix:
    return sp.Matrix([M[i, j] for j in range(M.cols) for i in range(M.rows)])


def synthesis_pair_functor_residual(
    library_second_moment: Matrix,
    synthesis: Matrix,
) -> Matrix:
    """vec(A Q A^T)=(A tensor A) vec(Q), the full pair functor."""
    lhs = column_vectorize(synthesized_second_moment(library_second_moment, synthesis))
    rhs = sp.kronecker_product(synthesis, synthesis) * column_vectorize(library_second_moment)
    return sp.simplify(lhs - rhs)


def library_block(
    library_second_moment: Matrix,
    left: int,
    right: int,
    fiber_dim: int = 3,
) -> Matrix:
    n = library_second_moment.rows // fiber_dim
    if library_second_moment.shape != (n * fiber_dim, n * fiber_dim):
        raise ValueError("library matrix size must be a multiple of fiber dimension")
    if not (0 <= left < n and 0 <= right < n):
        raise ValueError("library block index out of range")
    rs = slice(left * fiber_dim, (left + 1) * fiber_dim)
    cs = slice(right * fiber_dim, (right + 1) * fiber_dim)
    return library_second_moment[rs, cs]


def synthesis_block_expansion_residual(
    library_second_moment: Matrix,
    coefficients: Sequence[sp.Expr],
    fiber_dim: int = 3,
) -> Matrix:
    A = coefficient_synthesis_map(coefficients, fiber_dim)
    exact = synthesized_second_moment(library_second_moment, A)
    expanded = sp.zeros(fiber_dim)
    for i, ai in enumerate(coefficients):
        for j, aj in enumerate(coefficients):
            expanded += ai * aj * library_block(library_second_moment, i, j, fiber_dim)
    return sp.simplify(exact - expanded)


def spectral_synthesis_channel(
    library_second_moment: Matrix,
    coefficients: Sequence[sp.Expr],
    eigenvalue: sp.Expr,
    projector: Matrix,
) -> sp.Expr:
    d = projector.rows
    if projector.shape != (d, d):
        raise ValueError("spectral projector must be square")
    Q = synthesized_second_moment(
        library_second_moment, coefficient_synthesis_map(coefficients, d)
    )
    return sp.simplify(eigenvalue * sp.trace(projector * Q))


def spectral_synthesis_pair_expansion_residual(
    library_second_moment: Matrix,
    coefficients: Sequence[sp.Expr],
    eigenvalue: sp.Expr,
    projector: Matrix,
) -> sp.Expr:
    d = projector.rows
    exact = spectral_synthesis_channel(
        library_second_moment, coefficients, eigenvalue, projector
    )
    expanded = sp.Integer(0)
    for i, ai in enumerate(coefficients):
        for j, aj in enumerate(coefficients):
            expanded += ai * aj * eigenvalue * sp.trace(
                projector * library_block(library_second_moment, i, j, d)
            )
    return sp.simplify(exact - expanded)


def diagonal_only_spectral_channel(
    library_second_moment: Matrix,
    coefficients: Sequence[sp.Expr],
    eigenvalue: sp.Expr,
    projector: Matrix,
) -> sp.Expr:
    d = projector.rows
    return sp.simplify(sum(
        ai**2 * eigenvalue * sp.trace(
            projector * library_block(library_second_moment, i, i, d)
        )
        for i, ai in enumerate(coefficients)
    ))


@dataclass(frozen=True)
class SelectorResetFaces:
    geometry: sp.Expr
    pair_left: sp.Expr
    pair_right: sp.Expr
    pair_quadratic: sp.Expr
    total_jump: sp.Expr

    @property
    def reconstructed(self) -> sp.Expr:
        return sp.simplify(
            self.geometry + self.pair_left + self.pair_right + self.pair_quadratic
        )


def selector_reset_weighted_faces(
    library_second_moment: Matrix,
    synthesis_minus: Matrix,
    synthesis_plus: Matrix,
    metric_minus: Matrix,
    metric_plus: Matrix,
) -> SelectorResetFaces:
    """Exact fixed/conditioned finite selector reset with endpoint metric change.

    The metric midpoint carries geometry revaluation.  The state midpoint face is
    resolved further by the exact tensor-square jump of the synthesis map.
    """
    Qm = synthesized_second_moment(library_second_moment, synthesis_minus)
    Qp = synthesized_second_moment(library_second_moment, synthesis_plus)
    if not (Qm.shape == Qp.shape == metric_minus.shape == metric_plus.shape):
        raise ValueError("endpoint residual and metric dimensions must match")
    dA = sp.simplify(synthesis_plus - synthesis_minus)
    Mbar = sp.simplify((metric_plus + metric_minus) / 2)
    Qbar = sp.simplify((Qp + Qm) / 2)
    dM = sp.simplify(metric_plus - metric_minus)
    geometry = sp.simplify(sp.trace(Qbar * dM))
    left = sp.simplify(sp.trace(Mbar * dA * library_second_moment * synthesis_minus.T))
    right = sp.simplify(sp.trace(Mbar * synthesis_minus * library_second_moment * dA.T))
    quad = sp.simplify(sp.trace(Mbar * dA * library_second_moment * dA.T))
    jump = sp.simplify(sp.trace(metric_plus * Qp) - sp.trace(metric_minus * Qm))
    return SelectorResetFaces(geometry, left, right, quad, jump)


def selector_reset_weighted_residual(
    library_second_moment: Matrix,
    synthesis_minus: Matrix,
    synthesis_plus: Matrix,
    metric_minus: Matrix,
    metric_plus: Matrix,
) -> sp.Expr:
    faces = selector_reset_weighted_faces(
        library_second_moment, synthesis_minus, synthesis_plus, metric_minus, metric_plus
    )
    return sp.simplify(faces.total_jump - faces.reconstructed)


def selector_reset_excursion_residual(
    library_second_moment: Matrix,
    syntheses: Sequence[Matrix],
    metrics: Sequence[Matrix],
) -> sp.Expr:
    """Finite reset telescope for a frozen library over a selector excursion."""
    if len(syntheses) != len(metrics) or len(syntheses) < 2:
        raise ValueError("matching endpoint synthesis/metric sequence of length at least two required")
    event_sum = sp.Integer(0)
    for j in range(len(syntheses)-1):
        faces = selector_reset_weighted_faces(
            library_second_moment, syntheses[j], syntheses[j+1], metrics[j], metrics[j+1]
        )
        event_sum += faces.reconstructed
    Q0 = synthesized_second_moment(library_second_moment, syntheses[0])
    QN = synthesized_second_moment(library_second_moment, syntheses[-1])
    endpoint = sp.simplify(sp.trace(metrics[-1]*QN)-sp.trace(metrics[0]*Q0))
    return sp.simplify(endpoint-event_sum)


def selector_excursion_pair_face_sums(
    library_second_moment: Matrix,
    syntheses: Sequence[Matrix],
    metrics: Sequence[Matrix],
) -> tuple[sp.Expr,sp.Expr,sp.Expr,sp.Expr]:
    if len(syntheses) != len(metrics) or len(syntheses) < 2:
        raise ValueError("matching endpoint synthesis/metric sequence of length at least two required")
    geometry=left=right=quad=sp.Integer(0)
    for j in range(len(syntheses)-1):
        faces=selector_reset_weighted_faces(
            library_second_moment,syntheses[j],syntheses[j+1],metrics[j],metrics[j+1]
        )
        geometry += faces.geometry
        left += faces.pair_left
        right += faces.pair_right
        quad += faces.pair_quadratic
    return tuple(sp.simplify(x) for x in (geometry,left,right,quad))


def one_mode_half_period_lineage_calibration(
    time: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> dict[str, sp.Expr | Matrix]:
    """Exact NS half-period children: residuals are opposite on a common isotropic frame."""
    Y = sp.symbols("Y_lineage", real=True)
    side = sp.pi / (2 * k)
    chi = one_mode_asymmetric_codeforming_residual(Y, time, side, nu, k)
    chi0 = sp.simplify(chi.subs(Y, 0))
    chi1 = sp.simplify(chi.subs(Y, sp.pi / k))
    v = sp.Matrix([0, 0, chi0, 0, 0, chi1])
    Qlib = sp.simplify(v * v.T)
    Pz = sp.diag(0, 0, 1)
    lam = sp.simplify(side**2)
    coeffs = [sp.Integer(1), sp.Integer(1)]
    full_channel = spectral_synthesis_channel(Qlib, coeffs, lam, Pz)
    diag_channel = diagonal_only_spectral_channel(Qlib, coeffs, lam, Pz)
    A0 = germ_extraction_map(2, 0)
    A1 = germ_extraction_map(2, 1)
    M = sp.simplify(lam * sp.eye(3))
    reset = selector_reset_weighted_faces(Qlib, A0, A1, M, M)
    return {
        "side": side,
        "chi0": chi0,
        "chi1": chi1,
        "opposite_residual_zero": sp.simplify(chi0 + chi1),
        "library_second_moment": Qlib,
        "full_parent_channel": full_channel,
        "diagonal_parent_channel": diag_channel,
        "cross_child_channel": sp.simplify(full_channel - diag_channel),
        "reset_total_jump": reset.total_jump,
        "reset_pair_left": reset.pair_left,
        "reset_pair_right": reset.pair_right,
        "reset_pair_quadratic": reset.pair_quadratic,
        "reset_reconstruction_residual": sp.simplify(reset.total_jump - reset.reconstructed),
    }
