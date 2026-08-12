# Research ledger

## 2026-08-12 — repository initialization

This repository was created as a standalone local Git project so the PDE-first/Kelvin programme does not modify or inherit the theorem spine of any other research repository.

### Current established structure

- Fixed physical Kelvin circulation: future conditional variance is the exact Doob bank for its quadratic variation.
- Selector switching: observer jumps do not create stochastic quadratic variation; they create exact covariance revaluation/reset terms.
- Canonical Kelvin mixed current: the germ differential of instantaneous Kelvin action is a signed polarization/Hodge transfer, not a standalone positive payment.
- Normalized ancestry law: it yields an exact distributed future-variance/current balance; Fisher/osmotic entropy is a distinct bank with a distinct conjugate potential.
- Strong-Hodge case: `q j_circ` is a closed occupation current and therefore globally performs zero work against an exact covariance potential; localization turns this into boundary-crossing covariance flux.
- Same-ancestor two-replica construction: future replicas must be independent after the **full physical** common ancestor. On the full diffusion state the continuous second-order branching source is the diagonal viscous tensor `2 nu q K delta_Delta`, not `q j_circ tensor j_circ`. A reduced ancestor has an additional conditional resolution-covariance face.
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

The full-state continuous same-ancestor source `2 nu q K delta_Delta` is structurally the same
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



## 2026-08-12 — backward-Kelvin full current-shape state resolves the generator dichotomy

The stochastic generator frontier was descended from an abstract hidden-state
question to the literal material current.  Constantin--Iyer/Eyink uniform Wiener
transport means all points of one current share the same Brownian increment.  With a
material anchor `X` and relative embedding `R`, the exact backward kinematics is
`d^-X=u(X)dt+sqrt(2nu)d^-W` and
`d^-R=[u(X+R)-u(X)]dt`.  Therefore relative shape has zero q.v.; the finite-cylinder
generator contains `-nu Delta_X` only in the anchor coordinate and first-order
velocity-difference drift in shape.

For differential area elements this closes exactly on `(X,H)` by Nanson.  For a
finite material surface the exact law is
`Hdot=-(grad u(X))^T H+E_shape`, where
`E_shape=-int_S[(grad u(y)-grad u(X))^T n]dA`.  This term is physical
finite-variation strain-gradient/surface-shape deformation.

The exact smooth Navier--Stokes heat shear
`u=(y^3+6 nu t y,0,0)` gives two centered `yz` rectangles with the same anchor and
same area vector `4 e_x`, but `E_shape=-4e_y` and `-16e_y`.  Thus finite-scale
`(x,H)` generator descent is rigorously false even in exact NS; orientation
completion does not encode higher surface shape.  The missing term is exactly
`-3 int_S y^2 dA e_y` in this calibration, exposing the surface quadrupole as the
first centered hidden shape state.  Under linear scaling `r`, the raw residual is
`r^4` while its size relative to area is exactly `r^2`.

This resolves the old binary generator-descent seam: full current-shape kinematics is
literal, infinitesimal `(x,H)` descent is exact, finite `(x,H)` descent is false, and
the living question is uniform collapse/control of the finite-shape hierarchy near
a candidate singular time.  The `r^2` order matches the centered covariance
localization remainder geometrically, but the two physical channels are not
identified.

**Classification: Exact stochastic/material identities + exact NS calibration +
rigorous structural consequence.  Uniform singular-time shape collapse,
forward-future/backward-Kelvin identification, restart capacity, and continuation
remain open.**



## 2026-08-12 — normalized ancestry time reversal turns the causal seam into a state-map question

The normalized ancestry operator was expanded before identifying any symbol with the
physical Kelvin drift.  For symmetric `K`, with
`L psi=w.grad psi+nu phi^{-1} div(phi K grad psi)` and `q=f phi`, define
`(c_phi)_j=phi^{-1} partial_i(phi K_ij)`.  The exact forward Itô drift is
`b_+=w+nu c_phi`; the exact time-reversed drift is
`b_-=w-nu c_phi-2nu K grad log f`; and the stored current velocity satisfies
`j=(b_++b_-)/2=w-nu K grad log f`.  The Fokker--Planck current is exactly `qj`.

Therefore the operator-level forward/backward orientation is no longer an open
bridge.  If the ancestry backward drift is the physical backward-Kelvin drift `u`,
then `w` is forced to be `u+nu c_phi+2nu K grad log f`.  Setting `w=u` by notation
alone leaves the explicit mismatch `-nu c_phi-2nu K grad log f`, classified as
reference-geometry plus time-reversal/osmotic drift rather than an internal source.

What remains open-literal is the actual state map from the ancestry variables
`(f,phi,K,w,...)` to the physical backward Kelvin anchor/current-shape state.  This
is especially nontrivial because the physical current-shape diffusion is degenerate:
common Brownian noise lives only in the anchor while relative shape has zero q.v.

**Classification: Exact weighted time-reversal/Fokker--Planck identities.  Physical
state identification, uniform singular-time shape/covariance collapse, restart
capacity, and continuation remain open.**


## 2026-08-12 — adversarial locality repair separates area, support, and whitened covariance

An independent audit found a genuine gap in the wording of the local future-tensor
bridge: `H_r -> 0` does not imply spatial support locality.  The exact incompressible
deformation `F_r=diag(r^-1,1,r)` sends an isotropic reference packet to
`H_r=diag(r^3,r^2,r)->0` while the largest transported line scale
`sqrt(det H_r)/sigma_min(H_r)` remains `1`.  A smooth flux witness
`X cos(x_1)e_2` then has an order-area payoff error and order-`r^4` covariance defect,
so the area-only local tensor statement is false.

The fixed-state theorem was repaired to the invariant topology
`H_r^{-T} epsilon_r -> 0` in conditional `L^2`.  A sufficient condition is support
diameter -> 0 together with
`sqrt(sum A_j^2)/sigma_min(H_r) * omega_2(diameter) -> 0`.  Raw Frobenius remainder
smallness is not enough: the long-thin witness has raw remainder small relative to
`|H|_F^2` while the metric-whitened contraction remains order one.  The general
Nanson determinant wording was also corrected: `D_t log det M_H=-4 div u`; only its
incompressible consequence `D_t det M_H=0` is used in the NS programme.

**Classification: Exact identities/counterexamples plus rigorous conditional
fixed-state repair.  Uniform singular-time packet locality remains open.**

## 2026-08-12 — ancestry reference gauge exposes the true state-map domain

The normalized ancestry coefficients have the exact gauge
`phi'=e^g phi`, `f'=e^-g f`, `w'=w-nu K grad g`.  The density `q`, current velocity
`j`, generator `L`, and both Ito drifts `b_+,b_-` remain unchanged.  Thus `f,phi,w`
are representation data, not independent physical hidden state coordinates.

Writing `K=BB^T`, the physical Kelvin fact that anchored relative shape has zero
quadratic variation forces `D Pi_shape B=0`.  Hence a positive-definite/full-rank
ancestry diffusion cannot encode nontrivial smooth Kelvin shape on an open region;
the true ancestry state must contain deterministic/null directions carrying shape,
or shape must be represented by enlarged path/history state.  The repository still
does not define the full ancestry state coordinate/manifold `y` line by line, so the
programme-specific state map remains definition-blocked rather than estimate-blocked.

**Classification: Exact reference-gauge/diffusion identities and rigorous generic
no-go; ancestry state manifold remains open-literal.**

## 2026-08-12 — same ancestor is state-resolution sensitive

The ancestry-state audit was generalized from deterministic state maps to a
conditional lift kernel `kappa(y,dY_K)`.  The exact law of total covariance gives a
new named physical object,
`C_res=Cov_kappa(m(Y_K))=1/2 int int (m(Y1)-m(Y2))^{otimes2} dkappa dkappa`.
It is the covariance created by conditioning on a reduced ancestry label that does
not resolve the full physical current shape.  It can be nonzero with zero full-state
future variance and even with zero hidden dynamics, so it is not viscous q.v.

An exact affine Navier--Stokes shear `u=(a y,0,0)` shows why the alternative
full-state interpretation is nontrivial: fixed relative shape evolves
deterministically while the anchor diffuses, giving a joint `(X,R)` covariance of
rank 3 in dimension 6 and determinant zero.  Hence a smooth positive density with
respect to ordinary full current-shape volume is not universal.  A full-state
ancestry route needs degenerate/submanifold/hypoelliptic measure geometry; a reduced
route needs `kappa` and its resolution pair face.

The old viscous branching tensor `2 nu q K delta_Delta` remains exact on the full
diffusion state.  Its scope is now explicit: it is not the whole pair content after
a state reduction.  No identification of `C_res` with the still-undefined
`S^int/Z_irr` is made.

**Classification: Exact identities and exact NS calibration; ancestry-state
semantics remain open-literal.**

## 2026-08-12 — resolved enstrophy and future covariance form one tensor bank

Combining the physical backward-Kelvin state `(X,F)` with the full-state covariance
law gives a general co-deforming identity.  `eta=F^-1 omega` has zero backward mean
residual and carré-du-champ
`Gtilde=2 nu F^-1 grad(omega) grad(omega)^T F^-T`.  The resolved mean dyad loses
`Gtilde`, future covariance gains `Gtilde`, and their sum is homogeneous in the
co-deforming frame.  After pushing forward physically,
`T_tot=omega omega^T+Sigma_fut` obeys only the common two-sided stretch operator.
Half-trace gives
`D_K^-(|omega|^2/2+B_fut)=tr(S T_tot)`: viscous q.v. is internal transfer between
resolved and unresolved second moment.  This retypes the restart obstruction as
strain work on the **total** second-moment tensor plus localization/boundary/exit and
finite-size/state-resolution faces.

**Classification: Exact full-state tensor identity.  No continuation claim.**

## 2026-08-12 — ideal coherent restart core collapses to `(rho,F,Q_tot)`

After the locality, deformation and future-covariance audits are combined, an
isotropically refined coherent infinitesimal packet has exact factorization
`L=rho F`, `H=rho^2 F^-T`, `Q_flux_raw=rho^4 Q_tot`, and
`T_tot=F Q_tot F^T`.  The packet metric is `rho^-4 F^T F`, so the ideal normalized
bank is exactly `tr(T_tot)/2`: physical scale cancels.  The variables have distinct
physical roles: `rho` is changed only by actual refinement/reselection, `F` carries
material support/strain, and `Q_tot` carries resolved plus unresolved Kelvin second
moment with viscous q.v. only as internal transfer.

The exact affine vortex-stretch calibration prevents an overclaim: the
support-normalized scalar `tr(Q_tot)/2` can stay constant while physical enstrophy
grows exponentially, so deformation/support geometry remains indispensable for
restart.  The remaining nonideal faces are finite quadrupole/locality error,
state-resolution covariance, and physical boundary/exit/reset currents.

**Classification: Exact factorization and exact NS no-go; no restart theorem.**

## 2026-08-12 — exact polynomial NS shears rule out finite shape-moment closure

The cubic heat shear identified the centered surface quadrupole as the first
finite-size shape carrier, but an exact quintic heat shear shows that quadrupole is
not a finite closure.  Two positive centered `yz` surfaces with widths
`1` and `1+(1/2)P_4(y)` have identical area and identical second moment by Legendre
orthogonality, while their fourth moments differ by `8/315`.  Under
`U_5=y^5+20 nu t y^3+60 nu^2 t^2 y`, an exact NS heat shear, their material area
rates differ exactly by `-(8/63)e_y`.

More generally, for every `m`, the perturbation `P_{2m}` preserves all lower even
moments while the exact heat shear `U_{2m+1}=exp(nu t d_yy)y^{2m+1}` detects the
`2m`-th moment.  Hence no finite centered surface-moment truncation universally
closes the exact finite current generator.  The physical shape hierarchy is real;
the viable restart route is uniform finite-shape collapse, not finite-dimensional
moment completion.

**Classification: Exact NS calibration family and rigorous structural no-go.**


## 2026-08-12 — Draft PR #1 clock/de Rham/moving-cut audit repaired

The open Draft PR #1 was read as an adversarial referee report rather than merged by
provenance.  Four proof-critical claims were checked against exact NS/Kelvin
calibrations.

First, the one-mode shear `u=e^{-nu k^2 t} cos(ka)` separates physical forward
Brownian time from the causal backward-Kelvin martingale: `(partial_t+nu d_aa)u`
equals `-2 nu k^2 u`, while `(partial_t-nu d_aa)u=0`.  Therefore the fixed-current
conditional-variance bank is exact only on one specified compatible Markov clock.
For a physical selector `a_t` and a separate horizon `tau`, the literal chain rule is
`d[a^T C(t,tau(t))a]/dt = a^T(C_t+tau_dot C_tau)a + 2 a^T C a_dot`.  The physical
first-bad/Kelvin two-clock lift remains open-literal.

Second, the old world-sheet equation `d_pair V-gamma ds=d_spacetime V` is false for
a second-order generator.  The exact one-mode law is
`(partial_tau-nu partial_aa)V=gamma`; with `s=Theta-tau`,
`partial_s V+gamma=-nu partial_aa V`, nonzero even at a symmetry anchor where
`gamma=0`.  The correct payment object is the exact divergence current
`partial_s(qV)+div(qjV+nu q K grad V)=-q gamma`.  Topological boundary-squared-zero
remains exact, but payment uses Dynkin/Fokker--Planck duality and the spacetime
divergence theorem.

Third, a moving cut has a distinct time face.  For `Q_s`,
`G_Q=Qdot+T_out Q-Q T_in`; in 1D Reynolds transport on `(-infinity,a(t))` gives
`d int q = q(a,t)(a_dot-v)=-qv+q a_dot`.  The boundary-speed term is not contained in
the static spatial commutator.  The pair lift has one such face per replica.  The
the generic quantile-current speed law is now exact; what remains open-literal is
its first-bad instantiation because the scalar germ observable and outer physical-time
lift are not defined.

Fourth, the PR objection to identifying centered covariance with deterministic
stretching is correct but already superseded on main by the exact split
`Q=C+mm^T` and `T_tot=omega omega^T+Sigma_fut`.  Its locality and general-Nanson
determinant findings were likewise already repaired.

**Classification: Exact one-mode NS/Kelvin counterexamples and exact generic
Dynkin/Reynolds identities; two-clock first-bad lift and literal moving-cut speed
laws open-literal.  No continuation/restart claim.**


## 2026-08-12 — reverse-age Kelvin clock and probability-current quantile law

A future conditional bank and a same-clock time-reversed diffusion are now kept
strictly separate.  For physical observation time `t` and reverse age
`sigma`, `r=t-sigma`, the full physical backward-Kelvin state has ordinary forward
reverse-age generator `L_K,rev(t,sigma)=-K^-_{t-sigma}`.  Hence a physical past-payoff
Kelvin covariance is literally a future covariance in reverse age.  Under a flat
identity-map ancestry bridge this uses `b_+=-u`; the earlier condition `b_-=u` is the
distinct same-clock backward-drift match.  Imposing both on one identity map forces
`b_++b_-=2j=0`.

For a fixed-mass chamber `{g<a_p}`, Reynolds plus
`partial_s q+div(qj)=0` gives the exact coarea speed
`a_dot = [int q/|grad g| (g_s+j.grad g)]/[int q/|grad g|]`; for `g=x` in one
dimension, `a_dot=j` exactly.  A zero-drift Gaussian heat flow already has moving
quantiles because `j=-nu grad log q`, so the moving cut cannot be tied to Itô drift
alone.  The repo still does not define the scalar germ observable `g` underlying its
first-bad quantile chamber, and one-clock ancestry continuity does not determine the
outer physical-time cut motion.

**Classification: Exact clock-reversal/current identities and exact diffusion
calibration; programme-specific ancestry/reverse-Kelvin intertwining and first-bad
quantile observable/outer-time law remain open-literal.  No restart claim.**


## 2026-08-12 — affine reverse-age quantile shells are integrated support geometry

For exact incompressible linear-strain NS `u=Ax`, the reverse-age anchor
`dX=-A X d sigma+sqrt(2nu)dW` has covariance
`Sigma_dot=-A Sigma-Sigma A^T+2nu I` and, for constant `A`,
`Sigma=2nu int_0^sigma exp(-Ar)exp(-A^T r) dr`.  The integrand is exactly reverse
material-line Cauchy--Green geometry.  For `A=diag(s,0,-s)`, the three variances are
`nu(1-e^-2s sigma)/s`, `2nu sigma`, and `nu(e^2s sigma-1)/s`; hence the Kelvin
parabolic scale is the leading term and strain supplies anisotropic `O(sigma^2)`
corrections.  The Gaussian probability current `j=-Ax+nu Sigma^-1 x` transports
the Mahalanobis shell `g=x^T Sigma^-1 x` pointwise: `g_sigma+j.grad g=0`.

**Classification: Exact affine NS/Gaussian calibration; no identification with the
programme first-bad shell without its missing scalar germ observable/state lift.**


## 2026-08-12 — first-bad projector is an event selector, not the moving cut

The literal hysteresis implementation was audited separately from the quantile/shell
restriction maps.  With an active `previous_index` and `resolved=False`,
`M_fb` is independent of every change in `bad_flags`; hence coordinate `Mdot_fb=0`
on frozen intervals.  Entry and resolve/reselection are finite jumps and use the
already exact full tensor-square reset law.  The input `resolved` is independent of
`bad_flags`: identical flags can keep the old germ or reselect a new first germ
depending only on this bit.

Therefore the programme has three distinct missing PDE definitions, not one: an
NS-derived badness score/threshold generating `bad_flags`, an NS-derived resolve
predicate generating `resolved`, and the separate scalar/state observable whose
level sets define moving `Q_s/H_s`.  The latter already has an exact Reynolds/coarea
probability-current speed law once specified.  Continuous germ-frame commutator
`A_g M-M A_g` may remain in non-co-moving coordinates, but it is not threshold
crossing `Mdot`.

**Classification: Exact implementation/event semantics and type separation;
badness functional, resolve predicate, and localization observable remain
open-literal.  No restart claim.**


## 2026-08-12 — exact periodic ABC excludes naive first-bad size thresholds

The arbitrary-amplitude periodic Beltrami family `u=A e^-nu t U_ABC` remains an
exact globally smooth NS solution for every finite `A`.  At the origin it has
`|omega|^2=3a^2`, `e=3a^2/2`, stretching `3a^3`, Kelvin bulk
`nu|grad omega|^2=3nu a^2`, ratio `a/nu`, and growth margin
`3a^2(a-nu)`, where `a=A e^-nu t`.  All are unbounded with `A` at fixed time.
Therefore no finite threshold on any one of these raw instantaneous quantities can
alone be a universal continuation-failure predicate, although they may remain
diagnostic/localization scores.

Referee scope is explicit: the origin is not an enstrophy critical point.  At the
symmetric ABC critical point `(pi/4,pi/4,pi/4)`, `grad e=0` and Beltrami stretching
is zero.  Thus this calibration does not falsify the already rigorous local-maximum
growth gate; that gate remains necessary only, not a first-bad theorem.

**Classification: Exact periodic NS calibration and rigorous candidate exclusion;
true badness/resolve definitions remain open-literal.**


## 2026-08-12 — support x total-bank algebra is scale-parametric; causal horizon requires a separate face

The support×bank factorization has been causally repaired.  Its exact object is a
coherent material support tensor `P_ell=ell^2 F F^T` at an arbitrary positive
physical scale `ell`, together with `omega=F eta` and
`Q_tot=eta eta^T+Ctilde`, `Ctilde>=0`, on the same state/frame.  The exact identity
`p q I-ell^2 omega omega^T = q(pI-P_ell)+ell^2 F(qI-Q_tot)F^T+ell^2 F Ctilde F^T`
splits the gap into support headroom, total-bank headroom, and unresolved covariance.
Thus aligned Loewner envelopes give the conditional algebraic rate
`|omega|^2<=p q/ell^2`.

The previous wording overtyped `ell^2=2nu(Theta-t)` as the causal physical
backward-Kelvin horizon.  The actual fixed-past Kelvin horizon is `h=t-t0`, with
`h_dot=+1`; the future candidate remaining time is `tau=Theta-t`, with
`tau_dot=-1`.  They are not equal for fixed `t0`.  Pointwise matching is possible
with the causal moving past terminal `t0(t)=2t-Theta`, for which `h=tau`, but then
`t0_dot=2` and every bank derivative gains the explicit terminal-motion face
`2 partial_t0`.  Exact one-mode NS shear audits both the homogeneous fixed-terminal
second-moment law and the moving-terminal q.v.+terminal-face covariance law.

Consequently a terminal `tau^-1/2` rate remains a **rigorous conditional
scale-parametric/two-clock consequence** if a same-state covariance family is paired
with the shrinking scale and `p q` is uniformly bounded.  The programme has not yet
proved that pairing, the first-bad parabolic scale identification, uniform envelopes,
nonideal face control, or continuation.

**Classification: Exact scale-parametric factorization and exact causal clock/terminal
calibration; scale--covariance horizon identification Open-literal; restart and
continuation open.**

## 2026-08-12 — fixed-past total bank reduces to stochastic Cauchy deformation plus covariance

For fixed causal past time `s<t`, the literal stochastic Cauchy contribution is
`Y_s=D_s^t omega(A_s^t,s)` and `E Y_s=omega(x,t)`.  With
`Q_s=E[Y_s Y_s^T]`, `C_s=Q_s-omega omega^T`,
`W_s=sup_y|omega(y,s)|^2`, and `R_s=E[D_s^t(D_s^t)^T]`, exact samplewise algebra gives
`W_s D D^T-Y Y^T=D(W_s I-w_s w_s^T)D^T`, hence
`omega omega^T<=Q_s<=W_s R_s`.  The full gap splits exactly as
`W_s R_s-omega omega^T=(W_s R_s-Q_s)+C_s`: terminal directional headroom plus
centered stochastic covariance.

In reverse age the deformation obeys `D_sigma=D(grad u)^T` and
`(D D^T)_sigma=2 D S D^T`, so `R_sigma=2 E[D S D^T]`; this is finite-variation
stochastic deformation work and is generally not closed on `R`.  Incompressibility
preserves `det D` pathwise but not its anisotropy/second moment.

Two exact NS calibrations separate the mechanisms.  In the genuine affine
vortex-stretch flow, vorticity and gradient are spatially uniform, centered covariance
is zero, and the z-deformation factor carries the full vorticity growth pathwise.  In
the one-mode shear the vorticity-direction deformation is one while the fixed-past
second moment/covariance is nontrivial and remains below the fixed terminal supremum.
Thus smooth past vorticity alone does not make the total bank a free bounded
reservoir; the remaining sufficient envelope is the stochastic Cauchy deformation
moment, with exact directional headroom quantifying looseness.

**Classification: Exact stochastic-Cauchy tensor identities and exact NS calibration
pair; uniform stochastic deformation control and alignment with selected support remain
open.  No restart claim.**

## 2026-08-12 — stochastic Cauchy deformation Gram equals the same-replica packet metric

On each stochastic Cauchy replica define `F_C=D^T`.  The reverse-age law
`D_sigma=D(grad u)^T` becomes the ordinary line-deformation law
`(F_C)_sigma=(grad u)F_C`.  For a coherent replica microcell of fixed reference
scale `rho`, `H_C=rho^2 F_C^-T`, so exact algebra gives
`D D^T=F_C^T F_C=rho^4 (H_C^T H_C)^-1`.  Hence the Cauchy deformation Gram is
exactly the unscaled orientation-complete packet metric on the same stochastic
replica, and `R_s=rho^4 E[M_HC]`.  Its strain work is the same metric work:
`rho^4 (M_HC)_sigma=2 D S D^T`.

This closes the geometric identity inside each replica but does not identify the
deterministic/hysteretic first-bad selected support with a stochastic Cauchy replica
or its expectation/projection.  That cross-state alignment remains open-literal.

**Classification: Exact same-replica deformation/packet-metric duality; selector-to-
replica alignment open-literal.**

## 2026-08-12 — general vectorized stochastic-deformation covariance law

The previous `C_D` notation was too compressed if read as the covariance of the
matrix-valued deformation itself. The literal reverse-age state is
`dX=-u(X,t-sigma) dsigma+sqrt(2nu)dW` together with the finite-variation law
`D_sigma=D(grad u)^T`, `D_0=I`. Hence pathwise `D` has zero direct martingale q.v.
For column-major `z=vec(D)`, the pathwise connection is
`K_path=(grad u) tensor I`. Conditioning from the fixed current endpoint reverses
the matrix ordering: with `H_h=partial_h+partial_t+u.grad-nu Delta`,
`H_h Dbar=(grad u)^T Dbar`; equivalently the vectorized horizon connection is
`B=I tensor (grad u)^T`.

Define the full covariance `Sigma_D=Cov(vec D)`. Then the exact connected law is
`H_h Sigma_D=B Sigma_D+Sigma_D B^T+Gamma_D^vec`, where
`Gamma_D^vec=2nu sum_mu vec(partial_mu Dbar) vec(partial_mu Dbar)^T`.

The packet-metric covariance is only the column partial trace
`C_D^Gram=E[D D^T]-Dbar Dbar^T=ptr_col Sigma_D`, and therefore obeys
`H_h C_D^Gram=(grad u)^T C_D^Gram+C_D^Gram(grad u)
 +2nu sum_mu (partial_mu Dbar)(partial_mu Dbar)^T`.
Both full and projected covariances have exact independent-two-replica pair forms.
Same-replica packet duality becomes
`rho^4 E[M_H]=Dbar Dbar^T+C_D^Gram`; it does not see every entry of `Sigma_D`, only
this row-Gram projection.

At a smooth current point,
`Sigma_D(h)=(2nu/3)h^3 sum_mu vec((partial_mu grad u)^T)
 vec((partial_mu grad u)^T)^T+O(h^4)`, and hence
`C_D^Gram(h)=(2nu/3)h^3 sum_mu (partial_mu grad u)^T
 (partial_mu grad u)+O(h^4)`.
Thus the candidate `3 x 3` formula is correct precisely as the row-Gram projection;
the full deformation covariance is `9 x 9` in three dimensions.

The exact periodic one-mode NS shear satisfies the mean, second-moment, projected
covariance, and full vectorized covariance PDEs symbolically. Its exact variance
starts at `(2nu/3)|partial_y U_y|^2 h^3`, fixing the positive source sign, transpose,
and coefficient. At `y=0` the deterministic selected deformation is exactly `I`
while stochastic replicas have positive `C_D^Gram`, so naive deterministic = expected
stochastic packet-metric alignment remains false. The exact affine-vortex NS
calibration has spatially uniform `grad u`, hence zero deformation-dispersion source,
as required.

Physical placement is now sharper. Under the reverse-age generator
`L_rev=-partial_t-u.grad+nu Delta`, the law is an exact specialization of the repo's
existing connected vector covariance theorem after the connection identification
`B_conn=-(I tensor (grad u)^T)^T`. The existing product-pair diagonal-defect theorem
returns exactly `Gamma_D^vec`. Thus the covariance algebraic face and same-ancestor
pair source were already present; the new physical sector is the literal Cauchy
deformation payload, reverse-age connection ordering, and causal-past clock.

`C_D^Gram` remains only the row-Gram projection covariance. Neither `Sigma_D` nor its
projection is automatically the future-remaining bank `tau=Theta-t` or the ancestry
resolution covariance. If an explicit reduced/full lift kernel `R` hides deformation,
the exact vector law of total covariance is
`Sigma_D^red=R Sigma_D+Cov_R(Dbar_vec)`. The first term is averaged intrinsic
same-clock deformation covariance; the second is a genuinely additional resolution
covariance with its own hidden-state two-replica form. Partial trace commutes with the
split, so the reduced packet-metric face contains both `R C_D^Gram` and the projected
resolution term. The actual programme-specific ancestry lift/kernel remains
open-literal. No part is called `S^int`, `Z_irr`, or irreducible without a theorem.

**Status: Exact identity** for the mean/second-moment/vectorized/projected covariance
laws, connected-theorem specialization, pair diagonal defect, and vector
law-of-total-covariance split. **Status: Rigorous consequence** for the local smooth
`h^3` asymptotic and PSD projections. **Status: Audited calibration** for one-mode
shear and affine-vortex NS. Cross-clock, actual reduced-state lift construction, and
deterministic-selected support identifications remain **Conjectural bridge /
Open-literal**. No restart, continuation, or regularity theorem is claimed.


## 2026-08-12 — Cauchy deformation / physical-current pair coupling

- **Exact identity:** the reverse-age Cauchy matrix acts on the spatial tangent fiber through `F=D^T`, while the first-bad selector/current map acts on chain/germ coefficients.  The literal local combined map is `T(P,D)=P tensor D^T`.
- **Exact identity:** physical boundary factorizes as `(B tensor I)T(P,D)=(BP) tensor D^T`.  Hence a closed selected Kelvin cycle stays closed replica by replica; the ordered pair boundary contains only the two chain faces and no autonomous deformation seam.
- **Exact identity:** for a fixed reference tangent `e`, `D^T e=(I tensor e^T) vec(D)`, so tangent covariance and every fixed local cochain readout are exact linear projections of the full `Sigma_D`.  They are not new covariance species.
- **Rigorous consequence:** the short-horizon cochain readout keeps the same cubic onset, `Var(alpha^T D_h^T e)=(2 nu/3) h^3 sum_mu [alpha^T (partial_mu grad u)e]^2+O(h^4)` for locally smooth NS coefficients.
- **Exact two-replica identity:** `T(P1,D1)-T(P2,D2)=T(P1-P2,D1)+T(P2,D1-D2)`.  Squaring gives selector, deformation, and mandatory cross pair terms.  A shared/frozen selector kills selector and cross sectors exactly; replica-dependent reselection does not.
- **Audited calibration / rigorous no-descent consequence:** exact cubic heat-shear NS gives two finite surfaces with the same anchor, initial local `D=I`, and the same area vector but different finite-surface shape currents (`-4 e_y` versus `-16 e_y`).  Existing polynomial/Legendre calibrations already exclude every universal finite even-moment closure.  Thus `D` is an exact local tangent transport but not a complete finite-current state.
- **Open-literal:** derive the same-ancestor pair law on the actual stochastic current-shape state `(X,R(.),D)` with the Kelvin cochain sampled along that moving current; only then test shrinking first-bad descent.  No `S^int`, future-bank, restart, continuation, or regularity identification is claimed.


## 2026-08-12 — Full current-shape Kelvin covariance and deformation–circulation cross block

- **Exact identity / physical typing:** on the literal reverse-age state `(r,X,R(.),D)`, only the material anchor has Brownian covariance `2 nu I`; relative shape and Cauchy deformation have zero direct q.v. and evolve by finite-variation velocity-difference / strain transport.
- **Exact Navier–Stokes / Cartan identity:** `(partial_t+L_u-nu Delta)u^flat=d(|u|^2/2-p)`, so the finite-variation drift of the actual moving circulation is pure Bernoulli/pressure gauge on a closed current.  Constant-frame Cartan gives `partial_Xmu <u^flat,Z>=<i_e_mu Omega,Z>` modulo an exact form killed by closedness.
- **Exact identity:** the same-ancestor full-state carré-du-champ is anchor-only and its Kelvin block is `Gamma_K(Z,Z')=2 nu sum_mu a_mu(Z)a_mu(Z')`.
- **Exact identity:** `C_DK=Cov(vec D,K_Z)` obeys `H C_DK=B_D C_DK+2 nu sum_mu vec(partial_mu Dbar) partial_mu Kbar`.  It is the off-diagonal block of the existing joint connected covariance theorem, not `S^int`, not resolution covariance, and not a new branching source.
- **Rigorous consequence for locally smooth NS:** the joint short-age hierarchy is `V_K=O(h)`, `C_DK=O(h^2)`, `Sigma_D=O(h^3)`, with leading coefficients `2 nu`, `nu`, `2 nu/3`.  The full leading block is exactly `2 nu sum_mu int_0^h [s v_mu;g_mu][s v_mu;g_mu]^T ds`, hence PSD by literal Gram geometry rather than a norm estimate.
- **Audited calibration (exact periodic NS):** one-mode shear gives an exact closed form for `Cov(c_h,K_h)`, satisfies the mixed horizon PDE and the joint connected theorem, and referees the sign/factor `nu h^2 U_yy U_y`.
- **Open-literal:** exact cubic/Legendre NS still blocks any finite-scale descent of the full current shape to `D`, area frame, or finite moments.  A theorem that genuinely shrinking/hysteretic first-bad support makes the full `R(.)` dependence descend to the local joint block is not proved.  No restart, continuation, or regularity theorem is claimed.

## 2026-08-12 — Literal finite-shape Kelvin descent error and covariance-only no-go

- **Exact identity / theorem-type correction:** the actual material current marched backward in reverse age has local tangent law `ell_sigma=-(grad u) ell` and oriented-area law `h_sigma=+(grad u)^T h`.  The same-replica Cauchy metric-dual frame `H_C=rho^2 D^-1` instead obeys `H_C,sigma=-(grad u)^T H_C`.  Therefore the old shorthand `Z_local(D,H)` was overtyped if `H` was read as the actual backward-current area; the two geometries have opposite connection signs and are not directly identified.
- **Exact Stokes identity:** for the actual finite surface `Sigma_R`, `epsilon_K=K_{Z(R)}-omega(X).h_R=int_Sigma [omega(X+r)-omega(X)].n dA`.  This is finite-support vorticity-inhomogeneity flux, not a norm remainder, q.v., pressure/gauge, resolution covariance, or `S^int`.
- **Exact reverse-age NS/Nanson/Itô identity:** `h_R,sigma=A(X)^T h_R+R_A`, with `R_A=int [A(X+r)-A(X)]^T n dA`; `d omega(X,r)=-A omega dsigma+sqrt(2nu) partial_mu omega dW_mu`.  Hence local stretching cancels and the descent error obeys `d epsilon_K=-omega.R_A dsigma+sqrt(2nu) sum_mu q_mu^err dW_mu`, where `q_mu^err=int [partial_mu omega(X+r)-partial_mu omega(X)].n dA`.
- **Exact pathwise typing:** `d[epsilon_K]/dsigma=2nu sum_mu (q_mu^err)^2`, but `[vec D,epsilon_K]=0` because `D` is finite variation.  Finite-horizon `Cov(vec D,epsilon_K)` can nevertheless be nonzero through the ordinary anchor carré-du-champ `2nu sum vec(partial_mu Dbar) partial_mu epsilon_bar`; this is the existing connected-covariance algebra, not a new branching source.
- **Rigorous local-smooth consequence:** the leading joint `(vec D,epsilon_K)` covariance is one Gram integral, giving `Var(epsilon_K)=O(h)`, `Cov(vec D,epsilon_K)=O(h^2)`, and `Sigma_D=O(h^3)`.  For a centered shrinking surface the deterministic bias, reverse strain-shape residual, and error noise coefficient are carried first by the oriented quadrupole `M_kl=int r_k r_l n dA=O(r^4)`; the error q.v. rate is therefore `O(r^8)` at a fixed smooth state.
- **Audited calibration / rigorous covariance-only no-go:** exact cubic heat shear `u=(y^3+6nu t y,0,0)` on a centered `xy` rectangle gives `epsilon_K=-4ab^3 !=0` exactly, independent of Brownian anchor, reverse age, and time.  Thus its drift, q.v., variance, and covariance with `D` are all exactly zero while the deterministic finite-shape bias survives.
- **Audited calibration:** exact periodic one-mode shear has nonzero finite-shape error q.v. and exact `D`/error cross covariance obeying the mixed horizon law with leading coefficient `nu h^2`; exact ABC/Beltrami NS has nonzero `-omega.R_A`, proving the finite-variation shape-drift face is physically active.
- **Audited calibration family / rigorous finite-moment no-go:** for every finite even-moment truncation, an odd polynomial heat-shear and Legendre `P_{2m}` surface pair match all lower even moments but have different deterministic Kelvin descent bias.  At the centered symmetry point the error q.v. coefficient is zero, so covariance bookkeeping is blind to the exposing unresolved mode.
- **Open-literal:** the surviving first-bad problem is a genuine shrinking-support/jet-collapse theorem for the actual material current controlling deterministic bias `epsilon_K`, shape drift `R_A`, stochastic residual `q_mu^err`, metric-whitened pair covariance remainder, and selector/boundary/exit/reset faces on one compatible physical state/clock.  No `S^int`, future-bank, restart, continuation, or regularity identification is claimed.

## 2026-08-12 — Exact reverse-age oriented surface-moment hierarchy

- **Exact identity:** for `M_alpha=int_Sigma r^alpha n dA`, reverse-age material surface kinematics give `Mdot_alpha=-sum_i alpha_i int r^(alpha-e_i) Delta u_i n dA+int r^alpha A(X+r)^T n dA`.  The two terms are literal relative-position transport and oriented-area transport; shape still has no martingale source.
- **Exact affine closure theorem:** if `Delta u=A r`, `Mdot_alpha=A^T M_alpha-sum_i alpha_i sum_j A_ij M_(alpha-e_i+e_j)`.  Every term has the same order `|alpha|`; affine velocity is the exact order-preserving case.
- **Exact homogeneous-polynomial / rigorous local-jet consequence:** a degree-`p` velocity jet couples moment order `m` to order `m+p-1`.  Nonlinear `p>=2` jets therefore make the low-moment hierarchy upward-coupled rather than finitely closed.
- **Audited calibration / centering no-go:** exact quadratic heat shear `u=(y^2+2nu t,0,0)` takes a centered `yz` rectangle with `M_y=0` and produces `Mdot_y=(8/3)b^3 c e_y !=0` from its quadrupole.  Material-anchor centering is not dynamically preserved.
- **Exact geometry / audited obstruction:** under anchor shift `r->r-c`, the vector-valued oriented first-moment matrix obeys `F->F-c h^T`; all first moments are centerable by one shift only if `F=c h^T`.  The quadratic shear generates a transverse component not removable by such a shift.
- **Exact shear identity:** for any shear `u=(U(y,t),0,0)` and an `xy` surface with normal `e_z`, every oriented `y`-moment is conserved.  This is the material mechanism behind the cubic heat-shear conserved finite-shape bias.
- **Exact polynomial jet/moment contraction:** polynomial Kelvin descent bias, reverse shape residual, and error-noise coefficients are exact contractions of vorticity/velocity-gradient jets with the same oriented moment tower.  A physically zero centered moment must be stored as zero; omission is not equivalent to zero.
- **Rigorous dynamic finite-truncation no-go:** the earlier Legendre static counterexample is now complemented by generator algebra: any finite low-moment cutoff is generically called by omitted higher moments under nonlinear spatial jets.  Smooth exact NS polynomial heat shears realize arbitrarily high degree.
- **Open-literal:** no theorem yet shows that the actual first-bad material support remains sufficiently shrinking/conditioned to make `M^(m)/ell^(m+2)` uniformly subordinate across the full tower.  No restart, continuation, `S^int`, or regularity conclusion is claimed.
