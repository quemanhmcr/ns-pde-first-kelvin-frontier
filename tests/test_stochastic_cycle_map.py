from __future__ import annotations

from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.active_pair import matrix_is_zero  # noqa: E402
from pde_audit.stochastic_cycle_map import (  # noqa: E402
    ito_cycle_diffusions,
    ito_cycle_drift,
    ito_pair_drift,
    ito_pair_quadratic_source,
    pair_source_boundary,
    scalar_qv_density,
)


class StochasticCycleMapAudit(unittest.TestCase):
    def test_nonlinear_stochastic_cycle_map_keeps_ito_drift_and_diffusion_closed(self) -> None:
        B = sp.Matrix([
            [-1, 0, 1],
            [1, -1, 0],
            [0, 1, -1],
        ])
        K = sp.Matrix([1, 1, 1])
        a, beta, sigma = sp.symbols("a beta sigma")
        # Phi(a)=K(a+a^2), da=beta dt + sigma dW.
        J = K * (1 + 2 * a)
        hessians = [sp.Matrix([[2]]) for _ in range(3)]
        drift = ito_cycle_drift(J, sp.Matrix([beta]), hessians, sp.Matrix([[sigma**2]]))
        diffusions = ito_cycle_diffusions(J, sp.Matrix([[sigma]]))
        self.assertEqual(B * drift, sp.zeros(3, 1))
        self.assertEqual(B * diffusions[0], sp.zeros(3, 1))

    def test_stochastic_cycle_pair_source_is_explicit_qv_and_pair_closed(self) -> None:
        B = sp.Matrix([
            [-1, 0, 1],
            [1, -1, 0],
            [0, 1, -1],
        ])
        K = sp.Matrix([1, 1, 1])
        a, sigma = sp.symbols("a sigma", nonzero=True)
        psi = K * (1 + 2 * a) * sigma
        source = ito_pair_quadratic_source([psi])
        self.assertFalse(matrix_is_zero(source))
        self.assertTrue(matrix_is_zero(pair_source_boundary(B, source)))
        self.assertEqual(source, sp.kronecker_product(psi, psi))

    def test_finite_variation_observer_has_zero_extra_pair_qv(self) -> None:
        K = sp.Matrix([1, 1, 1])
        a = sp.symbols("a")
        zero_psi = K * 0 * a
        source = ito_pair_quadratic_source([zero_psi])
        self.assertTrue(matrix_is_zero(source))

    def test_ito_pair_product_rule_contains_only_drift_faces_plus_qv_source(self) -> None:
        z1, z2, b1, b2, s1, s2 = sp.symbols("z1 z2 b1 b2 s1 s2")
        Z = sp.Matrix([z1, z2])
        drift = sp.Matrix([b1, b2])
        psi = sp.Matrix([s1, s2])
        expected = (
            sp.kronecker_product(drift, Z)
            + sp.kronecker_product(Z, drift)
            + sp.kronecker_product(psi, psi)
        )
        self.assertEqual(ito_pair_drift(Z, drift, [psi]), expected)

    def test_exact_one_mode_kelvin_carre_du_champ_is_the_stochastic_qv_channel(self) -> None:
        a, tau, nu, k = sp.symbols("a tau nu k", positive=True)
        mean = sp.exp(-nu * k**2 * tau) * sp.cos(k * a)
        grad = sp.Matrix([sp.diff(mean, a)])
        covariance = sp.Matrix([[2 * nu]])
        qv = scalar_qv_density(grad, covariance)
        gamma = 2 * nu * sp.diff(mean, a) ** 2
        self.assertEqual(sp.simplify(qv - gamma), 0)

    def test_two_noise_directions_add_as_physical_pair_qv(self) -> None:
        p, q, r, s = sp.symbols("p q r s")
        psi1 = sp.Matrix([p, q])
        psi2 = sp.Matrix([r, s])
        source = ito_pair_quadratic_source([psi1, psi2])
        expected = sp.kronecker_product(psi1, psi1) + sp.kronecker_product(psi2, psi2)
        self.assertEqual(source, expected)


if __name__ == "__main__":
    unittest.main()
