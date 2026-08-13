from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.first_bad_candidate_exclusions import abc_velocity,curl3
from src.pde_audit.local_enstrophy_kelvin_growth_gate import enstrophy_density
from src.pde_audit.moving_enstrophy_critical_point import (
    abc_fixed_critical_point_speed_calibration,
    affine_degenerate_critical_speed_calibration,
    critical_path_value_derivative_residual,
    critical_point_speed_residual,
    critical_relative_velocity_faces,
    nondegenerate_critical_velocity,
    nondegenerate_critical_velocity_at,
    nondegenerate_scalar_critical_velocity_at,
    scalar_critical_constraint_speed_residual_at,
)


class MovingEnstrophyCriticalPointAudit(unittest.TestCase):
    def setUp(self) -> None:
        self.x,self.y,self.z,self.t=sp.symbols('x y z t', real=True)
        self.nu=sp.symbols('nu', positive=True)
        self.coords=(self.x,self.y,self.z)

    def test_critical_path_value_derivative_drops_path_velocity_when_gradient_zero(self) -> None:
        ft=sp.symbols('ft')
        v=sp.Matrix(sp.symbols('v0:3'))
        self.assertEqual(critical_path_value_derivative_residual(ft,ft,sp.zeros(3,1),v),0)

    def test_abc_symmetric_critical_point_is_nondegenerate_strict_maximum(self) -> None:
        A=sp.symbols('A', positive=True)
        c=abc_fixed_critical_point_speed_calibration(A,self.nu,self.t,self.coords)
        H=c['hessian']
        self.assertEqual(c['gradient'],sp.zeros(3,1))
        self.assertNotEqual(c['hessian_det'],0)
        self.assertLess(H[0,0],0)
        self.assertGreater(sp.det(H[:2,:2]),0)
        self.assertLess(H.det(),0)

    def test_abc_critical_maximum_is_fixed_while_fluid_velocity_is_nonzero(self) -> None:
        A=sp.symbols('A', positive=True)
        c=abc_fixed_critical_point_speed_calibration(A,self.nu,self.t,self.coords)
        self.assertNotEqual(c['fluid_velocity'],sp.zeros(3,1))
        self.assertEqual(c['critical_velocity'],sp.zeros(3,1))
        self.assertEqual(c['predicted_critical_velocity'],sp.zeros(3,1))
        self.assertEqual(c['constraint_speed_residual'],sp.zeros(3,1))
        self.assertEqual(c['pde_speed_residual'],sp.zeros(3,1))

    def test_abc_relative_critical_speed_faces_sum_to_minus_fluid_velocity(self) -> None:
        A=sp.symbols('A', positive=True)
        c=abc_fixed_critical_point_speed_calibration(A,self.nu,self.t,self.coords)
        self.assertEqual(sp.simplify(c['relative_velocity']+c['fluid_velocity']),sp.zeros(3,1))

    def test_nondegenerate_scalar_critical_speed_formula_closes_abc_constraint(self) -> None:
        A=sp.symbols('A', positive=True)
        u=abc_velocity(A,self.nu,self.t,self.coords)
        omega=curl3(u,self.coords)
        e=enstrophy_density(omega)
        point={q:sp.pi/4 for q in self.coords}
        vstar=nondegenerate_scalar_critical_velocity_at(e,self.coords,self.t,point)
        residual=scalar_critical_constraint_speed_residual_at(e,self.coords,self.t,point,vstar)
        self.assertEqual(vstar,sp.zeros(3,1))
        self.assertEqual(residual,sp.zeros(3,1))

    def test_affine_uniform_enstrophy_has_degenerate_hessian_and_zero_growth_gradient(self) -> None:
        a,r0=sp.symbols('a r0', positive=True)
        c=affine_degenerate_critical_speed_calibration(a,r0,self.t,self.coords,self.nu)
        self.assertEqual(c['gradient'],sp.zeros(3,1))
        self.assertEqual(c['hessian'],sp.zeros(3))
        self.assertEqual(c['growth_gradient'],sp.zeros(3,1))

    def test_affine_degenerate_critical_set_does_not_determine_unique_speed(self) -> None:
        a,r0=sp.symbols('a r0', positive=True)
        c=affine_degenerate_critical_speed_calibration(a,r0,self.t,self.coords,self.nu)
        self.assertEqual(c['speed_residual_v1'],sp.zeros(3,1))
        self.assertEqual(c['speed_residual_v2'],sp.zeros(3,1))

    def test_inverse_hessian_speed_api_rejects_affine_degeneracy(self) -> None:
        a,r0=sp.symbols('a r0', positive=True)
        from src.pde_audit.kelvin_packet_locality import affine_vortex_stretch_gradient,affine_vortex_stretch_vorticity
        u=affine_vortex_stretch_gradient(a,r0,self.t)*sp.Matrix(self.coords)
        omega=affine_vortex_stretch_vorticity(a,r0,self.t)
        with self.assertRaises(ValueError):
            nondegenerate_critical_velocity(u,omega,self.coords,self.t,self.nu)

    def test_abc_maximum_value_derivative_is_independent_of_critical_point_speed(self) -> None:
        A=sp.symbols('A', positive=True)
        u=abc_velocity(A,self.nu,self.t,self.coords)
        omega=curl3(u,self.coords)
        e=enstrophy_density(omega)
        point={q:sp.pi/4 for q in self.coords}
        grad=sp.Matrix([sp.diff(e,q) for q in self.coords]).subs(point)
        et=sp.diff(e,self.t).subs(point)
        arbitrary=sp.Matrix([3,-2,5])
        total=sp.simplify(et+(grad.T*arbitrary)[0])
        self.assertEqual(critical_path_value_derivative_residual(total,et,grad,arbitrary),0)
        self.assertEqual(sp.simplify(total-et),0)


if __name__ == '__main__':
    unittest.main()
