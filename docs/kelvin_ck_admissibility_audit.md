# Kelvin admissibility dichotomy for the remaining CK operation

This note continues the PDE-first audit after the first-bad selector was typed on
closed Kelvin cycles and after idempotent Hodge-projector motion was classified as
range/complement exchange.  The question is now sharper:

> Can a genuinely non-projector CK operation acting on the selected Kelvin current
> create an irreducible internal boundary or pair-content source?

The answer is rigid for every operation that is genuinely an operation **on Kelvin
currents**.  Idempotency is not needed.  Closedness and exact pressure gauge already
force the relevant dichotomy.

No norm estimate is used.  No continuation/restart or regularity statement is made.

---

## 1. Physical type of a Kelvin operation

Let

\[
B:C_1^{\rm phys}\to C_0^{\rm phys}
\]

be the physical current boundary and let

\[
K:G\to C_1^{\rm phys},
\qquad BK=0,
\]

be the closed Kelvin germ library.  Suppose an additional ambient operation `H`
is inserted before Kelvin evaluation.  Only its restriction

\[
Y:=HK
\]

is physically visible to the selector.

For `H` to remain an **internal Kelvin-current operation**, it must satisfy

\[
\boxed{BHK=0.}
\]

This does not require

\[
H^2=H,
\]

nor does it require the chosen off-cycle extension of `H` to commute with `B` on
all ambient chains.

**Classification: Exact physical typing condition.**

---

## 2. Exact pressure/gauge dichotomy

For every scalar zero-cochain or smooth scalar pressure `p`, Stokes gives

\[
\boxed{
\langle dp,Z\rangle=\langle p,BZ\rangle.
}
\]

Therefore an exact pressure form is invisible on a closed Kelvin current:

\[
BZ=0
\quad\Longrightarrow\quad
\langle dp,Z\rangle=0.
\]

Now let `Z=HKa`.  There are only two structural cases.

### Case A: cycle preserving

If

\[
BHKa=0
\]

for every admissible germ coefficient `a`, exact pressure remains gauge.  The
operation stays inside the physical Kelvin-current type.

### Case B: cycle breaking

If

\[
BHKa\ne0
\]

for some admissible `a`, choose in a finite-chain witness

\[
p=BHKa.
\]

Then

\[
\boxed{
\langle dp,HKa\rangle
=(BHKa)^T(BHKa)>0
}
\]

for a nonzero real incidence boundary.  In smooth current language the same
statement is simply the endpoint/interface term supplied by Stokes.

Thus a cycle-breaking operation cannot be hidden as an "internal Kelvin source".
It has exposed a physical boundary.  It must be classified as a cut/interface,
open-current operation, physical exit, or a change of observable that is no longer
Kelvin circulation on a closed current.

**Classification: Exact identity and rigorous physical consequence.**

This criterion is stronger than asking whether an arbitrary ambient matrix is a
chain map: only the physically admissible cycle range matters, but on that range
closedness is compulsory if pressure is to remain gauge.

---

## 3. Exact 3D Navier--Stokes gauge witness

Use the exact decaying ABC/Beltrami solution

\[
u=e^{-\nu t}U,
\]

\[
U=(\sin z+\cos y,\;\sin x+\cos z,\;\sin y+\cos x),
\]

with exact pressure

\[
p=-\frac12|u|^2.
\]

On the closed `x`-torus cycle, exact pressure circulation is zero.

Now keep the physical line `y=pi/2,z=0` but cut the `x` cycle to the open segment
`0 <= x <= pi`.  Direct symbolic integration gives

\[
\boxed{
\int_0^{2\pi}\partial_xp\,dx=0,
}
\]

while

\[
\boxed{
\int_0^{\pi}\partial_xp\,dx
=2e^{-2\nu t}\ne0.
}
\]

The second quantity is exactly the endpoint pressure difference.  So genuine 3D
Navier--Stokes itself detects the distinction between a closed Kelvin cycle and a
cycle-breaking/open-current operation.

**Classification: Exact 3D Navier--Stokes calibration.**

---

## 4. Non-idempotent cycle-preserving maps are coefficient maps

Assume `H` is linear and its physically realized output lies in a closed-cycle
library `K_out`.  In the simplest same-library case,

\[
HK=KL
\]

for a coefficient map `L` on germ/cycle coordinates.

No projector identity is required.  In particular `H^2 != H` is allowed.

The physical boundary is nevertheless

\[
\boxed{
BHK=BKL=0.
}
\]

The full pair content is

\[
(HK)\otimes(HK)
=(KL)\otimes(KL),
\]

and Kronecker functoriality gives

\[
\boxed{
(KL)^{(2)}=K^{(2)}L^{(2)}.
}
\]

Thus an arbitrary linear cycle-preserving CK operation becomes a coefficient
transformation on physical cycle space.  If the full tensor square is retained,
it creates no missing pair content.

The exact CI witness uses a two-cycle figure-eight current complex and an explicit
non-idempotent ambient `H`.  It verifies

\[
H^2\ne H,
\qquad
BHK=0,
\qquad
\partial_{\rm pair}(HK\otimes HK)=0
\]

and recovers the exact nontrivial coefficient matrix `L`.

**Classification: Exact identity.**

---

## 5. Off-cycle behavior is still extension data

Two ambient operators `H_1,H_2` may agree on the Kelvin library,

\[
H_1K=H_2K,
\]

while

\[
BH_1\ne BH_2
\]

on arbitrary ambient chains.  Their Kelvin observable and intrinsic boundary are
nevertheless identical.

Therefore the earlier cycle-typing lesson survives unchanged for non-projectors:
an off-cycle ambient residual is not physical `Z_irr` unless it survives restriction
to the admissible Kelvin currents.

**Classification: Exact finite-chain consequence.**

---

## 6. Covariant transport of a non-projector operation

Let

\[
Y=HK.
\]

With physical output transport `T_out`, intermediate transport `T_mid`, and germ
transport `A_g`, define

\[
G_Y
=\dot Y+T_{\rm out}Y-YA_g.
\]

The ordinary product rule gives exactly

\[
\boxed{
G_Y
=(\dot H+T_{\rm out}H-HT_{\rm mid})K
+H(\dot K+T_{\rm mid}K-KA_g).
}
\]

The first term is motion of the additional realization; the second is motion of
the physical Kelvin library through that realization.  There is no third internal
term.

If `Y_s` remains in the closed-cycle space for all `s`, then its ordinary tangent
is also closed.  With a connection preserving the physical current complex, the
covariant version is again a cycle-valued connection/deformation term.  A finite
discontinuity is governed by the already-audited reset identity.

**Classification: Exact product identity; physical connection interpretation is a
rigorous consequence when the stated transport preserves the current complex.**

---

## 7. Differentiable nonlinear CK maps obey the same physical constraint

Linearity is not essential to the boundary conclusion.  Let

\[
\Phi:\mathcal U\subset G\to C_1^{\rm phys}
\]

be differentiable and suppose

\[
B\Phi(a)=0
\]

for every admissible `a`.  Differentiating gives

\[
\boxed{
B\,D\Phi_a=0.
}
\]

Hence tangent motion of an honest cycle-valued nonlinear CK map is itself a closed
physical current.

Along a differentiable path `a(s)`, write

\[
Z_s=\Phi(a(s)).
\]

Then the full pair derivative is only the Leibniz derivative

\[
\boxed{
\frac d{ds}(Z_s\otimes Z_s)
=\dot Z_s\otimes Z_s+Z_s\otimes\dot Z_s.
}
\]

Since both `Z_s` and `dot Z_s` are cycles,

\[
\boxed{
\partial_{\rm pair}
\frac d{ds}(Z_s\otimes Z_s)=0.
}
\]

Thus differentiable nonlinear reparameterization of closed Kelvin currents also
does not manufacture an autonomous pair-only internal boundary source.

**Classification: Exact identity.**

Nondifferentiable selector changes are not silently included here; the existing
hysteresis/reset audit treats finite jumps, while moving localization cuts remain
physical interface currents.

---

## 8. Return to the original `Pi_irr` content-defect placeholder

In the initial repository commit, the pair-level placeholder was written

\[
\Pi_{\rm irr}^{(2)}
=(R\otimes R)_*\Pi-\Pi_{\rm allowed}^{(2)}.
\]

That formula is a **content defect relative to an allowed projection**.  The audit
now separates its possibilities.

1. If `R` is a physical linear cycle map and `Pi_allowed^(2)` retains the full
   tensor-square image, then
   \[
   \boxed{\Pi_{\rm irr}^{(2)}=0}
   \]
   exactly.
2. If `Pi_allowed^(2)` drops cross-child, cross-shell, or cross-cycle blocks, the
   difference is omitted physical covariance content.  The exact odd-mode NS
   shear already shows such truncation can turn a true zero bank into a positive
   fake bank.  This is an observer/analysis projection defect.
3. If the operation breaks closedness, the defect is seen by exact pressure gauge
   and belongs to physical boundary/interface/exit.
4. If the operation is differentiable and cycle-valued but nonlinear, its physical
   pair current is simply `Phi(Z) tensor Phi(Z)` and its path derivative is the
   exact two-factor Leibniz law above.  Any smaller "allowed" pair content again
   requires an explicit physical reason rather than being called internal by
   default.

So the original pair-content realization of an irreducible CK defect is exhausted
for the presently specified Kelvin construction: full physical content gives zero;
truncation is an observer projection; cycle breaking is a physical boundary.

**Classification: Rigorous consequence for the original pair-content-defect
realization.**

This does **not** prove a theorem about an independently defined `Z_irr` if that
symbol is intended to mean some future object not yet written in the repository.

---

## 9. What remains genuinely open

The present hierarchy is now:

\[
\boxed{
\begin{array}{ll}
\text{first-bad support selection} & \text{closed by cycle typing},\\
\text{full pair lifting} & \text{no autonomous pair-only residual},\\
\text{linear refinement/shell mixing} & \text{full cross covariance retained},\\
\text{idempotent Hodge projector} & \text{exchange/connection only},\\
\text{arbitrary linear cycle-preserving CK map} & \text{coefficient map on cycles},\\
\text{differentiable nonlinear cycle-preserving CK map} & \text{cycle tangent + pair Leibniz},\\
\text{cycle-breaking map} & \text{physical boundary/gauge-visible},\\
\text{finite discontinuity} & \text{reset revaluation}.
\end{array}
}
\]

None of those mechanisms supplies a genuinely unclassified internal producer.

What remains open is literal rather than algebraically vague: the repository still
contains no line-by-line definition of `S^int`.  If `S^int` is later defined, each
of its terms must first be typed against the dichotomy above.  A term cannot be
called internal merely because it appears in an ambient representation.

**Classification: Rigorous consequence for all operation classes explicitly listed
above; Conjectural bridge only for identification with the still-undefined
programme-specific `S^int`.**

No continuation/restart conclusion follows here.
