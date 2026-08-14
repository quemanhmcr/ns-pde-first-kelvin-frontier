# Signed-curl alternating three-current master law

## Purpose

The recent heat-scale continuity theorem compressed kinetic energy, enstrophy,
vortex stretching, critical paired-chirality transfer, and critical viscous loss into
one positive heat-age density `rho(h,t)` and one nonlinear heat flux `Pi(h,t)`.
That is already much smaller than a shell-by-shell or mechanism-by-mechanism
architecture.

This note asks one level deeper whether the heat-age law itself is the primitive.
It is not.

On the mean-zero divergence-free three-torus, the self-adjoint Hodge curl operator

\[
C=\operatorname{curl}
\]

has a canonical **signed** spectral resolution.  Navier--Stokes assigns positive
energy to those signed curl eigenspaces, while its nonlinear Lamb rotation generates
one fully alternating three-index current.  Every quadratic Hodge spectral balance
is obtained by pairing that same three-current with one three-point determinant of
the chosen spectral weight.

The resulting master formula has no shell partition, no chosen scale ratio, no
selector, and no phenomenological cascade model.  It is the literal spectral
exterior algebra of

\[
\partial_t u=\mathcal R_\beta u-\nu C^2u,
\qquad
\mathcal R_\beta^*=-\mathcal R_\beta,
\qquad
\mathcal R_\beta(Cu)=0.
\]

Its main consequences are:

- kinetic energy and Euler helicity vanish nonlinearly **on every signed-curl
  spectral triple**, because affine spectral weights have zero determinant;
- vortex stretching is the quadratic/Vandermonde face of the same determinant law;
- positive critical `H^(1/2)` growth is the `F(c)=|c|` face, so it can occur only
  through mixed curl signs because `|c|` is affine on each chirality half-line;
- the canonical heat-scale continuity law is the Laplace transform of this same
  signed-curl current;
- the positive heat-age density is not an arbitrary positive profile: it belongs to
  the completely monotone/Bernstein cone forced by the positive Hodge spectral
  measure;
- Fourier support supplies an exact triangle/no-teleportation law for the same
  three-current.

No no-escape, blow-up exclusion, restart, continuation, or global-regularity theorem
is claimed.

Throughout, all identities are stated on a smooth interval.  Smoothness makes all
spectral sums absolutely convergent after the harmless rearrangements used below.
The conserved mean/harmonic velocity mode is removed by the same Galilean choice as
in the preceding milestones.

---

## 1. Signed Hodge-curl spectral blocks

Let

\[
\mathcal H
=
\left\{
 u\in L^2(\mathbb T^3;\mathbb R^3):
 \nabla\cdot u=0,
 \ \int_{\mathbb T^3}u=0
\right\}.
\]

On `H`, the Euclidean curl operator

\[
C=\operatorname{curl}
\]

is self-adjoint and

\[
C^2=A=-\Delta.
\]

Its nonzero spectrum on the flat torus is discrete.  Denote the signed curl
eigenvalues by

\[
c\in\Sigma_C\subset\mathbb R\setminus\{0\},
\]

and the corresponding orthogonal spectral projectors by `P_c`.  Write

\[
\boxed{
 u_c:=P_cu,
 \qquad
 Cu_c=c\,u_c,
 \qquad
 u=\sum_{c\in\Sigma_C}u_c.
}
\]

Define the positive energy atom

\[
\boxed{
 e_c(t):=\frac12\|u_c(t)\|_2^2\ge0.
}
\]

Then

\[
\frac12\|u\|_2^2=\sum_c e_c,
\qquad
\frac12\langle u,Cu\rangle=\sum_c c\,e_c,
\qquad
\frac12\langle u,|C|u\rangle=\sum_c |c|\,e_c.
\]

Thus energy, signed helicity, and positive critical content are not three state
variables.  They are three moments of the same positive energy measure on the
canonical signed curl spectrum.

**Classification: Exact Hodge spectral decomposition.**

---

## 2. The nonlinear spectral transfer is one fully alternating three-current

The preceding de Rham/skew-square theorem wrote the projected velocity equation as

\[
\boxed{
\partial_tu
=\mathcal R_\beta u-\nu C^2u,
}
\]

where

\[
(\mathcal R_\beta v)^\sharp
=P(v^\sharp\times\omega),
\qquad
\omega=Cu,
\]

and

\[
\mathcal R_\beta^*=-\mathcal R_\beta,
\qquad
\mathcal R_\beta(Cu)=0.
\]

For signed curl blocks define

\[
\boxed{
\mathscr T_{cdr}
:=
\int_{\mathbb T^3}
 u_c\cdot(u_d\times u_r)\,dx.
}
\]

The scalar triple product is fully alternating, hence

\[
\boxed{
\mathscr T_{cdr}
=\operatorname{sgn}(\sigma)
\mathscr T_{\sigma(cdr)}
}
\]

for every permutation `sigma`, and `T_cdr=0` whenever two spectral labels coincide.

Because

\[
\omega=Cu=\sum_r r\,u_r,
\]

the nonlinear pair current between curl blocks is

\[
\begin{aligned}
\mathscr J_{cd}
&:=\langle u_c,\mathcal R_\beta u_d\rangle\\
&=\int u_c\cdot(u_d\times\omega)\,dx\\
&=\sum_r r\,\mathscr T_{cdr}.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathscr J=\iota_{\,c}\mathscr T
\quad\text{in the literal sense}\quad
\mathscr J_{cd}=\sum_r r\,\mathscr T_{cdr}.
}
\]

The nonlinear two-current is the contraction of one fully alternating three-current
with the signed curl coordinate itself.  Neither `T` nor `J` is promoted as an
independent state: both are exact instantaneous readouts of the same physical
velocity/vorticity field.

This is the spectral image of the physical alternating law

\[
\iota_\omega\iota_\omega\mathrm{vol}=0.
\]

Nothing has been added to Navier--Stokes: `T` is the orthogonal signed-curl spectral
resolution of the original Lamb scalar triple product.

**Classification: Exact signed-curl three-current identity.**

---

## 3. Skew current and blockwise curl-weighted nullity

Full alternation immediately gives

\[
\boxed{
\mathscr J_{cd}=-\mathscr J_{dc}.
}
\]

More strongly, for every fixed output curl block `c`,

\[
\begin{aligned}
\sum_d d\,\mathscr J_{cd}
&=\sum_{d,r}dr\,\mathscr T_{cdr}\\
&=0,
\end{aligned}
\]

because `dr` is symmetric in `(d,r)` while `T_cdr` is antisymmetric.  Thus

\[
\boxed{
\sum_d d\,\mathscr J_{cd}=0
\qquad\text{for every }c.
}
\]

Equivalently, directly from the PDE null vector,

\[
\sum_d d\,\mathscr J_{cd}
=
\langle u_c,\mathcal R_\beta(Cu)\rangle
=0.
\]

Skewness gives the column version as well:

\[
\boxed{
\sum_c c\,\mathscr J_{cd}=0
\qquad\text{for every }d.
}
\]

This is stronger than the single global statement that nonlinear helicity production
vanishes.  The curl-weighted cancellation already holds block by block in the
canonical signed spectrum.

**Classification: Exact blockwise spectral nullity.**

---

## 4. Positive spectral energy obeys one exact current law

Project Navier--Stokes onto the `c` curl eigenspace.  Since `C^2u_c=c^2u_c`,

\[
\begin{aligned}
\dot e_c
&=\langle u_c,\partial_tu_c\rangle\\
&=\sum_d\mathscr J_{cd}-\nu c^2\|u_c\|_2^2.
\end{aligned}
\]

Hence

\[
\boxed{
\dot e_c
=\sum_d\mathscr J_{cd}
-2\nu c^2e_c.
}
\]

This is the smallest positive **spectral readout law** currently visible:

\[
\boxed{
\text{positive signed-curl energy atoms}
\quad+
\text{one antisymmetric self-generated current}
\quad-
\text{diagonal }c^2\text{ killing}.
}
\]

The current is not a Markov jump rate and no positivity is assigned to `J_cd`; its
sign is physical transfer orientation.  Positivity belongs to the actual energy
atoms `e_c`.

**Classification: Exact spectral energy-current law.**

For later use, the nonlinear part of any spectral quadratic already has the exact
two-current weak form

\[
\boxed{
(\dot Q_F)_{\rm nl}
=\frac12\sum_{c,d}
\bigl(F(c)-F(d)\bigr)\mathscr J_{cd}.
}
\]

Thus `J` is literally the single signed transport current seen by the whole spectral
functional calculus.  Section 5 resolves this two-current one level deeper into the
fully alternating three-current `T`.

**Classification: Exact weak spectral-current identity.**

---

## 5. One determinant generates every Hodge spectral quadratic balance

Let `F` be any real spectral weight for which the following smooth-solution sums are
finite, and define

\[
\boxed{
Q_F
:=\frac12\langle u,F(C)u\rangle
=\sum_c F(c)e_c.
}
\]

The nonlinear part is

\[
(\dot Q_F)_{\rm nl}
=\sum_{c,d,r}F(c)\,r\,\mathscr T_{cdr}.
\]

Because `T` is fully alternating, only the fully alternating part of the coefficient
`F(c)r` survives.  Define the canonical three-point determinant

\[
\boxed{
\mathfrak D_F(c,d,r)
:=
\det
\begin{pmatrix}
1&1&1\\
c&d&r\\
F(c)&F(d)&F(r)
\end{pmatrix}.
}
\]

Explicitly,

\[
\boxed{
\mathfrak D_F(c,d,r)
=(r-d)F(c)+(c-r)F(d)+(d-c)F(r).
}
\]

Then

\[
\boxed{
(\dot Q_F)_{\rm nl}
=\frac16
\sum_{c,d,r}
\mathfrak D_F(c,d,r)\,
\mathscr T_{cdr}.
}
\]

Including viscosity gives the universal law

\[
\boxed{
\dot Q_F
=\frac16\sum_{c,d,r}
\mathfrak D_F(c,d,r)\mathscr T_{cdr}
-2\nu\sum_c c^2F(c)e_c.
}
\]

For distinct `c,d,r`, the determinant is the Vandermonde factor times the second
divided difference:

\[
\boxed{
\mathfrak D_F(c,d,r)
=(c-d)(d-r)(r-c)\,F[c,d,r].
}
\]

Thus the Navier--Stokes nonlinearity does not see an arbitrary collection of
spectral observables.  At quadratic level it sees only the **second spectral
curvature** of the chosen Hodge weight, paired against one alternating three-current.

This is the principal whole-family compression of the note.

**Classification: Exact master determinant/divided-difference identity.**

---

## 6. Energy and helicity are universal affine null directions of the master transfer

If

\[
F(c)=a+bc
\]

is affine in the signed curl eigenvalue, the third row of the determinant is a
linear combination of the first two rows.  Therefore

\[
\boxed{
\mathfrak D_F(c,d,r)=0
\quad\text{for every spectral triple}.
}
\]

Two special choices are:

\[
F(c)=1
\]

for kinetic energy, and

\[
F(c)=c
\]

for signed helicity.  Hence their nonlinear cancellation occurs **triple by triple**:

\[
\boxed{
(\dot E)_{\rm nl}=0,
\qquad
(\dot H)_{\rm nl}=0.
}
\]

Energy and Euler-helicity conservation are therefore not two unrelated invariants.
They are the two basis elements of the **universal affine family** annihilated
triplewise by the spectral exterior-curvature law.  A particular state may of course
have additional accidental cancellations.

This is the signed-curl spectral version of the earlier physical statement that both
cancellations descend from the same alternating vorticity-form contraction.

**Classification: Exact triplewise energy/helicity cancellation.**

---

## 7. Vortex stretching is the Vandermonde face

Take

\[
F(c)=c^2.
\]

Then

\[
Q_F
=\frac12\langle u,C^2u\rangle
=\frac12\|\omega\|_2^2
=:Z.
\]

Because the second divided difference of `c^2` is exactly one,

\[
\boxed{
\mathfrak D_{c^2}(c,d,r)
=(c-d)(d-r)(r-c).
}
\]

Therefore the nonlinear enstrophy production is

\[
\boxed{
\int\omega\cdot S\omega\,dx
=\frac16\sum_{c,d,r}
(c-d)(d-r)(r-c)\,
\mathscr T_{cdr}.
}
\]

So stretching is not a new local producer below the master law.  It is the
quadratic/Vandermonde spectral-curvature readout of the same alternating current.

**Classification: Exact spectral stretching identity.**

---

## 8. Critical transfer is the kink-curvature face

Take

\[
F(c)=|c|.
\]

Then

\[
Q_F
=\frac12\langle u,|C|u\rangle
=\mathcal K,
\]

the canonical positive critical quadratic.

On either chirality half-line separately, `|c|` is affine:

\[
|c|=c\quad(c>0),
\qquad
|c|=-c\quad(c<0).
\]

Therefore

\[
\boxed{
\mathfrak D_{|\cdot|}(c,d,r)=0
\quad\text{whenever }c,d,r\text{ have one common sign}.
}
\]

Hence critical nonlinear production is **supported only on heterochiral
spectral triples**.  Mixed-sign triples may still vanish by further geometric or
amplitude cancellation.  The preceding paired-chirality theorem is not a separate mechanism; it is
the fact that the absolute-value spectral weight has only one non-affine feature:
the kink at curl sign zero.

If, for example,

\[
c>0,\qquad d>0,\qquad r<0,
\]

then direct evaluation gives

\[
\boxed{
\mathfrak D_{|\cdot|}(c,d,r)
=2r(c-d).
}
\]

The other sign pattern is obtained by cyclic permutation.  Since

\[
(\dot{\mathcal K})_{\rm nl}=2\tau,
\]

one has

\[
\boxed{
2\tau
=\frac16\sum_{c,d,r}
\mathfrak D_{|\cdot|}(c,d,r)\mathscr T_{cdr}.
}
\]

This determinant law also explains the earlier finite-mode referee in which a mixed
helicity triad with two equal curl magnitudes had zero critical transfer: the
same-sign spectral difference `c-d` vanishes.

**Classification: Exact heterochiral determinant/null identity.**

---

## 9. Fourier support gives an exact triangle/no-teleportation law

The signed curl eigenspaces are helical Fourier eigenspaces.  Every Fourier mode in
`u_c` has wavevector `k` with

\[
|k|=|c|,
\]

and analogous statements hold for `u_d,u_r`.

A spatial integral contributing to

\[
\mathscr T_{cdr}
=\int u_c\cdot(u_d\times u_r)
\]

is nonzero only when its underlying Fourier wavevectors satisfy

\[
k+p+q=0.
\]

Consequently

\[
\boxed{
\mathscr T_{cdr}\ne0
\quad\Longrightarrow\quad
\begin{aligned}
|c|&\le |d|+|r|,\\
|d|&\le |r|+|c|,\\
|r|&\le |c|+|d|.
\end{aligned}
}
\]

Equivalently,

\[
\boxed{
\big||c|-|d|\big|\le |r|
}
\]

and its cyclic versions.

Thus the quadratic nonlinearity cannot teleport energy from two bounded curl
frequencies directly into one arbitrarily larger curl frequency.  A high-frequency
output requires at least one comparably high-frequency companion in the same exact
spectral triple.

This is a support theorem, not a quantitative bound on the amplitude of the current.
It does not exclude a Zeno cascade through an infinite chain of successively finer
triangles.

**Classification: Exact Fourier-support consequence of the canonical curl spectral
resolution.**

---

## 10. Heterochiral high--high--low transfer has an additional null factor

Consider a nonzero mixed-sign triple with

\[
c,d>0,
\qquad
r<0.
\]

Section 8 gives

\[
|\mathfrak D_{|\cdot|}|
=2|r|\,|c-d|.
\]

The Fourier triangle support of Section 9 gives

\[
|c-d|\le|r|.
\]

Therefore

\[
\boxed{
|\mathfrak D_{|\cdot|}(c,d,r)|
\le2|r|^2.
}
\]

In words: if the lone opposite-chirality leg is low frequency while the two
same-sign legs are high and nearly cancelling in wavevector magnitude, the critical
spectral coefficient is controlled by the **square of the low opposite-sign
frequency**, not by the high frequency squared.

The same statement holds after cyclic relabeling when the lone chirality sign is on
another leg.

This is an exact symbol-level null gain.  It is not a transfer-versus-viscosity
estimate because the alternating amplitude `T_cdr` remains cubic and uncontrolled
by this coefficient identity alone.  The amplitude-scaling no-go from the preceding
milestone therefore remains fully active.

**Classification: Rigorous heterochiral triangle-null consequence.**

---

## 11. The heat-age state is the Laplace shadow of the same spectral law

The canonical heat-resolved energy from the preceding milestone is

\[
\mathcal E(h,t)
=\frac12\langle u,e^{-hC^2}u\rangle.
\]

In signed curl blocks,

\[
\boxed{
\mathcal E(h,t)
=\sum_c e^{-hc^2}e_c(t).
}
\]

Its positive density is

\[
\boxed{
\rho(h,t)
=-\partial_h\mathcal E
=\sum_c c^2e^{-hc^2}e_c(t).
}
\]

The nonlinear heat flux

\[
\Pi(h,t)
=-\langle\mathcal R_\beta u,e^{-hC^2}u\rangle
\]

is correspondingly

\[
\boxed{
\Pi(h,t)
=-\frac12\sum_{c,d}
\bigl(e^{-hc^2}-e^{-hd^2}\bigr)
\mathscr J_{cd}.
}
\]

Equivalently, by the master determinant law with

\[
F_h(c)=e^{-hc^2},
\]

\[
\boxed{
\Pi(h,t)
=-\frac16\sum_{c,d,r}
\mathfrak D_{F_h}(c,d,r)\mathscr T_{cdr}.
}
\]

Applying the Laplace weight `e^{-hc^2}` to the exact block energy law

\[
\dot e_c=\sum_d\mathscr J_{cd}-2\nu c^2e_c
\]

gives exactly

\[
\boxed{
\partial_t\rho
-\partial_h(2\nu\rho+\Pi)=0.
}
\]

Thus the one-dimensional heat-age continuity theorem is not a separate scale
mechanism.  It is the Laplace-functional-calculus image of the signed-curl spectral
energy/current law.

**Classification: Exact spectral-to-heat conjugate representation.**

---

## 12. The positive heat profile lies in a completely monotone cone

The previous heat-age frontier retained only

\[
\rho(h,t)\ge0.
\]

The actual Navier--Stokes state satisfies much more.  For every integer `m>=0`,

\[
\boxed{
(-1)^m\partial_h^m\rho(h,t)
=\sum_c c^{2m+2}e^{-hc^2}e_c(t)
\ge0.
}
\]

Hence, at every smooth physical time,

\[
\boxed{
\rho(\cdot,t)\text{ is completely monotone on }(0,\infty).
}
\]

Equivalently, if the positive unsigned Hodge energy measure is

\[
\mu_t
:=\sum_c e_c(t)\,\delta_{c^2},
\]

then

\[
\boxed{
\mathcal E(h,t)=\int_0^\infty e^{-ha}\,d\mu_t(a),
\qquad
\rho(h,t)=\int_0^\infty a e^{-ha}\,d\mu_t(a).
}
\]

So the heat-age state is a Laplace transform of a positive spectral measure, not an
arbitrary positive half-line density.

In particular `rho` is decreasing and log-convex:

\[
\boxed{
\partial_h\rho\le0,
\qquad
\rho\,\partial_h^2\rho-(\partial_h\rho)^2\ge0.
}
\]

Define, wherever `rho>0`, the canonical heat-age spectral barycenter

\[
\boxed{
\kappa(h,t)
:=-\partial_h\log\rho(h,t).
}
\]

With the probability measure

\[
d\pi_{h,t}(a)
:=\frac{a e^{-ha}}{\rho(h,t)}\,d\mu_t(a),
\]

one has

\[
\boxed{
\kappa(h,t)=\mathbb E_{\pi_{h,t}}a,
\qquad
\partial_h\kappa(h,t)
=-\operatorname{Var}_{\pi_{h,t}}(a)
\le0.
}
\]

Thus increasing heat age moves the canonical spectral barycenter monotonically
toward lower Hodge frequencies at a rate equal to its own spectral variance.

This is a universal shape law for **every** smooth Navier--Stokes heat profile.

**Classification: Exact positive spectral-measure / complete-monotonicity identity.**

---

## 13. Boundary-layer mass is a Bernstein function, and the critical law is its time derivative

Define the actual heat-boundary mass

\[
\boxed{
M(h,t)
:=\int_0^h\rho(s,t)\,ds
=\mathcal E(0,t)-\mathcal E(h,t).
}
\]

Spectrally,

\[
\boxed{
M(h,t)
=\sum_c\bigl(1-e^{-hc^2}\bigr)e_c(t).
}
\]

Since `M_h=rho` is completely monotone, `M` is a Bernstein function of heat age:

\[
M\ge0,
\qquad
M_h\ge0,
\qquad
M_{hh}\le0,
\]

with the full alternating derivative hierarchy inherited from `rho`.

Integrating the heat-scale continuity equation from `0` to `h` and using `Pi(0)=0`
gives

\[
\boxed{
\partial_tM(h,t)
=\Pi(h,t)
-2\nu\bigl(\rho(0,t)-\rho(h,t)\bigr).
}
\]

But the critical quadratic has the exact boundary-mass representation

\[
\boxed{
\mathcal K(t)
=\frac1{2\sqrt\pi}
\int_0^\infty h^{-3/2}M(h,t)\,dh.
}
\]

Therefore its complete evolution is simply

\[
\boxed{
\dot{\mathcal K}(t)
=\frac1{2\sqrt\pi}
\int_0^\infty h^{-3/2}\partial_tM(h,t)\,dh.
}
\]

The earlier critical formula

\[
\Pi(h)-2\nu(\rho(0)-\rho(h))
\]

is thus not a third nonlinear-versus-viscous mechanism.  It is exactly the time
velocity of the canonical Bernstein boundary mass.

**Classification: Exact Bernstein boundary-mass identity / rigorous mechanism
compression.**

---

## 14. Whole-quadratic exhaustion no-go: the positive spectral state does not close the current

The determinant theorem also gives a strict stopping rule against searching for one
more quadratic Hodge observable.

Apply the instantaneous state reversal

\[
u\longmapsto -u.
\]

Then every signed curl block changes sign,

\[
u_c\longmapsto -u_c,
\]

but every positive energy atom is unchanged:

\[
\boxed{e_c\longmapsto e_c.}
\]

Consequently the **entire** quadratic Hodge functional calculus is unchanged:

\[
\boxed{
Q_F=\frac12\langle u,F(C)u\rangle
\quad\longmapsto\quad
Q_F
}
\]

for every admissible `F`.  In particular, the two states have identical

\[
E,\ H,\ \mathcal K,\ Z,\ \mathcal E(h),\ \rho(h),\ M(h)
\]

for every heat age `h`.

The alternating current behaves differently.  Since it is cubic,

\[
\boxed{
\mathscr T_{cdr}\longmapsto-\mathscr T_{cdr},
\qquad
\mathscr J_{cd}\longmapsto-\mathscr J_{cd}.
}
\]

Therefore every nonlinear quadratic rate changes sign:

\[
\boxed{
(\dot Q_F)_{\rm nl}
\longmapsto
-(\dot Q_F)_{\rm nl}.
}
\]

The viscous term, being quadratic, is unchanged.

Hence there is no universal deterministic rule of the form

\[
\boxed{
\text{nonlinear current}
=\Phi(\{e_c\}_c)
}
\]

and, in particular, no closure

\[
\Pi=\Phi[\rho]
\]

on the positive heat profile alone.  Two smooth admissible instantaneous states can
have identical **all-case quadratic spectral data** and opposite nonlinear transfer.

The missing information is not another magnitude.  It is the odd
phase/orientation content carried minimally here by the alternating scalar triple
products `T_cdr`, and ultimately by the original exact vorticity/velocity field.

This is the quadratic-family analogue of the earlier magnitude-only parity no-go,
but it is stronger in scope: it exhausts the entire Hodge spectral functional
calculus at once.

**Classification: Exact parity consequence / rigorous whole-quadratic closure no-go.**

---

## 15. Exact Beltrami no-go: thin heat layers and large critical size are not badness

The completely monotone shape law is exact, but it cannot by itself be the hidden
no-escape mechanism.  Navier--Stokes supplies an exact smooth family that kills that
interpretation.

Let `u_0` lie entirely in one nonzero signed curl eigenspace:

\[
Cu_0=c\,u_0.
\]

Then

\[
\omega_0=c\,u_0,
\qquad
u_0\times\omega_0=0.
\]

Hence the projected nonlinear Lamb current vanishes identically and the exact
Navier--Stokes solution is

\[
\boxed{
u(t)=e^{-\nu c^2t}u_0.}
\]

Its signed-curl spectral state consists of one positive atom.  Writing

\[
e_c(t)=\frac12\|u(t)\|_2^2,
\]

one has

\[
\boxed{
\Pi(h,t)=0,
\qquad
\rho(h,t)=c^2e^{-hc^2}e_c(t),
\qquad
\mathcal K(t)=|c|e_c(t).
}
\]

Across the family `|c|\to\infty`, the canonical heat boundary width `c^{-2}` tends
to zero and the ratio

\[
\frac{\mathcal K}{E}=|c|
\]

becomes arbitrarily large, yet every member is a globally smooth exact solution and
its critical content only decays viscously.

Therefore:

\[
\boxed{
\text{thin Bernstein boundary concentration or large critical magnitude alone}
\neq
\text{singular escape mechanism}.
}
\]

What distinguishes a hypothetical escape is not the static presence of fine-scale
mass.  It is the **dynamic self-generated alternating current** that would have to
keep transporting positive energy into progressively finer admissible spectral
triangles quickly enough to overcome diagonal viscous killing.

This exact family also makes the whole-family determinant law transparent: with only
one curl block, the fully alternating `T_cdr` vanishes because spectral labels repeat,
so every nonlinear `F(C)` transfer vanishes at once.

**Classification: Audited exact-Navier--Stokes no-go for static boundary-width or
critical-magnitude criteria.**

---

## 16. What has actually been reduced

The repository previously reached the sequence

\[
\text{de Rham skew-square current}
\to
\text{critical heat-null defect}
\to
\text{positive heat-scale continuity}.
\]

The present theorem shows that these are all shadows of an even smaller signed-curl
spectral algebra:

\[
\boxed{
\begin{gathered}
 e_c\ge0,\\
\mathscr T_{cdr}\text{ fully alternating},\\
\mathscr J_{cd}=\sum_r r\mathscr T_{cdr},\\
\dot e_c=\sum_d\mathscr J_{cd}-2\nu c^2e_c,
\end{gathered}
}
\]

and every Hodge quadratic is obtained from

\[
\boxed{
\mathfrak D_F
=1\wedge c\wedge F(c).
}
\]

In this sense:

- energy is `F=1`;
- helicity is `F=c`;
- stretching/enstrophy is `F=c^2`;
- positive critical content is `F=|c|`;
- heat-scale continuity is `F=e^{-hc^2}` and its `h` derivative;
- the complete heat profile is the Laplace transform of the positive atoms `e_c`.

There is no independent mechanism attached to any one of these choices.

The determinant law supplies a mathematical stopping rule against adding further
quadratic Hodge cases one by one: a new spectral quadratic changes only the scalar
curvature weight `D_F`; the physical current `T` is already fixed by Navier--Stokes.

**Classification: Rigorous synthesis of exact identities.**

---

## 17. The no-escape frontier after whole-family compression

The generic positive continuity equation

\[
\rho_t-\partial_h(2\nu\rho+\Pi)=0,
\qquad \rho\ge0,
\]

is now known to be too large a state space.  An actual smooth Navier--Stokes state
must simultaneously satisfy:

\[
\boxed{
\begin{aligned}
&\rho(h)=\sum_c c^2e^{-hc^2}e_c,
&&e_c\ge0,\\
&(-1)^m\partial_h^m\rho\ge0
&&\text{for every }m,\\
&\dot e_c=\sum_d\mathscr J_{cd}-2\nu c^2e_c,\\
&\mathscr J_{cd}=\sum_r r\mathscr T_{cdr},
&&\mathscr T\text{ fully alternating},\\
&\sum_d d\mathscr J_{cd}=0
&&\text{for every }c,\\
&\mathscr T_{cdr}=0
&&\text{outside the Fourier triangle cone}.
\end{aligned}
}
\]

A hypothetical critical escape must therefore do much more than concentrate an
arbitrary positive half-line density.  It must drive the positive signed-curl energy
measure toward `|c|=infinity` through an infinite chain of admissible alternating
spectral triangles, with critical growth coming only from the non-affine chirality
kink `|c|`, while viscosity kills the same energy atoms at the diagonal rate

\[
2\nu c^2e_c.
\]

The heat-age zero-Zeno boundary concentration identified previously is exactly the
Laplace shadow of this signed spectral escape.

The literal remaining question is

\[
\boxed{
\begin{gathered}
\text{Can the self-generated fully alternating curl-spectral three-current}\
\text{transport enough positive energy through an infinite heterochiral triangle chain}\
\text{toward }|c|\to\infty\text{ in finite time, while the same curl coordinate}\
\text{annihilates the current in its first signed moment and its square supplies}\
\text{the diagonal viscous killing }2\nu c^2e_c?
\end{gathered}
}
\]

No theorem here proves that it cannot.

Complete monotonicity alone cannot close the problem: a family of positive spectral
measures can move a vanishing amount of energy to arbitrarily high curl frequency
while keeping total energy bounded and making the critical moment large.  The
missing ingredient, if no-escape is true, must therefore use the **dynamic
self-generation and alternating triangle current**, not merely the static Bernstein
shape of `rho`.

This is the current whole-family frontier.

**Classification: Conjectural bridge / Open.**

No no-escape, blow-up exclusion, restart, continuation, or global-regularity theorem
is claimed.

---

## 18. Classification

**Exact identity**

- signed curl spectral decomposition `u=sum_c u_c`, `Cu_c=c u_c`;
- positive energy atoms `e_c=||u_c||_2^2/2`;
- fully alternating current `T_cdr=int u_c.(u_d cross u_r)`;
- pair current `J_cd=sum_r r T_cdr`;
- skewness and blockwise weighted nullity `sum_d d J_cd=0`;
- positive block law `edot_c=sum_d J_cd-2nu c^2 e_c`;
- master determinant law for every `F(C)` quadratic;
- triplewise affine cancellation of energy and Euler helicity;
- Vandermonde stretching formula for `F=c^2`;
- heterochiral critical determinant for `F=|c|`;
- Laplace representation of the heat-age continuity law;
- complete monotonicity/log-convexity of `rho`;
- spectral barycenter derivative `kappa_h=-Var`;
- Bernstein boundary mass and `M_t=Pi-2nu(rho(0)-rho(h))`.

**Rigorous consequence**

- all quadratic Hodge spectral cases are second-divided-difference readouts of one
  alternating three-current;
- energy and helicity belong to the universal affine family annihilated by that transfer law;
- critical nonlinear growth is supported only on heterochiral signed-curl triples;
- nonzero spectral triples obey exact Fourier triangle support/no teleportation;
- mixed high--high--low critical coefficients have the exact low-frequency-square
  null bound described in Section 10;
- the generic positive heat continuity state space is too large: actual `rho` lies
  in the completely monotone/Bernstein cone;
- even the complete positive signed-curl energy family `{e_c}` (equivalently every
  quadratic `F(C)` readout) does not determine the nonlinear current, by exact state
  reversal parity;
- the earlier heat-scale critical bracket is exactly the time velocity of the
  canonical boundary mass.

**Audited algebra referee**

- a three-label exact rational alternating-current model verifies skewness,
  blockwise curl-weighted nullity, and the determinant master formula for
  `F=1,c,|c|,c^2,c^3`;
- exact rational checks verify `D_{c^2}` equals the Vandermonde and the explicit
  mixed-sign `D_|c|` formulas;
- a positive finite spectral measure checks the complete-monotone derivative signs
  and the spectral-barycenter variance formula.

These are sign/factor referees only; the theorem follows from the exact Hodge-curl
spectral decomposition and alternating scalar triple product.

**Conjectural bridge / Open**

- a dynamic obstruction to an infinite heterochiral triangle cascade toward
  `|c|=infinity`;
- uniform exclusion of zero-heat-age Bernstein mass concentration;
- no-escape/blow-up exclusion;
- restart/continuation/global regularity.
