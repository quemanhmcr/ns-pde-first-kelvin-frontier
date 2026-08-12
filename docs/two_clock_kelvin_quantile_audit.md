# Reverse-age Kelvin clock and quantile-current audit

This note attacks the two living compatibility seams left after the clock/cut
referee repair:

1. how an abstract **future** conditional covariance bank can be the causal
   **past-payoff** bank of the physical backward stochastic Kelvin theorem;
2. what actually moves a fixed-mass quantile/shell boundary.

The derivation keeps three operations distinct: physical time, reversal of the
future-bank clock, and time reversal of a diffusion law.  No continuation or
regularity conclusion is claimed.

---

## 1. Physical backward Kelvin operator and reverse age

Let `r` denote physical time and let the physical backward-Itô state operator be

\[
\boxed{
\mathscr K_r^-
= B_{\rm K}(r)\cdot\nabla
-\nu K_{\rm K}:\nabla^2.
}
\]

For the anchor-only flat sector, `B_K=u` and `K_K=I`.  For the full common-noise
current-shape state, the anchor has drift `u`, relative shape has the exact
finite-variation velocity-difference drift, and the second-order block is the
rank-three common translation operator.  For an infinitesimal `(X,H)` packet,

\[
B_{\rm K}=(u,-(\nabla u)^T H).
\]

Fix a physical observation time `t` and introduce **reverse age**

\[
\boxed{r=t-\sigma.}
\]

Then `partial_sigma=-partial_r`.  Therefore a physical backward-Kelvin mean

\[
(\partial_r+\mathscr K_r^-)m=0
\]

becomes

\[
\boxed{
(\partial_\sigma+\mathscr L_{\rm rev}^{(t)}(\sigma))\widehat m=0,
\qquad
\mathscr L_{\rm rev}^{(t)}(\sigma)
=-\mathscr K^-_{t-\sigma}.
}
\]

The second-order sign is now positive.  Hence `L_rev` is an ordinary forward
Markov generator in reverse age.  At current physical time `t`, a payoff at a past
time `t_0<t` is simply a **future terminal payoff** at reverse-age horizon

\[
\Theta_t=t-t_0.
\]

Thus the causal physical past-payoff Kelvin bank is literally a future
conditional bank in the reverse-age clock.

**Classification: Exact clock-reparameterization identity.**

---

## 2. Exact one-mode calibration

For the exact NS shear mode, the relevant anchor mean is

\[
\widehat m(\sigma,a)
=e^{-\nu k^2\sigma}\cos(ka).
\]

It satisfies

\[
\boxed{
(\partial_\sigma-\nu\partial_a^2)\widehat m=0,
}
\]

which is exactly the physical backward-Kelvin mean equation in reverse age for the
shear anchor (`u_a=0`).

The associated centered covariance satisfies

\[
\boxed{
(\partial_\sigma-\nu\partial_a^2)\widehat C=\widehat\gamma,
}
\]

so the bank grows away from its past terminal while the same object decreases as a
future bank when read in the unreversed ancestry clock.  The sign change is clock
orientation, not a new source.

**Classification: Exact Navier--Stokes/Kelvin calibration.**

---

## 3. Future-bank clock reversal uses `b_+`, not the same-clock `b_-`

The normalized ancestry future operator is

\[
\mathscr L_+
=b_+\cdot\nabla+\nu K:\nabla^2.
\]

A future conditional mean obeys

\[
(\partial_s+\mathscr L_+)m=0.
\]

Set

\[
\sigma=\Theta-s,
\qquad
\widehat m(\sigma,y)=m(\Theta-\sigma,y).
\]

Then

\[
\boxed{
(\partial_\sigma-b_+\cdot\nabla-\nu K:\nabla^2)\widehat m=0.
}
\]

Therefore, in a flat identity-map anchor sector, matching the physical
backward-Kelvin operator

\[
\partial_\sigma+u\cdot\nabla-\nu\Delta
\]

requires

\[
\boxed{b_+=-u.}
\]

This is **not** the same statement as the same-clock diffusion-reversal condition

\[
\boxed{b_-=u.}
\]

already audited in `ancestry_time_reversal_audit.md`.  The first reverses the clock
of a future bank.  The second compares the backward drift of a diffusion while
keeping the clock orientation fixed.

Since

\[
j=\frac{b_++b_-}{2},
\]

an identity map satisfying both conditions against the same physical drift would
force

\[
\boxed{j=0.}
\]

Thus for a nonzero ancestry probability current the two interpretations cannot be
silently identified.

**Classification: Exact operator distinction and rigorous incompatibility
consequence.**

---

## 4. General clock-reversed state-map equations

Let `Pi(tau,y)` map ancestry state to a physical Kelvin state.  Under clock reversal,
write

\[
z=\Pi(\sigma,y).
\]

The diffusion pushforward is

\[
\boxed{
K_{\rm K}=D\Pi\,K\,D\Pi^T.
}
\]

The physical backward-Itô drift appearing after the future-bank clock is reversed
must satisfy

\[
\boxed{
B_{\rm K}
=\partial_\sigma\Pi
-D\Pi\,b_+
-\nu\,(K:D^2\Pi).
}
\]

Compare this with the distinct same-clock backward-drift map

\[
\boxed{
B_{\rm K}
=\partial_t\Pi
+D\Pi\,b_-
-\nu\,(K:D^2\Pi).
}
\]

These are two exact equations for two different constructions.  The programme's
future covariance bridge must use the **first** system.

For a time-independent identity map with flat diffusion, it reduces exactly to
`b_+=-u` and `K=I`.

**Classification: Exact backward/clock-reversed Itô state-map system.  Existence of
the programme-specific map remains open-literal.**

---

## 5. Reference-gauge consequence for the future-bank bridge

The ancestry expansion gives

\[
b_+=w+\nu c_\phi.
\]

Hence, in the flat identity-map physical anchor interpretation of the **future-bank
clock reversal**, the required symbol is

\[
\boxed{
w_{\rm future}=-u-\nu c_\phi.
}
\]

By contrast, same-clock matching of `b_-=u` requires

\[
w_{\rm same}
=u+\nu c_\phi+2\nu K\nabla\log f.
\]

The difference is not a contradiction: the equations answer different causal
questions.  Equating the two without an additional theorem would amount to forcing
the probability-current sector to collapse.

**Classification: Exact coefficient consequence; no state identification claimed.**

---

## 6. Clock reversal also reverses probability-current velocity

The normalized ancestry continuity equation is

\[
\partial_s q+\nabla\cdot(qj)=0.
\]

Define

\[
\widehat q(\sigma,y)=q(\Theta-\sigma,y).
\]

Then

\[
\boxed{
\partial_\sigma\widehat q
+\nabla\cdot(\widehat q\,\widehat j)=0,
\qquad
\widehat j=-j.
}
\]

So probability current, unlike quadratic variation, is orientation-sensitive and
changes sign under clock reversal.

The distributed covariance balance transforms consistently.  If

\[
\partial_s(qV)
+\nabla\cdot(qjV+\nu qK\nabla V)
=-q\gamma,
\]

then in reverse age

\[
\boxed{
\partial_\sigma(\widehat q\widehat V)
+\nabla\cdot
\big(
\widehat q\widehat j\widehat V
-\nu\widehat qK\nabla\widehat V
\big)
=+\widehat q\widehat\gamma.
}
\]

This is the divergence-form version of the causal past-payoff covariance growth
law.

**Classification: Exact clock-reversed continuity/covariance-current identities.**

---

## 7. Fixed-mass quantile speed is determined by probability current

Now let a scalar observable `g(y,t)` define a chamber

\[
D_t=\{y:g(y,t)<a_p(t)\}
\]

with fixed probability mass `p`.  Assume `grad g` is nonzero on the boundary.
For

\[
\partial_tq+\nabla\cdot(qj)=0,
\]

Reynolds transport gives boundary normal speed

\[
V_n=\frac{\dot a_p-\partial_tg}{|\nabla g|}.
\]

Mass conservation therefore forces

\[
\boxed{
\dot a_p
=
\frac{
\displaystyle
\int_{g=a_p}
\frac{q}{|\nabla g|}
(\partial_tg+j\cdot\nabla g)\,dS
}{
\displaystyle
\int_{g=a_p}\frac{q}{|\nabla g|}\,dS
}.
}
\]

This is the literal level-set/quantile speed law.  It says the cut moves with a
coarea-weighted probability-current material rate of its defining observable.

In one dimension, for `g=x`,

\[
\boxed{\dot a_p=j(a_p,t).}
\]

Thus the quantile boundary follows the **probability-current velocity**.  It is not
in general transported by `b_+`, `b_-`, or `u` alone.

**Classification: Exact Reynolds/coarea consequence.**

---

## 8. Exact diffusion calibration: even zero drift moves quantiles

For zero-drift heat flow starting from a centered Gaussian with variance `v_0`,

\[
v(\sigma)=v_0+2\nu\sigma.
\]

If `z_p` is the standard-normal `p`-quantile,

\[
a_p(\sigma)=z_p\sqrt{v_0+2\nu\sigma}.
\]

Hence

\[
\boxed{
\dot a_p
=\frac{\nu a_p}{v_0+2\nu\sigma}.
}
\]

The probability-current velocity is exactly

\[
j(x,\sigma)
=-\nu\partial_x\log q
=\frac{\nu x}{v_0+2\nu\sigma},
\]

so

\[
\boxed{\dot a_p=j(a_p,\sigma).}
\]

This calibration shows physically why a moving quantile face cannot be replaced by
transport drift alone: diffusion moves the quantile through the osmotic/current
part even when the Itô drift is zero.

**Classification: Exact heat/Kelvin calibration.**

---

## 9. Physical reverse-Kelvin anchor quantiles

For the flat physical reverse-age anchor SDE

\[
dX_\sigma=-u(X_\sigma,t-\sigma)\,d\sigma
+\sqrt{2\nu}\,dW_\sigma,
\]

the forward reverse-age drift is `-u`.  If its density is `rho`, the probability
current velocity is

\[
\boxed{
j_{\rm K,rev}=-u-\nu\nabla\log\rho.}
\]

Therefore a one-dimensional coordinate quantile of the physical reverse-age Kelvin
anchor moves with

\[
\boxed{
\dot a_p=-u(a_p,t-\sigma)
-\nu\partial_x\log\rho(a_p,\sigma).
}
\]

The second term is a physical diffusion/current face, not `S^int` and not observer
noise.

**Classification: Exact physical consequence conditional only on the stated anchor
density.**

---

## 10. Exact affine NS calibration: quantile shells are integrated support geometry

Take the exact incompressible linear-strain Navier--Stokes flow

\[
u(x)=Ax,
\qquad
A=\operatorname{diag}(s,0,-s),
\]

with its quadratic pressure cancellation.  The reverse-age anchor is the linear
SDE

\[
dX_\sigma=-AX_\sigma\,d\sigma+\sqrt{2\nu}\,dW_\sigma.
\]

Starting from a centered point/Gaussian state, its covariance obeys

\[
\boxed{
\dot\Sigma=-A\Sigma-\Sigma A^T+2\nu I.
}
\]

For constant `A`,

\[
\boxed{
\Sigma(\sigma)
=2\nu\int_0^\sigma
 e^{-Ar}e^{-A^Tr}\,dr.
}
\]

The matrix inside the integral is exactly the Cauchy--Green tensor of a reverse
material line element.  Thus stochastic quantile geometry is the **time-integrated
reverse support geometry**.

For the diagonal NS strain,

\[
\boxed{
\Sigma_{xx}
=\frac{\nu}{s}(1-e^{-2s\sigma}),
\qquad
\Sigma_{yy}=2\nu\sigma,
\qquad
\Sigma_{zz}
=\frac{\nu}{s}(e^{2s\sigma}-1).
}
\]

Their short-horizon expansions are

\[
\Sigma_{xx}=2\nu\sigma-2\nu s\sigma^2+O(\sigma^3),
\qquad
\Sigma_{zz}=2\nu\sigma+2\nu s\sigma^2+O(\sigma^3).
\]

So the isotropic Kelvin parabolic scale is the exact leading term, while real NS
strain creates the first anisotropic correction.

Now define the Mahalanobis shell

\[
\boxed{g(x,\sigma)=x^T\Sigma(\sigma)^{-1}x.}
\]

For the Gaussian density, probability-current velocity is

\[
j=-Ax+\nu\Sigma^{-1}x.
\]

Using the covariance ODE gives the **pointwise** cancellation

\[
\boxed{
\partial_\sigma g+j\cdot\nabla g=0.
}
\]

Therefore every fixed Mahalanobis quantile ellipsoid is transported exactly by the
probability current.  This is stronger than integrated mass conservation and gives
an exact moving-shell calibration in a genuine Navier--Stokes flow.

**Classification: Exact affine Navier--Stokes/Gaussian calibration and exact
support--quantile Gramian identity.**

---

## 11. What the current repo still does not determine

The selector documents say that `Q_s` is a moving quantile chamber, but they do not
write the scalar germ observable `g` whose level sets define that chamber.  The
threshold functions deciding which germ is bad are also abstract.

Therefore the exact coarea formula above determines the speed **once `g` and the
relevant continuity clock are supplied**, but the programme-specific first-bad
speed is still not instantiated.

There is a second obstruction.  A one-clock ancestry continuity law in `sigma` does
not determine arbitrary outer physical-time dependence.  For example, both

\[
q_1(t,\sigma,x)=\varphi(x),
\qquad
q_2(t,\sigma,x)=\varphi(x-ct)
\]

solve

\[
\partial_\sigma q=0
\]

with zero ancestry current in `sigma`, yet their physical-time quantiles move with
speeds `0` and `c`.  Hence physical first-bad cut speed cannot be recovered from the
one-clock ancestry PDE alone.

**Classification: Exact underdetermination counterexample.**

The living data seam is now precise:

\[
\boxed{
\text{define the first-bad scalar germ observable }g
\;+
\text{construct the physical/reverse-age state and outer-time lift}.
}
\]

---

## 12. Updated frontier

Audited:

- `L_rev=-K^-` for the physical reverse-age Kelvin state;
- future-bank clock reversal uses the forward ancestry drift `b_+`;
- same-clock `b_-` matching is a distinct construction;
- reverse-age state-map drift/diffusion equations;
- probability-current sign reversal under clock reversal;
- exact fixed-mass level-set quantile speed;
- Gaussian diffusion and physical reverse-Kelvin quantile calibrations;
- one-clock ancestry continuity does not determine outer physical cut speed.

Open-literal:

1. identify/construct the programme ancestry state with the physical reverse-age
   Kelvin state, using the `b_+` clock-reversed intertwining equations;
2. define the scalar germ observable/threshold geometry that the first-bad quantile
   chamber actually cuts;
3. supply the outer physical-time law needed to differentiate that chamber along the
   first-bad selector.

Uniform support/shape/covariance collapse, restart capacity, `S^int`, and
continuation remain open.

**Classification: Structural clock/cut advance; no continuation/restart theorem.**
