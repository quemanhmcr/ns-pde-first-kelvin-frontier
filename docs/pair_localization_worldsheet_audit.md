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

## 7. Nested refinement has an exact pair functor

For a linear physical refinement map `R` on currents, the correct pair lift is

\[
\boxed{R^{(2)}=R\otimes R.}
\]

For two consecutive refinements,

\[
\boxed{
(R_2R_1)^{(2)}
=(R_2\otimes R_2)(R_1\otimes R_1).
}
\]

Equivalently, a covariance matrix/cochain pulls back by

\[
\boxed{C_{\rm parent}=R^T C_{\rm child}R,}
\]

and consecutive pullbacks compose exactly.  Therefore **internal refinement seams
telescope at pair level when the full tensor-square lift is retained**.

A projection that keeps only child diagonals does not commute with `R tensor R` in
general; its commutator is precisely the lost cross-child covariance sector.  This
is an analysis/projection defect, not evidence of irreducible physical content.
Only a residual that remains after the full pair functor and all tracked physical
projections have been applied is eligible for the literal `S^int / Z_irr` slot.

**Classification: Exact identity.**

This narrows the refinement part of the active-chain audit: the remaining unknown
is no longer whether cross-child covariance should be present, but whether the
actual shell/refinement maps used by the first-bad-germ construction realize the
full pair functor without an additional non-functorial remainder.

## 8. A nondegenerate 3D pressure calibration is included in CI

The audit suite also uses the decaying ABC/Beltrami field

\[
U=(\sin z+\cos y,\;\sin x+\cos z,\;\sin y+\cos x),
\qquad u(t)=e^{-\nu t}U.
\]

It satisfies `curl U=U`, `Delta U=-U`, and the nonlinear term is not zero.  Instead

\[
(u\cdot\nabla)u=\nabla\frac{|u|^2}{2},
\]

so with

\[
p=-\frac{|u|^2}{2}
\]

the full 3D Navier--Stokes residual vanishes exactly.  This regression prevents
the PDE audit from relying only on shear solutions whose advective term happens to
vanish.

**Classification: Exact Navier--Stokes identity, symbolically audited.**

The same symbolic lane now audits the multidimensional same-ancestor branching
formula with a symmetric anisotropic diffusion tensor `K`; the diagonal branch-time
source is exactly `2 nu K` contracted against cross-replica derivatives, while the
drift cancels from the branching source.

**Classification: Exact identity.**

## 9. Quantile conservation does not lift to pair conservation

The quantile seam has its own exact obstruction.  Let a common ancestor be

\[
Y\sim N(0,\sigma^2)
\]

and let two future replicas branch independently,

\[
X_1=Y+E_1,
\qquad
X_2=Y+E_2,
\qquad
E_1,E_2\sim N(0,\tau^2).
\]

Each marginal is centered and symmetric, so the physical half-space chamber
`D={x>0}` has exactly fixed one-particle quantile mass

\[
\boxed{P(X_i>0)=\frac12.}
\]

But the two replicas retain correlation

\[
\rho=\frac{\sigma^2}{\sigma^2+\tau^2},
\]

and the exact centered-Gaussian quadrant formula gives

\[
\boxed{
P(X_1>0,X_2>0)
=\frac14+\frac1{2\pi}\arcsin\rho.
}
\]

Thus the one-particle quantile mass is constant while the pair mass decreases from
`1/2` at zero branch separation toward `1/4` as the two futures decorrelate.  For
`tau^2>0`,

\[
\boxed{
\frac{d}{d\tau^2}P(X_1>0,X_2>0)
=-\frac{\sigma^2}
{2\pi(\sigma^2+\tau^2)\sqrt{\tau^2(2\sigma^2+\tau^2)}}<0.
}
\]

**Classification: Exact identity for the same-ancestor Gaussian diffusion
calibration.**

Physical interpretation: a quantile chamber can conserve ancestry mass exactly
while losing same-ancestor pair correlation through its pair boundary.  This is a
pair-localization covariance flux, not ancestry production and not an observer
reset.  Therefore the first-bad-germ world-sheet must retain an explicit
`Pi_quant^(2)` seam even when the one-particle quantile current has zero total mass.

**Rigorous consequence:** one-particle quantile conservation cannot be used to
erase the pair quantile seam.

## 10. Shell decomposition must also be lifted by the full product partition

If a one-particle region is partitioned into physical shells

\[
D=\bigsqcup_i A_i,
\]

then pair space decomposes as

\[
\boxed{
D\times D=\bigsqcup_{i,j}(A_i\times A_j).
}
\]

Keeping only the diagonal blocks `A_i x A_i` discards cross-shell pair content.
For the exact same-ancestor Gaussian sign partition `A_+={x>0}`, `A_-={x<0}`,
branching transfers pair mass continuously from the same-shell blocks into
`A_+ x A_-` and `A_- x A_+`, even though each one-particle shell mass remains
exactly `1/2`.

**Classification: Exact identity for the product partition; rigorous consequence
from the same-ancestor Gaussian calibration.**

Thus shell telescoping is legitimate only in the **full pair shell complex**.
Cross-shell blocks are physical covariance transport and must not be erased as
refinement noise or observer error.

## 11. Physical exit is a genuine two-face pair sink

For the killed diffusion

\[
dX=\sqrt{2\nu}\,dW,
\qquad X>0,
\]

with absorption at `0`, a particle starting at `x>0` has exact survival

\[
\boxed{
S(x,t)=\operatorname{erf}\!\left(\frac{x}{\sqrt{4\nu t}}\right).
}
\]

The positive first-exit density is

\[
\boxed{
f_{\rm exit}(x,t)
=-\partial_tS
=\frac{x e^{-x^2/(4\nu t)}}
{2\sqrt{\pi\nu}\,t^{3/2}}.
}
\]

For two independent future replicas from the same fixed ancestor, pair survival is
`S^2`, hence

\[
\boxed{
-\partial_t(S^2)=2S f_{\rm exit}=S f_{\rm exit}+f_{\rm exit}S.
}
\]

The two summands are exactly the two physical pair-boundary faces

\[
(\partial D\times D)\cup(D\times\partial D).
\]

**Classification: Exact identity for killed diffusion.**

Physical exit therefore does not telescope away as an observer seam.  It is a true
sub-Markov sink and remains explicitly in the pair covariance budget.  Any
renormalization of survivors is a new conditional observable and must not be
silently substituted for the unconditioned physical exit law.
