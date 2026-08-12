from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.cycle_selector import two_cycle_library
from pde_audit.hodge_projector import (
    covariant_projector_derivative,
    pair_projector_derivative,
    projector_idempotency_residual,
    projector_motion_blocks,
    projector_tangent_residual,
    weighted_cycle_projector,
)


def zero(M: sp.MatrixBase) -> bool:
    return all(sp.simplify(x) == 0 for x in M)


def main() -> None:
    B, K = two_cycle_library()
    W = sp.diag(1, 2, 3, 5)
    H = weighted_cycle_projector(K, W)

    r = sp.symbols("r", real=True)
    P = sp.Matrix([[1, r], [r, r**2]]) / (1 + r**2)
    G = sp.simplify(sp.diff(P, r))
    blocks = projector_motion_blocks(P, G)
    A = sp.simplify(G * P - P * G)
    G_comoving = covariant_projector_derivative(P, -A, G)
    pair_G = pair_projector_derivative(P, G)
    PP = sp.kronecker_product(P, P)

    report = {
        "classification": {
            "weighted_cycle_projector": "Exact identity",
            "projector_tangent_off_diagonal": "Exact identity",
            "comoving_projector_transport": "Exact connection identity",
            "pair_projector_internal_source": "Exactly zero",
            "actual_CK_Hodge_identification": "Conjectural bridge; no literal extra operator is defined in the repository",
            "global_Sint_Zirr_equivalence": "Open literal audit",
            "continuation_restart": "Open; no regularity conclusion",
        },
        "weighted_cycle_projector": {
            "idempotent": zero(projector_idempotency_residual(H)),
            "physical_boundary_zero": zero(B * H),
            "fixes_cycle_library": zero(H * K - K),
            "W_selfadjoint": zero(H.T * W - W * H),
        },
        "projector_motion": {
            "tangent_identity": zero(projector_tangent_residual(P, G)),
            "active_internal_zero": zero(blocks.active_internal),
            "inactive_internal_zero": zero(blocks.inactive_internal),
            "motion_equals_exchange_sum": zero(G - blocks.transfer_sum),
            "motion_nonzero": not zero(G),
            "comoving_covariant_derivative_zero": zero(G_comoving),
        },
        "pair_motion": {
            "pair_derivative_factorization": zero(
                pair_G - (sp.kronecker_product(G, P) + sp.kronecker_product(P, G))
            ),
            "active_pair_internal_source_zero": zero(sp.simplify(PP * pair_G * PP)),
        },
        "frontier": {
            "first_bad_selector": "closed by cycle typing",
            "idempotent_closed_range_CK_if_intended": "kinematics classified as boundary-zero plus exchange/connection",
            "nonprojector_CK_or_S_int": "not defined; remains open literal datum",
        },
    }
    out = ROOT / "audit-results" / "hodge_cycle_projector_report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(out)
    print("H^2=H:", report["weighted_cycle_projector"]["idempotent"])
    print("B H=0:", report["weighted_cycle_projector"]["physical_boundary_zero"])
    print("P G P=0:", report["projector_motion"]["active_internal_zero"])
    print("Q G Q=0:", report["projector_motion"]["inactive_internal_zero"])
    print("co-moving G=0:", report["projector_motion"]["comoving_covariant_derivative_zero"])
    print("pair active-active internal source=0:", report["pair_motion"]["active_pair_internal_source_zero"])


if __name__ == "__main__":
    main()
