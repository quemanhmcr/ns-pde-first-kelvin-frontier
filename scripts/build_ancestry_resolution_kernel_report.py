from __future__ import annotations

import json
from pathlib import Path
import sys
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.ancestry_resolution_kernel import (  # noqa: E402
    affine_shear_joint_state_covariance,
    affine_shear_ns_residual,
    affine_shear_relative_shape,
    generator_carre_du_champ_scalar,
    hidden_two_state_mean,
    hidden_two_state_resolution_variance,
    kernel_covariances,
    kernel_intertwining_residual,
    resolution_horizon_source_scalar,
    scalar_resolution_variance,
    total_variance_decomposition,
)

x, y, z, t, nu, a = sp.symbols("x y z t nu a", positive=True)
Rhalf = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]])
means = sp.Matrix([[a], [-a]])
zeroV = sp.zeros(2, 1)
avg, resolution, total = total_variance_decomposition(Rhalf, means, zeroV)
Lphys = sp.Matrix([[-1, 1], [1, -1]])
Lred = sp.zeros(1)
Fvec = sp.Matrix([[1, 2, -1], [-1, 0, 3]])
Cvec = kernel_covariances(Rhalf, Fvec)[0]

lam, tau = sp.symbols("lam tau", positive=True)
Lhidden = sp.Matrix([[-lam, lam], [lam, -lam]])
Lone = sp.zeros(1)
hidden_m = hidden_two_state_mean(a, lam, tau)
hidden_Cres = hidden_two_state_resolution_variance(a, lam, tau)
hidden_Gfull = generator_carre_du_champ_scalar(Lhidden, hidden_m)
hidden_source = resolution_horizon_source_scalar(Lone, Rhalf, Lhidden, hidden_m)

Cx = sp.diag(sp.Symbol('c1', positive=True), sp.Symbol('c2', positive=True), sp.Symbol('c3', positive=True))
Cjoint = affine_shear_joint_state_covariance(Cx)
rx, ry, rz, tau_shape = sp.symbols("rx ry rz tau_shape")

report = {
    "classification": {
        "resolution_covariance": "Exact law-of-total-variance term from unresolved physical current state; not viscous q.v.",
        "pair_resolution": "Exact 1/2 kappa x kappa squared-difference identity",
        "resolution_horizon_transfer": "Exact: H_red C_res = Gamma_red[Rm] - R Gamma_full[m] for a horizon-compatible lift",
        "reduced_total_future_bank": "Exact: C_red=R C_full+C_res and its horizon source is Gamma_red[Rm]",
        "kernel_intertwining": "Exact reduced/full generator compatibility Rdot+L_red R-R L_phys=0",
        "affine_shear_singularity": "Exact NS calibration: fixed relative shape plus diffusive anchor gives singular full (X,R) law",
        "state_definition_dichotomy": "Rigorous structural dichotomy: full-state ancestry needs singular/degenerate measure support in some exact NS flows; reduced ancestry needs a conditional physical-state kernel and its resolution covariance",
        "S_int_identification": "Open-literal; resolution covariance is not identified with any undefined S^int/Z_irr",
        "continuation_restart": "Open; no regularity conclusion",
    },
    "hidden_shape_variance": {
        "averaged_full_future_variance": [str(v) for v in avg],
        "resolution_variance": [str(v) for v in resolution],
        "reduced_total_variance": [str(v) for v in total],
        "exists_with_zero_full_future_variance": resolution != sp.zeros(1, 1),
    },
    "dynamic_resolution_transfer": {
        "hidden_mean": [str(v) for v in hidden_m],
        "resolution_variance": str(hidden_Cres),
        "full_gamma": [str(v) for v in hidden_Gfull],
        "resolution_horizon_source": [str(v) for v in hidden_source],
        "source_residual_zero": sp.simplify(sp.diff(hidden_Cres, tau) - hidden_source[0]) == 0,
        "interpretation": "full hidden-state carre-du-champ depletes unresolved shape covariance even though the reduced one-state generator has zero carre-du-champ",
    },
    "kernel_intertwining": {
        "stationary_hidden_shape_residual_zero": kernel_intertwining_residual(Lred, Rhalf, Lphys) == sp.zeros(1, 2),
        "interpretation": "a reduced Markov state can be generator-compatible while still hiding physical shape covariance",
    },
    "vector_pair_content": {
        "covariance": [[str(Cvec[i,j]) for j in range(3)] for i in range(3)],
        "cross_orientation_nonzero": any(Cvec[i,j] != 0 for i in range(3) for j in range(3) if i != j),
    },
    "affine_shear": {
        "ns_residual_zero": affine_shear_ns_residual(a, (x,y,z), t, nu) == sp.zeros(3,1),
        "relative_shape": [str(v) for v in affine_shear_relative_shape(a, sp.Matrix([rx,ry,rz]), tau_shape)],
        "joint_covariance_rank": Cjoint.rank(),
        "joint_covariance_determinant": str(sp.det(Cjoint)),
        "shape_covariance_zero": Cjoint[3:,3:] == sp.zeros(3),
    },
    "frontier": {
        "full_state_option": "must allow degenerate/singular shape support or an appropriate non-volume reference measure; a smooth positive density on full current-shape volume is not universal",
        "reduced_state_option": "must specify a conditional lift kernel kappa(y,dY_K); its full pair covariance includes resolution covariance Var_kappa(mean payoff)",
        "branching_consequence": "same-ancestor pair source depends on what 'ancestor state' contains; reduced ancestors have branch-time hidden-state covariance in addition to viscous future branching",
        "remaining": "define the ancestry state y and decide full-state versus reduced-kernel semantics before identifying the canonical pair source globally",
    },
}

out = ROOT / "audit-results" / "ancestry_resolution_kernel_report.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n")
print(out)
print("hidden resolution variance:", report["hidden_shape_variance"]["resolution_variance"])
print("kernel intertwining / dynamic resolution:", report["kernel_intertwining"]["stationary_hidden_shape_residual_zero"], report["dynamic_resolution_transfer"]["source_residual_zero"])
print("vector cross orientation:", report["vector_pair_content"]["cross_orientation_nonzero"])
print("affine shear NS/rank/det:", report["affine_shear"]["ns_residual_zero"], report["affine_shear"]["joint_covariance_rank"], report["affine_shear"]["joint_covariance_determinant"])
