import unittest
import sympy as sp

from src.pde_audit.intrinsic_curvature_support_grammar import (
    coercive_curvature_support_trace_gap,
    critical_curvature_covariant_residual_at,
    curvature_support_connection_cancellation_residual,
    curvature_support_tensor,
    curvature_support_trace_connection_residual,
    kernel_compression,
    kernel_normalization_face_residual,
    kernel_normalization_compression_residual,
    moving_branch_curvature_support_residual,
    moving_branch_effective_curvature_source,
    one_mode_persistent_flat_kernel_calibration,
    psd_kernel_right_viability_quadratic,
)
from src.pde_audit.intrinsic_curvature_support_calibrations import (
    three_mode_kernel_birth_calibration,
    three_mode_kernel_birth_global_certificate,
    three_mode_kernel_birth_global_polynomial,
)


class IntrinsicCurvatureSupportGrammarTests(unittest.TestCase):
    def setUp(self):
        self.x,self.y,self.z,self.t=sp.symbols('x y z t', real=True)
        self.coords=(self.x,self.y,self.z)
        self.nu=sp.symbols('nu', positive=True)

    def test_covariant_curvature_law_is_exact_at_critical_point(self):
        x,y,z=self.coords
        a,b=sp.symbols('a b', real=True)
        g=1-x**2-2*y**2-3*z**2
        u=sp.Matrix([a*x+b*y,-a*y,-b*x])
        gradg=sp.Matrix([sp.diff(g,q) for q in self.coords])
        phi=sp.simplify((gradg.T*u)[0])
        r=critical_curvature_covariant_residual_at(g,phi,u,self.coords,self.t,{x:0,y:0,z:0})
        self.assertEqual(r,sp.zeros(3))

    def test_connection_cancels_matrixwise_in_curvature_support_tensor(self):
        A=sp.Matrix([[1,2,0],[0,-3,1],[4,0,2]])
        Q=sp.Matrix([[2,1,0],[1,3,1],[0,1,5]])
        K=sp.Matrix([[5,0,1],[0,6,2],[1,2,7]])
        L=sp.Matrix([[1,1,0],[0,2,1],[1,0,1]])
        self.assertEqual(curvature_support_connection_cancellation_residual(A,Q,K,L),sp.zeros(3))

    def test_trace_pairing_has_same_connection_cancellation(self):
        A=sp.Matrix([[1,2,0],[0,-3,1],[4,0,2]])
        Q=sp.diag(2,3,5); K=sp.diag(7,11,13); B=sp.Matrix([[2,1,0],[1,4,1],[0,1,3]])
        self.assertEqual(curvature_support_trace_connection_residual(A,Q,K,B),0)

    def test_curvature_support_tensor_is_singularity_safe_and_similarity_neutral(self):
        lam=sp.symbols('lam', positive=True)
        Q=sp.diag(0,2,0); L=sp.diag(3,4,5)
        C=curvature_support_tensor(Q,L)
        self.assertEqual(C,sp.diag(0,32,0))
        self.assertEqual(curvature_support_tensor(lam**2*Q,L/lam),C)

    def test_moving_branch_adds_only_literal_reanchoring_face(self):
        x,y,z=self.coords
        q=sp.Matrix([[x,0,0],[0,2,0],[0,0,3]])
        K=sp.diag(5,6,7); c=sp.Matrix([2,0,0])
        eff=moving_branch_effective_curvature_source(K,q,c,self.coords)
        self.assertEqual(eff,sp.diag(7,6,7))

    def test_moving_branch_pairing_connection_still_cancels(self):
        A=sp.Matrix([[1,2,0],[0,-1,0],[0,0,0]])
        Q=sp.diag(0,2,3); Keff=sp.diag(5,6,7); L=sp.diag(2,3,4)
        Qdot=sp.simplify(-A.T*Q-Q*A+Keff)
        self.assertEqual(moving_branch_curvature_support_residual(A,Q,Qdot,Keff,L),sp.zeros(3))

    def test_one_mode_exact_ns_has_two_persistent_flat_curvature_directions(self):
        A,n=sp.symbols('A n', positive=True)
        c=one_mode_persistent_flat_kernel_calibration(A,n,self.coords,self.t,self.nu)
        self.assertEqual(c['curvature'],sp.diag(0,2*n**2,0))
        self.assertEqual(c['source_curvature'],sp.zeros(3))
        self.assertEqual(c['x_flat_opening'],0)
        self.assertEqual(c['z_flat_opening'],0)
        self.assertEqual(c['covariant_residual'],sp.zeros(3))

    def test_three_mode_referee_is_literal_periodic_ns(self):
        c=three_mode_kernel_birth_calibration(self.coords,self.t,self.nu)
        self.assertEqual(c['ns_residual'],sp.zeros(3,1))
        self.assertEqual(c['enstrophy_balance_residual'],0)

    def test_three_mode_global_quartic_maximum_has_exact_certificate(self):
        cvar=sp.symbols('c', real=True)
        cert=three_mode_kernel_birth_global_certificate(cvar)
        self.assertEqual(cert['upper_factor'],2*(cvar-1)**2*(2*cvar+3))
        self.assertEqual(sp.simplify(cert['derivative_factor']+4*(cvar-1)*(3*cvar+2)),0)
        self.assertEqual(cert['value_at_one'],5)
        self.assertEqual(cert['value_at_minus_one'],-3)
        self.assertEqual(cert['value_at_internal_critical'],-sp.Rational(115,27))
        self.assertGreater(cert['lower_margin_at_internal_critical'],0)

    def test_three_mode_polynomial_is_exact_trig_reduction(self):
        cvar=sp.symbols('c', real=True)
        self.assertEqual(three_mode_kernel_birth_global_polynomial(cvar),-4*cvar**3+2*cvar**2+8*cvar-1)

    def test_quartic_global_maximum_is_second_order_flat(self):
        c=three_mode_kernel_birth_calibration(self.coords,self.t,self.nu)
        self.assertEqual(c['curvature'],sp.zeros(3))
        self.assertEqual(c['quartic_enstrophy_derivative'],-300)
        self.assertEqual(c['max_rate'],0)

    def test_diffusion_endogenously_opens_one_flat_direction(self):
        c=three_mode_kernel_birth_calibration(self.coords,self.t,self.nu)
        self.assertEqual(c['source_curvature'],sp.diag(0,0,24*self.nu))
        self.assertEqual(c['z_kernel_opening'],24*self.nu)
        self.assertEqual(c['z_curvature_opening_rate'],24*self.nu)

    def test_kernel_opening_is_pure_curvature_diffusion_in_referee(self):
        c=three_mode_kernel_birth_calibration(self.coords,self.t,self.nu)
        self.assertEqual(c['stretch_source_curvature'],sp.zeros(3))
        self.assertEqual(c['kelvin_bulk_source_curvature'],sp.zeros(3))
        self.assertEqual(c['curvature_diffusion_source_curvature'],sp.diag(0,0,24*self.nu))
        self.assertEqual(c['source_face_residual'],sp.zeros(3))

    def test_global_normalization_disappears_on_flat_direction(self):
        c=three_mode_kernel_birth_calibration(self.coords,self.t,self.nu)
        self.assertEqual(c['kernel_normalization_residual'],0)

    def test_global_normalization_disappears_matrixwise_on_kernel(self):
        M,md,q=sp.symbols('M md q', nonzero=True)
        Q=sp.diag(0,q,0); P=sp.diag(1,0,1)
        HR=sp.Matrix([[2,1,3],[1,5,4],[3,4,7]])
        K=sp.simplify(-HR/M-(md/M)*Q)
        self.assertEqual(kernel_normalization_compression_residual(HR,Q,M,md,P,K),sp.zeros(3))

    def test_exact_covariant_law_referees_kernel_birth(self):
        c=three_mode_kernel_birth_calibration(self.coords,self.t,self.nu)
        self.assertEqual(c['covariant_residual'],sp.zeros(3))

    def test_psd_right_viability_form_is_positive_at_kernel_birth(self):
        c=three_mode_kernel_birth_calibration(self.coords,self.t,self.nu)
        self.assertEqual(psd_kernel_right_viability_quadratic(c['source_curvature'],sp.Matrix([0,0,1])),24*self.nu)

    def test_kernel_compression_separates_closed_and_still_flat_directions(self):
        c=three_mode_kernel_birth_calibration(self.coords,self.t,self.nu)
        P=sp.eye(3)
        self.assertEqual(kernel_compression(P,c['source_curvature']),sp.diag(0,0,24*self.nu))

    def test_coercive_curvature_pairing_controls_support_trace(self):
        k,a,b,c=sp.symbols('k a b c', positive=True)
        Q=sp.diag(k+a,k+b,k+c); B=sp.diag(2,3,5)
        self.assertEqual(coercive_curvature_support_trace_gap(Q,B,k),2*a+3*b+5*c)


if __name__=='__main__':
    unittest.main()
