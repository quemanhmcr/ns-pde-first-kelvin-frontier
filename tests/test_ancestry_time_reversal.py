from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.ancestry_time_reversal import (
    backward_kelvin_matching_residual,
    backward_state_map_drift,
    backward_state_map_residuals,
    expanded_forward_drift,
    forward_drift_required_for_backward_kelvin,
    midpoint_current_residual,
    naive_w_equals_u_mismatch,
    probability_current_residual,
    repository_current_velocity,
    reversed_drift,
    weighted_diffusion_connection,
)


class AncestryTimeReversalAudit(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y, self.nu = sp.symbols("x y nu", positive=True)
        x, y = self.x, self.y
        self.coords = (x, y)
        self.K = sp.Matrix([[1 + x**2, x * y], [x * y, 2 + y**2]])
        self.phi = sp.exp(x + 2 * y)
        self.f = sp.exp(3 * x - y)
        self.w = sp.Matrix([x + y, x - 2 * y])

    def test_weighted_operator_forward_drift_contains_reference_geometry(self) -> None:
        c = weighted_diffusion_connection(self.K, self.phi, self.coords)
        bplus = expanded_forward_drift(self.w, self.K, self.phi, self.coords, self.nu)
        self.assertEqual(sp.simplify(bplus - self.w - self.nu * c), sp.zeros(2, 1))

    def test_repository_current_is_exact_fokker_planck_current_velocity(self) -> None:
        self.assertEqual(
            probability_current_residual(self.w, self.K, self.phi, self.f, self.coords, self.nu),
            sp.zeros(2, 1),
        )

    def test_repository_current_velocity_is_midpoint_of_forward_and_backward_drifts(self) -> None:
        self.assertEqual(
            midpoint_current_residual(self.w, self.K, self.phi, self.f, self.coords, self.nu),
            sp.zeros(2, 1),
        )

    def test_reversed_drift_has_exact_weighted_osmotic_formula(self) -> None:
        c = weighted_diffusion_connection(self.K, self.phi, self.coords)
        expected = sp.simplify(
            self.w - self.nu * c - 2 * self.nu * self.K * sp.Matrix([
                sp.diff(sp.log(self.f), self.x), sp.diff(sp.log(self.f), self.y)
            ])
        )
        actual = reversed_drift(self.w, self.K, self.phi, self.f, self.coords, self.nu)
        self.assertEqual(sp.simplify(actual - expected), sp.zeros(2, 1))

    def test_flat_uniform_sector_reduces_to_nelson_forward_backward_split(self) -> None:
        x, y, nu = self.x, self.y, self.nu
        K = sp.eye(2)
        phi = sp.Integer(1)
        f = sp.exp(2 * x - 3 * y)
        w = sp.Matrix([x, y])
        gradlogf = sp.Matrix([2, -3])
        bplus = expanded_forward_drift(w, K, phi, (x, y), nu)
        bminus = reversed_drift(w, K, phi, f, (x, y), nu)
        j = repository_current_velocity(w, K, f, (x, y), nu)
        self.assertEqual(bplus, w)
        self.assertEqual(sp.simplify(bminus - (w - 2 * nu * gradlogf)), sp.zeros(2, 1))
        self.assertEqual(sp.simplify(j - (w - nu * gradlogf)), sp.zeros(2, 1))

    def test_physical_backward_kelvin_matching_fixes_forward_ancestry_drift(self) -> None:
        u = sp.Matrix([self.y, -self.x])
        w_required = forward_drift_required_for_backward_kelvin(
            u, self.K, self.phi, self.f, self.coords, self.nu
        )
        self.assertNotEqual(w_required, u)
        self.assertEqual(
            backward_kelvin_matching_residual(u, self.K, self.phi, self.f, self.coords, self.nu),
            sp.zeros(2, 1),
        )

    def test_silently_setting_w_equal_u_creates_explicit_time_reversal_mismatch(self) -> None:
        u = sp.Matrix([self.y, -self.x])
        mismatch = naive_w_equals_u_mismatch(
            u, self.K, self.phi, self.f, self.coords, self.nu
        )
        c = weighted_diffusion_connection(self.K, self.phi, self.coords)
        gradlogf = sp.Matrix([3, -1])
        expected = sp.simplify(-self.nu * c - 2 * self.nu * self.K * gradlogf)
        self.assertEqual(sp.simplify(mismatch - expected), sp.zeros(2, 1))
        self.assertNotEqual(mismatch, sp.zeros(2, 1))


    def test_backward_state_map_requires_physical_zero_shape_diffusion(self) -> None:
        x, r, z, nu = sp.symbols("x r z nu")
        coords = (x, r, z)
        K = sp.diag(1, 0, 1)
        bminus = sp.Matrix([x, r, z])
        # Good projection ignores the hidden noisy z direction; physical relative
        # shape remains finite variation.
        Pi_good = sp.Matrix([x, r])
        target_drift = sp.Matrix([x, r])
        target_K = sp.diag(1, 0)
        drift_res, diff_res = backward_state_map_residuals(
            Pi_good, bminus, K, coords, nu, target_drift, target_K
        )
        self.assertEqual(drift_res, sp.zeros(2, 1))
        self.assertEqual(diff_res, sp.zeros(2))

        # If the same noisy hidden direction is mixed into physical shape, the
        # pushed shape q.v. is nonzero and cannot equal common-noise Kelvin shape.
        Pi_bad = sp.Matrix([x, r + z])
        pushed_K = sp.simplify(sp.Matrix([[sp.diff(Pi_bad[a], c) for c in coords] for a in range(2)]) * K * sp.Matrix([[sp.diff(Pi_bad[a], c) for c in coords] for a in range(2)]).T)
        self.assertEqual(pushed_K, sp.eye(2))
        self.assertNotEqual(pushed_K, target_K)

    def test_backward_state_map_has_negative_ito_hessian_correction(self) -> None:
        x, nu = sp.symbols("x nu")
        Pi = sp.Matrix([x**2])
        drift = backward_state_map_drift(Pi, sp.Matrix([0]), sp.Matrix([[1]]), (x,), nu)
        self.assertEqual(drift, sp.Matrix([-2 * nu]))

    def test_constant_density_and_flat_reference_remove_osmotic_mismatch(self) -> None:
        x, y, nu = self.x, self.y, self.nu
        u = sp.Matrix([self.y, -self.x])
        mismatch = naive_w_equals_u_mismatch(
            u, sp.eye(2), sp.Integer(1), sp.Integer(1), (x, y), nu
        )
        self.assertEqual(mismatch, sp.zeros(2, 1))


if __name__ == "__main__":
    unittest.main()
