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

## 2026-08-12 — full pair shell partition and physical two-face exit

The shell and exit seams now have exact calibration laws.  A one-particle shell
partition lifts to the full product partition `A_i x A_j`; diagonal shell blocks
alone lose cross-shell same-ancestor covariance.  In the Gaussian branching audit,
pair mass moves from same-sign shell blocks into cross-sign blocks while each
one-particle shell mass stays fixed.

Physical exit is audited with killed Brownian ancestry on the half-line.  Single
survival is `erf(x/sqrt(4 nu t))`; two-replica survival is its square, and the pair
loss rate is exactly the sum of the two exit faces.  Exit is therefore a genuine
physical sink, not an observer seam and not a quantity to renormalize away.

## 2026-08-12 — continuous anchor covariance current and seam coverage guard

The exact one-mode shear now audits the continuous anchor version of the
localization law.  Its future variance satisfies the backward/remaining-time
variance PDE with Kelvin carré-du-champ source, and its anchor derivative equals
twice the covariance between circulation and the physical anchor derivative of
circulation.  This identifies continuous anchor motion and finite selector reset
as two forms of the same covariance revaluation geometry.

CI now also contains an explicit frontier seam registry.  Quantile, shell,
refinement, reset and physical exit have audited structural/calibration status;
variable-frame connection terms and the literal active CK/Pillar-II sector remain
open, and continuation/restart is forced to remain open.  The registry is an
overclaim guard, not a proof of pair-localization closure.

## 2026-08-12 — variable-frame geometry audit

The variable-frame caveat has been narrowed.  Symbolic CI now checks Cartan's
identity for a genuinely nonconstant noise vector field and a nontrivial closed
vorticity two-form.  The Lie derivative contains frame-derivative terms absent from
naive coefficientwise translation, and it still preserves closedness.  These terms
are therefore transported geometry/connection content, not a new production
channel.

A separate variable-coefficient derivation test verifies that same-ancestor
branching still produces the cross operator `2 D_1 D_2`; variable noise
coefficients do not add a distinct pair source.  What remains open is the literal
active-frame/Hodge commutator in the first-bad-germ construction, not the generic
Cartan/branching algebra.

## 2026-08-12 — active first-bad pair commutator reduction

The full pair world-sheet has been pushed one level closer to the literal
first-bad construction.  A new symbolic current-algebra module now represents a
one-current stage by `(F_1,F_0)` between literal chain complexes and audits the
boundary defect

`C_F = B_out F_1 - F_0 B_in`.

For the full ordered pair lift `F^(2)=F_1 tensor F_1`, the pair boundary defect is
now proved and tested exactly as the two-face factorization

`C_F^(2) = [C_F tensor F_1 ; - F_1 tensor C_F]`.

The covariant transport analogue is likewise exact:

`G_F^(2)=G_F tensor F + F tensor G_F`, with
`G_F=Fdot+T_out F-F T_in`.

**Classification: Exact identities.**

This removes the possibility of an autonomous pair-only producer created merely by
the full tensor-square lift.  Quantile/shell/exit defects remain physical interface
or exit currents on the two replica faces; variable-frame terms remain connection
geometry; full refinement remains functorial and keeps every cross-child term.
Only a one-current active-map remainder that survives after subtracting those
classified terms can feed `S^int / Z_irr`.

**Classification: Rigorous consequence.**

A completed finite-cell hysteresis witness now instantiates, in chronological
order, freeze, quantile, anchor/orientation, shell, refinement, resolve/reset and
physical exit.  The direct completed boundary residual equals the exact sum of all
transported stage seams.  Removing the physical localization/exit stages leaves a
functorial composition with zero boundary residual.  A separate full-shell test
reconstructs the parent pair only after all ordered shell blocks are included.

The exact odd-mode Navier--Stokes shear now also audits an active interpolation
`Z_h=h Z_0+(1-h) Z_pi`.  Since `X_pi=-X_0` pathwise,
`V(Z_h)=(2h-1)^2 V(Z_0)` and the physical pair bank vanishes at `h=1/2`; a
diagonal-only active pair projection remains strictly positive.  This is a new
anti-cancellation guard for active/refinement implementations.

**Classification: Rigorous consequence from an exact Navier--Stokes calibration.**

The literal Pillar-II question has therefore narrowed to the actual one-current CK
projection.  The repository still does **not** contain the chain-level incidence
maps `(P_active,1,P_active,0)` or the active transport generator needed to compute

`B P_active,1 - P_active,0 B`

and

`Pdot_active + T_out P_active - P_active T_in`

after removing quantile/shell/exit/connection/reset terms.  Those residuals are not
set to zero.  A generic finite-cell counterexample in CI shows that an arbitrary
projection onto "active" cells need not commute with boundary, so naturality cannot
be assumed from the word active alone.

**Classification at this stage: Conjectural bridge / literal missing active-CK datum.  This specific ambient-map gap is superseded below by cycle typing and the Kelvin-admissibility audit.**

Current answer to the frontier question: after FULL pair content and all already
identified physical boundary/connection terms are retained, there is **no
independent pair-only residual**.  A genuine residual can remain only if the actual
one-current active CK projection has a nonzero irreducible boundary or transport
commutator.  If those one-current remainders vanish, the pair `Pi_irr^(2)` vanishes
exactly; if not, its explicit tensor lift is the obstruction.  No finite universal
bank for a nonzero irreducible active commutator has been established.

No continuation/restart theorem and no 3D Navier--Stokes regularity claim.


## 2026-08-12 — cycle-typed first-bad selector removes the intrinsic ambient defect

The active first-bad map has been retyped on the actual domain of the Kelvin
observable.  Candidate germ currents form a library `K` of closed physical cycles,
`B_x K=0`, and the first-bad/hysteresis logic acts by a state-dependent support
projector `M_fb` in germ coefficient space.  Thus the intrinsic selector is
`P_fb=K M_fb`, not an arbitrary endomorphism of the full ambient physical chain
complex.

This yields the exact identities `B_x P_fb=0` and zero full-pair physical boundary
for `P_fb tensor P_fb`.  CI includes an exact counterexample showing why this type
correction matters: two ambient extensions can have different global commutators,
including a nonzero one, while the commutator restricted to the actual Kelvin cycle
and pair cycle is exactly zero.  Off-cycle ambient commutator mass is therefore an
extension/observer artifact unless it survives the physical cycle restriction.

The transport analogue is also exact.  For `P_fb=K M`,
`G_P=G_K M + K G_M`; for a diagonal germ support mask,
`[A_g,M]_{ij}=A_ij(chi_j-chi_i)`, so only active/inactive interface crossings
survive.  Finite hysteresis switches satisfy the full tensor-square jump identity
and pair with future covariance as exact reset revaluation.

Exact NS pressure tests were added.  In the odd-mode shear, the selector switch
`0 -> pi` has strictly positive increment variance but zero net bank change because
the mixed covariance cancels the diagonal increment exactly.  In the genuine 3D
ABC/Beltrami solution, an `x`-torus closed cycle has nonzero circulation while the
exact pressure gradient has zero circulation.

**Classification: Exact identities plus rigorous consequences from exact NS
calibrations.**

For the cycle-typed first-bad selector itself, after quantile/shell interfaces,
connection geometry, refinement, physical exit and finite reset are retained, the
intrinsic selector remainders satisfy `C_irr^selector=G_irr^selector=0`.  The
selected-Kelvin pair localization identity therefore has no intrinsic
active-selector defect.  This does **not** establish the programme-wide Pillar-II
claim: `S^int` is still not defined line by line in this repository, and no
additional ambient CK/Hodge operator beyond the closed-cycle realization has been
specified.  Any such future operator must be audited separately.

No continuation/restart theorem and no regularity claim.


## 2026-08-12 — closed-range Hodge projector kinematics

A second active-CK layer has been audited conditionally on a precise structural
hypothesis: any additional CK/Hodge operation is an idempotent projector `H` whose
range lies in the closed physical-current subspace.  The weighted finite-chain
model `H=K(K^T W K)^(-1)K^T W` satisfies `H^2=H`, `B_x H=0`, fixes the cycle
library, and is `W`-selfadjoint.

Differentiating idempotency covariantly gives `G H+H G=G`, hence
`H G H=0` and `(I-H)G(I-H)=0`.  Projector motion is therefore purely signed
range/complement exchange; a co-moving connection removes pure frame motion
exactly.  The full pair derivative is `G tensor H + H tensor G`, with zero
active-pair internal sandwich `(H tensor H) D(H tensor H) (H tensor H)`.

**Classification: Exact identities under the stated projector hypotheses.**

This narrows but does not close global Pillar II.  The repository still has no
line-by-line `S^int` definition and no literal extra CK/Hodge operator to identify
with this projector.  The immediately following Kelvin-admissibility audit removes
the non-idempotent loophole and classifies range-outside-cycle behavior as physical
gauge-visible boundary.  No continuation/restart theorem and no regularity claim.


## 2026-08-12 — Kelvin admissibility closes the non-projector CK loophole

The original commit was re-audited to determine what `S^int / Z_irr` actually
encoded.  No literal `S^int` implementation has ever existed in repository
history.  The only explicit pair-level realization was the content defect
`Pi_irr^(2)=(R tensor R)_* Pi-Pi_allowed^(2)` associated with an allowed
projection.

A new exact admissibility audit removes the remaining non-projector ambiguity.
For a closed Kelvin library `K`, `BK=0`, an arbitrary linear ambient operation `H`
need not be idempotent.  Its intrinsic physical type depends only on `HK`.  If
`BHK=0`, it remains a Kelvin-cycle operation; when its output lies in the chosen
cycle span it factors exactly as `HK=KL`, and full pair content satisfies
`(KL)^(2)=K^(2)L^(2)`.  CI uses an explicit non-idempotent `H` with `H^2 != H` and
verifies zero intrinsic one-current and pair boundary.

If `BHK != 0`, exact Stokes pairing makes a pressure/gauge form observable through
`<dp,HK a>=<p,BHK a>`.  A finite-chain witness gives canonical gauge work `2`.
The exact 3D ABC/Beltrami Navier--Stokes calibration makes the same distinction in
the PDE itself: pressure work is zero around the closed `x` torus cycle but equals
`2 exp(-2 nu t)` on an open half-cycle at `y=pi/2,z=0`.

The audit also covers differentiable nonlinear cycle-valued maps: `B Phi=0`
forces `B D Phi=0`, and the full pair derivative is exactly
`dot Z tensor Z + Z tensor dot Z` with zero pair physical boundary.  Finite jumps
remain reset revaluations.

**Classification: Exact identities and rigorous physical consequences.**

Consequently the original pair-content-defect mechanism is exhausted for the
specified construction: full admissible content gives zero; deleted cross content
is observer/analysis projection; cycle breaking is physical interface/exit;
continuous cycle-preserving motion is cycle-coordinate/connection work.  Global
Pillar II is still not declared proved because `S^int` has no line-by-line
definition and an independently intended `Z_irr` has not been supplied.

No continuation/restart theorem and no regularity claim.

## 2026-08-12 — stochastic CK loophole is named quadratic variation

The admissibility audit was extended from finite-variation/differentiable CK motion
to a semimartingale state `dS=b ds+sigma dW`.  If `Z=Phi(S)` remains a closed
physical Kelvin current, differentiating `B Phi=0` forces both the Itô drift and
every diffusion tangent to remain closed.  The exact pair Itô formula contains one
second-order source,

`Q_Phi^(2)=sum_mu Psi_mu tensor Psi_mu`,

which is precisely martingale quadratic variation/carré-du-champ.  Its pair
physical boundary is zero when the diffusion tangents are cycles.  This is a named
physical stochastic producer with the existing future-variance interpretation, not
an untyped internal seam.

For the current first-bad construction the observer motion is finite variation, so
`Psi_mu=0` and the extra observer pair q.v. source vanishes exactly.  A one-mode
Kelvin audit checks that Brownian anchor covariance `2 nu` gives q.v. density
`2 nu (partial_a m)^2`, exactly the Kelvin carré-du-champ.

**Classification: Exact Itô identities and exact Kelvin stochastic calibration.**

The canonical same-ancestor source `2 nu q K delta_Delta` is structurally the same
diagonal carré-du-champ class, but no new coordinate-level identification is made
without a literal state map.  `S^int` remains undefined; no continuation/restart or
regularity conclusion follows.


## 2026-08-12 — vorticity/Kelvin microframe exposes the physical restart ledger

The restart frontier was returned to the literal incompressible Navier--Stokes
vorticity PDE before introducing any continuation norm.  Curl removes pressure as
an exact gauge sector and the velocity-gradient skew part annihilates its own
vorticity, leaving
`D_t omega = S omega + nu Delta omega`.  Material-line kinematics gives
`d|ell|^2/dt = 2 ell.S ell`, so for a vortex-line tangent the scalar
`alpha_vort = xi_omega.S xi_omega` is the literal logarithmic line-stretching rate.
The old phrase `alpha^2 tau` remains undefined and is not identified with this new
quantity.

For `omega=rho xi`, `|xi|=1`, the exact amplitude equation is
`D_t rho = rho alpha_vort + nu(Delta rho-rho|grad xi|^2)`.  The local enstrophy
identity is
`D_t (|omega|^2/2) = omega.S omega + nu Delta e - nu|grad omega|^2`.

The new bridge to the Kelvin sector is exact.  For a small closed disk loop with
normal `n` in the constant orthonormal noise frame, Stokes gives
`gamma(Z_r)/Area_r^2 -> 2 nu |(grad omega)^T n|^2`.  Summing over any orthonormal
triple of loop normals gives
`(1/2) sum_j gamma_dens(n_j)=nu|grad omega|^2`.  Thus an orientation-complete
Kelvin microframe is exactly the bulk viscous enstrophy-dissipation channel.

A rank-one loop can be exactly blind.  The exact periodic shear has two coordinate
loop normals with zero Kelvin density and only the third detects the nonzero
vorticity gradient.  Therefore a restart proof using Kelvin q.v. must contain an
orientation-complete packet or a proved equivalent coverage mechanism.

Small-loop raw action scales as area squared (`r^4` under linear scale), so a finite
raw bank does not control the local gradient density as scale shrinks.  For
`V_hat=V/A^2`, the exact continuous bank law has the additional dilation term
`-2(A_dot/A)V_hat`.  This is shell/refinement/zoom geometry, not stochastic
production and not `S^int`.

For a material germ volume the exact physical restart ledger is

`d/dt int_D e = int_D omega.S omega - (1/2) sum_j int_D gamma_dens(n_j) + nu int_boundary grad e.n`.

Advection disappears only because the domain moves with the fluid; pressure has
already disappeared by curl.  The remaining channels are therefore literal vortex
stretching production, Kelvin microframe bulk dissipation, and signed spatial/Hodge
boundary flux.  At a local enstrophy maximum, positive material growth requires
`omega.S omega > nu|grad omega|^2`; this is a necessary local growth gate, not a
first-bad threshold or continuation criterion.

Exact shear, Galilean-advected shear, and genuine 3D ABC/Beltrami calibrations
close the vorticity, enstrophy, and microframe identities.  The Galilean shear has
nonzero vorticity advection with zero stretching, preventing those mechanisms from
being conflated.  At the symmetric ABC enstrophy maximum, stretching is
zero, Kelvin bulk dissipation is `3 nu exp(-2 nu t)`, the spatial Laplacian term is
`-3 nu exp(-2 nu t)`, and `partial_t e=-6 nu exp(-2 nu t)`, demonstrating that
bulk q.v. dissipation and spatial flux are distinct physical channels.

**Classification: Exact identities plus rigorous structural consequences from
exact Navier--Stokes calibrations.**

At this stage the restart target was sharpened to an orientation-complete,
area-normalized packet.  The subsequent material-packet audit below refines this
further: passive dilation/rotation/shear cancel in the full GL(3) metric capacity,
while material metric work is the vortex-stretching channel itself.  The living
frontier is therefore the local future-covariance tensor/remainder law plus signed
material metric and physical boundary/exit work.  No continuation/restart theorem
and no regularity claim.


## 2026-08-12 — orientation-complete material packet turns stretching into metric work

The restart layer was lifted from one selected Kelvin loop to a three-loop packet per
first-bad germ.  The germ selector is now `M_fb tensor I_3` for this restart layer,
so one selected germ retains all three orientations and all nine ordered
cross-orientation pair slots.  A finite-chain CI witness verifies rank `3`, zero
one-current physical boundary, and zero full-pair physical boundary.

The full instantaneous packet q.v. is the shared-noise Gram matrix
`Gamma_mf=2 nu N^T (grad omega)(grad omega)^T N`.  Cross-orientation covariance is
physical: at the symmetric exact ABC enstrophy maximum CI obtains the matrix
`nu exp(-2 nu t) [[2,-1,-1],[-1,2,-1],[-1,-1,2]]`, including negative cross terms
and a blind diagonal normal `(1,1,1)/sqrt(3)` while the bulk payment remains
positive.

A general material loop packet is represented by its invertible oriented area frame
`H`.  The raw packet q.v. is `2 nu H^T(grad omega)(grad omega)^T H` and the exact
contravariant packet metric is `M=(H^T H)^(-1)`.  Their contraction satisfies
`(1/2) tr(Gamma_H M)=nu|grad omega|^2` for arbitrary non-orthogonal `H`.  More
generally `B(C,H)=(1/2)tr(CM)` is invariant under passive `GL(3)` packet
reparameterization.  Continuous rotation/dilation/shear and finite passive GL jumps
therefore have exact signed cancellation when covariance and metric are both kept.

If raw covariance has local tensor form `C_H=H^T C_local H`, the packet capacity is
exactly `tr(C_local)/2` at every invertible scale and shape.  For isotropic linear
scale `r`, the only surviving packet-normalized scale content is a non-tensorial
remainder: `R_r=r^pR_0` contributes exactly `r^(p-4)`.  Perfect tensorial dyadic
shrinking has zero capacity cost.

The material kinematics reveals the physical nonlinear channel.  Nanson gives
`D_t H=-(grad u)^T H`, while the NS vorticity equation gives
`D_t(H^T omega)=nu H^T Delta omega`; vortex stretching cancels exactly from material
flux coordinates.  With `Phi=H^T omega` and `M=(H^T H)^(-1)`, however,
`|omega|^2=Phi^T M Phi` and `(1/2) Phi^T Mdot Phi=omega.S omega`.  Thus literal
vortex stretching is material packet **metric work**, not production of vortex
flux.  Incompressibility preserves `det M` while allowing anisotropy to grow.

An amplitude-scaled exact ABC family supplies a no-go for a tempting closure:
`stretching/(instantaneous Kelvin bulk)=A exp(-nu t)/nu`, so instantaneous packet
q.v. alone cannot universally dominate stretching.

**Classification: Exact packet, GL(3), material-flux and metric-stretching
identities; rigorous no-go from an exact 3D NS family.**

The remaining restart question is narrower: establish a local future-covariance
tensor/remainder law uniformly near a candidate singular time and control the
metric-amplified remainder, signed physical boundary/exit terms, and covariance-
weighted material metric work.  `restart-capacity` and continuation/restart remain
open; no regularity claim.


## 2026-08-12 — full-state Kelvin covariance tensor meets the NS vorticity dyad

The restart frontier was pushed from finite orientation-packet algebra into the
conditional moment equation on the full stochastic Kelvin state.  For vector
terminal payoff `F`, conditional mean `m`, second moment `Q`, and covariance
`C=Q-mm^T`, the exact remaining-horizon laws are
`(partial_tau-L)C=Gamma_L[m]`, `(partial_tau-L)(mm^T)=-Gamma_L[m]`, and
`(partial_tau-L)Q=0`, with the complete mixed matrix carré-du-champ
`Gamma_L[m]=(grad m) a (grad m)^T`.  Thus martingale q.v. is an exact transfer from
conditional mean-square into future covariance, not a source of terminal second
moment.

The same tensor was recovered independently as the diagonal cross-derivation of the
same-ancestor pair generator.  At current level, double Stokes gives
`C(partial Sigma_i,partial Sigma_j)=<(d box d) K_s,Sigma_i box Sigma_j>`, where
`K_s` is the already existing pair momentum covariance cochain.  Boundary-squared-
zero makes exact pressure/gauge cochains invisible before taking any local limit.

This closes an earlier overly broad “tensor existence” gap at fixed regular state.
If the random terminal vorticity two-form `zeta=d beta` is conditionally mean-square
continuous at `x`, conditional Jensen implies the small-surface average converges in
conditional `L^2`; hence
`C_H^future=H^T C_local H+o(|H|^2)` with
`C_local=Cov_s(zeta(x))`.  For centered conditionally `C^2` packets the raw
non-tensorial covariance remainder begins at `r^6`, so metric normalization leaves
`O(r^2)` at fixed state.  No uniform singular-time constants are inferred.

Navier--Stokes supplies a matching deterministic tensor law:
`(partial_t+u.grad-nu Delta)(omega omega^T)=A omega omega^T+omega omega^T A^T-2nu grad(omega)grad(omega)^T`.
Thus the entire Kelvin Gram tensor is the viscous defect tensor of the vorticity
dyad; its half-trace is the previously audited enstrophy identity.  Exact shear and
ABC symbolic calibrations close the full `3 x 3` residual.

For additive Brownian Kelvin flow the causal backward-Ito packet mean operator is
fixed by Nanson and NS:
`[partial_t+u.grad-nu Delta-A^T H:grad_H](H^T omega)=0`.  An attempted future-terminal
shear covariance through this anti-diffusive physical-time operator failed and was
rejected.  Using the correct past terminal `t0<t`, exact shear instead gives
`D_K C=+G_K`, `D_K(omega omega^T)=-G_K`, and homogeneous total second moment.  This
exposes a new literal seam: the abstract forward future-ancestry bank and the
physical backward-Kelvin martingale need a line-by-line causal/time-state
identification before they are called the same bank.

Generator compatibility is also now explicit.  A reduced autonomous generator
requires `L R=R L_bar`.  Exact four-state audits show both a lumpable hidden-shape
model and a non-lumpable one with different physical exit rates on the same reduced
spatial fiber.  Therefore current shape/history cannot be dropped by declaration.

**Classification: Exact full-state conditional-moment, pair-generator,
double-Stokes, and Navier--Stokes tensor identities; rigorous conditional fixed-state
Stokes limit.**

Open: programme-specific full-state generator descent, forward-future/backward-
Kelvin causal identification, uniform singular-time diagonal trace/remainder,
material metric/boundary/exit capacity, literal `S^int` if separately intended, and
continuation/restart.  No regularity claim.
