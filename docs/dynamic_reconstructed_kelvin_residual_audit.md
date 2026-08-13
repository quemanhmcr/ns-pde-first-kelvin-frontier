# Dynamic reconstructed Kelvin residual audit

## Scope

The previous fixed-state audit identified

\[
r_H=H^{-T}\varepsilon_H
\]

as the physical vector reconstructed from an orientation-complete finite Kelvin
remainder.  This note asks the next literal question: **how does that reconstructed
vector move on the actual reverse-age Kelvin state?**

No norm estimate is introduced.  We keep separately:

- the actual finite closed-current circulations;
- the local reverse cofactor frame;
- the local vorticity;
- the actual finite-area geometry;
- the local-frame finite-to-local error;
- the reconstructed physical residual;
- all local/residual cross quadratic variation.

The result is another rigid NS law: the orientation-coordinate local-frame error is a
pure Kelvin martingale, while its reconstructed physical vector carries exactly the
reverse material-line connection `-grad u`.

No future-clock, ancestry, first-bad, restart, continuation, or regularity theorem is
claimed.

---

## 1. Two finite-to-local errors must not be conflated

For one actual finite spanning surface/current, let

\[
K
\]

be its closed-current Kelvin circulation, let `h_R` be its **actual finite oriented
area vector**, and let `h` be the corresponding column of the **local reverse
cofactor frame**.

There are two different errors.

### Actual-area vorticity-inhomogeneity error

\[
\boxed{
\varepsilon_{\rm area}
=K-\omega(X)\cdot h_R.
}
\]

By exact Stokes,

\[
\varepsilon_{\rm area}
=\int_{\Sigma_R}[\omega(X+r)-\omega(X)]\cdot n\,dA.
\]

Its exact reverse-age drift, already audited, is

\[
\boxed{
\dot\varepsilon_{\rm area}^{\rm FV}
=-\omega(X)\cdot\mathcal R_A,
}
\]

where

\[
\dot h_R=A_0^Th_R+\mathcal R_A,
\qquad A_0=\nabla u(X).
\]

### Local-frame finite-to-local error

\[
\boxed{
\varepsilon_{\rm lin}
=K-\omega(X)\cdot h.
}
\]

Here

\[
\boxed{
\dot h=A_0^Th.
}
\]

and therefore

\[
\boxed{
\varepsilon_{\rm lin}
=\varepsilon_{\rm area}
+\omega(X)\cdot(h_R-h).
}
\]

These are different physical observables.  The first isolates vorticity
inhomogeneity on the actual finite area; the second measures the entire finite
circulation defect relative to the local affine/Nanson frame.

**Status: Exact identity / physical typing.**

---

## 2. The finite-variation shape drift transfers; it does not disappear

Define

\[
\delta h=h_R-h.
\]

Then

\[
\boxed{
\dot{\delta h}=A_0^T\delta h+\mathcal R_A.
}
\]

Reverse-age Navier--Stokes gives

\[
d\omega=-A_0\omega\,d\sigma
+\sqrt{2\nu}\,\nabla\omega\,dW.
\]

Hence the finite-variation drift of the geometry-mismatch flux is

\[
\begin{aligned}
\frac d{d\sigma}[\omega\cdot\delta h]_{\rm FV}
&=(-A_0\omega)\cdot\delta h
+\omega\cdot(A_0^T\delta h+\mathcal R_A)\\
&=\boxed{\omega\cdot\mathcal R_A}.
\end{aligned}
\]

Therefore

\[
\boxed{
(-\omega\cdot\mathcal R_A)
+(+\omega\cdot\mathcal R_A)=0.
}
\]

The shape drift has not been discarded.  It is an exact transfer between

1. the actual-area vorticity-inhomogeneity error; and
2. the finite-area versus local-frame geometry mismatch.

Consequently the local-frame error has zero finite-variation drift.

**Status: Exact Navier--Stokes/Nanson transfer identity.**

---

## 3. The noise transfers in the same way

Let `a_mu(K)` be the actual finite-current Kelvin martingale coefficient.  For one
face,

\[
q_\mu^{\rm area}
=a_\mu(K)-\partial_\mu\omega\cdot h_R.
\]

The geometry-mismatch flux contributes

\[
q_\mu^{\rm geom}
=\partial_\mu\omega\cdot(h_R-h).
\]

Thus

\[
\boxed{
q_\mu^{\rm area}+q_\mu^{\rm geom}
=a_\mu(K)-\partial_\mu\omega\cdot h
=:q_\mu^{\rm lin}.
}
\]

So drift and noise transfers are two faces of the same change of local target.

**Status: Exact identity.**

---

## 4. Orientation-complete local-frame error is a pure Kelvin martingale

Now collect three actual closed-current circulations into

\[
K\in\mathbb R^3
\]

and their local area vectors as the columns of an invertible frame

\[
H=[h_1\ h_2\ h_3].
\]

The local vorticity-flux vector is

\[
\boxed{
\Phi=H^T\omega.
}
\]

The reverse local cofactor law is

\[
\boxed{
\dot H=A_0^TH.
}
\]

Using `d omega=-A_0 omega dsigma+sqrt(2nu) grad omega dW`, the local flux drift is

\[
\dot H^T\omega+H^T(-A_0\omega)
=H^TA_0\omega-H^TA_0\omega=0.
\]

The actual closed-current Kelvin drift is also zero because the NS one-form drift is
an exact Bernoulli/pressure gauge.

Therefore for

\[
\boxed{
\varepsilon:=K-H^T\omega
}
\]

one has the exact pathwise SDE

\[
\boxed{
d\varepsilon
=\sqrt{2\nu}\,Q\,dW,
\qquad
Q=A_K-H^T\nabla\omega,
}
\]

where the columns of `A_K` are the actual finite-current martingale coefficients.

Thus `epsilon` is a pure martingale **in orientation coordinates**.  This does not say
the physical finite shape has no finite-variation dynamics; Section 2 shows exactly
where that dynamics has transferred.

**Status: Exact closed-current Kelvin / local Nanson identity.**

---

## 5. Reconstruction produces exactly the reverse material-line connection

Define

\[
\boxed{
W=H^{-T}K,
\qquad
r=H^{-T}\varepsilon=W-\omega.
}
\]

Differentiate the inverse transpose of the local area frame:

\[
\frac d{d\sigma}H^{-T}
=-H^{-T}\dot H^TH^{-T}.
\]

Since

\[
\dot H^T=H^TA_0,
\]

one gets

\[
\boxed{
\frac d{d\sigma}H^{-T}
=-A_0H^{-T}.
}
\]

Therefore the reconstructed actual finite Kelvin payoff obeys

\[
\boxed{
dW
=-A_0W\,d\sigma
+\sqrt{2\nu}\,\widehat A_K\,dW_{\rm B},
\qquad
\widehat A_K=H^{-T}A_K,
}
\]

and the reconstructed residual obeys

\[
\boxed{
dr
=-A_0r\,d\sigma
+\sqrt{2\nu}\,\widehat Q\,dW_{\rm B},
\qquad
\widehat Q=H^{-T}Q.
}
\]

The local vorticity itself obeys

\[
\boxed{
d\omega
=-A_0\omega\,d\sigma
+\sqrt{2\nu}\,(\nabla\omega)\,dW_{\rm B}.
}
\]

Hence `W`, `omega`, and `r=W-omega` all carry the **same reverse material-line
connection `-A_0`**.  Their distinction is in their martingale response matrices.

For incompressible coherent geometry, `H=cof(L)=L^{-T}` and therefore
`H^{-T}=L`.  Orientation-coordinate `epsilon` is the line-frame coordinate of the
physical residual `r`.

**Status: Exact identity / physical connection theorem.**

---

## 6. Reconstructed q.v. and local--residual cross q.v.

The residual q.v. tensor is

\[
\boxed{
\Gamma_r
=2\nu\,\widehat Q\widehat Q^T.
}
\]

The local vorticity q.v. tensor is

\[
\boxed{
\Gamma_\omega
=2\nu(\nabla\omega)(\nabla\omega)^T.
}
\]

Because the same Brownian anchor drives both, their cross q.v. is

\[
\boxed{
\Gamma_{\omega r}
=2\nu(\nabla\omega)\widehat Q^T.
}
\]

This cross block is signed and need not vanish.

The full reconstructed finite-payoff noise matrix is

\[
\widehat A_K
=\nabla\omega+\widehat Q,
\]

and therefore

\[
\boxed{
\Gamma_W
=\Gamma_\omega
+\Gamma_r
+\Gamma_{\omega r}
+\Gamma_{\omega r}^T.
}
\]

This is the dynamic q.v. analogue of the fixed-state covariance cross-block identity.
Deleting the cross blocks is not an identity.

**Status: Exact Itô/q.v. identity.**

---

## 7. Exact dyad law of the physical reconstructed residual

From

\[
dr=-A_0r\,d\sigma+\sqrt{2\nu}\,\widehat Q\,dW
\]

Itô gives

\[
\boxed{
\frac{d}{d\sigma}[rr^T]_{\rm drift}
=-A_0rr^T-rr^TA_0^T+\Gamma_r.
}
\]

Taking half the trace, with

\[
S_0=\frac12(A_0+A_0^T),
\]

gives

\[
\boxed{
\frac{d}{d\sigma}\frac12|r|^2\Big|_{\rm drift}
=-r\cdot S_0r
+\nu\|\widehat Q\|_F^2.
}
\]

The two terms are physically different:

- `-r.S.r` is signed reverse material-strain work on the reconstructed vector;
- `nu ||Qhat||_F^2` is positive anchor q.v. injection.

Thus reconstructed residual energy is not a monotone positive "bank" by itself.

**Status: Exact Itô identity.**

---

## 8. Exact local--residual cross dyad law

The mixed dyad obeys

\[
\boxed{
\frac d{d\sigma}[\omega r^T]_{\rm drift}
=-A_0\omega r^T
-\omega r^TA_0^T
+\Gamma_{\omega r}.
}
\]

The transpose gives the other cross face.

Since

\[
W=\omega+r,
\]

one has exactly

\[
\boxed{
WW^T
=\omega\omega^T
+rr^T
+\omega r^T
+r\omega^T,
}
\]

and the full drift decomposes into the four corresponding drift laws.  In particular, **both cross blocks** and both cross q.v. sources are mandatory.

So the cross blocks are mandatory both:

1. algebraically at fixed-state covariance level; and
2. dynamically at pathwise dyad/q.v. level.

**Status: Exact identity.**

---

## 9. Exact cubic heat-shear referee: a nonzero conserved reconstructed mode

For

\[
u=(y^3+6\nu ty,0,0)
\]

at `y=0`, the unit centered `xy` face has the already audited finite reconstructed
residual

\[
\boxed{
r=-\frac14e_z.
}
\]

The local velocity gradient is

\[
A_0=6\nu t\,e_x\otimes e_y.
\]

Therefore

\[
A_0r=0.
\]

The cubic centered residual is also Brownian-anchor blind at this symmetry point, so

\[
\widehat Q=0.
\]

Hence

\[
\boxed{
dr=0,
\qquad
\Gamma_r=0,
\qquad
\frac d{d\sigma}|r|^2=0.
}
\]

This is the dynamic version of the earlier covariance-blind no-go: a nonzero
finite-scale reconstructed residual can be an exact conserved mode.

**Status: Audited calibration (exact Navier--Stokes) / rigorous no-go consequence.**

---

## 10. Exact periodic one-mode shear referee: residual martingale and cross q.v. are active

For

\[
u=(e^{-\nu k^2t}\cos ky,0,0),
\]

the centered finite `xy` rectangle has reconstructed residual along `e_z`.
The local shear connection maps only `e_y` into `e_x`, so

\[
A_0e_z=0.
\]

Thus this residual has no connection drift:

\[
\boxed{dr_z=\sqrt{2\nu}\,\widehat q_y\,dW_y.}
\]

The exact finite-horizon variance previously derived satisfies

\[
\boxed{
\partial_h\operatorname{Var}(r_z)|_{h=0}
=2\nu(\partial_y\varepsilon_0)^2,
}
\]

which is exactly the reconstructed q.v. rate.

Meanwhile local vorticity has

\[
\partial_y\omega_z=-U_{yy},
\]

so

\[
\boxed{
(\Gamma_{\omega r})_{zz}
=2\nu(-U_{yy})\,\partial_y\varepsilon_0,
}
\]

which is generically nonzero.  The local/residual cross q.v. is therefore a real
exact-NS channel, not merely generic matrix algebra.

**Status: Audited calibration (exact periodic Navier--Stokes).**

---

## 11. What is closed, and what is not

The following are now exact on the literal full reverse-age current/local-frame state:

- local-frame error is a pure orientation-coordinate martingale;
- physical reconstruction has connection `-A_0`;
- residual q.v., energy and dyad laws;
- local/residual cross q.v. and cross dyad laws;
- full reconstructed q.v./dyad block decomposition;
- actual-area shape drift transfers exactly into geometry mismatch when changing the
  local target.

But an autonomous equation for a **reduced centered covariance `C_r` alone** has not
been proved.  In general the drift contains full-state correlations such as

\[
\mathbb E[A_0rr^T]
\]

and the q.v. coefficient depends on the full finite current shape through `A_K`.
The existing connected-covariance theorem applies on a declared full Markov state;
reducing/hiding that state can add resolution covariance, as already audited.

Therefore the pathwise dyad law must not be silently rewritten as a closed covariance
PDE on `(x,H)` or on a first-bad reduced state.

**Status: Exact full-state pathwise law; Reduced covariance closure Open-literal.**

---

## 12. Placement relative to the future covariance bank

The present dynamics use the actual reverse-age causal-past Kelvin state.  They do
not identify

\[
r_H
\]

with the future-remaining covariance bank or with an ancestry resolution residual.

The theorem instead tells us what any such bridge would have to preserve:

1. the material-line connection `-A_0` of reconstructed vectors;
2. the actual finite-current martingale coefficient;
3. local/residual cross q.v.;
4. geometry-mismatch transfer;
5. selector/boundary/exit/reset faces;
6. the clock orientation.

**Status: Exact same-clock dynamics; future-clock/ancestry identification Open-literal.**

---

## 13. Refined first-bad target

There are now three independent literal questions:

### Physical support descent

Does the actual selected finite current become support-local with controlled
conditioning?

### Instantaneous reconstructed Kelvin descent

Does

\[
r_H=H^{-T}(K-H^T\omega)
\]

tend to zero on that actual current?

### Dynamic residual control

Do the exact terms

\[
-r\cdot S r,
\qquad
\Gamma_r,
\qquad
\Gamma_{\omega r}
\]

and the full finite-current coefficient remain controllable under the actual moving
selector/refinement/boundary/exit dynamics?

The exact cubic calibration shows `Gamma_r=0` does not imply `r=0`.  The exact
one-mode calibration shows the local/residual cross q.v. can be active.  Therefore a
first-bad argument cannot replace these objects by a single positive covariance
payment.

**Status: Open-literal/Open.  No restart/continuation/regularity theorem claimed.**

---

## 14. Pulling the physical residual back one more time removes all affine strain

With `Ldot=-A L`, `J=det L` constant by incompressibility, and `H=cof(L)`, define

\[
\eta=L^{-1}\omega,
\qquad
\chi=L^{-1}r=J^{-1}\varepsilon,
\qquad
\kappa=J^{-1}K=\eta+\chi.
\]

Then all three are driftless reverse-age martingales.  Their complete local/residual
second-moment system is the one Gram matrix of the stacked noise response
`[L^-1 grad omega; Q/J]`.  The physical strain term in the `r` energy law is exactly
the metric work of the pushforward `r=L chi`.

This gives a strict bias/spread separation: `E chi` is constant while
`Cov(chi)` grows only by the residual q.v. tensor.  Exact cubic NS has nonzero
constant `chi` with zero q.v.; an exact one-mode full-period face has positive local
and residual diagonal q.v. that cancel completely through a negative cross q.v.,
leaving the full circulation q.v. zero.

**Status: Exact same-clock co-deforming martingale identity / audited exact-NS
calibrations.  First-bad bias collapse, reduced covariance closure, and future-clock
identification remain Open-literal/Open.**

See `docs/reverse_codeforming_kelvin_martingale_audit.md`.
