from __future__ import annotations

from pathlib import Path
import sys
import unittest
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.two_clock_kelvin_quantile import (
    affine_reverse_covariance_residual,
    affine_reverse_probability_current,
    centered_gaussian_current_velocity,
    centered_gaussian_quantile,
    diagonal_reverse_covariance_component,
    flat_reverse_kelvin_current_velocity,
    identity_map_future_bridge_residual,
    identity_map_same_clock_residual,
    mahalanobis_shell_material_rate,
    moving_chamber_mass_rate_1d,
    one_dimensional_quantile_speed,
    outer_time_shifted_quantile,
    reverse_age_generator_of_backward_operator,
    reverse_age_state_map_diffusion,
    reverse_age_state_map_drift,
    reverse_probability_current_velocity,
    same_clock_backward_state_map_drift,
    simultaneous_identity_map_obstruction,
    weighted_level_quantile_speed,
    zero_rate_reverse_covariance_component,
)


class TwoClockKelvinQuantileAudit(unittest.TestCase):
    def test_reverse_age_generator_is_negative_backward_spatial_operator(self) -> None:
        x, nu, u = sp.symbols("x nu u")
        f = sp.Function("f")(x)
        Kminus = u * sp.diff(f, x) - nu * sp.diff(f, x, 2)
        Lrev = reverse_age_generator_of_backward_operator(Kminus)
        self.assertEqual(sp.expand(Lrev), -u * sp.diff(f, x) + nu * sp.diff(f, x, 2))

    def test_one_mode_future_heat_mean_becomes_causal_backward_kelvin_mean(self) -> None:
        a, tau, nu, k = sp.symbols("a tau nu k", positive=True)
        m = sp.exp(-nu * k**2 * tau) * sp.cos(k * a)
        residual = sp.diff(m, tau) - nu * sp.diff(m, a, 2)
        self.assertEqual(sp.simplify(residual), 0)

    def test_one_mode_future_covariance_clock_reversal_has_positive_source(self) -> None:
        a, tau, nu, k = sp.symbols("a tau nu k", positive=True)
        r = nu * k**2 * tau
        m = sp.exp(-r) * sp.cos(k * a)
        Q = sp.Rational(1, 2) * (1 + sp.exp(-4 * r) * sp.cos(2 * k * a))
        C = sp.simplify(Q - m**2)
        gamma = 2 * nu * sp.diff(m, a) ** 2
        self.assertEqual(sp.trigsimp(sp.diff(C, tau) - nu * sp.diff(C, a, 2) - gamma), 0)

    def test_reverse_age_state_map_pushes_diffusion_by_congruence(self) -> None:
        a, b, c, d = sp.symbols("a b c d")
        DPi = sp.Matrix([[a, b], [c, d]])
        K = sp.diag(2, 3)
        self.assertEqual(reverse_age_state_map_diffusion(DPi, K), sp.simplify(DPi * K * DPi.T))

    def test_reverse_age_state_map_drift_has_forward_bplus_and_clock_sign(self) -> None:
        pt1, pt2, b1, b2, h1, h2, nu = sp.symbols("pt1 pt2 b1 b2 h1 h2 nu")
        DPi = sp.eye(2)
        got = reverse_age_state_map_drift(
            sp.Matrix([pt1, pt2]), DPi, sp.Matrix([b1, b2]), sp.Matrix([h1, h2]), nu
        )
        self.assertEqual(got, sp.Matrix([pt1 - b1 - nu * h1, pt2 - b2 - nu * h2]))

    def test_same_clock_and_future_clock_state_maps_are_distinct(self) -> None:
        bp, bm, u = sp.symbols("bp bm u")
        zero = sp.Matrix([0])
        I = sp.eye(1)
        future = reverse_age_state_map_drift(zero, I, sp.Matrix([bp]), zero, sp.Integer(1))
        same = same_clock_backward_state_map_drift(zero, I, sp.Matrix([bm]), zero, sp.Integer(1))
        self.assertEqual(future, sp.Matrix([-bp]))
        self.assertEqual(same, sp.Matrix([bm]))
        self.assertEqual(identity_map_future_bridge_residual(sp.Matrix([bp]), sp.Matrix([u])), sp.Matrix([bp + u]))
        self.assertEqual(identity_map_same_clock_residual(sp.Matrix([bm]), sp.Matrix([u])), sp.Matrix([bm - u]))

    def test_demanding_both_identity_map_interpretations_forces_zero_current(self) -> None:
        j, d, u = sp.symbols("j d u")
        bp = j - d
        bm = j + d
        obstruction = simultaneous_identity_map_obstruction(sp.Matrix([bp]), sp.Matrix([bm]))
        self.assertEqual(obstruction, sp.Matrix([2*j]))
        # If the same physical drift also requires bp=-u and bm=u, then their
        # sum is zero and therefore j=0.
        self.assertEqual(sp.simplify((-u) + u), 0)

    def test_nonuniform_brownian_density_separates_the_two_interpretations(self) -> None:
        x, nu, v = sp.symbols("x nu v", positive=True)
        # Forward heat diffusion: b_+=0.  For N(0,v), b_-=2 nu x/v.
        bp = sp.Integer(0)
        bm = 2 * nu * x / v
        physical_u = sp.Integer(0)
        self.assertEqual(identity_map_future_bridge_residual(sp.Matrix([bp]), sp.Matrix([physical_u])), sp.zeros(1, 1))
        self.assertEqual(identity_map_same_clock_residual(sp.Matrix([bm]), sp.Matrix([physical_u])), sp.Matrix([2 * nu * x / v]))

    def test_clock_reversal_flips_probability_current_velocity(self) -> None:
        j1, j2 = sp.symbols("j1 j2")
        self.assertEqual(reverse_probability_current_velocity(sp.Matrix([j1, j2])), sp.Matrix([-j1, -j2]))

    def test_weighted_level_set_quantile_speed_is_coarea_average(self) -> None:
        w1, w2, r1, r2 = sp.symbols("w1 w2 r1 r2", nonzero=True)
        speed = weighted_level_quantile_speed([w1, w2], [r1, r2])
        self.assertEqual(sp.simplify(speed - (w1 * r1 + w2 * r2) / (w1 + w2)), 0)

    def test_one_dimensional_fixed_coordinate_quantile_moves_with_current_velocity(self) -> None:
        j = sp.symbols("j")
        self.assertEqual(one_dimensional_quantile_speed(j), j)

    def test_mass_conservation_selects_quantile_speed_equal_current_velocity(self) -> None:
        q, j = sp.symbols("q j", nonzero=True)
        rate = moving_chamber_mass_rate_1d(q, j, j)
        self.assertEqual(rate, 0)

    def test_zero_drift_gaussian_quantile_speed_equals_probability_current_velocity(self) -> None:
        z, var0, nu, tau = sp.symbols("z var0 nu tau", positive=True)
        a = centered_gaussian_quantile(z, var0, nu, tau)
        adot = sp.diff(a, tau)
        j = centered_gaussian_current_velocity(a, var0, nu, tau)
        self.assertEqual(sp.simplify(adot - j), 0)

    def test_reverse_kelvin_quantile_speed_contains_osmotic_face_not_only_drift(self) -> None:
        u, gx, nu = sp.symbols("u gx nu")
        jrev = flat_reverse_kelvin_current_velocity(u, gx, nu)
        self.assertEqual(jrev, -u - nu * gx)
        self.assertEqual(one_dimensional_quantile_speed(jrev), -u - nu * gx)

    def test_clock_reversal_reverses_quantile_speed_for_reversed_level_data(self) -> None:
        gs, gx, j = sp.symbols("gs gx j")
        forward = gs + j * gx
        reversed_speed = (-gs) + (-j) * gx
        self.assertEqual(sp.simplify(reversed_speed + forward), 0)


    def test_exact_affine_ns_reverse_covariance_obeys_gramian_ode(self) -> None:
        srate, tau, nu = sp.symbols("s tau nu", positive=True)
        A = sp.diag(srate, 0, -srate)
        Sigma = sp.diag(
            diagonal_reverse_covariance_component(srate, tau, nu),
            zero_rate_reverse_covariance_component(tau, nu),
            diagonal_reverse_covariance_component(-srate, tau, nu),
        )
        residual = affine_reverse_covariance_residual(A, Sigma, sp.diff(Sigma, tau), nu)
        self.assertEqual(sp.simplify(residual), sp.zeros(3))

    def test_mahalanobis_quantile_shell_is_pointwise_material_for_probability_current(self) -> None:
        a1, a2, nu = sp.symbols("a1 a2 nu")
        s1, s2 = sp.symbols("s1 s2", positive=True)
        x1, x2 = sp.symbols("x1 x2")
        A = sp.diag(a1, a2)
        Sigma = sp.diag(s1, s2)
        Sigma_dot = -A * Sigma - Sigma * A.T + 2 * nu * sp.eye(2)
        rate = mahalanobis_shell_material_rate(A, Sigma, Sigma_dot, sp.Matrix([x1, x2]), nu)
        self.assertEqual(sp.simplify(rate), 0)

    def test_affine_gaussian_current_has_drift_and_diffusive_faces(self) -> None:
        a1, a2, nu = sp.symbols("a1 a2 nu")
        s1, s2 = sp.symbols("s1 s2", positive=True)
        x1, x2 = sp.symbols("x1 x2")
        A = sp.diag(a1, a2)
        Sigma = sp.diag(s1, s2)
        j = affine_reverse_probability_current(A, Sigma, sp.Matrix([x1, x2]), nu)
        expected = sp.Matrix([-a1*x1 + nu*x1/s1, -a2*x2 + nu*x2/s2])
        self.assertEqual(sp.simplify(j - expected), sp.zeros(2, 1))

    def test_reverse_noise_covariance_is_integrated_reverse_support_geometry(self) -> None:
        srate, tau, nu, r = sp.symbols("s tau nu r", positive=True)
        # Along the +s material direction the reverse tangent factor is exp(-s r).
        gramian = sp.integrate(2 * nu * sp.exp(-2 * srate * r), (r, 0, tau))
        sigma = diagonal_reverse_covariance_component(srate, tau, nu)
        self.assertEqual(sp.simplify(gramian - sigma), 0)

    def test_parabolic_scale_is_leading_term_of_affine_reverse_quantile_covariance(self) -> None:
        srate, tau, nu = sp.symbols("s tau nu", positive=True)
        sig_plus = diagonal_reverse_covariance_component(srate, tau, nu)
        sig_minus = diagonal_reverse_covariance_component(-srate, tau, nu)
        self.assertEqual(sp.series(sig_plus, tau, 0, 3).removeO(), 2*nu*tau - 2*nu*srate*tau**2)
        self.assertEqual(sp.series(sig_minus, tau, 0, 3).removeO(), 2*nu*tau + 2*nu*srate*tau**2)

    def test_one_clock_ancestry_continuity_does_not_determine_outer_physical_cut_speed(self) -> None:
        z, variance, c, t, sigma = sp.symbols("z variance c t sigma", positive=True)
        # Both families are independent of the ancestry clock sigma, hence solve
        # partial_sigma q=0 with ancestry current j_sigma=0.  Their outer-time
        # quantiles can nevertheless move at different speeds.
        a1 = outer_time_shifted_quantile(z, variance, sp.Integer(0), t)
        a2 = outer_time_shifted_quantile(z, variance, c, t)
        self.assertEqual(sp.diff(a1, sigma), 0)
        self.assertEqual(sp.diff(a2, sigma), 0)
        self.assertEqual(sp.diff(a1, t), 0)
        self.assertEqual(sp.diff(a2, t), c)


if __name__ == "__main__":
    unittest.main()
