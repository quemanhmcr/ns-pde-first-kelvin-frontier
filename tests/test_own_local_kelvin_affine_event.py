from __future__ import annotations
import unittest
import sympy as sp
from src.pde_audit.codeforming_surface_moment_tower import cofactor_map
from src.pde_audit.own_local_kelvin_affine_event import (
    affine_composition_residuals, affine_noise_gram_residual, affine_noise_response,
    affine_pathwise_second_moment_residual, affine_target_coboundary,
    cubic_heat_shear_reanchoring_calibration, cubic_two_child_own_local_mismatch,
    own_local_codeforming_affine_data, own_local_physical_affine_data,
    own_local_physical_refinement_residual, own_local_raw_error_refinement_residual,
    own_local_target_face, selected_affine_jump, selected_affine_jump_square_residual,
    target_gradient_coboundary,
)

class OwnLocalKelvinAffineEventAudit(unittest.TestCase):
    def setUp(self) -> None:
        self.Lp=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        self.L1=sp.Matrix([[1,1,0],[0,2,0],[0,1,3]])
        self.L2=sp.Matrix([[3,0,1],[1,2,0],[0,1,1]])
        self.Hp=cofactor_map(self.Lp); self.H1=cofactor_map(self.L1); self.H2=cofactor_map(self.L2)
        self.R1=sp.Matrix([[1,1,0],[0,1,0],[0,0,2]])
        self.R2=sp.Matrix([[2,0,0],[1,1,1],[0,0,1]])

    def test_raw_own_local_refinement_has_exact_target_face(self) -> None:
        K1=sp.Matrix(sp.symbols('k1_0:3')); K2=sp.Matrix(sp.symbols('k2_0:3'))
        w1=sp.Matrix(sp.symbols('w1_0:3')); w2=sp.Matrix(sp.symbols('w2_0:3')); wp=sp.Matrix(sp.symbols('wp_0:3'))
        self.assertEqual(own_local_raw_error_refinement_residual(
            [K1,K2],[self.H1,self.H2],[self.R1,self.R2],[w1,w2],wp),sp.zeros(3,1))
        self.assertEqual(own_local_target_face(
            [self.H1,self.H2],[self.R1,self.R2],[wp,wp],wp),sp.zeros(3,1))
        self.assertNotEqual(own_local_target_face(
            [self.H1,self.H2],[self.R1,self.R2],[w1,w2],wp),sp.zeros(3,1))

    def test_physical_own_local_event_is_affine(self) -> None:
        K1=sp.Matrix(sp.symbols('a1_0:3')); K2=sp.Matrix(sp.symbols('a2_0:3'))
        w1=sp.Matrix([1,2,3]); w2=sp.Matrix([2,-1,4]); wp=sp.Matrix([-1,1,0])
        self.assertEqual(own_local_physical_refinement_residual(
            [K1,K2],[self.H1,self.H2],[self.R1,self.R2],[w1,w2],wp),sp.zeros(3,1))
        A,d=own_local_physical_affine_data(self.Hp,[self.H1,self.H2],[self.R1,self.R2],[w1,w2],wp)
        self.assertEqual(A.shape,(3,6)); self.assertNotEqual(d,sp.zeros(3,1))

    def test_codeforming_offset_is_delta_over_parent_volume(self) -> None:
        w1=sp.Matrix([1,2,3]); w2=sp.Matrix([2,-1,4]); wp=sp.Matrix([-1,1,0])
        B,d=own_local_codeforming_affine_data(self.Lp,[self.L1,self.L2],[self.R1,self.R2],[w1,w2],wp)
        delta=own_local_target_face([self.H1,self.H2],[self.R1,self.R2],[w1,w2],wp)
        self.assertEqual(d,sp.simplify(delta/sp.det(self.Lp))); self.assertEqual(B.shape,(3,6))

    def test_target_coboundary_composes_exactly(self) -> None:
        A1=sp.Matrix([[1,2],[0,1]]); A2=sp.Matrix([[2,0],[1,1]])
        O0=sp.Matrix([1,3]); O1=sp.Matrix([2,-1]); O2=sp.Matrix([4,5]); x0=sp.Matrix([7,-2])
        sr,dr=affine_composition_residuals(A1,A2,O0,O1,O2,x0)
        self.assertEqual(sr,sp.zeros(2,1)); self.assertEqual(dr,sp.zeros(2,1))
        d1=affine_target_coboundary(A1,O0,O1); d2=affine_target_coboundary(A2,O1,O2)
        self.assertEqual(sp.simplify(A2*d1+d2),affine_target_coboundary(A2*A1,O0,O2))

    def test_affine_second_moment_has_cross_and_offset_faces(self) -> None:
        A=sp.Matrix([[1,2],[0,1]]); x=sp.Matrix([3,-1]); d=sp.Matrix([2,4])
        self.assertEqual(affine_pathwise_second_moment_residual(A,x,d),sp.zeros(2))

    def test_selector_plus_affine_event_has_target_jump_faces(self) -> None:
        x=sp.Matrix([1,2,3,4])
        A=sp.Matrix([[1,0,0,0],[0,1,1,0],[0,0,0,1],[1,0,0,1]])
        Em=sp.Matrix([[1,0,0,0],[0,1,0,0]]); Ep=sp.Matrix([[0,0,1,0],[0,0,0,1]])
        d=sp.Matrix([2,-1,3,5])
        self.assertEqual(selected_affine_jump(x,A,d,Em,Ep),sp.simplify((Ep*A-Em)*x+Ep*d))
        self.assertEqual(selected_affine_jump_square_residual(x,A,d,Em,Ep),sp.zeros(2))

    def test_target_gradient_face_changes_noise_when_A_is_identity(self) -> None:
        A=sp.eye(2); N=sp.zeros(2); Gm=sp.zeros(2); Gp=sp.Matrix([[1,2],[3,4]])
        self.assertEqual(target_gradient_coboundary(A,Gm,Gp),-Gp)
        self.assertEqual(affine_noise_response(A,N,Gm,Gp),-Gp)
        self.assertEqual(affine_noise_gram_residual(A,N,Gm,Gp),sp.zeros(2))

    def test_cubic_heat_shear_exact_ns_reanchoring_referee(self) -> None:
        a,p,b,ell,t,nu=sp.symbols('a p b ell t nu', nonzero=True)
        c=cubic_heat_shear_reanchoring_calibration(a,p,b,ell,t,nu)
        self.assertEqual(c['heat_equation_residual'],0)
        self.assertEqual(c['raw_error'],sp.simplify(2*b*ell*(-3*a**2-b**2+3*p**2)))
        self.assertEqual(c['residual_noise_y'],sp.simplify(12*b*ell*(p-a)))
        own=cubic_heat_shear_reanchoring_calibration(a,a,b,ell,t,nu)
        zero=cubic_heat_shear_reanchoring_calibration(a,0,b,ell,t,nu)
        self.assertEqual(own['residual_noise_y'],0)
        self.assertEqual(zero['residual_noise_y'],sp.simplify(-12*a*b*ell))

    def test_two_child_cubic_witness_refutes_own_local_linear_extension(self) -> None:
        a,b,ell,t,nu=sp.symbols('a b ell t nu', positive=True)
        c=cubic_two_child_own_local_mismatch(a,b,ell,t,nu)
        self.assertEqual(c['mismatch'],c['expected_mismatch']); self.assertNotEqual(c['mismatch'],0)

if __name__ == '__main__':
    unittest.main()
