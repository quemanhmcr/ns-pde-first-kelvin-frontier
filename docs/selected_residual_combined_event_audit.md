# Selected residual under a simultaneous physical packet event and selector switch

This note keeps two operations physically distinct:

1. a **physical linear packet-library event** `A` acting on the persistent residual library;
2. a **hysteretic selector readout change** from `E_-` to `E_+`.

The point is not to estimate either operation.  The point is to let the literal
current/readout algebra say what the finite event actually is before any norm is
introduced.

## 1. Post-event readout is `E_+ A`

Let the pre-event persistent library state be `X_-`.  A specified linear physical
packet event gives

\[
X_+=A X_-.
\]

The post-event active residual is therefore

\[
\boxed{Y_+=E_+A X_-.}
\]

The pre-event active residual is

\[
Y_-=E_-X_-.
\]

Thus the finite selected jump is

\[
\boxed{\Delta Y=D X_-,\qquad D=E_+A-E_-.}
\]

This is the literal combined event.  It is not the sum of an independently computed
"physical cost" and an independently computed "selector cost".

**Classification: Exact identity.**

## 2. Discrete product rule and the physical--selector interaction face

On a common library space write

\[
A=I+\Delta A,
\qquad
E_+=E_-+\Delta E.
\]

Then

\[
\boxed{
D
=E_-\Delta A+\Delta E+\Delta E\,\Delta A.
}
\]

The three operator faces have distinct physical meanings:

- `E_- DeltaA`: physical packet change visible through the **old** selected readout;
- `DeltaE`: selector revaluation of the **old** library;
- `DeltaE DeltaA`: the genuine **physical--selector interaction**: the new observer
  sees a part of the physical update that cannot be represented by adding the two
  old-reference faces separately.

There are also two exact sequential forms,

\[
\boxed{
D=E_-\Delta A+\Delta E\,A
}
\]

(physical event first, then selector re-read of the post-event library), and

\[
\boxed{
D=\Delta E+E_+\Delta A
}
\]

(selector change first as a bookkeeping decomposition, then physical change read by
the new observer).

The mixed face is not an extra stochastic producer.  It is the finite product-rule
interaction between two simultaneous typed operations.

**Classification: Exact identity.**

## 3. Pure limits

If `A=I`, then `DeltaA=0` and the event reduces to the already audited pure selector
jump

\[
D=\Delta E.
\]

If `E_+=E_-`, then `DeltaE=0` and the event reduces to the physical packet change seen
through a fixed readout,

\[
D=E_-\Delta A.
\]

Thus the interaction face vanishes exactly whenever either operation is absent.

**Classification: Exact identity.**

## 4. Full second-moment jump keeps the pair state

Let `Q` be the full pre-event library second moment.  Define

\[
C=E_+A,
\qquad
D=C-E_-.
\]

Then

\[
Q_{\rm sel,+}=CQC^T,
\qquad
Q_{\rm sel,-}=E_-QE_-^T.
\]

The exact finite jump is

\[
\boxed{
Q_{\rm sel,+}-Q_{\rm sel,-}
=DQE_-^T+E_-QD^T+DQD^T.
}
\]

These are the same left/right/quadratic pair faces already forced by selector-reset
and physical-event covariance algebra.  The only change is that the literal jump
operator is now the combined `D=E_+A-E_-`.

No diagonal-only or selected-endpoint closure is introduced.

**Classification: Exact identity.**

## 5. Jump optional q.v. is only the quadratic face

Pathwise, when `Q=X_-X_-^T`,

\[
DQD^T=(\Delta Y)(\Delta Y)^T.
\]

Thus the càdlàg optional quadratic variation at the combined finite event contains
the jump square, but that jump square is only the quadratic face of the full dyad or
second-moment revaluation.  The signed left/right faces remain physically distinct.

Therefore a simultaneous event does not turn optional jump q.v. into a covariance
bank.

**Classification: Exact semimartingale typing consequence.**

## 6. Exact one-mode Navier--Stokes referee: the mixed face is mandatory

Use the exact one-mode Navier--Stokes shear already audited in the selected-lineage
layer.  Two half-period packets have codeforming residuals

\[
\chi_0
=\frac{4k^2e^{-\nu k^2t}}{\pi^2},
\qquad
\chi_1=-\chi_0.
\]

Take the exact NS residual payload

\[
X_-=(\chi_0 e_z,\chi_1 e_z)
\]

and apply a specified orientation-preserving linear current synthesis that leaves
germ `0` unchanged and sends

\[
g_1\mapsto g_1+g_0.
\]

Then switch the active readout `0 -> 1` at the same finite event.

The physical update is hidden from the old selector:

\[
(E_-\Delta A)X_-=0.
\]

The selector-old-library face is

\[
(\Delta E)X_-
=-\frac{8k^2e^{-\nu k^2t}}{\pi^2}e_z.
\]

But the interaction face is

\[
(\Delta E\,\Delta A)X_-
=+\frac{4k^2e^{-\nu k^2t}}{\pi^2}e_z.
\]

Hence the actual selected jump is

\[
\boxed{
\Delta Y
=-\frac{4k^2e^{-\nu k^2t}}{\pi^2}e_z,
}
\]

and the post-event selected residual is exactly zero because the synthesized hidden
germ is `chi_1+chi_0=0`.

So the naive additive rule

\[
\text{physical-old face}+\text{selector-old face}
\]

is wrong even on an exact Navier--Stokes payload under a specified literal linear
current event.  The missing amount is exactly the physical--selector interaction
face.

**Classification: Audited calibration / rigorous no-naive-additivity consequence.**

## 7. What this closes

For any **specified** same-space linear packet event and specified selector switch,
the one-current selected jump, the finite product rule, the physical--selector
interaction, the full second-moment pair jump, and the jump-square typing are now
exact.

Together with the previous layers, a supplied same-clock path has the following
literal architecture:

- persistent same-replica library: common Brownian Gram dynamics;
- frozen selector interval: active block of that Brownian martingale;
- finite physical packet event: full-library linear event map;
- finite selector change: active observer readout change;
- simultaneous physical + selector event: `D=E_+A-E_-` with the mandatory mixed
  product-rule face.

**Classification: Rigorous conditional composition of exact identities.**

## 8. What remains Open-literal

This layer does **not** define the first-bad badness functional, resolve predicate,
event time, or actual Navier--Stokes-generated packet map.  It also does not identify
the same-replica reverse-age clock with the programme's future-bank/ancestry clock.

The remaining first-bad event problem is now more literal:

> Which persistent physical candidate library does Navier--Stokes select, when does
> the hysteretic badness/resolve logic switch the active readout, and which actual
> physical packet map `A` occurs at the same event?

The algebra after those data are supplied is no longer open.

**Status: Open-literal only at actual first-bad timing/event-map/state instantiation.**

No restart/continuation/regularity theorem claimed.
