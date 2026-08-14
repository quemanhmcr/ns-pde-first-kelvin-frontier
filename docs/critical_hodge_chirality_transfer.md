# Critical Hodge chirality transfer: the single signed-to-absolute obstruction

This note continues the compression programme after the self-Hodge conjugacy/Lax
law.  It does **not** introduce a new selector, score, packet family, or continuation
criterion.  The question is narrower and more intrinsic:

> once all natural Hodge geometry has been shown to move by one conjugacy law, what
> is the smallest operation by which the Navier--Stokes nonlinearity can still move
> a solution toward a genuinely critical escape?

The answer below identifies one exact obstruction at the velocity/Hodge-spectral
level.  On mean-zero divergence-free velocity fields in three dimensions,

\[
A:=-\Delta=\operatorname{curl}^2.
\]

The positive square root `|curl|=A^{1/2}` gives the canonical positive quadratic
quantity at the half-derivative level, while `curl` itself gives the signed helicity
at exactly the same differential order.  The Euler/nonlinear part of Navier--Stokes
is invisible to the signed helicity but not to the absolute value.  The difference
between those two statements is entirely the two-sign spectrum of the Hodge curl.

Equivalently: nonlinear critical growth is not arbitrary production.  It is exactly
paired transfer into the positive and negative curl-helicity sectors at equal signed
rates.  Viscosity is the only direct sink in each sector.

This is a compression theorem and a frontier correction.  It does **not** prove
that the paired transfer is bounded, integrable, or dominated by viscosity.  In
fact an amplitude-scaling no-go below shows why no universal instantaneous
domination of that kind can be the hidden no-escape law.

No blow-up exclusion, restart, continuation, or global-regularity theorem is
claimed.

---

## 1. Fixed-Hodge gauge and the exact skew-plus-positive split

Work on the flat three-torus and remove the conserved spatial mean velocity by a
Galilean choice.  Let

\[
\mathcal H
=
\{u\in L^2(\mathbb T^3;\mathbb R^3):\nabla\cdot u=0,\ \int u=0\}.
\]

Let `P` be the orthogonal Leray--Hodge projector onto `H` and define the positive
Stokes/Hodge operator

\[
A=-\Delta
\]

on this divergence-free mean-zero sector.  Since the Euclidean Laplacian preserves
`H`, no extra projection is needed in `A`.

For fixed divergence-free `u`, define the transport operator

\[
\mathcal T_u v
:=P((u\cdot\nabla)v).
\]

For divergence-free `v,w`, periodic integration by parts gives

\[
\langle\mathcal T_uv,w\rangle
=
-\langle v,\mathcal T_uw\rangle.
\]

Hence

\[
\boxed{\mathcal T_u^*=-\mathcal T_u.}
\]

The incompressible Navier--Stokes equation is exactly

\[
\boxed{
\partial_tu+\mathcal T_u u+\nu A u=0.
}
\]

Thus, in the fixed-Hodge gauge, the PDE has only two operator types:

\[
\boxed{
\text{self-generated skew transfer}
\quad+
\text{fixed positive Hodge diffusion}.
}
\]

Pressure is not missing.  The Leray--Hodge projection is exactly the constraint
operation that removes the gradient component and leaves the skew transport on the
incompressible tangent space.  This is the fixed-geometry representation of the
moving-Hodge projector law derived in the preceding milestone.

**Classification: Exact Leray/Hodge identity.**

---

## 2. One master spectral-transfer identity for every Hodge scale

Let `F` be any self-adjoint Hodge spectral operator on a smooth solution that
commutes with `A`.  This includes `F(A)`, spectral functions of `C=curl`, and the
canonical curl-sign projectors used below.  Define

\[
Q_F(t)=\frac12\langle u,F u\rangle.
\]

Using the equation and the skew-adjointness of `T_u`,

\[
\begin{aligned}
\dot Q_F
&=-\langle \mathcal T_u u,F u\rangle
-\nu\langle Au,F u\rangle\\
&=\frac12\langle u,[\mathcal T_u,F]u\rangle
-\nu\langle A^{1/2}u,F A^{1/2}u\rangle.
\end{aligned}
\]

Therefore

\[
\boxed{
\frac d{dt}\frac12\langle u,F u\rangle
=
\frac12\langle u,[\mathcal T_u,F]u\rangle
-
\nu\langle A^{1/2}u,F A^{1/2}u\rangle.
}
\]

This is the complete spectral production--transfer--dissipation law in one formula.
The nonlinear term is always a **commutator transfer**.  The viscous term is always
spectrally diagonal.

For `F=I`, the commutator vanishes and one obtains the ordinary kinetic-energy law.
For a spectral projector, the commutator is the exact exchange between that Hodge
spectral subspace and its complement.  No shell library is required: the identity
holds simultaneously for the entire functional calculus.

**Classification: Exact operator identity.**

---

## 3. Vortex stretching is spectral transfer, not an independent producer

Take `F=A`.  Then

\[
Q_A=\frac12\langle u,Au\rangle
=\frac12\|\omega\|_2^2.
\]

The master law gives

\[
\frac d{dt}\frac12\|\omega\|_2^2
=
\frac12\langle u,[\mathcal T_u,A]u\rangle
-
u\|Au\|_2^2.
\]

The standard vorticity identity gives

\[
\frac d{dt}\frac12\|\omega\|_2^2
=
\int\omega\cdot S\omega
-
u\|\nabla\omega\|_2^2.
\]

On the periodic divergence-free sector,

\[
\|Au\|_2^2=\|\nabla\omega\|_2^2.
\]

Hence

\[
\boxed{
\int\omega\cdot S\omega
=
\frac12\langle u,[\mathcal T_u,A]u\rangle.
}
\]

So vortex stretching is precisely the failure of the self-generated conservative
transport to commute with the Hodge frequency operator.  At kinetic-energy level
`F=I` the transfer is invisible; at enstrophy level `F=A` the same conservative
rearrangement appears as stretching production.

This is another reduction of mechanisms: stretching is the frequency-weighted
shadow of energy transfer.

**Classification: Exact identity / rigorous operator interpretation.**

---

## 4. Three-dimensional Hodge square root: `A=curl^2`

Now use the genuinely three-dimensional structure.  On `H`, let

\[
C:=\operatorname{curl}.
\]

For periodic divergence-free mean-zero vector fields, `C` is self-adjoint and

\[
\boxed{C^2=A=-\Delta.}
\]

Thus

\[
|C|=A^{1/2}.
\]

Since the zero mode has been removed, define the Hodge chirality involution

\[
J:=C|C|^{-1}.
\]

Then

\[
\boxed{
J^*=J,
\qquad
J^2=I,
\qquad
C=J|C|.
}
\]

The canonical chiral projectors are

\[
\boxed{
P_\pm=\frac12(I\pm J).
}
\]

This is not a Fourier-coordinate choice.  It is the sign decomposition of the
intrinsic Hodge curl operator.  Under the material Hodge conjugacy of the previous
milestone, `C`, `|C|`, `J`, and `P_±` are all carried by the same natural conjugacy
law.

**Classification: Exact three-dimensional Hodge identity.**

---

## 5. The missing half derivative is already present inside NS as signed helicity

Define the positive critical Hodge quadratic form

\[
\mathcal K
:=
\frac12\langle u,|C|u\rangle
=
\frac12\|A^{1/4}u\|_2^2.
\]

Under the standard Euclidean Navier--Stokes scaling, `H^{1/2}` is the invariant
velocity Sobolev order, so `K` lies exactly at the canonical half-derivative critical
level.  On the torus this statement should be read as differential/scaling order,
not as an exact torus dilation symmetry.

Now define the signed helicity quadratic

\[
\mathcal H
:=
\frac12\langle u,Cu\rangle
=
\frac12\int u\cdot\omega.
\]

Because `C=J|C|`, the only difference between these two quantities is the sign of
the curl spectrum:

\[
\boxed{
\mathcal H
=
\frac12\langle A^{1/4}u,J A^{1/4}u\rangle,
\qquad
\mathcal K
=
\frac12\|A^{1/4}u\|_2^2.
}
\]

Thus the Navier--Stokes nonlinearity already carries a **signed quadratic inviscid
invariant at exactly the same differential order as the positive critical size**.  The difficulty is not a
missing differential order.  It is the cancellation allowed by the two signs of
`J`.

**Classification: Exact Hodge identity; critical-order statement by the standard NS
scaling.**

---

## 6. Helicity sees no nonlinear production

Take `F=C` in the quadratic-form calculation.  The nonlinear helicity contribution
vanishes exactly.  Indeed

\[
(u\cdot\nabla)u
=
\omega\times u+\nabla\frac{|u|^2}{2},
\]

so

\[
\int (u\cdot\nabla u)\cdot\omega=0
\]

by orthogonality of `omega x u` to `omega` and `div omega=0` for the gradient term.
Therefore

\[
\boxed{
\frac12\langle u,[\mathcal T_u,C]u\rangle=0.
}
\]

The full helicity law is consequently

\[
\boxed{
\dot{\mathcal H}
=-\nu\langle Au,Cu\rangle
=-\nu\langle u,C^3u\rangle.
}
\]

The Euler/nonlinear part can transfer helicity among locations and frequencies, but
it cannot change the total signed critical quadratic.

**Classification: Exact helicity identity.**

---

## 7. Absolute critical size has exactly one nonlinear obstruction

Take instead `F=|C|`.  The master transfer law gives

\[
\boxed{
\dot{\mathcal K}
=
\frac12\langle u,[\mathcal T_u,|C|]u\rangle
-
\nu\langle u,|C|^3u\rangle.
}
\]

The viscous term is nonpositive and canonical:

\[
\langle u,|C|^3u\rangle
=\||C|^{3/2}u\|_2^2.
\]

Therefore every nonlinear increase of the positive critical Hodge size is contained
in the single commutator

\[
\boxed{
\frac12\langle u,[\mathcal T_u,|C|]u\rangle.
}
\]

Compare Sections 6 and 7:

\[
\boxed{
\text{nonlinearity is invisible to }C,
\qquad
\text{but not to }|C|.
}
\]

At this level, the entire three-dimensional critical obstruction is the
**signed-to-absolute Hodge defect** `C -> |C|`.

This statement does not give a sign or bound on the commutator.

**Classification: Exact identity / rigorous compression of the critical
obstruction.**

---

## 8. Exact paired-chirality law

Let

\[
u_\pm=P_\pm u
\]

and define the two nonnegative chiral critical contents

\[
\boxed{
\mathcal K_\pm
:=
\frac12\langle u_\pm,|C|u_\pm\rangle
\ge0.
}
\]

Then

\[
\boxed{
\mathcal K=\mathcal K_++\mathcal K_-,
\qquad
\mathcal H=\mathcal K_+-\mathcal K_-.
}
\]

Write the nonlinear contribution to each chiral content as

\[
\tau_\pm
:=-\langle\mathcal T_u u,|C|u_\pm\rangle.
\]

The viscous chiral dissipations are

\[
D_\pm
:=
\langle u_\pm,|C|^3u_\pm\rangle
\ge0.
\]

Since the nonlinear helicity rate is zero,

\[
0=(\dot{\mathcal H})_{\rm nl}=\tau_+-\tau_-.
\]

Hence

\[
\boxed{
\tau_+=\tau_-=:\tau.
}
\]

The exact chiral critical laws are therefore

\[
\boxed{
\begin{aligned}
\dot{\mathcal K}_+&=\tau-\nu D_+,\\
\dot{\mathcal K}_-&=\tau-\nu D_-.
\end{aligned}
}
\]

Equivalently,

\[
\boxed{
\dot{\mathcal K}
=2\tau-\nu(D_++D_-),
\qquad
\dot{\mathcal H}
=-\nu(D_+-D_-).
}
\]

This is the smallest exact critical transfer grammar visible here.

The nonlinear dynamics cannot increase one signed critical sector without making an
equal instantaneous contribution to the other signed sector at the level of the
global chiral quadratic contents.  Every nonlinear change of the positive critical
size is therefore **paired opposite-chirality transfer**.  Viscosity acts separately
and dissipatively on the two positive sectors.

The word `paired` describes this exact global quadratic law; it does not assert a
local vortex-pair creation event or a topological reconnection mechanism.

**Classification: Exact consequence of helicity cancellation and the canonical curl
sign decomposition.**

---

## 9. Homochiral transfer is invisible to the critical positive quadratic

The preceding law has a useful exact interpretation.  If a nonlinear interaction is
confined to a single curl-sign sector, then on that sector

\[
C=\pm|C|.
\]

For an isolated interaction whose nonlinear energy/helicity exchange closes inside
that one sign sector, conservation of signed helicity is exactly conservation of the
positive critical quadratic on that interaction.

At Fourier-triad level this means an isolated triad carrying one common helicity
sign has zero nonlinear change of `K`; a triad containing both signs can have a
nonzero `K` transfer while still conserving both total energy and signed helicity.

A lightweight exact finite-Fourier convolution referee on the triad

\[
(1,0,0)+(1,1,0)+(-2,-1,0)=0
\]

checks this distinction.  Same-sign helical choices give nonlinear energy,
helicity, and `K` rates zero to roundoff.  Mixed-sign choices give zero nonlinear
energy and helicity rates while `K` is nonzero, with the positive and negative
chiral `K` rates equal to roundoff.  This computation is only an algebra referee;
the operator identities in Sections 1--8 are the theorem.

**Classification: Rigorous one-sign consequence; audited heterochiral finite-mode
referee.**

---

## 10. Why an instantaneous `transfer <= viscosity` theorem cannot be the hidden law

The paired-transfer law also kills a tempting false route.

For any smooth divergence-free state `u` with nonzero nonlinear critical transfer,
scale only its amplitude:

\[
u\mapsto a u.
\]

Then

\[
\mathcal T_{au}(au)=a^2\mathcal T_u u,
\]

so the critical nonlinear transfer scales cubically:

\[
\tau(au)=a^3\tau(u).
\]

The viscous critical dissipation scales quadratically:

\[
D_\pm(au)=a^2D_\pm(u).
\]

Therefore, whenever a state has `tau>0`, sufficiently large amplitude makes the
instantaneous nonlinear critical feeding dominate any fixed-`nu` quadratic viscous
sink at that snapshot.

Thus the hidden no-escape mechanism, if it exists, cannot be a universal pointwise
inequality of the form

\[
2\tau\le \nu(D_++D_-)
\]

for all smooth states.

Mixed-helicity finite Fourier triads provide audited smooth periodic states with
both signs of nonzero `tau` (and `u -> -u` flips its sign), so the obstruction is
literal rather than formal.

The conclusion is methodological and important:

\[
\boxed{
\text{no-escape, if true, must be a dynamic/causal compatibility law, not a
snapshot domination estimate.}
}
\]

**Classification: Exact amplitude-scaling obstruction conditional on nonzero
transfer; audited periodic finite-mode witness for nonzero transfer.**

---

## 11. The cumulative paired-transfer law is an exact causal bank

The instantaneous rate `tau` has no favorable universal sign, but its time integral
has an exact two-sector meaning that does not require any invented storage variable.
Define

\[
\Theta(t):=\int_0^t\tau(s)\,ds.
\]

Integrating the two exact chiral laws gives simultaneously

\[
\boxed{
\Theta(t)
=
\mathcal K_+(t)-\mathcal K_+(0)
+
\nu\int_0^tD_+(s)\,ds
}
\]

and

\[
\boxed{
\Theta(t)
=
\mathcal K_-(t)-\mathcal K_-(0)
+
\nu\int_0^tD_-(s)\,ds.
}
\]

Thus the same cumulative nonlinear transfer is resolved in **both** chirality
sectors into only two literal fates:

\[
\boxed{
\text{stored positive critical content}
+
\text{viscously dissipated positive critical content}.
}
\]

Equivalently, the compensated quantities

\[
\mathcal B_\pm(t)
:=
\mathcal K_\pm(t)+\nu\int_0^tD_\pm(s)\,ds
\]

obey

\[
\boxed{
\dot{\mathcal B}_+=\dot{\mathcal B}_-=\tau,
\qquad
\mathcal B_+(t)-\mathcal B_-(t)
=
\mathcal H(0).
}
\]

`B_±` are not promoted as new primitive state variables; they are just the integrated
form of the exact PDE balance.  The point is the common causal accounting.

In particular, if the positive critical size `K` diverges along a finite-time
sequence, then

\[
\boxed{
\Theta(t)\to+\infty
}
\]

along that escape sequence.  Moreover, in the opposite chirality sector that same
infinite cumulative transfer must appear either as unbounded stored `K_-` (or
`K_+`, depending on the escaping sign) or as unbounded accumulated critical
viscous dissipation.

So a one-sign isolated critical escape is impossible at the level of the exact
causal balance: the opposite sign must participate through storage or dissipation,
even if it does not itself remain large at the terminal time.

**Classification: Exact integrated consequence / rigorous necessary condition for
critical escape.**

---

## 12. Energy already limits how long large critical content can persist

The ordinary energy law gives one further intrinsic restriction, although it does
not close no-escape.  Let

\[
E=\frac12\|u\|_2^2,
\qquad
Z=\frac12\|Cu\|_2^2.
\]

By spectral Cauchy--Schwarz,

\[
\mathcal K
=\frac12\langle u,|C|u\rangle
\le
\frac12\|u\|_2\|Cu\|_2
=
\sqrt{EZ}.
\]

Hence

\[
\boxed{\mathcal K^2\le EZ.}
\]

Since

\[
\dot E=-2\nu Z,
\]

one obtains on every smooth interval

\[
\boxed{
\int_0^T\mathcal K(t)^2\,dt
\le
\frac{E(0)^2}{2\nu}.
}
\]

This is the standard energy interpolation written at the exact Hodge-critical
order.  It is not claimed as a new regularity estimate.  Its role here is to type
the remaining escape geometry:

- positive critical content cannot remain arbitrarily large for an order-one amount
  of time while the energy stays finite;
- but `L^2_t` control still allows concentration into shorter and shorter time
  windows;
- therefore the divergence of the cumulative paired-transfer `Theta` required by
  Section 11 would have to occur through increasingly concentrated transfer and/or
  critical dissipation.

This is why the next missing theorem is genuinely causal.  Neither a snapshot bound
nor the ordinary energy interpolation excludes the required concentration.

**Classification: Rigorous consequence of the exact energy law; not a no-escape
estimate.**

---

## 13. Relation to the previous Hodge-conjugacy theorem

Nothing in this note adds an independent spectral architecture.

The operators

\[
C_G=*_{G}d,
\qquad
|C_G|=(-\Delta_G)^{1/2},
\qquad
J_G=C_G|C_G|^{-1},
\qquad
P_{G,\pm}=\frac12(I\pm J_G)
\]

on the co-closed nonharmonic one-form sector are all natural Hodge functional-calculus
objects.  Hence the previous conjugacy theorem already forces

\[
A_{G_t}=T_tA_{g_0}T_t^{-1}
\]

for each of them.

The present theorem simply chooses the fixed-Hodge/Eulerian gauge to expose what the
self-generated transport does **relative to that already-fixed Hodge spectrum**.
The material and Eulerian descriptions are two representations of the same law.

The prior mechanisms now descend as follows:

- pressure: the Leray/Hodge constraint needed for skew transport on `H`;
- stretching: the `F=A` spectral commutator;
- energy cascade: the `F`-commutator for arbitrary Hodge spectral multipliers;
- viscosity/Kelvin carré-du-champ: the positive `A=C^2` sector;
- material Hodge motion: the conjugate representation of the same fixed spectral
  calculus;
- critical three-dimensional obstruction: replacing signed `C` by positive `|C|`.

**Classification: Rigorous synthesis of exact identities.**

---

## 14. What has actually been reduced

The previous frontier said that a singularity would have to be an unbounded
self-generated conjugacy distortion while the intrinsic Hodge spectrum stays fixed.
This note identifies the spectral operation capable of feeding that distortion at
the canonical critical differential order.

The irreducible chain is now

\[
\boxed{
\begin{gathered}
\text{self-generated skew Hodge transfer }\mathcal T_u\\
\Downarrow\\
\text{signed critical helicity unchanged nonlinearly}\\
\Downarrow\\
\text{positive critical size can change only through equal }(+/-)\text{ transfer}\\
\Downarrow\\
\text{viscosity dissipates both chiral critical sectors through }|C|^3.
\end{gathered}
}
\]

Thus the full critical difficulty is no longer an unspecified collection of
stretching, pressure, deformation, localization, or Kelvin mechanisms.  At this
level it is one scalar global transfer rate `tau`, generated by the same skew
nonlinearity that preserves energy and signed helicity.

This is a strong compression.  It is not a bound on `tau`.

---

## 15. The next literal no-escape question

A genuine singular escape would have to exploit the only remaining critical freedom:
it would have to make the cumulative paired transfer `Theta` diverge positively in
finite time, while the same transfer is simultaneously accounted for in both
chirality sectors as stored critical content or `|C|^3` viscous dissipation.  The
ordinary energy law further forces this process into increasingly concentrated time
windows if the critical size becomes unbounded.

The next question is therefore not

> can stretching be bounded by dissipation at each time?

That route is ruled out by Section 10.

The sharper question is

\[
\boxed{
\begin{gathered}
\text{Can the self-generated skew transport sustain an infinite finite-time}\
\text{cascade of equal opposite-chirality critical content while the same}\
\text{Hodge operator that defines chirality supplies the quadratic viscous square }C^2?
\end{gathered}
}
\]

Equivalently: what exact **dynamic compatibility** constrains the cumulative paired
transfer `tau` when `T_u` is generated by the same velocity whose signed critical
helicity it cannot change?

If a no-escape theorem exists at this level, it must use that self-generation and
causal accumulation.  It cannot be obtained by declaring `tau` small or by inserting
an external threshold.

**Classification: Conjectural bridge / Open.**

No no-escape, continuation, restart, or global-regularity theorem is claimed.

---

## 16. Classification

**Exact identity**

- Leray/Hodge split `u_t+T_u u+nu A u=0` with `T_u^*=-T_u`.
- universal spectral commutator law for `F(A)`.
- stretching as the `F=A` commutator.
- three-dimensional Hodge square `A=C^2`.
- chirality involution/projectors and signed/absolute critical split.
- nonlinear helicity cancellation.
- paired chiral critical laws `Kdot_+=tau-nu D_+`,
  `Kdot_-=tau-nu D_-`.

**Rigorous consequence**

- all nonlinear positive-critical growth is paired opposite-sign helicity transfer in
  the canonical global curl decomposition.
- on a one-sign closed interaction, signed helicity and positive critical content
  coincide up to sign, so nonlinear critical production vanishes there.
- the previous pressure/stretching/Hodge-conjugacy descriptions are representations
  of the same skew-transfer / Hodge-square structure.

**Audited calibration**

- finite Fourier helical triads verify zero nonlinear energy/helicity rates;
  same-sign triads have zero critical transfer, while mixed-sign triads can have
  nonzero critical transfer with equal `+/-` rates.

**Rigorous no-go / audited witness**

- nonlinear critical transfer scales as amplitude cubed while viscous critical
  dissipation scales as amplitude squared; a mixed-helicity finite-mode witness has
  nonzero transfer.  Hence no universal instantaneous transfer-below-dissipation
  inequality can be the hidden mechanism.

**Conjectural bridge**

- a true no-escape law may constrain the *cumulative causal paired-helicity transfer*
  generated by the self-consistent velocity, rather than any instantaneous rate.

**Open**

- such a dynamic paired-transfer constraint;
- blow-up exclusion;
- restart/continuation;
- global regularity.

---

## Follow-through: chirality descends from the de Rham skew-square current

The next reduction is recorded in `docs/derham_skew_square_critical_current.md`.
The scalar paired transfer introduced here is no longer primitive.  With
`alpha=u^flat`, `beta=d alpha`, and `C=*d`, literal NS is

\[
\partial_t\beta+d(\iota_u\beta+\nu\delta\beta)=0,
\]

or, on co-closed one-forms,

\[
\partial_t\alpha=\mathcal R_\beta\alpha-\nu C^2\alpha,
\qquad
\mathcal R_\beta^*=-\mathcal R_\beta,
\qquad
\mathcal R_\beta(C\alpha)=0.
\]

The chirality split in this note is the sign decomposition of that same first-order
operator `C`.  More sharply,

\[
\boxed{
\tau=-\int u\cdot(\omega_+\times\omega_-)\,dx
=\frac14\iint K_{|C|}(x,y)
(\omega(x)-\omega(y))\cdot(u(x)\times u(y))\,dx\,dy.
}
\]

Thus heterochiral mixing and the oriented critical vorticity-increment current are
two exact representations of the same original NS transfer.  Critical viscosity is
`(1/2) doubleint K_|C| |delta omega|^2` on the identical positive kernel.  The open
bridge is therefore a self-induced signed correlation/anti-concentration law, not a
new chirality bank or shell architecture.  No no-escape or regularity claim follows.

---

## Postscript: chirality transfer is one determinant face of a whole-family law

A later signed-curl spectral reduction shows that the paired critical law is the
`F(c)=|c|` instance of the universal determinant

\[
\mathfrak D_F(c,d,r)
=\det\begin{pmatrix}1&1&1\\c&d&r\\F(c)&F(d)&F(r)\end{pmatrix}
\]

paired with the same fully alternating spectral three-current for every Hodge
quadratic.  Since `|c|` is affine on each chirality half-line, homochiral triples have
zero critical determinant identically.  Energy `F=1`, helicity `F=c`, stretching
`F=c^2`, and heat-scale flux `F=e^{-hc^2}` are other readouts of the same law rather
than separate mechanisms.  See
`docs/signed_curl_alternating_three_current_master.md`.

**Classification: Exact architecture compression.**
