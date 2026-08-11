from __future__ import annotations

import math
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.pair_quantile import (  # noqa: E402
    halfspace_indicator_covariance,
    one_particle_halfspace_mass,
    pair_mass_derivative_tau2,
    replica_correlation,
    same_ancestor_halfspace_pair_mass,
)


class PairQuantileLeakageAudit(unittest.TestCase):
    def test_one_particle_quantile_mass_is_exactly_fixed(self) -> None:
        self.assertEqual(one_particle_halfspace_mass(), 0.5)

    def test_pair_quantile_mass_decreases_under_independent_future_branching(self) -> None:
        sigma2 = 1.7
        vals = [same_ancestor_halfspace_pair_mass(sigma2, tau2) for tau2 in [0.0, 0.1, 1.0, 10.0, 100.0]]
        self.assertAlmostEqual(vals[0], 0.5, places=14)
        self.assertTrue(all(b < a for a, b in zip(vals, vals[1:])))
        self.assertGreater(vals[-1], 0.25)
        self.assertLess(vals[-1] - 0.25, 0.01)

    def test_pair_covariance_is_arcsine_of_same_ancestor_correlation(self) -> None:
        sigma2, tau2 = 2.3, 0.8
        rho = replica_correlation(sigma2, tau2)
        expected = math.asin(rho) / (2.0 * math.pi)
        self.assertAlmostEqual(halfspace_indicator_covariance(sigma2, tau2), expected, places=14)

    def test_exact_pair_flux_derivative_matches_finite_difference(self) -> None:
        sigma2, tau2 = 1.3, 0.9
        h = 1e-6
        fd = (
            same_ancestor_halfspace_pair_mass(sigma2, tau2 + h)
            - same_ancestor_halfspace_pair_mass(sigma2, tau2 - h)
        ) / (2.0 * h)
        exact = pair_mass_derivative_tau2(sigma2, tau2)
        self.assertLess(exact, 0.0)
        self.assertAlmostEqual(fd, exact, places=8)

    def test_pair_leakage_integrates_to_exact_endpoint_difference(self) -> None:
        # Simpson integration is only an audit of the already exact derivative formula;
        # endpoint values come from the exact arcsine law.
        sigma2 = 1.0
        a, b = 0.2, 4.0
        n = 2000
        h = (b - a) / n
        total = pair_mass_derivative_tau2(sigma2, a) + pair_mass_derivative_tau2(sigma2, b)
        for i in range(1, n):
            x = a + i * h
            total += (4.0 if i % 2 else 2.0) * pair_mass_derivative_tau2(sigma2, x)
        integral = total * h / 3.0
        endpoint = same_ancestor_halfspace_pair_mass(sigma2, b) - same_ancestor_halfspace_pair_mass(sigma2, a)
        self.assertAlmostEqual(integral, endpoint, places=9)


if __name__ == "__main__":
    unittest.main()
