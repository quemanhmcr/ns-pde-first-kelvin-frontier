from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.active_pair import interval_boundary, interval_refinement_map
from src.pde_audit.pair_worldsheet import refinement_pair_coefficients

from src.pde_audit.codeforming_surface_moment_tower import cofactor_map
from src.pde_audit.frame_aware_kelvin_residual_refinement import (
    block_synthesis_pair_expansion_residual,
    block_synthesis_pair_functor_residual,
    block_synthesis_second_moment,
    block_synthesis_spectral_channel_residual,
    codeforming_determinant_ratio_residual,
    codeforming_refinement_from_raw_error_residual,
    codeforming_synthesis_block,
    compatible_parent_packet,
    compatible_raw_error_refinement_residual,
    cofactor_physical_synthesis_residual,
    frame_aware_physical_synthesis_block,
    frame_aware_physical_synthesis_map,
    isotropic_frame_aware_scale_residuals,
    orientation_complete_chain_refinement_residual,
    orientation_preserving_scalar_refinement_blocks,
    scalar_refinement_pair_block_residual,
    physical_reconstruction_refinement_residual,
    physical_synthesis_gauge_residual,
    quadratic_isotropic_packet_refinement_calibration,
    raw_orientation_error,
    reparameterized_raw_refinement_block,
)


class FrameAwareKelvinResidualRefinementAudit(unittest.TestCase):
    def setUp(self) -> None:
        self.Lp = sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        self.L1 = sp.Matrix([[1,1,0],[0,2,0],[0,1,3]])
        self.L2 = sp.Matrix([[3,0,1],[1,2,0],[0,1,1]])
        self.Hp = cofactor_map(self.Lp)
        self.H1 = cofactor_map(self.L1)
        self.H2 = cofactor_map(self.L2)
        self.R1 = sp.Matrix([[1,1,0],[0,1,0],[0,0,2]])
        self.R2 = sp.Matrix([[2,0,0],[1,1,1],[0,0,1]])

    def test_compatible_packet_refinement_makes_raw_error_linear(self) -> None:
        omega = sp.Matrix(sp.symbols('w0:3'))
        K1 = sp.Matrix(sp.symbols('k1_0:3'))
        K2 = sp.Matrix(sp.symbols('k2_0:3'))
        Kp, Hp = compatible_parent_packet([K1,K2],[self.H1,self.H2],[self.R1,self.R2])
        self.assertEqual(
            raw_orientation_error(Kp,Hp,omega),
            sp.simplify(
                self.R1*raw_orientation_error(K1,self.H1,omega)
                + self.R2*raw_orientation_error(K2,self.H2,omega)
            ),
        )
        self.assertEqual(
            compatible_raw_error_refinement_residual(
                [K1,K2],[self.H1,self.H2],[self.R1,self.R2],omega
            ),
            sp.zeros(3,1),
        )

    def test_whitening_forces_frame_aware_physical_residual_synthesis(self) -> None:
        e1 = sp.Matrix(sp.symbols('e1_0:3'))
        e2 = sp.Matrix(sp.symbols('e2_0:3'))
        self.assertEqual(
            physical_reconstruction_refinement_residual(
                [e1,e2],[self.H1,self.H2],[self.R1,self.R2],self.Hp
            ),
            sp.zeros(3,1),
        )

    def test_parent_and_child_orientation_basis_changes_leave_physical_synthesis_invariant(self) -> None:
        Sp = sp.Matrix([[1,1,0],[0,1,0],[0,0,2]])
        S1 = sp.Matrix([[2,0,0],[1,1,0],[0,0,1]])
        self.assertEqual(
            physical_synthesis_gauge_residual(self.Hp,self.H1,self.R1,Sp,S1),
            sp.zeros(3),
        )
        Rnew = reparameterized_raw_refinement_block(self.R1,Sp,S1)
        before = frame_aware_physical_synthesis_block(self.Hp,self.H1,self.R1)
        after = frame_aware_physical_synthesis_block(self.Hp*Sp,self.H1*S1,Rnew)
        self.assertEqual(after,before)

    def test_cofactor_geometry_gives_exact_line_frame_conjugation(self) -> None:
        self.assertEqual(
            cofactor_physical_synthesis_residual(self.Lp,self.L1,self.R1),
            sp.zeros(3),
        )

    def test_codeforming_synthesis_collapses_to_determinant_ratio_times_raw_block(self) -> None:
        self.assertEqual(
            codeforming_determinant_ratio_residual(self.Lp,self.L1,self.R1),
            sp.zeros(3),
        )
        expected = sp.simplify(sp.det(self.L1)/sp.det(self.Lp)*self.R1)
        self.assertEqual(codeforming_synthesis_block(self.Lp,self.L1,self.R1),expected)

    def test_direct_raw_error_parent_equals_codeforming_block_synthesis(self) -> None:
        c1 = sp.Matrix(sp.symbols('c1_0:3'))
        c2 = sp.Matrix(sp.symbols('c2_0:3'))
        self.assertEqual(
            codeforming_refinement_from_raw_error_residual(
                [c1,c2],self.Lp,[self.L1,self.L2],[self.R1,self.R2]
            ),
            sp.zeros(3,1),
        )

    def test_common_frame_scalar_blocks_reduce_to_previous_common_fiber_synthesis(self) -> None:
        a = sp.symbols('a')
        R = a*sp.eye(3)
        A = frame_aware_physical_synthesis_block(self.Hp,self.Hp,R)
        B = codeforming_synthesis_block(self.Lp,self.Lp,R)
        self.assertEqual(A,R)
        self.assertEqual(B,R)

    def test_naive_common_fiber_scalar_weight_fails_for_unequal_frames(self) -> None:
        a = sp.symbols('a', nonzero=True)
        R = a*sp.eye(3)
        A = frame_aware_physical_synthesis_block(self.Hp,self.H1,R)
        self.assertNotEqual(sp.simplify(A-R),sp.zeros(3))
        self.assertEqual(
            sp.simplify(
                A - sp.det(self.L1)/sp.det(self.Lp)*self.Lp*R*self.L1.inv()
            ),
            sp.zeros(3),
        )

    def test_isotropic_frames_expose_exact_area_and_volume_ratios(self) -> None:
        rp,ri,a = sp.symbols('rp ri a', positive=True)
        phys,cof = isotropic_frame_aware_scale_residuals(rp,ri,a)
        self.assertEqual(phys,sp.zeros(3))
        self.assertEqual(cof,sp.zeros(3))

    def test_block_synthesis_second_moment_uses_full_pair_functor(self) -> None:
        q = sp.symbols('q0:36')
        Q = sp.Matrix(6,6,q)
        A1 = frame_aware_physical_synthesis_block(self.Hp,self.H1,self.R1)
        A2 = frame_aware_physical_synthesis_block(self.Hp,self.H2,self.R2)
        self.assertEqual(block_synthesis_pair_functor_residual(Q,[A1,A2]),sp.zeros(9,1))
        self.assertEqual(block_synthesis_pair_expansion_residual(Q,[A1,A2]),sp.zeros(3))

    def test_frame_aware_parent_spectral_channel_contains_all_ordered_child_pairs(self) -> None:
        q = sp.symbols('q0:36')
        Q = sp.Matrix(6,6,q)
        A1 = frame_aware_physical_synthesis_block(self.Hp,self.H1,self.R1)
        A2 = frame_aware_physical_synthesis_block(self.Hp,self.H2,self.R2)
        lam = sp.symbols('lam')
        P = sp.diag(1,0,1)
        self.assertEqual(
            block_synthesis_spectral_channel_residual(Q,[A1,A2],lam,P),0
        )

    def test_exact_quadratic_ns_packet_refinement_uses_area_and_volume_weights(self) -> None:
        r1,r2,a1,a2,t,nu = sp.symbols('r1 r2 a1 a2 t nu', positive=True)
        c=quadratic_isotropic_packet_refinement_calibration([r1,r2],[a1,a2],t,nu)
        self.assertEqual(c['physical_prediction_residual'],sp.zeros(3,1))
        self.assertEqual(c['codeforming_prediction_residual'],sp.zeros(3,1))
        hp=a1*r1**2+a2*r2**2
        expected_r=sp.Matrix([0,0,-(a1*r1**3+a2*r2**3)/hp])
        expected_chi=sp.Matrix([0,0,-(a1*r1**3+a2*r2**3)/hp**sp.Rational(3,2)])
        self.assertEqual(sp.simplify(c['parent_physical_residual']-expected_r),sp.zeros(3,1))
        self.assertEqual(sp.simplify(c['parent_codeforming_residual']-expected_chi),sp.zeros(3,1))
        numeric={r1:1,r2:2,a1:1,a2:1,t:1,nu:1}
        self.assertNotEqual(
            c['parent_physical_residual'].subs(numeric),
            c['naive_common_fiber_physical_sum'].subs(numeric),
        )

    def test_scalar_current_refinement_has_canonical_orientation_complete_lift(self) -> None:
        weights=[sp.Rational(1,3),sp.Rational(2,3)]
        blocks=orientation_preserving_scalar_refinement_blocks(weights)
        self.assertEqual(blocks,[weights[0]*sp.eye(3),weights[1]*sp.eye(3)])
        self.assertTrue(all(R == sp.zeros(9) for R in scalar_refinement_pair_block_residual(weights)))
        coeffs=refinement_pair_coefficients([sp.Rational(1,3),sp.Rational(2,3)])
        for i in range(2):
            for j in range(2):
                self.assertEqual(
                    sp.kronecker_product(blocks[i],blocks[j]),
                    sp.Rational(coeffs[(i,j)].numerator,coeffs[(i,j)].denominator)*sp.eye(9),
                )

    def test_interval_chain_refinement_lifts_exactly_to_orientation_complete_packet(self) -> None:
        Bfine,R1,R0=interval_refinement_map(2,2)
        Bcoarse=interval_boundary(2)
        self.assertEqual(
            orientation_complete_chain_refinement_residual(Bfine,Bcoarse,R1,R0,3),
            sp.zeros(Bfine.rows*3,R1.cols*3),
        )

    def test_frame_aware_map_is_unique_for_arbitrary_child_physical_residuals(self) -> None:
        # If C maps every child r to the whitened parent residual, C must equal H_P^-T R H_i^T.
        C = frame_aware_physical_synthesis_block(self.Hp,self.H1,self.R1)
        basis = [sp.eye(3)[:,i] for i in range(3)]
        for r in basis:
            eps = self.H1.T*r
            parent = self.Hp.inv().T*self.R1*eps
            self.assertEqual(sp.simplify(parent-C*r),sp.zeros(3,1))


if __name__ == '__main__':
    unittest.main()
