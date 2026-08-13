from __future__ import annotations

import json
import sys
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.critical_sheet_transport_nanson_event import (
    branch_nanson_shear_history,
    critical_branch_normal_speed,
    critical_vorticity_gap_side_minus_central,
    kelvin_anchor_y_qv_rate,
    literal_sheet_kelvin_ancestry_qv_defect,
    merger_history_area_comparison,
    merger_history_line_comparison,
    merger_moving_cut_flux_distance_product_limit,
    merger_nanson_history_gap,
    merger_residual_cusp_from_moving_cut,
    merger_residual_cusp_identification_residual,
    merger_support_vorticity_jump,
    merger_viscous_circulation_face,
    nanson_history_gap_rate,
    side_cut_total_variation_to_merger,
    transported_merger_packet_state,
)

OUT = ROOT / "audit-results" / "critical_sheet_transport_nanson_event_report.json"

t = sp.symbols("t", real=True)
nu = sp.symbols("nu", positive=True)
s = sp.pi / 2
ell = sp.Integer(1)
m = sp.Integer(1)
central = transported_merger_packet_state("central", s, ell, m, nu)
side = transported_merger_packet_state("side", s, ell, m, nu)
J = merger_history_line_comparison(nu)
C = merger_history_area_comparison(nu)

report = {
    "classification": {
        "critical_sheet_vs_material_transport": "Exact identity / Rigorous consequence",
        "literal_critical_path_vs_kelvin_anchor": "Rigorous no-go by quadratic-variation mismatch",
        "nanson_branch_history_memory": "Exact identity / Rigorous consequence",
        "residual_coalescence_vs_full_geometry": "Exact NS semantic no-go",
        "moving_cut_circulation_law": "Exact identity",
        "cusp_identification": "Exact identity / Rigorous physical identification",
        "specific_selector_variation": "Exact identity / Audited calibration",
        "programme_ancestry_lift": "Open-literal",
        "first_bad_restart_continuation": "Open-literal / Open",
    },
    "transport": {
        "central_normal_speed": str(critical_branch_normal_speed("central", t, nu)),
        "minus_normal_speed": str(critical_branch_normal_speed("minus", t, nu)),
        "plus_normal_speed": str(critical_branch_normal_speed("plus", t, nu)),
        "kelvin_anchor_y_qv_rate": str(kelvin_anchor_y_qv_rate(nu)),
        "literal_sheet_kelvin_qv_defect": str(literal_sheet_kelvin_ancestry_qv_defect(nu)),
    },
    "nanson_history": {
        "gamma_central_from_zero": str(branch_nanson_shear_history("central", t, nu)),
        "gamma_side_from_zero": str(branch_nanson_shear_history("side", t, nu)),
        "gap_rate": str(nanson_history_gap_rate(t, nu)),
        "q_side_minus_q_central": str(critical_vorticity_gap_side_minus_central(t, nu)),
        "merger_gap": str(merger_nanson_history_gap(nu)),
        "nu_times_merger_gap_numeric": str(sp.N(nu * merger_nanson_history_gap(nu), 15)),
        "line_history_comparison": str(J),
        "line_history_comparison_det": str(sp.simplify(sp.det(J))),
        "area_history_comparison": str(C),
    },
    "endpoint_packets": {
        "central_line_frame": str(central.line_frame),
        "side_line_frame": str(side.line_frame),
        "line_frame_difference": str(sp.simplify(central.line_frame - side.line_frame)),
        "area_frame_difference": str(sp.simplify(central.area_frame - side.area_frame)),
        "circulation_difference": str(sp.simplify(central.circulation - side.circulation)),
        "target_difference": str(sp.simplify(central.target_vorticity - side.target_vorticity)),
        "physical_residual_difference": str(sp.simplify(central.physical_residual - side.physical_residual)),
        "codeforming_residual_difference": str(sp.simplify(central.codeforming_residual - side.codeforming_residual)),
    },
    "moving_cut": {
        "canonical_y_span": str(s),
        "merger_vorticity_jump": str(merger_support_vorticity_jump(s)),
        "viscous_circulation_face": str(merger_viscous_circulation_face(s, ell, nu)),
        "distance_weighted_cut_flux_limit": str(merger_moving_cut_flux_distance_product_limit(s, ell, nu)),
        "area_normalized_cusp": str(merger_residual_cusp_from_moving_cut(s, nu)),
        "cusp_identification_residual": str(merger_residual_cusp_identification_residual(s, nu)),
        "side_cut_total_variation_from_t0_zero": str(side_cut_total_variation_to_merger(0, nu)),
    },
    "frontier": {
        "resolved_no_go": "critical-sheet path is not literal Kelvin ancestry; dynamically Nanson-transported branch frames retain history at merger",
        "correct_interface": "sheet attachment is a moving-cut/reanchored readout with an exact Reynolds circulation face",
        "still_open_literal": "programme first-bad badness/resolve and nontrivial ancestry/readout/future-bank lift",
        "still_open": "uniform first-bad collapse, restart capacity, continuation/global regularity",
        "no_claim": "no restart/continuation/regularity theorem",
    },
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(OUT)
