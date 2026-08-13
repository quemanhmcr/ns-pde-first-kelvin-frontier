from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.cycle_selector import rank_one_selector
from src.pde_audit.selected_principal_kelvin_lineage import (
    block_diagonal_fiber_operator,
    coefficient_synthesis_map,
    diagonal_only_spectral_channel,
    first_bad_pair_spectral_commutator,
    first_bad_spectral_commutator,
    germ_extraction_map,
    one_mode_half_period_lineage_calibration,
    selector_reset_weighted_faces,
    selector_reset_weighted_residual,
    selector_reset_excursion_residual,
    selector_excursion_pair_face_sums,
    selected_library_weighted_energy,
    selected_library_spectral_decomposition_residual,
    spectral_synthesis_channel,
    spectral_synthesis_pair_expansion_residual,
    synthesis_block_expansion_residual,
    synthesis_pair_functor_residual,
    synthesized_second_moment,
)


class SelectedPrincipalKelvinLineageAudit(unittest.TestCase):
    def test_first_bad_rank_one_selector_commutes_with_per_germ_spectral_blocks(self) -> None:
        S = rank_one_selector(3, 1)
        P0 = sp.diag(1, 0, 0)
        P1 = sp.diag(0, 1, 0)
        P2 = sp.Matrix([[sp.Rational(1,2), sp.Rational(1,2), 0], [sp.Rational(1,2), sp.Rational(1,2), 0], [0,0,0]])
        self.assertEqual(first_bad_spectral_commutator(S, [P0,P1,P2]), sp.zeros(9))
        self.assertEqual(first_bad_pair_spectral_commutator(S, [P0,P1,P2]), sp.zeros(81))

    def test_germ_mixing_map_need_not_commute_with_per_germ_spectral_blocks(self) -> None:
        S = sp.Matrix([[0,1],[1,0]])
        P0 = sp.diag(1,0,0)
        P1 = sp.diag(0,1,0)
        comm = first_bad_spectral_commutator(S, [P0,P1])
        self.assertNotEqual(comm, sp.zeros(6))

    def test_selected_endpoint_energy_is_exact_sum_of_selected_germ_spectral_blocks(self) -> None:
        S = rank_one_selector(2,1)
        Q = sp.Matrix(6,6,sp.symbols('qs0:36'))
        P0 = [sp.diag(1,0,0),sp.diag(0,1,0),sp.diag(0,0,1)]
        c = sp.sqrt(2)/2
        v1 = sp.Matrix([c,c,0]); v2 = sp.Matrix([c,-c,0]); v3 = sp.Matrix([0,0,1])
        P1 = [v1*v1.T,v2*v2.T,v3*v3.T]
        lam0=[1,4,9]; lam1=[2,5,7]
        M0=sum((lam0[i]*P0[i] for i in range(3)),sp.zeros(3))
        M1=sum((lam1[i]*P1[i] for i in range(3)),sp.zeros(3))
        self.assertEqual(
            selected_library_spectral_decomposition_residual(Q,S,[M0,M1],[P0,P1],[lam0,lam1]),
            0,
        )
        A1=germ_extraction_map(2,1)
        self.assertEqual(
            selected_library_weighted_energy(Q,S,[M0,M1]),
            sp.simplify(sp.trace(M1*synthesized_second_moment(Q,A1))),
        )

    def test_first_bad_extraction_is_literal_fiber_coordinate_selection(self) -> None:
        A = germ_extraction_map(3, 1)
        x = sp.Matrix(sp.symbols('x0:9'))
        self.assertEqual(A*x, sp.Matrix(x[3:6, :]))

    def test_linear_synthesis_second_moment_uses_full_pair_functor(self) -> None:
        q = sp.symbols('q0:36')
        Q = sp.Matrix(6,6,q)
        a,b = sp.symbols('a b')
        A = coefficient_synthesis_map([a,b])
        self.assertEqual(synthesis_pair_functor_residual(Q,A), sp.zeros(9,1))
        self.assertEqual(synthesis_block_expansion_residual(Q,[a,b]), sp.zeros(3))

    def test_spectral_parent_channel_expands_over_all_ordered_child_pairs(self) -> None:
        q = sp.symbols('q0:36')
        Q = sp.Matrix(6,6,q)
        a,b,lam = sp.symbols('a b lam')
        P = sp.diag(1,0,1)
        self.assertEqual(
            spectral_synthesis_pair_expansion_residual(Q,[a,b],lam,P),
            0,
        )

    def test_diagonal_only_spectral_parent_channel_drops_cross_child_content(self) -> None:
        x,y = sp.symbols('x y', nonzero=True)
        v = sp.Matrix([x,0,0,y,0,0])
        Q = v*v.T
        P = sp.diag(1,0,0)
        full = spectral_synthesis_channel(Q,[1,1],1,P)
        diag = diagonal_only_spectral_channel(Q,[1,1],1,P)
        self.assertEqual(sp.expand(full-diag), 2*x*y)

    def test_finite_first_bad_reset_is_metric_face_plus_full_pair_jump(self) -> None:
        q = sp.symbols('q0:36')
        Q = sp.Matrix(6,6,q)
        A0 = germ_extraction_map(2,0)
        A1 = germ_extraction_map(2,1)
        M0 = sp.diag(1,2,3)
        M1 = sp.diag(4,5,6)
        self.assertEqual(selector_reset_weighted_residual(Q,A0,A1,M0,M1),0)
        faces = selector_reset_weighted_faces(Q,A0,A1,M0,M1)
        self.assertEqual(faces.total_jump, faces.reconstructed)

    def test_pure_selector_reset_with_fixed_metric_has_no_geometry_face(self) -> None:
        q = sp.symbols('q0:36')
        Q = sp.Matrix(6,6,q)
        A0 = germ_extraction_map(2,0)
        A1 = germ_extraction_map(2,1)
        M = sp.diag(2,3,5)
        faces = selector_reset_weighted_faces(Q,A0,A1,M,M)
        self.assertEqual(faces.geometry,0)
        self.assertEqual(faces.total_jump,faces.pair_left+faces.pair_right+faces.pair_quadratic)

    def test_exact_one_mode_half_period_children_have_opposite_finite_residuals(self) -> None:
        t,nu,k = sp.symbols('t nu k', positive=True)
        c = one_mode_half_period_lineage_calibration(t,nu,k)
        self.assertEqual(c['opposite_residual_zero'],0)
        self.assertNotEqual(c['chi0'],0)
        self.assertEqual(c['chi1'],-c['chi0'])

    def test_exact_one_mode_cross_child_channel_cancels_positive_diagonals(self) -> None:
        t,nu,k = sp.symbols('t nu k', positive=True)
        c = one_mode_half_period_lineage_calibration(t,nu,k)
        self.assertEqual(c['full_parent_channel'],0)
        self.assertNotEqual(c['diagonal_parent_channel'],0)
        self.assertEqual(c['cross_child_channel'],-c['diagonal_parent_channel'])

    def test_exact_one_mode_closed_selector_excursion_has_positive_quadratic_path_length_but_zero_net_revaluation(self) -> None:
        t,nu,k = sp.symbols('t nu k', positive=True)
        c = one_mode_half_period_lineage_calibration(t,nu,k)
        Q = c['library_second_moment']
        A0,A1 = germ_extraction_map(2,0),germ_extraction_map(2,1)
        M = (sp.pi/(2*k))**2*sp.eye(3)
        self.assertEqual(selector_reset_excursion_residual(Q,[A0,A1,A0],[M,M,M]),0)
        geometry,left,right,quad = selector_excursion_pair_face_sums(Q,[A0,A1,A0],[M,M,M])
        self.assertEqual(geometry,0)
        self.assertEqual(sp.simplify(left+right+quad),0)
        self.assertGreater(float(quad.subs({t:1,nu:1,k:1}).evalf()),0)
        self.assertLess(float((left+right).subs({t:1,nu:1,k:1}).evalf()),0)

    def test_exact_one_mode_first_bad_reset_is_signed_pair_revaluation_not_positive_cost(self) -> None:
        t,nu,k = sp.symbols('t nu k', positive=True)
        c = one_mode_half_period_lineage_calibration(t,nu,k)
        self.assertEqual(c['reset_total_jump'],0)
        self.assertEqual(c['reset_reconstruction_residual'],0)
        self.assertLess(float(c['reset_pair_left'].subs({t:1,nu:1,k:1}).evalf()),0)
        self.assertLess(float(c['reset_pair_right'].subs({t:1,nu:1,k:1}).evalf()),0)
        self.assertGreater(float(c['reset_pair_quadratic'].subs({t:1,nu:1,k:1}).evalf()),0)

    def test_endpoint_spectral_channels_do_not_define_cross_event_axis_matching(self) -> None:
        # A repeated eigenvalue block has many rank-one bases with the same block energy.
        Q = sp.diag(3,1,2)
        e1,e2 = sp.eye(3)[:,0],sp.eye(3)[:,1]
        u = sp.simplify((e1+e2)/sp.sqrt(2))
        v = sp.simplify((e1-e2)/sp.sqrt(2))
        before = [(e1.T*Q*e1)[0],(e2.T*Q*e2)[0]]
        after = [sp.simplify((u.T*Q*u)[0]),sp.simplify((v.T*Q*v)[0])]
        self.assertNotEqual(before,after)
        self.assertEqual(sp.simplify(sum(before)-sum(after)),0)


if __name__ == '__main__':
    unittest.main()
