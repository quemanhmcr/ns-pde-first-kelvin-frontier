# Backward-Kelvin current-shape generator and finite-surface descent audit

This note resolves the next generator question at the level where the physical
Kelvin current actually lives.  The stochastic flow is not reduced to a spatial
point by declaration.  A finite material loop has a shape, and the correct question
is which part of that shape is stochastic, which part is finite-variation
kinematics, and whether an orientation-complete area frame `H` is a sufficient
finite-scale Markov state.

The answer is rigid:

- the uniform Wiener motion is a **common translation** of every point of the
  current;
- after anchoring, relative shape has **zero martingale part**;
- finite shape evolves by physical velocity differences;
- a differential area element closes exactly on `(x,H)` by Nanson;
- a finite surface does **not** close on `(x,H)` in general, because it samples
  spatial variation of `grad u` across the surface;
- the first centered correction is carried by a surface quadrupole in an exact
  Navier--Stokes cubic-shear calibration and is `O(r^2)` relative to the area scale.

No norm estimate, continuation theorem, or regularity claim is used.

---

## 1. The physical backward stochastic flow uses one common Wiener motion

For smooth Navier--Stokes, the backward stochastic Kelvin flow has the form

\[
\widehat d_t X(a,t)
=
 u(X(a,t),t)\,dt
+
\sqrt{2\nu}\,\widehat dW_t,
\qquad t<t_f,
\]

with the same spatially uniform Brownian motion for the whole flow.  This is the
Constantin--Iyer stochastic Lagrangian structure; in backward Itô form the chain
rule carries the physical-time second-order operator `-nu Delta`.

For finitely many material points `X_p`, the joint diffusion covariance is therefore

\[
\boxed{
A_{\rm common}
=
2\nu\,(\mathbf 1\mathbf 1^T)\otimes I_3.
}
\]

For any number of points this matrix has rank exactly `3`, not `3N`.

**Physical type:** common stochastic translation of the whole current.

**Classification: Exact stochastic-flow identity.**

---

## 2. Anchor plus relative shape removes all shape quadratic variation

Choose one material anchor `X` and write every point of the current as

\[
X_p=X+R_p.
\]

Because the same Brownian increment appears in both `X_p` and `X`, subtraction gives

\[
\boxed{
\widehat d_tR_p
=
[u(X+R_p,t)-u(X,t)]\,dt.
}
\]

There is no `dW` term.

Thus the full current state may be written as

\[
\boxed{
Y=(X,R(\cdot)),
}
\]

where `R` is the relative loop/surface embedding.  The anchor is stochastic; the
shape is finite variation along the random anchor path.

For a cylinder observable of finitely many relative points, the exact backward
current-shape generator is

\[
\boxed{
\begin{aligned}
\mathscr K^-F
={}&
 u(X)\cdot\nabla_XF
-
\nu\Delta_XF
\\
&+
\sum_p
[u(X+R_p)-u(X)]\cdot\nabla_{R_p}F.
\end{aligned}
}
\]

The source code also verifies this by starting in the original point coordinates:

\[
\mathscr K^-F
=
\sum_pu(X_p)\cdot\nabla_pF
-
\nu\sum_{p,q}\nabla_p\cdot\nabla_qF.
\]

The cross derivatives are mandatory because the noises are common.  Under the
anchor/relative transformation they collapse exactly to `-nu Delta_X`.

**Physical type:** Brownian translation plus deterministic relative deformation.

**Classification: Exact backward-Itô cylinder identity.**

---

## 3. Consequence for quadratic variation: shape is not a hidden stochastic producer

Since relative shape has zero martingale part, moving from `(X,R)` to a richer shape
representation cannot create an additional shape quadratic variation merely because
more shape variables are retained.

All stochastic q.v. comes from the common translation direction.  Shape motion can
still change the observed Kelvin payoff, but it does so through finite-variation
covariance/connection work.

This exactly agrees with the earlier cycle-map audit: finite-variation observer or
shape motion has no autonomous Itô pair source.

**Classification: Rigorous consequence of the exact common-noise covariance.**

---

## 4. Differential area elements close exactly on `(X,H)`

Let `h=n\,dA` be an infinitesimal oriented material area vector.  For incompressible
flow, Nanson kinematics gives

\[
\boxed{
D_th=-(\nabla u(X,t))^Th.
}
\]

For an orientation-complete infinitesimal packet

\[
H=(h_1,h_2,h_3),
\]

this is

\[
\boxed{
D_tH=-(\nabla u(X,t))^TH.
}
\]

Together with the common-noise anchor SDE, `(X,H)` is therefore an exact local
Markov state for differential area elements.

This is the geometric state already used in the material-flux packet audit.

**Classification: Exact infinitesimal material kinematics.**

---

## 5. A finite surface has an extra physical shape current

Let `Sigma_t` be a finite material spanning surface and let

\[
h_\Sigma(t)=\int_{\Sigma_t}n\,dA.
\]

Integrating the pointwise Nanson law over the material surface gives

\[
\boxed{
\frac d{dt}h_\Sigma
=
-\int_{\Sigma_t}(\nabla u(y,t))^Tn(y,t)\,dA.
}
\]

Choose the material anchor `X` and split the velocity gradient into its anchor value
and spatial variation.  Then

\[
\boxed{
\frac d{dt}h_\Sigma
=
-(\nabla u(X,t))^Th_\Sigma
+
E_{\rm shape}(\Sigma;X),
}
\]

where

\[
\boxed{
E_{\rm shape}
:=
-\int_{\Sigma_t}
[(\nabla u(y,t)-\nabla u(X,t))^Tn(y,t)]\,dA.
}
\]

This term has an unambiguous physical meaning:

> the finite surface samples **strain/velocity-gradient variation across its actual
> shape**.

It is not stochastic quadratic variation.  It is not pressure/gauge.  It is not
`S^int`.  It is a finite-variation material deformation current.

If `grad u` is spatially constant, as for affine velocity fields, `E_shape=0`
exactly and the finite surface descends to the local Nanson law.

**Classification: Exact material-surface identity.**

---

## 6. Centering removes the first shape moment, not all shape information

For a small flat surface written as `y=X+r` with fixed normal, expand

\[
\nabla u(X+r)-\nabla u(X).
\]

If the oriented first moment is centered,

\[
\int_\Sigma r_k\,n\,dA=0,
\]

the term linear in `r` cancels.  The next geometric carrier is the oriented second
surface moment

\[
\boxed{
\mathcal M_{kl}
=
\int_\Sigma r_kr_l\,n\,dA.
}
\]

Thus centering does not make finite shape irrelevant.  It pushes the first missing
state from a dipole to a quadrupole.

For a smooth field the exact Taylor-integral remainder can be left in physical form;
there is no need to replace it prematurely by a norm bound.

**Classification: Exact moment cancellation plus rigorous kinematic consequence.**

---

## 7. Exact Navier--Stokes calibration: cubic heat shear

Consider on `R^3`

\[
\boxed{
u
u?}
\]

More explicitly,

\[
\boxed{
 u(y,t)
=
(y^3+6\nu ty,0,0).
}
\]

Its advective nonlinearity vanishes identically and

\[
\partial_tU-\nu\partial_y^2U
=6\nu y-6\nu y
=0,
\]

so this is an exact smooth incompressible Navier--Stokes shear with constant
pressure.

Let `Sigma_{b,c}` be the centered rectangle

\[
-b\le y\le b,
\qquad
-c\le z\le c,
\]

with normal `+e_x`.  Its area vector is

\[
 h=4bc\,e_x.
\]

Since

\[
\partial_yU=3y^2+6\nu t,
\]

the exact finite-surface area rate is

\[
\frac d{dt}h
=
-\left(\int_{\Sigma_{b,c}}(3y^2+6\nu t)\,dA\right)e_y.
\]

The local Nanson term at the anchor `y=0` is

\[
-6\nu t\,(4bc)e_y.
\]

Therefore

\[
\boxed{
E_{\rm shape}
=
-3\left(\int_{\Sigma_{b,c}}y^2\,dA\right)e_y
=
-(4bc)b^2e_y.
}
\]

The residual is literally the surface second moment sampled by the cubic shear.

**Classification: Exact Navier--Stokes calibration.**

---

## 8. Same anchor + same area vector is not enough at finite scale

Take two centered rectangles:

\[
(b,c)=(1,1),
\qquad
(b,c)=(2,1/2).
\]

Both have the same anchor and the same area vector

\[
\boxed{h=4e_x.}
\]

But the exact shape currents are

\[
\boxed{
E_{\rm shape}^{(1)}=-4e_y,
\qquad
E_{\rm shape}^{(2)}=-16e_y.
}
\]

Hence

\[
\boxed{
E_{\rm shape}^{(2)}-E_{\rm shape}^{(1)}=-12e_y\neq0.
}
\]

So there cannot be an exact finite-scale generator depending only on `(X,h)` for
all smooth Navier--Stokes flows.

This is not a generic Markov toy counterexample.  It occurs inside an exact smooth
Navier--Stokes solution.

**Classification: Rigorous no-descent consequence from exact NS.**

---

## 9. Orientation completion does not cure finite-shape blindness

Now assemble three area vectors into a restart packet `H`.  Keep the second and third
loop shapes fixed and replace only the first loop by the two rectangles above.  The
two packets can have exactly the same

\[
H=4I_3,
\]

while their finite-surface drift matrices differ by

\[
\boxed{
\Delta E_{\rm packet}
=
\begin{pmatrix}
0&0&0\\
-12&0&0\\
0&0&0
\end{pmatrix}.
}
\]

Thus orientation completion solves rank-one **orientation** blindness, but it does
not magically encode finite **shape** moments.

The missing information is a different physical phenomenon.

**Classification: Rigorous structural consequence.**

---

## 10. Shrinking scale: the exact cubic residual is raw `r^4`, relative `r^2`

Scale a centered rectangle by

\[
b=rb_0,
\qquad
c=rc_0.
\]

Then

\[
h_r=4r^2b_0c_0\,e_x,
\]

whereas

\[
\boxed{
E_{\rm shape}(r)
=
-4r^4b_0^3c_0\,e_y.
}
\]

Therefore

\[
\boxed{
\frac{(E_{\rm shape})_y}{(h_r)_x}
=-r^2b_0^2.
}
\]

So at every fixed smooth state the finite-shape correction disappears in the
differential-area limit.

But the restart programme needs more than pointwise fixed-time convergence: it must
know whether the coefficient carried by the true first-bad surface geometry remains
controlled as `r->0` and physical time approaches a candidate singular time.

**Classification: Exact NS scaling calibration; uniform singular-time collapse is
open.**

---

## 11. The same second-moment scale appears in covariance localization

The previous future-covariance audit found that a centered conditionally `C^2`
small-loop packet has

\[
C_r=r^4C_0+r^6C_1+\cdots,
\]

so after area-metric normalization its first non-tensorial correction is `r^2`.

The present generator audit finds independently that the first centered
finite-surface Nanson correction is also relative order `r^2` in the cubic NS
calibration.

These are **not the same physical term**:

- the covariance remainder comes from spatial variation of the random terminal
  cochain/vorticity covariance;
- `E_shape` comes from spatial variation of the deterministic velocity gradient
  across the material surface.

But both are carried by the same geometric fact: after centering, the first surviving
finite-size information is a second surface moment.

This identifies the first literal shape variable that any uniform finite-scale
restart analysis may need to retain.

**Classification: Rigorous structural comparison; no identification of the two
physical channels.**

---

## 12. What happened to the old generator-descent seam?

The old question was too binary:

> does the full stochastic Kelvin generator descend to `(x,H)`?

The PDE-first answer is now more precise.

### Finite scale

No, not in general.  `E_shape` is an exact physical obstruction, and exact cubic
Navier--Stokes gives two states with identical `(x,H)` but different `Hdot`.

### Infinitesimal scale

Yes.  A differential material area frame obeys exact Nanson kinematics, and common
Brownian noise acts only on the anchor.

### First-bad shrinking limit

Open.  One must prove that the finite-shape hierarchy collapses uniformly enough as
the selected physical scale tends to zero, or else carry the necessary shape
moments explicitly.

The correct open object is therefore no longer an unspecified "generator
compatibility".  It is the **uniform finite-shape collapse/current hierarchy**.

**Classification: Exact structural resolution of the descent dichotomy; uniform
singular-time shape collapse remains a Conjectural bridge.**

---

## 13. Updated restart state architecture

The literal state hierarchy is now

\[
\boxed{
(X,R(\cdot))
\longrightarrow
(X,H,\mathcal M_2,\mathcal M_3,\ldots)
\longrightarrow
(X,H)
}
\]

where the first arrow is a moment description of the finite shape and the second is
valid exactly only at differential scale or when the higher shape currents vanish.

For the next restart step, one should not add all moments abstractly.  The correct
procedure is:

1. keep `E_shape` as its exact surface integral;
2. exploit centering/symmetry before expanding it;
3. introduce only the first moment tensor that actually survives;
4. ask whether the coupled NS/Kelvin ledger itself pays or telescopes that term;
5. only then consider estimates if an exact cancellation does not close it.

The next unresolved seams are therefore:

- forward-future versus backward-Kelvin causal identification;
- uniform collapse/control of the finite-shape current and covariance remainder;
- material metric stretching + physical boundary/exit capacity;
- restart/continuation.

`S^int` remains undefined and untouched.

No regularity conclusion is made.


---

## Causal state-map handoff

The separate ancestry time-reversal audit proves that the normalized ancestry law
already determines `b_+`, `b_-`, and their midpoint current `j` exactly.  The living
causal problem is therefore to map the ancestry backward state onto the physical
anchor/relative-shape state constructed here.  See
`docs/ancestry_time_reversal_audit.md`.

**Classification: Exact operator-side handoff; state identification remains
open-literal.**

---

## 14. Quadrupole is the first missing carrier, not an exact finite-state closure

The cubic heat shear shows that the second surface moment is the first correction
beyond the area frame.  It would still be incorrect to stop there and declare
`(X,H,Q_Sigma)` a closed finite-state model.

Every polynomial heat shear

\[
\boxed{
U_n(y,t)=e^{\nu t\partial_{yy}}y^n
=\sum_{j=0}^{\lfloor n/2\rfloor}
\frac{n!}{(n-2j)!j!}(\nu t)^j y^{n-2j}
}
\]

satisfies

\[
\partial_tU_n=\nu\partial_{yy}U_n.
\]

Hence `u=(U_n(y,t),0,0)` is an exact Navier--Stokes shear with constant pressure.

For `n=5`,

\[
\boxed{
U_5=y^5+20\nu t y^3+60\nu^2t^2y,
}
\]

so

\[
U_{5,y}=5y^4+60\nu t y^2+60\nu^2t^2.
\]

Take centered `yz` strips with width functions

\[
w_0(y)=1,
\qquad
w_1(y)=1+\frac12P_4(y),
\]

where

\[
P_4(y)=\frac{35y^4-30y^2+3}{8}.
\]

Since `P_4 >= -3/7` on `[-1,1]`, `w_1 >= 11/14>0`; both are legitimate positive
surfaces.  Legendre orthogonality gives

\[
\int P_4\,dy=0,
\qquad
\int y^2P_4\,dy=0,
\]

so the two surfaces have the same area vector and the same `yy` quadrupole.  But

\[
\int y^4P_4(y)\,dy=\frac{16}{315},
\]

and therefore their exact material area-vector rates differ by

\[
\boxed{
\dot H_1-\dot H_0
=-\frac8{63}e_y.
}
\]

Thus even `(X,H,Q_Sigma)` is not an exact finite-scale Markov quotient.

**Classification: Exact Navier--Stokes counter-calibration.**

---

## 15. No finite surface-moment truncation closes universally

The same construction is not special to the fourth moment.  For every `m>=1`, use

\[
w_1=1+\varepsilon P_{2m},
\qquad |arepsilon|<1,
\]

and the exact heat shear `U_{2m+1}`.  Legendre orthogonality gives

\[
\int_{-1}^1 y^{2j}P_{2m}(y)\,dy=0,
\qquad 0\le j<m,
\]

while

\[
\boxed{
\int_{-1}^1 y^{2m}P_{2m}(y)\,dy
=
\frac{2^{2m+1}[(2m)!]^2}{(4m+1)!}>0.
}
\]

The derivative `U_{2m+1,y}` contains the leading term
`(2m+1)y^{2m}` and only lower even powers.  All lower moments cancel between the
two surfaces, leaving the exact nonzero generator difference

\[
\boxed{
\Delta\dot H_y
=-(2m+1)\varepsilon
\frac{2^{2m+1}[(2m)!]^2}{(4m+1)!}.
}
\]

Therefore for every finite list of even centered surface moments, there is a smooth
exact Navier--Stokes heat shear that sees the next unresolved moment.

The finite current-shape state is genuinely an **infinite moment/embedding
hierarchy**.  The restart programme should not attempt to close it by adding a
finite number of ad hoc moments.  The correct remaining theorem is the already
identified one: prove uniform collapse of the entire finite-shape remainder as the
physical first-bad packet scale becomes local.

**Classification: Rigorous structural consequence of an exact infinite family of
Navier--Stokes calibrations.**
