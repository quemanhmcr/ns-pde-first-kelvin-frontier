from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.codeforming_surface_moment_tower import cofactor_map
from src.pde_audit.frame_aware_kelvin_residual_refinement import (
    frame_aware_physical_synthesis_block,
    codeforming_synthesis_block,
)
from src.pde_audit.kelvin_event_normal_form import (
    channel_only_composition_counterexample,
    codeforming_event_composition_residual,
    codeforming_raw_normal_form_residual,
    frame_aware_event_composition_residual,
    intermediate_degenerate_basis_telescope_residual,
    intermediate_projector_telescope_residual,
    pair_functor_event_composition_residual,
    physical_raw_normal_form_residual,
    raw_block_from_codeforming_synthesis,
    raw_block_from_physical_synthesis,
    second_moment_event_composition_residual,
    symmetric_event_probe_reconstruction_residual,
    symmetric_second_moment_from_event_probes,
)


class KelvinEventNormalFormAudit(unittest.TestCase):
    def setUp(self) -> None:
        self.Lp=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        self.Lm=sp.Matrix([[1,1,0],[0,2,1],[1,0,3]])
        self.Lc=sp.Matrix([[3,0,1],[1,2,0],[0,1,1]])
        self.Hp=cofactor_map(self.Lp); self.Hm=cofactor_map(self.Lm); self.Hc=cofactor_map(self.Lc)
        self.Rpm=sp.Matrix([[1,1,0],[0,1,0],[0,0,2]])
        self.Rmc=sp.Matrix([[2,0,0],[1,1,1],[0,0,1]])

    def test_physical_A_is_a_complete_raw_packet_normal_form_given_frames(self) -> None:
        A=frame_aware_physical_synthesis_block(self.Hp,self.Hc,self.Rpm)
        recovered=raw_block_from_physical_synthesis(self.Hp,self.Hc,A)
        self.assertEqual(recovered,self.Rpm)
        self.assertEqual(physical_raw_normal_form_residual(self.Hp,self.Hc,self.Rpm),sp.zeros(3))

    def test_codeforming_B_is_a_complete_raw_packet_normal_form_given_volumes(self) -> None:
        B=codeforming_synthesis_block(self.Lp,self.Lc,self.Rpm)
        recovered=raw_block_from_codeforming_synthesis(self.Lp,self.Lc,B)
        self.assertEqual(recovered,self.Rpm)
        self.assertEqual(codeforming_raw_normal_form_residual(self.Lp,self.Lc,self.Rpm),sp.zeros(3))

    def test_frame_aware_event_maps_compose_and_intermediate_area_frame_cancels(self) -> None:
        self.assertEqual(
            frame_aware_event_composition_residual(
                self.Hp,self.Hm,self.Hc,self.Rpm,self.Rmc
            ),sp.zeros(3)
        )

    def test_codeforming_event_maps_compose_and_intermediate_volume_cancels(self) -> None:
        self.assertEqual(
            codeforming_event_composition_residual(
                self.Lp,self.Lm,self.Lc,self.Rpm,self.Rmc
            ),sp.zeros(3)
        )

    def test_second_moment_event_composition_is_exact_for_rectangular_maps(self) -> None:
        Q=sp.Matrix(3,3,sp.symbols('q0:9'))
        A1=sp.Matrix([[1,2,0],[0,1,1]])
        A2=sp.Matrix([[1,0],[0,1],[1,1]])
        self.assertEqual(second_moment_event_composition_residual(Q,A1,A2),sp.zeros(3))

    def test_pair_functor_composes_exactly(self) -> None:
        A1=sp.Matrix(4,6,sp.symbols('pa0:24'))
        A2=sp.Matrix(3,4,sp.symbols('pb0:12'))
        self.assertEqual(pair_functor_event_composition_residual(A1,A2),sp.zeros(9,36))

    def test_intermediate_spectral_resolution_telescopes_out_of_composite_event(self) -> None:
        Q=sp.Matrix(3,3,sp.symbols('qt0:9'))
        A1=sp.Matrix([[1,1,0],[0,1,0],[0,0,1]])
        A2=sp.Matrix([[2,0,1],[0,1,0],[1,0,1]])
        P=[sp.diag(1,0,0),sp.diag(0,1,0),sp.diag(0,0,1)]
        self.assertEqual(
            intermediate_projector_telescope_residual(Q,A1,A2,5,P[0],P),0
        )

    def test_degenerate_intermediate_basis_is_not_event_ancestry_data(self) -> None:
        Q=sp.Matrix(3,3,sp.symbols('qd0:9'))
        A1=sp.Matrix([[1,1,0],[0,1,0],[0,0,1]])
        A2=sp.Matrix([[2,0,1],[0,1,0],[1,0,1]])
        e1,e2,e3=sp.eye(3)[:,0],sp.eye(3)[:,1],sp.eye(3)[:,2]
        c=sp.sqrt(2)/2; u=c*(e1+e2); v=c*(e1-e2)
        fam_a=[e1*e1.T,e2*e2.T,e3*e3.T]
        fam_b=[u*u.T,v*v.T,e3*e3.T]
        self.assertEqual(
            intermediate_degenerate_basis_telescope_residual(
                Q,A1,A2,5,sp.diag(1,1,0),fam_a,fam_b
            ),0
        )

    def test_scalar_endpoint_channel_list_is_not_compositional_state(self) -> None:
        c=channel_only_composition_counterexample()
        self.assertEqual(c['input_channels_plus'],c['input_channels_minus'])
        self.assertNotEqual(c['cross_coherence_plus'],c['cross_coherence_minus'])
        self.assertNotEqual(c['parent_channel_plus'],c['parent_channel_minus'])
        self.assertEqual(c['parent_channel_difference'],2)

    def test_full_symmetric_second_moment_is_reconstructed_by_linear_event_probes(self) -> None:
        q00,q11,q22,q01,q02,q12=sp.symbols('q00 q11 q22 q01 q02 q12')
        Q=sp.Matrix([[q00,q01,q02],[q01,q11,q12],[q02,q12,q22]])
        self.assertEqual(symmetric_event_probe_reconstruction_residual(Q),sp.zeros(3))
        self.assertEqual(symmetric_second_moment_from_event_probes(Q),Q)

    def test_channel_only_counterexample_uses_positive_semidefinite_second_moments(self) -> None:
        c=channel_only_composition_counterexample(sp.Rational(1,2))
        for key in ('Q_plus','Q_minus'):
            Q=c[key]
            self.assertTrue(all(ev >= 0 for ev in Q.eigenvals()))


if __name__ == '__main__':
    unittest.main()
