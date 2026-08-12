from __future__ import annotations

import unittest

import sympy as sp

from src.pde_audit.full_current_shape_covariance import (
    anchor_cross_carre_du_champ,
    closed_current_cartan_noise_residual,
    deformation_kelvin_cross_carre_du_champ,
    deformation_kelvin_cross_covariance_horizon_residual,
    deformation_kelvin_cross_covariance_leading_tensor,
    full_state_carre_du_champ,
    joint_deformation_kelvin_leading_covariance,
    joint_deformation_kelvin_leading_gramian_residual,
    kelvin_pair_anchor_source,
    navier_stokes_kelvin_gauge_residual,
    one_mode_shear_deformation_kelvin_cross_covariance,
    one_mode_shear_deformation_kelvin_cross_leading_residual,
    one_mode_shear_kelvin_mean,
    one_mode_shear_kelvin_variance,
    reverse_age_current_shape_diffusion_covariance,
    reverse_age_current_shape_drift,
    translation_cartan_residual,
)
from src.pde_audit.future_covariance_tensor import connected_covariance_horizon_residual
from src.pde_audit.stochastic_cauchy_deformation import (
    column_vectorize,
    one_mode_shear_deformation_mean_coefficient,
    reverse_age_horizon_operator_matrix,
)


class FullCurrentShapeCovarianceAudit(unittest.TestCase):
    def test_full_state_noise_is_anchor_only_even_with_shape_and_D_coordinates(self) -> None:
        nu = sp.symbols("nu", positive=True)
        a = reverse_age_current_shape_diffusion_covariance(2, 2, 2, nu)
        self.assertEqual(a.shape, (10, 10))
        self.assertEqual(a[:2, :2], 2 * nu * sp.eye(2))
        self.assertEqual(a[2:, :], sp.zeros(8, 10))
        self.assertEqual(a[:, 2:], sp.zeros(10, 8))

    def test_reverse_age_full_state_drift_types_anchor_shape_and_deformation_separately(self) -> None:
        u1, u2, v11, v12, v21, v22 = sp.symbols("u1 u2 v11 v12 v21 v22")
        a, b, c, d, p, q, r, s = sp.symbols("a b c d p q r s")
        u = sp.Matrix([u1, u2])
        v1 = sp.Matrix([v11, v12])
        v2 = sp.Matrix([v21, v22])
        D = sp.Matrix([[a, b], [c, d]])
        A = sp.Matrix([[p, q], [r, s]])
        drift = reverse_age_current_shape_drift(u, [v1, v2], D, A)
        expected = sp.Matrix.vstack(
            -u,
            -(v1 - u),
            -(v2 - u),
            column_vectorize(D * A.T),
        )
        self.assertEqual(sp.simplify(drift - expected), sp.zeros(10, 1))

    def test_full_state_carre_du_champ_ignores_finite_variation_shape_and_D_derivatives(self) -> None:
        X1, X2, R1, R2, d11, d21, d12, d22, nu = sp.symbols(
            "X1 X2 R1 R2 d11 d21 d12 d22 nu"
        )
        coords = (X1, X2, R1, R2, d11, d21, d12, d22)
        a = reverse_age_current_shape_diffusion_covariance(1, 2, 2, nu)
        mean = sp.Matrix([
            X1 * R1 + d11 * X2 + R2**2,
            X2 * d22 + R1 * d12 + X1**2,
        ])
        full = full_state_carre_du_champ(mean, coords, a)
        anchor = anchor_cross_carre_du_champ(mean, mean, (X1, X2), nu)
        self.assertEqual(sp.simplify(full - anchor), sp.zeros(2))

    def test_exact_ns_one_form_drift_is_pure_kelvin_gauge_on_closed_current(self) -> None:
        x, y, t, nu, k = sp.symbols("x y t nu k", positive=True)
        U = sp.exp(-nu * k**2 * t) * sp.cos(k * y)
        u = sp.Matrix([U, 0])
        residual = navier_stokes_kelvin_gauge_residual(u, sp.Integer(0), t, (x, y), nu)
        self.assertEqual(sp.trigsimp(sp.simplify(residual)), sp.zeros(2, 1))
        # Constant-frame Cartan decomposition of the Brownian translation derivative.
        self.assertEqual(translation_cartan_residual(u, (x, y), 0), sp.zeros(2, 1))
        self.assertEqual(translation_cartan_residual(u, (x, y), 1), sp.zeros(2, 1))
        # In the y-noise direction i_e_y du^flat = U_y dx: this is the normalized
        # x-cycle Kelvin noise coefficient used by the exact shear cross calibration.
        contraction_y = sp.Matrix([sp.diff(U, y), 0])
        self.assertEqual(contraction_y[0], sp.diff(one_mode_shear_kelvin_mean(y, t, nu, k), y))

    def test_closed_current_cartan_kills_exact_translation_gauge_term(self) -> None:
        B = sp.Matrix([
            [-1, 0, 1],
            [1, -1, 0],
            [0, 1, -1],
        ])
        Z = sp.Matrix([1, 1, 1])
        b1, b2, b3, p1, p2, p3 = sp.symbols("b1 b2 b3 p1 p2 p3")
        b = sp.Matrix([b1, b2, b3])
        p = sp.Matrix([p1, p2, p3])
        self.assertEqual(B * Z, sp.zeros(3, 1))
        self.assertEqual(closed_current_cartan_noise_residual(B, Z, b, p), 0)

    def test_anchor_carre_du_champ_becomes_literal_kelvin_pair_source(self) -> None:
        x, y, nu = sp.symbols("x y nu")
        left = sp.Matrix([x**2 + x * y])
        right = sp.Matrix([x - y**2])
        source = anchor_cross_carre_du_champ(left, right, (x, y), nu)[0]
        coeff_left = [sp.diff(left[0], x), sp.diff(left[0], y)]
        coeff_right = [sp.diff(right[0], x), sp.diff(right[0], y)]
        self.assertEqual(sp.simplify(source - kelvin_pair_anchor_source(coeff_left, coeff_right, nu)), 0)

    def test_deformation_kelvin_cross_source_is_joint_anchor_carre_du_champ_block(self) -> None:
        x, y, nu = sp.symbols("x y nu")
        meanD = sp.Matrix([[1 + x*y, x], [y**2, 1]])
        K = sp.Matrix([x**2 - y])
        joint = column_vectorize(meanD).col_join(K)
        full = anchor_cross_carre_du_champ(joint, joint, (x, y), nu)
        cross = deformation_kelvin_cross_carre_du_champ(
            [sp.diff(meanD, x), sp.diff(meanD, y)],
            [sp.diff(K[0], x), sp.diff(K[0], y)],
            nu,
        )
        self.assertEqual(sp.simplify(full[:4, 4:5] - cross), sp.zeros(4, 1))

    def test_joint_short_horizon_block_has_exact_gram_integral_and_forced_h3_h2_h_scaling(self) -> None:
        nu, h = sp.symbols("nu h", positive=True)
        a, b, c, d, e, f, g, q = sp.symbols("a b c d e f g q")
        dA1 = sp.Matrix([[a, b], [c, d]])
        dA2 = sp.Matrix([[e, f], [g, q]])
        k1, k2 = sp.symbols("k1 k2")
        residual = joint_deformation_kelvin_leading_gramian_residual(
            [dA1, dA2], [k1, k2], nu, h
        )
        self.assertEqual(residual, sp.zeros(5))
        joint = joint_deformation_kelvin_leading_covariance(
            [dA1, dA2], [k1, k2], nu, h
        )
        # The diagonal blocks have h^3 and h; the mixed block has the forced h^2.
        self.assertEqual(sp.simplify(joint[4, 4] / h), 2 * nu * (k1**2 + k2**2))
        cross = deformation_kelvin_cross_covariance_leading_tensor(
            [dA1, dA2], [k1, k2], nu, h
        )
        self.assertEqual(sp.simplify(joint[:4, 4:5] - cross), sp.zeros(4, 1))
        self.assertTrue(all(sp.simplify(v / h**2).has(nu) for v in cross if v != 0))

    def test_exact_shear_joint_D_K_covariance_is_existing_connected_theorem_block(self) -> None:
        x, y, t, h, nu, k = sp.symbols("x y t h nu k", positive=True)
        U = one_mode_shear_kelvin_mean(y, t, nu, k)
        Uy = sp.diff(U, y)
        A = sp.Matrix([[0, Uy], [0, 0]])
        mean_c = one_mode_shear_deformation_mean_coefficient(y, t, h, nu, k)
        meanD = sp.Matrix([[1, 0], [mean_c, 1]])
        zbar = column_vectorize(meanD)
        Kbar = one_mode_shear_kelvin_mean(y, t, nu, k)
        mean_joint = zbar.col_join(sp.Matrix([Kbar]))

        from src.pde_audit.stochastic_cauchy_deformation import one_mode_shear_deformation_variance, vectorized_horizon_connection
        var_c = one_mode_shear_deformation_variance(y, t, h, nu, k)
        E21 = sp.Matrix([[0, 0], [1, 0]])
        v = column_vectorize(E21)
        Sigma_D = sp.simplify(var_c * v * v.T)
        C_DK = sp.simplify(
            one_mode_shear_deformation_kelvin_cross_covariance(y, t, h, nu, k) * v
        )
        V_K = one_mode_shear_kelvin_variance(y, t, h, nu, k)
        covariance = Sigma_D.row_join(C_DK).col_join(C_DK.T.row_join(sp.Matrix([[V_K]])))
        second = sp.simplify(covariance + mean_joint * mean_joint.T)

        B_h = vectorized_horizon_connection(A)
        # connected theorem convention is H mean + B_conn^T mean=0.
        B_conn = sp.diag(1, 1, 1, 1, 1)
        B_conn[:4, :4] = -B_h.T
        B_conn[4, 4] = 0
        # Coordinates include physical time; reverse-age generator has rdot=-1,
        # anchor drift -u, and covariance 2nu I in spatial coordinates.
        coords = (x, y, t)
        drift = sp.Matrix([-U, 0, -1])
        diffusion = sp.diag(2 * nu, 2 * nu, 0)
        residual = connected_covariance_horizon_residual(
            mean_joint, second, B_conn, h, drift, diffusion, coords
        )
        self.assertEqual(sp.trigsimp(sp.simplify(residual)), sp.zeros(5))
        # The mixed deformation--Kelvin covariance is literally the off-diagonal block.
        self.assertEqual(sp.simplify(covariance[:4, 4:5] - C_DK), sp.zeros(4, 1))

    def test_exact_one_mode_ns_cross_covariance_referees_sign_factor_and_h2_onset(self) -> None:
        x, y, t, h, nu, k = sp.symbols("x y t h nu k", positive=True)
        alpha = nu * k**2
        U = one_mode_shear_kelvin_mean(y, t, nu, k)
        Uy = sp.diff(U, y)
        A = sp.Matrix([[0, Uy], [0, 0]])
        velocity = sp.Matrix([U, 0])
        mean_c = one_mode_shear_deformation_mean_coefficient(y, t, h, nu, k)
        meanD = sp.Matrix([[1, 0], [mean_c, 1]])
        scalar_cross = one_mode_shear_deformation_kelvin_cross_covariance(y, t, h, nu, k)
        E21 = sp.Matrix([[0, 0], [1, 0]])
        C = scalar_cross * column_vectorize(E21)
        HC = reverse_age_horizon_operator_matrix(C, h, t, velocity, nu, (x, y))
        dM = [sp.diff(meanD, x), sp.diff(meanD, y)]
        dK = [sp.diff(U, x), sp.diff(U, y)]
        self.assertEqual(
            deformation_kelvin_cross_covariance_horizon_residual(C, HC, A, dM, dK, nu),
            sp.zeros(4, 1),
        )
        self.assertEqual(
            one_mode_shear_deformation_kelvin_cross_leading_residual(y, t, h, nu, k),
            0,
        )
        expected = sp.simplify(nu * h**2 * sp.diff(U, y, 2) * sp.diff(U, y))
        series = sp.series(scalar_cross, h, 0, 3).removeO()
        self.assertEqual(sp.trigsimp(sp.simplify(series - expected)), 0)
        # Direct closed form contains the positive bracket 2 alpha h - 1 + exp(-2 alpha h).
        bracket = sp.simplify(2 * alpha * h - 1 + sp.exp(-2 * alpha * h))
        self.assertEqual(
            sp.simplify(
                scalar_cross
                - k * sp.exp(-2 * alpha * t) * sp.sin(2 * k * y) * bracket / (4 * alpha)
            ),
            0,
        )


if __name__ == "__main__":
    unittest.main()
