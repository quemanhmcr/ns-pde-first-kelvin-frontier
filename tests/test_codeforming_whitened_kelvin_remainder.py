from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.codeforming_surface_moment_tower import (
    codeforming_nonaffinity_field,
    codeforming_nonaffinity_one_form,
    cofactor_map,
    curl3,
)
from src.pde_audit.codeforming_whitened_kelvin_remainder import (
    coordinate_face_flux_vector,
    equal_two_state_covariance,
    equal_two_state_cross_covariance,
    face_error_qv_tensor,
    homogeneous_beta_scale_shape_residual,
    passive_orientation_reparameterization_residual,
    pointwise_orientation_density,
    pointwise_whitening_residual,
    whitened_covariance,
    whitened_covariance_trace_residual,
    whitened_energy_residual,
    whitened_face_error_qv_residual,
    whitened_face_reconstruction,
    whitened_full_covariance_from_blocks,
)
from src.pde_audit.kelvin_packet_locality import metric_from_area_frame
from src.pde_audit.kelvin_shape_generator import cubic_heat_shear_ns_residual


class CodeformingWhitenedKelvinRemainderAudit(unittest.TestCase):
    def test_pointwise_orientation_density_whitening_is_exact_physical_field_defect(self) -> None:
        e=sp.Matrix(sp.symbols('e0:3'))
        H=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        g=pointwise_orientation_density(e,H)
        self.assertEqual(pointwise_whitening_residual(e,H),sp.zeros(3,1))
        self.assertEqual(whitened_face_reconstruction(g,H),e)

    def test_codeforming_beta_curl_whitening_is_exact_vorticity_defect(self) -> None:
        x,y,z,X,Y,Z=sp.symbols('x y z X Y Z')
        L=sp.diag(2,3,5)
        residual=sp.Matrix([y**3,z**3,x**3])
        N=codeforming_nonaffinity_field(residual,sp.zeros(3),(x,y,z),L,(X,Y,Z))
        beta=codeforming_nonaffinity_one_form(N,L)
        H=cofactor_map(L)
        omega_defect=sp.Matrix([
            sp.diff(residual[2],y)-sp.diff(residual[1],z),
            sp.diff(residual[0],z)-sp.diff(residual[2],x),
            sp.diff(residual[1],x)-sp.diff(residual[0],y),
        ]).subs({x:2*X,y:3*Y,z:5*Z})
        self.assertEqual(sp.simplify(H.inv().T*curl3(beta,(X,Y,Z))-omega_defect),sp.zeros(3,1))

    def test_metric_whitened_energy_and_covariance_are_exact_reconstruction_energy(self) -> None:
        e=sp.Matrix(sp.symbols('e0:3'))
        c=sp.symbols('c0:9')
        C=sp.Matrix(3,3,c)
        H=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        self.assertEqual(whitened_energy_residual(e,H),0)
        self.assertEqual(whitened_covariance_trace_residual(C,H),0)
        W=whitened_covariance(C,H)
        self.assertEqual(sp.simplify(sp.trace(W)-sp.trace(C*metric_from_area_frame(H))),0)

    def test_passive_orientation_reparameterization_does_not_change_reconstructed_physical_residual(self) -> None:
        e=sp.Matrix(sp.symbols('e0:3'))
        H=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        R=sp.Matrix([[1,1,0],[0,1,1],[0,0,1]])
        self.assertEqual(passive_orientation_reparameterization_residual(e,H,R),sp.zeros(3,1))

    def test_whitened_error_qv_is_qv_of_reconstructed_anchor_noise_coefficients(self) -> None:
        nu=sp.symbols('nu', positive=True)
        q1=sp.Matrix(sp.symbols('q1_0:3'))
        q2=sp.Matrix(sp.symbols('q2_0:3'))
        H=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        gamma=face_error_qv_tensor([q1,q2],nu)
        self.assertEqual(whitened_face_error_qv_residual([q1,q2],H,nu),sp.zeros(3))
        rhs=2*nu*sum((whitened_face_reconstruction(q,H)*whitened_face_reconstruction(q,H).T for q in [q1,q2]),sp.zeros(3))
        self.assertEqual(sp.simplify(whitened_covariance(gamma,H)-rhs),sp.zeros(3))

    def test_whitened_full_covariance_has_mandatory_local_residual_cross_blocks(self) -> None:
        # Two equally likely coupled states: local and residual are anti-correlated.
        z1=sp.Matrix([1,0]); z2=sp.Matrix([-1,0])
        r1=sp.Matrix([-sp.Rational(1,2),1]); r2=sp.Matrix([sp.Rational(1,2),-1])
        C_z=equal_two_state_covariance(z1,z2)
        C_r=equal_two_state_covariance(r1,r2)
        C_zr=equal_two_state_cross_covariance(z1,z2,r1,r2)
        C_full=equal_two_state_covariance(z1+r1,z2+r2)
        self.assertEqual(whitened_full_covariance_from_blocks(C_z,C_r,C_zr),C_full)
        self.assertNotEqual(C_full,C_z+C_r)
        self.assertNotEqual(C_zr+C_zr.T,sp.zeros(2))

    def test_homogeneous_kelvin_one_form_has_rho_p_plus_one_scale_and_shape_law(self) -> None:
        x,y,z,X,Y,Z,rho,a=sp.symbols('x y z X Y Z rho a', nonzero=True)
        U=sp.Matrix([y**3,z**3,x**3])
        S=sp.diag(a,1,1/a)
        self.assertEqual(
            homogeneous_beta_scale_shape_residual(U,3,(x,y,z),rho,S,(X,Y,Z)),
            sp.zeros(3,1),
        )

    def test_exact_cubic_NS_unit_cube_has_nonzero_finite_reconstruction_at_zero_center_defect(self) -> None:
        y,t,nu=sp.symbols('y t nu')
        self.assertEqual(cubic_heat_shear_ns_residual(y,t,nu),0)
        X,Y,Z=sp.symbols('X Y Z')
        # After subtracting value+linear Taylor part at y=0, beta=(Y^3,0,0).
        beta=sp.Matrix([Y**3,0,0])
        density=curl3(beta,(X,Y,Z))
        eps=coordinate_face_flux_vector(density,(X,Y,Z),(sp.Rational(1,2),)*3)
        self.assertEqual(density,sp.Matrix([0,0,-3*Y**2]))
        self.assertEqual(eps,sp.Matrix([0,0,-sp.Rational(1,4)]))
        H=sp.eye(3)
        reconstructed=whitened_face_reconstruction(eps,H)
        self.assertEqual(reconstructed,eps)
        self.assertNotEqual(reconstructed,sp.zeros(3,1))  # center vorticity defect is zero

    def test_isotropic_cubic_NS_whitened_finite_remainder_is_exact_r_squared(self) -> None:
        r=sp.symbols('r', positive=True)
        X,Y,Z=sp.symbols('X Y Z')
        L=r*sp.eye(3)
        H=cofactor_map(L)
        # Physical residual u_x=y^3 gives N_x=r^2 Y^3 and beta_x=r^4 Y^3.
        N=sp.Matrix([r**2*Y**3,0,0])
        beta=codeforming_nonaffinity_one_form(N,L)
        self.assertEqual(beta,sp.Matrix([r**4*Y**3,0,0]))
        eps=coordinate_face_flux_vector(curl3(beta,(X,Y,Z)),(X,Y,Z),(sp.Rational(1,2),)*3)
        self.assertEqual(eps,sp.Matrix([0,0,-r**4/sp.Integer(4)]))
        reconstructed=whitened_face_reconstruction(eps,H)
        self.assertEqual(reconstructed,sp.Matrix([0,0,-r**2/sp.Integer(4)]))


if __name__=='__main__':
    unittest.main()
