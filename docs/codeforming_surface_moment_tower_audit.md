# Codeforming surface-moment tower audit

## Scope

This note continues the finite-shape Kelvin audit without replacing the physical
surface by a norm, a finite closure ansatz, or an abstract regularity surrogate.
The object is still the actual reverse-age material spanning surface.  The only new
operation is an exact change of coordinates by its local affine tangent frame.

The resulting law is unexpectedly small: after the local affine deformation is
removed, the whole infinite oriented-moment tower is transported by one residual
incompressible velocity field.

No continuation/restart/regularity theorem is claimed.

---

## 1. Raw oriented moments and the forced `m+2` refinement weight

For a physical oriented surface in relative coordinates `r`, write the oriented
area element as

\[
a=n\,dA
\]

and the order-`m` monomial moments as

\[
M_\alpha=\int_\Sigma r^\alpha a,
\qquad |\alpha|=m.
\]

Under a linear physical map

\[
r_+=Jr_-,
\qquad
a_+=\operatorname{cof}(J)a_-,
\]

the moment transforms exactly by

\[
\boxed{
M_{\alpha,+}
=
\operatorname{cof}(J)
\int (Jr_-)^\alpha a_- .
}
\]

A general `J` therefore mixes only moments of the same total order.  No absent
moment is silently interpreted as zero.

For isotropic refinement `J=\lambda I` in three dimensions,

\[
\operatorname{cof}(\lambda I)=\lambda^2I,
\]

and hence

\[
\boxed{
M_\alpha\mapsto \lambda^{m+2}M_\alpha.
}
\]

The exponent `m+2` is not dimensional guessing.  It is the exact combination of
`m` line-coordinate slots and one two-dimensional oriented-area/cofactor slot.

**Status: Exact identity.**

---

## 2. Scalar scale normalization leaves a genuine unit-determinant shape action

Let a three-dimensional refinement split as

\[
J=dS,
\qquad
d=(\det J)^{1/3},
\qquad
\det S=1.
\]

If `rho` is the old coherent linear scale, define

\[
\widehat M_\alpha
=
\rho^{-(m+2)}M_\alpha.
\]

Then exact cofactor algebra gives

\[
\boxed{
\widehat M_{\alpha,+}
=
\operatorname{cof}(S)
\int (Sr)^\alpha\,d\widehat a_- .
}
\]

All scalar powers of `d` cancel.  What remains is a real physical shape action.
Therefore scalar normalization removes isotropic scale but does **not** remove
anisotropy.

**Status: Exact identity.**

---

## 3. The full local reverse frame

On a smooth reverse-age material segment let

\[
A_0=A(X,r)=\nabla u(X,r),
\]

and define the local reverse line frame `L` by

\[
\boxed{
\dot L=-A_0L.
}
\]

For incompressible Navier--Stokes,

\[
\frac d{d\sigma}\det L=0.
\]

Its cofactor frame

\[
C=\operatorname{cof}(L)
\]

satisfies

\[
\boxed{
\dot C=A_0^TC.
}
\]

This is the same sign as the actual reverse-age local area law and is deliberately
not identified with the stochastic Cauchy metric-dual frame `H_C`, whose connection
has the opposite sign.

**Status: Exact reverse-age tangent/cofactor identity.**

---

## 4. Full codeforming pullback

Define

\[
\boxed{
\xi=L^{-1}r,
\qquad
\widetilde a=C^{-1}a.
}
\]

and

\[
\boxed{
\widetilde M_\alpha
=\int \xi^\alpha\widetilde a.
}
\]

If

\[
L=\rho S,
\qquad \det S=1,
\]

then

\[
L^{-1}=\rho^{-1}S^{-1},
\qquad
C^{-1}=\rho^{-2}\operatorname{cof}(S)^{-1}.
\]

Consequently

\[
\boxed{
\widetilde M^{(m)}
=
(S^{-1})^{\otimes m}
\otimes\operatorname{cof}(S)^{-1}
\;\widehat M^{(m)}.
}
\]

Thus the full pullback removes scalar scale and coherent linear anisotropy in one
exact operation.

**Status: Exact scale--shape factorization.**

---

## 5. The single codeforming nonaffinity field

The actual reverse-age relative velocity is

\[
\dot r
=-\Delta u(r),
\qquad
\Delta u(r)=u(X+r)-u(X).
\]

Separate its local affine part:

\[
\Delta u(r)=A_0r+N_{\rm phys}(r).
\]

In codeforming coordinates define

\[
\boxed{
\mathcal N_L(\xi)
=
L^{-1}
\left[
 u(X+L\xi)-u(X)-A_0L\xi
\right].
}
\]

A direct chain rule using `L_dot=-A_0L` gives

\[
\boxed{
\dot\xi=-\mathcal N_L(\xi).
}
\]

There is no affine remainder.  `mathcal N_L` is literally the nonaffine velocity
difference measured in the deforming physical line frame.

**Status: Exact identity / physical typing.**

---

## 6. The area source is not independent: it is `D N_L` transpose

The actual oriented-area element satisfies

\[
\dot a=A(X+r)^Ta.
\]

Using `C_dot=A_0^TC`,

\[
\dot{\widetilde a}
=
C^{-1}[A(X+L\xi)-A_0]^TC\widetilde a.
\]

But

\[
D_\xi\mathcal N_L
=
L^{-1}[A(X+L\xi)-A_0]L.
\]

Since `C=det(L)L^{-T}`,

\[
C^{-1}[A-A_0]^TC
=
\left[L^{-1}(A-A_0)L\right]^T.
\]

Therefore

\[
\boxed{
\dot{\widetilde a}
=
(D_\xi\mathcal N_L)^T\widetilde a.
}
\]

For incompressible NS,

\[
\boxed{
\nabla_\xi\cdot\mathcal N_L=0.
}
\]

So after affine deformation is removed, the pulled-back physical surface is simply
transported by the residual incompressible velocity

\[
\boxed{-\mathcal N_L.}
\]

This is the small rigid law underneath the full finite-shape hierarchy.

**Status: Exact identity.**

---

## 7. Entire oriented-moment tower from the one residual field

For every multi-index `alpha`, the exact codeforming law is

\[
\boxed{
\frac d{d\sigma}\widetilde M_\alpha
=
-\sum_i\alpha_i
\int
\xi^{\alpha-e_i}
(\mathcal N_L)_i\,\widetilde a
+
\int
\xi^\alpha
(D_\xi\mathcal N_L)^T\widetilde a.
}
\]

The affine same-order connection from the raw hierarchy has disappeared completely.
Every change of the pulled-back tower is nonaffine physical shape transport.

If `u` is affine on the current support, then

\[
\mathcal N_L\equiv0
\]

and hence

\[
\boxed{
\frac d{d\sigma}\widetilde M_\alpha=0
\quad\text{for every }\alpha.
}
\]

This strengthens the previous raw-moment statement "affine flow closes each order":
in the correct co-deforming frame the whole tower is frozen.

**Status: Exact identity / affine rigidity theorem.**

---

## 8. One generating current contains the full tower

Introduce

\[
\boxed{
\mathscr G_L(\theta)
=
\int_\Sigma e^{\theta\cdot\xi}\widetilde a.
}
\]

Every pulled-back moment is a derivative at `theta=0`:

\[
\widetilde M_\alpha
=
\partial_\theta^\alpha\mathscr G_L(0).
\]

The exact transport law is

\[
\boxed{
\frac d{d\sigma}\mathscr G_L(\theta)
=
\int
 e^{\theta\cdot\xi}
\left[
(D_\xi\mathcal N_L)^T
-(\theta\cdot\mathcal N_L)I
\right]
\widetilde a.
}
\]

Symbolic differentiation of this single equation reproduces the exact moment law at
every audited order.  The infinite tower is therefore not a collection of unrelated
ODEs: it is the Taylor face of one current-valued generating law.

**Status: Exact identity.**

---

## 9. Homogeneous NS jets: scalar power and anisotropy are separate faces

For a homogeneous nonaffine physical velocity jet of degree `p>=2`, write it as
`U_p(r)`.  If

\[
L=\rho S,
\qquad \det S=1,
\]

then

\[
\boxed{
\mathcal N_{\rho S}^{(p)}(\xi)
=
\rho^{p-1}
S^{-1}U_p(S\xi).
}
\]

Equivalently, for the underlying `p`-linear jet tensor,

\[
\boxed{
\mathfrak J_p(L)
=
L^{-1}(\nabla^pu)L^{\otimes p}.
}
\]

Under a coherent reparameterization `L -> L R`,

\[
\boxed{
\mathfrak J_p(LR)
=R^{-1}\mathfrak J_p(L)R^{\otimes p}.
}
\]

Under isotropic refinement `R=lambda I`, this reduces to the forced factor

\[
\lambda^{p-1}.
\]

Thus `rho^(p-1)` is only the scalar face.  The unit-determinant shape conjugation can
amplify, suppress, or rotate a nonlinear jet independently.

**Status: Exact homogeneous-jet identity.**

---

## 10. Coherent linear refinement is a gauge of the full pulled-back tower

Suppose the physical current and its local frame are refined coherently by the same
reference linear map `R`:

\[
L_+=L_-R.
\]

The physical map from old to new surface is

\[
P=L_-RL_-^{-1}.
\]

Then

\[
r_+=Pr_-,
\qquad
a_+=\operatorname{cof}(P)a_-.
\]

A direct substitution gives

\[
\boxed{
\xi_+=\xi_-,
\qquad
\widetilde a_+=\widetilde a_-,
\qquad
\widetilde M_{\alpha,+}=\widetilde M_{\alpha,-}.
}
\]

Hence a coherent linear refinement/reset is not internal shape production in the
codeforming tower.  If a selector/refinement operation changes the physical current
without the matching frame pushforward, its difference is a real reset/revaluation
face and must be retained by the existing full pair tensor-square algebra.

**Status: Exact identity.**

---

## 11. Exact linear-strain calibration: codeforming constancy is not support locality

Use the exact incompressible linear-strain NS solution

\[
u=(sx,0,-sz)
\]

with isotropic physical refinement rate `k`.  The coherent line frame is

\[
L(t)=
\operatorname{diag}
\left(
 e^{(s-k)t},
 e^{-kt},
 e^{-(s+k)t}
\right).
\]

At the critical rate `k=s`, put `r=e^{-st}`.  Then

\[
\boxed{
L=\operatorname{diag}(1,r,r^2).
}
\]

The local affine NS field has

\[
\mathcal N_L=0,
\]

so every codeforming moment is exactly constant.  Nevertheless the first physical
line stays of length one.  There is no support locality.

Therefore

> **codeforming tower constancy does not imply physical support collapse.**

**Status: Audited calibration / rigorous no-go consequence.**

---

## 12. Support-local packets can still have divergent scalar-normalized moments

For the same exact strain with `k>s`, every physical line scale tends to zero:

\[
e^{(s-k)t},\quad e^{-kt},\quad e^{-(s+k)t}\to0.
\]

Yet for the `xy` face,

\[
A_{xy}=e^{(s-2k)t},
\qquad
\rho=e^{-kt},
\]

so

\[
\boxed{
\frac{A_{xy}}{\rho^2}=e^{st}\to\infty.
}
\]

The full codeforming area remains exactly the reference area.

Thus bounded scalar-normalized moments are **not necessary** for physical support
locality.  Scalar volume scale and anisotropy must not be merged.

**Status: Audited exact-NS/refinement calibration.**

---

## 13. Support locality alone does not force codeforming affine collapse

Now use the exact quadratic heat-shear NS solution

\[
\boxed{
u=(y^2+2\nu t,0,0).}
\]

At anchor `y=0`, the local affine part vanishes and

\[
\Delta u=(y^2,0,0).
\]

For a genuinely shrinking anisotropic refined frame

\[
\boxed{
L_r=\operatorname{diag}(r^3,r,r),
\qquad r\downarrow0,
}
\]

all physical line scales go to zero.  But

\[
\boxed{
\mathcal N_{L_r}(\xi)
=
\frac1r\,\xi_y^2e_x.
}
\]

Hence the current is physically support-local while its codeforming nonlinear shape
velocity diverges.

The physics is transparent: the quadratic shear produces an `x` displacement of
size `y^2~r^2`, while the chosen physical `x` width is only `r^3`.  Relative to that
very thin output direction, the nonaffine deformation is order `r^{-1}`.

Therefore

> **support diameter collapse alone does not imply codeforming affine collapse.**

What is missing is a tensorial compatibility between the NS nonlinear jets and the
actual anisotropic support frame, represented literally by

\[
L^{-1}(\nabla^pu)L^{\otimes p}.
\]

This is stronger and more precise than a scalar small-scale statement.

**Status: Audited calibration (exact Navier--Stokes plus exact physical refinement) /
rigorous support-locality-only no-go.**

---

## 14. Placement in the first-bad ledger

The full finite-shape problem now separates into four physical layers.

### Raw physical layer

The actual current `R(.)`, actual support, actual area and Kelvin descent error remain
primary.  Their equations are exact and no local quotient has been assumed.

**Status: Exact physical state.**

### Coherent affine geometry

Local affine deformation and coherent linear refinement are pure coordinate geometry
for the codeforming tower.  They are removed exactly by `L` and `cof(L)`.

**Status: Exact identity.**

### Nonaffine shape production

All smooth material-shape production in the pulled-back tower is carried by the one
divergence-free field `mathcal N_L`, or equivalently by the family of tensorial
nonaffinity jets

\[
\mathfrak J_p(L)=L^{-1}(\nabla^pu)L^{\otimes p},\qquad p\ge2.
\]

**Status: Exact identity.**

### Selector/refinement/reset mismatch

A coherent refinement is gauge in the codeforming tower.  A real selector switch,
noncoherent refinement, boundary cut, physical exit, or reset remains a physical
current/pair face and is not absorbed into `mathcal N_L`.

**Status: Existing exact pair-current algebra; programme-specific moving first-bad
instantiation remains Open-literal.**

---

## 15. New literal first-bad target

The old question "which finite set of moments should be added?" is now closed by the
finite-moment no-go results.

The next literal question is whether the actual migrating first-bad current supplies
a frame/support law for which

\[
\boxed{
\mathcal N_{L_{fb}}(\xi)
= L_{fb}^{-1}
\left[
 u(X+L_{fb}\xi)-u(X)-A(X)L_{fb}\xi
\right]
}
\]

and the corresponding pulled-back vorticity inhomogeneity remain controlled in the
actual current topology while the physical support becomes local.

The exact quadratic-shear calibration proves that support shrink alone is
insufficient; anisotropic jet/frame compatibility is a separate physical seam.
Conversely, exact affine strain proves that a perfectly frozen codeforming tower is
insufficient without physical support locality.

So a valid first-bad descent theorem must control **both**:

1. physical support locality / boundary / exit / selector faces;
2. codeforming nonaffinity of the real NS velocity/vorticity fields relative to that
   support frame.

Only after these literal structures are established would estimates be relevant.

**Status: Open-literal.  No restart/continuation/regularity theorem claimed.**

---

## 16. Kelvin sees the metric-weighted nonaffinity one-form, not bare kinematic nonaffinity

Define the physical line metric

\[
G_L=L^TL.
\]

The physical nonaffine velocity residual is

\[
n_{\rm phys}(L\xi)=L\mathcal N_L(\xi).
\]

Because `dr=L dxi`, its momentum one-form pulls back exactly as

\[
\boxed{
n_{\rm phys}\cdot dr
=
(G_L\mathcal N_L)\cdot d\xi.
}
\]

Define

\[
\boxed{
\beta_L
:=G_L\mathcal N_L.
}
\]

`mathcal N_L` is a vector-field/kinematic object.  `beta_L` is a one-form/Kelvin
object.  They must not be identified when `L` is anisotropic.

Now subtract the affine Taylor field from the physical circulation.  Since the
constant velocity has zero closed-loop circulation and the linear field has exactly
the local vorticity flux,

\[
\boxed{
\varepsilon_K
=
\oint_{\widetilde Z}\beta_L\cdot d\xi.
}
\]

By the linear Piola/Stokes curl transform,

\[
\boxed{
\operatorname{curl}_\xi\beta_L
=
\operatorname{cof}(L)^T
[\omega(X+L\xi)-\omega(X)].
}
\]

Hence equivalently

\[
\boxed{
\varepsilon_K
=
\int_{\widetilde\Sigma}
\operatorname{curl}_\xi\beta_L\cdot\widetilde a.
}
\]

The finite Kelvin descent error is therefore literally the circulation of the
metric-weighted codeforming nonaffinity one-form.

**Status: Exact identity / exact Stokes--Piola identity.**

---

## 17. One nonaffinity, three distinct physical faces

The same `mathcal N_L` now has three typed manifestations:

\[
\boxed{
\begin{aligned}
\text{relative shape kinematics:}&\qquad \dot\xi=-\mathcal N_L,\\
\text{oriented-area kinematics:}&\qquad
\dot{\widetilde a}=(D_\xi\mathcal N_L)^T\widetilde a,\\
\text{Kelvin one-form:}&\qquad
\beta_L=G_L\mathcal N_L.
\end{aligned}
}
\]

The first two govern the evolution of the material surface.  The third governs the
instantaneous finite-to-local circulation defect.

They share one underlying physical nonaffinity but are not interchangeable
quantities.  In particular, the line metric can strongly suppress or amplify the
one-form relative to the vector field.

The existing finite-shape drift also becomes transparent.  If

\[
\widetilde h=\int\widetilde a,
\]

then

\[
\dot{\widetilde h}
=
\int(D_\xi\mathcal N_L)^T\widetilde a,
\]

and the physical strain-shape residual is

\[
\boxed{
\mathcal R_A
=
\operatorname{cof}(L)\dot{\widetilde h}.
}
\]

With the local pulled-back vorticity

\[
\eta_0=\operatorname{cof}(L)^T\omega(X),
\]

the deterministic part of the exact descent-error SDE is

\[
\boxed{
-\omega(X)\cdot\mathcal R_A
=-\eta_0\cdot\dot{\widetilde h}.
}
\]

So shape drift and Kelvin bias are two contractions of the same residual
codeforming geometry.

**Status: Exact identity.**

---

## 18. Exact anisotropic quadratic referee separates shape-affinity from Kelvin descent

Return to the exact quadratic heat-shear NS field and

\[
L_r=\operatorname{diag}(r^3,r,r).
\]

The kinematic nonaffinity is

\[
\mathcal N_{L_r}
=
r^{-1}\xi_y^2e_x.
\]

But

\[
G_{L_r}
=
\operatorname{diag}(r^6,r^2,r^2),
\]

so

\[
\boxed{
\beta_{L_r}
=G_{L_r}\mathcal N_{L_r}
=r^5\xi_y^2e_x.
}
\]

Its curl is

\[
\boxed{
\operatorname{curl}_\xi\beta_{L_r}
=-2r^5\xi_y e_z,
}
\]

exactly equal to

\[
\operatorname{cof}(L_r)^T
[\omega(L_r\xi)-\omega(0)].
\]

Thus a divergent codeforming shape velocity does **not** imply a large Kelvin descent error.  Here the metric-weighted Kelvin one-form shrinks like `r^5`.

This corrects the frontier wording:

- support locality alone does not force **kinematic affine collapse**;
- but failure of kinematic affine collapse alone does not obstruct
  **instantaneous Kelvin descent**;
- instantaneous Kelvin descent is typed by `beta_L` / its curl;
- dynamic control of the evolving finite surface still depends on `mathcal N_L` and
  `D mathcal N_L`.

**Status: Audited calibration (exact Navier--Stokes) / rigorous type-separation
consequence.**

---

## 19. Refined first-bad target

There are now two different literal descent questions.

### Instantaneous Kelvin readout descent

The object to control is

\[
\boxed{
\beta_{L_{fb}}
= L_{fb}^TL_{fb}\,
L_{fb}^{-1}
[u(X+L_{fb}\xi)-u(X)-A(X)L_{fb}\xi],
}
\]

or equivalently its Stokes curl

\[
\operatorname{cof}(L_{fb})^T\delta\omega.
\]

### Dynamic current-shape descent

The evolving pulled-back surface is controlled by

\[
\mathcal N_{L_{fb}},
\qquad
D_\xi\mathcal N_{L_{fb}},
\]

together with physical selector/refinement/boundary/exit/reset faces.

A theorem for one does not automatically prove the other.  The exact quadratic
calibration above makes that distinction mandatory.

The actual migrating first-bad state has not yet been shown to control either family
uniformly near a candidate singular time.

**Status: Open-literal.  No restart/continuation/regularity theorem claimed.**

---

## 20. The stochastic error channel is the anchor derivative of the Kelvin one-form

On the literal full reverse-age state, the anchor `X` is the only Brownian
coordinate.  The local line frame and pulled-back relative shape are finite variation
in the instantaneous martingale part.  Therefore the error martingale coefficient is
obtained by differentiating the residual one-form with respect to the anchor while
holding `L` and the pulled-back current fixed:

\[
\boxed{
q_\mu^{\rm err}
=
\oint_{\widetilde Z}
\partial_{X_\mu}\beta_L\cdot d\xi.
}
\]

By Stokes this is equivalent to

\[
q_\mu^{\rm err}
=
\int_{\widetilde\Sigma}
\operatorname{curl}_\xi
(\partial_{X_\mu}\beta_L)
\cdot\widetilde a,
\]

which is exactly the pulled-back finite-support vorticity-gradient residual already
identified in the physical-coordinate descent-error SDE.

Let

\[
\widetilde h=\int\widetilde a,
\qquad
\eta_0=\operatorname{cof}(L)^T\omega(X).
\]

Since

\[
\dot{\widetilde h}
=
\int(D_\xi\mathcal N_L)^T\widetilde a,
\]

the entire exact finite-shape error SDE can be written

\[
\boxed{
d\varepsilon_K
=
-\eta_0\cdot\dot{\widetilde h}\,d\sigma
+
\sqrt{2\nu}
\sum_\mu
\left(
\oint_{\widetilde Z}
\partial_{X_\mu}\beta_L\cdot d\xi
\right)dW^\mu.
}
\]

This representation creates no new bank.  It is the existing literal descent-error
SDE expressed in the local codeforming geometry.

The exact periodic one-mode NS shear reproduces its previously audited finite-surface
error and the exact anchor-noise coefficient from this one-form formula.

**Status: Exact identity / audited exact-NS calibration.  No new covariance species
and no restart/continuation/regularity theorem claimed.**
