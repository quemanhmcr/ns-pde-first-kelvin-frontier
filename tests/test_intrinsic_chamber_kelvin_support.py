import unittest
import sympy as sp

from src.pde_audit.intrinsic_chamber_kelvin_support import (
    chamber_boundary_level_residual,
    centered_one_mode_endpoint_nonaffinity,
    centered_one_mode_physical_residual_z,
    intrinsic_chamber_packet_state,
    unit_transverse_intrinsic_support_no_go,
)
from src.pde_audit.intrinsic_enstrophy_localization import integer_scaled_one_mode_ns_residual


class IntrinsicChamberKelvinSupportTests(unittest.TestCase):
    def setUp(self):
        self.x, self.y, self.z, self.t = sp.symbols("x y z t", real=True)
        self.nu = sp.symbols("nu", positive=True)
        self.A = sp.symbols("A", positive=True)
        self.n = sp.symbols("n", positive=True)
        self.alpha = sp.symbols("alpha", positive=True)
        self.coords = (self.x, self.y, self.z)

    def state(self):
        return intrinsic_chamber_packet_state(
            self.A, self.n, self.alpha, 1, 1, self.coords, self.t, self.nu
        )

    def witness(self):
        return unit_transverse_intrinsic_support_no_go(
            self.A, self.n, self.alpha, self.coords, self.t, self.nu
        )

    def test_underlying_one_mode_field_is_literal_periodic_ns(self):
        r = integer_scaled_one_mode_ns_residual(self.A, self.n, self.coords, self.t, self.nu)
        self.assertEqual(r, sp.zeros(3, 1))

    def test_packet_exactly_spans_intrinsic_chamber_normally(self):
        self.assertEqual(chamber_boundary_level_residual(self.alpha, self.n), 0)
        s = self.state()
        self.assertEqual(s.y_span, 2 * self.alpha / self.n)
        self.assertEqual(s.level, sp.cos(self.alpha) ** 2)

    def test_scalar_compatibility_and_uniform_ancestry_flux_are_zero(self):
        s = self.state()
        self.assertEqual(s.compatibility_defect, 0)
        self.assertEqual(s.uniform_ancestry_flux, 0)

    def test_orientation_complete_area_frame_retains_transverse_face(self):
        H = self.state().area_frame
        expected = sp.diag(2 * self.alpha / self.n, 1, 2 * self.alpha / self.n)
        self.assertEqual(H, expected)

    def test_packet_volume_collapses_without_area_frame_collapse(self):
        s = self.state()
        self.assertEqual(sp.limit(sp.det(s.line_frame), self.alpha, 0, dir="+"), 0)
        Hlim = s.area_frame.applyfunc(lambda q: sp.limit(q, self.alpha, 0, dir="+"))
        self.assertEqual(Hlim, sp.diag(0, 1, 0))

    def test_exact_centered_kelvin_physical_residual(self):
        s = self.state()
        expected = centered_one_mode_physical_residual_z(self.A, self.n, self.alpha, self.t, self.nu)
        self.assertEqual(sp.simplify(s.physical_residual[2] - expected), 0)
        self.assertEqual(s.physical_residual[0], 0)
        self.assertEqual(s.physical_residual[1], 0)

    def test_target_gradient_and_orientation_qv_vanish_at_maximum(self):
        s = self.state()
        self.assertEqual(s.target_gradient, sp.zeros(3))
        self.assertEqual(s.orientation_qv, sp.zeros(3))

    def test_centered_anchor_residual_noise_is_exactly_zero(self):
        s = self.state()
        self.assertEqual(s.residual_noise, sp.zeros(3))
        self.assertEqual(s.full_codeforming_noise, sp.zeros(3))

    def test_support_tensor_retains_two_transverse_directions(self):
        self.assertEqual(self.state().tangential_support_tensor, sp.diag(1, 0, 1))

    def test_tangential_support_nanson_rate_is_zero(self):
        self.assertEqual(self.state().tangential_support_rate, sp.zeros(3))

    def test_support_tensor_does_not_collapse_in_nested_chambers(self):
        B = self.state().support_tensor
        Blim = B.applyfunc(lambda q: sp.limit(q, self.alpha, 0, dir="+"))
        self.assertEqual(Blim, sp.diag(1, 0, 1))
        self.assertEqual(self.witness()["diameter_limit"], 2)

    def test_orientation_complete_quadrupoles_reconstruct_support(self):
        s = self.state()
        residual = sp.simplify(s.quadrupole_sum - sp.Rational(2, 3) * s.support_tensor)
        self.assertEqual(residual, sp.zeros(3))

    def test_transverse_face_quadrupole_stays_nonzero(self):
        _, middle, _ = self.state().face_quadrupoles
        self.assertEqual(middle, sp.diag(sp.Rational(1, 3), 0, sp.Rational(1, 3)))

    def test_endpoint_shape_drift_collapses(self):
        val = self.state().endpoint_nonaffinity[0]
        self.assertEqual(sp.limit(val, self.alpha, 0, dir="+"), 0)

    def test_conditioning_diverges_while_compatibility_is_zero(self):
        w = self.witness()
        self.assertEqual(w["compatibility_defect"], 0)
        self.assertEqual(w["condition_limit"], sp.oo)

    def test_residual_and_diameter_limits_are_distinct(self):
        w = self.witness()
        self.assertEqual(w["residual_limit"], 0)
        self.assertEqual(w["diameter_limit"], 2)

    def test_persistent_transverse_face_is_kelvin_flux_blind(self):
        s = self.state()
        self.assertEqual(s.area_frame[1, 1], 1)
        self.assertEqual(s.circulation[1], 0)
        self.assertEqual((s.area_frame.T * s.target_vorticity)[1], 0)
        self.assertEqual(s.raw_error[1], 0)


if __name__ == "__main__":
    unittest.main()
