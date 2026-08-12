from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.clock_cut_compatibility import (  # noqa: E402
    backward_kelvin_shear_residual,
    forward_brownian_shear_residual,
    forward_future_terminal_mean,
    moving_halfline_boundary_speed_face,
    moving_halfline_mass_rate,
    moving_halfline_static_flux,
    normalized_variance_current_residual_1d,
    one_mode_future_variance,
    one_mode_gamma,
    one_mode_horizon_dynkin_residual,
    one_mode_ordinary_spacetime_defect,
    pair_moving_cut_mass_rate,
)

a, tau, t, s, Theta, nu, k = sp.symbols("a tau t s Theta nu k", positive=True)
V = one_mode_future_variance(a, tau, nu, k)
gamma = one_mode_gamma(a, tau, nu, k)
defect = sp.trigsimp(one_mode_ordinary_spacetime_defect(a, tau, nu, k))

x, ss, K, gam = sp.symbols("x ss K gam")
f = sp.Function("f")(x, ss)
phi = sp.Function("phi")(x)
w = sp.Function("w")(x, ss)
Vg = sp.Function("V")(x, ss)

q, v, adot = sp.symbols("q v adot")
p1, p2, v1, v2 = sp.symbols("p1 p2 v1 v2")

report = {
    "classification": {
        "ordinary_derham_covariance_form": "False; exact one-mode NS/Kelvin counterexample leaves the second-order diffusion term",
        "dynkin_horizon_covariance": "Exact: (partial_tau-nu partial_aa)V=gamma in the one-mode calibration",
        "distributed_covariance_current": "Exact under normalized ancestry generator compatibility: divergence-form spacetime balance",
        "forward_vs_backward_clock": "Exact one-mode separation; forward Brownian NS field is not the backward-Kelvin martingale",
        "two_clock_first_bad_identification": "Open-literal; physical selector time has not been identified with the ancestry/backward horizon clock",
        "moving_cut_time_face": "Exact Reynolds/operator identity; Qdot contributes boundary speed in addition to static transport flux",
        "literal_first_bad_quantile_speed": "Generic Reynolds/coarea speed law is exact; first-bad scalar germ observable and outer-time instantiation remain open-literal",
        "continuation_restart": "Open; no regularity conclusion",
    },
    "one_mode": {
        "dynkin_residual_zero": sp.trigsimp(one_mode_horizon_dynkin_residual(a, tau, nu, k)) == 0,
        "ordinary_defect_equals_minus_nu_Vaa": sp.trigsimp(defect + nu * sp.diff(V, a, 2)) == 0,
        "gamma_at_anchor_zero": sp.simplify(gamma.subs(a, 0)) == 0,
        "ordinary_defect_at_anchor": str(sp.factor(sp.simplify(defect.subs(a, 0)))),
        "forward_brownian_residual": str(sp.factor(forward_brownian_shear_residual(a, t, nu, k))),
        "backward_kelvin_residual_zero": backward_kelvin_shear_residual(a, t, nu, k) == 0,
        "forward_future_terminal_mean": str(forward_future_terminal_mean(a, s, Theta, nu, k)),
    },
    "distributed_balance": {
        "residual_zero": normalized_variance_current_residual_1d(f, phi, w, Vg, x, ss, nu, K, gam) == 0,
        "current": "J_V=(qV, q j V + nu q K grad V); div J_V=-q gamma",
        "interpretation": "use Dynkin/Fokker-Planck duality and the spacetime divergence theorem, not an ordinary exact one-form",
    },
    "moving_cut": {
        "mass_rate": str(moving_halfline_mass_rate(q, v, adot)),
        "static_flux": str(moving_halfline_static_flux(q, v)),
        "boundary_speed_face": str(moving_halfline_boundary_speed_face(q, adot)),
        "split_residual_zero": sp.simplify(
            moving_halfline_mass_rate(q, v, adot)
            - moving_halfline_static_flux(q, v)
            - moving_halfline_boundary_speed_face(q, adot)
        ) == 0,
        "pair_rate": str(pair_moving_cut_mass_rate([p1, p2], [v1, v2], adot)),
        "pair_boundary_speed_coefficient": str(sp.diff(pair_moving_cut_mass_rate([p1, p2], [v1, v2], adot), adot)),
    },
    "frontier": {
        "resolved": "parabolic covariance is packaged as a divergence/Dynkin current; moving cuts retain Qdot and two replica faces",
        "still_open": "construct the literal two-clock physical first-bad/Kelvin lift and the actual first-bad quantile/shell boundary-speed law",
    },
}

out = ROOT / "audit-results" / "clock_cut_compatibility_report.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(out)
print("Dynkin / ordinary defect:", report["one_mode"]["dynkin_residual_zero"], report["one_mode"]["ordinary_defect_at_anchor"])
print("forward/backward:", report["one_mode"]["forward_brownian_residual"], report["one_mode"]["backward_kelvin_residual_zero"])
print("distributed balance:", report["distributed_balance"]["residual_zero"])
print("moving cut split / pair speed:", report["moving_cut"]["split_residual_zero"], report["moving_cut"]["pair_boundary_speed_coefficient"])
