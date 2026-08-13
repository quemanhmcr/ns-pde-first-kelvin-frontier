import unittest
import sympy as sp

from src.pde_audit.directional_refinement_kelvin_residual import (
    directional_bias_spread_terms,
    directional_weighted_energy_residual,
    ensemble_event_three_face_residual,
    ensemble_event_three_faces,
    homogeneous_isotropic_refinement_residual,
    midpoint_revaluation_faces,
    midpoint_revaluation_residual,
    passive_midpoint_face_sum_residual,
    passive_reparameterization_energy_residual,
    quadratic_long_support_calibration,
    reverse_material_weighted_energy_rate_residual,
    right_refinement_metric_residual,
    scale_shape_smooth_rate_residual,
    spectral_metric,
    weighted_energy,
)


class DirectionalRefinementKelvinResidualAudit(unittest.TestCase):
    def test_principal_line_decomposition_is_exact_direction_by_direction(self) -> None:
        V=sp.Matrix([[sp.Rational(3,5),-sp.Rational(4,5),0],[sp.Rational(4,5),sp.Rational(3,5),0],[0,0,1]])
        s20,s21,s22=sp.symbols('s2_0 s2_1 s2_2', positive=True)
        s2=(s20,s21,s22)
        q=sp.symbols('q0:6')
        Q=sp.Matrix([[q[0],q[1],q[2]],[q[1],q[3],q[4]],[q[2],q[4],q[5]]])
        self.assertEqual(V.T*V,sp.eye(3))
        self.assertEqual(directional_weighted_energy_residual(Q,V,s2),0)

    def test_principal_direction_terms_split_bias_and_spread_without_norm_estimate(self) -> None:
        V=sp.eye(3)
        s20,s21,s22=sp.symbols('s2_0 s2_1 s2_2', positive=True)
        s2=(s20,s21,s22)
        m=sp.Matrix(sp.symbols('m0:3'))
        C=sp.diag(*sp.symbols('c0:3', nonnegative=True))
        terms=directional_bias_spread_terms(m,C,V,s2)
        self.assertEqual(terms,[sp.simplify(s2[i]*(m[i]**2+C[i,i])) for i in range(3)])
        Q=sp.simplify(C+m*m.T)
        self.assertEqual(sp.simplify(sum(terms)-weighted_energy(spectral_metric(V,s2),Q)),0)

    def test_repo_right_refinement_convention_pushes_metric_by_congruence(self) -> None:
        a=sp.symbols('a0:9')
        r=sp.symbols('r0:9')
        L=sp.Matrix(3,3,a)
        R=sp.Matrix(3,3,r)
        self.assertEqual(right_refinement_metric_residual(L,R),sp.zeros(3))

    def test_finite_event_midpoint_split_has_geometry_and_state_faces_exactly(self) -> None:
        a=sp.symbols('a0:6')
        b=sp.symbols('b0:6')
        c=sp.symbols('c0:6')
        d=sp.symbols('d0:6')
        Mm=sp.Matrix([[a[0],a[1],a[2]],[a[1],a[3],a[4]],[a[2],a[4],a[5]]])
        Qm=sp.Matrix([[b[0],b[1],b[2]],[b[1],b[3],b[4]],[b[2],b[4],b[5]]])
        Mp=sp.Matrix([[c[0],c[1],c[2]],[c[1],c[3],c[4]],[c[2],c[4],c[5]]])
        Qp=sp.Matrix([[d[0],d[1],d[2]],[d[1],d[3],d[4]],[d[2],d[4],d[5]]])
        self.assertEqual(midpoint_revaluation_residual(Mm,Qm,Mp,Qp),0)

    def test_passive_GL_reparameterization_has_nonzero_faces_but_zero_total_revaluation(self) -> None:
        M=sp.diag(2,3,5)
        Q=sp.Matrix([[1,1,0],[1,2,0],[0,0,1]])
        R=sp.Matrix([[1,1,0],[0,1,0],[0,0,1]])
        self.assertEqual(passive_reparameterization_energy_residual(M,Q,R),0)
        g,s=midpoint_revaluation_faces(M,Q,R.T*M*R,R.inv()*Q*R.inv().T)
        self.assertNotEqual(g,0)
        self.assertNotEqual(s,0)
        self.assertEqual(sp.simplify(g+s),0)
        self.assertEqual(passive_midpoint_face_sum_residual(M,Q,R),0)

    def test_full_random_frame_event_has_third_correlation_revaluation_face(self) -> None:
        Mm=sp.eye(3); Qm=sp.diag(1,0,0); cm=sp.Integer(0)
        Mp=sp.diag(4,1,1); Qp=sp.diag(2,0,0); cp=sp.Rational(3,4)
        g,s,c=ensemble_event_three_faces(Mm,Qm,cm,Mp,Qp,cp)
        self.assertEqual(g,sp.Rational(9,2))
        self.assertEqual(s,sp.Rational(5,2))
        self.assertEqual(c,sp.Rational(3,4))
        self.assertEqual(ensemble_event_three_face_residual(Mm,Qm,cm,Mp,Qp,cp),0)

    def test_smooth_scale_shape_current_product_rule_is_exact(self) -> None:
        rho,rhodot=sp.symbols('rho rhodot', nonzero=True)
        q=sp.symbols('q0:9'); qd=sp.symbols('qd0:9'); a=sp.symbols('a0:9'); ad=sp.symbols('ad0:9')
        Q=sp.Matrix(3,3,q); Qd=sp.Matrix(3,3,qd); A=sp.Matrix(3,3,a); Ad=sp.Matrix(3,3,ad)
        self.assertEqual(scale_shape_smooth_rate_residual(Q,Qd,rho,rhodot,A,Ad),0)

    def test_reverse_material_smooth_law_is_strain_work_plus_qv_content(self) -> None:
        a=sp.symbols('a0:9'); l=sp.symbols('l0:9'); q=sp.symbols('q0:9'); b=sp.symbols('b0:6'); nu=sp.symbols('nu')
        A=sp.Matrix(3,3,a); L=sp.Matrix(3,3,l); Q=sp.Matrix(3,3,q); B=sp.Matrix(3,2,b)
        self.assertEqual(reverse_material_weighted_energy_rate_residual(A,L,Q,B,nu),0)

    def test_homogeneous_isotropic_refinement_has_exact_2p_minus_2_weight(self) -> None:
        lam=sp.symbols('lam')
        M=sp.Matrix([[2,1],[1,3]])
        Q=sp.Matrix([[5,2],[2,4]])
        for p in range(2,8):
            self.assertEqual(homogeneous_isotropic_refinement_residual(M,Q,lam,p),0)

    def test_exact_quadratic_NS_weighted_descent_does_not_imply_support_locality(self) -> None:
        y,t,nu,rho=sp.symbols('y t nu rho', positive=True)
        cal=quadratic_long_support_calibration(y,t,nu,rho)
        self.assertEqual(cal['epsilon_z'],-rho**2)
        self.assertEqual(cal['chi'],sp.Matrix([0,0,-1]))
        self.assertEqual(cal['physical_residual'],sp.Matrix([0,0,-rho]))
        self.assertEqual(cal['physical_energy'],rho**2)
        self.assertEqual(cal['long_x_line_squared'],1)
        self.assertEqual(sp.limit(cal['physical_energy'],rho,0,dir='+'),0)
        # The x support line stays exactly length one, so the packet is not local.
        self.assertEqual(cal['line_frame'][0,0],1)


if __name__ == '__main__':
    unittest.main()
