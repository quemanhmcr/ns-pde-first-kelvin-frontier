from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.active_pair import matrix_is_zero, pair_lift  # noqa: E402
from pde_audit.kelvin_admissibility import (  # noqa: E402
    canonical_boundary_gauge_witness,
    factor_through_cycle_library,
    full_pair_factorization_residual,
    nonlinear_cycle_tangent_boundary,
    pair_curve_boundary,
    restricted_pair_boundary,
    restricted_physical_boundary,
)


def z(M: sp.MatrixBase) -> bool:
    return matrix_is_zero(M)


def main() -> None:
    B = sp.Matrix([
        [-1, 1, -1, 1],
        [1, -1, 0, 0],
        [0, 0, 1, -1],
    ])
    K = sp.Matrix([
        [1, 0],
        [1, 0],
        [0, 1],
        [0, 1],
    ])
    L = sp.Matrix([[2, 1], [-1, 3]])
    P = sp.simplify(K * (K.T * K).inv() * K.T)
    Q = sp.eye(4) - P
    H = sp.simplify(K * L * (K.T * K).inv() * K.T + 5 * Q)
    Y = H * K
    fac = factor_through_cycle_library(K, Y)

    Btri = sp.Matrix([
        [-1, 0, 1],
        [1, -1, 0],
        [0, 1, -1],
    ])
    Ztri = sp.Matrix([1, 1, 1])
    J = sp.diag(1, 0, 0)
    broken = J * Ztri
    broken_bdy = Btri * broken
    gauge_witness = canonical_boundary_gauge_witness(Btri, broken)

    a, adot = sp.symbols("a adot")
    Phi = Ztri * (a + a**2)
    Phidot = sp.diff(Phi, a) * adot
    nonlinear_tangent = nonlinear_cycle_tangent_boundary(Btri, sp.diff(Phi, a))
    nonlinear_pair_bdy = pair_curve_boundary(Btri, Phi, Phidot)

    x, y, zz, t, nu = sp.symbols("x y z t nu", positive=True)
    amp = sp.exp(-nu * t)
    u = amp * sp.Matrix([
        sp.sin(zz) + sp.cos(y),
        sp.sin(x) + sp.cos(zz),
        sp.sin(y) + sp.cos(x),
    ])
    p = -sp.Rational(1, 2) * u.dot(u)
    dpdx = sp.simplify(sp.diff(p, x).subs({y: sp.pi / 2, zz: 0}))
    closed_pressure = sp.simplify(sp.trigsimp(sp.integrate(dpdx, (x, 0, 2 * sp.pi))))
    open_pressure = sp.simplify(sp.trigsimp(sp.integrate(dpdx, (x, 0, sp.pi))))

    report = {
        "classification": {
            "cycle_preserving_linear_ck": "Exact identity: zero intrinsic physical and pair boundary; idempotency not required",
            "cycle_factorization": "Exact identity when the output lies in the chosen closed-cycle library span",
            "cycle_breaking_ck": "Physical open-boundary/interface/exit by exact Stokes gauge test, not an internal Kelvin producer",
            "differentiable_nonlinear_cycle_map": "Exact tangent-cycle and pair Leibniz identities",
            "original_allowed_pair_content_defect": "Zero when full physical tensor-square content is retained; truncation is observer/analysis projection",
            "abc_pressure_gauge": "Exact 3D Navier-Stokes calibration",
            "S_int": "Still undefined line by line; global Pillar-II equivalence remains open literal",
            "continuation_restart": "Open; no regularity conclusion",
        },
        "nonidempotent_cycle_operator": {
            "H_idempotent": z(sp.simplify(H * H - H)),
            "B_H_K_zero": z(restricted_physical_boundary(B, H, K)),
            "pair_boundary_zero": z(restricted_pair_boundary(B, H, K)),
            "factor_coordinates": [[str(v) for v in fac.coordinates.row(i)] for i in range(fac.coordinates.rows)],
            "factor_residual_zero": z(fac.residual),
            "full_pair_factorization_zero": z(full_pair_factorization_residual(K, L)),
        },
        "cycle_breaking_gauge_witness": {
            "boundary": [str(v) for v in broken_bdy],
            "canonical_exact_gauge_work": str(gauge_witness),
            "nonzero": gauge_witness != 0,
        },
        "nonlinear_cycle_map": {
            "boundary_zero": z(Btri * Phi),
            "tangent_boundary_zero": z(nonlinear_tangent),
            "pair_curve_boundary_zero": z(nonlinear_pair_bdy),
        },
        "exact_abc_pressure": {
            "closed_x_cycle_pressure_work": str(closed_pressure),
            "open_half_x_path_pressure_work": str(open_pressure),
            "expected_open_work": str(2 * amp**2),
            "open_matches_endpoint_pressure_difference": sp.simplify(open_pressure - 2 * amp**2) == 0,
        },
        "original_pair_content": {
            "full_pair_equals_cycle_pair_times_coefficient_pair": z(pair_lift(Y) - pair_lift(K) * pair_lift(L)),
        },
        "frontier": {
            "first_bad_selector": "closed by cycle typing",
            "idempotent_projector_motion": "classified as exchange/connection",
            "arbitrary_cycle_preserving_linear_ck": "classified; no intrinsic boundary or pair content defect with full lift",
            "differentiable_cycle_preserving_nonlinear_ck": "classified locally; tangent motion remains cycle-valued",
            "cycle_breaking_operation": "must be exposed as physical boundary/interface/exit because exact pressure gauge sees it",
            "remaining_literal_datum": "a line-by-line S^int definition, or an operation whose physical type is not yet specified",
        },
    }

    out = ROOT / "audit-results" / "kelvin_ck_admissibility_report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(out)
    print("non-idempotent H^2=H:", report["nonidempotent_cycle_operator"]["H_idempotent"])
    print("B H K = 0:", report["nonidempotent_cycle_operator"]["B_H_K_zero"])
    print("pair boundary = 0:", report["nonidempotent_cycle_operator"]["pair_boundary_zero"])
    print("cycle-breaking gauge work:", report["cycle_breaking_gauge_witness"]["canonical_exact_gauge_work"])
    print("nonlinear tangent boundary = 0:", report["nonlinear_cycle_map"]["tangent_boundary_zero"])
    print("ABC closed pressure work:", report["exact_abc_pressure"]["closed_x_cycle_pressure_work"])
    print("ABC open pressure work:", report["exact_abc_pressure"]["open_half_x_path_pressure_work"])
    print("full pair content defect = 0:", report["original_pair_content"]["full_pair_equals_cycle_pair_times_coefficient_pair"])


if __name__ == "__main__":
    main()
