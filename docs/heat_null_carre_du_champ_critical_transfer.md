# Heat-null / carré-du-champ reduction of the critical Navier--Stokes transfer

## Purpose

The preceding de Rham skew-square reduction left one literal critical obstruction:

\[
\tau
=-\int_{\mathbb T^3}u\cdot(\omega_+\times\omega_-)\,dx,
\]

or equivalently the oriented fractional-Hodge increment current.  This note asks
whether that scalar is already the bottom of the structure, or whether Navier--Stokes
forces one more exact compatibility beneath it.

The answer is yes.  After eliminating the velocity by the Hodge inverse, the
critical transfer has two additional null structures:

1. it is a commutator of the inverse half-Laplacian with the opposite-chirality
   local rotation, so it requires **simultaneous increments of both curl signs**;
2. by subordination, that commutator is exactly the **heat-semigroup product defect
   of a pointwise alternating null identity**, and that product defect is generated
   by the same carré-du-champ of `A=C^2` that underlies viscous dissipation.

Thus critical nonlinear transfer and critical viscosity are not merely terms of the
same scaling order and not merely two terms sharing a pair kernel.  They descend
from one heat calculus:

\[
\boxed{
\text{pointwise alternating null geometry}
\quad+\quad
\text{Hodge heat product defect / carré-du-champ}.
}
\]

No selector, shell library, packet score, or continuation hypothesis is introduced.
No no-escape, restart, continuation, or global-regularity theorem is claimed.

Throughout, work on the flat three-torus, remove the harmonic velocity mode by a
Galilean choice, and use the positive Hodge operator

\[
A=-\Delta=C^2,
\qquad
C=\operatorname{curl},
\qquad
\Lambda=A^{1/2}=|C|.
\]

All fields below are smooth, periodic and divergence-free on the interval under
consideration.

---

## 1. Canonical Hodge-sign variables

Let

\[
J=C|C|^{-1},
\qquad
P_\pm=\frac12(I\pm J).
\]

Write

\[
a:=\omega_+=P_+\omega,
\qquad
b:=\omega_-=P_-\omega,
\qquad
j:=J\omega=a-b.
\]

Then

\[
\omega=a+b,
\qquad
j=a-b.
\]

Since `C u=omega`, one has

\[
\boxed{
u=\Lambda^{-1}j.}
\]

Here and below the displayed `u` is the actual velocity; the formula is the canonical
Hodge/Biot--Savart reconstruction on the mean-zero divergence-free sector.

The preceding milestone identified the complete nonlinear critical rate as

\[
(\dot{\mathcal K})_{\rm nl}=2\tau,
\qquad
\boxed{
\tau=-\int u\cdot(a\times b)\,dx.
}
\]

Substitution of `u=Lambda^{-1}j` gives the beta-only/chirality-only formula

\[
\boxed{
\tau=-\langle \Lambda^{-1}(a-b),a\times b\rangle.
}
\]

**Classification: Exact Hodge/chirality identity.**

---

## 2. The transfer is an inverse-Hodge commutator, not a raw cubic product

For a vector field `q`, let

\[
X_qv:=v\times q.
\]

Pointwise cross multiplication is skew:

\[
X_q^*=-X_q.
\]

Let

\[
L:=\Lambda^{-1}=A^{-1/2}
\]

on the mean-zero sector, extended by zero on the harmonic sector when an everywhere
defined self-adjoint pseudoinverse is convenient.  Because `a,b` are mean-zero and
divergence-free, Leray and harmonic projections may be inserted or removed inside
the quadratic pairings below.

Using skewness of `X_b`,

\[
2\langle La,X_ba\rangle
=
\langle a,[L,X_b]a\rangle.
\]

Likewise,

\[
2\langle Lb,X_ab\rangle
=
\langle b,[L,X_a]b\rangle.
\]

Since `a cross b=X_ba=-X_ab`, the critical transfer becomes

\[
\boxed{
\tau
=-\frac12\left(
\langle a,[L,X_b]a\rangle
+
\langle b,[L,X_a]b\rangle
\right).
}
\]

Thus dangerous critical growth is already a **commutator defect of the Hodge
inverse**.  If the inverse-Hodge reconstruction commuted with the local opposite-sign
rotation, the critical transfer would vanish.

This is stronger than the statement that mixed chirality is required.  The transfer
also requires failure of spatial constancy/frequency coherence inside the two sign
sectors.

**Classification: Exact inverse-Hodge commutator identity.**

---

## 3. Double-increment null form

Let `G_{-1}(x,y)` denote the symmetric zero-mean Schwartz kernel of the
Moore--Penrose operator `A^{-1/2}` on the torus.  No pointwise positivity of this
zero-mean kernel is asserted or needed.

For a pair `(x,y)` write

\[
\delta a=a(x)-a(y),
\qquad
\delta b=b(x)-b(y),
\]

and

\[
m_a=\frac{a(x)+a(y)}2,
\qquad
m_b=\frac{b(x)+b(y)}2.
\]

Direct symmetrization of the two commutators in Section 2 gives

\[
\boxed{
\tau
=-\frac12\iint
G_{-1}(x,y)
\,(m_a-m_b)\cdot(\delta a\times\delta b)
\,dx\,dy.
}
\]

Using

\[
m_a-m_b=m_j,
\qquad
\delta a\times\delta b
=-\frac12\,\delta\omega\times\delta j,
\]

this becomes the sign-free Hodge form

\[
\boxed{
\tau
=\frac14\iint
G_{-1}(x,y)
\,m_j\cdot
\bigl(\delta\omega\times\delta j\bigr)
\,dx\,dy.
}
\]

This exposes a second exact null structure:

\[
\boxed{
\text{critical transfer requires simultaneous increments of }
\omega\text{ and }J\omega.
}
\]

Equivalently, in chiral variables, both `delta omega_+` and `delta omega_-` must be
present at the same physical pair.  A magnitude-only description that forgets this
signed co-variation cannot recover the transfer.

An independent finite symmetric-kernel algebra referee verifies both double-increment
formulas to machine roundoff.  The computation is only a sign/factor referee; the
formulas above follow algebraically from the self-adjoint inverse Hodge operator and
skew cross multiplication.

**Classification: Exact double-increment commutator identity; audited factor/sign
referee.**

---

## 4. The same viscous heat semigroup resolves the inverse-Hodge commutator

Let

\[
P_s=e^{-sA}
\]

be the canonical Hodge heat semigroup.  On the mean-zero sector,

\[
A^{-1/2}
=\frac1{\sqrt\pi}
\int_0^\infty s^{-1/2}P_s\,ds.
\]

If the pseudoinverse is extended to the full space, the usual harmonic subtraction
`P_s-P_0` is understood.  Its contribution to the quadratic commutators below is
zero because `a,b` are mean-zero and the outer test field is orthogonal to the
harmonic range.

Therefore Section 2 gives

\[
\boxed{
\tau
=-\frac1{2\sqrt\pi}
\int_0^\infty s^{-1/2}
\Big(
\langle a,[P_s,X_b]a\rangle
+
\langle b,[P_s,X_a]b\rangle
\Big)\,ds.
}
\]

This already has an important interpretation: the critical nonlinear transfer is an
integral over the failure of the **same heat semigroup generated by viscosity** to
commute with the local alternating rotation generated by vorticity.

**Classification: Exact subordination/heat-commutator identity.**

---

## 5. Heat smoothing exposes a pointwise null identity

Set

\[
t=\frac s2.
\]

Since `P_s=P_tP_t` and `P_t` is self-adjoint,

\[
\langle a,[P_s,X_b]a\rangle
=2\langle P_ta,P_t(a\times b)\rangle,
\]

while

\[
\langle b,[P_s,X_a]b\rangle
=2\langle P_tb,P_t(b\times a)\rangle.
\]

Adding and using `j=a-b` gives

\[
\langle a,[P_s,X_b]a\rangle
+
\langle b,[P_s,X_a]b\rangle
=
2\langle P_tj,P_t(a\times b)\rangle.
\]

But

\[
a\times b=-\frac12\omega\times j.
\]

Moreover the heat-smoothed fields still obey the pointwise alternating null identity

\[
\boxed{
P_tj\cdot(P_t\omega\times P_tj)=0.
}
\]

Define the heat cross-product defect

\[
\mathfrak D_t^\times(f,g)
:=
P_t(f\times g)-P_tf\times P_tg.
\]

Then the complete critical transfer is

\[
\boxed{
\tau
=\frac1{2\sqrt\pi}
\int_0^\infty s^{-1/2}
\left\langle
P_{s/2}j,
\mathfrak D_{s/2}^\times(\omega,j)
\right\rangle
\,ds.
}
\]

This is the central reduction of the note.

The raw pointwise triple product

\[
j\cdot(\omega\times j)
\]

is identically zero.  Critical transfer exists only because heat coarse-graining is
not multiplicative:

\[
P_t(\omega\times j)
\ne
P_t\omega\times P_tj.
\]

Thus

\[
\boxed{
\text{critical nonlinear growth}
=
\text{heat-product anomaly of an exact alternating null relation}.
}
\]

A two-point self-adjoint heat-semigroup algebra referee verifies at one fixed heat
scale that the spectral commutator, the smoothed cross-product pairing, and the
product-defect pairing agree with the forced factors above.

**Classification: Exact heat-null/product-defect identity; audited factor referee.**

---

## 6. The heat-product anomaly is exactly a carré-du-champ integral

For the flat heat semigroup the cross product obeys the exact product-defect formula

\[
\boxed{
\mathfrak D_t^\times(f,g)
=
2\int_0^t
P_{t-r}
\sum_{k=1}^3
\bigl(
\partial_kP_rf\times\partial_kP_rg
\bigr)
\,dr.
}
\]

This is simply the Duhamel form of the failure of `A=-Delta` to be a derivation.  It
is the cross-product version of the ordinary Bochner/carré-du-champ product defect.

Substituting into Section 5 and moving the self-adjoint heat operator between the two
factors yields

\[
\boxed{
\begin{aligned}
\tau
&=\frac1{\sqrt\pi}
\int_0^\infty s^{-1/2}
\int_0^{s/2}
\sum_{k=1}^3
\int_{\mathbb T^3}
P_{s-r}j
\cdot
\bigl(
\partial_kP_r\omega
\times
\partial_kP_rj
\bigr)
\,dx\,dr\,ds.
\end{aligned}
}
\]

So the only nonlinear critical obstruction left after all previous reductions is an
**oriented determinant of two legs of the Hodge heat carré-du-champ**, paired with a
heat-smoothed copy of the same Hodge-sign vorticity.

Nothing new has been added: `j=J omega`, `P_s=e^{-sC^2}`, and every term is a
canonical functional-calculus image of the original vorticity.

**Classification: Exact carré-du-champ representation of the critical transfer.**

---

## 7. Critical viscosity is the positive square of the same heat calculus

The critical viscous quantity is

\[
D
:=
\langle u,\Lambda^3u\rangle
=
\langle\omega,\Lambda\omega\rangle.
\]

Subordination of `Lambda=A^{1/2}` gives

\[
\boxed{
D
=\frac1{2\sqrt\pi}
\int_0^\infty
s^{-3/2}
\langle\omega,(I-P_s)\omega\rangle
\,ds.
}
\]

For the heat kernel `p_s(x,y)`,

\[
\boxed{
\langle\omega,(I-P_s)\omega\rangle
=
\frac12\iint
p_s(x,y)|\omega(x)-\omega(y)|^2
\,dx\,dy.
}
\]

Equivalently,

\[
\boxed{
\langle\omega,(I-P_s)\omega\rangle
=
2\int_0^{s/2}
\|\nabla P_r\omega\|_2^2\,dr.
}
\]

The Hodge sign is unitary and commutes with the full heat calculus, so at every heat
scale

\[
\boxed{
\langle j,(I-P_s)j\rangle
=
\langle\omega,(I-P_s)\omega\rangle,
}
\]

and at every heat age

\[
\boxed{
\|\nabla P_rj\|_2
=
\|\nabla P_r\omega\|_2.
}
\]

Hence the two derivative legs entering the oriented transfer in Section 6 carry
**exactly the same global heat-scale carré-du-champ energy**.  Critical viscosity is
the positive square of that same heat calculus.

**Classification: Exact heat-semigroup/carré-du-champ identities.**

---

## 8. Canonical heat covariance interpretation

Fix `t>0` and `x`, and let `Y` have density `p_t(x,dy)`.  Then

\[
P_tf(x)=\mathbb E_x f(Y).
\]

The heat product defect is exactly the oriented covariance

\[
\boxed{
\mathfrak D_t^\times(\omega,j)(x)
=
\mathbb E_x\Big[
(\omega(Y)-P_t\omega(x))
\times
(j(Y)-P_tj(x))
\Big].
}
\]

Meanwhile define the two heat variances

\[
V_t^\omega
:=P_t|\omega|^2-|P_t\omega|^2,
\qquad
V_t^j
:=P_t|j|^2-|P_tj|^2.
\]

They are nonnegative, and the vector covariance obeys the pointwise covariance
Cauchy inequality

\[
\boxed{
|\mathfrak D_t^\times(\omega,j)|^2
\le
V_t^\omega V_t^j.
}
\]

More importantly, the Hodge-sign relation is exact after spatial integration at
**every heat age**.  Heat preserves the spatial integral, `J` is unitary, and `J`
commutes with `P_t`, so

\[
\boxed{
\int V_t^j\,dx
=
\int V_t^\omega\,dx
=
\langle\omega,(I-P_{2t})\omega\rangle.
}
\]

Thus the two legs of the oriented heat covariance have the same global variance at
every canonical heat age.

Changing variables `s=2t` in the transfer formula gives

\[
\boxed{
\tau
=\frac1{\sqrt{2\pi}}
\int_0^\infty
t^{-1/2}
\int
P_tj\cdot\mathfrak D_t^\times(\omega,j)
\,dx\,dt.
}
\]

The critical viscous square from Section 7 becomes

\[
\boxed{
D
=\frac1{2\sqrt{2\pi}}
\int_0^\infty
t^{-3/2}
\int V_t^\omega\,dx\,dt.
}
\]

Hence transfer and viscosity can be read at exactly the same heat age `t`:

\[
\boxed{
\text{transfer: heat mean }\times\text{ oriented cross-covariance},
\qquad
\text{viscosity: positive heat variance}.
}
\]


Combining `Kdot=2 tau-nu D` with the two common-age formulas gives the exact
one-line critical balance

\[
\boxed{
\begin{aligned}
\dot{\mathcal K}
=\frac1{2\sqrt{2\pi}}
\int_0^\infty t^{-3/2}
\Bigg[
4t\int
P_tj\cdot\mathfrak D_t^\times(\omega,j)\,dx
-\nu\int V_t^\omega\,dx
\Bigg]dt.
\end{aligned}
}
\]

At this level every derivative/covariance leg has already been generated by the
same heat calculus.  The only unsquared orientation-bearing factor left in the
critical production face is the self-generated heat-scale mean `t P_t J omega`.
This is exact bookkeeping, not a smallness assumption or a new score.

This is not a new covariance bank.  It is the covariance representation of the
same fixed-time Hodge heat product defect.

This is not the programme's earlier future-bank clock and it is not a new stochastic
state.  It is simply the probabilistic representation of the fixed-time Hodge heat
functional calculus.  No cross-clock identification is asserted.

**Classification: Exact heat-kernel covariance representation / architecture typing.**

---

## 9. The previous Kelvin/contact/covariance faces descend again

The earlier repository milestones identified:

- Kelvin quadratic variation as a diffusion carré-du-champ Gram;
- covariance growth as the same product defect under conditional second moments;
- normalized-vorticity contact as the untraced Bochner product identity;
- material stretching as Hodge metric work;
- critical paired chirality as the signed-to-absolute curl defect.

Sections 5--8 now show that the remaining **critical nonlinear transfer itself** is
also generated by the Hodge heat product defect, but applied to the pointwise null
cross product involving `omega` and `J omega`.

Therefore the current primitive list shrinks again.  Below the representation layer,
there are not separate

\[
\text{Kelvin q.v.},\quad
\text{contact Gram},\quad
\text{critical transfer},\quad
\text{viscous dissipation}
\]

mechanisms.  They are positive, untraced, covariance, or oriented-determinant faces
of the same second-order Hodge product defect, with the alternating de Rham current
supplying the null geometry.

**Classification: Rigorous synthesis of exact identities.**

---

## 10. What this does and does not say about no-escape

The heat-null reduction is stronger than a generic Cauchy--Schwarz estimate, but it
does not prove a favorable sign.

Writing the transfer formula with the same scale weight used by the positive
half-Laplacian gives

\[
\tau
=\frac1{2\sqrt\pi}
\int_0^\infty
s^{-3/2}
\left\langle
s\,P_{s/2}j,
\mathfrak D_{s/2}^\times(\omega,j)
\right\rangle
\,ds.
\]

Critical viscosity is

\[
\nu D
=\frac\nu{2\sqrt\pi}
\int_0^\infty
s^{-3/2}
\langle\omega,(I-P_s)\omega\rangle
\,ds.
\]

Thus after all exact cancellations the unresolved factor is no longer an arbitrary
cubic forcing.  At each canonical heat scale it is the **signed alignment of a
heat-scale mean `s P_{s/2}J omega` with the oriented heat covariance generated by
the same field**, while viscosity charges the corresponding positive heat variance.

The factor `s P_{s/2}J omega` has the dimensions of circulation and is forced by the
Hodge heat scale; it has not been inserted as an external threshold or score.  No
uniform bound on it is proved here, and no claim is made that it is pointwise small.


### 10.1 Fixed positive heat ages cannot carry infinite cumulative transfer

The heat-scale representation also gives a genuine partial anti-concentration
theorem.  Let physical time be denoted by `r` in this paragraph, and for a fixed
heat-age cutoff `h_0>0` define the canonical coarse-heat contribution

\[
\tau_{\ge h_0}(r)
:=\frac1{\sqrt{2\pi}}
\int_{h_0}^\infty
h^{-1/2}
\int P_hj(r)\cdot\mathfrak D_h^\times(\omega(r),j(r))\,dx\,dh.
\]

The covariance inequality and the scale-by-scale integrated variance equality give

\[
\int|\mathfrak D_h^\times|\,dx
\le
\left(\int V_h^\omega\right)^{1/2}
\left(\int V_h^j\right)^{1/2}
=
\int V_h^\omega
\le
\|\omega\|_2^2.
\]

Since `j=Lambda u` and the mean-zero torus heat semigroup has a spectral gap,

\[
M(h):=\|\Lambda P_h\|_{L^2\to L^\infty}
\]

satisfies

\[
\int_{h_0}^\infty h^{-1/2}M(h)\,dh<\infty.
\]

Therefore

\[
\boxed{
|\tau_{\ge h_0}(r)|
\le
C(h_0)\,\|u(r)\|_2\,\|\omega(r)\|_2^2,
}
\]

with a finite constant depending only on the fixed torus and `h_0`.  The ordinary
Navier--Stokes energy identity then yields, for every finite smooth physical-time
interval `[0,T]`,

\[
\boxed{
\int_0^T|\tau_{\ge h_0}(r)|\,dr<\infty.
}
\]

Consequently, if the cumulative paired transfer

\[
\Theta(r)=\int_0^r\tau(q)\,dq
\]

were to diverge to `+infinity` at a finite physical time, then for **every** fixed
`h_0>0` the divergent contribution would have to come from heat ages `0<h<h_0`.
No fixed positive Hodge heat scale can carry an infinite cumulative transfer.

Thus any critical escape must be a literal **zero-heat-scale Zeno cascade** in the
canonical Hodge functional calculus, not merely a concentration in physical time at
one persistent spatial scale.

**Classification: Rigorous consequence of the exact heat-covariance law, torus heat
smoothing, and the exact kinetic-energy identity.**

### 10.2 Positive critical growth must reach the viscosity scale in the heat mean

At a fixed smooth physical time the same covariance inequality gives

\[
\left|
\int P_hj\cdot\mathfrak D_h^\times\,dx
\right|
\le
\|P_hj\|_\infty
\int V_h^\omega\,dx.
\]

Insert this into the common-age critical balance.  If

\[
4h\,\|P_hJ\omega\|_\infty\le\nu
\]

for every `h>0`, then every heat-age contribution to `Kdot` is nonpositive and
therefore

\[
\dot{\mathcal K}\le0.
\]

Hence the contrapositive is an exact necessary condition:

\[
\boxed{
\dot{\mathcal K}>0
\quad\Longrightarrow\quad
\text{there exists }h>0\text{ with }
4h\,\|P_hJ\omega\|_\infty>\nu.
}
\]

This is not promoted as a threshold-based no-escape theory.  The number `nu/4` is
forced by the exact common-age balance, and the statement is used only to type what
a growth episode must physically accomplish: its own Hodge-sign heat mean must reach
the viscosity circulation scale at some canonical heat age.

For every fixed smooth physical time, `h ||P_hJ omega||_infty` tends to zero as
`h downarrow 0` and as `h -> infinity`; the dangerous heat age is therefore an
interior scale.  Section 10.1 shows that a hypothetical finite-time escape cannot
keep using a fixed positive interior scale indefinitely: the cumulative obstruction
must migrate toward heat age zero.

**Classification: Rigorous necessary condition for instantaneous positive critical
growth; not a continuation theorem.**

The literal next question is therefore

\[
\boxed{
\begin{gathered}
\text{Can an actual Navier--Stokes vorticity field make its own heat-scale mean}\
\text{remain aligned with its own oriented heat covariance strongly enough}\
\text{across a Zeno sequence of shrinking heat scales to produce }\Theta\to+\infty,\\
\text{while the same heat calculus charges the variance by the positive }C^2\text{ square?}
\end{gathered}
}
\]

A true no-escape theorem would have to rule out that self-induced scale-by-scale
alignment/anti-concentration scenario.  Merely estimating the cross covariance by
its variance and then inserting an external supremum would lose the self-generation
that the present theorem exposes.

**Classification: Conjectural bridge / Open.**

No blow-up exclusion, restart, continuation, or global-regularity conclusion follows
from this note.

---

## 11. Classification

**Exact identity**

- `u=Lambda^{-1}J omega` on the fixed harmonic sector;
- inverse-Hodge commutator formula for `tau`;
- double-increment chiral and `J omega` formulas;
- subordination of `A^{-1/2}` into heat commutators;
- heat-null/product-defect formula for `tau`;
- Duhamel/carré-du-champ formula for the heat cross-product defect;
- positive heat-semigroup representation of critical viscosity;
- scale-by-scale equality of the `omega` and `J omega` heat increment energies;
- canonical heat covariance representation.

**Rigorous consequence**

- critical transfer requires simultaneous heterochiral spatial variation, not merely
  the presence of both signs globally;
- critical transfer is a heat-product anomaly of the exact pointwise null relation
  `J omega . (omega cross J omega)=0`;
- the oriented transfer and positive critical dissipation are generated by the same
  Hodge heat/carré-du-champ calculus;
- the previous Kelvin/contact/covariance critical faces are representations of this
  same second-order defect rather than independent mechanisms;
- every fixed positive heat-age portion of the cumulative transfer has finite total
  variation on finite physical-time intervals;
- positive instantaneous critical growth requires some canonical heat age `h` with
  `4 h ||P_h J omega||_infty > nu`.

**Audited algebra referee**

- a finite symmetric-kernel calculation verifies the double-increment formulas;
- a two-point self-adjoint heat-semigroup calculation verifies the fixed-scale
  commutator, smoothed-cross-product and heat-product-defect factors.

**Conjectural bridge / Open**

- a dynamic anti-concentration theorem for the self-generated heat-scale
  mean--oriented-covariance alignment;
- exclusion of `Theta -> +infinity` in finite physical time;
- no-escape/blow-up exclusion;
- restart/continuation/global regularity.
