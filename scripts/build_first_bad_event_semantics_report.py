from __future__ import annotations

import json
from pathlib import Path
import sys
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.first_bad_event_semantics import (
    frozen_branch_outputs,
    moving_cut_selector_independence_witness,
    resolve_flag_independence_witness,
    selected_projector_derivative_on_frozen_branch,
    selector_event_step,
    selector_pair_jump_residual,
)

entry = selector_event_step((False, True, False), None, False)
frozen = selector_event_step((True, True, True), 1, False)
resolve_false, resolve_true = resolve_flag_independence_witness((True, False, True), 2)
a=sp.symbols('a')
M,Q=moving_cut_selector_independence_witness(a)

report = {
    "classification": {
        "hysteretic_first_bad_event_structure": "Exact implementation semantics: M_fb is coordinate-piecewise-constant on unresolved intervals and changes only by finite entry/resolve events",
        "selector_vs_quantile_shell": "Exact type distinction: moving Q/H localization maps are not the same object as the rank-one hysteretic first-bad projector",
        "badness_functional": "Open-literal: bad_flags are Boolean oracle inputs; no Navier-Stokes score/threshold map generates them",
        "resolve_predicate": "Open-literal: resolved is an independent Boolean oracle input; no Navier-Stokes resolve condition generates it",
        "quantile_observable": "Open-literal: scalar observable defining the moving Q/H chamber remains unspecified",
        "continuation_restart": "Open; no regularity conclusion",
    },
    "frozen_branch": {
        "all_three_germ_badness_patterns_same_output_count": len(frozen_branch_outputs(3,1)),
        "Mdot_zero": bool(selected_projector_derivative_on_frozen_branch(3)==sp.zeros(3)),
        "new_earlier_bad_germ_changes_selector": frozen.changed,
    },
    "events": {
        "entry_index": entry.after_index,
        "entry_pair_jump_residual_zero": bool(selector_pair_jump_residual(entry)==sp.zeros(9)),
        "same_flags_unresolved_index": resolve_false.after_index,
        "same_flags_resolved_index": resolve_true.after_index,
        "resolve_bit_changes_output": bool(resolve_false.after != resolve_true.after),
        "resolve_pair_jump_residual_zero": bool(selector_pair_jump_residual(resolve_true)==sp.zeros(9)),
    },
    "type_separation": {
        "fixed_selector": str(M),
        "moving_cut": str(Q),
        "selector_derivative_in_cut_parameter_zero": bool(sp.diff(M,a)==sp.zeros(2)),
        "cut_derivative_nonzero": bool(sp.diff(Q,a)!=sp.zeros(2)),
    },
    "frontier": {
        "resolved": "event/reset structure of the hysteretic projector and its independence from continuously moving localization cuts",
        "still_open": "define NS-derived badness scores/thresholds, resolve criterion, and the separate quantile/shell observable/outer-time state law",
    },
}
out=Path('audit-results/first_bad_event_semantics_report.json')
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
print(json.dumps(report,indent=2,sort_keys=True))
