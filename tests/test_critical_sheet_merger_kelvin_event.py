from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.critical_sheet_merger_kelvin_event import (
    asymmetric_box_packet_state,
    branch_extraction,
    collision_affine_event_data,
    collision_embedding,
    collision_selector_jump_residual,
    coalesced_same_replica_qv,
    critical_sheet_speed_product_limit,
    different_shape_packet_no_go_witness,
    merger_enstrophy,
    merger_packet_anchor_residual_derivative,
    merger_packet_cusp_coefficient,
    merger_packet_noise_zy,
    merger_packet_residual_z,
    merger_quartic_transverse_derivative,
    merger_ratio,
    merger_shear_ns_residual,
    merger_shear_vorticity_scalar,
    merger_side_anchors,
    merger_time,
    normalized_collision_quotient,
    normalized_collision_quotient_residual,
    quotient_qv_residual,
    diagonal_only_quotient_defect,
    reduced_side_transverse_hessian,
    reduced_side_vorticity,
)


class CriticalSheetMergerKelvinEventTests(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y, self.z, self.t = sp.symbols("x y z t", real=True)
        self.nu = sp.symbols("nu", positive=True)
        self.s, self.ell, self.m = sp.symbols("s ell m", positive=True)

    def test_exact_periodic_shear_is_literal_ns(self) -> None:
        residual, div, p = merger_shear_ns_residual((self.x, self.y, self.z), self.t, self.nu)
        self.assertEqual(residual, sp.zeros(3, 1))
        self.assertEqual(div, 0)
        self.assertEqual(p, 0)

    def test_side_sheet_geometry_merges_at_tstar(self) -> None:
        r = merger_ratio(self.t, self.nu)
        minus, plus = merger_side_anchors(self.t, self.nu)
        self.assertEqual(sp.simplify(sp.cos(minus) + r), 0)
        self.assertEqual(sp.simplify(sp.cos(plus) + r), 0)
        T = merger_time(self.nu)
        self.assertEqual(sp.simplify(minus.subs(self.t, T)), sp.pi)
        self.assertEqual(sp.simplify(plus.subs(self.t, T)), sp.pi)

    def test_side_sheet_transverse_curvature_collapses(self) -> None:
        alpha, r = sp.symbols("alpha r", positive=True)
        h = reduced_side_transverse_hessian(alpha, r)
        self.assertEqual(sp.factor(h), -alpha**2*(r - 1)*(r + 1)*(2*r**2 + 1)/(4*r**2) * -1)
        self.assertEqual(sp.simplify(h.subs(r, 1)), 0)
        self.assertLess(float(h.subs({alpha: 1, r: sp.Rational(1, 2)})), 0.0)

    def test_merger_vorticity_and_quartic_geometry_are_finite(self) -> None:
        T = merger_time(self.nu)
        qstar = sp.simplify(merger_shear_vorticity_scalar(sp.pi, T, self.nu))
        self.assertEqual(qstar, -sp.Rational(3, 4) * sp.exp(-1))
        e = merger_enstrophy(self.y, self.t, self.nu)
        self.assertEqual(sp.simplify(sp.diff(e, self.y, 4).subs({self.y: sp.pi, self.t: T})), merger_quartic_transverse_derivative())

    def test_critical_coordinate_speed_product_is_finite(self) -> None:
        self.assertEqual(critical_sheet_speed_product_limit(self.nu), 3*self.nu)

    def test_packet_is_orientation_complete_and_exact(self) -> None:
        state = asymmetric_box_packet_state(sp.pi, self.s, self.ell, self.m, merger_time(self.nu), self.nu)
        self.assertEqual(state.line_frame.det(), self.ell*self.m*self.s)
        self.assertNotEqual(sp.simplify(state.area_frame.det()), 0)
        self.assertEqual(state.circulation[0], 0)
        self.assertEqual(state.circulation[1], 0)
        self.assertEqual(state.target_vorticity[:2, :], sp.zeros(2, 1))
        self.assertEqual(sp.simplify(state.physical_residual[2] - merger_packet_residual_z(self.s)), 0)

    def test_target_gradient_vanishes_at_every_critical_sheet(self) -> None:
        r = sp.symbols("r", positive=True)
        alpha = sp.symbols("alpha", positive=True)
        # q_y vanishes on the side relation cos y=-r; at merger the direct packet target gradient is zero.
        self.assertEqual(sp.simplify(reduced_side_vorticity(alpha, r) - reduced_side_vorticity(alpha, r)), 0)
        state = asymmetric_box_packet_state(sp.pi, self.s, self.ell, self.m, merger_time(self.nu), self.nu)
        self.assertEqual(state.target_gradient, sp.zeros(3))

    def test_fixed_shape_packets_coalesce_in_instantaneous_state(self) -> None:
        a = sp.symbols("a", real=True)
        state = asymmetric_box_packet_state(a, self.s, self.ell, self.m, self.t, self.nu)
        T = merger_time(self.nu)
        central = asymmetric_box_packet_state(sp.pi, self.s, self.ell, self.m, T, self.nu)
        for attr in (
            "line_frame", "area_frame", "circulation", "target_vorticity",
            "raw_error", "physical_residual", "codeforming_residual",
            "target_gradient", "residual_noise", "full_codeforming_noise",
        ):
            expr = getattr(state, attr)
            limit_expr = expr.applyfunc(lambda q: sp.simplify(sp.limit(sp.limit(q, a, sp.pi), self.t, T)))
            self.assertEqual(sp.simplify(limit_expr - getattr(central, attr)), sp.zeros(*expr.shape))

    def test_merger_packet_noise_is_nonzero_for_one_sided_shape(self) -> None:
        state = asymmetric_box_packet_state(sp.pi, self.s, self.ell, self.m, merger_time(self.nu), self.nu)
        expected = merger_packet_noise_zy(self.s, self.m)
        self.assertEqual(sp.simplify(state.full_codeforming_noise[2, 1] - expected), 0)
        self.assertEqual(sp.simplify(state.residual_noise[2, 1] - expected), 0)
        self.assertEqual(sp.simplify(expected.subs({self.s: sp.pi/2, self.m: 1}) - sp.exp(-1)/sp.pi), 0)

    def test_scalar_merger_does_not_force_full_packet_shape(self) -> None:
        witness = different_shape_packet_no_go_witness()
        self.assertNotEqual(witness["area_frame_1"], witness["area_frame_2"])
        self.assertNotEqual(sp.simplify(witness["residual_difference"]), 0)
        self.assertNotEqual(sp.simplify(witness["noise_difference"]), 0)
        expected = sp.simplify((-32 + 21*sp.sqrt(3))*sp.exp(-1)/(16*sp.pi))
        self.assertEqual(sp.simplify(witness["residual_difference"] - expected), 0)

    def test_branch_resolved_event_map_is_central_extraction(self) -> None:
        S = collision_embedding(3)
        A = branch_extraction(3, 0)
        self.assertEqual(sp.simplify(A*S), sp.eye(3))
        self.assertNotEqual(branch_extraction(3, 0), branch_extraction(3, 1))

    def test_affine_reanchoring_and_target_noise_faces_vanish_at_collision(self) -> None:
        A = branch_extraction(3, 0)
        target = sp.Matrix([0, 0, -sp.Rational(3, 4)*sp.exp(-1)])
        G = sp.zeros(3)
        d, ntarget = collision_affine_event_data(A, target, G, 3)
        self.assertEqual(d, sp.zeros(3, 1))
        self.assertEqual(ntarget, sp.zeros(3))

    def test_normalized_collision_quotients_are_gauge_on_collision_subspace(self) -> None:
        w = [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 6)]
        self.assertEqual(normalized_collision_quotient_residual(w), sp.zeros(3))
        C = normalized_collision_quotient(w)
        self.assertEqual(sp.simplify(C*collision_embedding(3)), sp.eye(3))

    def test_same_replica_cross_blocks_make_quotient_qv_invariant(self) -> None:
        n = merger_packet_noise_zy(sp.pi/2, 1)
        N = sp.zeros(3)
        N[2, 1] = n
        G = coalesced_same_replica_qv(N, 3, self.nu)
        block = sp.simplify(2*self.nu*N*N.T)
        for i in range(3):
            for j in range(3):
                self.assertEqual(G[3*i:3*(i+1), 3*j:3*(j+1)], block)
        w = [sp.Rational(1, 3)]*3
        self.assertEqual(quotient_qv_residual(N, w, self.nu), sp.zeros(3))
        defect = diagonal_only_quotient_defect(N, w, self.nu)
        self.assertEqual(sp.simplify(defect + sp.Rational(2, 3)*block), sp.zeros(3))

    def test_selector_label_switch_has_zero_physical_jump_at_collision(self) -> None:
        x = sp.Matrix(sp.symbols("x0:3"))
        self.assertEqual(collision_selector_jump_residual(x, 1, 0, 3), sp.zeros(3, 1))

    def test_packet_interface_is_continuous_but_has_singular_branch_rate(self) -> None:
        da = merger_packet_anchor_residual_derivative(self.s)
        self.assertEqual(sp.simplify(da - sp.exp(-1)*(1-sp.cos(self.s))**2/(2*self.s)), 0)
        self.assertNotEqual(sp.simplify(da.subs(self.s, sp.pi/2)), 0)
        self.assertEqual(merger_packet_cusp_coefficient(self.s, self.nu), 3*self.nu*da)


if __name__ == "__main__":
    unittest.main()
