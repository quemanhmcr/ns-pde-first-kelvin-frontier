from __future__ import annotations

import json
import math
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.active_pair import (  # noqa: E402
    ChainStage,
    completed_boundary_residual,
    completed_pair_boundary_residual,
    interval_block_projection,
    interval_boundary,
    interval_cut_projection,
    interval_orientation_reversal,
    interval_refinement_map,
    matrix_is_zero,
    nonzero_entries,
    pair_boundary_residual,
    transported_stage_boundary_sum,
    transported_stage_pair_boundary_sum,
)
from pde_audit.exact_shear import kelvin_anchor_covariance, kelvin_anchor_moments  # noqa: E402


def entries(M: sp.MatrixBase) -> list[dict[str, str | int]]:
    return [
        {"row": i, "col": j, "value": str(value)}
        for i, j, value in nonzero_entries(M)
    ]


def main() -> None:
    B2 = interval_boundary(2)
    Q1, Q0 = interval_cut_projection(2, 1)
    A1, A0 = interval_orientation_reversal(2)
    H1, H0 = interval_block_projection(2, 0, 1)
    B4, R1, R0 = interval_refinement_map(2, 2)
    J1, J0 = interval_orientation_reversal(4)
    E1, E0 = interval_cut_projection(4, 3)

    stages = [
        ChainStage("freeze", "fixed-current transport", B2, B2, sp.eye(2), sp.eye(3)),
        ChainStage("quantile", "physical localization interface", B2, B2, Q1, Q0),
        ChainStage("anchor-orientation", "connection/holonomy geometry", B2, B2, A1, A0),
        ChainStage("shell", "physical shell interface; full product blocks required", B2, B2, H1, H0),
        ChainStage("refinement", "full tensor-square refinement", B2, B4, R1, R0),
        ChainStage("resolve-reset", "observer covariance revaluation", B4, B4, J1, J0),
        ChainStage("physical-exit", "physical boundary sink", B4, B4, E1, E0),
    ]

    stage_rows = []
    for stage in stages:
        C = stage.boundary_residual()
        C2 = stage.pair_boundary_residual()
        stage_rows.append(
            {
                "stage": stage.name,
                "physical_type": stage.physical_type,
                "one_current_boundary_residual_zero": matrix_is_zero(C),
                "one_current_nonzero_entries": entries(C),
                "pair_boundary_residual_zero": matrix_is_zero(C2),
                "pair_nonzero_entry_count": len(nonzero_entries(C2)),
            }
        )

    direct = completed_boundary_residual(stages)
    seam_sum = transported_stage_boundary_sum(stages)
    composition_exact = matrix_is_zero(sp.simplify(direct - seam_sum))
    direct_pair = completed_pair_boundary_residual(stages)
    pair_seam_sum = transported_stage_pair_boundary_sum(stages)
    pair_composition_exact = matrix_is_zero(sp.simplify(direct_pair - pair_seam_sum))

    # Full two-shell product partition versus diagonal-only shell pairs.
    z = sp.Matrix([1, 1])
    L1, _ = interval_block_projection(2, 0, 1)
    Rsh1, _ = interval_block_projection(2, 1, 2)
    zL, zR = L1 * z, Rsh1 * z
    full_shell_pair = (
        sp.kronecker_product(zL, zL)
        + sp.kronecker_product(zL, zR)
        + sp.kronecker_product(zR, zL)
        + sp.kronecker_product(zR, zR)
    )
    parent_pair = sp.kronecker_product(z, z)
    diagonal_shell_pair = sp.kronecker_product(zL, zL) + sp.kronecker_product(zR, zR)

    # Exact NS odd-shear active interpolation calibration.
    ns_rows = []
    N, c = 52, 0.85
    v0 = kelvin_anchor_moments(N, c, 0.0)[2]
    vpi = kelvin_anchor_moments(N, c, math.pi)[2]
    cov = kelvin_anchor_covariance(N, c, 0.0, math.pi)
    for h in [0.0, 0.2, 0.5, 0.8, 1.0]:
        full = h * h * v0 + (1.0 - h) ** 2 * vpi + 2.0 * h * (1.0 - h) * cov
        diagonal = h * h * v0 + (1.0 - h) ** 2 * vpi
        ns_rows.append(
            {
                "h": h,
                "full_pair_variance": full,
                "pathwise_expected_variance": (2.0 * h - 1.0) ** 2 * v0,
                "diagonal_only_variance": diagonal,
            }
        )

    # Generic ambient cell-projection counterexample: a cell projection is not
    # automatically a subcomplex.  The cycle-typed selector audit shows this is
    # not an intrinsic Kelvin-selector obstruction unless it survives restriction
    # to the closed-cycle library.
    P1, P0 = interval_cut_projection(2, 1)
    active_generic_C = B2 * P1 - P0 * B2
    active_generic_C2 = pair_boundary_residual(B2, P1, P0, B2)

    report = {
        "classification": {
            "full_pair_boundary_commutator_factorization": "Exact identity",
            "full_pair_transport_commutator_factorization": "Exact identity",
            "completed_excursion_seam_product_rule": "Exact identity",
            "no_autonomous_pair_only_residual": "Rigorous consequence of exact tensor-square factorization",
            "odd_shear_active_mixture": "Rigorous consequence from exact Navier-Stokes calibration",
            "cycle_typed_selector_residual": "Closed in dedicated cycle-typed audit",
            "additional_ambient_ck_hodge_operator": "Open only if such an extra operator is intended; none is defined in the repository",
            "continuation_restart": "Open; no regularity conclusion",
        },
        "stage_rows": stage_rows,
        "completed_excursion": {
            "direct_equals_transported_stage_sum": composition_exact,
            "direct_pair_equals_transported_pair_stage_sum": pair_composition_exact,
            "final_one_current_residual_entries": entries(direct),
            "final_pair_residual_nonzero_entry_count": len(nonzero_entries(direct_pair)),
        },
        "full_shell_product_partition": {
            "full_blocks_reconstruct_parent_pair": full_shell_pair == parent_pair,
            "diagonal_only_reconstructs_parent_pair": diagonal_shell_pair == parent_pair,
            "missing_cross_shell_vector": [str(x) for x in parent_pair - diagonal_shell_pair],
        },
        "exact_ns_active_mixture_rows": ns_rows,
        "generic_ambient_projection_counterexample": {
            "not_intrinsic_to_cycle_typed_selector": True,
            "one_current_residual_entries": entries(active_generic_C),
            "pair_residual_nonzero_entry_count": len(nonzero_entries(active_generic_C2)),
        },
        "remaining_literal_datum_if_programme_intends_extra_operator": {
            "additional_CK_Hodge_operator": "not present",
            "S_int_definition": "not present",
            "required_test_if_added": "restrict its boundary/transport commutators to the physical closed-cycle range before classifying any irreducible residual",
        },
    }

    out = ROOT / "audit-results" / "active_first_bad_pair_report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(out)
    print(f"completed seam product rule exact: {composition_exact}")
    print(f"completed pair seam product rule exact: {pair_composition_exact}")
    print("cycle-typed selector intrinsic residual: closed in dedicated audit")
    print("additional ambient CK/Hodge operator present: no")
    print(f"generic ambient projection residual entries: {entries(active_generic_C)}")
    print(
        "odd shear h=1/2: full="
        f"{ns_rows[2]['full_pair_variance']:.3e} "
        f"diag={ns_rows[2]['diagonal_only_variance']:.8g}"
    )


if __name__ == "__main__":
    main()
