# Canonical energy-ray connection and eikonal Hodge hierarchy

## Purpose

The preceding projective-Hodge milestone introduced the operator curvature

\[
K=[\mathcal A_{NS},C]
\]

for the skew ray generator

\[
\mathcal A_{NS}
=\mathbb J(u)+\nu[\Pi,C^2].
\]

That formula is exact, but the interpretation of `K` as a canonical primitive can be
sharpened.

The reason is structural: a rank-one ray does not see the entire skew operator that
moves it.  Any skew tangent--tangent block commuting with `Pi` changes
`A_NS` without changing

\[
q_t,
\qquad
\Pi_t,
\qquad
m_F=\operatorname{tr}(\Pi F(C)).
\]

Therefore the full commutator `[A_NS,C]` contains ray-frame gauge that should not be
promoted to a physical source below the projective level.

There is a unique off-diagonal rank-two skew connection carried by the actual oriented energy ray:

\[
\boxed{
\Gamma
:=q_t\otimes q-q\otimes q_t.
}
\]

It has rank at most two,

\[
\Gamma q=q_t,
\qquad
\Pi_t=[\Gamma,\Pi],
\]

and every other skew generator of the same ray differs from `Gamma` by an operator
commuting with `Pi`.

With this canonical connection, the apparent curvature source collapses completely.
For the curl Rayleigh function

\[
\lambda(q)=\langle q,Cq\rangle,
\]

and its mismatch

\[
D=[\Pi,C],
\]

one has

\[
\boxed{
\nabla_t^\Gamma D
=
\frac12\,q\wedge
\big(\operatorname{Hess}_S\lambda\big)q_t,
}
\]

where

\[
q\wedge v:=q\otimes v-v\otimes q.
\]

More generally, for every quadratic Hodge Rayleigh readout

\[
m_F(q)=\langle q,F(C)q\rangle,
\qquad
D_F=[\Pi,F(C)],
\]

one has the universal canonical law

\[
\boxed{
\nabla_t^\Gamma D_F
=
\frac12\,q\wedge
\big(\operatorname{Hess}_S m_F\big)q_t.
}
\]

Thus the earlier operator curvature is not a new mechanism.  The projectively active
source is exactly the Hessian of the same quadratic Rayleigh landscape evaluated on
the actual ray velocity.

The second result is an infinite compression.  With

\[
\Lambda=|C|,
\]

define the positive dyadic Hodge Rayleigh hierarchy

\[
R_n(q):=\langle q,\Lambda^{2^n}q\rangle,
\qquad n\ge0.
\]

Then one universal eikonal-square rule generates the whole hierarchy:

\[
\boxed{
R_{n+1}
=R_n^2
+\frac14\|\nabla_SR_n\|_2^2
=R_n^2+\frac12\|[\Pi,\Lambda^{2^n}]\|_{HS}^2.
}
\]

In particular, with

\[
\kappa=R_0=\frac{\mathcal K}{E},
\qquad
\mu=R_1=\frac ZE,
\]

one gets the exact positive critical decomposition

\[
\boxed{
\mu
=\kappa^2
+\frac12\|[\Pi,\Lambda]\|_{HS}^2.
}
\]

The kinetic radius therefore obeys

\[
\boxed{
-\frac{\dot r}{\nu r}
=\kappa^2
+\frac12\|[\Pi,\Lambda]\|_{HS}^2.
}
\]

A state concentrated on one Laplacian shell has `[Pi,Lambda]=0`.  At such an instant
both Euler and viscosity have zero first derivative of the positive critical center
`kappa`, while viscosity still drains the physical radius at rate `nu kappa^2`.
Critical cascade cannot increase the positive center without first creating
positive-scale spread away from that shell.

No no-escape theorem is claimed.  The remaining question is whether the self-Lie
Euler ray can repeatedly create this spread quickly enough to sustain a parabolic
Zeno cascade while the same positive Hodge hierarchy is simultaneously sorted by
viscosity and taxed through the radius.

---

## 1. Skew generators of a rank-one ray have an exact gauge decomposition

Let

\[
\Pi=q\otimes q,
\qquad
\|q\|_2=1,
\]

and suppose a skew-adjoint operator `A` generates the oriented ray velocity

\[
q_t=Aq.
\]

Write

\[
a:=q_t.
\]

Because `A` is skew,

\[
\langle q,a\rangle=0.
\]

Define

\[
\boxed{
\Gamma_a
:=a\otimes q-q\otimes a.
}
\]

Then

\[
\Gamma_a^*=-\Gamma_a,
\qquad
\Gamma_aq=a.
\]

Moreover

\[
\boxed{
[\Gamma_a,\Pi]
=a\otimes q+q\otimes a
=\Pi_t.
}
\]

Now define

\[
A_\parallel:=A-\Gamma_a.
\]

Then

\[
A_\parallel q=0.
\]

For a real rank-one projector this is equivalent to

\[
\boxed{
[A_\parallel,\Pi]=0.
}
\]

Therefore

\[
\boxed{
A=\Gamma_a+A_\parallel,
\qquad
[A_\parallel,\Pi]=0.
}
\]

is the exact ray-gauge decomposition.

The canonical connection is the off-diagonal part

\[
\boxed{
\Gamma_a
=[\Pi,[\Pi,A]].
}
\]

The block `A_parallel` can rotate the orthogonal tangent space, but it cannot move the
energy ray and cannot change any scalar observable depending only on `Pi`.

This is why the full `A_NS` curvature should not be treated as a primitive below the
projective level.

**Classification: Exact rank-one skew-gauge identity.**

---

## 2. The canonical Navier--Stokes ray connection is rank two

For normalized Navier--Stokes,

\[
q_t
=(q_t)_E+(q_t)_\nu.
\]

The Euler face is

\[
\boxed{
(q_t)_E
=\mathbb J(u)q
=rC^{-1}[q,Dq]_{\rm Lie},
}
\]

while viscosity is

\[
\boxed{
(q_t)_\nu
=-\nu(C^2-\mu)q,
\qquad
\mu=\langle q,C^2q\rangle.
}
\]

Hence the canonical NS ray connection is

\[
\boxed{
\Gamma_{NS}
=q_t\otimes q-q\otimes q_t.
}
\]

It is rank at most two at every smooth nonzero state.

The viscous generator in the previous theorem is already canonical.  Indeed, with

\[
w:=(C^2-\mu)q,
\]

one has

\[
[\Pi,C^2]
=q\otimes w-w\otimes q,
\]

and therefore

\[
\boxed{
\Gamma_\nu
=(q_t)_\nu\otimes q-q\otimes(q_t)_\nu
=\nu[\Pi,C^2].
}
\]

The Euler Poisson operator contains an additional tangent gauge.  Its canonical ray
part is

\[
\boxed{
\Gamma_E
=[\Pi,[\Pi,\mathbb J(u)]]
=(q_t)_E\otimes q-q\otimes(q_t)_E.
}
\]

Thus

\[
\boxed{
\Gamma_{NS}
=\Gamma_E+\nu[\Pi,C^2].
}
\]

Every normalized Hodge moment can therefore be evolved using this one rank-two
connection instead of the full Poisson operator:

\[
\boxed{
\dot m_F
=-\langle\Gamma_{NS},[\Pi,F(C)]\rangle_{HS}.
}
\]

**Classification: Exact canonical-ray reduction of the normalized NS generator.**

---

## 3. Canonical curvature is a Rayleigh Hessian, not a new operator mechanism

Fix a self-adjoint Hodge multiplier

\[
F:=F(C)
\]

and define its quadratic Rayleigh function

\[
R_F(q):=\langle q,Fq\rangle.
\]

Set

\[
m_F:=R_F(q),
\qquad
P_q:=I-\Pi.
\]

The sphere gradient is

\[
\boxed{
\nabla_SR_F
=2(F-m_F)q.
}
\]

For tangent `v`, the sphere Hessian is

\[
\boxed{
\operatorname{Hess}_SR_F(v)
=2P_q(F-m_F)v.
}
\]

The ray commutator is

\[
D_F=[\Pi,F]
=q\wedge b_F,
\qquad
b_F:=(F-m_F)q.
\]

Let the canonical ray velocity be

\[
a=q_t
\]

and the canonical connection be

\[
\Gamma=a\otimes q-q\otimes a.
\]

Define

\[
\nabla_t^\Gamma X
:=X_t-[\Gamma,X].
\]

Direct differentiation of `D_F=[Pi,F]`, or equivalently Jacobi with
`Pi_t=[Gamma,Pi]`, gives

\[
\nabla_t^\Gamma D_F
=-[\Pi,[\Gamma,F]].
\]

The projectively active vector in the last commutator is

\[
\chi_F
:=P_q(F-m_F)a.
\]

Therefore

\[
\boxed{
\nabla_t^\Gamma D_F
=q\wedge\chi_F.
}
\]

Using the Hessian formula,

\[
\boxed{
\nabla_t^\Gamma D_F
=\frac12\,q\wedge
\big(\operatorname{Hess}_SR_F\big)q_t.
}
\]

This identity is universal for every quadratic Rayleigh readout.

For `F=C`,

\[
\boxed{
\nabla_t^\Gamma D
=\frac12\,q\wedge
\big(\operatorname{Hess}_S\lambda\big)q_t.
}
\]

Thus the projective curvature source is not an independent operator `K`.  It is the
second derivative of the one Rayleigh landscape already present in the preceding
energy-sphere theorem, applied to the actual ray velocity.

**Classification: Exact canonical curvature/Hessian identity.**

---

## 4. Relation to the previous `K=[A_NS,C]` law: a gauge correction

The preceding milestone used

\[
K=[\mathcal A_{NS},C]
\]

and the exact law

\[
D_t
=[\mathcal A_{NS},D]-[\Pi,K].
\]

That identity remains correct.

However decompose

\[
\mathcal A_{NS}
=\Gamma_{NS}+A_\parallel,
\qquad
[A_\parallel,\Pi]=0.
\]

Then

\[
[\mathcal A_{NS},D]
=[\Gamma_{NS},D]+[A_\parallel,D],
\]

while

\[
-[\Pi,[\mathcal A_{NS},C]]
=-[\Pi,[\Gamma_{NS},C]]
-[\Pi,[A_\parallel,C]].
\]

Jacobi and `[A_parallel,Pi]=0` give

\[
[A_\parallel,D]
=[\Pi,[A_\parallel,C]].
\]

Hence the two tangent-gauge terms cancel exactly.

Therefore the invariant projective law is

\[
\boxed{
D_t
=[\Gamma_{NS},D]
-[\Pi,[\Gamma_{NS},C]].
}
\]

The previous `K` description was an exact gauge-dependent split; the canonical
rank-two connection removes the unphysical tangent rotation and leaves the Hessian
source of Section 3.

This is an architecture correction, not a contradiction with the previous theorem.

**Classification: Exact gauge cancellation / projective correction.**

---

## 5. The whole Hodge curvature hierarchy has the same Hessian law

For every Hodge multiplier `F(C)`, Section 3 gives

\[
\boxed{
\nabla_t^\Gamma D_F
=\frac12 q\wedge H_F q_t,
\qquad
H_F:=\operatorname{Hess}_SR_F.
}
\]

Because `R_F` is a quadratic Rayleigh function, `H_F` has no independent third jet.
Its variation is algebraically forced by the state, exactly as established earlier
for `F=C`.

Thus the entire apparent curvature family

\[
[\mathcal A_{NS},F(C)]
\]

is not needed as primitive projective data.  Its only ray-active content is the
Hessian action

\[
H_Fq_t.
\]

Combined with the preceding divided-difference theorem,

\[
D_F=\mathfrak D_F^C(D),
\]

all strong Hodge mismatch evolution is generated by

\[
\boxed{
\text{one ray }q,
\quad
\text{one velocity }q_t,
\quad
\text{one fixed Hodge operator }C.
}
\]

No extra curvature state survives the canonical quotient.

**Classification: Exact/Rigorous projective synthesis.**

---

## 6. Universal eikonal squaring generates the dyadic Hodge hierarchy

For any self-adjoint operator `F` on the smooth core, the universal Rayleigh-square
identity is

\[
\boxed{
R_{F^2}
=R_F^2+\frac14\|\nabla_SR_F\|_2^2.
}
\]

By Section 3 of the preceding theorem and the covariance Gram identity,

\[
\frac14\|\nabla_SR_F\|_2^2
=\operatorname{Var}_q(F)
=\frac12\|[\Pi,F]\|_{HS}^2.
\]

Hence

\[
\boxed{
R_{F^2}
=R_F^2
+\frac12\|[\Pi,F]\|_{HS}^2.
}
\]

Now choose the positive Hodge generator

\[
\Lambda=|C|
\]

and define

\[
F_n:=\Lambda^{2^n},
\qquad
R_n:=\langle q,F_nq\rangle.
\]

Since

\[
F_{n+1}=F_n^2,
\]

one obtains the exact recursion

\[
\boxed{
R_{n+1}
=R_n^2
+\frac14\|\nabla_SR_n\|_2^2
=R_n^2+\frac12\|[\Pi,F_n]\|_{HS}^2.
}
\]

Thus no new scalar mechanism appears at arbitrarily high dyadic Hodge order.  Each
next scale is exactly

\[
\boxed{
\text{square of the current center}
+
\text{current projective spread}.
}
\]

This is an infinite first-jet/eikonal closure of the positive Hodge moment ladder.
It is not a finite-dimensional closure of the PDE state; `q` remains the full state.

**Classification: Exact iterated Rayleigh-square identity.**

---

## 7. Critical center plus critical spread is exactly the radial viscous tax

At the first two levels,

\[
R_0
=\kappa
:=\langle q,\Lambda q\rangle
=\frac{\mathcal K}{E},
\]

and

\[
R_1
=\langle q,\Lambda^2q\rangle
=\langle q,C^2q\rangle
=\mu
=\frac ZE.
\]

The eikonal recursion gives

\[
\boxed{
\mu
=\kappa^2
+\frac12\|D_\Lambda\|_{HS}^2,
\qquad
D_\Lambda:=[\Pi,\Lambda].
}
\]

Since

\[
\dot r=-\nu r\mu,
\]

one gets the exact positive-scale radius law

\[
\boxed{
-\frac{\dot r}{\nu r}
=\kappa^2
+\frac12\|D_\Lambda\|_{HS}^2.
}
\]

The two terms have a direct meaning:

- `kappa` is the positive Hodge center of the normalized spectral state;
- `||D_Lambda||^2/2` is its positive Hodge variance/spread.

A large positive critical center is therefore never free even when the state is
perfectly shell-aligned: its square is paid directly through radial viscous loss.
If positive-scale spread is also present, that spread adds another positive radial
tax.

This is the positive-Hodge counterpart of the earlier signed
`lambda^2+||D||^2/2` decomposition, but it is adapted directly to critical scale.

**Classification: Exact critical-center/spread radius identity.**

---

## 8. Viscosity descends the entire monotone positive-Hodge cone at once

Let

\[
A=C^2=\Lambda^2
\]

and let `f` be a real nondecreasing scalar function on the positive spectrum of `A`
for which the moment is finite.  Define

\[
m_f:=\langle q,f(A)q\rangle.
\]

The normalized Hodge moment law gives the viscous contribution

\[
(\dot m_f)_\nu
=-2\nu\operatorname{Cov}_q(f(A),A).
\]

If `X,Y` are independent spectral samples from the normalized `A`-measure, then

\[
\operatorname{Cov}(f(A),A)
=\frac12\mathbb E[(f(X)-f(Y))(X-Y)].
\]

Because `f` is nondecreasing, the integrand is nonnegative.  Therefore

\[
\boxed{
(\dot m_f)_\nu\le0
}
\]

for the whole monotone cone simultaneously.

Equivalently, in commutator Gram form,

\[
\boxed{
\langle[\Pi,f(A)],[\Pi,A]\rangle_{HS}
\ge0.
}
\]

Thus viscosity does not merely dissipate a selected norm.  Its one projective
gradient direction sorts the normalized spectral state downward for **every
monotone positive Hodge readout at once**.

For the dyadic hierarchy,

\[
\boxed{
(\dot R_n)_\nu
=-\nu\iint
(x^{2^{n-1}}-y^{2^{n-1}})(x-y)
\,d\pi_A(x)d\pi_A(y)
\le0
}
\]

for `n>=1`, with the obvious `R_0=<Lambda>` version written in the positive variable
`ell=sqrt(x)`.

**Classification: Rigorous monotone-covariance consequence of the exact normalized viscous law.**

---

## 9. One-Laplacian-shell states are a common first-order null of critical transfer and viscous shape motion

The condition

\[
D_\Lambda=[\Pi,\Lambda]=0
\]

is equivalent to

\[
\operatorname{Var}_q(\Lambda)=0.
\]

Hence the normalized spectral measure of `Lambda` is concentrated at one value

\[
\kappa>0.
\]

Equivalently,

\[
\boxed{
\Lambda q=\kappa q,
\qquad
C^2q=\kappa^2q.
}
\]

The state may still contain both curl signs `+kappa` and `-kappa`; this is broader
than a Beltrami eigenstate.

At such an instant the positive critical Rayleigh gradient vanishes:

\[
\nabla_S\kappa=0.
\]

Therefore the Euler critical-center derivative is exactly

\[
\boxed{
(\dot\kappa)_E=0.
}
\]

Viscous projective motion also vanishes because

\[
(C^2-\mu)q=0,
\qquad
\mu=\kappa^2,
\]

so

\[
\boxed{
(q_t)_\nu=0,
\qquad
(\dot\kappa)_\nu=0.
}
\]

Yet the physical radius still obeys

\[
\boxed{
\dot r=-\nu\kappa^2r.
}
\]

Thus a high-frequency one-Laplacian-shell state has a rigid first-order anatomy:

\[
\boxed{
\begin{gathered}
\text{positive critical center frozen,}\\
\text{viscous ray shape frozen,}\\
\text{but physical radius dissipated at rate }\nu\kappa^2.
\end{gathered}
}
\]

Euler may still move the oriented ray because signed `D=[Pi,C]` can be nonzero for a
heterochiral `+/-kappa` mixture.  But it cannot increase the positive Hodge center
without first leaving the shell and creating `D_Lambda`.

This strictly strengthens the earlier pure-Beltrami calibration: the positive-scale
null set is an entire Laplacian eigenshell, not only a single signed-curl eigenspace.

**Classification: Exact one-shell first-order null theorem.**

---

## 10. Critical cascade must create spread before it can move the center

At a one-shell state,

\[
D_\Lambda=0,
\qquad
(q_t)_\nu=0.
\]

Let

\[
a_E:=(q_t)_E.
\]

The canonical curvature law of Section 3 with `F=Lambda` gives

\[
\boxed{
\partial_tD_\Lambda
=q\wedge(\Lambda-\kappa)a_E
}
\]

at that instant, because the Lax term vanishes when `D_Lambda=0` and
`Lambda q=kappa q`.

The first derivative of the center is zero, but its second derivative is

\[
\boxed{
\ddot\kappa
=2\langle a_E,(\Lambda-\kappa)a_E\rangle
}
\]

at the same shell instant.  The acceleration has no universal sign: Euler may begin
to move positive mass toward higher or lower `Lambda` values.

The exact structural statement is instead causal:

\[
\boxed{
\text{Euler must first create }D_\Lambda\text{ before positive critical center transfer can occur.}
}
\]

Once the spread exists, Section 7 makes it an additional positive radial tax and
Section 8 makes it visible to the monotone viscous sorting direction.

This is a create--spread--transfer--dissipate grammar generated by one ray path, not
four independent mechanisms.

**Classification: Exact shell-departure curvature and second-variation identities; no favorable sign claimed.**

---

## 11. The signed mismatch remains the engine that can leave a positive shell

The one-shell condition

\[
D_\Lambda=0
\]

does **not** imply

\[
D=[\Pi,C]=0.
\]

For a heterochiral mixture on the same `Lambda=kappa` shell,

\[
Cq
\neq
\lambda q
\]

in general, so the signed ray--curl mismatch survives.

The Euler ray velocity is still

\[
\boxed{
(q_t)_E
=rC^{-1}[q,Dq]_{\rm Lie}.
}
\]

Therefore the only mechanism capable of leaving a positive shell is exactly the
signed/oriented mismatch already identified in the Hodge--Lie law.

This gives a sharper relationship between the signed and positive descriptions:

\[
\boxed{
\begin{gathered}
D=[\Pi,C]
\quad\text{is the orientation engine},\\
D_\Lambda=[\Pi,|C|]
\quad\text{is the positive-scale spread},\\
D_\Lambda=\mathfrak D_{|\cdot|}^C(D)
\quad\text{is a contraction/readout of the same }D.
\end{gathered}
}
\]

So positive-scale cascade cannot be generated by an independent unsigned mechanism.
It must be created by the signed mismatch and then appear as the contracted positive
spread.

**Classification: Exact functional-calculus synthesis.**

---

## 12. Infinite Hodge complexity is one repeated center--spread recursion

The dyadic hierarchy gives, for every `n`,

\[
R_{n+1}
=R_n^2+\frac12\|D_n\|_{HS}^2,
\qquad
D_n=[\Pi,\Lambda^{2^n}].
\]

Thus a large next Hodge level has only two intrinsic faces:

1. the current level center `R_n` is already large;
2. the current level has large projective spread `D_n`.

But `D_n` itself is not a new state:

\[
D_n
=\mathfrak D_{\Lambda^{2^n}}^C(D).
\]

Therefore the entire positive dyadic hierarchy is recursively generated from the
same signed first-order mismatch under fixed Hodge functional calculus.

A hypothetical escape through ever higher Hodge moments cannot choose a new mechanism
at each order.  It must repeatedly recycle the same operation:

\[
\boxed{
\text{signed ray--curl mismatch}
\longrightarrow
\text{positive Hodge spread}
\longrightarrow
\text{next Hodge center/spread}.
}
\]

At every positive level viscosity acts through the same monotone spectral selection,
and at the base critical level both center and spread enter the radial energy tax.

**Classification: Rigorous infinite-hierarchy synthesis of exact identities.**

---

## 13. No-escape frontier after the canonical-gauge correction

The preceding milestone left a curvature

\[
K=[\mathcal A_{NS},C]
\]

and asked for a boundary modulus strong enough to prevent causal heat-age
concentration.

The present theorem removes `K` as an independent projective primitive.  After the
canonical ray quotient,

\[
\boxed{
\Gamma_{NS}=q_t\otimes q-q\otimes q_t
}
\]

is the unique off-diagonal rank-two ray connection and

\[
\boxed{
\nabla_t^\Gamma D_F
=\frac12q\wedge H_Fq_t
}
\]

for every Hodge readout.

At the same time the whole positive Hodge hierarchy is generated by the eikonal
recursion

\[
\boxed{
R_{n+1}=R_n^2+\frac12\|D_n\|_{HS}^2.
}
\]

The open no-escape question therefore becomes still narrower:

\[
\boxed{
\begin{gathered}
\text{Can the self-Lie orientation engine }D=[\Pi,C]\text{ drive the canonical ray}\\
\text{through an infinite sequence of positive-scale spread creation events,}\\
\text{so that the eikonal Hodge hierarchy escapes to infinity, while}\\
\text{every one-shell episode freezes positive center transfer at first order,}\\
\text{every created positive spread adds to the radial tax, and viscosity}\\
\text{simultaneously descends the whole monotone positive-Hodge cone?}
\end{gathered}
}
\]

Equivalently, the remaining Zeno must repeatedly create `D_Lambda` and its higher
functional-calculus images from the signed `D` fast enough that the causal
`h^{-1/2}` active-loss measure of the preceding theorem still concentrates at zero.

No theorem here excludes that scenario.

But continuing case-by-case through higher Sobolev moments is now unjustified: the
entire hierarchy has one recursive center--spread law, one canonical ray connection,
one signed orientation engine and one monotone viscous sorting direction.

**Classification: Open no-escape frontier after exact canonical-gauge/eikonal compression.**

---

## 14. Classification summary

### Exact

- ray-gauge decomposition
  `A=Gamma+A_parallel`, `[A_parallel,Pi]=0`;
- canonical rank-two connection
  `Gamma=qdot tensor q-q tensor qdot`, `Pidot=[Gamma,Pi]`;
- `Gamma=[Pi,[Pi,A]]` for any skew generator of the same oriented ray;
- canonical NS connection
  `Gamma_NS=Gamma_E+nu[Pi,C^2]`;
- universal canonical curvature law
  `nabla_t^Gamma D_F=(1/2)q wedge Hess_S(R_F) qdot`;
- exact cancellation of tangent-gauge terms in the previous `K` law;
- universal square law
  `R_(F^2)=R_F^2+||grad R_F||^2/4=R_F^2+||[Pi,F]||_HS^2/2`;
- dyadic positive Hodge recursion
  `R_(n+1)=R_n^2+||D_n||_HS^2/2`;
- critical radius decomposition
  `-rdot/(nu r)=kappa^2+||[Pi,|C|]||_HS^2/2`;
- one-Laplacian-shell first-order null identities;
- shell-departure law
  `D_|C|dot=q wedge (|C|-kappa)(qdot)_E` at a shell state;
- shell second variation
  `kappaddot=2<(qdot)_E,(|C|-kappa)(qdot)_E>`.

### Rigorous consequences

- the full `K=[A_NS,C]` is gauge-dependent below the ray level and should not be a
  primitive no-escape variable;
- viscosity descends every nondecreasing functional of `A=C^2` simultaneously;
- positive critical center cannot be increased at first order from a one-Laplacian
  shell; positive-scale spread must be created first;
- the signed mismatch `D` is the only engine that can create that spread, while
  `D_|C|` and all higher `D_n` are functional-calculus readouts of the same `D`;
- arbitrarily high dyadic Hodge complexity has one repeated center--spread grammar,
  not an infinite mechanism list.

### Open

- a cumulative bound on repeated Euler creation of positive-scale spread;
- a proof that the recursive center--spread mechanism cannot execute a parabolic
  zero-age Zeno cascade;
- the Dini-half active-loss modulus from the preceding theorem;
- continuation, restart, blow-up exclusion and global regularity.
