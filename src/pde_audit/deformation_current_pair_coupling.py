"""Exact coupling algebra between stochastic Cauchy deformation and Kelvin currents.

The physical typing is deliberately strict.

* ``D`` is the reverse-age Cauchy deformation.  Its forward tangent map is
  ``F=D.T`` and has pathwise finite variation.
* A Kelvin chain/selector lives in a chain or germ coefficient factor.
* Spatial deformation lives in a separate Euclidean tangent factor.

Therefore the literal local coupling is a tensor product, not an identification of
those two factors.  This module records exact boundary, pair, covariance, and
cochain-projection identities for that product.  It does not claim that the full
finite-loop Kelvin state descends to ``D``: exact Navier--Stokes shape calibrations
show that it does not in general.
"""
from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from .active_pair import pair_boundary, pair_lift
from .stochastic_cauchy_deformation import column_vectorize

Matrix = sp.MatrixBase


def forward_tangent_deformation(deformation: Matrix) -> sp.Matrix:
    """Forward tangent map dual to the reverse-age Cauchy matrix: F=D^T."""
    if deformation.rows != deformation.cols:
        raise ValueError("deformation must be square")
    return sp.simplify(deformation.T)


def spatial_fiber_boundary(boundary: Matrix, spatial_dim: int) -> sp.Matrix:
    """Boundary acting on chain index while leaving the spatial tangent fiber intact."""
    if spatial_dim <= 0:
        raise ValueError("spatial_dim must be positive")
    return sp.kronecker_product(boundary, sp.eye(spatial_dim))


def spatial_fiber_current_map(current_map: Matrix, deformation: Matrix) -> sp.Matrix:
    """Selected/current map on chain index tensor forward tangent deformation."""
    return sp.kronecker_product(current_map, forward_tangent_deformation(deformation))


def spatial_fiber_boundary_factorization_residual(
    boundary: Matrix,
    current_map: Matrix,
    deformation: Matrix,
) -> sp.Matrix:
    """Audit (B⊗I)(P⊗D^T)=(BP)⊗D^T exactly.

    Hence a closed selected current cannot acquire a physical boundary merely from
    Cauchy deformation of its spatial tangent fiber.
    """
    n = deformation.rows
    lhs = spatial_fiber_boundary(boundary, n) * spatial_fiber_current_map(current_map, deformation)
    rhs = sp.kronecker_product(boundary * current_map, forward_tangent_deformation(deformation))
    return sp.simplify(lhs - rhs)


def spatial_fiber_pair_boundary_factorization_residual(
    boundary: Matrix,
    current_map: Matrix,
    deformation: Matrix,
) -> sp.Matrix:
    """Two-replica version of spatial-fiber boundary factorization.

    The pair boundary has two physical faces.  If C=(B⊗I)T then

        ∂pair (T⊗T) = [C⊗T ; -T⊗C].

    Thus deformation itself creates no pair boundary seam when BP=0.
    """
    n = deformation.rows
    Bf = spatial_fiber_boundary(boundary, n)
    T = spatial_fiber_current_map(current_map, deformation)
    C = sp.simplify(Bf * T)
    direct = sp.simplify(pair_boundary(Bf) * pair_lift(T))
    factorized = sp.kronecker_product(C, T).col_join(-sp.kronecker_product(T, C))
    return sp.simplify(direct - factorized)


def tangent_observation_map(reference_tangent: Matrix) -> sp.Matrix:
    """L_e with D^T e=L_e vec(D), using column-major vec(D)."""
    if reference_tangent.cols != 1:
        raise ValueError("reference_tangent must be a column vector")
    n = reference_tangent.rows
    return sp.kronecker_product(sp.eye(n), reference_tangent.T)


def tangent_projection_residual(deformation: Matrix, reference_tangent: Matrix) -> sp.Matrix:
    """Audit D^T e=(I⊗e^T)vec(D)."""
    L = tangent_observation_map(reference_tangent)
    return sp.simplify(
        forward_tangent_deformation(deformation) * reference_tangent
        - L * column_vectorize(deformation)
    )


def tangent_deformation_cross_covariance(
    vectorized_covariance: Matrix,
    left_tangent: Matrix,
    right_tangent: Matrix,
) -> sp.Matrix:
    """Cov(D^T e,D^T f)=L_e Sigma_D L_f^T for fixed reference tangents."""
    Le = tangent_observation_map(left_tangent)
    Lf = tangent_observation_map(right_tangent)
    if vectorized_covariance.shape != (Le.cols, Lf.cols):
        raise ValueError("vectorized covariance dimension mismatch")
    return sp.simplify(Le * vectorized_covariance * Lf.T)


def tangent_deformation_covariance(
    vectorized_covariance: Matrix,
    reference_tangent: Matrix,
) -> sp.Matrix:
    return tangent_deformation_cross_covariance(
        vectorized_covariance, reference_tangent, reference_tangent
    )


def tangent_carre_du_champ(
    vectorized_carre_du_champ: Matrix,
    reference_tangent: Matrix,
) -> sp.Matrix:
    """Projected finite-horizon covariance source on a fixed material tangent."""
    return tangent_deformation_covariance(vectorized_carre_du_champ, reference_tangent)


def tangent_cochain_readout_vector(reference_tangent: Matrix, cochain: Matrix) -> sp.Matrix:
    """ell=cochain⊗tangent for alpha^T D^T e = ell^T vec(D)."""
    if reference_tangent.cols != 1 or cochain.cols != 1:
        raise ValueError("tangent and cochain must be column vectors")
    if reference_tangent.rows != cochain.rows:
        raise ValueError("tangent/cochain spatial dimensions must match")
    return sp.kronecker_product(cochain, reference_tangent)


def tangent_cochain_readout_residual(
    deformation: Matrix,
    reference_tangent: Matrix,
    cochain: Matrix,
) -> sp.Expr:
    """Audit alpha^T D^T e=(alpha⊗e)^T vec(D)."""
    ell = tangent_cochain_readout_vector(reference_tangent, cochain)
    lhs = (cochain.T * forward_tangent_deformation(deformation) * reference_tangent)[0]
    rhs = (ell.T * column_vectorize(deformation))[0]
    return sp.simplify(lhs - rhs)


def tangent_cochain_cross_covariance(
    vectorized_covariance: Matrix,
    left_tangent: Matrix,
    left_cochain: Matrix,
    right_tangent: Matrix,
    right_cochain: Matrix,
) -> sp.Expr:
    """Exact fixed-local-cochain projection of full deformation covariance."""
    l = tangent_cochain_readout_vector(left_tangent, left_cochain)
    r = tangent_cochain_readout_vector(right_tangent, right_cochain)
    if vectorized_covariance.shape != (l.rows, r.rows):
        raise ValueError("vectorized covariance dimension mismatch")
    return sp.simplify((l.T * vectorized_covariance * r)[0])


def tangent_cochain_covariance(
    vectorized_covariance: Matrix,
    reference_tangent: Matrix,
    cochain: Matrix,
) -> sp.Expr:
    return tangent_cochain_cross_covariance(
        vectorized_covariance,
        reference_tangent,
        cochain,
        reference_tangent,
        cochain,
    )


@dataclass(frozen=True)
class SelectedDeformationPairDecomposition:
    """Pathwise two-replica split before taking any expectation/covariance."""

    total_difference: sp.Matrix
    selector_difference: sp.Matrix
    deformation_difference: sp.Matrix

    @property
    def reconstructed_difference(self) -> sp.Matrix:
        return sp.simplify(self.selector_difference + self.deformation_difference)

    def pair_lift_parts(self) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
        """Return literal pair-current total, selector, deformation, and cross lifts.

        The pair functor is the tensor square of the current map.  We deliberately
        keep this Kronecker indexing rather than replacing it by an entrywise
        ``vec(T) vec(T)^T`` covariance, which is only permutation-equivalent data
        and is not the physical pair-current map itself.
        """
        total = pair_lift(self.total_difference)
        selector = pair_lift(self.selector_difference)
        deformation = pair_lift(self.deformation_difference)
        cross = sp.simplify(
            sp.kronecker_product(self.selector_difference, self.deformation_difference)
            + sp.kronecker_product(self.deformation_difference, self.selector_difference)
        )
        return sp.simplify(total), sp.simplify(selector), sp.simplify(deformation), cross


def selected_deformation_pair_decomposition(
    selector_left: Matrix,
    deformation_left: Matrix,
    selector_right: Matrix,
    deformation_right: Matrix,
) -> SelectedDeformationPairDecomposition:
    """Exact split of two selected spatial-current maps.

    With T(P,D)=P⊗D^T,

      T(P1,D1)-T(P2,D2)
       = T(P1-P2,D1) + T(P2,D1-D2).

    If both selector and deformation differ, the literal tensor-square pair lift
    contains generally nonzero cross terms.  Therefore deformation covariance must not be
    retyped as selector/resolution covariance, nor vice versa.
    """
    if selector_left.shape != selector_right.shape:
        raise ValueError("selector maps must have the same shape")
    if deformation_left.shape != deformation_right.shape:
        raise ValueError("deformations must have the same shape")
    total = sp.simplify(
        spatial_fiber_current_map(selector_left, deformation_left)
        - spatial_fiber_current_map(selector_right, deformation_right)
    )
    selector = spatial_fiber_current_map(
        selector_left - selector_right, deformation_left
    )
    deformation = spatial_fiber_current_map(
        selector_right, deformation_left - deformation_right
    )
    return SelectedDeformationPairDecomposition(
        total_difference=total,
        selector_difference=sp.simplify(selector),
        deformation_difference=sp.simplify(deformation),
    )


def selected_deformation_pair_dyad_residual(
    selector_left: Matrix,
    deformation_left: Matrix,
    selector_right: Matrix,
    deformation_right: Matrix,
) -> sp.Matrix:
    """Residual of the literal pair lift after selector/deformation expansion."""
    dec = selected_deformation_pair_decomposition(
        selector_left, deformation_left, selector_right, deformation_right
    )
    total, selector, deformation, cross = dec.pair_lift_parts()
    return sp.simplify(total - selector - deformation - cross)
