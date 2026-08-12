from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.dynamic_reconstructed_kelvin_residual import (
    actual_area_mismatch_rate,
    full_qv_block_decomposition_residual,
    full_dyad_block_decomposition_residual,
    full_reconstructed_noise_decomposition_residual,
    geometry_mismatch_flux_drift,
    inverse_transpose_connection_residual,
    local_error_noise_transfer_residual,
    local_frame_kelvin_error_noise,
    local_residual_cross_dyad_drift,
    local_residual_cross_qv,
    local_vorticity_flux_drift_residual,
    local_vorticity_flux_noise_matrix,
    noise_qv_tensor,
    reconstructed_kelvin_noise,
    reconstructed_residual_drift,
    reconstructed_residual_dyad_drift,
    reconstructed_residual_energy_drift,
    reconstructed_residual_qv,
    shape_drift_transfer_residual,
)
from src.pde_audit.finite_shape_kelvin_descent import (
    one_mode_shear_rectangle_error_mean,
    one_mode_shear_rectangle_error_variance,
)
from src.pde_audit.kelvin_shape_generator import cubic_heat_shear_ns_residual


class DynamicReconstructedKelvinResidualAudit(unittest.TestCase):
    def test_reverse_local_frame_reconstruction_has_exact_minus_A_connection(self) -> None:
        a=sp.symbols('a0:9')
        h=sp.symbols('h0:9')
        A=sp.Matrix(3,3,a)
        H=sp.Matrix(3,3,h)
        self.assertEqual(inverse_transpose_connection_residual(A,H),sp.zeros(3))

    def test_local_Nanson_vorticity_flux_has_zero_reverse_age_drift(self) -> None:
        a=sp.symbols('a0:9')
        h=sp.symbols('h0:9')
        w=sp.Matrix(sp.symbols('w0:3'))
        A=sp.Matrix(3,3,a); H=sp.Matrix(3,3,h)
        self.assertEqual(local_vorticity_flux_drift_residual(A,H,w),sp.zeros(3,1))

    def test_actual_area_shape_drift_transfers_exactly_into_geometry_mismatch(self) -> None:
        A=sp.Matrix([[1,2,0],[3,-1,0],[0,0,0]])
        omega=sp.Matrix(sp.symbols('w0:3'))
        hR=sp.Matrix(sp.symbols('hR0:3'))
        h=sp.Matrix(sp.symbols('h0:3'))
        RA=sp.Matrix(sp.symbols('R0:3'))
        self.assertEqual(shape_drift_transfer_residual(A,omega,hR,h,RA),0)
        self.assertEqual(
            sp.simplify(geometry_mismatch_flux_drift(A,omega,hR,h,RA)-(omega.T*RA)[0]),0
        )
        self.assertEqual(actual_area_mismatch_rate(A,hR,h,RA),sp.simplify(A.T*(hR-h)+RA))

    def test_noise_transfer_matches_drift_transfer_for_one_physical_face(self) -> None:
        g=sp.symbols('g0:9')
        grad=sp.Matrix(3,3,g)
        hR=sp.Matrix(sp.symbols('hR0:3')); h=sp.Matrix(sp.symbols('h0:3'))
        arow=sp.Matrix(1,3,sp.symbols('ak0:3'))
        self.assertEqual(local_error_noise_transfer_residual(arow,grad,hR,h),sp.zeros(1,3))

    def test_reconstructed_residual_SDE_has_line_connection_and_reconstructed_qv(self) -> None:
        nu=sp.symbols('nu', positive=True)
        A=sp.Matrix([[1,2,0],[3,-1,0],[0,0,0]])
        H=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        r=sp.Matrix(sp.symbols('r0:3'))
        Q=sp.Matrix(3,3,sp.symbols('q0:9'))
        qhat=reconstructed_kelvin_noise(Q,H)
        self.assertEqual(reconstructed_residual_drift(A,r),-A*r)
        self.assertEqual(reconstructed_residual_qv(Q,H,nu),noise_qv_tensor(qhat,nu))

    def test_residual_dyad_and_energy_drift_are_same_physical_strain_plus_qv(self) -> None:
        nu=sp.symbols('nu', positive=True)
        A=sp.Matrix([[1,2,0],[3,-1,0],[0,0,0]])
        r=sp.Matrix(sp.symbols('r0:3'))
        Q=sp.Matrix(3,3,sp.symbols('q0:9'))
        dyad=reconstructed_residual_dyad_drift(A,r,Q,nu)
        energy=reconstructed_residual_energy_drift(A,r,Q,nu)
        self.assertEqual(sp.simplify(sp.trace(dyad)/2-energy),0)

    def test_local_residual_cross_qv_is_mandatory_in_full_reconstructed_qv(self) -> None:
        nu=sp.symbols('nu', positive=True)
        H=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        G=sp.Matrix(3,3,sp.symbols('g0:9'))
        Afin=sp.Matrix(3,3,sp.symbols('ak0:9'))
        self.assertEqual(full_reconstructed_noise_decomposition_residual(Afin,H,G),sp.zeros(3))
        self.assertEqual(full_qv_block_decomposition_residual(Afin,H,G,nu),sp.zeros(3))
        Q=local_frame_kelvin_error_noise(Afin,H,G)
        qhat=reconstructed_kelvin_noise(Q,H)
        cross=local_residual_cross_qv(G,qhat,nu)
        self.assertNotEqual(cross,sp.zeros(3))

    def test_full_reconstructed_dyad_dynamics_requires_both_cross_blocks(self) -> None:
        nu=sp.symbols('nu', positive=True)
        A=sp.Matrix([[1,2,0],[3,-1,0],[0,0,0]])
        omega=sp.Matrix(sp.symbols('w0:3')); r=sp.Matrix(sp.symbols('r0:3'))
        G=sp.Matrix(3,3,sp.symbols('g0:9')); Q=sp.Matrix(3,3,sp.symbols('q0:9'))
        self.assertEqual(
            full_dyad_block_decomposition_residual(A,omega,r,G,Q,nu),
            sp.zeros(3),
        )
        cross=local_residual_cross_dyad_drift(A,omega,r,G,Q,nu)
        self.assertNotEqual(sp.simplify(cross+cross.T),sp.zeros(3))

    def test_cross_dyad_drift_contains_signed_cross_qv_source(self) -> None:
        nu=sp.symbols('nu', positive=True)
        A=sp.Matrix([[1,2,0],[3,-1,0],[0,0,0]])
        omega=sp.Matrix(sp.symbols('w0:3')); r=sp.Matrix(sp.symbols('r0:3'))
        G=sp.Matrix(3,3,sp.symbols('g0:9')); Q=sp.Matrix(3,3,sp.symbols('q0:9'))
        drift=local_residual_cross_dyad_drift(A,omega,r,G,Q,nu)
        M=omega*r.T
        expected=sp.simplify(-A*M-M*A.T+2*nu*G*Q.T)
        self.assertEqual(sp.simplify(drift-expected),sp.zeros(3))

    def test_exact_cubic_NS_has_nonzero_reconstructed_bias_with_zero_drift_and_qv_in_blind_direction(self) -> None:
        y,t,nu=sp.symbols('y t nu')
        self.assertEqual(cubic_heat_shear_ns_residual(y,t,nu),0)
        # Centered xy square unit side: reconstructed residual is -e_z/4.
        r=sp.Matrix([0,0,-sp.Rational(1,4)])
        # At y=0 the cubic heat-shear gradient has only A_xy=6nu t, which annihilates e_z.
        A=sp.Matrix([[0,6*nu*t,0],[0,0,0],[0,0,0]])
        Q=sp.zeros(3)
        self.assertEqual(reconstructed_residual_drift(A,r),sp.zeros(3,1))
        self.assertEqual(reconstructed_residual_qv(Q,sp.eye(3),nu),sp.zeros(3))
        self.assertEqual(reconstructed_residual_energy_drift(A,r,Q,nu),0)

    def test_exact_one_mode_NS_local_residual_cross_qv_is_generically_nonzero(self) -> None:
        y,t,nu,k,a,b=sp.symbols('y t nu k a b', positive=True)
        alpha=nu*k**2
        U=sp.exp(-alpha*t)*sp.cos(k*y)
        eps=one_mode_shear_rectangle_error_mean(y,t,a,b,nu,k)
        # omega_z=-U_y, so the only local Brownian response is partial_y omega_z=-U_yy.
        G=sp.zeros(3); G[2,1]=-sp.diff(U,y,2)
        Q=sp.zeros(3); Q[2,1]=sp.diff(eps,y)
        cross=local_residual_cross_qv(G,Q,nu)
        expected=sp.zeros(3); expected[2,2]=sp.simplify(2*nu*(-sp.diff(U,y,2))*sp.diff(eps,y))
        self.assertEqual(sp.trigsimp(sp.simplify(cross-expected)),sp.zeros(3))
        self.assertNotEqual(sp.simplify(expected[2,2]),0)

    def test_exact_one_mode_NS_reconstructed_residual_is_pure_martingale_in_ez_face(self) -> None:
        y,t,h,nu,k,a,b=sp.symbols('y t h nu k a b', positive=True)
        alpha=nu*k**2
        U=sp.exp(-alpha*t)*sp.cos(k*y)
        A=sp.Matrix([[0,sp.diff(U,y),0],[0,0,0],[0,0,0]])
        mean_err=one_mode_shear_rectangle_error_mean(y,t,a,b,nu,k)
        r=sp.Matrix([0,0,mean_err])
        self.assertEqual(reconstructed_residual_drift(A,r),sp.zeros(3,1))
        # Exact finite-horizon variance already audited; its h derivative at zero equals qv rate.
        V=one_mode_shear_rectangle_error_variance(y,t,h,a,b,nu,k)
        q0=sp.diff(mean_err,y)
        leading=sp.simplify(sp.diff(V,h).subs(h,0)-2*nu*q0**2)
        self.assertEqual(sp.trigsimp(leading),0)


if __name__=='__main__':
    unittest.main()
