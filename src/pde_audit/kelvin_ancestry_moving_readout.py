"""Exact Kelvin-ancestry -> Eulerian moving-readout covariance laws.

The physical object is kept in two layers instead of being identified prematurely:

* a Kelvin/material ancestry state, possibly reduced to an anchor coordinate ``y``
  with a conditional lift kernel ``kappa(y,dY)`` to the full current-shape state;
* an Eulerian localization/readout region ``Omega(t)`` moving through that ancestry
  population.

For a full-state payoff, conditioning and Eulerian selection force three covariance
layers by the law of total covariance:

    intrinsic full-Kelvin covariance
  + hidden-state/resolution covariance
  + localization covariance of the conditional mean.

A moving cut does not create a new Brownian source.  Its exact contribution is a
signed Reynolds/coarea revaluation of those existing layers.  The exact periodic
critical-sheet merger provides a physical calibration: the uniform Kelvin-anchor
measure is stationary, while the side critical cut moves through it.  Although the
cut speed diverges like 1/d, criticality forces the vorticity contrast to vanish like
d^4 and the selected variance like d^8, so normalized readout rates vanish at the
merger.

No first-bad badness functional, restart, continuation, or regularity conclusion is
made here.
"""
from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Sequence
import sympy as sp

from .ancestry_resolution_kernel import kernel_covariances
from .critical_sheet_merger_kelvin_event import merger_half_separation, merger_time

Matrix = sp.MatrixBase


@dataclass(frozen=True)
class SelectedCovarianceLayers:
    mean: Matrix
    intrinsic: Matrix
    resolution: Matrix
    localization: Matrix
    total: Matrix


def _as_column(weights: Matrix) -> Matrix:
    if weights.cols == 1:
        return weights
    if weights.rows == 1:
        return weights.T
    raise ValueError("weights must be a row or column vector")


def selected_covariance_layers(
    reduced_weights: Matrix,
    lift_kernel: Matrix,
    physical_means: Matrix,
    physical_covariances: Sequence[Matrix],
) -> SelectedCovarianceLayers:
    """Two-stage law of total covariance after a normalized Eulerian readout.

    ``reduced_weights`` are the normalized selected weights on reduced ancestry
    states.  ``lift_kernel`` gives the conditional full-state law.  The result is

      C_sel = E_sel E_kappa[C_full]
            + E_sel Cov_kappa(m_full)
            + Cov_sel(E_kappa[m_full]).

    The first term is intrinsic Kelvin/future covariance already present on the full
    state.  The second is hidden-state resolution covariance.  The third is ordinary
    Eulerian localization dispersion of the reduced conditional mean.
    """
    w = _as_column(reduced_weights)
    if lift_kernel.rows != w.rows:
        raise ValueError("one selected weight per reduced ancestry state is required")
    if lift_kernel.cols != physical_means.rows:
        raise ValueError("lift/full-state dimensions do not match")
    for a in range(lift_kernel.rows):
        if sp.simplify(sum(lift_kernel[a, i] for i in range(lift_kernel.cols))) != 1:
            raise ValueError("each lift-kernel row must sum to one")
    if len(physical_covariances) != lift_kernel.cols:
        raise ValueError("one physical covariance per full state is required")
    if sp.simplify(sum(w)) != 1:
        raise ValueError("selected reduced weights must sum to one")
    d = physical_means.cols
    if any(C.shape != (d, d) for C in physical_covariances):
        raise ValueError("physical covariance dimension mismatch")

    reduced_means = sp.simplify(lift_kernel * physical_means)
    mean = sp.simplify(reduced_means.T * w)

    conditional_intrinsic: list[Matrix] = []
    for a in range(lift_kernel.rows):
        C = sp.zeros(d)
        for i in range(lift_kernel.cols):
            C += lift_kernel[a, i] * physical_covariances[i]
        conditional_intrinsic.append(sp.simplify(C))
    conditional_resolution = kernel_covariances(lift_kernel, physical_means)

    intrinsic = sp.zeros(d)
    resolution = sp.zeros(d)
    localization = sp.zeros(d)
    for a in range(lift_kernel.rows):
        intrinsic += w[a] * conditional_intrinsic[a]
        resolution += w[a] * conditional_resolution[a]
        ma = sp.Matrix(reduced_means[a, :]).T
        delta = ma - mean
        localization += w[a] * delta * delta.T
    intrinsic = sp.simplify(intrinsic)
    resolution = sp.simplify(resolution)
    localization = sp.simplify(localization)
    return SelectedCovarianceLayers(
        mean=mean,
        intrinsic=intrinsic,
        resolution=resolution,
        localization=localization,
        total=sp.simplify(intrinsic + resolution + localization),
    )


def moving_boundary_average_revaluation(
    selected_mass: sp.Expr,
    selected_average: Matrix,
    signed_boundary_fluxes: Sequence[sp.Expr],
    boundary_values: Sequence[Matrix],
) -> Matrix:
    """Boundary-only rate of a normalized selected average.

    A signed flux is positive when ancestry mass enters the selected region and
    negative when it leaves.  Reynolds normalization forces

      d<E[A]>_bdry = M^-1 sum_b lambda_b (A_b-<A>).

    This is a finite-variation revaluation, not Brownian quadratic variation.
    """
    if len(signed_boundary_fluxes) != len(boundary_values):
        raise ValueError("one value per signed boundary flux is required")
    out = sp.zeros(*selected_average.shape)
    for flux, value in zip(signed_boundary_fluxes, boundary_values):
        if value.shape != selected_average.shape:
            raise ValueError("boundary value shape mismatch")
        out += flux * (value - selected_average)
    return sp.simplify(out / selected_mass)


def moving_boundary_mean_revaluation(
    selected_mass: sp.Expr,
    selected_mean: Matrix,
    signed_boundary_fluxes: Sequence[sp.Expr],
    boundary_means: Sequence[Matrix],
) -> Matrix:
    return moving_boundary_average_revaluation(
        selected_mass, selected_mean, signed_boundary_fluxes, boundary_means
    )


def moving_boundary_covariance_revaluation(
    selected_mass: sp.Expr,
    selected_mean: Matrix,
    selected_covariance: Matrix,
    signed_boundary_fluxes: Sequence[sp.Expr],
    boundary_means: Sequence[Matrix],
    boundary_covariances: Sequence[Matrix],
) -> Matrix:
    """Exact Reynolds boundary face for normalized total covariance.

      Cdot_bdry = M^-1 sum_b lambda_b[
          C_b + (m_b-m)(m_b-m)^T - C
      ].

    The bracket can have either sign after contraction; this is a signed population
    revaluation and is not a new positive covariance producer.
    """
    if not (
        len(signed_boundary_fluxes)
        == len(boundary_means)
        == len(boundary_covariances)
    ):
        raise ValueError("boundary data lengths must match")
    out = sp.zeros(*selected_covariance.shape)
    for flux, mean_b, cov_b in zip(
        signed_boundary_fluxes, boundary_means, boundary_covariances
    ):
        delta = mean_b - selected_mean
        out += flux * (cov_b + delta * delta.T - selected_covariance)
    return sp.simplify(out / selected_mass)


def moving_boundary_three_layer_residual(
    selected_mass: sp.Expr,
    selected_mean: Matrix,
    intrinsic: Matrix,
    resolution: Matrix,
    localization: Matrix,
    signed_boundary_fluxes: Sequence[sp.Expr],
    boundary_means: Sequence[Matrix],
    boundary_intrinsic: Sequence[Matrix],
    boundary_resolution: Sequence[Matrix],
) -> Matrix:
    """Residual: layerwise boundary transport equals total covariance transport."""
    if not (
        len(signed_boundary_fluxes)
        == len(boundary_means)
        == len(boundary_intrinsic)
        == len(boundary_resolution)
    ):
        raise ValueError("boundary data lengths must match")
    intrinsic_rate = moving_boundary_average_revaluation(
        selected_mass, intrinsic, signed_boundary_fluxes, boundary_intrinsic
    )
    resolution_rate = moving_boundary_average_revaluation(
        selected_mass, resolution, signed_boundary_fluxes, boundary_resolution
    )
    zero_covariances = [sp.zeros(*localization.shape) for _ in boundary_means]
    localization_rate = moving_boundary_covariance_revaluation(
        selected_mass,
        selected_mean,
        localization,
        signed_boundary_fluxes,
        boundary_means,
        zero_covariances,
    )
    boundary_total = [
        sp.simplify(boundary_intrinsic[i] + boundary_resolution[i])
        for i in range(len(boundary_means))
    ]
    total_rate = moving_boundary_covariance_revaluation(
        selected_mass,
        selected_mean,
        sp.simplify(intrinsic + resolution + localization),
        signed_boundary_fluxes,
        boundary_means,
        boundary_total,
    )
    return sp.simplify(intrinsic_rate + resolution_rate + localization_rate - total_rate)


def uniform_torus_kelvin_anchor_density() -> sp.Expr:
    """Uniform y-marginal of the Kelvin anchor on a 2pi-periodic torus."""
    return sp.Rational(1, 2) / sp.pi




def uniform_anchor_fp_residual_1d(
    y_drift: sp.Expr, y: sp.Symbol, nu: sp.Expr
) -> sp.Expr:
    """Fokker--Planck residual of the uniform 2pi-periodic anchor marginal.

    For reverse-age SDE ``dY=b(Y) dsigma+sqrt(2nu)dW``, a stationary density rho
    obeys ``-d_y(b rho)+nu d_yy rho=0``.  The exact merger shear has b_y=0, so the
    uniform y marginal is an exact stationary Kelvin-ancestry measure.
    """
    rho = uniform_torus_kelvin_anchor_density()
    return sp.simplify(-sp.diff(y_drift * rho, y) + nu * sp.diff(rho, y, 2))


def critical_chamber_d_dot(d: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Physical-time rate of the half-width d: d_dot=-3 nu cot(d)."""
    return sp.simplify(-3 * nu * sp.cos(d) / sp.sin(d))


def critical_chamber_mass_from_d(d: sp.Expr) -> sp.Expr:
    """Uniform Kelvin-anchor mass of the chamber [pi-d,pi]."""
    return sp.simplify(uniform_torus_kelvin_anchor_density() * d)


def critical_chamber_mass(t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    return sp.simplify(critical_chamber_mass_from_d(merger_half_separation(t, nu)))


def critical_chamber_mass_rate_from_d(d: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Signed mass flux through the moving side boundary; central boundary is fixed."""
    return sp.simplify(uniform_torus_kelvin_anchor_density() * critical_chamber_d_dot(d, nu))


def critical_chamber_mass_total_variation_from_d0(d0: sp.Expr) -> sp.Expr:
    """Total variation of selected uniform mass as d decreases from d0 to zero."""
    return sp.simplify(uniform_torus_kelvin_anchor_density() * d0)


def reduced_merger_alpha(d: sp.Expr) -> sp.Expr:
    """e^{-nu t} on the critical relation cos d=e^{3(nu t-1)}."""
    return sp.simplify(sp.exp(-1) * sp.cos(d) ** (-sp.Rational(1, 3)))


def reduced_critical_chamber_vorticity(x_from_central: sp.Expr, d: sp.Expr) -> sp.Expr:
    """Exact q(pi-x,t(d)) on 0<=x<=d along the merger family."""
    alpha = reduced_merger_alpha(d)
    return sp.simplify(
        alpha
        * (-sp.cos(x_from_central) + sp.cos(2 * x_from_central) / (4 * sp.cos(d)))
    )


def reduced_critical_chamber_vorticity_mean(d: sp.Expr) -> sp.Expr:
    """Exact uniform selected mean: -3 alpha sin(d)/(4d)."""
    alpha = reduced_merger_alpha(d)
    return sp.simplify(-sp.Rational(3, 4) * alpha * sp.sin(d) / d)


def reduced_side_boundary_vorticity(d: sp.Expr) -> sp.Expr:
    return sp.simplify(reduced_critical_chamber_vorticity(d, d))


def reduced_critical_chamber_vorticity_second_moment(d: sp.Expr) -> sp.Expr:
    """Exact uniform chamber second moment of q, written by elementary trig integrals."""
    alpha = reduced_merger_alpha(d)
    r = sp.cos(d)
    return sp.simplify(
        alpha**2
        * (
            sp.Rational(1, 2)
            + sp.sin(2 * d) / (4 * d)
            - (sp.sin(d) + sp.sin(3 * d) / 3) / (4 * r * d)
            + (sp.Rational(1, 2) + sp.sin(4 * d) / (8 * d)) / (16 * r**2)
        )
    )


def reduced_critical_chamber_vorticity_variance(d: sp.Expr) -> sp.Expr:
    mean = reduced_critical_chamber_vorticity_mean(d)
    return sp.simplify(reduced_critical_chamber_vorticity_second_moment(d) - mean**2)


def reduced_critical_chamber_gradient_square_mean(d: sp.Expr) -> sp.Expr:
    """Exact chamber average of |partial_y q|^2 (=|partial_x q|^2 here)."""
    alpha = reduced_merger_alpha(d)
    r = sp.cos(d)
    return sp.simplify(
        alpha**2
        * (
            sp.Rational(1, 2)
            - sp.sin(2 * d) / (4 * d)
            - (sp.sin(d) - sp.sin(3 * d) / 3) / (2 * r * d)
            + (sp.Rational(1, 2) - sp.sin(4 * d) / (8 * d)) / (4 * r**2)
        )
    )


def reduced_chamber_mean_rate(d: sp.Expr, nu: sp.Expr) -> sp.Expr:
    mean = reduced_critical_chamber_vorticity_mean(d)
    return sp.simplify(sp.diff(mean, d) * critical_chamber_d_dot(d, nu))


def reduced_chamber_mean_boundary_revaluation(d: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Boundary revaluation of the normalized mean; interior heat flux is zero.

    Both chamber endpoints are vorticity-critical, so integrating q_t=nu q_yy gives
    no interior contribution to the first moment.  All mean motion is the moving-cut
    Reynolds face.
    """
    mean = reduced_critical_chamber_vorticity_mean(d)
    side = reduced_side_boundary_vorticity(d)
    return sp.simplify(critical_chamber_d_dot(d, nu) * (side - mean) / d)


def reduced_chamber_mean_rate_residual(d: sp.Expr, nu: sp.Expr) -> sp.Expr:
    return sp.simplify(
        reduced_chamber_mean_rate(d, nu)
        - reduced_chamber_mean_boundary_revaluation(d, nu)
    )


def reduced_chamber_variance_bulk_face(d: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Intrinsic NS/Kelvin bulk face -2 nu <|grad q|^2> in the chamber."""
    return sp.simplify(-2 * nu * reduced_critical_chamber_gradient_square_mean(d))


def reduced_chamber_variance_boundary_face(d: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Signed moving-cut covariance revaluation for the shrinking chamber."""
    mean = reduced_critical_chamber_vorticity_mean(d)
    side = reduced_side_boundary_vorticity(d)
    variance = reduced_critical_chamber_vorticity_variance(d)
    return sp.simplify(
        critical_chamber_d_dot(d, nu)
        * ((side - mean) ** 2 - variance)
        / d
    )


def reduced_chamber_variance_rate(d: sp.Expr, nu: sp.Expr) -> sp.Expr:
    variance = reduced_critical_chamber_vorticity_variance(d)
    return sp.simplify(sp.diff(variance, d) * critical_chamber_d_dot(d, nu))


def reduced_chamber_variance_balance_residual(d: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Residual of variance rate = Kelvin bulk + moving-cut revaluation."""
    return sp.simplify(
        sp.trigsimp(
            reduced_chamber_variance_rate(d, nu)
            - reduced_chamber_variance_bulk_face(d, nu)
            - reduced_chamber_variance_boundary_face(d, nu)
        )
    )


def merger_mean_rate_scaled_limit(nu: sp.Expr) -> sp.Expr:
    d = sp.symbols("d_readout_mean", positive=True)
    return sp.simplify(sp.limit(reduced_chamber_mean_rate(d, nu) / d**2, d, 0, dir="+"))


def merger_variance_scaled_limit() -> sp.Expr:
    d = sp.symbols("d_readout_var", positive=True)
    return sp.simplify(
        sp.limit(reduced_critical_chamber_vorticity_variance(d) / d**8, d, 0, dir="+")
    )


def merger_variance_bulk_scaled_limit(nu: sp.Expr) -> sp.Expr:
    d = sp.symbols("d_readout_bulk", positive=True)
    return sp.simplify(
        sp.limit(reduced_chamber_variance_bulk_face(d, nu) / d**6, d, 0, dir="+")
    )


def merger_variance_boundary_scaled_limit(nu: sp.Expr) -> sp.Expr:
    d = sp.symbols("d_readout_boundary", positive=True)
    return sp.simplify(
        sp.limit(reduced_chamber_variance_boundary_face(d, nu) / d**6, d, 0, dir="+")
    )


def merger_variance_rate_scaled_limit(nu: sp.Expr) -> sp.Expr:
    d = sp.symbols("d_readout_rate", positive=True)
    return sp.simplify(
        sp.limit(reduced_chamber_variance_rate(d, nu) / d**6, d, 0, dir="+")
    )


def merger_readout_endpoint_mean() -> sp.Expr:
    d = sp.symbols("d_readout_endpoint", positive=True)
    return sp.simplify(
        sp.limit(reduced_critical_chamber_vorticity_mean(d), d, 0, dir="+")
    )


def merger_time_identity(nu: sp.Expr) -> sp.Expr:
    """Expose the same merger time used by the previous physical calibration."""
    return merger_time(nu)
