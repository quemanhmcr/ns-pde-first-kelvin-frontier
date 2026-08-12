# Cycle-typed first-bad selector audit

This note records a type correction in the active first-bad-germ world-sheet.  It is
uncertified research and makes no continuation/restart or 3D Navier--Stokes
regularity claim.

The selected Kelvin observable in this repository is defined on **closed physical
currents**.  Therefore the first-bad selector is not intrinsically an endomorphism
of the full ambient physical chain complex.  It acts on the coefficient/germ space
of a library of closed Kelvin cycles and is then realized in physical current
space.  Once the map is typed this way, a large class of apparent active
commutators disappears as an off-cycle extension artefact, while the genuine
support-crossing and switching terms remain visible as localization current or
finite reset revaluation.

---

## 1. Two different boundaries must not be conflated

Let

\[
B_x:C_1^{\rm phys}\to C_0^{\rm phys}
\]

be the physical spatial current boundary.  Let the candidate Kelvin germs be
represented by the columns of

\[
K_s:G\to C_1^{\rm phys}.
\]

The standing Kelvin observable requires these candidates to be closed:

\[
\boxed{B_xK_s=0.}
\]

The first-bad logic lives instead in the germ/selector state space `G`.  Its
world-sheet has its own parameter/time boundary, switching faces, quantile faces,
shell faces, and reset endpoints.  Those are **not** the same operator as `B_x`.

This distinction is physical: a closed Kelvin loop can migrate in anchor, move
through a quantile chamber, change shell label, refine, and reset while remaining a
closed spatial current throughout.

**Classification: Exact type distinction.**

---

## 2. Literal first-bad support map

For a fixed ordered list of germ candidates, let

\[
M_{\rm fb}(s):G\to G
\]

be the state-dependent rank-one support projector selecting the first bad germ.
If no germ is bad, it is the zero projector.  On a hysteresis interval the selected
index is frozen until the resolve event; only at resolve is first-bad priority
recomputed.

The active physical current map is therefore

\[
\boxed{P_{\rm fb}(s)=K_sM_{\rm fb}(s).}
\]

This is the intrinsic active selector present in the selected-Kelvin observable.
The threshold functions deciding which germ is bad determine `M_fb`; the current
realization is carried by `K_s`.

**Classification: Exact definition of the cycle-typed selector.**

---

## 3. Physical boundary commutator closes immediately on the correct domain

Because `B_x K_s=0`,

\[
\boxed{
B_xP_{\rm fb}
=B_xK_sM_{\rm fb}
=0.
}
\]

There is no need to invent a degree-zero map on arbitrary ambient chains.  The
germ coefficient space has zero **physical** boundary, so the chain map is simply

\[
G\xrightarrow{K_sM_{\rm fb}} Z_1^{\rm phys}
\longrightarrow 0.
\]

The full ordered pair lift also has zero physical boundary exactly:

\[
\boxed{
\partial_{x,\rm pair}
(P_{\rm fb}\otimes P_{\rm fb})=0,
}
\]

where

\[
\partial_{x,\rm pair}
=
\begin{bmatrix}
B_x\otimes I\\
-I\otimes B_x
\end{bmatrix}.
\]

Thus the first-bad support choice cannot create a physical-current boundary if its
candidate Kelvin currents were already closed.

**Classification: Exact identity.**

A useful stronger form is

\[
\boxed{
B_x(KM)=(B_xK)M.
}
\]

Hence if a realization has a nonzero boundary because a physical restriction or
exit has genuinely opened it, the selector merely transports that already existing
boundary.  It does not manufacture a new boundary sector.

**Classification: Rigorous consequence.**

---

## 4. Why an ambient `B P_1-P_0 B` can be a false obstruction

Suppose one extends the active selector away from the physical cycle library to all
ambient one-chains.  Such an extension is not unique.  Its degree-zero part is even
less constrained because the selected cycles have zero boundary.

The symbolic audit constructs two ambient extensions which agree on the actual
physical cycle but have different global commutators:

\[
C^{(a)}=B_xF_1-F_0^{(a)}B_x=0,
\]

while

\[
C^{(b)}=B_xF_1-F_0^{(b)}B_x\ne0.
\]

Nevertheless, on the physical cycle library `K`,

\[
\boxed{C^{(b)}K=0,}
\]

and on the full physical pair library,

\[
\boxed{C^{(b,2)}(K\otimes K)=0.}
\]

So a nonzero **ambient** active commutator is not an intrinsic physical residual
unless it survives restriction to the actually admissible Kelvin cycles.

This revises the interpretation of the earlier generic interval counterexample:
that example correctly showed that arbitrary cell projections need not be chain
maps, but it does not establish a Kelvin obstruction because the Kelvin selector is
not defined on arbitrary interval chains.

**Classification: Exact finite-chain counterexample to off-cycle overinterpretation.**

---

## 5. Support cuts are exact interface currents

When a physical or germ-space localization is genuinely represented by a support
mask, its commutator has a rigid entrywise form.

For an incidence matrix `B` and diagonal activity masks `chi_e`, `chi_v`,

\[
\boxed{
(BM_1-M_0B)_{ve}
=B_{ve}(\chi_e-\chi_v).
}
\]

Only incidences crossing the active/inactive cut survive.  This is a literal
boundary/interface current.

Likewise, if `A` transports germ coefficients and `M=diag(chi_i)`,

\[
\boxed{
(AM-MA)_{ij}
=A_{ij}(\chi_j-\chi_i).
}
\]

Only germ transitions crossing the selected support survive.  Thus a nonzero
selector transport commutator is a localization crossing current, not an
unclassified producer.

**Classification: Exact identities.**

These formulas are the finite-chain/current analogues of distributional
`d 1_D` interface terms.  Quantile and shell motion belong here.  Physical exit is
the corresponding genuine absorbing boundary rather than an observer cut.

---

## 6. Exact transport factorization `P_fb = K M_fb`

Let `T_x` be physical covariant transport and `A_g` the germ-frame connection.
Define

\[
G_K
=\dot K+T_xK-KA_g,
\]

and

\[
G_M
=\dot M+A_gM-MA_g.
\]

Then for `P_fb=KM`,

\[
\boxed{
G_{P_{\rm fb}}
=\dot P_{\rm fb}+T_xP_{\rm fb}-P_{\rm fb}A_g
=G_KM+KG_M.
}
\]

No third term exists.

Physical classification is therefore forced:

- `G_K M`: anchor/orientation push-forward, frame/Hodge connection, refinement,
  or any genuine physical change in the realized cycle library;
- `K G_M`: first-bad support transport, hence quantile/shell/localization crossing
  when nonzero;
- finite discontinuities of `M`: resolve/reset, treated by the exact finite jump
  law below rather than by inventing a positive jump density.

**Classification: Exact identity.**

If `K` is covariantly transported and the selector support is frozen in the same
co-moving germ frame, both terms vanish on that interval.  In a fixed frame the
nonzero `G_K` is connection geometry already identified by the Cartan audit.

**Classification: Rigorous consequence.**

---

## 7. Hysteresis switching is finite covariance revaluation

At a resolve/reset time let

\[
P^+=P^-+\Delta P.
\]

The full pair jump is exactly

\[
\boxed{
P^+\otimes P^+-P^-\otimes P^-
=\Delta P\otimes P^-
+P^-\otimes\Delta P
+\Delta P\otimes\Delta P.
}
\]

Pairing this identity with the future covariance cochain gives

\[
\boxed{
V(Z^+)-V(Z^-)
=2C(Z^-,\Delta Z)+V(\Delta Z).
}
\]

The quadratic increment term cannot be read alone: the signed mixed covariance is
part of the exact reset law.

**Classification: Exact identity.**

---

## 8. Exact Navier--Stokes pressure tests

### 8.1 Odd-mode shear: selector reset is not positive payment

For the exact odd-mode periodic Navier--Stokes shear,

\[
X_\pi=-X_0
\]

pathwise.  A first-bad reset from the anchor-`0` Kelvin cycle to the anchor-`pi`
cycle therefore has

\[
V_\pi-V_0=0,
\]

while

\[
V(X_\pi-X_0)=4V_0>0.
\]

The exact mixed term is

\[
2\operatorname{Cov}(X_0,X_\pi-X_0)=-4V_0,
\]

so the reset identity closes exactly.  CI checks this with the closed-form NS
calibration.

**Classification: Rigorous consequence from an exact Navier--Stokes solution.**

### 8.2 Genuine 3D ABC/Beltrami flow: pressure remains gauge on a closed cycle

For

\[
u(t)=e^{-\nu t}U,
\qquad
U=(\sin z+\cos y,\sin x+\cos z,\sin y+\cos x),
\]

with exact pressure

\[
p=-\frac12|u|^2,
\]

the `x`-torus cycle at `y=0,z=pi/2` has nonzero circulation

\[
\boxed{\oint u\cdot dx=4\pi e^{-\nu t},}
\]

but

\[
\boxed{\oint dp=0.}
\]

Thus the cycle-typed domain is not a trivial zero-observable sector: the physical
Kelvin circulation is nonzero while exact pressure remains pure gauge on the
closed current, exactly as required by Navier--Stokes.

**Classification: Exact 3D Navier--Stokes calibration.**

---

## 9. What remains of the active CK question

The notation `P_active` had previously bundled two logically different operations:

1. first-bad support selection among closed Kelvin germs;
2. a possible additional CK/Hodge realization operator on ambient physical chains.

The first operation is now literal and audited:

\[
\boxed{
C_{\rm irr}^{\rm selector}=0.
}
\]

Its transport remainder is exhausted by support-interface transport, connection
geometry, and finite reset jumps:

\[
\boxed{
G_{\rm irr}^{\rm selector}=0
}
\]

once those named terms are kept rather than discarded.

**Classification: Rigorous consequence of the exact typed selector algebra.**

If the programme intends an **additional** ambient CK/Hodge operator `H_CK`, write

\[
P_{\rm full}=H_{\rm CK}K M_{\rm fb}.
\]

Then its physical boundary defect factorizes through the additional operator:

\[
B_xH_{\rm CK}K M_{\rm fb}
=
(B_xH_{\rm CK}-H_{0,\rm CK}B_x)K M_{\rm fb},
\]

because `B_xK=0`.  Thus any remaining irreducible boundary term belongs to
`H_CK`, not to first-bad selection or to pair lifting.

The current repository still contains no independent literal definition of such an
extra `H_CK` operator and no line-by-line definition of `S^int`.  However, the later
Kelvin-admissibility audit classifies the entire generic operation class: if
`H_CK K` remains cycle-valued, idempotency is unnecessary and its intrinsic
physical boundary is zero; if it breaks closedness, exact pressure gauge exposes a
physical interface/open-current/exit.  Stochastic cycle-valued motion likewise has
only its explicit martingale carré-du-champ source.  Consequently the global
Pillar-II equivalence involving `S^int / Z_irr` is **not** declared proved solely
because those symbols have no independent literal definition.

**Classification: Rigorous consequence for the admissible CK operation classes;
Conjectural bridge only for the still-undefined global `S^int / Z_irr` objects.**

---

## 10. Selected-Kelvin pair bank after the type correction

For the **cycle-typed first-bad selector actually used by the selected Kelvin
observable**, there is no intrinsic active-selector irreducible pair term.  The
pair-localization current identity therefore has the form

\[
\boxed{
\Pi^{\rm sel}-\Pi^{\rm dist}
=
\partial_{\rm pair}\mathscr W_{\rm loc}^{(2)}
+\Pi_{\rm quant}^{(2)}
+\Pi_{\rm shell}^{(2)}
+\Pi_{\rm exit}^{(2)}
+\Pi_{\rm conn}^{(2)}
+\Pi_{\rm reset}^{(2)},
}
\]

with full cross-shell and cross-child content retained inside the physical maps.
There is no diagonal refinement payment and no autonomous pair-only residual.

Pairing with the future Kelvin covariance cochain gives

\[
\boxed{
\begin{aligned}
V(\lambda_*)-R_{\rm dist}
={}&
\langle d_{\rm pair}\mathbb K,
        \mathscr W_{\rm loc}^{(2)}\rangle\\
&+\langle\mathbb K,
  \Pi_{\rm quant}^{(2)}
 +\Pi_{\rm shell}^{(2)}
 +\Pi_{\rm exit}^{(2)}\rangle\\
&+\mathcal H_{\rm conn}
 +\mathcal R_{\rm reset}.
\end{aligned}
}
\]

**Classification: Exact current/covariance identity for the cycle-typed selector
sector, subject to the already stated generator compatibility of the Kelvin future
variance and to retaining the named physical interface/connection/exit terms.**

This statement does not identify or eliminate a separate future operator that has
not been defined.  In particular it does not assert the repository-wide statement
`S^int=0 iff Z_irr=0`, and it gives no continuation/restart conclusion.

---

## 11. Exact selected-Kelvin bank along the cycle coefficient path

The cycle typing also exposes the selected bank without hiding selector motion in
an abstract residual.  Let the selected closed current be

\[
Z_s=K_s a_s
\]

and let the future covariance matrix on the germ library be `C_s`, so

\[
V_s(a)=a^T C_s a.
\]

On a frozen physical library, the fixed-current Kelvin identity is the matrix law

\[
\dot C_s=-\Gamma_{K,s},
\]

where `Gamma_K` is the polarized instantaneous Kelvin action.  For a continuous
selector coefficient path,

\[
\boxed{
\frac d{ds}V_s(a_s)
=-\Gamma_{K,s}(a_s,a_s)
+2C_s(a_s,\dot a_s).
}
\]

Equivalently,

\[
\boxed{
\Gamma_{K,s}(a_s,a_s)\,ds
=-dV_s(a_s)+2C_s(a_s,da_s).
}
\]

The second term is the exact signed covariance work of selector motion.  It is not
stochastic quadratic variation generated by the observer.

At a hysteresis jump `a^+=a^-+Delta a`,

\[
\boxed{
V_s(a^+)-V_s(a^-)
=2C_s(a^-,\Delta a)+C_s(\Delta a,\Delta a).
}
\]

Thus for a bounded-variation selector path over a completed finite excursion, the
selected Kelvin payment is exactly initial future covariance minus final future
covariance plus continuous covariance work and the finite reset terms, together
with the already classified physical change of the cycle library `K_s`
(anchor/connection, quantile/shell transport, refinement, and exit).

**Classification: Exact identity.**

The identity is a bank *decomposition*, not yet a uniform continuation estimate.  A
later tensor audit makes the old “generator compatibility” caveat literal: if `R`
lifts a proposed reduced germ/current-frame observable to the full stochastic Kelvin
state, an autonomous reduced generator requires the exact intertwining
`L R = R L_bar`.  A non-lumpable hidden-shape counterexample shows that this can
fail even when two states have the same reduced spatial label.  Thus any failure of
descent is hidden-state physical flux, not an intrinsic selector residual.
Repeated selector work is signed and cannot be replaced by the sum of positive
quadratic increments; the odd-shear reset calibration shows why.  Finiteness or
cancellation of the total physical localization work over an arbitrary approach to
a singular time remains a separate restart/continuation question.  The later
vorticity/Kelvin and orientation-packet audits sharpen that question: the restart
extension selects a whole three-loop block `M_fb tensor I_3`, retains the full
`3 x 3` cross-orientation covariance, and normalizes by the packet metric
`(H^T H)^(-1)`.  Passive orientation/scale/shear changes then cancel exactly.  What
remains is material metric-stretching work and the metric-amplified departure of
future covariance from an area-squared local tensor law; raw rank-one loop variance
is not sufficient by itself.

**Classification: Rigorous consequence; no continuation claim.**

---

## 12. Frontier after this audit

The active-selector question is no longer

> does an arbitrary ambient projection commute with boundary?

That question is extension-dependent and not intrinsic to the Kelvin observable.
The remaining literal question is narrower:

> Is there any additional programme-specific CK/Hodge operator beyond the
> cycle-valued germ realization `K`, and if so, what is its exact current-level
> definition and transport law?

If no such extra operator is part of the construction, the first-bad selector
itself contributes no irreducible residual.  If such an operator exists, its
commutator must be inserted explicitly and audited against exact NS calibrations;
it cannot be inferred from a generic ambient projection or hidden by an estimate.
