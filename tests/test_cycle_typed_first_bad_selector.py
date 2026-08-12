from __future__ import annotations

import math
from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.active_pair import (  # noqa: E402
    boundary_residual,
    matrix_is_zero,
    pair_boundary_residual,
    pair_lift,
)
from pde_audit.cycle_selector import (  # noqa: E402
    cycle_library_boundary,
    cycle_selector_boundary_residual,
    cycle_selector_pair_boundary_residual,
    cycle_span_projector,
    first_bad_projection,
    germ_cut_formula,
    germ_support_transport_commutator,
    hysteretic_first_bad_projection,
    incidence_cut_formula,
    incidence_mask_commutator,
    pair_jump_decomposition,
    rank_one_selector,
    restricted_ambient_commutator,
    selected_cycle_map,
    selector_transport_decomposition,
    two_cycle_library,
)
from pde_audit.exact_shear import (  # noqa: E402
    kelvin_anchor_covariance,
    kelvin_anchor_moments,
    kelvin_increment_variance,
)


class CycleTypedFirstBadSelectorAudit(unittest.TestCase):
    def test_cycle_library_is_physically_closed(self) -> None:
        B, K = two_cycle_library()
        self.assertTrue(matrix_is_zero(cycle_library_boundary(B, K)))

    def test_canonical_cycle_span_projection_is_idempotent_and_physically_closed(self) -> None:
        B, K = two_cycle_library()
        H = cycle_span_projector(K)
        self.assertEqual(sp.simplify(H * H - H), sp.zeros(*H.shape))
        self.assertTrue(matrix_is_zero(B * H))
        self.assertEqual(sp.simplify(H * K - K), sp.zeros(*K.shape))

    def test_any_first_bad_choice_preserves_physical_closedness(self) -> None:
        B, K = two_cycle_library()
        for flags in [(False, False), (True, False), (False, True), (True, True)]:
            M = first_bad_projection(flags)
            self.assertTrue(matrix_is_zero(cycle_selector_boundary_residual(B, K, M)))
            self.assertTrue(matrix_is_zero(cycle_selector_pair_boundary_residual(B, K, M)))

        # Priority is literal: if both are bad, the first germ alone is selected.
        self.assertEqual(first_bad_projection((True, True)), sp.diag(1, 0))

    def test_hysteresis_freezes_until_resolve_then_reselects(self) -> None:
        M0, idx0 = hysteretic_first_bad_projection((False, True, True), None, resolved=False)
        self.assertEqual(idx0, 1)
        self.assertEqual(M0, sp.diag(0, 1, 0))

        # A new earlier bad germ appears, but the selector is frozen.
        M1, idx1 = hysteretic_first_bad_projection((True, True, True), idx0, resolved=False)
        self.assertEqual(idx1, 1)
        self.assertEqual(M1, M0)

        # Resolve is the finite reset event; only then is priority recomputed.
        M2, idx2 = hysteretic_first_bad_projection((True, False, True), idx1, resolved=True)
        self.assertEqual(idx2, 0)
        self.assertEqual(M2, sp.diag(1, 0, 0))

    def test_support_mask_commutator_is_exact_cut_incidence_current(self) -> None:
        B = sp.Matrix([[-1, 0], [1, -1], [0, 1]])
        edge = [1, 0]
        vertex = [1, 1, 0]
        C = incidence_mask_commutator(B, edge, vertex)
        expected = incidence_cut_formula(B, edge, vertex)
        self.assertEqual(C, expected)
        self.assertEqual(C, sp.Matrix([[0, 0], [0, 1], [0, 0]]))

    def test_selector_boundary_failure_can_only_come_from_noncycle_realization(self) -> None:
        B, K = two_cycle_library()
        M = rank_one_selector(2, 0)
        self.assertEqual(cycle_selector_boundary_residual(B, K, M), (B * K) * M)
        self.assertTrue(matrix_is_zero((B * K) * M))

        # Break closedness in the realization itself.  The selector merely carries
        # that pre-existing boundary; it does not manufacture a new one.
        K_bad = K.copy()
        K_bad[0, 0] += 1
        lhs = cycle_selector_boundary_residual(B, K_bad, M)
        rhs = sp.simplify((B * K_bad) * M)
        self.assertEqual(lhs, rhs)
        self.assertFalse(matrix_is_zero(lhs))

    def test_global_ambient_commutator_is_extension_dependent_but_cycle_restriction_is_zero(self) -> None:
        # One physical cycle z=e0-e1 in a two-parallel-edge graph.
        B = sp.Matrix([[-1, -1], [1, 1]])
        K = sp.Matrix([[1], [-1]])
        F1 = sp.eye(2)

        # Two degree-zero extensions agree on every physical cycle because B K=0,
        # but their global ambient commutators differ.
        C_chain = boundary_residual(B, F1, sp.eye(2), B)
        C_arbitrary = boundary_residual(B, F1, sp.zeros(2), B)
        self.assertTrue(matrix_is_zero(C_chain))
        self.assertFalse(matrix_is_zero(C_arbitrary))
        self.assertTrue(matrix_is_zero(restricted_ambient_commutator(B, F1, sp.zeros(2), B, K)))

        C2_arbitrary = pair_boundary_residual(B, F1, sp.zeros(2), B)
        self.assertFalse(matrix_is_zero(C2_arbitrary))
        self.assertTrue(matrix_is_zero(sp.simplify(C2_arbitrary * pair_lift(K))))

    def test_germ_transport_commutator_is_exact_support_cut_flux(self) -> None:
        A = sp.Matrix([[0, 2, -1], [3, 0, 5], [7, 11, 0]])
        activity = [1, 0, 0]
        comm = germ_support_transport_commutator(A, activity)
        cut = germ_cut_formula(A, activity)
        self.assertEqual(comm, cut)
        # Entries wholly inside active or inactive support vanish.  Only crossings
        # of the first-bad chamber survive.
        self.assertEqual(comm[1, 2], 0)
        self.assertEqual(comm[2, 1], 0)
        self.assertNotEqual(comm[0, 1], 0)
        self.assertNotEqual(comm[1, 0], 0)

    def test_selector_transport_splits_exactly_into_realization_and_support_parts(self) -> None:
        T = sp.Matrix([[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 2], [0, 0, -2, 0]])
        A = sp.Matrix([[0, 3], [-3, 0]])
        _, K = two_cycle_library()
        M = sp.Matrix([[1, 0], [0, 0]])
        Kdot = sp.Matrix([[1, 0], [1, 0], [0, -1], [0, -1]])
        Mdot = sp.Matrix([[0, 2], [2, 0]])
        dec = selector_transport_decomposition(T, K, A, M, Kdot, Mdot)
        self.assertEqual(sp.simplify(dec.total - dec.realization - dec.support), sp.zeros(*dec.total.shape))

    def test_exact_selected_covariance_bank_chain_rule_on_cycle_coefficients(self) -> None:
        # V=a^T C a with Cdot=-Gamma.  For a continuously moving selector
        # coefficient a(s), dV/ds=-Gamma(a,a)+2 C(a,adot) exactly.
        c11, c12, c22 = sp.symbols("c11 c12 c22")
        g11, g12, g22 = sp.symbols("g11 g12 g22")
        a1, a2, da1, da2 = sp.symbols("a1 a2 da1 da2")
        C = sp.Matrix([[c11, c12], [c12, c22]])
        Gamma = sp.Matrix([[g11, g12], [g12, g22]])
        a = sp.Matrix([a1, a2])
        adot = sp.Matrix([da1, da2])
        dV = (-(a.T * Gamma * a)[0] + (adot.T * C * a)[0] + (a.T * C * adot)[0])
        gamma = (a.T * Gamma * a)[0]
        covariance_work = 2 * (a.T * C * adot)[0]
        self.assertEqual(sp.expand(dV + gamma - covariance_work), 0)

        # The finite jump version is the exact quadratic reset identity.
        d1, d2 = sp.symbols("d1 d2")
        delta = sp.Matrix([d1, d2])
        Vminus = (a.T * C * a)[0]
        Vplus = ((a + delta).T * C * (a + delta))[0]
        jump_rhs = 2 * (a.T * C * delta)[0] + (delta.T * C * delta)[0]
        self.assertEqual(sp.expand(Vplus - Vminus - jump_rhs), 0)

    def test_finite_selector_jump_is_exact_pair_reset_identity(self) -> None:
        Pm = sp.diag(1, 0)
        Pp = sp.diag(0, 1)
        dec = pair_jump_decomposition(Pm, Pp)
        self.assertEqual(dec.total, dec.reconstructed)
        self.assertFalse(matrix_is_zero(dec.total))

    def test_exact_abc_navier_stokes_closed_cycle_keeps_pressure_as_pure_gauge(self) -> None:
        # Genuine 3D ABC/Beltrami NS calibration.  On the x-torus cycle at
        # y=0,z=pi/2 the physical circulation is nonzero, while the exact pressure
        # gradient has zero circulation because it is an exact periodic form.
        x, y, z, t, nu = sp.symbols("x y z t nu", positive=True)
        amp = sp.exp(-nu * t)
        u = amp * sp.Matrix([
            sp.sin(z) + sp.cos(y),
            sp.sin(x) + sp.cos(z),
            sp.sin(y) + sp.cos(x),
        ])
        p = -sp.Rational(1, 2) * u.dot(u)
        ux_cycle = sp.simplify(u[0].subs({y: 0, z: sp.pi / 2}))
        circulation = sp.integrate(ux_cycle, (x, 0, 2 * sp.pi))
        pressure_circulation = sp.integrate(
            sp.diff(p, x).subs({y: 0, z: sp.pi / 2}),
            (x, 0, 2 * sp.pi),
        )
        self.assertEqual(sp.simplify(circulation - 4 * sp.pi * amp), 0)
        self.assertEqual(sp.simplify(sp.trigsimp(pressure_circulation)), 0)

    def test_exact_ns_odd_shear_selector_switch_is_signed_revaluation_not_positive_payment(self) -> None:
        # Exact odd-mode NS shear has X_pi=-X_0 pathwise.  A first-bad reset from
        # anchor 0 to anchor pi changes the selected variance by zero, although the
        # diagonal variance of the increment is strictly positive.  The mixed
        # covariance cancels it exactly.
        N, c = 48, 1.0
        v0 = kelvin_anchor_moments(N, c, 0.0)[2]
        vpi = kelvin_anchor_moments(N, c, math.pi)[2]
        cov = kelvin_anchor_covariance(N, c, 0.0, math.pi)
        vinc = kelvin_increment_variance(N, c, 0.0, math.pi)
        cov_old_increment = cov - v0
        self.assertGreater(vinc, 0.0)
        self.assertAlmostEqual(vpi - v0, 0.0, places=10)
        self.assertAlmostEqual(vinc + 2.0 * cov_old_increment, 0.0, places=9)
        self.assertAlmostEqual(vinc, 4.0 * v0, places=9)


if __name__ == "__main__":
    unittest.main()
