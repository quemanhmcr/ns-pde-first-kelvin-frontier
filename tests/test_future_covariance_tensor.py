from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.future_covariance_tensor import (
    backward_kelvin_flux_mean_residual,
    codeforming_covariance_metric_work_residual,
    codeforming_gram_bulk_reconstruction_residual,
    codeforming_kelvin_gram,
    codeforming_mean_dyad_backward_source,
    codeforming_support_normalized_total_bank,
    codeforming_vorticity_mean_residual,
    physical_covariance_from_codeforming,
    support_normalized_common_stretch_derivative_residual,
    support_normalized_total_bank_pullback_residual,
    total_physical_second_moment,
    total_scalar_strain_work,
    total_second_moment_stretch_source,
    backward_local_tensor_operator,
    conditional_covariance,
    connected_covariance_horizon_residual,
    connected_mean_horizon_residual,
    connected_mean_square_horizon_residual,
    connected_second_moment_horizon_residual,
    double_stokes_pair_covariance,
    exact_gauge_cycle_projection,
    fiber_constant_columns,
    generator_descends,
    generator_intertwining_residual,
    metric_amplified_symmetric_remainder,
    product_pair_diagonal_defect,
    packet_tensor_pullback,
    projection_lift,
    quotient_generator,
    symmetric_loop_covariance_expansion,
    vector_carre_du_champ,
    vorticity_dyad_residual,
)
from src.pde_audit.vorticity_restart import curl3, gradient
from src.pde_audit.orientation_packet import area_frame_qv_matrix


class FutureCovarianceTensorAudit(unittest.TestCase):
    def setUp(self) -> None:
        self.a, self.tau, self.nu, self.k = sp.symbols("a tau nu k", positive=True)

    def _connected_cos_sin(self):
        a, tau, nu, k = self.a, self.tau, self.nu, self.k
        b1, b2 = sp.symbols("b1 b2")
        heat = sp.exp(-nu * k**2 * tau)
        mean = sp.Matrix([
            sp.exp(-b1 * tau) * heat * sp.cos(k * a),
            sp.exp(-b2 * tau) * heat * sp.sin(k * a),
        ])
        e4 = sp.exp(-4 * nu * k**2 * tau)
        Q0 = sp.Matrix([
            [sp.Rational(1, 2) * (1 + e4 * sp.cos(2 * k * a)), sp.Rational(1, 2) * e4 * sp.sin(2 * k * a)],
            [sp.Rational(1, 2) * e4 * sp.sin(2 * k * a), sp.Rational(1, 2) * (1 - e4 * sp.cos(2 * k * a))],
        ])
        D = sp.diag(sp.exp(-b1 * tau), sp.exp(-b2 * tau))
        second = sp.simplify(D * Q0 * D)
        B = sp.diag(b1, b2)
        drift = sp.Matrix([0])
        diffusion = sp.Matrix([[2 * nu]])
        return mean, second, B, drift, diffusion

    def test_vector_future_covariance_pde_is_full_carre_du_champ_matrix(self) -> None:
        mean, second, B, drift, diffusion = self._connected_cos_sin()
        residual = connected_covariance_horizon_residual(mean, second, B, self.tau, drift, diffusion, [self.a])
        self.assertEqual(sp.simplify(residual), sp.zeros(2))
        Gamma = vector_carre_du_champ(mean, diffusion, [self.a])
        self.assertNotEqual(sp.simplify(Gamma[0, 1]), 0)

    def test_mean_and_terminal_second_moment_are_homogeneous_connected_fields(self) -> None:
        mean, second, B, drift, diffusion = self._connected_cos_sin()
        self.assertEqual(
            sp.simplify(connected_mean_horizon_residual(mean, B, self.tau, drift, diffusion, [self.a])),
            sp.zeros(2, 1),
        )
        self.assertEqual(
            sp.simplify(connected_second_moment_horizon_residual(second, B, self.tau, drift, diffusion, [self.a])),
            sp.zeros(2),
        )




    def test_support_normalized_total_bank_is_exact_codeforming_trace(self) -> None:
        F=sp.Matrix([[2,1,0],[0,2,1],[1,0,1]])
        q=sp.symbols("q0:9")
        Q=sp.Matrix(3,3,q)
        self.assertEqual(support_normalized_total_bank_pullback_residual(Q,F),0)

    def test_support_normalized_total_bank_cancels_common_stretch_exactly(self) -> None:
        a=sp.symbols("a0:9")
        A=sp.Matrix(3,3,a)
        F=sp.Matrix([[2,1,0],[0,2,1],[1,0,1]])
        t=sp.symbols("t0:9")
        T=sp.Matrix(3,3,t)
        self.assertEqual(support_normalized_common_stretch_derivative_residual(A,F,T),0)

    def test_support_normalized_bank_is_invariant_under_isotropic_physical_refinement_scale(self) -> None:
        rho=sp.symbols("rho", positive=True)
        F=sp.Matrix([[2,1,0],[0,2,1],[1,0,1]])
        q=sp.symbols("q0:9")
        Q=sp.Matrix(3,3,q)
        T=sp.simplify(F*Q*F.T)
        # Shape support tensor uses F F^T; rho belongs to the separate physical scale face.
        I0=codeforming_support_normalized_total_bank(T,F)
        # Replacing the coherent line frame by rho F changes support scale, not F-shape.
        self.assertEqual(sp.simplify(I0-sp.trace(Q)/2),0)

    def test_pulledback_kelvin_gram_reconstructs_bulk_viscous_enstrophy_loss_in_any_F(self) -> None:
        nu=sp.symbols("nu")
        F=sp.Matrix([[2,1,0],[0,2,1],[1,0,1]])
        g=sp.symbols("g0:9")
        G=sp.Matrix(3,3,g)
        self.assertEqual(codeforming_gram_bulk_reconstruction_residual(F,G,nu),0)

    def test_future_covariance_metric_work_is_physical_covariance_weighted_strain(self) -> None:
        F=sp.Matrix([[2,1,0],[0,2,1],[1,0,1]])
        c=sp.symbols("c0:6")
        C=sp.Matrix([[c[0],c[1],c[2]],[c[1],c[3],c[4]],[c[2],c[4],c[5]]])
        s=sp.symbols("s0:6")
        S=sp.Matrix([[s[0],s[1],s[2]],[s[1],s[3],s[4]],[s[2],s[4],s[5]]])
        self.assertEqual(codeforming_covariance_metric_work_residual(C,F,S),0)

    def test_kelvin_gram_is_internal_transfer_in_total_second_moment_tensor(self) -> None:
        nu=sp.symbols("nu")
        F=sp.Matrix([[2,1,0],[0,2,1],[1,0,1]])
        g=sp.symbols("g0:9")
        G=sp.Matrix(3,3,g)
        gram=codeforming_kelvin_gram(F,G,nu)
        mean_nonstretch=-sp.simplify(F*gram*F.T)
        cov_nonstretch=sp.simplify(F*gram*F.T)
        self.assertEqual(sp.simplify(mean_nonstretch+cov_nonstretch),sp.zeros(3))

    def test_total_second_moment_half_trace_has_only_total_strain_work_after_transfer(self) -> None:
        a=sp.symbols("a0:9")
        A=sp.Matrix(3,3,a)
        S=sp.simplify((A+A.T)/2)
        w=sp.Matrix(sp.symbols("w0:3"))
        F=sp.Matrix([[2,1,0],[0,2,1],[1,0,1]])
        c=sp.symbols("c0:6")
        C=sp.Matrix([[c[0],c[1],c[2]],[c[1],c[3],c[4]],[c[2],c[4],c[5]]])
        T=total_physical_second_moment(w,C,F)
        stretch=total_second_moment_stretch_source(A,T)
        self.assertEqual(sp.simplify(sp.trace(stretch)/2-total_scalar_strain_work(S,T)),0)

    def test_resolved_plus_future_covariance_scalar_is_mean_enstrophy_plus_packet_bank(self) -> None:
        w=sp.Matrix(sp.symbols("w0:3"))
        F=sp.Matrix([[2,1,0],[0,2,1],[1,0,1]])
        c=sp.symbols("c0:6")
        C=sp.Matrix([[c[0],c[1],c[2]],[c[1],c[3],c[4]],[c[2],c[4],c[5]]])
        T=total_physical_second_moment(w,C,F)
        eta=sp.simplify(F.inv()*w)
        bank=sp.simplify(sp.trace(C*(F.T*F))/2)
        self.assertEqual(sp.simplify(sp.trace(T)/2-(w.dot(w)/2+bank)),0)
        self.assertEqual(sp.simplify(w.dot(w)-sp.trace(F*eta*eta.T*F.T)),0)

    def test_generic_codeforming_vorticity_mean_cancels_stretching(self) -> None:
        a=sp.symbols("a0:9")
        A=sp.Matrix(3,3,a)
        F=sp.Matrix([[2,1,0],[0,2,1],[1,0,1]])
        w=sp.Matrix(sp.symbols("w0:3"))
        backward_op=sp.simplify(A*w)
        self.assertEqual(codeforming_vorticity_mean_residual(F,A,w,backward_op),sp.zeros(3,1))

    def test_codeforming_kelvin_gram_is_full_state_carre_du_champ_of_pulledback_mean(self) -> None:
        x1,x2,x3,nu=sp.symbols("x1 x2 x3 nu")
        coords=(x1,x2,x3)
        F=sp.Matrix([[2,1,0],[0,2,1],[1,0,1]])
        g=sp.symbols("g0:9")
        G=sp.Matrix(3,3,g)
        x=sp.Matrix(coords)
        mean=sp.simplify(F.inv()*G*x)
        Gamma=vector_carre_du_champ(mean,2*nu*sp.eye(3),coords)
        self.assertEqual(sp.simplify(Gamma-codeforming_kelvin_gram(F,G,nu)),sp.zeros(3))

    def test_codeforming_mean_square_and_future_covariance_sources_cancel_tensorially(self) -> None:
        nu=sp.symbols("nu")
        F=sp.Matrix([[2,1,0],[0,2,1],[1,0,1]])
        g=sp.symbols("g0:9")
        G=sp.Matrix(3,3,g)
        mean_source=codeforming_mean_dyad_backward_source(F,G,nu)
        covariance_source=codeforming_kelvin_gram(F,G,nu)
        self.assertEqual(sp.simplify(mean_source+covariance_source),sp.zeros(3))

    def test_carre_du_champ_is_exact_transfer_from_mean_square_to_future_covariance(self) -> None:
        mean, second, B, drift, diffusion = self._connected_cos_sin()
        self.assertEqual(
            sp.simplify(connected_mean_square_horizon_residual(mean, B, self.tau, drift, diffusion, [self.a])),
            sp.zeros(2),
        )
        C = conditional_covariance(mean, second)
        self.assertEqual(sp.simplify(C + mean * mean.T - second), sp.zeros(2))

    def test_cross_covariance_source_has_physical_signed_orientation_content(self) -> None:
        mean, _, _, _, diffusion = self._connected_cos_sin()
        Gamma = sp.simplify(vector_carre_du_champ(mean, diffusion, [self.a]))
        b1, b2 = sp.symbols("b1 b2")
        expected = -2 * self.nu * self.k**2 * sp.exp(-(b1 + b2 + 2 * self.nu * self.k**2) * self.tau) * sp.sin(self.k * self.a) * sp.cos(self.k * self.a)
        self.assertEqual(sp.simplify(Gamma[0, 1] - expected), 0)

    def test_exact_ns_vorticity_dyad_has_kelvin_gram_as_viscous_defect_tensor(self) -> None:
        x, y, z, t, nu, k = sp.symbols("x y z t nu k", positive=True)
        u = sp.Matrix([sp.exp(-nu * k**2 * t) * sp.cos(k * y), 0, 0])
        coords = (x, y, z)
        omega = curl3(u, coords)
        A = gradient(u, coords)
        self.assertEqual(sp.simplify(vorticity_dyad_residual(omega, A, u, nu, t, coords)), sp.zeros(3))

    def test_exact_abc_vorticity_dyad_tensor_identity(self) -> None:
        x, y, z, t, nu = sp.symbols("x y z t nu", positive=True)
        amp = sp.exp(-nu * t)
        u = amp * sp.Matrix([
            sp.sin(z) + sp.cos(y),
            sp.sin(x) + sp.cos(z),
            sp.sin(y) + sp.cos(x),
        ])
        coords = (x, y, z)
        omega = curl3(u, coords)
        A = gradient(u, coords)
        residual = vorticity_dyad_residual(omega, A, u, nu, t, coords)
        self.assertEqual(sp.simplify(residual), sp.zeros(3))

    def test_dyad_kelvin_tensor_trace_is_twice_bulk_viscous_enstrophy_payment(self) -> None:
        g = sp.Matrix(3, 3, sp.symbols("g0:9"))
        nu = sp.symbols("nu", positive=True)
        G = sp.simplify(2 * nu * g * g.T)
        frob = sum(g[i, j] ** 2 for i in range(3) for j in range(3))
        self.assertEqual(sp.expand(sp.trace(G) - 2 * nu * frob), 0)

    def test_non_lumpable_hidden_shape_state_blocks_spatial_generator_descent(self) -> None:
        # States 0+,0- project to spatial x=0 but have different escape rates to x=1.
        L = sp.Matrix([
            [-1, 0, 1, 0],
            [0, -2, 0, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ])
        labels = [0, 0, 1, 1]
        self.assertFalse(generator_descends(L, labels))
        obstruction = generator_intertwining_residual(L, labels)
        self.assertNotEqual(obstruction, sp.zeros(*obstruction.shape))
        R = projection_lift(labels)
        self.assertFalse(fiber_constant_columns(L * R, labels))
        with self.assertRaises(ValueError):
            quotient_generator(L, labels)

    def test_lumpable_hidden_shape_state_has_exact_generator_intertwining(self) -> None:
        L = sp.Matrix([
            [-1, 0, 1, 0],
            [0, -1, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ])
        labels = [0, 0, 1, 1]
        self.assertTrue(generator_descends(L, labels))
        Lbar = quotient_generator(L, labels)
        self.assertEqual(Lbar, sp.Matrix([[-1, 1], [0, 0]]))
        self.assertEqual(generator_intertwining_residual(L, labels), sp.zeros(4, 2))

    def test_centered_C2_loop_covariance_has_r6_raw_remainder_and_r2_capacity_remainder(self) -> None:
        r = sp.symbols("r", positive=True)
        c11, c12, c22 = sp.symbols("c11 c12 c22")
        d11, d12, d22 = sp.symbols("d11 d12 d22")
        e11, e12, e22 = sp.symbols("e11 e12 e22")
        C0 = sp.Matrix([[c11, c12], [c12, c22]])
        C1 = sp.Matrix([[d11, d12], [d12, d22]])
        C2 = sp.Matrix([[e11, e12], [e12, e22]])
        raw = symmetric_loop_covariance_expansion(C0, C1, C2, r)
        amp = metric_amplified_symmetric_remainder(raw, C0, r)
        self.assertEqual(sp.simplify(amp - (r**2 * C1 + r**4 * C2)), sp.zeros(2))
        self.assertEqual(sp.simplify(amp.subs(r, 0)), sp.zeros(2))


    def test_pair_diagonal_generator_defect_is_vector_carre_du_champ(self) -> None:
        x, nu = sp.symbols("x nu", positive=True)
        x1, x2 = sp.symbols("x1 x2")
        mean = sp.Matrix([x**2 + x, x**3 - 2 * x])
        drift = sp.Matrix([x + 1])
        diffusion = sp.Matrix([[2 * nu]])
        defect = product_pair_diagonal_defect(mean, [x], [x1], [x2], drift, diffusion)
        Gamma = vector_carre_du_champ(mean, diffusion, [x])
        self.assertEqual(sp.simplify(defect - Gamma), sp.zeros(2))

    def test_double_stokes_turns_pair_momentum_covariance_into_cycle_flux_covariance(self) -> None:
        # One oriented triangle: B1 D2=0.  K is an arbitrary edge-cochain covariance.
        B1 = sp.Matrix([
            [-1, 0, 1],
            [1, -1, 0],
            [0, 1, -1],
        ])
        D2 = sp.Matrix([1, 1, 1])
        self.assertEqual(B1 * D2, sp.zeros(3, 1))
        k11, k12, k13, k22, k23, k33 = sp.symbols("k11 k12 k13 k22 k23 k33")
        K = sp.Matrix([
            [k11, k12, k13],
            [k12, k22, k23],
            [k13, k23, k33],
        ])
        cycle_cov = double_stokes_pair_covariance(K, D2)
        direct = sp.expand(sum(K[i, j] for i in range(3) for j in range(3)))
        self.assertEqual(sp.expand(cycle_cov[0, 0] - direct), 0)

    def test_double_stokes_is_exact_gauge_blind(self) -> None:
        B1 = sp.Matrix([
            [-1, 0, 1],
            [1, -1, 0],
            [0, 1, -1],
        ])
        D2 = sp.Matrix([1, 1, 1])
        p0, p1, p2 = sp.symbols("p0 p1 p2")
        projected = exact_gauge_cycle_projection(B1, D2, sp.Matrix([p0, p1, p2]))
        self.assertEqual(projected, sp.zeros(1, 1))

    def test_exact_shear_orientation_packet_source_is_pair_diagonal_branching_tensor(self) -> None:
        a, nu, k, tau = self.a, self.nu, self.k, self.tau
        scalar_mean = sp.exp(-nu * k**2 * tau) * sp.cos(k * a)
        orientation = sp.Matrix([1, 0, -1])
        mean = orientation * scalar_mean
        diffusion = sp.Matrix([[2 * nu]])
        Gamma = sp.simplify(vector_carre_du_champ(mean, diffusion, [a]))
        scalar_gamma = sp.simplify(2 * nu * sp.diff(scalar_mean, a) ** 2)
        self.assertEqual(sp.simplify(Gamma - scalar_gamma * orientation * orientation.T), sp.zeros(3))
        self.assertLess(sp.simplify(Gamma[0, 2] / scalar_gamma), 0)


    def test_local_kelvin_source_tensor_pullback_is_exact_area_frame_qv_matrix(self) -> None:
        nu = sp.symbols("nu", positive=True)
        G = sp.Matrix(3, 3, sp.symbols("g0:9"))
        H = sp.Matrix([
            [1, 2, 0],
            [0, 1, 1],
            [1, 0, 1],
        ])
        local_source = sp.simplify(2 * nu * G * G.T)
        pulled = packet_tensor_pullback(local_source, H)
        direct = area_frame_qv_matrix(G, H, nu)
        self.assertEqual(sp.simplify(pulled - direct), sp.zeros(3))


    def test_backward_kelvin_infinitesimal_packet_mean_is_exact_for_ns_shear(self) -> None:
        x, y, z, t, nu, k = sp.symbols("x y z t nu k", positive=True)
        coords = (x, y, z)
        u = sp.Matrix([sp.exp(-nu * k**2 * t) * sp.cos(k * y), 0, 0])
        omega = curl3(u, coords)
        A = gradient(u, coords)
        H = sp.Matrix(3, 3, sp.symbols("h0:9"))
        residual = backward_kelvin_flux_mean_residual(omega, A, u, H, nu, t, coords)
        self.assertEqual(sp.simplify(residual), sp.zeros(3, 1))

    def test_backward_kelvin_infinitesimal_packet_mean_is_exact_for_abc(self) -> None:
        x, y, z, t, nu = sp.symbols("x y z t nu", positive=True)
        coords = (x, y, z)
        amp = sp.exp(-nu * t)
        u = amp * sp.Matrix([
            sp.sin(z) + sp.cos(y),
            sp.sin(x) + sp.cos(z),
            sp.sin(y) + sp.cos(x),
        ])
        omega = curl3(u, coords)
        A = gradient(u, coords)
        H = sp.Matrix([
            [1, 2, 0],
            [0, 1, 1],
            [1, 0, 1],
        ])
        residual = backward_kelvin_flux_mean_residual(omega, A, u, H, nu, t, coords)
        self.assertEqual(sp.simplify(residual), sp.zeros(3, 1))

    def test_backward_tensor_operator_on_vorticity_dyad_is_minus_kelvin_gram(self) -> None:
        x, y, z, t, nu, k = sp.symbols("x y z t nu k", positive=True)
        coords = (x, y, z)
        u = sp.Matrix([sp.exp(-nu * k**2 * t) * sp.cos(k * y), 0, 0])
        omega = curl3(u, coords)
        A = gradient(u, coords)
        E = sp.simplify(omega * omega.T)
        G = gradient(omega, coords)
        Gamma = sp.simplify(2 * nu * G * G.T)
        self.assertEqual(sp.simplify(backward_local_tensor_operator(E, A, u, nu, t, coords) + Gamma), sp.zeros(3))


    def test_exact_ns_shear_has_closed_form_backward_kelvin_covariance_tensor_pde(self) -> None:
        x, y, z, t, t0, nu, k = sp.symbols("x y z t t0 nu k", positive=True)
        coords = (x, y, z)
        u = sp.Matrix([sp.exp(-nu * k**2 * t) * sp.cos(k * y), 0, 0])
        omega = curl3(u, coords)
        A = gradient(u, coords)
        # Backward stochastic Kelvin uses a past terminal time t0.  The past payoff
        # has zero conditional covariance at t=t0, and the backward-martingale
        # covariance grows positively for t>t0.
        Qzz = sp.Rational(1, 2) * k**2 * sp.exp(-2 * nu * k**2 * t0) * (
            1 - sp.exp(-4 * nu * k**2 * (t - t0)) * sp.cos(2 * k * y)
        )
        Czz = sp.simplify(Qzz - omega[2] ** 2)
        C = sp.diag(0, 0, Czz)
        G = gradient(omega, coords)
        Gamma = sp.simplify(2 * nu * G * G.T)
        residual = sp.simplify(backward_local_tensor_operator(C, A, u, nu, t, coords) - Gamma)
        self.assertEqual(residual, sp.zeros(3))
        self.assertEqual(sp.simplify(Czz.subs(t, t0)), 0)

    def test_exact_ns_shear_backward_total_second_moment_tensor_is_homogeneous(self) -> None:
        x, y, z, t, t0, nu, k = sp.symbols("x y z t t0 nu k", positive=True)
        coords = (x, y, z)
        u = sp.Matrix([sp.exp(-nu * k**2 * t) * sp.cos(k * y), 0, 0])
        omega = curl3(u, coords)
        A = gradient(u, coords)
        Qzz = sp.Rational(1, 2) * k**2 * sp.exp(-2 * nu * k**2 * t0) * (
            1 - sp.exp(-4 * nu * k**2 * (t - t0)) * sp.cos(2 * k * y)
        )
        Q = sp.diag(0, 0, Qzz)
        self.assertEqual(sp.simplify(backward_local_tensor_operator(Q, A, u, nu, t, coords)), sp.zeros(3))


    def test_exact_shear_backward_covariance_has_manifest_positive_causal_factorization(self) -> None:
        y, t, t0, nu, k = sp.symbols("y t t0 nu k", positive=True)
        rho = sp.exp(-2 * nu * k**2 * (t - t0))
        Qzz = sp.Rational(1, 2) * k**2 * sp.exp(-2 * nu * k**2 * t0) * (
            1 - rho**2 * sp.cos(2 * k * y)
        )
        mean_sq = k**2 * sp.exp(-2 * nu * k**2 * t) * sp.sin(k * y) ** 2
        Czz = sp.trigsimp(sp.simplify(Qzz - mean_sq))
        manifest = sp.Rational(1, 2) * k**2 * sp.exp(-2 * nu * k**2 * t0) * (
            (1 - rho) * (1 + rho * sp.cos(2 * k * y))
        )
        self.assertEqual(sp.trigsimp(sp.simplify(Czz - manifest)), 0)


if __name__ == "__main__":
    unittest.main()
