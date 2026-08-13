"""Continuous Brownian-source revaluation across a combined finite selected event.

A finite physical/selector event has two distinct stochastic effects:

1. the selected càdlàg path may jump, contributing a jump square to optional q.v.;
2. the *continuous Brownian q.v. rate after the event* may be different because the
   physical library noise response and/or active selector changed.

These are different tensors.  For pre-event stacked same-replica noise response N,
physical library map A, and selector readouts E_-, E_+,

    B_- = E_- N,
    B_+ = E_+ A N,
    dB  = (E_+ A-E_-)N = D N.

The continuous q.v. source revaluation is the exact dyad product rule

    Gamma_+ - Gamma_-
      = 2nu[dB B_-^T + B_- dB^T + dB dB^T].

It is a finite revaluation of the *rate*, not a Brownian q.v. atom at the event.
"""
from __future__ import annotations

import sympy as sp

from .selected_principal_kelvin_lineage import germ_extraction_map
from .selected_residual_combined_event import combined_selected_jump_operator, combined_jump_square
from .same_replica_residual_library_dynamics import one_mode_two_packet_common_noise_calibration

Matrix = sp.MatrixBase


def pre_selected_noise_response(
    stacked_noise: Matrix,
    germ_count: int,
    pre_index: int,
    fiber_dim: int = 3,
) -> Matrix:
    Eminus=germ_extraction_map(germ_count,pre_index,fiber_dim)
    if Eminus.cols != stacked_noise.rows:
        raise ValueError("pre selector/noise dimensions mismatch")
    return sp.simplify(Eminus*stacked_noise)


def post_selected_noise_response(
    stacked_noise: Matrix,
    full_event_map: Matrix,
    post_germ_count: int,
    post_index: int,
    fiber_dim: int = 3,
) -> Matrix:
    Eplus=germ_extraction_map(post_germ_count,post_index,fiber_dim)
    if full_event_map.cols != stacked_noise.rows or Eplus.cols != full_event_map.rows:
        raise ValueError("post selector/event/noise dimensions mismatch")
    return sp.simplify(Eplus*full_event_map*stacked_noise)


def selected_continuous_qv_rate_from_noise(noise_response: Matrix, nu: sp.Expr) -> Matrix:
    return sp.simplify(2*nu*noise_response*noise_response.T)


def combined_continuous_qv_rate_revaluation_faces(
    stacked_noise: Matrix,
    full_event_map: Matrix,
    pre_germ_count: int,
    pre_index: int,
    post_germ_count: int,
    post_index: int,
    nu: sp.Expr,
    fiber_dim: int = 3,
) -> tuple[Matrix,Matrix,Matrix]:
    Bminus=pre_selected_noise_response(stacked_noise,pre_germ_count,pre_index,fiber_dim)
    D=combined_selected_jump_operator(
        full_event_map,pre_germ_count,pre_index,post_germ_count,post_index,fiber_dim
    )
    if D.cols != stacked_noise.rows:
        raise ValueError("combined jump/noise dimensions mismatch")
    dB=sp.simplify(D*stacked_noise)
    left=sp.simplify(2*nu*dB*Bminus.T)
    right=sp.simplify(2*nu*Bminus*dB.T)
    quadratic=sp.simplify(2*nu*dB*dB.T)
    return left,right,quadratic


def combined_continuous_qv_rate_revaluation_residual(
    stacked_noise: Matrix,
    full_event_map: Matrix,
    pre_germ_count: int,
    pre_index: int,
    post_germ_count: int,
    post_index: int,
    nu: sp.Expr,
    fiber_dim: int = 3,
) -> Matrix:
    Bminus=pre_selected_noise_response(stacked_noise,pre_germ_count,pre_index,fiber_dim)
    Bplus=post_selected_noise_response(stacked_noise,full_event_map,post_germ_count,post_index,fiber_dim)
    Gminus=selected_continuous_qv_rate_from_noise(Bminus,nu)
    Gplus=selected_continuous_qv_rate_from_noise(Bplus,nu)
    left,right,quad=combined_continuous_qv_rate_revaluation_faces(
        stacked_noise,full_event_map,pre_germ_count,pre_index,
        post_germ_count,post_index,nu,fiber_dim
    )
    return sp.simplify(Gplus-Gminus-left-right-quad)


def source_revaluation_vs_jump_square_calibrations() -> dict[str,Matrix|bool]:
    """Two exact witnesses proving q.v.-rate revaluation and jump square are independent.

    Witness A: X=0 but a selector switch changes continuous source rate.
    Witness B: N=0 but a selector switch produces a nonzero state jump square.
    """
    nu=sp.Integer(1)
    I6=sp.eye(6)
    # A: zero state, unequal noise blocks.
    Xzero=sp.zeros(6,1)
    N=sp.zeros(6,3)
    N[2,1]=1
    N[5,1]=2
    B0=pre_selected_noise_response(N,2,0)
    B1=post_selected_noise_response(N,I6,2,1)
    rate_jump=sp.simplify(
        selected_continuous_qv_rate_from_noise(B1,nu)
        - selected_continuous_qv_rate_from_noise(B0,nu)
    )
    state_jump_square_zero=combined_jump_square(Xzero,I6,2,0,2,1) == sp.zeros(3)

    # B: zero continuous noise, nonzero library state.
    Nzero=sp.zeros(6,3)
    X=sp.Matrix([1,0,0,0,1,0])
    rate_jump_zero=sp.simplify(
        selected_continuous_qv_rate_from_noise(post_selected_noise_response(Nzero,I6,2,1),nu)
        - selected_continuous_qv_rate_from_noise(pre_selected_noise_response(Nzero,2,0),nu)
    )
    jump_square=combined_jump_square(X,I6,2,0,2,1)
    return {
        "rate_revaluation_nonzero_with_zero_state_jump_square": rate_jump != sp.zeros(3) and state_jump_square_zero,
        "rate_revaluation": rate_jump,
        "zero_rate_revaluation_with_nonzero_state_jump_square": rate_jump_zero == sp.zeros(3) and jump_square != sp.zeros(3),
        "jump_square": jump_square,
    }


def one_mode_hidden_synthesis_qv_rate_calibration(
    t: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> dict[str,Matrix|sp.Expr|bool]:
    """Exact one-mode NS same-replica noise payload through hidden synthesis + switch.

    The two packet noise responses are opposite.  A specified current event leaves
    germ 0 unchanged and sends germ 1 -> germ 1 + germ 0; then selector switches 0->1.
    The post-event selected continuous Brownian response vanishes exactly.
    """
    c=one_mode_two_packet_common_noise_calibration(t,nu,k)
    Q0=sp.zeros(3); Q1=sp.zeros(3)
    Q0[2,1]=c["q1"]
    Q1[2,1]=c["q2"]
    N=sp.Matrix.vstack(Q0,Q1)
    I=sp.eye(3); Z=sp.zeros(3)
    A=sp.Matrix.vstack(
        sp.Matrix.hstack(I,Z),
        sp.Matrix.hstack(I,I),
    )
    Bpre=pre_selected_noise_response(N,2,0)
    Bselector_only=post_selected_noise_response(N,sp.eye(6),2,1)
    Bpost=post_selected_noise_response(N,A,2,1)
    Gpre=selected_continuous_qv_rate_from_noise(Bpre,nu)
    Gselector_only=selected_continuous_qv_rate_from_noise(Bselector_only,nu)
    Gpost=selected_continuous_qv_rate_from_noise(Bpost,nu)
    left,right,quad=combined_continuous_qv_rate_revaluation_faces(N,A,2,0,2,1,nu)
    return {
        "q0":c["q1"],
        "q1":c["q2"],
        "opposite_noise_residual":sp.simplify(c["q1"]+c["q2"]),
        "pre_noise":Bpre,
        "selector_only_post_noise":Bselector_only,
        "actual_post_noise":Bpost,
        "pre_qv_rate":Gpre,
        "selector_only_post_qv_rate":Gselector_only,
        "actual_post_qv_rate":Gpost,
        "actual_rate_revaluation":sp.simplify(Gpost-Gpre),
        "selector_only_rate_revaluation":sp.simplify(Gselector_only-Gpre),
        "rate_left":left,
        "rate_right":right,
        "rate_quadratic":quad,
        "rate_revaluation_residual":combined_continuous_qv_rate_revaluation_residual(N,A,2,0,2,1,nu),
    }
