from __future__ import annotations

import unittest
import sympy as sp


class SymbolicIdentityAudit(unittest.TestCase):
    def test_exact_multimode_periodic_ns_shear(self) -> None:
        x, y, z, t, nu = sp.symbols("x y z t nu", positive=True)
        modes = [
            sp.exp(-nu * t) * sp.cos(y),
            sp.Rational(1, 2) * sp.exp(-9 * nu * t) * sp.cos(3 * y),
            sp.Rational(1, 3) * sp.exp(-25 * nu * t) * sp.cos(5 * y),
        ]
        U = sp.Add(*modes)
        u = sp.Matrix([U, 0, 0])
        coords = (x, y, z)
        divergence = sum(sp.diff(u[i], coords[i]) for i in range(3))
        nonlinear = sp.Matrix([
            sum(u[j] * sp.diff(u[i], coords[j]) for j in range(3))
            for i in range(3)
        ])
        laplacian = sp.Matrix([
            sum(sp.diff(u[i], c, 2) for c in coords) for i in range(3)
        ])
        residual = sp.simplify(sp.diff(u, t) + nonlinear - nu * laplacian)
        self.assertEqual(sp.simplify(divergence), 0)
        self.assertEqual(nonlinear, sp.zeros(3, 1))
        self.assertEqual(residual, sp.zeros(3, 1))

    def test_pair_branching_diagonal_identity(self) -> None:
        x1, x2, x, nu = sp.symbols("x1 x2 x nu")
        b = x**2 + 1
        U = x1**3 * x2**2 + 2 * x1 * x2 + x1**2 + 7 * x2
        Udiag = U.subs({x1: x, x2: x})
        Ldiag = b * sp.diff(Udiag, x) + nu * sp.diff(Udiag, x, 2)
        b1 = (x1**2 + 1)
        b2 = (x2**2 + 1)
        L12 = (
            b1 * sp.diff(U, x1) + nu * sp.diff(U, x1, 2)
            + b2 * sp.diff(U, x2) + nu * sp.diff(U, x2, 2)
        ).subs({x1: x, x2: x})
        cross = (2 * nu * sp.diff(U, x1, x2)).subs({x1: x, x2: x})
        self.assertEqual(sp.simplify(Ldiag - L12 - cross), 0)

    def test_kelvin_quadratic_polarization(self) -> None:
        a, da, nu = sp.symbols("a da nu")
        gamma = lambda q: 2 * nu * q**2
        mixed = 4 * nu * a * da
        self.assertEqual(sp.expand(gamma(a + da) - gamma(a) - gamma(da) - mixed), 0)

    def test_normalized_ancestry_variance_current_identity_1d(self) -> None:
        x, t, nu, K, gamma = sp.symbols("x t nu K gamma")
        f = sp.Function("f")(x, t)
        phi = sp.Function("phi")(x)
        w = sp.Function("w")(x, t)
        V = sp.Function("V")(x, t)
        q = f * phi
        j = w - nu * K * sp.diff(sp.log(f), x)
        L_V = w * sp.diff(V, x) + nu / phi * sp.diff(phi * K * sp.diff(V, x), x)
        q_t_from_forward = -sp.diff(q * j, x)
        V_t_from_backward = -L_V - gamma
        balance = (
            q_t_from_forward * V
            + q * V_t_from_backward
            + sp.diff(q * j * V + nu * q * K * sp.diff(V, x), x)
            + q * gamma
        )
        self.assertEqual(sp.simplify(sp.expand(balance.doit())), 0)

    def test_full_pair_refinement_contains_mandatory_cross_covariance(self) -> None:
        a, b = sp.symbols("a b")
        C11, C12, C22 = sp.symbols("C11 C12 C22")
        full = a**2 * C11 + 2 * a * b * C12 + b**2 * C22
        diagonal = a**2 * C11 + b**2 * C22
        self.assertEqual(sp.expand(full - diagonal), 2 * a * b * C12)
        # If the two child payoffs are exact negatives, C12=-C11=-C22 with
        # equal diagonal variances and equal weights.  The physical parent then
        # has zero variance while the diagonal-only lift remains positive.
        V = sp.symbols("V", positive=True)
        anti = full.subs({a: 1, b: 1, C11: V, C22: V, C12: -V})
        diag_anti = diagonal.subs({a: 1, b: 1, C11: V, C22: V})
        self.assertEqual(sp.simplify(anti), 0)
        self.assertEqual(sp.simplify(diag_anti), 2 * V)

    def test_pair_refinement_tensor_lift_is_functorial_under_composition(self) -> None:
        R1 = sp.Matrix([[sp.Rational(1, 2), 0], [sp.Rational(1, 2), 1]])
        R2 = sp.Matrix([[1, sp.Rational(1, 3)], [0, sp.Rational(2, 3)]])
        lhs = sp.kronecker_product(R2 * R1, R2 * R1)
        rhs = sp.kronecker_product(R2, R2) * sp.kronecker_product(R1, R1)
        self.assertEqual(lhs, rhs)

    def test_covariance_pullback_composes_exactly_under_refinement(self) -> None:
        R1 = sp.Matrix([[1, 0], [sp.Rational(1, 2), sp.Rational(1, 2)]])
        R2 = sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 3)], [0, 1]])
        C = sp.Matrix([[3, -1], [-1, 2]])
        direct = (R2 * R1).T * C * (R2 * R1)
        staged = R1.T * (R2.T * C * R2) * R1
        self.assertEqual(sp.simplify(direct - staged), sp.zeros(2))

    def test_diagonal_pair_projection_breaks_refinement_naturality(self) -> None:
        a, b = sp.symbols("a b", nonzero=True)
        full = sp.Matrix([a**2, a*b, a*b, b**2])
        diagonal_projection = sp.diag(1, 0, 0, 1)
        lost = sp.simplify(full - diagonal_projection * full)
        self.assertEqual(lost, sp.Matrix([0, a*b, a*b, 0]))
        self.assertNotEqual(lost, sp.zeros(4, 1))

    def test_exact_abc_beltrami_navier_stokes_with_pressure(self) -> None:
        x, y, z, t, nu = sp.symbols("x y z t nu", positive=True)
        U = sp.Matrix([
            sp.sin(z) + sp.cos(y),
            sp.sin(x) + sp.cos(z),
            sp.sin(y) + sp.cos(x),
        ])
        amp = sp.exp(-nu * t)
        u = amp * U
        coords = (x, y, z)
        div = sum(sp.diff(u[i], coords[i]) for i in range(3))
        curl = sp.Matrix([
            sp.diff(u[2], y) - sp.diff(u[1], z),
            sp.diff(u[0], z) - sp.diff(u[2], x),
            sp.diff(u[1], x) - sp.diff(u[0], y),
        ])
        lap = sp.Matrix([sum(sp.diff(u[i], q, 2) for q in coords) for i in range(3)])
        adv = sp.Matrix([
            sum(u[j] * sp.diff(u[i], coords[j]) for j in range(3))
            for i in range(3)
        ])
        p = -sp.Rational(1, 2) * u.dot(u)
        grad_p = sp.Matrix([sp.diff(p, q) for q in coords])
        residual = sp.Matrix([
            sp.trigsimp(sp.diff(u[i], t) + adv[i] + grad_p[i] - nu * lap[i])
            for i in range(3)
        ])
        self.assertEqual(sp.simplify(div), 0)
        self.assertEqual(sp.Matrix([sp.trigsimp(curl[i] - u[i]) for i in range(3)]), sp.zeros(3, 1))
        self.assertEqual(sp.Matrix([sp.trigsimp(lap[i] + u[i]) for i in range(3)]), sp.zeros(3, 1))
        self.assertEqual(residual, sp.zeros(3, 1))
        self.assertTrue(any(sp.simplify(component) != 0 for component in adv))

    def test_multidimensional_pair_branching_tensor_is_2nuK(self) -> None:
        x, y, X1, Y1, X2, Y2, nu = sp.symbols("x y X1 Y1 X2 Y2 nu")
        k11, k12, k22 = sp.symbols("k11 k12 k22")
        b1 = x**2 + y
        b2 = x - y**2
        U = X1**2 * X2 + X1 * Y1 * Y2 + Y1**2 * Y2**2 + X2 * Y2
        diag = U.subs({X1: x, Y1: y, X2: x, Y2: y})

        def L_xy(expr, xx, yy, drift1, drift2):
            return (
                drift1 * sp.diff(expr, xx)
                + drift2 * sp.diff(expr, yy)
                + nu * (
                    k11 * sp.diff(expr, xx, 2)
                    + 2 * k12 * sp.diff(expr, xx, yy)
                    + k22 * sp.diff(expr, yy, 2)
                )
            )

        Ldiag = L_xy(diag, x, y, b1, b2)
        b1_1, b2_1 = X1**2 + Y1, X1 - Y1**2
        b1_2, b2_2 = X2**2 + Y2, X2 - Y2**2
        Lrep = (
            L_xy(U, X1, Y1, b1_1, b2_1)
            + L_xy(U, X2, Y2, b1_2, b2_2)
        ).subs({X1: x, Y1: y, X2: x, Y2: y})
        cross = 2 * nu * (
            k11 * sp.diff(U, X1, X2)
            + k12 * sp.diff(U, X1, Y2)
            + k12 * sp.diff(U, Y1, X2)
            + k22 * sp.diff(U, Y1, Y2)
        ).subs({X1: x, Y1: y, X2: x, Y2: y})
        self.assertEqual(sp.simplify(Ldiag - Lrep - cross), 0)

    def test_quadratic_diagonal_refinement_is_not_additive(self) -> None:
        Q, n = sp.symbols("Q n", positive=True)
        # Q(delta/n)=Q(delta)/n^2 for a quadratic form; summing n pieces gives Q/n.
        refined_sum = n * Q / n**2
        self.assertEqual(sp.simplify(refined_sum), Q / n)
        self.assertNotEqual(sp.simplify(refined_sum - Q), 0)


if __name__ == "__main__":
    unittest.main()
