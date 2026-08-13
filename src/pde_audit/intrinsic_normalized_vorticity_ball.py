"""Intrinsic normalized-vorticity unit-ball contact grammar.

Let M(t)=max_x |omega|^2/2>0 and W=sqrt(2M)=||omega||_infty.  The
similarity-neutral normalized vorticity

    V = omega / W

maps physical space into the closed Euclidean unit ball.  At times when the max
envelope M is differentiable it satisfies the literal normalized vorticity equation

    D_t V = (grad u)V + nu Delta V - mu V,    mu=Wdot/W=Mdot/(2M).

The previous scalar localization field is only its squared radius, g=|V|^2.  At
an active maximum |V|=1, define

    Q = -Hess |V|^2,
    G_R = (grad V)^T grad V,
    H_c = -[V dot partial_ij V].

Then exactly

    H_c = G_R + Q/2.

Both Q and G_R are positive semidefinite at an active maximum, so the contact
form H_c is positive semidefinite and

    ker H_c = ker Q intersect ker(grad V).

Thus a scalar-curvature-flat direction is not physically flat when normalized
vorticity still moves tangentially along the unit sphere.  The left Gram
G_L=(grad V)(grad V)^T is exactly the orientation-complete Kelvin q.v. tensor
after division by 4 nu M.  No new stochastic source or external score is added.

No first-bad identification, support-collapse theorem, restart, continuation, or
regularity theorem is asserted here.
"""
from __future__ import annotations

from collections.abc import Sequence
import sympy as sp

from .first_bad_candidate_exclusions import curl3, gradient, laplacian, navier_stokes_residual
from .orientation_packet import orientation_qv_matrix, packet_bulk_payment

Matrix = sp.MatrixBase


def normalized_vorticity(omega: Matrix, vorticity_scale: sp.Expr) -> Matrix:
    """V=omega/W for a positive time-only vorticity scale W."""
    return sp.simplify(omega / vorticity_scale)


def normalized_enstrophy(normalized_omega: Matrix) -> sp.Expr:
    """g=|V|^2=e/M."""
    return sp.simplify(normalized_omega.dot(normalized_omega))


def normalized_vorticity_pde_residual(
    velocity: Matrix,
    normalized_omega: Matrix,
    coords: Sequence[sp.Symbol],
    time: sp.Symbol,
    nu: sp.Expr,
    log_scale_rate: sp.Expr,
) -> Matrix:
    """Residual of D_t V=(grad u)V+nu Delta V-mu V."""
    A = gradient(velocity, coords)
    J = gradient(normalized_omega, coords)
    material = sp.simplify(sp.diff(normalized_omega, time) + J * velocity)
    rhs = sp.simplify(A * normalized_omega + nu * laplacian(normalized_omega, coords) - log_scale_rate * normalized_omega)
    return sp.simplify(material - rhs)


def normalized_gradient_right_gram(normalized_omega: Matrix, coords: Sequence[sp.Symbol]) -> Matrix:
    """Domain-direction Gram G_R=(grad V)^T grad V."""
    J = gradient(normalized_omega, coords)
    return sp.simplify(J.T * J)


def normalized_gradient_left_gram(normalized_omega: Matrix, coords: Sequence[sp.Symbol]) -> Matrix:
    """Range/orientation Gram G_L=(grad V)(grad V)^T."""
    J = gradient(normalized_omega, coords)
    return sp.simplify(J * J.T)


def normalized_scalar_curvature(normalized_omega: Matrix, coords: Sequence[sp.Symbol]) -> Matrix:
    """Q=-Hess |V|^2, positive semidefinite at an active maximum."""
    return sp.simplify(-sp.hessian(normalized_enstrophy(normalized_omega), coords))


def radial_second_derivative_form(normalized_omega: Matrix, coords: Sequence[sp.Symbol]) -> Matrix:
    """R_ij=V dot partial_ij V."""
    d = len(coords)
    if normalized_omega.shape != (d, 1):
        raise ValueError("normalized vorticity and coordinate dimensions must match")
    out = sp.zeros(d)
    for i, qi in enumerate(coords):
        for j, qj in enumerate(coords):
            out[i, j] = sp.simplify((normalized_omega.T * normalized_omega.diff(qi, qj))[0])
    return out


def unit_ball_contact_form(normalized_omega: Matrix, coords: Sequence[sp.Symbol]) -> Matrix:
    """H_c=-R, the inward radial second-contact form with the unit sphere."""
    return sp.simplify(-radial_second_derivative_form(normalized_omega, coords))


def unit_ball_contact_identity_residual(normalized_omega: Matrix, coords: Sequence[sp.Symbol]) -> Matrix:
    """Residual H_c-G_R-Q/2; identically zero for every smooth V."""
    Hc = unit_ball_contact_form(normalized_omega, coords)
    Gr = normalized_gradient_right_gram(normalized_omega, coords)
    Q = normalized_scalar_curvature(normalized_omega, coords)
    return sp.simplify(Hc - Gr - Q / 2)


def boundary_tangency_identity_residual(normalized_omega: Matrix, coords: Sequence[sp.Symbol]) -> Matrix:
    """Residual (grad V)^T V - grad(|V|^2)/2; identically zero."""
    J = gradient(normalized_omega, coords)
    g = normalized_enstrophy(normalized_omega)
    grad_g = sp.Matrix([sp.diff(g, q) for q in coords])
    return sp.simplify(J.T * normalized_omega - grad_g / 2)


def directional_contact_split_residual(
    contact_form: Matrix,
    right_gram: Matrix,
    scalar_curvature: Matrix,
    direction: Matrix,
) -> sp.Expr:
    """Residual xi^T H_c xi-|J xi|^2-(1/2)xi^T Q xi."""
    if direction.cols != 1:
        raise ValueError("direction must be a column vector")
    lhs = (direction.T * contact_form * direction)[0]
    rhs = (direction.T * right_gram * direction)[0] + (direction.T * scalar_curvature * direction)[0] / 2
    return sp.simplify(lhs - rhs)


def left_right_gram_trace_residual(normalized_omega: Matrix, coords: Sequence[sp.Symbol]) -> sp.Expr:
    """Left and right gradient Grams carry the same Frobenius/Kelvin bulk trace."""
    return sp.simplify(
        sp.trace(normalized_gradient_left_gram(normalized_omega, coords))
        - sp.trace(normalized_gradient_right_gram(normalized_omega, coords))
    )


def normalized_kelvin_left_gram_residual(
    grad_omega: Matrix,
    max_enstrophy: sp.Expr,
    normalized_left_gram: Matrix,
    nu: sp.Expr,
) -> Matrix:
    """Gamma_I=4 nu M G_L for the canonical orientation-complete Kelvin frame."""
    Gamma = orientation_qv_matrix(grad_omega, sp.eye(3), nu)
    return sp.simplify(Gamma - 4 * nu * max_enstrophy * normalized_left_gram)


def normalized_kelvin_bulk_trace_residual(
    grad_omega: Matrix,
    max_enstrophy: sp.Expr,
    normalized_right_gram: Matrix,
    nu: sp.Expr,
) -> sp.Expr:
    """Kelvin bulk payment equals 2 nu M tr(G_R)."""
    Gamma = orientation_qv_matrix(grad_omega, sp.eye(3), nu)
    return sp.simplify(packet_bulk_payment(Gamma) - 2 * nu * max_enstrophy * sp.trace(normalized_right_gram))


def elliptic_polarization_heat_shear_velocity(
    amplitude: sp.Expr,
    beta: sp.Expr,
    mode: sp.Expr,
    z: sp.Expr,
    time: sp.Expr,
    nu: sp.Expr,
) -> Matrix:
    """Exact periodic heat shear interpolating linear and circular polarization."""
    decay = sp.exp(-nu * mode**2 * time)
    return sp.Matrix([
        -beta * amplitude * sp.cos(mode * z) * decay / mode,
        -amplitude * sp.sin(mode * z) * decay / mode,
        0,
    ])


def elliptic_polarization_contact_calibration(
    amplitude: sp.Expr,
    beta: sp.Expr,
    mode: sp.Expr,
    coords: tuple[sp.Symbol, sp.Symbol, sp.Symbol],
    time: sp.Symbol,
    nu: sp.Expr,
) -> dict[str, sp.Expr | Matrix]:
    """Exact NS family transferring geometry between amplitude curvature and orientation twist.

    For 0<=beta<=1 the normalized vorticity is

        V=(cos(kz), beta sin(kz), 0),

    so |V|<=1.  At z=0,

        G_R,zz=beta^2 k^2,
        Q_zz=2(1-beta^2)k^2,
        H_c,zz=k^2.

    beta=1 is a circular/helical endpoint with g identically one: every scalar
    spatial jet vanishes although the Kelvin gradient/contact channel remains nonzero.
    """
    x, y, z = coords
    u = elliptic_polarization_heat_shear_velocity(amplitude, beta, mode, z, time, nu)
    omega = sp.simplify(curl3(u, coords))
    decay = sp.exp(-nu * mode**2 * time)
    W = sp.simplify(amplitude * decay)
    M = sp.simplify(W**2 / 2)
    V = normalized_vorticity(omega, W)
    g = sp.simplify(sp.trigsimp(normalized_enstrophy(V)))
    J = gradient(V, coords)
    Gr = normalized_gradient_right_gram(V, coords)
    Gl = normalized_gradient_left_gram(V, coords)
    Q = normalized_scalar_curvature(V, coords)
    Hc = unit_ball_contact_form(V, coords)
    point = {x: 0, y: 0, z: 0}
    mu = sp.simplify(sp.diff(W, time) / W)
    grad_omega = gradient(omega, coords)
    scalar_source = sp.simplify(sp.diff(g, time) + (sp.Matrix([sp.diff(g, q) for q in coords]).T * u)[0])
    return {
        "velocity": u,
        "vorticity": omega,
        "vorticity_scale": W,
        "max_enstrophy": M,
        "normalized_vorticity": V,
        "normalized_enstrophy": g,
        "unit_ball_gap": sp.simplify(1 - g),
        "unit_ball_gap_factor_residual": sp.simplify(1 - g - (1 - beta**2) * sp.sin(mode * z) ** 2),
        "log_scale_rate": mu,
        "normalized_vorticity_pde_residual": normalized_vorticity_pde_residual(u, V, coords, time, nu, mu),
        "ns_residual": sp.simplify(navier_stokes_residual(u, 0, coords, time, nu)),
        "scalar_source": scalar_source,
        "tangency_identity_residual": boundary_tangency_identity_residual(V, coords),
        "contact_identity_residual": unit_ball_contact_identity_residual(V, coords),
        "right_gram": sp.simplify(Gr.subs(point)),
        "left_gram": sp.simplify(Gl.subs(point)),
        "scalar_curvature": sp.simplify(Q.subs(point)),
        "contact_form": sp.simplify(Hc.subs(point)),
        "polarization_transfer_residual": sp.simplify(Hc[2, 2].subs(point) - Gr[2, 2].subs(point) - Q[2, 2].subs(point) / 2),
        "contact_frequency_residual": sp.simplify(Hc[2, 2].subs(point) - mode**2),
        "gram_trace_residual": left_right_gram_trace_residual(V, coords),
        "kelvin_left_gram_residual": normalized_kelvin_left_gram_residual(grad_omega, M, Gl, nu),
        "kelvin_bulk_trace_residual": normalized_kelvin_bulk_trace_residual(grad_omega, M, Gr, nu),
        "kelvin_bulk": sp.simplify(nu * sum(grad_omega[i, j] ** 2 for i in range(3) for j in range(3))),
        "normalized_gradient": J,
    }
