"""Exact vorticity/Kelvin microframe identities for the restart frontier.

This module deliberately stays below norm estimates.  It audits the local physical
mechanisms appearing in the 3D incompressible Navier--Stokes vorticity equation:
vortex stretching, viscous spatial flux, bulk vorticity-gradient dissipation, and
the infinitesimal closed-loop Kelvin quadratic-variation density.

All identities are symbolic/algebraic.  No continuation theorem is asserted here.
"""
from __future__ import annotations

from typing import Sequence

import sympy as sp


Matrix = sp.MatrixBase


def gradient(v: Matrix, coords: Sequence[sp.Symbol]) -> sp.Matrix:
    """Jacobian with vector components as rows and coordinates as columns."""
    return sp.Matrix([[sp.diff(v[i], q) for q in coords] for i in range(len(v))])


def curl3(v: Matrix, coords: Sequence[sp.Symbol]) -> sp.Matrix:
    if len(v) != 3 or len(coords) != 3:
        raise ValueError("curl3 is three-dimensional")
    x, y, z = coords
    return sp.Matrix([
        sp.diff(v[2], y) - sp.diff(v[1], z),
        sp.diff(v[0], z) - sp.diff(v[2], x),
        sp.diff(v[1], x) - sp.diff(v[0], y),
    ])


def laplacian_scalar(f: sp.Expr, coords: Sequence[sp.Symbol]) -> sp.Expr:
    return sp.simplify(sum(sp.diff(f, q, 2) for q in coords))


def laplacian_vector(v: Matrix, coords: Sequence[sp.Symbol]) -> sp.Matrix:
    return sp.Matrix([laplacian_scalar(v[i], coords) for i in range(len(v))])


def strain_tensor(u: Matrix, coords: Sequence[sp.Symbol]) -> sp.Matrix:
    G = gradient(u, coords)
    return sp.simplify((G + G.T) / 2)


def frobenius_square(M: Matrix) -> sp.Expr:
    return sp.simplify(sum(entry * entry for entry in M))


def vorticity_stretching(u: Matrix, coords: Sequence[sp.Symbol]) -> sp.Matrix:
    omega = curl3(u, coords)
    return sp.simplify(strain_tensor(u, coords) * omega)


def vorticity_equation_residual(
    u: Matrix,
    coords: Sequence[sp.Symbol],
    time: sp.Symbol,
    nu: sp.Expr,
) -> sp.Matrix:
    """Residual of D_t omega = S omega + nu Delta omega."""
    omega = curl3(u, coords)
    grad_omega = gradient(omega, coords)
    S = strain_tensor(u, coords)
    return sp.Matrix([
        sp.trigsimp(sp.simplify(
            sp.diff(omega[i], time)
            + (grad_omega * u)[i]
            - (S * omega)[i]
            - nu * laplacian_vector(omega, coords)[i]
        ))
        for i in range(3)
    ])


def enstrophy_density(omega: Matrix) -> sp.Expr:
    return sp.simplify(omega.dot(omega) / 2)


def stretching_power(u: Matrix, coords: Sequence[sp.Symbol]) -> sp.Expr:
    omega = curl3(u, coords)
    return sp.trigsimp(sp.simplify(omega.dot(strain_tensor(u, coords) * omega)))


def kelvin_microframe_density(
    grad_omega: Matrix,
    normal: Matrix,
    nu: sp.Expr,
) -> sp.Expr:
    """Infinitesimal closed-loop Kelvin q.v. density for one disk normal.

    In a constant orthonormal noise frame e_i and for a small oriented disk with
    unit normal n,

        gamma(∂D_r)/|D_r|^2 -> 2 nu |(grad omega)^T n|^2.

    This function returns the exact limiting right-hand side.
    """
    if grad_omega.shape != (3, 3) or normal.shape not in {(3, 1), (3,)}:
        raise ValueError("expected a 3x3 vorticity gradient and a 3-vector normal")
    n = sp.Matrix(normal)
    projected = grad_omega.T * n
    return sp.simplify(2 * nu * projected.dot(projected))


def kelvin_microframe_bulk_dissipation(
    grad_omega: Matrix,
    normals: Sequence[Matrix],
    nu: sp.Expr,
) -> sp.Expr:
    """Half the sum of the three orthonormal-loop q.v. densities."""
    if len(normals) != 3:
        raise ValueError("a 3D Kelvin microframe has three loop normals")
    return sp.simplify(sum(kelvin_microframe_density(grad_omega, n, nu) for n in normals) / 2)



def kelvin_small_disk_action_from_local_gradient(
    grad_omega: Matrix,
    normal: Matrix,
    area: sp.Expr,
    nu: sp.Expr,
) -> sp.Expr:
    """Leading/exact-affine raw Kelvin action for a disk of area ``area``.

    If the directional vorticity gradient is constant across the spanning disk,
    Stokes gives a_i = area * (partial_i omega)·n exactly, hence gamma is area^2
    times the microframe density.  For a smooth field this is the small-disk
    leading term.
    """
    return sp.simplify(area**2 * kelvin_microframe_density(grad_omega, normal, nu))


def normalized_small_disk_action(
    raw_action: sp.Expr, area: sp.Expr
) -> sp.Expr:
    """Convert raw closed-loop q.v. action to area-squared density."""
    return sp.simplify(raw_action / area**2)

def canonical_microframe_bulk_dissipation(grad_omega: Matrix, nu: sp.Expr) -> sp.Expr:
    I = sp.eye(3)
    return kelvin_microframe_bulk_dissipation(grad_omega, [I[:, j] for j in range(3)], nu)


def microframe_reconstruction_residual(grad_omega: Matrix, nu: sp.Expr) -> sp.Expr:
    """Residual of 1/2 sum_j gamma_dens(e_j) = nu |grad omega|_F^2."""
    return sp.simplify(
        canonical_microframe_bulk_dissipation(grad_omega, nu)
        - nu * frobenius_square(grad_omega)
    )


def local_enstrophy_balance_residual(
    u: Matrix,
    coords: Sequence[sp.Symbol],
    time: sp.Symbol,
    nu: sp.Expr,
) -> sp.Expr:
    """Residual of the exact local enstrophy equation.

      (∂t+u·∇) e = omega·S omega + nu Δe - nu |∇omega|^2.
    """
    omega = curl3(u, coords)
    e = enstrophy_density(omega)
    grad_e = sp.Matrix([sp.diff(e, q) for q in coords])
    grad_omega = gradient(omega, coords)
    residual = (
        sp.diff(e, time)
        + u.dot(grad_e)
        - stretching_power(u, coords)
        - nu * laplacian_scalar(e, coords)
        + nu * frobenius_square(grad_omega)
    )
    return sp.trigsimp(sp.simplify(residual))


def amplitude_direction_laplacian_residual(
    rho: sp.Expr,
    xi: Matrix,
    coords: Sequence[sp.Symbol],
) -> sp.Expr:
    """Residual of omega·Δomega = rho Δrho - rho^2 |∇xi|^2 for omega=rho xi.

    The identity is exact when xi·xi=1.  Tests instantiate an exactly unit vector
    field rather than asking SymPy to infer the unit constraint abstractly.
    """
    omega = sp.simplify(rho * xi)
    grad_xi = gradient(xi, coords)
    lhs = sp.simplify(omega.dot(laplacian_vector(omega, coords)))
    rhs = sp.simplify(
        rho * laplacian_scalar(rho, coords)
        - rho**2 * frobenius_square(grad_xi)
    )
    return sp.trigsimp(sp.simplify(lhs - rhs))


def skew_annihilates_vorticity_residual(G: Matrix) -> sp.Matrix:
    """For a 3x3 velocity gradient G, its skew part annihilates curl(u)."""
    if G.shape != (3, 3):
        raise ValueError("expected a 3x3 velocity gradient")
    A = sp.simplify((G - G.T) / 2)
    omega = sp.Matrix([
        G[2, 1] - G[1, 2],
        G[0, 2] - G[2, 0],
        G[1, 0] - G[0, 1],
    ])
    return sp.simplify(A * omega)


def material_line_length_residual(G: Matrix, ell: Matrix) -> sp.Expr:
    """Residual of d|ell|^2/dt = 2 ell·S ell when ell_dot=G ell."""
    if G.shape != (3, 3) or ell.shape not in {(3, 1), (3,)}:
        raise ValueError("expected a 3x3 gradient and a 3-vector material line")
    v = sp.Matrix(ell)
    S = sp.simplify((G + G.T) / 2)
    lhs = sp.simplify(2 * v.dot(G * v))
    rhs = sp.simplify(2 * v.dot(S * v))
    return sp.simplify(lhs - rhs)


def stretching_gate_margin(u: Matrix, coords: Sequence[sp.Symbol], nu: sp.Expr) -> sp.Expr:
    """Stretching minus Kelvin-microframe bulk dissipation.

    At a spatial local maximum of enstrophy e, positive material growth implies
    this margin is strictly positive because nu Δe <= 0.  This is a necessary
    local growth gate, not a continuation criterion.
    """
    omega = curl3(u, coords)
    return sp.trigsimp(sp.simplify(
        stretching_power(u, coords)
        - nu * frobenius_square(gradient(omega, coords))
    ))


def renormalized_bank_derivative(
    V: sp.Expr,
    Vdot: sp.Expr,
    area: sp.Expr,
    area_dot: sp.Expr,
) -> sp.Expr:
    """Exact derivative of V/area^2 under continuous scale motion."""
    return sp.simplify(Vdot / area**2 - 2 * area_dot * V / area**3)


def renormalized_bank_chain_residual(
    V: sp.Expr,
    gamma: sp.Expr,
    covariance_work: sp.Expr,
    area: sp.Expr,
    area_dot: sp.Expr,
) -> sp.Expr:
    """Residual of the area-density bank chain rule.

    If Vdot = -gamma + covariance_work, then

      d(V/A^2) = -gamma/A^2 + covariance_work/A^2
                  - 2 (A_dot/A) (V/A^2).
    """
    Vdot = -gamma + covariance_work
    lhs = renormalized_bank_derivative(V, Vdot, area, area_dot)
    rhs = (
        -gamma / area**2
        + covariance_work / area**2
        - 2 * area_dot / area * (V / area**2)
    )
    return sp.simplify(lhs - rhs)
