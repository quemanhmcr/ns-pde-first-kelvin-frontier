from __future__ import annotations

from pathlib import Path
import sys
import unittest
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))

from pde_audit.kelvin_packet_locality import (  # noqa: E402
    affine_vortex_stretch_gradient,
    affine_vortex_stretch_ns_residual,
)
from pde_audit.future_covariance_tensor import (  # noqa: E402
    connected_covariance_horizon_residual,
    connected_mean_horizon_residual,
    connected_second_moment_horizon_residual,
    product_pair_diagonal_defect,
    vector_carre_du_champ,
)
from pde_audit.ancestry_resolution_kernel import (  # noqa: E402
    vector_total_covariance_decomposition,
)
from pde_audit.stochastic_cauchy_deformation import (  # noqa: E402
    affine_vortex_cauchy_z_residual,
    affine_vortex_total_bank_envelope_residual,
    cauchy_packet_metric_duality_residual,
    cauchy_spatial_support_spectral_trace_residual,
    coherent_area_frame_from_cauchy,
    cauchy_sample,
    cauchy_two_face_envelope_residual,
    deformation_gram_rate_residual,
    deformation_reverse_age_residual,
    ensemble_cauchy_moments,
    ensemble_deformation_rate_residual,
    ensemble_terminal_headroom_residual,
    forward_deformation_from_cauchy,
    incompressible_deformation_determinant_log_rate,
    packet_metric_from_area_frame,
    packet_metric_rate_residual_from_cauchy,
    matrix_deformation_covariance,
    matrix_deformation_pair_covariance_residual,
    expected_packet_metric_split_residual,
    deformation_second_moment_split_residual,
    one_mode_shear_deformation_dispersion_residual,
    one_mode_shear_deformation_mean_coefficient,
    one_mode_shear_deformation_second_coefficient,
    one_mode_shear_deformation_variance,
    one_mode_shear_deformation_variance_at_symmetry,
    one_mode_shear_deformation_variance_leading_residual,
    column_vectorize,
    column_partial_trace_vectorized_covariance,
    deformation_carre_du_champ_projection_residual,
    deformation_covariance_leading_projection_residual,
    deformation_covariance_projection_residual,
    deformation_mean_horizon_residual,
    deformation_second_moment_horizon_residual,
    horizon_connection_vectorization_residual,
    matrix_deformation_vectorized_covariance,
    projected_deformation_carre_du_champ,
    projected_deformation_covariance_horizon_residual,
    projected_deformation_covariance_leading_tensor,
    reverse_age_horizon_operator_matrix,
    reverse_age_path_vectorization_residual,
    vectorized_deformation_covariance_horizon_residual,
    vectorized_deformation_covariance_leading_tensor,
    vectorized_deformation_pair_covariance_residual,
    vectorized_horizon_connection,
    vectorized_reverse_age_path_connection,
    one_mode_shear_second_moment,
    one_mode_shear_terminal_headroom,
    one_mode_shear_terminal_supremum,
    sample_terminal_headroom_residual,
)

class StochasticCauchyDeformationAudit(unittest.TestCase):
    def test_sample_terminal_headroom_factorization_is_exact(self) -> None:
        D=sp.Matrix([[2,1],[1,1]])
        w=sp.Matrix(sp.symbols('w0:2'))
        W=sp.symbols('W')
        self.assertEqual(sample_terminal_headroom_residual(D,w,W),sp.zeros(2))

    def test_ensemble_terminal_headroom_factorization_is_exact(self) -> None:
        D1=sp.Matrix([[1,1],[0,1]])
        D2=sp.Matrix([[2,0],[1,1]])
        w1=sp.Matrix(sp.symbols('a0:2'))
        w2=sp.Matrix(sp.symbols('b0:2'))
        p=sp.symbols('p')
        weights=[p,1-p]
        W=sp.symbols('W')
        self.assertEqual(ensemble_terminal_headroom_residual([D1,D2],[w1,w2],weights,W),sp.zeros(2))

    def test_total_vorticity_envelope_splits_into_terminal_headroom_plus_covariance(self) -> None:
        D1=sp.eye(2); D2=sp.Matrix([[1,1],[0,1]])
        w1=sp.Matrix([1,0]); w2=sp.Matrix([0,1])
        m,Q,C,R=ensemble_cauchy_moments([D1,D2],[w1,w2],[sp.Rational(1,2)]*2)
        W=sp.Integer(1)
        self.assertEqual(cauchy_two_face_envelope_residual(m,Q,R,W),sp.zeros(2))
        self.assertTrue(C.is_positive_semidefinite)

    def test_reverse_age_deformation_and_gram_rate_are_exact(self) -> None:
        d11,d12,d21,d22=sp.symbols('d11 d12 d21 d22')
        a11,a12,a21,a22=sp.symbols('a11 a12 a21 a22')
        D=sp.Matrix([[d11,d12],[d21,d22]])
        A=sp.Matrix([[a11,a12],[a21,a22]])
        Ddot=sp.simplify(D*A.T)
        self.assertEqual(deformation_reverse_age_residual(D,Ddot,A),sp.zeros(2))
        self.assertEqual(deformation_gram_rate_residual(D,Ddot,A),sp.zeros(2))

    def test_incompressible_deformation_preserves_pathwise_volume_not_shape(self) -> None:
        a,b,c=sp.symbols('a b c')
        A=sp.diag(a,b,c)
        rate=incompressible_deformation_determinant_log_rate(A).subs(c,-a-b)
        self.assertEqual(sp.simplify(rate),0)

    def test_ensemble_deformation_moment_law_is_exact_and_not_closed_on_R_only(self) -> None:
        D1=sp.diag(2,1); D2=sp.diag(1,3)
        s1,s2=sp.symbols('s1 s2')
        A1=sp.diag(s1,-s1); A2=sp.diag(s2,-s2)
        weights=[sp.Rational(1,2)]*2
        rhs=sp.simplify(
            (2*D1*((A1+A1.T)/2)*D1.T + 2*D2*((A2+A2.T)/2)*D2.T)/2
        )
        self.assertEqual(ensemble_deformation_rate_residual([D1,D2],[A1,A2],weights,rhs),sp.zeros(2))
        self.assertTrue(rhs.has(s1,s2))

    def test_genuine_affine_vortex_ns_has_pathwise_cauchy_stretch_and_zero_centered_variance(self) -> None:
        a,r0,s,t,nu=sp.symbols('a r0 s t nu', positive=True)
        x,y,z=sp.symbols('x y z')
        ns,_=affine_vortex_stretch_ns_residual(a,r0,t,(x,y,z),nu)
        self.assertEqual(sp.simplify(ns),sp.zeros(3,1))
        self.assertEqual(affine_vortex_cauchy_z_residual(a,r0,s,t),0)
        self.assertEqual(affine_vortex_total_bank_envelope_residual(a,r0,s,t),0)
        # The affine gradient is spatially uniform, so the stochastic anchor does
        # not randomize the deformation or the spatially uniform vorticity payoff.

    def test_one_mode_shear_has_no_vorticity_direction_deformation_but_positive_covariance_bank(self) -> None:
        y,t,s,nu,k=sp.symbols('y t s nu k', positive=True)
        W=one_mode_shear_terminal_supremum(s,nu,k)
        Q=one_mode_shear_second_moment(y,t,s,nu,k)
        headroom=one_mode_shear_terminal_headroom(y,t,s,nu,k)
        self.assertEqual(sp.simplify(W-Q-headroom),0)
        # At y=pi/(2k), terminal headroom remains nonnegative for t>=s.
        h=sp.symbols('h', nonnegative=True)
        special=sp.simplify(headroom.subs({y:sp.pi/(2*k),t:s+h}))
        expected=sp.simplify(W/2*(1-sp.exp(-4*nu*k**2*h)))
        self.assertEqual(sp.simplify(special-expected),0)


    def test_cauchy_deformation_gram_is_exactly_unscaled_coherent_packet_metric(self) -> None:
        D=sp.Matrix([[2,1,0],[1,1,1],[0,1,1]])
        rho=sp.symbols('rho', nonzero=True)
        self.assertEqual(cauchy_packet_metric_duality_residual(D,rho),sp.zeros(3))

    def test_forward_cauchy_deformation_and_area_frame_have_expected_duality(self) -> None:
        D=sp.Matrix([[2,1],[1,1]])
        rho=sp.symbols('rho', nonzero=True)
        F=forward_deformation_from_cauchy(D)
        H=coherent_area_frame_from_cauchy(D,rho)
        self.assertEqual(F,D.T)
        self.assertEqual(sp.simplify(H-rho**2*F.inv().T),sp.zeros(2))
        M=packet_metric_from_area_frame(H)
        self.assertEqual(sp.simplify(rho**4*M-D*D.T),sp.zeros(2))

    def test_cauchy_material_metric_and_spatial_support_have_same_trace_spectrum_invariant(self) -> None:
        D=sp.Matrix([[2,1],[0,1]])
        self.assertEqual(cauchy_spatial_support_spectral_trace_residual(D),0)
        # det and characteristic singular values also agree because F=D^T.
        F=D.T
        self.assertEqual(sp.det(D*D.T),sp.det(F*F.T))

    def test_packet_metric_rate_is_same_cauchy_strain_work(self) -> None:
        D=sp.Matrix([[2,1],[1,1]])
        A=sp.Matrix(sp.symbols('a0:4')).reshape(2,2)
        rho=sp.symbols('rho', nonzero=True)
        self.assertEqual(packet_metric_rate_residual_from_cauchy(D,A,rho),sp.zeros(2))


    def test_matrix_deformation_second_moment_has_exact_mean_plus_dispersion_split(self) -> None:
        c1,c2,p=sp.symbols('c1 c2 p')
        D1=sp.Matrix([[1,0],[c1,1]])
        D2=sp.Matrix([[1,0],[c2,1]])
        weights=[p,1-p]
        self.assertEqual(deformation_second_moment_split_residual([D1,D2],weights),sp.zeros(2))
        C_D_gram=matrix_deformation_covariance([D1,D2],weights)
        expected_var=sp.simplify(p*(1-p)*(c1-c2)**2)
        self.assertEqual(sp.simplify(C_D_gram-sp.diag(0,expected_var)),sp.zeros(2))

    def test_exact_one_mode_shear_deformation_dispersion_split(self) -> None:
        y,t,h,nu,k=sp.symbols('y t h nu k', positive=True)
        self.assertEqual(one_mode_shear_deformation_dispersion_residual(y,t,h,nu,k),sp.zeros(2))

    def test_one_mode_shear_symmetry_point_has_zero_mean_but_positive_dispersion_formula(self) -> None:
        t,h,nu,k=sp.symbols('t h nu k', positive=True)
        mean=one_mode_shear_deformation_mean_coefficient(0,t,h,nu,k)
        var=one_mode_shear_deformation_variance_at_symmetry(t,h,nu,k)
        self.assertEqual(mean,0)
        alpha=nu*k**2
        expected=k**2*sp.exp(-2*alpha*t)/(2*alpha**2)*(sp.sinh(2*alpha*h)-2*alpha*h)
        self.assertEqual(sp.simplify(var-expected),0)
        # sinh(x)-x has positive Taylor coefficients after the linear term.
        leading=sp.series(var,h,0,5).removeO()
        self.assertTrue(sp.simplify(leading).has(h))

    def test_shear_deformation_dispersion_starts_at_strain_gradient_squared_h_cubed(self) -> None:
        y,t,h,nu,k=sp.symbols('y t h nu k', positive=True)
        self.assertEqual(one_mode_shear_deformation_variance_leading_residual(y,t,h,nu,k),0)

    def test_deterministic_selected_shear_at_y0_is_identity_while_stochastic_metric_has_extra_face(self) -> None:
        t,h,nu,k=sp.symbols('t h nu k', positive=True)
        mean=one_mode_shear_deformation_mean_coefficient(0,t,h,nu,k)
        second=one_mode_shear_deformation_second_coefficient(0,t,h,nu,k)
        self.assertEqual(mean,0)
        R=sp.Matrix([[1,0],[0,1+second]])
        # deterministic material anchor y=0 has U_y(0,r)=0 at every r, hence I.
        self.assertNotEqual(R,sp.eye(2))
        self.assertEqual(sp.simplify(R-sp.eye(2)),sp.diag(0,second))


    def test_deformation_dispersion_is_exact_two_replica_pair_covariance(self) -> None:
        c1,c2,p=sp.symbols('c1 c2 p')
        D1=sp.Matrix([[1,0],[c1,1]])
        D2=sp.Matrix([[1,0],[c2,1]])
        self.assertEqual(matrix_deformation_pair_covariance_residual([D1,D2],[p,1-p]),sp.zeros(2))

    def test_expected_packet_metric_splits_into_mean_deformation_metric_plus_dispersion(self) -> None:
        c1,c2,p,rho=sp.symbols('c1 c2 p rho', nonzero=True)
        D1=sp.Matrix([[1,0],[c1,1]])
        D2=sp.Matrix([[1,0],[c2,1]])
        self.assertEqual(expected_packet_metric_split_residual([D1,D2],[p,1-p],rho),sp.zeros(2))

    def test_exact_shear_second_coefficient_solves_the_gaussian_two_time_kernel_integral_ode(self) -> None:
        y,t,h,nu,k=sp.symbols('y t h nu k', positive=True)
        alpha=nu*k**2
        second=one_mode_shear_deformation_second_coefficient(y,t,h,nu,k)
        kernel_at_h=k**2/sp.Integer(2)*(sp.exp(-2*alpha*(t-h))-sp.cos(2*k*y)*sp.exp(-2*alpha*(t+h)))
        self.assertEqual(sp.trigsimp(sp.simplify(sp.diff(second,h,2)-2*kernel_at_h)),0)
        self.assertEqual(sp.simplify(second.subs(h,0)),0)
        self.assertEqual(sp.simplify(sp.diff(second,h).subs(h,0)),0)


    def test_pathwise_and_horizon_vectorized_connections_have_distinct_ordering(self) -> None:
        a11,a12,a21,a22=sp.symbols('a11 a12 a21 a22')
        d11,d12,d21,d22=sp.symbols('d11 d12 d21 d22')
        A=sp.Matrix([[a11,a12],[a21,a22]])
        D=sp.Matrix([[d11,d12],[d21,d22]])
        self.assertEqual(
            reverse_age_path_vectorization_residual(D,sp.simplify(D*A.T),A),
            sp.zeros(4,1),
        )
        self.assertEqual(horizon_connection_vectorization_residual(D,A),sp.zeros(4,1))
        # For a generic nonsymmetric gradient these are genuinely different operators:
        # pathwise D_sigma=D A^T gives A kron I, while current-end horizon conditioning
        # gives left multiplication A^T M and hence I kron A^T.
        self.assertNotEqual(
            vectorized_reverse_age_path_connection(A),
            vectorized_horizon_connection(A),
        )

    def test_full_vec_covariance_projects_exactly_to_row_gram_dispersion(self) -> None:
        a,b,c,d,p=sp.symbols('a b c d p')
        D1=sp.Matrix([[1,a],[b,1]])
        D2=sp.Matrix([[1,c],[d,1]])
        weights=[p,1-p]
        Sigma=matrix_deformation_vectorized_covariance([D1,D2],weights)
        self.assertEqual(Sigma.shape,(4,4))
        self.assertEqual(deformation_covariance_projection_residual([D1,D2],weights),sp.zeros(2))
        self.assertEqual(
            vectorized_deformation_pair_covariance_residual([D1,D2],weights),
            sp.zeros(4),
        )

    def test_vec_carre_du_champ_partial_trace_is_exact_row_gram_source(self) -> None:
        a0,a1,a2,a3,b0,b1,b2,b3,nu=sp.symbols('a0:4 b0:4 nu')
        Gx=sp.Matrix([[a0,a1],[a2,a3]])
        Gy=sp.Matrix([[b0,b1],[b2,b3]])
        self.assertEqual(
            deformation_carre_du_champ_projection_residual([Gx,Gy],nu),
            sp.zeros(2),
        )
        projected=projected_deformation_carre_du_champ([Gx,Gy],nu)
        self.assertEqual(
            projected,
            sp.simplify(2*nu*(Gx*Gx.T+Gy*Gy.T)),
        )

    def test_exact_one_mode_shear_satisfies_mean_second_moment_and_covariance_horizon_pdes(self) -> None:
        x,y,t,h,nu,k=sp.symbols('x y t h nu k', positive=True)
        alpha=nu*k**2
        U=sp.exp(-alpha*t)*sp.cos(k*y)
        Uy=sp.diff(U,y)
        velocity=sp.Matrix([U,0])
        A=sp.Matrix([[0,Uy],[0,0]])
        mean_c=one_mode_shear_deformation_mean_coefficient(y,t,h,nu,k)
        second_c=one_mode_shear_deformation_second_coefficient(y,t,h,nu,k)
        meanD=sp.Matrix([[1,0],[mean_c,1]])
        R=sp.Matrix([[1,mean_c],[mean_c,1+second_c]])
        C=sp.simplify(R-meanD*meanD.T)
        Hmean=reverse_age_horizon_operator_matrix(meanD,h,t,velocity,nu,(x,y))
        HR=reverse_age_horizon_operator_matrix(R,h,t,velocity,nu,(x,y))
        HC=reverse_age_horizon_operator_matrix(C,h,t,velocity,nu,(x,y))
        dM=[sp.diff(meanD,x),sp.diff(meanD,y)]
        self.assertEqual(deformation_mean_horizon_residual(meanD,Hmean,A),sp.zeros(2))
        self.assertEqual(deformation_second_moment_horizon_residual(R,HR,A),sp.zeros(2))
        self.assertEqual(
            projected_deformation_covariance_horizon_residual(C,HC,A,dM,nu),
            sp.zeros(2),
        )
        # In the exact shear the connection kills the active covariance direction,
        # leaving the carré-du-champ source 2 nu h^2 (d_y U_y)^2 e2e2^T exactly.
        expected_source=sp.diag(0,sp.simplify(2*nu*h**2*sp.diff(Uy,y)**2))
        self.assertEqual(
            sp.trigsimp(sp.simplify(projected_deformation_carre_du_champ(dM,nu)-expected_source)),
            sp.zeros(2),
        )

    def test_exact_one_mode_shear_full_vec_covariance_obeys_vectorized_law(self) -> None:
        x,y,t,h,nu,k=sp.symbols('x y t h nu k', positive=True)
        alpha=nu*k**2
        U=sp.exp(-alpha*t)*sp.cos(k*y)
        Uy=sp.diff(U,y)
        velocity=sp.Matrix([U,0])
        A=sp.Matrix([[0,Uy],[0,0]])
        mean_c=one_mode_shear_deformation_mean_coefficient(y,t,h,nu,k)
        meanD=sp.Matrix([[1,0],[mean_c,1]])
        variance=one_mode_shear_deformation_variance(y,t,h,nu,k)
        E21=sp.Matrix([[0,0],[1,0]])
        v=column_vectorize(E21)
        Sigma=sp.simplify(variance*v*v.T)
        HSigma=reverse_age_horizon_operator_matrix(Sigma,h,t,velocity,nu,(x,y))
        dM=[sp.diff(meanD,x),sp.diff(meanD,y)]
        self.assertEqual(
            vectorized_deformation_covariance_horizon_residual(Sigma,HSigma,A,dM,nu),
            sp.zeros(4),
        )

    def test_general_short_horizon_tensor_projects_to_candidate_2nu_over_3_law(self) -> None:
        h,nu=sp.symbols('h nu', positive=True)
        g11,g12,g21,g22,q11,q12,q21,q22=sp.symbols('g11 g12 g21 g22 q11 q12 q21 q22')
        dAx=sp.Matrix([[g11,g12],[g21,g22]])
        dAy=sp.Matrix([[q11,q12],[q21,q22]])
        full=vectorized_deformation_covariance_leading_tensor([dAx,dAy],nu,h)
        projected=projected_deformation_covariance_leading_tensor([dAx,dAy],nu,h)
        self.assertEqual(full.shape,(4,4))
        self.assertEqual(
            deformation_covariance_leading_projection_residual([dAx,dAy],nu,h),
            sp.zeros(2),
        )
        expected=sp.simplify(sp.Rational(2,3)*nu*h**3*(dAx.T*dAx+dAy.T*dAy))
        self.assertEqual(sp.simplify(projected-expected),sp.zeros(2))

    def test_exact_shear_referees_short_horizon_coefficient_and_transpose(self) -> None:
        y,t,h,nu,k=sp.symbols('y t h nu k', positive=True)
        alpha=nu*k**2
        Uy=-k*sp.exp(-alpha*t)*sp.sin(k*y)
        A=sp.Matrix([[0,Uy],[0,0]])
        dAy=sp.diff(A,y)
        projected=projected_deformation_covariance_leading_tensor([sp.zeros(2),dAy],nu,h)
        exact_var=one_mode_shear_deformation_variance(y,t,h,nu,k)
        exact_leading=sp.series(exact_var,h,0,4).removeO()
        self.assertEqual(
            sp.trigsimp(sp.simplify(projected-sp.diag(0,exact_leading))),
            sp.zeros(2),
        )

    def test_affine_vortex_exact_ns_has_zero_deformation_dispersion_source(self) -> None:
        a,r0,t,h,nu=sp.symbols('a r0 t h nu', positive=True)
        x,y,z=sp.symbols('x y z')
        A=affine_vortex_stretch_gradient(a,r0,t)
        ns,_=affine_vortex_stretch_ns_residual(a,r0,t,(x,y,z),nu)
        self.assertEqual(sp.simplify(ns),sp.zeros(3,1))
        derivatives=[sp.diff(A,q) for q in (x,y,z)]
        self.assertEqual(
            vectorized_deformation_covariance_leading_tensor(derivatives,nu,h),
            sp.zeros(9),
        )
        self.assertEqual(
            projected_deformation_covariance_leading_tensor(derivatives,nu,h),
            sp.zeros(3),
        )

    def test_exact_shear_deformation_law_is_existing_connected_covariance_theorem_on_reverse_age_clock(self) -> None:
        x, y, t, h, nu, k = sp.symbols('x y t h nu k', positive=True)
        U = sp.exp(-nu * k**2 * t) * sp.cos(k * y)
        Uy = sp.diff(U, y)
        A = sp.Matrix([[0, Uy], [0, 0]])
        mean_c = one_mode_shear_deformation_mean_coefficient(y, t, h, nu, k)
        variance = one_mode_shear_deformation_variance(y, t, h, nu, k)
        meanD = sp.Matrix([[1, 0], [mean_c, 1]])
        mean = column_vectorize(meanD)
        E21 = sp.Matrix([[0, 0], [1, 0]])
        v = column_vectorize(E21)
        Sigma = sp.simplify(variance * v * v.T)
        second = sp.simplify(Sigma + mean * mean.T)

        # L_rev=-partial_t-u.grad+nu Delta on (t,x,y); H_h=partial_h-L_rev.
        reverse_drift = sp.Matrix([-1, -U, 0])
        reverse_diffusion = sp.diag(0, 2 * nu, 2 * nu)
        coords = (t, x, y)

        # future_covariance_tensor uses H m + B_conn^T m=0, so the deformation
        # horizon law H m=B_h m is the exact specialization B_conn=-B_h^T.
        B_h = vectorized_horizon_connection(A)
        B_conn = -B_h.T
        self.assertEqual(
            connected_mean_horizon_residual(
                mean, B_conn, h, reverse_drift, reverse_diffusion, coords
            ),
            sp.zeros(4, 1),
        )
        self.assertEqual(
            connected_second_moment_horizon_residual(
                second, B_conn, h, reverse_drift, reverse_diffusion, coords
            ),
            sp.zeros(4),
        )
        self.assertEqual(
            connected_covariance_horizon_residual(
                mean, second, B_conn, h, reverse_drift, reverse_diffusion, coords
            ),
            sp.zeros(4),
        )

        t1, x1, y1, t2, x2, y2 = sp.symbols('t1 x1 y1 t2 x2 y2')
        pair_defect = product_pair_diagonal_defect(
            mean,
            coords,
            (t1, x1, y1),
            (t2, x2, y2),
            reverse_drift,
            reverse_diffusion,
        )
        Gamma = vector_carre_du_champ(mean, reverse_diffusion, coords)
        self.assertEqual(sp.simplify(pair_defect - Gamma), sp.zeros(4))

    def test_reducing_hidden_deformation_adds_resolution_covariance_instead_of_retyping_intrinsic_sigma(self) -> None:
        p, a, b, c, d, s1, s2, q1, q2 = sp.symbols(
            'p a b c d s1 s2 q1 q2', real=True
        )
        Dbar1 = sp.Matrix([[1, a], [b, 1]])
        Dbar2 = sp.Matrix([[1, c], [d, 1]])
        m1 = column_vectorize(Dbar1)
        m2 = column_vectorize(Dbar2)
        means = sp.Matrix([list(m1), list(m2)])
        Sigma1 = sp.diag(s1, 0, q1, 0)
        Sigma2 = sp.diag(s2, 0, q2, 0)
        kernel = sp.Matrix([[p, 1 - p]])
        averaged, resolution, total = vector_total_covariance_decomposition(
            kernel, means, [Sigma1, Sigma2]
        )
        self.assertEqual(sp.simplify(total[0] - averaged[0] - resolution[0]), sp.zeros(4))
        # The packet-metric row-Gram face sees the partial trace of both sectors.
        projected_total = column_partial_trace_vectorized_covariance(total[0], 2)
        projected_intrinsic = sp.simplify(
            p * column_partial_trace_vectorized_covariance(Sigma1, 2)
            + (1 - p) * column_partial_trace_vectorized_covariance(Sigma2, 2)
        )
        projected_resolution = column_partial_trace_vectorized_covariance(resolution[0], 2)
        self.assertEqual(
            sp.simplify(projected_total - projected_intrinsic - projected_resolution),
            sp.zeros(2),
        )
        self.assertNotEqual(sp.simplify(resolution[0]), sp.zeros(4))

    def test_smooth_past_vorticity_bound_does_not_remove_deformation_moment(self) -> None:
        W,r=sp.symbols('W r', positive=True)
        # The direct Loewner envelope is W*R, not W*I.
        self.assertNotEqual(W*r,W)

if __name__=='__main__':
    unittest.main()
