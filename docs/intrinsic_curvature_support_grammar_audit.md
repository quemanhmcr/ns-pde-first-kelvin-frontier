# Intrinsic curvature--support kernel grammar

This milestone asks a narrower question than support locality itself:

> At a max-normalized enstrophy maximum, what exact Navier--Stokes law decides whether a spatially flat direction remains flat, becomes localized, or makes the maximum branch nonviable?

No score or threshold is introduced.  The answer comes from composing the exact local enstrophy PDE with the exact Cauchy/Nanson transport representation.

No first-bad identification, restart, continuation, or regularity theorem is claimed.

## 1. The local normalized scalar law

Let

\[
e=\frac12|\omega|^2,\qquad M(t)>0,\qquad g=\frac eM.
\]

For Navier--Stokes,

\[
D_t e=R,
\qquad
R=\omega\!\cdot S\omega-\nu|\nabla\omega|^2+\nu\Delta e,
\qquad D_t=\partial_t+u\cdot\nabla.
\]

Hence

\[
\boxed{D_tg=\Phi},
\qquad
\Phi=\frac RM-\frac{\dot M}{M}g.
\]

At a smooth spatial maximum of `g`, `grad g=0` and

\[
Q:=-\nabla^2g\succeq0.
\]

The commutator of the material derivative with the scalar Hessian is

\[
D_t(\nabla^2g)
=
\nabla^2\Phi-(\nabla u)^T\nabla^2g-\nabla^2g\,\nabla u
-\sum_k (\partial_k g)\nabla^2u_k.
\]

The last term vanishes exactly at a critical point.  Writing `A=grad u` and

\[
\mathcal K:=-\nabla^2\Phi,
\]

we obtain

\[
\boxed{D_tQ+A^TQ+QA=\mathcal K.}
\]

**Classification: Exact local Navier--Stokes identity.**

## 2. Why the connection is not a source of localization

If the right-hand side were zero,

\[
D_tQ=-A^TQ-QA.
\]

Under the deformation gradient `Fdot=A F`, this integrates as

\[
Q(t)=F(t)^{-T}Q(t_0)F(t)^{-1}.
\]

Thus the connection-only flow is a congruence action.  It preserves positivity, inertia, and rank exactly.  It can rotate and reshape curvature but cannot create or destroy a flat direction.

This is the singular-Hessian extension of the earlier incompressible log-determinant cancellation: it requires neither `Q^{-1}` nor `det Q != 0`.

**Classification: Rigorous consequence of the exact covariant law.**

## 3. Physical support is the dual representation

A physical material line frame obeys

\[
D_tL=AL.
\]

Define the curvature seen in packet coordinates by

\[
\boxed{\mathfrak C=L^TQL.}
\]

It is dimensionless under Navier--Stokes similarity: `Q` has inverse-length-square weight while `L` has length weight.

Differentiate and use the two exact transport laws:

\[
\begin{aligned}
D_t\mathfrak C
&=(AL)^TQL+L^T(-A^TQ-QA+\mathcal K)L+L^TQ(AL)\\
&=\boxed{L^T\mathcal K L}.
\end{aligned}
\]

All deformation-connection terms cancel matrix-wise, not merely after taking a trace.

With `B=LL^T`, the scalar pairing obeys

\[
\boxed{D_t\operatorname{tr}(QB)=\operatorname{tr}(\mathcal K B).}
\]

This is the exact curvature--support duality law.

**Classification: Exact Cauchy/Nanson--curvature compatibility identity.**

## 4. Moving critical branches add exactly one geometric face

A critical branch need not be material.  Let

\[
c=\dot x_*-u(x_*,t).
\]

Along that branch,

\[
\dot Q=D_tQ+(c\cdot\nabla)Q.
\]

If the local support frame is carried by the same Nanson connection `Ldot=A L`, then

\[
\boxed{
\frac d{dt}(L^TQL)
=L^T\mathcal K_*L,
\qquad
\mathcal K_*=\mathcal K+(c\cdot\nabla)Q.
}
\]

There are therefore exactly two continuous faces that can change curvature relative to physical support:

1. local normalized Navier--Stokes source curvature `K`;
2. literal critical-set reanchoring through spatial curvature variation.

There is no selector force.

**Classification: Exact moving-critical/Nanson consequence.**

## 5. The global normalization disappears on the flat subspace

For max normalization,

\[
\mathcal K
=-\frac1M\nabla^2R-\frac{\dot M}{M}Q.
\]

Let `P0` be the orthogonal projector onto `ker Q`.  Since `P0 Q=0`,

\[
\boxed{
P_0\mathcal K P_0
=-\frac1M P_0(\nabla^2R)P_0.
}
\]

Thus the law deciding whether a second-order flat direction opens is independent of the global normalization rate.  It is local Navier--Stokes physics:

\[
-\nabla^2R
=-\nabla^2(\omega\cdot S\omega)
+\nu\nabla^2|\nabla\omega|^2
-\nu\nabla^2\Delta e.
\]

On a moving branch one adds only `P0[(c.grad)Q]P0`.

**Classification: Exact kernel reduction / local-physics consequence.**

## 6. The PSD tangent-cone compatibility law

At every smooth spatial maximum,

\[
Q\succeq0.
\]

Suppose a differentiable maximum branch persists for `t>=t0`.  Then

\[
\mathfrak C(t)=L(t)^TQ(t)L(t)\succeq0.
\]

Choose `z` so that `xi=L(t0)z` lies in `ker Q(t0)`.  Then

\[
f(t)=z^T\mathfrak C(t)z\ge0,
\qquad f(t_0)=0.
\]

Hence `f'_+(t0)>=0`.  The exact grammar gives

\[
f'_+(t_0)=\xi^T\mathcal K_*\xi.
\]

Therefore a right-persistent maximum branch must satisfy

\[
\boxed{P_0\mathcal K_*P_0\succeq0.}
\]

This is precisely the tangent-cone condition for the PSD curvature cone after the congruence connection has been removed.

Its physical meanings are forced:

- negative kernel direction: the branch cannot remain a maximum to the right;
- positive kernel direction: NS creates second-order curvature there;
- zero kernel compression: flatness survives to first order and higher-order PDE geometry must decide.

If a differentiable maximum branch persists on both sides with constant curvature rank, the kernel compression must vanish at first order.

**Classification: Rigorous consequence / intrinsic branch-viability theorem.**

## 7. Exact NS referee I: persistent blind directions

For the exact periodic one-mode heat shear from the previous milestone,

\[
g=\cos^2(ny).
\]

At `y=0`,

\[
\boxed{Q=\operatorname{diag}(0,2n^2,0)}.
\]

The normalized profile is stationary and `u.grad g=0`, so

\[
\boxed{\mathcal K=0}.
\]

Thus the `x` and `z` flat directions receive zero first-order opening.  This is exactly the transverse-support persistence seen in the prior chamber no-go.

**Classification: Audited exact-NS calibration.**

## 8. Exact NS referee II: diffusion closes a quartic flat direction

Consider the literal periodic 3D heat shear

\[
u=(U(z,t),0,0),
\]

with

\[
U=5e^{1-\nu t}\sin z
+\frac12e^{4-4\nu t}\sin2z
-\frac13e^{9-9\nu t}\sin3z.
\]

Its nonlinear term vanishes and `U_t=nu U_zz`, so it is an exact incompressible Navier--Stokes solution with constant pressure.

At `T=1/nu`, its vorticity scalar is

\[
q_*(z)=5\cos z+\cos2z-\cos3z.
\]

Writing `c=cos z`,

\[
q_*(c)=-4c^3+2c^2+8c-1.
\]

The exact certificates are

\[
5-q_*=2(c-1)^2(2c+3)\ge0,
\]

and

\[
q_*'(c)=-4(c-1)(3c+2).
\]

The only candidates for the lower extreme are `c=-1` and `c=-2/3`, where

\[
q_*(-1)=-3,
\qquad
q_*(-2/3)=-115/27>-5.
\]

Hence `z=0` is the unique global maximum of `|q_*|`, with `q_*(0)=5` and

\[
M(T)=25/2.
\]

At this global enstrophy maximum,

\[
Q(T)=0,
\qquad
\partial_z^4e(0,T)=-300<0.
\]

It is a strict quartic maximum, completely flat at second order.

Yet the exact source curvature is

\[
\boxed{\mathcal K(T)=24\nu\,e_z\otimes e_z.}
\]

More sharply, the three physical source-curvature faces are

\[
\mathcal K_{\rm stretch}=0,
\qquad
\mathcal K_{\rm Kelvin\ bulk}=0,
\qquad
\boxed{\mathcal K_{\rm curvature\ diffusion}=24\nu\,e_z\otimes e_z.}
\]

Thus

\[
\boxed{\partial_tQ_{zz}(T)=24\nu>0.}
\]

Diffusion itself converts a quartically flat global maximum into a quadratically localized direction.  The two translation-symmetry directions remain flat.

**Classification: Audited exact-NS global calibration / rigorous kernel-opening consequence.**

## 9. What this changes in the proof architecture

The previous milestone showed that scalar compatibility and Kelvin residual collapse cannot see transverse support.  This milestone identifies the exact endogenous law that decides whether such support can remain hidden.

The grammar is short:

\[
\boxed{
D_tQ+A^TQ+QA=\mathcal K,
\qquad
D_tL=AL,
\qquad
D_t(L^TQL)=L^T\mathcal K L.
}
\]

At a moving maximum, replace `K` by `K_* = K+(c.grad)Q`.

The connection transports geometry but cannot change curvature rank.  Rank-changing/flat-direction closure is entirely a source-curvature/reanchoring event.  On `ker Q`, even max normalization drops out.

This is a genuine compatibility theorem rather than an externally imposed badness mechanism.

## 10. Explicit frontier

**Open-literal:** no theorem yet identifies a genuine Navier--Stokes first-bad state with a failure of the PSD kernel-viability condition.

**Open-literal:** when `P0 K_* P0=0`, no theorem yet proves that the higher-order intrinsic jet hierarchy must eventually close every support-carrying flat direction.

**Open:** uniform singular-time support/refinement control, restart capacity, continuation, and global regularity.

The curvature scale is not identified with the Kelvin diffusion length merely from dimensional similarity.

No restart/continuation/regularity theorem claimed.
