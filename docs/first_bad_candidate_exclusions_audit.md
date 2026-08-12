# Exact Navier--Stokes exclusion audit for naive first-bad predicates

The first-bad selector now has a literal missing-definition problem: `bad_flags` and
`resolved` are Boolean oracles, but the repository does not yet say which
Navier--Stokes event generates them.

Before proposing a new badness functional, this note lets exact smooth NS solutions
eliminate candidates that are too weak.  The calibration used here is the periodic
amplitude-scaled ABC/Beltrami family, so the exclusions stay inside a genuine smooth
3D periodic Navier--Stokes class.

The conclusion is deliberately narrow: a quantity may still be a useful diagnostic
or localization score even if it cannot, by itself, certify continuation failure.
No replacement threshold and no regularity theorem are claimed.

---

## 1. Exact periodic amplitude-scaled ABC family

Let

\[
U(x,y,z)=
\begin{pmatrix}
\sin z+\cos y\\
\sin x+\cos z\\
\sin y+\cos x
\end{pmatrix},
\qquad
u>0,
\]

and for arbitrary finite amplitude `A>0` define

\[
\boxed{
u_A(x,t)=A e^{-\nu t}U(x).}
\]

The base field is Beltrami:

\[
\boxed{
\nabla\times U=U,
\qquad
\nabla\cdot U=0,
\qquad
\Delta U=-U.
}
\]

Hence

\[
(u_A\cdot\nabla)u_A
=\nabla\frac{|u_A|^2}{2}
\]

and the exact pressure

\[
\boxed{p_A=-\frac12|u_A|^2}
\]

cancels the nonlinear acceleration.  Therefore

\[
\boxed{
\partial_tu_A+(u_A\cdot\nabla)u_A+\nabla p_A-\nu\Delta u_A=0
}
\]

for every finite `A` and all `t>=0`.

This is an explicit smooth periodic solution family with no finite-time loss of
regularity as amplitude varies.

**Classification: Exact 3D periodic Navier--Stokes identity.**

---

## 2. Raw instantaneous quantities can be arbitrarily large in that smooth family

At `(0,0,0)`, set

\[
a(t)=A e^{-\nu t}.
\]

Because `omega=u` in the Beltrami family, exact symbolic audit gives

\[
\boxed{|\omega|^2=3a^2,}
\]

\[
\boxed{e=\frac32a^2,}
\]

\[
\boxed{\omega\cdot S\omega=3a^3,}
\]

and the orientation-complete Kelvin bulk payment is

\[
\boxed{
\nu|\nabla\omega|^2
=\frac12\operatorname{tr}\Gamma_{\rm mf}
=3\nu a^2.
}
\]

Consequently

\[
\boxed{
\frac{\omega\cdot S\omega}{\nu|\nabla\omega|^2}
=\frac{a}{\nu}
=\frac{A e^{-\nu t}}{\nu}.
}
\]

At `t=0`, all of

\[
|\omega|^2,
\quad
e,
\quad
\omega\cdot S\omega,
\quad
\nu|\nabla\omega|^2,
\quad
\frac{\omega\cdot S\omega}{\nu|\nabla\omega|^2}
\]

can exceed any prescribed finite value by increasing `A`, while the exact periodic
solution remains smooth.

The local growth-margin diagnostic is likewise

\[
\boxed{
\mathfrak G
=\omega\cdot S\omega-\nu|\nabla\omega|^2
=3a^2(a-\nu),
}
\]

and is unbounded above with `A` at this point.

**Classification: Exact smooth-NS calibration.**

---

## 3. What this excludes

Suppose a proposed Boolean event has the form

\[
\texttt{bad}=\mathbf 1_{\{X>\Theta\}}
\]

with a universal finite threshold `Theta`, where `X` is any one of the raw
instantaneous quantities above evaluated at a point/germ.

Then the amplitude-scaled ABC family can make `bad=True` already at `t=0` while the
solution is an exact smooth periodic solution for all later time.

Therefore such a predicate cannot, **by itself**, mean

> continuation/restart has failed,

or

> a singularity is now forced.

This does **not** forbid using the same quantity to choose where to inspect, refine,
or localize.  A first-bad **diagnostic selector** may fire many times on smooth
solutions.  What is excluded is interpreting the raw threshold alone as a
continuation-failure certificate.

**Classification: Rigorous consequence of the exact ABC family.**

---

## 4. Explicit finite-threshold witnesses

At `t=0`, for any finite `T>0`:

### Vorticity-squared threshold

Choose

\[
A=\sqrt{\frac{T+1}{3}}.
\]

Then

\[
\boxed{|\omega(0,0)|^2=T+1>T.}
\]

### Stretching/Kelvin-bulk ratio threshold

Choose

\[
A=\nu(T+1).
\]

Then

\[
\boxed{
\frac{\omega\cdot S\omega}{\nu|\nabla\omega|^2}
=T+1>T.
}
\]

Analogous explicit amplitude choices cross any finite threshold on enstrophy,
stretching power, or Kelvin bulk q.v.

**Classification: Exact algebraic witnesses inside the smooth ABC family.**

---

## 5. Referee correction: this does not disprove the local-max growth gate

The repository previously derived the exact necessary condition

\[
(\partial_t+u\cdot\nabla)e>0
\quad\text{at a local enstrophy maximum}
\quad\Longrightarrow\quad
\omega\cdot S\omega>\nu|\nabla\omega|^2.
\]

The ABC origin has positive/unbounded `mathfrak G` for large amplitude, but it is
**not** an enstrophy critical point.  CI checks

\[
\boxed{\nabla e(0,0,0)\ne0.}
\]

Thus the origin witness must not be advertised as a counterexample to the
local-maximum hypothesis.

At the symmetric critical point

\[
(x,y,z)=\left(\frac\pi4,\frac\pi4,\frac\pi4\right),
\]

the exact Beltrami geometry gives

\[
\boxed{\nabla e=0,}
\qquad
\boxed{\omega\cdot S\omega=0.}
\]

So this ABC family does not falsify the necessary local-max gate.  The gate remains
exactly what it was classified as: a necessary local growth condition, **not** a
sufficient singularity or first-bad criterion.

**Classification: Exact referee scope check.**

---

## 6. Physical lesson for constructing `bad_flags`

The first-bad event definition cannot be obtained merely by choosing a sufficiently
large finite threshold for a raw instantaneous amplitude or a local
stretching/dissipation ratio.

The missing event must encode something closer to the actual restart obstruction,
for example a relation among

- physical scale/refinement `rho`,
- material deformation/support `F`,
- total co-deforming second moment `Q_tot`,
- reverse-age horizon/support geometry,
- finite-shape/localization remainder,
- boundary/exit/reset work,

rather than a single instantaneous magnitude.

This list is **not** a proposed formula.  It records the physical sectors already
forced by exact audits.  The subsequent support×bank audit derives one precise **scale-parametric**
conditional tensor bridge from these sectors without promoting it to a finite
threshold; its shrinking-scale/covariance-horizon identification remains explicit
and open.  See `docs/support_bank_restart_bridge_audit.md`.

**Classification: Rigorous exclusion of a class of naive predicates; construction
of the true badness functional remains open-literal.**

---

## 7. Updated badness frontier

Excluded as standalone universal continuation-failure flags:

- finite threshold on raw `|omega|^2`;
- finite threshold on raw enstrophy;
- finite threshold on instantaneous vortex stretching;
- finite threshold on instantaneous Kelvin bulk q.v.;
- finite threshold on the instantaneous stretching/Kelvin-bulk ratio;
- finite threshold on the raw growth-margin `mathfrak G` at an arbitrary point.

Not excluded / not promoted:

- the local-maximum growth gate remains a necessary PDE consequence only;
- any of the above may still be a diagnostic/localization score;
- scale/horizon/deformation/covariance coupled event definitions remain to be
  derived.

The programme still needs a literal NS badness functional and resolve predicate.
Both remain **Open-literal**.  The ABC origin is explicitly **not an enstrophy
critical point**, so this audit does not overstate the local-maximum gate scope.
Audit marker: origin is not an enstrophy critical point.

**Classification: Exact calibration-driven narrowing; no continuation/restart
claim.**
