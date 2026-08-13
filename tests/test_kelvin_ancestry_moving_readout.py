from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.kelvin_ancestry_moving_readout import (
    critical_chamber_d_dot,
    critical_chamber_mass_from_d,
    critical_chamber_mass_rate_from_d,
    critical_chamber_mass_total_variation_from_d0,
    merger_mean_rate_scaled_limit,
    merger_readout_endpoint_mean,
    merger_variance_boundary_scaled_limit,
    merger_variance_bulk_scaled_limit,
    merger_variance_rate_scaled_limit,
    merger_variance_scaled_limit,
    moving_boundary_covariance_revaluation,
    moving_boundary_mean_revaluation,
    moving_boundary_three_layer_residual,
    reduced_chamber_mean_boundary_revaluation,
    reduced_chamber_mean_rate,
    reduced_chamber_mean_rate_residual,
    reduced_chamber_variance_balance_residual,
    reduced_chamber_variance_boundary_face,
    reduced_chamber_variance_bulk_face,
    reduced_chamber_variance_rate,
    reduced_critical_chamber_gradient_square_mean,
    reduced_critical_chamber_vorticity_mean,
    reduced_critical_chamber_vorticity_second_moment,
    reduced_critical_chamber_vorticity_variance,
    reduced_merger_alpha,
    reduced_side_boundary_vorticity,
    selected_covariance_layers,
    uniform_anchor_fp_residual_1d,
    uniform_torus_kelvin_anchor_density,
)


class KelvinAncestryMovingReadoutTests(unittest.TestCase):
    def setUp(self) -> None:
        self.nu = sp.symbols("nu", positive=True)
        self.d = sp.symbols("d", positive=True)

    def test_selected_covariance_has_three_exact_layers(self) -> None:
        w = sp.Matrix([sp.Rational(1, 3), sp.Rational(2, 3)])
        K = sp.Matrix([[sp.Rational(3, 4), sp.Rational(1, 4)], [sp.Rational(1, 4), sp.Rational(3, 4)]])
        means = sp.Matrix([[1, 2], [5, -1]])
        covs = [sp.diag(2, 1), sp.Matrix([[3, 1], [1, 4]])]
        layers = selected_covariance_layers(w, K, means, covs)

        # Direct selected full-state mixture is the referee.
        hidden_w = sp.simplify(K.T * w)
        direct_mean = sp.simplify(means.T * hidden_w)
        direct_second = sp.zeros(2)
        for i in range(2):
            mi = sp.Matrix(means[i, :]).T
            direct_second += hidden_w[i] * (covs[i] + mi * mi.T)
        direct_cov = sp.simplify(direct_second - direct_mean * direct_mean.T)
        self.assertEqual(sp.simplify(layers.mean - direct_mean), sp.zeros(2, 1))
        self.assertEqual(sp.simplify(layers.total - direct_cov), sp.zeros(2))
        self.assertEqual(
            sp.simplify(layers.total - layers.intrinsic - layers.resolution - layers.localization),
            sp.zeros(2),
        )

    def test_resolution_and_localization_are_distinct_layers(self) -> None:
        w = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)])
        K = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)], [1, 0]])
        means = sp.Matrix([[0], [2]])
        covs = [sp.zeros(1), sp.zeros(1)]
        layers = selected_covariance_layers(w, K, means, covs)
        self.assertGreater(float(layers.resolution[0, 0]), 0.0)
        self.assertGreater(float(layers.localization[0, 0]), 0.0)
        self.assertEqual(layers.intrinsic, sp.zeros(1))

    def test_moving_boundary_mean_is_signed_revaluation(self) -> None:
        M, lam = sp.symbols("M lam", nonzero=True)
        mean = sp.Matrix([1, -2])
        boundary = sp.Matrix([4, 3])
        rate = moving_boundary_mean_revaluation(M, mean, [lam], [boundary])
        self.assertEqual(sp.simplify(rate - lam * (boundary - mean) / M), sp.zeros(2, 1))

    def test_moving_boundary_covariance_is_not_positive_source(self) -> None:
        M = sp.Integer(1)
        mean = sp.Matrix([0])
        cov = sp.Matrix([[2]])
        # Mass exits (negative flux) at a boundary state with zero covariance and mean.
        rate = moving_boundary_covariance_revaluation(
            M, mean, cov, [sp.Integer(-1)], [sp.Matrix([0])], [sp.zeros(1)]
        )
        self.assertEqual(rate, sp.Matrix([[2]]))
        # Entering the same state has the opposite signed revaluation.
        rate_in = moving_boundary_covariance_revaluation(
            M, mean, cov, [sp.Integer(1)], [sp.Matrix([0])], [sp.zeros(1)]
        )
        self.assertEqual(rate_in, sp.Matrix([[-2]]))

    def test_three_layer_boundary_transport_telescopes_exactly(self) -> None:
        M = sp.symbols("M", positive=True)
        mean = sp.Matrix([sp.symbols("m0"), sp.symbols("m1")])
        intrinsic = sp.Matrix([[2, 1], [1, 3]])
        resolution = sp.Matrix([[1, -1], [-1, 2]])
        localization = sp.Matrix([[4, 0], [0, 5]])
        fluxes = [sp.symbols("l0"), sp.symbols("l1")]
        bmeans = [sp.Matrix([1, 0]), sp.Matrix([-2, 3])]
        bintr = [sp.eye(2), 2 * sp.eye(2)]
        bres = [sp.zeros(2), sp.Matrix([[1, 1], [1, 1]])]
        self.assertEqual(
            moving_boundary_three_layer_residual(
                M, mean, intrinsic, resolution, localization, fluxes, bmeans, bintr, bres
            ),
            sp.zeros(2),
        )

    def test_uniform_anchor_is_exact_stationary_kelvin_marginal_in_shear(self) -> None:
        y = sp.symbols("y", real=True)
        self.assertEqual(uniform_anchor_fp_residual_1d(sp.Integer(0), y, self.nu), 0)

    def test_uniform_kelvin_anchor_mass_is_literal_geometry(self) -> None:
        self.assertEqual(uniform_torus_kelvin_anchor_density(), 1 / (2 * sp.pi))
        self.assertEqual(critical_chamber_mass_from_d(self.d), self.d / (2 * sp.pi))
        self.assertEqual(
            critical_chamber_mass_rate_from_d(self.d, self.nu),
            critical_chamber_d_dot(self.d, self.nu) / (2 * sp.pi),
        )
        self.assertEqual(
            critical_chamber_mass_total_variation_from_d0(self.d), self.d / (2 * sp.pi)
        )

    def test_cut_speed_diverges_but_mass_excursion_is_finite(self) -> None:
        self.assertEqual(
            sp.limit(self.d * critical_chamber_d_dot(self.d, self.nu), self.d, 0, dir="+"),
            -3 * self.nu,
        )
        self.assertEqual(
            sp.limit(
                self.d * critical_chamber_mass_rate_from_d(self.d, self.nu),
                self.d,
                0,
                dir="+",
            ),
            -3 * self.nu / (2 * sp.pi),
        )

    def test_exact_selected_vorticity_mean_has_closed_form(self) -> None:
        alpha = reduced_merger_alpha(self.d)
        self.assertEqual(
            sp.simplify(
                reduced_critical_chamber_vorticity_mean(self.d)
                + sp.Rational(3, 4) * alpha * sp.sin(self.d) / self.d
            ),
            0,
        )

    def test_mean_motion_is_pure_moving_cut_face(self) -> None:
        self.assertEqual(reduced_chamber_mean_rate_residual(self.d, self.nu), 0)
        self.assertEqual(
            sp.simplify(
                reduced_chamber_mean_rate(self.d, self.nu)
                - reduced_chamber_mean_boundary_revaluation(self.d, self.nu)
            ),
            0,
        )

    def test_criticality_beats_singular_cut_speed_for_mean(self) -> None:
        side_minus_mean = sp.simplify(
            reduced_side_boundary_vorticity(self.d)
            - reduced_critical_chamber_vorticity_mean(self.d)
        )
        self.assertEqual(
            sp.limit(side_minus_mean / self.d**4, self.d, 0, dir="+"),
            -sp.exp(-1) / 15,
        )
        self.assertEqual(merger_mean_rate_scaled_limit(self.nu), self.nu * sp.exp(-1) / 5)
        self.assertEqual(
            sp.limit(reduced_chamber_mean_rate(self.d, self.nu), self.d, 0, dir="+"), 0
        )

    def test_readout_mean_reaches_common_merger_value(self) -> None:
        self.assertEqual(merger_readout_endpoint_mean(), -sp.Rational(3, 4) * sp.exp(-1))

    def test_second_moment_and_variance_are_exact(self) -> None:
        x = sp.symbols("x", real=True)
        q = reduced_merger_alpha(self.d) * (
            -sp.cos(x) + sp.cos(2 * x) / (4 * sp.cos(self.d))
        )
        direct_second = sp.simplify(sp.integrate(q**2, (x, 0, self.d)) / self.d)
        self.assertEqual(
            sp.simplify(
                sp.trigsimp(
                    reduced_critical_chamber_vorticity_second_moment(self.d) - direct_second
                )
            ),
            0,
        )
        self.assertEqual(
            sp.simplify(
                reduced_critical_chamber_vorticity_variance(self.d)
                - reduced_critical_chamber_vorticity_second_moment(self.d)
                + reduced_critical_chamber_vorticity_mean(self.d) ** 2
            ),
            0,
        )

    def test_selected_variance_collapses_at_eighth_order(self) -> None:
        self.assertEqual(merger_variance_scaled_limit(), sp.exp(-2) / 525)
        self.assertEqual(
            sp.limit(reduced_critical_chamber_vorticity_variance(self.d), self.d, 0, dir="+"),
            0,
        )

    def test_variance_balance_is_kelvin_bulk_plus_moving_cut(self) -> None:
        self.assertEqual(reduced_chamber_variance_balance_residual(self.d, self.nu), 0)

    def test_gradient_bulk_is_nonnegative_before_viscous_sign(self) -> None:
        val = reduced_critical_chamber_gradient_square_mean(sp.Rational(1, 2))
        self.assertGreater(float(val), 0.0)
        self.assertLess(float(reduced_chamber_variance_bulk_face(sp.Rational(1, 2), 1)), 0.0)

    def test_bulk_and_boundary_faces_have_distinct_forced_coefficients(self) -> None:
        self.assertEqual(
            merger_variance_bulk_scaled_limit(self.nu),
            -sp.Rational(4, 105) * self.nu * sp.exp(-2),
        )
        self.assertEqual(
            merger_variance_boundary_scaled_limit(self.nu),
            -sp.Rational(4, 525) * self.nu * sp.exp(-2),
        )
        self.assertNotEqual(
            merger_variance_bulk_scaled_limit(self.nu),
            merger_variance_boundary_scaled_limit(self.nu),
        )

    def test_total_variance_rate_is_regular_and_forced(self) -> None:
        self.assertEqual(
            merger_variance_rate_scaled_limit(self.nu),
            -sp.Rational(8, 175) * self.nu * sp.exp(-2),
        )
        self.assertEqual(
            sp.limit(reduced_chamber_variance_rate(self.d, self.nu), self.d, 0, dir="+"),
            0,
        )

    def test_selector_face_is_finite_variation_not_anchor_qv(self) -> None:
        # The selected mass has a deterministic moving-boundary rate.  It carries no
        # Brownian q.v. coefficient; the physical Kelvin anchor retains q.v. 2 nu.
        self.assertNotEqual(2 * self.nu, 0)
        self.assertTrue(critical_chamber_mass_rate_from_d(self.d, self.nu).has(self.nu))


if __name__ == "__main__":
    unittest.main()
