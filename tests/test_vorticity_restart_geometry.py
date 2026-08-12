from __future__ import annotations

import unittest
import sympy as sp

from src.pde_audit.vorticity_restart import (
    amplitude_direction_laplacian_residual,
    canonical_microframe_bulk_dissipation,
    curl3,
    enstrophy_density,
    frobenius_square,
    gradient,
    kelvin_microframe_bulk_dissipation,
    kelvin_microframe_density,
    kelvin_small_disk_action_from_local_gradient,
    laplacian_scalar,
    local_enstrophy_balance_residual,
    material_line_length_residual,
    microframe_reconstruction_residual,
    normalized_small_disk_action,
    renormalized_bank_chain_residual,
    renormalized_bank_derivative,
    skew_annihilates_vorticity_residual,
    strain_tensor,
    stretching_gate_margin,
    stretching_power,
    vorticity_equation_residual,
)


class VorticityRestartGeometryAudit(unittest.TestCase):
    def test_skew_velocity_gradient_cannot_stretch_its_own_vorticity(self) -> None:
        g = sp.symbols("g0:9")
        G = sp.Matrix(3, 3, g)
        self.assertEqual(skew_annihilates_vorticity_residual(G), sp.zeros(3, 1))

    def test_material_line_length_change_is_pure_strain(self) -> None:
        g = sp.symbols("g0:9")
        l1, l2, l3 = sp.symbols("l1 l2 l3")
        G = sp.Matrix(3, 3, g)
        ell = sp.Matrix([l1, l2, l3])
        self.assertEqual(material_line_length_residual(G, ell), 0)

    def test_three_closed_loop_normals_reconstruct_bulk_vorticity_gradient_dissipation(self) -> None:
        entries = sp.symbols("a0:9")
        nu = sp.symbols("nu", positive=True)
        Gomega = sp.Matrix(3, 3, entries)
        self.assertEqual(microframe_reconstruction_residual(Gomega, nu), 0)
        I = sp.eye(3)
        rotated = [
            sp.Matrix([1, 1, 0]) / sp.sqrt(2),
            sp.Matrix([1, -1, 0]) / sp.sqrt(2),
            sp.Matrix([0, 0, 1]),
        ]
        canonical = canonical_microframe_bulk_dissipation(Gomega, nu)
        other = kelvin_microframe_bulk_dissipation(Gomega, rotated, nu)
        self.assertEqual(sp.simplify(canonical - other), 0)
        self.assertEqual(sp.simplify(canonical - nu * frobenius_square(Gomega)), 0)

    def test_one_normal_kelvin_density_is_directional_gradient_content_not_full_bulk(self) -> None:
        a, b, c, nu = sp.symbols("a b c nu", nonzero=True)
        Gomega = sp.Matrix([[a, 0, 0], [0, b, 0], [0, 0, c]])
        n = sp.Matrix([1, 0, 0])
        gamma = kelvin_microframe_density(Gomega, n, nu)
        self.assertEqual(sp.simplify(gamma - 2 * nu * a**2), 0)
        self.assertNotEqual(sp.simplify(gamma / 2 - nu * frobenius_square(Gomega)), 0)

    def test_single_loop_orientation_can_be_exactly_blind_to_nonzero_bulk_dissipation(self) -> None:
        b, c, nu = sp.symbols("b c nu", positive=True)
        Gomega = sp.diag(0, b, c)
        blind = kelvin_microframe_density(Gomega, sp.Matrix([1, 0, 0]), nu)
        bulk = nu * frobenius_square(Gomega)
        self.assertEqual(blind, 0)
        self.assertEqual(sp.simplify(bulk - nu * (b**2 + c**2)), 0)
        self.assertNotEqual(bulk, 0)

    def test_raw_small_loop_action_scales_like_area_squared_while_density_is_invariant(self) -> None:
        a, b, c, A, lam, nu = sp.symbols("a b c A lam nu", positive=True)
        Gomega = sp.diag(a, b, c)
        n = sp.Matrix([0, 0, 1])
        raw = kelvin_small_disk_action_from_local_gradient(Gomega, n, A, nu)
        raw_scaled = kelvin_small_disk_action_from_local_gradient(Gomega, n, lam**2 * A, nu)
        self.assertEqual(sp.simplify(raw_scaled - lam**4 * raw), 0)
        self.assertEqual(
            sp.simplify(normalized_small_disk_action(raw_scaled, lam**2 * A) - normalized_small_disk_action(raw, A)),
            0,
        )

    def test_scale_renormalized_future_variance_bank_has_exact_dilation_work(self) -> None:
        V, gamma, work, A, Adot = sp.symbols("V gamma work A Adot", nonzero=True)
        self.assertEqual(renormalized_bank_chain_residual(V, gamma, work, A, Adot), 0)
        derivative = renormalized_bank_derivative(V, -gamma + work, A, Adot)
        expected = -gamma / A**2 + work / A**2 - 2 * Adot * V / A**3
        self.assertEqual(sp.simplify(derivative - expected), 0)

    def test_amplitude_direction_split_has_exact_directional_roughness_penalty(self) -> None:
        x, y = sp.symbols("x y", real=True)
        rho = sp.exp(x + 2 * y)
        theta = x - 3 * y
        xi = sp.Matrix([sp.cos(theta), sp.sin(theta), 0])
        self.assertEqual(amplitude_direction_laplacian_residual(rho, xi, (x, y)), 0)

    def test_exact_galilean_advected_shear_separates_advection_from_stretching(self) -> None:
        x, y, z, t, nu, k, U = sp.symbols("x y z t nu k U", positive=True)
        phase = k * (y - U * t)
        amp = sp.exp(-nu * k**2 * t)
        u = sp.Matrix([amp * sp.cos(phase), U, 0])
        coords = (x, y, z)
        omega = curl3(u, coords)
        grad_omega = gradient(omega, coords)
        advection = sp.Matrix([sp.trigsimp(sp.simplify(c)) for c in grad_omega * u])
        stretching = sp.Matrix([sp.trigsimp(sp.simplify(c)) for c in strain_tensor(u, coords) * omega])
        self.assertNotEqual(advection, sp.zeros(3, 1))
        self.assertEqual(stretching, sp.zeros(3, 1))
        self.assertEqual(vorticity_equation_residual(u, coords, t, nu), sp.zeros(3, 1))
        self.assertEqual(local_enstrophy_balance_residual(u, coords, t, nu), 0)

    def test_exact_ns_shear_has_no_vortex_stretching_and_closes_vorticity_enstrophy_balances(self) -> None:
        x, y, z, t, nu, k = sp.symbols("x y z t nu k", positive=True)
        amp = sp.exp(-nu * k**2 * t)
        u = sp.Matrix([amp * sp.cos(k * y), 0, 0])
        coords = (x, y, z)
        omega = curl3(u, coords)
        self.assertEqual(vorticity_equation_residual(u, coords, t, nu), sp.zeros(3, 1))
        self.assertEqual(sp.simplify(strain_tensor(u, coords) * omega), sp.zeros(3, 1))
        self.assertEqual(stretching_power(u, coords), 0)
        self.assertEqual(local_enstrophy_balance_residual(u, coords, t, nu), 0)
        Gomega = gradient(omega, coords)
        self.assertEqual(microframe_reconstruction_residual(Gomega, nu), 0)
        gammas = [sp.simplify(kelvin_microframe_density(Gomega, sp.eye(3)[:, j], nu)) for j in range(3)]
        self.assertEqual(gammas[0], 0)
        self.assertEqual(gammas[1], 0)
        self.assertNotEqual(gammas[2], 0)
        self.assertEqual(sp.simplify(sum(gammas) / 2 - nu * frobenius_square(Gomega)), 0)

    def test_exact_abc_has_nonzero_stretching_away_from_peak_but_exact_local_balance(self) -> None:
        x, y, z, t, nu = sp.symbols("x y z t nu", positive=True)
        amp = sp.exp(-nu * t)
        u = amp * sp.Matrix([
            sp.sin(z) + sp.cos(y),
            sp.sin(x) + sp.cos(z),
            sp.sin(y) + sp.cos(x),
        ])
        coords = (x, y, z)
        omega = curl3(u, coords)
        self.assertEqual(sp.Matrix([sp.trigsimp(sp.simplify(c)) for c in omega - u]), sp.zeros(3, 1))
        self.assertEqual(vorticity_equation_residual(u, coords, t, nu), sp.zeros(3, 1))
        self.assertEqual(local_enstrophy_balance_residual(u, coords, t, nu), 0)
        self.assertEqual(microframe_reconstruction_residual(gradient(omega, coords), nu), 0)
        p0 = {x: 0, y: 0, z: 0}
        self.assertEqual(sp.simplify(stretching_power(u, coords).subs(p0) - 3 * sp.exp(-3 * nu * t)), 0)

    def test_exact_abc_enstrophy_peak_separates_kelvin_bulk_dissipation_from_spatial_flux(self) -> None:
        x, y, z, t, nu = sp.symbols("x y z t nu", positive=True)
        amp = sp.exp(-nu * t)
        u = amp * sp.Matrix([
            sp.sin(z) + sp.cos(y),
            sp.sin(x) + sp.cos(z),
            sp.sin(y) + sp.cos(x),
        ])
        coords = (x, y, z)
        omega = curl3(u, coords)
        e = enstrophy_density(omega)
        pt = {x: sp.pi / 4, y: sp.pi / 4, z: sp.pi / 4}
        grad_e = [sp.simplify(sp.diff(e, q).subs(pt)) for q in coords]
        Dk = sp.simplify(canonical_microframe_bulk_dissipation(gradient(omega, coords), nu).subs(pt))
        flux_laplacian = sp.simplify(nu * laplacian_scalar(e, coords).subs(pt))
        dt_e = sp.simplify(sp.diff(e, t).subs(pt))
        self.assertEqual(grad_e, [0, 0, 0])
        self.assertEqual(sp.simplify(stretching_power(u, coords).subs(pt)), 0)
        self.assertEqual(sp.simplify(Dk - 3 * nu * amp**2), 0)
        self.assertEqual(sp.simplify(flux_laplacian + 3 * nu * amp**2), 0)
        self.assertEqual(sp.simplify(dt_e + 6 * nu * amp**2), 0)
        self.assertLess(float(sp.N((stretching_gate_margin(u, coords, nu) / (nu * amp**2)).subs(pt))), 0.0)

    def test_local_maximum_growth_gate_is_stretching_minus_kelvin_bulk_before_negative_laplacian(self) -> None:
        P, Dk, nu, lap_e = sp.symbols("P Dk nu lap_e", real=True)
        material_growth = P - Dk + nu * lap_e
        # At a spatial local maximum lap_e <= 0.  If P-Dk <= 0 then growth cannot be positive.
        self.assertEqual(sp.expand(material_growth.subs(P, Dk) - nu * lap_e), 0)
        self.assertEqual(sp.expand(material_growth.subs({P: Dk - 1, lap_e: 0})), -1)


if __name__ == "__main__":
    unittest.main()
