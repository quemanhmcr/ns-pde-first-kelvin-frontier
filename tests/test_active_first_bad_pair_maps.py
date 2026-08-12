from __future__ import annotations

import math
from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.active_pair import (  # noqa: E402
    ChainStage,
    boundary_residual,
    completed_boundary_residual,
    completed_pair_boundary_residual,
    factorized_pair_boundary_residual,
    factorized_pair_transport_residual,
    interval_block_projection,
    interval_boundary,
    interval_cut_projection,
    interval_orientation_reversal,
    interval_refinement_map,
    matrix_is_zero,
    nonzero_entries,
    pair_boundary_residual,
    pair_lift,
    pair_transport_residual,
    transported_stage_boundary_sum,
    transported_stage_pair_boundary_sum,
    transport_residual,
)
from pde_audit.exact_shear import (  # noqa: E402
    kelvin_anchor_covariance,
    kelvin_anchor_moments,
)


class ActiveFirstBadPairMapAudit(unittest.TestCase):
    def test_full_pair_boundary_commutator_is_exact_two_face_lift(self) -> None:
        B = interval_boundary(3)
        P1, P0 = interval_cut_projection(3, 2)
        C = boundary_residual(B, P1, P0, B)
        C2 = pair_boundary_residual(B, P1, P0, B)
        expected = factorized_pair_boundary_residual(C, P1)
        self.assertFalse(matrix_is_zero(C))
        self.assertEqual(sp.simplify(C2 - expected), sp.zeros(*C2.shape))

        # The one-current cut has one interface atom; the pair lift has that
        # interface on each ordered replica face, with opposite product sign.
        self.assertEqual(nonzero_entries(C), [(2, 2, sp.Integer(1))])
        self.assertFalse(matrix_is_zero(C2))

    def test_chain_functor_has_no_new_pair_only_boundary_residual(self) -> None:
        B = interval_boundary(4)
        F1, F0 = interval_orientation_reversal(4)
        C = boundary_residual(B, F1, F0, B)
        C2 = pair_boundary_residual(B, F1, F0, B)
        self.assertTrue(matrix_is_zero(C))
        self.assertTrue(matrix_is_zero(C2))

    def test_full_shell_product_partition_restores_parent_and_requires_cross_shell_blocks(self) -> None:
        # Two contiguous shells of the two-edge parent current z=e0+e1.
        # Individual shell restrictions have interface boundary currents, but the
        # physical parent is recovered only by summing *all* ordered shell pairs.
        z = sp.Matrix([1, 1])
        L1, _ = interval_block_projection(2, 0, 1)
        R1, _ = interval_block_projection(2, 1, 2)
        zL, zR = L1 * z, R1 * z
        self.assertEqual(zL + zR, z)

        full = (
            sp.kronecker_product(zL, zL)
            + sp.kronecker_product(zL, zR)
            + sp.kronecker_product(zR, zL)
            + sp.kronecker_product(zR, zR)
        )
        parent_pair = sp.kronecker_product(z, z)
        diagonal_only = sp.kronecker_product(zL, zL) + sp.kronecker_product(zR, zR)
        self.assertEqual(full, parent_pair)
        self.assertNotEqual(diagonal_only, parent_pair)
        self.assertEqual(parent_pair - diagonal_only, sp.Matrix([0, 1, 1, 0]))

    def test_refinement_is_literal_chain_map_and_full_pair_lift_keeps_cross_children(self) -> None:
        B2 = interval_boundary(2)
        B4, R1, R0 = interval_refinement_map(2, 2)
        C = boundary_residual(B4, R1, R0, B2)
        self.assertTrue(matrix_is_zero(C))
        self.assertTrue(matrix_is_zero(pair_boundary_residual(B4, R1, R0, B2)))

        R2 = pair_lift(R1)
        # Parent pair e0 x e0 expands to all four ordered fine-child pairs,
        # not only the two diagonal children.
        column = list(R2[:, 0])
        self.assertEqual(sum(1 for x in column if x != 0), 4)
        fine_n = R1.rows
        child_pairs = [(i // fine_n, i % fine_n) for i, x in enumerate(column) if x != 0]
        self.assertEqual(child_pairs, [(0, 0), (0, 1), (1, 0), (1, 1)])

    def test_completed_physical_excursion_residual_is_only_transported_interface_and_exit(self) -> None:
        B2 = interval_boundary(2)
        I1_2, I0_2 = sp.eye(2), sp.eye(3)
        Q1, Q0 = interval_cut_projection(2, 1)
        A1, A0 = interval_orientation_reversal(2)
        H1, H0 = interval_block_projection(2, 0, 1)
        B4, R1, R0 = interval_refinement_map(2, 2)
        J1, J0 = interval_orientation_reversal(4)
        E1, E0 = interval_cut_projection(4, 3)

        stages = [
            ChainStage("freeze", "fixed-current transport", B2, B2, I1_2, I0_2),
            ChainStage("quantile", "physical localization interface", B2, B2, Q1, Q0),
            ChainStage("anchor-orientation", "connection/holonomy geometry", B2, B2, A1, A0),
            ChainStage("shell", "physical shell interface; full product blocks retained separately", B2, B2, H1, H0),
            ChainStage("refinement", "full tensor-square refinement", B2, B4, R1, R0),
            ChainStage("resolve-reset", "observer covariance revaluation", B4, B4, J1, J0),
            ChainStage("physical-exit", "physical boundary sink", B4, B4, E1, E0),
        ]

        residuals = {stage.name: stage.boundary_residual() for stage in stages}
        self.assertTrue(matrix_is_zero(residuals["freeze"]))
        self.assertFalse(matrix_is_zero(residuals["quantile"]))
        self.assertTrue(matrix_is_zero(residuals["anchor-orientation"]))
        self.assertFalse(matrix_is_zero(residuals["shell"]))
        self.assertTrue(matrix_is_zero(residuals["refinement"]))
        self.assertTrue(matrix_is_zero(residuals["resolve-reset"]))
        self.assertFalse(matrix_is_zero(residuals["physical-exit"]))

        direct = completed_boundary_residual(stages)
        seam_sum = transported_stage_boundary_sum(stages)
        self.assertEqual(sp.simplify(direct - seam_sum), sp.zeros(*direct.shape))

        direct_pair = completed_pair_boundary_residual(stages)
        pair_seam_sum = transported_stage_pair_boundary_sum(stages)
        self.assertEqual(
            sp.simplify(direct_pair - pair_seam_sum),
            sp.zeros(*direct_pair.shape),
        )

        # Removing the three physical-boundary/localization stages leaves an
        # exactly functorial composition.  Thus anchor/refinement/reset do not
        # manufacture an unexplained boundary residual by themselves.
        functorial_stages = [stages[0], stages[2], stages[4], stages[5]]
        self.assertTrue(matrix_is_zero(completed_boundary_residual(functorial_stages)))

    def test_transport_commutator_has_no_new_pair_only_source(self) -> None:
        a, b, c, d, p, q, r, s = sp.symbols("a b c d p q r s")
        da, db, dc, dd = sp.symbols("da db dc dd")
        T = sp.Matrix([[a, b], [c, d]])
        P = sp.Matrix([[p, q], [r, s]])
        Pdot = sp.Matrix([[da, db], [dc, dd]])
        G = transport_residual(T, P, T, Pdot)
        G2 = pair_transport_residual(T, P, T, Pdot)
        expected = factorized_pair_transport_residual(G, P)
        self.assertEqual(sp.simplify(G2 - expected), sp.zeros(4, 4))

    def test_covariantly_transporting_active_frame_has_zero_pair_transport_residual(self) -> None:
        a = sp.symbols("a")
        T = sp.Matrix([[0, a], [-a, 0]])
        # A co-moving active frame obeys Pdot = P T - T P.
        P = sp.Matrix([[1, 0], [0, 0]])
        Pdot = P * T - T * P
        G = transport_residual(T, P, T, Pdot)
        self.assertTrue(matrix_is_zero(G))
        self.assertTrue(matrix_is_zero(pair_transport_residual(T, P, T, Pdot)))

    def test_exact_ns_odd_shear_active_mixture_requires_full_pair_covariance(self) -> None:
        # Exact smooth periodic NS shear: X_pi=-X_0 pathwise for the odd packet.
        # Therefore a physical active interpolation Z_h=h Z_0+(1-h) Z_pi has
        # X_h=(2h-1)X_0 and its full pair bank must vanish at h=1/2.
        N, c = 52, 0.85
        v0 = kelvin_anchor_moments(N, c, 0.0)[2]
        vpi = kelvin_anchor_moments(N, c, math.pi)[2]
        cov = kelvin_anchor_covariance(N, c, 0.0, math.pi)
        self.assertGreater(v0, 0.0)
        self.assertAlmostEqual(vpi, v0, places=10)
        self.assertAlmostEqual(cov, -v0, places=10)

        for h in [0.0, 0.2, 0.5, 0.8, 1.0]:
            full = h * h * v0 + (1.0 - h) ** 2 * vpi + 2.0 * h * (1.0 - h) * cov
            expected = (2.0 * h - 1.0) ** 2 * v0
            diagonal_projection = h * h * v0 + (1.0 - h) ** 2 * vpi
            self.assertAlmostEqual(full, expected, places=9)
            if h == 0.5:
                self.assertAlmostEqual(full, 0.0, places=9)
                self.assertGreater(diagonal_projection, 0.0)

    def test_active_projection_nonfunctoriality_cannot_be_declared_zero_without_incidence_data(self) -> None:
        # This is a counterexample to the *generic* claim that a projection onto
        # "active" cells automatically commutes with boundary.  It is not an
        # assertion that the still-unspecified CK projection equals this matrix.
        B = interval_boundary(2)
        P1, P0 = interval_cut_projection(2, 1)
        C = boundary_residual(B, P1, P0, B)
        C2 = pair_boundary_residual(B, P1, P0, B)
        self.assertFalse(matrix_is_zero(C))
        self.assertFalse(matrix_is_zero(C2))


if __name__ == "__main__":
    unittest.main()
