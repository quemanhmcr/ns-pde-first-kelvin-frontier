from __future__ import annotations

import unittest

import sympy as sp

from src.pde_audit.cycle_selector import two_cycle_library
from src.pde_audit.deformation_current_pair_coupling import (
    selected_deformation_pair_decomposition,
    selected_deformation_pair_dyad_residual,
    spatial_fiber_boundary,
    spatial_fiber_boundary_factorization_residual,
    spatial_fiber_current_map,
    spatial_fiber_pair_boundary_factorization_residual,
    tangent_carre_du_champ,
    tangent_cochain_covariance,
    tangent_cochain_readout_residual,
    tangent_deformation_covariance,
    tangent_projection_residual,
)
from src.pde_audit.kelvin_shape_generator import (
    cubic_shear_rectangle_shape_residual,
    oriented_rectangle_area_vector_yz,
)
from src.pde_audit.stochastic_cauchy_deformation import (
    column_vectorize,
    vectorized_deformation_carre_du_champ,
    vectorized_deformation_covariance_leading_tensor,
)


class DeformationCurrentPairCouplingAudit(unittest.TestCase):
    def test_deformation_is_spatial_fiber_transport_and_preserves_closed_selected_cycles(self) -> None:
        B, K = two_cycle_library()
        M = sp.diag(1, 0)
        P = K * M
        D = sp.Matrix([[1, 2, 0], [0, 1, 3], [0, 0, 1]])
        self.assertEqual(B * P, sp.zeros(B.rows, P.cols))
        self.assertEqual(
            spatial_fiber_boundary_factorization_residual(B, P, D),
            sp.zeros(B.rows * 3, P.cols * 3),
        )
        lifted_boundary = spatial_fiber_boundary(B, 3)
        lifted_current = spatial_fiber_current_map(P, D)
        self.assertEqual(
            sp.simplify(lifted_boundary * lifted_current),
            sp.zeros(B.rows * 3, P.cols * 3),
        )

    def test_pair_boundary_has_only_the_two_chain_faces_and_no_deformation_seam(self) -> None:
        B, K = two_cycle_library()
        P = K * sp.diag(0, 1)
        D = sp.Matrix([[2, 1], [1, 1]])
        # Use a two-dimensional spatial fiber; chain closure is dimension-independent.
        self.assertEqual(
            spatial_fiber_pair_boundary_factorization_residual(B, P, D),
            sp.zeros(2 * B.rows * 2 * P.rows * 2, P.cols**2 * 2**2),
        )

    def test_fixed_tangent_is_exact_linear_projection_of_full_vecD_covariance(self) -> None:
        a, b, c, d = sp.symbols("a b c d")
        D = sp.Matrix([[a, b], [c, d]])
        e = sp.Matrix([2, -1])
        self.assertEqual(tangent_projection_residual(D, e), sp.zeros(2, 1))

        deformations = [sp.eye(2), sp.Matrix([[1, 2], [3, 1]])]
        z1, z2 = map(column_vectorize, deformations)
        zbar = sp.simplify((z1 + z2) / 2)
        Sigma = sp.simplify((z1 * z1.T + z2 * z2.T) / 2 - zbar * zbar.T)
        y1 = deformations[0].T * e
        y2 = deformations[1].T * e
        ybar = sp.simplify((y1 + y2) / 2)
        direct = sp.simplify((y1 * y1.T + y2 * y2.T) / 2 - ybar * ybar.T)
        self.assertEqual(sp.simplify(tangent_deformation_covariance(Sigma, e) - direct), sp.zeros(2))

    def test_fixed_local_cochain_readout_projects_vecD_covariance_without_new_sector(self) -> None:
        D = sp.Matrix([[1, 2], [3, 4]])
        e = sp.Matrix([2, -1])
        alpha = sp.Matrix([5, 7])
        self.assertEqual(tangent_cochain_readout_residual(D, e, alpha), 0)

        q = sp.symbols("q", positive=True)
        v = sp.Matrix([1, 0, 0, 1])
        Sigma = q * v * v.T
        ell = sp.kronecker_product(alpha, e)
        expected = sp.simplify(q * (ell.T * v)[0] ** 2)
        self.assertEqual(tangent_cochain_covariance(Sigma, e, alpha), expected)

    def test_short_horizon_current_projection_keeps_same_2nu_over_3_source(self) -> None:
        nu, h = sp.symbols("nu h", positive=True)
        g11, g12, g21, g22 = sp.symbols("g11 g12 g21 g22")
        q11, q12, q21, q22 = sp.symbols("q11 q12 q21 q22")
        dAx = sp.Matrix([[g11, g12], [g21, g22]])
        dAy = sp.Matrix([[q11, q12], [q21, q22]])
        e = sp.Matrix([sp.Symbol("e1"), sp.Symbol("e2")])
        alpha = sp.Matrix([sp.Symbol("a1"), sp.Symbol("a2")])
        Sigma3 = vectorized_deformation_covariance_leading_tensor([dAx, dAy], nu, h)
        observed = tangent_cochain_covariance(Sigma3, e, alpha)
        expected = sp.simplify(
            sp.Rational(2, 3) * nu * h**3 * (
                (alpha.T * dAx * e)[0] ** 2 + (alpha.T * dAy * e)[0] ** 2
            )
        )
        self.assertEqual(sp.simplify(observed - expected), 0)

    def test_carre_du_champ_projects_to_current_tangent_without_pathwise_D_qv(self) -> None:
        nu = sp.symbols("nu", positive=True)
        x, y = sp.symbols("x y")
        mD = sp.Matrix([[1 + x, y], [x*y, 1]])
        Gamma = vectorized_deformation_carre_du_champ([sp.diff(mD, x), sp.diff(mD, y)], nu)
        e = sp.Matrix([2, 3])
        projected = tangent_carre_du_champ(Gamma, e)
        direct_grads = [sp.diff(mD.T * e, q) for q in (x, y)]
        direct = sp.simplify(2 * nu * sum((g * g.T for g in direct_grads), sp.zeros(2)))
        self.assertEqual(sp.simplify(projected - direct), sp.zeros(2))

    def test_two_replica_selected_current_has_selector_deformation_and_mandatory_cross_pair_terms(self) -> None:
        P1 = sp.Matrix([[1, 0], [0, 0]])
        P2 = sp.Matrix([[0, 0], [0, 1]])
        D1 = sp.Matrix([[1, 1], [0, 1]])
        D2 = sp.Matrix([[1, 0], [2, 1]])
        dec = selected_deformation_pair_decomposition(P1, D1, P2, D2)
        self.assertEqual(sp.simplify(dec.total_difference - dec.reconstructed_difference), sp.zeros(4))
        self.assertEqual(selected_deformation_pair_dyad_residual(P1, D1, P2, D2), sp.zeros(16))
        _, selector, deformation, cross = dec.pair_lift_parts()
        self.assertNotEqual(selector, sp.zeros(16))
        self.assertNotEqual(deformation, sp.zeros(16))
        self.assertNotEqual(cross, sp.zeros(16))

    def test_shared_first_bad_selector_removes_selector_and_cross_pair_sectors(self) -> None:
        P = sp.Matrix([[1, 0], [0, 0]])
        D1 = sp.Matrix([[1, 1], [0, 1]])
        D2 = sp.Matrix([[1, 0], [2, 1]])
        dec = selected_deformation_pair_decomposition(P, D1, P, D2)
        _, selector, deformation, cross = dec.pair_lift_parts()
        self.assertEqual(selector, sp.zeros(16))
        self.assertNotEqual(deformation, sp.zeros(16))
        self.assertEqual(cross, sp.zeros(16))

    def test_exact_cubic_ns_blocks_D_only_descent_of_finite_surface_current(self) -> None:
        t, nu = sp.symbols("t nu")
        # Same anchor and same initial local deformation D=I.  The two finite
        # surfaces also have the same area vector, yet their literal NS shape
        # currents differ.  Hence D (even together with local H) is not a complete
        # finite-current state.
        h1 = oriented_rectangle_area_vector_yz(1, 1)
        h2 = oriented_rectangle_area_vector_yz(2, sp.Rational(1, 2))
        self.assertEqual(h1, h2)
        e1 = cubic_shear_rectangle_shape_residual(1, 1, t, nu)
        e2 = cubic_shear_rectangle_shape_residual(2, sp.Rational(1, 2), t, nu)
        self.assertEqual(e1, sp.Matrix([0, -4, 0]))
        self.assertEqual(e2, sp.Matrix([0, -16, 0]))
        self.assertEqual(e2 - e1, sp.Matrix([0, -12, 0]))


if __name__ == "__main__":
    unittest.main()
