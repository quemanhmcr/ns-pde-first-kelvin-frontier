from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.kelvin_shape_generator import polynomial_heat_shear, polynomial_heat_shear_residual
from src.pde_audit.surface_moment_hierarchy import (
    affine_reverse_age_oriented_moment_rate,
    homogeneous_moment_rate_degree,
    monomial,
    oriented_first_moment_recentering_residual,
    polynomial_error_noise_from_oriented_moments,
    polynomial_flux_error_from_oriented_moments,
    polynomial_shape_residual_from_oriented_moments,
    reverse_age_oriented_moment_rate_integrand,
)


class SurfaceMomentHierarchyAudit(unittest.TestCase):
    def test_reverse_age_oriented_monomial_transport_is_literal_product_rule(self) -> None:
        x,y=sp.symbols('x y')
        p,q,a,b,c,d=sp.symbols('p q a b c d')
        r=sp.Matrix([x,y]); area=sp.Matrix([p,q])
        du=sp.Matrix([a*x+b*y,c*x+d*y])
        A=sp.Matrix([[a,b],[c,d]])
        rate=reverse_age_oriented_moment_rate_integrand(r,area,du,A,(2,1))
        expected=sp.simplify(
            x**2*y*A.T*area
            -2*x*y*du[0]*area
            -x**2*du[1]*area
        )
        self.assertEqual(sp.simplify(rate-expected),sp.zeros(2,1))

    def test_affine_velocity_closes_each_oriented_moment_order_exactly(self) -> None:
        a,b,c,d=sp.symbols('a b c d')
        A=sp.Matrix([[a,b],[c,d]])
        # All order-two moments required by alpha=(1,1).
        M20=sp.Matrix(sp.symbols('m20_1:3'))
        M11=sp.Matrix(sp.symbols('m11_1:3'))
        M02=sp.Matrix(sp.symbols('m02_1:3'))
        moments={(2,0):M20,(1,1):M11,(0,2):M02}
        rate=affine_reverse_age_oriented_moment_rate(moments,(1,1),A)
        expected=sp.simplify(A.T*M11-a*M11-b*M02-c*M20-d*M11)
        self.assertEqual(sp.simplify(rate-expected),sp.zeros(2,1))
        # No order 0,1,3 moment is requested: affine transport is same-order closed.

    def test_nonlinear_degree_p_velocity_raises_order_m_to_m_plus_p_minus_one(self) -> None:
        x,y,z=sp.symbols('x y z')
        r=sp.Matrix([x,y,z]); area=sp.Matrix([1,0,0])
        for p in range(2,7):
            # Divergence-free shear delta u=(y^p,0,0).
            du=sp.Matrix([y**p,0,0])
            A=du.jacobian((x,y,z))
            for m in range(0,5):
                rate=reverse_age_oriented_moment_rate_integrand(r,area,du,A,(0,m,0))
                degrees=homogeneous_moment_rate_degree(rate,(x,y,z))
                self.assertEqual(degrees,{m+p-1})
                self.assertEqual(sp.simplify(rate[1]-p*y**(m+p-1)),0)

    def test_exact_quadratic_heat_shear_breaks_material_anchor_centering(self) -> None:
        y,t,nu,b,c=sp.symbols('y t nu b c', positive=True)
        U=polynomial_heat_shear(2,y,t,nu)
        self.assertEqual(polynomial_heat_shear_residual(2,y,t,nu),0)
        # At anchor y=0, delta u=(y^2,0,0). A^T e_x=2y e_y.
        x,z=sp.symbols('x z')
        r=sp.Matrix([x,y,z]); area=sp.Matrix([1,0,0])
        du=sp.Matrix([sp.simplify(U-U.subs(y,0)),0,0])
        A=sp.Matrix([[0,sp.diff(U,y),0],[0,0,0],[0,0,0]])
        M1rate=reverse_age_oriented_moment_rate_integrand(r,area,du,A,(0,1,0))
        integrated=M1rate.applyfunc(lambda q: sp.simplify(sp.integrate(sp.integrate(q,(y,-b,b)),(z,-c,c))))
        self.assertEqual(integrated,sp.Matrix([0,sp.Rational(8,3)*b**3*c,0]))
        # Initial oriented y-first moment is zero by symmetry, yet its rate is nonzero.
        self.assertNotEqual(integrated,sp.zeros(3,1))

    def test_tangential_xy_shear_conserves_entire_oriented_y_moment_tower(self) -> None:
        x,y,z=sp.symbols('x y z')
        f=sp.Function('f')
        r=sp.Matrix([x,y,z]); area=sp.Matrix([0,0,1])
        du=sp.Matrix([f(y)-f(0),0,0])
        A=sp.Matrix([[0,sp.diff(f(y),y),0],[0,0,0],[0,0,0]])
        for m in range(8):
            rate=reverse_age_oriented_moment_rate_integrand(r,area,du,A,(0,m,0))
            self.assertEqual(rate,sp.zeros(3,1))

    def test_cubic_heat_shear_flux_bias_is_exact_quadrupole_moment_contraction(self) -> None:
        x,y,z,t,nu,a,b=sp.symbols('x y z t nu a b', positive=True)
        U=polynomial_heat_shear(3,y,t,nu)
        omega=sp.Matrix([0,0,-sp.diff(U,y)])
        # xy rectangle normal e_z: M_yy=(4/3)a b^3 e_z. Constant area moment is not needed after subtracting omega(0).
        moments={
            (0,1,0):sp.zeros(3,1),  # centered oriented first moment: known zero, not missing
            (0,2,0):sp.Matrix([0,0,sp.Rational(4,3)*a*b**3]),
        }
        err=polynomial_flux_error_from_oriented_moments(omega,(x,y,z),moments)
        self.assertEqual(sp.simplify(err+4*a*b**3),0)
        q=polynomial_error_noise_from_oriented_moments(omega,(x,y,z),moments)
        self.assertEqual(q,[0,0,0])

    def test_cubic_heat_shear_reverse_shape_residual_is_same_quadrupole_carrier(self) -> None:
        x,y,z,t,nu,b,c=sp.symbols('x y z t nu b c', positive=True)
        U=polynomial_heat_shear(3,y,t,nu)
        A=sp.Matrix([[0,sp.diff(U,y),0],[0,0,0],[0,0,0]])
        # yz rectangle normal e_x.
        moments={(0,2,0):sp.Matrix([sp.Rational(4,3)*b**3*c,0,0])}
        RA=polynomial_shape_residual_from_oriented_moments(A,(x,y,z),moments)
        self.assertEqual(RA,sp.Matrix([0,4*b**3*c,0]))

    def test_affine_flow_preserves_zero_first_moments_but_nonlinear_flow_need_not(self) -> None:
        a,b,c,d=sp.symbols('a b c d')
        A=sp.Matrix([[a,b],[c,d]])
        z=sp.zeros(2,1)
        # Order-one moment family all zero -> affine rate zero.
        moments={(1,0):z,(0,1):z}
        self.assertEqual(affine_reverse_age_oriented_moment_rate(moments,(1,0),A),z)
        self.assertEqual(affine_reverse_age_oriented_moment_rate(moments,(0,1),A),z)

    def test_single_anchor_shift_cannot_generically_center_vector_valued_first_moment(self) -> None:
        h1,h2,c1,c2=sp.symbols('h1 h2 c1 c2')
        h=sp.Matrix([h1,h2]); c=sp.Matrix([c1,c2])
        M=sp.Matrix([[1,0],[0,1]])
        residual=oriented_first_moment_recentering_residual(M,h,c)
        # A zero residual would force a rank-two identity matrix to equal the rank<=1 dyad c h^T.
        self.assertEqual(sp.simplify(residual.det()),sp.simplify(1-c1*h1-c2*h2))
        # Concrete witness: h=e1 forces the second column of every c h^T to zero, unlike I.
        self.assertNotEqual(oriented_first_moment_recentering_residual(M,sp.Matrix([1,0]),sp.Matrix([c1,c2])),sp.zeros(2))


if __name__ == '__main__':
    unittest.main()
