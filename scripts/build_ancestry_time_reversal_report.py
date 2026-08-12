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
    reference_gauge_invariance_residuals,
    repository_current_velocity,
    state_map_diffusion_factorization,
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



# Reference-gauge witness.
gauge_g = x**2 - 2 * y
gauge_psi = x**3 + x * y + y**2
gauge_res = reference_gauge_invariance_residuals(
    gauge_psi, w, K, phi, f, gauge_g, coords, nu
)

# Noisy-distribution/shape witness.
Sx, Sr, Sz = sp.symbols("Sx Sr Sz")
shape_coords = (Sx, Sr, Sz)
B_shape = sp.Matrix([[1, 0], [0, 0], [0, 1]])
shape_good = sp.Matrix([Sr])
shape_bad = sp.Matrix([Sr + Sz])
JB_good, shape_qv_good = state_map_diffusion_factorization(shape_good, B_shape, shape_coords)
JB_bad, shape_qv_bad = state_map_diffusion_factorization(shape_bad, B_shape, shape_coords)

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
        "reference_gauge": "Exact: phi,f,w are representation-gauge data while q,j,L,b_+,b_- are invariant",
        "shape_noise_distribution": "Exact: zero-qv Kelvin shape must annihilate the ancestry noisy distribution; full-rank diffusion cannot carry nontrivial smooth shape on an open region",
        "actual_state_identification": "Open-literal; the repository does not define the full ancestry state manifold/coordinate y line by line, so the ancestry-to-Kelvin state map cannot yet be constructed",
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
    "reference_gauge": {
        "q_residual_zero": gauge_res["q"] == 0,
        "j_residual_zero": gauge_res["j"] == sp.zeros(2, 1),
        "operator_residual_zero": gauge_res["L"] == 0,
        "b_plus_residual_zero": gauge_res["b_plus"] == sp.zeros(2, 1),
        "b_minus_residual_zero": gauge_res["b_minus"] == sp.zeros(2, 1),
        "meaning": "phi'=e^g phi, f'=e^-g f, w'=w-nu K grad g is a reference gauge, not a physical state change",
    },
    "shape_noise_distribution": {
        "good_DPiB": smat(JB_good),
        "good_shape_qv": smat(shape_qv_good),
        "bad_DPiB": smat(JB_bad),
        "bad_shape_qv": smat(shape_qv_bad),
        "full_rank_no_go": "if K=BB^T is positive definite on an open region, DPi_shape B=0 forces DPi_shape=0 there",
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
        "state_domain_blocker": "the full ancestry state y is not line-by-line defined in the repository; f,phi,w cannot substitute for it because they are reference-gauge data",
        "remaining_state_map": "define/construct the ancestry state manifold with a degenerate deterministic shape sector, then solve the exact backward-Ito pushforward equations",
        "shape_interaction": "the physical backward Kelvin state now has literal anchor+relative-shape kinematics; mapping the ancestry K,phi,f,w onto that degenerate common-noise state is still open",
    },
}

OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(OUT)
print("probability current / midpoint residuals:", report["weighted_example"]["probability_current_residual_zero"], report["weighted_example"]["midpoint_residual_zero"])
print("physical b-=u matching residual:", report["physical_backward_matching"]["matching_residual_zero"])
print("naive w=u mismatch nonzero:", report["physical_backward_matching"]["naive_mismatch_nonzero"])
print("state-map good drift/diffusion, bad shape qv:", report["state_map_conditions"]["good_projection_drift_residual_zero"], report["state_map_conditions"]["good_projection_diffusion_residual_zero"], report["state_map_conditions"]["bad_hidden_noise_violates_zero_shape_qv"])
print("reference gauge q/j/L/b+/b-:", report["reference_gauge"]["q_residual_zero"], report["reference_gauge"]["j_residual_zero"], report["reference_gauge"]["operator_residual_zero"], report["reference_gauge"]["b_plus_residual_zero"], report["reference_gauge"]["b_minus_residual_zero"])
print("shape noisy distribution good/bad qv:", report["shape_noise_distribution"]["good_shape_qv"], report["shape_noise_distribution"]["bad_shape_qv"])
print("naive mismatch:", report["physical_backward_matching"]["naive_w_equals_u_mismatch"])
