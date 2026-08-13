import unittest
import sympy as sp

from src.pde_audit.principal_kelvin_residual_channels import (
    degenerate_basis_rotation_residual,
    degenerate_eigenspace_energy,
    orthogonal_directional_channels,
    principal_channel_rate_faces,
    principal_channel_rate_sum_residual,
    principal_metric_rate_reconstruction_residual,
    principal_mixing_offdiagonal_residual,
    projector_channel_decomposition_residual,
    reverse_linear_shear_metric_rate,
    simple_spectrum_connection,
    simple_spectrum_connection_skew_residual,
    two_replica_pathwise_channel_residual,
)


class PrincipalKelvinResidualChannelsAudit(unittest.TestCase):
    def test_pathwise_projector_channels_reconstruct_weighted_energy_exactly(self) -> None:
        P1=sp.diag(1,0,0); P2=sp.diag(0,1,0); P3=sp.diag(0,0,1)
        lam=(sp.Integer(1),sp.Integer(4),sp.Integer(9))
        M=sp.diag(*lam)
        Q=sp.Matrix([[2,1,0],[1,3,1],[0,1,5]])
        self.assertEqual(projector_channel_decomposition_residual(M,Q,[P1,P2,P3],lam),0)

    def test_random_replica_channel_sum_keeps_geometry_residual_correlation_pathwise(self) -> None:
        V1=sp.eye(3)
        V2=sp.Matrix([[0,1,0],[1,0,0],[0,0,1]])
        l1=(1,4,9); l2=(2,5,7)
        Q1=sp.diag(3,1,2)
        Q2=sp.Matrix([[1,sp.Rational(1,2),0],[sp.Rational(1,2),4,0],[0,0,2]])
        self.assertEqual(two_replica_pathwise_channel_residual(V1,l1,Q1,V2,l2,Q2),0)

    def test_nonnegative_principal_channels_are_literal_products_not_max_norm_bounds(self) -> None:
        V=sp.eye(3); lam=(1,4,9); Q=sp.diag(2,3,5)
        self.assertEqual(orthogonal_directional_channels(V,lam,Q),[2,12,45])

    def test_simple_spectrum_connection_is_skew_and_reconstructs_metric_rate(self) -> None:
        b12,b13,b23=sp.symbols('b12 b13 b23')
        B=sp.Matrix([[2,b12,b13],[b12,-1,b23],[b13,b23,3]])
        lam=(1,4,9)
        self.assertEqual(simple_spectrum_connection_skew_residual(B,lam),sp.zeros(3))
        self.assertEqual(principal_metric_rate_reconstruction_residual(B,lam),sp.zeros(3))

    def test_principal_channel_rate_splits_stretch_content_and_axis_mixing_exactly(self) -> None:
        B=sp.Matrix([[2,3,1],[3,-1,2],[1,2,4]])
        lam=(1,4,9)
        Q=sp.Matrix([[5,2,1],[2,3,sp.Rational(1,2)],[1,sp.Rational(1,2),4]])
        Qdot=sp.Matrix([[1,2,0],[2,3,1],[0,1,-2]])
        self.assertEqual(principal_channel_rate_sum_residual(B,lam,Q,Qdot),0)
        self.assertEqual(principal_mixing_offdiagonal_residual(B,lam,Q),0)

    def test_exact_linear_NS_shear_activates_eigenframe_mixing_face(self) -> None:
        gamma,q=sp.symbols('gamma q', nonzero=True)
        L=sp.diag(2,1,3)
        B=reverse_linear_shear_metric_rate(gamma,L)
        lam=(4,1,9)
        Omega=simple_spectrum_connection(B,lam)
        self.assertEqual(B,sp.Matrix([[0,-2*gamma,0],[-2*gamma,0,0],[0,0,0]]))
        self.assertEqual(Omega[0,1],sp.Rational(2,3)*gamma)
        self.assertEqual(Omega[1,0],-sp.Rational(2,3)*gamma)
        Q=sp.Matrix([[1,q,0],[q,2,0],[0,0,3]])
        stretch,content,mixing=principal_channel_rate_faces(B,lam,Q,sp.zeros(3))
        self.assertEqual(stretch,[0,0,0])
        self.assertEqual(content,[0,0,0])
        self.assertEqual(sp.simplify(sum(mixing)+4*gamma*q),0)
        self.assertNotEqual(mixing[0],0)
        self.assertNotEqual(mixing[1],0)

    def test_offdiagonal_metric_work_is_exactly_eigenframe_mixing_traffic(self) -> None:
        B=sp.Matrix([[0,2,0],[2,0,3],[0,3,0]])
        lam=(1,4,9)
        Q=sp.Matrix([[1,5,0],[5,2,7],[0,7,3]])
        _,_,mixing=principal_channel_rate_faces(B,lam,Q,sp.zeros(3))
        expected=2*(2*5+3*7)
        self.assertEqual(sp.simplify(sum(mixing)-expected),0)

    def test_degenerate_eigenspace_energy_is_basis_gauge_invariant(self) -> None:
        B=sp.Matrix([[1,0],[0,1],[0,0]])
        R=sp.Matrix([[sp.Rational(3,5),-sp.Rational(4,5)],[sp.Rational(4,5),sp.Rational(3,5)]])
        Q=sp.Matrix([[2,1,3],[1,5,2],[3,2,7]])
        self.assertEqual(R.T*R,sp.eye(2))
        self.assertEqual(degenerate_basis_rotation_residual(B,R,4,Q),0)
        self.assertEqual(degenerate_eigenspace_energy(B,4,Q),28)

    def test_simple_spectrum_formula_is_not_used_at_degeneracy(self) -> None:
        # The projector block remains meaningful when lambda1=lambda2; individual
        # eigenvector angular velocity is gauge-dependent and the denominator vanishes.
        B=sp.Matrix([[0,1,0],[1,0,0],[0,0,0]])
        with self.assertRaises(ValueError):
            simple_spectrum_connection(B,(1,1,4))


if __name__ == '__main__':
    unittest.main()
