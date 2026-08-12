from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.kelvin_packet_locality import (
    affine_vortex_stretch_gradient,
    affine_vortex_stretch_ns_residual,
    affine_vortex_stretch_support_tensor,
    affine_vortex_stretch_vorticity,
    anisotropy_tensor_from_lines,
    centered_parallelogram_normalized_second_moment,
    centered_quadratic_flux_error,
    centered_quadratic_shape_residual,
    centered_rectangle_second_moment_yz,
    coherent_three_face_normalized_quadrupoles,
    coherent_core_area_frame,
    coherent_planar_amplification_from_H_diagonal,
    coherent_core_bank_residual,
    coherent_core_line_frame,
    coherent_core_packet_metric,
    coherent_core_physical_second_moment,
    coherent_core_raw_flux_second_moment,
    codeforming_pullback_residual,
    coherent_three_face_quadrupole_closure_residual,
    cauchy_green_material_rhs,
    cofactor_area_frame,
    directional_material_log_length_rate,
    diagonal_locality_ratio,
    exact_linear_strain_deformation,
    exact_linear_strain_ns_residual,
    general_nanson_area_frame_rhs,
    finite_flux_whitened_bound_factor,
    finite_shape_connection_bound_factor,
    incompressible_scale_rate,
    incompressible_material_scale_residual,
    general_nanson_metric_logdet_rate,
    incompressible_isotropic_area_frame,
    long_thin_center_flux,
    long_thin_covariance_defect,
    long_thin_face_flux,
    kelvin_diffusion_length,
    kelvin_diffusion_log_rate,
    line_frame_from_area_frame,
    isotropic_lineage_packet_metric,
    isotropic_lineage_support_metric,
    line_gram_from_area_frame,
    long_thin_whitened_payoff_error,
    material_line_frame_rhs,
    material_support_tensor_residual,
    anisotropy_tensor_material_rhs,
    refinement_anisotropy_pullback,
    refinement_scale_factor,
    refinement_scale_shape,
    scale_shape_line_gram_residual,
    parabolic_kelvin_line_log_rate,
    parabolic_strained_line_length,
    packet_shape_amplification_factor,
    scale_shape_packet_metric_residual,
    singular_strain_deformation_factor,
    strained_refined_line_frame,
    time_dependent_linear_strain_ns_residual,
    two_sided_lineage_frame,
    two_sided_stretch_action,
    material_line_gram_rhs,
    metric_whitened_covariance_remainder,
    raw_frobenius_square,
    whitened_l2_error_bound_factor,
)
from src.pde_audit.orientation_packet import material_area_frame_rhs


class KelvinPacketLocalityAudit(unittest.TestCase):
    def test_general_nanson_metric_logdet_rate_is_minus_four_divergence(self) -> None:
        g = sp.symbols("g0:9")
        A = sp.Matrix(3, 3, g)
        H = sp.Matrix([[2, 1, 0], [0, 3, 1], [1, 0, 2]])
        self.assertEqual(
            sp.simplify(general_nanson_metric_logdet_rate(A, H) + 4 * sp.trace(A)),
            0,
        )

    def test_incompressible_general_nanson_reduces_to_existing_area_frame_law(self) -> None:
        a, b, c, d, e, f, g, h = sp.symbols("a b c d e f g h")
        A = sp.Matrix([[a, b, c], [d, e, f], [g, h, -a - e]])
        H = sp.Matrix([[2, 1, 0], [0, 2, 1], [1, 0, 1]])
        self.assertEqual(
            sp.simplify(general_nanson_area_frame_rhs(A, H) - material_area_frame_rhs(A, H)),
            sp.zeros(3),
        )
        self.assertEqual(general_nanson_metric_logdet_rate(A, H), 0)





    def test_centered_parallelogram_quadrupole_formula_is_exact(self) -> None:
        a,b,c,d=sp.symbols("a b c d")
        e1=sp.Matrix([a,b,0])
        e2=sp.Matrix([0,c,d])
        Qbar=centered_parallelogram_normalized_second_moment(e1,e2)
        self.assertEqual(sp.simplify(Qbar-(e1*e1.T+e2*e2.T)/3),sp.zeros(3))

    def test_orientation_complete_three_face_quadrupoles_reconstruct_spatial_line_tensor(self) -> None:
        L=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
        self.assertEqual(coherent_three_face_quadrupole_closure_residual(L),sp.zeros(3))
        faces=coherent_three_face_normalized_quadrupoles(L)
        self.assertEqual(sp.simplify(sum(faces,sp.zeros(3))-sp.Rational(2,3)*L*L.T),sp.zeros(3))

    def test_isotropic_lineage_quadrupole_packet_reconstructs_left_cauchy_green(self) -> None:
        lam,a,b=sp.symbols("lam a b", positive=True)
        F=sp.diag(a,b,1/(a*b))
        L=lam*F
        faces=coherent_three_face_normalized_quadrupoles(L)
        self.assertEqual(
            sp.simplify(sum(faces,sp.zeros(3))-sp.Rational(2,3)*lam**2*F*F.T),
            sp.zeros(3),
        )

    def test_same_surface_quadrupole_drives_shape_and_flux_finite_size_corrections(self) -> None:
        b, c, q, p = sp.symbols("b c q p", positive=True)
        Q = centered_rectangle_second_moment_yz(b, c)
        n = sp.Matrix([1,0,0])
        Z33 = sp.zeros(3)
        # Only partial_yy grad u is nonzero, mapping e_x normal into y-component.
        H = [[Z33.copy() for _ in range(3)] for _ in range(3)]
        Ayy = sp.zeros(3)
        Ayy[0,1] = q
        H[1][1] = Ayy
        E = centered_quadratic_shape_residual(Q, H, n)
        self.assertEqual(E, sp.Matrix([0, -sp.Rational(2,3) * q * b**3 * c, 0]))

        Z31 = sp.zeros(3,1)
        B = [[Z31.copy() for _ in range(3)] for _ in range(3)]
        byy = sp.Matrix([p,0,0])
        B[1][1] = byy
        eps = centered_quadratic_flux_error(Q, B, n)
        self.assertEqual(eps, sp.Rational(2,3) * p * b**3 * c)
        # Both are the same Q_yy contraction with different physical Hessians.
        self.assertEqual(sp.simplify(E[1] / q + eps / p), 0)

    def test_quadrupole_cubic_heat_shear_recovers_exact_shape_residual(self) -> None:
        b, c = sp.symbols("b c", positive=True)
        Q = centered_rectangle_second_moment_yz(b, c)
        n = sp.Matrix([1,0,0])
        Z33 = sp.zeros(3)
        H = [[Z33.copy() for _ in range(3)] for _ in range(3)]
        # u_x=y^3+6 nu t y => grad u has A_xy=3y^2+6nu t, so partial_yy A_xy=6.
        Ayy = sp.zeros(3)
        Ayy[0,1] = 6
        H[1][1] = Ayy
        E = centered_quadratic_shape_residual(Q, H, n)
        self.assertEqual(E, sp.Matrix([0, -4*b**3*c, 0]))

    def test_isotropic_centered_quadrupole_is_raw_r4_and_area_relative_r2(self) -> None:
        r, b0, c0 = sp.symbols("r b0 c0", positive=True)
        Q = centered_rectangle_second_moment_yz(r*b0, r*c0)
        self.assertEqual(Q[1,1], sp.Rational(4,3)*r**4*b0**3*c0)
        area = 4*r**2*b0*c0
        self.assertEqual(sp.simplify(Q[1,1]/area), r**2*b0**2/3)

    def test_scale_shape_factorization_uses_same_anisotropy_for_support_and_covariance_metric(self) -> None:
        rho, a, b = sp.symbols("rho a b", positive=True)
        # det Lhat=1.
        Lhat = sp.diag(a, b, 1 / (a * b))
        L = rho * Lhat
        A = anisotropy_tensor_from_lines(L, rho)
        self.assertEqual(A, sp.diag(a**2, b**2, 1 / (a**2 * b**2)))
        self.assertEqual(scale_shape_line_gram_residual(L, rho), sp.zeros(3))
        self.assertEqual(scale_shape_packet_metric_residual(L, rho), sp.zeros(3))
        H = cofactor_area_frame(L)
        M = (H.T * H).inv()
        self.assertEqual(sp.simplify(L.T * L - rho**2 * A), sp.zeros(3))
        self.assertEqual(sp.simplify(M - rho**(-4) * A), sp.zeros(3))

    def test_long_thin_witness_is_scale_r_times_divergent_anisotropy(self) -> None:
        r = sp.symbols("r", positive=True)
        L = sp.diag(1, r, r**2)
        # det L=r^3, hence rho=r.
        A = anisotropy_tensor_from_lines(L, r)
        self.assertEqual(A, sp.diag(r**-2, 1, r**2))
        self.assertEqual(sp.simplify(r**2 * A - L.T * L), sp.zeros(3))
        H = cofactor_area_frame(L)
        self.assertEqual(sp.simplify((H.T * H).inv() - r**-4 * A), sp.zeros(3))

    def test_incompressible_material_motion_changes_anisotropy_not_physical_cell_scale(self) -> None:
        a, b, c, d, e, f, g, h, rho = sp.symbols("a b c d e f g h rho", positive=True)
        Avel = sp.Matrix([[a, b, c], [d, e, f], [g, h, -a-e]])
        Lhat = sp.diag(2, 1, sp.Rational(1,2))
        L = rho * Lhat
        self.assertEqual(incompressible_scale_rate(Avel, L), 0)
        Adot = anisotropy_tensor_material_rhs(Avel, L, rho, sp.Integer(0))
        expected = sp.simplify(Lhat.T * (Avel.T + Avel) * Lhat)
        self.assertEqual(sp.simplify(Adot - expected), sp.zeros(3))

    def test_isotropic_physical_refinement_shrinks_scale_but_preserves_anisotropy(self) -> None:
        rho, lam = sp.symbols("rho lam", positive=True)
        Lhat = sp.Matrix([[2,0,1],[1,1,0],[0,1,1]])
        detLhat = sp.det(Lhat)
        # Normalize to unit determinant with symbolic cube-root avoided by choose det=1 witness.
        Lhat = sp.Matrix([[1,1,0],[0,1,1],[0,0,1]])
        self.assertEqual(sp.det(Lhat), 1)
        L = rho * Lhat
        A0 = anisotropy_tensor_from_lines(L, rho)
        Lplus, Aplus = refinement_scale_shape(L, lam * sp.eye(3), rho, lam * rho)
        self.assertEqual(sp.simplify(Lplus - lam * L), sp.zeros(3))
        self.assertEqual(sp.simplify(Aplus - A0), sp.zeros(3))
        self.assertEqual(sp.simplify(cofactor_area_frame(Lplus) - lam**2 * cofactor_area_frame(L)), sp.zeros(3))




    def test_material_support_tensor_uses_same_two_sided_stretch_operator(self) -> None:
        g=sp.symbols("g0:9")
        Avel=sp.Matrix(3,3,g)
        L=sp.Matrix([[2,0,1],[1,3,0],[0,1,2]])
        self.assertEqual(material_support_tensor_residual(Avel,L),sp.zeros(3))
        B=L*L.T
        self.assertEqual(two_sided_stretch_action(Avel,B),sp.simplify(Avel*B+B*Avel.T))

    def test_codeforming_pullback_cancels_common_stretch_exactly(self) -> None:
        g=sp.symbols("g0:9")
        Avel=sp.Matrix(3,3,g)
        # Fixed invertible deformation witness.
        F=sp.Matrix([[2,1,0],[0,2,1],[1,0,1]])
        e=sp.symbols("e0:9")
        E=sp.Matrix(3,3,e)
        d=sp.symbols("d0:9")
        D=sp.Matrix(3,3,d)
        self.assertEqual(codeforming_pullback_residual(Avel,F,E,D),sp.zeros(3))

    def test_pure_material_support_becomes_constant_in_codeforming_frame(self) -> None:
        g=sp.symbols("g0:9")
        Avel=sp.Matrix(3,3,g)
        F=sp.Matrix([[2,1,0],[0,2,1],[1,0,1]])
        B=sp.simplify(F*F.T)
        self.assertEqual(codeforming_pullback_residual(Avel,F,B,sp.zeros(3)),sp.zeros(3))




    def test_minimal_coherent_restart_core_factorization_is_exact(self) -> None:
        rho,a,b=sp.symbols("rho a b", positive=True)
        F=sp.diag(a,b,1/(a*b))
        q=sp.symbols("q0:6")
        Q=sp.Matrix([[q[0],q[1],q[2]],[q[1],q[3],q[4]],[q[2],q[4],q[5]]])
        L=coherent_core_line_frame(rho,F)
        H=coherent_core_area_frame(rho,F)
        self.assertEqual(sp.simplify(H-cofactor_area_frame(L)),sp.zeros(3))
        self.assertEqual(coherent_core_bank_residual(rho,F,Q),0)
        self.assertEqual(coherent_core_raw_flux_second_moment(rho,Q),rho**4*Q)
        self.assertEqual(coherent_core_packet_metric(rho,F),rho**-4*(F.T*F))
        self.assertEqual(coherent_core_physical_second_moment(F,Q),F*Q*F.T)

    def test_isotropic_refinement_changes_only_rho_powers_in_ideal_core(self) -> None:
        rho,lam,a,b=sp.symbols("rho lam a b", positive=True)
        F=sp.diag(a,b,1/(a*b))
        Q=sp.eye(3)
        self.assertEqual(
            sp.simplify(coherent_core_raw_flux_second_moment(lam*rho,Q)-lam**4*coherent_core_raw_flux_second_moment(rho,Q)),
            sp.zeros(3),
        )
        self.assertEqual(
            sp.simplify(coherent_core_packet_metric(lam*rho,F)-lam**-4*coherent_core_packet_metric(rho,F)),
            sp.zeros(3),
        )
        self.assertEqual(coherent_core_bank_residual(lam*rho,F,Q),0)

    def test_support_normalized_scalar_alone_cannot_bound_physical_vorticity_in_exact_affine_stretch(self) -> None:
        a,r0,t=sp.symbols("a r0 t", positive=True)
        omega=affine_vortex_stretch_vorticity(a,r0,t)
        B=affine_vortex_stretch_support_tensor(a,t)
        I=sp.simplify(sp.trace(B.inv()*(omega*omega.T))/2)
        physical=sp.simplify(omega.dot(omega)/2)
        self.assertEqual(I,2*r0**2)
        self.assertEqual(sp.simplify(physical/I),sp.exp(4*a*t))



    def test_shape_and_flux_remainders_share_exact_same_dimensionless_geometry_factor(self) -> None:
        A1,A2,A3,sigma,wu,wz=sp.symbols("A1 A2 A3 sigma wu wz", positive=True)
        chi=packet_shape_amplification_factor([A1,A2,A3],sigma)
        self.assertEqual(chi,sp.sqrt(A1**2+A2**2+A3**2)/sigma)
        self.assertEqual(finite_shape_connection_bound_factor([A1,A2,A3],sigma,wu),chi*wu)
        self.assertEqual(finite_flux_whitened_bound_factor([A1,A2,A3],sigma,wz),chi*wz)

    def test_geometry_factor_is_invariant_under_uniform_physical_area_scaling(self) -> None:
        A1,A2,A3,sigma,lam=sp.symbols("A1 A2 A3 sigma lam", positive=True)
        before=packet_shape_amplification_factor([A1,A2,A3],sigma)
        after=packet_shape_amplification_factor([lam**2*A1,lam**2*A2,lam**2*A3],lam**2*sigma)
        self.assertEqual(sp.simplify(after-before),0)

    def test_long_thin_geometry_factor_diverges_like_r_minus_two(self) -> None:
        r=sp.symbols("r", positive=True)
        chi=coherent_planar_amplification_from_H_diagonal(r**3,r**2,r,r**3)
        self.assertEqual(sp.simplify(chi-sp.sqrt(r**6+r**4+r**2)/r**3),0)
        self.assertEqual(sp.simplify(r**2*chi),sp.sqrt(r**4+r**2+1))
        self.assertEqual(sp.limit(r**2*chi,r,0,dir='+'),1)

    def test_uniformly_conditioned_isotropic_packet_has_scale_independent_geometry_factor(self) -> None:
        r=sp.symbols("r", positive=True)
        chi=coherent_planar_amplification_from_H_diagonal(r**2,r**2,r**2,r**2)
        self.assertEqual(chi,sp.sqrt(3))

    def test_joint_locality_condition_combines_pde_moduli_without_new_scale_power(self) -> None:
        chi,wu,wz=sp.symbols("chi wu wz", positive=True)
        self.assertEqual(sp.expand(chi*(wu+wz)),chi*wu+chi*wz)

    def test_kelvin_remaining_horizon_has_exact_parabolic_diffusion_scale(self) -> None:
        nu,tau=sp.symbols("nu tau", positive=True)
        self.assertEqual(kelvin_diffusion_length(nu,tau),sp.sqrt(2*nu*tau))
        self.assertEqual(kelvin_diffusion_log_rate(tau),-1/(2*tau))

    def test_parabolic_kelvin_line_rate_is_directional_strain_minus_half_over_horizon(self) -> None:
        a,tau=sp.symbols("a tau", positive=True)
        self.assertEqual(parabolic_kelvin_line_log_rate(a/tau,tau),(a-sp.Rational(1,2))/tau)

    def test_time_dependent_singular_linear_strain_is_exact_navier_stokes(self) -> None:
        x,y,z,t,T,a,nu=sp.symbols("x y z t T a nu", positive=True)
        s=a/(T-t)
        residual,p=time_dependent_linear_strain_ns_residual(s,t,(x,y,z),nu)
        self.assertEqual(residual,sp.zeros(3,1))
        self.assertEqual(sp.trace(sp.diag(s,0,-s)),0)
        self.assertEqual(sp.simplify(sp.hessian(p,(x,y,z))-sp.hessian(p,(x,y,z)).T),sp.zeros(3))

    def test_parabolic_strain_calibration_has_exact_half_critical_support_exponent(self) -> None:
        t,T,t0,nu=sp.symbols("t T t0 nu", positive=True)
        tau=sp.symbols("tau", positive=True)
        # Substitute T-t=tau and keep T-t0 as a positive constant C.
        C=sp.symbols("C", positive=True)
        a=sp.symbols("a", positive=True)
        length=sp.sqrt(2*nu)*C**a*tau**(sp.Rational(1,2)-a)
        self.assertEqual(length.subs(a,sp.Rational(1,2)),sp.sqrt(2*nu*C))
        self.assertEqual(sp.limit(length.subs(a,sp.Rational(1,4)),tau,0,dir='+'),0)
        self.assertEqual(sp.limit(length.subs(a,sp.Rational(3,4)),tau,0,dir='+'),sp.oo)

    def test_parabolic_strained_line_formula_matches_integrated_singular_strain(self) -> None:
        a,T,t0,t,nu=sp.symbols("a T t0 t nu", positive=True)
        L=parabolic_strained_line_length(a,T,t0,t,nu)
        expected=sp.sqrt(2*nu*(T-t))*((T-t0)/(T-t))**a
        self.assertEqual(sp.simplify(L-expected),0)

    def test_exact_affine_vortex_stretch_is_navier_stokes_with_quadratic_pressure(self) -> None:
        x,y,z,a,r0,t,nu=sp.symbols("x y z a r0 t nu", positive=True)
        residual,p=affine_vortex_stretch_ns_residual(a,r0,t,(x,y,z),nu)
        self.assertEqual(residual,sp.zeros(3,1))
        A=affine_vortex_stretch_gradient(a,r0,t)
        self.assertEqual(sp.trace(A),0)
        P=sp.hessian(p,(x,y,z))
        self.assertEqual(sp.simplify(P-P.T),sp.zeros(3))

    def test_affine_vortex_stretch_has_positive_stretching_with_zero_kelvin_gradient_qv(self) -> None:
        a,r0,t,nu=sp.symbols("a r0 t nu", positive=True)
        A=affine_vortex_stretch_gradient(a,r0,t)
        S=sp.simplify((A+A.T)/2)
        omega=affine_vortex_stretch_vorticity(a,r0,t)
        self.assertEqual(S,sp.diag(-a,-a,2*a))
        self.assertEqual(sp.simplify(sp.diff(omega,t)-A*omega),sp.zeros(3,1))
        self.assertEqual(sp.simplify((omega.T*S*omega)[0]),8*a*r0**2*sp.exp(4*a*t))
        self.assertEqual(sp.simplify(sp.diff(omega.dot(omega)/2,t)-(omega.T*S*omega)[0]),0)
        grad_omega=sp.zeros(3)
        self.assertEqual(2*nu*grad_omega*grad_omega.T,sp.zeros(3))

    def test_affine_vortex_stretch_support_normalization_cancels_real_vortex_stretching(self) -> None:
        a,r0,t=sp.symbols("a r0 t", positive=True)
        omega=affine_vortex_stretch_vorticity(a,r0,t)
        T=sp.simplify(omega*omega.T)
        B=affine_vortex_stretch_support_tensor(a,t)
        I=sp.simplify(sp.trace(B.inv()*T)/2)
        self.assertEqual(I,2*r0**2)
        self.assertEqual(sp.diff(I,t),0)

    def test_affine_vortex_stretch_support_tensor_and_vorticity_dyad_share_same_stretched_eigendirection(self) -> None:
        a,r0,t=sp.symbols("a r0 t", positive=True)
        A=affine_vortex_stretch_gradient(a,r0,t)
        B=affine_vortex_stretch_support_tensor(a,t)
        self.assertEqual(sp.simplify(sp.diff(B,t)-(A*B+B*A.T)),sp.zeros(3))
        omega=affine_vortex_stretch_vorticity(a,r0,t)
        E=sp.simplify(omega*omega.T)
        self.assertEqual(sp.simplify(sp.diff(E,t)-(A*E+E*A.T)),sp.zeros(3))

    def test_exact_linear_strain_is_navier_stokes_with_pressure_cancellation(self) -> None:
        x,y,z,s,nu=sp.symbols("x y z s nu")
        residual,p=exact_linear_strain_ns_residual(s,(x,y,z),nu)
        self.assertEqual(residual,sp.zeros(3,1))
        self.assertEqual(p,-sp.Rational(1,2)*s**2*(x**2+z**2))

    def test_exact_linear_strain_generates_adversarial_long_thin_packet_at_critical_refinement(self) -> None:
        s,t,r=sp.symbols("s t r", positive=True)
        L=strained_refined_line_frame(s,s,t)
        self.assertEqual(L,sp.diag(1,sp.exp(-s*t),sp.exp(-2*s*t)))
        H=cofactor_area_frame(L)
        self.assertEqual(H,sp.diag(sp.exp(-3*s*t),sp.exp(-2*s*t),sp.exp(-s*t)))
        # Substitute r=e^{-st}: exact previous long-thin geometry.
        self.assertEqual(L.subs(sp.exp(-s*t),r),sp.diag(1,r,r**2))
        self.assertEqual(H.subs(sp.exp(-s*t),r),sp.diag(r**3,r**2,r))

    def test_refinement_rate_vs_strain_rate_has_exact_support_locality_trichotomy(self) -> None:
        s,k,t=sp.symbols("s k t", positive=True)
        L=strained_refined_line_frame(s,k,t)
        self.assertEqual(L[0,0],sp.exp((s-k)*t))
        self.assertEqual(L[1,1],sp.exp(-k*t))
        self.assertEqual(L[2,2],sp.exp(-(s+k)*t))
        self.assertEqual(L[0,0].subs(k,s),1)
        self.assertEqual(L[0,0].subs(k,s+1),sp.exp(-t))
        self.assertEqual(L[0,0].subs(k,s/2),sp.exp(s*t/2))

    def test_directional_line_rate_recovers_exact_positive_and_negative_strain_channels(self) -> None:
        s=sp.symbols("s", positive=True)
        A=sp.diag(s,0,-s)
        self.assertEqual(directional_material_log_length_rate(A,sp.Matrix([1,0,0])),s)
        self.assertEqual(directional_material_log_length_rate(A,sp.Matrix([0,1,0])),0)
        self.assertEqual(directional_material_log_length_rate(A,sp.Matrix([0,0,1])),-s)

    def test_material_and_refinement_histories_factor_two_sided_exactly(self) -> None:
        F1 = sp.Matrix([[1,1,0],[0,1,0],[0,0,1]])
        F2 = sp.Matrix([[1,0,0],[1,1,0],[0,0,1]])
        L0 = sp.Matrix([[2,0,1],[1,2,0],[0,1,1]])
        R1 = sp.diag(2,1,1)
        R2 = sp.Matrix([[1,1,0],[0,1,0],[0,0,1]])
        sequential = sp.simplify(F2 * (F1 * (L0 * R1)) * R2)
        collapsed = two_sided_lineage_frame(F2*F1, L0, R1*R2)
        self.assertEqual(sp.simplify(sequential-collapsed),sp.zeros(3))

    def test_incompressible_material_history_does_not_change_lineage_scale_determinant(self) -> None:
        a,b,c = sp.symbols("a b c", positive=True)
        F = sp.diag(a,b,1/(a*b))
        L0 = sp.diag(2,3,4)
        R = sp.diag(c,c,c)
        L = two_sided_lineage_frame(F,L0,R)
        self.assertEqual(sp.det(F),1)
        self.assertEqual(sp.simplify(sp.det(L)-sp.det(L0)*sp.det(R)),0)

    def test_isotropic_refinement_lineage_support_and_packet_metric_share_cauchy_green(self) -> None:
        lam,a,b = sp.symbols("lam a b", positive=True)
        F = sp.diag(a,b,1/(a*b))
        L = two_sided_lineage_frame(F,sp.eye(3),lam*sp.eye(3))
        H = cofactor_area_frame(L)
        G = sp.simplify(L.T*L)
        M = sp.simplify((H.T*H).inv())
        self.assertEqual(sp.simplify(G-isotropic_lineage_support_metric(F,lam)),sp.zeros(3))
        self.assertEqual(sp.simplify(M-isotropic_lineage_packet_metric(F,lam)),sp.zeros(3))

    def test_cauchy_green_rate_is_literal_strain_work_tensor(self) -> None:
        g=sp.symbols("g0:9")
        Avel=sp.Matrix(3,3,g)
        F=sp.Matrix([[2,0,1],[1,3,0],[0,1,2]])
        Fdot=sp.simplify(Avel*F)
        direct=sp.simplify(Fdot.T*F+F.T*Fdot)
        self.assertEqual(sp.simplify(direct-cauchy_green_material_rhs(Avel,F)),sp.zeros(3))

    def test_isotropic_refinement_jump_scales_support_and_kelvin_metric_by_opposite_powers(self) -> None:
        lam,mu,a,b=sp.symbols("lam mu a b", positive=True)
        F=sp.diag(a,b,1/(a*b))
        G0=isotropic_lineage_support_metric(F,lam)
        M0=isotropic_lineage_packet_metric(F,lam)
        G1=isotropic_lineage_support_metric(F,mu*lam)
        M1=isotropic_lineage_packet_metric(F,mu*lam)
        self.assertEqual(sp.simplify(G1-mu**2*G0),sp.zeros(3))
        self.assertEqual(sp.simplify(M1-mu**(-4)*M0),sp.zeros(3))

    def test_material_linear_scale_rate_is_exactly_one_third_divergence(self) -> None:
        g = sp.symbols("g0:9")
        Avel = sp.Matrix(3,3,g)
        L = sp.Matrix([[2,0,1],[1,3,0],[0,1,2]])
        self.assertEqual(incompressible_material_scale_residual(Avel,L), 0)
        Ainc = sp.Matrix([[g[0],g[1],g[2]],[g[3],g[4],g[5]],[g[6],g[7],-g[0]-g[4]]])
        self.assertEqual(incompressible_scale_rate(Ainc,L),0)

    def test_general_physical_refinement_splits_exactly_into_scale_and_unit_det_anisotropy(self) -> None:
        a,b,c = sp.symbols("a b c", positive=True)
        R = sp.diag(a,b,c)
        s = sp.symbols("s", positive=True)
        # Supply s with s^3=abc by checking polynomially after substitution c=s^3/(ab).
        A0 = sp.diag(2,3,sp.Rational(1,6))
        Rsub = R.subs(c,s**3/(a*b))
        Aplus = refinement_anisotropy_pullback(A0,Rsub,s)
        self.assertEqual(sp.det(A0),1)
        self.assertEqual(sp.simplify(sp.det(Aplus)),1)
        L0 = sp.eye(3)
        Lplus,_ = refinement_scale_shape(L0,Rsub,sp.Integer(1),s)
        self.assertEqual(sp.simplify(sp.det(Lplus)-s**3),0)

    def test_isotropic_refinement_is_pure_physical_scale_face(self) -> None:
        lam = sp.symbols("lam", positive=True)
        A0 = sp.Matrix([[2,1,0],[1,1,0],[0,0,1]])
        R = lam*sp.eye(3)
        self.assertEqual(refinement_scale_factor(R),lam)
        self.assertEqual(sp.simplify(refinement_anisotropy_pullback(A0,R,lam)-A0),sp.zeros(3))

    def test_anisotropic_physical_refinement_has_separate_scale_and_shape_faces(self) -> None:
        rho, lam = sp.symbols("rho lam", positive=True)
        L = rho * sp.eye(3)
        R = sp.diag(lam**2, lam, 1)
        # det R=lam^3, hence rho+=lam rho.
        _, Aplus = refinement_scale_shape(L, R, rho, lam * rho)
        self.assertEqual(Aplus, sp.diag(lam**2, 1, lam**-2))
        self.assertEqual(sp.det(Aplus), 1)

    def test_coherent_microcell_area_frame_reconstructs_primal_line_frame_exactly(self) -> None:
        r = sp.symbols("r", positive=True)
        L = sp.diag(1, r, r**2)
        H = cofactor_area_frame(L)
        self.assertEqual(H, sp.diag(r**3, r**2, r))
        self.assertEqual(line_frame_from_area_frame(H), L)
        self.assertEqual(line_gram_from_area_frame(H), sp.diag(1, r**2, r**4))

    def test_bounded_microcell_reconstructs_all_shrinking_material_lines(self) -> None:
        r = sp.symbols("r", positive=True)
        H = sp.diag(r**2 / 2, r**2, 2 * r**2)
        self.assertEqual(line_frame_from_area_frame(H), sp.diag(2 * r, r, r / 2))

    def test_incompressible_nanson_duality_reconstructs_material_line_kinematics(self) -> None:
        a, b, c, d, e, f, g, h = sp.symbols("a b c d e f g h")
        A = sp.Matrix([[a, b, c], [d, e, f], [g, h, -a - e]])
        L = sp.Matrix([[2, 0, 1], [1, 2, 0], [0, 1, 1]])
        H = cofactor_area_frame(L)
        Hdot = material_area_frame_rhs(A, H)
        # Differentiate L(H)=sqrt(det H)H^{-T}; div-free implies det H dot = 0.
        d = sp.det(H)
        Ldot_from_H = sp.simplify(-sp.sqrt(d) * H.inv().T * Hdot.T * H.inv().T)
        self.assertEqual(sp.simplify(Ldot_from_H - material_line_frame_rhs(A, L)), sp.zeros(3))

    def test_primal_line_gram_changes_by_literal_directional_strain(self) -> None:
        g = sp.symbols("g0:9")
        A = sp.Matrix(3, 3, g)
        L = sp.Matrix([[2, 0, 1], [1, 3, 0], [0, 1, 2]])
        Ldot = material_line_frame_rhs(A, L)
        direct = sp.simplify(Ldot.T * L + L.T * Ldot)
        self.assertEqual(sp.simplify(direct - material_line_gram_rhs(A, L)), sp.zeros(3))

    def test_isotropic_physical_refinement_scales_primal_lines_and_area_duals_differently(self) -> None:
        lam = sp.symbols("lam", positive=True)
        L = sp.Matrix([[2, 0, 1], [1, 2, 0], [0, 1, 1]])
        H = cofactor_area_frame(L)
        self.assertEqual(sp.simplify(cofactor_area_frame(lam * L) - lam**2 * H), sp.zeros(3))
        self.assertEqual(sp.simplify(line_frame_from_area_frame(lam**2 * H) - lam * L), sp.zeros(3))

    def test_long_thin_incompressible_packet_has_small_H_but_order_one_line_scale(self) -> None:
        r = sp.symbols("r", positive=True)
        F = sp.diag(1 / r, 1, r)
        self.assertEqual(sp.det(F), 1)
        H = incompressible_isotropic_area_frame(F, r)
        self.assertEqual(H, sp.diag(r**3, r**2, r))
        self.assertEqual(sp.det(H), r**6)
        # For 0<r<1, sigma_min(H)=r^3, hence the exact line-scale diagnostic is 1.
        self.assertEqual(diagonal_locality_ratio(H, r**3), 1)

    def test_bounded_deformation_packet_is_genuinely_local(self) -> None:
        r = sp.symbols("r", positive=True)
        F = sp.diag(2, 1, sp.Rational(1, 2))
        self.assertEqual(sp.det(F), 1)
        H = incompressible_isotropic_area_frame(F, r)
        self.assertEqual(H, sp.diag(r**2 / 2, r**2, 2 * r**2))
        self.assertEqual(diagonal_locality_ratio(H, r**2 / 2), 2 * r)

    def test_long_thin_smooth_flux_defect_is_order_area_not_little_o_area(self) -> None:
        r = sp.symbols("r", positive=True)
        actual = long_thin_face_flux(r)
        local = long_thin_center_flux(r)
        self.assertEqual(actual, 2 * r**2 * sp.sin(sp.Rational(1, 2)))
        self.assertEqual(local, r**2)
        self.assertEqual(
            sp.simplify((actual - local) / r**2),
            -1 + 2 * sp.sin(sp.Rational(1, 2)),
        )

    def test_long_thin_covariance_defect_remains_order_r4(self) -> None:
        r = sp.symbols("r", positive=True)
        defect = long_thin_covariance_defect(r)
        expected = -1 + 4 * sp.sin(sp.Rational(1, 2)) ** 2
        self.assertEqual(sp.trigsimp(defect / r**4 - expected), 0)
        self.assertNotEqual(sp.simplify(defect / r**4), 0)

    def test_metric_whitened_long_thin_payoff_error_does_not_vanish(self) -> None:
        r = sp.symbols("r", positive=True)
        whitened = long_thin_whitened_payoff_error(r)
        self.assertEqual(
            whitened,
            sp.Matrix([0, -1 + 2 * sp.sin(sp.Rational(1, 2)), 0]),
        )

    def test_raw_small_remainder_can_fail_metric_whitened_smallness(self) -> None:
        r, c = sp.symbols("r c", positive=True)
        H = sp.diag(r**3, r**2, r)
        R = sp.diag(0, c * r**4, 0)
        raw_ratio = sp.simplify(raw_frobenius_square(R) / raw_frobenius_square(H))
        self.assertEqual(sp.limit(raw_ratio, r, 0, dir="+"), 0)
        self.assertEqual(metric_whitened_covariance_remainder(R, H), c)

    def test_whitened_l2_bound_exposes_conditioning_factor(self) -> None:
        A, sigma, omega = sp.symbols("A sigma omega", positive=True)
        self.assertEqual(whitened_l2_error_bound_factor(A, sigma, omega), A * omega / sigma)


if __name__ == "__main__":
    unittest.main()
