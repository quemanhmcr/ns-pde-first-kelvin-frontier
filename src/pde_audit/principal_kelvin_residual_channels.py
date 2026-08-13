"""Pathwise principal-channel laws for the physical weighted Kelvin residual.

The physical line metric M is symmetric positive definite on an invertible coherent
line frame.  Keeping its spectral projectors *inside each realization* gives a
literal directional decomposition that automatically retains random geometry--
residual correlation.  For a simple spectrum, differentiating the moving principal
frame exposes eigenvalue stretch, eigenframe mixing, and residual-content faces.

No support-locality, first-bad, future-bank, restart, continuation, or regularity
claim is made here.
"""
from __future__ import annotations

from collections.abc import Sequence
import sympy as sp

Matrix = sp.MatrixBase


def projector_channel_energy(
    eigenvalue: sp.Expr,
    projector: Matrix,
    residual_second_moment: Matrix,
) -> sp.Expr:
    if projector.shape != residual_second_moment.shape or projector.rows != projector.cols:
        raise ValueError("projector and second moment must be equal square matrices")
    return sp.simplify(eigenvalue * sp.trace(projector * residual_second_moment))


def projector_channel_decomposition_residual(
    metric: Matrix,
    residual_second_moment: Matrix,
    projectors: Sequence[Matrix],
    eigenvalues: Sequence[sp.Expr],
) -> sp.Expr:
    if len(projectors) != len(eigenvalues) or not projectors:
        raise ValueError("one eigenvalue per nonempty projector family is required")
    if metric.shape != residual_second_moment.shape or metric.rows != metric.cols:
        raise ValueError("metric and second moment must be equal square matrices")
    rhs=sum(
        projector_channel_energy(lam,P,residual_second_moment)
        for lam,P in zip(eigenvalues,projectors)
    )
    return sp.simplify(sp.trace(metric*residual_second_moment)-rhs)


def orthogonal_directional_channels(
    principal_frame: Matrix,
    squared_line_scales: Sequence[sp.Expr],
    residual_second_moment: Matrix,
) -> list[sp.Expr]:
    n=principal_frame.rows
    if principal_frame.shape != (n,n) or residual_second_moment.shape != (n,n):
        raise ValueError("principal frame and second moment dimension mismatch")
    if len(squared_line_scales) != n:
        raise ValueError("one squared line scale per direction is required")
    out=[]
    for i,lam in enumerate(squared_line_scales):
        v=principal_frame[:,i]
        out.append(sp.simplify(lam*(v.T*residual_second_moment*v)[0]))
    return out


def two_replica_pathwise_channel_residual(
    principal_frame_1: Matrix,
    eigenvalues_1: Sequence[sp.Expr],
    second_moment_1: Matrix,
    principal_frame_2: Matrix,
    eigenvalues_2: Sequence[sp.Expr],
    second_moment_2: Matrix,
) -> sp.Expr:
    """Equal-weight full-state energy equals equal-weight pathwise channel sums."""
    if principal_frame_1.shape != principal_frame_2.shape:
        raise ValueError("replica principal frames must have equal shape")
    M1=sp.simplify(principal_frame_1*sp.diag(*eigenvalues_1)*principal_frame_1.T)
    M2=sp.simplify(principal_frame_2*sp.diag(*eigenvalues_2)*principal_frame_2.T)
    exact=sp.simplify((sp.trace(M1*second_moment_1)+sp.trace(M2*second_moment_2))/2)
    channels=sp.simplify((
        sum(orthogonal_directional_channels(principal_frame_1,eigenvalues_1,second_moment_1))
        + sum(orthogonal_directional_channels(principal_frame_2,eigenvalues_2,second_moment_2))
    )/2)
    return sp.simplify(exact-channels)


def simple_spectrum_connection(
    metric_rate_in_principal_frame: Matrix,
    eigenvalues: Sequence[sp.Expr],
) -> Matrix:
    """Omega_ij=B_ij/(lambda_j-lambda_i), i!=j, for Vdot=V Omega."""
    n=metric_rate_in_principal_frame.rows
    if metric_rate_in_principal_frame.shape != (n,n) or len(eigenvalues) != n:
        raise ValueError("metric-rate/eigenvalue dimension mismatch")
    Omega=sp.zeros(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                gap=sp.simplify(eigenvalues[j]-eigenvalues[i])
                if gap == 0:
                    raise ValueError("simple-spectrum connection requires distinct eigenvalues; use spectral projector blocks at degeneracy")
                Omega[i,j]=sp.simplify(metric_rate_in_principal_frame[i,j]/gap)
    return sp.simplify(Omega)


def simple_spectrum_connection_skew_residual(
    metric_rate_in_principal_frame: Matrix,
    eigenvalues: Sequence[sp.Expr],
) -> Matrix:
    Omega=simple_spectrum_connection(metric_rate_in_principal_frame,eigenvalues)
    return sp.simplify(Omega+Omega.T)


def principal_metric_rate_reconstruction_residual(
    metric_rate_in_principal_frame: Matrix,
    eigenvalues: Sequence[sp.Expr],
) -> Matrix:
    """B = Lambda_dot + Omega Lambda - Lambda Omega for simple spectrum."""
    n=metric_rate_in_principal_frame.rows
    if metric_rate_in_principal_frame.shape != (n,n) or len(eigenvalues) != n:
        raise ValueError("metric-rate/eigenvalue dimension mismatch")
    Omega=simple_spectrum_connection(metric_rate_in_principal_frame,eigenvalues)
    Lambda=sp.diag(*eigenvalues)
    Lambda_dot=sp.diag(*[metric_rate_in_principal_frame[i,i] for i in range(n)])
    reconstructed=sp.simplify(Lambda_dot+Omega*Lambda-Lambda*Omega)
    return sp.simplify(metric_rate_in_principal_frame-reconstructed)


def principal_second_moment_rate(
    second_moment_in_principal_frame: Matrix,
    physical_second_moment_rate_in_principal_frame: Matrix,
    connection: Matrix,
) -> Matrix:
    """Qtilde_dot=Qdot_0 + [Qtilde,Omega] in the moving eigenframe."""
    if not (
        second_moment_in_principal_frame.shape
        == physical_second_moment_rate_in_principal_frame.shape
        == connection.shape
    ):
        raise ValueError("principal second-moment data must have equal shape")
    return sp.simplify(
        physical_second_moment_rate_in_principal_frame
        + second_moment_in_principal_frame*connection
        - connection*second_moment_in_principal_frame
    )


def principal_channel_rate_faces(
    metric_rate_in_principal_frame: Matrix,
    eigenvalues: Sequence[sp.Expr],
    second_moment_in_principal_frame: Matrix,
    physical_second_moment_rate_in_principal_frame: Matrix,
) -> tuple[list[sp.Expr],list[sp.Expr],list[sp.Expr]]:
    """Return eigenvalue-stretch, content, eigenframe-mixing faces per channel."""
    n=metric_rate_in_principal_frame.rows
    if not (
        metric_rate_in_principal_frame.shape
        == second_moment_in_principal_frame.shape
        == physical_second_moment_rate_in_principal_frame.shape
        == (n,n)
    ) or len(eigenvalues) != n:
        raise ValueError("principal channel-rate dimension mismatch")
    Omega=simple_spectrum_connection(metric_rate_in_principal_frame,eigenvalues)
    comm=sp.simplify(second_moment_in_principal_frame*Omega-Omega*second_moment_in_principal_frame)
    stretch=[]; content=[]; mixing=[]
    for i,lam in enumerate(eigenvalues):
        stretch.append(sp.simplify(metric_rate_in_principal_frame[i,i]*second_moment_in_principal_frame[i,i]))
        content.append(sp.simplify(lam*physical_second_moment_rate_in_principal_frame[i,i]))
        mixing.append(sp.simplify(lam*comm[i,i]))
    return stretch,content,mixing


def principal_channel_rate_sum_residual(
    metric_rate_in_principal_frame: Matrix,
    eigenvalues: Sequence[sp.Expr],
    second_moment_in_principal_frame: Matrix,
    physical_second_moment_rate_in_principal_frame: Matrix,
) -> sp.Expr:
    faces=principal_channel_rate_faces(
        metric_rate_in_principal_frame,eigenvalues,
        second_moment_in_principal_frame,physical_second_moment_rate_in_principal_frame,
    )
    channel_rate=sp.simplify(sum(sum(face) for face in faces))
    direct=sp.simplify(
        sp.trace(metric_rate_in_principal_frame*second_moment_in_principal_frame)
        + sp.trace(sp.diag(*eigenvalues)*physical_second_moment_rate_in_principal_frame)
    )
    return sp.simplify(channel_rate-direct)


def principal_mixing_offdiagonal_residual(
    metric_rate_in_principal_frame: Matrix,
    eigenvalues: Sequence[sp.Expr],
    second_moment_in_principal_frame: Matrix,
) -> sp.Expr:
    n=metric_rate_in_principal_frame.rows
    zero=sp.zeros(n)
    _,_,mixing=principal_channel_rate_faces(
        metric_rate_in_principal_frame,eigenvalues,second_moment_in_principal_frame,zero
    )
    offdiag=sp.Integer(0)
    for i in range(n):
        for j in range(i+1,n):
            offdiag += 2*metric_rate_in_principal_frame[i,j]*second_moment_in_principal_frame[i,j]
    return sp.simplify(sum(mixing)-offdiag)


def degenerate_eigenspace_energy(
    eigenspace_basis: Matrix,
    eigenvalue: sp.Expr,
    residual_second_moment: Matrix,
) -> sp.Expr:
    """Canonical energy of a degenerate eigenspace, independent of its basis."""
    if eigenspace_basis.rows != residual_second_moment.rows or residual_second_moment.rows != residual_second_moment.cols:
        raise ValueError("eigenspace basis/second moment dimension mismatch")
    return sp.simplify(eigenvalue*sp.trace(eigenspace_basis.T*residual_second_moment*eigenspace_basis))


def degenerate_basis_rotation_residual(
    eigenspace_basis: Matrix,
    internal_rotation: Matrix,
    eigenvalue: sp.Expr,
    residual_second_moment: Matrix,
) -> sp.Expr:
    if internal_rotation.rows != internal_rotation.cols or eigenspace_basis.cols != internal_rotation.rows:
        raise ValueError("internal rotation/eigenspace dimension mismatch")
    before=degenerate_eigenspace_energy(eigenspace_basis,eigenvalue,residual_second_moment)
    after=degenerate_eigenspace_energy(sp.simplify(eigenspace_basis*internal_rotation),eigenvalue,residual_second_moment)
    return sp.simplify(after-before)


def reverse_linear_shear_metric_rate(
    shear_rate: sp.Expr,
    diagonal_line_frame: Matrix,
) -> Matrix:
    """Exact NS shear u=(gamma y,0,0): Mdot=-L^T(A^T+A)L."""
    if diagonal_line_frame.shape != (3,3):
        raise ValueError("linear shear calibration is 3D")
    A=sp.Matrix([[0,shear_rate,0],[0,0,0],[0,0,0]])
    return sp.simplify(-diagonal_line_frame.T*(A.T+A)*diagonal_line_frame)
