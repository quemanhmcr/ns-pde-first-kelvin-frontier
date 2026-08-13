from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.enstrophy_critical_branch_competition import (
    branch_value_gap,
    branch_value_gap_rate,
    crossing_gap_rate_face_difference_residual,
    selector_scalar_jump_at_tie,
    nondegenerate_value_crossing_geometry_calibration,
    three_mode_branch_crossing_calibration,
    transverse_crossing_orientation,
    two_branch_max_envelope_at_crossing,
)


class EnstrophyCriticalBranchCompetitionAudit(unittest.TestCase):
    def setUp(self) -> None:
        self.x,self.y,self.z,self.t=sp.symbols('x y z t', real=True)
        self.nu=sp.symbols('nu', positive=True)

    def test_gap_and_gap_rate_are_exact_branch_differences(self) -> None:
        e1,e2,r1,r2=sp.symbols('e1 e2 r1 r2')
        self.assertEqual(branch_value_gap(e1,e2),e1-e2)
        self.assertEqual(branch_value_gap_rate(r1,r2),r1-r2)

    def test_crossing_gap_rate_is_difference_of_three_face_branch_rates(self) -> None:
        s1,b1,c1,s2,b2,c2=sp.symbols('s1 b1 c1 s2 b2 c2')
        gapdot=(s1-b1+c1)-(s2-b2+c2)
        self.assertEqual(crossing_gap_rate_face_difference_residual(gapdot,s1,b1,c1,s2,b2,c2),0)

    def test_selector_scalar_value_has_zero_jump_at_exact_tie(self) -> None:
        E0=sp.Matrix([[1,0]]); E1=sp.Matrix([[0,1]])
        q=sp.symbols('q')
        self.assertEqual(selector_scalar_jump_at_tie(q,E0,E1),0)

    def test_transverse_crossing_orientation_uses_gap_rate_sign(self) -> None:
        self.assertEqual(transverse_crossing_orientation(sp.Integer(3)),1)
        self.assertEqual(transverse_crossing_orientation(sp.Integer(-2)),-1)
        with self.assertRaises(ValueError):
            transverse_crossing_orientation(sp.Integer(0))

    def test_max_envelope_is_continuous_but_can_have_derivative_switch(self) -> None:
        q,a,b=sp.symbols('q a b')
        c=two_branch_max_envelope_at_crossing(q,a,b)
        self.assertEqual(c['value_left'],c['value_right'])
        self.assertEqual(c['derivative_jump'],b-a)

    def test_value_crossing_and_full_hessian_degeneracy_are_independent_geometry_conditions(self) -> None:
        c=nondegenerate_value_crossing_geometry_calibration(self.t)
        self.assertEqual(c['gap'].subs(self.t,0),0)
        self.assertEqual(c['gap_rate'],2)
        self.assertNotEqual(c['det_hessian_1'],0)
        self.assertNotEqual(c['det_hessian_2'],0)
        self.assertLess(c['hessian_1'][0,0],0)
        self.assertLess(c['hessian_2'][0,0],0)

    def test_three_mode_periodic_shear_is_exact_navier_stokes(self) -> None:
        c=three_mode_branch_crossing_calibration(self.x,self.y,self.z,self.t,self.nu)
        self.assertEqual(c['ns_residual'],sp.zeros(3,1))

    def test_two_fixed_critical_sheets_cross_with_equal_values_and_negative_transverse_curvature(self) -> None:
        c=three_mode_branch_crossing_calibration(self.x,self.y,self.z,self.t,self.nu)
        self.assertEqual(c['critical_y_derivative_0'],0)
        self.assertEqual(c['critical_y_derivative_pi'],0)
        self.assertEqual(c['value_0'],c['value_pi'])
        self.assertEqual(c['value_0'],sp.Rational(9,2)*sp.exp(-2))
        self.assertEqual(c['hessian_yy_0'],-12*sp.exp(-2))
        self.assertEqual(c['hessian_yy_pi'],-60*sp.exp(-2))

    def test_winner_switch_is_transverse_while_both_critical_sheets_persist(self) -> None:
        c=three_mode_branch_crossing_calibration(self.x,self.y,self.z,self.t,self.nu)
        self.assertLess(c['gap_before'],0)
        self.assertGreater(c['gap_after'],0)
        self.assertEqual(c['gap_rate_at_crossing'],48*self.nu*sp.exp(-2))
        self.assertEqual(transverse_crossing_orientation(c['gap_rate_at_crossing']),1)
        self.assertNotEqual(c['hessian_yy_0'],0)
        self.assertNotEqual(c['hessian_yy_pi'],0)

    def test_crossing_is_pure_curvature_rate_competition_at_the_two_shear_maxima(self) -> None:
        c=three_mode_branch_crossing_calibration(self.x,self.y,self.z,self.t,self.nu)
        self.assertEqual(c['stretching_0'],0); self.assertEqual(c['stretching_pi'],0)
        self.assertEqual(c['kelvin_bulk_0'],0); self.assertEqual(c['kelvin_bulk_pi'],0)
        self.assertEqual(c['time_rate_0'],c['curvature_0'])
        self.assertEqual(c['time_rate_pi'],c['curvature_pi'])
        self.assertEqual(c['time_rate_0'],-12*self.nu*sp.exp(-2))
        self.assertEqual(c['time_rate_pi'],-60*self.nu*sp.exp(-2))
        self.assertEqual(c['gap_rate_face_residual'],0)

    def test_both_branch_values_decrease_while_the_winner_switches(self) -> None:
        c=three_mode_branch_crossing_calibration(self.x,self.y,self.z,self.t,self.nu)
        self.assertLess(c['time_rate_0'],0)
        self.assertLess(c['time_rate_pi'],0)
        self.assertGreater(c['gap_rate_at_crossing'],0)

    def test_selector_index_switch_at_tie_has_no_selected_scalar_jump_but_changes_derivative(self) -> None:
        c=three_mode_branch_crossing_calibration(self.x,self.y,self.z,self.t,self.nu)
        self.assertEqual(c['selector_scalar_jump_at_tie'],0)
        env=c['envelope']
        self.assertEqual(env['value_left'],env['value_right'])
        self.assertEqual(env['left_derivative'],c['time_rate_pi'])
        self.assertEqual(env['right_derivative'],c['time_rate_0'])
        self.assertEqual(env['derivative_jump'],48*self.nu*sp.exp(-2))


if __name__ == '__main__':
    unittest.main()
