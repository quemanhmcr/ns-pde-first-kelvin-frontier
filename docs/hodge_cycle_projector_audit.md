# Hodge/cycle projector audit after cycle-typing

This note audits one precise possibility for the still-undefined additional
CK/Hodge operator: that it is an idempotent projector whose range consists of
closed physical currents.  It does **not** assert that the programme's `S^int` is
this projector motion, nor that any not-yet-written CK operator satisfies these
hypotheses.

No continuation/restart or 3D Navier--Stokes regularity claim is made.

---

## 1. Exact weighted cycle projector

Let

\[
K:G\to C_1^{\rm phys},
\qquad B_xK=0,
\]

have linearly independent cycle columns, and let `W` be a nondegenerate positive
current metric.  Define

\[
\boxed{
H_W
=K(K^T W K)^{-1}K^T W.
}
\]

Then

\[
\boxed{H_W^2=H_W,}
\qquad
\boxed{B_xH_W=0,}
\qquad
\boxed{H_WK=K,}
\]

and

\[
\boxed{H_W^T W=W H_W.}
\]

Thus this literal Hodge/cycle projector sends every ambient current into the
closed-cycle subspace.  Its physical-current boundary is zero by construction;
there is no physical exit or localization boundary hidden inside the projector.

**Classification: Exact identity under the stated projector hypotheses.**

The metric `W` may change which complementary sector is used, but not the fact
that the range lies in `ker B_x`.

---

## 2. Differentiated idempotency forbids internal projector production

Let `P_s` be any differentiable projector,

\[
P_s^2=P_s,
\]

and let `G=D_sP` be its covariant derivative as an endomorphism.  Because the
covariant derivative is a derivation,

\[
D_s(P^2)=G P+P G.
\]

Differentiating `P^2=P` therefore gives

\[
\boxed{G P+P G=G.}
\]

Multiplying by `P` on both sides yields

\[
\boxed{P G P=0.}
\]

With `Q=I-P`, the same identity gives

\[
\boxed{Q G Q=0.}
\]

Hence

\[
\boxed{
G=P G Q+Q G P.
}
\]

The motion of an exact projector is purely off-diagonal exchange between its
selected range and its complement.  There is no active-to-active or
inactive-to-inactive derivative term that could be interpreted as a new internal
source.

**Classification: Exact identity.**

Physical type: `P G Q` and `Q G P` are connection/selection transfer.  They are
signed exchange terms.  Idempotency supplies no positive production law.

---

## 3. Co-moving connection removes pure frame motion exactly

Write the covariant derivative of an endomorphism as

\[
G=\dot P+[T,P].
\]

For every tangent projector motion satisfying the differentiated idempotency
identity, set

\[
A=[\dot P,P].
\]

Then

\[
[[\dot P,P],P]=\dot P,
\]

so choosing the co-moving connection `T=-A` gives

\[
\boxed{G=0.}
\]

Thus pure motion of the projector frame is connection geometry.  A fixed-frame
representation may display a nonzero commutator, but that is not a new Kelvin
producer.

**Classification: Exact identity.**

This is the finite-dimensional projector counterpart of the already-audited
Cartan/variable-frame geometry.

---

## 4. Full pair lift has no active-active internal projector source

For the tensor-square pair projector

\[
P^{(2)}=P\otimes P,
\]

its covariant derivative is

\[
\boxed{
D_sP^{(2)}=G\otimes P+P\otimes G.
}
\]

There is no additional pair-only term.  Moreover, using `P G P=0`,

\[
\boxed{
(P\otimes P)\,D_sP^{(2)}\,(P\otimes P)=0.
}
\]

So even before choosing a co-moving connection, an exact projector cannot create
an internal active-pair source inside its own selected pair range.  Pair motion is
the one-replica-at-a-time lift of the same range/complement exchange.

**Classification: Exact identity.**

This is stronger than merely saying that full pair lifting is functorial: the
idempotency tangent law itself forbids an active-active projector-production
sector.

---

## 5. Time-dependent weighted Hodge metric does not change the conclusion

The symbolic audit also lets the weight `W_s` vary while the physical cycle range
is fixed.  The weighted projector `H_{W_s}` changes because its complement changes,
but it still satisfies

\[
H_{W_s}^2=H_{W_s},
\qquad
B_xH_{W_s}=0.
\]

Its derivative obeys

\[
H\dot H H=0,
\qquad
(I-H)\dot H(I-H)=0.
\]

Thus metric/Hodge-frame motion produces only exchange/connection geometry.  It
does not create a new internal resource.

**Classification: Exact identity in the finite-chain weighted projector model.**

---

## 6. Consequence for the CK/Pillar-II frontier

There are now three logically distinct levels:

1. **First-bad support selector** `M_fb` on closed Kelvin germs: intrinsic residual
   already closed by the cycle-typed audit.
2. **Cycle realization** `K`: its range is closed, and anchor/frame motion is
   physical push-forward/connection geometry.
3. **Any additional CK/Hodge operator**: still absent from the repository as a
   literal definition.

If level 3, when written, is an idempotent projector `H` with

\[
\operatorname{Ran}H\subseteq\ker B_x,
\]

then its two candidate obstruction channels close structurally:

\[
\boxed{B_xH=0}
\]

and

\[
\boxed{H(DH)H=(I-H)(DH)(I-H)=0.}
\]

The remaining `DH` terms are exactly range/complement exchange and may be killed by
a co-moving connection when they are pure frame motion.

**Classification: Rigorous consequence conditional on the literal CK/Hodge map
being such a projector.**

This does **not** prove the global statement

\[
S^{\rm int}=0\iff Z_{\rm irr}=0.
\]

The repository still has no line-by-line definition of `S^int`, and it has no
literal extra CK/Hodge map to identify with `H`.  A non-idempotent operator, an
operator whose range is not closed, or an operator carrying additional physical
restriction/exit content must be audited on its own terms.

**Classification: Conjectural bridge for the identification with the programme's
still-undefined CK/Pillar-II objects.**

---

## 7. What this rules out

Under the projector hypotheses it is no longer legitimate to posit a positive
`internal projector production` simply from motion of the active subspace.
Differentiated idempotency says the motion is off-diagonal transfer.  At pair level
there is likewise no active-active internal production term.

This does not make the transfer vanish.  It classifies it: connection/selection
exchange, to be paired with the physical covariance cochain with its sign intact.
No estimate may turn that signed exchange into a fictitious positive reservoir.

**Classification: Rigorous consequence.**

The next unresolved structural question is therefore not projector kinematics but
whether the programme contains any **non-projector CK operation** or an independent
`S^int` definition whose physical current content is not already among
quantile/shell interfaces, connection exchange, reset, refinement, or physical
exit.
