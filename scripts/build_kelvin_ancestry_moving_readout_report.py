from __future__ import annotations

import json
import sys
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.kelvin_ancestry_moving_readout import (
    critical_chamber_d_dot,
    critical_chamber_mass_from_d,
    critical_chamber_mass_rate_from_d,
    critical_chamber_mass_total_variation_from_d0,
    merger_mean_rate_scaled_limit,
    merger_readout_endpoint_mean,
    merger_variance_boundary_scaled_limit,
    merger_variance_bulk_scaled_limit,
    merger_variance_rate_scaled_limit,
    merger_variance_scaled_limit,
    reduced_chamber_mean_rate_residual,
    reduced_chamber_variance_balance_residual,
    uniform_anchor_fp_residual_1d,
)

OUT = ROOT / "audit-results" / "kelvin_ancestry_moving_readout_report.json"
nu = sp.symbols("nu", positive=True)
d = sp.symbols("d", positive=True)
y = sp.symbols("y", real=True)

report = {
    "classification": {
        "three_layer_covariance": "Exact identity",
        "moving_boundary_revaluation": "Exact Reynolds/conditional-covariance identity",
        "uniform_kelvin_anchor": "Exact identity / Audited exact-NS calibration",
        "critical_chamber_mass": "Exact identity / Audited calibration",
        "critical_mean_regularization": "Exact identity / Rigorous consequence in exact NS calibration",
        "critical_variance_balance": "Exact identity / Audited exact-NS calibration",
        "first_bad_observable": "Open-literal",
        "restart_continuation_regularity": "Open",
    },
    "physical_semantics": {
        "ancestry": "Kelvin/material stochastic population",
        "eulerian_selector": "moving restriction/readout of ancestry population",
        "covariance_layers": [
            "intrinsic full-Kelvin covariance",
            "hidden-state resolution covariance",
            "Eulerian localization covariance",
        ],
        "selector_extra_brownian_source": False,
    },
    "critical_chamber": {
        "uniform_anchor_fp_residual": str(uniform_anchor_fp_residual_1d(0, y, nu)),
        "mass": str(critical_chamber_mass_from_d(d)),
        "mass_rate": str(critical_chamber_mass_rate_from_d(d, nu)),
        "d_dot": str(critical_chamber_d_dot(d, nu)),
        "mass_total_variation_from_d0": str(critical_chamber_mass_total_variation_from_d0(d)),
    },
    "mean": {
        "moving_cut_identity_residual": str(reduced_chamber_mean_rate_residual(d, nu)),
        "rate_over_d2_limit": str(merger_mean_rate_scaled_limit(nu)),
        "endpoint_mean": str(merger_readout_endpoint_mean()),
    },
    "variance": {
        "balance_residual": str(reduced_chamber_variance_balance_residual(d, nu)),
        "variance_over_d8_limit": str(merger_variance_scaled_limit()),
        "bulk_over_d6_limit": str(merger_variance_bulk_scaled_limit(nu)),
        "boundary_over_d6_limit": str(merger_variance_boundary_scaled_limit(nu)),
        "rate_over_d6_limit": str(merger_variance_rate_scaled_limit(nu)),
    },
    "frontier": {
        "resolved": "ancestry conditional lift plus supplied moving Eulerian localization has an exact second-order transport law with no independent selector covariance producer",
        "open_literal": "programme first-bad observable/localization, global ancestry semantics/lift, two-clock identification, general endogenous interface accumulation",
        "open": "uniform first-bad finite-shape/support control, restart, continuation, regularity",
    },
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(OUT)
