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

    def test_quadratic_diagonal_refinement_is_not_additive(self) -> None:
        Q, n = sp.symbols("Q n", positive=True)
        # Q(delta/n)=Q(delta)/n^2 for a quadratic form; summing n pieces gives Q/n.
        refined_sum = n * Q / n**2
        self.assertEqual(sp.simplify(refined_sum), Q / n)
        self.assertNotEqual(sp.simplify(refined_sum - Q), 0)


if __name__ == "__main__":
    unittest.main()
