# Continuous Brownian-source revaluation across a combined selected event

A selected residual path has two stochastic structures that must not be conflated:

1. the càdlàg **state path** may have a finite event jump `DeltaY`, whose optional
   quadratic variation contains the jump square `DeltaY DeltaY^T`;
2. the **continuous Brownian q.v. rate** on the interval after the event may differ
   from the rate before the event because the physical packet library and/or active
   selector changed.

This note derives the second object literally from the same-replica Navier--Stokes
noise response and keeps it separate from the first.

## 1. Pre/post selected Brownian response

Let the pre-event persistent same-replica residual library have stacked Brownian
response

\[
\mathcal N\in\mathbb R^{3N\times3},
\qquad
d\Chi=\sqrt{2\nu}\,\mathcal N\,dW.
\]

Let `A` be a specified finite physical library event, with pre/post selector readouts
`E_-`, `E_+`.  Then

\[
\boxed{B_-=E_-\mathcal N,}
\qquad
\boxed{B_+=E_+A\mathcal N.}
\]

The selected continuous Brownian q.v. rates on the two adjacent frozen intervals are

\[
\boxed{
\Gamma_-^{\rm cont}=2\nu B_-B_-^T,
\qquad
\Gamma_+^{\rm cont}=2\nu B_+B_+^T.
}
\]

Both endpoint rates are positive semidefinite Gram tensors.  Their finite difference
need not be positive.

**Classification: Exact identity.**

## 2. The rate revaluation uses the same full pair product rule

Let

\[
D=E_+A-E_-.
\]

Then the Brownian response changes by

\[
\delta B=D\mathcal N.
\]

Therefore

\[
\boxed{
\Gamma_+^{\rm cont}-\Gamma_-^{\rm cont}
=2\nu\left[
\delta B B_-^T+B_-\delta B^T+\delta B\delta B^T
\right].
}
\]

Equivalently, with the full pre-event same-replica Gram

\[
\Gamma_{\rm lib}=2\nu\mathcal N\mathcal N^T,
\]

the selected rate revaluation is

\[
D\Gamma_{\rm lib}E_-^T
+E_-\Gamma_{\rm lib}D^T
+D\Gamma_{\rm lib}D^T.
\]

Thus cross-germ common-noise blocks remain mandatory at a finite event.  The event
does not diagonalize the pair state.

**Classification: Exact identity.**

## 3. A signed rate revaluation is not negative q.v. production

Each endpoint rate `Gamma_-^cont`, `Gamma_+^cont` is a positive semidefinite Brownian
source.  Their difference is a **signed finite revaluation** of which continuous
source is active after the event.

A negative direction in

\[
\Gamma_+^{\rm cont}-\Gamma_-^{\rm cont}
\]

means that the post-event packet/readout has less Brownian q.v. rate in that direction
than the pre-event packet/readout.  It is not a negative carré-du-champ and not a
negative Brownian production mechanism.

**Classification: Exact physical typing consequence.**

## 4. Continuous source-rate revaluation and jump optional q.v. are independent

The finite state jump is

\[
\Delta Y=D X_-.
\]

Its optional q.v. atom is

\[
(\Delta Y)(\Delta Y)^T.
\]

The continuous-rate revaluation instead depends on `mathcal N` through `D mathcal N`.
They are different state functions.

Two exact algebraic witnesses show neither determines the other:

- take `X_-=0` but unequal pre/post noise blocks: the jump square is zero while the
  continuous q.v. rate changes;
- take `mathcal N=0` but a nonzero library state and selector jump: the continuous
  q.v. rate does not change while the jump square is nonzero.

So the hybrid ledger must keep both objects.

**Classification: Rigorous consequence of exact path/noise typing.**

## 5. Exact one-mode Navier--Stokes referee

Use the exact same-replica one-mode packets already audited.  Their active
`z`-residual / `y`-Brownian coefficients are

\[
q_0=-\frac{4k^3e^{-\nu k^2t}}{\pi^2},
\qquad
q_1=+\frac{4k^3e^{-\nu k^2t}}{\pi^2}=-q_0.
\]

Hence the pre-event selected continuous q.v. rate is

\[
\Gamma_-^{\rm cont}
=
\frac{32\nu k^6e^{-2\nu k^2t}}{\pi^4}
\,e_ze_z^T.
\]

Now use the same specified hidden-germ current synthesis as in the simultaneous-event
audit,

\[
g_1\mapsto g_1+g_0,
\]

and switch `0 -> 1`.

If one performs the **selector switch only** and ignores the hidden physical event,
then `q_1=-q_0` gives exactly the same diagonal q.v. rate before and after:

\[
\Gamma_{\rm selector-only,+}^{\rm cont}
=
\Gamma_-^{\rm cont}.
\]

But the actual post-event Brownian response is

\[
q_1+q_0=0,
\]

so

\[
\boxed{\Gamma_+^{\rm cont}=0.}
\]

Therefore the actual rate revaluation is

\[
\boxed{
\Gamma_+^{\rm cont}-\Gamma_-^{\rm cont}
=-\frac{32\nu k^6e^{-2\nu k^2t}}{\pi^4}e_ze_z^T.
}
\]

The exact left/right/quadratic pair faces are respectively

\[
-G,
\qquad
-G,
\qquad
+G,
\]

with

\[
G=\frac{32\nu k^6e^{-2\nu k^2t}}{\pi^4}e_ze_z^T,
\]

and they sum to `-G` exactly.

Thus a selector-only q.v.-rate update misses a physical event that is invisible in
the old selected diagonal but cancels the new selected Brownian response through
cross-germ same-replica structure.

**Classification: Audited exact-Navier--Stokes calibration / rigorous hidden-event necessity.**

## 6. Updated hybrid ledger

For a supplied same-clock path with specified finite linear packet events, the
selected residual now has the following exact typed ledger:

- **continuous interval state:** selected martingale driven by the active block of the
  common same-replica noise response;
- **continuous q.v. rate:** positive semidefinite selected Gram on each frozen
  interval;
- **finite state event:** `DeltaY=(E_+A-E_-)X_-`;
- **optional q.v. atom:** `DeltaY DeltaY^T`;
- **continuous-source rate revaluation:** signed full-pair difference between the
  pre/post selected Gram rates;
- **finite second-moment revaluation:** signed left/right/quadratic event faces on the
  persistent full pair state.

These are not interchangeable names for one scalar payment.

**Classification: Rigorous conditional composition of exact identities.**

## 7. Remaining first-bad frontier

The stochastic/event algebra is exact once the physical library, common replica,
selector path, and finite packet maps are supplied.  What remains Open-literal is
still the actual Navier--Stokes first-bad instantiation:

- badness functional and resolve predicate;
- event times;
- actual persistent candidate packet library;
- actual physical packet event maps;
- support locality/conditioning;
- relation of this same-replica clock to the future-bank/ancestry clock.

**Status: Open-literal at actual first-bad library/timing/event/clock instantiation.**

No restart/continuation/regularity theorem claimed.


---

## 8. Own-local target-gradient extension

The formula `B_+=E_+A\mathcal N` is exact only when the event is genuinely linear in the residual/noise state.  For own-local targets,

\[
\boxed{\mathcal N_+=A\mathcal N_-+N_{\rm target},\qquad N_{\rm target}=AG_- - G_+.}
\]

Thus the post-event Gram contains the base pushed Gram, two signed cross faces with `N_target`, and the positive `N_target N_target^T` face.  A pure reanchor can change continuous q.v. even with `A=I`.

**Classification: Exact affine/noise scope correction.**
