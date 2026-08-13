# Exact motion law for a nondegenerate enstrophy critical point

This note asks a literal geometric question: if a spatial enstrophy critical point
moves in time, what velocity is forced by the Navier--Stokes PDE?

It does **not** identify the programme's first-bad selector with an enstrophy maximum.
The result applies conditionally if such a critical-point observable is chosen.

Let

\[
e(x,t)=\frac12|\omega(x,t)|^2
\]

and suppose a differentiable path `x_*(t)` satisfies

\[
\nabla e(x_*(t),t)=0.
\]

## 1. Differentiate the critical-point constraint before choosing a speed

Differentiating the exact constraint gives

\[
0=\frac d{dt}\nabla e(x_*(t),t)
=\partial_t\nabla e+H_e\dot x_*,
\]

where

\[
H_e=\nabla^2e.
\]

Thus

\[
\boxed{
H_e\dot x_*+\partial_t\nabla e=0.
}
\]

If `H_e` is invertible,

\[
\boxed{
\dot x_*=-H_e^{-1}\partial_t\nabla e.
}
\]

This is the local implicit-function speed of the critical branch.  It is derived from
the critical constraint itself, not guessed from fluid transport.

**Classification: Exact conditional identity on a differentiable nondegenerate critical branch.**

## 2. Insert the literal three-face Navier--Stokes growth law

From the previous audit,

\[
\partial_t e+u\cdot\nabla e
=G+\nu\Delta e,
\]

with

\[
G=\omega\cdot S\omega-\nu|\nabla\omega|_F^2.
\]

Take a spatial gradient.  At a critical point `grad e=0`,

\[
\nabla(u\cdot\nabla e)=H_eu.
\]

Therefore

\[
\partial_t\nabla e
=-H_eu
+\nabla\left(G+\nu\Delta e\right).
\]

Insert this into the differentiated critical constraint:

\[
\boxed{
H_e(\dot x_*-u)
+\nabla\left[
\omega\cdot S\omega
-\nu|\nabla\omega|_F^2
+\nu\Delta e
\right]
=0.
}
\]

For invertible `H_e`,

\[
\boxed{
\dot x_*-u
=-H_e^{-1}\nabla\left[
\omega\cdot S\omega
-\nu|\nabla\omega|_F^2
+\nu\Delta e
\right].
}
\]

Thus an enstrophy critical point is generally **not material**.

**Classification: Exact conditional Navier--Stokes identity.**

## 3. Relative critical speed has three physical gradient faces

The relative speed decomposes exactly as

\[
\boxed{
\dot x_*-u
=
-H_e^{-1}\nabla(\omega\cdot S\omega)
+H_e^{-1}\nabla\!\left(\nu|\nabla\omega|_F^2\right)
-\nu H_e^{-1}\nabla\Delta e.
}
\]

The three faces are:

1. **stretching-landscape drift**;
2. **Kelvin-q.v.-bulk landscape drift**;
3. **curvature-gradient drift**.

The same three local mechanisms that determine the critical value growth also
control how the critical geometry moves relative to the fluid.

**Classification: Exact conditional identity.**

## 4. The value growth along a critical path does not depend on its velocity

For any differentiable path,

\[
\frac d{dt}e(x_*(t),t)
=\partial_t e+\nabla e\cdot\dot x_*.
\]

At a critical point,

\[
\boxed{
\frac d{dt}e(x_*(t),t)=\partial_t e.
}
\]

So the path velocity matters for **where** the extremum goes, but not for the first
derivative of the extremal value itself.

**Classification: Exact identity.**

## 5. Exact periodic ABC referee: the strict maximum is fixed while fluid moves through it

For the exact periodic ABC Navier--Stokes family, the point

\[
x_*=\left(\frac\pi4,\frac\pi4,\frac\pi4\right)
\]

is an enstrophy critical point for all time.  Its Hessian is

\[
H_e
=-A^2e^{-2\nu t}
\begin{pmatrix}
1&1/2&1/2\\
1/2&1&1/2\\
1/2&1/2&1
\end{pmatrix},
\]

with

\[
\boxed{
\det H_e=-\frac12A^6e^{-6\nu t}\ne0.
}
\]

The Sylvester signs show this Hessian is negative definite, so the point is a strict
nondegenerate local maximum.

Its fluid velocity is

\[
\boxed{
u(x_*,t)
=\sqrt2Ae^{-\nu t}(1,1,1)^T\ne0.}
\]

But the ABC spatial shape is fixed, so the critical point itself has

\[
\boxed{\dot x_*=0.}
\]

The exact critical-speed formula reconstructs `xdot_*=0`; equivalently, the relative
critical drift is exactly

\[
\boxed{\dot x_*-u=-u.}
\]

Therefore even in the periodic smooth target class, a nondegenerate enstrophy
maximum need not move with the fluid velocity.

**Classification: Audited exact periodic-NS calibration / rigorous no-material-max consequence.**

## 6. Degenerate critical sets do not have a unique inverse-Hessian speed

For the exact affine vortex calibration, enstrophy is spatially uniform.  Hence

\[
\nabla e=0,
\qquad
H_e=0,
\qquad
\nabla(G+\nu\Delta e)=0.
\]

The critical-speed constraint becomes

\[
0=0.
\]

Every differentiable spatial path remains an enstrophy critical path.  Two different
trial velocities in the symbolic referee both satisfy the exact speed residual.

Thus the inverse-Hessian formula has a sharp theorem domain: it is not meaningful at
a degenerate critical set.  The API explicitly rejects singular Hessians rather than
returning a formal inverse.

**Classification: Audited exact-NS degeneracy calibration / theorem-domain correction.**

## 7. This is not the first-bad quantile speed law

The programme's generic moving quantile/shell law and hysteretic first-bad selector
remain different typed objects.  This critical-point formula becomes a candidate
first-bad speed law only after all of the following are proved:

- the first-bad observable is actually local enstrophy;
- the active branch is a differentiable nondegenerate critical maximum;
- the relevant support/local packet is tied to that branch;
- selector/refinement/reset events are reconciled with branch creation, loss, and
  Hessian degeneracy.

None of those identifications is supplied merely by the critical-point calculation.

**Status: first-bad critical-path identification remains Open-literal.**

## 8. Physical payoff

A moving enstrophy maximum has a small rigid law:

- its **value** obeys the three-face stretching/Kelvin-bulk/curvature balance;
- its **position relative to the fluid** is driven by the spatial gradients of those
  same three faces through the enstrophy Hessian;
- Hessian degeneracy is a real geometry event where unique critical-lineage speed can
  fail.

This is the kind of simplification that appears only after keeping the literal PDE
geometry intact.

No restart/continuation/regularity theorem claimed.
