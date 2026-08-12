# Fixed-past stochastic Cauchy deformation and total-bank envelope audit

This note continues the causal repair of the support×bank route.  Instead of trying
to force the future remaining time into the physical backward-Kelvin covariance,
fix a genuine past terminal `s<t` and inspect the **literal stochastic Cauchy
invariant** that represents current vorticity.

The resulting anatomy is sharper than the informal statement "past vorticity is
smooth, so the future/total bank is bounded."  Past vorticity amplitude is only one
factor.  The other is a stochastic deformation matrix that can stretch and rotate
the terminal vector before averaging.

Primary representation context: the stochastic Cauchy invariant used here is the
standard backward stochastic vorticity representation of Constantin--Iyer type;
Eyink--Gupta--Zaki, arXiv:1912.06677, equations (2.37), (2.39), and (2.51)--(2.52)
write the backward-flow deformation and the random invariant explicitly.

No global deformation bound, restart theorem, or regularity conclusion is claimed.

---

## 1. Literal fixed-past payoff

For current point/time `(x,t)` and fixed past time

\[
s<t,
\]

let `A_s^t(x)` be the stochastic back-to-label position and let `D_s^t(x)` denote
the stochastic Cauchy deformation matrix appearing in the vorticity
representation.  The random terminal contribution is

\[
\boxed{
Y_s(x,t)
=D_s^t(x)\,\omega(A_s^t(x),s).
}
\]

The backward martingale representation gives

\[
\boxed{
\mathbb E[Y_s(x,t)]=\omega(x,t).
}
\]

Thus define

\[
m:=\mathbb E Y_s=\omega(x,t),
\]

\[
\boxed{
Q_s:=\mathbb E[Y_sY_s^T],
}
\]

and

\[
\boxed{
C_s:=Q_s-mm^T\succeq0.
}
\]

`Q_s` is the literal fixed-past total second moment.  `C_s` is only its centered
stochastic-covariance sector.

**Physical classification:** stochastic Cauchy total second moment = resolved
current vorticity dyad + centered stochastic cancellation/resolution content.

**Classification: Exact stochastic representation identity, conditional on the
standard smooth backward-Kelvin representation.**

---

## 2. Smooth past vorticity does not remove deformation

Because `s` is strictly before a candidate singular time, a smooth solution has a
finite terminal amplitude

\[
\boxed{
W_s:=\sup_y|\omega(y,s)|^2<\infty.
}
\]

For each stochastic sample write

\[
w_s=\omega(A_s^t(x),s),
\qquad
Y=Dw_s.
\]

Samplewise,

\[
\boxed{
W_sDD^T-YY^T
=D(W_sI-w_sw_s^T)D^T.
}
\]

Since

\[
w_sw_s^T\preceq |w_s|^2I\preceq W_sI,
\]

the right side is positive semidefinite.

Define the stochastic deformation second moment

\[
\boxed{
R_s(x,t):=\mathbb E[D_s^t(D_s^t)^T].
}
\]

Averaging gives

\[
\boxed{
Q_s\preceq W_sR_s.
}
\]

Therefore

\[
\boxed{
\omega(x,t)\omega(x,t)^T
\preceq Q_s(x,t)
\preceq W_sR_s(x,t).
}
\]

The first inequality is covariance positivity.  The second is terminal smoothness
**times stochastic deformation**.

Hence the false shortcut is

> fixed-past vorticity is bounded, therefore the total bank is bounded.

The correct statement is

> fixed-past vorticity is bounded, therefore any remaining sufficient envelope is a
> stochastic Cauchy deformation-moment problem.

**Classification: Rigorous Loewner consequence.**

---

## 3. Exact two-face gap

There is an exact decomposition of the gap between the sufficient deformation
envelope and the resolved mean dyad:

\[
\boxed{
W_sR_s-mm^T
=
(W_sR_s-Q_s)
+
(Q_s-mm^T).
}
\]

The two terms have different physical types.

### A. Terminal directional headroom

\[
\boxed{
W_sR_s-Q_s
=
\mathbb E\!\left[
D(W_sI-w_sw_s^T)D^T
\right].
}
\]

This records deformation in directions not fully occupied by the actual terminal
vorticity vector/amplitude.  It quantifies how loose the scalar terminal supremum
`W_s` is.

### B. Stochastic covariance

\[
\boxed{
Q_s-mm^T=C_s.
}
\]

This is the usual stochastic spread/cancellation of Cauchy-invariant samples around
the current mean vorticity.

Thus `R_s` must not be identified with `Q_s`, and `Q_s` must not be identified with
centered covariance `C_s`.

**Classification: Exact tensor identity and exact physical typing.**

---

## 4. Deformation is finite variation but physically active

Use reverse age

\[
\sigma=t-s.
\]

With the convention of the stochastic Cauchy deformation matrix above, the
backward-flow Jacobian algebra gives

\[
\boxed{
\partial_\sigma D
=D(\nabla u)^T
}
\]

along each stochastic trajectory.  There is no direct Brownian differential in
`D`: uniform translational Brownian noise has zero spatial gradient.  Randomness
enters because `grad u` is sampled along the random anchor path.

For the pathwise deformation Gram tensor

\[
G_D=DD^T,
\]

one obtains

\[
\boxed{
\partial_\sigma G_D
=2DSD^T,
\qquad
S=\frac12(\nabla u+\nabla u^T).
}
\]

Averaging,

\[
\boxed{
\partial_\sigma R_s
=2\mathbb E[DSD^T].
}
\]

This equation is generally **not closed on `R_s` alone** because strain and
stochastic deformation are correlated along the back trajectories.

**Physical classification:** finite-variation stochastic deformation/strain work,
not martingale q.v. and not centered covariance production.

**Classification: Exact pathwise identity and exact ensemble hierarchy law.**

---

## 5. Incompressibility preserves stochastic volume but not deformation energy

Pathwise,

\[
\partial_\sigma\log\det D
=\operatorname{tr}(\nabla u)
=0
\]

for incompressible Navier--Stokes.  Thus

\[
\boxed{
\det D=1
}
\]

when normalized at the current end of the backward interval.

But

\[
\partial_\sigma(DD^T)=2DSD^T
\]

can have large positive principal growth.  Volume preservation therefore does not
bound the deformation second moment.

This is the stochastic analogue of the deterministic long-thin material-cell
phenomenon already audited: fixed determinant does not prevent severe anisotropy.

**Classification: Exact incompressible deformation identity.**

---

## 6. Same-replica Cauchy deformation is exactly the coherent packet metric

The stochastic Cauchy deformation does not introduce a new kind of anisotropy.
Define the forward deformation dual to the backflow Cauchy matrix by

\[
\boxed{F_{\rm C}:=D^T.}
\]

Since

\[
\partial_\sigma D=D(\nabla u)^T,
\]

we have

\[
\boxed{
\partial_\sigma F_{\rm C}
=(\nabla u)F_{\rm C}.
}
\]

Thus `F_C` obeys the ordinary line-deformation law on that same stochastic replica.

Now attach a coherent isotropic microcell of reference linear scale `rho` to this
same deformation.  Its material area frame is

\[
\boxed{
H_{\rm C}
=\rho^2F_{\rm C}^{-T}.
}
\]

The packet metric is

\[
M_{H_{\rm C}}
=(H_{\rm C}^TH_{\rm C})^{-1}.
\]

Direct algebra gives

\[
\boxed{
D D^T
=F_{\rm C}^TF_{\rm C}
=\rho^4M_{H_{\rm C}}.
}
\]

Therefore the stochastic Cauchy deformation Gram tensor is exactly the **unscaled
coherent Kelvin packet metric** on the same stochastic deformation replica.

This identifies two structures that had entered the programme from different
routes:

- the packet metric measuring material anisotropy/stretching;
- the stochastic Cauchy deformation tensor controlling the fixed-past total-bank
  envelope.

They are the same right Cauchy--Green geometry, before expectation.

The spatial support tensor

\[
F_{\rm C}F_{\rm C}^T
\]

and the material metric

\[
F_{\rm C}^TF_{\rm C}=DD^T
\]

have the same singular values, trace, and determinant pathwise, although their
principal directions live in different frames.

**Classification: Exact same-replica primal/dual deformation identity.**

---

## 7. Packet-metric work and Cauchy deformation work are the same strain law

For fixed reference scale `rho`, the duality gives

\[
\rho^4 M_H=DD^T.
\]

Hence

\[
\boxed{
\rho^4\partial_\sigma M_H
=2DSD^T.
}
\]

The exact pathwise Cauchy deformation work of Section 4 is therefore the same
packet-metric/anisotropy work already seen in the orientation-complete restart
packet.

Averaging,

\[
\boxed{
R_s
=\rho^4\,\mathbb E[M_{H_{\rm C}}].
}
\]

for a common fixed reference scale on the replica ensemble.

Thus the sufficient fixed-past envelope can be written as

\[
\boxed{
Q_s
\preceq
W_s\rho^4\,\mathbb E[M_{H_{\rm C}}].
}
\]

This is not a norm invented after the fact.  It is the exact expectation of the
same packet metric forced by Nanson/current geometry.

**Classification: Exact same-replica metric identity and rigorous covariance
envelope consequence.**

---

## 8. What this does and does not align

The identity above closes the geometry **inside one stochastic Kelvin replica**.
It does not yet identify

- the deterministic/hysteretic first-bad selected material packet used by the
  restart selector, with
- the stochastic replica packet `H_C` generated by a backward Cauchy ancestor.

Those objects can follow different anchor histories.  A programme-specific theorem
must still say whether the selected packet is

1. one stochastic replica,
2. an expectation/projection of replicas,
3. a deterministic material packet coupled to them through a conditional kernel,
   or
4. something else.

Therefore `selected-support-cauchy-deformation-alignment` remains open-literal even
though the same-replica metric duality is exact.

**Classification: Exact local/state identity; cross-state selector/replica alignment
Open-literal.**

---

## 9. Genuine affine-vortex NS calibration: growth with zero centered covariance

Use the previously audited exact affine Navier--Stokes flow

\[
\nabla u=A(t)
=
\begin{pmatrix}
-a&-r(t)&0\\
r(t)&-a&0\\
0&0&2a
\end{pmatrix},
\qquad
r(t)=r_0e^{2at},
\]

with its quadratic pressure cancellation.  Its vorticity is spatially uniform:

\[
\boxed{
\omega(t)=(0,0,2r_0e^{2at}).
}
\]

Because the velocity gradient and vorticity are spatially uniform, anchor Brownian
sampling does not randomize either quantity.  Along the vorticity direction, the
Cauchy deformation from past `s` to current `t` is

\[
\boxed{
D_z(s,t)=e^{2a(t-s)}.
}
\]

Therefore

\[
\boxed{
D_z(s,t)\,\omega_z(s)=\omega_z(t)
}
\]

pathwise.

Consequently

\[
\boxed{C_s=0}
\]

for this calibration, while

\[
Q_{zz}=|\omega_z(t)|^2
=W_sR_{zz}
\]

in the active vorticity direction.

Thus positive vortex stretching can be carried entirely by deterministic/stochastic
Cauchy deformation with **zero centered covariance**.

This independently reinforces the earlier mean-vs-covariance referee correction.

**Classification: Exact genuine 3D Navier--Stokes calibration.**

---

## 10. One-mode NS shear: covariance active with no vorticity-direction stretching

For the exact periodic one-mode shear,

\[
\omega_z(y,t)=k e^{-\nu k^2t}\sin(ky),
\]

vortex stretching vanishes.  The Cauchy deformation factor in the `z` vorticity
direction is therefore `1`.

At fixed past terminal `s`,

\[
W_s=k^2e^{-2\nu k^2s}.
\]

The exact past-payoff second moment is

\[
\boxed{
Q_{zz}(y,t;s)
=
\frac{W_s}{2}
\left[
1-e^{-4\nu k^2(t-s)}\cos(2ky)
\right].
}
\]

Hence

\[
\boxed{
W_s-Q_{zz}
=
\frac{W_s}{2}
\left[
1+e^{-4\nu k^2(t-s)}\cos(2ky)
\right]\ge0.
}
\]

Here the deformation envelope is simply `R_zz=1`, while centered future/past
sampling covariance is nontrivial.

Thus the affine-vortex and one-mode-shear calibrations isolate opposite limiting
mechanisms:

- affine vortex: deformation active, centered covariance zero;
- shear: vorticity-direction deformation absent, stochastic covariance active.

**Classification: Exact Navier--Stokes calibration pair.**

---

## 11. Fixed-past `Q_tot` is not a free finite reservoir

The fixed-past second moment has a real advantage: its terminal time is causal and
fixed.  But its amplitude contains the stochastic deformation accumulated between
`s` and `t`.

A sufficient scalar principal envelope is

\[
\boxed{
\lambda_{\max}(Q_s)
\le
W_s\,\lambda_{\max}(R_s).
}
\]

Since `W_s` is finite at every fixed smooth past time, a blow-up of this sufficient
envelope can only come through the stochastic deformation second moment.

However this bound is not necessary: `W_sR_s-Q_s` may be large when deformation
occurs in directions poorly occupied by terminal vorticity.  The exact directional
headroom term must be kept if one wants a sharp theorem.

So the fixed-past route has not solved the restart problem; it has **typed its bank
obstruction more precisely**.

**Classification: Rigorous sufficient envelope and exact sharpness caveat.**

---

## 12. Relation to the support×bank factorization

The scale-parametric support×bank theorem needs a same-state total second moment
`Q_tot`.  A fixed-past stochastic Cauchy bank is a physically legitimate candidate,
but only after the support deformation/frame and the Cauchy deformation state are
identified line by line.

If that alignment is established, the sufficient replacement

\[
Q_s\preceq W_sR_s
\]

would convert the total-bank envelope problem into a coupled geometry problem:

\[
\boxed{
\text{selected material support}
\times
\text{stochastic Cauchy deformation moment}.
}
\]

This is more physical than a raw vorticity norm but is not yet controlled.

In particular, the repo has not proved that the deterministic/coherent packet
`F` used by the first-bad support geometry is the same deformation object, or a
closed projection of the same object, as the random Cauchy deformation `D` used by
the fixed-past stochastic bank.

**Classification: Conjectural/programme-specific alignment bridge after exact
component identities.**

---

## 13. Updated obstruction ledger

For a fixed smooth past time `s`, current vorticity amplification may enter through:

1. actual terminal vorticity amplitude `W_s` — finite once `s` is fixed;
2. stochastic Cauchy deformation `D` and its second moment `R_s`;
3. terminal directional correlation/headroom `W_sR_s-Q_s`;
4. centered stochastic covariance `C_s=Q_s-mm^T`;
5. state/projection mismatch between this full physical bank and the repo ancestry
   state;
6. finite-shape/localization, moving-cut, exit, and reset faces;
7. lack of a physical first-bad badness/resolve theorem.

No item is silently renamed `S^int`.

**Classification: Exact/rigorous physical typing; global exhaustiveness remains
open.**

---

## 14. Updated next target

The most concrete next mathematical object is now

\[
\boxed{
R_s(x,t)=\mathbb E[D_s^t(D_s^t)^T].
}
\]

The PDE-first questions are:

- can its strain hierarchy be localized by the same orientation-complete packet
  geometry already used for vorticity?
- does pair/common-noise structure force useful correlations between deterministic
  selected support and stochastic deformation replicas?
- can first-bad refinement keep the product of selected support and the relevant
  **directional** Cauchy deformation content controlled without replacing it by a
  crude scalar norm?

Those questions remain open.

Audit markers: **stochastic Cauchy deformation**, **terminal directional headroom**,
**centered covariance**, **Open** deformation control, and **No continuation**.

`S^int`, badness/resolve definitions, support--Cauchy state alignment, uniform
collapse, restart capacity, and continuation remain open.

**Classification: Structural advance; no regularity conclusion.**
