from __future__ import annotations

from fractions import Fraction
import math
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.exact_shear import (  # noqa: E402
    kelvin_anchor_covariance,
    kelvin_anchor_moments,
    kelvin_increment_variance,
)
from pde_audit.pair_worldsheet import (  # noqa: E402
    internal_rung_coefficients,
    make_stage,
    refinement_cross_defect,
    refinement_pair_coefficients,
    worldsheet_boundary,
)


class PairLocalizationWorldsheetAudit(unittest.TestCase):
    def test_each_elementary_stage_has_boundary_squared_zero(self) -> None:
        labels = ["freeze", "quantile", "anchor", "shell", "refinement", "resolve", "exit"]
        for k, label in enumerate(labels):
            self.assertTrue(make_stage(label, k).boundary_squared().is_zero(), label)

    def test_complete_excursion_cancels_every_internal_localization_rung(self) -> None:
        labels = ["freeze", "quantile", "anchor", "shell", "refinement", "resolve", "exit"]
        stages = [make_stage(label, k) for k, label in enumerate(labels)]
        boundary = worldsheet_boundary(stages)
        internal = internal_rung_coefficients(boundary, len(stages))
        self.assertTrue(all(value == 0 for value in internal.values()))
        self.assertEqual(boundary.coefficient("R0"), -1)
        self.assertEqual(boundary.coefficient(f"R{len(stages)}"), 1)

    def test_full_pair_refinement_requires_cross_child_terms(self) -> None:
        weights = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
        full = refinement_pair_coefficients(weights)
        defect = refinement_cross_defect(weights)
        self.assertEqual(sum(full.values()), Fraction(1))
        self.assertTrue(defect)
        self.assertTrue(all(i != j for i, j in defect))
        self.assertEqual(defect[(0, 1)], Fraction(1, 6))
        self.assertEqual(defect[(1, 0)], Fraction(1, 6))

    def test_exact_ns_odd_shear_refinement_cross_covariance_cancels_diagonals(self) -> None:
        # For odd modes, X_pi=-X_0 pathwise.  Thus the parent Z_0+Z_pi has zero
        # future variance although both child diagonal variances are positive.
        N, c = 48, 1.0
        v0 = kelvin_anchor_moments(N, c, 0.0)[2]
        vpi = kelvin_anchor_moments(N, c, math.pi)[2]
        cov = kelvin_anchor_covariance(N, c, 0.0, math.pi)
        self.assertGreater(v0, 0.0)
        self.assertAlmostEqual(vpi, v0, places=10)
        self.assertAlmostEqual(cov, -v0, places=10)
        diagonal_only = v0 + vpi
        full_parent = v0 + vpi + 2.0 * cov
        self.assertGreater(diagonal_only, 0.0)
        self.assertAlmostEqual(full_parent, 0.0, places=9)

    def test_exact_ns_reset_revaluation_is_covariance_identity(self) -> None:
        N, c = 40, 0.7
        a, b = 0.23, 1.17
        va = kelvin_anchor_moments(N, c, a)[2]
        vb = kelvin_anchor_moments(N, c, b)[2]
        cab = kelvin_anchor_covariance(N, c, a, b)
        vinc = kelvin_increment_variance(N, c, a, b)
        cov_a_inc = cab - va
        self.assertAlmostEqual(vb - va, vinc + 2.0 * cov_a_inc, places=10)

    def test_closed_observer_loop_has_zero_net_bank_change_but_positive_diagonal_cost(self) -> None:
        N, c = 36, 0.9
        anchors = [0.11, 0.77, 1.43, 0.11]
        vars_ = [kelvin_anchor_moments(N, c, a)[2] for a in anchors]
        net = sum(vars_[i + 1] - vars_[i] for i in range(len(anchors) - 1))
        diagonal_cost = sum(
            kelvin_increment_variance(N, c, anchors[i], anchors[i + 1])
            for i in range(len(anchors) - 1)
        )
        self.assertAlmostEqual(net, 0.0, places=11)
        self.assertGreater(diagonal_cost, 0.0)


if __name__ == "__main__":
    unittest.main()
