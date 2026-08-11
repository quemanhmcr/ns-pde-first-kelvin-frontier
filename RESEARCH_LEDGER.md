# Research ledger

## 2026-08-12 — repository initialization

This repository was created as a standalone local Git project so the PDE-first/Kelvin programme does not modify or inherit the theorem spine of any other research repository.

### Current established structure

- Fixed physical Kelvin circulation: future conditional variance is the exact Doob bank for its quadratic variation.
- Selector switching: observer jumps do not create stochastic quadratic variation; they create exact covariance revaluation/reset terms.
- Canonical Kelvin mixed current: the germ differential of instantaneous Kelvin action is a signed polarization/Hodge transfer, not a standalone positive payment.
- Normalized ancestry law: it yields an exact distributed future-variance/current balance; Fisher/osmotic entropy is a distinct bank with a distinct conjugate potential.
- Strong-Hodge case: `q j_circ` is a closed occupation current and therefore globally performs zero work against an exact covariance potential; localization turns this into boundary-crossing covariance flux.
- Same-ancestor two-replica construction: future replicas must be independent after the common ancestor. The true second-order branching source is the diagonal viscous tensor `2 nu q K delta_Delta`, not `q j_circ tensor j_circ`.
- Exact smooth periodic shear calibrations rule out several tempting selector-independent scalar reservoirs at the current structural level.

### Current frontier

Construct the literal pair-current lift of one complete first-bad-germ hysteresis excursion and compute every boundary/seam:

1. entry and frozen selector interval;
2. quantile motion;
3. anchor/orientation motion;
4. shell/scale transition;
5. refinement;
6. resolve/reset;
7. physical exit;
8. literal non-functorial `S^int / Z_irr` sector.

The target is an exact current identity converting selected pair localization into finite endpoints plus tracked physical transfers/exits. If a non-boundary observer component remains, that component is the missing physical resource; do not hide it with an inequality.

### Status

No continuation/restart conclusion. No 3D Navier--Stokes regularity proof. Pillar II remains literally unverified.

## 2026-08-12 — exact PDE audit harness

The repository now carries a dedicated GitHub Actions audit harness. It is deliberately
not a numerical PDE solver and does not treat floating-point stress as proof. The core
calibration family is an exact smooth periodic 3D Navier--Stokes shear for which the
nonlinearity vanishes identically. The audit uses symbolic residual checks and closed-form
Gaussian expectations for the Kelvin terminal payoff.

The CI distinguishes three layers:

1. **Symbolic exact identities**: divergence-free condition, exact Navier--Stokes residual,
   pair diagonal-branching identity, Kelvin quadratic polarization, normalized ancestry
   variance-current identity, and the quadratic-refinement no-go.
2. **Exact-solution calibration**: closed-form evaluation of selected Kelvin future
   variance, drift-square circulation traffic, and the natural coexact Hodge bank across
   increasing odd Fourier packets.
3. **Anti-theorem guards**: the research note must retain explicit classification labels,
   the `S^int / Z_irr` caveat, and the no-continuation/no-regularity status.

The calibration is designed to falsify false reservoirs, not to certify a regularity
bridge. A CI pass means only that the encoded exact identities and anti-theorem tests are
consistent with the tested PDE family.


## 2026-08-12 — pair-localization world-sheet audit

A new uncertified note `docs/pair_localization_worldsheet_audit.md` records the
minimal spacetime pair-current strip identity for a complete first-bad-germ
excursion.  The exact chain algebra cancels all internal localization rungs and
forces every remaining longitudinal seam to be classified as physical pair
transport/quantile/shell/refinement, exit, connection geometry, or literal
`S^int / Z_irr` defect.

A new exact refinement obstruction was isolated: if a physical parent current
refines linearly as `Z_P=sum_i a_i Z_i`, then its pair lift is the full tensor
square `sum_ij a_i a_j Z_i tensor Z_j`.  Keeping only child diagonals loses
cross-child covariance even when the one-current refinement has zero irreducible
defect.  Those cross terms are physical refinement content, not Pillar-II error.

The exact odd-mode periodic NS shear supplies a sharp witness: rectangular Kelvin
payoffs at anchors `0` and `pi` satisfy `X_pi=-X_0` pathwise, so both child
variances are positive while the parent variance of `Z_0+Z_pi` is exactly zero.
The cross-child covariance cancels the diagonal contribution.  GitHub Actions now
audits this identity, closed observer-loop covariance revaluation, `boundary^2=0`,
and internal pair-world-sheet seam cancellation.

Status remains: no continuation/restart theorem, no regularity claim, and literal
Pillar II remains open.

## 2026-08-12 — refinement functoriality and nondegenerate 3D PDE audit

The pair-localization frontier has been sharpened further.  A linear current
refinement `R` has the exact pair lift `R tensor R`; composition is functorial and
covariance pulls back as `R^T C R`.  Thus nested refinement seams telescope at pair
level **provided the full tensor square is retained**.  Diagonal-only projection
breaks this naturality by deleting physical cross-child covariance.  Such deleted
cross terms are an observer/analysis projection defect, not `Z_irr`.

The symbolic CI lane has also been extended beyond zero-advection shears.  It now
audits the exact decaying ABC/Beltrami 3D Navier--Stokes solution, where the
nonlinear term is nonzero and is cancelled by the exact pressure gradient.  A
separate multidimensional pair-generator test verifies that the same-ancestor
branch-time source is `2 nu K` for anisotropic symmetric diffusion and that drift
terms cancel from the branching source.

These are structural audit gains only.  Literal shell/quantile/active CK maps are
still not inserted into the pair world-sheet, Pillar II remains open, and no
continuation or regularity claim is made.

## 2026-08-12 — exact same-ancestor quantile leakage

The quantile part of the pair-localization world-sheet now has an exact calibration.
For a centered Gaussian common ancestor with two independent future branches, the
half-space chamber keeps one-particle mass exactly `1/2`, while the pair mass is
`1/4 + asin(rho)/(2 pi)` and strictly decreases as branch noise decorrelates the
replicas.  Its exact derivative is negative and is audited in CI.

Therefore a zero-mass one-particle quantile current does not imply zero pair
quantile current.  The pair seam is genuine localization covariance transport and
must remain explicit in the selected Kelvin budget.  It is neither ancestry
production nor an observer reset.
