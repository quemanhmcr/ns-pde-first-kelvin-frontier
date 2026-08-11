from __future__ import annotations

import math
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.exact_shear import (  # noqa: E402
    circulation_traffic_integral,
    hodge_green_bank_initial,
    kelvin_terminal_moments,
)


class ExactShearCalibrationAudit(unittest.TestCase):
    def test_selected_kelvin_variance_is_positive_and_asymptotically_linear(self) -> None:
        c = 1.0
        Ns = [16, 32, 64, 128]
        vars_ = [kelvin_terminal_moments(N, c)[2] for N in Ns]
        self.assertTrue(all(v > 0 for v in vars_))
        normalized = [v / N for v, N in zip(vars_, Ns)]
        # Exact Gaussian sums converge to a nonzero limiting coefficient.
        self.assertGreater(min(normalized[-2:]), 1e-3)
        ratio = vars_[-1] / vars_[-2]
        self.assertGreater(ratio, 1.8)
        self.assertLess(ratio, 2.2)

    def test_drift_square_traffic_decays_on_kelvin_horizon(self) -> None:
        nu = 1.0
        c = 1.0
        Ns = [32, 64, 128]
        vals = [circulation_traffic_integral(N, nu, c) for N in Ns]
        scaled = [v * N * N for v, N in zip(vals, Ns)]
        self.assertTrue(all(v > 0 for v in vals))
        self.assertLess(max(scaled) / min(scaled), 1.15)

    def test_hodge_bank_is_inverse_linear_in_mode_count(self) -> None:
        Ns = [32, 64, 128]
        vals = [hodge_green_bank_initial(N) for N in Ns]
        scaled = [v * N for v, N in zip(vals, Ns)]
        self.assertTrue(all(v > 0 for v in vals))
        self.assertLess(max(scaled) / min(scaled), 1.05)

    def test_false_reservoir_separation_strengthens_with_frequency(self) -> None:
        nu = c = 1.0
        ratios = []
        for N in [16, 32, 64, 128]:
            var = kelvin_terminal_moments(N, c)[2]
            traffic = circulation_traffic_integral(N, nu, c)
            ratios.append(var / traffic)
        self.assertTrue(all(b > a for a, b in zip(ratios, ratios[1:])))
        self.assertGreater(ratios[-1] / ratios[-2], 6.0)


if __name__ == "__main__":
    unittest.main()
