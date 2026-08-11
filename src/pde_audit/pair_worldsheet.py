"""Formal pair-localization world-sheet algebra.

This module does not prove the Navier--Stokes continuation bridge.  It encodes the
minimal chain identities that any literal first-bad-germ pair localization must
satisfy.  Coefficients are exact Fractions so seam cancellation is audited without
floating-point tolerance.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Iterable


Coeff = Fraction


class Chain:
    def __init__(self, terms: Dict[str, Coeff] | None = None) -> None:
        self.terms: Dict[str, Coeff] = {}
        if terms:
            for key, value in terms.items():
                value = Fraction(value)
                if value:
                    self.terms[key] = value

    @classmethod
    def basis(cls, name: str, coeff: int | Fraction = 1) -> "Chain":
        return cls({name: Fraction(coeff)})

    def __add__(self, other: "Chain") -> "Chain":
        out = dict(self.terms)
        for key, value in other.terms.items():
            out[key] = out.get(key, Fraction(0)) + value
            if not out[key]:
                del out[key]
        return Chain(out)

    def __sub__(self, other: "Chain") -> "Chain":
        return self + (-other)

    def __neg__(self) -> "Chain":
        return Chain({k: -v for k, v in self.terms.items()})

    def __mul__(self, scalar: int | Fraction) -> "Chain":
        scalar = Fraction(scalar)
        return Chain({k: scalar * v for k, v in self.terms.items()})

    __rmul__ = __mul__

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Chain) and self.terms == other.terms

    def is_zero(self) -> bool:
        return not self.terms

    def coefficient(self, name: str) -> Fraction:
        return self.terms.get(name, Fraction(0))

    def as_dict(self) -> dict[str, str]:
        return {k: str(v) for k, v in sorted(self.terms.items())}


@dataclass(frozen=True)
class Edge:
    """Oriented one-cell from source 0-chain to target 0-chain."""

    name: str
    source: Chain
    target: Chain

    def boundary(self) -> Chain:
        return self.target - self.source


@dataclass(frozen=True)
class StageStrip:
    """One oriented spacetime strip between distributed and selected pair paths.

    Rungs are oriented distributed -> selected.  The positively oriented boundary
    is

        distributed_edge + end_rung - selected_edge - start_rung.

    For a literal strip, applying the vertex boundary once more must give zero.
    """

    label: str
    distributed_edge: Edge
    selected_edge: Edge
    start_rung: Edge
    end_rung: Edge

    def boundary_1chain(self) -> Chain:
        return (
            Chain.basis(self.distributed_edge.name)
            + Chain.basis(self.end_rung.name)
            - Chain.basis(self.selected_edge.name)
            - Chain.basis(self.start_rung.name)
        )

    def boundary_squared(self) -> Chain:
        return (
            self.distributed_edge.boundary()
            + self.end_rung.boundary()
            - self.selected_edge.boundary()
            - self.start_rung.boundary()
        )


def make_stage(label: str, k: int) -> StageStrip:
    """Canonical rectangle with D_k,S_k -> D_{k+1},S_{k+1}."""
    d0 = Chain.basis(f"D{k}")
    d1 = Chain.basis(f"D{k+1}")
    s0 = Chain.basis(f"S{k}")
    s1 = Chain.basis(f"S{k+1}")
    return StageStrip(
        label=label,
        distributed_edge=Edge(f"D:{label}:{k}", d0, d1),
        selected_edge=Edge(f"S:{label}:{k}", s0, s1),
        start_rung=Edge(f"R{k}", d0, s0),
        end_rung=Edge(f"R{k+1}", d1, s1),
    )


def worldsheet_boundary(stages: Iterable[StageStrip]) -> Chain:
    out = Chain()
    for stage in stages:
        out += stage.boundary_1chain()
    return out


def internal_rung_coefficients(boundary: Chain, count: int) -> dict[str, Fraction]:
    """Return coefficients of the internal localization rungs R1,...,R_{count-1}."""
    return {f"R{k}": boundary.coefficient(f"R{k}") for k in range(1, count)}


def refinement_pair_coefficients(weights: list[Fraction]) -> dict[tuple[int, int], Fraction]:
    """Full tensor-square coefficients for Z_parent=sum_i w_i Z_i.

    Ordered pair basis is used.  The diagonal-only lift consists of i==j terms;
    all i!=j terms are required cross-child physical covariance content.
    """
    return {
        (i, j): Fraction(wi) * Fraction(wj)
        for i, wi in enumerate(weights)
        for j, wj in enumerate(weights)
        if Fraction(wi) * Fraction(wj)
    }


def diagonal_only_refinement_coefficients(weights: list[Fraction]) -> dict[tuple[int, int], Fraction]:
    return {
        (i, i): Fraction(wi) * Fraction(wi)
        for i, wi in enumerate(weights)
        if Fraction(wi)
    }


def refinement_cross_defect(weights: list[Fraction]) -> dict[tuple[int, int], Fraction]:
    full = refinement_pair_coefficients(weights)
    diag = diagonal_only_refinement_coefficients(weights)
    keys = set(full) | set(diag)
    return {k: full.get(k, Fraction(0)) - diag.get(k, Fraction(0)) for k in keys if full.get(k, Fraction(0)) != diag.get(k, Fraction(0))}
