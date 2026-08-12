# Kelvin clock, parabolic covariance, and moving-cut compatibility audit

This audit incorporates the proof-critical findings raised in Draft PR #1 and
separates what is exact, what was false, and what remains open.

No continuation, restart, or regularity theorem is claimed.

## 1. Two clocks must not be silently identified

For the exact one-mode Navier--Stokes shear

\[
u(a,t)=e^{-\nu k^2t}\cos(ka),
\]

a forward Brownian anchor with covariance `2 nu` gives

\[
\boxed{
(\partial_t+\nu\partial_a^2)u=-2\nu k^2u\neq0.
}
\]

Thus the physical-time forward Brownian evaluation is not the Kelvin martingale.
In the causal backward-Kelvin orientation,

\[
\boxed{
(\partial_t-\nu\partial_a^2)u=0.
}
\]

Likewise, for `s<Theta`, ordinary forward Brownian conditioning of the future NS
field gives

\[
\boxed{
\mathbb E[u(A_\Theta,\Theta)\mid A_s=a]
=e^{-\nu k^2(2\Theta-s)}\cos(ka),
}
\]

which is not `u(a,s)` unless `Theta=s`.

**Physical classification.** The discrepancy is a **clock/filtration/state
orientation mismatch**, not pressure, not selector q.v., and not an intrinsic pair
producer.

**Classification: Exact one-mode Navier--Stokes/Kelvin calibration.**

The abstract conditional-variance bank remains exact on a single specified Markov
clock.  What is not proved is that the physical first-bad time `t` is that same
clock.  If the bank also carries a remaining/backward horizon `tau`, then for

\[
V(t)=a_t^TC(t,\tau(t))a_t
\]

the literal chain rule is

\[
\boxed{
\frac d{dt}V
=a_t^T(\partial_tC+\dot\tau\,\partial_\tau C)a_t
+2a_t^TC\dot a_t.
}
\]

Therefore the old one-clock formula cannot be promoted to a physical first-bad
telescope until the time/state lift is constructed.

**Classification: Exact two-clock chain rule; physical first-bad/Kelvin clock lift
open-literal.**

---

## 2. The covariance PDE is parabolic, not an ordinary exact one-form

For the canonical one-mode future covariance in remaining-horizon time,

\[
\boxed{
(\partial_\tau-\nu\partial_a^2)V=\gamma,
\qquad
\gamma=2\nu|\partial_a m|^2.
}
\]

Putting `s=Theta-tau` gives

\[
\boxed{
\partial_sV+\gamma=-\nu\partial_a^2V.
}
\]

The right-hand side is not identically zero.  At `a=0`, the exact calibration has
`gamma=0` but `nu partial_a^2 V>0`.  Hence

\[
d_{\rm pair}V-\gamma\,ds
\]

cannot be identified with the ordinary exterior derivative of `V` in spacetime.
A second-order generator is not an exterior derivation.

**Classification: Exact counterexample to the previous ordinary de Rham
packaging.**

The correct replacement is already present in the normalized ancestry algebra.  If

\[
q=f\phi,
\qquad
j=w-\nu K\nabla\log f,
\]

and the same Markov generator gives `D_sV=-gamma`, then

\[
\boxed{
\partial_s(qV)
+\nabla\cdot(qjV+\nu qK\nabla V)
=-q\gamma.
}
\]

Thus the physical spacetime object is the covariance current

\[
\boxed{
\mathbf J_V=(qV,\;qjV+\nu qK\nabla V),
\qquad
\operatorname{div}_{s,x}\mathbf J_V=-q\gamma.
}
\]

The divergence theorem/Dynkin--Itô duality, not ordinary de Rham exactness, is the
correct payment law.  The topological world-sheet statement `boundary^2=0` remains
valid independently.

**Classification: Exact divergence-form covariance balance under generator
compatibility.**

---

## 3. Moving quantile/shell cuts have a time face

Let `Q_s` be a time-dependent restriction.  Its fixed-time chain-boundary defect is

\[
C_Q=B_{\rm out}Q_1-Q_0B_{\rm in}.
\]

That is a spatial cut/interface face.  The transport defect is separately

\[
\boxed{
G_Q=\dot Q+T_{\rm out}Q-QT_{\rm in}.
}
\]

For the full pair lift,

\[
\boxed{
G_Q^{(2)}=G_Q\otimes Q+Q\otimes G_Q.
}
\]

So a moving cut has one time/boundary-speed face in each replica.

The literal one-dimensional Reynolds calibration makes the physical meaning
transparent.  If

\[
\partial_tq+\partial_x(qv)=0,
\qquad
D_t=(-\infty,a(t)),
\]

then

\[
\boxed{
\frac d{dt}\int_{D_t}q\,dx
=q(a,t)[\dot a(t)-v(a,t)]
=-qv+q\dot a.
}
\]

The `-qv` term is the static transport flux.  The `q dot a` term is the moving
boundary-speed face.  It cannot be obtained from the static spatial boundary
commutator alone.

At pair level the exact Reynolds rate has two faces,

\[
\boxed{
\dot M^{(2)}
=p_1(\dot a-v_1)+p_2(\dot a-v_2).
}
\]

**Classification: Exact generic Reynolds/operator identity and exact pair
factorization.**

The current repository does not yet define the actual first-bad quantile/shell
boundary-speed law line by line.  Static finite-cell cut tests therefore do not
certify a moving physical excursion by themselves.

**Classification: Programme-specific moving-cut realization open-literal.**

---

## 4. Mean-square and centered covariance must stay distinct

Draft PR #1 also objected to identifying centered future covariance with
deterministic vortex stretching.  That objection is correct, but the current main
branch has already repaired it.

With

\[
Q=C+mm^T,
\]

`mm^T` loses the Kelvin carré-du-champ while `C` gains it.  On the physical
backward-Kelvin state the resolved vorticity dyad and future covariance combine as

\[
\boxed{
T_{\rm tot}=\omega\omega^T+\Sigma_{\rm fut},
}
\]

and the Kelvin Gram tensor is an internal transfer.  The deterministic stretching
channel acts on the total tensor through the common two-sided strain operator.

**Classification: Finding correct; repaired by the exact mean/covariance/total
second-moment tensor split.**

---

## 5. Locality and determinant findings

The locality and general-Nanson determinant findings from Draft PR #1 were also
correct and are already repaired on main:

- `H->0` alone is not support locality;
- the invariant fixed-state topology is support-local plus
  `H^{-T} epsilon ->0` in conditional `L^2`;
- for a coherent microcell `L=sqrt(det H)H^{-T}` recovers primal line geometry;
- the general 3D Nanson rate is `D_t log det M_H=-4 div u`, while incompressible
  transport keeps `det M_H` constant.

**Classification: Audited and repaired.**

---

## 6. Frontier after incorporating Draft PR #1

Closed/audited:

- ordinary de Rham packaging is rejected;
- covariance spacetime transport is rewritten as Dynkin/Fokker--Planck divergence
  current;
- moving-cut `dot Q` / boundary-speed faces and their pair product rule are explicit;
- mean versus covariance and locality/determinant distinctions are repaired.

The subsequent reverse-age audit closes more of the first two items.  It proves
`L_K,rev=-K^-`, shows that a future-bank clock reversal uses `b_+` rather than the
same-clock `b_-`, and derives the exact fixed-mass level-set quantile speed from
probability current.

Still open:

1. programme-specific intertwining from the normalized ancestry state to the
   physical reverse-age Kelvin state;
2. the scalar germ observable/threshold geometry whose level sets define the
   first-bad quantile/shell chamber, plus its outer physical-time law;
3. ancestry state semantics/lift;
4. uniform singular-time support/shape/covariance collapse;
5. restart capacity and continuation.

See `docs/two_clock_kelvin_quantile_audit.md`.

`S^int` and any independently intended `Z_irr` remain open-literal.  No term above
is silently identified with them.

**Classification: Structural audit repair; no continuation/restart conclusion.**
