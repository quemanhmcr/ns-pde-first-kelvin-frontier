from __future__ import annotations

import json
import sys
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.critical_sheet_merger_kelvin_event import (
    asymmetric_box_packet_state,
    branch_extraction,
    collision_affine_event_data,
    collision_embedding,
    coalesced_same_replica_qv,
    critical_sheet_speed_product_limit,
    different_shape_packet_no_go_witness,
    merger_packet_cusp_coefficient,
    merger_packet_noise_zy,
    merger_packet_residual_z,
    merger_quartic_transverse_derivative,
    merger_shear_ns_residual,
    merger_shear_vorticity_scalar,
    merger_time,
    normalized_collision_quotient,
    quotient_qv_residual,
    diagonal_only_quotient_defect,
)

OUT = ROOT / "audit-results" / "critical_sheet_merger_kelvin_event_report.json"

x, y, z, t = sp.symbols("x y z t", real=True)
nu = sp.symbols("nu", positive=True)
T = merger_time(nu)
s = sp.pi/2
state = asymmetric_box_packet_state(sp.pi, s, sp.Integer(1), sp.Integer(1), T, nu)
residual, div, pressure = merger_shear_ns_residual((x, y, z), t, nu)
A = branch_extraction(3, 0)
S = collision_embedding(3)
target = state.target_vorticity
d, ntarget = collision_affine_event_data(A, target, state.target_gradient, 3)
N = state.full_codeforming_noise
G = coalesced_same_replica_qv(N, 3, nu)
w = [sp.Rational(1,3)]*3
C = normalized_collision_quotient(w)
block = sp.simplify(2*nu*N*N.T)
witness = different_shape_packet_no_go_witness()

report = {
    "classification": {
        "ns_merger": "Exact identity / Audited calibration",
        "fixed_shape_packet_coalescence": "Rigorous consequence",
        "scalar_to_full_packet_implication": "Rigorous no-go",
        "collision_event_map": "Exact identity on the instantiated branch-resolved library",
        "same_replica_cross_blocks": "Exact identity",
        "selector_interface": "Exact zero jump plus audited singular one-sided rate calibration",
        "ancestry_identification": "Open-literal",
        "first_bad_or_continuation": "Open-literal / Open",
    },
    "ns": {
        "momentum_residual": str(residual),
        "divergence": str(div),
        "pressure": str(pressure),
        "merger_time": str(T),
        "merged_vorticity": str(merger_shear_vorticity_scalar(sp.pi, T, nu)),
        "quartic_transverse_derivative": str(merger_quartic_transverse_derivative()),
        "d_abs_d_dot_limit": str(critical_sheet_speed_product_limit(nu)),
    },
    "canonical_packet_at_merger": {
        "y_span": str(s),
        "line_frame": str(state.line_frame),
        "area_frame": str(state.area_frame),
        "circulation": str(state.circulation),
        "target_vorticity": str(state.target_vorticity),
        "physical_residual": str(state.physical_residual),
        "codeforming_noise": str(state.full_codeforming_noise),
        "residual_z_closed_form": str(merger_packet_residual_z(s)),
        "noise_zy_closed_form": str(merger_packet_noise_zy(s, 1)),
        "cusp_coefficient": str(merger_packet_cusp_coefficient(s, nu)),
    },
    "event": {
        "A_central_extraction": str(A),
        "collision_embedding": str(S),
        "A_S_minus_I": str(sp.simplify(A*S-sp.eye(3))),
        "affine_reanchoring_d": str(d),
        "target_noise_coboundary": str(ntarget),
        "selector_jump_on_collision_subspace": str(sp.simplify((branch_extraction(3,0)-branch_extraction(3,1))*S)),
    },
    "same_replica": {
        "single_block_qv": str(block),
        "full_library_qv": str(G),
        "equal_weight_quotient": str(C),
        "full_qv_quotient_residual": str(quotient_qv_residual(N,w,nu)),
        "diagonal_only_defect": str(diagonal_only_quotient_defect(N,w,nu)),
    },
    "no_go": {key: str(value) for key, value in witness.items()},
    "frontier": {
        "forced_by_ns": "critical anchors/local scalar target coalesce; analytic PDE survives merger",
        "needs_packet_functor": "support/frame/current/residual/noise coalescence",
        "ancestry": "distinct branch histories are not identified by instantaneous collision",
        "first_bad": "badness/resolve selector mapping remains Open-literal",
        "regularity": "no restart/continuation/regularity theorem claimed",
    },
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(OUT)
