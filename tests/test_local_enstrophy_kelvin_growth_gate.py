from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.local_enstrophy_kelvin_growth_gate import (
    abc_beltrami_enstrophy_stretching_calibration,
    affine_vortex_local_growth_calibration,
    critical_point_growth_residual,
    enstrophy_balance_faces,
    growth_gate_margin,
    kelvin_bulk_packet_residual,
    vorticity_equation_residual,
)


class LocalEnstrophyKelvinGrowthGateAudit(unittest.TestCase):
    def setUp(self) -> None:
        self.x,self.y,self.z,self.t=sp.symbols('x y z t', real=True)
        self.nu=sp.symbols('nu', positive=True)
        self.coords=(self.x,self.y,self.z)

    def test_enstrophy_balance_residual_is_vorticity_residual_contraction(self) -> None:
        u=sp.Matrix([self.x*self.y,self.y*self.z,self.z*self.x])
        omega=sp.Matrix([self.x+self.t,self.y**2,self.z+self.x])
        faces=enstrophy_balance_faces(u,omega,self.coords,self.t,self.nu)
        self.assertEqual(faces['balance_minus_vorticity_contraction'],0)
        vort=vorticity_equation_residual(u,omega,self.coords,self.t,self.nu)
        self.assertEqual(sp.simplify(faces['balance_residual']-(omega.T*vort)[0]),0)

    def test_critical_point_growth_identity_keeps_curvature_face(self) -> None:
        s,b,ell=sp.symbols('s b ell')
        et=sp.simplify(s-b-self.nu*ell)
        self.assertEqual(critical_point_growth_residual(et,s,b,-ell,self.nu),0)
        self.assertEqual(growth_gate_margin(s,b),s-b)

    def test_orientation_complete_kelvin_bulk_is_exact_enstrophy_gradient_dissipation(self) -> None:
        G=sp.Matrix([[1,2,0],[0,1,3],[2,0,1]])
        H=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        self.assertEqual(kelvin_bulk_packet_residual(G,H,self.nu),0)

    def test_abc_beltrami_stretching_equals_enstrophy_transport_everywhere(self) -> None:
        A=sp.symbols('A', positive=True)
        c=abc_beltrami_enstrophy_stretching_calibration(A,self.nu,self.t,self.coords)
        self.assertEqual(c['beltrami_residual'],sp.zeros(3,1))
        self.assertEqual(c['stretching_minus_enstrophy_transport'],0)
        self.assertEqual(c['ns_residual'],sp.zeros(3,1))

    def test_every_abc_enstrophy_critical_point_has_zero_stretching_by_global_identity(self) -> None:
        A=sp.symbols('A', positive=True)
        c=abc_beltrami_enstrophy_stretching_calibration(A,self.nu,self.t,self.coords)
        point={self.x:sp.pi/4,self.y:sp.pi/4,self.z:sp.pi/4}
        self.assertEqual(sp.simplify(c['enstrophy_gradient'].subs(point)),sp.zeros(3,1))
        self.assertEqual(sp.simplify(c['stretching'].subs(point)),0)
        self.assertEqual(c['stretching_minus_enstrophy_transport'],0)

    def test_affine_vortex_is_exact_ns_and_has_uniform_enstrophy(self) -> None:
        a,r0=sp.symbols('a r0', positive=True)
        c=affine_vortex_local_growth_calibration(a,r0,self.t,self.coords,self.nu)
        self.assertEqual(c['ns_residual'],sp.zeros(3,1))
        self.assertEqual(c['gradient'],sp.zeros(3,1))
        self.assertEqual(c['laplacian'],0)
        self.assertEqual(c['kelvin_bulk'],0)

    def test_affine_vortex_positive_gate_equals_exact_enstrophy_time_growth(self) -> None:
        a,r0=sp.symbols('a r0', positive=True)
        c=affine_vortex_local_growth_calibration(a,r0,self.t,self.coords,self.nu)
        r=sp.simplify(r0*sp.exp(2*a*self.t))
        expected=sp.simplify(8*a*r**2)
        self.assertEqual(c['stretching'],expected)
        self.assertEqual(c['time'],expected)
        self.assertEqual(growth_gate_margin(c['stretching'],c['kelvin_bulk']),expected)
        self.assertEqual(c['balance_residual'],0)

    def test_affine_vortex_calibration_is_not_periodic_target_class(self) -> None:
        a,r0=sp.symbols('a r0', positive=True)
        c=affine_vortex_local_growth_calibration(a,r0,self.t,self.coords,self.nu)
        self.assertNotEqual(c['periodicity_defect_x_2pi'],sp.zeros(3,1))

    def test_positive_local_growth_gate_is_not_itself_a_brownian_source(self) -> None:
        a,r0=sp.symbols('a r0', positive=True)
        c=affine_vortex_local_growth_calibration(a,r0,self.t,self.coords,self.nu)
        self.assertEqual(c['kelvin_bulk'],0)
        self.assertNotEqual(c['stretching'],0)


if __name__ == '__main__':
    unittest.main()
