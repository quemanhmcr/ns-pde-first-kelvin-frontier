from __future__ import annotations

import json
from pathlib import Path
import sys
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.two_clock_kelvin_quantile import (
    affine_reverse_covariance_residual,
    affine_reverse_probability_current,
    centered_gaussian_current_velocity,
    centered_gaussian_quantile,
    flat_reverse_kelvin_current_velocity,
    identity_map_future_bridge_residual,
    diagonal_reverse_covariance_component,
    identity_map_same_clock_residual,
    mahalanobis_shell_material_rate,
    reverse_age_state_map_drift,
    simultaneous_identity_map_obstruction,
    weighted_level_quantile_speed,
    zero_rate_reverse_covariance_component,
)

out = Path("audit-results/two_clock_kelvin_quantile_report.json")
out.parent.mkdir(parents=True, exist_ok=True)

a, tau, nu, k = sp.symbols("a tau nu k", positive=True)
r = nu * k**2 * tau
m = sp.exp(-r) * sp.cos(k*a)
Q = sp.Rational(1,2)*(1+sp.exp(-4*r)*sp.cos(2*k*a))
C = sp.simplify(Q-m**2)
gamma = 2*nu*sp.diff(m,a)**2

bp, bm, u = sp.symbols("b_plus b_minus u")
future_res = identity_map_future_bridge_residual(sp.Matrix([bp]), sp.Matrix([u]))
same_res = identity_map_same_clock_residual(sp.Matrix([bm]), sp.Matrix([u]))

z, var0 = sp.symbols("z var0", positive=True)
aq = centered_gaussian_quantile(z,var0,nu,tau)
jq = centered_gaussian_current_velocity(aq,var0,nu,tau)

w1,w2,r1,r2=sp.symbols("w1 w2 r1 r2", positive=True)

srate=sp.symbols("srate", positive=True)
A3=sp.diag(srate,0,-srate)
Sigma3=sp.diag(
    diagonal_reverse_covariance_component(srate,tau,nu),
    zero_rate_reverse_covariance_component(tau,nu),
    diagonal_reverse_covariance_component(-srate,tau,nu),
)
a1,a2,s1,s2,x1,x2=sp.symbols("a1 a2 s1 s2 x1 x2", positive=True)
A2=sp.diag(a1,a2)
S2=sp.diag(s1,s2)
S2dot=-A2*S2-S2*A2.T+2*nu*sp.eye(2)
maha=mahalanobis_shell_material_rate(A2,S2,S2dot,sp.Matrix([x1,x2]),nu)

report = {
    "classification": {
        "physical_reverse_age_generator": "Exact: L_rev(t,sigma)=-K^-_{t-sigma}",
        "future_bank_clock_reversal": "Exact: future ancestry covariance becomes a causal physical past-payoff bank after reverse-age reparameterization",
        "identity_map_future_bridge": "Exact condition b_+=-u in the flat anchor sector; programme-specific state intertwining remains open-literal",
        "same_clock_bminus_match": "Distinct exact condition b_-=u; not the same construction as reversing a future bank",
        "quantile_level_speed": "Exact Reynolds/coarea law: fixed-mass level set moves with weighted boundary average of g_t+j.grad g",
        "literal_first_bad_quantile_observable": "Open-literal: the scalar germ observable defining the programme quantile chamber is not written line by line",
        "outer_physical_cut_speed": "Underdetermined by one-clock ancestry continuity alone; needs the two-clock/state lift or an independent physical outer-time law",
        "continuation_restart": "Open; no regularity conclusion",
    },
    "one_mode": {
        "mean_reverse_age_residual_zero": bool(sp.simplify(sp.diff(m,tau)-nu*sp.diff(m,a,2)) == 0),
        "covariance_reverse_age_residual_zero": bool(sp.trigsimp(sp.diff(C,tau)-nu*sp.diff(C,a,2)-gamma) == 0),
    },
    "state_map": {
        "identity_future_residual": str(future_res[0]),
        "identity_same_clock_residual": str(same_res[0]),
        "simultaneous_obstruction": str(simultaneous_identity_map_obstruction(sp.Matrix([bp]),sp.Matrix([bm]))[0]),
        "interpretation": "future bridge uses b_+ with reversed clock; same-clock reversed diffusion uses b_-",
    },
    "quantile": {
        "coarea_weighted_speed": str(weighted_level_quantile_speed([w1,w2],[r1,r2])),
        "one_dimensional_rule": "adot=j at g=x",
        "gaussian_quantile": str(aq),
        "gaussian_speed_equals_current": bool(sp.simplify(sp.diff(aq,tau)-jq)==0),
        "reverse_kelvin_current_velocity": str(flat_reverse_kelvin_current_velocity(sp.Symbol('u'),sp.Symbol('dlogrho'),nu)),
    },
    "affine_reverse_quantile_shell": {
        "covariance_ode_residual_zero": bool(sp.simplify(affine_reverse_covariance_residual(A3,Sigma3,sp.diff(Sigma3,tau),nu)) == sp.zeros(3)),
        "mahalanobis_material_rate_zero": bool(sp.simplify(maha)==0),
        "covariance_x": str(Sigma3[0,0]),
        "covariance_y": str(Sigma3[1,1]),
        "covariance_z": str(Sigma3[2,2]),
        "interpretation": "Gaussian quantile ellipsoid is transported pointwise by probability current; covariance is the reverse-flow controllability/support Gramian",
    },
    "frontier": {
        "resolved": "the physical reverse-age clock, generator sign, future-bank source sign, and same-clock-vs-clock-reversed drift distinction",
        "still_open": "intertwine the repository ancestry state with the physical reverse-age Kelvin state and define the literal first-bad quantile observable/outer-time law",
    },
}
out.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
print(json.dumps(report,indent=2,sort_keys=True))
