"""Exact algebra for active first-bad-germ maps on the pair world-sheet.

The point of this module is deliberately narrow.  It does *not* declare the
repository's unresolved active CK/Pillar-II projection to be functorial.  Instead
it gives exact matrix identities that reduce every full-pair boundary/transport
residual to the corresponding one-current commutator.

All matrices are SymPy matrices, so the audit is symbolic/exact rather than a
floating-point stress test.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

import sympy as sp


Matrix = sp.MatrixBase


def pair_lift(F: Matrix) -> sp.Matrix:
    """Full ordered pair lift F^(2)=F tensor F."""
    return sp.kronecker_product(F, F)


def pair_boundary(B: Matrix) -> sp.Matrix:
    """Boundary on C_1 tensor C_1 -> (C_0 tensor C_1) direct-sum (C_1 tensor C_0).

    With degree-one factors,

        partial_pair = [ partial tensor I ; - I tensor partial ].

    Keeping the two faces in a direct sum prevents an artificial cancellation
    between the first- and second-replica physical faces.
    """
    n0, n1 = B.shape
    I1 = sp.eye(n1)
    top = sp.kronecker_product(B, I1)
    bottom = -sp.kronecker_product(I1, B)
    return top.col_join(bottom)


def pair_boundary_map(F0: Matrix, F1: Matrix) -> sp.Matrix:
    """Map induced on the two ordered pair-boundary faces."""
    top = sp.kronecker_product(F0, F1)
    bottom = sp.kronecker_product(F1, F0)
    ztr = sp.zeros(top.rows, bottom.cols)
    zbl = sp.zeros(bottom.rows, top.cols)
    return top.row_join(ztr).col_join(zbl.row_join(bottom))


def boundary_residual(B_out: Matrix, F1: Matrix, F0: Matrix, B_in: Matrix) -> sp.Matrix:
    """One-current chain-map defect: partial_out F1 - F0 partial_in."""
    return sp.simplify(B_out * F1 - F0 * B_in)


def pair_boundary_residual(B_out: Matrix, F1: Matrix, F0: Matrix, B_in: Matrix) -> sp.Matrix:
    """Full-pair chain-map defect for the tensor-square lift."""
    return sp.simplify(
        pair_boundary(B_out) * pair_lift(F1)
        - pair_boundary_map(F0, F1) * pair_boundary(B_in)
    )


def factorized_pair_boundary_residual(C: Matrix, F1: Matrix) -> sp.Matrix:
    """Two-face factorization of the full-pair boundary residual.

    If C = partial_out F1 - F0 partial_in, then exactly

        C_pair = [ C tensor F1 ; - F1 tensor C ].
    """
    return sp.kronecker_product(C, F1).col_join(
        -sp.kronecker_product(F1, C)
    )


def transport_residual(
    T_out: Matrix,
    F: Matrix,
    T_in: Matrix,
    Fdot: Matrix | None = None,
) -> sp.Matrix:
    """Covariant transport defect (d_s+T_out)F - F(d_s+T_in)."""
    if Fdot is None:
        Fdot = sp.zeros(*F.shape)
    return sp.simplify(Fdot + T_out * F - F * T_in)


def pair_transport_generator(T: Matrix) -> sp.Matrix:
    """Ordered-pair transport generator T^(2)=T tensor I + I tensor T."""
    n, m = T.shape
    if n != m:
        raise ValueError("pair transport generator requires a square matrix")
    I = sp.eye(n)
    return sp.kronecker_product(T, I) + sp.kronecker_product(I, T)


def pair_transport_residual(
    T_out: Matrix,
    F: Matrix,
    T_in: Matrix,
    Fdot: Matrix | None = None,
) -> sp.Matrix:
    """Full-pair covariant transport defect for F tensor F."""
    if Fdot is None:
        Fdot = sp.zeros(*F.shape)
    F2dot = sp.kronecker_product(Fdot, F) + sp.kronecker_product(F, Fdot)
    return sp.simplify(
        F2dot
        + pair_transport_generator(T_out) * pair_lift(F)
        - pair_lift(F) * pair_transport_generator(T_in)
    )


def factorized_pair_transport_residual(G: Matrix, F: Matrix) -> sp.Matrix:
    """Exact factorization G tensor F + F tensor G of pair transport defect."""
    return sp.simplify(
        sp.kronecker_product(G, F) + sp.kronecker_product(F, G)
    )


@dataclass(frozen=True)
class ChainStage:
    """One stage of a literal first-bad-germ chain map.

    F1 acts on degree-one physical currents and F0 on their degree-zero boundary
    data.  B_in/B_out are the literal boundary matrices on the two sides of the
    stage.  `physical_type` is a research classification, not a theorem label.
    """

    name: str
    physical_type: str
    B_in: Matrix
    B_out: Matrix
    F1: Matrix
    F0: Matrix

    def boundary_residual(self) -> sp.Matrix:
        return boundary_residual(self.B_out, self.F1, self.F0, self.B_in)

    def pair_boundary_residual(self) -> sp.Matrix:
        return pair_boundary_residual(self.B_out, self.F1, self.F0, self.B_in)


def compose_chain_stages(stages: Sequence[ChainStage]) -> tuple[sp.Matrix, sp.Matrix]:
    """Return (F1_total,F0_total) in chronological order."""
    if not stages:
        raise ValueError("at least one stage is required")
    F1 = sp.eye(stages[0].B_in.cols)
    F0 = sp.eye(stages[0].B_in.rows)
    current_B = stages[0].B_in
    for stage in stages:
        if stage.B_in.shape != current_B.shape or stage.B_in != current_B:
            raise ValueError(f"boundary mismatch before stage {stage.name}")
        F1 = stage.F1 * F1
        F0 = stage.F0 * F0
        current_B = stage.B_out
    return sp.simplify(F1), sp.simplify(F0)


def transported_stage_boundary_sum(stages: Sequence[ChainStage]) -> sp.Matrix:
    """Leibniz expansion of the completed-excursion one-current residual.

    For G after F,

        C(GF)=C(G)F1 + G0 C(F).

    Iterating gives every stage seam transported to the final boundary space.
    This is the literal line-by-line algebra behind the longitudinal world-sheet
    seam sum.
    """
    if not stages:
        raise ValueError("at least one stage is required")

    # prefix current map into each stage's input
    prefixes: list[sp.Matrix] = []
    prefix = sp.eye(stages[0].B_in.cols)
    for stage in stages:
        prefixes.append(prefix)
        prefix = stage.F1 * prefix

    # suffix boundary map from each stage's output to the final boundary space
    suffixes: list[sp.Matrix] = [sp.zeros(0, 0)] * len(stages)
    suffix = sp.eye(stages[-1].B_out.rows)
    for k in range(len(stages) - 1, -1, -1):
        suffixes[k] = suffix
        suffix = suffix * stages[k].F0

    total = sp.zeros(stages[-1].B_out.rows, stages[0].B_in.cols)
    for stage, pre, post in zip(stages, prefixes, suffixes):
        total += post * stage.boundary_residual() * pre
    return sp.simplify(total)


def completed_boundary_residual(stages: Sequence[ChainStage]) -> sp.Matrix:
    """Direct completed-excursion chain defect."""
    F1, F0 = compose_chain_stages(stages)
    return boundary_residual(stages[-1].B_out, F1, F0, stages[0].B_in)


def completed_pair_boundary_residual(stages: Sequence[ChainStage]) -> sp.Matrix:
    """Direct full-pair boundary defect of the completed excursion."""
    F1, F0 = compose_chain_stages(stages)
    return pair_boundary_residual(stages[-1].B_out, F1, F0, stages[0].B_in)


def transported_stage_pair_boundary_sum(stages: Sequence[ChainStage]) -> sp.Matrix:
    """Line-by-line transported pair seam sum for a completed excursion."""
    if not stages:
        raise ValueError("at least one stage is required")

    prefixes: list[sp.Matrix] = []
    prefix = sp.eye(stages[0].B_in.cols ** 2)
    for stage in stages:
        prefixes.append(prefix)
        prefix = pair_lift(stage.F1) * prefix

    final_n0 = stages[-1].B_out.rows
    final_n1 = stages[-1].B_out.cols
    suffixes: list[sp.Matrix] = [sp.zeros(0, 0)] * len(stages)
    suffix = sp.eye(2 * final_n0 * final_n1)
    for k in range(len(stages) - 1, -1, -1):
        suffixes[k] = suffix
        suffix = suffix * pair_boundary_map(stages[k].F0, stages[k].F1)

    rows = 2 * final_n0 * final_n1
    cols = stages[0].B_in.cols ** 2
    total = sp.zeros(rows, cols)
    for stage, pre, post in zip(stages, prefixes, suffixes):
        total += post * stage.pair_boundary_residual() * pre
    return sp.simplify(total)


def interval_boundary(edge_count: int) -> sp.Matrix:
    """Exact oriented boundary matrix for a subdivided interval."""
    if edge_count <= 0:
        raise ValueError("edge_count must be positive")
    B = sp.zeros(edge_count + 1, edge_count)
    for j in range(edge_count):
        B[j, j] = -1
        B[j + 1, j] = 1
    return B


def interval_refinement_map(edge_count: int, parts: int = 2) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    """Literal linear subdivision map and refined interval boundary.

    Each coarse edge is the signed sum of `parts` consecutive fine edges.  The
    vertex map sends coarse vertices to the corresponding fine endpoints.
    Returns (B_fine,R1,R0), and satisfies B_fine R1 = R0 B_coarse exactly.
    """
    if edge_count <= 0 or parts <= 0:
        raise ValueError("edge_count and parts must be positive")
    fine_edges = edge_count * parts
    Bfine = interval_boundary(fine_edges)
    R1 = sp.zeros(fine_edges, edge_count)
    for j in range(edge_count):
        for r in range(parts):
            R1[j * parts + r, j] = 1
    R0 = sp.zeros(fine_edges + 1, edge_count + 1)
    for j in range(edge_count + 1):
        R0[j * parts, j] = 1
    return Bfine, R1, R0


def interval_orientation_reversal(edge_count: int) -> tuple[sp.Matrix, sp.Matrix]:
    """Chain automorphism reversing interval orientation."""
    F1 = sp.zeros(edge_count, edge_count)
    for j in range(edge_count):
        F1[edge_count - 1 - j, j] = -1
    F0 = sp.zeros(edge_count + 1, edge_count + 1)
    for j in range(edge_count + 1):
        F0[edge_count - j, j] = 1
    return F1, F0


def interval_block_projection(
    edge_count: int, start_edge: int, stop_edge: int
) -> tuple[sp.Matrix, sp.Matrix]:
    """Restriction to the contiguous edge block [start_edge, stop_edge).

    Its chain-map defect is supported only on the block interfaces.  This is the
    finite-cell analogue of a quantile/shell restriction whose distributional
    boundary carries the localization flux.
    """
    if not (0 <= start_edge <= stop_edge <= edge_count):
        raise ValueError("require 0 <= start_edge <= stop_edge <= edge_count")
    P1 = sp.zeros(edge_count, edge_count)
    for j in range(start_edge, stop_edge):
        P1[j, j] = 1
    P0 = sp.zeros(edge_count + 1, edge_count + 1)
    if start_edge < stop_edge:
        for j in range(start_edge, stop_edge + 1):
            P0[j, j] = 1
    return P1, P0


def interval_cut_projection(edge_count: int, keep_edges: int) -> tuple[sp.Matrix, sp.Matrix]:
    """Restriction to the first `keep_edges` interval edges."""
    if keep_edges == 0:
        return sp.zeros(edge_count, edge_count), sp.zeros(edge_count + 1, edge_count + 1)
    return interval_block_projection(edge_count, 0, keep_edges)


def matrix_is_zero(M: Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in M)


def nonzero_entries(M: Matrix) -> list[tuple[int, int, sp.Expr]]:
    out: list[tuple[int, int, sp.Expr]] = []
    for i in range(M.rows):
        for j in range(M.cols):
            x = sp.simplify(M[i, j])
            if x != 0:
                out.append((i, j, x))
    return out
