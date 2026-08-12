"""Exact event semantics of the hysteretic first-bad selector.

The intrinsic first-bad support projector M_fb and the moving localization maps
Q_s/H_s are different typed objects.  M_fb is piecewise constant under the current
hysteresis API: while an active germ is unresolved, changes in bad flags do not
change the selected index.  Entry and resolve/reselect events are finite jumps.

This module records those exact semantics without defining a Navier--Stokes
badness functional or resolve predicate.  Those programme-specific definitions
remain open.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Sequence

import sympy as sp

from .cycle_selector import hysteretic_first_bad_projection, pair_jump_decomposition

Matrix = sp.MatrixBase


@dataclass(frozen=True)
class SelectorEventStep:
    before_index: int | None
    after_index: int | None
    before: sp.Matrix
    after: sp.Matrix

    @property
    def jump(self) -> sp.Matrix:
        return sp.simplify(self.after - self.before)

    @property
    def changed(self) -> bool:
        return not self.jump.equals(sp.zeros(*self.jump.shape))


def selector_event_step(
    bad_flags: Sequence[bool],
    previous_index: int | None,
    resolved: bool,
) -> SelectorEventStep:
    """One literal hysteretic selector update.

    ``before`` is the rank-one projector on ``previous_index`` (or zero).  ``after``
    is exactly the current ``hysteretic_first_bad_projection`` result.
    """
    n = len(bad_flags)
    before = sp.zeros(n)
    if previous_index is not None:
        if not 0 <= previous_index < n:
            raise ValueError("previous selector index out of range")
        before[previous_index, previous_index] = 1
    after, after_index = hysteretic_first_bad_projection(
        bad_flags, previous_index, resolved
    )
    return SelectorEventStep(previous_index, after_index, before, after)


def frozen_branch_outputs(size: int, previous_index: int) -> set[tuple[tuple[sp.Expr, ...], ...]]:
    """All frozen-branch selector outputs over every Boolean badness pattern."""
    if size <= 0 or not 0 <= previous_index < size:
        raise ValueError("invalid frozen selector size/index")
    outputs: set[tuple[tuple[sp.Expr, ...], ...]] = set()
    for flags in product((False, True), repeat=size):
        M, _ = hysteretic_first_bad_projection(flags, previous_index, resolved=False)
        outputs.add(tuple(tuple(M[i, j] for j in range(size)) for i in range(size)))
    return outputs


def resolve_flag_independence_witness(
    bad_flags: Sequence[bool], previous_index: int
) -> tuple[SelectorEventStep, SelectorEventStep]:
    """Same bad flags, different resolve bit: the resolve predicate is independent input."""
    return (
        selector_event_step(bad_flags, previous_index, resolved=False),
        selector_event_step(bad_flags, previous_index, resolved=True),
    )


def selector_pair_jump_residual(step: SelectorEventStep) -> sp.Matrix:
    """Residual of the exact tensor-square finite jump decomposition."""
    dec = pair_jump_decomposition(step.before, step.after)
    return sp.simplify(dec.total - dec.reconstructed)


def piecewise_constant_selector_distributional_jump(
    jump: Matrix, event_weight: sp.Expr
) -> sp.Matrix:
    """Coefficient of the event measure dM = Delta M delta_event.

    ``event_weight`` is a symbolic placeholder for a Dirac/event measure weight;
    no smooth density is invented.
    """
    return sp.simplify(event_weight * jump)


def threshold_flags_from_scores(
    scores: Sequence[sp.Expr], thresholds: Sequence[sp.Expr]
) -> tuple[sp.Rel, ...]:
    """Generic symbolic threshold predicates score_i >= theta_i.

    This is a type constructor only.  It does not supply the programme's missing
    Navier--Stokes scores or thresholds.
    """
    if len(scores) != len(thresholds):
        raise ValueError("score/threshold lengths must match")
    return tuple(sp.Ge(score, threshold) for score, threshold in zip(scores, thresholds))


def moving_cut_selector_independence_witness(a: sp.Expr) -> tuple[sp.Matrix, sp.Matrix]:
    """A fixed first-bad projector can coexist with a continuously moving cut map.

    M_fb is kept fixed at diag(1,0); Q(a)=diag(a,1-a) varies with a.  This finite
    matrix witness is only a type-separation audit, not a literal physical cut.
    """
    return sp.diag(1, 0), sp.diag(a, 1 - a)


def selected_projector_derivative_on_frozen_branch(size: int) -> sp.Matrix:
    """Coordinate derivative Mdot on a literal frozen hysteresis interval."""
    if size < 0:
        raise ValueError("size must be nonnegative")
    return sp.zeros(size)
