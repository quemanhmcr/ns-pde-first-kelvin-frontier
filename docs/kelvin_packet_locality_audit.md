# Kelvin packet locality and metric-whitened Stokes audit

This note repairs a locality gap identified by the independent adversarial audit
`docs/adversarial_audit_2026-08-12.md`.  The repair is PDE-first: distinguish
oriented area, spatial support, and metric-normalized covariance before making any
small-loop limit.

No estimate toward continuation is inserted here.  No regularity theorem is
claimed.

---

## 1. General Nanson first, incompressibility second

For a general three-dimensional material area frame `H`, Nanson gives

\[
\boxed{
D_tH=[(\nabla\!\cdot u)I-(\nabla u)^T]H.
}
\]

Let

\[
M_H=(H^TH)^{-1}.
\]

Then

\[
D_t\log\det H=2\nabla\!\cdot u,
\]

and therefore

\[
\boxed{
D_t\log\det M_H=-4\nabla\!\cdot u.
}
\]

For incompressible Navier--Stokes this reduces to

\[
\boxed{D_t\det M_H=0.}
\]

The older helper `material_area_frame_rhs` is already specialized to
`div u=0`, where it reads `D_tH=-(grad u)^T H`.  Its determinant conclusion was
correct on that domain; only the wording of a general determinant-rate formula was
too broad.

**Classification: Exact Nanson identity and exact incompressible consequence.**

---

## 2. Small area is not spatial locality

Let an isotropic reference packet have linear scale `r`, and let `F` be its material
deformation gradient.  In the incompressible case `det F=1`, the oriented area
frame is

\[
\boxed{H_r=r^2F^{-T}.}
\]

Take the exact incompressible deformation

\[
F_r=\operatorname{diag}(r^{-1},1,r),
\qquad \det F_r=1.
\]

Then

\[
\boxed{H_r=\operatorname{diag}(r^3,r^2,r)\to0.}
\]

Nevertheless a reference `r x r` face in the stretched/compressed directions
becomes a `1 x r^2` face: its diameter remains order one.

For an isotropic reference packet the largest transported line scale is encoded by

\[
\boxed{
\ell_{\max}(H_r)
=
\frac{\sqrt{\det H_r}}{\sigma_{\min}(H_r)}.
}
\]

For the long-thin witness,

\[
\ell_{\max}=1.
\]

By contrast, for the bounded incompressible deformation

\[
F=\operatorname{diag}(2,1,1/2),
\]

one has

\[
H_r=\operatorname{diag}(r^2/2,r^2,2r^2),
\qquad
\ell_{\max}=2r\to0.
\]

Thus `H -> 0` and `support diameter -> 0` are different statements.

**Classification: Exact incompressible kinematic counterexample and exact diagonal
singular-value identity.**

---

## 3. A coherent microcell reconstructs primal line geometry from `H`

For a coherent oriented material microcell let the columns of

\[
L=(\ell_1,\ell_2,\ell_3)
\]

be its three primal material edge vectors.  Its dual face-area frame is

\[
\boxed{H=\operatorname{cof}L=(\det L)L^{-T}.}
\]

For positive orientation this relation is invertible:

\[
\boxed{
L=\sqrt{\det H}\,H^{-T}.
}
\]

Hence the complete primal line Gram matrix is

\[
\boxed{
G_{\rm line}=L^TL
=(\det H)(H^TH)^{-1}
=(\det H)M_H.
}
\]

So the adversarial long-thin example does **not** mean that the full coherent area
frame forgets support geometry.  It means that the smallness of its entries or its
face areas is the wrong criterion.  The conditioning of `H` reconstructs the primal
line scales exactly.

For

\[
H_r=\operatorname{diag}(r^3,r^2,r),
\]

one recovers

\[
\boxed{L_r=\operatorname{diag}(1,r,r^2),}
\]

so the nonlocal line is visible directly in the dual frame.

In incompressible flow,

\[
D_tL=(\nabla u)L,
\qquad
D_tH=-(\nabla u)^TH,
\]

and

\[
\boxed{
D_tG_{\rm line}
=L^T[(\nabla u)^T+\nabla u]L
=2L^TSL.
}
\]

Since `det H` is constant along an incompressible material segment,

\[
D_tG_{\rm line}=(\det H)D_tM_H.
\]

Thus the packet metric that measures vortex-stretching work is also, up to the
material cell determinant, the literal Gram metric of the primal material lines.
Support stretching and vorticity metric work are two physical readings of the same
material geometry.

**Classification: Exact cofactor duality and exact material-line/area kinematics.**

---

## 4. Smooth covariance sees the nonlocal long-thin packet

Let

\[
W(x)=X\cos(x_1)e_2,
\qquad
\mathbb E X=0,
\qquad
\mathbb E X^2=1.
\]

Consider

\[
\Sigma_r=[-1/2,1/2]\times\{0\}\times[-r^2/2,r^2/2].
\]

Its area vector is

\[
h_r=r^2e_2\to0.
\]

But the exact flux is

\[
\boxed{
\int_{\Sigma_r}W\cdot n\,dA
=
2r^2\sin(1/2)X,
}
\]

whereas the local-center approximation is

\[
r^2X.
\]

The payoff error divided by area is the nonzero constant

\[
\boxed{2\sin(1/2)-1.}
\]

The covariance defect is consequently

\[
\boxed{
\operatorname{Var}(X_{\Sigma_r})
-r^4\operatorname{Var}(W(0)\cdot e_2)
=
[4\sin^2(1/2)-1]r^4,
}
\]

not `o(r^4)`.

**Classification: Exact smooth covariance counterexample to area-only
localization.**

---

## 5. The invariant topology is metric-whitened

For a three-face packet let the flux vector be `X_H` and write

\[
X_H=H^T\zeta(x)+\varepsilon_H.
\]

The scalar packet bank obeys

\[
2\mathcal B_H
=
\operatorname{tr}\!\left[C_H(H^TH)^{-1}\right]
=
\operatorname{tr}\operatorname{Cov}(H^{-T}X_H).
\]

Hence the exact normalized observable is

\[
\boxed{
H^{-T}X_H
=
\zeta(x)+H^{-T}\varepsilon_H.
}
\]

The correct local-tensor remainder condition is therefore

\[
\boxed{
H^{-T}\varepsilon_H\to0
\quad\text{in conditional }L^2,
}
\]

or equivalently at covariance level a metric-whitened contraction such as

\[
\boxed{
\operatorname{tr}
[R_H(H^TH)^{-1}]	o0.
}
\]

Raw Frobenius smallness is insufficient.  In the long-thin witness take

\[
H_r=\operatorname{diag}(r^3,r^2,r),
\qquad
R_r=cr^4e_2e_2^T.
\]

Then the raw ratio tends to zero,

\[
\frac{|R_r|_F^2}{|H_r|_F^2}\to0,
\]

but

\[
\boxed{
\operatorname{tr}[R_r(H_r^TH_r)^{-1}]=c.
}
\]

Likewise the exact whitened payoff error in the smooth long-thin example is

\[
\boxed{
H_r^{-T}\varepsilon_r
=(0,\,2\sin(1/2)-1,\,0)^T,
}
\]

which does not vanish.

**Classification: Exact normalization identity plus rigorous no-go for raw
smallness.**

---

## 6. Repaired fixed-state Stokes theorem

Let `Sigma_{r,j}` be the three packet faces, with oriented area vectors `h_{r,j}`
and area frame `H_r`.  Suppose all faces lie inside a support neighborhood of
diameter `delta_r`.  Let the random terminal vorticity two-form/vector `zeta` have
conditional `L^2` modulus

\[
\omega_2(\delta)
=
\sup_{|y-x|\le\delta}
\|\zeta(y)-\zeta(x)\|_{L^2_s}.
\]

For

\[
\varepsilon_{r,j}
=
\int_{\Sigma_{r,j}}
(\zeta(y)-\zeta(x))\cdot n\,dA,
\]

Minkowski gives

\[
\|\varepsilon_{r,j}\|_{L^2_s}
\le A_{r,j}\omega_2(\delta_r).
\]

Therefore

\[
\boxed{
\|H_r^{-T}\varepsilon_r\|_{L^2_s}
\le
\frac{(\sum_jA_{r,j}^2)^{1/2}}
{\sigma_{\min}(H_r)}
\,\omega_2(\delta_r).
}
\]

A sufficient fixed-state condition for the local covariance tensor is consequently

\[
\boxed{
\delta_r\to0,
\qquad
\frac{(\sum_jA_{r,j}^2)^{1/2}}
{\sigma_{\min}(H_r)}
\omega_2(\delta_r)	o0.
}
\]

Under this condition,

\[
H_r^{-T}X_{H_r}	o\zeta(x)
\quad\text{in conditional }L^2,
\]

and hence

\[
\operatorname{Cov}(H_r^{-T}X_{H_r})
\to
\operatorname{Cov}(\zeta(x)).
\]

For uniformly conditioned, genuinely local centered packets this reduces to the
previous mean-square Stokes limit; for strongly anisotropic packets it exposes the
extra conditioning factor that was previously hidden.

**Classification: Rigorous conditional fixed-state theorem.**

---

## 7. What remains open

At a candidate singular time one must prove simultaneously:

- physical support locality, not merely small area;
- sufficient control of packet conditioning;
- metric-whitened covariance/payoff remainder collapse;
- finite-shape strain-gradient current collapse;
- signed material metric/boundary/exit accounting.

The exact long-thin witness shows that none of the first three can be deleted by
notation.

**Classification: Open singular-time bridge.  No continuation/restart theorem.**

---

## 8. The first finite-size carrier is the same surface quadrupole

For a centered planar face with offset `xi` from its anchor, define

\[
\boxed{
Q_\Sigma=\int_\Sigma \xi\xi^T\,dA.
}
\]

Centering gives `int xi dA=0`, so every linear Taylor correction disappears.
For a velocity-gradient field that is quadratic in `xi`, the finite-surface Nanson
residual is exactly

\[
\boxed{
E_{\rm shape}
=-\frac12\sum_{k\ell}
(Q_\Sigma)_{k\ell}
(\partial_{k\ell}\nabla u)^Tn.
}
\]

For a terminal vorticity/flux field `zeta` quadratic in `xi`, the Stokes payoff
error is exactly

\[
\boxed{
\varepsilon_{\rm flux}
=\frac12\sum_{k\ell}
(Q_\Sigma)_{k\ell}
(\partial_{k\ell}\zeta)\cdot n.
}
\]

Thus finite current-shape drift and finite local-covariance error are not merely two
quantities that happen to scale as `r^2` after normalization.  Their first
centered finite-size carrier is the **same physical surface quadrupole**; only the
PDE field contracted against it differs.

For the centered `yz` rectangle `[-b,b] x [-c,c]`,

\[
(Q_\Sigma)_{yy}=\frac43 b^3c,
\qquad
(Q_\Sigma)_{zz}=\frac43 bc^3.
\]

The exact cubic heat-shear calibration has
`partial_yy (grad u)_{xy}=6`, giving

\[
\boxed{E_{\rm shape}=-4b^3c\,e_y,}
\]

exactly the independently audited surface result.  Under isotropic physical scale
`b=r b_0`, `c=r c_0`, the quadrupole is raw order `r^4`, while
`Q_\Sigma/Area` is order `r^2`.

**Classification: Exact centered quadratic Taylor identities and exact NS
calibration.**

---

## 9. Incompressibility freezes material scale; refinement is the scale-change face

For a coherent material line frame write

\[
L=\rho\widetilde L,
\qquad
\rho=(\det L)^{1/3},
\qquad
\det\widetilde L=1,
\]

and define

\[
\boxed{\mathcal A=\widetilde L^T\widetilde L.}
\]

Then

\[
\boxed{
G_{\rm line}=L^TL=\rho^2\mathcal A,
\qquad
M_H=(H^TH)^{-1}=\rho^{-4}\mathcal A.
}
\]

Thus one unit-determinant anisotropy tensor is read in two physical ways: `rho^2 A`
measures primal material-line geometry, while `rho^-4 A` is the Kelvin packet
covariance metric.

Material line kinematics gives

\[
\boxed{
D_t\log\rho=\frac13\nabla\cdot u.
}
\]

Therefore incompressible Navier--Stokes has

\[
\boxed{D_t\rho=0.}
\]

A fixed material microcell can change shape but cannot continuously collapse its
physical volume-equivalent scale.  A first-bad packet sequence with `rho -> 0` must
therefore obtain its scale change from a **physical refinement/reselection/reset**,
not from ordinary incompressible material transport.

If a physical linear refinement acts by

\[
L^+=L^-R,
\qquad d=\det R>0,
\]

then exactly

\[
\boxed{
\rho^+=\rho^-d^{1/3},
\qquad
\mathcal A^+=d^{-2/3}R^T\mathcal A^-R.
}
\]

For isotropic refinement `R=lambda I`,

\[
\boxed{
ho^+=\lambda\rho^-,\qquad\mathcal A^+=\mathcal A^-.}
\]

For anisotropic refinement, physical scale and shape both change and must be carried
as separate signed/refinement faces.  This operation is not the same physical event
as a passive `GL(3)` change of packet coordinates, even when the matrix algebra looks
similar: the actual current support and its pair covariance have changed.

**Classification: Exact scale/shape factorization, exact incompressible material
kinematics, and exact physical-refinement algebra.**

---

## 10. Material deformation and physical refinement form a two-sided lineage

Let `F_{k+1,k}` be the material deformation between two refinement events and let
`R_k` be the physical linear refinement map on the coherent microcell.  The line
frame obeys

\[
L_{k+1}^-=F_{k+1,k}L_k^+,
\qquad
L_k^+=L_k^-R_k.
\]

Because physical-space deformation acts on the left and cell refinement acts on the
right, a complete lineage factorizes exactly as

\[
\boxed{
L_N=F_{N:0}L_0R_{1:N}.
}
\]

For incompressible material deformation `det F_{N:0}=1`,

\[
\boxed{
\det L_N=\det L_0\det R_{1:N}.
}
\]

Thus all physical scale-determinant loss comes from the refinement/reselection
history, while continuous Navier--Stokes strain changes the shape of the cell.

For an initially isotropic coherent cell and an isotropic cumulative refinement
`R_{1:N}=Lambda I`, define the physical right Cauchy--Green tensor

\[
C_F=F^TF.
\]

Then

\[
\boxed{
G_{\rm line}=\Lambda^2C_F,
\qquad
M_H=\Lambda^{-4}C_F.
}
\]

and

\[
\boxed{
D_tC_F=F^T[(\nabla u)^T+\nabla u]F=2F^TSF.
}
\]

So the complete first-bad geometry has an exact two-factor reading:

- `Lambda` is the physical refinement scale;
- `C_F` is the accumulated material strain geometry.

The same `C_F` determines both the physical support Gram matrix and the Kelvin
metric amplification.  No auxiliary continuation norm is introduced.

**Classification: Exact two-sided material/refinement factorization and exact
Cauchy--Green strain identity.**

---

## 11. Orientation-complete quadrupoles reconstruct spatial support geometry

Let a coherent material microcell have half-edge columns

\[
L=(\ell_1,\ell_2,\ell_3).
\]

For a centered parallelogram face spanned by half-edges `a,b`, direct integration
gives

\[
\boxed{
\frac{Q_\Sigma}{A_\Sigma}
=
\frac13(aa^T+bb^T).
}
\]

Apply this to the three faces dual to `ell_1,ell_2,ell_3`.  Then

\[
\boxed{
\sum_{i=1}^3\frac{Q_i}{A_i}
=
\frac23LL^T.
}
\]

Thus the orientation-complete three-face packet reconstructs the entire **spatial**
line-deformation tensor from its normalized surface quadrupoles.  In an isotropic
refinement lineage `L=Lambda F`,

\[
\boxed{
\sum_i\frac{Q_i}{A_i}
=
\frac23\Lambda^2FF^T,
}
\]

the left Cauchy--Green support tensor.

This is the finite-size analogue of the independently audited fact that three
orientation Kelvin q.v. channels reconstruct the full vorticity-gradient
dissipation.  Orientation completion therefore closes both the infinitesimal q.v.
geometry and, for a coherent microcell, the first centered finite-size support
geometry.

For arbitrary non-coherent finite surfaces the quadrupole is additional physical
shape data; the exact cubic-shear counterexample remains applicable.  The closure is
a coherent-microcell identity, not a license to discard finite shape generally.

**Classification: Exact centered-parallelogram integration and exact
orientation-complete quadrupole closure.**

---

## 12. Support tensor and vorticity dyad share the same stretch operator

The spatial material-support tensor

\[
B_{\rm supp}=LL^T
\]

obeys exactly

\[
\boxed{
D_tB_{\rm supp}
=(\nabla u)B_{\rm supp}
+B_{\rm supp}(\nabla u)^T.
}
\]

The independently audited Navier--Stokes vorticity dyad satisfies

\[
\boxed{
D_t(\omega\omega^T)
=(\nabla u)(\omega\omega^T)
+(\omega\omega^T)(\nabla u)^T
+\nu\Delta(\omega\omega^T)
-2\nu(\nabla\omega)(\nabla\omega)^T.
}
\]

Thus the nonlinear two-sided stretching operator is literally the same on material
support and on the vorticity dyad.  The difference is physical viscosity: spatial
Hodge diffusion and the Kelvin Gram defect tensor.

For any tensor `E` satisfying

\[
D_tE=(\nabla u)E+E(\nabla u)^T+D,
\]

and deformation gradient `D_tF=(grad u)F`, direct product differentiation gives

\[
\boxed{
D_t(F^{-1}EF^{-T})
=F^{-1}DF^{-T}.
}
\]

The co-deforming pullback cancels the stretch operator exactly.  For pure material
support `D=0`, the pullback is constant.  For the vorticity dyad, only the viscous
terms survive.  This is the tensor version of the previously audited material-flux
identity in which vortex stretching disappears from `H^T omega`.

**Classification: Exact material-support identity and exact co-deforming tensor
cancellation; Navier--Stokes vorticity counterpart already audited exactly.**

---

## 13. Exact Navier--Stokes strain realizes the long-thin locality obstruction

The locality obstruction is dynamically realizable by an exact Navier--Stokes
solution.  On `R^3`, take

\[
\boxed{
u=(sx,0,-sz),}
\]

with

\[
\boxed{p=-\frac12s^2(x^2+z^2).}
\]

Then `div u=0`, `Delta u=0`, and

\[
(u\cdot\nabla)u+\nabla p=0,
\]

so this is an exact steady Navier--Stokes flow for every viscosity.

Its material deformation is

\[
\boxed{
F(t)=\operatorname{diag}(e^{st},1,e^{-st}).
}
\]

Now impose an isotropic physical refinement scale

\[
\rho(t)=e^{-\kappa t}.
\]

The coherent line frame is

\[
\boxed{
L(t)=\rho F
=\operatorname{diag}
(e^{(s-\kappa)t},e^{-\kappa t},e^{-(s+\kappa)t}).
}
\]

Therefore the stretched line has an exact trichotomy:

- `kappa>s`: it shrinks;
- `kappa=s`: it remains exactly length one;
- `kappa<s`: it grows.

At the critical rate `kappa=s`, set `r=e^{-st}`.  Then

\[
\boxed{
L=\operatorname{diag}(1,r,r^2),
\qquad
H=\operatorname{diag}(r^3,r^2,r),
}
\]

which is exactly the adversarial small-area/nonlocal-support packet.

The local differential law behind the calibration is

\[
\boxed{
\frac d{dt}\log|\ell|
=\frac{\ell^TS\ell}{\ell^T\ell}.
}
\]

Thus physical packet locality is an exact competition between refinement scale loss
and cumulative directional strain.  This is not a norm estimate; it is the literal
material-line equation with discrete physical scale changes.

**Classification: Exact Navier--Stokes calibration and exact material-line
kinematics.**

---

## 14. Exact affine Navier--Stokes vortex stretching with zero Kelvin gradient q.v.

There is also an exact affine Navier--Stokes calibration with genuine vortex
stretching.  Set

\[
r(t)=r_0e^{2at},
\qquad
A(t)=
\begin{pmatrix}
-a&-r(t)&0\\
r(t)&-a&0\\
0&0&2a
\end{pmatrix},
\qquad
u(x,t)=A(t)x.
\]

The skew part satisfies

\[
\Omega'+S\Omega+\Omega S=0,
\qquad
S=\operatorname{diag}(-a,-a,2a),
\]

so `A'+A^2` is symmetric.  With quadratic pressure Hessian

\[
P=-(A'+A^2),
\]

one has

\[
\boxed{
\partial_tu+(u\cdot\nabla)u+\nabla p=0,
\qquad
\nabla\cdot u=0,
\qquad
\Delta u=0.
}
\]

Hence this is an exact Navier--Stokes flow for every viscosity.

Its vorticity is spatially uniform,

\[
\boxed{
\omega=(0,0,2r_0e^{2at}).
}
\]

Therefore

\[
\boxed{\nabla\omega=0,\qquad\mathcal G_K=0,}
\]

but

\[
\boxed{
\omega\cdot S\omega
=8ar_0^2e^{4at}>0.
}
\]

The spatial support tensor is

\[
B_F=\operatorname{diag}(e^{-2at},e^{-2at},e^{4at}),
\]

and both `B_F` and `omega omega^T` are stretched in the same `z` direction.  Their
co-deforming contraction is exactly constant:

\[
\boxed{
\frac12\operatorname{tr}
[B_F^{-1}\omega\omega^T]
=2r_0^2.
}
\]

This flow is a sharp physical calibration of the new total-bank typing: real vortex
stretching can occur with **zero** vorticity-gradient Kelvin q.v.; support-normalized
co-deforming geometry cancels that stretching because the vorticity and its material
support are stretched by the same tensor operator.

**Classification: Exact Navier--Stokes calibration.**

---

## 15. Minimal ideal coherent restart core: scale, deformation, total second moment

For an initially isotropic coherent packet with incompressible material deformation
`F`, separate the physical refinement scale `rho` and the co-deforming total
second-moment tensor `Q_tot`.  The exact ideal infinitesimal factorization is

\[
\boxed{
L=\rho F,
\qquad
H=\rho^2F^{-T},
\qquad
T_{\rm tot}=FQ_{\rm tot}F^T.
}
\]

The raw total flux second moment and packet metric are

\[
\boxed{
Q_{\Phi,\rm raw}=\rho^4Q_{\rm tot},
\qquad
M_H=\rho^{-4}F^TF.
}
\]

Therefore physical scale cancels exactly from the ideal normalized bank:

\[
\boxed{
\frac12\operatorname{tr}(Q_{\Phi,\rm raw}M_H)
=
\frac12\operatorname{tr}(FQ_{\rm tot}F^T)
=
\frac12\operatorname{tr}T_{\rm tot}.
}
\]

The three factors have sharply separated physical jobs:

1. `rho`: actual refinement/reselection scale;
2. `F`: accumulated material deformation/support geometry;
3. `Q_tot`: resolved-plus-future co-deforming Kelvin second moment.

Viscous q.v. is internal transfer inside `Q_tot`; common strain is the deformation
geometry `F`; incompressible continuous transport does not change `rho`.
Finite-size quadrupole error, reduced-state resolution covariance, and physical
boundary/exit/reset faces sit outside this ideal core and have already been named
separately.

The exact affine vortex-stretch flow also gives a no-go against using the
co-deforming scalar alone as a restart criterion:

\[
\mathcal I_{\rm cof}=2r_0^2
\]

is constant while

\[
\frac12|\omega|^2
=2r_0^2e^{4at}.
\]

Thus the deformation/support factor cannot be discarded when returning from the
co-deforming bank to physical vorticity.

**Classification: Exact coherent factorization plus exact Navier--Stokes no-go
calibration.**

A later support×bank audit uses this same core without discarding deformation.
Its exact identity is scale-parametric: `P_ell=ell^2 F F^T` and
`Q_tot=eta eta^T+Ctilde` give a PSD decomposition and conditional
`|omega|^2<=p q/ell^2`.  Choosing `ell^2=2nu(Theta-t)` is a separate first-bad
scale specialization, not automatically the horizon of the causal fixed-past
backward-Kelvin bank.  Matching those horizons requires a moving past terminal and
its terminal-motion face.  See `docs/support_bank_restart_bridge_audit.md`.

---

## 16. Kelvin remaining horizon supplies a natural parabolic support scale

The future-variance construction already has a physical clock.  If its common
terminal horizon is `Theta`, define

\[
\tau=\Theta-t.
\]

The common anchor Brownian motion has covariance `2 nu I`, so a one-coordinate
standard-deviation length is

\[
\boxed{
\rho_\nu(\tau)=\sqrt{2\nu\tau}.
}
\]

This scale is supplied by the Kelvin noise itself; it is not a first-bad threshold
chosen for an estimate.  Its physical-time logarithmic rate is

\[
\boxed{
\frac d{dt}\log\rho_\nu=-\frac1{2\tau}.
}
\]

For a material line direction with literal strain rate

\[
\sigma_\ell=n_\ell\cdot S n_\ell,
\]

the corresponding parabolically scaled line obeys

\[
\boxed{
\frac d{dt}\log|\ell_\nu|
=\sigma_\ell-\frac1{2\tau}.
}
\]

### Exact Navier--Stokes calibration

Take the time-dependent affine strain

\[
A(t)=\operatorname{diag}
\left(\frac a{\Theta-t},0,-\frac a{\Theta-t}\right),
\qquad
u(x,t)=A(t)x.
\]

For every smooth preterminal time, `A'+A^2` is symmetric.  Choosing quadratic
pressure Hessian `-(A'+A^2)` gives an exact incompressible Navier--Stokes solution
with zero Laplacian.

The positively stretched material line gains deformation factor

\[
F_+(t)
=\left(\frac{\Theta-t_0}{\Theta-t}\right)^a.
\]

Multiplying by the Kelvin diffusion length gives

\[
\boxed{
|\ell_\nu(t)|
=\sqrt{2\nu}\,(\Theta-t_0)^a
(\Theta-t)^{1/2-a}.
}
\]

Hence the support geometry has the exact calibration

\[
\begin{array}{ccl}
a<1/2 &\Rightarrow& |\ell_\nu|\to0,\\
a=1/2 &\Rightarrow& |\ell_\nu|\to\text{constant},\\
a>1/2 &\Rightarrow& |\ell_\nu|\to\infty.
\end{array}
\]

The coefficient `1/2` is therefore a genuine **parabolic Kelvin support-locality
coefficient** in this exact NS family.  It is not declared to be the first-bad
threshold, a blow-up criterion, or a continuation criterion.

**Classification: Exact Brownian scale identity and exact Navier--Stokes
calibration; identification of first-bad germ scale with `rho_nu` remains an open
bridge.**

---

## 17. One geometry factor controls both finite-shape and flux-localization collapse

For a three-face packet let `A_j` be the actual face areas and let `H` be the
oriented area frame.  Define the dimensionless physical shape-amplification factor

\[
\boxed{
\chi_H
=
\frac{(\sum_jA_j^2)^{1/2}}{\sigma_{\min}(H)}.
}
\]

It is invariant under a uniform physical rescaling of the packet: both numerator
and denominator scale like area.  It therefore measures anisotropy/folding rather
than packet size.

For the finite-surface Nanson remainder matrix `E_shape`, whose columns are

\[
e_j
=-\int_{\Sigma_j}
[(\nabla u(y)-\nabla u(X))^Tn]\,dA,
\]

let

\[
\omega_{\nabla u}(\delta)
=
\sup_{|y-X|\le\delta}
|\nabla u(y)-\nabla u(X)|.
\]

Then exact integral geometry gives

\[
\boxed{
\|E_{\rm shape}H^{-1}\|_F
\le
\chi_H\,\omega_{\nabla u}(\delta).
}
\]

This is the relative finite-shape connection error beyond local Nanson.

For the terminal random flux/vorticity field, the previously repaired Stokes
estimate gives with its conditional `L^2` modulus `omega_zeta,2(delta)`

\[
\boxed{
\|H^{-T}\varepsilon_{\rm flux}\|_{L^2_s}
\le
\chi_H\,\omega_{\zeta,2}(\delta).
}
\]

Thus the same physical geometry factor controls both open finite-size seams.  A
single sufficient local-collapse condition is

\[
\boxed{
\delta\to0,
\qquad
\chi_H
\left[
\omega_{\nabla u}(\delta)
+
\omega_{\zeta,2}(\delta)
\right]
\to0.
}
\]

For an isotropic coherent packet, `chi_H=sqrt(3)` independently of scale.  For the
long-thin witness `H=diag(r^3,r^2,r)`,

\[
\chi_H
=
\frac{\sqrt{r^6+r^4+r^2}}{r^3}
\sim r^{-2},
\]

so anisotropy can exactly defeat otherwise small local field variation.

This is the first inequality inserted only after the exact shape and covariance
channels have been fully typed.  It does not replace them by a generic norm; it
states how the physical support geometry amplifies the two already identified PDE
remainders.

**Classification: Rigorous consequence of the exact integral identities; uniform
first-bad verification remains open.**

---

## 13. Physical meaning of the metric-whitened remainder

For a coherent line frame `L`, `H=cof(L)`.  The orientation density of a common
physical field defect is `g_H=H^T delta zeta`, hence

\[
H^{-T}g_H=\delta\zeta
\]

exactly.  For the same-time Navier--Stokes finite-current error,
`curl_xi beta_L=H^T delta omega`, so whitening its Stokes density returns the literal
vorticity defect.

For a finite three-face packet, however, the components of `epsilon_H` are integrated
on three different faces.  The exact object

\[
r_H=H^{-T}\varepsilon_H
\]

is therefore a **reconstructed physical residual vector**, not generally a pointwise
field value.  Its Euclidean energy and covariance are exactly the existing packet
metric contractions.  Passive orientation reparameterization leaves `r_H`
invariant.

Exact cubic heat-shear NS gives a unit-cube finite residual `r_H=-e_z/4` while the
center vorticity defect is zero; under isotropic scale `r`, the reconstructed
remainder is exactly `-r^2 e_z/4`.  This is the literal NS calibration behind the
fixed-state `r^2` metric-whitened remainder.

For random full payoffs `H^{-T}X_H=zeta+r_H`, covariance contains the mandatory cross
blocks `Cov(zeta,r_H)+transpose`; the finite covariance defect is not simply
`Cov(r_H)`.

**Classification: Exact fixed-state reconstruction/covariance identities and audited
exact-NS scaling calibration.  Uniform first-bad control and cross-clock future-bank
identification remain Open-literal.**

See `docs/codeforming_whitened_kelvin_remainder_audit.md`.
