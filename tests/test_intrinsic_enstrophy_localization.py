from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.intrinsic_enstrophy_localization import (
    ancestry_superlevel_flux_faces,
    integer_scaled_one_mode_ns_residual,
    max_envelope_left_dini,
    max_envelope_right_dini,
    navier_stokes_similarity_weights,
    normalized_enstrophy,
    normalized_enstrophy_gradient,
    normalized_relative_speed_residual,
    normalized_superlevel_compatibility_defect,
    one_mode_intrinsic_localization_calibration,
    one_mode_similarity_threshold_no_go,
    similarity_normalized_defect_residual,
    similarity_normalized_speed_residual,
    superlevel_material_compatibility_defect,
    four_mode_global_crossing_calibration,
)


class IntrinsicEnstrophyLocalizationTests(unittest.TestCase):
    def setUp(self):
        self.x, self.y, self.z, self.t = sp.symbols("x y z t", real=True)
        self.nu = sp.symbols("nu", positive=True)
        self.A = sp.symbols("A", positive=True)
        self.n = sp.symbols("n", positive=True, integer=True)
        self.theta = sp.symbols("theta", positive=True)
        self.M = sp.symbols("M", positive=True)

    def test_similarity_weights_are_forced_by_ns(self):
        w = navier_stokes_similarity_weights()
        self.assertEqual(w["vorticity"], 2)
        self.assertEqual(w["enstrophy"], 4)
        self.assertEqual(w["enstrophy_rate"], 6)
        self.assertEqual(w["kelvin_bulk"], 6)
        self.assertEqual(w["boundary_speed"], 1)

    def test_normalized_enstrophy_is_dimensionless(self):
        e = sp.symbols("e", positive=True)
        lam = sp.symbols("lam", positive=True)
        self.assertEqual(
            sp.simplify(normalized_enstrophy(lam**4 * e, lam**4 * self.M) - normalized_enstrophy(e, self.M)),
            0,
        )

    def test_normalized_compatibility_defect_is_similarity_invariant(self):
        lam = sp.symbols("lam", positive=True)
        R, Md = sp.symbols("R Md", real=True)
        self.assertEqual(similarity_normalized_defect_residual(lam, R, self.theta, Md, self.M), 0)

    def test_normalized_boundary_speed_is_similarity_invariant(self):
        lam = sp.symbols("lam", positive=True)
        v = sp.symbols("v", real=True)
        self.assertEqual(similarity_normalized_speed_residual(lam, v, self.M), 0)

    def test_intrinsic_normalized_speed_grammar_closes(self):
        R, Md, ge = sp.symbols("R Md ge", positive=True)
        defect = normalized_superlevel_compatibility_defect(R, self.theta, Md, self.M)
        grad = normalized_enstrophy_gradient(ge, self.M)
        rel = (R - self.theta * Md) / ge
        self.assertEqual(normalized_relative_speed_residual(rel, defect, grad, self.M), 0)

    def test_ancestry_flux_has_only_two_physical_faces(self):
        rho, un, cn, C, ge = sp.symbols("rho un cn C ge", nonzero=True)
        faces = ancestry_superlevel_flux_faces(rho, un, cn, C, ge)
        self.assertEqual(faces["residual"], 0)
        self.assertEqual(
            sp.simplify(faces["total"] - rho * ((un - cn) + C / ge)),
            0,
        )

    def test_exact_scaled_one_mode_is_literal_periodic_ns(self):
        residual = integer_scaled_one_mode_ns_residual(
            self.A, self.n, (self.x, self.y, self.z), self.t, self.nu
        )
        self.assertEqual(residual, sp.zeros(3, 1))

    def test_one_mode_normalized_profile_is_stationary(self):
        c = one_mode_intrinsic_localization_calibration(
            self.A, self.n, self.theta, (self.x, self.y, self.z), self.t, self.nu
        )
        self.assertEqual(sp.trigsimp(c["normalized_enstrophy"] - sp.cos(self.n * self.y) ** 2), 0)
        self.assertEqual(c["normalized_time_derivative"], 0)

    def test_one_mode_faces_are_literal_enstrophy_pde_faces(self):
        c = one_mode_intrinsic_localization_calibration(
            self.A, self.n, self.theta, (self.x, self.y, self.z), self.t, self.nu
        )
        self.assertEqual(c["stretching_expression_residual"], 0)
        self.assertEqual(c["kelvin_bulk_expression_residual"], 0)
        self.assertEqual(c["curvature_expression_residual"], 0)
        self.assertEqual(c["time_expression_residual"], 0)
        self.assertEqual(c["enstrophy_balance_residual"], 0)

    def test_one_mode_kelvin_bulk_and_curvature_are_separately_active(self):
        c = one_mode_intrinsic_localization_calibration(
            self.A, self.n, sp.Rational(1, 4), (self.x, self.y, self.z), self.t, self.nu
        )
        self.assertNotEqual(sp.simplify(c["kelvin_bulk_level"]), 0)
        self.assertNotEqual(sp.simplify(c["curvature_level"]), 0)

    def test_one_mode_three_face_rate_matches_global_normalization(self):
        c = one_mode_intrinsic_localization_calibration(
            self.A, self.n, self.theta, (self.x, self.y, self.z), self.t, self.nu
        )
        self.assertEqual(
            sp.simplify(c["local_growth_rate_level"] - self.theta * c["max_rate"]),
            0,
        )
        self.assertEqual(c["compatibility_defect"], 0)

    def test_absolute_enstrophy_threshold_is_similarity_artifact(self):
        c = one_mode_similarity_threshold_no_go(self.A, self.n, sp.Rational(1, 4), self.nu)
        self.assertEqual(c["max_enstrophy_n4_coefficient"], self.A**2 / 2)
        self.assertEqual(sp.limit(c["max_enstrophy"], self.n, sp.oo), sp.oo)
        self.assertEqual(c["compatibility_defect"], 0)

    def test_absolute_kelvin_bulk_threshold_is_similarity_artifact(self):
        c = one_mode_similarity_threshold_no_go(self.A, self.n, sp.Rational(1, 4), self.nu)
        self.assertEqual(c["kelvin_bulk_n6_coefficient"], 3 * self.A**2 * self.nu / 4)
        self.assertEqual(sp.limit(c["kelvin_bulk"], self.n, sp.oo), sp.oo)
        self.assertEqual(c["compatibility_defect"], 0)

    def test_max_envelope_dini_uses_active_rates_without_selector_path(self):
        a, b = sp.Integer(-5), sp.Integer(-2)
        self.assertEqual(max_envelope_left_dini([a, b]), -5)
        self.assertEqual(max_envelope_right_dini([a, b]), -2)

    def test_four_mode_crossing_is_literal_periodic_ns(self):
        c = four_mode_global_crossing_calibration(
            (self.x, self.y, self.z), self.t, self.nu
        )
        self.assertEqual(c["ns_residual"], sp.zeros(3, 1))
        self.assertEqual(c["q0"], 6)
        self.assertEqual(c["qpi"], 6)
        self.assertEqual(c["common_max_enstrophy"], 18)
        self.assertEqual(c["common_max_residual"], 0)

    def test_four_mode_crossing_has_exact_global_upper_certificate(self):
        c = four_mode_global_crossing_calibration(
            (self.x, self.y, self.z), self.t, self.nu
        )
        self.assertEqual(c["upper_certificate_residual"], 0)
        self.assertEqual(c["lower_decomposition_residual"], 0)
        self.assertEqual(c["lower_remainder_critical_plus"], 2 / (3 * sp.sqrt(3)))
        self.assertEqual(c["lower_remainder_critical_minus"], -2 / (3 * sp.sqrt(3)))
        self.assertTrue(c["lower_margin"].is_positive)

    def test_four_mode_crossing_global_maxima_are_nondegenerate(self):
        c = four_mode_global_crossing_calibration(
            (self.x, self.y, self.z), self.t, self.nu
        )
        self.assertEqual(c["hessian_yy_0"], -240)
        self.assertEqual(c["hessian_yy_pi"], -336)

    def test_four_mode_global_max_envelope_has_forced_dini_switch(self):
        c = four_mode_global_crossing_calibration(
            (self.x, self.y, self.z), self.t, self.nu
        )
        self.assertEqual(c["left_dini"], -336 * self.nu)
        self.assertEqual(c["right_dini"], -240 * self.nu)
        self.assertEqual(c["dini_jump"], 96 * self.nu)
        self.assertEqual(c["gap_rate"], 96 * self.nu)

    def test_four_mode_global_max_rates_are_literal_curvature_faces(self):
        c = four_mode_global_crossing_calibration(
            (self.x, self.y, self.z), self.t, self.nu
        )
        self.assertEqual(c["stretching_0"], 0)
        self.assertEqual(c["stretching_pi"], 0)
        self.assertEqual(c["kelvin_bulk_0"], 0)
        self.assertEqual(c["kelvin_bulk_pi"], 0)
        self.assertEqual(c["curvature_0"], -240 * self.nu)
        self.assertEqual(c["curvature_pi"], -336 * self.nu)
        self.assertEqual(c["balance_0"], 0)
        self.assertEqual(c["balance_pi"], 0)

    def test_similarity_invariant_defect_is_not_absolute_face_size(self):
        c = one_mode_similarity_threshold_no_go(self.A, self.n, sp.Rational(1, 4), self.nu)
        defect_hat = normalized_superlevel_compatibility_defect(
            c["local_rate"], sp.Rational(1, 4), c["max_rate"], c["max_enstrophy"]
        )
        self.assertEqual(sp.simplify(defect_hat), 0)
        self.assertNotEqual(c["kelvin_bulk"], 0)

    def test_superlevel_compatibility_defect_is_three_face_difference(self):
        S, K, C, Md = sp.symbols("S K C Md", real=True)
        R = S - K + C
        self.assertEqual(
            superlevel_material_compatibility_defect(R, self.theta, Md),
            S - K + C - self.theta * Md,
        )


if __name__ == "__main__":
    unittest.main()
