from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.first_bad_rule_admissibility import (
    adaptive_event_joint_law_obstruction,
    first_bad_admissibility_ledger,
    full_coherence_event_obstruction,
    passive_event_gauge_calibration,
    passive_raw_ranking_flip_calibration,
    physical_residual_support_locality_no_go,
    physical_score_passive_gauge_residual,
    persistent_library_switch_obstruction,
    raw_score_passive_gauge_change,
)


class FirstBadRuleAdmissibilityAudit(unittest.TestCase):
    def test_whitened_physical_score_is_exactly_passive_gauge_invariant(self) -> None:
        eps=sp.Matrix([2,-1,3])
        H=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        S=sp.Matrix([[1,1,0],[0,2,0],[1,0,1]])
        self.assertEqual(physical_score_passive_gauge_residual(eps,H,S),0)

    def test_raw_face_norm_is_not_passive_gauge_invariant(self) -> None:
        eps=sp.Matrix([1,0,0]); H=sp.eye(3); S=sp.diag(2,1,1)
        self.assertEqual(raw_score_passive_gauge_change(eps,H,S),3)

    def test_passive_basis_change_flips_raw_first_bad_ranking_without_physical_change(self) -> None:
        c=passive_raw_ranking_flip_calibration()
        self.assertEqual(c['raw_before'],(1,sp.Rational(9,4)))
        self.assertEqual(c['raw_after'],(4,sp.Rational(9,4)))
        self.assertEqual((c['raw_winner_before'],c['raw_winner_after']),(1,0))
        self.assertEqual(c['physical_before'],c['physical_after'])
        self.assertEqual((c['physical_winner_before'],c['physical_winner_after']),(1,1))

    def test_raw_event_block_changes_under_passive_bases_but_physical_event_map_does_not(self) -> None:
        c=passive_event_gauge_calibration()
        self.assertTrue(c['raw_block_changes'])
        self.assertEqual(c['physical_event_gauge_residual'],sp.zeros(3))

    def test_exact_quadratic_ns_physical_residual_collapse_does_not_imply_support_locality(self) -> None:
        Y,t,nu,rho=sp.symbols('Y t nu rho', positive=True)
        c=physical_residual_support_locality_no_go(Y,t,nu,rho)
        self.assertEqual(c['physical_energy'],rho**2)
        self.assertEqual(c['physical_energy_limit'],0)
        self.assertEqual(c['long_x_line_squared'],1)
        self.assertEqual(c['support_line_limit'],1)

    def test_selected_endpoint_state_and_second_moment_do_not_close_genuine_switches(self) -> None:
        c=persistent_library_switch_obstruction()
        self.assertTrue(all(c.values()))

    def test_diagonal_spectral_channels_do_not_close_next_linear_event(self) -> None:
        c=full_coherence_event_obstruction()
        self.assertTrue(c['input_channels_equal'])
        self.assertTrue(c['cross_coherence_different'])
        self.assertTrue(c['parent_channels_different'])
        self.assertEqual(c['parent_channel_difference'],2)

    def test_adaptive_event_requires_joint_event_state_law(self) -> None:
        c=adaptive_event_joint_law_obstruction()
        self.assertTrue(c['all_payloads_psd'])
        self.assertTrue(c['aligned_mean_closure_false'])
        self.assertTrue(c['anti_aligned_mean_closure_false'])
        self.assertEqual((c['aligned_exact'],c['aligned_naive']),(4,1))
        self.assertEqual((c['anti_aligned_exact'],c['anti_aligned_naive']),(0,1))

    def test_admissibility_ledger_is_necessary_only_and_does_not_define_first_bad_functional(self) -> None:
        Y,t,nu,rho=sp.symbols('Y t nu rho', positive=True)
        c=first_bad_admissibility_ledger(Y,t,nu,rho)
        for key in [
            'raw_ranking_is_gauge_artifact','physical_ranking_gauge_invariant',
            'physical_event_map_gauge_invariant','residual_collapse_does_not_imply_support_locality',
            'persistent_library_needed_for_switch','full_coherence_needed_for_linear_events',
            'adaptive_joint_law_needed',
        ]:
            self.assertTrue(c[key])
        self.assertFalse(c['sufficient_first_bad_functional_defined'])
        self.assertFalse(c['restart_continuation_regularity_proved'])


if __name__ == '__main__':
    unittest.main()
