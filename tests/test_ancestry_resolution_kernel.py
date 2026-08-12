from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.ancestry_resolution_kernel import (
    affine_shear_joint_state_covariance,
    affine_shear_ns_residual,
    affine_shear_relative_shape,
    flat_anchor_marginal_fp_operator_1d,
    flat_conditional_shape_operator_1d,
    flat_joint_fp_operator_1d,
    flat_joint_marginal_conditional_factorization_residual_1d,
    generator_carre_du_champ_scalar,
    hidden_two_state_mean,
    hidden_two_state_resolution_variance,
    kernel_covariances,
    kernel_intertwining_residual,
    kernel_mean,
    scalar_pair_resolution_variance,
    resolution_horizon_source_scalar,
    scalar_resolution_variance,
    total_variance_decomposition,
)


class AncestryResolutionKernelAudit(unittest.TestCase):

    def test_joint_common_noise_density_factorizes_into_anchor_marginal_and_backward_conditional_shape_pde(self) -> None:
        x,r,t,nu=sp.symbols("x r t nu", positive=True)
        q=sp.Function("q")(x,t)
        k=sp.Function("k")(x,r,t)
        b=sp.Function("b")(x,t)
        v=sp.Function("v")(x,r,t)
        residual=flat_joint_marginal_conditional_factorization_residual_1d(q,k,b,v,x,r,t,nu)
        self.assertEqual(residual,0)

    def test_conditional_shape_anchor_drift_is_exact_time_reversed_drift(self) -> None:
        x,r,t,nu,b0,c=sp.symbols("x r t nu b0 c", positive=True)
        q=sp.exp(-c*x**2)
        k=sp.Function("k")(x,r,t)
        b=sp.Integer(0)
        v=sp.Integer(0)
        C=flat_conditional_shape_operator_1d(k,q,b,v,x,r,t,nu)
        bminus=4*nu*c*x
        expected=sp.diff(k,t)+bminus*sp.diff(k,x)-nu*sp.diff(k,x,2)
        self.assertEqual(sp.simplify(C-expected),0)

    def test_joint_and_marginal_zero_force_conditional_kernel_equation_algebraically(self) -> None:
        x,r,t,nu=sp.symbols("x r t nu", positive=True)
        q=sp.Function("q")(x,t)
        k=sp.Function("k")(x,r,t)
        b=sp.Function("b")(x,t)
        v=sp.Function("v")(x,r,t)
        J=flat_joint_fp_operator_1d(q*k,b,v,x,r,t,nu)
        M=flat_anchor_marginal_fp_operator_1d(q,b,x,t,nu)
        C=flat_conditional_shape_operator_1d(k,q,b,v,x,r,t,nu)
        self.assertEqual(sp.simplify(J-k*M-q*C),0)

    def test_pair_resolution_identity_is_exact_conditional_variance(self) -> None:
        p, a, b = sp.symbols("p a b", real=True)
        R = sp.Matrix([[p, 1 - p]])
        F = sp.Matrix([[a], [b]])
        self.assertEqual(
            sp.simplify(scalar_pair_resolution_variance(R, F) - scalar_resolution_variance(R, F)),
            sp.zeros(1, 1),
        )

    def test_two_hidden_shapes_can_carry_variance_with_zero_viscous_future_bank(self) -> None:
        a = sp.symbols("a", real=True)
        R = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]])
        means = sp.Matrix([[a], [-a]])
        full_V = sp.zeros(2, 1)
        avg, resolution, total = total_variance_decomposition(R, means, full_V)
        self.assertEqual(avg, sp.zeros(1, 1))
        self.assertEqual(resolution, sp.Matrix([a**2]))
        self.assertEqual(total, sp.Matrix([a**2]))

    def test_deterministic_dirac_lift_has_zero_resolution_covariance(self) -> None:
        a, b = sp.symbols("a b")
        R = sp.eye(2)
        F = sp.Matrix([[a], [b]])
        self.assertEqual(scalar_resolution_variance(R, F), sp.zeros(2, 1))

    def test_vector_resolution_covariance_keeps_cross_orientation_terms(self) -> None:
        R = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]])
        F = sp.Matrix([[1, 2, -1], [-1, 0, 3]])
        C = kernel_covariances(R, F)[0]
        d = sp.Matrix([2, 2, -4])  # F_1-F_2
        self.assertEqual(sp.simplify(C - sp.Rational(1, 4) * d * d.T), sp.zeros(3))
        self.assertNotEqual(C[0, 2], 0)

    def test_stationary_hidden_shape_kernel_can_intertwine_exactly_while_hiding_variance(self) -> None:
        lam, a = sp.symbols("lam a", positive=True)
        Lphys = sp.Matrix([[-lam, lam], [lam, -lam]])
        Lred = sp.zeros(1)
        R = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]])
        self.assertEqual(kernel_intertwining_residual(Lred, R, Lphys), sp.zeros(1, 2))
        F = sp.Matrix([[a], [-a]])
        self.assertEqual(kernel_mean(R, F), sp.zeros(1, 1))
        self.assertEqual(scalar_resolution_variance(R, F), sp.Matrix([a**2]))

    def test_resolution_variance_exists_even_without_hidden_dynamics(self) -> None:
        a = sp.symbols("a", real=True)
        Lphys = sp.zeros(2)
        Lred = sp.zeros(1)
        R = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]])
        self.assertEqual(kernel_intertwining_residual(Lred, R, Lphys), sp.zeros(1, 2))
        self.assertEqual(scalar_resolution_variance(R, sp.Matrix([[a], [-a]])), sp.Matrix([a**2]))


    def test_resolution_covariance_horizon_source_is_carre_du_champ_mismatch(self) -> None:
        lam, a, tau = sp.symbols("lam a tau", positive=True)
        Lfull = sp.Matrix([[-lam, lam], [lam, -lam]])
        Lred = sp.zeros(1)
        R = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]])
        m = hidden_two_state_mean(a, lam, tau)
        Cres = hidden_two_state_resolution_variance(a, lam, tau)
        source = resolution_horizon_source_scalar(Lred, R, Lfull, m)
        # H_red=partial_tau because the reduced generator is zero.
        self.assertEqual(sp.simplify(sp.diff(Cres, tau) - source[0]), 0)
        self.assertEqual(source, sp.Matrix([-4 * a**2 * lam * sp.exp(-4 * lam * tau)]))

    def test_full_hidden_carre_du_champ_feeds_resolution_decay_exactly(self) -> None:
        lam, a, tau = sp.symbols("lam a tau", positive=True)
        Lfull = sp.Matrix([[-lam, lam], [lam, -lam]])
        R = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]])
        m = hidden_two_state_mean(a, lam, tau)
        gamma_full = generator_carre_du_champ_scalar(Lfull, m)
        expected = 4 * lam * a**2 * sp.exp(-4 * lam * tau)
        self.assertEqual(gamma_full, sp.Matrix([expected, expected]))
        self.assertEqual(sp.simplify((R * gamma_full)[0] - expected), 0)

    def test_reduced_total_covariance_recovers_reduced_carre_du_champ_law(self) -> None:
        # Algebraic source cancellation: R Gamma_full + (Gamma_red-R Gamma_full)=Gamma_red.
        g1, g2, Gred, p = sp.symbols("g1 g2 Gred p")
        R = sp.Matrix([[p, 1-p]])
        Gfull = sp.Matrix([g1, g2])
        averaged_full_source = (R * Gfull)[0]
        resolution_source = sp.simplify(Gred - averaged_full_source)
        self.assertEqual(sp.simplify(averaged_full_source + resolution_source - Gred), 0)

    def test_exact_affine_shear_has_deterministic_relative_shape(self) -> None:
        x, y, z, t, nu, a = sp.symbols("x y z t nu a")
        self.assertEqual(affine_shear_ns_residual(a, (x, y, z), t, nu), sp.zeros(3, 1))
        rx, ry, rz, tau = sp.symbols("rx ry rz tau")
        R = affine_shear_relative_shape(a, sp.Matrix([rx, ry, rz]), tau)
        self.assertEqual(R, sp.Matrix([rx + a * tau * ry, ry, rz]))

    def test_fixed_shape_affine_shear_full_state_law_is_singular_in_shape_directions(self) -> None:
        c1, c2, c3 = sp.symbols("c1 c2 c3", positive=True)
        Cx = sp.diag(c1, c2, c3)
        C = affine_shear_joint_state_covariance(Cx)
        self.assertEqual(C.rank(), 3)
        self.assertEqual(sp.det(C), 0)
        self.assertEqual(C[3:, 3:], sp.zeros(3))

    def test_reduced_branch_and_full_branch_are_state_definition_sensitive(self) -> None:
        a = sp.symbols("a", real=True)
        payoff = sp.Matrix([[a], [-a]])
        # Full physical ancestor knows which shape: Dirac kernels -> no branch-time resolution variance.
        full_R = sp.eye(2)
        self.assertEqual(scalar_resolution_variance(full_R, payoff), sp.zeros(2, 1))
        # Reduced ancestor forgets shape: same reduced label carries positive resolution covariance.
        reduced_R = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]])
        self.assertEqual(scalar_resolution_variance(reduced_R, payoff), sp.Matrix([a**2]))


if __name__ == "__main__":
    unittest.main()
