# Pair-localization world-sheet audit

This is an **uncertified PDE-first frontier note**.  It records exact chain algebra
and exact smooth Navier--Stokes calibrations.  It does not claim continuation or
regularity, and it does not assume the literal Pillar-II statement
`S^int = 0 iff Z_irr = 0`.

## 1. The spacetime strip identity

Let `D_k` be the distributed physical pair state and `S_k` the selected physical
pair state at stage boundary `k`.  Let `R_k` be the degree-one localization rung
oriented from `D_k` to `S_k`.  During one elementary physical stage, let
`D_k -> D_(k+1)` and `S_k -> S_(k+1)` be the distributed and selected longitudinal
pair paths.  The oriented spacetime strip `F_k` has boundary

\[
\boxed{
\partial F_k
= D_{k\to k+1}+R_{k+1}-S_{k\to k+1}-R_k .
}
\]

Applying the boundary once more gives zero exactly.  Summing stages gives

\[
\boxed{
\partial\Big(\sum_k F_k\Big)
= D_{\rm path}-S_{\rm path}+R_{\rm final}-R_{\rm initial}.
}
\]

Every internal localization rung cancels with opposite orientation.  This is the
minimal pair-world-sheet topology behind any complete hysteresis excursion.

**Classification: Exact identity.**

The identity alone does **not** say that the longitudinal difference
`D_path-S_path` vanishes.  Each longitudinal segment must still be classified
literally as physical transport, quantile/shell/refinement transfer, physical
exit, connection/holonomy geometry, or an irreducible active-chain defect.

## 2. Covariance Stokes law

For the future covariance potential `V`, the functorial flat-sector spacetime
covariance one-form is

\[
\mathfrak A_{\rm cov}=d_{\rm pair}V-\gamma\,ds=d_{\rm spacetime}V,
\]

because the fixed-current Doob equation is `D_s V = -gamma`.  Hence on every
literal pair strip

\[
\boxed{
\langle \mathfrak A_{\rm cov},\partial F_k\rangle=0.
}
\]

Summing strips converts the difference of selected and distributed accumulated
Kelvin action into endpoint localization covariance plus the covariance work of
the non-cancelled physical side currents.  In a variable frame, the same statement
must be written with the transported connection; connection/holonomy terms are
geometry, not production.

**Classification: Exact identity in the functorial same-generator sector.**

A projected active chain may leave a commutator residual.  That residual is the
literal slot for `S^int / Z_irr` and is not set to zero here.

## 3. Pair refinement is quadratic: diagonal children are not enough

Suppose a physical parent current refines linearly as

\[
Z_P=\sum_i a_i Z_i
\]

with no irreducible current defect.  Its pair atom is

\[
\boxed{
Z_P\boxtimes Z_P
=\sum_{i,j}a_i a_j\,Z_i\boxtimes Z_j.
}
\]

The diagonal-only descendant

\[
\sum_i a_i^2 Z_i\boxtimes Z_i
\]

misses the physical cross-child current

\[
\boxed{
\Pi_{\rm cross}^{\rm ref}
=\sum_{i\ne j}a_i a_j Z_i\boxtimes Z_j.
}
\]

Therefore a linear refinement can be perfectly functorial at one-current level
while a **diagonal-only pair implementation is non-functorial at covariance level**.
The missing cross-child current is legitimate physical covariance content.  It is
not `Z_irr` and must not be charged to Pillar II.

**Classification: Exact identity.**

## 4. Exact Navier--Stokes witness for the cross-child term

Use the exact periodic shear family

\[
u_N(y,t)=\frac1{\sqrt N}\sum_{m=1}^N
 e^{-\nu(2m-1)^2t}\cos((2m-1)y)\,e_x .
\]

The nonlinear term vanishes identically, so this is an exact smooth 3D periodic
Navier--Stokes solution with constant pressure.  For the rectangular Kelvin
payoffs at anchors `0` and `pi`, odd parity gives pathwise

\[
\boxed{X_\pi=-X_0.}
\]

Consequently

\[
V_0=V_\pi>0,
\qquad
C(0,\pi)=-V_0.
\]

For the parent current `Z_0+Z_pi`,

\[
\boxed{
V(Z_0+Z_\pi)=V_0+V_\pi+2C(0,\pi)=0,
}
\]

while a diagonal-only refinement would report `2 V_0 > 0`.

**Classification: Rigorous consequence from an exact Navier--Stokes calibration.**

This is a hard anti-theorem: positive child diagonal variance is not refinable
physical payment unless the cross-child covariance is retained.

## 5. Reset work versus observer path length

For any two selector coordinates,

\[
\boxed{
V(Z_b)-V(Z_a)
=V(Z_b-Z_a)+2C(Z_a,Z_b-Z_a).
}
\]

Along a closed observer loop the left-hand side telescopes to zero, while the sum
of positive diagonal increment variances can be strictly positive.  Thus observer
path length cannot be a finite physical bank.  The signed covariance cross terms
are required for exact revaluation.

**Classification: Exact identity; the nonzero closed-loop diagonal cost is a
rigorous consequence of the exact shear calibration in the audit suite.**

## 6. What the complete hysteresis lift must now prove

For the actual first-bad-germ excursion, build strips in the literal order

1. entry/freeze;
2. quantile motion;
3. anchor/orientation motion;
4. shell transition;
5. refinement **with the full pair tensor square**;
6. resolve/reset;
7. physical exit.

The abstract world-sheet theorem already guarantees cancellation of internal
localization rungs.  What remains to be proved from the actual active definitions
is that every longitudinal seam is one of:

- physical covariance transport;
- quantile/shell/refinement pair flux;
- physical exit;
- transported connection/holonomy geometry;
- literal `S^int / Z_irr` defect.

There is no remaining legitimate category called “diagonal refinement error”.
Cross-child covariance belongs to the physical refinement current.

**Classification: Conjectural bridge until the actual active maps are inserted
line by line.**
