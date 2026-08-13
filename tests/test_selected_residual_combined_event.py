from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.selected_residual_combined_event import (
    combined_jump_square,
    combined_post_readout_map,
    combined_second_moment_jump_faces,
    combined_second_moment_jump_residual,
    combined_selected_jump,
    combined_selected_jump_operator,
    one_mode_hidden_germ_synthesis_calibration,
    same_space_event_interaction_faces,
    same_space_event_interaction_residual,
    same_space_sequential_product_rule_residuals,
)
from src.pde_audit.selected_principal_kelvin_lineage import germ_extraction_map


class SelectedResidualCombinedEventAudit(unittest.TestCase):
    def setUp(self) -> None:
        I=sp.eye(3); Z=sp.zeros(3)
        self.A=sp.Matrix.vstack(
            sp.Matrix.hstack(I,Z),
            sp.Matrix.hstack(I,I),
        )

    def test_post_event_selected_readout_is_Eplus_A(self) -> None:
        self.assertEqual(combined_post_readout_map(self.A,2,1),germ_extraction_map(2,1)*self.A)

    def test_combined_jump_operator_is_post_event_readout_minus_pre_readout(self) -> None:
        D=combined_selected_jump_operator(self.A,2,0,2,1)
        self.assertEqual(sp.simplify(D-(germ_extraction_map(2,1)*self.A-germ_extraction_map(2,0))),sp.zeros(3,6))

    def test_simultaneous_event_has_exact_physical_selector_mixed_product_rule(self) -> None:
        self.assertEqual(same_space_event_interaction_residual(self.A,2,0,1),sp.zeros(3,6))
        r1,r2=same_space_sequential_product_rule_residuals(self.A,2,0,1)
        self.assertEqual(r1,sp.zeros(3,6))
        self.assertEqual(r2,sp.zeros(3,6))

    def test_mixed_physical_selector_face_is_generically_nonzero(self) -> None:
        _,_,mixed=same_space_event_interaction_faces(self.A,2,0,1)
        self.assertNotEqual(mixed,sp.zeros(3,6))

    def test_naive_physical_plus_old_selector_faces_drop_the_mixed_interaction(self) -> None:
        D=combined_selected_jump_operator(self.A,2,0,2,1)
        physical,selector,mixed=same_space_event_interaction_faces(self.A,2,0,1)
        self.assertEqual(sp.simplify(D-physical-selector),mixed)
        self.assertNotEqual(mixed,sp.zeros(3,6))

    def test_full_second_moment_jump_keeps_left_right_quadratic_pair_faces(self) -> None:
        Q=sp.Matrix(6,6,sp.symbols('q0:36'))
        self.assertEqual(combined_second_moment_jump_residual(Q,self.A,2,0,2,1),sp.zeros(3))

    def test_pathwise_jump_square_is_only_quadratic_second_moment_face(self) -> None:
        X=sp.Matrix(sp.symbols('x0:6'))
        Q=sp.simplify(X*X.T)
        _,_,quad=combined_second_moment_jump_faces(Q,self.A,2,0,2,1)
        self.assertEqual(sp.simplify(quad-combined_jump_square(X,self.A,2,0,2,1)),sp.zeros(3))

    def test_pure_selector_and_pure_physical_limits_remove_the_correct_faces(self) -> None:
        I6=sp.eye(6)
        p,s,m=same_space_event_interaction_faces(I6,2,0,1)
        self.assertEqual(p,sp.zeros(3,6)); self.assertEqual(m,sp.zeros(3,6))
        self.assertNotEqual(s,sp.zeros(3,6))
        p2,s2,m2=same_space_event_interaction_faces(self.A,2,1,1)
        self.assertNotEqual(p2,sp.zeros(3,6)); self.assertEqual(s2,sp.zeros(3,6)); self.assertEqual(m2,sp.zeros(3,6))

    def test_exact_one_mode_ns_payload_activates_mixed_event_face(self) -> None:
        t,nu,k=sp.symbols('t nu k', positive=True)
        c=one_mode_hidden_germ_synthesis_calibration(t,nu,k)
        self.assertEqual(c['chi1'],-c['chi0'])
        self.assertEqual(c['physical_old_jump'],sp.zeros(3,1))
        self.assertNotEqual(c['selector_old_jump'],sp.zeros(3,1))
        self.assertNotEqual(c['mixed_jump'],sp.zeros(3,1))
        self.assertEqual(sp.simplify(c['total_jump']-c['selector_old_jump']-c['mixed_jump']),sp.zeros(3,1))
        self.assertEqual(c['post_selected'],sp.zeros(3,1))
        self.assertEqual(c['total_jump'],-c['pre_selected'])

    def test_exact_one_mode_naive_selector_only_jump_is_wrong_after_hidden_physical_synthesis(self) -> None:
        t,nu,k=sp.symbols('t nu k', positive=True)
        c=one_mode_hidden_germ_synthesis_calibration(t,nu,k)
        self.assertNotEqual(c['total_jump'],c['selector_old_jump'])
        self.assertEqual(sp.simplify(c['total_jump']-c['selector_old_jump']),c['mixed_jump'])


if __name__ == '__main__':
    unittest.main()
