from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.codeforming_surface_moment_tower import (
    codeforming_generating_current_rate_integrand,
    codeforming_gradient_residual,
    codeforming_homogeneous_jet_refinement_residual,
    codeforming_homogeneous_scale_shape_residual,
    codeforming_nonaffinity_divergence,
    codeforming_nonaffinity_field,
    codeforming_nonaffinity_geometry_residual,
    codeforming_nonaffinity_one_form,
    codeforming_residual_one_form_pullback_residual,
    codeforming_kelvin_curl_residual,
    codeforming_anchor_one_form_derivative,
    codeforming_descent_error_drift,
    pulledback_vorticity_defect,
    codeforming_oriented_moment,
    codeforming_oriented_moment_rate_integrand,
    coherent_refinement_codeforming_moment_residual,
    oriented_moment_linear_pushforward,
    scalar_normalized_oriented_moments,
    scalar_normalized_refinement_residual,
    scale_shape_codeforming_residual,
)
from src.pde_audit.kelvin_packet_locality import (
    exact_linear_strain_ns_residual,
    strained_refined_line_frame,
)
from src.pde_audit.kelvin_shape_generator import polynomial_heat_shear, polynomial_heat_shear_residual
from src.pde_audit.finite_shape_kelvin_descent import one_mode_shear_rectangle_error_mean


class CodeformingSurfaceMomentTowerAudit(unittest.TestCase):
    def test_isotropic_refinement_exponent_m_plus_two_is_exact_line_plus_area_scaling(self) -> None:
        x,y,z,lam=sp.symbols('x y z lam', positive=True)
        alpha=(2,1,0)
        M=sp.Matrix(sp.symbols('m0:3'))
        moments={alpha:M}
        pushed=oriented_moment_linear_pushforward(moments,alpha,lam*sp.eye(3),(x,y,z))
        self.assertEqual(sp.simplify(pushed-lam**(sum(alpha)+2)*M),sp.zeros(3,1))

    def test_general_refinement_scalar_normalization_leaves_only_unit_det_shape_action(self) -> None:
        x,y,z,rho,d,a,b=sp.symbols('x y z rho d a b', positive=True)
        # det R=d^3 exactly after choosing the third diagonal entry.
        R=sp.diag(a,b,d**3/(a*b))
        moments={
            (2,0,0):sp.Matrix(sp.symbols('m200_0:3')),
            (0,2,0):sp.Matrix(sp.symbols('m020_0:3')),
            (0,0,2):sp.Matrix(sp.symbols('m002_0:3')),
            (1,1,0):sp.Matrix(sp.symbols('m110_0:3')),
            (1,0,1):sp.Matrix(sp.symbols('m101_0:3')),
            (0,1,1):sp.Matrix(sp.symbols('m011_0:3')),
        }
        self.assertEqual(
            scalar_normalized_refinement_residual(moments,(1,1,0),R,rho,d,(x,y,z)),
            sp.zeros(3,1),
        )

    def test_full_codeforming_pullback_equals_scalar_normalization_then_unit_det_shape_pullback(self) -> None:
        x,y,z,rho,a,b=sp.symbols('x y z rho a b', positive=True)
        S=sp.diag(a,b,1/(a*b))
        L=sp.simplify(rho*S)
        alpha=(1,1,0)
        moments={
            (2,0,0):sp.Matrix(sp.symbols('m200_0:3')),
            (0,2,0):sp.Matrix(sp.symbols('m020_0:3')),
            (0,0,2):sp.Matrix(sp.symbols('m002_0:3')),
            (1,1,0):sp.Matrix(sp.symbols('m110_0:3')),
            (1,0,1):sp.Matrix(sp.symbols('m101_0:3')),
            (0,1,1):sp.Matrix(sp.symbols('m011_0:3')),
        }
        self.assertEqual(scale_shape_codeforming_residual(moments,alpha,L,rho,(x,y,z)),sp.zeros(3,1))

    def test_codeforming_nonaffinity_is_one_divergence_free_residual_velocity_field(self) -> None:
        x,y,z,X,Y,Z,nu,t=sp.symbols('x y z X Y Z nu t')
        # Exact quadratic heat shear; use anchor Y and relative coordinates (x,y,z).
        U=lambda yy: yy**2+2*nu*t
        delta=sp.Matrix([sp.expand(U(Y+y)-U(Y)),0,0])
        A0=sp.Matrix([[0,2*Y,0],[0,0,0],[0,0,0]])
        Aprof=sp.Matrix([[0,2*(Y+y),0],[0,0,0],[0,0,0]])
        lx,ly,lz=sp.symbols('lx ly lz', nonzero=True)
        L=sp.diag(lx,ly,lz)
        N=codeforming_nonaffinity_field(delta,A0,(x,y,z),L,(X,Y,Z))
        self.assertEqual(N,sp.Matrix([ly**2*Y**2/lx,0,0]))
        self.assertEqual(codeforming_nonaffinity_divergence(N,(X,Y,Z)),0)
        self.assertEqual(
            codeforming_nonaffinity_geometry_residual(delta,Aprof,A0,(x,y,z),L,(X,Y,Z)),
            sp.zeros(3),
        )
        self.assertEqual(codeforming_gradient_residual(Aprof,A0,(x,y,z),L,(X,Y,Z)),N.jacobian((X,Y,Z)).T)

    def test_generating_current_theta_derivatives_are_exactly_the_full_moment_rate_tower(self) -> None:
        X,Y=sp.symbols('X Y')
        th1,th2=sp.symbols('th1 th2')
        p,q=sp.symbols('p q')
        xi=sp.Matrix([X,Y]); area=sp.Matrix([p,q]); theta=sp.Matrix([th1,th2])
        N=sp.Matrix([X**2+X*Y,-X*Y-Y**2])  # divergence X+Y-X-2Y? choose corrected below
        N=sp.Matrix([X**2, -2*X*Y])
        # div N=2X-2X=0: a literal incompressible residual field.
        Gdot=codeforming_generating_current_rate_integrand(xi,area,theta,N)
        alpha=(2,1)
        recovered=Gdot
        for _ in range(alpha[0]):
            recovered=sp.diff(recovered,th1)
        for _ in range(alpha[1]):
            recovered=sp.diff(recovered,th2)
        recovered=sp.simplify(recovered.subs({th1:0,th2:0}))
        direct=codeforming_oriented_moment_rate_integrand(xi,area,N,alpha)
        self.assertEqual(sp.simplify(recovered-direct),sp.zeros(2,1))

    def test_kelvin_descent_error_is_circulation_of_metric_weighted_nonaffinity_one_form(self) -> None:
        x,y,z,X,Y,Z,a,b=sp.symbols('x y z X Y Z a b', positive=True)
        # Cubic heat-shear after subtracting its local affine part at y=0.
        residual=sp.Matrix([y**3,0,0])
        L=sp.eye(3)
        N=codeforming_nonaffinity_field(residual,sp.zeros(3),(x,y,z),L,(X,Y,Z))
        beta=codeforming_nonaffinity_one_form(N,L)
        self.assertEqual(beta,sp.Matrix([Y**3,0,0]))
        self.assertEqual(
            codeforming_residual_one_form_pullback_residual(residual,(x,y,z),L,(X,Y,Z)),
            sp.zeros(3,1),
        )
        # Counter-clockwise rectangle line integral: bottom + right + top + left.
        line=sp.integrate((-b)**3,(X,-a,a))+sp.integrate(b**3,(X,a,-a))
        self.assertEqual(sp.simplify(line+4*a*b**3),0)
        omega_defect=sp.Matrix([0,0,-3*y**2])
        pulled=pulledback_vorticity_defect(omega_defect,sp.zeros(3,1),(x,y,z),L,(X,Y,Z))
        self.assertEqual(codeforming_kelvin_curl_residual(N,L,(X,Y,Z),pulled),sp.zeros(3,1))
        flux=sp.integrate(sp.integrate(pulled[2],(Y,-b,b)),(X,-a,a))
        self.assertEqual(sp.simplify(flux-line),0)

    def test_one_mode_exact_NS_anchor_derivative_of_kelvin_one_form_is_literal_error_noise_coefficient(self) -> None:
        x,y,z,X,Y,Z,t,nu,k,a,b=sp.symbols('x y z X Y Z t nu k a b', positive=True)
        alpha=nu*k**2
        U=lambda yy: sp.exp(-alpha*t)*sp.cos(k*yy)
        residual=sp.Matrix([
            sp.simplify(U(Y+y)-U(Y)-sp.diff(U(Y),Y)*y),0,0
        ])
        L=sp.eye(3)
        N=codeforming_nonaffinity_field(residual,sp.zeros(3),(x,y,z),L,(X,Z,sp.Symbol('Q')))
        # The codeforming y-coordinate above is Z; rename the resulting expression back to y-like Z.
        beta=codeforming_nonaffinity_one_form(N,L)
        bx=beta[0]
        eps_line=sp.simplify(2*a*(bx.subs(Z,-b)-bx.subs(Z,b)))
        expected=one_mode_shear_rectangle_error_mean(Y,t,a,b,nu,k)
        self.assertEqual(sp.trigsimp(sp.simplify(eps_line-expected)),0)
        q_line=sp.simplify(2*a*(
            codeforming_anchor_one_form_derivative(beta,Y)[0].subs(Z,-b)
            -codeforming_anchor_one_form_derivative(beta,Y)[0].subs(Z,b)
        ))
        self.assertEqual(sp.trigsimp(sp.simplify(q_line-sp.diff(expected,Y))),0)

    def test_codeforming_shape_drift_contraction_is_same_physical_error_drift(self) -> None:
        e1,e2,e3,h1,h2,h3=sp.symbols('e1 e2 e3 h1 h2 h3')
        eta=sp.Matrix([e1,e2,e3]); hdot=sp.Matrix([h1,h2,h3])
        self.assertEqual(codeforming_descent_error_drift(eta,hdot),-(eta.T*hdot)[0])

    def test_anisotropic_quadratic_nonaffinity_can_diverge_while_kelvin_one_form_shrinks(self) -> None:
        x,y,z,X,Y,Z,r=sp.symbols('x y z X Y Z r', positive=True)
        residual=sp.Matrix([y**2,0,0])
        L=sp.diag(r**3,r,r)
        N=codeforming_nonaffinity_field(residual,sp.zeros(3),(x,y,z),L,(X,Y,Z))
        self.assertEqual(N,sp.Matrix([Y**2/r,0,0]))
        beta=codeforming_nonaffinity_one_form(N,L)
        self.assertEqual(beta,sp.Matrix([r**5*Y**2,0,0]))
        omega_defect=sp.Matrix([0,0,-2*y])
        pulled=pulledback_vorticity_defect(omega_defect,sp.zeros(3,1),(x,y,z),L,(X,Y,Z))
        self.assertEqual(pulled,sp.Matrix([0,0,-2*r**5*Y]))
        self.assertEqual(codeforming_kelvin_curl_residual(N,L,(X,Y,Z),pulled),sp.zeros(3,1))

    def test_codeforming_moment_and_generating_current_freeze_for_affine_incompressible_flow(self) -> None:
        x,y,z,X,Y,Z=sp.symbols('x y z X Y Z')
        a,b,c=sp.symbols('a b c')
        A=sp.Matrix([[a,b,0],[c,-a,0],[0,0,0]])
        r=sp.Matrix([x,y,z])
        delta=sp.simplify(A*r)
        L=sp.Matrix([[2,1,0],[0,1,0],[0,0,1]])
        N=codeforming_nonaffinity_field(delta,A,(x,y,z),L,(X,Y,Z))
        self.assertEqual(N,sp.zeros(3,1))
        xi=sp.Matrix([X,Y,Z]); area=sp.Matrix(sp.symbols('q0:3')); theta=sp.Matrix(sp.symbols('th0:3'))
        self.assertEqual(codeforming_oriented_moment_rate_integrand(xi,area,N,(2,1,0)),sp.zeros(3,1))
        self.assertEqual(codeforming_generating_current_rate_integrand(xi,area,theta,N),sp.zeros(3,1))

    def test_coherent_linear_refinement_is_exact_gauge_for_full_codeforming_tower(self) -> None:
        x,y,z=sp.symbols('x y z')
        L=sp.Matrix([[2,1,0],[0,1,0],[0,0,1]])
        R=sp.Matrix([[1,1,0],[0,1,0],[0,0,1]])
        moments={
            (2,0,0):sp.Matrix(sp.symbols('m200_0:3')),
            (0,2,0):sp.Matrix(sp.symbols('m020_0:3')),
            (0,0,2):sp.Matrix(sp.symbols('m002_0:3')),
            (1,1,0):sp.Matrix(sp.symbols('m110_0:3')),
            (1,0,1):sp.Matrix(sp.symbols('m101_0:3')),
            (0,1,1):sp.Matrix(sp.symbols('m011_0:3')),
        }
        self.assertEqual(
            coherent_refinement_codeforming_moment_residual(moments,(1,1,0),L,R,(x,y,z)),
            sp.zeros(3,1),
        )

    def test_homogeneous_nonaffinity_jet_has_exact_rho_p_minus_one_times_shape_conjugation(self) -> None:
        x,y,z,X,Y,Z,rho,a=sp.symbols('x y z X Y Z rho a', nonzero=True)
        field=sp.Matrix([y**3, z**3, x**3])
        S=sp.diag(a,1,1/a)
        self.assertEqual(
            codeforming_homogeneous_scale_shape_residual(
                field,3,(x,y,z),rho,S,(X,Y,Z)
            ),
            sp.zeros(3,1),
        )

    def test_homogeneous_nonaffinity_jet_reparameterizes_tensorially_under_refinement(self) -> None:
        x,y,z,X,Y,Z=sp.symbols('x y z X Y Z')
        field=sp.Matrix([y**3+2*x*y*z,z**3,0])
        L=sp.Matrix([[2,0,0],[0,3,0],[0,0,1]])
        R=sp.Matrix([[1,1,0],[0,1,0],[0,0,1]])
        self.assertEqual(
            codeforming_homogeneous_jet_refinement_residual(field,(x,y,z),L,R,(X,Y,Z)),
            sp.zeros(3,1),
        )

    def test_exact_quadratic_ns_exposes_anisotropic_nonaffinity_ratio_not_scalar_scale_alone(self) -> None:
        y,t,nu,r=sp.symbols('y t nu r', positive=True)
        self.assertEqual(polynomial_heat_shear_residual(2,y,t,nu),0)
        x,z,X,Y,Z=sp.symbols('x z X Y Z')
        U=polynomial_heat_shear(2,y,t,nu)
        delta=sp.Matrix([sp.simplify(U-U.subs(y,0)),0,0])
        A0=sp.zeros(3)
        # All physical line scales shrink, yet y^2/l_x = r^2/r^3=r^-1 in codeforming units.
        L=sp.diag(r**3,r,r)
        N=codeforming_nonaffinity_field(delta,A0,(x,y,z),L,(X,Y,Z))
        self.assertEqual(N,sp.Matrix([Y**2/r,0,0]))

    def test_critical_long_thin_strain_has_divergent_scalar_normalized_area_but_constant_codeforming_area(self) -> None:
        s,t,r=sp.symbols('s t r', positive=True)
        x,y,z=sp.symbols('x y z')
        # exact linear strain NS, with critical isotropic refinement k=s and r=e^{-st}
        residual,_=exact_linear_strain_ns_residual(s,(x,y,z),sp.Symbol('nu'))
        self.assertEqual(residual,sp.zeros(3,1))
        L=strained_refined_line_frame(s,s,t).subs(sp.exp(-s*t),r)
        self.assertEqual(L,sp.diag(1,r,r**2))
        # xy reference face area vector e_z pushes to cof(L)e_z = r e_z.
        physical_area=sp.Matrix([0,0,r])
        moments={(0,0,0):physical_area}
        normalized=scalar_normalized_oriented_moments(moments,r)[(0,0,0)]
        self.assertEqual(normalized,sp.Matrix([0,0,1/r]))
        pulled=codeforming_oriented_moment(moments,(0,0,0),L,(x,y,z))
        self.assertEqual(pulled,sp.Matrix([0,0,1]))
        self.assertEqual(L[0,0],1)  # no support locality despite perfect codeforming constancy

    def test_supercritical_refinement_can_be_support_local_while_scalar_normalized_tower_diverges(self) -> None:
        s,k,t=sp.symbols('s k t', positive=True)
        x,y,z=sp.symbols('x y z')
        L=strained_refined_line_frame(s,k,t)
        rho=sp.exp(-k*t)
        # xy face area l_x*l_y = exp((s-2k)t), normalized by rho^2 leaves exp(st).
        area=sp.Matrix([0,0,sp.exp((s-2*k)*t)])
        moments={(0,0,0):area}
        normalized=scalar_normalized_oriented_moments(moments,rho)[(0,0,0)]
        self.assertEqual(normalized,sp.Matrix([0,0,sp.exp(s*t)]))
        pulled=codeforming_oriented_moment(moments,(0,0,0),L,(x,y,z))
        self.assertEqual(pulled,sp.Matrix([0,0,1]))
        # When k>s, all diagonal line exponents are negative; algebraically locality and
        # scalar-normalized boundedness are therefore distinct requirements.
        self.assertEqual(L,sp.diag(sp.exp((s-k)*t),sp.exp(-k*t),sp.exp(-(s+k)*t)))


if __name__ == '__main__':
    unittest.main()
