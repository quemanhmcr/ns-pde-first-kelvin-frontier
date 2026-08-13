# Enstrophy critical-branch competition and value-crossing events

The preceding audits separated critical-value growth, critical-point motion, and
critical-Hessian degeneracy.  A different event remains possible even when the
underlying critical objects persist smoothly:

> two candidate critical branches/critical sheets can exchange which one has the
> larger enstrophy value.

This **value-crossing event** is an observer/ranking event, not automatically a
critical-geometry birth/death event and not automatically a Navier--Stokes
continuation failure.

## 1. Two-branch value gap

Let two differentiable critical objects have enstrophy values

\[
e_1(t),\qquad e_2(t).
\]

Define the ranking gap

\[
\boxed{\Delta e=e_1-e_2.}
\]

Then

\[
\boxed{\dot{\Delta e}=\dot e_1-\dot e_2.}
\]

A value crossing at `t=t_*` satisfies

\[
\Delta e(t_*)=0.
\]

If

\[
\dot{\Delta e}(t_*)\ne0,
\]

the crossing is transverse.  A positive gap rate means branch `2` wins immediately
before the crossing and branch `1` immediately after; a negative gap rate gives the
opposite orientation.

**Classification: Exact identity / elementary transverse-crossing consequence.**

## 2. Navier--Stokes branch-rate difference keeps the three physical faces

At an enstrophy critical point/sheet, each branch value rate is

\[
\dot e_i
=\mathcal S_i-\mathcal K_i+\mathcal C_i,
\]

where

\[
\mathcal S_i=\omega\cdot S\omega,
\qquad
\mathcal K_i=\nu|\nabla\omega|^2,
\qquad
\mathcal C_i=\nu\Delta e.
\]

Therefore the crossing gap rate is exactly

\[
\boxed{
\dot{\Delta e}
=(\mathcal S_1-\mathcal S_2)
-(\mathcal K_1-\mathcal K_2)
+(\mathcal C_1-\mathcal C_2).
}
\]

The ranking competition has its own literal three-face ledger: relative stretching,
relative Kelvin-bulk loss, and relative curvature diffusion.  No norm or threshold
has been inserted.

**Classification: Exact conditional Navier--Stokes identity.**

## 3. Value crossing and Hessian degeneracy are different event surfaces

The condition

\[
e_1=e_2
\]

places one scalar constraint on the two branch values.  Critical-Hessian degeneracy
instead requires

\[
\det H_i=0
\]

for one of the branches.  There is no algebraic implication between these
conditions.

A full three-dimensional geometry calibration makes this explicit.  Take two local
strict maxima with branch values

\[
e_1^*(t)=t,
\qquad
e_2^*(t)=-t,
\]

and fixed Hessians

\[
H_1=-2I,
\qquad
H_2=-4I.
\]

At `t=0`,

\[
e_1^*=e_2^*,
\qquad
\dot{\Delta e}=2,
\]

while

\[
\det H_1=-8\ne0,
\qquad
\det H_2=-64\ne0.
\]

Thus a transverse ranking crossing is geometrically compatible with two fully
nondegenerate strict maxima.

This calibration is pure critical-point geometry, **not** a Navier--Stokes solution.
Its role is only to prove independence of the two event conditions.

**Classification: Audited geometric calibration / theorem-domain separation.**

## 4. Exact periodic Navier--Stokes crossing calibration

Consider the periodic shear

\[
u=(U(y,t),0,0)
\]

with

\[
\boxed{
U(y,t)=
-e^{-\nu t}\sin y
-\frac32e^3e^{-4\nu t}\sin 2y
+\frac13e^8e^{-9\nu t}\sin 3y.
}
\]

Because `U` is independent of `x`,

\[
(u\cdot\nabla)u=0,
\]

and every Fourier mode solves the heat equation.  Hence with constant pressure this
is an exact periodic Navier--Stokes solution.

Its vorticity is

\[
\omega=(0,0,w),
\]

with

\[
w(y,t)=
e^{-\nu t}\cos y
+3e^3e^{-4\nu t}\cos2y
-e^8e^{-9\nu t}\cos3y.
\]

The enstrophy is

\[
e=\frac12w^2.
\]

The sheets `y=0` and `y=pi` are critical for all time because `w_y=0` there.
Translation symmetry leaves flat `x,z` directions, so these are critical **sheets**,
not isolated three-dimensional critical points.

**Classification: Exact periodic Navier--Stokes calibration.**

## 5. Exact crossing time and transverse curvature

At

\[
\boxed{t_*=\frac1\nu,}
\]

the odd-mode contributions cancel in the branch-value difference.  Both critical
sheets have the same value

\[
\boxed{
e_0(t_*)=e_\pi(t_*)=\frac92e^{-2}.
}
\]

Their transverse `y` Hessians are

\[
\boxed{
\partial_{yy}e(0,t_*)=-12e^{-2},
}
\]

and

\[
\boxed{
\partial_{yy}e(\pi,t_*)=-60e^{-2}.
}
\]

Both are strictly negative and nonzero.  Hence neither critical sheet is being
created, destroyed, or losing its transverse-max character at the crossing.

The full three-dimensional Hessian is still degenerate because the shear has exact
`x,z` translation symmetries.  The calibration therefore proves persistence of the
critical sheets and nondegeneracy of the physically active transverse curvature; it
does **not** supply a full isolated-Hessian NS crossing example.

**Classification: Audited exact-NS critical-sheet calibration / scope correction.**

## 6. Winner switch is transverse

Let

\[
\Delta e(t)=e(0,t)-e(\pi,t).
\]

The exact formula changes sign across `t_*`:

- for `t<t_*` near the crossing, `Delta e<0`, so the `y=pi` sheet has larger
  enstrophy;
- for `t>t_*` near the crossing, `Delta e>0`, so the `y=0` sheet wins.

At the crossing,

\[
\boxed{
\dot{\Delta e}(t_*)=48\nu e^{-2}>0.
}
\]

Thus the ranking switch is transverse.

**Classification: Audited exact-Navier--Stokes calibration.**

## 7. The crossing is pure curvature-rate competition

At both critical sheets and at the crossing,

\[
\omega\cdot S\omega=0
\]

and

\[
\nu|\nabla\omega|^2=0.
\]

Therefore each branch rate is carried entirely by the curvature face:

\[
\boxed{
\dot e_0(t_*)
=\nu\Delta e(0,t_*)
=-12\nu e^{-2},
}
\]

and

\[
\boxed{
\dot e_\pi(t_*)
=\nu\Delta e(\pi,t_*)
=-60\nu e^{-2}.
}
\]

Both branch values are decreasing.  The winner switches only because the `y=pi`
branch decays faster.

Consequently a first-bad/ranking switch does not require positive local growth of the
new winner and does not require a singular local mechanism.  It can be a smooth
competition of decay rates.

**Classification: Audited exact-NS calibration / rigorous no-growth-switch consequence.**

## 8. The selected maximum is continuous but its derivative can switch

For the non-hysteretic envelope

\[
M(t)=\max\{e_0(t),e_\pi(t)\},
\]

the crossing values agree, so

\[
\boxed{M(t_*^-)=M(t_*^+).}
\]

There is no scalar state jump at the tie.

But the one-sided derivatives are

\[
M'_-(t_*)=-60\nu e^{-2},
\qquad
M'_+(t_*)=-12\nu e^{-2},
\]

so

\[
\boxed{
M'_+(t_*)-M'_-(t_*)=48\nu e^{-2}.
}
\]

The active branch index jumps while the selected scalar value remains continuous.
This is a readout/ranking event, not a physical jump in the scalar field.

A vector packet/residual readout tied to the branch can still jump when the selector
changes, because equal scalar badness values do not imply equal packet states.  That
is the separate selector-readout algebra already audited elsewhere.

**Classification: Exact envelope consequence / audited NS calibration.**

## 9. Hysteresis is a separate rule layer

The programme's actual first-bad selector is hysteretic: it can keep the previous
index until a resolve condition is satisfied.  Therefore a raw value crossing need
not trigger an immediate selector switch.

This note supplies the physical competition law **if** enstrophy critical values are
used as a ranking observable.  It does not define the badness threshold, resolve
predicate, or hysteretic switching time.

**Classification: Exact conditional competition law; first-bad hysteresis mapping remains Open-literal.**

## 10. Updated event taxonomy

Critical-branch geometry now has at least three distinct event types:

1. **branch value crossing:** two persistent candidates exchange ranking;
2. **branch degeneracy/birth/death:** Hessian/implicit-function geometry loses a
   unique local branch;
3. **physical packet event:** refinement/reselection/reset changes the packet state.

A selector event can be associated with any of these only after the programme's
badness/resolve logic is defined.  They are not interchangeable physical names.

**Classification: Rigorous structural consequence.**

## 11. Remaining first-bad frontier

The exact NS crossing calibration removes one possible false identification:

> a change of the active worst candidate does not by itself diagnose branch
> degeneracy, positive growth, or continuation failure.

What remains Open-literal is the actual mapping from the programme's physical packet
library and badness/resolve functional to branch ranking, hysteresis, and event
selection.

**Status: first-bad branch-competition/hysteresis identification remains Open-literal.**

No restart/continuation/regularity theorem claimed.
