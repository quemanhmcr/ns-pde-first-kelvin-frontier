"""Exact orientation-complete Kelvin packet algebra for the restart frontier.

This module does not assert a first-bad threshold or a continuation theorem.  It
only records the exact finite-dimensional algebra forced when one physical germ is
represented by a three-loop Kelvin microframe rather than by one orientation.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import sympy as sp

Matrix = sp.MatrixBase


def _diag(values: Sequence[sp.Expr]) -> sp.Matrix:
    return sp.diag(*list(values))


def orientation_qv_matrix(
    grad_omega: Matrix,
    normals: Matrix,
    nu: sp.Expr,
) -> sp.Matrix:
    """Full cross-orientation Kelvin q.v. density matrix.

    The columns of ``normals`` are loop normals n_j.  In a constant orthonormal
    noise frame the area-normalized Kelvin coefficient matrix is

        B_ij = (partial_i omega) dot n_j.

    Hence the shared-noise q.v. covariance across loop orientations is

        Gamma_mf = 2 nu B^T B
                 = 2 nu N^T (grad omega)(grad omega)^T N.

    The diagonal gives the one-loop densities.  Off-diagonal entries are physical
    cross-orientation martingale covariance and must not be discarded.
    """
    if grad_omega.shape != (3, 3) or normals.shape != (3, 3):
        raise ValueError("expected 3x3 vorticity gradient and 3x3 normal frame")
    return sp.simplify(2 * nu * normals.T * grad_omega * grad_omega.T * normals)


def packet_bulk_payment(gamma_packet: Matrix) -> sp.Expr:
    """One-half trace of the orientation q.v. matrix."""
    if gamma_packet.shape != (3, 3):
        raise ValueError("orientation packet covariance must be 3x3")
    return sp.simplify(sp.trace(gamma_packet) / 2)


def packet_covariance_pullback(C: Matrix, L: Matrix) -> sp.Matrix:
    """Full covariance pullback under an orientation/coefficient map L."""
    if C.rows != C.cols or C.rows != L.rows:
        raise ValueError("covariance and coefficient map dimensions must agree")
    return sp.simplify(L.T * C * L)


def packet_pair_map(L: Matrix) -> sp.Matrix:
    """Full ordered-pair coefficient map L tensor L."""
    return sp.kronecker_product(L, L)


def orientation_diagonal_projection(C: Matrix) -> sp.Matrix:
    """Observer projection that discards cross-orientation covariance."""
    if C.rows != C.cols:
        raise ValueError("covariance must be square")
    return sp.diag(*[C[i, i] for i in range(C.rows)])


def packet_selector(germ_selector: Matrix, orientation_dim: int = 3) -> sp.Matrix:
    """Lift a germ selector to an orientation-complete block selector M tensor I."""
    if germ_selector.rows != germ_selector.cols:
        raise ValueError("germ selector must be square")
    if orientation_dim <= 0:
        raise ValueError("orientation dimension must be positive")
    return sp.kronecker_product(germ_selector, sp.eye(orientation_dim))


def parallel_cycle_packet_library(
    germ_count: int,
    orientation_dim: int = 3,
) -> tuple[sp.Matrix, sp.Matrix]:
    """Exact graph library with one independent closed cycle per germ/orientation.

    Each cycle is the difference of two parallel oriented edges.  Coefficients are
    ordered germ-major, then orientation-major, matching ``M tensor I_3``.
    """
    if germ_count <= 0 or orientation_dim <= 0:
        raise ValueError("germ and orientation counts must be positive")
    atoms = germ_count * orientation_dim
    B = sp.zeros(atoms + 1, 2 * atoms)
    K = sp.zeros(2 * atoms, atoms)
    for j in range(atoms):
        B[j, 2 * j] = -1
        B[j, 2 * j + 1] = -1
        B[j + 1, 2 * j] = 1
        B[j + 1, 2 * j + 1] = 1
        K[2 * j, j] = 1
        K[2 * j + 1, j] = -1
    return B, K


def rotation_connection_residual(
    C: Matrix,
    Cdot: Matrix,
    Q: Matrix,
    Qdot: Matrix,
) -> sp.Matrix:
    """Residual of the exact rotating-orientation covariance derivative.

    For Q in SO(3), Omega=Q^T Qdot is skew and

      d(Q^T C Q)
      = Q^T Cdot Q + C_Q Omega - Omega C_Q.

    The commutator redistributes directional covariance but has zero trace.
    """
    Cq = sp.simplify(Q.T * C * Q)
    Omega = sp.simplify(Q.T * Qdot)
    direct = sp.simplify(Qdot.T * C * Q + Q.T * Cdot * Q + Q.T * C * Qdot)
    expected = sp.simplify(Q.T * Cdot * Q + Cq * Omega - Omega * Cq)
    return sp.simplify(direct - expected)


def rotation_commutator(C_rot: Matrix, Omega: Matrix) -> sp.Matrix:
    """Pure orientation-connection work C Omega - Omega C."""
    return sp.simplify(C_rot * Omega - Omega * C_rot)


def normalized_packet_covariance(C: Matrix, areas: Sequence[sp.Expr]) -> sp.Matrix:
    """Area-normalized packet covariance D^{-1} C D^{-1}."""
    if C.rows != C.cols or C.rows != len(areas):
        raise ValueError("area vector must match square covariance")
    Dinv = _diag([sp.simplify(1 / a) for a in areas])
    return sp.simplify(Dinv * C * Dinv)


def normalized_packet_derivative(
    C: Matrix,
    Cdot: Matrix,
    areas: Sequence[sp.Expr],
    area_dots: Sequence[sp.Expr],
) -> sp.Matrix:
    """Exact derivative of D^{-1} C D^{-1}.

    With E=D^{-1} Ddot and Chat=D^{-1} C D^{-1},

      Chatdot = D^{-1} Cdot D^{-1} - E Chat - Chat E.

    This is the anisotropic two-face dilation law.  The scalar
    -2(A_dot/A)Vhat is only the isotropic special case.
    """
    if len(areas) != len(area_dots):
        raise ValueError("area and area-derivative vectors must agree")
    Chat = normalized_packet_covariance(C, areas)
    Dinv = _diag([sp.simplify(1 / a) for a in areas])
    E = _diag([sp.simplify(da / a) for a, da in zip(areas, area_dots)])
    return sp.simplify(Dinv * Cdot * Dinv - E * Chat - Chat * E)


def normalized_packet_bank_rhs(
    C: Matrix,
    Gamma: Matrix,
    W: Matrix,
    areas: Sequence[sp.Expr],
    area_dots: Sequence[sp.Expr],
) -> sp.Matrix:
    """Normalized covariance law when Cdot=-Gamma+W."""
    return normalized_packet_derivative(C, -Gamma + W, areas, area_dots)


def packet_scalar_bank(Chat: Matrix) -> sp.Expr:
    """Orientation-complete scalar bank, one-half trace of normalized covariance."""
    if Chat.rows != Chat.cols:
        raise ValueError("normalized covariance must be square")
    return sp.simplify(sp.trace(Chat) / 2)


@dataclass(frozen=True)
class PacketResetDecomposition:
    total: sp.Matrix
    linear_left: sp.Matrix
    linear_right: sp.Matrix
    quadratic: sp.Matrix

    @property
    def reconstructed(self) -> sp.Matrix:
        return sp.simplify(self.linear_left + self.linear_right + self.quadratic)


def packet_reset_decomposition(C0: Matrix, L_minus: Matrix, L_plus: Matrix) -> PacketResetDecomposition:
    """Exact matrix covariance reset under a finite packet coefficient jump.

      C(L+) - C(L-)
      = DeltaL^T C0 L- + L-^T C0 DeltaL + DeltaL^T C0 DeltaL.
    """
    if L_minus.shape != L_plus.shape:
        raise ValueError("packet reset maps must have the same shape")
    delta = L_plus - L_minus
    Cminus = packet_covariance_pullback(C0, L_minus)
    Cplus = packet_covariance_pullback(C0, L_plus)
    left = sp.simplify(delta.T * C0 * L_minus)
    right = sp.simplify(L_minus.T * C0 * delta)
    quad = sp.simplify(delta.T * C0 * delta)
    return PacketResetDecomposition(
        total=sp.simplify(Cplus - Cminus),
        linear_left=left,
        linear_right=right,
        quadratic=quad,
    )


@dataclass(frozen=True)
class NormalizedPacketJumpDecomposition:
    total: sp.Matrix
    map_reset_at_new_scale: sp.Matrix
    pure_scale_revaluation: sp.Matrix

    @property
    def reconstructed(self) -> sp.Matrix:
        return sp.simplify(self.map_reset_at_new_scale + self.pure_scale_revaluation)


def normalized_packet_jump_decomposition(
    C0: Matrix,
    L_minus: Matrix,
    L_plus: Matrix,
    areas_minus: Sequence[sp.Expr],
    areas_plus: Sequence[sp.Expr],
) -> NormalizedPacketJumpDecomposition:
    """Separate a finite packet jump into map reset and finite scale revaluation.

    The decomposition is exact with the map reset measured at the new scale:

      Chat+ - Chat-
      = D+^-1 (C+ - C-) D+^-1
        + [D+^-1 C- D+^-1 - D-^-1 C- D-^-1].

    The second term is the finite counterpart of continuous dilation work.
    """
    if len(areas_minus) != len(areas_plus):
        raise ValueError("jump area vectors must have the same length")
    Cminus = packet_covariance_pullback(C0, L_minus)
    Cplus = packet_covariance_pullback(C0, L_plus)
    Chat_minus = normalized_packet_covariance(Cminus, areas_minus)
    Chat_plus = normalized_packet_covariance(Cplus, areas_plus)
    Dpinv = _diag([sp.simplify(1 / a) for a in areas_plus])
    map_reset = sp.simplify(Dpinv * (Cplus - Cminus) * Dpinv)
    scale_revaluation = sp.simplify(
        normalized_packet_covariance(Cminus, areas_plus) - Chat_minus
    )
    return NormalizedPacketJumpDecomposition(
        total=sp.simplify(Chat_plus - Chat_minus),
        map_reset_at_new_scale=map_reset,
        pure_scale_revaluation=scale_revaluation,
    )


def area_frame_qv_matrix(
    grad_omega: Matrix,
    area_frame: Matrix,
    nu: sp.Expr,
) -> sp.Matrix:
    """Raw Kelvin q.v. matrix for three small-loop area vectors.

    Columns h_j are oriented area vectors, not necessarily unit or orthogonal.
    The small-loop coefficient is linear in h_j, so

      Gamma_H = 2 nu H^T (grad omega)(grad omega)^T H.
    """
    if grad_omega.shape != (3, 3) or area_frame.shape != (3, 3):
        raise ValueError("expected 3x3 vorticity gradient and invertible 3x3 area frame")
    return sp.simplify(2 * nu * area_frame.T * grad_omega * grad_omega.T * area_frame)


def area_frame_metric(area_frame: Matrix) -> sp.Matrix:
    """Contravariant packet metric (H^T H)^(-1)."""
    if area_frame.shape != (3, 3):
        raise ValueError("area frame must be 3x3")
    return sp.simplify((area_frame.T * area_frame).inv())


def metric_normalized_packet_bank(C_raw: Matrix, area_frame: Matrix) -> sp.Expr:
    """GL(3)-covariant scalar packet bank 1/2 tr(C_raw (H^T H)^-1)."""
    if C_raw.shape != (3, 3):
        raise ValueError("raw packet covariance must be 3x3")
    M = area_frame_metric(area_frame)
    return sp.simplify(sp.trace(C_raw * M) / 2)


def metric_bulk_reconstruction_residual(
    grad_omega: Matrix,
    area_frame: Matrix,
    nu: sp.Expr,
) -> sp.Expr:
    """Residual of metric-normalized packet payment = nu |grad omega|_F^2."""
    Gamma = area_frame_qv_matrix(grad_omega, area_frame, nu)
    target = nu * sum(grad_omega[i, j] ** 2 for i in range(3) for j in range(3))
    return sp.simplify(metric_normalized_packet_bank(Gamma, area_frame) - target)


def packet_basis_change_invariance_residual(
    C_raw: Matrix,
    area_frame: Matrix,
    L: Matrix,
) -> sp.Expr:
    """Residual under H->HL, C->L^T C L for invertible packet reparameterization."""
    before = metric_normalized_packet_bank(C_raw, area_frame)
    after = metric_normalized_packet_bank(L.T * C_raw * L, area_frame * L)
    return sp.simplify(after - before)


def area_frame_metric_derivative(area_frame: Matrix, area_frame_dot: Matrix) -> sp.Matrix:
    """Exact derivative of M=(H^T H)^(-1)."""
    J = sp.simplify(area_frame.T * area_frame)
    M = sp.simplify(J.inv())
    Jdot = sp.simplify(area_frame_dot.T * area_frame + area_frame.T * area_frame_dot)
    return sp.simplify(-M * Jdot * M)


def metric_normalized_packet_bank_derivative(
    C_raw: Matrix,
    C_raw_dot: Matrix,
    area_frame: Matrix,
    area_frame_dot: Matrix,
) -> sp.Expr:
    """Exact derivative of the metric-normalized scalar packet bank."""
    M = area_frame_metric(area_frame)
    Mdot = area_frame_metric_derivative(area_frame, area_frame_dot)
    return sp.simplify(sp.trace(C_raw_dot * M + C_raw * Mdot) / 2)


def pure_frame_covariance_derivative(C_raw: Matrix, R: Matrix) -> sp.Matrix:
    """Covariance derivative induced only by packet basis motion Hdot=H R."""
    return sp.simplify(R.T * C_raw + C_raw * R)


def pure_frame_bank_derivative_residual(
    C_raw: Matrix,
    area_frame: Matrix,
    R: Matrix,
) -> sp.Expr:
    """Pure invertible packet reparameterization creates zero normalized bank."""
    Hdot = sp.simplify(area_frame * R)
    Cdot = pure_frame_covariance_derivative(C_raw, R)
    return sp.simplify(
        metric_normalized_packet_bank_derivative(C_raw, Cdot, area_frame, Hdot)
    )


def material_area_frame_rhs(grad_u: Matrix, area_frame: Matrix) -> sp.Matrix:
    """Nanson/cofactor kinematics for oriented material area vectors in div-free flow."""
    if grad_u.shape != (3, 3) or area_frame.shape != (3, 3):
        raise ValueError("material area-frame law is 3D")
    return sp.simplify(-grad_u.T * area_frame)


def material_area_log_rate(grad_u: Matrix, normal: Matrix) -> sp.Expr:
    """Logarithmic area rate for a unit material surface normal: -n.S.n."""
    if grad_u.shape != (3, 3) or normal.shape != (3, 1):
        raise ValueError("expected 3x3 velocity gradient and 3-vector normal")
    S = sp.simplify((grad_u + grad_u.T) / 2)
    return sp.simplify(-(normal.T * S * normal)[0])


def local_tensor_packet_covariance(local_tensor: Matrix, area_frame: Matrix) -> sp.Matrix:
    """Raw packet covariance induced by a local physical 2-tensor C_H=H^T T H."""
    if local_tensor.shape != (3, 3) or area_frame.shape != (3, 3):
        raise ValueError("local tensor and area frame must be 3x3")
    return sp.simplify(area_frame.T * local_tensor * area_frame)


def local_tensor_bank_residual(local_tensor: Matrix, area_frame: Matrix) -> sp.Expr:
    """Residual of B_H=1/2 tr(T), independent of invertible packet geometry."""
    Craw = local_tensor_packet_covariance(local_tensor, area_frame)
    return sp.simplify(
        metric_normalized_packet_bank(Craw, area_frame) - sp.trace(local_tensor) / 2
    )


def local_tensor_bank_derivative_residual(
    local_tensor: Matrix,
    local_tensor_dot: Matrix,
    area_frame: Matrix,
    area_frame_dot: Matrix,
) -> sp.Expr:
    """Frame motion cancels exactly: Bdot=1/2 tr(Tdot) for C_H=H^T T H."""
    C = local_tensor_packet_covariance(local_tensor, area_frame)
    Cdot = sp.simplify(
        area_frame_dot.T * local_tensor * area_frame
        + area_frame.T * local_tensor_dot * area_frame
        + area_frame.T * local_tensor * area_frame_dot
    )
    direct = metric_normalized_packet_bank_derivative(C, Cdot, area_frame, area_frame_dot)
    return sp.simplify(direct - sp.trace(local_tensor_dot) / 2)


def metric_amplified_remainder_bank(
    C_raw: Matrix,
    local_tensor: Matrix,
    area_frame: Matrix,
) -> sp.Expr:
    """Normalized capacity carried only by departure from local tensoriality."""
    remainder = sp.simplify(C_raw - local_tensor_packet_covariance(local_tensor, area_frame))
    return metric_normalized_packet_bank(remainder, area_frame)


def isotropic_scale_remainder_law(
    remainder0: Matrix,
    area_frame0: Matrix,
    radius: sp.Expr,
    raw_power: sp.Expr,
) -> sp.Expr:
    """Metric-normalized contribution of R_r=r^p R_0 for H_r=r^2 H_0.

    Exact scaling is r^(p-4) times the reference metric contraction.
    """
    Hr = sp.simplify(radius**2 * area_frame0)
    Rr = sp.simplify(radius**raw_power * remainder0)
    return sp.simplify(metric_normalized_packet_bank(Rr, Hr))


def material_metric_derivative(grad_u: Matrix, area_frame: Matrix) -> sp.Matrix:
    """Physical derivative of M=(H^T H)^-1 under Nanson Hdot=-(grad u)^T H."""
    Hdot = material_area_frame_rhs(grad_u, area_frame)
    return area_frame_metric_derivative(area_frame, Hdot)


def material_metric_logdet_rate(grad_u: Matrix, area_frame: Matrix) -> sp.Expr:
    """Incompressible-specialized d log det M/dt under Hdot=-(grad u)^T H.

    The helper ``material_area_frame_rhs`` is already the div-free Nanson law.
    Within that specialization this expression is 2 div u and therefore zero.
    The general compressible Nanson law instead gives d log det M/dt=-4 div u.
    """
    M = area_frame_metric(area_frame)
    Mdot = material_metric_derivative(grad_u, area_frame)
    return sp.simplify(sp.trace(M.inv() * Mdot))


def material_flux_transport_residual(
    grad_u: Matrix,
    omega: Matrix,
    laplacian_omega: Matrix,
    area_frame: Matrix,
    nu: sp.Expr,
) -> sp.Matrix:
    """Residual of D_t(H^T omega)=nu H^T Delta omega.

    Uses only the exact NS vorticity law D_t omega=(grad u)omega+nu Delta omega
    and Nanson area-frame kinematics.  Vortex stretching cancels from material
    vorticity flux coordinates exactly.
    """
    Hdot = material_area_frame_rhs(grad_u, area_frame)
    Domega = sp.simplify(grad_u * omega + nu * laplacian_omega)
    Dphi = sp.simplify(Hdot.T * omega + area_frame.T * Domega)
    return sp.simplify(Dphi - nu * area_frame.T * laplacian_omega)


def physical_covariance_from_flux(C_flux: Matrix, area_frame: Matrix) -> sp.Matrix:
    """Convert material-flux covariance to physical vorticity covariance."""
    if C_flux.shape != (3, 3) or area_frame.shape != (3, 3):
        raise ValueError("flux covariance and area frame must be 3x3")
    return sp.simplify(area_frame.T.inv() * C_flux * area_frame.inv())


def flux_metric_stretching_work(
    C_flux: Matrix,
    grad_u: Matrix,
    area_frame: Matrix,
) -> sp.Expr:
    """One-half tr(C_flux Mdot), the physical metric-stretching work."""
    Mdot = material_metric_derivative(grad_u, area_frame)
    return sp.simplify(sp.trace(C_flux * Mdot) / 2)


def flux_metric_stretching_residual(
    C_flux: Matrix,
    grad_u: Matrix,
    area_frame: Matrix,
) -> sp.Expr:
    """Residual of metric work = tr(S Sigma_omega)."""
    S = sp.simplify((grad_u + grad_u.T) / 2)
    Sigma = physical_covariance_from_flux(C_flux, area_frame)
    return sp.simplify(flux_metric_stretching_work(C_flux, grad_u, area_frame) - sp.trace(S * Sigma))


def deterministic_flux_stretching_residual(
    omega: Matrix,
    grad_u: Matrix,
    area_frame: Matrix,
) -> sp.Expr:
    """Rank-one flux covariance recovers literal vortex stretching omega.S.omega."""
    phi = sp.simplify(area_frame.T * omega)
    C_flux = sp.simplify(phi * phi.T)
    S = sp.simplify((grad_u + grad_u.T) / 2)
    return sp.simplify(flux_metric_stretching_work(C_flux, grad_u, area_frame) - (omega.T * S * omega)[0])


def metric_packet_bank_rhs(
    C_raw: Matrix,
    Gamma_raw: Matrix,
    W_raw: Matrix,
    area_frame: Matrix,
    area_frame_dot: Matrix,
) -> sp.Expr:
    """Exact scalar packet bank law for Cdot=-Gamma+W and moving packet metric."""
    M = area_frame_metric(area_frame)
    Mdot = area_frame_metric_derivative(area_frame, area_frame_dot)
    return sp.simplify(
        sp.trace((-Gamma_raw + W_raw) * M + C_raw * Mdot) / 2
    )


@dataclass(frozen=True)
class MetricPacketJumpDecomposition:
    total: sp.Expr
    covariance_reset_at_new_metric: sp.Expr
    metric_revaluation: sp.Expr

    @property
    def reconstructed(self) -> sp.Expr:
        return sp.simplify(self.covariance_reset_at_new_metric + self.metric_revaluation)


def metric_packet_jump_decomposition(
    C_minus: Matrix,
    C_plus: Matrix,
    H_minus: Matrix,
    H_plus: Matrix,
) -> MetricPacketJumpDecomposition:
    """Exact finite jump law for the GL(3)-normalized scalar packet bank.

      B+ - B-
      = 1/2 tr((C+-C-) M+)
        + 1/2 tr(C- (M+-M-)).

    A passive basis/scale change makes the two signed pieces cancel exactly.
    """
    Mminus = area_frame_metric(H_minus)
    Mplus = area_frame_metric(H_plus)
    Bminus = sp.trace(C_minus * Mminus) / 2
    Bplus = sp.trace(C_plus * Mplus) / 2
    cov_reset = sp.trace((C_plus - C_minus) * Mplus) / 2
    metric_reval = sp.trace(C_minus * (Mplus - Mminus)) / 2
    return MetricPacketJumpDecomposition(
        total=sp.simplify(Bplus - Bminus),
        covariance_reset_at_new_metric=sp.simplify(cov_reset),
        metric_revaluation=sp.simplify(metric_reval),
    )
