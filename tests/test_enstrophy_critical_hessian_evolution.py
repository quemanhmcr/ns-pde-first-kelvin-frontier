from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.enstrophy_critical_hessian_evolution import (
    abc_hessian_logdet_calibration,
    critical_hessian_evolution_faces_at,
    determinant_jacobi_residual,
    hessian_connection_logdet_divergence_residual,
    hessian_connection_strain_rotation_residual,
    hessian_strain_rotation_logdet_rates,
    hessian_connection_logdet_rate,
    hessian_logdet_face_rates,
    hessian_logdet_rate,
    nonzero_determinant_from_lograte,
)


class EnstrophyCriticalHessianEvolutionAudit(unittest.TestCase):
    def setUp(self) -> None:
        self.x,self.y,self.z,self.t=sp.symbols('x y z t', real=True)
        self.coords=(self.x,self.y,self.z)
        self.nu=sp.symbols('nu', positive=True)

    def test_generic_moving_quadratic_critical_branch_hessian_evolution_closes_exactly(self) -> None:
        a,b,c1,c2,c3=sp.symbols('a b c1 c2 c3')
        e=-(self.x-a*self.t)**2-2*(self.y-b*self.t)**2-3*self.z**2
        u=sp.Matrix([c1,c2,c3])
        source=sp.simplify(sp.diff(e,self.t)+(sp.Matrix([sp.diff(e,q) for q in self.coords]).T*u)[0])
        point={self.x:a*self.t,self.y:b*self.t,self.z:0}
        v=sp.Matrix([a,b,0])
        faces=critical_hessian_evolution_faces_at(e,u,source,self.coords,self.t,point,v)
        self.assertEqual(faces['residual'],sp.zeros(3))
        self.assertEqual(faces['path_derivative'],sp.zeros(3))

    def test_connection_logdet_rate_is_exactly_minus_two_divergence(self) -> None:
        g=sp.Matrix([[1,2,0],[0,-3,1],[4,0,2]])
        H=sp.Matrix([[-2,1,0],[1,-3,1],[0,1,-4]])
        self.assertEqual(hessian_connection_logdet_divergence_residual(g,H),0)
        self.assertEqual(hessian_connection_logdet_rate(g,H),-2*sp.trace(g))

    def test_connection_splits_exactly_into_strain_reshaping_and_rotation_commutator(self) -> None:
        g=sp.Matrix([[1,2,0],[-1,-3,4],[2,0,2]])
        H=sp.Matrix([[-3,1,0],[1,-4,2],[0,2,-5]])
        self.assertEqual(hessian_connection_strain_rotation_residual(g,H),sp.zeros(3))
        strain_rate,rotation_rate=hessian_strain_rotation_logdet_rates(g,H)
        self.assertEqual(rotation_rate,0)
        self.assertEqual(strain_rate,-2*sp.trace((g+g.T)/2))

    def test_incompressible_connection_can_reshape_hessian_while_preserving_curvature_volume_rate(self) -> None:
        p,q=sp.symbols('p q')
        g=sp.Matrix([[p,2,0],[0,q,1],[3,0,-p-q]])
        H=sp.diag(-2,-3,-5)
        strain,rotation=__import__('src.pde_audit.enstrophy_critical_hessian_evolution',fromlist=['hessian_connection_strain_rotation_faces']).hessian_connection_strain_rotation_faces(g,H)
        connection=sp.simplify(strain+rotation)
        self.assertNotEqual(connection,sp.zeros(3))
        self.assertEqual(hessian_connection_logdet_rate(g,H),0)

    def test_incompressibility_erases_connection_from_hessian_logdet_rate(self) -> None:
        p,q,r=sp.symbols('p q r')
        g=sp.Matrix([[p,1,0],[0,q,2],[3,0,-p-q]])
        H=sp.diag(-2,-3,-5)
        self.assertEqual(sp.trace(g),0)
        self.assertEqual(hessian_connection_logdet_rate(g,H),0)

    def test_jacobi_determinant_identity_is_exact(self) -> None:
        t=self.t
        H=sp.diag(-sp.exp(t),-2*sp.exp(2*t),-3*sp.exp(-t))
        Hd=sp.diff(H,t)
        detd=sp.diff(H.det(),t)
        self.assertEqual(determinant_jacobi_residual(H,Hd,detd),0)
        self.assertEqual(hessian_logdet_rate(H,Hd),2)

    def test_logdet_face_rates_sum_to_total(self) -> None:
        H=sp.diag(-2,-3,-4)
        G=sp.diag(1,2,3)
        C=sp.Matrix([[0,1,0],[1,0,0],[0,0,0]])
        R=sp.diag(-1,0,1)
        faces={'hessian':H,'path_derivative':G+C+R,'growth_hessian':G,'connection':C,'relative_transport':R}
        rates=hessian_logdet_face_rates(faces)
        self.assertEqual(sp.simplify(rates['total']-rates['growth']-rates['connection']-rates['relative']),0)

    def test_finite_integrated_lograte_preserves_nonzero_hessian_determinant(self) -> None:
        d0,I=sp.symbols('d0 I', nonzero=True, finite=True)
        expr=nonzero_determinant_from_lograte(d0,I)
        self.assertEqual(expr,d0*sp.exp(I))
        self.assertNotEqual(expr,0)

    def test_abc_hessian_decays_but_remains_nondegenerate_at_every_finite_time(self) -> None:
        A=sp.symbols('A', positive=True)
        c=abc_hessian_logdet_calibration(A,self.nu,self.t,self.coords)
        self.assertEqual(c['hessian_dot_plus_2nu_hessian'],sp.zeros(3))
        self.assertEqual(c['logdet_rate'],-6*self.nu)
        self.assertEqual(c['jacobi_residual'],0)
        self.assertNotEqual(c['determinant'],0)

    def test_abc_incompressibility_zeroes_connection_logdet_face(self) -> None:
        A=sp.symbols('A', positive=True)
        c=abc_hessian_logdet_calibration(A,self.nu,self.t,self.coords)
        self.assertEqual(c['divergence'],0)
        self.assertEqual(c['connection_logdet_rate'],0)
        self.assertEqual(c['connection_divergence_residual'],0)

    def test_logdet_api_rejects_singular_hessian(self) -> None:
        H=sp.diag(-1,-2,0)
        with self.assertRaises(ValueError):
            hessian_logdet_rate(H,sp.eye(3))


if __name__ == '__main__':
    unittest.main()
