# Energy-ray Lax / double-bracket master law

## Purpose

The preceding energy-sphere theorem rewrote every smooth nonzero incompressible
Navier--Stokes state as

\[
u=rq,
\qquad
r=\|u\|_2,
\qquad
\|q\|_2=1,
\]

and showed that the scale-free Hodge geometry is the Rayleigh landscape of

\[
C=\operatorname{curl}.
\]

That theorem still described the normalized state through a skew Euler leg and a
sphere-gradient viscous leg.  This note asks the next compression question:

> are those really two different kinds of shape motion, or are they two faces of one
> operator motion of the physical energy ray?

For a smooth nonzero state define the canonical rank-one energy-ray projector

\[
\boxed{
\Pi_q:=q\otimes q,
\qquad
\Pi_qv=q\langle q,v\rangle.
}
\]

No new modeled state is introduced.  `Pi_q` is only the orthogonal projector onto the
actual normalized velocity direction.  It deliberately forgets the sign/orientation
`q -> -q`, so it is **not** claimed to close Navier--Stokes by itself.

Let

\[
\mathbb J(u)v=P_\sigma(v\times Cu)
\]

be the existing skew Lie--Poisson operator, where `P_sigma` is the Leray projector.
Then the normalized Navier--Stokes direction satisfies the exact one-line law

\[
\boxed{
\partial_tq
=\mathcal A_{NS}(u,q)q,
\qquad
\mathcal A_{NS}
:=\mathbb J(u)+\nu[\Pi_q,C^2],
\qquad
\mathcal A_{NS}^*=-\mathcal A_{NS}.
}
\]

The kinetic radius obeys the separate scalar law

\[
\boxed{
\dot r
=-\nu r\,\langle q,C^2q\rangle.
}
\]

Equivalently, the energy ray obeys one Lax equation

\[
\boxed{
\partial_t\Pi_q
=[\mathcal A_{NS},\Pi_q].
}
\]

Thus after the physical `L^2` radius is removed, **both Euler and viscosity act by a
single skew rotation of the energy ray**.  Viscosity becomes the canonical
double-bracket motion

\[
-\nu[\Pi_q,[\Pi_q,C^2]],
\]

while all actual norm loss is carried by the radius equation.

The same calculation also exposes a shorter full-state Hodge--Lie law,

\[
\boxed{
(\partial_t+\nu C^2)u
=C^{-1}[C,\operatorname{ad}_u]u.
}
\]

Thus the Euler velocity is the inverse-Hodge image of the failure of `C` to commute
with self-Lie transport, while viscosity is the square of that same `C`.

The theorem then compresses once more around the single ray--curl commutator

\[
\boxed{D_q:=[\Pi_q,C].}
\]

The previous Beltrami defect, Rayleigh slope, viscous projective generator and extra
radial dissipation all descend from this one rank-two skew operator.

No no-escape or regularity theorem is claimed.  A final section derives a rigorous
cumulative anti-Zeno consequence in a weak Sobolev topology and states precisely why
it is still below continuation strength.

All unbounded-operator identities below are read on the common smooth mean-zero
divergence-free core.  Rank-one commutators are then extended by the displayed
finite-rank formulas whenever convenient.

---

## 1. The unnormalized energy dyad has a commutator--anticommutator law

The whole-PDE law from the preceding milestones is

\[
\boxed{
\partial_tu
=\mathbb J(u)u-\nu C^2u,
\qquad
\mathbb J(u)^*=-\mathbb J(u).
}
\]

Define the canonical energy dyad

\[
\mathcal Q:=u\otimes u.
\]

For rank-one operators we use

\[
(a\otimes b)v=a\langle b,v\rangle.
\]

Differentiate `Q`.  Since `J^*=-J`,

\[
(\mathbb Ju)\otimes u
+u\otimes(\mathbb Ju)
=[\mathbb J,\mathcal Q].
\]

Since `C^2` is self-adjoint,

\[
(C^2u)\otimes u
+u\otimes(C^2u)
=\{C^2,\mathcal Q\},
\]

where

\[
\{A,B\}:=AB+BA.
\]

Hence

\[
\boxed{
\partial_t\mathcal Q
=[\mathbb J(u),\mathcal Q]
-\nu\{C^2,\mathcal Q\}.
}
\]

This is the exact rank-one operator lift of the literal PDE.

The two terms have opposite operator parity:

- the conservative part is a **commutator** with a skew operator;
- the viscous part is an **anticommutator** with the positive Hodge square.

Taking the trace removes the commutator and gives

\[
\operatorname{tr}\mathcal Q=r^2=2E,
\]

and

\[
\boxed{
\frac d{dt}r^2
=-2\nu\langle u,C^2u\rangle.
}
\]

Thus the familiar energy identity is the scalar trace face of the same dyadic law.

The dyad is **not** a reduced Navier--Stokes state: `u` and `-u` have the same
`mathcal Q`, while `mathbb J(-u)=-mathbb J(u)` and the oriented nonlinear motion is
not recoverable from the dyad alone.  This is exactly the orientation/phase no-go
already established elsewhere in the repository.

**Classification: Exact rank-one operator lift; exact parity/trace consequences.**

---

## 2. Normalization turns viscous anticommutator loss into a double bracket

Write

\[
\mathcal Q=r^2\Pi,
\qquad
\Pi=\Pi_q=q\otimes q,
\qquad
\Pi^2=\Pi=\Pi^*.
\]

Define

\[
\boxed{
\mu
:=\langle q,C^2q\rangle
=\operatorname{tr}(\Pi C^2)
=\frac ZE.
}
\]

The radius equation is

\[
\boxed{
\dot r=-\nu r\mu.
}
\]

Differentiate `Q=r^2 Pi` and divide the dyadic law by `r^2`.  The radial loss removes
exactly the scalar part of the viscous anticommutator:

\[
\partial_t\Pi
=[\mathbb J(u),\Pi]
-\nu
\left(
C^2\Pi+\Pi C^2-2\mu\Pi
\right).
\]

Because `Pi` has rank one,

\[
\Pi C^2\Pi=\mu\Pi.
\]

Therefore

\[
\boxed{
C^2\Pi+\Pi C^2-2\mu\Pi
=[\Pi,[\Pi,C^2]].
}
\]

and hence

\[
\boxed{
\partial_t\Pi
=[\mathbb J(u),\Pi]
-\nu[\Pi,[\Pi,C^2]].
}
\]

This is not a formal analogy with a double-bracket flow.  It is the literal
normalized viscous term.

The same identity at the vector level follows from

\[
[\Pi,C^2]q
=\Pi C^2q-C^2q
=-(C^2-\mu)q.
\]

Thus

\[
\boxed{
(\partial_tq)_{visc}
=\nu[\Pi,C^2]q
=-\nu(C^2-\mu)q.
}
\]

The normalized heat leg is tangent to the unit sphere because the radial Hodge-square
expectation `mu` has been removed exactly.

**Classification: Exact normalized double-bracket identity.**

---

## 3. The entire normalized PDE is one skew Lax rotation

Both terms in

\[
\mathcal A_{NS}
:=\mathbb J(u)+\nu[\Pi,C^2]
\]

are skew-adjoint:

\[
\mathbb J(u)^*=-\mathbb J(u),
\qquad
[\Pi,C^2]^*=-[\Pi,C^2].
\]

Therefore

\[
\boxed{\mathcal A_{NS}^*=-\mathcal A_{NS}.}
\]

The normalized state equation is exactly

\[
\boxed{
\partial_tq=\mathcal A_{NS}q.
}
\]

Differentiating `Pi=q tensor q` gives

\[
\boxed{
\partial_t\Pi=[\mathcal A_{NS},\Pi].
}
\]

Equivalently,

\[
\boxed{
\partial_t\Pi
=
\left[
\mathbb J(u)+\nu[\Pi,C^2],
\Pi
\right].
}
\]

The equality with Section 2 uses

\[
[[\Pi,C^2],\Pi]
=-[\Pi,[\Pi,C^2]].
\]

Thus the full nonzero smooth Navier--Stokes trajectory admits the two-line
radius/ray form

\[
\boxed{
\begin{aligned}
\dot r
&=-\nu r\,\operatorname{tr}(\Pi C^2),\\[1mm]
\partial_t\Pi
&=
\left[
\mathbb J(rq)+\nu[\Pi,C^2],
\Pi
\right].
\end{aligned}
}
\]

Or, retaining the oriented unit vector rather than its sign-blind projector,

\[
\boxed{
\begin{aligned}
\dot r
&=-\nu r\,\langle q,C^2q\rangle,\\[1mm]
\partial_tq
&=
\left[
\mathbb J(rq)+\nu[\Pi_q,C^2]
\right]q.
\end{aligned}
}
\]

The radius equation contains all loss of the `L^2` norm.  The ray equation is purely
skew in Hilbert space.  In particular, on every smooth interval one may regard the
ray as transported by the canonical unitary propagator generated by
`mathcal A_NS`; the generator itself remains state-dependent and contains the full
Navier--Stokes difficulty.

This is a geometric decomposition of the actual PDE, not a claim that dissipation has
somehow disappeared.  Viscosity changes the ray by the double bracket and decreases
its radius simultaneously.

**Classification: Exact radius/ray Lax law.**

---

## 4. First operator reduction: fixed Hodge plus alternating form

The Poisson operator is itself generated by the same normalized state:

\[
Cu=rCq,
\]

so

\[
\boxed{
\mathbb J(rq)
=r\,(\iota_{Cq}\Omega)^\sharp,
}
\]

in the pairing convention of the Poisson--Casimir theorem.

Consequently the oriented radius/ray law may be written as

\[
\boxed{
\begin{aligned}
\dot r
&=-\nu r\,\langle q,C^2q\rangle,\\[1mm]
\partial_tq
&=
\left[
 r(\iota_{Cq}\Omega)^\sharp
 +\nu[\Pi_q,C^2]
\right]q.
\end{aligned}
}
\]

No separate `E`, `H`, `Z`, Beltrami score, chirality variable, heat-scale state or
metric state is needed to **write** this law.  They remain useful readouts, but the
literal operator grammar is now

\[
\boxed{
\text{one oriented unit state }q
+\text{ its radius }r
+\text{ fixed first-order Hodge }C
+\text{ constant alternating }\Omega.
}
\]

Moreover `Omega` and `C=*d` are themselves the three-dimensional Hodge/de Rham
operations already present in the earlier skew-square current law.  The present
result does not add a new physical mechanism; it exposes the energy-ray geometry of
that same core.

**Classification: Exact substitution / operator compression.**

---

## 5. The Euler operator is the inverse-Hodge self-Lie defect

The Poisson form is not the only exact representation of the conservative operator.
There is a shorter Lie/Hodge form on the fixed mean-zero harmonic sector.

For smooth divergence-free `v`, with `omega=Cu`,

\[
\nabla\times(v\times\omega)
=(\omega\cdot\nabla)v-(v\cdot\nabla)\omega
=[\omega,v]_{\rm Lie}.
\]

Curl removes the exact component killed by the Leray--Hodge projection.  Therefore

\[
\boxed{
C\,\mathbb J(u)v
=[Cu,v]_{\rm Lie}.
}
\]

After the harmonic component is fixed, this may be read as

\[
\boxed{
\mathbb J(u)v
=C^{-1}[Cu,v]_{\rm Lie}
}
\]

on the corresponding curl-invertible range.  For the actual state `v=u` there is no
harmonic ambiguity, because the Euler nonlinearity has zero spatial mean.

Consequently the full velocity PDE itself is

\[
\boxed{
\partial_tu
=C^{-1}[Cu,u]_{\rm Lie}
-\nu C^2u.
}
\]

This already removes the phase-space three-form and Poisson operator from the
minimal **evolution formula** if one chooses the Lie-algebra representation.  They
remain exact geometric readouts, not independent mechanisms.

There is a still sharper commutator interpretation.  Let

\[
\operatorname{ad}_u v:=[u,v]_{\rm Lie}.
\]

Since

\[
\operatorname{ad}_u u=[u,u]=0,
\]

one has

\[
\begin{aligned}
[C,\operatorname{ad}_u]u
&=C[u,u]-[u,Cu]\\
&=-[u,Cu]\\
&=[Cu,u].
\end{aligned}
\]

Hence literal Navier--Stokes on the fixed mean-zero sector obeys the one-line
Hodge--Lie defect law

\[
\boxed{
\partial_tu
=C^{-1}[C,\operatorname{ad}_u]u
-\nu C^2u.
}
\]

Equivalently,

\[
\boxed{
(\partial_t+\nu C^2)u
=C^{-1}[C,\operatorname{ad}_u]u.
}
\]

This is not a new PDE or a formal analogy.  It is the projected velocity form of the
literal vorticity equation.

Its structural meaning is stricter than the previous phrase "skew rotation minus
Hodge square":

- the entire Euler velocity is generated only by the **failure of the first-order
  Hodge operator `C` to commute with self-Lie transport**;
- the entire viscous operator is the **square of that same `C`**.

Thus the nonlinear and dissipative faces are generated by one fixed Hodge operator:
one through its transport commutator, the other through its adjoint square.

This also meets the material Hodge theorem literally.  In material coordinates the
same natural Hodge operator satisfies

\[
\partial_tC_G=[\mathcal L_U,C_G].
\]

On vector fields `mathcal L_U` is the Lie adjoint representation.  Therefore the
Eulerian operator defect `[C,ad_u]` appearing in the velocity equation is the
conjugate/sign-reversed representation of the same Hodge/Lie noncommutation whose
material face is the Hodge Lax velocity.  Vortex stretching, material Hodge motion
and the full Euler velocity are consequently not merely correlated effects: they
are evaluations of the same naturality defect in different representations.

**Classification: Exact curl/Lie identity and exact velocity master law; rigorous
bridge to the established material Hodge Lax theorem.**

---

## 6. The two apparent commutator defects collapse on the actual state

The preceding section uses the Hodge--Lie defect

\[
[C,\operatorname{ad}_q],
\]

whereas the energy-ray geometry uses the ray--Hodge defect

\[
D=[\Pi,C].
\]

They are not independent on the actual normalized state.

Since

\[
Dq=\lambda q-Cq,
\]

and `lambda` is a spatially constant scalar,

\[
[q,Dq]
=-[q,Cq].
\]

But `ad_q q=0`, so

\[
[C,\operatorname{ad}_q]q
=C[q,q]-[q,Cq]
=-[q,Cq].
\]

Therefore

\[
\boxed{
[C,\operatorname{ad}_q]q
=[q,Dq]_{\rm Lie},
\qquad
D=[\Pi,C].
}
\]

The nonlinear ray velocity becomes

\[
\boxed{
(\partial_tq)_{Euler}
=rC^{-1}[q,Dq]_{\rm Lie}.
}
\]

Section 8 below already gives the viscous identity

\[
[\Pi,C^2]=\{C,D\}.
\]

Combining the two faces yields the single-defect normalized equation

\[
\boxed{
\partial_tq
=rC^{-1}[q,Dq]_{\rm Lie}
+\nu\{C,D\}q,
\qquad
D=[\Pi_q,C].
}
\]

Together with

\[
\boxed{
\dot r
=-\nu r
\left[
(\operatorname{tr}\Pi C)^2
+\frac12\|D\|_{HS}^2
\right],
}
\]

this is an exact radius/single-defect form of Navier--Stokes.

The same derived mismatch `D` is forced to perform all nontrivial shape work:

\[
\boxed{
D
\xrightarrow{\ C^{-1}[q,\,\cdot\,]\ }
\text{Euler Lie rotation},
\qquad
D
\xrightarrow{\ \{C,\,\cdot\,\}\ }
\text{viscous Hodge rotation}.
}
\]

At the same time `||D||_HS^2/2` is exactly the non-Beltrami contribution to the
radial viscous tax.

There is an exact evolution law for the mismatch itself.  Since `C` is fixed in the
Eulerian gauge and

\[
D=[\Pi,C],
\qquad
\Pi_t=[\mathcal A_{NS},\Pi],
\]

Jacobi gives

\[
\boxed{
\partial_tD
=[\mathcal A_{NS},D]
-[\Pi,[\mathcal A_{NS},C]].
}
\]

This separates two fundamentally different operations:

- `[A_NS,D]` is pure Lax transport of the defect;
- `-[Pi,[A_NS,C]]` is the only source that can create or destroy its size.

Indeed `A_NS` and `D` are skew-adjoint, so cyclicity of the finite-rank
Hilbert--Schmidt pairing gives

\[
\boxed{
\langle D,[\mathcal A_{NS},D]\rangle_{HS}=0.
}
\]

Therefore

\[
\boxed{
\frac12\frac d{dt}\|D\|_{HS}^2
=-\left\langle
D,
[\Pi,[\mathcal A_{NS},C]]
\right\rangle_{HS}.
}
\]

Thus the entire change of the unique non-Beltrami mismatch is a **curvature source**:
it is produced only because the actual ray generator fails to commute with the same
fixed Hodge operator `C`.

Using

\[
\mathcal A_{NS}
=\mathbb J(u)+\nu\{C,D\},
\]

one further has

\[
\boxed{
[\mathcal A_{NS},C]
=[\mathbb J(u),C]
+\nu[D,C^2].
}
\]

So even the defect source contains no new operator family: it is the Euler Hodge
commutator plus the `C^2` commutator of the same `D`.

This gives a precise meaning to the possible "zero-curvature" frontier.  A theorem
strong enough for no-escape would have to control this self-generated curvature
source in a topology that sees high-Hodge concentration; the Lax transport term by
itself can never enlarge `||D||_HS`.

This is the strongest compression in the present note.  It does **not** say that an
estimate on `D` is already known.  It says that below this level there are no longer
separate Euler-defect, viscous-shape and Beltrami-defect mechanisms to estimate:
they are three forced actions of one ray--Hodge mismatch.

**Classification: Exact commutator-collapse / single-defect Navier--Stokes law.**

---
## 7. The single ray--curl commutator is the complete non-Beltrami shape defect

Define

\[
\boxed{D:=[\Pi,C].}
\]

Because `Pi` and `C` are self-adjoint,

\[
\boxed{D^*=-D.}
\]

Let

\[
\lambda:=\langle q,Cq\rangle
=H/E,
\qquad
\boxed{g:=\nabla_S\lambda=2(C-\lambda)q}
\]

as in the preceding theorem.  A direct rank-one calculation gives

\[
\boxed{
D
=\frac12
\left(
q\otimes g-g\otimes q
\right).
}
\]

In particular,

\[
\boxed{Dq=-\frac12g.}
\]

Thus the previous Rayleigh gradient and transverse Casimir defect are simply the
vector face of the ray--curl noncommutation:

\[
\boxed{
B=(C-\lambda)u
=\frac r2g
=-rDq.
}
\]

The Hilbert--Schmidt size of `D` is

\[
\|D\|_{HS}^2
=\frac12\|g\|_2^2.
\]

Since

\[
\mu-\lambda^2
=\frac14\|g\|_2^2,
\]

one obtains

\[
\boxed{
\mu-\lambda^2
=\frac12\|D\|_{HS}^2
=\frac{D_B}{E}.
}
\]

Therefore the normalized Hodge-square expectation is

\[
\boxed{
\mu
=\lambda^2+\frac12\|D\|_{HS}^2.
}
\]

The radius law becomes

\[
\boxed{
\dot r
=-\nu r
\left(
\lambda^2+\frac12\|[\Pi,C]\|_{HS}^2
\right).
}
\]

The meaning is exact:

- the commuting part `lambda` is the Beltrami-aligned curl barycenter;
- the entire departure of the energy ray from a curl eigendirection is the one
  commutator `[Pi,C]`;
- that same commutator contributes an additional strictly nonnegative radial drain.

Beltrami states are precisely

\[
\boxed{[\Pi,C]=0}
\]

on the oriented rank-one ray, equivalently `g=B=0`.

**Classification: Exact ray--curl commutator / Rayleigh-defect identities.**

---

## 8. Viscous ray rotation is one Hodge action on the same defect

The commutator Leibniz rule gives

\[
[\Pi,C^2]
=[\Pi,C]C+C[\Pi,C].
\]

Hence, with `D=[Pi,C]`,

\[
\boxed{
[\Pi,C^2]
=DC+CD
=\{C,D\}.
}
\]

Because `C` is self-adjoint and `D` is skew,

\[
\{C,D\}^*=-\{C,D\}.
\]

Therefore the normalized viscous rotation generator is not a second independent
shape defect:

\[
\boxed{
\mathcal A_{visc}^{ray}
=\nu\{C,D\}.
}
\]

It is obtained by one Hodge action on the same ray--curl commutator that measures the
Beltrami defect.

The viscous ray equation is correspondingly

\[
\boxed{
(\partial_t\Pi)_{visc}
=\nu[\{C,D\},\Pi].
}
\]

or

\[
\boxed{
(\partial_tq)_{visc}
=\nu\{C,D\}q.
}
\]

This is exactly equal to `-nu(C^2-mu)q`; no new viscous operator has been invented.

**Classification: Exact commutator-Leibniz compression.**

---

## 9. Euler ray motion also sees only the same defect

The Poisson operator obeys the already-established Casimir nullity

\[
\mathbb J(u)Cu=0.
\]

At the normalized level,

\[
\mathbb J(u)q
=P_\sigma(q\times Cu)
=rP_\sigma(q\times Cq).
\]

But

\[
Cq=\lambda q+\frac12g
=\lambda q-Dq.
\]

Pointwise alternation kills the `lambda q` component, so

\[
\boxed{
\mathbb J(u)q
=-r\,\mathcal K_qDq,
\qquad
\mathcal K_qv:=P_\sigma(q\times v).
}
\]

Thus the Euler motion of the energy ray depends only on the same off-diagonal defect
`D`:

\[
\boxed{
(\partial_t\Pi)_{Euler}
=[\mathbb J(u),\Pi]
=
(\mathbb J(u)q)\otimes q
+q\otimes(\mathbb J(u)q).
}
\]

If `D=0`, this vanishes exactly.

The full projective shape law can therefore be read as

\[
\boxed{
\text{one ray--curl defect }D=[\Pi,C]
\quad\xrightarrow{\text{alternation}}\quad
\text{Euler ray rotation},
}
\]

and

\[
\boxed{
D=[\Pi,C]
\quad\xrightarrow{\text{one more Hodge action}}\quad
\text{viscous ray rotation}.
}
\]

The aligned curl `lambda q` contributes to radial dissipation but not to the Euler
ray motion.  This is the operator form of the preceding transverse-Casimir theorem,
now without introducing `B` as an independent primitive.

**Classification: Exact projective-Euler defect dependence.**

---

## 10. The Rayleigh landscape is a scalar shadow of the ray--curl commutator

The preceding milestone used

\[
\lambda(q)=\langle q,Cq\rangle,
\qquad
g=\nabla_S\lambda.
\]

Sections 5--7 show that

\[
g=-2Dq,
\qquad
D=\frac12(q\otimes g-g\otimes q).
\]

Thus `lambda` and its gradient are not an additional layer beneath the present
operator law.  They are the diagonal and off-diagonal blocks of the fixed `C` relative
to the moving energy ray.

Indeed the state-adapted block identity from the preceding theorem can be rewritten
as

\[
C
=\begin{pmatrix}
\lambda & *\\
* & *
\end{pmatrix},
\qquad
[\Pi,C]
=\begin{pmatrix}
0 & *\\
-* & 0
\end{pmatrix}.
\]

The scalar Rayleigh variance law

\[
\mu=\lambda^2+\frac14\|g\|^2
\]

is exactly

\[
\boxed{
\mu=\lambda^2+\frac12\|[\Pi,C]\|_{HS}^2.
}
\]

Hence the `value + slope` theorem is the scalar Hilbert--Schmidt shadow of one
operator diagonal/off-diagonal decomposition.

Likewise the previous leaf-tangent curvature and Hessian commutator laws arise by
differentiating the moving off-diagonal block `D=[Pi,C]` while `C` itself remains
fixed.

**Classification: Rigorous representation descent from the exact commutator
identities.**

---

## 11. One normalized Hodge-moment law follows from the same Lax equation

Let `F(C)` be a self-adjoint Hodge spectral multiplier on the common smooth domain and
define its normalized moment

\[
\boxed{
m_F
:=\langle q,F(C)q\rangle
=\operatorname{tr}(\Pi F(C)).
}
\]

Differentiate with the Lax equation.  The Euler contribution is

\[
\operatorname{tr}
([\mathbb J,\Pi]F)
=\operatorname{tr}
(\Pi[F,\mathbb J]).
\]

Since `F(C)` commutes with `C^2`, the double-bracket term reduces to the centered
Hodge covariance

\[
-2\nu
\left(
\langle q,F(C)C^2q\rangle
-m_F\mu
\right).
\]

Thus the whole normalized Hodge family obeys

\[
\boxed{
\dot m_F
=\langle q,[F(C),\mathbb J(u)]q\rangle
-2\nu
\left(
 m_{FC^2}-m_Fm_{C^2}
\right).
}
\]

The two faces have a precise common meaning:

- Euler changes a Hodge moment only by **noncommutation** of that Hodge readout with
  the same Poisson rotation;
- viscosity changes it by the **centered covariance with `C^2`** required by unit
  normalization.

For `F=I`, both terms vanish.

For `F=C`, Casimir nullity gives

\[
\boxed{
\dot\lambda
=-2\nu(m_{C^3}-\lambda\mu).
}
\]

There is no Euler contribution.

For `F=C^2`,

\[
\boxed{
\dot\mu
=\langle q,[C^2,\mathbb J(u)]q\rangle
-2\nu(m_{C^4}-\mu^2).
}
\]

The viscous term is exactly

\[
-2\nu\operatorname{Var}_q(C^2)
=-\frac\nu2\|\nabla_S\mu\|_2^2.
\]

The Euler commutator is the same Hessian/rotation production derived in the preceding
Rayleigh theorem.

Thus that theorem's scalar hierarchy descends from the single energy-ray Lax law.

**Classification: Exact whole-Hodge normalized moment law.**

---

## 12. Spectrally, viscosity is a centered selection law, not an independent sink zoo

Let `E_C(dc)` denote the spectral resolution of self-adjoint curl and define the
probability spectral measure of the normalized state by

\[
\boxed{
\pi_q(B)
:=\langle q,E_C(B)q\rangle.
}
\]

Then

\[
\int d\pi_q=1,
\qquad
\lambda=\int c\,d\pi_q(c),
\qquad
\mu=\int c^2\,d\pi_q(c).
\]

Applying Section 9 to bounded spectral indicators gives, on the smooth spectral
approximation domain,

\[
\boxed{
\partial_t\pi_q(B)
=\langle q,[E_C(B),\mathbb J(u)]q\rangle
-2\nu\int_B(c^2-\mu)\,d\pi_q(c).
}
\]

The viscous face is therefore a centered spectral selection/replicator law: modes
with `c^2` above the current mean `mu` lose normalized weight, and modes below it gain
normalized weight because the total mass has been renormalized to one.

The Euler face is a signed phase/orientation current.  It is not determined by
`pi_q` alone, in agreement with the earlier parity and whole-quadratic exhaustion
no-go theorems.

This section is not a new spectral model.  It is the spectral shadow of the exact
rank-one Lax equation.

**Classification: Exact spectral-measure consequence on the common smooth/bounded
functional-calculus domain; no spectral closure claim.**

---

## 13. The same law yields a cumulative Hamiltonian path budget

The operator compression also gives a rigorous partial anti-Zeno consequence without
inventing a first-bad score.

The actual Euler velocity is

\[
X_E=\mathbb J(u)u=P_\sigma(u\times Cu).
\]

Because

\[
Cu=\lambda u+B,
\qquad
u\times(\lambda u)=0,
\]

one has

\[
\boxed{X_E=P_\sigma(u\times B).}
\]

On the three-dimensional torus, Sobolev duality

\[
H^{1/2}\hookrightarrow L^3,
\qquad
H^1\hookrightarrow L^6
\]

and boundedness of the Leray projector give a torus constant `C_T` such that

\[
\|X_E\|_{H^{-1/2}}
\le
C_T\|u\|_{H^1}\|B\|_2.
\]

On the mean-zero divergence-free sector, the Hodge identity/Poincare equivalence
allows `||u||_(H^1)` here to be bounded by a fixed torus constant times `||Cu||_2`.
Absorbing that fixed constant into `C_T`,

\[
\boxed{
\|X_E\|_{H^{-1/2}}
\le
C_T\|Cu\|_2\|B\|_2.
}
\]

Now

\[
\|Cu\|_2^2=r^2\mu,
\qquad
\|B\|_2^2=r^2(\mu-\lambda^2),
\]

whereas the exact energy law is

\[
-\dot E
=\nu r^2\mu.
\]

Therefore

\[
\boxed{
\|X_E\|_{H^{-1/2}}
\le
\frac{C_T}{\nu}
\sqrt{1-\frac{\lambda^2}{\mu}}
\,(-\dot E).
}
\]

The square-root factor is intrinsic:

\[
1-\frac{\lambda^2}{\mu}
=\frac{D_B}{Z}
=\frac{\|[\Pi,C]\|_{HS}^2}{2\mu}.
\]

Thus every increment of Hamiltonian motion in this energy-level weak topology is
absolutely continuous with respect to the **actual viscous energy-loss measure**, and
its density vanishes in the Beltrami limit.

Integrating over any smooth interval `[a,b]` gives

\[
\boxed{
\int_a^b
\|X_E(t)\|_{H^{-1/2}}\,dt
\le
\frac{C_T}{\nu}
\big(E(a)-E(b)\big)
\le
\frac{C_T}{\nu}E(a).
}
\]

There is an equivalent normalized-ray version.  Since

\[
(\partial_tq)_{Euler}=X_E/r
\]

and

\[
-\dot r=\nu r\mu,
\]

one has

\[
\boxed{
\|(\partial_tq)_{Euler}\|_{H^{-1/2}}
\le
\frac{C_T}{\nu}
\sqrt{1-\frac{\lambda^2}{\mu}}
\,(-\dot r),
}
\]

hence

\[
\boxed{
\int_a^b
\|(\partial_tq)_{Euler}\|_{H^{-1/2}}\,dt
\le
\frac{C_T}{\nu}
\big(r(a)-r(b)\big).
}
\]

This is a genuine cumulative anti-Zeno statement: an infinite amount of Euler ray
travel cannot be hidden in finite time **in `H^{-1/2}`** while the energy/radius
budget stays finite.

It is not a regularity theorem.  `H^{-1/2}` is much weaker than the positive
critical topologies whose blow-up control is needed.  A candidate singular cascade
may still have finite weak path length while concentrating infinitely in stronger
Hodge scales.

**Classification: Rigorous Sobolev consequence of the exact ray/defect and energy
laws; partial weak-topology anti-Zeno theorem only.**

---

## 14. Relation to the material Hodge Lax law

The earlier material theorem showed that every natural Hodge operator satisfies

\[
\partial_tA_G=[\mathcal L_U,A_G].
\]

The preceding Rayleigh theorem then identified

\[
\mathcal K_q=-C^{-1}\operatorname{ad}_q
\]

and related spectral transfer to the same Lie/Hodge commutator.

The present result reveals a second Lax face that was still hidden there:

\[
\boxed{
\partial_t\Pi_q
=[\mathcal A_{NS},\Pi_q].
}
\]

These are not two unrelated Lax tricks.

- the **material Hodge Lax law** describes motion of the Hodge calculus under the
  physical diffeomorphism generated by the state;
- the **energy-ray Lax law** describes motion of the normalized state ray relative to
  that Hodge calculus;
- their mismatch is precisely the commutator information already exposed as
  stretching/spectral transfer.

The single defect

\[
[\Pi_q,C]
\]

is the instantaneous off-diagonal mismatch between the energy ray and the Hodge
operator.  It vanishes exactly at Beltrami alignment and drives every nontrivial ray
motion identified above.

This does not yet produce a zero-curvature theorem coupling the two Lax connections.
Establishing or refuting such a stronger compatibility is part of the open frontier.

**Classification: Rigorous synthesis of existing exact Lax identities; stronger
zero-curvature/no-escape consequence Open.**

---

## 15. What has actually been removed from the primitive list

Below this theorem, the following should no longer be treated as independent shape
mechanisms:

- the viscous sphere-gradient leg: it is `nu[Pi,C^2]q`;
- the normalized viscous Hodge sink family: it is the covariance shadow of the same
  double bracket;
- the Rayleigh slope `g`: it is `-2[Pi,C]q`;
- the transverse Casimir defect `B`: it is `-r[Pi,C]q`;
- the Rayleigh variance `mu-lambda^2`: it is `||[Pi,C]||_HS^2/2`;
- the viscous ray generator: it is `nu{C,[Pi,C]}`;
- Beltrami rank collapse: it is simply `[Pi,C]=0`;
- the entire normalized Hodge-moment family: it is a trace shadow of the one ray Lax
  equation.

In the Lie/Hodge representation the minimal evolution grammar is therefore

\[
\boxed{
\begin{gathered}
\text{radius }r,\quad
\text{oriented unit state }q,\quad
\Pi_q=q\otimes q,\\
\text{fixed Hodge generator }C,\quad
\text{the intrinsic Lie bracket of divergence-free fields},\\
\text{and the derived mismatch }D=[\Pi_q,C].
\end{gathered}
}
\]

The alternating form `Omega` and Poisson operator remain exact equivalent geometric
representations, but they are no longer required to write the minimal Lie/Hodge
evolution law.

But even `[Pi,C]` is derived from `q` and the fixed `C`; it is listed only to expose
the unique active mismatch, not as an additional state variable.

**Classification: Rigorous synthesis.**

---

## 16. The no-escape frontier after the energy-ray Lax compression

The new law makes the hypothetical escape geometry still narrower.

A smooth nonzero state must obey simultaneously

\[
\boxed{
\dot r
=-\nu r
\left(
\lambda^2+\frac12\|[\Pi,C]\|_{HS}^2
\right),
}
\]

and

\[
\boxed{
\partial_t\Pi
=\left[
\mathbb J(rq)+\nu\{C,[\Pi,C]\},
\Pi
\right].
}
\]

The aligned part of curl contributes to radial loss but not Euler ray motion.  The
non-Beltrami part is exactly the off-diagonal Hodge commutator `[Pi,C]`.  That same
defect:

1. creates the Euler ray motion through the alternating Poisson operator;
2. creates the viscous ray rotation after one more action of `C`;
3. contributes positively to the radial drain;
4. is the entire Rayleigh slope/variance;
5. generates the spectral/material commutators found in the preceding theorem.

So a candidate escape cannot merely make a Hodge norm large.  It must repeatedly use
one and the same ray--Hodge noncommutation to rotate the state toward higher Hodge
complexity while that mismatch is simultaneously fed into both Hodge sorting and
radial energy loss.

The weak-topology path theorem of Section 13 proves that this self-generated Euler
rotation has finite cumulative `H^{-1/2}` travel.  Therefore any genuine finite-time
escape, if it exists, must be a **strong-topology Zeno phenomenon**: infinitely much
higher-Hodge complexity generated along a ray path that is nevertheless summable in
the energy-level negative topology.

The next literal operator question is therefore not another norm inequality.  The
mismatch already has the exact curvature-source law

\[
\partial_tD
=[\mathcal A_{NS},D]
-[\Pi,[\mathcal A_{NS},C]],
\]

and the first term cannot change `||D||_HS`.  The unresolved question is therefore

\[
\boxed{
\begin{gathered}
\text{Can the self-generated curvature source }
-[\Pi,[\mathcal A_{NS},C]]\\
\text{drive an infinite strong-topology Hodge cascade while the same mismatch }D
\text{ simultaneously}\\
\text{generates viscous Hodge sorting, radial loss, and only finite weak Euler path?}
\end{gathered}
}
\]

Equivalently: does the joint ray/material Hodge geometry force a cumulative
positive-topology control of this already-identified curvature source, or can that
source execute a strong-topology Zeno path despite all the exact simultaneous
constraints above?

That question is Open.

No sign theorem for the active commutator, no positive-topology anti-Zeno estimate,
no restart theorem, no blow-up exclusion and no global-regularity conclusion is
claimed.

**Classification: Open no-escape frontier.**

---

## 17. Classification summary

### Exact

- Hodge--Lie velocity law
  `ut=C^-1[C,ad_u]u-nu C^2u`, equivalently `C J(u)v=[Cu,v]` on the fixed harmonic sector;
- dyadic law
  `Qdot=[J(u),Q]-nu{C^2,Q}`;
- radius law `rdot=-nu r <q,C^2q>`;
- normalized double bracket
  `Pidot=[J(u),Pi]-nu[Pi,[Pi,C^2]]`;
- single skew generator
  `A_NS=J(u)+nu[Pi,C^2]`, `qdot=A_NS q`, `Pidot=[A_NS,Pi]`;
- ray--curl defect
  `D=[Pi,C]=(q tensor g-g tensor q)/2`;
- `B=-rDq`, `mu-lambda^2=||D||_HS^2/2`;
- `[Pi,C^2]={C,D}`;
- single-defect ray law `qdot=r C^-1[q,Dq]+nu{C,D}q`;
- Euler ray motion depends only on `Dq`;
- defect-curvature law `Ddot=[A_NS,D]-[Pi,[A_NS,C]]`, with the Lax transport term
  exactly Hilbert--Schmidt norm-neutral;
- normalized Hodge-moment commutator/covariance law.

### Rigorous consequence

- spectral viscosity is the centered `C^2` selection law of the same double bracket;
- the preceding Rayleigh landscape is the scalar diagonal/off-diagonal shadow of
  `[Pi,C]`;
- Hamiltonian path measure is dominated in `H^{-1/2}` by the actual viscous
  energy/radius-loss measure, with intrinsic Beltrami-defect factor;
- any remaining finite-time escape must be strong-topology Zeno, not infinite weak
  Euler path length.

### Open

- a zero-curvature or mismatch-transport law strong enough to control positive Hodge
  topology;
- a dynamic exclusion of strong-topology Zeno concentration;
- continuation, restart, blow-up exclusion and global regularity.
