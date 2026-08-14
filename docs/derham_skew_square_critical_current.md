# De Rham skew-square core and the critical increment current

## Purpose

This note deliberately strips away the names accumulated in the preceding
milestones.  It does not add a selector, packet, score, shell model, or continuation
criterion.  The question is whether the material-Hodge conjugacy and the critical
paired-chirality law are themselves shadows of a still smaller operation already
present in literal three-dimensional incompressible Navier--Stokes.

They are.

Let

\[
\alpha=u^\flat,
\qquad
\beta=d\alpha,
\qquad
\delta\alpha=0
\]

on the flat three-torus, after fixing the conserved harmonic/Galilean velocity mode.
The entire equation can be written as one exact closed-two-form current law

\[
\boxed{
\partial_t\beta
+d\Big(\iota_u\beta+\nu\,\delta\beta\Big)=0,
\qquad
\beta=d\alpha.
}
\]

Thus transport and viscosity are not two unrelated mechanisms acting on vorticity.
They are the two canonical one-form currents built from the **same exact two-form**:

\[
\boxed{
\text{antisymmetric self-contraction }\iota_u\beta
\quad+\quad
\text{Hodge-adjoint current }\nu\delta\beta.
}
\]

In three dimensions, after Hodge duality, the same statement becomes an even shorter
skew-square law.  With

\[
C=*d=\operatorname{curl}
\]

on co-closed mean-zero one-forms, the positive Stokes operator is exactly

\[
C^2=-\Delta.
\]

The Euler part uses `C alpha` only to generate a skew rotation of `alpha`; viscosity
uses the square `C^2`.  The skew rotation has `C alpha` in its kernel.  Energy
cancellation, nonlinear helicity cancellation, curl chirality, paired critical
transfer, and positive Hodge diffusion all descend from these facts.

At the canonical critical order `Lambda=|C|`, there is a further exact identity.
The nonlinear critical transfer and the critical viscous sink use the **same positive
fractional-Hodge pair kernel**.  The transfer is its oriented cross-correlation face;
the sink is its squared vorticity-increment face.

No no-escape, restart, continuation, or global-regularity theorem is claimed.

---

## 1. The vorticity equation is one de Rham current conservation law

Use the positive Hodge Laplacian

\[
\Delta_H=d\delta+\delta d=-\Delta_{\rm PDE}.
\]

The exact vorticity-form equation is

\[
\partial_t\beta+\mathcal L_u\beta+\nu\Delta_H\beta=0,
\qquad d\beta=0.
\]

Cartan and closedness give

\[
\mathcal L_u\beta=d\iota_u\beta,
\]

while

\[
\Delta_H\beta=d\delta\beta
\]

because `d beta=0`.  Hence

\[
\boxed{
\partial_t\beta+d\mathcal J_{\rm NS}=0,
\qquad
\mathcal J_{\rm NS}:=\iota_u\beta+\nu\delta\beta.
}
\]

This is an exact conservation law in the de Rham complex.  It says that the vorticity
two-form has no independent bulk source: its time change is an exact differential of
one physical one-form current.

The two visible terms in that current are forced by the same `beta`:

\[
\mathcal J_{\rm Euler}=\iota_u\beta,
\qquad
\mathcal J_{\rm visc}=\nu\delta\beta.
\]

The first is the contraction of the field strength with its own reconstructed
velocity; the second is its Hodge-adjoint current.

**Classification: Exact de Rham/Navier--Stokes identity.**

---

## 2. The velocity can be eliminated: a beta-only self-induced conservation law

On the mean-zero exact vorticity sector, Hodge/Biot--Savart reconstruction gives the
unique co-closed primitive

\[
\alpha=\mathcal B\beta,
\qquad
u=(\mathcal B\beta)^\sharp.
\]

Therefore the vorticity equation closes as

\[
\boxed{
\partial_t\beta
+d\Big(
\iota_{(\mathcal B\beta)^\sharp}\beta
+\nu\delta\beta
\Big)=0,
\qquad d\beta=0.
}
\]

The harmonic velocity mode, if not removed by a Galilean choice, is finite
dimensional and must be carried separately.  It is not hidden in `mathcal B`.

Thus the literal smooth NS vorticity dynamics are a **self-induced nonlinear Hodge
conservation law for one exact two-form**.  No material metric, strain tensor,
pressure field, Kelvin packet, or chirality variable is required as an independent
state at this level.

**Classification: Exact reduction from smooth Navier--Stokes after the harmonic mode
is fixed.**

---

### 2.1 One master Hodge-current identity generates the whole quadratic scale

The conservation law of Section 1 can be tested without introducing separate
balance mechanisms.  Let

\[
A:=\Delta_H
\]

on the exact closed two-form sector, and let `F` be any self-adjoint Hodge spectral
multiplier commuting with `A` on a smooth solution.  Define

\[
Q_F:=\frac12\langle\beta,F\beta\rangle.
\]

Since

\[
\partial_t\beta=-d\mathcal J_{\rm NS},
\qquad
\mathcal J_{\rm NS}=\iota_u\beta+\nu\delta\beta,
\]

adjointness of `d` and `delta` gives the exact master law

\[
\boxed{
\dot Q_F
=-\langle\delta F\beta,\iota_u\beta\rangle
-\nu\langle\delta F\beta,\delta\beta\rangle.
}
\]

Because `d beta=0` and `F` commutes with the Hodge calculus,

\[
\langle\delta F\beta,\delta\beta\rangle
=\langle F\beta,A\beta\rangle.
\]

Thus for positive `F` the second term is the spectrally diagonal Hodge sink.  The
first term is always the pairing of a Hodge test of the **same beta** against the
same alternating current `i_u beta`.

Three formerly separate balances are now just three choices of `F`.

For

\[
F=A^{-1},
\]

one has

\[
Q_{A^{-1}}=\frac12\|u\|_2^2,
\qquad
\delta A^{-1}\beta=\alpha,
\]

and therefore

\[
-\langle\alpha,\iota_u\beta\rangle=0,
\qquad
\dot Q_{A^{-1}}=-\nu\|\beta\|_2^2.
\]

This is kinetic energy.

For

\[
F=A^{-1/2},
\]

one gets exactly the positive critical quadratic

\[
Q_{A^{-1/2}}
=\frac12\langle u,|C|u\rangle
=\mathcal K,
\]

whose nonlinear face is the critical oriented increment current derived below.

For

\[
F=I,
\]

one gets enstrophy:

\[
\boxed{
\frac d{dt}\frac12\|\beta\|_2^2
=-\langle\delta\beta,\iota_u\beta\rangle
-\nu\|\delta\beta\|_2^2.
}
\]

In vector notation the first term is precisely

\[
\int\omega\cdot S\omega,
\]

so vortex stretching is the cross-current face between the alternating and
Hodge-adjoint pieces of `J_NS`.

Hence energy, critical transfer, enstrophy production, and their viscous sinks are
not independent PDE laws.  They are different Hodge tests of one exact two-form
continuity equation.

**Classification: Exact master Hodge-current identity and exact energy/critical/
enstrophy specializations.**

---

## 3. The projected one-form equation uses the same current

Cartan's identity for the momentum one-form gives

\[
\mathcal L_u\alpha
=\iota_u\beta+d(\iota_u\alpha).
\]

Project the one-form Navier--Stokes equation onto co-closed forms.  Exact
pressure/Bernoulli terms disappear under the Leray--Hodge projector `P`, and because
`delta alpha=0`,

\[
\Delta_H\alpha=\delta d\alpha=\delta\beta.
\]

Hence

\[
\boxed{
\partial_t\alpha
+P(\iota_u\beta)
+\nu\delta\beta=0.
}
\]

Applying `d` recovers Section 1.  Conversely, the co-closed Hodge primitive of the
exact two-form equation gives this projected momentum law, modulo the fixed harmonic
mode.

Pressure is therefore the exact complement required before projection; the internal
co-closed dynamics see only the same vorticity current.

There is an even shorter literal notation.  Let

\[
\mathscr D:=d+\delta
\]

be the Hodge--Dirac operator.  On the incompressible one-form sector `delta alpha=0`,

\[
\mathscr D\alpha=d\alpha=\beta,
\qquad
\mathscr D^2\alpha=\Delta_H\alpha.
\]

Hence the projected momentum equation is exactly

\[
\boxed{
\partial_t\alpha
+P\,\iota_{\alpha^\sharp}(\mathscr D\alpha)
+\nu\mathscr D^2\alpha=0,
\qquad
\delta\alpha=0.
}
\]

This notation introduces no new mechanism: it only exposes that the first-order
field generated by the Hodge--Dirac operator is used in an alternating
self-contraction, while the square of the same operator is the viscous generator.

**Classification: Exact projected momentum identity / exact Hodge--Dirac rewrite /
rigorous equivalence on the fixed harmonic sector.**

---

## 4. Three dimensions: one first-order Hodge operator and its square

On co-closed mean-zero one-forms define

\[
C:=*d.
\]

Under the Euclidean musical identification this is the ordinary curl.  It is
self-adjoint and

\[
\boxed{C^2=\Delta_H=-\Delta_{\rm PDE}.}
\]

Moreover

\[
C\alpha=(*\beta)=\omega^\flat.
\]

Thus the same first-order Hodge operator that produces vorticity has a square equal
to the positive viscous generator.

Define, for the actual vorticity two-form `beta`, the co-closed rotation operator

\[
\boxed{
\mathcal R_\beta\eta
:=-P\big(\iota_{\eta^\sharp}\beta\big).
}
\]

In vector notation,

\[
(\mathcal R_\beta\eta)^\sharp
=P(\eta^\sharp\times\omega).
\]

Section 3 becomes

\[
\boxed{
\partial_t\alpha
=\mathcal R_\beta\alpha
-\nu C^2\alpha,
\qquad
\beta=d\alpha.
}
\]

So literal three-dimensional NS has the operator anatomy

\[
\boxed{
\text{state-generated skew rotation from }C\alpha
\quad-\quad
\nu\,C^2\text{ dissipation}.
}
\]

The first derivative is used conservatively as an orientation generator; its square
is used dissipatively.

**Classification: Exact three-dimensional Hodge/Lamb identity.**

---

## 5. The rotation operator is skew and its generator is a null direction

For co-closed one-forms `eta,zeta`, write their dual vectors as `v,w`.  Pointwise,

\[
\langle-\iota_v\beta,\zeta\rangle
=-\beta(v,w)
=\beta(w,v)
=-\langle\eta,-\iota_w\beta\rangle.
\]

Orthogonal projection preserves this pairing on the co-closed range.  Therefore

\[
\boxed{\mathcal R_\beta^*=-\mathcal R_\beta.}
\]

There is also a stronger state-specific null relation.  Since

\[
(C\alpha)^\sharp=\omega
\]

and

\[
\beta=\iota_\omega\,\mathrm{vol},
\]

one has

\[
\iota_\omega\beta
=\iota_\omega\iota_\omega\mathrm{vol}=0.
\]

Hence

\[
\boxed{\mathcal R_\beta(C\alpha)=0.}
\]

These are not estimates.  They are the alternating algebra of the actual vorticity
two-form.

**Classification: Exact algebraic identities.**

---

## 6. Energy and helicity cancellations are the two immediate shadows

Let

\[
E=\frac12\|\alpha\|_2^2.
\]

The nonlinear energy rate is

\[
\langle\alpha,\mathcal R_\beta\alpha\rangle=0
\]

by skew-adjointness; pointwise it is simply

\[
\beta(u,u)=0.
\]

Thus

\[
\boxed{
\dot E=-\nu\|C\alpha\|_2^2.
}
\]

Now let

\[
H=\frac12\langle\alpha,C\alpha\rangle
=\frac12\int u\cdot\omega.
\]

Because `C` is self-adjoint,

\[
(\dot H)_{\rm nl}
=\langle\mathcal R_\beta\alpha,C\alpha\rangle
=-\langle\alpha,\mathcal R_\beta(C\alpha)\rangle
=0.
\]

Therefore

\[
\boxed{
\dot H=-\nu\langle\alpha,C^3\alpha\rangle.
}
\]

In exterior algebra, the same nonlinear helicity cancellation is

\[
\iota_u\beta\wedge\beta=0,
\]

which follows from

\[
0=\iota_u(\beta\wedge\beta)
=2\,\iota_u\beta\wedge\beta
\]

in three dimensions.

Thus energy conservation and Euler-helicity conservation are not two unrelated
miracles.  They are the degree-one and degree-three shadows of the same alternating
vorticity-form contraction.

**Classification: Exact energy/helicity identities; rigorous common-algebra
interpretation.**

---

## 7. Vorticity transport and stretching are the curl of the same sideways current

Apply `C=*d` to the projected one-form equation.  In vector notation this gives

\[
\boxed{
\partial_t\omega
=\nabla\times(u\times\omega)
+\nu\Delta\omega.
}
\]

Equivalently,

\[
\nabla\times(u\times\omega)
=(\omega\cdot\nabla)u-(u\cdot\nabla)\omega
\]

for divergence-free `u,omega`.

Hence the usual split into advection and stretching is a representation split of the
single curl of the same skew current `u cross omega`.

The earlier material statement that stretching becomes metric work is compatible
with this: pulling this same current law into material coordinates removes the
transport representation and transfers the amplitude readout into the moving Hodge
metric.

**Classification: Exact curl/current identity / rigorous representation
compression.**

---

## 8. The previous chirality theorem is the sign decomposition of the same C

Let

\[
\Lambda:=|C|,
\qquad
J:=C|C|^{-1},
\qquad
P_\pm=\frac12(I\pm J).
\]

The positive critical quadratic and signed helicity are

\[
\mathcal K=\frac12\langle\alpha,\Lambda\alpha\rangle,
\qquad
H=\frac12\langle\alpha,C\alpha\rangle.
\]

The nonlinear critical rate from Section 4 is

\[
(\dot{\mathcal K})_{\rm nl}
=\langle\mathcal R_\beta\alpha,\Lambda\alpha\rangle.
\]

Since `R_beta` is skew,

\[
\boxed{
(\dot{\mathcal K})_{\rm nl}
=\frac12
\langle\alpha,[\Lambda,\mathcal R_\beta]\alpha\rangle.
}
\]

By contrast, Section 5 gives

\[
\langle\mathcal R_\beta\alpha,C\alpha\rangle=0.
\]

Therefore the previous signed-to-absolute obstruction is now seen at its source:

\[
\boxed{
\text{the same skew rotation annihilates the signed generator }C\alpha,
\text{ but need not commute with }|C|.
}
\]

The exact equal `+/-` critical transfer law follows by decomposing this single
commutator with the canonical projectors `P_±`.  Chirality is therefore not an added
mechanism; it is the spectral sign anatomy of the first-order operator already
present in the skew-square equation.

There is also a local physical-space form of the same transfer.  Because

\[
\omega=C\alpha,
\qquad
\Lambda\alpha=J\omega,
\]

one has

\[
(\dot{\mathcal K})_{\rm nl}
=\int (u\times\omega)\cdot J\omega\,dx
=\int u\cdot(\omega\times J\omega)\,dx.
\]

Writing

\[
\omega_\pm=P_\pm\omega,
\qquad
J\omega=\omega_+-\omega_-,
\]

gives pointwise

\[
\omega\times J\omega
=-2\,\omega_+\times\omega_-.
\]

Since the preceding milestone used

\[
(\dot{\mathcal K})_{\rm nl}=2\tau,
\]

we obtain the exact heterochiral triple-product law

\[
\boxed{
\tau
=-\int_{\mathbb T^3}
u\cdot(\omega_+\times\omega_-)\,dx.
}
\]

Thus paired critical transfer is not merely a statement about two global spectral
contents.  It is the scalar triple product of the actual velocity with the two
opposite Hodge-curl vorticity components.  If either chirality is absent, the
critical nonlinear transfer vanishes identically.

Combining this with the pair-kernel formula of Section 9 below yields the exact
spectral/physical-space bridge

\[
\boxed{
-\int u\cdot(\omega_+\times\omega_-)\,dx
=
\frac14\iint K_\Lambda(x,y)
(\omega(x)-\omega(y))\cdot(u(x)\times u(y))\,dx\,dy.
}
\]

So heterochiral mixing and oriented vorticity-increment transfer are literally the
same NS quantity in two natural representations.

**Classification: Exact identity / rigorous descent of the preceding chirality
milestone and exact spectral-to-increment bridge.**

---

## 9. The dangerous critical transfer is a vorticity-increment correlation

The previous section still leaves the commutator abstract.  It has a canonical exact
pair representation.

Let

\[
A=C^2=-\Delta,
\qquad
\Lambda=A^{1/2}=|C|.
\]

By subordination,

\[
\Lambda f
=\frac1{2\sqrt\pi}
\int_0^\infty
(I-e^{-sA})f\,\frac{ds}{s^{3/2}}.
\]

Let `p_s(x,y)` be the flat-torus heat kernel and define the positive symmetric
fractional-Hodge kernel

\[
\boxed{
K_\Lambda(x,y)
:=\frac1{2\sqrt\pi}
\int_0^\infty
p_s(x,y)\,\frac{ds}{s^{3/2}}
}
\]

away from the diagonal, understood in the standard principal-value sense.  Then

\[
\Lambda f(x)
=\operatorname{PV}\int
K_\Lambda(x,y)(f(x)-f(y))\,dy.
\]

Because `P` commutes with `Lambda` and can be removed inside pairings with
co-closed fields,

\[
[\Lambda,\mathcal R_\beta]\alpha
\]

has the same quadratic pairing as the commutator of `Lambda` with multiplication by
`v -> v cross omega`.  Direct substitution gives

\[
\boxed{
\langle\alpha,[\Lambda,\mathcal R_\beta]\alpha\rangle
=
\iint
K_\Lambda(x,y)
\big(\omega(x)-\omega(y)\big)
\cdot
\big(u(x)\times u(y)\big)
\,dx\,dy.
}
\]

Consequently

\[
\boxed{
(\dot{\mathcal K})_{\rm nl}
=
\frac12
\iint
K_\Lambda(x,y)
\big(\omega(x)-\omega(y)\big)
\cdot
\big(u(x)\times u(y)\big)
\,dx\,dy.
}
\]

Since the paired-chirality notation of the previous milestone used

\[
(\dot{\mathcal K})_{\rm nl}=2\tau,
\]

one also has

\[
\boxed{
\tau
=
\frac14
\iint
K_\Lambda(x,y)
\big(\omega(x)-\omega(y)\big)
\cdot
\big(u(x)\times u(y)\big)
\,dx\,dy.
}
\]

Thus the scalar `tau` was never an independent bank.  It is the exact oriented
vorticity-increment current of the original PDE at the canonical critical Hodge
order.

**Classification: Exact fractional-Hodge commutator identity.**

---

## 10. Critical viscosity uses the identical pair kernel

The critical viscous term is

\[
D
:=
\langle\alpha,\Lambda^3\alpha\rangle.
\]

Because `omega=C alpha` and `C` commutes with `Lambda`,

\[
D
=\langle\omega,\Lambda\omega\rangle.
\]

The same positive kernel therefore gives

\[
\boxed{
D
=
\frac12
\iint
K_\Lambda(x,y)
|\omega(x)-\omega(y)|^2
\,dx\,dy.
}
\]

Combining Sections 9 and 10 yields the exact critical balance

\[
\boxed{
\begin{aligned}
\dot{\mathcal K}
&=
\frac12
\iint K_\Lambda(x,y)
\Big[
(\omega(x)-\omega(y))\cdot(u(x)\times u(y))\\
&\hspace{37mm}
-\nu|\omega(x)-\omega(y)|^2
\Big]
\,dx\,dy.
\end{aligned}
}
\]

The dangerous transfer and the viscous sink are therefore not merely at the same
scaling order.  They are the **linear-correlation and quadratic-square faces of the
same vorticity-increment field in the same canonical pair geometry**.

This is substantially stronger structurally than saying that one term is cubic and
the other quadratic.

**Classification: Exact common-kernel critical balance.**

---

## 11. Exact square completion, and what it does not prove

At each ordered pair set

\[
a=\omega(x)-\omega(y),
\qquad
b=u(x)\times u(y).
\]

The common-kernel integrand satisfies the algebraic identity

\[
\frac12 a\cdot b-rac\nu2|a|^2
=
-\frac\nu2\left|a-\frac{b}{2\nu}\right|^2
+
\frac1{8\nu}|b|^2.
\]

Therefore

\[
\boxed{
\dot{\mathcal K}
=
-\frac\nu2
\iint K_\Lambda
\left|
\omega(x)-\omega(y)-\frac{u(x)\times u(y)}{2\nu}
\right|^2
+
\frac1{8\nu}
\iint K_\Lambda|u(x)\times u(y)|^2.
}
\]

This is an exact identity, not a proposed Lyapunov functional.  The last positive
term is not known to be controlled by the first one or by energy alone, and the
amplitude-scaling no-go from the preceding milestone forbids interpreting this
square completion as an instantaneous no-escape estimate.

Its structural content is different: any positive critical growth requires a
coherent pairwise orientation correlation between the vorticity increment and the
oriented velocity pair in precisely the same fractional geometry in which viscosity
measures the increment square.

**Classification: Exact algebraic reformulation; no favorable sign claimed.**

---

## 12. The same law explains the prior local/contact/Kelvin observations

The pair kernel in Section 10 is the critical fractional counterpart of the local
Bochner/Kelvin Gram already present in the repository.  At full derivative order,
viscous enstrophy loss uses

\[
\nu\|\nabla\omega\|_2^2,
\]

and orientation-complete Kelvin quadratic variation reads the corresponding local
gradient Gram.  At the half-derivative critical order, the same positive Hodge
calculus reads vorticity increments through `K_Lambda`.

Likewise, the normalized-vorticity contact Gram records how the direction/amplitude
of vorticity changes spatially.  Section 9 shows that critical spectral transfer is
also driven by vorticity variation, but paired against the oriented velocity
geometry rather than against itself.

These are not new independent mechanisms.  They are different pairings of the same
Hodge-generated variation of the exact vorticity form.

**Classification: Rigorous synthesis of previously exact local and spectral
identities.**

---

## 13. Orientation/phase cannot be quotiented out

The common-kernel law gives a sharp no-go against another tempting reduction.
Consider the instantaneous state reversal

\[
u\mapsto -u,
\qquad
\omega\mapsto-\omega.
\]

Every even magnitude observable in the critical pair law is unchanged:

\[
E,\quad \mathcal K,\quad D,\quad
|\omega(x)-\omega(y)|^2,\quad
|u(x)\times u(y)|^2
\]

are identical for `u` and `-u`.  But

\[
u(x)\times u(y)
\]

is unchanged while

\[
\omega(x)-\omega(y)
\]

changes sign.  Therefore

\[
\boxed{\tau(-u)=-\tau(u).}
\]

So no instantaneous state description that retains only magnitude, Gram, spectral
mass, or unsigned pair-energy data can determine even the **sign** of the dangerous
critical transfer.  The oriented triple correlation is irreducible unless another
exact PDE law reconstructs it.

This is the critical-order version of the earlier warning about over-quotienting
cross-channel coherence.  Here it is forced directly by Navier--Stokes itself:
phase/orientation is not bookkeeping decoration but literal transfer information.

A norm-only or positive-bank no-escape theory therefore cannot be the hidden law.
Any successful dynamic compatibility must retain enough signed/oriented information
to distinguish the two states above.

**Classification: Exact parity consequence / rigorous magnitude-only no-go.**

---

## 14. The material-Hodge theorem is the pulled-back representation of the same core

The earlier material theorem wrote

\[
\partial_t\bar\beta=\nu\Delta_G\bar\beta
\]

because the pullback by the actual Lagrangian flow absorbs the Lie-transport face.
Section 1 instead keeps fixed Eulerian coordinates and writes

\[
\partial_t\beta+d(\iota_u\beta+\nu\delta\beta)=0.
\]

These are the same equation in two gauges:

- fixed Eulerian gauge: the self-contraction current is visible;
- material gauge: that current is absorbed by pullback and the Hodge geometry moves.

The universal Hodge-conjugacy/Lax law from the preceding milestone is therefore not
a second primitive.  It is the functorial motion of the Hodge calculus generated
when the same de Rham current law is expressed in material coordinates.

**Classification: Exact gauge/representation equivalence.**

---

## 15. What has actually been compressed

After this reduction, the following formerly separate statements descend from one
small algebraic/PDE core:

\[
\boxed{
\beta=d\alpha,
\qquad
\partial_t\beta+d(\iota_{\mathcal B\beta}\beta+\nu\delta\beta)=0.
}
\]

In three dimensions this is equivalently

\[
\boxed{
\partial_t\alpha
=\mathcal R_\beta\alpha-
u C^2\alpha,
\qquad
\mathcal R_\beta^*=-\mathcal R_\beta,
\qquad
\mathcal R_\beta(C\alpha)=0.
}
\]

From these follow, as representations or immediate algebraic consequences:

- pressure/Leray constraint;
- Kelvin/Cartan transport;
- vorticity advection plus stretching;
- energy nonlinear cancellation;
- helicity nonlinear cancellation;
- `C^2` viscous diffusion;
- curl chirality and the signed/absolute critical split;
- equal paired critical transfer;
- the Hodge spectral commutator law;
- the material Hodge conjugacy law;
- the critical transfer/dissipation common-kernel identity.

The apparent zoo has therefore reduced to one exact two-form, one self-contraction,
and the Hodge adjoint of the same differential.

**Classification: Rigorous operator-level synthesis of exact identities.**

---

## 16. The no-escape question after the reduction

The preceding milestone left an abstract cumulative paired-transfer obstruction

\[
\Theta(t)=\int_0^t\tau(s)\,ds.
\]

Section 9 now identifies it literally:

\[
\boxed{
\Theta(t)
=
\frac14
\int_0^t\iint
K_\Lambda(x,y)
\big(\omega(x,s)-\omega(y,s)\big)
\cdot
\big(u(x,s)\times u(y,s)\big)
\,dx\,dy\,ds.
}
\]

A critical escape would require this quantity to diverge to `+infinity`, while the
same vorticity increments are simultaneously charged by

\[
\frac\nu2
\int_0^t\iint
K_\Lambda(x,y)
|\omega(x,s)-\omega(y,s)|^2
\,dx\,dy\,ds.
\]

The open question is therefore no longer whether an arbitrary scalar transfer can be
bounded.  It is the literal PDE question

\[
\boxed{
\begin{gathered}
\text{Can the self-induced alternating current }
\iota_{\mathcal B\beta}\beta
\text{ maintain an infinite finite-time oriented correlation}\\
\text{with the exact vorticity increments that the adjoint-square current }
\nu\delta\beta
\text{ simultaneously dissipates?}
\end{gathered}
}
\]

Any true no-escape theorem at this level must exploit the fact that `u` in the
oriented factor is not independent data: it is the Hodge/Biot--Savart primitive of
the same exact `beta` whose increment appears in the dissipative square.

A generic Cauchy--Schwarz or Young inequality that forgets that self-generation is
therefore not the desired endpoint.  The missing law, if it exists, is a
**self-induced correlation/anti-concentration compatibility** of this one de Rham
current.

**Classification: Conjectural bridge / Open.**

No blow-up exclusion, restart, continuation, or global-regularity conclusion is
claimed.

---

## 17. Classification

**Exact identity**

- de Rham current law `beta_t+d(i_u beta+nu delta beta)=0`;
- beta-only Hodge/Biot--Savart closure on the fixed harmonic sector;
- projected momentum law `alpha_t+P i_u beta+nu delta beta=0`;
- three-dimensional skew-square form `alpha_t=R_beta alpha-nu C^2 alpha`;
- `R_beta^*=-R_beta` and `R_beta(C alpha)=0`;
- energy and nonlinear-helicity cancellations;
- vorticity equation as curl of the same sideways current;
- critical commutator with `Lambda=|C|`;
- positive fractional-Hodge pair-kernel representation;
- common-kernel critical transfer/dissipation identity and square completion.

**Rigorous consequence**

- pressure, stretching, helicity, chirality, material Hodge motion, and critical
  paired transfer are representations of the same skew-square/de Rham current core;
- positive critical growth requires oriented correlation of vorticity increments
  with velocity pairs in the same pair geometry used by critical viscosity;
- the cumulative `Theta` from the previous milestone is exactly the spacetime
  integral of this oriented increment current.

**Audited algebra referee**

- direct cross-product checks verify `i_u beta(u)=0`,
  `u cross omega=-(i_u beta)^sharp`, and orthogonality to both `u` and `omega`;
- an independent finite-Fourier calculation gives exactly
  `<alpha,[Lambda,R_beta]alpha>=2 (Kdot)_nl` and
  `tau=-int u.(omega_+ cross omega_-)` to roundoff;
- an independent finite symmetric-kernel algebra check gives exactly the pair
  commutator formula and the `1/2` increment-square coefficient.  These are factor
  and sign referees only, not a calibration campaign.

**Conjectural bridge / Open**

- a self-induced correlation/anti-concentration law strong enough to prevent
  `Theta -> +infinity` in finite time;
- no-escape/blow-up exclusion;
- restart/continuation;
- global regularity.
