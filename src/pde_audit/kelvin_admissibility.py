"""Exact admissibility calculus for CK operations acting on Kelvin currents.

Kelvin circulation is evaluated on closed physical currents.  This module audits
an additional linear or differentiable CK realization at that physical type,
without assuming idempotency.  The key dichotomy is exact:

* a cycle-preserving operation remains inside the Kelvin current space and its
  motion is coefficient/connection/reset work;
* a cycle-breaking operation exposes exact pressure/gauge forms through its
  physical boundary and must therefore be classified as an interface/open-current
  or exit operation, not as an internal Kelvin producer.

All finite-chain identities use exact SymPy algebra.  No norm estimate enters.
"""
from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from .active_pair import pair_boundary, pair_lift


Matrix = sp.MatrixBase


def realized_operator(H: Matrix, K: Matrix) -> sp.Matrix:
    """Restrict an ambient current operator H to a Kelvin cycle library K."""
    return sp.simplify(H * K)


def restricted_physical_boundary(B: Matrix, H: Matrix, K: Matrix) -> sp.Matrix:
    """Physical boundary B H K seen by the admissible Kelvin library."""
    return sp.simplify(B * H * K)


def restricted_pair_boundary(B: Matrix, H: Matrix, K: Matrix) -> sp.Matrix:
    """Full ordered-pair physical boundary of the realized operation H K."""
    Y = realized_operator(H, K)
    return sp.simplify(pair_boundary(B) * pair_lift(Y))


def exact_gauge_work(p: Matrix, B: Matrix, Z: Matrix) -> sp.Expr:
    """Finite-chain Stokes pairing <d p,Z>=<p,BZ>."""
    if p.cols != 1 or Z.cols != 1:
        raise ValueError("p and Z must be column vectors")
    return sp.simplify((p.T * B * Z)[0])


def canonical_boundary_gauge_witness(B: Matrix, Z: Matrix) -> sp.Expr:
    """Choose p=BZ, yielding the exact Euclidean witness (BZ)^T(BZ)."""
    b = sp.simplify(B * Z)
    return sp.simplify((b.T * b)[0])


@dataclass(frozen=True)
class CycleFactorization:
    coordinates: sp.Matrix
    residual: sp.Matrix


def factor_through_cycle_library(K: Matrix, Y: Matrix) -> CycleFactorization:
    """Exact coordinates of Y in span(K), with an explicit residual.

    K must have linearly independent columns.  If residual=0 then the operation
    has become a pure coefficient map on the chosen closed-cycle library.
    """
    gram = sp.simplify(K.T * K)
    if gram.det() == 0:
        raise ValueError("cycle library columns must be linearly independent")
    L = sp.simplify(gram.inv() * K.T * Y)
    return CycleFactorization(coordinates=L, residual=sp.simplify(Y - K * L))


def full_pair_factorization_residual(K: Matrix, L: Matrix) -> sp.Matrix:
    """Check (K L)^(2) = K^(2) L^(2) with the full tensor-square lift."""
    return sp.simplify(
        pair_lift(K * L) - pair_lift(K) * pair_lift(L)
    )


@dataclass(frozen=True)
class OperatorTransportDecomposition:
    total: sp.Matrix
    operator_motion: sp.Matrix
    input_realization: sp.Matrix

    @property
    def reconstructed(self) -> sp.Matrix:
        return sp.simplify(self.operator_motion + self.input_realization)


def operator_transport_decomposition(
    T_out: Matrix,
    H: Matrix,
    T_mid: Matrix,
    K: Matrix,
    A_germ: Matrix,
    Hdot: Matrix | None = None,
    Kdot: Matrix | None = None,
) -> OperatorTransportDecomposition:
    """Exact covariant product rule for Y=H K.

    G_Y = d(HK) + T_out H K - H K A_germ
        = (dH + T_out H - H T_mid) K
          + H (dK + T_mid K - K A_germ).
    """
    if Hdot is None:
        Hdot = sp.zeros(*H.shape)
    if Kdot is None:
        Kdot = sp.zeros(*K.shape)
    Y = H * K
    Ydot = Hdot * K + H * Kdot
    total = sp.simplify(Ydot + T_out * Y - Y * A_germ)
    G_H = sp.simplify(Hdot + T_out * H - H * T_mid)
    G_K = sp.simplify(Kdot + T_mid * K - K * A_germ)
    return OperatorTransportDecomposition(
        total=total,
        operator_motion=sp.simplify(G_H * K),
        input_realization=sp.simplify(H * G_K),
    )


def nonlinear_cycle_tangent_boundary(B: Matrix, J_phi: Matrix) -> sp.Matrix:
    """Boundary of the differential of a differentiable cycle-valued map."""
    return sp.simplify(B * J_phi)


def pair_curve_derivative(Z: Matrix, Zdot: Matrix) -> sp.Matrix:
    """Leibniz derivative of Z tensor Z along any differentiable current curve."""
    return sp.simplify(
        sp.kronecker_product(Zdot, Z) + sp.kronecker_product(Z, Zdot)
    )


def pair_curve_boundary(B: Matrix, Z: Matrix, Zdot: Matrix) -> sp.Matrix:
    """Physical pair boundary of d(Z tensor Z)/ds."""
    return sp.simplify(pair_boundary(B) * pair_curve_derivative(Z, Zdot))
