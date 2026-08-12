"""Exact scale-parametric support x total-bank tensor factorization.

Write on one coherent state/frame

    omega = F eta,
    Q_tot = eta eta^T + C_tilde,  C_tilde >= 0,
    P_ell = ell^2 F F^T.

The core identity is clock-free:

    p q I - ell^2 omega omega^T
      = q (p I-P_ell)
        + ell^2 F(q I-Q_tot)F^T
        + ell^2 F(Q_tot-eta eta^T)F^T.

Setting ell^2=2 nu tau is a separate scale specialization.  The causal physical
backward-Kelvin bank has a past horizon h=t-t0; for fixed t0 this is not the future
remaining horizon tau=Theta-t.  Matching h=tau requires a moving past terminal
`t0(t)=2t-Theta`, whose derivative produces an explicit terminal-motion face.

No programme-specific scale/covariance horizon identification, uniform first-bad
envelope, continuation, or regularity theorem is encoded here.
"""
from __future__ import annotations

import sympy as sp

Matrix = sp.MatrixBase


def codeforming_total_second_moment(mean: Matrix, covariance: Matrix) -> sp.Matrix:
    if mean.cols != 1 or covariance.rows != covariance.cols or covariance.rows != mean.rows:
        raise ValueError("mean/covariance dimension mismatch")
    return sp.simplify(mean * mean.T + covariance)


def physical_vorticity_from_codeforming(deformation: Matrix, mean: Matrix) -> sp.Matrix:
    return sp.simplify(deformation * mean)


def physical_total_second_moment(deformation: Matrix, total: Matrix) -> sp.Matrix:
    return sp.simplify(deformation * total * deformation.T)


def parabolic_support_tensor(
    deformation: Matrix,
    nu: sp.Expr,
    remaining_horizon: sp.Expr,
) -> sp.Matrix:
    return sp.simplify(2 * nu * remaining_horizon * deformation * deformation.T)


def resolved_unresolved_factorization_residual(
    deformation: Matrix,
    mean: Matrix,
    covariance: Matrix,
) -> sp.Matrix:
    Q = codeforming_total_second_moment(mean, covariance)
    T = physical_total_second_moment(deformation, Q)
    omega = physical_vorticity_from_codeforming(deformation, mean)
    return sp.simplify(T - omega * omega.T - deformation * covariance * deformation.T)


def support_bank_three_face_residual(
    deformation: Matrix,
    mean: Matrix,
    covariance: Matrix,
    p_star: sp.Expr,
    q_star: sp.Expr,
    nu: sp.Expr,
    remaining_horizon: sp.Expr,
) -> sp.Matrix:
    """Residual of the exact three-positive-sector decomposition."""
    n = deformation.rows
    if deformation.cols != n or mean.shape != (n, 1) or covariance.shape != (n, n):
        raise ValueError("all state tensors must have one common square dimension")
    I = sp.eye(n)
    Q = codeforming_total_second_moment(mean, covariance)
    P = parabolic_support_tensor(deformation, nu, remaining_horizon)
    omega = physical_vorticity_from_codeforming(deformation, mean)
    lhs = sp.simplify(p_star * q_star * I - 2 * nu * remaining_horizon * omega * omega.T)
    rhs = sp.simplify(
        q_star * (p_star * I - P)
        + 2 * nu * remaining_horizon * deformation * (q_star * I - Q) * deformation.T
        + 2 * nu * remaining_horizon * deformation * (Q - mean * mean.T) * deformation.T
    )
    return sp.simplify(lhs - rhs)


def total_bank_support_factorization_residual(
    deformation: Matrix,
    total: Matrix,
    q_star: sp.Expr,
    nu: sp.Expr,
    remaining_horizon: sp.Expr,
) -> sp.Matrix:
    """q P_nu - 2 nu tau T_tot = 2 nu tau F(q I-Q_tot)F^T."""
    n = deformation.rows
    I = sp.eye(n)
    P = parabolic_support_tensor(deformation, nu, remaining_horizon)
    T = physical_total_second_moment(deformation, total)
    return sp.simplify(
        q_star * P
        - 2 * nu * remaining_horizon * T
        - 2 * nu * remaining_horizon * deformation * (q_star * I - total) * deformation.T
    )


def scalar_vorticity_rate_square_bound(
    p_star: sp.Expr,
    q_star: sp.Expr,
    nu: sp.Expr,
    remaining_horizon: sp.Expr,
) -> sp.Expr:
    """Scalar RHS p*q/(2 nu tau) implied by the tensor Loewner envelope."""
    return sp.simplify(p_star * q_star / (2 * nu * remaining_horizon))


def time_integrated_vorticity_rate_bound(
    product_bound: sp.Expr,
    nu: sp.Expr,
    epsilon: sp.Expr,
) -> sp.Expr:
    """Integral of sqrt(M/(2nu tau)) from tau=0 to epsilon."""
    return sp.simplify(sp.sqrt(2 * product_bound * epsilon / nu))


def parabolic_support_dynamics_residual(
    grad_u: Matrix,
    deformation: Matrix,
    nu: sp.Expr,
    remaining_horizon: sp.Expr,
) -> sp.Matrix:
    """Physical-time law Pdot=A P+P A^T-P/tau for tau=Theta-t."""
    B = sp.simplify(deformation * deformation.T)
    P = sp.simplify(2 * nu * remaining_horizon * B)
    Bdot = sp.simplify(grad_u * B + B * grad_u.T)
    Pdot_direct = sp.simplify(-2 * nu * B + 2 * nu * remaining_horizon * Bdot)
    Pdot_rhs = sp.simplify(grad_u * P + P * grad_u.T - P / remaining_horizon)
    return sp.simplify(Pdot_direct - Pdot_rhs)


def isotropic_diagonal_envelope_gap(
    p_star: sp.Expr,
    q_star: sp.Expr,
    support_diagonal: tuple[sp.Expr, ...],
    total_diagonal: tuple[sp.Expr, ...],
    resolved_diagonal: tuple[sp.Expr, ...],
    nu: sp.Expr,
    tau: sp.Expr,
) -> sp.Matrix:
    """Diagonal witness of the three-sector PSD gap.

    resolved_diagonal are eta_i^2, so Q_i-resolved_i is covariance content.
    """
    if not (len(support_diagonal) == len(total_diagonal) == len(resolved_diagonal)):
        raise ValueError("diagonal lengths must match")
    return sp.diag(*[
        sp.simplify(
            q_star * (p_star - support_diagonal[i])
            + (q_star * support_diagonal[i] - support_diagonal[i] * total_diagonal[i])
            + support_diagonal[i] * (total_diagonal[i] - resolved_diagonal[i])
        )
        for i in range(len(support_diagonal))
    ])


def support_tensor_from_scale_squared(deformation: Matrix, scale_squared: sp.Expr) -> sp.Matrix:
    """Pure geometric support tensor ell^2 F F^T for any positive scale ell."""
    return sp.simplify(scale_squared * deformation * deformation.T)


def scale_parametric_three_face_residual(
    deformation: Matrix,
    mean: Matrix,
    covariance: Matrix,
    p_star: sp.Expr,
    q_star: sp.Expr,
    scale_squared: sp.Expr,
) -> sp.Matrix:
    """Scale-parametric version of the three-face factorization.

    No stochastic clock is assumed.  Setting scale_squared=2 nu h is a separate
    physical identification step.
    """
    n = deformation.rows
    I = sp.eye(n)
    Q = codeforming_total_second_moment(mean, covariance)
    P = support_tensor_from_scale_squared(deformation, scale_squared)
    omega = physical_vorticity_from_codeforming(deformation, mean)
    lhs = sp.simplify(p_star*q_star*I - scale_squared*omega*omega.T)
    rhs = sp.simplify(
        q_star*(p_star*I-P)
        + scale_squared*deformation*(q_star*I-Q)*deformation.T
        + scale_squared*deformation*(Q-mean*mean.T)*deformation.T
    )
    return sp.simplify(lhs-rhs)


def causal_backward_kelvin_horizon(physical_time: sp.Expr, past_terminal: sp.Expr) -> sp.Expr:
    """Causal fixed-past-terminal backward-Kelvin horizon h=t-t0."""
    return sp.simplify(physical_time - past_terminal)


def future_candidate_remaining_horizon(candidate_time: sp.Expr, physical_time: sp.Expr) -> sp.Expr:
    """Future first-bad/candidate remaining horizon tau=Theta-t."""
    return sp.simplify(candidate_time - physical_time)


def moving_past_terminal_matching_future_horizon(
    candidate_time: sp.Expr,
    physical_time: sp.Expr,
) -> sp.Expr:
    """Past terminal t0(t) required by t-t0 = Theta-t."""
    return sp.simplify(2*physical_time - candidate_time)


def horizon_matching_residual(
    candidate_time: sp.Expr,
    physical_time: sp.Expr,
) -> sp.Expr:
    t0 = moving_past_terminal_matching_future_horizon(candidate_time, physical_time)
    return sp.simplify(
        causal_backward_kelvin_horizon(physical_time, t0)
        - future_candidate_remaining_horizon(candidate_time, physical_time)
    )


def fixed_past_horizon_candidate_limit(candidate_time: sp.Expr, past_terminal: sp.Expr) -> sp.Expr:
    """lim_{t->Theta} (t-t0)=Theta-t0, hence no shrinking for fixed t0<Theta."""
    return sp.simplify(candidate_time - past_terminal)


def moving_terminal_chain_derivative(
    partial_current_time: sp.Expr,
    partial_terminal_time: sp.Expr,
    terminal_speed: sp.Expr,
) -> sp.Expr:
    """d/dt Q(t,t0(t)) = Q_t + t0dot Q_t0."""
    return sp.simplify(partial_current_time + terminal_speed * partial_terminal_time)


def one_mode_backward_kelvin_second_moment(
    y: sp.Expr,
    current_time: sp.Expr,
    past_terminal: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """Exact causal past-payoff second moment for one-mode shear vorticity."""
    h = sp.simplify(current_time - past_terminal)
    return sp.simplify(
        k**2 * sp.exp(-2 * nu * k**2 * past_terminal) / 2
        * (1 - sp.exp(-4 * nu * k**2 * h) * sp.cos(2 * k * y))
    )


def one_mode_current_vorticity_square(
    y: sp.Expr,
    current_time: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    return sp.simplify(k**2 * sp.exp(-2 * nu * k**2 * current_time) * sp.sin(k * y)**2)


def one_mode_backward_kelvin_covariance(
    y: sp.Expr,
    current_time: sp.Expr,
    past_terminal: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    Q = one_mode_backward_kelvin_second_moment(y, current_time, past_terminal, nu, k)
    return sp.simplify(Q - one_mode_current_vorticity_square(y, current_time, nu, k))


def one_mode_fixed_terminal_second_moment_residual(
    y: sp.Expr,
    current_time: sp.Symbol,
    past_terminal: sp.Symbol,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """(partial_t-nu partial_yy)Q=0 at fixed past terminal."""
    Q = one_mode_backward_kelvin_second_moment(y, current_time, past_terminal, nu, k)
    return sp.trigsimp(sp.simplify(sp.diff(Q, current_time) - nu * sp.diff(Q, y, 2)))


def one_mode_moving_terminal_second_moment_residual(
    y: sp.Expr,
    current_time: sp.Symbol,
    candidate_time: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """Moving t0=2t-Theta leaves exactly the terminal-motion face 2 partial_t0 Q."""
    t0 = sp.Symbol("t0", real=True)
    Q = one_mode_backward_kelvin_second_moment(y, current_time, t0, nu, k)
    moving = sp.simplify(Q.subs(t0, 2 * current_time - candidate_time))
    lhs = sp.simplify(sp.diff(moving, current_time) - nu * sp.diff(moving, y, 2))
    terminal_face = sp.simplify(2 * sp.diff(Q, t0).subs(t0, 2 * current_time - candidate_time))
    return sp.trigsimp(sp.simplify(lhs - terminal_face))


def one_mode_moving_terminal_covariance_residual(
    y: sp.Expr,
    current_time: sp.Symbol,
    candidate_time: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> sp.Expr:
    """Moving-terminal covariance law = fixed-terminal qv source + terminal face."""
    t0 = sp.Symbol("t0", real=True)
    C = one_mode_backward_kelvin_covariance(y, current_time, t0, nu, k)
    moving = sp.simplify(C.subs(t0, 2 * current_time - candidate_time))
    omega = k * sp.exp(-nu * k**2 * current_time) * sp.sin(k * y)
    gamma = sp.simplify(2 * nu * sp.diff(omega, y)**2)
    lhs = sp.simplify(sp.diff(moving, current_time) - nu * sp.diff(moving, y, 2))
    terminal_face = sp.simplify(2 * sp.diff(C, t0).subs(t0, 2 * current_time - candidate_time))
    return sp.trigsimp(sp.simplify(lhs - gamma - terminal_face))
