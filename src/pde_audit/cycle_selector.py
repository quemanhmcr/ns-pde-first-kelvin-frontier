"""Exact algebra for a first-bad selector typed on closed Kelvin cycles.

The selected Kelvin observable is defined on closed physical currents.  Therefore
an active selector should first be typed on a library of cycle atoms and only then
realized in the ambient physical current complex.  This module separates that
intrinsic selector from arbitrary off-cycle extensions.

All matrix identities are exact SymPy identities.  No norm or estimate enters.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import sympy as sp

from .active_pair import pair_boundary, pair_lift, transport_residual


Matrix = sp.MatrixBase


def cycle_library_boundary(B: Matrix, K: Matrix) -> sp.Matrix:
    """Physical boundary of the cycle library columns."""
    return sp.simplify(B * K)


def cycle_span_projector(K: Matrix) -> sp.Matrix:
    """Canonical exact projector onto the span of independent cycle columns.

    This Euclidean finite-chain projector is only an incidence witness.  The key
    structural fact is range(P) subset span(K) subset ker(B), so its output is a
    closed physical current.
    """
    gram = sp.simplify(K.T * K)
    if gram.det() == 0:
        raise ValueError("cycle library columns must be linearly independent")
    return sp.simplify(K * gram.inv() * K.T)


def selected_cycle_map(K: Matrix, M: Matrix) -> sp.Matrix:
    """Realize a state-dependent germ-space selector in physical current space."""
    return sp.simplify(K * M)


def cycle_selector_boundary_residual(B: Matrix, K: Matrix, M: Matrix) -> sp.Matrix:
    """Intrinsic physical-boundary residual of a cycle-typed selector.

    The germ coefficient complex has zero *physical* boundary.  Hence the typed
    residual is simply

        B (K M) = (B K) M.

    In particular, if every candidate Kelvin current is closed (B K = 0), no
    choice of first-bad support M can manufacture a physical-current boundary.
    """
    return sp.simplify(B * K * M)


def cycle_selector_pair_boundary_residual(B: Matrix, K: Matrix, M: Matrix) -> sp.Matrix:
    """Two-face physical boundary of the full pair-selected cycle map."""
    P = selected_cycle_map(K, M)
    return sp.simplify(pair_boundary(B) * pair_lift(P))


def restricted_ambient_commutator(
    B_out: Matrix,
    F1: Matrix,
    F0: Matrix,
    B_in: Matrix,
    K: Matrix,
) -> sp.Matrix:
    """Ambient chain commutator restricted to the physically admissible library.

    Global values of B_out F1 - F0 B_in away from the cycle library depend on how
    an active map is extended to chains that are never selected.  The intrinsic
    residual is its action on K.
    """
    return sp.simplify((B_out * F1 - F0 * B_in) * K)


def incidence_mask_commutator(
    B: Matrix,
    edge_activity: Sequence[int | sp.Expr],
    vertex_activity: Sequence[int | sp.Expr],
) -> sp.Matrix:
    """Boundary commutator of a literal support mask on a one-complex."""
    if len(edge_activity) != B.cols or len(vertex_activity) != B.rows:
        raise ValueError("activity masks must match the boundary matrix")
    P1 = sp.diag(*edge_activity)
    P0 = sp.diag(*vertex_activity)
    return sp.simplify(B * P1 - P0 * B)


def incidence_cut_formula(
    B: Matrix,
    edge_activity: Sequence[int | sp.Expr],
    vertex_activity: Sequence[int | sp.Expr],
) -> sp.Matrix:
    """Entrywise cut-current formula B_ve (chi_e-chi_v)."""
    if len(edge_activity) != B.cols or len(vertex_activity) != B.rows:
        raise ValueError("activity masks must match the boundary matrix")
    return sp.Matrix(
        B.rows,
        B.cols,
        lambda v, e: sp.simplify(B[v, e] * (edge_activity[e] - vertex_activity[v])),
    )


def germ_support_transport_commutator(
    A: Matrix, activity: Sequence[int | sp.Expr]
) -> sp.Matrix:
    """Transport commutator A M - M A for a diagonal germ support mask."""
    if A.rows != A.cols or len(activity) != A.rows:
        raise ValueError("activity mask must match a square germ generator")
    M = sp.diag(*activity)
    return sp.simplify(A * M - M * A)


def germ_cut_formula(A: Matrix, activity: Sequence[int | sp.Expr]) -> sp.Matrix:
    """Entrywise germ-interface flux A_ij (chi_j-chi_i)."""
    if A.rows != A.cols or len(activity) != A.rows:
        raise ValueError("activity mask must match a square germ generator")
    return sp.Matrix(
        A.rows,
        A.cols,
        lambda i, j: sp.simplify(A[i, j] * (activity[j] - activity[i])),
    )


def first_bad_index(bad_flags: Sequence[bool]) -> int | None:
    """First active germ in the prescribed priority order, or None."""
    return next((i for i, bad in enumerate(bad_flags) if bad), None)


def rank_one_selector(size: int, index: int | None) -> sp.Matrix:
    """Exact diagonal rank-one support projector (zero if no germ is active)."""
    if size < 0:
        raise ValueError("size must be nonnegative")
    M = sp.zeros(size, size)
    if index is not None:
        if not 0 <= index < size:
            raise ValueError("selector index out of range")
        M[index, index] = 1
    return M


def first_bad_projection(bad_flags: Sequence[bool]) -> sp.Matrix:
    """Canonical support projection forced by first-bad priority semantics."""
    return rank_one_selector(len(bad_flags), first_bad_index(bad_flags))


def hysteretic_first_bad_projection(
    bad_flags: Sequence[bool],
    previous_index: int | None,
    resolved: bool,
) -> tuple[sp.Matrix, int | None]:
    """Freeze the active germ until resolve; then choose the new first bad germ."""
    n = len(bad_flags)
    if previous_index is not None and not 0 <= previous_index < n:
        raise ValueError("previous selector index out of range")
    if previous_index is not None and not resolved:
        index = previous_index
    else:
        index = first_bad_index(bad_flags)
    return rank_one_selector(n, index), index


@dataclass(frozen=True)
class SelectorTransportDecomposition:
    total: sp.Matrix
    realization: sp.Matrix
    support: sp.Matrix


def selector_transport_decomposition(
    T_physical: Matrix,
    K: Matrix,
    A_germ: Matrix,
    M: Matrix,
    Kdot: Matrix | None = None,
    Mdot: Matrix | None = None,
) -> SelectorTransportDecomposition:
    """Exact covariant product rule for P_act = K M.

    With
        G_K = Kdot + T_physical K - K A_germ,
        G_M = Mdot + A_germ M - M A_germ,
    one has exactly
        G_{K M} = G_K M + K G_M.

    The first term is realization/connection geometry.  The second is selector
    support transport (continuous interface crossing on frozen-coordinate charts).
    Finite hysteresis jumps are handled by ``pair_jump_decomposition`` below.
    """
    if Kdot is None:
        Kdot = sp.zeros(*K.shape)
    if Mdot is None:
        Mdot = sp.zeros(*M.shape)
    P = K * M
    Pdot = Kdot * M + K * Mdot
    total = transport_residual(T_physical, P, A_germ, Pdot)
    G_K = transport_residual(T_physical, K, A_germ, Kdot)
    G_M = transport_residual(A_germ, M, A_germ, Mdot)
    realization = sp.simplify(G_K * M)
    support = sp.simplify(K * G_M)
    return SelectorTransportDecomposition(
        total=sp.simplify(total),
        realization=realization,
        support=support,
    )


@dataclass(frozen=True)
class PairJumpDecomposition:
    total: sp.Matrix
    linear_left: sp.Matrix
    linear_right: sp.Matrix
    quadratic: sp.Matrix

    @property
    def reconstructed(self) -> sp.Matrix:
        return sp.simplify(self.linear_left + self.linear_right + self.quadratic)


def pair_jump_decomposition(P_minus: Matrix, P_plus: Matrix) -> PairJumpDecomposition:
    """Exact finite reset law for a tensor-square selected map.

    For Delta=P_plus-P_minus,

      P_plus⊗P_plus - P_minus⊗P_minus
      = Delta⊗P_minus + P_minus⊗Delta + Delta⊗Delta.

    This is the current-level origin of the signed covariance reset identity.
    """
    if P_minus.shape != P_plus.shape:
        raise ValueError("jump endpoints must have the same shape")
    delta = P_plus - P_minus
    total = sp.simplify(pair_lift(P_plus) - pair_lift(P_minus))
    left = sp.kronecker_product(delta, P_minus)
    right = sp.kronecker_product(P_minus, delta)
    quadratic = sp.kronecker_product(delta, delta)
    return PairJumpDecomposition(
        total=total,
        linear_left=sp.simplify(left),
        linear_right=sp.simplify(right),
        quadratic=sp.simplify(quadratic),
    )


def two_cycle_library() -> tuple[sp.Matrix, sp.Matrix]:
    """A tiny exact graph carrying two independent closed cycle atoms.

    The graph consists of two pairs of parallel oriented edges.  The cycle atoms
    are their signed differences.  It is deliberately minimal and used only as an
    incidence witness for the typed-selector identities.
    """
    B = sp.Matrix(
        [
            [-1, -1, 0, 0],
            [1, 1, -1, -1],
            [0, 0, 1, 1],
        ]
    )
    K = sp.Matrix(
        [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
        ]
    )
    return B, K
