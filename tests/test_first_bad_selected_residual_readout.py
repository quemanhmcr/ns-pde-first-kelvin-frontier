from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.selected_principal_kelvin_lineage import germ_extraction_map
from src.pde_audit.first_bad_selected_residual_readout import (
    hidden_reset_faces_from_blocks,
    same_selector_factorization_residual,
    selected_after_physical_event,
    selected_physical_event_factorization_residual,
    selected_second_moment,
    selector_second_moment_jump_residual,
    selector_switch_factorization_on_subspace_residual,
    selector_switch_second_moment_counterexample,
    selector_switch_state_counterexample,
    selector_switch_unavoidable_new_block,
    selector_switch_universal_factorization_residual,
)


class FirstBadSelectedResidualReadoutAudit(unittest.TestCase):
    def test_genuine_selector_switch_has_no_universal_selected_to_selected_map(self) -> None:
        T=sp.Matrix(3,3,sp.symbols('t0:9'))
        residual=selector_switch_universal_factorization_residual(2,0,1,T)
        self.assertNotEqual(residual,sp.zeros(3,6))
        self.assertEqual(selector_switch_unavoidable_new_block(2,0,1,T),sp.eye(3))

    def test_same_selector_does_not_create_a_readout_obstruction(self) -> None:
        T=sp.Matrix(3,3,sp.symbols('s0:9'))
        self.assertEqual(same_selector_factorization_residual(2,0,T),sp.zeros(3,6))

    def test_two_library_states_can_share_old_selected_residual_and_differ_after_switch(self) -> None:
        c=selector_switch_state_counterexample()
        self.assertEqual(c['old_readout_1'],c['old_readout_2'])
        self.assertNotEqual(c['new_readout_1'],c['new_readout_2'])

    def test_selected_second_moment_reset_uses_full_pair_jump_exactly(self) -> None:
        Q=sp.Matrix(6,6,sp.symbols('q0:36'))
        self.assertEqual(selector_second_moment_jump_residual(Q,2,0,1),sp.zeros(3))

    def test_same_old_selected_second_moment_does_not_determine_new_selected_second_moment(self) -> None:
        c=selector_switch_second_moment_counterexample()
        self.assertEqual(c['old_Q_1'],c['old_Q_2'])
        self.assertNotEqual(c['new_Q_1'],c['new_Q_2'])
        for key in ('Q_full_1','Q_full_2'):
            self.assertTrue(all(ev >= 0 for ev in c[key].eigenvals()))

    def test_reset_faces_expose_offdiagonal_and_hidden_new_germ_blocks(self) -> None:
        Q00=sp.Matrix(3,3,sp.symbols('a0:9'))
        Q01=sp.Matrix(3,3,sp.symbols('b0:9'))
        Q10=sp.Matrix(3,3,sp.symbols('c0:9'))
        Q11=sp.Matrix(3,3,sp.symbols('d0:9'))
        Q=Q00.row_join(Q01).col_join(Q10.row_join(Q11))
        f=hidden_reset_faces_from_blocks(Q)
        self.assertEqual(f['left'],sp.simplify(Q10-Q00))
        self.assertEqual(f['right'],sp.simplify(Q01-Q00))
        self.assertEqual(f['quadratic'],sp.simplify(Q11-Q10-Q01+Q00))
        self.assertEqual(sp.simplify(f['left']+f['right']+f['quadratic']),sp.simplify(Q11-Q00))

    def test_factorization_can_hold_only_after_an_explicit_admissible_subspace_relation_is_supplied(self) -> None:
        E0=germ_extraction_map(2,0)
        E1=germ_extraction_map(2,1)
        T=sp.Matrix([[1,2,0],[0,1,0],[0,0,1]])
        S=sp.Matrix.vstack(sp.eye(3),T)
        self.assertEqual(selector_switch_factorization_on_subspace_residual(E0,E1,S,T),sp.zeros(3))

    def test_selector_after_full_physical_event_is_Epost_Afull(self) -> None:
        A=sp.Matrix(6,6,sp.symbols('a0:36'))
        E1=germ_extraction_map(2,1)
        self.assertEqual(selected_after_physical_event(A,2,1),sp.simplify(E1*A))

    def test_generic_full_event_plus_selector_switch_still_does_not_factor_through_old_selected_state(self) -> None:
        A=sp.eye(6)
        T=sp.Matrix(3,3,sp.symbols('u0:9'))
        residual=selected_physical_event_factorization_residual(A,2,0,2,1,T)
        self.assertEqual(residual,selector_switch_universal_factorization_residual(2,0,1,T))
        self.assertNotEqual(residual,sp.zeros(3,6))

    def test_germwise_physical_event_with_same_selector_factors_through_selected_state(self) -> None:
        B0=sp.Matrix([[2,0,0],[0,1,0],[0,0,3]])
        B1=sp.Matrix([[1,1,0],[0,1,0],[0,0,1]])
        A=sp.diag(B0,B1)
        self.assertEqual(selected_physical_event_factorization_residual(A,2,0,2,0,B0),sp.zeros(3,6))


if __name__ == '__main__':
    unittest.main()
