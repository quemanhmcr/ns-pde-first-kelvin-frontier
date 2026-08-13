from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.critical_sheet_merger_kelvin_event import merger_time
from src.pde_audit.critical_sheet_transport_nanson_event import (
    branch_nanson_shear_history,
    central_critical_vorticity,
    critical_branch_normal_speed,
    critical_sheet_path_y_qv_rate,
    critical_vorticity_gap_side_minus_central,
    finite_shear_nonaffinity_x,
    kelvin_anchor_y_qv_rate,
    literal_sheet_kelvin_ancestry_qv_defect,
    merger_history_area_comparison,
    merger_history_line_comparison,
    merger_moving_cut_flux_distance_product_limit,
    merger_nanson_history_gap,
    merger_residual_cusp_from_moving_cut,
    merger_residual_cusp_identification_residual,
    merger_support_vorticity_jump,
    merger_viscous_circulation_face,
    moving_cut_chain_rule_residual,
    nanson_history_gap,
    nanson_history_gap_rate,
    shear_nanson_area_frame,
    shear_nanson_line_frame,
    sheet_attached_affine_grid_slip,
    side_critical_vorticity,
    side_cut_total_variation_to_merger,
    transported_merger_packet_state,
)


class CriticalSheetTransportNansonEventTests(unittest.TestCase):
    def setUp(self) -> None:
        self.t = sp.symbols("t", real=True)
        self.nu = sp.symbols("nu", positive=True)
        self.s, self.ell, self.m = sp.symbols("s ell m", positive=True)

    def test_exact_critical_vorticity_gap_has_rigid_negative_square(self) -> None:
        r = sp.exp(3 * (self.nu * self.t - 1))
        alpha = sp.exp(-self.nu * self.t)
        direct = sp.simplify(
            side_critical_vorticity(self.t, self.nu)
            - central_critical_vorticity(self.t, self.nu)
        )
        expected = -alpha * (1-r)**2/(2*r)
        self.assertEqual(sp.simplify(direct-expected), 0)
        self.assertEqual(
            sp.simplify(critical_vorticity_gap_side_minus_central(self.t, self.nu)-expected),
            0,
        )

    def test_side_critical_sheet_is_not_material_in_y(self) -> None:
        vminus = critical_branch_normal_speed("minus", self.t, self.nu)
        vplus = critical_branch_normal_speed("plus", self.t, self.nu)
        self.assertEqual(sp.simplify(vminus + vplus), 0)
        self.assertNotEqual(sp.simplify(vminus), 0)
        self.assertEqual(critical_branch_normal_speed("central", self.t, self.nu), 0)
        # The exact shear has u_y=0, so side-sheet normal speed is pure reanchoring.

    def test_literal_critical_path_cannot_be_kelvin_anchor_by_quadratic_variation(self) -> None:
        self.assertEqual(kelvin_anchor_y_qv_rate(self.nu), 2*self.nu)
        self.assertEqual(critical_sheet_path_y_qv_rate(), 0)
        self.assertEqual(literal_sheet_kelvin_ancestry_qv_defect(self.nu), 2*self.nu)

    def test_branch_nanson_histories_satisfy_gamma_dot_equals_minus_q(self) -> None:
        gc = branch_nanson_shear_history("central", self.t, self.nu)
        gs = branch_nanson_shear_history("side", self.t, self.nu)
        self.assertEqual(sp.simplify(sp.diff(gc,self.t)+central_critical_vorticity(self.t,self.nu)), 0)
        self.assertEqual(sp.simplify(sp.diff(gs,self.t)+side_critical_vorticity(self.t,self.nu)), 0)
        self.assertEqual(gc.subs(self.t,0), 0)
        self.assertEqual(gs.subs(self.t,0), 0)

    def test_history_gap_rate_is_strict_premerger_square(self) -> None:
        gap = nanson_history_gap(self.t, self.nu)
        self.assertEqual(sp.simplify(sp.diff(gap,self.t)-nanson_history_gap_rate(self.t,self.nu)), 0)
        sample = nanson_history_gap_rate(sp.Rational(1,2)/self.nu, self.nu)
        self.assertLess(float(sample.subs(self.nu,1)), 0.0)

    def test_merger_nanson_history_gap_is_nonzero(self) -> None:
        dg = merger_nanson_history_gap(self.nu)
        self.assertNotEqual(sp.simplify(dg), 0)
        self.assertLess(float((self.nu*dg).subs(self.nu,1)), 0.0)

    def test_nanson_line_and_area_frames_obey_forward_connection(self) -> None:
        gamma = sp.Function("gamma")(self.t)
        L = shear_nanson_line_frame(gamma, self.s, self.ell, self.m)
        H = shear_nanson_area_frame(gamma, self.s, self.ell, self.m)
        A = sp.zeros(3)
        A[0,1] = sp.diff(gamma,self.t)
        self.assertEqual(sp.simplify(sp.diff(L,self.t)-A*L), sp.zeros(3))
        self.assertEqual(sp.simplify(sp.diff(H,self.t)+A.T*H), sp.zeros(3))

    def test_history_comparison_is_nontrivial_incompressible_shear(self) -> None:
        J = merger_history_line_comparison(self.nu)
        C = merger_history_area_comparison(self.nu)
        self.assertEqual(sp.simplify(sp.det(J)), 1)
        self.assertEqual(sp.simplify(C-sp.det(J)*J.inv().T), sp.zeros(3))
        self.assertNotEqual(sp.simplify(J-sp.eye(3)), sp.zeros(3))

    def test_transported_side_and_central_packets_share_readout_but_not_geometry(self) -> None:
        c = transported_merger_packet_state("central", self.s, self.ell, self.m, self.nu)
        s = transported_merger_packet_state("side", self.s, self.ell, self.m, self.nu)
        self.assertNotEqual(sp.simplify(c.line_frame-s.line_frame), sp.zeros(3))
        self.assertNotEqual(sp.simplify(c.area_frame-s.area_frame), sp.zeros(3))
        self.assertEqual(sp.simplify(c.circulation-s.circulation), sp.zeros(3,1))
        self.assertEqual(sp.simplify(c.target_vorticity-s.target_vorticity), sp.zeros(3,1))
        self.assertEqual(sp.simplify(c.physical_residual-s.physical_residual), sp.zeros(3,1))
        self.assertEqual(sp.simplify(c.codeforming_residual-s.codeforming_residual), sp.zeros(3,1))

    def test_two_side_histories_match_by_symmetry(self) -> None:
        m = transported_merger_packet_state("minus", self.s, self.ell, self.m, self.nu)
        p = transported_merger_packet_state("plus", self.s, self.ell, self.m, self.nu)
        self.assertEqual(sp.simplify(m.line_frame-p.line_frame), sp.zeros(3))
        self.assertEqual(sp.simplify(m.area_frame-p.area_frame), sp.zeros(3))

    def test_sheet_attached_grid_slip_splits_orthogonal_physical_faces(self) -> None:
        a, ry, v = sp.symbols("a ry v", real=True)
        slip = sheet_attached_affine_grid_slip(a,v,ry,self.t,self.nu)
        nonaff = finite_shear_nonaffinity_x(a,ry,self.t,self.nu)
        self.assertEqual(sp.simplify(slip[0]+nonaff), 0)
        self.assertEqual(sp.simplify(slip[1]-v), 0)
        self.assertEqual(slip[2], 0)

    def test_side_sheet_packet_cannot_be_material_even_at_anchor(self) -> None:
        a = sp.pi
        v = critical_branch_normal_speed("minus", self.t, self.nu)
        slip = sheet_attached_affine_grid_slip(a,v,0,self.t,self.nu)
        self.assertEqual(slip[0], 0)
        self.assertNotEqual(sp.simplify(slip[1]), 0)

    def test_moving_cut_circulation_law_is_exact_heat_reynolds_identity(self) -> None:
        a, v = sp.symbols("a v", real=True)
        self.assertEqual(
            moving_cut_chain_rule_residual(a,v,self.s,self.ell,self.t,self.nu),
            0,
        )

    def test_merger_support_vorticity_jump_is_positive_square(self) -> None:
        jump = merger_support_vorticity_jump(self.s)
        expected = sp.exp(-1)*(1-sp.cos(self.s))**2/2
        self.assertEqual(sp.simplify(jump-expected),0)
        self.assertGreater(float(jump.subs(self.s,sp.pi/2)),0.0)

    def test_viscous_circulation_face_stays_finite_at_merger(self) -> None:
        face = merger_viscous_circulation_face(self.s,self.ell,self.nu)
        expected = self.ell*self.nu*sp.exp(-1)*sp.sin(self.s)*(1-sp.cos(self.s))
        self.assertEqual(sp.simplify(face-expected),0)

    def test_singular_residual_cusp_is_exactly_moving_cut_flux(self) -> None:
        self.assertEqual(merger_residual_cusp_identification_residual(self.s,self.nu),0)
        expected = 3*self.nu*sp.exp(-1)*(1-sp.cos(self.s))**2/(2*self.s)
        self.assertEqual(sp.simplify(merger_residual_cusp_from_moving_cut(self.s,self.nu)-expected),0)

    def test_distance_weighted_moving_cut_flux_has_finite_limit(self) -> None:
        expected = 3*self.nu*self.ell*sp.exp(-1)*(1-sp.cos(self.s))**2/2
        self.assertEqual(
            sp.simplify(merger_moving_cut_flux_distance_product_limit(self.s,self.ell,self.nu)-expected),
            0,
        )

    def test_side_cut_has_finite_total_variation_despite_singular_speed(self) -> None:
        t0 = sp.Integer(0)
        variation = side_cut_total_variation_to_merger(t0,self.nu)
        self.assertEqual(variation, sp.acos(sp.exp(-3)))
        self.assertGreater(float(variation),0.0)
        self.assertLess(float(variation),float(sp.pi))


if __name__ == "__main__":
    unittest.main()
