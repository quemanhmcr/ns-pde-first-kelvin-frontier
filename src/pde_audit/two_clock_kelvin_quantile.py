"""Exact reverse-age Kelvin clock and quantile-interface identities.

This module separates three operations that must not be conflated:

1. a same-clock time-reversal drift b_- of a diffusion;
2. reversal of the clock of a future conditional bank, tau=Theta-s;
3. a physical moving quantile/shell cut driven by a continuity current.

For the physical backward-Kelvin state, clock reversal turns the backward-Ito
state operator K^- into the ordinary forward Markov generator -K^- in reverse
age.  A future conditional bank in reverse age is therefore a causal past-payoff
bank in physical time.

No restart or regularity conclusion is encoded here.
"""
from __future__ import annotations

from typing import Sequence

import sympy as sp

Matrix = sp.MatrixBase


def reverse_age_generator_of_backward_operator(backward_spatial_generator: sp.Expr) -> sp.Expr:
    """Frozen-coefficient reverse-age generator: L_rev = - K^-.

    The physical-time derivative also reverses because r=t-tau.  Coefficients of
    K^- are understood at the physical time r=t-tau.
    """
    return sp.expand(-backward_spatial_generator)


def reverse_age_state_map_diffusion(DPi: Matrix, K: Matrix) -> sp.Matrix:
    """Diffusion pushforward DPi K DPi^T for a clock-reversed future-bank map."""
    return sp.simplify(DPi * K * DPi.T)


def reverse_age_state_map_drift(
    Pi_tau: Matrix,
    DPi: Matrix,
    b_plus: Matrix,
    K_hess_Pi: Matrix,
    nu: sp.Expr,
) -> sp.Matrix:
    """Target backward-Ito physical drift after reversing a future-bank clock.

    If f(s,y)=g(tau,Pi(tau,y)), tau=Theta-s, and

        (partial_s + b_+.grad + nu K:Hess) f = 0,

    then g obeys

        partial_tau g + B_phys.grad g - nu K_phys:Hess g = 0

    precisely when

        B_phys = Pi_tau - DPi b_+ - nu (K:D^2 Pi).

    K_hess_Pi is the vector with components K:D^2 Pi^alpha.
    """
    return sp.simplify(Pi_tau - DPi * b_plus - nu * K_hess_Pi)


def same_clock_backward_state_map_drift(
    Pi_t: Matrix,
    DPi: Matrix,
    b_minus: Matrix,
    K_hess_Pi: Matrix,
    nu: sp.Expr,
) -> sp.Matrix:
    """Same-clock backward-Ito map, for comparison with clock reversal.

    B_phys = Pi_t + DPi b_- - nu K:D^2 Pi.
    """
    return sp.simplify(Pi_t + DPi * b_minus - nu * K_hess_Pi)


def identity_map_future_bridge_residual(b_plus: Matrix, physical_drift: Matrix) -> sp.Matrix:
    """Identity-map reverse-age bridge residual b_+ + B_phys."""
    return sp.simplify(b_plus + physical_drift)


def identity_map_same_clock_residual(b_minus: Matrix, physical_drift: Matrix) -> sp.Matrix:
    """Identity-map same-clock backward-drift residual b_- - B_phys."""
    return sp.simplify(b_minus - physical_drift)


def simultaneous_identity_map_obstruction(b_plus: Matrix, b_minus: Matrix) -> sp.Matrix:
    """If both identity-map interpretations target the same B_phys, 2j must vanish."""
    return sp.simplify(b_plus + b_minus)


def reverse_probability_current_velocity(j: Matrix) -> sp.Matrix:
    """Clock reversal reverses probability-current velocity."""
    return sp.simplify(-j)


def weighted_level_quantile_speed(
    boundary_weights: Sequence[sp.Expr],
    level_material_rates: Sequence[sp.Expr],
) -> sp.Expr:
    """Coarea form of the fixed-mass level-set speed.

    For D_t={g<a(t)} and partial_t q+div(q j)=0,

      adot = [int_{g=a} q/|grad g| (g_t+j.grad g) dS]
             / [int_{g=a} q/|grad g| dS].

    The inputs represent exact symbolic quadrature/finite sums of the numerator
    and denominator.  This helper records the algebraic weighted-average structure.
    """
    if len(boundary_weights) != len(level_material_rates) or not boundary_weights:
        raise ValueError("nonempty equally-sized boundary data are required")
    denom = sp.Add(*boundary_weights)
    numer = sp.Add(*(w * r for w, r in zip(boundary_weights, level_material_rates)))
    return sp.simplify(numer / denom)


def one_dimensional_quantile_speed(current_velocity_at_cut: sp.Expr, level_t: sp.Expr = sp.Integer(0), level_x: sp.Expr = sp.Integer(1)) -> sp.Expr:
    """For g(x,t) with one boundary point: adot=g_t+j g_x.

    In particular g=x gives adot=j at the quantile.
    """
    return sp.simplify(level_t + current_velocity_at_cut * level_x)


def moving_chamber_mass_rate_1d(q: sp.Expr, j: sp.Expr, a_dot: sp.Expr) -> sp.Expr:
    """Mass rate for (-infinity,a(t)) under partial_t q+partial_x(q j)=0."""
    return sp.simplify(q * (a_dot - j))


def flat_reverse_kelvin_current_velocity(
    physical_velocity: sp.Expr,
    log_density_gradient: sp.Expr,
    nu: sp.Expr,
) -> sp.Expr:
    """Current velocity of dX_tau=-u d tau+sqrt(2nu)dW in one coordinate."""
    return sp.simplify(-physical_velocity - nu * log_density_gradient)


def gaussian_variance(var0: sp.Expr, nu: sp.Expr, tau: sp.Expr) -> sp.Expr:
    return sp.simplify(var0 + 2 * nu * tau)


def centered_gaussian_quantile(z_p: sp.Expr, var0: sp.Expr, nu: sp.Expr, tau: sp.Expr) -> sp.Expr:
    """p-quantile written using its fixed standard-normal quantile z_p."""
    return sp.simplify(z_p * sp.sqrt(gaussian_variance(var0, nu, tau)))


def centered_gaussian_current_velocity(x: sp.Expr, var0: sp.Expr, nu: sp.Expr, tau: sp.Expr) -> sp.Expr:
    """Probability-current velocity for zero-drift heat flow from N(0,var0)."""
    var = gaussian_variance(var0, nu, tau)
    # b_+=0 and j=b_+-nu grad log q = nu x/var.
    return sp.simplify(nu * x / var)


def outer_time_shifted_quantile(z_p: sp.Expr, variance: sp.Expr, shift_speed: sp.Expr, t: sp.Expr) -> sp.Expr:
    """Quantile of a Gaussian family shifted arbitrarily in an outer time t."""
    return sp.simplify(shift_speed * t + z_p * sp.sqrt(variance))


def affine_reverse_covariance_residual(
    A: Matrix,
    Sigma: Matrix,
    Sigma_dot: Matrix,
    nu: sp.Expr,
) -> sp.Matrix:
    """Covariance ODE residual for dX=-A X d tau+sqrt(2nu)dW."""
    if A.rows != A.cols or Sigma.shape != A.shape or Sigma_dot.shape != A.shape:
        raise ValueError("A, Sigma, and Sigma_dot must be square matrices of equal size")
    return sp.simplify(Sigma_dot + A * Sigma + Sigma * A.T - 2 * nu * sp.eye(A.rows))


def affine_reverse_probability_current(
    A: Matrix,
    Sigma: Matrix,
    x: Matrix,
    nu: sp.Expr,
) -> sp.Matrix:
    """Probability-current velocity -A x + nu Sigma^-1 x of a centered Gaussian."""
    if A.rows != A.cols or Sigma.shape != A.shape or x.shape != (A.rows, 1):
        raise ValueError("dimension mismatch")
    return sp.simplify(-A * x + nu * Sigma.inv() * x)


def mahalanobis_shell_material_rate(
    A: Matrix,
    Sigma: Matrix,
    Sigma_dot: Matrix,
    x: Matrix,
    nu: sp.Expr,
) -> sp.Expr:
    """partial_tau g + j.grad g for g=x^T Sigma^-1 x.

    Substituting the exact affine covariance ODE makes this identically zero.
    """
    Sinv = Sigma.inv()
    g_t = sp.simplify(-(x.T * Sinv * Sigma_dot * Sinv * x)[0])
    grad_g = sp.simplify(2 * Sinv * x)
    j = affine_reverse_probability_current(A, Sigma, x, nu)
    return sp.simplify(g_t + (j.T * grad_g)[0])


def diagonal_reverse_covariance_component(
    strain_rate: sp.Expr,
    tau: sp.Expr,
    nu: sp.Expr,
) -> sp.Expr:
    """Variance for dX=-a X d tau+sqrt(2nu)dW when a is nonzero."""
    return sp.simplify(nu * (1 - sp.exp(-2 * strain_rate * tau)) / strain_rate)


def zero_rate_reverse_covariance_component(tau: sp.Expr, nu: sp.Expr) -> sp.Expr:
    return sp.simplify(2 * nu * tau)
