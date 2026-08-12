from __future__ import annotations

from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.active_pair import matrix_is_zero, pair_lift  # noqa: E402
from pde_audit.kelvin_admissibility import (  # noqa: E402
    canonical_boundary_gauge_witness,
    exact_gauge_work,
    factor_through_cycle_library,
    full_pair_factorization_residual,
    nonlinear_cycle_tangent_boundary,
    operator_transport_decomposition,
    pair_curve_boundary,
    pair_curve_derivative,
    realized_operator,
    restricted_pair_boundary,
    restricted_physical_boundary,
)


def figure_eight_complex() -> tuple[sp.Matrix, sp.Matrix]:
    # Two oriented 2-edge loops sharing vertex v0.
    B = sp.Matrix([
        [-1, 1, -1, 1],
        [1, -1, 0, 0],
        [0, 0, 1, -1],
    ])
    K = sp.Matrix([
        [1, 0],
        [1, 0],
        [0, 1],
        [0, 1],
    ])
    return B, K


class KelvinCKAdmissibilityAudit(unittest.TestCase):
    def test_arbitrary_nonidempotent_cycle_preserving_operator_has_zero_intrinsic_boundary(self) -> None:
        B, K = figure_eight_complex()
        P = sp.simplify(K * (K.T * K).inv() * K.T)
        Q = sp.eye(4) - P
        L = sp.Matrix([[2, 1], [-1, 3]])
        H = sp.simplify(K * L * (K.T * K).inv() * K.T + 5 * Q)
        self.assertNotEqual(sp.simplify(H * H - H), sp.zeros(4))
        self.assertEqual(sp.simplify(H * K - K * L), sp.zeros(4, 2))
        self.assertTrue(matrix_is_zero(restricted_physical_boundary(B, H, K)))
        self.assertTrue(matrix_is_zero(restricted_pair_boundary(B, H, K)))

    def test_cycle_preserving_operator_factors_as_coefficient_map_and_full_pair_map(self) -> None:
        B, K = figure_eight_complex()
        L = sp.Matrix([[2, 1], [-1, 3]])
        Y = K * L
        fac = factor_through_cycle_library(K, Y)
        self.assertEqual(fac.coordinates, L)
        self.assertEqual(fac.residual, sp.zeros(4, 2))
        self.assertEqual(B * Y, sp.zeros(3, 2))
        self.assertEqual(full_pair_factorization_residual(K, L), sp.zeros(16, 4))

    def test_off_cycle_ambient_extension_is_irrelevant_if_restriction_is_cycle_preserving(self) -> None:
        B, K = figure_eight_complex()
        P = sp.simplify(K * (K.T * K).inv() * K.T)
        Q = sp.eye(4) - P
        H1 = 2 * P
        H2 = 2 * P + sp.Matrix([
            [1, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 3, 0],
            [0, 0, 0, 4],
        ]) * Q
        self.assertEqual(sp.simplify(H1 * K - H2 * K), sp.zeros(4, 2))
        self.assertNotEqual(sp.simplify(B * H1 - B * H2), sp.zeros(3, 4))
        self.assertTrue(matrix_is_zero(restricted_physical_boundary(B, H1, K)))
        self.assertTrue(matrix_is_zero(restricted_physical_boundary(B, H2, K)))

    def test_cycle_breaking_operation_exposes_exact_gauge_form(self) -> None:
        # Triangle cycle Z=(1,1,1).  Keeping only one edge creates a true boundary.
        B = sp.Matrix([
            [-1, 0, 1],
            [1, -1, 0],
            [0, 1, -1],
        ])
        Z = sp.Matrix([1, 1, 1])
        H = sp.diag(1, 0, 0)
        Y = H * Z
        b = B * Y
        self.assertNotEqual(b, sp.zeros(3, 1))
        p = b
        self.assertEqual(exact_gauge_work(p, B, Y), 2)
        self.assertEqual(canonical_boundary_gauge_witness(B, Y), 2)

    def test_nonidempotent_operator_transport_is_exact_product_rule(self) -> None:
        h11, h12, h21, h22 = sp.symbols("h11 h12 h21 h22")
        dh11, dh12, dh21, dh22 = sp.symbols("dh11 dh12 dh21 dh22")
        H = sp.Matrix([[h11, h12], [h21, h22]])
        Hdot = sp.Matrix([[dh11, dh12], [dh21, dh22]])
        K = sp.Matrix([[1, 0], [0, 1]])
        Kdot = sp.Matrix([[1, 2], [3, 4]])
        T_out = sp.Matrix([[0, 1], [-1, 0]])
        T_mid = sp.Matrix([[2, 0], [1, -1]])
        A = sp.Matrix([[0, 3], [5, 0]])
        dec = operator_transport_decomposition(T_out, H, T_mid, K, A, Hdot, Kdot)
        self.assertEqual(sp.simplify(dec.total - dec.reconstructed), sp.zeros(2))

    def test_differentiable_nonlinear_cycle_map_has_cycle_tangent_and_no_pair_boundary(self) -> None:
        B = sp.Matrix([
            [-1, 0, 1],
            [1, -1, 0],
            [0, 1, -1],
        ])
        K = sp.Matrix([1, 1, 1])
        a, adot = sp.symbols("a adot")
        coeff = a + a**2
        Z = K * coeff
        Zdot = sp.diff(Z, a) * adot
        J = sp.diff(Z, a)
        self.assertEqual(B * Z, sp.zeros(3, 1))
        self.assertEqual(nonlinear_cycle_tangent_boundary(B, J), sp.zeros(3, 1))
        pair_bdy = pair_curve_boundary(B, Z, Zdot)
        self.assertEqual(pair_bdy, sp.zeros(*pair_bdy.shape))
        direct = sp.diff(pair_lift(Z), a) * adot
        self.assertEqual(sp.simplify(direct - pair_curve_derivative(Z, Zdot)), sp.zeros(9, 1))

    def test_exact_abc_pressure_distinguishes_closed_cycle_from_open_current(self) -> None:
        x, y, z, t, nu = sp.symbols("x y z t nu", positive=True)
        amp = sp.exp(-nu * t)
        u = amp * sp.Matrix([
            sp.sin(z) + sp.cos(y),
            sp.sin(x) + sp.cos(z),
            sp.sin(y) + sp.cos(x),
        ])
        p = -sp.Rational(1, 2) * u.dot(u)
        dpdx = sp.simplify(sp.diff(p, x).subs({y: sp.pi / 2, z: 0}))
        closed = sp.simplify(sp.trigsimp(sp.integrate(dpdx, (x, 0, 2 * sp.pi))))
        open_segment = sp.simplify(sp.trigsimp(sp.integrate(dpdx, (x, 0, sp.pi))))
        self.assertEqual(closed, 0)
        self.assertEqual(sp.simplify(open_segment - 2 * amp**2), 0)

    def test_original_allowed_pair_content_defect_is_zero_for_full_cycle_map(self) -> None:
        # The original Pi_irr placeholder compared physical full pair content with
        # an "allowed" pair content.  For a genuine cycle coefficient map L, the
        # natural allowed map is exactly L tensor L, so the content defect is zero.
        B, K = figure_eight_complex()
        L = sp.Matrix([[1, 2], [3, -1]])
        Y = K * L
        full = pair_lift(Y)
        allowed = pair_lift(K) * pair_lift(L)
        self.assertEqual(sp.simplify(full - allowed), sp.zeros(*full.shape))
        self.assertTrue(matrix_is_zero(restricted_pair_boundary(B, sp.eye(4), Y)))


if __name__ == "__main__":
    unittest.main()
