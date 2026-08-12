from __future__ import annotations

from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.active_pair import (  # noqa: E402
    factorized_pair_transport_residual,
    pair_transport_residual,
    transport_residual,
)
from pde_audit.clock_cut_compatibility import (  # noqa: E402
    backward_kelvin_shear_residual,
    forward_brownian_shear_residual,
    forward_future_terminal_mean,
    moving_cut_operator_face,
    moving_halfline_boundary_speed_face,
    moving_halfline_mass_rate,
    moving_halfline_static_flux,
    normalized_variance_current_residual_1d,
    one_mode_future_variance,
    one_mode_gamma,
    one_mode_horizon_dynkin_residual,
    one_mode_ordinary_spacetime_defect,
    pair_moving_cut_mass_rate,
    two_clock_quadratic_rate,
)


class ClockCutCompatibilityAudit(unittest.TestCase):
    def test_one_mode_covariance_obeys_dynkin_not_ordinary_derham_law(self) -> None:
        a, tau, nu, k = sp.symbols("a tau nu k", positive=True)
        self.assertEqual(sp.trigsimp(one_mode_horizon_dynkin_residual(a, tau, nu, k)), 0)
        defect = sp.trigsimp(one_mode_ordinary_spacetime_defect(a, tau, nu, k))
        V = one_mode_future_variance(a, tau, nu, k)
        self.assertEqual(sp.trigsimp(defect + nu * sp.diff(V, a, 2)), 0)
        # At the symmetry anchor gamma=0, yet the ordinary spacetime coefficient
        # is still nonzero because diffusion remains.
        self.assertEqual(sp.simplify(one_mode_gamma(a, tau, nu, k).subs(a, 0)), 0)
        self.assertNotEqual(sp.simplify(defect.subs(a, 0)), 0)

    def test_normalized_covariance_has_exact_divergence_form_balance(self) -> None:
        x, s, nu, K, gamma = sp.symbols("x s nu K gamma")
        f = sp.Function("f")(x, s)
        phi = sp.Function("phi")(x)
        w = sp.Function("w")(x, s)
        V = sp.Function("V")(x, s)
        self.assertEqual(
            normalized_variance_current_residual_1d(f, phi, w, V, x, s, nu, K, gamma),
            0,
        )

    def test_forward_brownian_clock_is_not_the_backward_kelvin_martingale_clock(self) -> None:
        a, t, nu, k = sp.symbols("a t nu k", positive=True)
        u = sp.exp(-nu * k**2 * t) * sp.cos(k * a)
        self.assertEqual(backward_kelvin_shear_residual(a, t, nu, k), 0)
        self.assertEqual(
            sp.simplify(forward_brownian_shear_residual(a, t, nu, k) + 2 * nu * k**2 * u),
            0,
        )
        self.assertNotEqual(forward_brownian_shear_residual(a, t, nu, k), 0)

    def test_forward_future_terminal_conditioning_does_not_reproduce_current_ns_shear(self) -> None:
        a, s, Theta, nu, k = sp.symbols("a s Theta nu k", positive=True)
        current = sp.exp(-nu * k**2 * s) * sp.cos(k * a)
        future = forward_future_terminal_mean(a, s, Theta, nu, k)
        # Equality occurs only at the degenerate horizon Theta=s, not generally.
        self.assertEqual(sp.simplify((future - current).subs(Theta, s)), 0)
        self.assertNotEqual(sp.simplify(future - current), 0)

    def test_two_clock_selected_bank_chain_rule_has_clock_faces(self) -> None:
        c11, c12, c22 = sp.symbols("c11 c12 c22")
        ct11, ct12, ct22 = sp.symbols("ct11 ct12 ct22")
        ch11, ch12, ch22 = sp.symbols("ch11 ch12 ch22")
        a1, a2, da1, da2, tau_t = sp.symbols("a1 a2 da1 da2 tau_t")
        C = sp.Matrix([[c11, c12], [c12, c22]])
        Ct = sp.Matrix([[ct11, ct12], [ct12, ct22]])
        Ctau = sp.Matrix([[ch11, ch12], [ch12, ch22]])
        avec = sp.Matrix([a1, a2])
        adot = sp.Matrix([da1, da2])
        rate = two_clock_quadratic_rate(C, Ct, Ctau, avec, adot, tau_t)
        selector_only = 2 * (avec.T * C * adot)[0]
        clock_faces = (avec.T * (Ct + tau_t * Ctau) * avec)[0]
        self.assertEqual(sp.expand(rate - selector_only - clock_faces), 0)
        self.assertNotEqual(sp.expand(rate - selector_only), 0)

    def test_moving_halfline_cut_splits_static_flux_and_boundary_speed_face(self) -> None:
        q, v, adot = sp.symbols("q v adot")
        total = moving_halfline_mass_rate(q, v, adot)
        static = moving_halfline_static_flux(q, v)
        speed = moving_halfline_boundary_speed_face(q, adot)
        self.assertEqual(sp.simplify(total - static - speed), 0)
        self.assertEqual(moving_cut_operator_face(v, adot), adot - v)
        self.assertNotEqual(sp.simplify(total - static), 0)


    def test_operator_pair_transport_changes_when_moving_cut_qdot_is_retained(self) -> None:
        h, dh, c = sp.symbols("h dh c")
        Q = sp.diag(h, 1 - h)
        Qdot = sp.diag(dh, -dh)
        T = sp.Matrix([[0, c], [-c, 0]])
        G = transport_residual(T, Q, T, Qdot)
        G_static = transport_residual(T, Q, T, sp.zeros(2))
        self.assertEqual(sp.simplify(G - G_static - Qdot), sp.zeros(2))
        G2 = pair_transport_residual(T, Q, T, Qdot)
        expected = factorized_pair_transport_residual(G, Q)
        self.assertEqual(sp.simplify(G2 - expected), sp.zeros(4))
        G2_static = pair_transport_residual(T, Q, T, sp.zeros(2))
        self.assertNotEqual(sp.simplify(G2 - G2_static), sp.zeros(4))

    def test_pair_moving_cut_has_two_time_faces(self) -> None:
        p1, p2, v1, v2, adot = sp.symbols("p1 p2 v1 v2 adot")
        total = pair_moving_cut_mass_rate([p1, p2], [v1, v2], adot)
        static = -p1 * v1 - p2 * v2
        speed = adot * (p1 + p2)
        self.assertEqual(sp.expand(total - static - speed), 0)
        self.assertEqual(sp.diff(total, adot), p1 + p2)


if __name__ == "__main__":
    unittest.main()
