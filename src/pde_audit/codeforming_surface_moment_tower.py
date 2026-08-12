"""Exact scale/shape and co-deforming laws for the material-surface moment tower.

The physical surface is kept literal.  A local reverse-age line frame L obeys
L_dot=-A(X)L.  Pulling relative position and oriented area back by

    xi = L^{-1} r,
    a_tilde = cof(L)^{-1} a,

removes the entire local affine deformation.  The residual shape dynamics is
carried by the single codeforming nonaffinity field

    N_L(xi)=L^{-1}[u(X+L xi)-u(X)-A(X)L xi].

For incompressible u, div_xi N_L=0 and

    xi_dot=-N_L,
    a_tilde_dot=(D_xi N_L)^T a_tilde.

Thus the full pulled-back oriented moment tower is transported by one residual
incompressible vector field.  No moment closure or norm estimate is used.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence

import sympy as sp

from .surface_moment_hierarchy import Exponent, monomial

Matrix = sp.MatrixBase


def cofactor_map(linear_map: Matrix) -> sp.Matrix:
    """cof J = det(J) J^{-T}, the oriented-area action of a linear map."""
    if linear_map.rows != linear_map.cols:
        raise ValueError("linear map must be square")
    return sp.simplify(sp.det(linear_map) * linear_map.inv().T)


def oriented_moment_linear_pushforward(
    moments: Mapping[Exponent, Matrix],
    exponent: Exponent,
    linear_map: Matrix,
    coords: Sequence[sp.Symbol],
) -> Matrix:
    """Exact pushforward of M_alpha=int r^alpha a under r+=Jr, a+=cof(J)a.

    General J mixes monomials of the same total order, so every required same-order
    moment must be supplied explicitly.  Missing moment is not interpreted as zero.
    """
    n = len(coords)
    if linear_map.shape != (n, n) or len(exponent) != n:
        raise ValueError("dimension mismatch")
    r = sp.Matrix(coords)
    transformed = sp.simplify(linear_map * r)
    poly = sp.Poly(sp.expand(monomial(transformed, exponent)), *coords)
    out = sp.zeros(n, 1)
    for powers, coeff in poly.terms():
        beta = tuple(int(q) for q in powers)
        if beta not in moments:
            raise KeyError(f"missing oriented moment {beta}")
        M = moments[beta]
        if M.shape != (n, 1):
            raise ValueError("oriented moments must be spatial column vectors")
        out += coeff * M
    return sp.simplify(cofactor_map(linear_map) * out)


def scalar_normalized_oriented_moments(
    moments: Mapping[Exponent, Matrix],
    scale: sp.Expr,
) -> dict[Exponent, Matrix]:
    """hat M_alpha=M_alpha/scale^(|alpha|+2), forced by line+area scaling."""
    return {
        alpha: sp.simplify(M / scale ** (sum(alpha) + 2))
        for alpha, M in moments.items()
    }


def scalar_normalized_refinement_residual(
    moments: Mapping[Exponent, Matrix],
    exponent: Exponent,
    refinement: Matrix,
    scale_old: sp.Expr,
    scale_factor: sp.Expr,
    coords: Sequence[sp.Symbol],
) -> Matrix:
    """Residual proving that scalar scale cancels and only unit-det shape acts.

    Caller supplies d=scale_factor with det(refinement)=d^n.  For 3D oriented
    surfaces M scales with d^(m+2), hence

      M_+/(d rho)^(m+2) = push_{S}(M_-/rho^(m+2)), S=R/d.
    """
    n = len(coords)
    if n != 3 or refinement.shape != (3, 3):
        raise ValueError("current theorem is the 3D surface law")
    pushed = oriented_moment_linear_pushforward(moments, exponent, refinement, coords)
    lhs = sp.simplify(pushed / (scale_factor * scale_old) ** (sum(exponent) + 2))
    normalized = scalar_normalized_oriented_moments(moments, scale_old)
    shape = sp.simplify(refinement / scale_factor)
    rhs = oriented_moment_linear_pushforward(normalized, exponent, shape, coords)
    return sp.simplify(lhs - rhs)


def codeforming_oriented_moment(
    moments: Mapping[Exponent, Matrix],
    exponent: Exponent,
    line_frame: Matrix,
    coords: Sequence[sp.Symbol],
) -> Matrix:
    """Pulled-back moment in xi=L^-1 r and a~=cof(L)^-1 a coordinates."""
    return oriented_moment_linear_pushforward(
        moments, exponent, sp.simplify(line_frame.inv()), coords
    )


def scale_shape_codeforming_residual(
    moments: Mapping[Exponent, Matrix],
    exponent: Exponent,
    line_frame: Matrix,
    scale: sp.Expr,
    coords: Sequence[sp.Symbol],
) -> Matrix:
    """Residual: full L pullback = unit-det-shape pullback after scalar normalization."""
    full = codeforming_oriented_moment(moments, exponent, line_frame, coords)
    normalized = scalar_normalized_oriented_moments(moments, scale)
    shape = sp.simplify(line_frame / scale)
    shaped = oriented_moment_linear_pushforward(
        normalized, exponent, sp.simplify(shape.inv()), coords
    )
    return sp.simplify(full - shaped)


def codeforming_nonaffinity_field(
    velocity_difference: Matrix,
    grad_u_anchor: Matrix,
    physical_relative_coords: Sequence[sp.Symbol],
    line_frame: Matrix,
    codeforming_coords: Sequence[sp.Symbol],
) -> Matrix:
    """N_L=L^-1[Delta u(L xi)-A0 L xi], the literal nonaffine relative velocity."""
    n = len(physical_relative_coords)
    if (
        velocity_difference.shape != (n, 1)
        or grad_u_anchor.shape != (n, n)
        or line_frame.shape != (n, n)
        or len(codeforming_coords) != n
    ):
        raise ValueError("dimension mismatch")
    r = sp.Matrix(physical_relative_coords)
    xi = sp.Matrix(codeforming_coords)
    residual = sp.simplify(velocity_difference - grad_u_anchor * r)
    substitution = {physical_relative_coords[i]: (line_frame * xi)[i] for i in range(n)}
    return sp.simplify(line_frame.inv() * residual.subs(substitution))


def codeforming_gradient_residual(
    grad_u_profile: Matrix,
    grad_u_anchor: Matrix,
    physical_relative_coords: Sequence[sp.Symbol],
    line_frame: Matrix,
    codeforming_coords: Sequence[sp.Symbol],
) -> Matrix:
    """Pulled-back area connection C^-1[A(r)-A0]^T C."""
    n = len(physical_relative_coords)
    if grad_u_profile.shape != (n, n) or grad_u_anchor.shape != (n, n):
        raise ValueError("gradient dimension mismatch")
    xi = sp.Matrix(codeforming_coords)
    substitution = {physical_relative_coords[i]: (line_frame * xi)[i] for i in range(n)}
    delta_A = sp.simplify((grad_u_profile - grad_u_anchor).subs(substitution))
    C = cofactor_map(line_frame)
    return sp.simplify(C.inv() * delta_A.T * C)


def codeforming_nonaffinity_geometry_residual(
    velocity_difference: Matrix,
    grad_u_profile: Matrix,
    grad_u_anchor: Matrix,
    physical_relative_coords: Sequence[sp.Symbol],
    line_frame: Matrix,
    codeforming_coords: Sequence[sp.Symbol],
) -> Matrix:
    """Residual C^-1 DeltaA^T C - (D_xi N_L)^T."""
    N = codeforming_nonaffinity_field(
        velocity_difference,
        grad_u_anchor,
        physical_relative_coords,
        line_frame,
        codeforming_coords,
    )
    area_connection = codeforming_gradient_residual(
        grad_u_profile,
        grad_u_anchor,
        physical_relative_coords,
        line_frame,
        codeforming_coords,
    )
    return sp.simplify(area_connection - N.jacobian(codeforming_coords).T)


def codeforming_nonaffinity_divergence(
    nonaffinity: Matrix,
    codeforming_coords: Sequence[sp.Symbol],
) -> sp.Expr:
    """div_xi N_L; zero for incompressible Delta u-A0 r."""
    if nonaffinity.shape != (len(codeforming_coords), 1):
        raise ValueError("dimension mismatch")
    return sp.simplify(
        sum(sp.diff(nonaffinity[i], codeforming_coords[i]) for i in range(len(codeforming_coords)))
    )


def codeforming_nonaffinity_one_form(
    nonaffinity: Matrix,
    line_frame: Matrix,
) -> Matrix:
    """beta_N=(L^T L)N, the codeforming residual momentum one-form coefficients.

    If the physical residual velocity is n(r)=L N(xi) and dr=L dxi, then
    n.dr = beta_N.dxi exactly.  Kinematic N and Kelvin one-form beta_N are
    therefore distinct physical faces of the same nonaffinity.
    """
    if line_frame.rows != line_frame.cols or nonaffinity.shape != (line_frame.rows, 1):
        raise ValueError("dimension mismatch")
    return sp.simplify(line_frame.T * line_frame * nonaffinity)


def codeforming_residual_one_form_pullback_residual(
    physical_residual_velocity: Matrix,
    physical_relative_coords: Sequence[sp.Symbol],
    line_frame: Matrix,
    codeforming_coords: Sequence[sp.Symbol],
) -> Matrix:
    """Residual L^T n(Lxi) - (L^T L)N_L for a purely nonaffine residual n."""
    n = len(physical_relative_coords)
    zero_A = sp.zeros(n)
    N = codeforming_nonaffinity_field(
        physical_residual_velocity, zero_A, physical_relative_coords, line_frame, codeforming_coords
    )
    xi = sp.Matrix(codeforming_coords)
    substitution = {physical_relative_coords[i]: (line_frame * xi)[i] for i in range(n)}
    pulled_one_form = sp.simplify(line_frame.T * physical_residual_velocity.subs(substitution))
    return sp.simplify(pulled_one_form - codeforming_nonaffinity_one_form(N, line_frame))


def curl3(field: Matrix, coords: Sequence[sp.Symbol]) -> Matrix:
    """Three-dimensional curl of one-form coefficient/vector components."""
    if field.shape != (3, 1) or len(coords) != 3:
        raise ValueError("curl3 is three-dimensional")
    x, y, z = coords
    return sp.Matrix([
        sp.diff(field[2], y) - sp.diff(field[1], z),
        sp.diff(field[0], z) - sp.diff(field[2], x),
        sp.diff(field[1], x) - sp.diff(field[0], y),
    ])


def pulledback_vorticity_defect(
    vorticity_profile: Matrix,
    vorticity_anchor: Matrix,
    physical_relative_coords: Sequence[sp.Symbol],
    line_frame: Matrix,
    codeforming_coords: Sequence[sp.Symbol],
) -> Matrix:
    """cof(L)^T[omega(X+Lxi)-omega(X)], the Stokes-compatible flux pullback."""
    if vorticity_profile.shape != (3, 1) or vorticity_anchor.shape != (3, 1):
        raise ValueError("vorticity pullback is three-dimensional")
    xi = sp.Matrix(codeforming_coords)
    substitution = {physical_relative_coords[i]: (line_frame * xi)[i] for i in range(3)}
    delta = sp.simplify((vorticity_profile - vorticity_anchor).subs(substitution))
    return sp.simplify(cofactor_map(line_frame).T * delta)


def codeforming_anchor_one_form_derivative(
    kelvin_one_form: Matrix,
    anchor_coordinate: sp.Symbol,
) -> Matrix:
    """Partial_X beta_L with line frame and codeforming shape held fixed.

    On the literal full reverse-age state L and relative shape are finite-variation
    coordinates, so this is the martingale-direction derivative of the Kelvin
    residual one-form.
    """
    return sp.simplify(kelvin_one_form.diff(anchor_coordinate))


def codeforming_descent_error_drift(
    pulled_local_vorticity: Matrix,
    codeforming_total_area_rate: Matrix,
) -> sp.Expr:
    """-eta_0 . htilde_dot, equal to -omega(X).R_A in physical coordinates."""
    if pulled_local_vorticity.shape != codeforming_total_area_rate.shape:
        raise ValueError("vorticity and area-rate dimensions must match")
    return sp.simplify(-(pulled_local_vorticity.T * codeforming_total_area_rate)[0])


def codeforming_kelvin_curl_residual(
    nonaffinity: Matrix,
    line_frame: Matrix,
    codeforming_coords: Sequence[sp.Symbol],
    pulled_vorticity_defect: Matrix,
) -> Matrix:
    """Residual curl_xi[(L^T L)N_L]-cof(L)^T delta omega."""
    beta = codeforming_nonaffinity_one_form(nonaffinity, line_frame)
    return sp.simplify(curl3(beta, codeforming_coords) - pulled_vorticity_defect)


def codeforming_oriented_moment_rate_integrand(
    codeforming_relative: Matrix,
    codeforming_area: Matrix,
    nonaffinity: Matrix,
    exponent: Exponent,
) -> Matrix:
    """Exact pulled-back moment rate under xi_dot=-N, a~_dot=(D N)^T a~."""
    if codeforming_relative.cols != 1 or codeforming_area.shape != codeforming_relative.shape:
        raise ValueError("relative and area coordinates must be equal column vectors")
    n = codeforming_relative.rows
    if nonaffinity.shape != (n, 1) or len(exponent) != n:
        raise ValueError("dimension mismatch")
    coords = tuple(codeforming_relative)
    base = monomial(codeforming_relative, exponent)
    out = sp.simplify(base * nonaffinity.jacobian(coords).T * codeforming_area)
    for i, power in enumerate(exponent):
        if power == 0:
            continue
        beta = list(exponent)
        beta[i] -= 1
        out -= power * monomial(codeforming_relative, tuple(beta)) * nonaffinity[i] * codeforming_area
    return sp.simplify(out)


def codeforming_generating_current_integrand(
    codeforming_relative: Matrix,
    codeforming_area: Matrix,
    theta: Matrix,
) -> Matrix:
    """e^{theta.xi} a~, whose theta derivatives contain the entire moment tower."""
    if theta.shape != codeforming_relative.shape or codeforming_area.shape != codeforming_relative.shape:
        raise ValueError("all generating-current vectors must have the same dimension")
    return sp.simplify(sp.exp((theta.T * codeforming_relative)[0]) * codeforming_area)


def codeforming_generating_current_rate_integrand(
    codeforming_relative: Matrix,
    codeforming_area: Matrix,
    theta: Matrix,
    nonaffinity: Matrix,
) -> Matrix:
    """Exact entire-tower law e^{theta.xi}[(DN)^T-(theta.N)I]a~."""
    n = codeforming_relative.rows
    if any(v.shape != (n, 1) for v in (codeforming_area, theta, nonaffinity)):
        raise ValueError("dimension mismatch")
    coords = tuple(codeforming_relative)
    pref = sp.exp((theta.T * codeforming_relative)[0])
    return sp.simplify(
        pref
        * (
            nonaffinity.jacobian(coords).T
            - (theta.T * nonaffinity)[0] * sp.eye(n)
        )
        * codeforming_area
    )


def coherent_refinement_codeforming_moment_residual(
    moments: Mapping[Exponent, Matrix],
    exponent: Exponent,
    line_frame: Matrix,
    refinement: Matrix,
    coords: Sequence[sp.Symbol],
) -> Matrix:
    """Exact invariance when surface and local frame undergo the same coherent refinement.

    Physical map between old/new surfaces is P=L R L^-1, while L+=L R.
    """
    P = sp.simplify(line_frame * refinement * line_frame.inv())
    same_order = {
        alpha: oriented_moment_linear_pushforward(moments, alpha, P, coords)
        for alpha in moments
    }
    before = codeforming_oriented_moment(moments, exponent, line_frame, coords)
    after = codeforming_oriented_moment(
        same_order, exponent, sp.simplify(line_frame * refinement), coords
    )
    return sp.simplify(after - before)


def codeforming_homogeneous_scale_shape_residual(
    physical_homogeneous_residual: Matrix,
    degree: int,
    physical_relative_coords: Sequence[sp.Symbol],
    scale: sp.Expr,
    unit_det_shape: Matrix,
    codeforming_coords: Sequence[sp.Symbol],
) -> Matrix:
    """Residual N_{rho S}=rho^(p-1) S^-1 U_p(S xi) for homogeneous degree p.

    This exposes the exact scalar power and the independent anisotropy conjugation.
    The scalar factor rho^(p-1) alone is therefore not the full nonaffinity size.
    """
    if degree < 2:
        raise ValueError("nonaffine homogeneous degree must be at least two")
    n = len(physical_relative_coords)
    L = sp.simplify(scale * unit_det_shape)
    zero_A = sp.zeros(n)
    lhs = codeforming_nonaffinity_field(
        physical_homogeneous_residual,
        zero_A,
        physical_relative_coords,
        L,
        codeforming_coords,
    )
    xi = sp.Matrix(codeforming_coords)
    substitution = {
        physical_relative_coords[i]: (unit_det_shape * xi)[i]
        for i in range(n)
    }
    rhs = sp.simplify(
        scale ** (degree - 1)
        * unit_det_shape.inv()
        * physical_homogeneous_residual.subs(substitution, simultaneous=True)
    )
    return sp.simplify(lhs - rhs)


def codeforming_homogeneous_jet_refinement_residual(
    physical_homogeneous_residual: Matrix,
    physical_relative_coords: Sequence[sp.Symbol],
    line_frame: Matrix,
    refinement: Matrix,
    codeforming_coords: Sequence[sp.Symbol],
) -> Matrix:
    """Tensorial reparameterization N_{LR}(xi)=R^-1 N_L(R xi) for a fixed physical jet."""
    n = len(physical_relative_coords)
    zero_A = sp.zeros(n)
    N_LR = codeforming_nonaffinity_field(
        physical_homogeneous_residual,
        zero_A,
        physical_relative_coords,
        sp.simplify(line_frame * refinement),
        codeforming_coords,
    )
    N_L = codeforming_nonaffinity_field(
        physical_homogeneous_residual,
        zero_A,
        physical_relative_coords,
        line_frame,
        codeforming_coords,
    )
    xi = sp.Matrix(codeforming_coords)
    sub = {codeforming_coords[i]: (refinement * xi)[i] for i in range(n)}
    rhs = sp.simplify(refinement.inv() * N_L.subs(sub, simultaneous=True))
    return sp.simplify(N_LR - rhs)
