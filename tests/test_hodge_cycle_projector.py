from __future__ import annotations

from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.cycle_selector import two_cycle_library  # noqa: E402
from pde_audit.hodge_projector import (  # noqa: E402
    covariant_projector_derivative,
    pair_projector_derivative,
    projector_idempotency_residual,
    projector_motion_blocks,
    projector_tangent_residual,
    weighted_cycle_projector,
)


class HodgeCycleProjectorAudit(unittest.TestCase):
    def test_weighted_hodge_projector_is_idempotent_cycle_valued_and_metric_selfadjoint(self) -> None:
        B, K = two_cycle_library()
        W = sp.diag(1, 2, 3, 5)
        H = weighted_cycle_projector(K, W)
        self.assertEqual(projector_idempotency_residual(H), sp.zeros(*H.shape))
        self.assertEqual(sp.simplify(B * H), sp.zeros(B.rows, H.cols))
        self.assertEqual(sp.simplify(H * K - K), sp.zeros(*K.shape))
        self.assertEqual(sp.simplify(H.T * W - W * H), sp.zeros(*H.shape))

    @staticmethod
    def rational_rank_one_projector() -> tuple[sp.Symbol, sp.Matrix]:
        r = sp.symbols("r", real=True)
        denom = 1 + r**2
        P = sp.Matrix([[1, r], [r, r**2]]) / denom
        return r, P

    def test_differentiated_projector_has_no_internal_active_or_inactive_source(self) -> None:
        r, P = self.rational_rank_one_projector()
        Pdot = sp.simplify(sp.diff(P, r))
        self.assertEqual(projector_idempotency_residual(P), sp.zeros(2))
        self.assertEqual(projector_tangent_residual(P, Pdot), sp.zeros(2))

        blocks = projector_motion_blocks(P, Pdot)
        self.assertEqual(blocks.active_internal, sp.zeros(2))
        self.assertEqual(blocks.inactive_internal, sp.zeros(2))
        self.assertEqual(sp.simplify(Pdot - blocks.transfer_sum), sp.zeros(2))
        self.assertNotEqual(Pdot, sp.zeros(2))

    def test_covariantly_comoving_projector_has_zero_transport_residual(self) -> None:
        r, P = self.rational_rank_one_projector()
        Pdot = sp.simplify(sp.diff(P, r))
        # Any projector tangent G satisfies G=[[G,P],P].  Therefore choosing
        # T=-[G,P] gives the exact co-moving connection Pdot+[T,P]=0.
        A = sp.simplify(Pdot * P - P * Pdot)
        G = covariant_projector_derivative(P, -A, Pdot)
        self.assertEqual(sp.simplify(G), sp.zeros(2))

    def test_pair_projector_motion_has_only_one_replica_transfer_factors(self) -> None:
        r, P = self.rational_rank_one_projector()
        G = sp.simplify(sp.diff(P, r))
        pair = pair_projector_derivative(P, G)
        expected = sp.kronecker_product(G, P) + sp.kronecker_product(P, G)
        self.assertEqual(sp.simplify(pair - expected), sp.zeros(4))

        # There is no active-active pair-internal derivative inherited from a
        # one-current internal term, because P G P=0 exactly.
        PP = sp.kronecker_product(P, P)
        self.assertEqual(sp.simplify(PP * pair * PP), sp.zeros(4))

    def test_time_dependent_weighted_cycle_projector_motion_is_tangent_and_boundary_closed(self) -> None:
        s = sp.symbols("s", positive=True)
        B = sp.Matrix([[-1, -1], [1, 1]])
        K = sp.Matrix([[1], [-1]])
        W = sp.diag(1 + s, 2)
        H = weighted_cycle_projector(K, W)
        Hdot = sp.simplify(sp.diff(H, s))
        self.assertEqual(sp.simplify(B * H), sp.zeros(2, 2))
        self.assertEqual(projector_tangent_residual(H, Hdot), sp.zeros(2))
        blocks = projector_motion_blocks(H, Hdot)
        self.assertEqual(blocks.active_internal, sp.zeros(2))
        self.assertEqual(blocks.inactive_internal, sp.zeros(2))


if __name__ == "__main__":
    unittest.main()
