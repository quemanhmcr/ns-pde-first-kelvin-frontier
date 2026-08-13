from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.frame_aware_kelvin_residual_refinement import (
    frame_aware_physical_synthesis_block,
)
from src.pde_audit.codeforming_surface_moment_tower import cofactor_map
from src.pde_audit.selected_principal_kelvin_lineage import one_mode_half_period_lineage_calibration
from src.pde_audit.spectral_kelvin_event_transfer import (
    degenerate_block_internal_basis_residual,
    full_parent_spectral_energy_residual,
    parent_spectral_channel,
    projector_family_algebra_residuals,
    spectral_event_transfer_residual,
    spectral_event_transfer_term,
    transfer_sector_sums,
    two_child_opposite_residual_transfer_calibration,
)


class SpectralKelvinEventTransferAudit(unittest.TestCase):
    def setUp(self) -> None:
        self.Pstd=[sp.diag(1,0,0),sp.diag(0,1,0),sp.diag(0,0,1)]
        self.Lp=sp.diag(2,3,4)
        self.L1=sp.diag(1,2,5)
        self.L2=sp.diag(3,1,2)
        self.Hp=cofactor_map(self.Lp)
        self.H1=cofactor_map(self.L1)
        self.H2=cofactor_map(self.L2)
        self.R1=sp.Matrix([[0,1,0],[1,0,0],[0,0,1]])
        self.R2=sp.eye(3)
        self.A1=frame_aware_physical_synthesis_block(self.Hp,self.H1,self.R1)
        self.A2=frame_aware_physical_synthesis_block(self.Hp,self.H2,self.R2)

    def test_standard_projectors_are_an_exact_resolution(self) -> None:
        self.assertTrue(all(R==sp.zeros(3) for R in projector_family_algebra_residuals(self.Pstd)))

    def test_parent_channel_is_exact_sum_of_all_child_pair_spectral_traffic(self) -> None:
        Q=sp.Matrix(6,6,sp.symbols('q0:36'))
        for alpha,Pp in enumerate(self.Pstd):
            self.assertEqual(
                spectral_event_transfer_residual(
                    Q,[self.A1,self.A2],sp.Integer(alpha+2),Pp,[self.Pstd,self.Pstd]
                ),0
            )

    def test_full_parent_metric_energy_is_sum_of_parent_projector_channels(self) -> None:
        Q=sp.Matrix(6,6,sp.symbols('qe0:36'))
        lambdas=[4,9,16]
        M=sp.diag(*lambdas)
        self.assertEqual(
            full_parent_spectral_energy_residual(Q,[self.A1,self.A2],lambdas,self.Pstd,M),0
        )

    def test_frame_aware_axis_mix_activates_cross_channel_transfer(self) -> None:
        # Child 1 x-channel is sent into parent y by R1/frame conversion.
        Q=sp.zeros(6)
        Q[0,0]=1
        Pparent_y=self.Pstd[1]
        term=spectral_event_transfer_term(
            Q,[self.A1,self.A2],1,Pparent_y,[self.Pstd,self.Pstd],0,0,0,0
        )
        self.assertNotEqual(sp.simplify(term),0)
        self.assertEqual(
            spectral_event_transfer_residual(Q,[self.A1,self.A2],1,Pparent_y,[self.Pstd,self.Pstd]),0
        )

    def test_transfer_uses_projectors_and_is_regular_at_parent_degeneracy(self) -> None:
        Q=sp.Matrix(6,6,sp.symbols('qd0:36'))
        Pxy=sp.diag(1,1,0); Pz=sp.diag(0,0,1)
        self.assertTrue(all(R==sp.zeros(3) for R in projector_family_algebra_residuals([Pxy,Pz])))
        self.assertEqual(
            spectral_event_transfer_residual(Q,[self.A1,self.A2],4,Pxy,[self.Pstd,self.Pstd]),0
        )

    def test_internal_basis_of_degenerate_child_block_does_not_change_total_transfer(self) -> None:
        Q=sp.Matrix(6,6,sp.symbols('qg0:36'))
        e1,e2,e3=sp.eye(3)[:,0],sp.eye(3)[:,1],sp.eye(3)[:,2]
        c=sp.sqrt(2)/2
        u=c*(e1+e2); v=c*(e1-e2)
        fam_a=[e1*e1.T,e2*e2.T,e3*e3.T]
        fam_b=[u*u.T,v*v.T,e3*e3.T]
        self.assertEqual(
            degenerate_block_internal_basis_residual(
                Q,[self.A1,self.A2],4,sp.diag(1,1,0),0,
                [fam_a,self.Pstd],fam_a,fam_b
            ),0
        )

    def test_exact_opposite_residual_calibration_requires_signed_cross_child_transfer(self) -> None:
        a=sp.symbols('a', nonzero=True)
        c=two_child_opposite_residual_transfer_calibration(a)
        self.assertEqual(c['parent_channel'],0)
        self.assertEqual(c['transfer_residual'],0)
        self.assertEqual(c['same_child_same_channel'],2*a**2)
        self.assertEqual(c['cross_child_same_channel'],-2*a**2)
        self.assertEqual(c['same_child_cross_channel'],0)
        self.assertEqual(c['cross_child_cross_channel'],0)

    def test_exact_one_mode_ns_half_period_is_the_signed_projector_transfer_witness(self) -> None:
        t,nu,k=sp.symbols('t nu k', positive=True)
        ns=one_mode_half_period_lineage_calibration(t,nu,k)
        amp=sp.simplify(ns['chi0'])
        c=two_child_opposite_residual_transfer_calibration(amp)
        self.assertNotEqual(amp,0)
        self.assertEqual(c['parent_channel'],0)
        self.assertEqual(c['same_child_same_channel'],sp.simplify(2*amp**2))
        self.assertEqual(c['cross_child_same_channel'],sp.simplify(-2*amp**2))
        self.assertEqual(c['transfer_residual'],0)

    def test_signed_transfer_cannot_be_replaced_by_positive_child_channel_kernel(self) -> None:
        c=two_child_opposite_residual_transfer_calibration(sp.Integer(1))
        positive_diagonal=c['same_child_same_channel']
        exact=c['parent_channel']
        self.assertGreater(int(positive_diagonal),0)
        self.assertEqual(exact,0)
        self.assertLess(int(c['cross_child_same_channel']),0)

    def test_sector_sum_reconstructs_parent_channel(self) -> None:
        Q=sp.Matrix(6,6,sp.symbols('qs0:36'))
        Pp=self.Pstd[0]
        sectors=transfer_sector_sums(Q,[self.A1,self.A2],2,Pp,[self.Pstd,self.Pstd])
        exact=parent_spectral_channel(Q,[self.A1,self.A2],2,Pp)
        self.assertEqual(sp.simplify(sum(sectors)-exact),0)


if __name__ == '__main__':
    unittest.main()
