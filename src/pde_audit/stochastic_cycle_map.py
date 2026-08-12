"""Exact Itô bookkeeping for stochastic cycle-valued CK coordinates.

This module closes a classification loophole left by deterministic/finitely varying
selector motion.  If a cycle-valued coordinate itself carries diffusion, the extra
second-order pair term is its explicit martingale quadratic variation/carre-du-
champ.  It is therefore a physical stochastic source, not an untyped internal seam.
"""
from __future__ import annotations

from typing import Sequence

import sympy as sp

from .active_pair import pair_boundary


Matrix = sp.MatrixBase


def ito_cycle_drift(J: Matrix, b: Matrix, hessians: Sequence[Matrix], covariance: Matrix) -> sp.Matrix:
    """Itô drift of Phi(S) from Jacobian J and component Hessians.

    `hessians[i]` is the Hessian of output component Phi_i.  The correction is
    1/2 sum_ab covariance_ab * d_ab Phi_i.
    """
    if covariance.rows != covariance.cols:
        raise ValueError("covariance must be square")
    if J.cols != covariance.rows or b.rows != J.cols or b.cols != 1:
        raise ValueError("state dimensions do not match")
    if len(hessians) != J.rows:
        raise ValueError("one Hessian per output component is required")
    correction = sp.Matrix([
        sp.Rational(1, 2) * sum(
            covariance[a, c] * hessians[i][a, c]
            for a in range(covariance.rows)
            for c in range(covariance.cols)
        )
        for i in range(J.rows)
    ])
    return sp.simplify(J * b + correction)


def ito_cycle_diffusions(J: Matrix, sigma: Matrix) -> list[sp.Matrix]:
    """Diffusion current Psi_mu = D Phi sigma_mu for each noise column."""
    if J.cols != sigma.rows:
        raise ValueError("state dimensions do not match")
    return [sp.simplify(J * sigma[:, mu]) for mu in range(sigma.cols)]


def ito_pair_quadratic_source(diffusions: Sequence[Matrix]) -> sp.Matrix:
    """Pair quadratic-variation source sum_mu Psi_mu tensor Psi_mu."""
    if not diffusions:
        return sp.zeros(0, 1)
    out = sp.zeros(diffusions[0].rows ** 2, 1)
    for psi in diffusions:
        out += sp.kronecker_product(psi, psi)
    return sp.simplify(out)


def ito_pair_drift(Z: Matrix, drift: Matrix, diffusions: Sequence[Matrix]) -> sp.Matrix:
    """dt coefficient in d(Z tensor Z) by the exact Itô product rule."""
    first_order = sp.kronecker_product(drift, Z) + sp.kronecker_product(Z, drift)
    if diffusions:
        return sp.simplify(first_order + ito_pair_quadratic_source(diffusions))
    return sp.simplify(first_order)


def pair_source_boundary(B: Matrix, source: Matrix) -> sp.Matrix:
    """Physical pair boundary of a pair-current source vector."""
    return sp.simplify(pair_boundary(B) * source)


def scalar_qv_density(gradient: Matrix, covariance: Matrix) -> sp.Expr:
    """Carré-du-champ density grad(F)^T covariance grad(F)."""
    if gradient.cols != 1:
        raise ValueError("gradient must be a column vector")
    return sp.simplify((gradient.T * covariance * gradient)[0])
