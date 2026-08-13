"""Necessary physical admissibility checks for any future first-bad rule.

This module does *not* define a first-bad functional.  It only records exact
obstructions that any physically meaningful rule must survive:

* passive orientation-coordinate changes cannot alter the physical decision;
* physical reconstructed residual collapse does not imply support locality;
* genuine selector switches require persistent-library information;
* diagonal spectral channels do not retain event coherence;
* adaptive event expectations require event-map/state joint information.

Passing these checks is necessary typing, not a continuation theorem and not a
sufficient regularity criterion.
"""
from __future__ import annotations

import sympy as sp

from .codeforming_whitened_kelvin_remainder import whitened_face_reconstruction
from .directional_refinement_kelvin_residual import quadratic_long_support_calibration
from .first_bad_selected_residual_readout import (
    selector_switch_second_moment_counterexample,
    selector_switch_state_counterexample,
)
from .frame_aware_kelvin_residual_refinement import (
    physical_synthesis_gauge_residual,
    reparameterized_raw_refinement_block,
)
from .kelvin_event_normal_form import channel_only_composition_counterexample
from .random_selected_event_correlation import adaptive_event_alignment_calibrations

Matrix = sp.MatrixBase


def raw_face_residual_energy(face_residual: Matrix) -> sp.Expr:
    """Observer-coordinate Euclidean square |epsilon|^2."""
    if face_residual.cols != 1:
        raise ValueError("face residual must be a column")
    return sp.simplify(face_residual.dot(face_residual))


def physical_reconstructed_residual_energy(
    face_residual: Matrix,
    area_frame: Matrix,
) -> sp.Expr:
    """Literal physical square |H^{-T} epsilon|^2."""
    r=whitened_face_reconstruction(face_residual,area_frame)
    return sp.simplify(r.dot(r))


def passive_packet_reparameterization(
    face_residual: Matrix,
    area_frame: Matrix,
    orientation_map: Matrix,
) -> tuple[Matrix,Matrix]:
    """Passive packet basis: H->H S, epsilon->S^T epsilon."""
    if area_frame.shape != orientation_map.shape:
        raise ValueError("area frame and orientation map dimensions must match")
    if face_residual.shape != (area_frame.rows,1):
        raise ValueError("face residual/frame dimensions mismatch")
    return (
        sp.simplify(orientation_map.T*face_residual),
        sp.simplify(area_frame*orientation_map),
    )


def physical_score_passive_gauge_residual(
    face_residual: Matrix,
    area_frame: Matrix,
    orientation_map: Matrix,
) -> sp.Expr:
    before=physical_reconstructed_residual_energy(face_residual,area_frame)
    eps_new,H_new=passive_packet_reparameterization(face_residual,area_frame,orientation_map)
    after=physical_reconstructed_residual_energy(eps_new,H_new)
    return sp.simplify(after-before)


def raw_score_passive_gauge_change(
    face_residual: Matrix,
    area_frame: Matrix,
    orientation_map: Matrix,
) -> sp.Expr:
    before=raw_face_residual_energy(face_residual)
    eps_new,_=passive_packet_reparameterization(face_residual,area_frame,orientation_map)
    after=raw_face_residual_energy(eps_new)
    return sp.simplify(after-before)


def unique_max_index(scores: list[sp.Expr]) -> int:
    """Exact numeric/rational ranking helper used only in audited calibrations."""
    if not scores:
        raise ValueError("scores cannot be empty")
    vals=[sp.N(v) for v in scores]
    winner=max(range(len(vals)),key=lambda i: float(vals[i]))
    if any(i != winner and sp.simplify(scores[i]-scores[winner]) == 0 for i in range(len(scores))):
        raise ValueError("calibration requires a unique maximum")
    return winner


def passive_raw_ranking_flip_calibration() -> dict[str,object]:
    """Same physical two-germ packets; raw-norm first-bad ranking flips by basis only."""
    e1=sp.Matrix([1,0,0])
    H0=sp.eye(3); H1=sp.eye(3)
    eps0=e1
    eps1=sp.Rational(3,2)*e1
    S0=sp.diag(2,1,1)
    eps0_new,H0_new=passive_packet_reparameterization(eps0,H0,S0)

    raw_before=[raw_face_residual_energy(eps0),raw_face_residual_energy(eps1)]
    raw_after=[raw_face_residual_energy(eps0_new),raw_face_residual_energy(eps1)]
    physical_before=[
        physical_reconstructed_residual_energy(eps0,H0),
        physical_reconstructed_residual_energy(eps1,H1),
    ]
    physical_after=[
        physical_reconstructed_residual_energy(eps0_new,H0_new),
        physical_reconstructed_residual_energy(eps1,H1),
    ]
    return {
        "raw_before":tuple(raw_before),
        "raw_after":tuple(raw_after),
        "physical_before":tuple(physical_before),
        "physical_after":tuple(physical_after),
        "raw_winner_before":unique_max_index(raw_before),
        "raw_winner_after":unique_max_index(raw_after),
        "physical_winner_before":unique_max_index(physical_before),
        "physical_winner_after":unique_max_index(physical_after),
    }


def passive_event_gauge_calibration() -> dict[str,Matrix|bool]:
    """Raw refinement coordinates change, physical residual event map does not."""
    Hp=sp.diag(2,3,5)
    Hc=sp.diag(1,4,2)
    R=sp.Matrix([[1,1,0],[0,2,1],[1,0,1]])
    Sp=sp.Matrix([[1,1,0],[0,1,0],[0,0,2]])
    Sc=sp.Matrix([[2,0,0],[1,1,0],[0,0,1]])
    Rnew=reparameterized_raw_refinement_block(R,Sp,Sc)
    residual=physical_synthesis_gauge_residual(Hp,Hc,R,Sp,Sc)
    return {
        "raw_block_before":R,
        "raw_block_after":Rnew,
        "raw_block_changes":Rnew != R,
        "physical_event_gauge_residual":residual,
    }


def physical_residual_support_locality_no_go(
    anchor_y: sp.Symbol,
    time: sp.Expr,
    nu: sp.Expr,
    rho: sp.Expr,
) -> dict[str,object]:
    """Exact quadratic NS: gauge-correct physical residual collapses, support does not."""
    c=quadratic_long_support_calibration(anchor_y,time,nu,rho)
    return {
        **c,
        "physical_energy_limit":sp.limit(c["physical_energy"],rho,0,dir="+"),
        "support_line_limit":sp.limit(c["long_x_line_squared"],rho,0,dir="+"),
    }


def persistent_library_switch_obstruction() -> dict[str,bool]:
    state=selector_switch_state_counterexample()
    second=selector_switch_second_moment_counterexample()
    return {
        "old_selected_state_equal":state["old_readout_1"] == state["old_readout_2"],
        "new_selected_state_different":state["new_readout_1"] != state["new_readout_2"],
        "old_selected_second_moment_equal":second["old_Q_1"] == second["old_Q_2"],
        "new_selected_second_moment_different":second["new_Q_1"] != second["new_Q_2"],
    }


def full_coherence_event_obstruction() -> dict[str,object]:
    c=channel_only_composition_counterexample()
    return {
        "input_channels_equal":c["input_channels_plus"] == c["input_channels_minus"],
        "cross_coherence_different":c["cross_coherence_plus"] != c["cross_coherence_minus"],
        "parent_channel_difference":c["parent_channel_difference"],
        "parent_channels_different":c["parent_channel_plus"] != c["parent_channel_minus"],
    }


def adaptive_event_joint_law_obstruction() -> dict[str,object]:
    c=adaptive_event_alignment_calibrations()
    return {
        "all_payloads_psd":bool(c["all_payloads_psd"]),
        "aligned_exact":c["positive_exact"],
        "aligned_naive":c["positive_naive"],
        "anti_aligned_exact":c["negative_exact"],
        "anti_aligned_naive":c["negative_naive"],
        "aligned_mean_closure_false":c["positive_exact"] != c["positive_naive"],
        "anti_aligned_mean_closure_false":c["negative_exact"] != c["negative_naive"],
    }


def first_bad_admissibility_ledger(
    anchor_y: sp.Symbol,
    time: sp.Expr,
    nu: sp.Expr,
    rho: sp.Expr,
) -> dict[str,object]:
    """Assemble necessary typing checks.  Deliberately makes no sufficiency claim."""
    ranking=passive_raw_ranking_flip_calibration()
    event=passive_event_gauge_calibration()
    support=physical_residual_support_locality_no_go(anchor_y,time,nu,rho)
    library=persistent_library_switch_obstruction()
    coherence=full_coherence_event_obstruction()
    adaptive=adaptive_event_joint_law_obstruction()
    return {
        "raw_ranking_is_gauge_artifact":ranking["raw_winner_before"] != ranking["raw_winner_after"],
        "physical_ranking_gauge_invariant":ranking["physical_winner_before"] == ranking["physical_winner_after"],
        "physical_event_map_gauge_invariant":event["physical_event_gauge_residual"] == sp.zeros(3),
        "residual_collapse_does_not_imply_support_locality":support["physical_energy_limit"] == 0 and support["support_line_limit"] == 1,
        "persistent_library_needed_for_switch":all(library.values()),
        "full_coherence_needed_for_linear_events":coherence["input_channels_equal"] and coherence["parent_channels_different"],
        "adaptive_joint_law_needed":adaptive["aligned_mean_closure_false"] and adaptive["anti_aligned_mean_closure_false"],
        "sufficient_first_bad_functional_defined":False,
        "restart_continuation_regularity_proved":False,
    }
