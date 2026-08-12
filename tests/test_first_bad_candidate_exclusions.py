from __future__ import annotations

from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.first_bad_candidate_exclusions import (  # noqa: E402
    abc_enstrophy_gradient_at,
    abc_origin_quantities,
    abc_pressure,
    abc_stretching_at,
    abc_velocity,
    amplitude_limits,
    curl3,
    navier_stokes_residual,
)


class FirstBadCandidateExclusionsAudit(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y, self.z, self.t, self.nu, self.A = sp.symbols(
            "x y z t nu A", positive=True
        )
        self.coords = (self.x, self.y, self.z)

    def test_amplitude_scaled_abc_is_exact_periodic_ns_for_arbitrary_amplitude(self) -> None:
        u = abc_velocity(self.A, self.nu, self.t, self.coords)
        p = abc_pressure(u)
        div = sum(sp.diff(u[i], self.coords[i]) for i in range(3))
        residual = navier_stokes_residual(u, p, self.coords, self.t, self.nu)
        self.assertEqual(sp.simplify(sp.trigsimp(div)), 0)
        self.assertEqual(sp.simplify(sp.trigsimp(residual)), sp.zeros(3, 1))

    def test_abc_is_beltrami_for_every_amplitude(self) -> None:
        u = abc_velocity(self.A, self.nu, self.t, self.coords)
        omega = curl3(u, self.coords)
        self.assertEqual(sp.simplify(sp.trigsimp(omega-u)), sp.zeros(3,1))

    def test_origin_instantaneous_quantities_have_exact_amplitude_scaling(self) -> None:
        q = abc_origin_quantities(self.A, self.nu, self.t)
        amp = self.A * sp.exp(-self.nu*self.t)
        self.assertEqual(sp.simplify(q.omega_sq - 3*amp**2), 0)
        self.assertEqual(sp.simplify(q.enstrophy - sp.Rational(3,2)*amp**2), 0)
        self.assertEqual(sp.simplify(q.stretching - 3*amp**3), 0)
        self.assertEqual(sp.simplify(q.kelvin_bulk - 3*self.nu*amp**2), 0)
        self.assertEqual(sp.simplify(q.stretch_bulk_ratio - amp/self.nu), 0)
        self.assertEqual(sp.simplify(q.growth_gate_margin - 3*amp**2*(amp-self.nu)), 0)

    def test_all_raw_origin_candidates_are_unbounded_with_amplitude(self) -> None:
        q = abc_origin_quantities(self.A, self.nu, sp.Integer(0))
        limits = amplitude_limits(self.A, q)
        self.assertTrue(all(value == sp.oo for value in limits.values()))

    def test_any_finite_ratio_threshold_can_be_crossed_by_smooth_abc_data(self) -> None:
        T = sp.symbols("T", positive=True)
        q = abc_origin_quantities(self.A, self.nu, sp.Integer(0))
        # Choosing A=nu(T+1) gives ratio=T+1>T exactly.
        ratio = sp.simplify(q.stretch_bulk_ratio.subs(self.A, self.nu*(T+1)))
        self.assertEqual(ratio, T+1)
        self.assertEqual(sp.simplify(ratio-T), 1)

    def test_any_finite_vorticity_squared_threshold_can_be_crossed_by_smooth_abc_data(self) -> None:
        T = sp.symbols("T", positive=True)
        q = abc_origin_quantities(self.A, self.nu, sp.Integer(0))
        # A=sqrt((T+1)/3) makes |omega|^2=T+1.
        val = sp.simplify(q.omega_sq.subs(self.A, sp.sqrt((T+1)/3)))
        self.assertEqual(val, T+1)

    def test_origin_is_not_an_enstrophy_critical_point_so_abc_does_not_refute_local_max_gate(self) -> None:
        point = (0, 0, 0)
        grad = abc_enstrophy_gradient_at(self.A,self.nu,self.t,point)
        self.assertNotEqual(grad, sp.zeros(3,1))

    def test_symmetric_abc_enstrophy_critical_point_has_zero_stretching(self) -> None:
        point = (sp.pi/4, sp.pi/4, sp.pi/4)
        grad = abc_enstrophy_gradient_at(self.A,self.nu,self.t,point)
        stretch = abc_stretching_at(self.A,self.nu,self.t,point)
        self.assertEqual(sp.simplify(sp.trigsimp(grad)), sp.zeros(3,1))
        self.assertEqual(sp.simplify(sp.trigsimp(stretch)), 0)


if __name__ == "__main__":
    unittest.main()
