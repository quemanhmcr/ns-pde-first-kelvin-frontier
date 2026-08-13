from __future__ import annotations

import json
import sys
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.intrinsic_enstrophy_localization import (
    ancestry_superlevel_flux_faces,
    four_mode_global_crossing_calibration,
    navier_stokes_similarity_weights,
    one_mode_intrinsic_localization_calibration,
    one_mode_similarity_threshold_no_go,
    similarity_normalized_defect_residual,
    similarity_normalized_speed_residual,
)

OUT = ROOT / "audit-results" / "intrinsic_enstrophy_localization_report.json"
x, y, z, t = sp.symbols("x y z t", real=True)
nu = sp.symbols("nu", positive=True)
n = sp.symbols("n", positive=True, integer=True)
lam = sp.symbols("lambda", positive=True)
M = sp.symbols("M", positive=True)
R, Md, v = sp.symbols("R Md v", real=True)
theta = sp.Rational(1, 4)

one = one_mode_intrinsic_localization_calibration(
    sp.Integer(1), n, theta, (x, y, z), t, nu
)
threshold = one_mode_similarity_threshold_no_go(sp.Integer(1), n, theta, nu)
cross = four_mode_global_crossing_calibration((x, y, z), t, nu)
rho, un, cn, C, ge = sp.symbols("rho un cn C ge", nonzero=True)
flux = ancestry_superlevel_flux_faces(rho, un, cn, C, ge)

report = {
    "classification": {
        "ns_similarity_weights": "Exact identity / exact NS symmetry typing",
        "absolute_threshold_no_go": "Audited exact-NS calibration / rigorous no-go",
        "max_envelope_dini_law": "Rigorous consequence",
        "intrinsic_filtration": "Exact construction / intrinsic candidate localization",
        "superlevel_compatibility_defect": "Exact identity / exact physical interpretation",
        "ancestry_flux_split": "Exact continuity/Reynolds consequence",
        "one_mode_compatibility_cancellation": "Audited exact-NS cancellation",
        "four_mode_global_max_crossing": "Audited exact-NS global calibration",
        "first_bad_continuation_identification": "Open-literal / Open",
    },
    "similarity": {
        "weights": navier_stokes_similarity_weights(),
        "normalized_defect_residual": str(
            similarity_normalized_defect_residual(lam, R, theta, Md, M)
        ),
        "normalized_speed_residual": str(
            similarity_normalized_speed_residual(lam, v, M)
        ),
    },
    "one_mode": {
        "ns_residual": str(one["ns_residual"]),
        "enstrophy_balance_residual": str(one["enstrophy_balance_residual"]),
        "normalized_enstrophy": str(one["normalized_enstrophy"]),
        "normalized_time_derivative": str(one["normalized_time_derivative"]),
        "kelvin_bulk_level": str(one["kelvin_bulk_level"]),
        "curvature_level": str(one["curvature_level"]),
        "compatibility_defect": str(one["compatibility_defect"]),
        "max_enstrophy_t0": str(threshold["max_enstrophy"]),
        "kelvin_bulk_t0": str(threshold["kelvin_bulk"]),
    },
    "four_mode_global_crossing": {
        "ns_residual": str(cross["ns_residual"]),
        "common_max_enstrophy": str(cross["common_max_enstrophy"]),
        "upper_global_certificate": str(cross["upper_global_certificate"]),
        "lower_decomposition_residual": str(cross["lower_decomposition_residual"]),
        "lower_remainder_critical_plus": str(cross["lower_remainder_critical_plus"]),
        "lower_remainder_critical_minus": str(cross["lower_remainder_critical_minus"]),
        "lower_margin": str(cross["lower_margin"]),
        "hessian_yy_0": str(cross["hessian_yy_0"]),
        "hessian_yy_pi": str(cross["hessian_yy_pi"]),
        "left_dini": str(cross["left_dini"]),
        "right_dini": str(cross["right_dini"]),
        "dini_jump": str(cross["dini_jump"]),
        "stretching_0": str(cross["stretching_0"]),
        "kelvin_bulk_0": str(cross["kelvin_bulk_0"]),
        "curvature_0": str(cross["curvature_0"]),
        "stretching_pi": str(cross["stretching_pi"]),
        "kelvin_bulk_pi": str(cross["kelvin_bulk_pi"]),
        "curvature_pi": str(cross["curvature_pi"]),
        "balance_0": str(cross["balance_0"]),
        "balance_pi": str(cross["balance_pi"]),
    },
    "ancestry_flux": {key: str(value) for key, value in flux.items()},
    "frontier": {
        "resolved": "NS supplies a max-normalized enstrophy filtration and exact similarity-invariant boundary compatibility law; supplied ancestry current then sees only material/current mismatch plus intrinsic level-slip flux",
        "open_literal": "identification with the programme actual first-bad localization, badness/resolve sufficiency, packet selector accumulation, and two-clock ancestry semantics",
        "open": "uniform first-bad support/finite-shape control, restart capacity, continuation, regularity",
    },
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(OUT)
