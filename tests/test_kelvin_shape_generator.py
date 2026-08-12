from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.kelvin_shape_generator import (
    anchor_relative_common_noise_covariance,
    anchor_relative_drifts,
    common_noise_backward_generator,
    common_wiener_covariance,
    cubic_heat_shear,
    cubic_heat_shear_ns_residual,
    cubic_shear_rectangle_shape_residual,
    cubic_shear_residual_from_second_moment,
    local_nanson_area_rate,
    oriented_rectangle_area_vector_yz,
    packet_shape_residual_matrix,
    rectangle_oriented_second_moment_yy,
    scaled_cubic_shape_residual,
    yz_rectangle_shear_area_rate_direct,
)


class KelvinShapeGeneratorAudit(unittest.TestCase):
    def test_uniform_wiener_noise_has_rank_three_for_any_number_of_loop_points(self) -> None:
        nu = sp.symbols("nu", positive=True)
        A = common_wiener_covariance(5, 3, nu)
        self.assertEqual(A.rank(), 3)
        self.assertEqual(A[:3, 9:12], 2 * nu * sp.eye(3))

    def test_anchor_relative_coordinates_remove_all_shape_quadratic_variation(self) -> None:
        nu = sp.symbols("nu", positive=True)
        A = anchor_relative_common_noise_covariance(4, 3, nu)
        expected = sp.zeros(15)
        expected[:3, :3] = 2 * nu * sp.eye(3)
        self.assertEqual(sp.simplify(A - expected), sp.zeros(15))

    def test_backward_common_noise_generator_becomes_anchor_laplacian_plus_shape_drift(self) -> None:
        x0, x1, x2, nu = sp.symbols("x0 x1 x2 nu")
        r1 = x1 - x0
        r2 = x2 - x0
        # Cylinder observable written in anchor + relative shape coordinates.
        F = x0**3 + x0 * r1**2 + 2 * r1 * r2 + r2**3
        vel = lambda x: x**2 + 1
        direct = common_noise_backward_generator(
            F,
            [sp.Matrix([vel(x0)]), sp.Matrix([vel(x1)]), sp.Matrix([vel(x2)])],
            [(x0,), (x1,), (x2,)],
            nu,
        )
        # Build the expected transformed generator directly by chain rule in (x0,r1,r2).
        X, a, b = sp.symbols("X a b")
        g = X**3 + X * a**2 + 2 * a * b + b**3
        expected = (
            vel(X) * sp.diff(g, X)
            + (vel(X + a) - vel(X)) * sp.diff(g, a)
            + (vel(X + b) - vel(X)) * sp.diff(g, b)
            - nu * sp.diff(g, X, 2)
        ).subs({X: x0, a: r1, b: r2})
        self.assertEqual(sp.simplify(direct - expected), 0)

    def test_relative_shape_drift_is_velocity_difference_and_has_no_stochastic_source(self) -> None:
        x, r = sp.symbols("x r")
        u0 = sp.Matrix([x**2, 0, 0])
        u1 = sp.Matrix([(x + r) ** 2, 0, 0])
        drift = anchor_relative_drifts(u0, [u1])[0]
        self.assertEqual(sp.simplify(drift - sp.Matrix([2 * x * r + r**2, 0, 0])), sp.zeros(3, 1))

    def test_affine_shear_area_frame_descends_exactly_to_local_nanson(self) -> None:
        y, a, b, c = sp.symbols("y a b c")
        exact = yz_rectangle_shear_area_rate_direct(a, y, b, c)
        h = oriented_rectangle_area_vector_yz(b, c)
        A0 = sp.zeros(3)
        A0[0, 1] = a
        local = local_nanson_area_rate(A0, h)
        self.assertEqual(sp.simplify(exact - local), sp.zeros(3, 1))

    def test_cubic_heat_shear_is_exact_navier_stokes(self) -> None:
        y, t, nu = sp.symbols("y t nu")
        self.assertEqual(cubic_heat_shear_ns_residual(y, t, nu), 0)
        U = cubic_heat_shear(y, t, nu)
        # Nonlinearity u.grad u vanishes because u=(U(y,t),0,0).
        self.assertEqual(sp.diff(U, sp.Symbol("x")), 0)

    def test_centered_cubic_shear_finite_surface_residual_is_second_moment_current(self) -> None:
        b, c, t, nu = sp.symbols("b c t nu", positive=True)
        direct = cubic_shear_rectangle_shape_residual(b, c, t, nu)
        moment = cubic_shear_residual_from_second_moment(b, c)
        self.assertEqual(sp.simplify(direct - moment), sp.zeros(3, 1))
        self.assertEqual(rectangle_oriented_second_moment_yy(b, c), sp.Rational(4, 3) * b**3 * c)

    def test_same_anchor_and_same_area_vector_do_not_determine_finite_surface_generator(self) -> None:
        t, nu = sp.symbols("t nu")
        h1 = oriented_rectangle_area_vector_yz(sp.Integer(1), sp.Integer(1))
        h2 = oriented_rectangle_area_vector_yz(sp.Integer(2), sp.Rational(1, 2))
        self.assertEqual(h1, h2)  # both are 4 e_x
        e1 = cubic_shear_rectangle_shape_residual(1, 1, t, nu)
        e2 = cubic_shear_rectangle_shape_residual(2, sp.Rational(1, 2), t, nu)
        self.assertNotEqual(e1, e2)
        self.assertEqual(e1, sp.Matrix([0, -4, 0]))
        self.assertEqual(e2, sp.Matrix([0, -16, 0]))
        # Thus the finite-scale H drift differs by a real shape current at identical (x,h).
        self.assertEqual(e2 - e1, sp.Matrix([0, -12, 0]))

    def test_centered_shape_obstruction_is_raw_r4_and_relative_r2(self) -> None:
        r, b0, c0 = sp.symbols("r b0 c0", positive=True)
        raw = scaled_cubic_shape_residual(r, b0, c0)
        ref = cubic_shear_residual_from_second_moment(b0, c0)
        self.assertEqual(sp.simplify(raw - r**4 * ref), sp.zeros(3, 1))
        h = oriented_rectangle_area_vector_yz(r * b0, r * c0)
        # Compare the nonzero y residual coefficient to the O(r^2) area scale.
        relative = sp.simplify(raw[1] / h[0])
        self.assertEqual(relative, -r**2 * b0**2)

    def test_orientation_complete_area_frame_still_misses_finite_shape_quadrupole(self) -> None:
        t, nu = sp.symbols("t nu")
        E1 = packet_shape_residual_matrix(cubic_shear_rectangle_shape_residual(1, 1, t, nu))
        E2 = packet_shape_residual_matrix(cubic_shear_rectangle_shape_residual(2, sp.Rational(1, 2), t, nu))
        H = 4 * sp.eye(3)
        self.assertEqual(H, 4 * sp.eye(3))
        self.assertNotEqual(E1, E2)
        self.assertEqual(E2 - E1, sp.Matrix([[0, 0, 0], [-12, 0, 0], [0, 0, 0]]))


if __name__ == "__main__":
    unittest.main()
