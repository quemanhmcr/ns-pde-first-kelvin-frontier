"""Exact NS calibrations excluding overly naive first-bad predicates.

The amplitude-scaled ABC Beltrami family is a global smooth periodic Navier--Stokes
solution for every finite amplitude A.  Therefore raw instantaneous quantities
that become arbitrarily large with A cannot, by themselves, be universal
continuation-failure predicates.

This does not forbid using them as diagnostic/localization scores, and it does not
supply the programme's missing badness functional.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import sympy as sp

Matrix = sp.MatrixBase


def gradient(v: Matrix, coords: Sequence[sp.Symbol]) -> sp.Matrix:
    return sp.Matrix([[sp.diff(v[i], x) for x in coords] for i in range(v.rows)])


def curl3(v: Matrix, coords: Sequence[sp.Symbol]) -> sp.Matrix:
    x, y, z = coords
    return sp.Matrix([
        sp.diff(v[2], y) - sp.diff(v[1], z),
        sp.diff(v[0], z) - sp.diff(v[2], x),
        sp.diff(v[1], x) - sp.diff(v[0], y),
    ])


def laplacian(v: Matrix, coords: Sequence[sp.Symbol]) -> sp.Matrix:
    return sp.Matrix([sum(sp.diff(v[i], x, 2) for x in coords) for i in range(v.rows)])


def abc_velocity(A: sp.Expr, nu: sp.Expr, t: sp.Expr, coords: Sequence[sp.Symbol]) -> sp.Matrix:
    x, y, z = coords
    amp = A * sp.exp(-nu * t)
    return amp * sp.Matrix([
        sp.sin(z) + sp.cos(y),
        sp.sin(x) + sp.cos(z),
        sp.sin(y) + sp.cos(x),
    ])


def abc_pressure(u: Matrix) -> sp.Expr:
    return sp.simplify(-sp.Rational(1, 2) * u.dot(u))


def navier_stokes_residual(
    u: Matrix,
    p: sp.Expr,
    coords: Sequence[sp.Symbol],
    t: sp.Symbol,
    nu: sp.Expr,
) -> sp.Matrix:
    G = gradient(u, coords)
    nonlinear = sp.simplify(G * u)
    gradp = sp.Matrix([sp.diff(p, x) for x in coords])
    return sp.simplify(sp.diff(u, t) + nonlinear + gradp - nu * laplacian(u, coords))


def strain(u: Matrix, coords: Sequence[sp.Symbol]) -> sp.Matrix:
    G = gradient(u, coords)
    return sp.simplify((G + G.T) / 2)


def frobenius_square(M: Matrix) -> sp.Expr:
    return sp.simplify(sum(e**2 for e in M))


@dataclass(frozen=True)
class ABCPointQuantities:
    omega_sq: sp.Expr
    enstrophy: sp.Expr
    stretching: sp.Expr
    kelvin_bulk: sp.Expr
    stretch_bulk_ratio: sp.Expr
    growth_gate_margin: sp.Expr


def abc_origin_quantities(A: sp.Expr, nu: sp.Expr, t: sp.Expr) -> ABCPointQuantities:
    x, y, z = sp.symbols("x y z", real=True)
    coords = (x, y, z)
    u = abc_velocity(A, nu, t, coords)
    omega = curl3(u, coords)
    Gomega = gradient(omega, coords)
    S = strain(u, coords)
    p0 = {x: 0, y: 0, z: 0}
    omega0 = sp.simplify(omega.subs(p0))
    omega_sq = sp.simplify(omega0.dot(omega0))
    stretching = sp.simplify((omega.T * S * omega)[0].subs(p0))
    grad_sq = sp.simplify(frobenius_square(Gomega).subs(p0))
    bulk = sp.simplify(nu * grad_sq)
    return ABCPointQuantities(
        omega_sq=omega_sq,
        enstrophy=sp.simplify(omega_sq / 2),
        stretching=stretching,
        kelvin_bulk=bulk,
        stretch_bulk_ratio=sp.simplify(stretching / bulk),
        growth_gate_margin=sp.simplify(stretching - bulk),
    )


def abc_enstrophy_gradient_at(
    A: sp.Expr,
    nu: sp.Expr,
    t: sp.Expr,
    point: Sequence[sp.Expr],
) -> sp.Matrix:
    if len(point) != 3:
        raise ValueError("ABC point must have three coordinates")
    x, y, z = sp.symbols("x y z", real=True)
    coords = (x, y, z)
    u = abc_velocity(A, nu, t, coords)
    omega = curl3(u, coords)
    e = sp.simplify(omega.dot(omega) / 2)
    subs = dict(zip(coords, point))
    return sp.simplify(sp.Matrix([sp.diff(e, q) for q in coords]).subs(subs))


def abc_stretching_at(
    A: sp.Expr,
    nu: sp.Expr,
    t: sp.Expr,
    point: Sequence[sp.Expr],
) -> sp.Expr:
    if len(point) != 3:
        raise ValueError("ABC point must have three coordinates")
    x, y, z = sp.symbols("x y z", real=True)
    coords = (x, y, z)
    u = abc_velocity(A, nu, t, coords)
    omega = curl3(u, coords)
    S = strain(u, coords)
    subs = dict(zip(coords, point))
    return sp.simplify((omega.T * S * omega)[0].subs(subs))


def amplitude_limits(A: sp.Symbol, quantities: ABCPointQuantities) -> dict[str, sp.Expr]:
    return {
        "omega_sq": sp.limit(quantities.omega_sq, A, sp.oo),
        "enstrophy": sp.limit(quantities.enstrophy, A, sp.oo),
        "stretching": sp.limit(quantities.stretching, A, sp.oo),
        "kelvin_bulk": sp.limit(quantities.kelvin_bulk, A, sp.oo),
        "stretch_bulk_ratio": sp.limit(quantities.stretch_bulk_ratio, A, sp.oo),
        "growth_gate_margin": sp.limit(quantities.growth_gate_margin, A, sp.oo),
    }
