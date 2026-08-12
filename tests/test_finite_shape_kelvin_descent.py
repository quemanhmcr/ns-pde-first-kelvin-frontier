from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.finite_shape_kelvin_descent import (
    abc_origin_xy_kelvin_descent_error,
    abc_origin_xy_local_vorticity,
    abc_origin_xy_reverse_shape_residual,
    centered_error_noise_quadrupole_leading,
    centered_kelvin_error_quadrupole_leading,
    centered_reverse_shape_residual_quadrupole_leading,
    cauchy_metric_dual_area_frame_rate,
    deformation_descent_error_cross_carre_du_champ,
    deformation_descent_error_leading_cross_covariance,
    deformation_descent_error_pathwise_cross_qv,
    descent_error_variance_leading,
    joint_deformation_error_leading_covariance,
    joint_deformation_error_leading_gramian,
    kelvin_descent_error_noise_coefficients,
    kelvin_descent_error_qv_rate,
    one_mode_shear_deformation_rectangle_error_cross_covariance,
    one_mode_shear_deformation_rectangle_error_cross_leading_residual,
    one_mode_shear_rectangle_error_mean,
    one_mode_shear_rectangle_error_shape_factor,
    one_mode_shear_rectangle_error_variance,
    reverse_age_kelvin_descent_error_drift,
    reverse_age_local_area_rate,
    reverse_age_local_tangent_rate,
    xy_rectangle_shear_descent_error,
    xy_rectangle_shear_kelvin_flux,
    xy_rectangle_shear_local_flux,
)
from src.pde_audit.first_bad_candidate_exclusions import (
    abc_pressure,
    abc_velocity,
    curl3,
    gradient,
    navier_stokes_residual,
)
from src.pde_audit.full_current_shape_covariance import (
    deformation_kelvin_cross_covariance_horizon_residual,
)
from src.pde_audit.kelvin_shape_generator import (
    legendre_leading_moment,
    legendre_width_density,
    polynomial_heat_shear,
    polynomial_heat_shear_residual,
    width_surface_area,
    width_surface_even_moment,
)
from src.pde_audit.stochastic_cauchy_deformation import (
    column_vectorize,
    one_mode_shear_deformation_mean_coefficient,
    reverse_age_horizon_operator_matrix,
)


class FiniteShapeKelvinDescentAudit(unittest.TestCase):
    def test_reverse_age_local_flux_stretching_cancels_leaving_shape_drift(self) -> None:
        a,b,c,d,e,f,g,h,i=sp.symbols('a b c d e f g h i')
        w1,w2,w3,r1,r2,r3=sp.symbols('w1 w2 w3 r1 r2 r3')
        A=sp.Matrix([[a,b,c],[d,e,f],[g,h,i]])
        omega=sp.Matrix([w1,w2,w3])
        area=sp.Matrix(sp.symbols('h1:4'))
        R=sp.Matrix([r1,r2,r3])
        # d omega drift=-A omega; hdot=A^T h+R.
        local_drift=sp.simplify((-A*omega).dot(area)+omega.dot(reverse_age_local_area_rate(A,area,R)))
        self.assertEqual(sp.simplify(local_drift-omega.dot(R)),0)
        self.assertEqual(reverse_age_kelvin_descent_error_drift(omega,R),-omega.dot(R))


    def test_actual_reverse_current_geometry_has_opposite_connection_from_cauchy_metric_dual(self) -> None:
        a,b,c,d=sp.symbols('a b c d')
        A=sp.Matrix([[a,b],[c,d]])
        ell=sp.Matrix(sp.symbols('l1:3'))
        h=sp.Matrix(sp.symbols('h1:3'))
        self.assertEqual(reverse_age_local_tangent_rate(A,ell),-A*ell)
        actual_area=reverse_age_local_area_rate(A,h,sp.zeros(2,1))
        cauchy_area=cauchy_metric_dual_area_frame_rate(A,h)
        self.assertEqual(actual_area,A.T*h)
        self.assertEqual(cauchy_area,-A.T*h)
        self.assertNotEqual(actual_area,cauchy_area)

    def test_descent_error_noise_is_literal_finite_support_vorticity_gradient_residual(self) -> None:
        nu=sp.symbols('nu', positive=True)
        area=sp.Matrix([2,3,5])
        Gx=sp.Matrix([1,2,4]); Gy=sp.Matrix([3,1,2])
        ax,ay=sp.symbols('ax ay')
        q=kelvin_descent_error_noise_coefficients([ax,ay],[Gx,Gy],area)
        self.assertEqual(q,[ax-(Gx.T*area)[0],ay-(Gy.T*area)[0]])
        self.assertEqual(kelvin_descent_error_qv_rate(q,nu),sp.simplify(2*nu*(q[0]**2+q[1]**2)))
        self.assertEqual(deformation_descent_error_pathwise_cross_qv(3),sp.zeros(9,1))

    def test_horizon_D_error_cross_source_is_not_pathwise_cross_qv(self) -> None:
        nu=sp.symbols('nu', positive=True)
        a0,a1,a2,a3,b0,b1,b2,b3,gx,gy=sp.symbols('a0:4 b0:4 gx gy')
        Gx=sp.Matrix([[a0,a1],[a2,a3]])
        Gy=sp.Matrix([[b0,b1],[b2,b3]])
        source=deformation_descent_error_cross_carre_du_champ([Gx,Gy],[gx,gy],nu)
        expected=2*nu*(column_vectorize(Gx)*gx+column_vectorize(Gy)*gy)
        self.assertEqual(sp.simplify(source-expected),sp.zeros(4,1))
        self.assertEqual(deformation_descent_error_pathwise_cross_qv(2),sp.zeros(4,1))

    def test_joint_short_horizon_error_block_is_one_response_gram_integral(self) -> None:
        nu,h=sp.symbols('nu h', positive=True)
        a0,a1,a2,a3,b0,b1,b2,b3,gx,gy=sp.symbols('a0:4 b0:4 gx gy')
        dAx=sp.Matrix([[a0,a1],[a2,a3]])
        dAy=sp.Matrix([[b0,b1],[b2,b3]])
        direct=joint_deformation_error_leading_covariance([dAx,dAy],[gx,gy],nu,h)
        gram=joint_deformation_error_leading_gramian([dAx,dAy],[gx,gy],nu,h)
        self.assertEqual(sp.simplify(direct-gram),sp.zeros(5))
        cross=deformation_descent_error_leading_cross_covariance([dAx,dAy],[gx,gy],nu,h)
        self.assertEqual(cross.applyfunc(lambda q: sp.factor(q)).applyfunc(lambda q: sp.simplify(q/h**2)).shape,(4,1))
        self.assertEqual(descent_error_variance_leading([gx,gy],nu,h),2*nu*h*(gx**2+gy**2))

    def test_cubic_heat_shear_has_nonzero_conserved_descent_bias_but_zero_qv_and_D_covariance(self) -> None:
        y,Y,r,t,nu,ax,by=sp.symbols('y Y r t nu ax by', positive=True)
        U=polynomial_heat_shear(3,y,t,nu)
        self.assertEqual(polynomial_heat_shear_residual(3,y,t,nu),0)
        Uy=sp.diff(U,y)
        err=xy_rectangle_shear_descent_error(Uy,y,Y,ax,by)
        self.assertEqual(sp.simplify(err+4*ax*by**3),0)
        self.assertEqual(sp.diff(err,Y),0)
        self.assertEqual(sp.diff(err,t),0)
        self.assertEqual(kelvin_descent_error_qv_rate([sp.diff(err,Y)],nu),0)
        # Error is a deterministic constant under common translation, so every covariance with D vanishes.
        c1,c2,p=sp.symbols('c1 c2 p')
        v1=sp.Matrix([1,c1,0,1]); v2=sp.Matrix([1,c2,0,1])
        meanD=sp.simplify(p*v1+(1-p)*v2)
        meanE=err
        meanDE=sp.simplify(p*v1*err+(1-p)*v2*err)
        self.assertEqual(sp.simplify(meanDE-meanD*meanE),sp.zeros(4,1))
        self.assertNotEqual(err,0)


    def test_centered_quadrupole_is_exact_cubic_bias_and_exposes_one_higher_qv_jet(self) -> None:
        x,y,z,t,nu,ax,by,r=sp.symbols('x y z t nu ax by r', positive=True)
        coords=(x,y,z)
        U=polynomial_heat_shear(3,y,t,nu)
        omega=sp.Matrix([0,0,-sp.diff(U,y)])
        A=sp.Matrix([[0,sp.diff(U,y),0],[0,0,0],[0,0,0]])
        # xy rectangle, normal e_z: only M_yy is nonzero for the cubic carrier relevant here.
        M=[[sp.zeros(3,1) for _ in range(3)] for __ in range(3)]
        M[1][1]=sp.Matrix([0,0,sp.Rational(4,3)*ax*by**3])
        d2w=[[sp.diff(omega,coords[k],coords[l]) for l in range(3)] for k in range(3)]
        bias2=centered_kelvin_error_quadrupole_leading(d2w,M)
        self.assertEqual(sp.simplify(bias2+4*ax*by**3),0)
        d2A=[[sp.diff(A,coords[k],coords[l]) for l in range(3)] for k in range(3)]
        RA2=centered_reverse_shape_residual_quadrupole_leading(d2A,M)
        self.assertEqual(RA2,sp.zeros(3,1))  # shear A^T n vanishes for n=e_z
        d3w=[[[sp.diff(omega,coords[mu],coords[k],coords[l]) for l in range(3)] for k in range(3)] for mu in range(3)]
        q2=centered_error_noise_quadrupole_leading(d3w,M)
        self.assertEqual(q2,[0,0,0])
        # Under isotropic surface scaling ax->r ax, by->r by, the bias is raw r^4.
        scaled=sp.simplify(bias2.subs({ax:r*ax,by:r*by}))
        self.assertEqual(sp.simplify(scaled-r**4*bias2),0)

    def test_one_mode_exact_NS_error_variance_referees_anchor_qv(self) -> None:
        y,t,h,nu,k,ax,by=sp.symbols('y t h nu k ax by', positive=True)
        mean=one_mode_shear_rectangle_error_mean(y,t,ax,by,nu,k)
        var=one_mode_shear_rectangle_error_variance(y,t,h,ax,by,nu,k)
        leading=sp.simplify(2*nu*h*sp.diff(mean,y)**2)
        self.assertEqual(sp.trigsimp(sp.simplify(sp.series(var,h,0,2).removeO()-leading)),0)
        self.assertNotEqual(one_mode_shear_rectangle_error_shape_factor(ax,by,k),0)

    def test_one_mode_exact_NS_D_error_cross_covariance_obeys_mixed_horizon_law(self) -> None:
        x,y,t,h,nu,k,ax,by=sp.symbols('x y t h nu k ax by', positive=True)
        alpha=nu*k**2
        U=sp.exp(-alpha*t)*sp.cos(k*y)
        Uy=sp.diff(U,y)
        velocity=sp.Matrix([U,0])
        A=sp.Matrix([[0,Uy],[0,0]])
        mean_c=one_mode_shear_deformation_mean_coefficient(y,t,h,nu,k)
        meanD=sp.Matrix([[1,0],[mean_c,1]])
        epsbar=one_mode_shear_rectangle_error_mean(y,t,ax,by,nu,k)
        cross_scalar=one_mode_shear_deformation_rectangle_error_cross_covariance(y,t,h,ax,by,nu,k)
        E21=sp.Matrix([[0,0],[1,0]])
        v21=column_vectorize(E21)
        cross=sp.simplify(v21*cross_scalar)
        Hcross=reverse_age_horizon_operator_matrix(cross,h,t,velocity,nu,(x,y))
        dM=[sp.diff(meanD,x),sp.diff(meanD,y)]
        deps=[sp.diff(epsbar,x),sp.diff(epsbar,y)]
        self.assertEqual(
            deformation_kelvin_cross_covariance_horizon_residual(cross,Hcross,A,dM,deps,nu),
            sp.zeros(4,1),
        )
        self.assertEqual(
            one_mode_shear_deformation_rectangle_error_cross_leading_residual(y,t,h,ax,by,nu,k),
            0,
        )

    def test_polynomial_heat_shear_hierarchy_hides_bias_from_qv_at_center(self) -> None:
        y,X,t,nu,eps=sp.symbols('y X t nu eps', real=True)
        for m in range(1,5):
            n=2*m
            U=polynomial_heat_shear(n+1,y,t,nu)
            self.assertEqual(polynomial_heat_shear_residual(n+1,y,t,nu),0)
            Uy=sp.diff(U,y)
            w0=sp.Integer(1)
            w1=legendre_width_density(n,y,eps)
            self.assertEqual(width_surface_area(w1,y),width_surface_area(w0,y))
            for j in range(m):
                self.assertEqual(sp.simplify(width_surface_even_moment(w1,y,2*j)-width_surface_even_moment(w0,y,2*j)),0)
            # Flux error difference; local term cancels because areas match.
            delta_err=sp.simplify(-sp.integrate(Uy*(w1-w0),(y,-1,1)))
            expected=sp.simplify(-(n+1)*eps*legendre_leading_moment(n))
            self.assertEqual(sp.simplify(delta_err-expected),0)
            self.assertNotEqual(expected.subs(eps,1),0)
            # Translate the common anchor: at X=0 the unresolved even mode has zero qv coefficient.
            s=sp.symbols('s', real=True)
            Uy_shift=Uy.subs(y,X+s)
            err1=sp.simplify(-sp.integrate((Uy_shift-Uy.subs(y,X))*w1.subs(y,s),(s,-1,1)))
            err0=sp.simplify(-sp.integrate((Uy_shift-Uy.subs(y,X))*w0,(s,-1,1)))
            self.assertEqual(sp.simplify(sp.diff(err1,X).subs(X,0)),0)
            self.assertEqual(sp.simplify(sp.diff(err0,X).subs(X,0)),0)

    def test_exact_ABC_activates_finite_variation_shape_drift_of_descent_error(self) -> None:
        x,y,z,t,nu,Amp,b=sp.symbols('x y z t nu Amp b', positive=True)
        coords=(x,y,z)
        u=abc_velocity(Amp,nu,t,coords)
        p=abc_pressure(u)
        self.assertEqual(sp.simplify(navier_stokes_residual(u,p,coords,t,nu)),sp.zeros(3,1))
        omega=curl3(u,coords)
        self.assertEqual(sp.simplify(omega-u),sp.zeros(3,1))
        origin={x:0,y:0,z:0}
        omega0=sp.simplify(omega.subs(origin))
        self.assertEqual(omega0,abc_origin_xy_local_vorticity(Amp,nu,t))
        # Direct R_A integral over centered xy square with normal +e_z.
        sx,sy=sp.symbols('sx sy', real=True)
        G=gradient(u,coords)
        nvec=sp.Matrix([0,0,1])
        Gp=G.subs({x:sx,y:sy,z:0})
        G0=G.subs(origin)
        integrand=sp.simplify((Gp-G0).T*nvec)
        R=integrand.applyfunc(lambda q: sp.simplify(sp.integrate(sp.integrate(q,(sx,-b,b)),(sy,-b,b))))
        self.assertEqual(sp.simplify(R-abc_origin_xy_reverse_shape_residual(Amp,nu,t,b)),sp.zeros(3,1))
        drift=reverse_age_kelvin_descent_error_drift(omega0,R)
        expected=sp.simplify(4*Amp**2*sp.exp(-2*nu*t)*b*(b-sp.sin(b)))
        self.assertEqual(sp.simplify(drift-expected),0)
        self.assertNotEqual(expected,0)
        # Initial finite Kelvin flux bias is also nonzero and has the same geometric sin(b)-b carrier.
        self.assertNotEqual(abc_origin_xy_kelvin_descent_error(Amp,nu,t,b),0)


if __name__ == '__main__':
    unittest.main()
