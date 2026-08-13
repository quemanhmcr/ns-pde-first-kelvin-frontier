import unittest
import sympy as sp

from src.pde_audit.weighted_codeforming_kelvin_residual import (
    asymmetric_square_codeforming_residual,
    homogeneous_weighted_exponent_residual,
    isotropic_physical_residual_from_scalar_chi,
    one_mode_asymmetric_codeforming_noise,
    one_mode_asymmetric_codeforming_residual,
    one_mode_shear,
    physical_residual,
    quadratic_asymmetric_square_exact_residual,
    quadratic_heat_shear_residual,
    residual_second_moment,
    weighted_bias_energy,
    weighted_bias_spread_residual,
    weighted_qv_trace_residual,
    weighted_second_moment_energy,
    weighted_spread_energy,
    two_state_metric_residual_correlation,
    two_state_metric_residual_decomposition_residual,
    two_state_mean_metric_mean_second_moment,
    two_state_weighted_energy,
)


class WeightedCodeformingKelvinResidualAudit(unittest.TestCase):
    def test_weighted_second_moment_is_exact_bias_plus_spread(self) -> None:
        a=sp.symbols('a0:9')
        L=sp.Matrix(3,3,a)
        m=sp.Matrix(sp.symbols('m0:3'))
        c=sp.symbols('c0:6')
        C=sp.Matrix([[c[0],c[1],c[2]],[c[1],c[3],c[4]],[c[2],c[4],c[5]]])
        self.assertEqual(weighted_bias_spread_residual(m,C,L),0)
        Q=residual_second_moment(m,C)
        self.assertEqual(
            sp.simplify(weighted_second_moment_energy(m,C,L)-sp.trace(Q*L.T*L)),0
        )

    def test_weighted_bias_is_literal_squared_physical_mean_residual(self) -> None:
        L=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        m=sp.Matrix(sp.symbols('m0:3'))
        r=physical_residual(L,m)
        self.assertEqual(sp.simplify(weighted_bias_energy(m,L)-r.dot(r)),0)

    def test_weighted_spread_is_literal_physical_covariance_trace(self) -> None:
        L=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        c=sp.symbols('c0:6')
        C=sp.Matrix([[c[0],c[1],c[2]],[c[1],c[3],c[4]],[c[2],c[4],c[5]]])
        self.assertEqual(
            sp.simplify(weighted_spread_energy(C,L)-sp.trace(L*C*L.T)),0
        )

    def test_random_frame_requires_metric_residual_cross_correlation(self) -> None:
        L1=sp.diag(2,1,1)
        L2=sp.eye(3)
        c1=sp.Matrix([1,0,0])
        c2=sp.zeros(3,1)
        exact=two_state_weighted_energy(L1,c1,L2,c2)
        fact=two_state_mean_metric_mean_second_moment(L1,c1,L2,c2)
        mixed=two_state_metric_residual_correlation(L1,c1,L2,c2)
        self.assertEqual(exact,2)
        self.assertEqual(fact,sp.Rational(5,4))
        self.assertEqual(mixed,sp.Rational(3,4))
        self.assertNotEqual(exact,fact)
        self.assertEqual(two_state_metric_residual_decomposition_residual(L1,c1,L2,c2),0)

    def test_random_frame_cross_face_can_be_signed(self) -> None:
        # Swapping which replica carries the larger residual reverses the mixed face.
        L1=sp.diag(2,1,1)
        L2=sp.eye(3)
        c1=sp.zeros(3,1)
        c2=sp.Matrix([1,0,0])
        self.assertEqual(two_state_metric_residual_correlation(L1,c1,L2,c2),-sp.Rational(3,4))

    def test_weighted_qv_is_literal_physical_reconstructed_qv(self) -> None:
        nu=sp.symbols('nu')
        L=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        q=sp.symbols('q0:6')
        Q=sp.Matrix(3,2,q)
        self.assertEqual(weighted_qv_trace_residual(L,Q,nu),0)

    def test_quadratic_heat_shear_is_exact_navier_stokes_shear(self) -> None:
        y,t,nu=sp.symbols('y t nu')
        self.assertEqual(quadratic_heat_shear_residual(y,t,nu),0)

    def test_exact_quadratic_NS_raw_chi_bias_stays_nonzero_while_physical_residual_shrinks(self) -> None:
        y,t,nu,rho=sp.symbols('y t nu rho', positive=True)
        eps,chi,r=quadratic_asymmetric_square_exact_residual(y,t,nu,rho)
        self.assertEqual(sp.simplify(eps+rho**3),0)
        self.assertEqual(chi,-1)
        self.assertEqual(r,-rho)
        self.assertEqual(sp.limit(chi,rho,0,dir='+'),-1)
        self.assertEqual(sp.limit(r,rho,0,dir='+'),0)
        self.assertEqual(weighted_bias_energy(sp.Matrix([0,0,chi]),rho*sp.eye(3)),rho**2)

    def test_one_mode_exact_NS_raw_chi_has_nonzero_quadratic_jet_limit(self) -> None:
        y,t,nu,k,rho=sp.symbols('y t nu k rho', positive=True)
        U=one_mode_shear(y,t,nu,k)
        chi=one_mode_asymmetric_codeforming_residual(y,t,rho,nu,k)
        expected=-sp.diff(U,y,2)/2
        self.assertEqual(sp.simplify(sp.limit(chi,rho,0,dir='+')-expected),0)

    def test_one_mode_exact_NS_raw_noise_can_stay_nonzero_while_physical_noise_shrinks(self) -> None:
        y,t,nu,k,rho=sp.symbols('y t nu k rho', positive=True)
        U=one_mode_shear(y,t,nu,k)
        qchi=one_mode_asymmetric_codeforming_noise(y,t,rho,nu,k)
        expected=-sp.diff(U,y,3)/2
        self.assertEqual(sp.simplify(sp.limit(qchi,rho,0,dir='+')-expected),0)
        qr=isotropic_physical_residual_from_scalar_chi(qchi,rho)
        self.assertEqual(sp.simplify(sp.limit(qr,rho,0,dir='+')),0)

    def test_homogeneous_degree_p_weighted_physical_exponent_is_2p_minus_2(self) -> None:
        rho,a=sp.symbols('rho a')
        for p in range(2,8):
            self.assertEqual(homogeneous_weighted_exponent_residual(rho,p,a),0)

    def test_raw_codeforming_bias_and_spread_are_not_physical_descent_targets(self) -> None:
        y,t,nu,k,rho=sp.symbols('y t nu k rho', positive=True)
        chi=one_mode_asymmetric_codeforming_residual(y,t,rho,nu,k)
        qchi=one_mode_asymmetric_codeforming_noise(y,t,rho,nu,k)
        # Both can have O(1) nonzero limits, while multiplying by the physical
        # line frame rho sends their physical reconstructed versions to zero.
        self.assertNotEqual(sp.simplify(sp.limit(chi,rho,0,dir='+')),0)
        self.assertNotEqual(sp.simplify(sp.limit(qchi,rho,0,dir='+')),0)
        self.assertEqual(sp.limit(rho*chi,rho,0,dir='+'),0)
        self.assertEqual(sp.limit(rho*qchi,rho,0,dir='+'),0)


if __name__ == '__main__':
    unittest.main()
