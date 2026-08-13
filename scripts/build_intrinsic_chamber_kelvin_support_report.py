from __future__ import annotations

import json
import sys
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.intrinsic_chamber_kelvin_support import (
    intrinsic_chamber_packet_state,
    unit_transverse_intrinsic_support_no_go,
)
from pde_audit.intrinsic_enstrophy_localization import integer_scaled_one_mode_ns_residual

OUT = ROOT / "audit-results" / "intrinsic_chamber_kelvin_support_report.json"

x, y, z, t = sp.symbols("x y z t", real=True)
nu, A, n, alpha = sp.symbols("nu A n alpha", positive=True)
coords = (x, y, z)
state = intrinsic_chamber_packet_state(A, n, alpha, 1, 1, coords, t, nu)
w = unit_transverse_intrinsic_support_no_go(A, n, alpha, coords, t, nu)
lim = lambda q: sp.simplify(sp.limit(q, alpha, 0, dir="+"))
matlim = lambda M: M.applyfunc(lim)
_, transverse_face, _ = state.face_quadrupoles

data = {
    "classification": {
        "intrinsic_chamber_packet_lift": "Exact construction / audited physical lift",
        "kelvin_flux_blind_transverse_face": "Exact identity / physical no-go mechanism",
        "nested_chamber_support_no_go": "Audited exact-NS calibration / rigorous insufficiency",
        "tangential_support_face": "Exact support/level-set geometry identity",
        "first_bad_support_collapse": "Open-literal / Open",
        "restart_continuation_regularity": "Open",
    },
    "exact_ns": {
        "momentum_residual": str(integer_scaled_one_mode_ns_residual(A, n, coords, t, nu)),
        "compatibility_defect": str(state.compatibility_defect),
        "uniform_ancestry_flux": str(state.uniform_ancestry_flux),
        "level": str(state.level),
        "normal_span": str(state.y_span),
    },
    "packet": {
        "line_frame": str(state.line_frame),
        "area_frame": str(state.area_frame),
        "support_tensor": str(state.support_tensor),
        "tangential_support_tensor": str(state.tangential_support_tensor),
        "physical_residual": str(state.physical_residual),
        "target_gradient": str(state.target_gradient),
        "full_codeforming_noise": str(state.full_codeforming_noise),
        "orientation_qv": str(state.orientation_qv),
        "endpoint_nonaffinity": str(state.endpoint_nonaffinity),
        "nanson_line_rate": str(state.nanson_line_rate),
        "tangential_support_rate": str(state.tangential_support_rate),
        "quadrupole_sum": str(state.quadrupole_sum),
        "transverse_face_quadrupole": str(transverse_face),
    },
    "flux_blind_face": {
        "persistent_area": str(state.area_frame[1, 1]),
        "circulation_component": str(state.circulation[1]),
        "target_flux_component": str((state.area_frame.T * state.target_vorticity)[1]),
        "raw_error_component": str(state.raw_error[1]),
    },
    "filtration_limits": {
        "volume": str(w["volume_limit"]),
        "physical_residual_z": str(w["residual_limit"]),
        "endpoint_nonaffinity": str(lim(state.endpoint_nonaffinity[0])),
        "nanson_line_rate": str(matlim(state.nanson_line_rate)),
        "area_frame": str(matlim(state.area_frame)),
        "support_tensor": str(matlim(state.support_tensor)),
        "tangential_support_tensor": str(matlim(state.tangential_support_tensor)),
        "quadrupole_sum": str(matlim(state.quadrupole_sum)),
        "diameter_squared": str(w["diameter_limit"]),
        "condition_ratio": str(w["condition_limit"]),
        "persistent_transverse_area": str(lim(state.area_frame[1, 1])),
    },
    "frontier": {
        "resolved": "scalar intrinsic compatibility and Kelvin-readout collapse do not force transverse packet support locality; P B P is the exact missing geometry face",
        "open_literal": "actual first-bad identification and a theorem coupling intrinsic compatibility to tangential support/refinement collapse",
        "open": "uniform singular-time support/conditioning control, restart capacity, continuation and regularity",
    },
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
print(OUT)
