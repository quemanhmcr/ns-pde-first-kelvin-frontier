# Local future-covariance tensor and backward-Kelvin generator audit

This note advances the PDE-first restart programme from a finite three-loop packet
to the conditional covariance tensor carried by that packet.

The goal is not to guess a matrix PDE from the scalar variance law.  The order is:

1. derive the full vector conditional-moment law on the **actual stochastic state**;
2. identify its carré-du-champ as the same-ancestor pair diagonal defect;
3. use Stokes on both replicas to identify the local tensor as a diagonal density of
   the already existing pair momentum covariance cochain;
4. only then ask whether the full stochastic generator descends to a spatial / area-
   frame state;
5. calibrate every sign against exact Navier--Stokes shear and ABC solutions.

No continuation/restart theorem and no 3D Navier--Stokes regularity claim is made.

---

## 1. Full-state vector conditional moments

Let `Y_s` denote the full Markov state used by a Kelvin representation, with Itô
generator

\[
\mathscr L
=b\cdot\nabla+\frac12 a:\nabla^2.
\]

Let the terminal Kelvin observable be vector-valued,

\[
F=(F_1,\ldots,F_m)^T.
\]

Define the conditional mean, terminal second moment and covariance

\[
m_s(y)=\mathbb E_{s,y}F,
\]

\[
Q_s(y)=\mathbb E_{s,y}[FF^T],
\]

\[
C_s(y)=Q_s(y)-m_s(y)m_s(y)^T.
\]

On the full state, the standard backward conditional-moment equations are

\[
(\partial_s+\mathscr L)m=0,
\qquad
(\partial_s+\mathscr L)Q=0.
\]

The matrix carré-du-champ is

\[
\boxed{
\Gamma_{\mathscr L}[m]
=(\nabla m)\,a\,(\nabla m)^T.
}
\]

Its `(i,j)` entry is the mixed quadratic covariation density between the two
conditional-mean components.

Because

\[
\mathscr L(m_i m_j)
=m_i\mathscr Lm_j+m_j\mathscr Lm_i
+\Gamma_{\mathscr L}(m_i,m_j),
\]

one obtains

\[
\boxed{
(\partial_s+\mathscr L)C
=-\Gamma_{\mathscr L}[m].
}
\]

Equivalently, in a time-homogeneous remaining-horizon coordinate `tau`,

\[
\boxed{
(\partial_\tau-\mathscr L)C
=\Gamma_{\mathscr L}[m].
}
\]

This is the matrix form of the fixed-current future-variance bank.

**Classification: Exact conditional-moment identity on the full stochastic state.**

---

## 2. The carré-du-champ is an exact transfer, not a new total source

The conditional mean-square tensor satisfies

\[
M:=mm^T.
\]

In remaining-horizon convention,

\[
\boxed{
(\partial_\tau-\mathscr L)M
=-\Gamma_{\mathscr L}[m].
}
\]

while

\[
\boxed{
(\partial_\tau-\mathscr L)C
=+\Gamma_{\mathscr L}[m].
}
\]

Therefore

\[
\boxed{
Q=C+mm^T
}
\]

has no carré-du-champ source:

\[
\boxed{
(\partial_\tau-\mathscr L)Q=0.
}
\]

So physical branching does something very specific:

\[
\boxed{
\text{conditional mean-square}
\longrightarrow
\text{future covariance}.
}
\]

It does not manufacture terminal second moment from nothing.

This is the tensor version of the scalar martingale variance identity, with every
mixed orientation term retained.

**Classification: Exact identity.**

---

## 3. Exact connected version

Suppose an output frame is part of the state and its horizon evolution is

\[
\dot H=BH.
\]

If a vector mean is represented by

\[
m_H=H^T\mu,
\]

then the quotient mean equation forced by the full-state homogeneous law is

\[
\boxed{
(\partial_\tau-\mathscr L_x)\mu+B^T\mu=0.
}
\]

If

\[
C_H=H^T\mathcal C H,
\qquad
Q_H=H^T\mathcal QH,
\]

then the corresponding local tensor equations are

\[
\boxed{
(\partial_\tau-\mathscr L_x)\mathcal C
+B^T\mathcal C+\mathcal C B
=\mathcal G,
}
\]

\[
\boxed{
(\partial_\tau-\mathscr L_x)\mathcal Q
+B^T\mathcal Q+\mathcal Q B
=0,
}
\]

where `mathcal G` is the local tensor whose packet pullback is the full mixed
carré-du-champ.

Likewise

\[
(\partial_\tau-\mathscr L_x)(\mu\mu^T)
+B^T\mu\mu^T+\mu\mu^TB
=-\mathcal G.
\]

Thus connection geometry acts on both mean-square and covariance, while the
carré-du-champ transfers exactly between them.

**Classification: Exact quotient algebra conditional on the stated tensor
factorization and generator descent.**

The factorization and descent are separate questions; they are not supplied merely
by writing these equations.

---

## 4. Exact vector one-mode Kelvin calibration

Take the one-dimensional heat/Kelvin state with diffusion covariance `2 nu` and two
terminal components

\[
F_1(a)=\cos(ka),
\qquad
F_2(a)=\sin(ka).
\]

The conditional means at remaining horizon `tau` are

\[
m_1=e^{-\nu k^2\tau}\cos(ka),
\qquad
m_2=e^{-\nu k^2\tau}\sin(ka).
\]

The terminal second moments are

\[
Q_{11}
=\frac12\left(1+e^{-4\nu k^2\tau}\cos 2ka\right),
\]

\[
Q_{22}
=\frac12\left(1-e^{-4\nu k^2\tau}\cos 2ka\right),
\]

\[
Q_{12}
=\frac12e^{-4\nu k^2\tau}\sin 2ka.
\]

The full source is

\[
\boxed{
\Gamma
=2\nu\,\partial_am\,(\partial_am)^T.
}
\]

Its mixed entry is

\[
\boxed{
\Gamma_{12}
=-2\nu k^2e^{-2\nu k^2\tau}\sin(ka)\cos(ka),
}
\]

which changes sign with orientation/anchor.

CI verifies simultaneously

\[
\mathfrak Hm=0,
\qquad
\mathfrak HQ=0,
\qquad
\mathfrak HC=\Gamma,
\qquad
\mathfrak H(mm^T)=-\Gamma,
\]

with `mathfrak H=partial_tau-L`.

**Classification: Exact one-mode Kelvin calibration.**

---

## 5. The same tensor is the same-ancestor pair diagonal defect

Let

\[
U(y_1,y_2)=m(y_1)m(y_2)^T.
\]

For two independent future replicas after the common branch time, the pair
generator is

\[
\mathscr L^{(1)}+\mathscr L^{(2)}.
\]

Restricting to the diagonal after applying the pair generator is not the same as
first restricting and then applying the one-state generator.  Exactly,

\[
\boxed{
\mathscr L(U^\Delta)
-(\mathscr L^{(1)}+\mathscr L^{(2)})U\big|_\Delta
=\Gamma_{\mathscr L}[m].
}
\]

All first-order drift pieces cancel.  Only the viscous cross-derivation remains.

The new symbolic audit verifies this identity for a vector polynomial mean and a
nonconstant drift, entry by entry.

Thus the matrix future-covariance source is not a new stochastic tensor invented for
restart.  It is precisely the vector contraction of the canonical same-ancestor
branching mechanism already present in the pair world-sheet.

**Classification: Exact pair-generator identity.**

---

## 6. Double Stokes: the local tensor is already inside the pair covariance cochain

The repository already carries the future momentum pair covariance cochain

\[
\mathbb K_s
=\mathbb E_s
[(\beta-\bar\beta_s)\boxtimes(\beta-\bar\beta_s)],
\]

where `beta` is the random transported momentum cochain modulo exact forms.

For two closed loops

\[
Z_i=\partial\Sigma_i,
\qquad
Z_j=\partial\Sigma_j,
\]

the future circulation covariance is

\[
C_s(Z_i,Z_j)
=\langle\mathbb K_s,Z_i\boxtimes Z_j\rangle.
\]

Apply Stokes separately in the two replicas:

\[
\boxed{
C_s(\partial\Sigma_i,\partial\Sigma_j)
=
\left\langle
(d\boxtimes d)\mathbb K_s,
\Sigma_i\boxtimes\Sigma_j
\right\rangle.
}
\]

This is the continuum version of the finite-chain identity

\[
\boxed{
C_{\rm face}=D^T K_{\rm edge}D.
}
\]

The CI triangle witness has

\[
B_1D_2=0
\]

and verifies the double-Stokes covariance formula exactly.

### Gauge sector

If

\[
\beta\mapsto\beta+dp,
\]

then for every closed loop

\[
\langle dp,\partial\Sigma\rangle
=\langle p,\partial^2\Sigma\rangle
=0.
\]

The finite-chain audit likewise gives

\[
D_2^TB_1^Tp=0.
\]

Therefore the local future vorticity/flux covariance tensor is gauge invariant
before any limit is taken.

**Classification: Exact double-Stokes and boundary-squared-zero identity.**

---

## 7. Fixed-state local covariance tensor theorem

The previous note treated the existence of a local future tensor as entirely open.
That was too coarse.  At a fixed regular state there is a simple conditional Stokes
theorem.

Let

\[
\zeta_s(y)=d\beta_s(y)
\]

be the random terminal vorticity two-form, identified with a random vector in 3D.
Assume conditional mean-square continuity at `x`:

\[
\boxed{
\mathbb E_s|\zeta_s(y)-\zeta_s(x)|^2
\longrightarrow0
\quad(y\to x).
}
\]

For a small planar surface `Sigma_r(x,n)` of area `A_r`, define

\[
X_r(n)
=\int_{\Sigma_r}\zeta_s(y)\cdot n\,dS.
\]

Then

\[
\frac{X_r(n)}{A_r}-\zeta_s(x)\cdot n
=
\frac1{A_r}\int_{\Sigma_r}
(\zeta_s(y)-\zeta_s(x))\cdot n\,dS.
\]

Conditional Jensen gives

\[
\mathbb E_s
\left|
\frac{X_r(n)}{A_r}-\zeta_s(x)\cdot n
\right|^2
\le
\frac1{A_r}\int_{\Sigma_r}
\mathbb E_s|\zeta_s(y)-\zeta_s(x)|^2\,dS,
\]

hence

\[
\boxed{
X_r(n)/A_r
\longrightarrow
\zeta_s(x)\cdot n
\quad\text{in conditional }L^2.
}
\]

Therefore for a packet with oriented area columns

\[
H_r=(h_{r,1},h_{r,2},h_{r,3}),
\qquad
h_{r,j}=A_{r,j}n_j,
\]

its future covariance has the area-squared local tensor limit

\[
\boxed{
C^{\rm future}_{H_r}
=H_r^T\mathcal C_s(x)H_r+o(|H_r|^2),
}
\]

where

\[
\boxed{
\mathcal C_s(x)
=\operatorname{Cov}_s(\zeta_s(x),\zeta_s(x)).
}
\]

Equivalently, `mathcal C_s(x)` is the diagonal density of

\[
(d\boxtimes d)\mathbb K_s
\]

when that diagonal trace is regular.

**Classification: Rigorous conditional theorem at a fixed state under conditional
mean-square continuity.**

What remains open is uniformity of this continuity and remainder as a candidate
singular time is approached.

---

## 8. Centered smooth packets improve the remainder to the safe side of `r^4`

For a centered symmetric surface and a conditionally `C^2` random field, the first
spatial moment vanishes.  Taylor expansion gives

\[
X_r
=r^2X_0+r^4X_2+o(r^4)
\]

for the loop/flux payoff.

Consequently

\[
\operatorname{Cov}(X_r)
=r^4C_0+r^6C_1+r^8C_2+o(r^8).
\]

After the packet metric contributes `r^{-4}`, the non-tensorial remainder is

\[
\boxed{
r^2C_1+r^4C_2+o(r^4),
}
\]

and therefore vanishes as `r -> 0` at every fixed state where the required local
regularity constants remain finite.

The new symbolic audit keeps `C_0,C_1,C_2` completely general and verifies the
`r^6 -> r^2` law exactly.

**Classification: Exact symmetric-loop scaling algebra; rigorous local consequence
under the stated conditional `C^2` regularity.**

This is not uniform singular-time control.

---

## 9. Full vorticity dyad equation: Kelvin Gram is the viscous defect tensor

Let

\[
E_\omega=\omega\omega^T,
\qquad
A=\nabla u.
\]

The vorticity equation is

\[
(\partial_t+u\cdot\nabla)\omega
=A\omega+\nu\Delta\omega.
\]

Apply the product rule before estimating anything.  Since

\[
\Delta(\omega\omega^T)
=(\Delta\omega)\omega^T
+\omega(\Delta\omega)^T
+2\sum_k(\partial_k\omega)(\partial_k\omega)^T,
\]

one obtains

\[
\boxed{
(\partial_t+u\cdot\nabla-\nu\Delta)E_\omega
=A E_\omega+E_\omega A^T
-2\nu(\nabla\omega)(\nabla\omega)^T.
}
\]

Define

\[
\boxed{
\mathcal G_K
=2\nu(\nabla\omega)(\nabla\omega)^T.
}
\]

Then

\[
\boxed{
\mathfrak D_K E_\omega=-\mathcal G_K,
}
\]

where

\[
\mathfrak D_KT
:=(\partial_t+u\cdot\nabla-\nu\Delta)T
-A T-T A^T.
\]

This is stronger than the earlier trace identity.  The **entire** local Kelvin Gram
tensor is the viscous defect tensor of the vorticity dyad.

Taking one-half trace gives exactly

\[
(\partial_t+u\cdot\nabla)e
=\omega\cdot S\omega
+\nu\Delta e
-\nu|\nabla\omega|^2.
\]

CI verifies the full `3 x 3` residual, not only its trace, on both exact periodic
shear and genuine 3D ABC/Beltrami Navier--Stokes solutions.

**Classification: Exact 3D Navier--Stokes tensor identity and exact NS
calibrations.**

---

## 10. The backward-Itô infinitesimal packet generator is fixed by NS

For an additive-noise stochastic flow, spatial differentiation of the noise is zero,
so the infinitesimal area-frame kinematics is the Nanson law

\[
\dot H=-A^TH.
\]

The causal Constantin--Iyer Kelvin law is naturally a **backward** stochastic
conservation law.  In physical-time PDE notation the corresponding infinitesimal
backward operator carries the second-order sign `-nu Delta`.

Act on the packet flux mean

\[
m_H=H^T\omega.
\]

Using the NS vorticity equation,

\[
\begin{aligned}
&\left[
\partial_t+u\cdot\nabla-\nu\Delta
-A^TH:\nabla_H
\right](H^T\omega)
\\
&\qquad
=(-A^TH)^T\omega
+H^T(\partial_t+u\cdot\nabla-\nu\Delta)\omega
\\
&\qquad
=-H^TA\omega+H^TA\omega
=0.
\end{aligned}
\]

Thus

\[
\boxed{
\left[
\partial_t+u\cdot\nabla-\nu\Delta
-A^TH:\nabla_H
\right](H^T\omega)=0.
}
\]

The CI suite verifies this exact cancellation for arbitrary symbolic `H` in the
periodic shear and for an explicit invertible `H` in ABC flow.

**Classification: Exact Navier--Stokes / backward-Kelvin infinitesimal packet
identity.**

This identifies the local mean operator.  It does not by itself prove that every
full future-covariance state variable in the repository is a function only of
`(x,H)`.

---

## 11. Causal orientation: backward Kelvin covariance is a past-payoff bank

A sign trap must be kept explicit.

The operator

\[
\partial_t+u\cdot\nabla-\nu\Delta
\]

is anti-diffusive if it is incorrectly interpreted as a forward Markov semigroup to
a terminal time `T>t`.  Doing that can even make a purported terminal second moment
lose positivity.

The physical stochastic Kelvin theorem instead uses a **backward martingale**.  Its
terminal payoff lies at a past time `t_0<t`.

For the exact one-mode NS shear,

\[
\omega_z(t,y)
=k e^{-\nu k^2t}\sin(ky).
\]

The past-payoff second moment propagated by the backward Kelvin law is

\[
\boxed{
Q_{zz}(t,y)
=\frac{k^2e^{-2\nu k^2t_0}}2
\left[
1-e^{-4\nu k^2(t-t_0)}\cos(2ky)
\right].
}
\]

Set

\[
C_{zz}=Q_{zz}-\omega_z^2.
\]

Then

\[
C_{zz}(t_0,y)=0,
\]

and CI verifies the exact tensor equations

\[
\boxed{
\mathfrak D_K C
=+\mathcal G_K,
}
\]

\[
\boxed{
\mathfrak D_K(\omega\omega^T)
=-\mathcal G_K,
}
\]

therefore

\[
\boxed{
\mathfrak D_K(C+\omega\omega^T)=0.
}
\]

This is an exact NS tensor transfer calibration.

**Classification: Exact one-mode Navier--Stokes backward-Kelvin covariance
calibration.**

The repository also uses an abstract **future** ancestry variance bank.  The algebra
is the same after a remaining-horizon reversal, but the global identification of the
forward ancestry state with the physical backward stochastic Kelvin state has not
been written line by line.

**Classification: Open-literal time-orientation/state-identification bridge.**

---

## 12. Generator descent is a real mathematical condition

The full stochastic state need not be just the spatial point `x`.  It may carry
current shape, area frame, deformation, back-to-label information, or other state
needed by the Kelvin payoff.

Let

\[
\pi:Y\to X
\]

be a proposed reduction and let `R` lift a reduced observable to the full state:

\[
(Rf)(y)=f(\pi(y)).
\]

An autonomous reduced generator `Lbar` exists only if

\[
\boxed{
\mathscr L R=R\bar{\mathscr L}.
}
\]

In finite-state language this is exactly the lumpability/intertwining condition.
Equivalently, `L R f` must be constant on every projection fiber for every reduced
observable `f`.

The new audit includes two four-state models.

### Lumpable model

Two hidden shape states at the same spatial point have the same physical exit rate.
Then

\[
\mathscr LR=R\bar{\mathscr L}
\]

exactly and the quotient generator exists.

### Non-lumpable model

Two hidden shape states at the same spatial point have rates `1` and `2` to the same
reduced destination.  Then a reduced observable has full generator values `1` and
`2` on the same spatial fiber.

Hence no `Lbar` exists.

The residual is a literal hidden-state flux, not an algebraic nuisance.

**Classification: Exact generic generator-descent criterion plus exact
counterexample.**

For the actual NS/Kelvin construction, the infinitesimal `(x,H)` mean operator is
now audited, but the complete full-state covariance/current-shape generator has not
been written line by line in this repository.

**Classification: Open-literal programme-specific generator descent.**

---

## 13. The local source tensor meets the orientation packet exactly

At a smooth physical state define

\[
\mathcal G_K
=2\nu(\nabla\omega)(\nabla\omega)^T.
\]

For an arbitrary invertible oriented area frame `H`, its packet pullback is

\[
H^T\mathcal G_KH
=2\nu H^T(\nabla\omega)(\nabla\omega)^TH.
\]

But this is exactly the independently audited raw area-frame Kelvin q.v. matrix

\[
\Gamma_H.
\]

Thus

\[
\boxed{
H^T\mathcal G_KH=\Gamma_H.
}
\]

The new cross-module CI test evaluates both constructions independently and obtains
zero residual.

We therefore have four exact descriptions of the same physical tensor:

1. vector conditional-mean carré-du-champ;
2. same-ancestor pair diagonal generator defect;
3. double-Stokes local density of pair momentum covariance;
4. viscous defect tensor of `omega tensor omega`.

This convergence of independently derived structures is the main result of this
audit.

**Classification: Exact identity / rigorous structural identification.**

---

## 14. What is now closed and what is still open

### Closed at the structural/full-state level

The following no longer belong to the unknown frontier:

- vectorization of the future covariance bank;
- mixed cross-orientation carré-du-champ;
- mean-square/future-covariance transfer;
- same-ancestor pair source at tensor level;
- double-Stokes identification with the existing pair covariance cochain;
- gauge blindness of the local flux covariance;
- fixed-state local tensor existence under conditional mean-square continuity;
- centered `C^2` packet remainder scaling `r^6` raw / `r^2` after metric
  normalization;
- full NS vorticity-dyad tensor identity;
- infinitesimal backward-Kelvin `(x,H)` mean generator;
- exact backward-Kelvin shear covariance tensor transfer.

### Still open

The real remaining questions are narrower.

1. **Full-state to reduced-state generator descent.**  Write the actual stochastic
   Kelvin covariance/current-shape state and prove the relevant projection is
   sufficient/lumpable.  Hidden shape/history cannot be dropped by declaration.

2. **Forward-future versus backward-Kelvin time orientation.**  Write the exact map
   between the abstract future-ancestry bank and the causal physical backward
   martingale used by the NS Kelvin representation.

3. **Uniform diagonal trace near a candidate singular time.**  Fixed-time
   conditional `L^2` continuity gives a tensor; the required continuity constants
   and metric-amplified remainder are not known uniformly as the selected scale and
   time approach a candidate singularity.

4. **Material metric/boundary/exit work.**  Even after the carré-du-champ becomes an
   internal transfer between mean-square and future covariance, the total second
   moment still feels physical connection/stretching and boundary/exit currents.

5. **Restart.**  No capacity inequality or continuation theorem has been proved.

The frontier is therefore no longer

> does a future covariance tensor exist at all?

At a fixed regular state, under the natural conditional mean-square Stokes
hypothesis, it does.

The sharper question is

> does the exact full-state tensor bank descend to the required physical reduced
> state with a uniform diagonal trace/remainder law, and can its remaining material
> metric and physical boundary/exit work stay controlled up to a candidate singular
> time?

**Classification: Rigorous structural reduction.  Generator descent, causal
future/backward identification, uniform singular-time tensor control, restart, and
regularity remain open.**
