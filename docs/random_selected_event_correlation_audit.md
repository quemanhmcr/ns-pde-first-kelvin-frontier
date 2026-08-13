# Random/adaptive selected-event map correlation audit

All previous finite-event laws were pathwise.  That is the correct first layer:
for each realized packet event and selector readout, the physical selected map is

\[
C=E_+A.
\]

A first-bad mechanism, however, is expected to be **adaptive**: the realized event
map/readout can depend on the same physical state being observed.  Therefore the
expectation-level law must retain the joint event-map/state distribution rather than
replace `C` by its mean.

This note derives the exact two-replica algebra before any estimate.

## 1. Mean selected output already has an event--state correlation face

For two equal-weight replicas `(C_1,x_1)` and `(C_2,x_2)`, define

\[
\bar C=\frac{C_1+C_2}{2},
\qquad
\Delta C=C_1-C_2,
\]

and

\[
\bar x=\frac{x_1+x_2}{2},
\qquad
\Delta x=x_1-x_2.
\]

Then

\[
\boxed{
\frac12(C_1x_1+C_2x_2)
=\bar C\,\bar x
+\frac14\Delta C\,\Delta x.
}
\]

Thus even the **mean** selected post-event residual is not generally
`mean event map x mean state` when the event map is replica/state dependent.

The extra face is zero if either the event map or the state is identical across the
two replicas.

**Classification: Exact two-replica identity.**

## 2. Exact second-order four-face law

Let `Q_1,Q_2` be symmetric second-order payloads on the event-map input space.  They
may be state second moments, pathwise dyads, or same-replica q.v. Grams.  Define

\[
\bar Q=\frac{Q_1+Q_2}{2},
\qquad
\Delta Q=Q_1-Q_2.
\]

Then

\[
\boxed{
\begin{aligned}
\frac12(&C_1Q_1C_1^T+C_2Q_2C_2^T)
={}&\bar C\bar Q\bar C^T\\
&+\frac14\Delta C\bar Q\Delta C^T\\
&+\frac14\bar C\Delta Q\Delta C^T\\
&+\frac14\Delta C\Delta Q\bar C^T.
\end{aligned}
}
\]

The four physical/statistical faces are:

1. **mean-map / mean-payload face**: `Cbar Qbar Cbar^T`;
2. **event-map dispersion face**: `(1/4) DeltaC Qbar DeltaC^T`;
3. **left event--state correlation face**;
4. **right event--state correlation face**.

No covariance estimate has been used; this is the exact finite-replica product law.

**Classification: Exact identity.**

## 3. Event-map dispersion is PSD, correlation faces are signed

If `Qbar` is positive semidefinite, then for every output probe `z`,

\[
z^T\left(\frac14\Delta C\bar Q\Delta C^T\right)z
=\frac14(\Delta C^Tz)^T\bar Q(\Delta C^Tz)\ge0.
\]

So event-map dispersion is a genuine nonnegative face.

The two event--state correlation faces are not sign-definite.  They record whether
large/small payload directions are aligned or anti-aligned with the realized event
map.

**Classification: Rigorous consequence of the exact four-face identity.**

## 4. Fixed event map is a special closure domain

If `C_1=C_2`, then `DeltaC=0`, and all three event-randomness correction faces vanish:

\[
\frac12(CQ_1C^T+CQ_2C^T)
=C\bar Q C^T.
\]

Thus the earlier deterministic/specified event laws remain exact.  The new faces
appear only because the event map/readout itself varies across replicas.

**Classification: Exact theorem-domain statement.**

## 5. Same payload but random event map leaves pure dispersion

If `Q_1=Q_2=Q`, then `DeltaQ=0`, and

\[
\frac12(C_1QC_1^T+C_2QC_2^T)
=\bar C Q\bar C^T
+\frac14\Delta C Q\Delta C^T.
\]

Therefore mean-map factorization already fails from event-map dispersion alone; no
state/event correlation is needed for that failure.

**Classification: Exact identity / rigorous no-mean-map consequence.**

## 6. PSD aligned and anti-aligned calibrations

Take the two scalar output maps

\[
C_1=(1,0),
\qquad
C_2=(0,1).
\]

### Aligned replicas

Let

\[
Q_1=\operatorname{diag}(4,0),
\qquad
Q_2=\operatorname{diag}(0,4).
\]

All payloads are PSD.  The exact four faces are

\[
\boxed{1+1+1+1=4.}
\]

The naive mean-map / mean-payload face is only `1`; three full units come from event
dispersion and event--state correlation.

### Anti-aligned replicas

Swap the payloads:

\[
Q_1=\operatorname{diag}(0,4),
\qquad
Q_2=\operatorname{diag}(4,0).
\]

Again all payloads are PSD, but now

\[
\boxed{1+1-1-1=0.}
\]

The signed event--state faces cancel both the naive mean contribution and the
positive event-dispersion face exactly.

Hence adaptive event correlation is neither a positive cost nor a negligible
correction.

**Classification: Audited algebraic calibration / rigorous sign necessity.**

## 7. The same law applies to continuous q.v. Gram payloads

The four-face identity is a congruence identity.  It does not care whether `Q_i` is a
state second moment or a continuous same-replica q.v. Gram.  Therefore an adaptive
first-bad event also requires joint event-map/noise-source bookkeeping:

\[
\mathbb E[C\Gamma_{\rm lib}C^T]
\neq
\mathbb E[C]\,\mathbb E[\Gamma_{\rm lib}]\,\mathbb E[C]^T
\]

generically.

**Classification: Exact identity under the same two-replica typing.**

## 8. Consequence for the first-bad programme

The pathwise event normal form remains simple: each realized event is described by
the physical map `C=E_+A`.  At expectation/covariance level, however, an adaptive
event rule must carry the **joint law of `C` and the persistent library payload**.

Therefore the following replacement is not an identity:

\[
\mathbb E[CQC^T]
\rightsquigarrow
\bar C\,\bar Q\,\bar C^T.
\]

This is especially relevant to a first-bad rule because the selector/event map is
intended to depend on the state.  But the actual badness functional and therefore
the actual joint law are still not defined.

**Classification: Rigorous structural consequence; programme-specific adaptive law remains Open-literal.**

## 9. Remaining Open-literal seam

What remains is not the algebra of a random event once its replicas are supplied.
It is the actual Navier--Stokes mechanism that generates:

- the candidate library;
- the badness/resolve rule;
- the adaptive selector/event map `C`;
- the event/state joint law;
- the outer first-bad clock and its relation to the reverse-age/future-bank clocks.

**Status: Open-literal at actual first-bad adaptive event/joint-law instantiation.**

No restart/continuation/regularity theorem claimed.
