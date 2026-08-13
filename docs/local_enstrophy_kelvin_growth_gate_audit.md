# Local enstrophy growth gate as a literal Navier--Stokes/Kelvin three-face law

This audit does not declare a new first-bad criterion.  It identifies exactly what
the surviving local enstrophy growth gate means inside the Navier--Stokes PDE.

Let

\[
e=\frac12|\omega|^2,
\qquad
S=\frac12(\nabla u+\nabla u^T).
\]

## 1. Exact local enstrophy balance

The incompressible vorticity equation is

\[
\partial_t\omega+(u\cdot\nabla)\omega
=(\omega\cdot\nabla)u+\nu\Delta\omega.
\]

Contract with `omega` and use

\[
\omega\cdot\Delta\omega
=\Delta e-|\nabla\omega|_F^2.
\]

Then

\[
\boxed{
(\partial_t+u\cdot\nabla-\nu\Delta)e
=\omega\cdot S\omega-\nu|\nabla\omega|_F^2.
}
\]

The symbolic implementation verifies that the enstrophy-balance residual is exactly
`omega` contracted with the vorticity-equation residual.

**Classification: Exact identity.**

## 2. The viscous enstrophy term is exactly the orientation-complete Kelvin q.v. bulk

For an arbitrary invertible material area frame `H`, the small-loop Kelvin q.v.
matrix is

\[
\Gamma_H
=2\nu H^T(\nabla\omega)(\nabla\omega)^T H.
\]

With packet metric

\[
M_H=(H^TH)^{-1},
\]

the exact normalized packet bulk is

\[
\boxed{
\frac12\operatorname{tr}(\Gamma_HM_H)
=\nu|\nabla\omega|_F^2.
}
\]

Thus the negative term in the local enstrophy balance is not merely an analytic
`H^1` dissipation norm.  It is the literal orientation-complete Kelvin Brownian q.v.
bulk reconstructed from the three closed-loop directions.

**Classification: Exact identity / exact physical typing.**

## 3. At a spatial critical point, the PDE has three literal faces

If

\[
\nabla e(x_*,t)=0,
\]

then the advective face vanishes at that point and

\[
\boxed{
\partial_t e
=\underbrace{\omega\cdot S\omega}_{\text{vortex stretching}}
-\underbrace{\nu|\nabla\omega|_F^2}_{\text{Kelvin q.v. bulk}}
+\underbrace{\nu\Delta e}_{\text{spatial curvature/diffusion}}.
}
\]

These are three different physical mechanisms and should not be merged before their
signs are understood.

**Classification: Exact identity.**

## 4. At a local maximum, positive margin is necessary but not sufficient for growth

At a spatial local maximum,

\[
\Delta e\le0.
\]

Define the stretching-over-Kelvin-bulk margin

\[
G=\omega\cdot S\omega-\nu|\nabla\omega|_F^2.
\]

Then

\[
\partial_t e=G+\nu\Delta e\le G.
\]

Hence

\[
\boxed{
\partial_t e>0
\quad\Longrightarrow\quad
G>-\nu\Delta e\ge0.
}
\]

In particular `G>0` is necessary, but it is **not sufficient even for instantaneous
positive growth of the local maximum** unless the curvature face is also controlled.
A positive margin smaller than `-nu Delta e` still gives negative time growth.

This is a sign consequence of the exact PDE identity, not a norm estimate.

**Classification: Rigorous consequence.**

## 5. ABC Beltrami family: every enstrophy critical point has zero stretching scalar

For the exact amplitude-scaled ABC Navier--Stokes family,

\[
\omega=u.
\]

For any Beltrami field with this normalization,

\[
(u\cdot\nabla)u
=\nabla\frac{|u|^2}{2}
\]

because `u x omega=0`.  Therefore

\[
\omega\cdot S\omega
=u\cdot(u\cdot\nabla u)
=u\cdot\nabla\frac{|u|^2}{2}
=u\cdot\nabla e.
\]

The symbolic audit proves the global identity

\[
\boxed{
\omega\cdot S\omega=u\cdot\nabla e
}
\]

for the entire ABC field, not merely at one sampled point.

Consequently, at **every** ABC enstrophy critical point,

\[
\nabla e=0
\quad\Longrightarrow\quad
\boxed{\omega\cdot S\omega=0.}
\]

Thus the arbitrary-amplitude smooth ABC family cannot activate a positive local-max
stretching gate at an enstrophy critical point.  The earlier single-point scope check
is strengthened to a full Beltrami theorem-domain statement.

**Classification: Exact identity / rigorous scope correction.**

## 6. Exact affine vortex: positive gate is a smooth local mechanism

The repository also contains the exact affine Navier--Stokes flow

\[
u(x,t)=A(t)x,
\]

with

\[
A(t)=
\begin{pmatrix}
-a&-r(t)&0\\
r(t)&-a&0\\
0&0&2a
\end{pmatrix},
\qquad
r(t)=r_0e^{2at}.
\]

Its vorticity is spatially uniform:

\[
\omega=(0,0,2r(t)).
\]

Hence

\[
\nabla e=0,
\qquad
\Delta e=0,
\qquad
\nabla\omega=0,
\qquad
\nu|\nabla\omega|^2=0.
\]

For `a>0`,

\[
\boxed{
\omega\cdot S\omega
=8a r(t)^2>0,
}
\]

and exactly

\[
\boxed{
\partial_t e=8a r(t)^2
=\omega\cdot S\omega.
}
\]

So the positive local growth gate is perfectly compatible with an exact smooth
Navier--Stokes mechanism on every finite time interval.  Here the gate records pure
vortex stretching, not a Brownian source and not an instantaneous loss of local
smoothness.

**Classification: Audited exact-NS mechanism calibration.**

## 7. The affine calibration does not refute the periodic/finite-energy target class

The affine velocity is linear in space.  Under an `x -> x+2pi e_x` shift, the
velocity changes by a nonzero constant vector determined by `A(t)`.  It is therefore
not a periodic torus solution and is not a finite-energy whole-space calibration.

Accordingly:

- it **does** prove that a positive local growth gate is a smooth local NS mechanism;
- it **does not** prove that a periodic/finite-energy first-bad criterion using
  additional global or scale structure is false;
- it **does not** prove regularity or singularity.

**Classification: Exact theorem-domain correction.**

## 8. Physical typing of the surviving growth gate

The local-max gate is therefore best typed as a **necessary instantaneous growth condition**, not as a continuation-failure detector:

1. stretching injects enstrophy into the vorticity direction;
2. orientation-complete Kelvin q.v. bulk removes local enstrophy through viscosity;
3. local curvature adds an additional nonpositive diffusion face at a maximum;
4. only after all three are combined can the time growth of the local maximum be
   known.

This is substantially more rigid than a raw threshold, but still does not define the
programme's first-bad event.

**Classification: Rigorous consequence of exact PDE/Kelvin identities.**

## 9. Remaining first-bad question

A viable first-bad mechanism must now do more than ask whether

\[
\omega\cdot S\omega-\nu|\nabla\omega|^2>0.
\]

It must retain at least the curvature face and the already-audited packet
support/gauge/history/event structure, and it must explain why the resulting event is
connected to continuation failure rather than ordinary smooth enstrophy growth.

**Status: first-bad local-growth-to-continuation bridge remains Open-literal.**

No restart/continuation/regularity theorem claimed.
