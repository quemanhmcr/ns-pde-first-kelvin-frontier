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

## 2026-08-13 — codeforming material-surface tower collapses to one nonaffinity field

- **Exact identity:** raw order-`m` oriented moments scale as `lambda^(m+2)` under
  isotropic physical refinement.  For `J=dS`, scalar normalization removes only
  `d`; the unit-determinant shape `S` acts nontrivially.
- **Exact identity:** with the actual reverse local line frame `L_dot=-A(X)L`, the
  pullback `xi=L^-1 r`, `a_tilde=cof(L)^-1 a` removes all local affine deformation.
  The only residual velocity is
  `N_L=L^-1[u(X+Lxi)-u(X)-A(X)Lxi]`.
- **Exact identity:** incompressibility gives `div_xi N_L=0` and the pulled-back area
  law `a_tilde_dot=(D_xi N_L)^T a_tilde`.  Therefore the whole infinite oriented
  moment tower is one material-surface transport system driven by `-N_L`.
- **Exact identity:** the generating current `G_L(theta)=int exp(theta.xi)a_tilde`
  reproduces every moment equation by theta derivatives.  Affine NS freezes the
  entire codeforming tower, not merely each raw moment order.
- **Exact identity:** homogeneous degree-`p` jets enter as
  `N_{rho S}^{(p)}=rho^(p-1) S^-1 U_p(Sxi)`; anisotropy conjugation is independent of
  scalar scale.  Coherent linear refinement is exact gauge for the pulled-back tower.
- **Audited calibration / rigorous no-go:** exact critical linear strain has constant
  codeforming tower but no support locality.  Supercritical refinement can be
  support-local while scalar-normalized area moments diverge.
- **Audited calibration / rigorous no-go:** exact quadratic heat-shear NS with
  shrinking `L_r=diag(r^3,r,r)` has `N_L=r^-1 xi_y^2 e_x`; support locality alone
  does not force codeforming affine collapse.
- **Open-literal:** a first-bad descent theorem must control both actual support and
  the tensorial nonaffinity jets `L^-1 (nabla^p u) L^tensor p`, together with existing
  selector/boundary/exit/reset faces.  No restart/continuation/regularity claim.

## 2026-08-13 — Kelvin descent is circulation of the codeforming nonaffinity one-form

- **Exact identity:** if `N_L=L^-1[u(X+Lxi)-u(X)-A(X)Lxi]` and `G=L^T L`, the
  physical nonaffine momentum one-form pulls back to `beta_L=G N_L`.
- **Exact Stokes--Piola identity:** `curl_xi(beta_L)=cof(L)^T[omega(X+Lxi)-omega(X)]`,
  and the finite Kelvin descent error is exactly `epsilon_K=oint beta_L.dxi`.
- **Exact identity:** the same underlying nonaffinity has three distinct physical
  faces: `xi_dot=-N_L`, `a_tilde_dot=(D N_L)^T a_tilde`, and Kelvin one-form
  `beta_L=G N_L`.  The first two are shape kinematics; the third is circulation.
- **Audited exact-NS calibration:** for quadratic heat shear with shrinking
  `L=diag(r^3,r,r)`, `N_L=r^-1 xi_y^2 e_x` diverges while
  `beta_L=r^5 xi_y^2 e_x` shrinks.  Therefore kinematic shape-affinity and
  instantaneous Kelvin descent are not equivalent.
- **Open-literal:** first-bad instantaneous Kelvin descent requires control of the
  metric-weighted one-form/curl on the actual selected current; dynamic shape descent
  separately requires the residual vector field/Jacobian plus physical current
  faces.  No restart/continuation/regularity claim.

## 2026-08-13 — codeforming representation of the finite-shape error SDE

- **Exact identity:** on the full reverse-age state, `L` and pulled-back shape have no
  direct Brownian q.v.; hence `q_mu^err=oint partial_Xmu beta_L . dxi` with
  `beta_L=(L^T L)N_L`.
- **Exact identity:** if `eta0=cof(L)^T omega(X)` and
  `htilde_dot=int(D N_L)^T a_tilde`, then the existing physical drift
  `-omega.R_A` is exactly `-eta0.htilde_dot`.
- **Exact codeforming SDE:** `d epsilon=-eta0.htilde_dot dsigma + sqrt(2nu) sum_mu
  (oint partial_Xmu beta_L.dxi)dW_mu`.
- **Audited calibration:** exact periodic one-mode NS shear reproduces both the finite
  rectangle descent error and its anchor-noise coefficient from the residual
  one-form.  This is a representation of the existing error process, not a new bank.

## 2026-08-13 — metric whitening is physical orientation reconstruction

- **Exact identity:** for common pointwise orientation density
  `g_H=H^T delta zeta`, `H^-T g_H=delta zeta`.  Whitening is the inverse orientation
  map, not an arbitrary norm at this level.
- **Exact Stokes--Piola identity:** for the same-time physical NS current,
  `H^-T curl_xi beta_L=omega(X+Lxi)-omega(X)` with `H=cof(L)`.
- **Exact physical typing:** for finite three-face error vector `epsilon_H`,
  `r_H=H^-T epsilon_H` is a reconstructed physical residual vector.  Its three
  components come from different faces, so it is not generally a pointwise field
  defect.
- **Audited exact-NS calibration:** cubic heat shear on the unit cube has center
  defect zero but finite reconstructed residual `-e_z/4`; isotropic scale `r` gives
  exactly `r_H=-r^2 e_z/4`.
- **Exact identity:** `|r_H|^2=epsilon_H^T(H^T H)^-1 epsilon_H`, and covariance/q.v.
  whiten by congruence.  Passive orientation-coordinate changes leave `r_H`
  invariant.
- **Exact covariance identity:** if `H^-T X_H=zeta+r_H`, then full covariance is
  `C_zeta+C_r+C_zeta,r+C_zeta,r^T`.  Cross blocks are mandatory at finite scale.
- **Exact scale--shape identity:** a homogeneous degree-p velocity jet gives
  `beta_{rho S}=rho^(p+1)S^T U_p(Sxi)`; whitening its Stokes density removes the
  area `rho^2` and returns the physical `rho^(p-1)` vorticity-defect scale.
- **Open-literal:** the metric-whitened topology now has exact fixed-state physical
  meaning, but no theorem gives uniform first-bad support locality/reconstructed
  residual collapse or identifies the future-bank clock/ancestry lift.  No restart,
  continuation, or regularity claim.

## 2026-08-13 — dynamic reconstructed finite Kelvin residual

- **Exact transfer identity:** `K-omega.h_local=(K-omega.h_actual)+omega.(h_actual-h_local)`.
  The actual-area error drift `-omega.R_A` and geometry-mismatch drift `+omega.R_A`
  cancel exactly; the corresponding martingale coefficients transfer in the same
  way.  Shape drift is moved between physical faces, not discarded.
- **Exact identity:** for the orientation-complete local frame `Hdot=A^T H`, the
  local flux `H^T omega` has zero reverse-age drift.  Since actual closed-current
  Kelvin drift is pure gauge, `epsilon=K-H^T omega` is a pure orientation-coordinate
  martingale with noise `Q=A_K-H^T grad omega`.
- **Exact identity:** `W=H^-T K` and `r=H^-T epsilon=W-omega` obey the common reverse
  material-line connection `-A`; `dr=-A r dsigma+sqrt(2nu) Qhat dW` with
  `Qhat=H^-T Q`.
- **Exact Itô identities:** `Gamma_r=2nu Qhat Qhat^T`,
  `Gamma_omega,r=2nu grad(omega) Qhat^T`; residual energy drift is
  `-r.S.r+nu||Qhat||_F^2`.  Full reconstructed q.v./dyad dynamics require both mixed
  local/residual cross blocks.
- **Audited exact-NS calibration:** cubic heat shear has nonzero reconstructed
  `r=-e_z/4` with zero drift/q.v. at the symmetry point.  Zero residual q.v. does not
  imply zero residual.
- **Audited exact-NS calibration:** one-mode periodic shear has a pure residual
  martingale in the `e_z` face and a generically nonzero local/residual cross q.v.
- **Open-literal:** the pathwise full-state law does not supply an autonomous reduced
  covariance PDE; full-state correlations, finite shape, selector/boundary/exit/reset,
  and clock/state lift remain.  No restart/continuation/regularity claim.

## 2026-08-13 — reverse-age co-deforming Kelvin martingale core

- **Exact identity:** for `Ldot=-A L`, incompressibility freezes `J=det L`; with
  `H=cof(L)`, `chi=L^-1 r=epsilon/J`, `eta=L^-1 omega`, and
  `kappa=K/J=eta+chi`.
- **Exact identity:** all three are driftless same-anchor reverse-age martingales:
  `d eta=sqrt(2nu) Gtilde dW`, `d chi=sqrt(2nu) Qtilde dW`,
  `d kappa=sqrt(2nu)(Gtilde+Qtilde)dW`.
- **Exact Gram identity:** the joint `(eta,chi)` q.v. is one PSD block Gram tensor;
  the local/residual cross block `2nu Gtilde Qtilde^T` is signed and mandatory.
- **Exact metric-work identity:** `|chi|^2/2` has only positive q.v. drift, while
  pushing `chi` to physical `r=L chi` recovers the signed `-r.S.r` strain term exactly
  as line-frame metric work.
- **Exact martingale consequence:** `E chi` is constant while centered covariance
  grows by the expected residual q.v.; deterministic bias and stochastic spread are
  separate physical faces.
- **Audited exact-NS calibration:** cubic heat shear has nonzero constant `chi=-e_z/4`
  and zero q.v., so covariance cannot remove mean finite-shape bias.
- **Audited exact-NS calibration:** a one-mode face spanning one full periodic `y`
  period has `K_z=0`, `chi_z=-eta_z`; positive local and residual q.v. diagonals are
  canceled exactly by a negative cross q.v., giving zero full-circulation q.v.
- **Exact clock identity:** reverse-age dyad q.v. source is the opposite sign of the
  existing physical-time backward mean-dyad source for the same pulled-back Gram.
- **Open-literal/Open:** no first-bad theorem forces mean bias and covariance to
  vanish simultaneously with support locality; reduced-state and future-bank bridges
  remain open.  No restart/continuation/regularity claim.

## 2026-08-13 — Physical frame-weighted codeforming Kelvin residual

- **Exact identity:** the reverse codeforming residual is a material coordinate; the physical residual is `r=L chi`, so the literal pathwise energy is `chi^T L^T L chi`.
- **Exact fixed-frame / conditional identity:** for fixed geometry, `E|r|^2=m_chi^T M_L m_chi+tr(C_chi M_L)`, separating physical deterministic bias from physical stochastic spread.
- **Exact full-state pair identity:** if the line frame is random, mean metric times mean residual second moment is not closed.  Two equal replicas require the signed mixed face `(1/4) tr[(M1-M2)(Q1-Q2)]`.
- **Audited calibration / target correction:** exact quadratic heat shear has `epsilon_z=-rho^3`, `chi_z=-1`, but `r_z=-rho -> 0`; raw codeforming mean-bias collapse is therefore not necessary for physical descent.
- **Audited calibration / spread correction:** exact one-mode shear on an asymmetric shrinking face has `q_chi -> -(1/2)U_yyy` generically nonzero while the physical noise `rho q_chi ->0`; raw codeforming q.v./spread collapse is not necessary either.
- **Exact homogeneous scale law:** a degree-`p` nonaffine jet has physical weighted residual energy `rho^(2p-2)`; at `p=2` the raw codeforming residual is order one while the physical energy is order `rho^2`.
- **Open:** the corrected first-bad target is the literal full-state `E[chi^T L^T L chi]` together with random-frame correlation and all selector/refinement/boundary/exit/reset faces.  Support locality remains a separate physical requirement.  No future-bank, restart, continuation, or regularity theorem is claimed.

## 2026-08-13 — Directional/refinement balance of the weighted Kelvin residual

- **Exact directional identity:** if `M=V diag(sigma_i^2)V^T`, then `tr(MQ)=sum_i sigma_i^2 v_i^T Q v_i`; at fixed geometry this becomes `sum_i sigma_i^2[(v_i.m_chi)^2+v_i^T C_chi v_i]`.  No max-singular-value norm is used.
- **Exact literal refinement law:** repo convention `L_+=L_-R` gives `M_+=R^T M_- R`.  This is only the geometry face; it does not define the post-event residual second moment.
- **Exact finite midpoint law:** `Delta tr(MQ)=tr(Qbar Delta M)+tr(Delta Q Mbar)`, separating signed geometry reweighting from signed current/residual revaluation without imposing an event ordering.
- **Exact passive-GL gauge calibration:** `M_+=R^TMR`, `Q_+=R^-1 Q R^-T` leaves total weighted energy invariant although the midpoint geometry/state faces are individually nonzero and cancel.
- **Exact full random-state law:** finite events require a third signed face `Delta C_MQ` for metric--residual correlation.  The energy ledger therefore has geometry, current-content, and correlation event faces.
- **Exact smooth law:** for `M=rho^2 A`, `E_dot=2(rho_dot/rho)E+rho^2 tr(Q A_dot)+tr(Q_dot M)`.  Under reverse incompressible material transport the first term vanishes and the law becomes physical strain work plus residual q.v. content.
- **Exact homogeneous refinement:** degree-`p` residuals give `E_+=lambda^(2p-2)E` under isotropic physical refinement.
- **Audited calibration / seam no-go:** exact quadratic heat shear with `L=diag(1,rho,rho)` has `chi=-e_z`, physical residual `r=-rho e_z` and weighted energy `rho^2 -> 0`, while the x support line remains exactly length one.  Weighted Kelvin descent does not imply support locality.
- **Open:** actual first-bad support locality and directional weighted residual products must be controlled simultaneously on the same migrating selected state, with correlation, pair refinement, selector, boundary, exit, and reset faces retained.  No restart/continuation/regularity theorem is claimed.

## 2026-08-13 — Pathwise spectral channels and principal-axis traffic

- **Exact spectral-projector identity:** `tr(MQ)=sum_alpha lambda_alpha tr(P_alpha Q)` pathwise.  Averaging this representation keeps random geometry--residual correlation inside each realization instead of factorizing mean metric and mean residual tensors.
- **Rigorous consequence:** the projector channels are nonnegative for `Q>=0`; in 3D weighted residual collapse is equivalent to collapse of every expected spectral-block channel, with support locality still separate.
- **Exact simple-spectrum connection:** with `B=V^T Mdot V`, `Omega_ij=B_ij/(lambda_j-lambda_i)` and `lambda_i_dot=B_ii`.  The API rejects repeated eigenvalues rather than emitting a singular principal-axis connection.
- **Exact channel traffic law:** `E_i=lambda_i Qtilde_ii` has eigenvalue-stretch, residual/current-content, and eigenframe-mixing faces.  The total mixing is exactly `2 sum_{i<j} B_ij Qtilde_ij`, the off-diagonal metric work.
- **Audited calibration:** exact linear NS shear `u=(gamma y,0,0)` with anisotropic frame `diag(2,1,3)` gives `Omega_12=2 gamma/3` and activates nonzero principal-axis mixing whose total is exactly the off-diagonal strain/metric work.
- **Exact degeneracy gauge:** within a repeated-eigenvalue subspace, individual axes are gauge but the projector-block energy `lambda tr(PQ)` is invariant under internal orthogonal rotations.
- **Open:** control pathwise spectral channel products on the same first-bad packet as support locality and all physical event faces.  No future-bank/restart/continuation/regularity theorem is claimed.

## Selected principal Kelvin lineage

- **Exact identity:** the cycle-typed diagonal rank-one first-bad selector lifts as `M_fb tensor I_3` and commutes with per-germ block-diagonal spectral fiber operators; the full pair lifts commute as well.  Generic germ mixing need not commute, so the theorem is typed to the literal first-bad selector.
- **Exact identity:** the selected endpoint weighted energy is the sum of the selected germ's spectral-projector channels.  Off-diagonal germ pair blocks remain in the full library state and enter finite selector resets.
- **Exact identity:** once a physical common-fiber synthesis `A=[a_i I_3]` is actually specified, `Q_A=A Q_lib A^T` and the pair map is `A tensor A`; each parent spectral channel contains every ordered child pair, including cross-child blocks.
- **Audited calibration:** exact half-period one-mode NS finite residuals are opposite.  The full `(1,1)` parent spectral channel vanishes while diagonal-only child channels are positive and are cancelled exactly by cross-child content.
- **Exact conditional event identity:** on a frozen/conditioned residual library a finite selector reset has four signed weighted faces: metric geometry, pair-left, pair-right, and pair-quadratic.
- **Audited calibration:** the exact one-mode selector reset has equal endpoint energies, negative left/right pair faces, and positive quadratic face with exact cancellation.  The closed `g0 -> g1 -> g0` excursion has positive accumulated quadratic path length but zero net revaluation.
- **Exact projector-gauge obstruction:** endpoint spectral projector blocks are canonical, but individual principal axes do not canonically match across a finite event without an explicit transport map; degeneracy makes that obstruction literal.
- **Rigorous conditional composition:** on one compatible clock, frozen-selector simple-spectrum intervals use stretch/content/eigenframe-mixing traffic and finite hysteresis events use geometry plus full pair reset; at degeneracy use projector blocks.
- **Open-literal:** the actual moving first-bad current-to-reconstructed-residual refinement lift is not yet derived; neither are the badness/resolve predicates, moving quantile/shell outer-time law, or cross-event principal-axis transport.  Support locality, uniform selected-channel collapse, future-bank/ancestry identification, restart, continuation, and regularity remain open.

## Frame-aware Kelvin residual refinement

- **Exact current/cochain identity:** for an orientation-complete linear current synthesis `Z_{P,a}=sum_{i,b}(R_i)_{ab}Z_{i,b}`, both circulation and oriented-area-vector readouts transform by the same blocks: `K_P=sum R_i K_i`, `H_P^T=sum R_i H_i^T`.  Hence `epsilon_P=sum R_i epsilon_i` for the same local field.
- **Exact identity / uniqueness:** whitening forces `r_P=sum A_i r_i` with `A_i=H_P^-T R_i H_i^T`; no unchanged child weights are available unless the frames actually make them so.
- **Exact gauge identity:** independent passive parent/child orientation bases transform `R_i` as `S_P^T R_i S_i^-T`, leaving `A_i` invariant.
- **Exact cofactor identity:** with `H=cof(L)` and `J=det L`, `A_i=(J_i/J_P)L_P R_i L_i^-1`.
- **Exact codeforming identity:** `B_i=L_P^-1 A_i L_i=(J_i/J_P)R_i`, so all anisotropic parent/child line-frame conjugation cancels in codeforming coordinates.
- **Exact scale law:** isotropic reconstructed physical weights carry `(rho_i/rho_P)^2`; codeforming weights carry `(rho_i/rho_P)^3`.
- **Audited exact-NS calibration:** quadratic heat-shear child packets of scales `rho_i` give parent `r_z=-(sum a_i rho_i^3)/(sum a_i rho_i^2)` and the corresponding volume-weighted codeforming residual, disproving naive unchanged scalar child weights.
- **Exact pair consequence:** frame-aware second moments and parent spectral channels use the full ordered child-pair `A tensor A` / `B tensor B` functor; cross-child content remains mandatory.
- **Frontier correction:** the broad physical-residual refinement lift is now audited-conditional once an orientation-complete current packet map is supplied.  The surviving refinement seam is **Open-literal:** instantiate the actual moving first-bad parent/child packet blocks `R_i`.  Support locality, selected-channel collapse, moving-cut time faces, ancestry/future-bank identification, restart, continuation, and regularity remain open.
- **Exact orientation-complete scalar refinement lift:** the existing current law `Z_parent=sum_i w_i Z_i` canonically gives `R_i=w_i I_3`, `R_i tensor R_j=w_i w_j I_9`; the exact interval chain refinement tensors with `I_3` and remains a chain map.  Thus orientation-preserving scalar refinement is structurally instantiated.  The remaining first-bad packet-map seam concerns actual event weights and any genuine orientation mixing/reselection.

## Spectral Kelvin event transfer

- **Exact identity:** after frame-aware synthesis `Q_P=sum_{ij}A_i Q_ij A_j^T`, each parent spectral channel is `E_{P,alpha}=sum_{i,j,beta,gamma} lambda_{P,alpha} tr(P_{P,alpha} A_i P_{i,beta} Q_ij P_{j,gamma} A_j^T)`.
- **Exact sector partition:** same-child/same-channel, same-child/cross-channel, cross-child/same-index and cross-child/cross-index terms sum to the exact parent channel.  Channel-index equality is bookkeeping, not physical axis ancestry.
- **Audited generic mechanism:** a frame-aware event block can route one child spectral projector into a different parent projector.
- **Exact degeneracy law:** projector transfer contains no spectral-gap denominator; changing an internal rank-one basis inside a repeated-eigenvalue block changes subterms but not the block-total transfer.
- **Audited exact-NS calibration:** half-period one-mode NS has positive same-child `z`-channel traffic and equal negative cross-child traffic, yielding zero parent channel exactly.  The signed cross-child sector is physically active.
- **Frontier correction:** individual cross-event principal-axis matching is a noncanonical target and is no longer an open theorem requirement; exact projector-pair transfer is the invariant substitute.
- **Open-literal:** the actual first-bad event map/state (`R_i`, hence `A_i`, plus the literal child pair state) is still not instantiated line by line.  Support locality, uniform selected-channel collapse, moving-cut clocks, ancestry/future-bank identification, restart, continuation, and regularity remain open.

## Kelvin finite-event normal form

- **Exact gauge normal form:** with invertible endpoint area frames, `R <-> A=H_P^-T R H_C^T`; `A` is invariant under passive packet bases and reconstructs `R` uniquely.
- **Exact codeforming normal form:** `B=(J_C/J_P)R` and `R=(J_P/J_C)B`.
- **Exact event composition:** `A_PC=A_PM A_MC`; the intermediate area frame cancels.  Codeforming maps compose with exact cancellation of the intermediate determinant.
- **Exact second-moment/pair functor:** sequential linear events satisfy `A2(A1 Q A1^T)A2^T=(A2A1)Q(A2A1)^T` and `(A2 tensor A2)(A1 tensor A1)=(A2A1) tensor (A2A1)`.
- **Exact spectral telescope:** complete intermediate projector resolutions sum out of the composite parent channel; internal bases of a degenerate intermediate block also telescope.
- **Audited PSD no-go:** two PSD states with the same diagonal spectral channel vector `(1,1,0)` but opposite off-diagonal coherence respond differently under the same next event; scalar channel lists are not a closed compositional state.
- **Frontier:** specified same-clock linear packet-event algebra is structurally closed modulo passive gauge.  What remains Open-literal/Open is the NS-generated first-bad event choice/map/state, support locality, full selected pair/projector control, moving-cut faces, and cross-clock ancestry/future-bank identification.  No restart/continuation/regularity theorem is claimed.
- **Exact polarization / audited-conditional observational completeness:** for the unrestricted linear event-probe class, coordinate probes `e_i` and pair-sum probes `e_i+e_j` reconstruct every symmetric second-moment entry `Q_ij`.  Thus full symmetric `Q` is complete for all such quadratic event responses, while diagonal channel data is not.  No claim is made that actual first-bad events realize all probes or that `Q` is minimal for that smaller physical event family.

## First-bad selected residual readout semantics

- **Exact type identity:** the active residual is `r_g=E_g X`, a coordinate readout from the persistent candidate germ/fiber library; selector choice is not itself a physical packet map.
- **Exact obstruction / audited counterexample:** for distinct germs no universal `T` satisfies `E_h=T E_g` on the full library.  Explicit states share the old selected residual and differ after the switch.
- **Exact pair reset:** `Q_h-Q_g=DeltaE Q E_g^T+E_g Q DeltaE^T+DeltaE Q DeltaE^T`.  For two germs the faces are `Q10-Q00`, `Q01-Q00`, and `Q11-Q10-Q01+Q00`; the old selected block alone does not contain them.
- **Audited PSD no-go:** two PSD full-library second moments can share the old selected block and have different switched blocks.
- **Exact conditional bridge:** selected-to-selected factorization on an admissible state family requires an independently supplied relation `E_h S=T E_g S`.
- **Exact event/selector typing:** after a genuine full-library physical event, the post-selected map is `E_post A_full`; reduction through the old selected state requires `E_post A_full=T E_pre` and fails generically for a genuine selector switch.
- **Rigorous architecture consequence:** arbitrary hysteretic switching requires a persistent library/full pair state plus an active selected observer.  The selected endpoint state alone is not universally compositional.
- **Open-literal:** Navier--Stokes/programme dynamics for the persistent first-bad candidate library and any programme-specific admissible inter-germ relations are still not defined line by line.  Support locality, moving-cut clocks, ancestry/future-bank identification, restart, continuation, and regularity remain open.

## Same-replica persistent residual-library dynamics

- **Exact conditional library law:** for a finite physical packet library carried by one stochastic-flow replica, stack the codeforming residual noises as `Qstack=[Q_1;...;Q_N]`; then `dChi=sqrt(2nu)Qstack dW` with one common three-dimensional Wiener motion.
- **Exact Gram identity:** `Gamma_lib=2nu Qstack Qstack^T`, with cross-germ block `2nu Q_g Q_h^T`; the instantaneous q.v. image has rank at most three.
- **Exact selector/event typing:** a frozen selector reads one diagonal q.v. block, while a specified linear physical event sends `Gamma` to `A Gamma A^T`.
- **Exact martingale consequence:** mean library bias is constant and centered spread is generated by the full expected same-replica Gram under the stated integrability/adapted-coefficient scope.
- **Exact model distinction:** independent per-germ Brownian drivers delete physical same-replica cross-germ q.v. and define a different stochastic model.
- **Audited exact-NS calibration:** two one-mode packets in the same replica have opposite residual anchor-noise coefficients, negative cross-germ q.v., and zero synthesized common-noise q.v.; the independent-noise counterfactual is strictly positive.
- **Frontier correction:** persistent library dynamics is structurally audited-conditional once a finite same-replica physical packet library is specified.  The actual first-bad candidate library, its packet/replica/clock semantics, moving cuts, support locality, future-bank/ancestry identification, restart, continuation, and regularity remain open.

## Selected residual hybrid semimartingale

- **Exact frozen-branch law:** `dY=sqrt(2nu)E_g Qstack dW` and `d[Y]^c/dsigma=E_g Gamma_lib E_g^T`.
- **Exact selector-only jump:** with continuous library state, `DeltaY=(E_+-E_-)Chi`; the selector creates no continuous Brownian q.v. source.
- **Exact càdlàg q.v. clarification:** total optional q.v. adds the finite jump square `DeltaY DeltaY^T`.  This jump variation is physically distinct from the continuous stochastic producer.
- **Exact reset dyad:** `Delta(YY^T)=DeltaY Y_-^T+Y_- DeltaY^T+DeltaY DeltaY^T`; jump q.v. is only the quadratic reset face.
- **Audited no-bank calibration:** a closed selector excursion can return to the identical selected state with positive accumulated jump-square.
- **Audited exact-NS calibration:** the half-period one-mode packets realize this closed excursion exactly, so positive selector jump q.v. is not a monotone physical covariance/uncertainty bank.
- **Open-literal:** the hybrid law does not generate badness/resolve timing, choose simultaneous physical packet events, or identify the programme cross-clock ancestry/future bank.  Restart, continuation, and regularity remain open.


## Simultaneous physical packet event + selector switch

- **Exact identity:** post-event selected readout is `E_+ A X`; the jump operator is `D=E_+ A-E_-`.
- **Exact identity:** on a common library space, `D=E_- DeltaA+DeltaE+DeltaE DeltaA`; the mixed `DeltaE DeltaA` face is mandatory finite physical--selector interaction.
- **Exact identity:** equivalently `D=E_- DeltaA+DeltaE A=DeltaE+E_+ DeltaA`.
- **Exact identity:** selected second-moment jump is `D Q E_-^T+E_- Q D^T+D Q D^T`; jump optional q.v. is only the quadratic pathwise face.
- **Audited calibration:** exact half-period one-mode NS residuals plus the specified current synthesis `g_1 -> g_1+g_0` give zero old-selector physical face, nonzero selector and mixed faces, and prove naive physical-plus-selector additivity false.
- **Rigorous conditional composition:** with supplied same-clock library/event/selector data, continuous Brownian and all finite linear selected-event faces are now literal.
- **Open-literal:** actual first-bad badness/resolve timing, physical event map/state, support locality, and cross-clock/future-bank identification.
- **Open:** restart/continuation/regularity.


## Continuous Brownian-source revaluation across combined selected events

- **Exact identity:** pre/post selected noise responses are `B_-=E_- N` and `B_+=E_+ A N`; endpoint continuous q.v. rates are `2nu B_-B_-^T` and `2nu B_+B_+^T`.
- **Exact identity:** with `dB=(E_+A-E_-)N`, the signed rate revaluation is `2nu[dB B_-^T+B_- dB^T+dB dB^T]`.
- **Exact physical typing:** the signed difference of two PSD q.v. rates is a finite source-rate revaluation, not negative Brownian production.
- **Rigorous consequence:** continuous source-rate revaluation and finite jump optional q.v. are independent state functions; either can vanish while the other is nonzero.
- **Audited calibration:** exact one-mode NS has opposite same-replica packet noises; selector-only rate is unchanged, but hidden synthesis `g_1 -> g_1+g_0` followed by `0 -> 1` makes the actual post-event continuous q.v. rate exactly zero.
- **Rigorous conditional composition:** continuous source, finite state jump, jump q.v. atom, source-rate revaluation, and second-moment reset are now separately typed on supplied same-clock paths.
- **Open-literal:** actual first-bad library/badness/timing/event maps and cross-clock/future-bank identification.
- **Open:** restart/continuation/regularity.


## Random/adaptive selected-event map correlation

- **Exact identity:** two-replica mean output is `Cbar xbar + (1/4) DeltaC Deltax`; mean event map x mean state is not universal when event choice is state dependent.
- **Exact identity:** `E_2[C Q C^T]` has four faces: mean-map/mean-payload, positive event-map dispersion, and two signed event--state correlation faces.
- **Rigorous consequence:** fixed event map removes all event-randomness faces; fixed payload leaves pure positive event-map dispersion.
- **Audited calibration:** PSD aligned replicas give `1+1+1+1=4`; PSD anti-aligned replicas give `1+1-1-1=0`.
- **Exact identity:** the same congruence law applies to continuous q.v. Gram payloads.
- **Rigorous structural consequence:** adaptive first-bad expectation/covariance bookkeeping requires the joint event-map/library law; `mean C x mean Q x mean C^T` is not an identity.
- **Open-literal:** actual first-bad badness/resolve rule, adaptive event map, event/state joint law, and clock identification.
- **Open:** restart/continuation/regularity.


## Necessary physical admissibility of any future first-bad rule

- **Exact identity:** passive packet basis `H->HS`, `epsilon->S^T epsilon` leaves `r=H^-T epsilon` and `|r|^2` invariant; raw `|epsilon|^2` is not invariant.
- **Audited calibration:** two fixed physical germs have raw scores `(1,9/4)`; a passive basis change on germ 0 gives `(4,9/4)` and flips the raw winner `1->0`, while physical scores/ranking remain unchanged.
- **Exact gauge identity:** raw event blocks transform equivariantly under independent parent/child packet bases while physical event map `A=H_p^-T R H_c^T` is invariant.
- **Audited exact-NS calibration:** gauge-correct physical residual energy `rho^2->0` does not imply support locality; one physical support line remains exactly length one.
- **Rigorous consequence:** genuine hysteretic switches require persistent-library state; old selected endpoint/second moment is not universally compositional.
- **Audited PSD calibration:** identical diagonal spectral channels can have different cross coherence and differ by exactly `2` under the same later linear event.
- **Rigorous consequence:** adaptive first-bad expectation-level bookkeeping requires the event-map/state joint law, not mean map x mean payload.
- **Necessary only:** no sufficient first-bad functional, restart, continuation, or regularity theorem is claimed.
- **Open-literal:** actual Navier--Stokes badness/resolve functional and event generation.


## Local enstrophy growth gate = stretching - Kelvin bulk + curvature

- **Exact identity:** `(partial_t+u.grad-nu Delta)(|omega|^2/2)=omega.S.omega-nu|grad omega|_F^2`.
- **Exact physical typing:** `nu|grad omega|_F^2` equals the metric-normalized orientation-complete Kelvin small-loop q.v. bulk for every invertible area frame.
- **Exact identity:** at `grad e=0`, `partial_t e=stretching-Kelvin_bulk+nu Delta e`.
- **Rigorous consequence:** at a local maximum `Delta e<=0`, positive margin `stretching-Kelvin_bulk>0` is necessary but not sufficient for positive time growth; it must exceed `-nu Delta e`.
- **Exact Beltrami scope theorem:** for the full ABC family, `omega.S.omega=u.grad e`; every enstrophy critical point therefore has zero stretching scalar.
- **Audited exact-NS calibration:** affine vortex has spatially uniform enstrophy, zero Kelvin bulk, positive stretching `8 a r(t)^2`, and exact `partial_t e=8 a r(t)^2`.
- **Exact theorem-domain correction:** the affine calibration is nonperiodic/non-finite-energy, so it types the local mechanism but does not refute a target-class global criterion.
- **Open-literal:** bridge from local growth mechanics plus packet/support/event structure to actual first-bad continuation failure.


## Moving enstrophy critical-point geometry

- **Exact conditional identity:** differentiating `grad e(x_*,t)=0` gives `H_e xdot_* + partial_t grad e=0`; if `H_e` is invertible, `xdot_*=-H_e^-1 partial_t grad e`.
- **Exact conditional NS identity:** `H_e(xdot_*-u)+grad[stretching-Kelvin_bulk+nu Delta e]=0`.
- **Exact physical split:** relative critical speed has stretching-gradient, Kelvin-bulk-gradient, and curvature-gradient faces.
- **Exact identity:** along a critical path, `d e(x_*(t),t)/dt=partial_t e`; critical-path speed does not enter the first value derivative.
- **Audited exact periodic-NS calibration:** ABC strict maximum at `(pi/4)^3` has invertible negative Hessian, nonzero fluid velocity, but fixed critical position `xdot_*=0`.
- **Audited exact-NS degeneracy calibration:** affine uniform enstrophy has `H_e=0`; distinct critical-path velocities satisfy the same constraint, so inverse-Hessian speed is not canonical through degeneracy.
- **Open-literal:** identification of the programme first-bad observable with a differentiable nondegenerate enstrophy-max branch and reconciliation with selector/refinement events.


## Enstrophy critical-Hessian evolution and curvature volume

- **Exact conditional identity:** along a differentiable critical branch, `Hdot=Hess(R)-(grad u)^T H-H grad u+((xdot_*-u).grad)H`, with `R=stretching-Kelvin_bulk+nu Delta e`.
- **Exact physical split:** local connection is strain reshaping `-(S H+H S)` plus rotation commutator `W H-H W`.
- **Exact identity:** connection contribution to `d log|det H|/dt` is `-2 div u`; rotation contributes zero and strain contributes `-2 tr S`.
- **Rigorous incompressible consequence:** local linear deformation can reshape Hessian but has zero direct curvature-volume rate when `div u=0`.
- **Exact conditional Jacobi law:** `det H(t)=det H(t0) exp(int tr(H^-1 Hdot))` on a nondegenerate branch.
- **Rigorous conditional consequence:** finite integrated log-rate prevents a smooth nondegenerate branch from reaching `det H=0`; a continuous determinant collapse requires log-rate integral `-> -infinity`.  This is not Navier--Stokes continuation.
- **Audited exact periodic-NS calibration:** ABC strict maximum has `Hdot=-2nu H`, logdet rate `-6nu`, determinant `-(A^6/2)e^-6nu t`, and zero incompressible connection logdet face.
- **Exact theorem-domain correction:** inverse-Hessian/logdet formulas stop at Hessian degeneracy; branch creation/loss/merger is a separate geometry/event seam.
- **Open-literal:** identification of critical-branch degeneracy with the actual first-bad selector/event/continuation mechanism.


## Enstrophy critical-branch competition and value crossing

- **Exact identity:** branch ranking gap `Delta e=e1-e2` has rate equal to the difference of the two critical-value rates.
- **Exact conditional NS identity:** gap rate splits into relative stretching, relative Kelvin-bulk loss, and relative curvature diffusion.
- **Audited geometry calibration:** transverse value crossing and full Hessian degeneracy are independent conditions; two negative-definite Hessians can persist through a value tie.
- **Audited exact periodic-NS calibration:** a three-mode heat shear has persistent critical sheets `y=0,pi` crossing at `t*=1/nu`, equal value `9e^-2/2`, and negative transverse curvatures `-12e^-2`, `-60e^-2`.
- **Audited exact-NS mechanism:** at the crossing both stretching and Kelvin bulk vanish; branch rates are pure curvature `-12nu e^-2` and `-60nu e^-2`, so both values decrease while the winner switches with gap rate `48nu e^-2`.
- **Exact envelope consequence:** selected scalar max is continuous at the tie but its derivative switches; selector index can jump without a scalar state jump.
- **Rigorous structural consequence:** branch ranking crossing, branch degeneracy/birth/death, and physical packet events are distinct event types.
- **Open-literal:** actual first-bad badness/resolve hysteresis and its mapping to critical-branch competition.


## 2026-08-13 — Draft PR #2 adjudication and own-local affine Kelvin event

- **Exact identity:** common-target current/cochain refinement remains unchanged.  For packet-specific local targets, `epsilon_P=sum_i R_i epsilon_i+Delta_omega` with `Delta_omega=sum_i R_i H_i^T(omega_i-omega_P)`.
- **Exact identity:** reconstructed own-local residual events are affine, `r_+=A r_-+d`, and coherent codeforming events have the corresponding `B` block plus target offset.
- **Exact identity / rigorous consequence:** `d=A Omega_- - Omega_+` is a target coboundary; sequential supplied events telescope exactly.
- **Exact identity:** affine pathwise second moments, simultaneous selector jumps, and target-gradient Brownian Gram faces retain all signed cross terms.
- **Audited calibration:** the exact cubic heat shear `u=(y^3+6 nu t y,0,0)` gives a nonzero own-local target mismatch and a pure-reanchor q.v.-source change even when the current map is `A=I`.
- **Rigorous anti-extension guardrail:** the finite-event hybrid theorem does not imply endogenous selector local finiteness; Brownian sign switching exhibits the missing Tanaka local-time/interface possibility.
- **Exact population identity / rigorous anti-factorization:** the two-replica four-face identity is exact in its stated domain, while general `E[C Q C^T]` also contains `E[delta C delta Q delta C^T]`; the equal-weight PSD three-state witness has missing face `2/9`.
- **Audit verdict:** the PR #2 enstrophy, critical-point-speed, and critical-Hessian checks survive in their stated smooth/nondegenerate domains.
- **Open-literal:** actual NS first-bad packet/anchor event, badness/resolve predicates, endogenous event local finiteness or interface law, support locality, and same-replica-to-restart-clock bridge.
- **No claim:** no restart, continuation, blow-up exclusion, or global-regularity theorem follows from this layer.

## Exact critical-sheet merger -> physical Kelvin packet event

- **Exact identity / Audited calibration:** the periodic two-mode heat shear `u=(-e^{-nu t} sin y-(e^3/8)e^{-4nu t}sin2y,0,0)` is an exact smooth 3D NS solution.  Its side enstrophy critical sheets `y=pi+-d`, `cos d=e^{3(nu t-1)}`, merge into the persistent `y=pi` sheet at `t*=1/nu`; `q_*=-3/(4e)` and `e_yyyy(pi,t*)=-9/(4e^2)` while the PDE field remains analytic.
- **Exact identity:** a one-sided orientation-complete box packet anchored to a critical sheet has literal finite circulation `K_z=ell int_a^{a+s} q dy`, own-local residual `r=H^{-T}(K-H^T omega(a))`, and at merger nonzero codeforming anchor-noise `N_zy=e^{-1}(1-cos s)^2/(2sm)`.
- **Rigorous consequence, conditional on the supplied physical packet functor:** with one common fixed shape `(ell,s,m)` translated to the three critical sheets, support placement, frames, circulation, target, residual, and Brownian response all coalesce in the instantaneous physical packet state.
- **Rigorous no-go / exact NS counterexample:** critical position/enstrophy coalescence alone does not force full packet-state coalescence.  At the same merged sheet, `s=pi/2` and `s=pi/3` give different area frames and `Delta r_z=e^{-1}(-32+21sqrt(3))/(16pi) != 0`, with different nonzero noise coefficients.
- **Exact instantiated event law:** for the branch-resolved rule one fixed-shape packet per critical sheet, the persistent central branch gives `A=E_0`, `AS=I` on `S=1_3 tensor I`, and common collision target plus `grad omega=0` give exactly `d=0` and `N_target=0`.
- **Exact same-replica law:** all collision noise blocks equal `N_*`; every q.v. diagonal/cross-label block is `2nu N_*N_*^T`.  Any normalized collision quotient preserves the physical q.v.; deleting cross blocks creates the spurious `sum w_i^2` factor (equal weights lose `2/3`).
- **Exact interface identity / Audited calibration:** `(E_0-E_side)Sx=0` type label changes have zero physical packet jump on the collision subspace, but for the one-sided packet `partial_a r_z|_*=e^{-1}(1-cos s)^2/(2s)` and the side-sheet speed yields a singular one-sided packet branch rate with finite `d|r_dot|` coefficient.
- **Open-literal:** branch-history/ancestry identification, actual first-bad badness/resolve mapping, and general endogenous selector local finiteness/interface accumulation.
- **Open:** restart/continuation/regularity consequences.  The merger distance has not been identified with Kelvin diffusion scale merely from a shared square-root exponent.

## 2026-08-13 — Critical-sheet transport / Nanson / moving-cut milestone

- **Exact material mismatch:** in the periodic two-mode heat shear `u_y=0`, while the side enstrophy critical sheets satisfy `a_dot_-=+3 nu r/sqrt(1-r^2)` and `a_dot_+=-3 nu r/sqrt(1-r^2)`.  A side-sheet-attached packet therefore moves through material labels; it is a moving-cut/reanchored observable, not a material packet.
- **Exact stochastic ancestry no-go:** the physical common-noise Kelvin anchor has y quadratic-variation rate `2 nu`, whereas the deterministic critical-sheet path has zero q.v.  Literal equality of the critical path and Kelvin ancestry anchor is excluded for `nu>0`; any relation must use a nontrivial lift/readout/conditioning construction.
- **Exact Nanson branch-memory law:** with forward local connection `Ldot=(grad u)L`, `L_b=(I+gamma_b E_xy)L_init` and `gamma_dot_b=-q_b`.  The critical-vorticity gap is the rigid square `q_side-q_central=-e^{-nu t}(1-r)^2/(2r)<0` for every `t<t_*`.  Hence any common pre-merger frame initialization gives a nonzero central/side shear-history gap at the merger.
- **Exact endpoint support mismatch:** at the common merger anchor/vorticity, `L_c L_s^-1=I+Delta gamma_* E_xy != I` and the area comparison is `I-Delta gamma_* E_yx`; the two side histories agree by symmetry, but the persistent central history differs.
- **Exact residual-vs-geometry separation:** for the z-vorticity shear, the sheared packet's xy area and Kelvin circulation are independent of the accumulated xy shear.  Central and side endpoint packets can therefore have identical circulation/target/raw error/reconstructed residual/codeforming residual while their line and area frames differ.  Residual-fiber coalescence is not full physical-state coalescence.
- **Exact finite-support slip decomposition:** a sheet-attached locally Nanson-deformed grid satisfies `V_grid-u=-N_a(r_y)e_x+a_dot e_y`, with finite nonaffinity and normal reanchoring in orthogonal physical directions.  They cannot cancel in this calibration.
- **Exact moving-cut circulation law:** `Kdot=ell nu[q_y(a+s)-q_y(a)]+ell a_dot[q(a+s)-q(a)]`.  At the merger `q(pi+s)-q(pi)=e^-1(1-cos s)^2/2`; the diffusion face is finite while `d |Kdot_cut| -> 3 nu ell e^-1(1-cos s)^2/2`.
- **Exact cusp identification:** after division by the xy area `ell s`, the moving-cut limit is exactly the prior residual cusp coefficient `3 nu e^-1(1-cos s)^2/(2s)`.  The singular branch derivative is therefore a selector/moving-boundary flux, not an NSE field singularity.
- **Exact finite-variation interface calibration:** each side cut has total variation `d(t0)` from `t0` to merger despite divergent instantaneous speed.  This exact isolated selector needs no jump atom or local-time correction, but general endogenous selector accumulation remains Open-literal.
- **Rigorous architecture consequence:** the Eulerian critical selector and Kelvin/material ancestry must remain separate state semantics.  The earlier fixed-shape coalescence theorem is an instantaneous Eulerian rebuild statement; dynamically history-carrying Nanson packets do not canonically coalesce in full support/frame state.
- **Open-literal:** actual first-bad badness/resolve definition, whether first-bad localization is critical-sheet based, the nontrivial Kelvin-ancestry-to-selector lift/readout, and future-bank/cross-clock identification.
- **Open:** uniform first-bad support/finite-shape collapse, restart capacity, continuation/global regularity.  No restart/continuation/regularity theorem is claimed.

## Kelvin ancestry -> Eulerian moving readout

- **Exact identity:** after a conditional reduced/full ancestry lift `kappa`, normalized Eulerian selection has exactly three covariance layers: averaged intrinsic full-Kelvin covariance, averaged hidden-state resolution covariance, and localization covariance of the conditional mean.
- **Exact Reynolds identity:** a moving Eulerian boundary with signed ancestry-mass flux `lambda` revalues a normalized selected average by `M^-1 sum lambda(A_boundary-A_selected)`; selected covariance uses `C_boundary+(m_boundary-m)(m_boundary-m)^T-C_selected`.
- **Exact structural consequence:** applying the boundary law separately to intrinsic, resolution, and localization layers telescopes to the total selected-covariance law.  The selector/readout supplies no independent Brownian covariance producer.
- **Audited exact-NS calibration:** in the periodic two-mode merger shear the reverse-age Kelvin anchor has zero `y` drift, so the uniform `1/(2pi)` torus marginal is stationary while the side critical chamber `[pi-d,pi]` moves through it.
- **Exact chamber law:** `M=d/(2pi)`, `d_dot=-3 nu cot d`; instantaneous mass-loss rate diverges like `-3nu/(2pi d)` but the total selected-mass variation to merger is finite.
- **Exact critical readout law:** the selected vorticity mean is `qbar=-(3/4)e^-1 cos(d)^(-1/3) sin(d)/d`; both endpoints are vorticity-critical, so its entire first-moment rate is the Reynolds moving-cut face.
- **Exact NS cancellation:** `q_side-qbar=-(e^-1/15)d^4+O(d^6)` while `d_dot/d~ -3nu/d^2`; therefore `qbar_dot=(nu e^-1/5)d^2+O(d^4)->0` despite the singular boundary speed.
- **Exact covariance law:** selected vorticity variance is `(e^-2/525)d^8+O(d^10)` and obeys `Vdot=-2nu<|grad q|^2>+(d_dot/d)[(q_side-qbar)^2-V]`.
- **Exact face coefficients:** Kelvin bulk is `-(4nu e^-2/105)d^6+O(d^8)`, moving-cut revaluation is `-(4nu e^-2/525)d^6+O(d^8)`, and total `Vdot=-(8nu e^-2/175)d^6+O(d^8)->0`.
- **Frontier correction:** the ancestry-to-moving-Eulerian-readout semantics and second-order transport law are now literal once the localization is supplied.  The actual NS first-bad observable defining that localization, global ancestry state/lift, two-clock future-bank identification, general endogenous interface accumulation, uniform first-bad support/finite-shape collapse, restart, continuation and regularity remain **Open-literal/Open**.
- **No claim:** no first-bad threshold, restart, continuation, blow-up exclusion, or global-regularity theorem follows from this milestone.

## 2026-08-13 — Intrinsic max-normalized enstrophy localization milestone

- Replaced the external-threshold picture at the candidate localization layer by the PDE-generated filtration `e -> M=max e -> g=e/M -> {g>=theta}`.
- Derived the exact regular-boundary compatibility law `V_n-u.n=(stretching-Kelvin_bulk+nu Delta e-theta Mdot)/|grad e|` and its NS-similarity-invariant normalization.
- Composed the boundary with a generic ancestry continuity current: mass flux is exactly fluid/current mismatch plus intrinsic level slip; no selector force or selector Brownian source appears.
- Exact periodic integer-frequency one-mode NS gives raw `M~n^4` and Kelvin bulk `~n^6` but stationary `g=cos^2(ny)` and zero compatibility defect, ruling out absolute-magnitude first-bad thresholds as intrinsic criteria.
- Built an exact four-mode periodic heat shear whose `y=0,pi` points are true global enstrophy maxima at `t*=1/nu`; exact polynomial bounds certify the global claim, and the max envelope switches one-sided rates from `-336nu` to `-240nu` with zero value jump.
- Classification: similarity/localization/speed/ancestry-flux laws Exact/Rigorous; one-mode and four-mode witnesses Audited exact-NS calibrations; actual first-bad/continuation identification remains Open-literal/Open.
- No restart/continuation/global-regularity claim.  No geometric scale is identified with the Kelvin diffusion scale merely from an exponent.


## Milestone: intrinsic chamber -> Kelvin/Nanson support no-go

- **Exact identity:** for the one-mode max-normalized chamber, `L=diag(1,2 alpha/n,1)`, `H=diag(2 alpha/n,1,2 alpha/n)`, `B=L L^T`, and the tangent-plane support face is `P B P=diag(1,0,1)`.
- **Exact physical typing:** the persistent face normal to `y` has area one but zero Kelvin flux, local target flux, and raw residual because `omega` is parallel to `z`; orientation-complete quadrupoles recover the transverse geometry the current channel misses.
- **Audited exact-NS calibration / rigorous no-go:** `alpha->0` in one fixed smooth periodic NS solution gives zero scalar compatibility, zero uniform-ancestry net flux, collapsing packet volume and physical residual, zero local q.v., and collapsing finite-shape/Nanson rates while transverse support and diameter remain order one and conditioning degenerates.
- **Open-literal:** no theorem yet identifies this filtration sequence with the actual first-bad state or forces tangential support/refinement collapse from a genuine first-bad compatibility obstruction.
- **Open:** uniform singular-time support/conditioning, restart capacity, continuation, and global regularity.
- The intrinsic chamber width is not identified with the Kelvin diffusion scale.

## Intrinsic normalized-vorticity unit-ball contact grammar

The attempted next descent through higher scalar jets exposed a stricter PDE-first reduction.  With `M=max |omega|^2/2` and `V=omega/sqrt(2M)`, at differentiability times of the max envelope, literal Navier--Stokes gives `D_t V=(grad u)V+nu Delta V-(Mdot/2M)V`, while always `g=e/M=|V|^2<=1`.  On the active unit sphere the exact contact form is `H_c=-V dot Hess(V)=(grad V)^T grad V+Q/2`, so `ker H_c=ker Q intersect ker(grad V)`.  The new tangent term is the right Gram of the same normalized gradient whose left Gram is exactly orientation-complete Kelvin q.v. divided by `4nuM`; no external score/source is introduced.  Exact periodic elliptic-polarization shears realize `G_R,zz=beta^2 k^2`, `Q_zz/2=(1-beta^2)k^2`, but `H_c,zz=k^2` for the whole family.  The helical endpoint has `g identically 1`, zero scalar source and all scalar `g` jets zero while `grad V`, contact and Kelvin bulk remain nonzero, so scalar higher-jet exhaustion is an exact-NS no-go.  Classification: normalized-vector PDE/contact/Kelvin Gram laws exact; contact-kernel completeness rigorous at active maxima; polarization transfer and helical no-go audited calibrations; actual first-bad contact-kernel closure Open-literal; restart/continuation/regularity Open.

## 2026-08-14 — Material Hodge--Bochner master compatibility reduction

The recent intrinsic-localization/contact milestones have now been compressed one
level below their separate Eulerian manifestations.  For the actual deterministic
Lagrangian flow `Phi_t`, set `G=Phi_t^* g_0`, `bar alpha=Phi_t^* u^flat`, and
`bar beta=Phi_t^* d u^flat`.  Naturality gives the exact material system

`partial_t bar beta = nu Delta_G bar beta`, `d bar beta=0`,
`bar beta=d bar alpha`, `delta_G bar alpha=0`, while
`partial_t G=L_U G` with `U=bar alpha^{sharp_G}`.  The metric is not a model state:
`G=F^T F` is flat and volume-one because it is the pullback Euclidean metric of the
same incompressible flow.  After fixing the harmonic/Galilean velocity mode,
`bar alpha` is Hodge-reconstructed from `(G,bar beta)`.

- **Exact reciprocal metric lock:** with `H=cof F=F^-T`, `H^T H=G^-1` and the old
  packet metric `(H^T H)^-1` is exactly `G`; physical vorticity amplitude is
  `|omega|^2 o Phi=b^T G b`, while the principal material Hodge-diffusion metric is
  `G^-1`.
- **Exact metric-work compression:** `(1/2)b^T Gdot b=(omega.S.omega)o Phi`; vortex
  stretching is only time variation of the material fiber metric once Lie transport
  has been removed by pullback.
- **Exact Hodge-star commutator:** with `H_G=partial_t-nu Delta_G`,
  `H_G(*_G bar beta)-*_G H_G(bar beta)=(partial_t *_G)bar beta`, and because
  `H_G bar beta=0` the right side is exactly `2 Phi^*[(S omega)^flat]`.  Stretching
  is therefore the time-Hodge representation defect of the same material heat law.
- **Exact Hodge--Bochner compression:** because every `G_t` is flat, diffusion has
  one bilinear product defect `2<grad X,grad Y>_G`.  Its scalar trace is viscous
  enstrophy loss; its tensor/pair/covariance representations are the already-audited
  vorticity-dyad defect, Kelvin common-noise q.v., same-ancestor diagonal defect, and
  future-covariance source.
- **Exact contact compression:** normalized-vorticity contact is the untraced
  covariant product rule
  `H_c,G=(nabla^G Vbar)^* nabla^G Vbar+Q_G/2`; the previous contact tensor is
  therefore not a new primitive beneath the carré-du-champ sector.
- **Rigorous architecture consequence:** deterministic Cauchy/Nanson/deformation and
  the full material finite-current shape are functorial images of one diffeomorphism;
  pulling back freezes the full reference current.  This explains the infinite
  finite-shape hierarchy without validating any finite moment/deformation closure.
- **Frontier correction:** the primitive local question is no longer to invent a
  higher contact tensor on `ker H_c`.  The smallest literal candidate core is the
  coupled exact-form/metric feedback `(G,bar beta)`.  A hypothetical no-escape
  theorem would have to show that an exact Hodge-heated two-form cannot escape in
  the self-generated flat volume-one metric whose velocity is reconstructed from
  that same form.  Sufficiency for blow-up exclusion, restart, continuation, or
  global regularity remains **Open**.

See `docs/material_hodge_bochner_master_compatibility.md`.  No CI/calibration
campaign was used for this milestone; only lightweight symbolic algebra checked the
matrix ordering and the already-exact contact/product identities.

## 2026-08-14 — Hodge–strain / null-Lagrangian compatibility compression

The material `(G,bar beta)` system has been compressed one level further.  The
material velocity one-form satisfies the exact pointwise split
`nabla^G bar alpha = (1/2) Gdot + (1/2) bar beta`: metric velocity/strain and
vorticity are the symmetric and antisymmetric faces of one actual covariant
gradient.  Flatness gives the local gradient-integrability relation coupling their
first derivatives, while incompressibility makes the symmetric face trace-free.
The Hodge–strain transform is insensitive to the parallel harmonic/Galilean mode and
`S_G:bar beta -> E=Sym nabla^G B_G bar beta` obeys the exact polarized identity
`<S_G beta1,S_G beta2>=(1/2)<beta1,beta2>`; hence
`||Gdot||_2^2=2||bar beta||_2^2`, with the same factor after every fixed covariant
derivative.  Total enstrophy is therefore exactly one quarter of the squared
material-metric speed, kinetic-energy dissipation is `(nu/2)||Gdot||_2^2`, and
bulk enstrophy dissipation is `(nu/2)||nabla Gdot||_2^2`.

The same integrable-gradient structure also retypes pressure and stretching.
Quadratic compatibility is the exact local identity
`-Delta_G pbar=|E|^2-|bar beta|^2/2`; its zero mean is precisely the global
Hodge strain–vorticity equipartition.  Pressure is therefore gauge only in the
closed-circulation quotient; in the symmetric gradient sector it is the nonlocal
incompressibility constraint potential.  Cubic determinant/Piola compatibility
is the Betchov law `int <b,Kb> = -4 int det K`, so vortex stretching and cubic strain
self-amplification are the antisymmetric/symmetric faces of the degree-three
null-Lagrangian of the same velocity gradient.  Consequently the exact integrated
enstrophy law is purely metric-tangent:
`d int|K|^2/dt = -4 int det K - 2nu int|nabla K|^2`, where
`K=(1/2)G^-1 Gdot`.

Classification: gradient split, local integrability, pressure Poisson, metric-speed
identities and Betchov/null-Lagrangian relations Exact; Hodge–strain scaled-isometry
and operator synthesis Rigorous consequences.  The new frontier is whether the
parabolic evolution of the antisymmetric face can remain compatible with an
escaping symmetric metric face under the exact flat/volume/integrability/minor
constraints.  Sufficiency for no-escape, restart, continuation and regularity
remains Conjectural/Open.

A further exact compression identifies the Bernoulli/pressure gauge itself with
motion of the material Hodge constraint.  If `P_G` is the orthogonal projector onto
co-closed one-forms, then `P_G bar alpha=bar alpha`, the fixed-`G` Hodge Laplacian
preserves `Ran P_G`, and the material momentum equation forces
`d bar B = (dot P_G) bar alpha`.  Hence
`(partial_t-dot P_G)bar alpha=nu Delta_G bar alpha`: NS momentum is Hodge heat in a
co-closed subspace whose projector is moved by the same self-generated metric.
Equivalently `delta_G d bar B=-(partial_t delta_G)bar alpha`.  Together with the
previous time-Hodge identity for stretching, pressure/Bernoulli and vortex
stretching become two functorial derivatives (`dot P_G` and `dot *_G`) of the same
moving Hodge geometry.  At frozen flat `G`, the Hodge–strain map intertwines the
form and symmetric-tensor Laplacians; along the actual path its sole failure to
heat is `(partial_t S_G)bar beta`, whose Eulerian representation is exactly
`S^2-Omega^2+[S,Omega]-Hess p`.  No sign or no-escape estimate is claimed.

## 2026-08-14 — self-Hodge conjugacy / Lax compression

The moving material Hodge objects have now collapsed to one universal naturality
law.  If `T_t=Phi_t^*` and `A_G` is any diffeomorphism-natural Hodge/tensor operator,
then `A_G=T_t A_0 T_t^-1`; differentiating gives
`A_Gdot=L_U^out A_G-A_G L_U^in`, with `U=Phi_t^*u`.  Thus `dot star_G`,
`dot delta_G`, `dot Delta_G`, `dot P_G`, the Biot--Savart/Hodge-strain transforms,
and the induced carré-du-champ are not separate geometric dynamics.  Pressure is
the projector component `dBbar=[L_U,P_G]bar alpha=(I-P_G)L_U bar alpha`; stretching
is the star component `[L_U,star_G]bar beta`; the full symmetric strain/rotation/
pressure-Hessian feedback is the Hodge--strain representation of the same operator
commutator.

A new exact architecture correction follows: because `G=Phi_t^*g_0`, the material
Hodge Laplacian is unitarily conjugate to the fixed Euclidean one at every smooth
time.  Its spectrum, spectral gaps, intrinsic Poincare constants, diameter and
heat-kernel geometry do not degenerate.  The reciprocal coefficient matrices
`G/G^-1` describe coordinate/diffeomorphism distortion, not intrinsic loss of the
Hodge diffusion geometry.  The genuine escape variable is therefore the
conjugating diffeomorphism/distortion, whose symmetric infinitesimal rate is the
same Hodge-strain image of the heated vorticity.

The prior scaled isometry also eliminates `bar beta` as an independent material
state: `Gdot=2 S_G bar beta` and `S_G^* S_G=I/2` imply exactly
`bar beta=S_G^* Gdot`.  Hence every smooth NS solution induces the metric-tangent
heat law `partial_t(S_G^*Gdot)=nu Delta_G^(2)(S_G^*Gdot)` on the flat volume-one
metric orbit, with `Gdot` restricted to the compatible symmetric-gradient range.
No converse for arbitrary metric paths is claimed.  The shortest current grammar is
now: the state is Hodge-heated while its entire Hodge calculus is inner-conjugated
by the velocity reconstructed from that same heated state.  Whether this
self-conjugate parabolic loop forbids finite-time diffeomorphism escape remains
Conjectural/Open; no restart, continuation or global-regularity theorem is claimed.

See `docs/self_hodge_conjugacy_lax_compatibility.md`.

The same conjugacy theorem gives a rigorous anti-case-by-case stopping rule.  Any
further operator built functorially from the material metric, de Rham/Hodge calculus,
Hodge functional calculus, natural tensor operations and current pairing has its
geometry motion forced by the same `L_U` conjugacy.  Nonlinear state observables add
only ordinary chain/product faces, with the unique second-order non-derivation
already typed by the Bochner/carre-du-champ.  Hence another natural Hodge/contact/
Kelvin representation cannot constitute a new primitive mechanism.  Any genuinely
new primitive must lie outside this functorial closure and must be derived literally
from NS rather than introduced architecturally.

## 2026-08-14 — critical Hodge chirality / paired-transfer compression

The self-Hodge conjugacy frontier has been compressed at the canonical critical
spectral order.  In the fixed-Hodge/Leray gauge, mean-zero divergence-free NS is
`u_t+T_u u+nu A u=0` with `T_u=P(u.grad)` skew-adjoint and `A=-Delta` positive.
For every self-adjoint spectral multiplier `F(A)`, the exact quadratic law is
`d <u,F u>/2 = <u,[T_u,F]u>/2 - nu <A^(1/2)u,F A^(1/2)u>`: nonlinearity is only
spectral commutator transfer and viscosity is diagonal.  `F=A` identifies literal
vortex stretching with this commutator; `F=I` gives zero nonlinear energy
production.

Three dimensions add the exact Hodge factorization `A=C^2`, `C=curl`.  With
`J=sign C` and `P_+-/=(I+-J)/2`, the positive critical form
`K=<u,|C|u>/2=||A^(1/4)u||^2/2` and signed helicity
`H=<u,C u>/2` have the same half-derivative order and differ only by the curl sign.
Writing `K_+-=<u_+-,|C|u_+->/2`, one has `K=K_++K_-`, `H=K_+-K_-`.  The nonlinear
helicity rate vanishes exactly, so the nonlinear critical rates satisfy one rigid
law `tau_+=tau_-=:tau`; hence
`Kdot_+=tau-nu D_+`, `Kdot_-=tau-nu D_-`, with
`D_+-=<u_+-,|C|^3u_+->>=0`.  All nonlinear positive-critical growth is therefore
paired opposite-chirality transfer in the canonical global Hodge decomposition.

A finite Fourier helical referee verifies the operator typing: homochiral triads have
zero nonlinear energy/helicity/critical rates; heterochiral triads can have zero
energy/helicity rates but nonzero critical rate, with equal positive/negative chiral
rates.  This also supplies a sharp anti-route.  Amplitude scaling gives
`tau(a u)=a^3 tau(u)` while `D_+-(a u)=a^2 D_+-(u)`, so no universal instantaneous
`2 tau <= nu(D_++D_-)` law can underlie no-escape.  Any true exclusion mechanism
must be dynamic/causal and constrain cumulative self-generated paired-helicity
transfer, not a snapshot domination estimate.

Classification: Leray skew split, master spectral commutator, curl square,
helicity cancellation and paired-transfer laws Exact; critical signed-to-absolute
compression Rigorous; finite helical triad is Audited calibration; instantaneous
domination route is ruled out by exact amplitude scaling once nonzero transfer is
activated.  Dynamic no-escape, continuation and regularity remain Open.

See `docs/critical_hodge_chirality_transfer.md`.  No CI/actions campaign was run.

Follow-through on the same milestone: integrating the paired laws produces a literal
causal identity, not an added bank.  With `Theta(t)=int_0^t tau`, one has exactly
`Theta=K_+(t)-K_+(0)+nu int D_+ = K_-(t)-K_-(0)+nu int D_-`.  Thus every cumulative
unit of nonlinear critical transfer must be accounted in both chirality sectors as
stored positive critical content or positive viscous critical dissipation.  A
critical escape therefore requires `Theta -> +infinity`; an apparently one-sign
terminal escape still forces the opposite sign to participate through co-storage or
unbounded accumulated critical dissipation.  Separately, spectral Cauchy--Schwarz
and the ordinary energy law give `K^2<=E Z` and
`int_0^T K^2 dt <= E(0)^2/(2nu)`.  This does not close regularity; it shows that any
required infinite cumulative paired transfer must concentrate into shrinking time
windows and/or critical dissipation.  The remaining gap is therefore a causal
anti-concentration law for the self-generated paired transfer, not another static
channel estimate.

## 2026-08-14 — de Rham skew-square / critical increment-current compression

The critical paired-chirality milestone has been pushed below chirality itself.  With
`alpha=u^flat`, `beta=d alpha`, `delta alpha=0`, literal NS is the exact two-form
current law `beta_t+d(i_u beta+nu delta beta)=0`.  After fixing the harmonic velocity
mode, `u=B beta`, so this is a beta-only self-induced nonlinear Hodge conservation
law.  In three dimensions `C=*d=curl`, `C^2=-Delta` on the co-closed mean-zero sector,
and the projected momentum equation is `alpha_t=R_beta alpha-nu C^2 alpha` with
`R_beta eta=-P i_{eta#} beta`.  The same alternating two-form forces
`R_beta^*=-R_beta` and `R_beta(C alpha)=0`; nonlinear energy cancellation and
nonlinear helicity cancellation are therefore two shadows of one skew/null algebra,
not separate conservation mechanisms.  Applying `C` gives vorticity
advection/stretching as the curl of the same sideways current.

At the critical Hodge order `Lambda=|C|`, the remaining nonlinear transfer has the
exact commutator form `(Kdot)_nl=(1/2)<alpha,[Lambda,R_beta]alpha>`.  Subordination of
`Lambda` gives a positive torus kernel `K_Lambda`; the commutator is exactly
`doubleint K_Lambda (omega(x)-omega(y)).(u(x) cross u(y))`, while the critical
viscous term is `(1/2) doubleint K_Lambda |omega(x)-omega(y)|^2`.  Hence
`Kdot=(1/2)doubleint K_Lambda[delta_omega.(u_x cross u_y)-nu|delta_omega|^2]`.
The cumulative paired transfer from the previous milestone is therefore the literal
spacetime oriented vorticity-increment current, not an independent bank.  Dangerous
critical transfer and critical viscosity use the same canonical pair geometry; one
is the orientation-correlation face and the other the increment-square face.

Classification: de Rham current, beta-only closure, skew-square form, null direction,
energy/helicity cancellations, fractional commutator kernel, and common-kernel
critical balance Exact; reduction of prior pressure/stretching/chirality/material
Hodge mechanisms to this core Rigorous.  The missing theorem is now a genuinely
self-induced correlation/anti-concentration law exploiting `u=B beta`; generic
Cauchy/Young bounds that discard this self-generation are not promoted.  No
no-escape, restart, continuation, or global-regularity claim.
- **Exact parity/no-quotient consequence:** under the instantaneous state reversal `u -> -u`, all even critical pair magnitudes (`E`, `K`, `D`, `|delta omega|^2`, `|u_x cross u_y|^2`) are unchanged while the oriented common-kernel transfer `tau` changes sign.  Therefore no magnitude-only/Gram-only positive state can determine the dangerous transfer; signed phase/orientation correlation is irreducible unless reconstructed by another exact PDE law.
- **Exact master Hodge-current identity:** for every self-adjoint spectral `F` on exact closed vorticity two-forms, `d/dt <beta,F beta>/2 = -<delta F beta,i_u beta>-nu<delta F beta,delta beta>`.  `F=A^-1`, `A^-1/2`, and `I` are respectively kinetic energy, the canonical critical quadratic, and enstrophy.  Thus their nonlinear/viscous faces are not separate balances but Hodge tests of the single current `J_NS=i_u beta+nu delta beta`; in particular stretching is `-<delta beta,i_u beta>`.
- **Exact spectral/physical-space bridge:** with chirality involution `J=C|C|^-1`, `(Kdot)_nl=int u.(omega cross J omega)=-2 int u.(omega_+ cross omega_-)`, hence `tau=-int u.(omega_+ cross omega_-)`.  The same `tau` is `(1/4)doubleint K_Lambda delta_omega.(u_x cross u_y)`.  Opposite-curl-sign mixing and the oriented vorticity-increment current are therefore exactly the same transfer in local spectral-sign and nonlocal pair representations.

## 2026-08-14 — Heat-null / carré-du-champ critical-transfer compression

The de Rham skew-square frontier has compressed one level further.  With
`A=C^2=-Delta`, `Lambda=A^(1/2)`, `J=C|C|^-1`, `a=omega_+`, `b=omega_-`, and
`j=J omega=a-b`, Hodge reconstruction gives `u=Lambda^-1 j`.  The complete paired
critical transfer is therefore not a raw cubic term but the exact inverse-Hodge
commutator
`tau=-(1/2)(<a,[Lambda^-1,X_b]a>+<b,[Lambda^-1,X_a]b>)`, where
`X_q v=v cross q`.  Symmetrization gives the double-increment null form
`tau=-(1/2) intint G_-1 (m_a-m_b).(delta a cross delta b)` or equivalently
`tau=(1/4) intint G_-1 m_j.(delta omega cross delta j)`.  Thus both curl signs must
vary at the same physical pair; magnitude-only coexistence is not enough.

Subordination by the same Hodge heat semigroup `P_s=e^-sA` gives the sharper exact
law
`tau=(1/(2 sqrt(pi))) int s^-1/2 <P_(s/2) j, D^x_(s/2)(omega,j)> ds`, where
`D^x_t(f,g)=P_t(f cross g)-P_t f cross P_t g`.  The pointwise null relation
`P_t j.(P_t omega cross P_t j)=0` shows that critical growth is entirely the heat
product anomaly of an alternating null form.  Duhamel converts this anomaly into the
cross-product carré-du-champ
`2 int_0^t P_(t-r) sum_k partial_k P_r f cross partial_k P_r g dr`.  Critical
viscosity is simultaneously the positive half-Laplacian heat square
`D=(1/(2 sqrt(pi))) int s^-3/2 <omega,(I-P_s)omega> ds`.  Since `J` is unitary and
commutes with the heat calculus, the `omega` and `J omega` heat increment/gradient
energies agree exactly at every heat scale.

Classification: inverse-Hodge commutator, double-increment formula, heat-null defect,
carré-du-champ representation, positive heat dissipation and scale-by-scale Hodge-sign
isometry Exact; the synthesis reducing critical transfer, Kelvin/contact/covariance
and viscosity to the same Hodge product defect is Rigorous.  The remaining bridge is
a dynamic anti-concentration theorem for the self-generated heat-scale
mean--oriented-covariance alignment.  No no-escape, continuation or regularity claim
is made.
- **Rigorous heat-scale anti-Zeno consequence:** for every fixed heat-age cutoff `h0>0`, the `h>=h0` part of the exact heat-covariance transfer is absolutely integrable over every finite smooth physical-time interval, by torus heat smoothing and the kinetic-energy identity.  Hence `Theta->+infinity`, if possible, must be carried by heat ages tending to zero.  The same common-age covariance inequality gives the necessary growth condition `Kdot>0 => exists h>0 with 4 h ||P_h J omega||_infty > nu`; this is only a PDE-forced viscosity-scale crossing, not a selector or continuation criterion.

## 2026-08-14 — Canonical Hodge heat-scale energy continuity law

The heat-null theorem exposes a still smaller state-space law.  Define the canonical heat-resolved energy `E(h,t)=<u,P_h u>/2`, `P_h=e^-hA`, and the positive heat-scale density `rho=-partial_h E=(1/2)||A^(1/2)P_(h/2)u||_2^2`.  Then `int_0^infty rho dh` is exactly kinetic energy and `rho(0)` is enstrophy.  With the canonical nonlinear scale flux `Pi(h,t)=-<u cross omega,P_hu>`, literal NS gives the exact one-dimensional continuity equation `rho_t-partial_h(2nu rho+Pi)=0`; `Pi(0)=0`, so nonlinearity has no direct flux through the finest heat-age boundary and viscosity is the only energy exit there.

The same `Pi` generates the formerly separate scale laws.  Its boundary slope is vortex stretching: `partial_h Pi(0)=int omega.S.omega`.  The positive critical quadratic is `K=(1/sqrt(pi)) int h^-1/2 rho dh`, while the complete paired nonlinear critical transfer is `2tau=(1/(2sqrt(pi))) int h^-3/2 Pi dh`.  Critical viscosity is the boundary-density deficit `D=(1/sqrt(pi)) int h^-3/2(rho(0)-rho(h)) dh`, giving the exact one-line critical balance `Kdot=(1/(2sqrt(pi))) int h^-3/2[Pi-2nu(rho(0)-rho(h))] dh`.  Moreover `Pi` itself is the same heat-null cross-product/carre-du-champ defect from the preceding milestone.

Classification: heat-scale density/flux, continuity law, boundary nullity, stretching slope, critical moment/flux moment and viscous deficit Exact; the reduction of energy cascade, stretching, critical chirality transfer and viscosity to one positive scale continuity law Rigorous.  Every fixed smooth state has a viscosity-dominated boundary layer because `Pi(h)=O(h)` while `rho(h)->rho(0)`.  Uniform persistence of that layer and exclusion of zero-heat-scale Zeno concentration remain Open; no no-escape or regularity theorem is claimed.

## 2026-08-14 — signed-curl alternating three-current / whole-family spectral law

The canonical heat-scale continuity frontier has been pushed below heat age itself.
On the mean-zero divergence-free torus, decompose the actual velocity by the signed
self-adjoint curl spectrum, `u=sum_c u_c`, `C u_c=c u_c`, and set
`e_c=||u_c||_2^2/2>=0`.  The Lamb rotation generates one fully alternating spectral
three-current `T_cdr=int u_c.(u_d cross u_r)`.  Its pair contraction is
`J_cd=sum_r r T_cdr`, so `J_cd=-J_dc` and the stronger blockwise null law
`sum_d d J_cd=0` holds for every output block, the spectral shadow of
`R_beta(Cu)=0`.  Positive spectral energy obeys the exact current equation
`edot_c=sum_d J_cd-2nu c^2 e_c`.

For every Hodge spectral quadratic `Q_F=<u,F(C)u>/2`, the complete nonlinear rate is
one determinant contraction
`(Q_F dot)_nl=(1/6)sum_cdr D_F(c,d,r) T_cdr`, with
`D_F=det[[1,1,1],[c,d,r],[F(c),F(d),F(r)]]`
`=(c-d)(d-r)(r-c) F[c,d,r]`.  Thus all quadratic Hodge cases are second spectral
curvature readouts of one physical current.  Affine `F=a+bc` vanish triplewise, so
energy and Euler helicity are universal affine null directions of the same law.  `F=c^2` gives the
Vandermonde stretching formula.  `F=|c|` vanishes on every homochiral triple because
absolute value is affine on each curl-sign half-line; mixed critical transfer is the
kink-curvature face.  Fourier support forces triangle inequalities among
`|c|,|d|,|r|`; hence no nonlinear spectral teleportation from two bounded frequencies
to one arbitrarily larger frequency.  For a mixed triple `c,d>0,r<0`,
`D_|.|=2r(c-d)` and triangle support gives `|D_|.||<=2|r|^2`, an exact high--high--low
null coefficient, not a transfer/dissipation estimate.

The heat-age law is exactly the Laplace image of this signed spectral current:
`E(h)=sum e^-h c^2 e_c`, `rho=sum c^2 e^-h c^2 e_c`.  Hence actual `rho` is completely
monotone, not an arbitrary positive profile:
`(-1)^m partial_h^m rho=sum c^(2m+2)e^-h c^2 e_c>=0`.  Its logarithmic spectral
barycenter `kappa=-partial_h log rho` obeys the exact variance law
`partial_h kappa=-Var_{pi_h}(c^2)<=0`.  The boundary mass
`M=int_0^h rho=E(0)-E(h)` is a Bernstein function and satisfies exactly
`M_t=Pi-2nu(rho(0)-rho(h))`; the complete critical evolution is merely the
`h^-3/2` moment of `M_t`.  Thus the earlier nonlinear-versus-viscous heat bracket is
the time velocity of one canonical positive boundary mass, not a third mechanism.

Classification: signed-curl block law, alternating three-current, weighted block
nullity, determinant master law, affine/triplewise energy-helicity cancellation,
Vandermonde stretching, heterochiral critical determinant, heat Laplace image,
complete monotonicity/Bernstein law Exact; Fourier triangle/no-teleportation and
heterochiral low-frequency-square coefficient Rigorous consequences.  Static
Bernstein shape alone cannot exclude escape; the remaining Open bridge is whether the
self-generated alternating triangle current can drive positive spectral mass through
an infinite heterochiral chain to `|c|->infinity` against diagonal `2nu c^2` killing.
No no-escape, continuation, or regularity claim.
- **Exact whole-family no-go calibration:** any field in one signed curl eigenspace
  `Cu_0=c u_0` has `u x omega=0` and evolves by the exact smooth NS heat law
  `u(t)=e^-nu c^2 t u_0`.  Its heat density is the single completely-monotone atom
  `rho=c^2 e^-h c^2 e_c(t)`, `Pi=0`, and `K/E=|c|`.  Thus across exact smooth NS
  families the heat boundary width `c^-2` can be arbitrarily small and critical
  magnitude arbitrarily large with no escape.  Static Bernstein concentration is
  not badness; the unresolved object is dynamic alternating spectral transport.
- **Exact whole-quadratic exhaustion no-go:** `u -> -u` leaves every signed-curl
  energy atom `e_c`, hence every quadratic Hodge readout `Q_F`, the full heat profile
  `rho(h)`, helicity, critical size, enstrophy and boundary mass unchanged.  But the
  cubic alternating current `T_cdr`, pair current `J_cd`, heat flux `Pi`, and every
  nonlinear quadratic rate change sign.  Therefore no closure of NS nonlinear
  spectral dynamics on the complete positive energy measure or on `rho` alone is
  possible.  The irreducible missing information is signed phase/orientation, not
  another quadratic magnitude.

## 2026-08-14 — Poisson--Casimir / metric-gradient whole-functional master law

The signed-curl alternating-current theorem has been pushed below spectral
coordinates.  On the mean-zero divergence-free phase space define the constant
alternating three-form `Omega(a,b,c)=int a.(b cross c)`, kinetic energy
`E=||u||^2/2`, helicity `H=<u,Cu>/2`, and enstrophy `Z=||Cu||^2/2`.  Their `L^2`
gradients form the exact Hodge ladder `grad E=u`, `grad H=Cu=omega`, `grad Z=C^2u`,
with `Z=||grad H||^2/2`.  The state-generated operator `J(u)v=P(v cross omega)` is
exactly the contraction `i_(grad H) Omega` in pairing form, is skew, and annihilates
`grad H`.

The induced functional bracket
`{F,G}=Omega(grad F,grad G,grad H)` equals
`-<u,[grad F,grad G]_Lie>`, hence is the Lie--Poisson bracket of divergence-free
vector fields and satisfies Jacobi on the standard smooth functional domain.  Euler
is the Hamiltonian flow generated by `E`, while `H` is a Casimir:
`Fdot_Euler={F,E}`, `{F,H}=0` for every smooth functional `F`.  Viscosity is ordinary
`L^2` gradient descent of `Z=||grad H||^2/2`.  Therefore literal Navier--Stokes obeys
the whole-functional law `Fdot={F,E}-nu <grad F,grad Z>` for every smooth `F`.

This subsumes the preceding spectral theorem: `T_cdr=Omega(u_c,u_d,u_r)` is only the
signed-curl coordinate tensor of the constant phase-space three-form, and the
three-point determinant law for `Q_f=<u,f(C)u>/2` is the coordinate expansion of
`Omega(f(C)u,u,Cu)`.  Stretching is `{Z,E}`; on a one-sign curl sector the positive
critical quantity is `+/-H` and is therefore a Casimir; the canonical heat flux is
`Pi(h)=-{E_h,E}`.  Pure Beltrami states satisfy `grad H=c grad E`, so the alternating
generator plane collapses and the Euler nonlinearity vanishes before any spectral
calibration is introduced.

The strongest operator synthesis is that the same field `grad H=omega` is both a
null direction of the conservative Poisson tensor and the exact energy-drain field
for viscosity: `J(u)grad H=0` while `-Edot/nu=||grad H||^2`.  The open no-escape
problem is consequently a dynamic Poisson--gradient compatibility question: can the
Hamiltonian tangent flow preserving `E` and `H` drive `Z=||grad H||^2/2` and higher
Hodge complexity into finite-time escape while viscosity descends the metric
potential generated by that same Casimir gradient?  The heterochiral spectral chain,
heat-age Zeno concentration and material-Hodge distortion frontiers are now
representations of this one Open problem.  No no-escape, continuation, restart or
global-regularity claim.

- **Exact transverse-Casimir defect law:** with `alpha=H/E` and
  `B=(C-alpha)u=omega-alpha u`, one has `<u,B>=0`,
  `D_B=Z-H^2/E=||B||^2/2`, and the actual Euler vector is `X_E=P(u cross B)`.
  The canonical defect closes at quadratic level without an `alpha_dot` remainder:
  `D_Bdot=<u cross B,C B>-nu||C B||^2`.  Its exact PDE is
  `B_t=(C-alpha)X_E-nu C^2B-alpha_dot u`, while
  `alpha_dot=-(nu/E)<B,(C+alpha)B>`.  Thus the Beltrami-aligned part of vorticity is
  nonlinearly invisible, and even the signed curl barycenter can move only through
  the transverse defect.  This is a derived representation of the Poisson--Casimir
  master law, not a new score or state.

## Energy-sphere Rayleigh/Hodge compression

The Poisson--Casimir/Beltrami-defect frontier has been compressed by separating the
kinetic-energy radius from the unit state.  For a smooth nonzero solution set
`r=||u||_2`, `q=u/r`, `lambda(q)=<q,Cq>=H/E`, and `mu(q)=<q,C^2q>=Z/E`.  On the unit
`L^2` sphere the universal self-adjoint Rayleigh identity is
`grad_S R_A=2(A-R_A)q`; hence `g:=grad_S lambda=2(C-lambda)q`,
`B=(r/2)g=E grad_u(H/E)`, and `D_B/E=||g||^2/4`.  Operator squaring becomes the
universal first-jet law `R_(A^2)=R_A^2+||grad_S R_A||^2/4`, so
`mu=lambda^2+||g||^2/4` and `C^2q=mu q+grad_S(mu)/2`.

Writing `K_q v=P(q cross v)`, the literal normalized Navier--Stokes dynamics are
`rdot=-nu r mu` and `qdot=(r/2)K_q g-(nu/2)grad_S mu`.  Since
`grad_S mu=2 lambda g+(1/2)Hess_S(lambda)g`, this is the one-landscape operator law
`qdot=[(r/2)K_q-nu lambda I-(nu/4)Hess_S(lambda)]g`.  Euler preserves `lambda`
exactly, so inviscid growth of `mu` is only steepening of the same Rayleigh
landscape along its own level set.  The exact law is
`mu_dot=(r/4)<Hess(lambda)g,K_q g>-(nu/2)||grad_S mu||^2`, equivalently an
`[Hess(lambda),K_q]` or `[C,K_q]` commutator.  The previous leaf-tangent enstrophy
residual is not primitive: `R_Z=(r/4)P_{q,g}^perp Hess(lambda)g`.

There is also a whole-functional-calculus bridge to the earlier material Hodge Lax
theorem.  For smooth divergence-free fields, `C K_q=-ad_q`, so on the mean-zero
sector `K_q=-C^{-1}ad_q` and for every admissible spectral multiplier
`[F(C),K_q]=C^{-1}[ad_q,F(C)]`; with `u=rq`,
`r[F(C),K_q]=C^{-1}[ad_u,F(C)]`.  Thus spectral transfer and material Hodge operator
motion use one literal commutator defect rather than two analogous mechanisms.
Relative to `span{q} + T_q S`, curl itself is exactly
`[[lambda,g*/2],[g/2,lambda I+Hess(lambda)/2]]`, and because `lambda` is quadratic
its Hessian derivative is algebraically forced by `g` and the sphere velocity; no
independent third phase-sphere jet exists.

Classification: all displayed Rayleigh, normalized-PDE, block-operator,
tangent-curvature and commutator identities Exact on the common smooth core; the
cross-representation synthesis Rigorous; any anti-Zeno/no-escape consequence Open.
No continuation, restart, blow-up exclusion or global-regularity theorem is claimed.

## Energy-ray Lax / double-bracket compression

The normalized Rayleigh law descends from a shorter rank-one operator identity.  For
`u=r q`, `||q||_2=1`, define the energy-ray projector `Pi=q tensor q`.  With the
existing skew Poisson operator `J(u)` and `C=curl`, the unnormalized dyad
`Q=u tensor u` obeys exactly `Qdot=[J(u),Q]-nu{C^2,Q}`.  Dividing by
`tr Q=r^2` converts the viscous anticommutator into a canonical double bracket:
`Pidot=[J(u),Pi]-nu[Pi,[Pi,C^2]]`.  Equivalently the whole normalized state is one
skew Lax rotation, `qdot=A_NS q`, `Pidot=[A_NS,Pi]`, with
`A_NS=J(u)+nu[Pi,C^2]` and `A_NS^*=-A_NS`; all actual `L^2` loss is isolated in
`rdot=-nu r mu`, `mu=tr(Pi C^2)=Z/E`.

The unique off-diagonal shape mismatch is `D=[Pi,C]`.  If
`lambda=<q,Cq>=H/E` and `g=grad_S lambda`, then exactly
`D=(q tensor g-g tensor q)/2`, `D q=-g/2`, `B=-r D q`, and
`mu-lambda^2=||D||_HS^2/2=D_B/E`.  The viscous ray generator is simply one Hodge
action on this same defect: `[Pi,C^2]=D C+C D={C,D}`.  The projective Euler motion
also sees only `D q`, because `J(u)q=r P_sigma(q cross Cq)=-r K_q Dq`; the aligned
`lambda q` component is exactly invisible.  Therefore the Rayleigh slope, Beltrami
defect, Euler ray rotation, viscous ray rotation and extra radial drain are not
independent mechanisms below the ray--curl commutator.

For every admissible self-adjoint Hodge multiplier `F(C)`, the same Lax equation gives
`m_Fdot=<q,[F(C),J(u)]q>-2nu(m_(F C^2)-m_F m_(C^2))`, so normalized viscosity is a
centered spectral `C^2` covariance/selection law and Euler is the corresponding
Hodge commutator current.  The spectral measure remains phase-incomplete and is not
a closed state.

A rigorous energy-level cumulative consequence follows without a new badness score.
Sobolev duality on the three-torus gives
`||X_E||_(H^-1/2) <= C_T ||C u||_2 ||B||_2`, hence
`||X_E||_(H^-1/2) <= (C_T/nu) sqrt(1-lambda^2/mu) (-Edot)` and similarly
`||(qdot)_Euler||_(H^-1/2) <= (C_T/nu) sqrt(1-lambda^2/mu) (-rdot)`.
Thus the total weak Euler path is finite and paid by the literal viscous energy/radius
loss, with zero density at Beltrami alignment.  This is only a weak-topology
anti-Zeno theorem; it does not control the positive Hodge topology needed for
continuation.

Classification: dyadic, double-bracket, skew-ray Lax, ray--curl defect and normalized
moment identities Exact on the common smooth core; the `H^-1/2` cumulative path
bound Rigorous; a stronger zero-curvature/mismatch-transport law, positive-topology
anti-Zeno, continuation, restart, blow-up exclusion and global regularity Open.

The same milestone admits a lower Lie/Hodge form.  For smooth divergence-free `v`,
`C J(u)v=[C u,v]_Lie` modulo the fixed harmonic convention.  Evaluated on the actual
state, `ad_u u=0` gives the exact master identity
`u_t=C^-1[C,ad_u]u-nu C^2u`.  Thus Euler is precisely the inverse-Hodge image of the
failure of the first-order Hodge operator to commute with self-Lie transport, while
viscosity is the square of the same operator.  This is the Eulerian face of the same
Hodge/Lie noncommutation whose material form is `C_Gdot=[L_U,C_G]`.

The ray and transport commutators collapse on the normalized state.  With
`D=[Pi,C]`, `Dq=lambda q-Cq`, hence exactly
`[C,ad_q]q=[q,Dq]` and
`qdot=r C^-1[q,Dq]+nu{C,D}q`.  Therefore both nonlinear Lie rotation and viscous Hodge
rotation are forced actions of the one ray--curl mismatch `D`; its squared
Hilbert--Schmidt size is simultaneously the non-Beltrami part of the radial tax.
Moreover `Ddot=[A_NS,D]-[Pi,[A_NS,C]]`.  The Lax transport term has zero
Hilbert--Schmidt pairing with `D`, so all change of mismatch size is generated by the
curvature source `-[Pi,[A_NS,C]]`, with
`[A_NS,C]=[J(u),C]+nu[D,C^2]`.  A positive-topology cumulative control of this exact
curvature source is now the sharp operator anti-Zeno seam; it remains Open.

## Projective Hodge covariance / causal heat-age compression

The ray--curl mismatch theorem has been extended to the whole Hodge functional
calculus.  For `Pi=q tensor q` and any self-adjoint Hodge multipliers `F(C),G(C)`, set
`D_F=[Pi,F(C)]`.  Rank-one algebra gives exactly
`Cov_q(F,G)=<D_F,D_G>_HS/2`, hence `Var_q(F)=||D_F||_HS^2/2`.  In curl spectral
coordinates `D_F(c,d)=(F(d)-F(c))Pi(c,d)`, so every Hodge mismatch is a
scalar divided-difference image of the one first-order defect `D=[Pi,C]`.  The same
is true of sources: with `K=[A_NS,C]`, every `[A_NS,F(C)]` is the identical
divided-difference transform of `K`, and the universal covariant law is
`nabla_t^A D_F=-[Pi,mathfrak D_F^C(K)]`.  Thus stronger Sobolev, critical, heat and spectral
readouts carry no independent mismatch/source mechanism.

The Hilbert--Schmidt spectral formula also yields a contraction principle: scalar
Lipschitz `F` obeys `||[Pi,F(C)]||_HS<=Lip(F)||D||_HS`.  In particular
`||[Pi,|C|]||_HS<=||D||_HS` and, writing `kappa=<q,|C|q>=Kcrit/E`,
`kappa^2-lambda^2=(||D||_HS^2-||[Pi,|C|]||_HS^2)/2`.  The contraction defect is
supported exactly on opposite-sign curl pairs, giving an operator form of the
heterochiral critical obstruction.  Heat satisfies both
`||[Pi,e^-hC^2]||_HS<=sqrt(2h/e)||D||_HS` and the exact Duhamel law generated by
`D_(C^2)={C,D}`.

The preceding weak Hamiltonian-path theorem now yields a causal positive-topology
reduction.  Define only as shorthand the active fraction
`theta=||B||/||Cu||=sqrt(1-lambda^2/mu)=||D||_HS/sqrt(2mu)` and the positive measure
`dM=theta(-dE)`.  It is a submeasure of literal viscous energy loss and vanishes
identically at Beltrami alignment.  The mild equation
`u(t)=e^-nu(t-a)A u(a)+int e^-nu(t-s)A X_E(s) ds`, together with
`||X_E||_(H^-1/2)dt<=(C_T/nu)dM`, gives the rigorous critical Abel bound
`||A^(1/4)u(t)||_2 <= C[nu(t-a)]^-1/4 r(a) + C nu^-3/2 int_a^t
(t-s)^-1/2 dM(s)`.  Under the canonical heat-age change `h=2nu(t-s)`, this is the
same `h^-1/2` moment used by the repository's exact critical heat representation.
Thus divergence of the positive critical Hodge norm requires a uniformly finite
positive defect-weighted energy-loss measure to concentrate at the single parabolic
boundary `h=0`.  A Dini-half modulus of that active loss would rule out this causal
critical Zeno mechanism, but no such intrinsic modulus is proved.

Classification: rank-one Hodge covariance Gram, divided-difference generation,
critical contraction/heterochiral gap, heat commutator, whole-Hodge projective pairing
and covariant curvature laws Exact on their stated smooth/bounded domains; the
Lipschitz contractions, weak-forcing-to-critical Abel bound and parabolic-clock
identification Rigorous; intrinsic boundary modulus, positive-topology anti-Zeno,
continuation, restart, blow-up exclusion and global regularity Open.

## Canonical ray connection / eikonal Hodge hierarchy correction

The curvature source from the preceding milestone has a projective gauge redundancy.
Any skew generator `A` of the same rank-one ray decomposes exactly as
`A=Gamma+A_parallel`, where `Gamma=qdot tensor q-q tensor qdot=[Pi,[Pi,A]]` and
`[A_parallel,Pi]=0`.  Therefore the full `K=[A_NS,C]` is not a canonical primitive
below the ray level: its tangent-gauge contribution cancels between the Lax-transport
and curvature faces of `Ddot`.  The invariant rank-two law is
`Pidot=[Gamma_NS,Pi]` with `Gamma_NS=qdot tensor q-q tensor qdot`.  Viscosity
`nu[Pi,C^2]` is already canonical; only the Euler Poisson operator carries the extra
tangent block.

For every quadratic Hodge Rayleigh readout `R_F(q)=<q,F(C)q>` and
`D_F=[Pi,F(C)]`, the canonical curvature is simply
`nabla_t^Gamma D_F=(1/2) q wedge Hess_S(R_F) qdot`.  In particular the mysterious
ray--curl curvature reduces to the Hessian of the one curl-Rayleigh landscape applied
to the actual ray velocity.  No independent operator-curvature state survives this
quotient.

The same Rayleigh-square identity iterates to all positive dyadic Hodge levels.  With
`Lambda=|C|`, `F_n=Lambda^(2^n)` and `R_n=<q,F_n q>`, exactly
`R_(n+1)=R_n^2+||grad_S R_n||^2/4=R_n^2+||[Pi,F_n]||_HS^2/2`.  Hence each next
Hodge level is only current center squared plus current projective spread.  At the
critical base, `kappa=Kcrit/E=<q,Lambda q>` and `mu=Z/E` satisfy
`mu=kappa^2+||[Pi,Lambda]||_HS^2/2`, so
`-rdot/(nu r)=kappa^2+||[Pi,Lambda]||_HS^2/2`.

Viscosity has a whole-cone monotonicity: for every nondecreasing scalar `f` on the
positive spectrum of `A=C^2`, `(d/dt)<q,f(A)q>|_visc=-2nu Cov_q(f(A),A)<=0`, because
the pair kernel `(f(x)-f(y))(x-y)` is nonnegative.  Thus the one viscous projective
direction simultaneously sorts every monotone positive Hodge readout downward.

A new exact null theorem holds on any single Laplacian shell, not only a signed
Beltrami eigenspace.  `[Pi,Lambda]=0` iff `Lambda q=kappa q`, hence
`C^2q=kappa^2q`.  At such an instant `(kappadot)_Euler=(kappadot)_visc=0` and
`(qdot)_visc=0`, while `rdot=-nu kappa^2 r`.  A heterochiral `+/-kappa` mixture may
still have signed `D=[Pi,C]` nonzero, so Euler can move the ray, but it must first
create positive spread: at the shell
`D_Lambdadot=q wedge (Lambda-kappa)(qdot)_Euler`, and
`kappaddot=2<(qdot)_Euler,(Lambda-kappa)(qdot)_Euler>` with no universal sign.  Thus
critical cascade has an exact create-spread-before-center-transfer anatomy.

Classification: ray-gauge decomposition, canonical rank-two connection, Hessian
curvature law, eikonal square recursion, critical center/spread radius identity and
one-shell null/second-variation laws Exact; whole monotone viscous-cone descent and
the architecture correction Rigorous; cumulative exclusion of repeated spread
creation, Dini-half parabolic anti-Zeno, continuation, restart, blow-up exclusion and
global regularity Open.

## Polar twin-Rayleigh / critical quotient-action compression

The normalized operator law has descended through the polar decomposition
`C=J Lambda`, `Lambda=|C|`.  Define the signed and positive energy-sphere Rayleigh
functions `lambda=<q,Cq>=H/E` and `kappa=<q,Lambda q>=Kcrit/E`.  Since
`C^2=Lambda^2`, the universal square identity gives the exact twin eikonal law
`mu=Z/E=lambda^2+||grad lambda||^2/4=kappa^2+||grad kappa||^2/4`.  The same square
has a positive tangent factorization `grad mu=M_q grad kappa` with
`M_q=P_q(Lambda+kappa)P_q>0`.  Hence literal normalized Navier--Stokes is
`qdot=(r/2)K_q grad lambda-(nu/2)M_q grad kappa`, `rdot=-nu r mu`: signed curl
supplies the skew orientation mobility and positive curl supplies the symmetric
critical mobility, both tied by one Hodge square.

Writing `a_E=(qdot)_Euler`, the positive critical center obeys exactly
`kappadot=<grad kappa,a_E>-(nu/2)<grad kappa,M_q grad kappa>`.  Completing the
actual positive metric yields
`kappadot=-(nu/2)||M_q^(1/2)grad kappa-nu^-1 M_q^-1/2 a_E||^2
+(2nu)^-1 Acrit`, where `Acrit=<a_E,M_q^-1 a_E>`.  Equivalently, with
`a_nu=(qdot)_visc`,
`kappadot=(2nu)^-1(||a_E||_(M^-1)^2-||a_E+2a_nu||_(M^-1)^2)`.  Thus maximum
critical feeding requires the exact impedance match `a_nu=-a_E/2`; a one-shell state
has `a_nu=0` and zero critical-center derivative even if Euler still moves the ray.

The action is not an added score.  Let `S_Lambda X=Lambda X+X Lambda`.  Among every
skew Hilbert--Schmidt generator `A` with `Aq=a`, the exact quotient minimum is
`inf <A,S_Lambda^-1 A>_HS=2<a,M_q^-1a>`.  The optimizer is
`A_*=S_Lambda(p tensor q-q tensor p)`, `p=M_q^-1a`; tangent-gauge cross terms vanish
because every competitor difference kills `q`.  A variational bound gives
`Acrit<=<a_E,(Lambda+kappa)^-1 a_E><=<a_E,Lambda^-1a_E>`, so the critical quotient
action is weaker than the homogeneous `H^-1/2` ray action.

Integrating the exact square shows that finite `int Acrit dt` bounds `kappa`.  Thus
any blow-up of the physical positive critical quadratic requires
`int Acrit=+infinity`, hence the Euler ray has infinite `L^2_t dot H^-1/2` action.
The preceding theorem already proves finite `L^1_t H^-1/2` ray length, so the
remaining Zeno is necessarily finite-length/infinite-action.  Since
`||a_E||_(H^-1/2)<=(C_T/nu) theta(-rdot)`, `theta=sqrt(1-lambda^2/mu)`, critical
escape further forces the actual active radial-loss density `theta(-rdot)` to lie in
`L^1` but not `L^2`.

The older common-kernel square has also been quotient-reduced.  In the pair Hilbert
space with norm `||F||_P^2=(1/2)doubleint K_Lambda |F|^2`, the increment map satisfies
`delta^*delta=Lambda`.  For `b_u(x,y)=u(x) cross u(y)`,
`delta^* b_u=P_H[-u cross Lambda u]=Y`.  Only the exact-increment projection
`P_R b_u=delta Lambda^-1 Y` pairs with `delta omega`, and
`||P_R b_u||_P^2=<Y,Lambda^-1Y><=||b_u||_P^2`.  Hence the old positive pair
remainder is an exact upper envelope; the dynamically realizable remainder is its
Riesz-projected inverse-Hodge action.

Classification: polar/twin-eikonal, positive mobility, normalized polar PDE,
critical action/reflection, quotient-minimum and pair-Riesz identities Exact on the
stated smooth domains; action-to-weak-topology comparison and finite-length/infinite-
action Zeno consequence Rigorous; finiteness of the quotient action, exclusion of
active-loss spikes, continuation, restart, blow-up exclusion and global regularity
Open.

## Causal heat-ray projective zero-curvature compression

The zero-curvature question left open by the energy-ray Lax theorem has an exact
answer after lifting the actual state over canonical heat age.  Put
`S_h=e^-hA/2`, `u_h=S_hu`, `r_h=||u_h||`, `q_h=u_h/r_h`, and
`P_h=q_h tensor q_h`.  The heat direction is exactly
`partial_h q_h=-(A-mu_h)q_h/2`, hence
`partial_h P_h=[B_h,P_h]` with `B_h=[P_h,A]/2`.  In the causal parabolic direction
`D_nu=partial_t-2nu partial_h`, the explicit viscous term cancels:
`D_nu u_h=S_hX_E(u)`.  Thus
`D_nu q_h=r_h^-1(I-P_h)S_hX_E(u)` and
`D_nu P_h=[Gamma_h^E,P_h]` for its canonical rank-two skew connection.  Since
`[D_nu,partial_h]=0`, Jacobi gives the exact projective zero-curvature law
`[partial_h Gamma_h^E-D_nu B_h+[Gamma_h^E,B_h],P_h]=0`.

The nonlinear content of this lift is one vector defect,
`N_h=S_hX_E(u)-X_E(S_hu)=P_sigma[S_h(u cross Cu)-S_hu cross S_hCu]`.  This is exactly
the existing cross-product heat-product/carre-du-champ defect.  Its radial projection
is the canonical scale flux:
`Pi_heat=-<u_h,N_h>` and `D_nu r_h=<q_h,N_h>`.  Its tangent projection is exactly the
renormalization anomaly in the heat-resolved Euler ray connection:
`D_nu q_h=X_E(u_h)/r_h+r_h^-1(I-P_h)N_h`.  Hence scalar cascade and directional
connection anomaly are not independent heat mechanisms.

The existing heat continuity law is now the radial flatness equation.  Since
`E(h,t)=r_h^2/2` obeys `partial_h E=-rho` and `D_nu E=-Pi_heat`, commutation of the
two derivatives is exactly `rho_t-partial_h(2nu rho+Pi_heat)=0`.  The projector
zero-curvature law is the directional counterpart of the same mixed-derivative
compatibility.  Therefore every positive heat-age rectangle is projectively flat;
any remaining Zeno escape must be a singular boundary concentration at `(T,0)`.

The polar action was also quotiented to the one scalar direction relevant to critical
center transfer.  With `T_kappa=<grad kappa,(qdot)_E>` and
`V_kappa=<grad kappa,M_q grad kappa>`, define
`A_rel=T_kappa^2/V_kappa` off the one-shell null set and zero on it.  The exact scalar
square is
`kappadot=-(nu/2)(sqrt(V_kappa)-T_kappa/(nu sqrt(V_kappa)))^2+A_rel/(2nu)`, so
critical escape requires `int A_rel=+infinity`, and `A_rel<=A_crit` by the positive
mobility Cauchy inequality.

A direct snapshot bound `A_rel <= C r^2 mu` is not compatible with spatial
intermittency.  Euclidean `L^2`-normalized localization has the exact formal Hodge
scaling `mu~eps^-2`, `V_kappa~eps^-3`, `T_kappa~eps^-7/2`, hence
`A_rel/mu~eps^-2`.  A torus auditor uses a nonzero-transfer mixed-helical carrier
triad at `N k_j`, multiplies its vector potential by a real Dirichlet envelope of
bandwidth `N`, takes curl (so divergence-free structure is exact), and normalizes in
`L^2`.  For `N=1,...,5`, `T_kappa^2/(mu V_kappa)` equals approximately
`0.000830, 0.001659, 0.003307, 0.005688, 0.008799`; after division by `N^2` the last
three values are `0.000367, 0.000356, 0.000352`.  The measured log slopes on
`N=2,...,5` are about `3.29,1.87,2.89,1.82` for `T_kappa,mu,V_kappa,ratio`, moving
toward the localization exponents `7/2,2,3,2`.  This is an audited adversarial
scaling calibration, not a rigorous torus asymptotic theorem.  It rules out using a
scale-wrong instantaneous action/drain estimate as the architecture endpoint; the
missing compensator must retain the parabolic heat/time variable.

Classification: heat lift, heat-age double bracket, causal ray Lax law, one vector
renormalization defect, radial flux identity, scalar continuity-as-flatness and
projective zero-curvature Exact; their synthesis Rigorous.  Intermittent wavepacket
onset Audited.  Boundary compactness/holonomy at `(T,0)`, action nonconcentration,
continuation, restart, blow-up exclusion and global regularity remain Open.

## Critical-spread heat continuity / boundary kinetic-action reduction

The polar critical action has acquired a literal positive continuity-law state.  On
the normalized heat ray set `kappa(h,t)=<q_h,Lambda q_h>`, `Lambda=|C|`.  Exact heat
sorting gives
`chi:=-partial_h kappa=<q_h,Lambda^3 q_h>-kappa mu=Cov_h(Lambda,Lambda^2)>=0`.
Equivalently
`chi=(1/2)<[P_h,Lambda],[P_h,A]>_HS=(1/2)<D_Lambda,S_Lambda D_Lambda>_HS`, and the
spectral pair form is
`chi=(1/2) E[(ell-ell')^2(ell+ell')]`.  Thus the one-Laplacian-shell null set is
exactly `chi=0`.

Define the causal current `Theta=D_nu kappa`,
`D_nu=partial_t-2nu partial_h`.  Since `D_nu` commutes with `partial_h`, literal NS
forces
`D_nu chi+partial_h Theta=0`, equivalently
`chi_t+partial_h(Theta-2nu chi)=0`.  In projective form
`Theta=-<Gamma_h^E,[P_h,Lambda]>_HS`.  At `h=0`,
`Theta=T_kappa` and `4chi=V_kappa`, so
`A_rel=T_kappa^2/V_kappa=(1/4)Theta(0)^2/chi(0)`.  The scalar critical square is
therefore exactly the boundary kinetic `flux^2/mass` action of a positive transport,
and `kappadot=Theta(0)-2nu chi(0)` is its boundary current law.

For a fixed nonzero smooth torus state, normalized heat sorting selects the lowest
occupied positive Hodge shell `ell_*`, giving the exact mass identity
`int_0^infty chi dh=kappa(0)-ell_*`.  Also
`K_h=(1/sqrt(pi))int_0^infty s^-1/2 rho(h+s) ds` and
`kappa=K_h/E_h`, so `chi=-partial_h kappa` is derived from the existing positive
heat-energy profile rather than an independent population.  The genuinely oriented
information remains in `Theta`, already generated by the projectively flat
heat-renormalized Euler connection.

Classification: positive spread density, spectral/projective representations,
critical continuity law, boundary current identities, kinetic-action identification,
fixed-state total spread mass and heat subordination Exact.  The interpretation as
one positive transport face Rigorous.  Finiteness of the boundary kinetic-action
trace, boundary compactness at `(T,0)`, continuation, restart, blow-up exclusion and
global regularity remain Open.

## Abstract shell-ladder escape / self-Lie stop theorem

An adversarial abstract Hodge system shows that the recent projective/heat
compression is not sufficient for no-escape unless the literal NS Lie/Lamb
realization is retained.  Let an abstract real Hilbert space have orthonormal
`s_n,t_n`, `L_n=2^n`, and self-adjoint
`C s_n=L_n t_n`, `C t_n=L_n s_n`.  Thus each shell is the real form of a paired
`+/-L_n` curl eigenspace and `A=C^2` has shell value `L_n^2`.  Choose a smooth
flat-endpoint monotone quarter-turn profile and transition from `s_n` to `s_(n+1)`
over `delta_n=L_n^-4`.  The intervals have finite total length.  Every `t<T` state
has finite spectral support and is in the common smooth Hodge core.

On the `n`th transition, with `L=L_n`, `q=c s_n+s s_(n+1)`, one has exactly
`lambda=<q,Cq>=0`, `kappa=L(c^2+2s^2)`, and
`mu=L^2(c^2+4s^2)`.  Solving `rdot=-nu r mu` gives
`int_(I_n)mu<=4L^-2`, hence `int_0^T mu<infinity` and `r->r_*>0`, while at shell
endpoints `kappa=L_(n+1)->infinity`, so the physical critical quadratic
`E kappa->infinity`.

Let `v_n=-s s_n+c s_(n+1)`.  The viscous normalized ray velocity is exactly
`a_nu=-3nu L^2 c s v_n`.  With the prescribed geometric velocity
`qdot=theta_dot v_n`, define
`a_E=(theta_dot+3nu L^2cs)v_n` and
`J_*=a_E tensor q-q tensor a_E`.  Then `J_*^*=-J_*`, `J_*q=a_E`, and because
`Cq` lies in the orthogonal `t` sector, `J_*Cq=0`.  Therefore the abstract path obeys
exactly `qdot=J_*q-nu(C^2-mu)q`, and the physical state obeys
`u_t=J_*u-nu C^2u`, retaining skew energy conservation and Casimir nullity.

The weak geometry realizes all necessary Zeno signatures.  Since
`||v_n||_(dot H^-1/2)^2=s^2/L+c^2/(2L)`, the Euler weak path length per transition is
`O(L^-1/2)+O(nu L^-5/2)`, hence summable.  If
`C2=int_0^1 |vartheta'|^2>0`, then weak quadratic action is at least
`C2 L^3/2` per transition.  The positive critical mobility on this tangent line is
exactly `3L`; therefore
`A_rel=(theta_dot+3nuL^2cs)^2/(3L)` and its integral is at least `C2 L^3/3`, so the
critical action diverges.  Because `lambda=0`, the active radial density is
`g_act=-rdot=nu r mu`; its `L1` mass is finite but each transition contributes a
fixed positive lower bound to `int g_act^2`, hence `g_act notin L2`.

The normalized heat lift of this abstract fixed-Hodge path still satisfies the same
heat sorting identities, mixed-derivative projective flatness and positive
critical-spread continuity law.  Thus those structures plus skewness and Casimir
nullity are abstractly insufficient.  The construction is **not** Navier--Stokes:
`J_*` is not the fixed divergence-free Lie--Poisson/Lamb operator
`P_sigma(v cross Cu)=C^-1[Cu,v]_Lie`, and no Jacobi/Fourier-triangle/de Rham local
realization is claimed.  This is an architecture stop theorem: a future no-escape
proof must use an identity which fails for arbitrary shell-dependent skew
Casimir-null rotation and depends essentially on the fixed physical self-Lie current.

Classification: shell construction, finite reservoir, escape, skew/Casimir-null
operator, weak-length/action and active-loss estimates Exact/Rigorous in the
abstract model; insufficiency of the abstract Hodge/ray/heat package Rigorous.  No
NS counterexample is claimed.  The shortest physical self-Lie compatibility which
excludes the adversary remains Open.

## Self-Lie derivation / Hodge-square carre-du-champ realization

The physical constraint missing from the abstract shell-ladder escape has been
compressed to one fixed derivation law.  For divergence-free
`[f,g]=(f.grad)g-(g.grad)f` and `A=-Delta=C^2`, direct differentiation gives
`A[f,g]-[Af,g]-[f,Ag]=-2 sum_j[partial_j f,partial_j g]`, hence
`[A,ad_f]=ad_(Af)-2 sum_j ad_(partial_j f) partial_j`.  This is a Lie
carre-du-champ: the commutator of the viscous Hodge square with the conservative
transport representation has a forced local first-derivative source.

For `P_s=e^-sA`, the heat Lie defect is exactly
`D_s^Lie(f,g)=P_s[f,g]-[P_s f,P_s g]
=2 int_0^s P_(s-r) sum_j[partial_j P_r f,partial_j P_r g] dr`.  Since
`C X_E(u)=[Cu,u]`, the established heat-ray vector anomaly satisfies
`C N_h=S_h[Cu,u]-[S_hCu,S_hu]` and is this same Lie defect with `f=Cu,g=u,s=h/2`.
Thus radial heat flux, tangent ray renormalization, cross-product heat anomaly and
the new Lie derivative defect are representations of one fixed self-Lie product.

In Fourier variables the ordered bracket contribution at `p+q=k` is
`i[(f_p.q)g_q-(g_q.p)f_p]`.  Divergence-free geometry gives the exact transverse
typing
`|f_p.q|<=|p cross q||f_p|/|p|` and the analogous `g` bound, hence the bracket
vanishes on collinear triangles.  Heron yields
`|p cross q|^2<=2ab(a+b)(a+b-c)` for side lengths `a,b,c`, and for equal input
shells `(|p cross q|/|p+q|)^2=L^2-|p+q|^2/4`; exact doubling has zero projected
coupling.  The heat defect multiplier of the same pair is
`e^-s|p+q|^2-e^-s(|p|^2+|q|^2)`, controlled by `p.q`, while
`(p.q)^2+|p cross q|^2=|p|^2|q|^2`.  Transfer and heat renormalization are therefore
complementary dot/area faces of one pair geometry.

A favorable one-shell second-variation sign is nevertheless false.  On the unit
shell take a real positive-helicity Beltrami pair at `+/-p`, `p=(1,0,0)`, and a real
negative-helicity pair at `+/-q`, `q=(0,1,0)`, with equal amplitudes and total L2
norm one.  The projected Lamb vector lies at the four modes `+/-(p+q),+/-(p-q)`, all
of magnitude `sqrt(2)`, with total L2 mass `3/8`.  Hence the exact shell formula gives
`kappaddot_E=2<a_E,(Lambda-1)a_E>=3(sqrt(2)-1)/4>0`.  The orthogonal pair also has
zero heat renormalization multiplier because `p.q=0`, so heat-anomaly size cannot
pointwise dominate every dangerous interaction.

Classification: self-Lie/Hodge-square derivative defect, heat Lie anomaly, Fourier
area typing, Heron soft edge, dot--area lock and sparse shell calibration Exact;
architecture synthesis Rigorous.  The remaining target is cumulative phase
coherence/intermittency of one fixed local Lie current, not another snapshot sign or
score.  No no-escape or regularity theorem is claimed.

## 2026-08-14 — material–vortex spacetime curvature / primitive current compression

- **Exact spacetime current curvature:** with `alpha=u^flat`, `beta=d alpha`, `J_NS=i_u beta+nu delta beta`, `varphi=B-alpha(u)`, literal NS gives `F=d_(t,x)(alpha+varphi dt)=beta-dt wedge J_NS`.  Hence `dF=0` is exactly the de Rham current law `beta_t+dJ_NS=0`; pressure/Bernoulli chooses the spacetime potential but disappears from the curvature.
- **Exact material constitutive law:** for `V=partial_t+u`, `i_V F=-nu(delta beta-delta beta(u)dt)`, so the spatial material curvature defect is exactly `-nu delta beta`.  Euler has the exact kernel law `i_V F=0`.
- **Exact material–vortex commutator:** the vector vorticity PDE is `[V,omega]=-nu A omega`, `A=-Delta`.  Since `d delta beta=Delta_H beta`, the material kernel defect `delta beta` and the material–vortex commutator defect `d delta beta` are consecutive de Rham levels of the same viscous current.
- **Exact Lagrangian-graph descent:** for the actual flow graph `Psi(t,a)=(t,Phi_t(a))`, `Psi^*F=bar beta-nu dt wedge delta_G bar beta`; closedness gives `bar beta_t+nu Delta_(H,G)bar beta=0`.  Thus the earlier material Hodge-heat theorem is the pulled-back Bianchi identity of the same spacetime curvature.
- **Exact scalar operator law:** with `D=partial_t+u.grad`, `W=omega.grad`, `A=-Delta`, `[D+nu A,W]=-2nu sum_j(partial_j omega.grad)partial_j`.  The Euler commuting material/vortex generators and the viscous carre-du-champ derivative defect are one operator law.
- **Exact worldsheet / helicity faces:** Stokes on a material loop worldsheet gives `d/dt int_gamma alpha=-nu int_gamma delta beta`; exterior algebra gives `F wedge F=-2nu dt wedge delta beta wedge beta` and `d(A_spacetime wedge F)=F wedge F`, so the local/global viscous helicity law is the same curvature transgression.
- **Audited exact referees:** the periodic one-mode NS heat shear gives zero residual for `[V,omega]+nu A omega` and for the scalar parabolic commutator.  The Beltrami family `u_N=e^(-nu N^2t)(sin Nz,cos Nz,0)` gives `curl u_N=N u_N`, `A omega_N=N^2 omega_N`, keeps `[V,omega_N]` parallel to `omega_N`, yet has `|delta beta_N|^2=N^4|u_N|^2` and Pfaffian/helicity density of order `N^3|u_N|^2`.  Therefore raw curvature-kernel, commutator, or Pfaffian magnitude is not badness.
- **Frontier:** no-escape, if true, must control cumulative *transverse* self-generated material–vortex noncommutation while the same `delta beta` simultaneously supplies material kernel defect, its exterior derivative, Hodge heat, Kelvin leakage and viscous Bochner square.  No such cumulative theorem is proved here; continuation/restart/global regularity remain Open.

## 2026-08-14 — self-generated current adjoint-square master law

- **Exact primitive adjoint pair:** for `alpha=u^flat`, set `R_alpha=nu d+alpha wedge`; periodic Hodge adjointness forces `C_alpha=R_alpha^*=nu delta+i_u`, and `C_alpha beta=J_NS` for `beta=d alpha`.
- **Exact whole exterior-algebra curvature squares:** `R_alpha^2=nu beta wedge`, `(R_alpha^*)^2=nu i_(beta sharp)`, equivalently `{delta,i_u}=i_(beta sharp)`.  Generic polynomial referees on form degrees 0–3 give zero residual.  In particular `C_alpha J_NS=nu|omega|^2` pointwise, with all derivatives of an arbitrary scalar cutoff cancelling in `C_alpha^2(f beta)=nu f|omega|^2`.
- **Exact finite descent:** `1 -> alpha -> nu beta -> nu alpha wedge beta ->0`; adjointly `vol -> i_u vol -> nu omega^flat -> nu u.omega ->0`; and `beta -> J_NS -> nu|omega|^2 ->0`.
- **Exact whole-PDE factorization:** `R_alpha alpha=nu beta` and `R_alpha^*R_alpha alpha=nu J_NS`, hence `alpha_t+(1/nu)R_alpha^*R_alpha alpha=d varphi`, `varphi=-(p+|u|^2/2)`, and after Hodge projection `alpha_t=-(1/nu)P R_alpha^*R_alpha alpha`.  Exact periodic heat shear gives zero residual.
- **Exact energy / local constraint faces:** `Edot=-(1/nu)||R_alpha alpha||^2=-nu||omega||^2`; the second current descent splits as `i_u J_NS=nu u.curl omega` and `delta J_NS=|omega|^2-u.curl omega`.  With `J_NS=-alpha_t+d varphi`, these are respectively the local kinetic-energy Lamb equation and `Delta_H varphi=|omega|^2-u.curl omega`, equivalent to the pressure Poisson constraint.
- **Exact current evolution:** with `H_u=partial_t+{d,C_alpha}=partial_t+L_u+nu Delta_H`, `[H_u,C_alpha]=i_(u_t)+nu[d,i_(beta sharp)]`; since `H_u beta=0`, `H_u J_NS=i_(u_t)beta+nu d|omega|^2`, or `H_u J_NS+i_((P J_NS)^sharp)beta=nu d|omega|^2` after projected momentum.  Thus the current equation is not an independent PDE.
- **Exact symmetric-square / strain face:** `R_alpha^*R_alpha+R_alpha R_alpha^*=nu^2 Delta_H+|u|^2+nu(L_u+L_u^*)`; on one-forms the symmetric Lie part is `+2S`, on two-forms it is `-2S`.  Applying to beta yields `2nu int omega.S omega=nu^2||curl omega||^2+||u cross omega||^2-||J_NS||^2`, the current-interference form of stretching.
- **Anti-overclaim:** the frozen co-closed mobility `(1/nu)P R_alpha^*R_alpha P` is positive, but state dependence contains the Euler Lamb rotation.  A smooth finite Fourier torus datum has audited `int omega.S omega=310/3`, `int|grad omega|^2=450`; amplitude scaling above `135/31` at `nu=1` gives positive instantaneous enstrophy growth.  High-frequency Beltrami heat modes also remain a no-go against raw curvature/current-square badness.
- **Frontier:** no-escape must use the self-generated adjoint-square feedback itself: the state creates `R_alpha`, its square creates vorticity curvature, its adjoint reads that curvature as the literal current, and the current moves the state.  Whether this closed curvature/current loop can Zeno-concentrate in finite time remains Open; no continuation or regularity theorem is claimed.
