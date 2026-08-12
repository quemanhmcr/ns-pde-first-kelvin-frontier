from __future__ import annotations

import json
from pathlib import Path
import sys
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.ancestry_time_reversal import (  # noqa: E402
    backward_kelvin_matching_residual,
    backward_state_map_residuals,
    expanded_forward_drift,
    forward_drift_required_for_backward_kelvin,
    midpoint_current_residual,
    naive_w_equals_u_mismatch,
    probability_current_residual,
    repository_current_velocity,
    reversed_drift,
    weighted_diffusion_connection,
)

OUT = ROOT / "audit-results" / "ancestry_time_reversal_report.json"
OUT.parent.mkdir(exist_ok=True)

x, y, nu = sp.symbols("x y nu", positive=True)
coords = (x, y)
K = sp.Matrix([[1 + x**2, x * y], [x * y, 2 + y**2]])
phi = sp.exp(x + 2 * y)
f = sp.exp(3 * x - y)
w = sp.Matrix([x + y, x - 2 * y])
u_phys = sp.Matrix([y, -x])
cphi = weighted_diffusion_connection(K, phi, coords)
bplus = expanded_forward_drift(w, K, phi, coords, nu)
bminus = reversed_drift(w, K, phi, f, coords, nu)
j = repository_current_velocity(w, K, f, coords, nu)
w_req = forward_drift_required_for_backward_kelvin(u_phys, K, phi, f, coords, nu)
mismatch = naive_w_equals_u_mismatch(u_phys, K, phi, f, coords, nu)

# Exact backward state-map residual witness: ancestry coordinates (X,R,Z_hidden).
X, R, Z = sp.symbols("X R Z")
map_coords = (X, R, Z)
K_map = sp.diag(1, 0, 1)
b_map = sp.Matrix([X, R, Z])
Pi_good = sp.Matrix([X, R])
physical_K = sp.diag(1, 0)
physical_b = sp.Matrix([X, R])
good_drift_res, good_diff_res = backward_state_map_residuals(
    Pi_good, b_map, K_map, map_coords, nu, physical_b, physical_K
)
Pi_bad = sp.Matrix([X, R + Z])
bad_J = sp.Matrix([[sp.diff(Pi_bad[a], c) for c in map_coords] for a in range(2)])
bad_pushed_K = sp.simplify(bad_J * K_map * bad_J.T)


def svec(v: sp.MatrixBase) -> list[str]:
    return [str(sp.factor(sp.simplify(v[i]))) for i in range(v.rows)]


def smat(M: sp.MatrixBase) -> list[list[str]]:
    return [[str(sp.factor(sp.simplify(M[i, j]))) for j in range(M.cols)] for i in range(M.rows)]

report = {
    "classification": {
        "weighted_forward_drift": "Exact expansion of L=w.grad+nu phi^-1 div(phi K grad)",
        "fokker_planck_current": "Exact J=q j with q=f phi and j=w-nu K grad log f",
        "forward_backward_midpoint": "Exact j=(b_++b_-)/2 for symmetric K",
        "time_reversed_drift": "Exact weighted diffusion time-reversal formula",
        "physical_backward_kelvin_matching": "Conditional algebra: if ancestry b_- is the physical backward Kelvin drift u, w is fixed explicitly",
        "actual_state_identification": "Open-literal; ancestry state/density/reference tensor have not been identified line by line with the physical Kelvin current-shape state",
        "continuation_restart": "Open; no regularity conclusion",
    },
    "weighted_example": {
        "c_phi": svec(cphi),
        "b_plus": svec(bplus),
        "b_minus": svec(bminus),
        "j": svec(j),
        "probability_current_residual_zero": probability_current_residual(w, K, phi, f, coords, nu) == sp.zeros(2, 1),
        "midpoint_residual_zero": midpoint_current_residual(w, K, phi, f, coords, nu) == sp.zeros(2, 1),
    },
    "state_map_conditions": {
        "backward_drift_equation": "B_K = DPi b_- - nu K:Hess(Pi)",
        "diffusion_equation": "K_K = DPi K DPi^T",
        "physical_kelvin_shape_diffusion": "anchor block nonzero, relative-shape block zero",
        "good_projection_drift_residual_zero": good_drift_res == sp.zeros(2, 1),
        "good_projection_diffusion_residual_zero": good_diff_res == sp.zeros(2),
        "bad_hidden_noise_into_shape_pushed_K": smat(bad_pushed_K),
        "bad_hidden_noise_violates_zero_shape_qv": bad_pushed_K != physical_K,
    },
    "physical_backward_matching": {
        "u_backward": svec(u_phys),
        "w_required": svec(w_req),
        "matching_residual_zero": backward_kelvin_matching_residual(u_phys, K, phi, f, coords, nu) == sp.zeros(2, 1),
        "naive_w_equals_u_mismatch": svec(mismatch),
        "naive_mismatch_nonzero": mismatch != sp.zeros(2, 1),
        "interpretation": "the mismatch is explicit time-reversal/osmotic plus reference-geometry drift, not an untyped internal source",
    },
    "flat_uniform_limit": {
        "formula": "K=I, phi=1: b_+=w, b_-=w-2nu grad log f, j=w-nu grad log f",
        "physical_matching": "if b_-=u then w=u+2nu grad log f",
        "constant_density": "if f is constant then b_+=b_-=j=w and w=u is consistent",
    },
    "frontier": {
        "resolved_time_orientation": "the normalized ancestry law already determines its forward and backward Ito drifts and their midpoint current exactly",
        "remaining_state_map": "prove that the ancestry backward drift/state is the physical backward Kelvin anchor/current-shape state, or exhibit the exact residual",
        "shape_interaction": "the physical backward Kelvin state now has literal anchor+relative-shape kinematics; mapping the ancestry K,phi,f,w onto that degenerate common-noise state is still open",
    },
}

OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(OUT)
print("probability current / midpoint residuals:", report["weighted_example"]["probability_current_residual_zero"], report["weighted_example"]["midpoint_residual_zero"])
print("physical b-=u matching residual:", report["physical_backward_matching"]["matching_residual_zero"])
print("naive w=u mismatch nonzero:", report["physical_backward_matching"]["naive_mismatch_nonzero"])
print("state-map good drift/diffusion, bad shape qv:", report["state_map_conditions"]["good_projection_drift_residual_zero"], report["state_map_conditions"]["good_projection_diffusion_residual_zero"], report["state_map_conditions"]["bad_hidden_noise_violates_zero_shape_qv"])
print("naive mismatch:", report["physical_backward_matching"]["naive_w_equals_u_mismatch"])
