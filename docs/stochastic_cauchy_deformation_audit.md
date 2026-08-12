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

## 9. Literal reverse-age state and the two deformation connections

Fix the current endpoint `(x,t)` and use causal reverse age

\[
\sigma\in[0,h],
\qquad
r_\sigma=t-\sigma.
\]

For the standard back-to-label convention used by the stochastic Cauchy
representation, the literal augmented state is

\[
\boxed{
\begin{aligned}
dX_\sigma
&=-u(X_\sigma,r_\sigma)\,d\sigma
 +\sqrt{2\nu}\,dW_\sigma,\\
\partial_\sigma D_\sigma
&=D_\sigma A(X_\sigma,r_\sigma)^T,
\qquad
A:=\nabla u,
\qquad D_0=I.
\end{aligned}}
\]

The deformation has **no direct Brownian differential**.  In particular

\[
\boxed{[D_{ij},D_{k\ell}]_\sigma=0}
\]

pathwise.  Its randomness is inherited from evaluating the finite-variation
coefficient `A` along the noisy anchor `X`.

For column-major vectorization

\[
z:=\operatorname{vec}D,
\]

the pathwise equation is

\[
\boxed{
\partial_\sigma z
=K_{\rm path}z,
\qquad
K_{\rm path}=A\otimes I,
}
\]

because

\[
\operatorname{vec}(DA^T)
=(A\otimes I)\operatorname{vec}D.
\]

That is **not** the connection appearing when one differentiates a conditional
horizon from the current endpoint.  Define the current-end reverse-age horizon
operator

\[
\boxed{
\mathcal H_h
:=
\partial_h+\partial_t+u\cdot\nabla-\nu\Delta
=
\partial_h-\mathcal L_{\rm rev},
}
\]

where

\[
\mathcal L_{\rm rev}
=-\partial_t-u\cdot\nabla+\nu\Delta.
\]

Let

\[
\bar D(h,x,t):=\mathbb E_{x,t}[D_h].
\]

Splitting off the **first** reverse-age increment gives

\[
D_h
=
\big(I+A(x,t)^T\,d\sigma+o(d\sigma)\big)
D_{h-d\sigma}^{\rm shifted}.
\]

Therefore the conditional mean obeys

\[
\boxed{
\mathcal H_h\bar D
=A^T\bar D,
\qquad
\bar D(0,x,t)=I.
}
\]

After vectorization,

\[
\bar z:=\operatorname{vec}\bar D,
\]

this becomes

\[
\boxed{
\mathcal H_h\bar z
=B\bar z,
\qquad
B=I\otimes A^T.
}
\]

So there are two exact but physically different orderings:

\[
\boxed{
K_{\rm path}=A\otimes I,
\qquad
B_{\rm horizon}=I\otimes A^T.
}
\]

The first is the pathwise finite-variation evolution `D_sigma=D A^T`; the second
is the connection generated by conditioning from the fixed current endpoint.  CI
contains a noncommuting symbolic guard so these two operators cannot be silently
identified.

**Status: Exact identity.**

---

## 10. General second-moment and covariance laws

Define the row-Gram second moment

\[
\boxed{
R(h,x,t):=\mathbb E[D_hD_h^T].
}
\]

The same first-increment composition gives the exact connected law

\[
\boxed{
\mathcal H_hR
=A^TR+RA,
\qquad
R(0)=I.
}
\]

Now define the **row-Gram deformation covariance**

\[
\boxed{
C_D^{\rm Gram}
:=R-\bar D\bar D^T
=\mathbb E[(D-\bar D)(D-\bar D)^T].
}
\]

The diffusion product rule is

\[
\mathcal H_h(\bar D\bar D^T)
=(\mathcal H_h\bar D)\bar D^T
+\bar D(\mathcal H_h\bar D)^T
-2\nu\sum_\mu
(\partial_\mu\bar D)(\partial_\mu\bar D)^T.
\]

Subtracting from the second-moment law yields

\[
\boxed{
\mathcal H_h C_D^{\rm Gram}
=A^TC_D^{\rm Gram}+C_D^{\rm Gram}A
+2\nu\sum_\mu
(\partial_\mu\bar D)(\partial_\mu\bar D)^T,
\qquad
C_D^{\rm Gram}(0)=0.
}
\]

This `3 x 3` tensor is useful because it is exactly the covariance face that appears
in the averaged packet metric, but it is **not** the full covariance of a matrix-valued
random variable.

For the full deformation covariance set

\[
\boxed{
\Sigma_D
:=
\operatorname{Cov}(\operatorname{vec}D)
=\mathbb E[(z-\bar z)(z-\bar z)^T]
\in\mathbb R^{9\times9}.
}
\]

Let

\[
Q_D^{\rm vec}:=\mathbb E[zz^T].
\]

Then

\[
\boxed{
\mathcal H_h Q_D^{\rm vec}
=BQ_D^{\rm vec}+Q_D^{\rm vec}B^T
}
\]

and

\[
\boxed{
\mathcal H_h\Sigma_D
=B\Sigma_D+\Sigma_DB^T
+\Gamma_D^{\rm vec},
}
\]

with the full mixed carré-du-champ

\[
\boxed{
\Gamma_D^{\rm vec}
=2\nu\sum_\mu
\operatorname{vec}(\partial_\mu\bar D)
\operatorname{vec}(\partial_\mu\bar D)^T.
}
\]

The row-Gram covariance is the exact column partial trace

\[
\boxed{
(C_D^{\rm Gram})_{ik}
=
\sum_j
(\Sigma_D)_{(i,j),(k,j)}.
}
\]

Consequently the projected carré-du-champ is exactly

\[
\boxed{
\operatorname{ptr}_{\rm col}\Gamma_D^{\rm vec}
=2\nu\sum_\mu
(\partial_\mu\bar D)(\partial_\mu\bar D)^T.
}
\]

For two conditionally independent replicas with the same current ancestor/state,

\[
\boxed{
\Sigma_D
=
\frac12\mathbb E[
(z^{(1)}-z^{(2)})(z^{(1)}-z^{(2)})^T
].
}
\]

Projecting gives

\[
\boxed{
C_D^{\rm Gram}
=
\frac12\mathbb E[
(D^{(1)}-D^{(2)})(D^{(1)}-D^{(2)})^T
].
}
\]

Thus the pair structure is exact before any norm or scalar contraction.

Finally, same-replica packet-metric duality

\[
\rho^4M_H=DD^T
\]

gives

\[
\boxed{
\rho^4\mathbb E[M_H]
=\bar D\bar D^T+C_D^{\rm Gram}.
}
\]

So the stochastic packet metric sees precisely the **row-Gram projection** of the
full vectorized deformation covariance.

**Status: Exact identity.  PSD and pair-positivity statements are Rigorous
consequences.**

---

## 11. Short-horizon law: the candidate is the projected tensor, not the full covariance

At a smooth current point `(x,t)`, write

\[
A_0:=\nabla u(x,t).
\]

The mean equation gives

\[
\bar D(h,x,t)
=I+hA_0^T+O(h^2),
\]

hence

\[
\boxed{
\partial_\mu\bar D
=h(\partial_\mu A_0)^T+O(h^2).
}
\]

Therefore

\[
\Gamma_D^{\rm vec}
=
2\nu h^2
\sum_\mu
v_\mu v_\mu^T
+O(h^3),
\qquad
v_\mu:=\operatorname{vec}((\partial_\mu A_0)^T).
\]

Since `Sigma_D(0)=0`, the connection and spatial-transport terms acting on
`Sigma_D` enter one order later than the leading source.  Integrating the exact
covariance equation gives

\[
\boxed{
\Sigma_D(h)
=
\frac{2\nu}{3}h^3
\sum_\mu
\operatorname{vec}((\partial_\mu\nabla u)^T)
\operatorname{vec}((\partial_\mu\nabla u)^T)^T
+O(h^4).
}
\]

This is the general vectorized law.

Taking the column partial trace gives

\[
\boxed{
C_D^{\rm Gram}(h)
=
\frac{2\nu}{3}h^3
\sum_\mu
(\partial_\mu\nabla u)^T
(\partial_\mu\nabla u)
+O(h^4).
}
\]

Therefore the proposed expression

\[
\frac{2\nu}{3}h^3
\sum_\mu
(\partial_\mu\nabla u)^T(\partial_\mu\nabla u)
\]

is **correct for the row-Gram projection** `C_D^Gram`.  It is not by itself the full
`9 x 9` covariance `Sigma_D`.

The physical onset is cubic because

1. anchor Brownian displacement is `O(sqrt(nu h))`;
2. a spatial gradient of `A=grad u` converts this into random strain/rotation-gradient
   sampling of size `O(sqrt(nu h))`;
3. deformation integrates that random coefficient once in reverse age, adding `h`;
4. covariance squares the result, giving `O(nu h^3)`.

No norm estimate is used in this derivation.

**Status: Rigorous consequence of the exact covariance law for locally smooth
Navier--Stokes coefficients.**

---

## 12. Exact one-mode shear referees sign, transpose, source, and `2 nu / 3`

Use the exact periodic Navier--Stokes shear

\[
\boxed{
u=(e^{-\nu k^2t}\cos ky,0,0).}
\]

In the active plane

\[
A
=
\begin{pmatrix}
0&U_y\\
0&0
\end{pmatrix},
\qquad
U_y=-k e^{-\nu k^2t}\sin(ky).
\]

The stochastic deformation is exactly

\[
\boxed{
D_h=I+c_hE_{21},
\qquad
c_h=\int_0^h U_y(Y_\sigma,t-\sigma)\,d\sigma,
}
\]

with

\[
Y_\sigma=y+\sqrt{2\nu}\,W_\sigma.
\]

The exact mean is

\[
\boxed{
\mathbb E[c_h]
=-kh e^{-\nu k^2t}\sin(ky)
=hU_y(y,t).
}
\]

Writing `alpha=nu k^2`, the exact second moment is

\[
\boxed{
\begin{aligned}
\mathbb E[c_h^2]
={}&
\frac{k^2e^{-2\alpha t}}{4\alpha^2}
\Big[
 e^{2\alpha h}-1-2\alpha h\\
&\qquad
-\cos(2ky)
 (e^{-2\alpha h}-1+2\alpha h)
\Big].
\end{aligned}}
\]

CI checks this closed form against the exact two-time Gaussian kernel.

More strongly, with

\[
\mathcal H_h=\partial_h+\partial_t-\nu\partial_{yy}
\]

on the shear-dependent entries, the exact formulas satisfy

\[
\boxed{
\mathcal H_h\bar D=A^T\bar D,
}
\]

\[
\boxed{
\mathcal H_hR=A^TR+RA,
}
\]

and

\[
\boxed{
\mathcal H_hC_D^{\rm Gram}
=A^TC_D^{\rm Gram}+C_D^{\rm Gram}A
+2\nu(\partial_y\bar D)(\partial_y\bar D)^T.
}
\]

Here

\[
C_D^{\rm Gram}
=\operatorname{Var}(c_h)e_2e_2^T,
\]

and the connection annihilates the active covariance direction, so the last equation
reduces exactly to

\[
\boxed{
\mathcal H_h\operatorname{Var}(c_h)
=2\nu h^2|\partial_yU_y|^2.
}
\]

Its Taylor expansion is

\[
\boxed{
\operatorname{Var}(c_h)
=
\frac{2\nu}{3}
|\partial_yU_y(y,t)|^2 h^3
+O(h^4).
}
\]

This simultaneously referees

- the positive sign of the carré-du-champ source;
- the left horizon connection `A^T bar D`;
- the transpose in `(partial_mu A)^T(partial_mu A)`;
- the coefficient `2 nu / 3`.

At the symmetry anchor `y=0`,

\[
\bar D=I,
\]

while

\[
\boxed{
\operatorname{Var}(c_h)
=
\frac{k^2e^{-2\alpha t}}{2\alpha^2}
\left[\sinh(2\alpha h)-2\alpha h\right]
>0
}
\]

for every `h>0`.

**Status: Audited calibration (exact periodic Navier--Stokes solution).**

---

## 13. Physical typing and placement in the pair/future/resolution ledger

The new law has to be typed at three different levels.

### A. It is not pathwise deformation q.v.

Pathwise,

\[
[D,D]=0.
\]

The carré-du-champ in the horizon covariance PDE is produced by the Brownian
**anchor** acting on the spatially varying conditional mean `bar D`.  It is the
infinitesimal law-of-total-covariance source generated when the current endpoint is
conditioned one reverse-age step at a time.  Calling it direct martingale q.v. of `D`
would be physically wrong.

**Status: Exact identity / Rigorous consequence.**

### B. `Sigma_D` is a full same-clock covariance sector; `C_D^Gram` is its projection

The repo already contains a general **connected vector covariance theorem**.  Its
horizon convention is

\[
(\partial_\tau-L)m+B_{\rm conn}^T m=0,
\]

and

\[
(\partial_\tau-L)C+B_{\rm conn}^TC+CB_{\rm conn}
=\Gamma[m].
\]

For deformation, take the literal reverse-age generator on current variables

\[
L_{\rm rev}=-\partial_t-u\cdot\nabla+\nu\Delta
\]

and the exact sign/order identification

\[
\boxed{
B_{\rm conn}
=-B_{\rm horizon}^T
=-\big(I\otimes A^T\big)^T.
}
\]

Then the existing connected theorem becomes exactly

\[
\mathcal H_h\bar z=B_{\rm horizon}\bar z,
\qquad
\mathcal H_h\Sigma_D
=B_{\rm horizon}\Sigma_D+\Sigma_DB_{\rm horizon}^T
+\Gamma_D^{\rm vec}.
\]

So the covariance **algebraic face is already present** in the repo; the new content is
the literal Cauchy-deformation payload, reverse-age connection ordering, and physical
clock semantics.  The existing product-pair diagonal-defect theorem also gives
exactly `Gamma_D^vec`; the deformation connection is homogeneous pair transport and
does not manufacture a new branching source.  The exact one-mode shear is now a
cross-module symbolic referee for all three statements: connected mean, connected
second moment/covariance, and pair diagonal defect.

But the `3 x 3` tensor entering the packet metric is only

\[
C_D^{\rm Gram}=\operatorname{ptr}_{\rm col}\Sigma_D.
\]

Thus the object previously called simply `C_D` was overtyped if read as the full
matrix-valued covariance.  The corrected theorem keeps the full `9 x 9` covariance
and labels the packet-metric object as its row-Gram projection.

**Status: Exact identity.**

### C. It is not automatically the existing future-remaining bank or resolution covariance

The present clock is the **causal past horizon**

\[
h=t-s.
\]

It is not the future remaining horizon

\[
\tau=\Theta-t.
\]

The equations have the same covariance algebra, but no clock identification is made.
Therefore this deformation sector is structurally an instance of the same general
covariance theorem, not a proof that it is the repo's future-remaining covariance
bank.

Likewise, `Sigma_D` is not automatically the ancestry **resolution covariance**.
Once an explicit reduced/full conditional lift kernel `R(y,dY)` is supplied, however,
the vector law of total covariance is exact.  If

\[
\bar z(Y)=\mathbb E[\operatorname{vec}D\mid Y],
\qquad
\Sigma_D(Y)=\operatorname{Cov}(\operatorname{vec}D\mid Y),
\]

then at the reduced state `y`,

\[
\boxed{
\Sigma_D^{\rm red}(y)
=
R\Sigma_D(y)
+
\operatorname{Cov}_R(\bar z)(y).
}
\]

The first term is the averaged **intrinsic same-clock deformation covariance** already
present on the full state.  The second is the genuinely additional **resolution
covariance** created by hiding full-state deformation information.  It has its own
exact hidden-state pair form

\[
\boxed{
\operatorname{Cov}_R(\bar z)
=
\frac12\mathbb E_{R\otimes R}
[(\bar z_1-\bar z_2)(\bar z_1-\bar z_2)^T].
}
\]

Column partial trace commutes with this decomposition, so the packet-metric face at
the reduced level is

\[
\boxed{
C_{D,\rm red}^{\rm Gram}
=
R C_D^{\rm Gram}
+
\operatorname{ptr}_{\rm col}\operatorname{Cov}_R(\bar z).
}
\]

Thus reduction does **not** retype intrinsic `Sigma_D` as resolution covariance; it
adds a second covariance sector.  What remains open-literal is not this algebra but
the programme-specific construction/identification of the actual ancestry lift
kernel and its state semantics.

No part of `Sigma_D`, `C_D^Gram`, or the new resolution term is renamed `S^int`,
`Z_irr`, or “irreducible.”  That identification has not been proved.

**Status: Exact identity** for the connected-theorem specialization and vector
law-of-total-covariance/pair decomposition.  **Status: Conjectural bridge /
Open-literal** for cross-clock identification and for constructing the actual
programme-specific reduced/full ancestry lift.

### D. Deterministic selected packet is still a different object

At `y=0` in the exact shear, the deterministic material trajectory remains on the
symmetry line and has

\[
D_{\rm det}=I.
\]

The stochastic replicas have

\[
\rho^4\mathbb E[M_H]
=I+\operatorname{Var}(c_h)e_2e_2^T.
\]

Hence the universal equality

\[
\text{deterministic selected packet metric}
=
\mathbb E[\text{stochastic replica packet metric}]
\]

is false even for a smooth exact periodic Navier--Stokes solution.

A conditional projection/coupling theorem could still exist, but it must retain the
deformation covariance sector rather than deleting it.

**Status: Audited calibration for the no-go; Conjectural bridge / Open-literal for
a nontrivial selected-support coupling.**

---

## 14. Genuine affine-vortex NS calibration: growth with zero centered covariance

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

## 15. One-mode NS shear: covariance active with no vorticity-direction stretching

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

## 16. Fixed-past `Q_tot` is not a free finite reservoir

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

## 17. Relation to the support×bank factorization

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

## 18. Updated obstruction ledger

For a fixed smooth past time `s`, current vorticity amplification may enter through:

1. actual terminal vorticity amplitude `W_s` — finite once `s` is fixed;
2. stochastic Cauchy deformation `D` and its second moment `R_s`;
3. full vectorized deformation covariance `Sigma_D` and its row-Gram projection
   `C_D^Gram`;
4. terminal directional correlation/headroom `W_sR_s-Q_s`;
5. centered stochastic Cauchy-payoff covariance `C_s=Q_s-mm^T`;
6. state/projection mismatch between this full physical bank and the repo ancestry
   state;
7. finite-shape/localization, moving-cut, exit, and reset faces;
8. lack of a physical first-bad badness/resolve theorem.

No item is silently renamed `S^int`.

**Classification: Exact/rigorous physical typing; global exhaustiveness remains
open.**

---

## 19. Updated next target

The general deformation-covariance law is now structural rather than heuristic:

\[
\mathcal H_h\Sigma_D
=B\Sigma_D+\Sigma_DB^T+\Gamma_D^{\rm vec},
\]

with `C_D^Gram` its exact row-Gram projection and with the cubic onset calibrated by
an exact periodic Navier--Stokes shear.

The next PDE-first questions are therefore downstream of this theorem, not substitutes
for it:

- can the same-ancestor deformation pair field be coupled to the physical current/pair
  cochain without collapsing `Sigma_D` to a scalar norm?
- under an explicit reduced ancestry lift, which part of deformation covariance is
  retained as ordinary observable covariance and which additional part is genuine
  resolution covariance?
- can any deterministic first-bad selected packet be related to the stochastic
  deformation ensemble by a conditional projection/coupling that survives the exact
  shear no-go?
- only after those identifications are exact: is there any structurally natural
  estimate near the singular frontier?

Audit markers: **full vectorized deformation covariance**, **row-Gram projection**,
**finite-variation deformation**, **anchor carré-du-champ**, **causal past horizon**,
**connected vector covariance theorem**, **vector law of total covariance**,
**additional resolution covariance**, **two-replica**, **terminal directional headroom**,
**naive equality no-go**, **Open-literal selected-support coupling**,
and **No continuation/restart theorem**.

`S^int`, badness/resolve definitions, cross-clock identification, support--Cauchy
state alignment, uniform collapse, restart capacity, and continuation remain open.

**Status: Exact identity / Rigorous consequence for the covariance law; Open-literal
for the remaining restart bridges.**


---

## 20. Physical-current/pair coupling refinement

The next coupling layer is now audited in `docs/deformation_current_pair_coupling_audit.md`.  On a fixed selected closed cycle, the local current lift is `P tensor D^T`; incidence boundary and spatial deformation act on different fibers, so deformation cannot manufacture a boundary seam.  Fixed tangent/cochain observations are exact projections of `Sigma_D`.  Replica-dependent selectors introduce a distinct selector sector and mandatory selector--deformation cross pair terms.  Exact cubic NS simultaneously blocks any inference that `D` alone closes the finite-current state.

**Status: Exact local fiber/pair identities plus Audited calibration; full finite-current/state lift remains Open-literal.**
