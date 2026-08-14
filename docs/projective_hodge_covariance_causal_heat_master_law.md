# Projective Hodge covariance and causal heat-age master law

## Purpose

The preceding energy-ray theorem reduced smooth three-dimensional incompressible
Navier--Stokes to the kinetic radius `r`, the oriented unit state `q`, the rank-one
energy-ray projector

\[
\Pi=q\otimes q,
\]

the fixed first-order Hodge operator

\[
C=\operatorname{curl},
\qquad
A=C^2,
\]

and the ray--curl mismatch

\[
D=[\Pi,C].
\]

The remaining no-escape seam was the curvature source in

\[
D_t=[\mathcal A_{NS},D]-[\Pi,[\mathcal A_{NS},C]],
\qquad
\Pi_t=[\mathcal A_{NS},\Pi].
\]

This note asks whether the apparently separate strong Hodge topologies that could
still support a Zeno escape are genuinely new mechanisms.

They are not.

For every Hodge spectral readout `F(C)`, define only the derived ray commutator

\[
\boxed{
D_F:=[\Pi,F(C)].
}
\]

Then the full normalized Hodge covariance geometry is exactly the Hilbert--Schmidt
Gram geometry of these commutators.  In particular,

\[
\boxed{
\operatorname{Cov}_q(F(C),G(C))
=\frac12\langle D_F,D_G\rangle_{HS}.
}
\]

Moreover every `D_F` is obtained from the single first-order mismatch `D` by the
scalar divided difference of `F`; and every curvature source for `F(C)` is obtained
from the single operator curvature

\[
\boxed{
K:=[\mathcal A_{NS},C]
}
\]

by the same divided-difference map.  Thus critical curl, heat scale, fractional
Hodge moments and higher spectral moments do not carry independent mismatch or
source mechanisms.

The second reduction is causal.  The preceding weak-path theorem gave

\[
\|X_E\|_{H^{-1/2}}
\le
\frac{C_{\mathbb T}}{\nu}
\sqrt{1-\frac{\lambda^2}{\mu}}\,(-\dot E),
\]

where

\[
\lambda=\frac HE,
\qquad
\mu=\frac ZE,
\qquad
X_E=\mathbb J(u)u.
\]

Insert this literal Euler forcing into the mild Hodge heat equation.  The same
canonical heat semigroup used by the earlier heat-scale theorem then yields a
positive causal measure obtained by pushing the **actual defect-weighted viscous
energy loss** onto the heat-age half-line

\[
h=2\nu(t-s).
\]

The critical `H^{1/2}` size is bounded by the negative-half moment of this one causal
measure.  Therefore any divergence of the positive critical Hodge norm must be a
literal zero-heat-age concentration of the same non-Beltrami mismatch that already
drives the energy-ray law.  Physical-time Zeno and heat-age Zeno are consequently
not two frontiers below this theorem: they are the same parabolic corner.

No no-escape, continuation, restart, blow-up exclusion or global-regularity theorem
is claimed.  The remaining open problem is a boundary-nonconcentration theorem for
this self-generated commutator/curvature measure.

All unbounded-operator statements are read on the common smooth mean-zero
divergence-free core unless a bounded functional-calculus statement is explicitly
used.

---

## 1. One ray commutator generates every normalized Hodge variance

Let `F(C)` and `G(C)` be self-adjoint Hodge spectral multipliers for which the
following pairings are finite.  Define

\[
m_F:=\langle q,F(C)q\rangle,
\qquad
m_G:=\langle q,G(C)q\rangle.
\]

Because `Pi=q tensor q`,

\[
D_F
=\Pi F-F\Pi
=q\otimes Fq-Fq\otimes q.
\]

The radial component `m_F q` cancels, so if

\[
b_F:=(I-\Pi)Fq,
\]

then

\[
\boxed{
D_F=q\otimes b_F-b_F\otimes q,
\qquad
D_Fq=-b_F.
}
\]

Thus every Hodge ray mismatch is rank at most two and contains exactly the tangent
fluctuation of that Hodge readout.

For real self-adjoint commuting Hodge multipliers, direct rank-one Hilbert--Schmidt
calculation gives

\[
\begin{aligned}
\frac12\langle D_F,D_G\rangle_{HS}
&=\langle b_F,b_G\rangle\\
&=\langle q,F(C)G(C)q\rangle-m_Fm_G.
\end{aligned}
\]

Hence

\[
\boxed{
\operatorname{Cov}_q(F(C),G(C))
=\frac12\langle D_F,D_G\rangle_{HS}.
}
\]

In particular,

\[
\boxed{
\operatorname{Var}_q(F(C))
=\frac12\|D_F\|_{HS}^2.
}
\]

The earlier identity

\[
\mu-\lambda^2=\frac12\|[\Pi,C]\|_{HS}^2
\]

is only the case `F(c)=c`.

This is not a probabilistic model.  It is the exact covariance geometry of the
spectral measure already carried by the actual normalized NS state.

**Classification: Exact rank-one commutator/covariance identity.**

---

## 2. Spectral formula: all Hodge mismatches are divided-difference images of `D`

Let `E_C(dc)` be the spectral resolution of `C` and

\[
\pi_q(dc):=\langle q,E_C(dc)q\rangle.
\]

The spectral kernel of `Pi` between curl values `c,d` is

\[
E_C(dc)\Pi E_C(dd).
\]

Therefore

\[
E_C(dc)D_FE_C(dd)
=
\big(F(d)-F(c)\big)
E_C(dc)\Pi E_C(dd),
\]

whereas

\[
E_C(dc)DE_C(dd)
=(d-c)E_C(dc)\Pi E_C(dd).
\]

For `c != d`, introduce the scalar divided difference

\[
F^{[1]}(c,d)
:=\frac{F(d)-F(c)}{d-c}.
\]

The diagonal is irrelevant because commutators vanish there.  Hence

\[
\boxed{
D_F
=\mathfrak D_F^C(D),
}
\]

where `mathfrak D_F^C` denotes the spectral double-operator multiplier with kernel
`F^[1](c,d)` on the off-diagonal curl spectrum.

For polynomials this is elementary.  For example,

\[
\boxed{
[\Pi,C^n]
=\sum_{j=0}^{n-1}C^jDC^{n-1-j}.
}
\]

Thus no higher Hodge power introduces a new ray mismatch.

The Hilbert--Schmidt norm has the exact pair representation

\[
\boxed{
\|D_F\|_{HS}^2
=
\iint |F(d)-F(c)|^2\,d\pi_q(c)d\pi_q(d).
}
\]

This is the pair form of Section 1.

**Classification: Exact spectral/divided-difference identity on the stated domain.**

---

## 3. Lipschitz functional calculus cannot amplify the fundamental mismatch

If `F` is scalar Lipschitz on the curl spectrum with constant `L_F`, Section 2 gives

\[
|F(d)-F(c)|\le L_F|d-c|.
\]

Therefore

\[
\boxed{
\|[\Pi,F(C)]\|_{HS}
\le
L_F\|[\Pi,C]\|_{HS}.
}
\]

This is an exact Hilbert--Schmidt contraction theorem for the actual rank-one ray.  It
requires only scalar Lipschitz continuity; no operator-Lipschitz claim in operator
norm is being made.

### 3.1 Positive critical curl

For

\[
F(c)=|c|,
\]

the scalar Lipschitz constant is one, so

\[
\boxed{
\|[\Pi,|C|]\|_{HS}
\le
\|[\Pi,C]\|_{HS}.
}
\]

Thus the projective gradient of the positive critical Hodge readout cannot exceed the
fundamental signed-curl mismatch.

Let

\[
\kappa:=\langle q,|C|q\rangle=\frac{\mathcal K}{E}.
\]

Using Section 1 twice,

\[
\operatorname{Var}_q(C)=\mu-\lambda^2,
\qquad
\operatorname{Var}_q(|C|)=\mu-\kappa^2.
\]

Hence the contraction defect is exactly

\[
\boxed{
\kappa^2-\lambda^2
=
\frac12
\left(
\|[\Pi,C]\|_{HS}^2
-
\|[\Pi,|C|]\|_{HS}^2
\right)
\ge0.
}
\]

This is the operator form of the signed-to-absolute chirality gap.

Spectrally,

\[
(d-c)^2-(|d|-|c|)^2
=
\begin{cases}
0,&cd\ge0,\\
4|cd|,&cd<0.
\end{cases}
\]

Therefore the entire contraction defect is supported on opposite curl signs.  The
previous heterochiral critical obstruction is exactly the failure of the absolute
value map to preserve the ray--curl commutator norm.

### 3.2 Chirality sign

On the mean-zero torus let

\[
J=\operatorname{sgn}C.
\]

The commutator

\[
[\Pi,J]
\]

vanishes on same-sign spectral pairs and sees only opposite-sign coherence.  If

\[
\sigma:=\langle q,Jq\rangle,
\]

then

\[
\boxed{
\frac12\|[\Pi,J]\|_{HS}^2
=1-\sigma^2.
}
\]

Thus chirality imbalance and heterochiral coherence are again one ray-commutator
variance, not a separate state.

### 3.3 Heat calculus

For

\[
F_h(c)=e^{-hc^2},
\]

one has

\[
\sup_c |F_h'(c)|=\sqrt{\frac{2h}{e}}.
\]

Hence

\[
\boxed{
\|[\Pi,e^{-hC^2}]\|_{HS}
\le
\sqrt{\frac{2h}{e}}\,\|D\|_{HS}.
}
\]

The heat ray therefore commutes with the energy ray at least at the canonical
`sqrt(h)` rate whenever the first-order mismatch is finite.

There is also a second exact heat formula using

\[
D_A:=[\Pi,A]=[\Pi,C^2]=\{C,D\}.
\]

Duhamel for the fixed heat semigroup gives

\[
\boxed{
[\Pi,e^{-hA}]
=-\int_0^h
 e^{-sA}D_Ae^{-(h-s)A}\,ds.
}
\]

Consequently

\[
\boxed{
\|[\Pi,e^{-hA}]\|_{HS}
\le h\|D_A\|_{HS}.
}
\]

These are two resolutions of the same heat mismatch: one from the first-order signed
curl defect, the other from the viscous `C^2` ray gradient.

**Classification: Rigorous Lipschitz/heat consequences of the exact spectral formula.**

---

## 4. The whole normalized Hodge family is one projective Gram law

The energy-ray theorem gave

\[
\Pi_t=[\mathcal A_{NS},\Pi],
\qquad
\mathcal A_{NS}
=\mathbb J(u)+\nu D_A,
\qquad
\mathcal A_{NS}^*=-\mathcal A_{NS}.
\]

For a fixed Hodge multiplier `F(C)`,

\[
\begin{aligned}
\dot m_F
&=\operatorname{tr}(\Pi_tF)\\
&=\operatorname{tr}([\mathcal A_{NS},\Pi]F)\\
&=\operatorname{tr}(\mathcal A_{NS}[\Pi,F]).
\end{aligned}
\]

Since both `A_NS` and `D_F` are skew-adjoint,

\[
\operatorname{tr}(\mathcal A_{NS}D_F)
=-\langle\mathcal A_{NS},D_F\rangle_{HS}
\]

whenever the finite-rank pairing is defined.  Thus

\[
\boxed{
\dot m_F
=-\langle\mathcal A_{NS},D_F\rangle_{HS}.
}
\]

Splitting the ray generator gives

\[
\boxed{
\dot m_F
=-\langle\mathbb J(u),D_F\rangle_{HS}
-\nu\langle D_A,D_F\rangle_{HS}.
}
\]

Section 1 converts the viscous face into

\[
-\nu\langle D_A,D_F\rangle_{HS}
=-2\nu\operatorname{Cov}_q(C^2,F(C)),
\]

exactly the centered spectral-selection law already derived in scalar coordinates.

Hence all normalized Hodge observables use the same projective current
`A_NS` and differ only by which derived commutator gradient `D_F` is paired against
that current.

No Hodge norm or moment has an independent evolution mechanism below this law.

**Classification: Exact whole-functional projective pairing law.**

---

## 5. One curvature generates every Hodge source

Define the operator curvature of the actual ray connection relative to fixed curl by

\[
\boxed{
K:=[\mathcal A_{NS},C].
}
\]

For every polynomial `F`, commutator expansion gives

\[
\boxed{
[\mathcal A_{NS},F(C)]
=\mathfrak D_F^C(K),
}
\]

with the same divided-difference map as in Section 2.  Explicitly,

\[
[\mathcal A_{NS},C^n]
=
\sum_{j=0}^{n-1}
C^jKC^{n-1-j}.
\]

The spectral statement is even shorter.  Since

\[
E_C(dc)KE_C(dd)
=(d-c)E_C(dc)\mathcal A_{NS}E_C(dd),
\]

one has

\[
E_C(dc)[\mathcal A_{NS},F(C)]E_C(dd)
=F^{[1]}(c,d)E_C(dc)KE_C(dd).
\]

Thus there is no separate `F`-curvature.

For heat,

\[
[\mathcal A_{NS},A]
=\{C,K\},
\]

and

\[
\boxed{
[\mathcal A_{NS},e^{-hA}]
=-\int_0^h
 e^{-sA}\{C,K\}e^{-(h-s)A}\,ds.
}
\]

The critical, heat, chirality and higher-Hodge transfer commutators are therefore
functional-calculus shadows of the same `K`.

**Classification: Exact commutator functional-calculus identity.**

---

## 6. Universal covariant mismatch law

Introduce the ray connection on operators

\[
\boxed{
\nabla_t^{\mathcal A}X
:=\partial_tX-[\mathcal A_{NS},X].
}
\]

The Lax equation is simply

\[
\boxed{
\nabla_t^{\mathcal A}\Pi=0.
}
\]

Because `C` is fixed in Eulerian coordinates,

\[
\boxed{
\nabla_t^{\mathcal A}C
=-[\mathcal A_{NS},C]
=-K.
}
\]

Now

\[
D_F=[\Pi,F(C)].
\]

Differentiate, use the Jacobi identity, and write

\[
K_F:=[\mathcal A_{NS},F(C)]
=\mathfrak D_F^C(K).
\]

Then

\[
\boxed{
\nabla_t^{\mathcal A}D_F
=-[\Pi,K_F]
=-[\Pi,\mathfrak D_F^C(K)].
}
\]

For `F(C)=C`, this is exactly

\[
\nabla_t^{\mathcal A}D
=-[\Pi,K],
\]

which is the curvature-source law of the preceding theorem.

The important point is that **every strong Hodge mismatch obeys this same law**.
The readout `F` changes only a divided-difference multiplier; it does not change the
underlying source.

This is the operator-level reason that continuing case-by-case through stronger
Sobolev, heat or spectral quantities would duplicate one curvature mechanism.

**Classification: Exact covariant/Jacobi compatibility law.**

---

## 7. Energy-ray co-moving gauge removes all fake Lax transport

Because `A_NS` is skew-adjoint on the smooth interval, let `U(t)` solve formally on
the common smooth core

\[
\partial_tU=\mathcal A_{NS}U,
\qquad
U(a)=I.
\]

On finite spectral truncations this is an ordinary unitary propagator.  The formulas
below are used as exact finite-dimensional conjugacy identities and as formal
common-core guidance only; no global propagator theorem for the unbounded
`A_NS` is claimed here.

Define

\[
\widehat\Pi:=U^*\Pi U,
\qquad
\widehat C:=U^*CU,
\qquad
\widehat K:=U^*KU.
\]

The ray Lax equation gives

\[
\boxed{
\widehat\Pi(t)=\Pi(a).
}
\]

Meanwhile

\[
\boxed{
\partial_t\widehat C
=-\widehat K
=[\widehat C,\widehat{\mathcal A}_{NS}].
}
\]

Thus `C-hat` moves isospectrally while the energy ray is fixed.  In particular the
curl spectrum itself never changes in this gauge; only its orientation relative to
the fixed physical ray changes.

For every Hodge readout,

\[
\widehat D_F
=[\Pi(a),F(\widehat C)],
\qquad
\widehat K_F:=U^*K_FU,
\]

and

\[
\boxed{
\partial_t\widehat D_F
=-[\Pi(a),\widehat K_F].
}
\]

The apparent Lax transport term in Eulerian coordinates was therefore pure frame
motion.  The only genuine change of any Hodge mismatch is the relative Hodge
curvature generated by `K`.

This is the phase-space analogue of the earlier material statement that the Hodge
calculus itself lies on one unitary conjugacy orbit.  The two gauges are not declared
identical; they expose the same structural fact that spectral complexity is relative
operator orientation, not creation of a new intrinsic spectrum.

**Classification: Exact finite-truncation/unitary-conjugacy identity; formal common-core synthesis only.**

---

## 8. The critical and heat frontiers are already contained in the commutator calculus

The positive critical quantity is

\[
\mathcal K
=\frac12\langle u,|C|u\rangle
=E\kappa.
\]

The earlier chirality theorem treated the nonlinear critical transfer and the heat
representation separately.  Sections 2--6 show that both descend from the same
projective functional calculus:

\[
D_{|C|}=\mathfrak D_{|\cdot|}^C(D),
\]

and

\[
[\mathcal A_{NS},|C|]
=\mathfrak D_{|\cdot|}^C(K).
\]

Likewise, at heat age `h`,

\[
D_{e^{-hA}}
=\mathfrak D_{e^{-h(\cdot)^2}}^C(D),
\]

and the heat transfer commutator is

\[
[\mathcal A_{NS},e^{-hA}]
=\mathfrak D_{e^{-h(\cdot)^2}}^C(K).
\]

So the former

\[
\text{critical chirality frontier}
\quad\text{and}\quad
\text{heat-age frontier}
\]

are not independent below the energy-ray law.  They are two scalar functional
calculi applied to the same mismatch and the same curvature.

The remaining analytical issue is not identifying another Hodge observable.  It is
whether the canonical divided-difference images of `D,K` can concentrate at
arbitrarily high Hodge scale in finite physical time.

**Classification: Rigorous synthesis of exact functional-calculus identities.**

---

## 9. The actual nonlinear forcing is dominated by defect-weighted energy loss

Return to the physical velocity equation

\[
\partial_tu=X_E-\nu Au,
\qquad
A=C^2,
\]

with

\[
X_E=P_\sigma(u\times Cu)=P_\sigma(u\times B),
\qquad
B=Cu-\lambda u.
\]

The preceding theorem proved on the three-torus

\[
\boxed{
\|X_E\|_{H^{-1/2}}
\le
C_{\mathbb T}\|Cu\|_2\|B\|_2.
}
\]

Write

\[
\mu=\frac ZE=\frac{\|Cu\|_2^2}{r^2},
\qquad
\mu-\lambda^2=\frac{\|B\|_2^2}{r^2}.
\]

The energy law is

\[
-\dot E
=\nu\|Cu\|_2^2
=\nu r^2\mu.
\]

Define only the derived active fraction

\[
\boxed{
\vartheta
:=
\frac{\|B\|_2}{\|Cu\|_2}
=
\sqrt{1-\frac{\lambda^2}{\mu}}
=
\frac{\|D\|_{HS}}{\sqrt{2\mu}}
\in[0,1].
}
\]

Then

\[
\boxed{
\|X_E\|_{H^{-1/2}}\,dt
\le
\frac{C_{\mathbb T}}{\nu}
\vartheta(t)\,(-dE(t)).
}
\]

The measure on the right is not a new bank.  It is the actual viscous energy-loss
measure multiplied by the exact fraction of curl lying transverse to global Beltrami
alignment.

Define shorthand

\[
\boxed{
d\mathfrak M(t)
:=\vartheta(t)(-dE(t)).
}
\]

only for the next causal statement.  It is positive and finite:

\[
\boxed{
0\le\mathfrak M([a,b])
\le E(a)-E(b)
\le E(a).
}
\]

At exact Beltrami alignment `D=0`, one has

\[
\vartheta=0,
\qquad
d\mathfrak M=0,
\qquad
X_E=0.
\]

Thus arbitrarily high but purely Beltrami dissipation contributes no active nonlinear
forcing measure.  This repairs the benign-thin-layer no-go at the causal forcing
level without declaring high frequency itself bad.

**Classification: Rigorous restatement of the exact energy and defect laws plus the established Sobolev product bound.**

---

## 10. Mild Hodge heat turns the weak path law into a critical Abel law

Fix a smooth interval `[a,t]`.  The projected velocity equation has the exact mild
form

\[
\boxed{
u(t)
=e^{-\nu(t-a)A}u(a)
+\int_a^t e^{-\nu(t-s)A}X_E(s)\,ds.
}
\]

Let

\[
\Lambda=A^{1/2}=|C|.
\]

The positive critical norm is

\[
\|A^{1/4}u(t)\|_2
=\|\Lambda^{1/2}u(t)\|_2.
\]

The fixed heat semigroup obeys the spectral bounds

\[
\|A^{1/4}e^{-\tau A}\|_{L^2\to L^2}
\le c_0\tau^{-1/4},
\]

and

\[
\|A^{1/4}e^{-\tau A}f\|_2
\le c_1\tau^{-1/2}\|f\|_{H^{-1/2}}.
\]

Applying them with `tau=nu(t-s)` gives

\[
\begin{aligned}
\|A^{1/4}u(t)\|_2
&\le
c_0[\nu(t-a)]^{-1/4}\|u(a)\|_2\\
&\quad+
c_1\int_a^t[\nu(t-s)]^{-1/2}
\|X_E(s)\|_{H^{-1/2}}\,ds.
\end{aligned}
\]

Insert Section 9:

\[
\boxed{
\begin{aligned}
\|A^{1/4}u(t)\|_2
&\le
c_0[\nu(t-a)]^{-1/4}r(a)\\
&\quad+
\frac{C_*}{\nu^{3/2}}
\int_a^t
(t-s)^{-1/2}\,d\mathfrak M(s),
\end{aligned}
}
\]

for a fixed torus constant `C_*`.

This is a new cumulative consequence of the earlier weak-path theorem: the positive
critical Hodge size is controlled by a **half-order Abel potential of the actual
active viscous-loss measure**.

No pointwise domination of nonlinearity by viscosity has been used.

**Classification: Rigorous mild-semigroup consequence on every smooth interval.**

---

## 11. Physical time and canonical heat age are the same Zeno variable

The canonical heat-scale theorem uses

\[
P_{h/2}=e^{-(h/2)A}.
\]

A physical-time lag `t-s` under viscosity produces exactly

\[
e^{-\nu(t-s)A}=P_{h/2}
\]

with

\[
\boxed{
h=2\nu(t-s).}
\]

Thus the Abel kernel in Section 10 is not an unrelated temporal construction.  It is
the negative-half kernel on the **same canonical Hodge heat half-line** used by the
existing heat-scale energy density.

For fixed observation time `t`, push the positive measure `dM(s)` forward by

\[
s\mapsto h=2\nu(t-s)
\]

and denote the resulting causal heat-age measure by

\[
\mathfrak M_t^{\rm heat}.
\]

Its total mass is unchanged and finite:

\[
\mathfrak M_t^{\rm heat}((0,2\nu(t-a)])
=\mathfrak M([a,t])
\le E(a)-E(t).
\]

Section 10 becomes, after absorbing fixed factors of two,

\[
\boxed{
\|A^{1/4}u(t)\|_2
\le
C_0h_a^{-1/4}r(a)
+
\frac{C_1}{\nu}
\int_{(0,h_a]}
h^{-1/2}\,d\mathfrak M_t^{\rm heat}(h),
}
\]

where

\[
h_a=2\nu(t-a).
\]

Compare this with the exact canonical heat representation already proved in the repo:

\[
\mathcal K(t)
=\frac1{\sqrt\pi}
\int_0^\infty h^{-1/2}\rho(h,t)\,dh.
\]

The same negative-half Hodge moment therefore appears twice:

1. statically, as the critical moment of the current positive heat density `rho`;
2. causally, as the critical moment of the past defect-weighted energy-loss measure
   pushed onto the same heat-age axis.

This identifies the previously separate phrases

\[
\text{physical-time Zeno}
\quad\text{and}\quad
\text{zero-heat-age Zeno}
\]

as one parabolic corner `h downarrow 0`.

**Classification: Exact parabolic clock identification plus rigorous rewriting of Section 10.**

---

## 12. Necessary parabolic-corner concentration for critical escape

Fix `a<T` inside a smooth interval and suppose the positive critical Hodge norm

\[
\|A^{1/4}u(t)\|_2
\]

diverges along times `t -> T`.

The initial-data term in Section 11 remains bounded because

\[
h_a=2\nu(t-a)
\]

stays bounded away from zero as `t -> T`.

Therefore necessarily

\[
\boxed{
\int_{(0,2\nu(t-a)]}
h^{-1/2}\,d\mathfrak M_t^{\rm heat}(h)
\longrightarrow\infty
}
\]

along the same sequence.

But

\[
\mathfrak M_t^{\rm heat}((0,\infty))
\le E(a)
\]

uniformly.  Hence any critical escape requires concentration of a uniformly finite
positive measure at the single boundary

\[
\boxed{h=0.}
\]

More specifically, because

\[
d\mathfrak M
=
\sqrt{1-\frac{\lambda^2}{\mu}}\,(-dE),
\]

the concentrating mass must carry transverse ray--curl mismatch.  Pure Beltrami
energy loss cannot produce it.

Thus the necessary escape geometry is now:

\[
\boxed{
\begin{gathered}
\text{finite total viscous energy loss,}\\
\text{finite total weak Euler path,}\\
\text{but divergent }h^{-1/2}\text{ moment of the defect-weighted loss}\\
\text{on the causal heat-age boundary }h\downarrow0.
\end{gathered}
}
\]

This is a genuine anti-Zeno reduction, not yet an exclusion theorem.

**Classification: Rigorous necessary condition for divergence of the critical Hodge norm.**

---

## 13. A Dini form of the remaining temporal obstruction

For a finite endpoint `T` define the cumulative active loss

\[
M(t):=\mathfrak M([a,t]),
\qquad
M(T^-):=\lim_{t\uparrow T}M(t),
\]

where the finite monotone limit exists because `M([a,t])<=E(a)`.  The Abel
potential remains finite at the endpoint whenever the near-terminal increments
satisfy the Dini-half condition

\[
\boxed{
\int_0^{\delta_0}
\frac{M(T^-)-M(T-h)}{h^{3/2}}\,dh
<\infty.
}
\]

Indeed integration by parts for the positive measure gives the standard Abel
identity, up to the finite outer-boundary term,

\[
\int_{[T-\delta_0,T)}
(T-s)^{-1/2}\,dM(s)
=
\delta_0^{-1/2}[M(T^-)-M(T-\delta_0)]
+
\frac12\int_0^{\delta_0}
\frac{M(T^-)-M(T-h)}{h^{3/2}}\,dh.
\]

A sufficient power-law condition is therefore

\[
M(T^-)-M(T-h)
\lesssim h^{1/2+\varepsilon}
\]

for some `epsilon>0` near zero.

No such estimate is proved here.  The point is only to identify **exactly which
modulus of the literal active energy-loss measure would close the critical causal
corner**.

This is much narrower than a generic regularity criterion because `M` is not an
externally selected norm: it is forced by the same `D=[Pi,C]` that generates the
normalized PDE.

**Classification: Rigorous Abel/Dini consequence; the required modulus is Open.**

---

## 14. The curvature law is now the only missing source of that boundary modulus

Sections 1--8 show that the entire Hodge functional calculus is generated by

\[
D=[\Pi,C]
\]

and

\[
K=[\mathcal A_{NS},C].
\]

Sections 9--13 show that critical causal escape requires the defect-weighted energy
loss to acquire a singular negative-half moment at zero heat age.

The mismatch itself obeys

\[
\boxed{
\nabla_t^{\mathcal A}D
=-[\Pi,K].
}
\]

Thus the only way the active fraction

\[
\vartheta
=\frac{\|D\|_{HS}}{\sqrt{2\mu}}
\]

can reorganize rapidly enough to feed the parabolic corner is through this same
curvature.

For every stronger Hodge readout `F`, the corresponding law is not new:

\[
\boxed{
\nabla_t^{\mathcal A}D_F
=-[\Pi,\mathfrak D_F^C(K)].
}
\]

Therefore a future no-escape theorem should not estimate an infinite Sobolev
hierarchy separately.  It should prove one boundary-modulus theorem for the
self-generated curvature `K` (or its projectively active block) strong enough to
prevent the finite measure `M` from developing an infinite `h^{-1/2}` moment.

The candidate theorem has now been reduced to the literal question

\[
\boxed{
\begin{gathered}
\text{Can }K=[\mathcal A_{NS},C]\text{, generated by the same NS state whose}\\
\text{ray mismatch is }D=[\Pi,C],\\
\text{drive }\vartheta(-dE)\text{ into a zero-heat-age negative-half-moment}\\
\text{singularity while }D_F=\mathfrak D_F^C(D)\text{ and all Hodge sources}\\
\text{remain divided-difference images of that same }D,K?
\end{gathered}
}
\]

No answer is proved here.

What has been proved is that there is no longer an independent

- critical-norm mechanism,
- chirality mechanism,
- heat-boundary mechanism,
- higher-Sobolev mechanism,
- spectral-covariance mechanism,
- or temporal-Zeno mechanism

below this point.  They are functional-calculus or parabolic readouts of one
ray/Hodge mismatch-curvature system.

**Classification: Rigorous synthesis / Open no-escape frontier.**

---

## 15. Classification summary

### Exact

- `D_F=[Pi,F(C)]=q tensor b_F-b_F tensor q` with
  `b_F=(I-Pi)F(C)q`;
- `Cov_q(F,G)=<D_F,D_G>_HS/2` and
  `Var_q(F)=||D_F||_HS^2/2`;
- spectral pair kernel
  `D_F(c,d)=(F(d)-F(c)) Pi(c,d)`;
- polynomial/divided-difference generation of every `D_F` from `D=[Pi,C]`;
- critical contraction identity
  `kappa^2-lambda^2=(||D||_HS^2-||D_|C|||_HS^2)/2`;
- `D_(C^2)={C,D}`;
- heat commutator Duhamel formula;
- whole normalized Hodge pairing
  `m_Fdot=-<A_NS,D_F>_HS`;
- one curvature `K=[A_NS,C]` generates every `[A_NS,F(C)]` by the same divided
  difference;
- covariant law
  `nabla_t^A D_F=-[Pi,mathfrak D_F^C(K)]`;
- canonical parabolic clock `h=2nu(t-s)`.

### Rigorous consequences

- scalar Lipschitz Hodge readouts contract the fundamental ray--curl mismatch in
  Hilbert--Schmidt norm;
- in particular `||[Pi,|C|]||_HS<=||D||_HS`;
- heat-ray mismatch has both `sqrt(h)||D||` and `h||D_(C^2)||` controls;
- the actual Euler forcing measure is dominated in `H^-1/2` by
  `(C_T/nu) theta(-dE)`;
- the positive critical norm is bounded by the negative-half Abel moment of the
  causal heat-age pushforward of this finite positive measure;
- divergence of the critical Hodge norm therefore requires zero-heat-age
  concentration of defect-weighted viscous loss;
- a Dini-half modulus of that active loss would exclude this particular critical
  causal Zeno mechanism.

### Open

- any intrinsic Dini-half or stronger boundary modulus for the active loss;
- a curvature estimate on `K=[A_NS,C]` strong enough to force that modulus;
- exclusion of the remaining parabolic-corner concentration;
- continuation, restart, blow-up exclusion and global regularity.
