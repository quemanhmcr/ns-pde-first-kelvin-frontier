# Reverse-age co-deforming Kelvin martingale core

## Scope

The previous audit derived the exact physical reconstructed residual law

\[
dr=-A_0r\,d\sigma+\sqrt{2\nu}\,\widehat Q\,dW,
\qquad A_0=\nabla u(X).
\]

This note does **not** estimate that equation.  Instead it follows the local reverse
material line frame itself and asks what the residual looks like in the coordinates
that the actual PDE supplies.

Let

\[
\boxed{\dot L=-A_0L}
\]

be the local reverse-age line frame and

\[
J=\det L,
\qquad
H=\operatorname{cof}(L)=J L^{-T}.
\]

For incompressible Navier--Stokes, `J` is constant along the material reverse-age
segment.  The remarkable consequence is that the local vorticity, the finite Kelvin
residual, and the full normalized circulation all become **driftless same-anchor
martingales** in this co-deforming frame.  Their complete second-moment dynamics is
one Gram matrix of physical Brownian responses.

This is a same-clock full-state theorem.  It is not the future-remaining covariance
bank, not an ancestry resolution bank, and not a continuation/regularity theorem.

---

## 1. Incompressibility freezes the material reference volume

From

\[
\dot L=-A_0L
\]

Jacobi's formula gives

\[
\dot J
=J\operatorname{tr}(L^{-1}\dot L)
=-J\operatorname{tr}A_0.
\]

Since Navier--Stokes is incompressible,

\[
\boxed{\operatorname{tr}A_0=0,\qquad \dot J=0.}
\]

Thus material reverse deformation changes shape but not the reference-volume factor
`J`.  Any physical refinement that changes `J` is a separate refinement/reset face,
not material incompressible evolution.

**Status: Exact identity.**

---

## 2. Orientation error, physical residual, and co-deforming residual are one exact triangle

Let `K` be the orientation-complete vector of actual finite closed-current
circulations and define the local-frame orientation error

\[
\varepsilon=K-H^T\omega.
\]

The physical reconstructed residual is

\[
r=H^{-T}\varepsilon.
\]

Because

\[
H^{-T}=J^{-1}L,
\]

we obtain

\[
\boxed{r=L\chi,}
\qquad
\boxed{\chi:=L^{-1}r=J^{-1}\varepsilon.}
\]

Now define

\[
\boxed{\eta=L^{-1}\omega,}
\qquad
\boxed{\kappa=J^{-1}K.}
\]

Since

\[
H^T=J L^{-1},
\]

one has the exact decomposition

\[
\boxed{\chi=\kappa-\eta,}
\qquad
\boxed{\kappa=\eta+\chi.}
\]

For `J=1` this becomes especially transparent:

\[
\boxed{\chi=\varepsilon.}
\]

So the orientation-coordinate error was already the fully co-deforming physical
residual coordinate.  Reconstruction `epsilon -> r` inserts the material line frame;
pulling `r` back by the same line frame returns `epsilon`.

**Status: Exact cofactor/line-frame identity.**

---

## 3. Local vorticity is a driftless reverse-age co-deforming martingale

The reverse-age vorticity SDE is

\[
d\omega
=-A_0\omega\,d\sigma
+\sqrt{2\nu}(\nabla\omega)dW.
\]

Differentiating the inverse line frame,

\[
\frac d{d\sigma}L^{-1}=L^{-1}A_0.
\]

Therefore

\[
\begin{aligned}
d\eta_{\rm FV}
&=(L^{-1}A_0)\omega\,d\sigma
+L^{-1}(-A_0\omega)\,d\sigma\\
&=0.
\end{aligned}
\]

Define

\[
\boxed{\widetilde G=L^{-1}\nabla\omega.}
\]

Then

\[
\boxed{
d\eta=\sqrt{2\nu}\,\widetilde G\,dW.
}
\]

All local affine vortex stretching has canceled in the co-deforming coordinates.
It has not disappeared from physical space; it lives in the map `omega=L eta`.

**Status: Exact Navier--Stokes / material-frame identity.**

---

## 4. The finite residual is also a driftless martingale

The previous dynamic audit gave the orientation-coordinate local-frame error

\[
d\varepsilon
=\sqrt{2\nu}\,Q\,dW,
\qquad
Q=A_K-H^T\nabla\omega,
\]

with zero finite-variation drift.

Since `J` is constant,

\[
\chi=J^{-1}\varepsilon
\]

obeys

\[
\boxed{
d\chi
=\sqrt{2\nu}\,\widetilde Q\,dW,
\qquad
\widetilde Q=J^{-1}Q.
}
\]

The full normalized finite circulation

\[
\kappa=J^{-1}K
\]

is likewise a driftless Kelvin martingale:

\[
\boxed{
d\kappa
=\sqrt{2\nu}\,\widetilde A_K\,dW,
\qquad
\widetilde A_K=J^{-1}A_K.
}
\]

The noise responses satisfy exactly

\[
\boxed{
\widetilde A_K
=\widetilde G+\widetilde Q.
}
\]

Thus the whole finite/current-to-local split is now a split of **martingale response**,
not a split of affine drift.

**Status: Exact identity.**

---

## 5. One joint Gram matrix contains local, residual, and cross q.v.

Stack the two driftless vectors:

\[
Y=
\begin{bmatrix}
\eta\\
\chi
\end{bmatrix},
\qquad
\mathcal Q=
\begin{bmatrix}
\widetilde G\\
\widetilde Q
\end{bmatrix}.
\]

Then

\[
\boxed{
dY=\sqrt{2\nu}\,\mathcal Q\,dW.}
\]

The exact joint q.v. tensor is

\[
\boxed{
\Gamma_Y
=2\nu\mathcal Q\mathcal Q^T
=
\begin{bmatrix}
\Gamma_\eta & \Gamma_{\eta\chi}\\
\Gamma_{\eta\chi}^T & \Gamma_\chi
\end{bmatrix},
}
\]

where

\[
\boxed{
\Gamma_\eta=2\nu\widetilde G\widetilde G^T,
\quad
\Gamma_\chi=2\nu\widetilde Q\widetilde Q^T,
\quad
\Gamma_{\eta\chi}=2\nu\widetilde G\widetilde Q^T.
}
\]

The full normalized circulation has

\[
\boxed{
\Gamma_\kappa
=\Gamma_\eta+
\Gamma_\chi+
\Gamma_{\eta\chi}+
\Gamma_{\eta\chi}^T.
}
\]

Only the **full block matrix** is manifestly a Gram tensor.  The mixed block is signed
and can cancel the positive diagonal blocks.

**Status: Exact Itô / Gram identity.**

---

## 6. All co-deforming dyad dynamics are q.v.-only

Because `eta`, `chi`, and `kappa` have zero drift,

\[
\boxed{
\frac d{d\sigma}[\eta\eta^T]_{\rm drift}
=\Gamma_\eta,
}
\]

\[
\boxed{
\frac d{d\sigma}[\chi\chi^T]_{\rm drift}
=\Gamma_\chi,
}
\]

and

\[
\boxed{
\frac d{d\sigma}[\eta\chi^T]_{\rm drift}
=\Gamma_{\eta\chi}.
}
\]

Therefore

\[
\boxed{
\frac d{d\sigma}[\kappa\kappa^T]_{\rm drift}
=\Gamma_\kappa.
}
\]

No affine strain term remains in these coordinates.

For the residual scalar energy,

\[
\boxed{
\frac d{d\sigma}\frac12|\chi|^2\Big|_{\rm drift}
=\nu\|\widetilde Q\|_F^2\ge0.
}
\]

This positivity is a property of the **co-deforming coordinate energy**.  It is not a
positive physical-energy bank in fixed coordinates.

**Status: Exact Itô identity.**

---

## 7. Physical residual strain is exactly metric work of the pushforward

The physical residual is

\[
r=L\chi.
\]

Even though `chi` has no affine drift, `L` does:

\[
\dot L=-A_0L.
\]

Therefore

\[
\frac d{d\sigma}\frac12|r|^2\Big|_{\rm drift}
=
\chi^TL^T\dot L\chi
+
u\|L\widetilde Q\|_F^2.
\]

Since `r=L chi`, the first term is

\[
\chi^TL^T(-A_0L)\chi
=-r\cdot S_0r,
\]

and hence

\[
\boxed{
\frac d{d\sigma}\frac12|r|^2\Big|_{\rm drift}
=-r\cdot S_0r
+\nu\|L\widetilde Q\|_F^2.
}
\]

This is exactly the physical residual-energy law already derived.

So the signed strain term is not removed by co-deforming coordinates.  It is
**retyped exactly as metric/frame work** when the driftless residual coordinate is
pushed back to physical space.

**Status: Exact identity / physical metric-work typing.**

---

## 8. Mean bias and covariance spread are rigorously separate

For a driftless same-clock martingale,

\[
\boxed{
\frac d{d\sigma}\mathbb E[\chi]=0.
}
\]

Thus

\[
\boxed{
\mathbb E[\chi_\sigma]=\chi_0.
}
\]

The deterministic/conditional mean bias is preserved along this reverse-age
martingale family.

Meanwhile, under the usual square-integrability needed for the Itô second-moment
identity,

\[
\boxed{
\frac d{d\sigma}\mathbb E[\chi\chi^T]
=\mathbb E[\Gamma_\chi],
}
\]

and because the mean is constant,

\[
\boxed{
\frac d{d\sigma}\operatorname{Cov}(\chi)
=\mathbb E[\Gamma_\chi].
}
\]

This is an exact bias-versus-spread decomposition.

It gives a sharp warning:

> a q.v./covariance bank can measure stochastic spread while being completely blind
> to a nonzero persistent mean finite-shape bias.

**Status: Exact martingale consequence under square-integrability.**

---

## 9. Exact cubic NS referee: nonzero mean bias, zero q.v.

For the exact cubic heat shear

\[
u=(y^3+6\nu ty,0,0)
\]

at the symmetry point and unit coherent frame,

\[
\boxed{
\chi=-\frac14e_z\neq0.
}
\]

The residual martingale coefficient vanishes:

\[
\boxed{\widetilde Q=0.}
\]

Hence

\[
\boxed{
\chi_\sigma\equiv\chi_0,
\qquad
\Gamma_\chi=0,
\qquad
\operatorname{Cov}(\chi)=0.
}
\]

This is stronger than merely saying covariance is small: the stochastic spread is
exactly zero while the finite reconstructed bias is nonzero.

**Status: Audited calibration (exact Navier--Stokes) / rigorous covariance-only no-go.**

---

## 10. Exact one-mode full-period referee: cross q.v. cancels both positive diagonals

Take the exact periodic one-mode shear

\[
u=(e^{-\nu k^2t}\cos ky,0,0).
\]

Choose an `xy` finite face whose `y` width is one full period,

\[
2b=\frac{2\pi}{k}.
\]

The actual finite circulation through that face is exactly zero for every anchor:

\[
\boxed{K_z=0.}
\]

Choose the coherent third line length equal to one.  Then

\[
\kappa_z=0,
\qquad
\boxed{\chi_z=-\eta_z.}
\]

Consequently their Brownian responses satisfy

\[
\boxed{\widetilde q_z=-\widetilde g_z.}
\]

Thus

\[
\Gamma_\eta=2\nu\widetilde g_z^2>0,
\qquad
\Gamma_\chi=2\nu\widetilde g_z^2>0,
\]

but

\[
\boxed{
\Gamma_{\eta\chi}
=-2\nu\widetilde g_z^2<0.
}
\]

Therefore

\[
\boxed{
\Gamma_\kappa
=\Gamma_\eta+\Gamma_\chi+2\Gamma_{\eta\chi}=0.
}
\]

The full finite circulation has zero q.v. only because the signed cross block exactly
cancels the two positive diagonal q.v. contributions.

This face spans a full periodic direction and is **not a local first-bad packet**.  It
is used only as an exact mechanism calibration proving that local/residual diagonal
payments cannot be separated from cross content.

**Status: Audited calibration (exact periodic Navier--Stokes) / rigorous cross-block
necessity.**

---

## 11. Reverse age and the existing backward physical-time operator have opposite source signs

The repository already proved, in a physical-time backward-Kelvin operator notation,

\[
\mathscr D_K^-(\eta\eta^T)
=-\widetilde{\mathcal G}_K.
\]

The present reverse-age SDE gives

\[
\frac d{d\sigma}[\eta\eta^T]_{\rm drift}
=+\widetilde{\mathcal G}_K.
\]

These are not competing formulas.  They have **opposite source signs** because reverse age increases as the physical time coordinate moves backward.  Thus the same q.v. coefficient appears with the opposite clock orientation:

\[
\boxed{
\text{reverse-age source}
+
\text{backward physical-time source}
=0.
}
\]

This exact sign reconciliation does **not** identify the reverse-age residual
covariance with the future covariance bank.  The future bank has its own terminal
conditioning and clock semantics, already audited separately.

**Status: Exact clock-orientation identity.**

---

## 12. What the simple law does and does not buy

The surface/current complexity has now collapsed, on the full same-clock state, to a
small exact system:

\[
\boxed{
\begin{aligned}
d\eta &=\sqrt{2\nu}\,\widetilde G\,dW,\\
d\chi &=\sqrt{2\nu}\,\widetilde Q\,dW,\\
d\kappa&=\sqrt{2\nu}(\widetilde G+\widetilde Q)\,dW,
\end{aligned}}
\]

with one joint Gram matrix and no affine drift.  Thus `eta`, `chi`, and `kappa` are **driftless same-anchor martingales** on this smooth reverse-age material segment, and their local/residual noise is carried by **one full Gram tensor** including the signed cross blocks.

But this simplicity does **not** prove local descent:

- the mean bias `E chi` is conserved, not dissipated;
- cubic NS can have nonzero `chi` with zero q.v.;
- cross q.v. can cancel positive diagonals completely;
- recovering physical residual `r=L chi` reintroduces material strain/geometry;
- support locality and conditioning remain separate physical requirements;
- selector/refinement/boundary/exit/reset faces remain outside this smooth material
  segment;
- reduced covariance closure remains unproved;
- future-clock/ancestry identification remains unproved; in particular this same-clock martingale covariance is **not the future-remaining covariance bank**.

**Status: Exact same-clock full-state martingale core; first-bad/reduction/cross-clock
bridges remain Open-literal/Open.**

---

## 13. First-bad target requires physical frame weighting

The martingale core identifies the exact same-clock variables, but **raw `chi` is
not yet the physical descent topology**.  The physical reconstructed residual is

\[
\boxed{r=L\chi.}
\]

Exact quadratic and one-mode Navier--Stokes calibrations in
`weighted_codeforming_kelvin_residual_audit.md` show that raw mean bias and raw
codeforming q.v. can remain order one while the physical residual and physical q.v.
shrink to zero.  Thus demanding `E chi -> 0` and `Cov(chi) -> 0` was a sufficient-looking
but unnecessarily strong target.

The corrected literal first-bad object is the frame-weighted full-state energy

\[
\boxed{\mathbb E[\chi^TL^TL\chi],}
\]

including the mixed metric--residual correlation when `L` is random.  Support
locality, selector/refinement/boundary/exit/reset faces, and cross-clock
identification remain separate.

**Status: theorem-target correction; weighted physical collapse remains
Open-literal/Open.  No restart/continuation/regularity theorem claimed.**
