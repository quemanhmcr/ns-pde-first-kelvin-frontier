from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.codeforming_surface_moment_tower import cofactor_map
from src.pde_audit.future_covariance_tensor import codeforming_mean_dyad_backward_source
from src.pde_audit.kelvin_shape_generator import cubic_heat_shear_ns_residual
from src.pde_audit.reverse_codeforming_kelvin_martingale import (
    codeforming_residual_energy_drift,
    constant_mean_bias_rate,
    cross_qv_tensor,
    full_circulation_qv_decomposition_residual,
    incompressible_volume_rate_residual,
    joint_local_residual_qv,
    joint_qv_block_residual,
    normalized_circulation_local_residual_identity_residual,
    orientation_error_to_codeforming_residual_residual,
    physical_pushforward_energy_drift_residual,
    qv_tensor,
    reverse_age_vs_backward_operator_source_residual,
    reverse_codeforming_noise_decomposition_residual,
    reverse_codeforming_residual_noise,
    reverse_codeforming_vorticity_drift_residual,
    reverse_codeforming_vorticity_noise,
    second_moment_minus_covariance_source_residual,
)


class ReverseCodeformingKelvinMartingaleAudit(unittest.TestCase):
    def test_incompressible_reverse_line_frame_preserves_reference_volume(self) -> None:
        a,b,c,d,e,f=sp.symbols('a b c d e f')
        A=sp.Matrix([[a,b,c],[d,e,f],[0,0,-a-e]])
        L=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        self.assertEqual(incompressible_volume_rate_residual(A,L),0)

    def test_orientation_error_is_exactly_J_times_codeforming_physical_residual(self) -> None:
        L=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        eps=sp.Matrix(sp.symbols('eps0:3'))
        self.assertEqual(orientation_error_to_codeforming_residual_residual(L,eps),sp.zeros(3,1))

    def test_normalized_circulation_splits_into_codeforming_local_vorticity_plus_residual(self) -> None:
        L=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        J=sp.det(L); H=cofactor_map(L)
        K=sp.Matrix(sp.symbols('K0:3')); w=sp.Matrix(sp.symbols('w0:3'))
        eps=sp.simplify(K-H.T*w)
        self.assertEqual(normalized_circulation_local_residual_identity_residual(L,K,w,eps),sp.zeros(3,1))
        self.assertEqual(sp.simplify(eps/J-(K/J-L.inv()*w)),sp.zeros(3,1))

    def test_reverse_codeforming_local_vorticity_has_zero_affine_drift(self) -> None:
        a=sp.symbols('a0:9'); A=sp.Matrix(3,3,a)
        L=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        w=sp.Matrix(sp.symbols('w0:3'))
        self.assertEqual(reverse_codeforming_vorticity_drift_residual(A,L,w),sp.zeros(3,1))

    def test_noise_decomposition_is_exact_after_codeforming_and_volume_normalization(self) -> None:
        L=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        G=sp.Matrix(3,3,sp.symbols('g0:9'))
        AK=sp.Matrix(3,3,sp.symbols('ak0:9'))
        J=sp.det(L); H=cofactor_map(L)
        Q=sp.simplify(AK-H.T*G)
        self.assertEqual(reverse_codeforming_noise_decomposition_residual(AK,Q,L,G),sp.zeros(3))
        self.assertEqual(sp.simplify(AK/J-(L.inv()*G+Q/J)),sp.zeros(3))

    def test_joint_eta_chi_qv_is_one_full_gram_with_mandatory_cross_blocks(self) -> None:
        nu=sp.symbols('nu', positive=True)
        G=sp.Matrix(3,3,sp.symbols('g0:9')); Q=sp.Matrix(3,3,sp.symbols('q0:9'))
        Gamma=joint_local_residual_qv(G,Q,nu)
        self.assertEqual(joint_qv_block_residual(G,Q,nu),sp.zeros(6))
        self.assertEqual(sp.simplify(Gamma-Gamma.T),sp.zeros(6))
        self.assertNotEqual(cross_qv_tensor(G,Q,nu),sp.zeros(3))
        self.assertEqual(full_circulation_qv_decomposition_residual(G,Q,nu),sp.zeros(3))

    def test_codeforming_residual_energy_has_only_positive_qv_and_physical_strain_is_metric_work(self) -> None:
        nu=sp.symbols('nu', positive=True)
        A=sp.Matrix([[1,2,0],[3,-1,0],[0,0,0]])
        L=sp.Matrix([[2,1,0],[0,1,0],[0,0,1]])
        chi=sp.Matrix(sp.symbols('c0:3')); Q=sp.Matrix(3,3,sp.symbols('q0:9'))
        self.assertEqual(
            codeforming_residual_energy_drift(Q,nu),
            nu*sum(e**2 for e in Q),
        )
        self.assertEqual(physical_pushforward_energy_drift_residual(A,L,chi,Q,nu),0)

    def test_constant_mean_bias_is_separate_from_covariance_growth(self) -> None:
        nu=sp.symbols('nu', positive=True)
        Q=sp.Matrix(3,3,sp.symbols('q0:9'))
        self.assertEqual(constant_mean_bias_rate(),0)
        self.assertEqual(second_moment_minus_covariance_source_residual(Q,nu),sp.zeros(3))
        self.assertNotEqual(qv_tensor(Q,nu),sp.zeros(3))

    def test_reverse_age_qv_source_is_opposite_sign_of_existing_backward_physical_time_mean_dyad_source(self) -> None:
        nu=sp.symbols('nu', positive=True)
        F=sp.Matrix([[2,1,0],[0,2,1],[1,0,1]])
        G=sp.Matrix(3,3,sp.symbols('g0:9'))
        reverse_noise=sp.simplify(F.inv()*G)
        reverse_source=qv_tensor(reverse_noise,nu)
        backward_source=codeforming_mean_dyad_backward_source(F,G,nu)
        self.assertEqual(reverse_age_vs_backward_operator_source_residual(reverse_source,backward_source),sp.zeros(3))

    def test_exact_cubic_NS_codeforming_bias_is_nonzero_constant_with_zero_qv(self) -> None:
        y,t,nu=sp.symbols('y t nu')
        self.assertEqual(cubic_heat_shear_ns_residual(y,t,nu),0)
        chi=sp.Matrix([0,0,-sp.Rational(1,4)])
        Q=sp.zeros(3)
        self.assertNotEqual(chi,sp.zeros(3,1))
        self.assertEqual(constant_mean_bias_rate(),0)
        self.assertEqual(qv_tensor(Q,nu),sp.zeros(3))
        self.assertEqual(codeforming_residual_energy_drift(Q,nu),0)

    def test_exact_one_mode_full_period_face_has_complete_local_residual_qv_cancellation(self) -> None:
        y,t,nu,k,a=sp.symbols('y t nu k a', positive=True)
        alpha=nu*k**2
        U=sp.exp(-alpha*t)*sp.cos(k*y)
        omega_z=-sp.diff(U,y)
        # Coherent box line lengths lx=2a, ly=2pi/k, lz=1.  The xy face spans one full y-period.
        L=sp.diag(2*a,2*sp.pi/k,1)
        J=sp.det(L)
        b=sp.pi/k
        Kz=sp.simplify(2*a*sp.integrate(-sp.diff(U,y),(y,y-b,y+b)))
        # Avoid dummy-limit shadowing: direct periodic endpoint form is exactly zero.
        Y=sp.symbols('Y', real=True)
        UY=lambda yy: sp.exp(-alpha*t)*sp.cos(k*yy)
        Kz_direct=sp.simplify(-2*a*(UY(Y+b)-UY(Y-b)))
        self.assertEqual(sp.trigsimp(Kz_direct),0)
        eta=sp.simplify((-sp.diff(UY(Y),Y))/L[2,2])
        chi=sp.simplify(Kz_direct/J-eta)
        self.assertEqual(sp.simplify(chi+eta),0)
        geta=sp.diff(eta,Y)
        qchi=sp.diff(chi,Y)
        self.assertEqual(sp.simplify(qchi+geta),0)
        gamma_local=sp.simplify(2*nu*geta**2)
        gamma_res=sp.simplify(2*nu*qchi**2)
        gamma_cross=sp.simplify(2*nu*geta*qchi)
        self.assertEqual(sp.simplify(gamma_cross+gamma_local),0)
        self.assertEqual(sp.simplify(gamma_res-gamma_local),0)
        self.assertEqual(sp.simplify(gamma_local+gamma_res+2*gamma_cross),0)
        self.assertNotEqual(gamma_local,0)
        self.assertNotEqual(gamma_cross,0)


if __name__=='__main__':
    unittest.main()
