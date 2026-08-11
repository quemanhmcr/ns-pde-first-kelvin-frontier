from __future__ import annotations

import math
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.pair_exit import (  # noqa: E402
    first_exit_density,
    pair_exit_rate,
    pair_survival_probability,
    survival_probability,
)
from pde_audit.pair_quantile import same_ancestor_halfspace_pair_mass  # noqa: E402


class PairShellExitAudit(unittest.TestCase):
    def test_full_two_shell_pair_partition_requires_cross_shell_blocks(self) -> None:
        # A+={x>0}, A-={x<0}; both one-particle shell masses are 1/2.
        qpp = same_ancestor_halfspace_pair_mass(1.0, 0.8)
        qmm = qpp
        qpm = 0.5 - qpp
        qmp = qpm
        full = qpp + qmm + qpm + qmp
        diagonal_only = qpp + qmm
        self.assertAlmostEqual(full, 1.0, places=14)
        self.assertGreater(qpm, 0.0)
        self.assertLess(diagonal_only, 1.0)
        self.assertAlmostEqual(1.0 - diagonal_only, qpm + qmp, places=14)

    def test_branching_moves_pair_mass_from_same_shell_to_cross_shell(self) -> None:
        tau2s = [0.0, 0.1, 0.5, 2.0, 10.0]
        same_shell = []
        cross_shell = []
        for tau2 in tau2s:
            qpp = same_ancestor_halfspace_pair_mass(1.0, tau2)
            same_shell.append(2.0 * qpp)
            cross_shell.append(1.0 - 2.0 * qpp)
        self.assertTrue(all(b < a for a, b in zip(same_shell, same_shell[1:])))
        self.assertTrue(all(b > a for a, b in zip(cross_shell, cross_shell[1:])))
        self.assertAlmostEqual(same_shell[0], 1.0, places=14)
        self.assertAlmostEqual(cross_shell[0], 0.0, places=14)

    def test_single_physical_exit_rate_matches_survival_derivative(self) -> None:
        x, nu, t = 1.2, 0.7, 0.9
        h = 1e-6
        fd = (survival_probability(x, nu, t + h) - survival_probability(x, nu, t - h)) / (2.0 * h)
        self.assertAlmostEqual(-fd, first_exit_density(x, nu, t), places=8)

    def test_pair_exit_is_sum_of_two_boundary_faces(self) -> None:
        x, nu, t = 1.1, 0.5, 0.8
        s = survival_probability(x, nu, t)
        f = first_exit_density(x, nu, t)
        self.assertAlmostEqual(pair_exit_rate(x, nu, t), s * f + f * s, places=14)

    def test_pair_survival_loss_rate_matches_exact_two_face_flux(self) -> None:
        x, nu, t = 0.9, 0.6, 1.4
        h = 1e-6
        fd = (
            pair_survival_probability(x, nu, t + h)
            - pair_survival_probability(x, nu, t - h)
        ) / (2.0 * h)
        self.assertLess(fd, 0.0)
        self.assertAlmostEqual(-fd, pair_exit_rate(x, nu, t), places=8)


if __name__ == "__main__":
    unittest.main()
