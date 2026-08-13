from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.random_selected_event_correlation import (
    adaptive_event_alignment_calibrations,
    event_dispersion_face_psd_quadratic_form,
    two_replica_congruence_faces,
    two_replica_congruence_residual,
    two_replica_mean_output_faces,
    two_replica_mean_output_residual,
    population_congruence_faces,
    population_congruence_residual,
    three_state_population_triple_face_calibration,
)


class RandomSelectedEventCorrelationAudit(unittest.TestCase):
    def test_two_replica_mean_output_has_map_state_correlation_face(self) -> None:
        C1=sp.Matrix([[1,0],[0,1]])
        C2=sp.Matrix([[2,1],[1,0]])
        x1=sp.Matrix([3,1]); x2=sp.Matrix([0,2])
        self.assertEqual(two_replica_mean_output_residual(C1,x1,C2,x2),sp.zeros(2,1))
        _,corr=two_replica_mean_output_faces(C1,x1,C2,x2)
        self.assertNotEqual(corr,sp.zeros(2,1))

    def test_two_replica_second_order_congruence_has_four_exact_faces(self) -> None:
        C1=sp.Matrix([[1,2],[0,1]])
        C2=sp.Matrix([[2,0],[1,1]])
        Q1=sp.Matrix([[3,1],[1,2]])
        Q2=sp.Matrix([[1,0],[0,4]])
        self.assertEqual(two_replica_congruence_residual(C1,Q1,C2,Q2),sp.zeros(2))

    def test_same_event_map_removes_all_event_randomness_faces(self) -> None:
        C=sp.Matrix([[1,2]])
        Q1=sp.diag(2,1); Q2=sp.diag(5,3)
        _,disp,left,right=two_replica_congruence_faces(C,Q1,C,Q2)
        self.assertEqual(disp,sp.zeros(1)); self.assertEqual(left,sp.zeros(1)); self.assertEqual(right,sp.zeros(1))

    def test_same_payload_random_event_keeps_positive_dispersion_only(self) -> None:
        C1=sp.Matrix([[1,0]]); C2=sp.Matrix([[0,1]])
        Q=sp.diag(2,3)
        _,disp,left,right=two_replica_congruence_faces(C1,Q,C2,Q)
        self.assertNotEqual(disp,sp.zeros(1))
        self.assertEqual(left,sp.zeros(1)); self.assertEqual(right,sp.zeros(1))

    def test_event_dispersion_quadratic_form_is_nonnegative_on_psd_payload(self) -> None:
        C1=sp.Matrix([[1,0],[0,1]]); C2=sp.Matrix([[0,1],[1,0]])
        Qbar=sp.diag(2,5); z=sp.Matrix([3,-1])
        value=event_dispersion_face_psd_quadratic_form(C1,Qbar,C2,z)
        self.assertGreaterEqual(int(value),0)

    def test_aligned_adaptive_event_has_three_positive_correction_units(self) -> None:
        c=adaptive_event_alignment_calibrations()
        self.assertTrue(c['all_payloads_psd'])
        self.assertEqual((c['positive_exact'],c['positive_naive'],c['positive_dispersion'],c['positive_corr_left'],c['positive_corr_right']),(4,1,1,1,1))

    def test_anti_aligned_adaptive_event_has_negative_signed_correlation_faces(self) -> None:
        c=adaptive_event_alignment_calibrations()
        self.assertEqual((c['negative_exact'],c['negative_naive'],c['negative_dispersion'],c['negative_corr_left'],c['negative_corr_right']),(0,1,1,-1,-1))

    def test_mean_event_map_times_mean_payload_is_not_a_universal_closure(self) -> None:
        c=adaptive_event_alignment_calibrations()
        self.assertNotEqual(c['positive_exact'],c['positive_naive'])
        self.assertNotEqual(c['negative_exact'],c['negative_naive'])

    def test_random_event_identity_applies_to_qv_gram_payload_too(self) -> None:
        C1=sp.Matrix([[1,0]]); C2=sp.Matrix([[0,1]])
        N1=sp.Matrix([[1,0],[0,0]])
        N2=sp.Matrix([[0,0],[0,2]])
        G1=sp.simplify(N1*N1.T); G2=sp.simplify(N2*N2.T)
        self.assertEqual(two_replica_congruence_residual(C1,G1,C2,G2),sp.zeros(1))

    def test_random_event_mean_correlation_vanishes_if_state_is_same(self) -> None:
        C1=sp.Matrix([[1,0]]); C2=sp.Matrix([[0,1]])
        x=sp.Matrix([2,3])
        _,corr=two_replica_mean_output_faces(C1,x,C2,x)
        self.assertEqual(corr,sp.zeros(1,1))

    def test_general_population_requires_centered_triple_face(self) -> None:
        Cs=[sp.Matrix([[0]]),sp.Matrix([[1]]),sp.Matrix([[2]])]
        Qs=[sp.Matrix([[1]]),sp.Matrix([[0]]),sp.Matrix([[1]])]
        self.assertEqual(population_congruence_residual(Cs,Qs),sp.zeros(1))
        faces=population_congruence_faces(Cs,Qs)
        self.assertEqual(faces[4],sp.Matrix([[sp.Rational(2,9)]]))

    def test_three_state_population_witness_blocks_four_face_promotion(self) -> None:
        c=three_state_population_triple_face_calibration()
        self.assertEqual(c['exact'],sp.Rational(4,3))
        self.assertEqual(c['four_face_sum'],sp.Rational(10,9))
        self.assertEqual(c['triple'],sp.Rational(2,9))
        self.assertEqual(c['exact']-c['four_face_sum'],c['triple'])


if __name__ == '__main__':
    unittest.main()
