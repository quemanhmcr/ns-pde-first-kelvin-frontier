from __future__ import annotations

from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.first_bad_event_semantics import (  # noqa: E402
    frozen_branch_outputs,
    moving_cut_selector_independence_witness,
    piecewise_constant_selector_distributional_jump,
    resolve_flag_independence_witness,
    selected_projector_derivative_on_frozen_branch,
    selector_event_step,
    selector_pair_jump_residual,
    threshold_flags_from_scores,
)


class FirstBadEventSemanticsAudit(unittest.TestCase):
    def test_frozen_hysteresis_selector_is_independent_of_all_bad_flag_changes(self) -> None:
        for n in (1, 2, 3, 4):
            for idx in range(n):
                outputs = frozen_branch_outputs(n, idx)
                self.assertEqual(len(outputs), 1)

    def test_new_earlier_bad_germ_does_not_move_unresolved_selector(self) -> None:
        before = selector_event_step((False, True, True), None, resolved=False)
        self.assertEqual(before.after_index, 1)
        frozen = selector_event_step((True, True, True), before.after_index, resolved=False)
        self.assertEqual(frozen.after_index, 1)
        self.assertEqual(frozen.jump, sp.zeros(3))

    def test_resolve_bit_is_independent_oracle_input(self) -> None:
        frozen, resolved = resolve_flag_independence_witness((True, False, True), 2)
        self.assertEqual(frozen.after_index, 2)
        self.assertEqual(resolved.after_index, 0)
        self.assertNotEqual(frozen.after, resolved.after)

    def test_entry_from_no_active_germ_is_finite_jump(self) -> None:
        step = selector_event_step((False, True, False), None, resolved=False)
        self.assertEqual(step.before, sp.zeros(3))
        self.assertEqual(step.after, sp.diag(0, 1, 0))
        self.assertTrue(step.changed)
        self.assertEqual(selector_pair_jump_residual(step), sp.zeros(9))

    def test_resolve_reselection_is_exact_finite_pair_jump(self) -> None:
        step = selector_event_step((True, False, True), 2, resolved=True)
        self.assertEqual(step.after_index, 0)
        self.assertTrue(step.changed)
        self.assertEqual(selector_pair_jump_residual(step), sp.zeros(9))

    def test_distributional_selector_derivative_is_event_measure_not_smooth_payment(self) -> None:
        delta = sp.symbols("delta_event")
        step = selector_event_step((True, False), 1, resolved=True)
        event = piecewise_constant_selector_distributional_jump(step.jump, delta)
        self.assertEqual(event, sp.simplify(delta * step.jump))
        self.assertEqual(selected_projector_derivative_on_frozen_branch(2), sp.zeros(2))

    def test_generic_threshold_constructor_does_not_choose_physical_scores(self) -> None:
        b1, b2, th1, th2 = sp.symbols("b1 b2 th1 th2", real=True)
        predicates = threshold_flags_from_scores([b1, b2], [th1, th2])
        self.assertEqual(predicates, (sp.Ge(b1, th1), sp.Ge(b2, th2)))

    def test_moving_localization_cut_can_change_while_first_bad_projector_is_fixed(self) -> None:
        a = sp.symbols("a")
        M, Q = moving_cut_selector_independence_witness(a)
        self.assertEqual(sp.diff(M, a), sp.zeros(2))
        self.assertNotEqual(sp.diff(Q, a), sp.zeros(2))

    def test_first_bad_projector_can_jump_while_same_cut_map_is_unchanged(self) -> None:
        a = sp.symbols("a")
        _, Q = moving_cut_selector_independence_witness(a)
        step = selector_event_step((False, True), 0, resolved=True)
        self.assertTrue(step.changed)
        self.assertEqual(sp.diff(Q, a), sp.diag(1, -1))
        # Q is independent of the resolve bit and selector index in this type witness.
        self.assertEqual(Q, sp.diag(a, 1-a))


if __name__ == "__main__":
    unittest.main()
