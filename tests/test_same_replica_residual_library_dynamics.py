from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.same_replica_residual_library_dynamics import (
    fixed_noise_centered_covariance_rate,
    independent_vs_common_qv_difference,
    library_qv_block_residual,
    linear_event_qv_functor_residual,
    one_mode_two_packet_common_noise_calibration,
    qv_image_rank_bound,
    same_replica_library_qv,
    same_replica_qv_block,
    selected_qv_readout_residual,
    stacked_common_noise,
    stacked_martingale_mean_rate,
)


class SameReplicaResidualLibraryDynamicsAudit(unittest.TestCase):
    def test_stacked_library_noise_has_one_common_three_direction_driver(self) -> None:
        Q1=sp.Matrix(3,3,sp.symbols('a0:9'))
        Q2=sp.Matrix(3,3,sp.symbols('b0:9'))
        S=stacked_common_noise([Q1,Q2])
        self.assertEqual(S.shape,(6,3))
        self.assertEqual(S[:3,:],Q1)
        self.assertEqual(S[3:,:],Q2)

    def test_full_library_qv_is_one_stacked_gram_with_cross_germ_blocks(self) -> None:
        nu=sp.symbols('nu')
        Q1=sp.Matrix(3,3,sp.symbols('c0:9'))
        Q2=sp.Matrix(3,3,sp.symbols('d0:9'))
        G=same_replica_library_qv([Q1,Q2],nu)
        self.assertEqual(G,sp.simplify(2*nu*sp.Matrix.vstack(Q1,Q2)*sp.Matrix.vstack(Q1,Q2).T))
        self.assertEqual(library_qv_block_residual([Q1,Q2],0,1,nu),sp.zeros(3))
        self.assertEqual(G[:3,3:],sp.simplify(2*nu*Q1*Q2.T))

    def test_selector_readout_recovers_the_selected_diagonal_qv_block(self) -> None:
        nu=sp.symbols('nu')
        Q1=sp.Matrix(3,3,sp.symbols('e0:9'))
        Q2=sp.Matrix(3,3,sp.symbols('f0:9'))
        self.assertEqual(selected_qv_readout_residual([Q1,Q2],1,nu),sp.zeros(3))

    def test_linear_physical_event_pushes_library_qv_by_congruence(self) -> None:
        nu=sp.symbols('nu')
        Q1=sp.Matrix(3,3,sp.symbols('g0:9'))
        Q2=sp.Matrix(3,3,sp.symbols('h0:9'))
        A=sp.Matrix(3,6,sp.symbols('p0:18'))
        self.assertEqual(linear_event_qv_functor_residual([Q1,Q2],A,nu),sp.zeros(3))

    def test_independent_noise_model_drops_common_replica_cross_blocks(self) -> None:
        nu=sp.symbols('nu')
        Q1=sp.diag(1,2,3); Q2=sp.diag(4,5,6)
        diff=independent_vs_common_qv_difference([Q1,Q2],nu)
        self.assertNotEqual(diff,sp.zeros(6))
        self.assertEqual(diff[:3,:3],sp.zeros(3))
        self.assertEqual(diff[3:,3:],sp.zeros(3))
        self.assertEqual(diff[:3,3:],sp.simplify(-2*nu*Q1*Q2.T))

    def test_stacked_martingale_mean_bias_rate_is_zero(self) -> None:
        self.assertEqual(stacked_martingale_mean_rate(4),sp.zeros(12,1))

    def test_fixed_noise_centered_covariance_rate_is_the_same_full_gram(self) -> None:
        nu=sp.symbols('nu')
        Q1=sp.diag(1,2,3); Q2=sp.Matrix([[0,1,0],[1,0,0],[0,0,1]])
        self.assertEqual(fixed_noise_centered_covariance_rate([Q1,Q2],nu),same_replica_library_qv([Q1,Q2],nu))

    def test_instantaneous_library_qv_rank_is_bounded_by_common_driver_dimension(self) -> None:
        Q1=sp.diag(1,2,3); Q2=sp.Matrix([[1,1,0],[0,1,1],[1,0,1]])
        rank,driver=qv_image_rank_bound([Q1,Q2],sp.Integer(1))
        self.assertLessEqual(rank,driver)
        self.assertEqual(driver,3)

    def test_exact_one_mode_ns_two_packet_noises_are_opposite_in_same_replica(self) -> None:
        t,nu,k=sp.symbols('t nu k', positive=True)
        c=one_mode_two_packet_common_noise_calibration(t,nu,k)
        self.assertEqual(c['opposite_noise_residual'],0)
        self.assertNotEqual(c['q1'],0)
        self.assertEqual(c['q2'],-c['q1'])

    def test_exact_one_mode_ns_cross_qv_is_negative_diagonal_and_cancels_synthesized_qv(self) -> None:
        t,nu,k=sp.symbols('t nu k', positive=True)
        c=one_mode_two_packet_common_noise_calibration(t,nu,k)
        self.assertEqual(c['cross_qv'],sp.simplify(-c['diagonal_qv']))
        self.assertEqual(c['synthesized_common_qv'],sp.zeros(3))
        self.assertNotEqual(c['synthesized_independent_qv'],sp.zeros(3))
        self.assertEqual(c['common_event_functor_residual'],sp.zeros(3))


if __name__ == '__main__':
    unittest.main()
