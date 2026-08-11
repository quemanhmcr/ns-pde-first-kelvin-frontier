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

    def test_exact_one_mode_kelvin_future_variance_pde(self) -> None:
        a, tau, nu, k = sp.symbols("a tau nu k", positive=True)
        r = nu * k**2 * tau
        m = sp.exp(-r) * sp.cos(k * a)
        second = sp.Rational(1, 2) * (1 + sp.exp(-4 * r) * sp.cos(2 * k * a))
        V = sp.simplify(second - m**2)
        gamma = 2 * nu * sp.diff(m, a) ** 2
        residual = sp.simplify(sp.diff(V, tau) - nu * sp.diff(V, a, 2) - gamma)
        self.assertEqual(sp.trigsimp(residual), 0)

    def test_exact_one_mode_anchor_localization_derivative_is_covariance(self) -> None:
        a, tau, nu, k = sp.symbols("a tau nu k", positive=True)
        r = nu * k**2 * tau
        m = sp.exp(-r) * sp.cos(k * a)
        dm = sp.diff(m, a)
        second = sp.Rational(1, 2) * (1 + sp.exp(-4 * r) * sp.cos(2 * k * a))
        V = sp.simplify(second - m**2)
        # E[X d_a X] for X=cos(k(a+sqrt(2 nu tau)Z)).
        EXdX = -sp.Rational(1, 2) * k * sp.exp(-4 * r) * sp.sin(2 * k * a)
        covariance = sp.simplify(EXdX - m * dm)
        self.assertEqual(sp.trigsimp(sp.diff(V, a) - 2 * covariance), 0)

    def test_exact_one_mode_kelvin_action_is_noise_carre_du_champ(self) -> None:
        a, tau, nu, k = sp.symbols("a tau nu k", positive=True)
        m = sp.exp(-nu * k**2 * tau) * sp.cos(k * a)
        gamma = 2 * nu * sp.diff(m, a) ** 2
        expected = 2 * nu * k**2 * sp.exp(-2 * nu * k**2 * tau) * sp.sin(k * a) ** 2
        self.assertEqual(sp.simplify(gamma - expected), 0)

    def test_variable_frame_cartan_identity_and_nontranslation_geometry(self) -> None:
        x, y, z = sp.symbols("x y z")
        coords = (x, y, z)
        xi = sp.Matrix([x * y, y * z, z * x])
        # Closed vorticity 2-form dual to omega=(sin y, sin z, sin x).
        O = sp.MutableDenseMatrix(3, 3, [0] * 9)
        O[0, 1] = sp.sin(x); O[1, 0] = -O[0, 1]
        O[1, 2] = sp.sin(y); O[2, 1] = -O[1, 2]
        O[2, 0] = sp.sin(z); O[0, 2] = -O[2, 0]
        dO = sp.diff(O[1, 2], x) - sp.diff(O[0, 2], y) + sp.diff(O[0, 1], z)
        self.assertEqual(sp.simplify(dO), 0)

        # b=i_xi Omega, b_i=xi^k Omega_{k i}; then db is a 2-form.
        b = sp.Matrix([sum(xi[k] * O[k, i] for k in range(3)) for i in range(3)])
        db = sp.MutableDenseMatrix(3, 3, [0] * 9)
        for i in range(3):
            for j in range(3):
                db[i, j] = sp.simplify(sp.diff(b[j], coords[i]) - sp.diff(b[i], coords[j]))

        # Coordinate Lie derivative of a covariant 2-form.
        L = sp.MutableDenseMatrix(3, 3, [0] * 9)
        naive = sp.MutableDenseMatrix(3, 3, [0] * 9)
        for i in range(3):
            for j in range(3):
                naive[i, j] = sum(xi[k] * sp.diff(O[i, j], coords[k]) for k in range(3))
                L[i, j] = sp.simplify(
                    naive[i, j]
                    + sum(O[k, j] * sp.diff(xi[k], coords[i]) for k in range(3))
                    + sum(O[i, k] * sp.diff(xi[k], coords[j]) for k in range(3))
                )
                self.assertEqual(sp.simplify(L[i, j] - db[i, j]), 0)

        # Nonconstant frame geometry is real: Lie transport is not coefficientwise
        # directional differentiation alone.
        self.assertTrue(any(sp.simplify(L[i, j] - naive[i, j]) != 0 for i in range(3) for j in range(3)))
        dL = sp.diff(L[1, 2], x) - sp.diff(L[0, 2], y) + sp.diff(L[0, 1], z)
        self.assertEqual(sp.simplify(sp.trigsimp(dL)), 0)

    def test_variable_coefficient_noise_pair_branching_is_cross_derivation(self) -> None:
        x, y, X1, Y1, X2, Y2 = sp.symbols("x y X1 Y1 X2 Y2")
        U = X1**2 * Y2 + X2 * Y1**2 + X1 * X2 * Y1 * Y2

        def D(expr, xx, yy):
            xi1 = 1 + xx**2
            xi2 = 1 + xx * yy
            return xi1 * sp.diff(expr, xx) + xi2 * sp.diff(expr, yy)

        diag = U.subs({X1: x, Y1: y, X2: x, Y2: y})
        lhs = sp.expand(D(D(diag, x, y), x, y))
        D1 = lambda expr: D(expr, X1, Y1)
        D2 = lambda expr: D(expr, X2, Y2)
        rhs_diag = (D1(D1(U)) + D2(D2(U))).subs({X1: x, Y1: y, X2: x, Y2: y})
        cross = (2 * D1(D2(U))).subs({X1: x, Y1: y, X2: x, Y2: y})
        self.assertEqual(sp.simplify(lhs - rhs_diag - cross), 0)

    def test_quadratic_diagonal_refinement_is_not_additive(self) -> None:
        Q, n = sp.symbols("Q n", positive=True)
        # Q(delta/n)=Q(delta)/n^2 for a quadratic form; summing n pieces gives Q/n.
        refined_sum = n * Q / n**2
        self.assertEqual(sp.simplify(refined_sum), Q / n)
        self.assertNotEqual(sp.simplify(refined_sum - Q), 0)


if __name__ == "__main__":
    unittest.main()
