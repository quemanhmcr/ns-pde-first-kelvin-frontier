# Polar twin-Rayleigh / critical action master law

## Purpose

The preceding milestones reduced normalized three-dimensional incompressible
Navier--Stokes to the energy radius

\[
r=\|u\|_2,
\]

the unit state

\[
q=u/r,
\qquad
\|q\|_2=1,
\]

and the fixed self-adjoint curl operator

\[
C=\operatorname{curl}.
\]

The present note asks what remains if one takes the polar decomposition of that one
Hodge operator seriously rather than treating the signed and positive critical
pictures as separate frontiers.

Write

\[
\boxed{
C=J\Lambda,
\qquad
\Lambda=|C|=(C^2)^{1/2},
\qquad
J=\operatorname{sgn}C.
}
\]

On the mean-zero torus, `Lambda` is strictly positive and `J^2=I`.

There are two canonical Rayleigh functions on the energy sphere:

\[
\boxed{
\lambda(q):=\langle q,Cq\rangle=\frac HE,
\qquad
\kappa(q):=\langle q,\Lambda q\rangle=\frac{\mathcal K}{E}.
}
\]

The first is signed; the second is positive and critical.  They are not independent.
Because

\[
C^2=\Lambda^2,
\]

the universal Rayleigh-square identity gives the **twin eikonal law**

\[
\boxed{
\mu
:=\langle q,C^2q\rangle
=\lambda^2+\frac14\|\nabla_S\lambda\|_2^2
=\kappa^2+\frac14\|\nabla_S\kappa\|_2^2.
}
\]

Thus signed orientation and positive scale are two first-jet factorizations of one
and the same viscous Hodge square.

The full normalized PDE then admits a polar metriplectic form:

\[
\boxed{
\begin{aligned}
\dot r
&=-\nu r\mu,\\[1mm]
q_t
&=\frac r2\,\mathcal K_q\nabla_S\lambda
-\frac\nu2\,M_q\nabla_S\kappa,
\end{aligned}
}
\]

where

\[
\boxed{
\mathcal K_qv=P_\sigma(q\times v)
=-C^{-1}\operatorname{ad}_qv,
\qquad
\mathcal K_q^*=-\mathcal K_q,
}
\]

and

\[
\boxed{
M_q
:=P_q(\Lambda+\kappa)P_q,
\qquad
P_q=I-q\otimes q.
}
\]

The mobility `M_q` is positive on the tangent space.  Moreover

\[
\boxed{
\nabla_S\mu
=M_q\nabla_S\kappa.
}
\]

So viscosity is not merely descent of a different quantity `mu`: it is the
state-generated positive-mobility gradient descent of the positive critical
Rayleigh function `kappa` itself.

This yields a canonical critical action law.  If

\[
a_E:=(q_t)_E
=\frac r2\mathcal K_q\nabla_S\lambda,
\]

then

\[
\boxed{
\dot\kappa
=\langle\nabla_S\kappa,a_E\rangle
-\frac\nu2\langle\nabla_S\kappa,M_q\nabla_S\kappa\rangle.
}
\]

Completing the square in the exact positive mobility gives

\[
\boxed{
\begin{aligned}
\dot\kappa
&=-\frac\nu2
\left\|
M_q^{1/2}\nabla_S\kappa
-\frac1\nu M_q^{-1/2}a_E
\right\|_2^2\\
&\quad+
\frac1{2\nu}\langle a_E,M_q^{-1}a_E\rangle.
\end{aligned}
}
\]

The final quadratic is not an externally chosen score.  It is the quotient action
forced by the positive mobility which viscosity itself supplies.  It is also the
minimum inverse-Sylvester action among all skew operator representatives of the same
Euler ray velocity.

The cumulative consequence is sharp enough to type the remaining Zeno scenario.
If the positive critical Hodge size diverges at a finite endpoint, then the Euler ray
has finite weak `H^{-1/2}` path length by the preceding theorem but infinite
quadratic critical action.  In particular the remaining escape must be a
finite-length / infinite-action concentration of the **same actual ray path**.

No no-escape, continuation, restart, blow-up exclusion or global-regularity theorem
is claimed.

---

## 1. Two Rayleigh landscapes share one exact eikonal envelope

Let

\[
\lambda=\langle q,Cq\rangle,
\qquad
\kappa=\langle q,\Lambda q\rangle,
\qquad
\mu=\langle q,C^2q\rangle.
\]

For any self-adjoint operator `F`, the sphere gradient of its Rayleigh function is

\[
\nabla_SR_F
=2(F-R_F)q.
\]

Hence

\[
\boxed{
\nabla_S\lambda
=2(C-\lambda)q,
\qquad
\nabla_S\kappa
=2(\Lambda-\kappa)q.
}
\]

The universal square law

\[
R_{F^2}
=R_F^2+\frac14\|\nabla_SR_F\|_2^2
\]

may be applied both to `F=C` and to `F=Lambda`.  Since their squares coincide,

\[
C^2=\Lambda^2,
\]

one obtains

\[
\boxed{
\mu
=\lambda^2+\frac14\|\nabla_S\lambda\|_2^2
=\kappa^2+\frac14\|\nabla_S\kappa\|_2^2.
}
\]

Subtracting the two factorizations gives

\[
\boxed{
\kappa^2-\lambda^2
=\frac14
\left(
\|\nabla_S\lambda\|_2^2
-\|\nabla_S\kappa\|_2^2
\right)
\ge0.
}
\]

The nonnegative gap is exactly the heterochiral contraction defect derived in the
preceding projective-Hodge theorem.

Thus the same `mu` simultaneously measures

- signed center plus signed slope;
- positive critical center plus positive-scale spread.

No third scalar Hodge mechanism is present at this level.

**Classification: Exact twin Rayleigh/eikonal identities.**

---

## 2. The viscous sphere gradient has two exact factorizations

The sphere gradient of `mu` is

\[
\boxed{
\nabla_S\mu
=2(C^2-\mu)q.
}
\]

The signed Rayleigh block formula gives

\[
\nabla_S\mu
=P_q(C+\lambda)P_q\,\nabla_S\lambda.
\]

This factor is self-adjoint but need not be positive because `C` is signed.

The positive factorization is stronger for dissipation.  Define

\[
\boxed{
M_q
:=P_q(\Lambda+\kappa)P_q
}
\]

on the tangent space `T_q S`.  Then

\[
\boxed{
\nabla_S\mu
=M_q\nabla_S\kappa.
}
\]

Indeed, if

\[
b:=(\Lambda-\kappa)q
=\frac12\nabla_S\kappa,
\]

then

\[
(\Lambda^2-\mu)q
=(\Lambda+\kappa)b+(\kappa^2-\mu)q,
\]

and the last radial term is exactly removed by tangent projection.

Because the mean-zero torus has a positive `Lambda` spectral gap and `kappa>0`,

\[
\boxed{
\langle v,M_qv\rangle
=\langle v,(\Lambda+\kappa)v\rangle
>0
}
\]

for every nonzero tangent `v` in the form domain.

Thus `M_q` is the canonical positive factor of the same Hodge square whose signed
factor is `P_q(C+lambda)P_q`.

**Classification: Exact polar factorization / positivity.**

---

## 3. Normalized Navier--Stokes is a skew--positive polar flow

The energy-sphere theorem gave

\[
(q_t)_E
=\frac r2\mathcal K_q\nabla_S\lambda,
\]

with

\[
\mathcal K_q^*=-\mathcal K_q.
\]

Viscosity gave

\[
(q_t)_\nu
=-\frac\nu2\nabla_S\mu.
\]

Section 2 now turns the latter into

\[
\boxed{
(q_t)_\nu
=-\frac\nu2M_q\nabla_S\kappa.
}
\]

Therefore the literal normalized PDE is

\[
\boxed{
q_t
=\frac r2\mathcal K_q\nabla_S\lambda
-\frac\nu2M_q\nabla_S\kappa.
}
\]

Together with

\[
\boxed{
\dot r
=-\nu r
\left(
\lambda^2+\frac14\|\nabla_S\lambda\|^2
\right)
=-\nu r
\left(
\kappa^2+\frac14\|\nabla_S\kappa\|^2
\right),
}
\]

this is a closed radius/sphere rewrite of smooth nonzero Navier--Stokes.

The division of labor is intrinsic:

\[
\boxed{
\begin{array}{ccl}
\text{signed curl }C
&\longrightarrow&
\text{skew orientation mobility }\mathcal K_q
\text{ acting on }\lambda,\\[1mm]
\text{positive curl }\Lambda=|C|
&\longrightarrow&
\text{positive mobility }M_q
\text{ acting on }\kappa.
\end{array}
}
\]

The two flows are tied by the same square `C^2=Lambda^2` and the same envelope
`mu`; they are not independently selected Hamiltonian and dissipative models.

**Classification: Exact whole-PDE polar Rayleigh law.**

---

## 4. The positive critical center has an exact forced-gradient law

Define

\[
\boxed{
a_E:=(q_t)_E.}
\]

Since

\[
\nabla_S\kappa=2b,
\qquad
b=(\Lambda-\kappa)q,
\]

and

\[
(q_t)_\nu=-\nu M_qb,
\]

the critical-center derivative is

\[
\boxed{
\dot\kappa
=2\langle b,a_E\rangle
-2\nu\langle b,M_qb\rangle.
}
\]

Equivalently,

\[
\boxed{
\dot\kappa
=\langle\nabla_S\kappa,a_E\rangle
-\frac\nu2
\langle\nabla_S\kappa,M_q\nabla_S\kappa\rangle.
}
\]

This is not a generic gradient estimate.  It is the literal positive critical
Rayleigh derivative of Navier--Stokes after the polar factorization of `C^2`.

The shell-null theorem from the preceding milestone is immediate: if

\[
\nabla_S\kappa=0,
\]

then both terms vanish instantaneously even when `a_E` itself is nonzero.

**Classification: Exact forced positive-gradient identity.**

---

## 5. Exact critical action square and impedance matching

Because `M_q` is positive on the tangent space, Section 4 may be completed in its
own metric:

\[
\boxed{
\begin{aligned}
\dot\kappa
&=-\frac\nu2
\left\|
M_q^{1/2}\nabla_S\kappa
-\frac1\nu M_q^{-1/2}a_E
\right\|_2^2\\
&\quad+
\frac1{2\nu}
\underbrace{\langle a_E,M_q^{-1}a_E\rangle}_{\mathscr A_{crit}}.
\end{aligned}
}
\]

The shorthand

\[
\boxed{
\mathscr A_{crit}(q,a_E)
:=\langle a_E,M_q^{-1}a_E\rangle
}
\]

is used only for the action forced by this identity.  It is not a new state or
badness score.

For fixed Euler ray velocity, the maximal possible instantaneous increase permitted
by the positive mobility is therefore

\[
\boxed{
\dot\kappa
\le\frac1{2\nu}\mathscr A_{crit}.
}
\]

Equality would require the exact matching condition

\[
\boxed{
M_q\nabla_S\kappa
=\frac1\nu a_E.
}
\]

Since

\[
(q_t)_\nu
=-\frac\nu2M_q\nabla_S\kappa,
\]

the matching condition is equivalently

\[
\boxed{
(q_t)_\nu=-\frac12(q_t)_E.
}
\]

Thus maximum critical feeding occurs only when the viscous ray rotation cancels
exactly one half of the Euler ray velocity.  The critical square is therefore a
self-generated **impedance matching law**, not a free transfer-versus-dissipation
inequality.

At a one-Laplacian-shell state the viscous ray velocity is zero, so the matching is
not satisfied unless the Euler ray is also zero; nevertheless the two faces of the
square cancel exactly to give `kappadot=0`.

**Classification: Exact positive-mobility square completion.**

---

## 6. Reflection law: the spread variable disappears entirely

Let

\[
a_\nu:=(q_t)_\nu.
\]

From Section 3,

\[
a_\nu
=-\frac\nu2M_q\nabla_S\kappa,
\]

so

\[
\nabla_S\kappa
=-\frac2\nu M_q^{-1}a_\nu.
\]

Substituting into

\[
\dot\kappa
=\langle\nabla_S\kappa,a_E+a_\nu\rangle
\]

gives

\[
\dot\kappa
=-\frac2\nu
\langle a_\nu,M_q^{-1}(a_E+a_\nu)\rangle.
\]

Consequently

\[
\boxed{
\dot\kappa
=\frac1{2\nu}
\left(
\|a_E\|_{M_q^{-1}}^2
-\|a_E+2a_\nu\|_{M_q^{-1}}^2
\right),
}
\]

where

\[
\|v\|_{M_q^{-1}}^2
:=\langle v,M_q^{-1}v\rangle.
\]

The critical center increases exactly when the viscous ray displacement makes the
reflected velocity

\[
a_E+2a_\nu
\]

smaller than the pure Euler velocity in the canonical inverse-mobility metric.

This formula contains no separately declared spread or transfer variable.  It uses
only the two actual ray velocities and the positive mobility forced by `|C|`.

**Classification: Exact critical reflection identity.**

---

## 7. The critical action is the quotient-minimum of the Sylvester operator action

The preceding energy-ray theorem used the positive Sylvester superoperator

\[
\mathcal S_\Lambda X
:=\Lambda X+X\Lambda
\]

on skew Hilbert--Schmidt operators.  Since `Lambda` has a positive spectral gap,
`S_Lambda` has a bounded positive inverse on that space.

Fix a tangent ray velocity

\[
a\perp q.
\]

Consider all skew operator representatives of that same velocity:

\[
\mathfrak G(a)
:=\{A:A^*=-A,\ Aq=a\}.
\]

Define their inverse-Sylvester action

\[
\mathscr J(A)
:=\langle A,\mathcal S_\Lambda^{-1}A\rangle_{HS}.
\]

Let

\[
p:=M_q^{-1}a.
\]

Then `p` is tangent and

\[
A_*
:=\mathcal S_\Lambda(p\otimes q-q\otimes p)
\]

satisfies

\[
A_*q=a.
\]

For any other `A in G(a)`, write

\[
A=A_*+H,
\qquad
Hq=0.
\]

The cross term vanishes:

\[
\begin{aligned}
\langle A_*,\mathcal S_\Lambda^{-1}H\rangle_{HS}
&=\langle p\otimes q-q\otimes p,H\rangle_{HS}\\
&=2\langle p,Hq\rangle=0.
\end{aligned}
\]

Therefore

\[
\boxed{
\inf_{A\in\mathfrak G(a)}
\langle A,\mathcal S_\Lambda^{-1}A\rangle_{HS}
=2\langle a,M_q^{-1}a\rangle.
}
\]

Thus `2 A_crit` is exactly the quotient action obtained after removing every skew
tangent gauge that does not move the energy ray.

The tangent square of Section 5 is consequently the gauge-minimal version of the
Sylvester square suggested by the previous operator theorem.

**Classification: Exact quotient/minimum theorem on the stated smooth finite-rank class.**

---

## 8. The quotient action is weaker than the canonical `H^{-1/2}` ray action

For tangent `a`, the inverse mobility has the elementary variational formula

\[
\langle a,M_q^{-1}a\rangle
=
\sup_{v\perp q}
\left[
2\langle a,v\rangle
-\langle v,(\Lambda+\kappa)v\rangle
\right].
\]

Dropping the constraint `v perp q` can only increase the supremum.  Hence

\[
\boxed{
\langle a,M_q^{-1}a\rangle
\le
\langle a,(\Lambda+\kappa)^{-1}a\rangle
\le
\langle a,\Lambda^{-1}a\rangle.
}
\]

On the mean-zero torus the last quantity is the homogeneous Hodge
`H^{-1/2}` norm squared:

\[
\boxed{
\mathscr A_{crit}(q,a)
\le
\|\Lambda^{-1/2}a\|_2^2.
}
\]

Thus the critical action does not introduce a stronger topology than the weak ray
space already singled out by the earlier cumulative path theorem.  It changes the
time integrability requirement from length to quadratic action.

**Classification: Rigorous variational consequence.**

---

## 9. Exact cumulative action budget

Integrate the square identity of Section 5 over a smooth interval `[a,t]`.  One gets

\[
\boxed{
\begin{aligned}
\kappa(t)
&+\frac\nu2\int_a^t
\left\|
M_q^{1/2}\nabla_S\kappa
-\frac1\nu M_q^{-1/2}a_E
\right\|_2^2ds\\
&=\kappa(a)
+\frac1{2\nu}\int_a^t
\mathscr A_{crit}(q(s),a_E(s))\,ds.
\end{aligned}
}
\]

Therefore

\[
\boxed{
\sup_{a\le s<t}\kappa(s)<\infty
}
\]

whenever

\[
\boxed{
\int_a^t\mathscr A_{crit}\,ds<\infty.
}
\]

Since

\[
\mathcal K=E\kappa
\le E(a)\kappa,
\]

divergence of the physical positive critical quadratic implies divergence of
`kappa`.  Hence any critical escape necessarily satisfies

\[
\boxed{
\int_a^T\mathscr A_{crit}(s)\,ds=\infty.
}
\]

This is a conditional no-escape theorem for the exact critical quotient action, not
a proof that the action is finite.

**Classification: Rigorous cumulative consequence of the exact square.**

---

## 10. Critical escape must have finite weak length but infinite weak action

The energy-ray theorem already proved

\[
\int_a^T
\|a_E(t)\|_{H^{-1/2}}\,dt
<\infty
\]

on every finite smooth interval, with total length paid by the viscous radius loss.

Section 8 gives

\[
\mathscr A_{crit}
\le
\|a_E\|_{\dot H^{-1/2}}^2.
\]

Consequently, if the critical Hodge size diverges at a finite endpoint, Section 9
forces

\[
\boxed{
\int_a^T
\|a_E(t)\|_{\dot H^{-1/2}}^2\,dt
=\infty.
}
\]

Together with the previous length theorem, the necessary Zeno signature is

\[
\boxed{
\begin{gathered}
a_E\in L^1_tH^{-1/2},\\
a_E\notin L^2_t\dot H^{-1/2}.
\end{gathered}
}
\]

The inhomogeneous/homogeneous distinction is immaterial up to fixed torus constants
on the mean-zero sector.

Thus the surviving critical escape is no longer merely "high frequency in finite
time."  It must be a finite-length but infinite-action path in the exact weak Hodge
geometry selected by the PDE.

**Classification: Rigorous necessary condition for critical escape.**

---

## 11. The same Zeno requires an `L^1` but non-`L^2` active radial-loss density

The earlier weak path theorem gave the pointwise bound

\[
\boxed{
\|a_E\|_{H^{-1/2}}
\le
\frac{C_{\mathbb T}}\nu
\vartheta(t)(-\dot r(t)),
}
\]

where

\[
\vartheta
=\sqrt{1-\frac{\lambda^2}{\mu}}
\in[0,1].
\]

Define only the literal density

\[
\boxed{
g_{act}(t):=\vartheta(t)(-\dot r(t))\ge0.
}
\]

Its total mass is finite:

\[
\boxed{
\int_a^Tg_{act}(t)\,dt
\le r(a)-r(T^-)
\le r(a).
}
\]

If critical escape occurs, Section 10 says the weak ray speed is not square
integrable.  Since

\[
\|a_E\|_{H^{-1/2}}^2
\le
\frac{C_{\mathbb T}^2}{\nu^2}g_{act}^2,
\]

one necessarily has

\[
\boxed{
\int_a^Tg_{act}(t)^2\,dt=\infty.
}
\]

Hence the same actual defect-weighted radial loss must obey

\[
\boxed{
g_{act}\in L^1(a,T)\setminus L^2(a,T).}
\]

This is a literal spike requirement on the existing radius-loss density, not a new
badness observable.

It is fully consistent with the causal heat-age theorem: finite mass can still
concentrate in arbitrarily narrow terminal windows.  The missing no-escape theorem
must forbid precisely this self-generated concentration.

**Classification: Rigorous consequence of the preceding exact/weak-path laws.**

---

## 12. Poisson-semigroup representation of the inverse-Sylvester action

Although the tangent quotient action is the sharp projective quantity, the parent
Sylvester action has a useful exact representation.

For any skew Hilbert--Schmidt operator `G`,

\[
\boxed{
\mathcal S_\Lambda^{-1}G
=\int_0^\infty
 e^{-s\Lambda}G e^{-s\Lambda}\,ds.
}
\]

Indeed differentiation of

\[
e^{-s\Lambda}Ge^{-s\Lambda}
\]

gives minus its Sylvester image, and the positive spectral gap kills the
infinite-`s` boundary.

Therefore

\[
\boxed{
\langle G,\mathcal S_\Lambda^{-1}G\rangle_{HS}
=\int_0^\infty
\left\|
 e^{-s\Lambda/2}G e^{-s\Lambda/2}
\right\|_{HS}^2ds.
}
\]

For the canonical rank-two representative

\[
G=a\otimes q-q\otimes a,
\]

set

\[
a_s=e^{-s\Lambda/2}a,
\qquad
q_s=e^{-s\Lambda/2}q.
\]

Then

\[
\left\|a_s\otimes q_s-q_s\otimes a_s\right\|_{HS}^2
=2\left(
\|a_s\|^2\|q_s\|^2
-|\langle a_s,q_s\rangle|^2
\right).
\]

Since the Poisson semigroup is contractive,

\[
\boxed{
\langle G,\mathcal S_\Lambda^{-1}G\rangle_{HS}
\le2\langle a,\Lambda^{-1}a\rangle.
}
\]

The quotient theorem of Section 7 sharpens this by minimizing away the tangent gauge
and replacing the right-hand side with exactly

\[
2\langle a,M_q^{-1}a\rangle.
\]

Thus the critical action is itself a Poisson/Hodge functional-calculus quantity, not
an extra mechanism outside the heat/Hodge grammar.

**Classification: Exact Poisson-semigroup identity and rigorous contraction.**

---

## 13. The older pair-kernel square has an exact Riesz projection descent

The de Rham critical-current theorem used the pair Hilbert space with inner product

\[
\boxed{
\langle F,G\rangle_{\mathscr P}
:=\frac12\iint
K_\Lambda(x,y)F(x,y)\cdot G(x,y)\,dx\,dy.
}
\]

Let the increment operator on the mean-zero divergence-free Hodge sector be

\[
\delta f(x,y):=f(x)-f(y).
\]

Then

\[
\boxed{
\|\delta f\|_{\mathscr P}^2
=\langle f,\Lambda f\rangle,
\qquad
\delta^*\delta=\Lambda.
}
\]

For the actual antisymmetric velocity-pair field

\[
b_u(x,y):=u(x)\times u(y),
\]

direct symmetrization gives

\[
\delta^*b_u
=P_{\mathcal H}\!\left[-u\times\Lambda u\right]
=:Y,
\]

where `P_H` denotes the mean-zero divergence-free Hodge projection; it may be omitted
inside pairings with divergence-free test fields.

The critical nonlinear term is exactly

\[
\boxed{
(\dot{\mathcal K})_{nl}
=\langle\delta\omega,b_u\rangle_{\mathscr P}
=\langle\omega,Y\rangle.
}
\]

Let

\[
\mathscr R:=\overline{\operatorname{Ran}\delta}
\]

and let `P_R` be orthogonal projection in the pair Hilbert space.  Since
`delta omega` lies in `R`, only

\[
P_\mathscr R b_u
\]

can participate in critical transfer.

Using `delta^*delta=Lambda`,

\[
\boxed{
P_\mathscr Rb_u
=\delta\Lambda^{-1}Y,
}
\]

and

\[
\boxed{
\|P_\mathscr Rb_u\|_{\mathscr P}^2
=\langle Y,\Lambda^{-1}Y\rangle
\le\|b_u\|_{\mathscr P}^2.
}
\]

Consequently the old pair square admits the sharper exact projection form

\[
\boxed{
\dot{\mathcal K}
=-\nu
\left\|
\delta\omega-\frac1{2\nu}P_\mathscr Rb_u
\right\|_{\mathscr P}^2
+\frac1{4\nu}
\|P_\mathscr Rb_u\|_{\mathscr P}^2.
}
\]

The previously displayed positive remainder using the full `b_u` is still exactly
correct, but it contains an orthogonal pair component that no one-field vorticity
increment can see.  The Riesz projection removes that dynamically invisible
pair-gauge direction.

Thus even the old common-kernel square compresses once more: the physically active
positive remainder is the inverse-Hodge action of the projected local field

\[
Y=-P_{\mathcal H}(u\times\Lambda u).
\]

This does not by itself bound that action.

**Classification: Exact pair-Hilbert/Riesz projection identity; architecture sharpening.**

---

## 14. What the polar/action law removes from the primitive list

Below this theorem the following should no longer be treated as independent
mechanisms:

- signed Rayleigh slope and positive critical slope: they are twin first-jet
  factorizations of the same `mu`;
- viscous descent of `mu`: it is positive-mobility descent of `kappa`;
- critical transfer versus critical viscosity: they are forcing and metric-gradient
  faces of one exact `M_q` action law;
- the Sylvester positive remainder: after the ray quotient its minimum is exactly
  `2<a_E,M_q^-1 a_E>`;
- one-shell critical nullity: it is the zero-gradient point of `kappa` in the same
  positive mobility;
- weak physical-time Zeno and critical action Zeno: an escape must have finite path
  length but infinite quadratic action on the same Euler ray;
- the full pair-kernel positive remainder: only its exact-increment Riesz projection
  is dynamically active.

The present whole-PDE grammar is

\[
\boxed{
\begin{gathered}
C=J\Lambda,\\
\mu=\lambda^2+\frac14\|\nabla\lambda\|^2
=\kappa^2+\frac14\|\nabla\kappa\|^2,\\
q_t=\frac r2\mathcal K_q\nabla\lambda
-\frac\nu2M_q\nabla\kappa,\\
\dot r=-\nu r\mu.
\end{gathered}
}
\]

Everything displayed is generated by the actual energy ray and the polar factors of
one fixed Hodge operator.

**Classification: Rigorous synthesis of exact identities.**

---

## 15. No-escape frontier after the polar action compression

A hypothetical critical escape can no longer be described merely as

\[
\text{nonlinearity beats viscosity}.
\]

It must realize all of the following simultaneously:

\[
\boxed{
\begin{gathered}
\text{the signed Rayleigh flow generates an Euler ray of finite }H^{-1/2}
\text{ length},\\
\text{that same ray has infinite quadratic critical quotient action},\\
\text{the positive mobility repeatedly impedance-matches that Euler forcing closely}
\text{ enough to raise }\kappa,\\
\text{the active radial-loss density remains finite in }L^1\text{ but develops}\
L^2\text{-divergent spikes},\\
\text{and the causal heat-age image of the same loss still develops the negative-half}
\text{ moment concentration identified previously.}
\end{gathered}
}
\]

The exact remaining question is therefore

\[
\boxed{
\begin{gathered}
\text{Can the self-Lie skew mobility }\mathcal K_q\nabla\lambda
\text{ generate infinite }M_q^{-1}\text{-action in finite time}\\
\text{while its total weak path length is finite and while the same polar Hodge square}
\text{ drives }M_q\text{-gradient descent and radial loss?}
\end{gathered}
}
\]

No theorem here proves that it cannot.

A true no-escape theorem at this stage would be an **action nonconcentration theorem**
for this one self-generated polar ray flow.  Proving another hierarchy of snapshot
norm estimates would sit above the compression already obtained here.

**Classification: Open.**

---

## 16. Classification summary

### Exact

- polar curl `C=J Lambda`;
- twin eikonal law
  `mu=lambda^2+||grad lambda||^2/4=kappa^2+||grad kappa||^2/4`;
- positive mobility factorization
  `grad mu=M_q grad kappa`, `M_q=P_q(Lambda+kappa)P_q>0`;
- whole normalized polar law
  `qdot=(r/2)K_q grad lambda-(nu/2)M_q grad kappa`;
- radius law `rdot=-nu r mu` in either twin-eikonal factorization;
- forced critical-gradient law and exact `M_q` square completion;
- reflected-velocity identity for `kappadot`;
- quotient-minimum identity
  `inf_(Aq=a)<A,S_Lambda^-1 A>_HS=2<a,M_q^-1 a>`;
- Poisson-semigroup representation of `S_Lambda^-1`;
- pair-increment adjoint and exact Riesz-projected pair square.

### Rigorous consequences

- `A_crit=<a_E,M_q^-1a_E>` is bounded by the homogeneous `H^-1/2` Euler-ray speed
  squared;
- finite time-integrated critical action bounds `kappa` and hence the physical
  positive critical quadratic;
- any critical escape requires finite weak path length but infinite weak quadratic
  action;
- the literal active radial-loss density must be `L^1` but not `L^2`;
- the full pair-square positive remainder is an upper envelope of the dynamically
  realizable exact-increment action.

### Open

- finiteness of the critical quotient action from the remaining NS compatibilities;
- exclusion of `L^1`/non-`L^2` active-loss spiking;
- exclusion of the equivalent causal zero-heat-age concentration;
- continuation, restart, blow-up exclusion and global regularity.

---

## Follow-through: quotient the critical action to the single scalar direction actually seen by `kappa`

The full quotient action

\[
\mathscr A_{crit}
=\langle a_E,M_q^{-1}a_E\rangle
\]

still counts Euler ray motion orthogonal to the positive critical gradient.  A later
heat--time audit removes that invisible motion as well.

Set

\[
T_\kappa
:=\langle\nabla_S\kappa,a_E\rangle,
\qquad
V_\kappa
:=\langle\nabla_S\kappa,M_q\nabla_S\kappa\rangle.
\]

If `V_kappa>0`, define only the derived scalar quotient

\[
\boxed{
\mathscr A_{rel}
:=\frac{T_\kappa^2}{V_\kappa};
}
\]

on the one-shell null set `V_kappa=0`, both `grad kappa` and `T_kappa` vanish and set
`A_rel=0` by continuity of the structural definition.

The exact critical law

\[
\dot\kappa
=T_\kappa-\frac\nu2V_\kappa
\]

becomes

\[
\boxed{
\dot\kappa
=-\frac\nu2
\left(
\sqrt{V_\kappa}
-\frac{T_\kappa}{\nu\sqrt{V_\kappa}}
\right)^2
+\frac1{2\nu}\mathscr A_{rel}.
}
\]

Positive-mobility Cauchy--Schwarz gives

\[
\boxed{
\mathscr A_{rel}
\le\mathscr A_{crit}.
}
\]

Hence a divergent critical center forces the still smaller necessary condition

\[
\boxed{
\int\mathscr A_{rel}\,dt=+\infty.
}
\]

A localized mixed-helical wavepacket audit in the later heat--time theorem shows why
one cannot close this by a scale-independent instantaneous estimate
`A_rel <= C r^2 mu`: the ratio `A_rel/(r^2 mu)` has the predicted intermittent
`~N^2` onset.  Thus the scalar quotient sharpens the action frontier but also makes
clear that the missing control must be dynamic/parabolic rather than a snapshot
energy inequality.

See `docs/causal_heat_ray_projective_zero_curvature_master_law.md`.

**Classification: Exact scalar action quotient; audited intermittent scaling no-go against scale-independent snapshot domination.**
