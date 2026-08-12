from __future__ import annotations

import unittest

import sympy as sp

from src.pde_audit.active_pair import pair_boundary, pair_lift
from src.pde_audit.orientation_packet import (
    area_frame_metric,
    area_frame_metric_derivative,
    area_frame_qv_matrix,
    material_area_frame_rhs,
    material_area_log_rate,
    material_flux_transport_residual,
    material_metric_logdet_rate,
    deterministic_flux_stretching_residual,
    flux_metric_stretching_residual,
    flux_metric_stretching_work,
    physical_covariance_from_flux,
    isotropic_scale_remainder_law,
    local_tensor_bank_derivative_residual,
    local_tensor_bank_residual,
    local_tensor_packet_covariance,
    metric_amplified_remainder_bank,
    metric_packet_bank_rhs,
    metric_packet_jump_decomposition,
    metric_bulk_reconstruction_residual,
    metric_normalized_packet_bank,
    metric_normalized_packet_bank_derivative,
    packet_basis_change_invariance_residual,
    pure_frame_bank_derivative_residual,
    normalized_packet_bank_rhs,
    normalized_packet_covariance,
    normalized_packet_jump_decomposition,
    orientation_diagonal_projection,
    orientation_qv_matrix,
    packet_bulk_payment,
    packet_covariance_pullback,
    packet_pair_map,
    packet_reset_decomposition,
    packet_scalar_bank,
    packet_selector,
    parallel_cycle_packet_library,
    rotation_commutator,
    rotation_connection_residual,
)
from src.pde_audit.vorticity_restart import curl3, gradient, strain_tensor, stretching_power


def strain_tensor_from_matrix(G: sp.MatrixBase) -> sp.Matrix:
    return sp.simplify((G + G.T) / 2)


class OrientationCompletePacketAudit(unittest.TestCase):
    def test_full_orientation_qv_matrix_is_shared_noise_gram_matrix(self) -> None:
        nu = sp.symbols("nu", positive=True)
        a = sp.symbols("a0:9")
        G = sp.Matrix(3, 3, a)
        Gamma = orientation_qv_matrix(G, sp.eye(3), nu)
        self.assertEqual(sp.simplify(Gamma - 2 * nu * G * G.T), sp.zeros(3))
        self.assertEqual(
            sp.simplify(packet_bulk_payment(Gamma) - nu * sum(x * x for x in a)),
            0,
        )

    def test_first_bad_restart_selector_selects_whole_three_loop_packet(self) -> None:
        B, K = parallel_cycle_packet_library(germ_count=2, orientation_dim=3)
        M = sp.diag(0, 1)
        S = packet_selector(M, 3)
        P = K * S
        self.assertEqual(S.rank(), 3)
        self.assertEqual(sp.simplify(B * P), sp.zeros(B.rows, P.cols))
        self.assertEqual(
            sp.simplify(pair_boundary(B) * pair_lift(P)),
            sp.zeros(pair_boundary(B).rows, pair_lift(P).cols),
        )

    def test_rotation_moves_cross_orientation_covariance_by_congruence_and_preserves_trace(self) -> None:
        c11, c12, c13, c22, c23, c33 = sp.symbols("c11 c12 c13 c22 c23 c33")
        C = sp.Matrix([[c11, c12, c13], [c12, c22, c23], [c13, c23, c33]])
        q = sp.sqrt(2) / 2
        Q = sp.Matrix([[q, 0, q], [0, 1, 0], [-q, 0, q]])
        Cq = packet_covariance_pullback(C, Q)
        self.assertEqual(sp.simplify(Q.T * Q - sp.eye(3)), sp.zeros(3))
        self.assertEqual(sp.simplify(sp.trace(Cq) - sp.trace(C)), 0)
        self.assertEqual(packet_pair_map(Q.T * Q), sp.eye(9))

    def test_rotation_connection_is_trace_free_redistribution(self) -> None:
        theta = sp.symbols("theta", real=True)
        C = sp.Matrix([[2, 1, 0], [1, 3, -1], [0, -1, 5]])
        Cdot = sp.Matrix([[1, 2, 0], [2, -1, 1], [0, 1, 4]])
        Q = sp.Matrix([
            [sp.cos(theta), 0, sp.sin(theta)],
            [0, 1, 0],
            [-sp.sin(theta), 0, sp.cos(theta)],
        ])
        Qdot = sp.diff(Q, theta)
        self.assertEqual(
            sp.trigsimp(rotation_connection_residual(C, Cdot, Q, Qdot)),
            sp.zeros(3),
        )
        Cq = sp.trigsimp(Q.T * C * Q)
        Omega = sp.trigsimp(Q.T * Qdot)
        comm = sp.trigsimp(rotation_commutator(Cq, Omega))
        self.assertEqual(sp.trigsimp(sp.trace(comm)), 0)

    def test_exact_ns_shear_rotation_creates_physical_cross_orientation_qv(self) -> None:
        y, t, nu, k = sp.symbols("y t nu k", positive=True)
        u = sp.Matrix([sp.exp(-nu * k**2 * t) * sp.cos(k * y), 0, 0])
        omega = curl3(u, (sp.symbols("x"), y, sp.symbols("z")))
        G = gradient(omega, (sp.symbols("x"), y, sp.symbols("z")))
        Gamma = orientation_qv_matrix(G, sp.eye(3), nu)
        q = sp.sqrt(2) / 2
        Q = sp.Matrix([[q, 0, q], [0, 1, 0], [-q, 0, q]])
        rotated = sp.simplify(Q.T * Gamma * Q)
        self.assertNotEqual(sp.simplify(rotated[0, 2]), 0)
        diagonal_only = orientation_diagonal_projection(rotated)
        recovered = sp.simplify(Q * diagonal_only * Q.T)
        self.assertNotEqual(sp.simplify(recovered - Gamma), sp.zeros(3))
        self.assertEqual(sp.simplify(sp.trace(rotated) - sp.trace(Gamma)), 0)

    def test_exact_abc_peak_has_negative_cross_orientation_qv_and_blind_diagonal_normal(self) -> None:
        x, y, z, t, nu = sp.symbols("x y z t nu", positive=True)
        amp = sp.exp(-nu * t)
        u = amp * sp.Matrix([
            sp.sin(z) + sp.cos(y),
            sp.sin(x) + sp.cos(z),
            sp.sin(y) + sp.cos(x),
        ])
        omega = curl3(u, (x, y, z))
        G = gradient(omega, (x, y, z))
        pt = {x: sp.pi / 4, y: sp.pi / 4, z: sp.pi / 4}
        Gamma = sp.simplify(orientation_qv_matrix(G, sp.eye(3), nu).subs(pt))
        expected = nu * amp**2 * sp.Matrix([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]])
        self.assertEqual(sp.simplify(Gamma - expected), sp.zeros(3))
        self.assertLess(float(sp.N(Gamma[0, 1].subs({nu: 1, t: 1}))), 0.0)
        n = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
        blind = sp.simplify((n.T * Gamma * n)[0])
        self.assertEqual(blind, 0)
        self.assertEqual(sp.simplify(packet_bulk_payment(Gamma) - 3 * nu * amp**2), 0)

    def test_anisotropic_area_normalization_has_two_face_dilation_law(self) -> None:
        a1, a2, a3, da1, da2, da3 = sp.symbols(
            "a1 a2 a3 da1 da2 da3", positive=True
        )
        c11, c12, c13, c22, c23, c33 = sp.symbols("c11 c12 c13 c22 c23 c33")
        g11, g22, g33 = sp.symbols("g11 g22 g33")
        w12 = sp.symbols("w12")
        C = sp.Matrix([[c11, c12, c13], [c12, c22, c23], [c13, c23, c33]])
        Gamma = sp.diag(g11, g22, g33)
        W = sp.Matrix([[0, w12, 0], [w12, 0, 0], [0, 0, 0]])
        areas = [a1, a2, a3]
        area_dots = [da1, da2, da3]
        rhs = normalized_packet_bank_rhs(C, Gamma, W, areas, area_dots)
        Chat = normalized_packet_covariance(C, areas)
        E = sp.diag(da1 / a1, da2 / a2, da3 / a3)
        Ghat = normalized_packet_covariance(Gamma, areas)
        What = normalized_packet_covariance(W, areas)
        self.assertEqual(sp.simplify(rhs - (-Ghat + What - E * Chat - Chat * E)), sp.zeros(3))

    def test_isotropic_area_law_reduces_to_scalar_dilation_term(self) -> None:
        A, Adot = sp.symbols("A Adot", positive=True)
        C = sp.Matrix([[3, -1, 2], [-1, 4, 0], [2, 0, 5]])
        Gamma = sp.Matrix([[2, 1, 0], [1, 3, -1], [0, -1, 4]])
        W = sp.zeros(3)
        rhs = normalized_packet_bank_rhs(C, Gamma, W, [A, A, A], [Adot, Adot, Adot])
        Bdot = sp.simplify(sp.trace(rhs) / 2)
        B = packet_scalar_bank(normalized_packet_covariance(C, [A, A, A]))
        payment = packet_scalar_bank(normalized_packet_covariance(Gamma, [A, A, A]))
        self.assertEqual(sp.simplify(Bdot + payment + 2 * Adot / A * B), 0)

    def test_packet_reset_keeps_all_mixed_orientation_covariance(self) -> None:
        C0 = sp.Matrix([[4, -2, 1], [-2, 5, 3], [1, 3, 6]])
        Lm = sp.eye(3)
        Lp = sp.Matrix([[1, 1, 0], [0, 1, 0], [0, 0, -1]])
        dec = packet_reset_decomposition(C0, Lm, Lp)
        self.assertEqual(dec.total, dec.reconstructed)
        self.assertNotEqual(dec.linear_left, sp.zeros(3))
        self.assertNotEqual(dec.quadratic, sp.zeros(3))

    def test_finite_scale_change_is_separate_signed_revaluation_from_packet_reset(self) -> None:
        C0 = sp.Matrix([[4, -1, 2], [-1, 3, 1], [2, 1, 5]])
        Lm = sp.eye(3)
        Lp = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
        dec = normalized_packet_jump_decomposition(
            C0,
            Lm,
            Lp,
            [2, 3, 4],
            [1, 2, 2],
        )
        self.assertEqual(dec.total, dec.reconstructed)
        self.assertNotEqual(dec.map_reset_at_new_scale, sp.zeros(3))
        self.assertNotEqual(dec.pure_scale_revaluation, sp.zeros(3))

    def test_full_pair_packet_maps_compose_but_diagonal_orientation_projection_does_not(self) -> None:
        q = sp.sqrt(2) / 2
        Q = sp.Matrix([[q, 0, q], [0, 1, 0], [-q, 0, q]])
        R = sp.Matrix([[1, sp.Rational(1, 2), 0], [0, 1, 0], [0, 0, sp.Rational(1, 2)]])
        lhs = packet_pair_map(R * Q)
        rhs = packet_pair_map(R) * packet_pair_map(Q)
        self.assertEqual(sp.simplify(lhs - rhs), sp.zeros(9))

        C = sp.Matrix([[3, -2, 1], [-2, 4, 2], [1, 2, 5]])
        full = packet_covariance_pullback(packet_covariance_pullback(C, R), Q)
        truncated = packet_covariance_pullback(orientation_diagonal_projection(packet_covariance_pullback(C, R)), Q)
        self.assertNotEqual(sp.simplify(full - truncated), sp.zeros(3))


    def test_nonorthogonal_area_frame_reconstructs_bulk_by_its_own_metric(self) -> None:
        nu = sp.symbols("nu", positive=True)
        vals = sp.symbols("g0:9")
        G = sp.Matrix(3, 3, vals)
        H = sp.Matrix([[2, 1, 0], [0, 3, 1], [1, 0, 2]])
        Gamma = area_frame_qv_matrix(G, H, nu)
        M = area_frame_metric(H)
        self.assertEqual(sp.simplify(M - (H.T * H).inv()), sp.zeros(3))
        self.assertEqual(metric_bulk_reconstruction_residual(G, H, nu), 0)
        self.assertEqual(
            sp.simplify(metric_normalized_packet_bank(Gamma, H) - nu * sum(v * v for v in vals)),
            0,
        )

    def test_metric_packet_capacity_is_invariant_under_general_GL3_reparameterization(self) -> None:
        C = sp.Matrix([[5, -2, 1], [-2, 4, 3], [1, 3, 7]])
        H = sp.Matrix([[2, 1, 0], [0, 1, 1], [1, 0, 2]])
        L = sp.Matrix([[1, 2, 0], [0, 1, 1], [1, 0, 1]])
        self.assertNotEqual(L.det(), 0)
        self.assertEqual(packet_basis_change_invariance_residual(C, H, L), 0)

    def test_rotation_dilation_and_shear_are_one_connection_under_metric_contraction(self) -> None:
        C = sp.Matrix([[5, -2, 1], [-2, 6, 3], [1, 3, 4]])
        H = sp.Matrix([[2, 0, 1], [1, 2, 0], [0, 1, 3]])
        # R contains diagonal dilation, skew rotation, and shear simultaneously.
        R = sp.Matrix([[2, -3, 1], [3, -1, 4], [0, 2, -1]])
        self.assertEqual(pure_frame_bank_derivative_residual(C, H, R), 0)

    def test_nanson_material_area_frame_separates_normal_strain_from_rotation(self) -> None:
        s1, s2, a = sp.symbols("s1 s2 a", real=True)
        # Trace-free velocity gradient: symmetric strain plus a skew rotation.
        G = sp.Matrix([[s1, -a, 0], [a, s2, 0], [0, 0, -s1 - s2]])
        H = sp.eye(3)
        Hdot = material_area_frame_rhs(G, H)
        self.assertEqual(Hdot, -G.T)
        n = sp.Matrix([1, 0, 0])
        self.assertEqual(material_area_log_rate(G, n), -s1)
        # Skew rotation a does not enter the area-magnitude rate.
        self.assertFalse(material_area_log_rate(G, n).has(a))
        # Incompressibility preserves the infinitesimal area-frame determinant at H=I.
        self.assertEqual(sp.trace(Hdot), 0)

    def test_exact_abc_amplitude_family_rules_out_instantaneous_bulk_payment_as_universal_stretching_bank(self) -> None:
        x, y, z, t, nu, A = sp.symbols("x y z t nu A", positive=True)
        amp = A * sp.exp(-nu * t)
        u = amp * sp.Matrix([
            sp.sin(z) + sp.cos(y),
            sp.sin(x) + sp.cos(z),
            sp.sin(y) + sp.cos(x),
        ])
        omega = curl3(u, (x, y, z))
        Gomega = gradient(omega, (x, y, z))
        p0 = {x: 0, y: 0, z: 0}
        stretching = sp.simplify(stretching_power(u, (x, y, z)).subs(p0))
        Gamma = sp.simplify(area_frame_qv_matrix(Gomega, sp.eye(3), nu).subs(p0))
        bulk = sp.simplify(metric_normalized_packet_bank(Gamma, sp.eye(3)))
        self.assertEqual(sp.simplify(stretching - 3 * A**3 * sp.exp(-3 * nu * t)), 0)
        self.assertEqual(sp.simplify(bulk - 3 * nu * A**2 * sp.exp(-2 * nu * t)), 0)
        ratio = sp.simplify(stretching / bulk)
        self.assertEqual(ratio, A * sp.exp(-nu * t) / nu)
        self.assertEqual(sp.limit(ratio.subs(t, 0), A, sp.oo), sp.oo)


    def test_local_tensor_packet_bank_cancels_all_invertible_frame_geometry(self) -> None:
        T = sp.Matrix([[4, -1, 2], [-1, 5, 3], [2, 3, 6]])
        H = sp.Matrix([[2, 1, 0], [1, 3, 1], [0, 1, 2]])
        self.assertNotEqual(H.det(), 0)
        self.assertEqual(local_tensor_bank_residual(T, H), 0)
        C = local_tensor_packet_covariance(T, H)
        self.assertEqual(
            sp.simplify(metric_normalized_packet_bank(C, H) - sp.trace(T) / 2),
            0,
        )

    def test_local_tensor_bank_derivative_removes_rotation_dilation_shear_connection_exactly(self) -> None:
        T = sp.Matrix([[4, -1, 2], [-1, 5, 3], [2, 3, 6]])
        Tdot = sp.Matrix([[1, 2, 0], [2, -3, 1], [0, 1, 4]])
        H = sp.Matrix([[2, 1, 0], [1, 3, 1], [0, 1, 2]])
        Hdot = sp.Matrix([[3, -2, 1], [1, 4, -1], [2, 0, -3]])
        self.assertEqual(local_tensor_bank_derivative_residual(T, Tdot, H, Hdot), 0)

    def test_dyadic_shrinking_of_a_perfect_local_tensor_has_zero_capacity_cost(self) -> None:
        T = sp.Matrix([[3, 1, -1], [1, 4, 2], [-1, 2, 5]])
        H0 = sp.Matrix([[1, 1, 0], [0, 2, 1], [1, 0, 1]])
        reference = sp.trace(T) / 2
        for n in range(7):
            r = sp.Rational(1, 2) ** n
            H = r**2 * H0
            C = local_tensor_packet_covariance(T, H)
            self.assertEqual(sp.simplify(metric_normalized_packet_bank(C, H) - reference), 0)

    def test_metric_amplified_remainder_has_exact_radius_p_minus_4_threshold(self) -> None:
        r, p = sp.symbols("r p", positive=True)
        R0 = sp.Matrix([[2, -1, 0], [-1, 3, 1], [0, 1, 4]])
        H0 = sp.Matrix([[1, 1, 0], [0, 2, 0], [0, 1, 1]])
        law = isotropic_scale_remainder_law(R0, H0, r, p)
        reference = metric_normalized_packet_bank(R0, H0)
        self.assertEqual(sp.simplify(law - r ** (p - 4) * reference), 0)
        self.assertEqual(sp.simplify(law.subs(p, 4) - reference), 0)
        self.assertEqual(sp.limit(law.subs(p, 5), r, 0, dir='+'), 0)
        # With positive reference contraction, p<4 blows up as r->0.
        self.assertGreater(float(reference), 0.0)
        self.assertEqual(sp.limit(law.subs(p, 3), r, 0, dir='+'), sp.oo)

    def test_only_nontensorial_remainder_survives_metric_normalization(self) -> None:
        T = sp.Matrix([[2, 0, 1], [0, 3, -1], [1, -1, 4]])
        H = sp.Matrix([[2, 1, 0], [0, 2, 1], [1, 0, 1]])
        R = sp.Matrix([[1, -2, 0], [-2, 1, 3], [0, 3, 2]])
        C = local_tensor_packet_covariance(T, H) + R
        total = metric_normalized_packet_bank(C, H)
        remainder = metric_amplified_remainder_bank(C, T, H)
        self.assertEqual(sp.simplify(total - sp.trace(T) / 2 - remainder), 0)


    def test_material_flux_coordinates_cancel_vortex_stretching_exactly(self) -> None:
        g = sp.symbols("g0:9")
        G = sp.Matrix(3, 3, g)
        w1, w2, w3, l1, l2, l3, nu = sp.symbols("w1 w2 w3 l1 l2 l3 nu")
        omega = sp.Matrix([w1, w2, w3])
        lap = sp.Matrix([l1, l2, l3])
        H = sp.Matrix([[2, 1, 0], [0, 2, 1], [1, 0, 1]])
        self.assertEqual(material_flux_transport_residual(G, omega, lap, H, nu), sp.zeros(3, 1))

    def test_incompressible_material_metric_changes_shape_but_not_determinant(self) -> None:
        a, b, c, d, e, f, g, h = sp.symbols("a b c d e f g h")
        G = sp.Matrix([[a, b, c], [d, e, f], [g, h, -a - e]])
        H = sp.Matrix([[2, 1, 0], [0, 2, 1], [1, 0, 1]])
        self.assertEqual(material_metric_logdet_rate(G, H), 0)

    def test_material_packet_metric_work_is_exact_vortex_stretching_for_rank_one_flux(self) -> None:
        g = sp.symbols("g0:9")
        G = sp.Matrix(3, 3, g)
        w1, w2, w3 = sp.symbols("w1 w2 w3")
        omega = sp.Matrix([w1, w2, w3])
        H = sp.Matrix([[2, 1, 0], [0, 2, 1], [1, 0, 1]])
        self.assertEqual(deterministic_flux_stretching_residual(omega, G, H), 0)

    def test_covariance_weighted_material_metric_work_is_physical_strain_contraction(self) -> None:
        G = sp.Matrix([[2, -1, 0], [3, -1, 2], [0, 1, -1]])
        H = sp.Matrix([[2, 1, 0], [0, 2, 1], [1, 0, 1]])
        Cflux = sp.Matrix([[5, -2, 1], [-2, 4, 3], [1, 3, 6]])
        Sigma = physical_covariance_from_flux(Cflux, H)
        self.assertEqual(flux_metric_stretching_residual(Cflux, G, H), 0)
        self.assertEqual(
            sp.simplify(flux_metric_stretching_work(Cflux, G, H) - sp.trace(strain_tensor_from_matrix(G) * Sigma)),
            0,
        )


    def test_metric_packet_continuous_bank_law_keeps_qv_work_and_metric_work_separate(self) -> None:
        C = sp.Matrix([[5, -1, 2], [-1, 4, 1], [2, 1, 6]])
        Gamma = sp.Matrix([[2, -1, 0], [-1, 3, 1], [0, 1, 4]])
        W = sp.Matrix([[1, 2, 0], [2, -1, 1], [0, 1, 0]])
        H = sp.Matrix([[2, 1, 0], [0, 2, 1], [1, 0, 1]])
        Hdot = sp.Matrix([[1, -2, 0], [3, 1, 2], [0, 1, -1]])
        M = area_frame_metric(H)
        # Direct derivative with Cdot=-Gamma+W.
        direct = metric_normalized_packet_bank_derivative(C, -Gamma + W, H, Hdot)
        rhs = metric_packet_bank_rhs(C, Gamma, W, H, Hdot)
        self.assertEqual(sp.simplify(direct - rhs), 0)
        # The three physical slots are separately visible and signed.
        self.assertEqual(
            sp.simplify(rhs - (
                -sp.trace(Gamma * M) / 2
                + sp.trace(W * M) / 2
                + sp.trace(C * area_frame_metric_derivative(H, Hdot)) / 2
            )),
            0,
        )

    def test_passive_GL3_jump_has_nonzero_signed_faces_but_zero_total_capacity_change(self) -> None:
        C = sp.Matrix([[5, -2, 1], [-2, 4, 3], [1, 3, 7]])
        H = sp.Matrix([[2, 1, 0], [0, 2, 1], [1, 0, 1]])
        L = sp.Matrix([[sp.Rational(1, 2), 1, 0], [0, sp.Rational(1, 3), 1], [0, 0, 2]])
        Cp = sp.simplify(L.T * C * L)
        Hp = sp.simplify(H * L)
        dec = metric_packet_jump_decomposition(C, Cp, H, Hp)
        self.assertEqual(dec.total, 0)
        self.assertEqual(dec.reconstructed, 0)
        self.assertNotEqual(dec.covariance_reset_at_new_metric, 0)
        self.assertNotEqual(dec.metric_revaluation, 0)
        self.assertEqual(
            sp.simplify(dec.covariance_reset_at_new_metric + dec.metric_revaluation),
            0,
        )

    def test_physical_packet_reset_at_fixed_metric_is_real_signed_covariance_revaluation(self) -> None:
        Cm = sp.Matrix([[4, -1, 0], [-1, 3, 2], [0, 2, 5]])
        Cp = sp.Matrix([[5, 2, 1], [2, 4, -1], [1, -1, 6]])
        H = sp.Matrix([[2, 1, 0], [0, 2, 1], [1, 0, 1]])
        dec = metric_packet_jump_decomposition(Cm, Cp, H, H)
        self.assertEqual(dec.total, dec.reconstructed)
        self.assertEqual(dec.metric_revaluation, 0)
        self.assertEqual(dec.total, dec.covariance_reset_at_new_metric)


if __name__ == "__main__":
    unittest.main()
