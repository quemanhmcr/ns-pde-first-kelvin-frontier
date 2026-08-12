"""Exact finite-chain calculus for Hodge/cycle projectors.

This module audits a possible *additional* CK/Hodge operator under the precise
hypothesis that it is an idempotent projector whose range lies in the closed
physical-current subspace.  It does not identify any repository object with that
operator; the identification remains a separate literal bridge.
"""
from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


Matrix = sp.MatrixBase


def weighted_cycle_projector(K: Matrix, W: Matrix) -> sp.Matrix:
    """W-orthogonal projector onto span(K).

    H = K (K^T W K)^(-1) K^T W.
    """
    if W.rows != W.cols or W.rows != K.rows:
        raise ValueError("W must be square on the ambient current space")
    gram = sp.simplify(K.T * W * K)
    if gram.rows != gram.cols or gram.det() == 0:
        raise ValueError("weighted cycle Gram matrix must be invertible")
    return sp.simplify(K * gram.inv() * K.T * W)


def projector_idempotency_residual(P: Matrix) -> sp.Matrix:
    return sp.simplify(P * P - P)


def projector_tangent_residual(P: Matrix, G: Matrix) -> sp.Matrix:
    """Derivative of P^2=P: G P + P G - G."""
    return sp.simplify(G * P + P * G - G)


@dataclass(frozen=True)
class ProjectorMotionBlocks:
    active_internal: sp.Matrix
    inactive_internal: sp.Matrix
    active_to_inactive: sp.Matrix
    inactive_to_active: sp.Matrix

    @property
    def transfer_sum(self) -> sp.Matrix:
        return sp.simplify(self.active_to_inactive + self.inactive_to_active)


def projector_motion_blocks(P: Matrix, G: Matrix) -> ProjectorMotionBlocks:
    """Decompose a projector derivative relative to P and Q=I-P."""
    if P.rows != P.cols or G.shape != P.shape:
        raise ValueError("P and G must be square matrices of the same size")
    Q = sp.eye(P.rows) - P
    return ProjectorMotionBlocks(
        active_internal=sp.simplify(P * G * P),
        inactive_internal=sp.simplify(Q * G * Q),
        active_to_inactive=sp.simplify(P * G * Q),
        inactive_to_active=sp.simplify(Q * G * P),
    )


def covariant_projector_derivative(P: Matrix, T: Matrix, Pdot: Matrix | None = None) -> sp.Matrix:
    """D P = Pdot + [T,P] for a connection/transport generator T."""
    if Pdot is None:
        Pdot = sp.zeros(*P.shape)
    return sp.simplify(Pdot + T * P - P * T)


def pair_projector_derivative(P: Matrix, G: Matrix) -> sp.Matrix:
    """Exact tensor-square derivative G⊗P + P⊗G."""
    return sp.simplify(sp.kronecker_product(G, P) + sp.kronecker_product(P, G))
