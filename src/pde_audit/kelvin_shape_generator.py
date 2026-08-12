"""Exact common-noise Kelvin current-shape generator identities.

The physical backward stochastic Kelvin flow uses one *uniform* Brownian motion for
all points of a material current.  Consequently, after choosing one material anchor
X and relative shape coordinates R_p=X_p-X, the Brownian increment lives only in X:
the relative shape has finite variation.  This module records that exact algebra and
the finite-surface obstruction to replacing the whole shape by one area frame H.

No continuation or regularity statement is made here.
"""
from __future__ import annotations

from typing import Sequence

import sympy as sp

Matrix = sp.MatrixBase


def common_wiener_covariance(point_count: int, dim: int, nu: sp.Expr) -> sp.Matrix:
    """Covariance 2 nu (1 1^T) tensor I for points driven by one common Wiener motion."""
    if point_count <= 0 or dim <= 0:
        raise ValueError("point_count and dim must be positive")
    return sp.simplify(2 * nu * sp.kronecker_product(sp.ones(point_count), sp.eye(dim)))


def anchor_relative_transform(relative_count: int, dim: int) -> sp.Matrix:
    """Linear map (X,X_1,...,X_N) -> (X,R_1,...,R_N), R_p=X_p-X."""
    if relative_count <= 0 or dim <= 0:
        raise ValueError("relative_count and dim must be positive")
    points = relative_count + 1
    T = sp.zeros(points * dim)
    I = sp.eye(dim)
    T[:dim, :dim] = I
    for p in range(relative_count):
        row = (p + 1) * dim
        col = (p + 1) * dim
        T[row : row + dim, :dim] = -I
        T[row : row + dim, col : col + dim] = I
    return T


def anchor_relative_common_noise_covariance(relative_count: int, dim: int, nu: sp.Expr) -> sp.Matrix:
    """Common-noise covariance in anchor/relative coordinates.

    The only nonzero block is the anchor covariance 2 nu I.  Every relative-shape
    coordinate has zero martingale covariance, including cross-covariance with X.
    """
    A = common_wiener_covariance(relative_count + 1, dim, nu)
    T = anchor_relative_transform(relative_count, dim)
    return sp.simplify(T * A * T.T)


def common_noise_backward_generator(
    observable: sp.Expr,
    velocities: Sequence[Matrix],
    point_coords: Sequence[Sequence[sp.Symbol]],
    nu: sp.Expr,
) -> sp.Expr:
    """Backward-Itô generator for points sharing one additive Brownian motion.

      K^- F = sum_p u(X_p).grad_p F - nu sum_{p,q} grad_p.grad_q F.

    The second-order cross terms are mandatory: the points do not have independent
    noises.  This is the finite-cylinder form of the full current-shape generator.
    """
    if len(velocities) != len(point_coords) or not point_coords:
        raise ValueError("one velocity and coordinate block per point are required")
    dim = len(point_coords[0])
    if any(len(c) != dim for c in point_coords):
        raise ValueError("all point coordinate blocks must have the same dimension")
    if any(v.shape != (dim, 1) for v in velocities):
        raise ValueError("velocity dimension mismatch")
    first = sum(
        velocities[p][i] * sp.diff(observable, point_coords[p][i])
        for p in range(len(point_coords))
        for i in range(dim)
    )
    second = -nu * sum(
        sp.diff(observable, point_coords[p][i], point_coords[q][i])
        for p in range(len(point_coords))
        for q in range(len(point_coords))
        for i in range(dim)
    )
    return sp.simplify(first + second)


def anchor_relative_drifts(anchor_velocity: Matrix, point_velocities: Sequence[Matrix]) -> list[sp.Matrix]:
    """Finite-variation shape drifts u(X+R_p)-u(X)."""
    return [sp.simplify(v - anchor_velocity) for v in point_velocities]


def oriented_rectangle_area_vector_yz(half_y: sp.Expr, half_z: sp.Expr) -> sp.Matrix:
    """Oriented area vector of [-b,b]_y x [-c,c]_z with normal +e_x."""
    return sp.Matrix([4 * half_y * half_z, 0, 0])


def yz_rectangle_shear_area_rate_direct(
    shear_derivative: sp.Expr,
    y: sp.Symbol,
    half_y: sp.Expr,
    half_z: sp.Expr,
) -> sp.Matrix:
    """Same exact rectangle law without introducing a persistent dummy symbol."""
    integral_y = sp.integrate(shear_derivative, (y, -half_y, half_y))
    return sp.simplify(sp.Matrix([0, -2 * half_z * integral_y, 0]))


def local_nanson_area_rate(grad_u_anchor: Matrix, area_vector: Matrix) -> sp.Matrix:
    """Infinitesimal incompressible Nanson rate - (grad u)^T h."""
    if grad_u_anchor.shape != (3, 3) or area_vector.shape != (3, 1):
        raise ValueError("expected 3D velocity gradient and area vector")
    return sp.simplify(-grad_u_anchor.T * area_vector)


def cubic_heat_shear(y: sp.Expr, t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Exact NS shear profile U=y^3+6 nu t y on R^3 (constant pressure)."""
    return sp.expand(y**3 + 6 * nu * t * y)


def cubic_heat_shear_ns_residual(y: sp.Symbol, t: sp.Symbol, nu: sp.Expr) -> sp.Expr:
    """Residual U_t - nu U_yy; advection vanishes identically for u=(U(y,t),0,0)."""
    U = cubic_heat_shear(y, t, nu)
    return sp.simplify(sp.diff(U, t) - nu * sp.diff(U, y, 2))


def cubic_shear_rectangle_shape_residual(
    half_y: sp.Expr,
    half_z: sp.Expr,
    t: sp.Expr,
    nu: sp.Expr,
) -> sp.Matrix:
    """Exact finite-surface residual beyond local Nanson for centered yz rectangle.

    For U=y^3+6 nu t y, the local gradient at y=0 contributes -6 nu t A e_y.
    The exact material-surface rate contains the additional physical shape term

        E_shape = - A b^2 e_y,

    which depends on the surface second moment and is invisible to (X,h) alone.
    """
    y = sp.Symbol("y", real=True)
    U_y = sp.diff(cubic_heat_shear(y, t, nu), y)
    exact = yz_rectangle_shear_area_rate_direct(U_y, y, half_y, half_z)
    area = oriented_rectangle_area_vector_yz(half_y, half_z)
    A0 = sp.zeros(3)
    A0[0, 1] = sp.simplify(U_y.subs(y, 0))
    local = local_nanson_area_rate(A0, area)
    return sp.simplify(exact - local)


def rectangle_oriented_second_moment_yy(half_y: sp.Expr, half_z: sp.Expr) -> sp.Expr:
    """Integral_S y^2 dA for the centered yz rectangle."""
    return sp.simplify(sp.Rational(4, 3) * half_y**3 * half_z)


def cubic_shear_residual_from_second_moment(half_y: sp.Expr, half_z: sp.Expr) -> sp.Matrix:
    """The cubic-shear shape residual written as -3 (integral y^2 dA) e_y."""
    qyy = rectangle_oriented_second_moment_yy(half_y, half_z)
    return sp.Matrix([0, -3 * qyy, 0])


def scaled_cubic_shape_residual(
    radius: sp.Expr,
    half_y0: sp.Expr,
    half_z0: sp.Expr,
) -> sp.Matrix:
    """Exact raw scaling of the centered cubic-shear finite-surface residual."""
    return sp.simplify(cubic_shear_residual_from_second_moment(radius * half_y0, radius * half_z0))


def packet_shape_residual_matrix(first_loop_residual: Matrix) -> sp.Matrix:
    """Three-loop packet residual with the first area-vector column carrying shape work."""
    if first_loop_residual.shape != (3, 1):
        raise ValueError("expected a 3-vector residual")
    out = sp.zeros(3)
    out[:, 0] = first_loop_residual
    return out


def polynomial_heat_shear(degree: int, y: sp.Symbol, t: sp.Expr, nu: sp.Expr) -> sp.Expr:
    """Exact polynomial heat shear e^{nu t d_yy} y^degree."""
    if degree < 0:
        raise ValueError("degree must be nonnegative")
    out = sp.Integer(0)
    for j in range(degree // 2 + 1):
        coeff = sp.factorial(degree) / (
            sp.factorial(degree - 2 * j) * sp.factorial(j)
        )
        out += coeff * (nu * t) ** j * y ** (degree - 2 * j)
    return sp.expand(out)


def polynomial_heat_shear_residual(
    degree: int,
    y: sp.Symbol,
    t: sp.Symbol,
    nu: sp.Expr,
) -> sp.Expr:
    U = polynomial_heat_shear(degree, y, t, nu)
    return sp.simplify(sp.diff(U, t) - nu * sp.diff(U, y, 2))


def legendre_width_density(order: int, y: sp.Symbol, epsilon: sp.Expr) -> sp.Expr:
    """Positive-width perturbation 1+epsilon P_order(y) when |epsilon|<1."""
    if order < 0:
        raise ValueError("Legendre order must be nonnegative")
    return sp.expand(1 + epsilon * sp.legendre(order, y))


def width_surface_area(width: sp.Expr, y: sp.Symbol) -> sp.Expr:
    """Area of yz graph-strip {y in [-1,1], z in [-w(y)/2,w(y)/2]} with normal e_x."""
    return sp.simplify(sp.integrate(width, (y, -1, 1)))


def width_surface_even_moment(
    width: sp.Expr,
    y: sp.Symbol,
    moment_order: int,
) -> sp.Expr:
    if moment_order < 0:
        raise ValueError("moment order must be nonnegative")
    return sp.simplify(sp.integrate(y ** moment_order * width, (y, -1, 1)))


def width_surface_shear_area_rate(
    shear_derivative: sp.Expr,
    width: sp.Expr,
    y: sp.Symbol,
) -> sp.Matrix:
    """Area-vector rate for centered yz strip with width w(y), normal e_x."""
    return sp.Matrix([
        0,
        sp.simplify(-sp.integrate(shear_derivative * width, (y, -1, 1))),
        0,
    ])


def legendre_leading_moment(order: int) -> sp.Expr:
    """Exact integral int_{-1}^1 y^n P_n(y) dy."""
    if order < 0:
        raise ValueError("order must be nonnegative")
    n = order
    return sp.simplify(
        2 ** (n + 1) * sp.factorial(n) ** 2 / sp.factorial(2 * n + 1)
    )


def moment_hierarchy_shear_rate_difference(
    m: int,
    epsilon: sp.Expr,
) -> sp.Expr:
    """Difference in y-component Hdot for w=1+eps P_{2m} vs w=1 under U_{2m+1}.

    All lower even moments cancel by Legendre orthogonality.  Only the leading
    derivative coefficient (2m+1)y^{2m} survives.
    """
    if m <= 0:
        raise ValueError("m must be positive")
    n = 2 * m
    return sp.simplify(-(n + 1) * epsilon * legendre_leading_moment(n))
