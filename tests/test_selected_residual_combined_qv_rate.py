from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.selected_residual_combined_qv_rate import (
    combined_continuous_qv_rate_revaluation_faces,
    combined_continuous_qv_rate_revaluation_residual,
    one_mode_hidden_synthesis_qv_rate_calibration,
    post_selected_noise_response,
    pre_selected_noise_response,
    selected_continuous_qv_rate_from_noise,
    source_revaluation_vs_jump_square_calibrations,
)


class SelectedResidualCombinedQvRateAudit(unittest.TestCase):
    def setUp(self) -> None:
        I=sp.eye(3); Z=sp.zeros(3)
        self.A=sp.Matrix.vstack(sp.Matrix.hstack(I,Z),sp.Matrix.hstack(I,I))
        self.N=sp.Matrix(6,3,sp.symbols('n0:18'))
        self.nu=sp.symbols('nu')

    def test_pre_and_post_selected_noise_are_literal_readouts(self) -> None:
        self.assertEqual(pre_selected_noise_response(self.N,2,0),self.N[:3,:])
        self.assertEqual(post_selected_noise_response(self.N,self.A,2,1),sp.simplify(self.N[:3,:]+self.N[3:,:]))

    def test_continuous_qv_rate_revaluation_has_full_left_right_quadratic_faces(self) -> None:
        self.assertEqual(
            combined_continuous_qv_rate_revaluation_residual(self.N,self.A,2,0,2,1,self.nu),
            sp.zeros(3),
        )

    def test_qv_rate_quadratic_face_is_noise_response_dyad_not_state_jump_square(self) -> None:
        _,_,quad=combined_continuous_qv_rate_revaluation_faces(self.N,self.A,2,0,2,1,self.nu)
        self.assertTrue(any(x.has(*list(self.N)) for x in quad))

    def test_source_rate_revaluation_can_be_nonzero_when_state_jump_square_is_zero(self) -> None:
        c=source_revaluation_vs_jump_square_calibrations()
        self.assertTrue(c['rate_revaluation_nonzero_with_zero_state_jump_square'])

    def test_state_jump_square_can_be_nonzero_when_continuous_source_revaluation_is_zero(self) -> None:
        c=source_revaluation_vs_jump_square_calibrations()
        self.assertTrue(c['zero_rate_revaluation_with_nonzero_state_jump_square'])

    def test_exact_one_mode_ns_hidden_synthesis_cancels_post_event_continuous_noise(self) -> None:
        t,nu,k=sp.symbols('t nu k', positive=True)
        c=one_mode_hidden_synthesis_qv_rate_calibration(t,nu,k)
        self.assertEqual(c['opposite_noise_residual'],0)
        self.assertNotEqual(c['pre_noise'],sp.zeros(3))
        self.assertEqual(c['actual_post_noise'],sp.zeros(3))
        self.assertEqual(c['actual_post_qv_rate'],sp.zeros(3))

    def test_exact_one_mode_selector_only_rate_revaluation_misses_hidden_physical_event(self) -> None:
        t,nu,k=sp.symbols('t nu k', positive=True)
        c=one_mode_hidden_synthesis_qv_rate_calibration(t,nu,k)
        self.assertEqual(c['selector_only_post_qv_rate'],c['pre_qv_rate'])
        self.assertEqual(c['selector_only_rate_revaluation'],sp.zeros(3))
        self.assertNotEqual(c['actual_rate_revaluation'],sp.zeros(3))
        self.assertEqual(c['actual_rate_revaluation'],sp.simplify(-c['pre_qv_rate']))

    def test_exact_one_mode_qv_rate_revaluation_full_pair_faces_close(self) -> None:
        t,nu,k=sp.symbols('t nu k', positive=True)
        c=one_mode_hidden_synthesis_qv_rate_calibration(t,nu,k)
        self.assertEqual(c['rate_revaluation_residual'],sp.zeros(3))
        self.assertEqual(
            sp.simplify(c['rate_left']+c['rate_right']+c['rate_quadratic']),
            c['actual_rate_revaluation'],
        )

    def test_selected_qv_rate_is_positive_semidefinite_gram_for_positive_nu(self) -> None:
        q=sp.symbols('q', real=True)
        N=sp.zeros(3); N[2,1]=q
        G=selected_continuous_qv_rate_from_noise(N,sp.Integer(1))
        self.assertEqual(G[2,2],2*q**2)
        self.assertEqual(G[:2,:],sp.zeros(2,3))


if __name__ == '__main__':
    unittest.main()
