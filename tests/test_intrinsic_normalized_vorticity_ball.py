from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.first_bad_candidate_exclusions import gradient
from src.pde_audit.intrinsic_normalized_vorticity_ball import (
    boundary_tangency_identity_residual,
    directional_contact_split_residual,
    elliptic_polarization_contact_calibration,
    left_right_gram_trace_residual,
    normalized_enstrophy,
    normalized_gradient_right_gram,
    normalized_scalar_curvature,
    radial_second_derivative_form,
    unit_ball_contact_form,
    unit_ball_contact_identity_residual,
)


class IntrinsicNormalizedVorticityBallTests(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y, self.z, self.t = sp.symbols('x y z t', real=True)
        self.coords = (self.x, self.y, self.z)
        self.nu, self.a, self.k = sp.symbols('nu a k', positive=True)
        self.beta = sp.symbols('beta', nonnegative=True)

    def calibration(self):
        return elliptic_polarization_contact_calibration(
            self.a, self.beta, self.k, self.coords, self.t, self.nu
        )

    def test_contact_identity_is_exact_for_generic_vector_map(self) -> None:
        V = sp.Matrix([self.x + self.y, self.y * self.z, self.z + self.x**2])
        self.assertEqual(unit_ball_contact_identity_residual(V, self.coords), sp.zeros(3))

    def test_boundary_tangency_is_radius_derivative_identity(self) -> None:
        V = sp.Matrix([self.x, self.y**2, self.z + self.x * self.y])
        self.assertEqual(boundary_tangency_identity_residual(V, self.coords), sp.zeros(3, 1))

    def test_left_and_right_gradient_grams_have_same_bulk_trace(self) -> None:
        V = sp.Matrix([self.x * self.y, self.y * self.z, self.z * self.x])
        self.assertEqual(left_right_gram_trace_residual(V, self.coords), 0)

    def test_radial_contact_split_is_exact(self) -> None:
        V = sp.Matrix([sp.cos(self.z), sp.sin(self.z) / 2, 0])
        Gr = normalized_gradient_right_gram(V, self.coords)
        Q = normalized_scalar_curvature(V, self.coords)
        Hc = unit_ball_contact_form(V, self.coords)
        xi = sp.Matrix([0, 0, 1])
        self.assertEqual(directional_contact_split_residual(Hc, Gr, Q, xi), 0)
        self.assertEqual(sp.simplify(Hc + radial_second_derivative_form(V, self.coords)), sp.zeros(3))

    def test_elliptic_polarization_is_literal_periodic_ns(self) -> None:
        self.assertEqual(self.calibration()['ns_residual'], sp.zeros(3, 1))

    def test_normalized_vorticity_obeys_exact_vector_pde(self) -> None:
        c = self.calibration()
        self.assertEqual(c['normalized_vorticity_pde_residual'], sp.zeros(3, 1))
        self.assertEqual(c['log_scale_rate'], -self.nu * self.k**2)

    def test_scalar_localization_is_squared_radius(self) -> None:
        c = self.calibration()
        self.assertEqual(
            sp.simplify(c['normalized_enstrophy'] - normalized_enstrophy(c['normalized_vorticity'])), 0
        )


    def test_unit_ball_global_max_certificate_is_exact(self) -> None:
        c = self.calibration()
        self.assertEqual(c["unit_ball_gap_factor_residual"], 0)
        expected = (1 - self.beta**2) * sp.sin(self.k * self.z) ** 2
        self.assertEqual(sp.simplify(c["unit_ball_gap"] - expected), 0)


    def test_normalized_scalar_source_is_zero_for_stationary_shape(self) -> None:
        self.assertEqual(self.calibration()["scalar_source"], 0)

    def test_active_point_gradient_is_tangent_to_unit_sphere(self) -> None:
        c = self.calibration()
        V0 = sp.simplify(c["normalized_vorticity"].subs(self.z, 0))
        J0 = sp.simplify(gradient(c["normalized_vorticity"], self.coords).subs(self.z, 0))
        self.assertEqual(sp.simplify(J0.T * V0), sp.zeros(3, 1))
        self.assertEqual(c["tangency_identity_residual"], sp.zeros(3, 1))

    def test_contact_transfers_between_amplitude_and_orientation(self) -> None:
        c = self.calibration()
        self.assertEqual(c["polarization_transfer_residual"], 0)
        self.assertEqual(c["contact_frequency_residual"], 0)
        self.assertEqual(c["right_gram"][2, 2], self.beta**2 * self.k**2)
        self.assertEqual(sp.simplify(c["scalar_curvature"][2, 2] - 2 * (1 - self.beta**2) * self.k**2), 0)
        self.assertEqual(c["contact_form"][2, 2], self.k**2)

    def test_helical_endpoint_scalar_kernel_is_strictly_too_large(self) -> None:
        c = self.calibration()
        Qh = sp.simplify(c["scalar_curvature"].subs(self.beta, 1))
        Hh = sp.simplify(c["contact_form"].subs(self.beta, 1))
        Grh = sp.simplify(c["right_gram"].subs(self.beta, 1))
        self.assertEqual(Qh, sp.zeros(3))
        self.assertEqual(Grh, sp.diag(0, 0, self.k**2))
        self.assertEqual(Hh, sp.diag(0, 0, self.k**2))

    def test_linear_endpoint_is_pure_amplitude_curvature(self) -> None:
        c = self.calibration()
        self.assertEqual(sp.simplify(c["right_gram"].subs(self.beta, 0)), sp.zeros(3))
        self.assertEqual(sp.simplify(c["scalar_curvature"].subs(self.beta, 0)), sp.diag(0, 0, 2*self.k**2))
        self.assertEqual(sp.simplify(c["contact_form"].subs(self.beta, 0)), sp.diag(0, 0, self.k**2))

    def test_helical_endpoint_has_identically_flat_scalar_germ(self) -> None:
        c = self.calibration()
        gh = sp.simplify(sp.trigsimp(c["normalized_enstrophy"].subs(self.beta, 1)))
        self.assertEqual(gh, 1)
        for order in range(1, 9):
            self.assertEqual(sp.diff(gh, self.z, order), 0)


    def test_helical_scalar_flatness_does_not_kill_vector_gradient(self) -> None:
        c = self.calibration()
        Jh0 = sp.simplify(c["normalized_gradient"].subs({self.beta: 1, self.z: 0}))
        self.assertNotEqual(Jh0, sp.zeros(3))
        self.assertEqual(Jh0.T * Jh0, sp.diag(0, 0, self.k**2))

    def test_kelvin_qv_is_exact_left_gram_of_normalized_gradient(self) -> None:
        c = self.calibration()
        self.assertEqual(c["kelvin_left_gram_residual"], sp.zeros(3))
        self.assertEqual(c["gram_trace_residual"], 0)
        self.assertEqual(c["kelvin_bulk_trace_residual"], 0)


    def test_helical_kelvin_bulk_remains_nonzero(self) -> None:
        c = self.calibration()
        bulk = sp.simplify(c["kelvin_bulk"].subs(self.beta, 1))
        expected = self.a**2 * self.k**2 * self.nu * sp.exp(-2 * self.k**2 * self.nu * self.t)
        self.assertEqual(bulk, expected)
        self.assertNotEqual(bulk, 0)


    def test_left_and_right_grams_are_dual_faces(self) -> None:
        c = self.calibration()
        self.assertEqual(c["right_gram"], sp.diag(0, 0, self.beta**2 * self.k**2))
        self.assertEqual(c["left_gram"], sp.diag(0, self.beta**2 * self.k**2, 0))
        self.assertEqual(sp.trace(c["right_gram"]), sp.trace(c["left_gram"]))


    def test_contact_kernel_intersection_in_exact_ns_family(self) -> None:
        c = self.calibration()
        ex, ey, ez = sp.eye(3).columnspace()
        for xi in (ex, ey):
            self.assertEqual((xi.T * c["contact_form"] * xi)[0], 0)
            self.assertEqual((xi.T * c["scalar_curvature"] * xi)[0], 0)
            self.assertEqual((xi.T * c["right_gram"] * xi)[0], 0)
        self.assertEqual((ez.T * c["contact_form"] * ez)[0], self.k**2)


if __name__ == "__main__":
    unittest.main()
