from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.selected_residual_hybrid_semimartingale import (
    hybrid_optional_qv,
    one_mode_selector_excursion_calibration,
    selected_continuous_noise,
    selected_continuous_qv_factorization_residual,
    selected_continuous_qv_rate,
    selector_closed_excursion,
    selector_jump_dyad_faces,
    selector_jump_dyad_residual,
    selector_jump_optional_qv,
    selector_readout_jump,
)


class SelectedResidualHybridSemimartingaleAudit(unittest.TestCase):
    def test_frozen_selector_continuous_noise_is_selected_block_of_library_noise(self) -> None:
        Q0=sp.Matrix(3,3,sp.symbols('a0:9'))
        Q1=sp.Matrix(3,3,sp.symbols('b0:9'))
        self.assertEqual(selected_continuous_noise([Q0,Q1],1),Q1)

    def test_frozen_selector_continuous_qv_is_brownian_selected_gram(self) -> None:
        Q0=sp.Matrix(3,3,sp.symbols('c0:9'))
        Q1=sp.Matrix(3,3,sp.symbols('d0:9'))
        nu=sp.symbols('nu')
        self.assertEqual(selected_continuous_qv_factorization_residual([Q0,Q1],0,nu),sp.zeros(3))
        self.assertEqual(selected_continuous_qv_rate([Q0,Q1],0,nu),sp.simplify(2*nu*Q0*Q0.T))

    def test_selector_jump_is_finite_readout_difference(self) -> None:
        X=sp.Matrix(sp.symbols('x0:6'))
        self.assertEqual(selector_readout_jump(X,2,0,1),sp.simplify(X[3:6,0]-X[0:3,0]))

    def test_selector_jump_optional_qv_is_jump_square_not_continuous_brownian_source(self) -> None:
        X=sp.Matrix([1,2,3,4,5,6])
        J=selector_readout_jump(X,2,0,1)
        self.assertEqual(selector_jump_optional_qv(X,2,0,1),J*J.T)

    def test_selector_jump_dyad_has_left_right_quadratic_faces_exactly(self) -> None:
        X=sp.Matrix(sp.symbols('y0:6'))
        self.assertEqual(selector_jump_dyad_residual(X,2,0,1),sp.zeros(3))
        left,right,quad=selector_jump_dyad_faces(X,2,0,1)
        J=selector_readout_jump(X,2,0,1)
        self.assertEqual(sp.simplify(quad-J*J.T),sp.zeros(3))
        self.assertEqual(sp.simplify(left.T-right),sp.zeros(3))

    def test_hybrid_optional_qv_adds_continuous_gram_and_finite_jump_squares(self) -> None:
        G=sp.diag(1,2,3)
        J1=sp.Matrix([1,0,2]); J2=sp.Matrix([0,3,0])
        self.assertEqual(hybrid_optional_qv([G],[J1,J2]),sp.simplify(G+J1*J1.T+J2*J2.T))

    def test_closed_selector_excursion_returns_to_same_state_but_has_positive_jump_qv(self) -> None:
        X=sp.Matrix([1,0,0,0,1,0])
        c=selector_closed_excursion(X,2,[0,1,0])
        self.assertEqual(c['state_change'],sp.zeros(3,1))
        self.assertEqual(c['jump_sum'],sp.zeros(3,1))
        self.assertGreater(int(sp.trace(c['jump_optional_qv'])),0)

    def test_exact_one_mode_ns_closed_selector_excursion_has_zero_net_state_and_positive_jump_qv(self) -> None:
        t,nu,k=sp.symbols('t nu k', positive=True)
        c=one_mode_selector_excursion_calibration(t,nu,k)
        self.assertEqual(c['chi1'],-c['chi0'])
        self.assertEqual(c['state_change'],sp.zeros(3,1))
        self.assertEqual(c['jump_sum'],sp.zeros(3,1))
        self.assertNotEqual(c['jump_optional_qv'],sp.zeros(3))
        self.assertTrue(sp.simplify(c['jump_optional_qv_trace']) != 0)

    def test_exact_one_mode_jump_squares_are_not_a_monotone_physical_bank(self) -> None:
        t,nu,k=sp.symbols('t nu k', positive=True)
        c=one_mode_selector_excursion_calibration(t,nu,k)
        self.assertEqual(c['jump_10'],-c['jump_01'])
        self.assertEqual(c['state_change'],sp.zeros(3,1))
        self.assertNotEqual(c['jump_optional_qv_trace'],0)


if __name__ == '__main__':
    unittest.main()
