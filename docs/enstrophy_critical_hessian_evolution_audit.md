# Enstrophy critical-Hessian evolution and curvature-volume law

This audit continues the literal geometry of a differentiable enstrophy critical
branch.  The previous layer derived the critical-point speed.  Here the question is:

> how does the **curvature tensor** of the critical point evolve, and what can make a
> nondegenerate critical branch lose nondegeneracy?

Nothing in this note identifies an enstrophy critical branch with the programme's
actual first-bad object.  The statements below are conditional critical-geometry
identities.

## 1. Exact Hessian evolution on a moving critical branch

Let a scalar `e` satisfy

\[
\partial_t e+u\cdot\nabla e=R,
\]

and let `x_*(t)` be a differentiable critical path,

\[
\nabla e(x_*(t),t)=0.
\]

Write

\[
H=\nabla^2e.
\]

Taking two spatial derivatives of the scalar equation and using `grad e=0` at the
critical point gives

\[
\nabla^2(u\cdot\nabla e)
=(\nabla u)^TH+H\nabla u+(u\cdot\nabla)H.
\]

Therefore the pathwise Hessian derivative is

\[
\boxed{
\frac{d_*H}{dt}
=
\nabla^2R
-(\nabla u)^TH-H\nabla u
+((\dot x_*-u)\cdot\nabla)H.
}
\]

The three literal faces are:

1. **growth-landscape curvature** `Hess R`;
2. **local fluid connection/congruence** `-(grad u)^T H-H grad u`;
3. **relative critical transport** of the Hessian through its third spatial
   derivatives.

For enstrophy,

\[
R
=\omega\cdot S\omega
-\nu|\nabla\omega|_F^2
+\nu\Delta e.
\]

Thus the critical curvature is driven by the second spatial derivatives of the same
stretching/Kelvin-bulk/curvature growth landscape that already controls critical
value growth and critical-point motion.

**Classification: Exact conditional identity on a differentiable critical branch.**

## 2. The local connection splits into strain reshaping and rigid rotation

Write

\[
\nabla u=S+W,
\qquad S^T=S,
\qquad W^T=-W.
\]

Then

\[
\boxed{
-(\nabla u)^TH-H\nabla u
=-(SH+HS)+(WH-HW).
}
\]

The first term is **strain reshaping** of the local enstrophy curvature.  The second
is a **rotation commutator**.

These faces can be nonzero even when their determinant-volume effect vanishes.  In
particular, incompressibility does **not** freeze Hessian eigenvalues, anisotropy, or
eigendirections.

**Classification: Exact identity / exact physical typing.**

## 3. Curvature-volume rate and the incompressible cancellation

On a nondegenerate branch, Jacobi's formula gives

\[
\boxed{
\frac d{dt}\log|\det H|
=\operatorname{tr}(H^{-1}\dot H).
}
\]

The local connection contribution is

\[
\begin{aligned}
\operatorname{tr}\!\left[
H^{-1}(-(\nabla u)^TH-H\nabla u)
\right]
&=-\operatorname{tr}(H^{-1}(\nabla u)^TH)
  -\operatorname{tr}(\nabla u)\\
&=-2\operatorname{tr}(\nabla u).
\end{aligned}
\]

Hence

\[
\boxed{
\text{connection logdet rate}=-2\,\nabla\cdot u.
}
\]

For incompressible Navier--Stokes,

\[
\boxed{
\nabla\cdot u=0
\quad\Longrightarrow\quad
\text{connection logdet rate}=0.
}
\]

This is a genuine cancellation of **curvature volume rate**, not of curvature shape.
The symbolic referee contains a trace-free velocity gradient for which the connection
matrix is nonzero while its `log|det H|` contribution is exactly zero.

**Classification: Exact identity / exact incompressible cancellation.**

## 4. Strain and rotation separately preserve curvature volume in incompressible flow

For the split connection,

\[
C_S=-(SH+HS),
\qquad
C_W=WH-HW.
\]

Their log-determinant rates are

\[
\boxed{
\operatorname{tr}(H^{-1}C_S)=-2\operatorname{tr}S,
}
\]

and

\[
\boxed{
\operatorname{tr}(H^{-1}C_W)=0.
}
\]

The rotation commutator preserves curvature volume for every flow.  In an
incompressible flow `tr S=0`, so the strain face also has zero curvature-volume
rate.

Nevertheless both faces can redistribute the Hessian spectrum and rotate its
principal directions.  Zero determinant-rate is not zero Hessian dynamics.

**Classification: Exact identity / theorem-type correction.**

## 5. Incompressible critical curvature-volume law

Substituting the three Hessian faces into Jacobi's formula gives

\[
\frac d{dt}\log|\det H|
=
\operatorname{tr}(H^{-1}\nabla^2R)
+\operatorname{tr}(H^{-1}C_{\rm conn})
+\operatorname{tr}\!\left[
H^{-1}((\dot x_*-u)\cdot\nabla)H
\right].
\]

For incompressible Navier--Stokes the middle face vanishes exactly:

\[
\boxed{
\frac d{dt}\log|\det H|
=
\operatorname{tr}(H^{-1}\nabla^2R)
+
\operatorname{tr}\!\left[
H^{-1}((\dot x_*-u)\cdot\nabla)H
\right].
}
\]

Thus, on a nondegenerate enstrophy critical branch, the local curvature volume can
change only through:

1. **growth-landscape curvature**; and
2. **relative critical transport through Hessian inhomogeneity**.

The volume-preserving local linear fluid deformation does not directly change this
scalar curvature volume.

**Classification: Rigorous consequence of exact identities, conditional on branch nondegeneracy.**

## 6. Jacobi determinant law

For every differentiable invertible Hessian,

\[
\boxed{
\frac d{dt}\det H
=\det H\,\operatorname{tr}(H^{-1}\dot H).
}
\]

Hence on an interval where the branch is already smooth and nondegenerate,

\[
\boxed{
\det H(t)
=\det H(t_0)
\exp\!\left(
\int_{t_0}^{t}
\operatorname{tr}(H^{-1}\dot H)\,ds
\right).
}
\]

This is a critical-geometry identity.  It does not bound the integral and does not
assert that the Navier--Stokes solution remains smooth.

**Classification: Exact conditional identity.**

## 7. Conditional nondegeneracy consequence

Suppose a differentiable critical branch is nondegenerate on `[t_0,T)` and

\[
\det H(t_0)\ne0.
\]

If the integrated log-determinant rate has a finite limit,

\[
\lim_{t\uparrow T}
\int_{t_0}^{t}
\operatorname{tr}(H^{-1}\dot H)\,ds
\in\mathbb R,
\]

then the exact exponential law gives a nonzero finite limit for `det H(t)`.
Therefore that branch cannot reach Hessian degeneracy continuously at `T`.

Equivalently, if a smooth nondegenerate branch approaches

\[
\det H(t)\to0
\qquad (t\uparrow T)
\]

from a nonzero initial determinant, then necessarily

\[
\boxed{
\int_{t_0}^{t}
\operatorname{tr}(H^{-1}\dot H)\,ds
\to-\infty.
}
\]

This is only a **conditional critical-branch nondegeneracy criterion**.  It is not a
Navier--Stokes continuation criterion: the branch may cease to be the relevant
observable for other reasons, and no uniform PDE estimate for this log-rate has been
proved.

**Classification: Rigorous conditional consequence.**

## 8. Exact periodic ABC calibration

At the exact periodic ABC strict enstrophy maximum from the previous audit,

\[
H(t)
=-A^2e^{-2\nu t}
\begin{pmatrix}
1&1/2&1/2\\
1/2&1&1/2\\
1/2&1/2&1
\end{pmatrix}.
\]

Therefore

\[
\boxed{\dot H=-2\nu H}
\]

and

\[
\boxed{
\frac d{dt}\log|\det H|=-6\nu.
}
\]

The exact determinant is

\[
\boxed{
\det H(t)
=-\frac12A^6e^{-6\nu t},
}
\]

which remains nonzero for every finite time.

The local fluid gradient is incompressible, and the symbolic audit verifies that its
connection log-determinant contribution is exactly zero.  Thus the observed `-6nu`
curvature-volume decay is carried by the non-connection faces, consistently with the
general cancellation law.

**Classification: Audited exact periodic-Navier--Stokes calibration.**

## 9. Hessian degeneracy is a real theorem boundary

All inverse-Hessian and `log|det H|` formulas require

\[
\det H\ne0.
\]

At a degenerate critical set such as the exact affine uniform-enstrophy calibration,
`H=0`; `H^{-1}` and the log-determinant rate are not physical objects.  The symbolic
API rejects singular Hessians instead of returning a formal expression.

Critical branch creation, annihilation, merging, splitting, or loss of a unique
implicit-function lineage must therefore be treated as a finite geometry/event seam,
not crossed by silently extending the inverse-Hessian formulas.

**Classification: Exact theorem-domain correction / Open-literal event seam.**

## 10. Updated first-bad frontier

The local enstrophy critical geometry now has a compact exact hierarchy:

- **value:** stretching - Kelvin bulk + curvature;
- **position:** gradients of those faces through `H^{-1}`;
- **curvature tensor:** growth Hessian + local connection + relative transport;
- **curvature volume:** for incompressible flow, only growth-Hessian and relative
  transport faces survive in `d log|det H|/dt`.

What remains unproved is the programme-specific identification:

- that the first-bad object is an enstrophy critical branch;
- that the relevant branch remains support-local and physically coupled to the
  Kelvin packet state;
- that its Hessian log-rate has a useful uniform bound;
- that branch degeneracy corresponds to a first-bad selector event or continuation
  failure.

**Status: first-bad critical-branch degeneracy identification remains Open-literal.**

No restart/continuation/regularity theorem claimed.
