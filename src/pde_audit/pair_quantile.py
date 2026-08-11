"""Exact same-ancestor Gaussian quantile leakage formulas.

Let Y~N(0,sigma2) be a common ancestor and let E1,E2~N(0,tau2) be independent
future noises.  Then X1=Y+E1 and X2=Y+E2 have identical symmetric marginals, so
the physical half-space quantile {x>0} has one-particle mass 1/2 for every tau2.
The pair mass in the same quantile chamber changes because the replicas decorrelate.
"""
from __future__ import annotations

import math


def replica_correlation(sigma2: float, tau2: float) -> float:
    if sigma2 <= 0.0:
        raise ValueError("sigma2 must be positive")
    if tau2 < 0.0:
        raise ValueError("tau2 must be nonnegative")
    return sigma2 / (sigma2 + tau2)


def one_particle_halfspace_mass() -> float:
    return 0.5


def same_ancestor_halfspace_pair_mass(sigma2: float, tau2: float) -> float:
    """P(X1>0,X2>0)=1/4+arcsin(rho)/(2pi) for centered Gaussian replicas."""
    rho = replica_correlation(sigma2, tau2)
    return 0.25 + math.asin(rho) / (2.0 * math.pi)


def halfspace_indicator_covariance(sigma2: float, tau2: float) -> float:
    return same_ancestor_halfspace_pair_mass(sigma2, tau2) - 0.25


def pair_mass_derivative_tau2(sigma2: float, tau2: float) -> float:
    """Exact d/d(tau2) of the pair half-space mass for tau2>0."""
    if sigma2 <= 0.0:
        raise ValueError("sigma2 must be positive")
    if tau2 <= 0.0:
        raise ValueError("tau2 must be positive for the classical derivative")
    return -sigma2 / (
        2.0
        * math.pi
        * (sigma2 + tau2)
        * math.sqrt(tau2 * (2.0 * sigma2 + tau2))
    )
