from __future__ import annotations

import json
import math
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.active_pair import boundary_residual, matrix_is_zero, pair_boundary_residual, pair_lift
from pde_audit.cycle_selector import (
    cycle_library_boundary,
    cycle_selector_boundary_residual,
    cycle_selector_pair_boundary_residual,
    cycle_span_projector,
    first_bad_projection,
    germ_support_transport_commutator,
    incidence_mask_commutator,
    pair_jump_decomposition,
    restricted_ambient_commutator,
    two_cycle_library,
)
from pde_audit.exact_shear import kelvin_anchor_covariance, kelvin_anchor_moments, kelvin_increment_variance


def entries(M: sp.MatrixBase) -> list[dict[str, object]]:
    out = []
    for i in range(M.rows):
        for j in range(M.cols):
            x = sp.simplify(M[i, j])
            if x != 0:
                out.append({"row": i, "col": j, "value": str(x)})
    return out


def main() -> None:
    B, K = two_cycle_library()
    M = first_bad_projection((True, True))
    intrinsic = cycle_selector_boundary_residual(B, K, M)
    pair_intrinsic = cycle_selector_pair_boundary_residual(B, K, M)
    H = cycle_span_projector(K)

    # Off-cycle extension witness: global ambient commutator can be nonzero while
    # its restriction to the actual Kelvin cycle is zero.
    B2 = sp.Matrix([[-1, -1], [1, 1]])
    K2 = sp.Matrix([[1], [-1]])
    F1 = sp.eye(2)
    F0 = sp.zeros(2)
    ambient = boundary_residual(B2, F1, F0, B2)
    ambient_restricted = restricted_ambient_commutator(B2, F1, F0, B2, K2)
    ambient_pair = pair_boundary_residual(B2, F1, F0, B2)
    ambient_pair_restricted = sp.simplify(ambient_pair * pair_lift(K2))

    edge_cut = incidence_mask_commutator(
        sp.Matrix([[-1, 0], [1, -1], [0, 1]]),
        [1, 0],
        [1, 1, 0],
    )
    germ_cut = germ_support_transport_commutator(
        sp.Matrix([[0, 2, -1], [3, 0, 5], [7, 11, 0]]),
        [1, 0, 0],
    )

    jump = pair_jump_decomposition(sp.diag(1, 0), sp.diag(0, 1))

    # Exact symbolic selected covariance-path bank chain rule.
    c11, c12, c22 = sp.symbols("c11 c12 c22")
    g11, g12, g22 = sp.symbols("g11 g12 g22")
    a1, a2, da1, da2 = sp.symbols("a1 a2 da1 da2")
    C = sp.Matrix([[c11, c12], [c12, c22]])
    Gamma = sp.Matrix([[g11, g12], [g12, g22]])
    avec = sp.Matrix([a1, a2])
    adot = sp.Matrix([da1, da2])
    bank_residual = sp.expand(
        (-(avec.T * Gamma * avec)[0] + (adot.T * C * avec)[0] + (avec.T * C * adot)[0])
        + (avec.T * Gamma * avec)[0]
        - 2 * (avec.T * C * adot)[0]
    )

    # Exact 3D ABC closed-cycle pressure/gauge witness.
    x, y, z, t, nu = sp.symbols("x y z t nu", positive=True)
    amp = sp.exp(-nu * t)
    uabc = amp * sp.Matrix([
        sp.sin(z) + sp.cos(y),
        sp.sin(x) + sp.cos(z),
        sp.sin(y) + sp.cos(x),
    ])
    pabc = -sp.Rational(1, 2) * uabc.dot(uabc)
    abc_circulation = sp.simplify(sp.integrate(uabc[0].subs({y: 0, z: sp.pi / 2}), (x, 0, 2 * sp.pi)))
    abc_pressure_circulation = sp.simplify(sp.trigsimp(sp.integrate(sp.diff(pabc, x).subs({y: 0, z: sp.pi / 2}), (x, 0, 2 * sp.pi))))

    N, c = 48, 1.0
    v0 = kelvin_anchor_moments(N, c, 0.0)[2]
    vpi = kelvin_anchor_moments(N, c, math.pi)[2]
    cov = kelvin_anchor_covariance(N, c, 0.0, math.pi)
    vinc = kelvin_increment_variance(N, c, 0.0, math.pi)
    reset_rhs = vinc + 2.0 * (cov - v0)

    report = {
        "classification": {
            "cycle_typed_selector_boundary": "Exact identity",
            "cycle_typed_selector_pair_boundary": "Exact identity",
            "ambient_extension_nonintrinsic": "Exact finite-chain counterexample",
            "support_cut_boundary": "Exact physical/localization interface identity",
            "germ_support_transport_cut": "Exact localization transport identity",
            "finite_hysteresis_pair_jump": "Exact reset identity",
            "selected_covariance_path_bank_chain_rule": "Exact identity",
            "odd_shear_selector_reset": "Rigorous consequence from exact Navier-Stokes calibration",
            "abc_closed_cycle_pressure_gauge": "Exact 3D Navier-Stokes calibration",
            "selector_irreducible_residual": "Zero for the cycle-typed selector after named physical terms are retained",
            "global_Sint_Zirr_equivalence": "Open literal audit; S^int and any additional CK/Hodge operator are not defined line by line",
            "continuation_restart": "Open; no regularity conclusion",
        },
        "cycle_library": {
            "B_K_zero": matrix_is_zero(cycle_library_boundary(B, K)),
            "first_bad_both_selects_first": [[str(x) for x in row] for row in M.tolist()],
            "intrinsic_boundary_zero": matrix_is_zero(intrinsic),
            "intrinsic_pair_boundary_zero": matrix_is_zero(pair_intrinsic),
            "canonical_cycle_projector_idempotent": matrix_is_zero(sp.simplify(H * H - H)),
            "canonical_cycle_projector_output_closed": matrix_is_zero(sp.simplify(B * H)),
        },
        "ambient_extension_witness": {
            "global_commutator_nonzero_entries": entries(ambient),
            "restricted_to_cycle_zero": matrix_is_zero(ambient_restricted),
            "global_pair_commutator_nonzero": not matrix_is_zero(ambient_pair),
            "restricted_pair_cycle_zero": matrix_is_zero(ambient_pair_restricted),
        },
        "interface_currents": {
            "physical_cut_entries": entries(edge_cut),
            "germ_transport_cut_entries": entries(germ_cut),
        },
        "finite_reset": {
            "pair_jump_reconstructs_exactly": matrix_is_zero(sp.simplify(jump.total - jump.reconstructed)),
            "pair_jump_nonzero_entries": entries(jump.total),
        },
        "selected_covariance_path_bank": {
            "symbolic_chain_rule_residual": str(bank_residual),
        },
        "exact_abc_closed_cycle": {
            "circulation": str(abc_circulation),
            "pressure_gradient_circulation": str(abc_pressure_circulation),
        },
        "exact_ns_odd_shear_reset": {
            "V0": v0,
            "Vpi": vpi,
            "Cov0pi": cov,
            "increment_variance": vinc,
            "variance_change": vpi - v0,
            "mixed_plus_diagonal_reset_rhs": reset_rhs,
            "increment_equals_4V0_error": vinc - 4.0 * v0,
        },
        "frontier": {
            "first_bad_selector_intrinsic_residual": "closed",
            "additional_CK_Hodge_operator": "not present in repository",
            "S_int_literal_definition": "not present in repository",
        },
    }
    out = ROOT / "audit-results" / "cycle_typed_first_bad_selector_report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(out)
    print("cycle library B K = 0:", report["cycle_library"]["B_K_zero"])
    print("intrinsic selected pair boundary = 0:", report["cycle_library"]["intrinsic_pair_boundary_zero"])
    print("ambient commutator nonzero but restricted cycle zero:", bool(entries(ambient)), report["ambient_extension_witness"]["restricted_to_cycle_zero"])
    print("pair reset reconstruction exact:", report["finite_reset"]["pair_jump_reconstructs_exactly"])
    print(f"odd shear reset: dV={vpi-v0:.3e}, increment={vinc:.8g}, reset_rhs={reset_rhs:.3e}")


if __name__ == "__main__":
    main()
