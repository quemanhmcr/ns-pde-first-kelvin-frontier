"""Exact vector future-covariance and generator-descent identities.

This module keeps three structures distinct:

1. the conditional future covariance of a vector Kelvin payoff;
2. the vector carré-du-champ that transfers conditional mean-square into that
   covariance;
3. the extra connection/frame action needed before a full-state tensor law can
   descend to a physical-space tensor law.

Nothing here supplies a singular-time bound.  The full-state moment identities are
exact.  Descent to a reduced spatial state requires an explicit generator
intertwining/lumpability condition.
"""
from __future__ import annotations

from typing import Sequence

import sympy as sp

Matrix = sp.MatrixBase


def vector_jacobian(v: Matrix, coords: Sequence[sp.Symbol]) -> sp.Matrix:
    """Jacobian with rows indexed by vector component and columns by state coordinate."""
    return sp.Matrix([[sp.diff(v[i], x) for x in coords] for i in range(v.rows)])


def diffusion_generator_scalar(
    f: sp.Expr,
    drift: Matrix,
    diffusion_covariance: Matrix,
    coords: Sequence[sp.Symbol],
) -> sp.Expr:
    """Itô generator L f = b.grad f + 1/2 a:Hess f."""
    n = len(coords)
    if drift.shape != (n, 1) or diffusion_covariance.shape != (n, n):
        raise ValueError("state dimensions do not match coordinates")
    first = sum(drift[i] * sp.diff(f, coords[i]) for i in range(n))
    second = sp.Rational(1, 2) * sum(
        diffusion_covariance[i, j] * sp.diff(f, coords[i], coords[j])
        for i in range(n)
        for j in range(n)
    )
    return sp.simplify(first + second)


def diffusion_generator_matrix(
    F: Matrix,
    drift: Matrix,
    diffusion_covariance: Matrix,
    coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    return sp.Matrix(F.rows, F.cols, lambda i, j: diffusion_generator_scalar(F[i, j], drift, diffusion_covariance, coords))


def vector_carre_du_champ(
    mean: Matrix,
    diffusion_covariance: Matrix,
    coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    """Gamma(mean)=J a J^T, including every mixed output covariance."""
    J = vector_jacobian(mean, coords)
    if diffusion_covariance.shape != (J.cols, J.cols):
        raise ValueError("diffusion covariance does not match state dimension")
    return sp.simplify(J * diffusion_covariance * J.T)


def conditional_covariance(mean: Matrix, second_moment: Matrix) -> sp.Matrix:
    if second_moment.shape != (mean.rows, mean.rows):
        raise ValueError("second moment must be square with the output dimension")
    return sp.simplify(second_moment - mean * mean.T)


def horizon_operator_matrix(
    F: Matrix,
    tau: sp.Symbol,
    drift: Matrix,
    diffusion_covariance: Matrix,
    coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    """Semigroup-horizon operator H = partial_tau - L, entrywise."""
    return sp.simplify(sp.diff(F, tau) - diffusion_generator_matrix(F, drift, diffusion_covariance, coords))


def connection_action(C: Matrix, B: Matrix) -> sp.Matrix:
    """Connection action B^T C + C B for a left-moving frame Hdot=B H."""
    if C.rows != C.cols or B.shape != C.shape:
        raise ValueError("connection and tensor must be square with the same shape")
    return sp.simplify(B.T * C + C * B)


def connected_mean_horizon_residual(
    mean: Matrix,
    B: Matrix,
    tau: sp.Symbol,
    drift: Matrix,
    diffusion_covariance: Matrix,
    coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    """Residual H mean + B^T mean."""
    if B.shape != (mean.rows, mean.rows):
        raise ValueError("connection does not match vector dimension")
    return sp.simplify(horizon_operator_matrix(mean, tau, drift, diffusion_covariance, coords) + B.T * mean)


def connected_second_moment_horizon_residual(
    second_moment: Matrix,
    B: Matrix,
    tau: sp.Symbol,
    drift: Matrix,
    diffusion_covariance: Matrix,
    coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    """Residual H Q + B^T Q + Q B for the terminal second moment."""
    return sp.simplify(
        horizon_operator_matrix(second_moment, tau, drift, diffusion_covariance, coords)
        + connection_action(second_moment, B)
    )


def connected_covariance_horizon_residual(
    mean: Matrix,
    second_moment: Matrix,
    B: Matrix,
    tau: sp.Symbol,
    drift: Matrix,
    diffusion_covariance: Matrix,
    coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    """Residual H C + B^T C + C B - Gamma(mean).

    If the connected conditional mean and terminal second moment are homogeneous
    under the horizon semigroup, this vanishes exactly.
    """
    C = conditional_covariance(mean, second_moment)
    Gamma = vector_carre_du_champ(mean, diffusion_covariance, coords)
    return sp.simplify(
        horizon_operator_matrix(C, tau, drift, diffusion_covariance, coords)
        + connection_action(C, B)
        - Gamma
    )


def connected_mean_square_horizon_residual(
    mean: Matrix,
    B: Matrix,
    tau: sp.Symbol,
    drift: Matrix,
    diffusion_covariance: Matrix,
    coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    """Residual H(mm^T)+connection+Gamma; mean-square loses what covariance gains."""
    M = sp.simplify(mean * mean.T)
    Gamma = vector_carre_du_champ(mean, diffusion_covariance, coords)
    return sp.simplify(
        horizon_operator_matrix(M, tau, drift, diffusion_covariance, coords)
        + connection_action(M, B)
        + Gamma
    )


def packet_tensor_pullback(local_tensor: Matrix, H: Matrix) -> sp.Matrix:
    """Raw packet tensor H^T C H."""
    if local_tensor.rows != local_tensor.cols or H.rows != local_tensor.rows:
        raise ValueError("physical tensor and area frame dimensions do not match")
    return sp.simplify(H.T * local_tensor * H)


def connected_local_tensor_horizon_residual(
    local_tensor: Matrix,
    local_source: Matrix,
    B: Matrix,
    tau: sp.Symbol,
    drift: Matrix,
    diffusion_covariance: Matrix,
    coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    """Quotient tensor law H C + B^T C + C B = source.

    This is the law forced by a full packet covariance factorization
    C_H=H^T C H and frame rate Hdot=B H.  Calling it a physical-space Kelvin PDE
    additionally requires literal generator descent from the full stochastic state.
    """
    return sp.simplify(
        horizon_operator_matrix(local_tensor, tau, drift, diffusion_covariance, coords)
        + connection_action(local_tensor, B)
        - local_source
    )


def vorticity_dyad_residual(
    omega: Matrix,
    velocity_gradient: Matrix,
    velocity: Matrix,
    nu: sp.Expr,
    t: sp.Symbol,
    coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    """Exact NS tensor-enstrophy residual.

    For E=omega omega^T,
      (partial_t+u.grad-nu Delta)E
      = A E + E A^T - 2 nu (grad omega)(grad omega)^T,
    with A=grad u.
    """
    if omega.shape != velocity.shape or velocity_gradient.shape != (omega.rows, omega.rows):
        raise ValueError("3D vector/tensor dimensions do not match")
    E = sp.simplify(omega * omega.T)
    adv = sp.Matrix(E.rows, E.cols, lambda i, j: sum(velocity[k] * sp.diff(E[i, j], coords[k]) for k in range(len(coords))))
    lap = sp.Matrix(E.rows, E.cols, lambda i, j: sum(sp.diff(E[i, j], x, 2) for x in coords))
    G = vector_jacobian(omega, coords)
    kelvin_tensor = sp.simplify(2 * nu * G * G.T)
    return sp.simplify(
        sp.diff(E, t) + adv - nu * lap
        - velocity_gradient * E - E * velocity_gradient.T
        + kelvin_tensor
    )


def projection_lift(labels: Sequence[int]) -> sp.Matrix:
    """Lift a reduced observable to full states by a deterministic projection label."""
    if not labels:
        return sp.zeros(0, 0)
    m = max(labels) + 1
    R = sp.zeros(len(labels), m)
    for i, lab in enumerate(labels):
        if lab < 0:
            raise ValueError("projection labels must be nonnegative")
        R[i, lab] = 1
    return R


def fiber_constant_columns(M: Matrix, labels: Sequence[int]) -> bool:
    """Whether every column of M is constant on every projection fiber."""
    if M.rows != len(labels):
        raise ValueError("row count must match projection labels")
    for lab in sorted(set(labels)):
        rows = [i for i, x in enumerate(labels) if x == lab]
        for j in range(M.cols):
            if any(sp.simplify(M[i, j] - M[rows[0], j]) != 0 for i in rows[1:]):
                return False
    return True


def generator_descends(full_generator: Matrix, labels: Sequence[int]) -> bool:
    """Exact lumpability test: L R must remain in the lifted reduced-observable subspace."""
    R = projection_lift(labels)
    if full_generator.shape != (R.rows, R.rows):
        raise ValueError("full generator must be square on full states")
    return fiber_constant_columns(sp.simplify(full_generator * R), labels)


def quotient_generator(full_generator: Matrix, labels: Sequence[int]) -> sp.Matrix:
    """Return the exact reduced generator when generator_descends is true."""
    if not generator_descends(full_generator, labels):
        raise ValueError("full generator does not descend through this projection")
    R = projection_lift(labels)
    representatives = [labels.index(lab) for lab in range(R.cols)]
    LR = sp.simplify(full_generator * R)
    return sp.Matrix([[LR[representatives[i], j] for j in range(R.cols)] for i in range(R.cols)])


def generator_intertwining_residual(full_generator: Matrix, labels: Sequence[int]) -> sp.Matrix:
    """L R - R Lbar when a quotient exists; otherwise expose fiber differences."""
    R = projection_lift(labels)
    if generator_descends(full_generator, labels):
        return sp.simplify(full_generator * R - R * quotient_generator(full_generator, labels))
    # No quotient exists.  Return LR with each fiber's first row subtracted so the
    # nonzero entries are the literal hidden-state flux obstruction.
    LR = sp.simplify(full_generator * R)
    out = sp.zeros(*LR.shape)
    for lab in sorted(set(labels)):
        rows = [i for i, x in enumerate(labels) if x == lab]
        ref = rows[0]
        for i in rows:
            for j in range(LR.cols):
                out[i, j] = sp.simplify(LR[i, j] - LR[ref, j])
    return out


def symmetric_loop_covariance_expansion(
    local_covariance: Matrix,
    local_next_cross: Matrix,
    next_covariance: Matrix,
    r: sp.Expr,
) -> sp.Matrix:
    """C^2 symmetric-loop model: r^4 C0 + r^6 Ccross + r^8 C2.

    A centered smooth disk has area O(r^2); symmetry removes the linear spatial
    moment, so a quadratic field correction enters the payoff at O(r^4).  Hence
    its covariance first differs from the area-squared local tensor at O(r^6).
    """
    if local_covariance.shape != local_next_cross.shape or local_covariance.shape != next_covariance.shape:
        raise ValueError("all covariance coefficients must have the same shape")
    return sp.simplify(r**4 * local_covariance + r**6 * local_next_cross + r**8 * next_covariance)


def metric_amplified_symmetric_remainder(
    raw_covariance: Matrix,
    local_covariance: Matrix,
    r: sp.Expr,
) -> Matrix:
    """Remove r^4 local tensor and apply the r^-4 packet metric scaling."""
    return sp.simplify((raw_covariance - r**4 * local_covariance) / r**4)


def double_stokes_pair_covariance(pair_cochain_covariance: Matrix, face_boundary: Matrix) -> sp.Matrix:
    """Induced covariance on face fluxes/cycle circulations: D^T K D.

    `face_boundary` maps 2-chains to closed 1-chains.  This is the finite-chain
    model of applying d on both cochain replicas before taking a small-surface
    diagonal trace.
    """
    if pair_cochain_covariance.rows != pair_cochain_covariance.cols:
        raise ValueError("pair cochain covariance must be square")
    if face_boundary.rows != pair_cochain_covariance.rows:
        raise ValueError("face boundary must land in the cochain's 1-chain space")
    return sp.simplify(face_boundary.T * pair_cochain_covariance * face_boundary)


def exact_gauge_cycle_projection(vertex_edge_boundary: Matrix, face_boundary: Matrix, vertex_potential: Matrix) -> sp.Matrix:
    """Pair a vertex-exact edge cochain B^T p with face boundaries D.

    Boundary-of-boundary B D=0 forces the result to vanish exactly.
    """
    if vertex_potential.cols != 1 or vertex_potential.rows != vertex_edge_boundary.rows:
        raise ValueError("vertex potential dimension mismatch")
    exact_edge_cochain = vertex_edge_boundary.T * vertex_potential
    return sp.simplify(face_boundary.T * exact_edge_cochain)


def product_pair_diagonal_defect(
    mean: Matrix,
    coords: Sequence[sp.Symbol],
    replica1_coords: Sequence[sp.Symbol],
    replica2_coords: Sequence[sp.Symbol],
    drift: Matrix,
    diffusion_covariance: Matrix,
) -> sp.Matrix:
    """Diagonal generator defect for U(y1,y2)=m(y1)m(y2)^T.

    Returns
      L(U^Delta) - (L1+L2)U|_Delta,
    which must equal the full vector carré-du-champ J a J^T.  This is the matrix
    form of the canonical same-ancestor viscous branch source.
    """
    if len(coords) != len(replica1_coords) or len(coords) != len(replica2_coords):
        raise ValueError("replica coordinate dimensions must match")
    sub1 = dict(zip(coords, replica1_coords))
    sub2 = dict(zip(coords, replica2_coords))
    diag_subs = {replica1_coords[i]: coords[i] for i in range(len(coords))}
    diag_subs.update({replica2_coords[i]: coords[i] for i in range(len(coords))})
    m1 = mean.xreplace(sub1)
    m2 = mean.xreplace(sub2)
    U = sp.simplify(m1 * m2.T)
    Udiag = sp.simplify(mean * mean.T)
    drift1 = drift.xreplace(sub1)
    drift2 = drift.xreplace(sub2)
    a1 = diffusion_covariance.xreplace(sub1)
    a2 = diffusion_covariance.xreplace(sub2)
    Ldiag = diffusion_generator_matrix(Udiag, drift, diffusion_covariance, coords)
    L1 = diffusion_generator_matrix(U, drift1, a1, replica1_coords)
    L2 = diffusion_generator_matrix(U, drift2, a2, replica2_coords)
    return sp.simplify(Ldiag - (L1 + L2).xreplace(diag_subs))


def backward_kelvin_flux_mean_residual(
    omega: Matrix,
    velocity_gradient: Matrix,
    velocity: Matrix,
    area_frame: Matrix,
    nu: sp.Expr,
    t: sp.Symbol,
    coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    """Backward-Itô infinitesimal Kelvin packet mean residual.

    The backward spatial operator is partial_t + u.grad - nu Delta and the
    additive-noise stochastic flow has Nanson frame drift Hdot=-(grad u)^T H.
    For the packet flux mean H^T omega, Navier--Stokes forces exact cancellation.
    """
    if area_frame.shape != (3, 3) or omega.shape != (3, 1) or velocity_gradient.shape != (3, 3):
        raise ValueError("backward Kelvin flux audit is 3D")
    Hdot = sp.simplify(-velocity_gradient.T * area_frame)
    omega_dt = sp.diff(omega, t)
    omega_adv = sp.Matrix([
        sum(velocity[j] * sp.diff(omega[i], coords[j]) for j in range(3))
        for i in range(3)
    ])
    omega_lap = sp.Matrix([
        sum(sp.diff(omega[i], x, 2) for x in coords)
        for i in range(3)
    ])
    return sp.simplify(Hdot.T * omega + area_frame.T * (omega_dt + omega_adv - nu * omega_lap))


def backward_local_tensor_operator(
    tensor: Matrix,
    velocity_gradient: Matrix,
    velocity: Matrix,
    nu: sp.Expr,
    t: sp.Symbol,
    coords: Sequence[sp.Symbol],
) -> sp.Matrix:
    """Connection-covariant backward Kelvin tensor operator.

      D_K T = (partial_t+u.grad-nu Delta)T - A T - T A^T,

    corresponding to Nanson frame rate Hdot=-A^T H.
    """
    A = velocity_gradient
    adv = sp.Matrix(tensor.rows, tensor.cols, lambda i, j: sum(velocity[k] * sp.diff(tensor[i, j], coords[k]) for k in range(3)))
    lap = sp.Matrix(tensor.rows, tensor.cols, lambda i, j: sum(sp.diff(tensor[i, j], x, 2) for x in coords))
    return sp.simplify(sp.diff(tensor, t) + adv - nu * lap - A * tensor - tensor * A.T)
