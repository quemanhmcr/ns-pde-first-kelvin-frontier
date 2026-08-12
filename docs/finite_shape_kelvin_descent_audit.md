# Finite-shape -> local Kelvin descent error audit

This note follows the literal reverse-age Navier--Stokes/Kelvin current one layer
below the full-state covariance theorem.  The target is not an estimate.  It is the
exact physical error made when a **finite material current/surface** is replaced by
its local Stokes jet at the anchor.

The audit deliberately keeps four objects distinct:

1. the actual backward material surface/current `R(.)`;
2. its actual oriented area vector `h_R`;
3. the Cauchy deformation `D` and its metric-dual coherent packet frame `H_C`;
4. stochastic covariance of any of these observables.

The first theorem below corrects an overtyped shorthand in the previous frontier:
`K_{Z_local(D,H)}` is not a literal full-current state until the geometry called `H`
has been specified.  The actual reverse-current area and the Cauchy metric-dual
packet frame have **opposite local connection signs**.  They cannot be identified by
notation.

No norm estimate, restart theorem, continuation theorem, singular-time bound, or
regularity conclusion is used.

---

## 1. Actual reverse-current geometry is not the Cauchy metric-dual packet geometry

Let reverse age be

\[
r=t-\sigma,
\qquad
dX_\sigma=-u(X_\sigma,r_\sigma)d\sigma
+\sqrt{2\nu}\,dW_\sigma.
\]

For an actual relative tangent `ell` of the material current being marched backward,

\[
\boxed{
\partial_\sigma \ell=-A(X,r)\ell,
\qquad A=\nabla u.
}
\]

Hence an infinitesimal actual reverse-current oriented area vector satisfies, for
incompressible flow,

\[
\boxed{
\partial_\sigma h_R=+A(X,r)^T h_R.
}
\]

By contrast, the stochastic Cauchy deformation convention already audited in the
repository is

\[
\partial_\sigma D=D A^T.
\]

Its same-replica coherent packet metric-dual area frame is

\[
H_C=\rho^2D^{-1},
\]

and therefore

\[
\boxed{
\partial_\sigma H_C=-A^T H_C.
}
\]

Thus

\[
\boxed{
\dot h_R=+A^T h_R,
\qquad
\dot H_C=-A^T H_C
}
\]

already at differential scale.

This is not a contradiction.  The two objects describe opposite geometric roles:
`h_R` is the area of the current being propagated backward in the full
current-shape state, whereas `H_C` is the metric-dual coherent packet associated
with the Cauchy deformation convention used to represent current-end vorticity.

**Status: Exact identity / theorem-type correction.**

A future bridge may relate these objects through a two-ended flow/state map, but
that bridge must be written explicitly.  It is not supplied by the symbol `H`.

**Status of direct identification `h_R = H_C`: false in general.**

---

## 2. The literal local Kelvin readout of a finite surface

Let `Sigma_R` be an oriented finite material spanning surface in the full state and

\[
Z(R)=\partial\Sigma_R.
\]

By Stokes,

\[
\boxed{
K_{Z(R)}
=\oint_{Z(R)}u^\flat
=\int_{\Sigma_R}\omega(X+r,r_{\rm phys})\cdot n_R\,dA.
}
\]

Write the actual oriented area vector

\[
\boxed{
h_R=\int_{\Sigma_R}n_R\,dA.}
\]

The first local Stokes jet is then not a modeled object.  It is simply

\[
\boxed{
K_{\rm loc}=\omega(X,r_{\rm phys})\cdot h_R.
}
\]

Therefore the exact finite-shape descent error is

\[
\boxed{
\varepsilon_K
:=K_{Z(R)}-K_{\rm loc}
=\int_{\Sigma_R}
[\omega(X+r)-\omega(X)]\cdot n_R\,dA.
}
\]

**Physical type:** finite-support vorticity-inhomogeneity flux.

It is not:

- a norm remainder;
- a stochastic q.v. by definition;
- a pressure/gauge term;
- deformation covariance;
- resolution covariance;
- selector covariance;
- `S^int` or irreducible content.

**Status: Exact Stokes identity / exact physical typing.**

---

## 3. Reverse-age area law for a finite surface: the first shape current

The actual reverse relative-shape velocity is

\[
-v_R(X,r)= -[u(X+r)-u(X)].
\]

Integrating the local incompressible area law over the finite surface gives

\[
\boxed{
\partial_\sigma h_R
=A(X)^T h_R+\mathcal R_A,
}
\]

where

\[
\boxed{
\mathcal R_A
:=\int_{\Sigma_R}
[A(X+r)-A(X)]^T n_R\,dA.
}
\]

`mathcal R_A` is the reverse-age sign of the forward finite-surface shape current
previously audited in `kelvin_shape_generator_audit.md`.

**Physical type:** finite-variation strain/velocity-gradient variation sampled over
the actual material shape.

There is no Brownian shape q.v. here because the common Wiener translation has been
removed by anchor-relative coordinates.

**Status: Exact material-surface identity.**

---

## 4. Reverse-age local vorticity has exact stretching cancellation against local area

From the genuine Navier--Stokes vorticity equation

\[
\partial_r\omega+u\cdot\nabla\omega
=A\omega+\nu\Delta\omega
\]

and

\[
dX=-u\,d\sigma+\sqrt{2\nu}\,dW,
\qquad dr=-d\sigma,
\]

Itô gives exactly

\[
\boxed{
d\omega(X,r)
=-A(X,r)\omega(X,r)d\sigma
+\sqrt{2\nu}\sum_\mu
\partial_\mu\omega(X,r)dW^\mu.
}
\]

There is no explicit Laplacian drift: the `+nu Delta` from anchor q.v. cancels the
viscous term after clock reversal.

Pair this with the finite-area law from Section 3.  Since `h_R` has finite variation,
there is no `d[omega,h_R]` term.  Therefore

\[
\begin{aligned}
d(\omega\cdot h_R)_{\rm drift}
&=(-A\omega)\cdot h_R
+\omega\cdot(A^T h_R+\mathcal R_A)\\
&=\omega\cdot\mathcal R_A.
\end{aligned}
\]

Thus

\[
\boxed{
\text{local-flux drift}=\omega(X)\cdot\mathcal R_A.
}
\]

The local vortex-stretching terms cancel exactly.  What survives is not “stretching
size”; it is the actual finite-shape failure of local Nanson closure.

**Status: Exact Navier--Stokes / Nanson / Itô identity.**

---

## 5. Exact SDE for the finite-shape Kelvin descent error

The full moving closed-current Kelvin observable has pure gauge finite-variation
drift, already audited.  Hence its reverse-age stochastic differential is

\[
 dK_{Z(R)}
=\sqrt{2\nu}\sum_\mu a_\mu(Z(R))\,dW^\mu,
\]

with

\[
a_\mu(Z)
=\left\langle\iota_{e_\mu}\Omega,Z\right\rangle.
\]

Constant-frame Cartan plus Stokes gives

\[
\boxed{
a_\mu(Z(R))
=\int_{\Sigma_R}\partial_\mu\omega(X+r)\cdot n_R\,dA.}
\]

The local flux has martingale coefficient

\[
\partial_\mu\omega(X)\cdot h_R.
\]

Define the **finite-support vorticity-gradient residual**

\[
\boxed{
q_\mu^{\rm err}
:=a_\mu(Z(R))-\partial_\mu\omega(X)\cdot h_R
=\int_{\Sigma_R}
[\partial_\mu\omega(X+r)-\partial_\mu\omega(X)]\cdot n_R\,dA.
}
\]

Subtracting the local flux SDE from the actual Kelvin SDE yields

\[
\boxed{
 d\varepsilon_K
=-\omega(X)\cdot\mathcal R_A\,d\sigma
+\sqrt{2\nu}\sum_\mu q_\mu^{\rm err}\,dW^\mu.
}
\]

This is the literal evolution equation requested by the previous frontier.

It has exactly two physical faces:

1. **finite-variation shape drift**
   \(-\omega\cdot\mathcal R_A\);
2. **anchor-translation stochastic spread**
   \(q_\mu^{\rm err}\).

No third shape-q.v. producer appears.

**Status: Exact identity on the smooth full reverse-age Kelvin current-shape state.**

---

## 6. Pathwise q.v. versus finite-horizon covariance: do not merge them

From Section 5,

\[
\boxed{
\frac{d}{d\sigma}[\varepsilon_K]_\sigma
=2\nu\sum_\mu(q_\mu^{\rm err})^2.
}
\]

But the Cauchy deformation is pathwise finite variation, so

\[
\boxed{
\frac{d}{d\sigma}
[\operatorname{vec}D,\varepsilon_K]_\sigma=0.
}
\]

This does **not** imply that finite-horizon

\[
\operatorname{Cov}(\operatorname{vec}D_h,\varepsilon_{K,h})
\]

vanishes.  Both observables sample the same Brownian anchor and can become
statistically correlated after finite time.

On the full augmented state, the connected-covariance source is the off-diagonal
anchor carré-du-champ

\[
\boxed{
\Gamma_{D\varepsilon}
=2\nu\sum_\mu
\operatorname{vec}(\partial_\mu\bar D)
\,\partial_\mu\bar\varepsilon_K.
}
\]

**Physical type:** finite-horizon same-ancestor covariance generated by common
anchor sampling.

It is not pathwise `[D,epsilon]`, and it is not a new branching mechanism.

**Status: Exact specialization of the existing connected-covariance theorem.**

---

## 7. Short-horizon joint hierarchy for deformation and descent error

At a smooth full current-shape state, hold the actual finite shape fixed at the
current end and set

\[
v_\mu
=\operatorname{vec}((\partial_\mu A)^T),
\qquad
q_\mu=q_\mu^{\rm err}ig|_{h=0}
=\partial_\mu\varepsilon_K\big|_{h=0}.
\]

Then the same response-Gram calculation used for `(vec D,K)` gives

\[
\boxed{
\operatorname{Var}(\varepsilon_K(h))
=2\nu h\sum_\mu q_\mu^2+O(h^2),
}
\]

\[
\boxed{
\operatorname{Cov}(\operatorname{vec}D_h,\varepsilon_K(h))
=\nu h^2\sum_\mu v_\mu q_\mu+O(h^3),
}
\]

and

\[
\boxed{
\Sigma_D(h)
=\frac{2\nu}{3}h^3\sum_\mu v_\mu v_\mu^T+O(h^4).
}
\]

All three leading blocks are one exact Gram integral:

\[
\boxed{
2\nu\sum_\mu\int_0^h
\begin{bmatrix}s v_\mu\\q_\mu\end{bmatrix}
\begin{bmatrix}s v_\mu\\q_\mu\end{bmatrix}^{T}ds.
}
\]

So the familiar

\[
h,\qquad h^2,\qquad h^3
\]

hierarchy survives with `K` replaced by the actual finite-shape descent error.

**Status: Rigorous consequence for locally smooth Navier--Stokes coefficients at a
fixed full current-shape state.**

This statement is not uniform near a candidate singular time.

---

## 8. Centered surfaces: the first bias carrier is the oriented quadrupole

Write the actual finite surface in anchor-relative coordinates `r`.  Suppose its
oriented first moment is centered:

\[
\int_{\Sigma_R}r_k n_R\,dA=0.
\]

Define the vector-valued oriented second moment

\[
\boxed{
\mathcal M_{k\ell}
:=\int_{\Sigma_R}r_kr_\ell n_R\,dA.
}
\]

Taylor expansion of the **literal flux identity** from Section 2 gives

\[
\boxed{
\varepsilon_K
=\frac12\sum_{k,\ell}
(\partial_{k\ell}\omega(X))\cdot\mathcal M_{k\ell}
+\text{higher shape moments}.
}
\]

The reverse strain-shape residual begins with the same geometric carrier:

\[
\boxed{
\mathcal R_A
=\frac12\sum_{k,\ell}
(\partial_{k\ell}A(X))^T\mathcal M_{k\ell}
+\text{higher shape moments}.
}
\]

But the stochastic error coefficient sees one more vorticity derivative:

\[
\boxed{
q_\mu^{\rm err}
=\frac12\sum_{k,\ell}
(\partial_{\mu k\ell}\omega(X))\cdot\mathcal M_{k\ell}
+\text{higher shape moments}.
}
\]

This is a physically important ordering:

- deterministic finite-shape bias: Hessian of vorticity;
- finite-variation shape drift: Hessian of velocity gradient;
- stochastic spread of the error: one more derivative of vorticity.

For isotropic surface scale `r`,

\[
\mathcal M_{k\ell}=O(r^4),
\]

so at a fixed smooth state

\[
\varepsilon_K=O(r^4),
\qquad
\mathcal R_A=O(r^4),
\qquad
q_\mu^{\rm err}=O(r^4),
\]

while

\[
\boxed{
\frac{d}{d\sigma}[\varepsilon_K]=O(r^8).
}
\]

Relative to the area scale `O(r^2)`, the deterministic flux bias is `O(r^2)`.
The error q.v. can therefore be much smaller than the bias it is measuring.

**Status: Rigorous local smooth expansion after exact physical typing; no uniform
singular-time estimate claimed.**

---

## 9. Exact cubic heat-shear counterexample: nonzero descent bias with zero drift,
## zero q.v., and zero deformation/error covariance

Take the exact smooth Navier--Stokes heat shear

\[
u=(U(y,t),0,0),
\qquad
U=y^3+6\nu t\,y.
\]

Then

\[
\omega_z=-U_y=-(3y^2+6\nu t).
\]

Use a centered material `xy` rectangle with half-widths `a,b` and normal `+e_z`.
The common backward shear preserves its `y`-relative coordinates and its `xy` area
form.  Direct Stokes integration gives

\[
K_{Z(R)}
=2a\int_{-b}^{b}
-[3(Y+r)^2+6\nu(t-h)]\,dr,
\]

where `Y` is the random anchor.  The local readout is

\[
K_{\rm loc}
=-4ab[3Y^2+6\nu(t-h)].
\]

The difference is exactly

\[
\boxed{
\varepsilon_K=-4ab^3,
}
\]

independent of:

- reverse age `h`;
- Brownian anchor `Y`;
- physical time;
- stochastic deformation `D`.

Therefore

\[
\boxed{
\varepsilon_K\neq0,
\qquad
\dot\varepsilon_K=0,
\qquad
[\varepsilon_K]=0,
\qquad
\operatorname{Var}(\varepsilon_K)=0,
\qquad
\operatorname{Cov}(\operatorname{vec}D,\varepsilon_K)=0.
}
\]

This is a decisive structural counterexample:

> stochastic covariance of the descent error does not control the deterministic
> finite-shape bias, even inside an exact smooth Navier--Stokes solution.

A covariance-only restart/descent argument can therefore miss a conserved
finite-shape mode completely.

The same value is exactly the quadrupole formula of Section 8, since

\[
\mathcal M_{yy}
=\frac{4}{3}ab^3e_z,
\qquad
\partial_{yy}\omega_z=-6.
\]

**Status: Audited calibration (exact Navier--Stokes) / rigorous covariance-only
no-go consequence.**

---

## 10. Exact one-mode periodic NS referee: the stochastic error channel can also be
## genuinely active

For

\[
U=e^{-\alpha t}\cos(ky),
\qquad
\alpha=\nu k^2,
\]

one has

\[
\omega_z=k e^{-\alpha t}\sin(ky).
\]

For the same centered `xy` rectangle,

\[
\boxed{
\varepsilon_0(y,t)
=C_b e^{-\alpha t}\sin(ky),
\qquad
C_b=4a[\sin(kb)-kb].
}
\]

Under the reverse common Brownian anchor,

\[
\varepsilon_h
=C_b e^{-\alpha(t-h)}\sin(kY_h).
\]

Thus the error itself is a genuine backward-Kelvin martingale in this calibration.
Its variance has short-age onset

\[
\boxed{
\operatorname{Var}(\varepsilon_h)
=2\nu h[\partial_y\varepsilon_0]^2+O(h^2).
}
\]

Let `c_h` be the active Cauchy deformation coefficient from the same shear.  Direct
Gaussian integration gives an exact closed form for

\[
\operatorname{Cov}(c_h,\varepsilon_h),
\]

and CI verifies the full mixed horizon equation.  Its leading term is

\[
\boxed{
\operatorname{Cov}(c_h,\varepsilon_h)
=\nu h^2 U_{yy}\,\partial_y\varepsilon_0+O(h^3).
}
\]

So exact NS independently referees both possibilities:

- cubic shear: finite descent bias active while covariance is completely blind;
- one-mode shear: anchor q.v. and deformation/error covariance genuinely active.

**Status: Audited calibration (exact periodic Navier--Stokes).**

---

## 11. Exact ABC referee: the finite-variation shape-drift face is genuinely active

Take the amplitude-scaled exact ABC/Beltrami solution

\[
 u=A_0e^{-\nu t}
\begin{pmatrix}
\sin z+\cos y\\
\sin x+\cos z\\
\sin y+\cos x
\end{pmatrix},
\qquad
\omega=u.
\]

At the origin, use the centered `xy` square `[-b,b]^2` with normal `+e_z`.  Direct
integration of the reverse strain-shape current gives

\[
\boxed{
\mathcal R_A
=4A_0e^{-\nu t}b[\sin b-b]\,e_y.
}
\]

Since

\[
\omega(0,t)=A_0e^{-\nu t}(1,1,1)^T,
\]

the descent-error drift is

\[
\boxed{
-\omega\cdot\mathcal R_A
=4A_0^2e^{-2\nu t}b[b-\sin b]
>0
\quad (0<b<\pi).
}
\]

The initial finite Kelvin flux bias is also nonzero:

\[
\boxed{
\varepsilon_K(0)
=4A_0e^{-\nu t}b[\sin b-b].
}
\]

Therefore the finite-variation shape-drift sector of Section 5 is not formal
bookkeeping.  Genuine 3D exact Navier--Stokes activates it.

**Status: Audited calibration (exact 3D periodic Navier--Stokes).**

---

## 12. No finite even-moment truncation closes the descent bias, and q.v. can be
## blind at the exposing symmetry point

For every `m>=1`, use the exact polynomial heat shear

\[
U_{2m+1}(y,t)=e^{\nu t\partial_{yy}}y^{2m+1}.
\]

Choose two symmetric width-surfaces

\[
w_0(y)=1,
\qquad
w_1(y)=1+\epsilon P_{2m}(y).
\]

Legendre orthogonality makes their area and every lower even moment

\[
0,2,\ldots,2m-2
\]

identical, but their `2m` moment differs.  Since the Kelvin flux for a shear uses
`-U_y`, the descent-bias difference is exactly

\[
\boxed{
\Delta\varepsilon_K
=-(2m+1)\epsilon
\int_{-1}^{1}y^{2m}P_{2m}(y)\,dy
\neq0.
}
\]

At the centered anchor, however, `U_{yy}` is odd while both width profiles are even.
Therefore

\[
\boxed{
\partial_X\varepsilon_K\big|_{X=0}=0
}
\]

for both surfaces, so the instantaneous error q.v. coefficient vanishes at exactly
the point where the unresolved higher shape moment is visible in the deterministic
bias.

Thus adding more covariance bookkeeping does not cure finite-moment shape blindness.
For every finite even-moment truncation, an exact NS heat shear exposes the next
unresolved deterministic flux mode.

**Status: Audited calibration family / rigorous finite-moment and covariance-blindness
no-go consequence.**

---

## 13. Ledger placement after the exact error equation

The finite-shape descent sector now has the following physical anatomy.

### Existing same-clock covariance face

`Var(epsilon_K)` and `Cov(vec D,epsilon_K)` are ordinary blocks of the same full-state
connected covariance theorem already used for `K_Z` and `D`.

**Status: Exact identity.**

### New physical payload, not a new covariance algebra

The new content is the literal observable

\[
\varepsilon_K
=\int[\omega(X+r)-\omega(X)]\cdot n\,dA
\]

and its two physical evolution faces

\[
-\omega\cdot\mathcal R_A,
\qquad
q_\mu^{\rm err}.
\]

**Status: Exact identity.**

### Deterministic bias sector

The value/mean of `epsilon_K` is not reconstructible from its covariance.  Cubic
heat shear proves that it can be nonzero while every covariance block involving the
error vanishes.

**Status: Rigorous no-go consequence.**

### Resolution covariance

If a reduced ancestry state hides the finite shape, law of total covariance can add
a separate resolution covariance of the conditional mean error.  That does not
retype the intrinsic full-state error covariance.

**Status: Exact generic decomposition given a lift; actual programme lift remains
Open-literal.**

### `S^int`, irreducible content, future-remaining bank

No identification is proved.

**Status: Open-literal.**

---

## 14. What the first-bad descent theorem would now have to prove

The previous vague target “make the full shape local” can now be stated more
literally.  Along the actual migrating selected support one would need, in a common
physical state/clock, control of at least:

\[
\varepsilon_K,
\qquad
\mathcal R_A,
\qquad
q_\mu^{\rm err},
\]

and the metric-whitened pair-covariance remainder, while preserving actual support
locality and the selector/boundary/exit/reset faces.

The exact calibrations show why no one face is sufficient:

- cubic shear: `epsilon_K != 0` with zero drift and zero q.v.;
- ABC: finite-variation `-omega dot R_A` is active;
- one-mode shear: stochastic `q_mu^err` and `Cov(D,error)` are active;
- polynomial/Legendre hierarchy: every finite moment truncation misses a higher
  deterministic shape mode.

So the next theorem cannot be a covariance theorem alone and cannot be an algebraic
finite-dimensional closure.  It must be a **genuine shrinking-support/jet-collapse
theorem for the actual first-bad material current**, or an exact NS counterexample to
such collapse.

Only after that state/descent question is settled does it make sense to introduce a
uniform estimate.

**Status: Open-literal.  No restart/continuation/regularity theorem claimed.**
