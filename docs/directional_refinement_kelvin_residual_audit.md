# Directional and refinement balance for the physical Kelvin residual

## Scope

The previous audits identified the literal physical finite-to-local residual as

\[
r=L\chi,
\qquad
M=L^TL,
\qquad
\mathcal E=\mathbb E[\chi^TM\chi].
\]

This note does not replace that object by a norm.  It follows its exact physical
faces further:

1. the **principal material-line directions** carried by `M`;
2. the **finite physical refinement/reselection event** carried by the repo's
   literal right action `L_+=L_-R`;
3. the **residual/current second moment** carried by the full current/pair state;
4. the **random-frame metric--residual correlation** already forced by the full
   stochastic state;
5. the distinction between a **passive GL coordinate change** and a real physical
   refinement;
6. the smooth material balance between scale, anisotropy/metric work, and
   martingale residual content.

Nothing below defines the post-refinement residual second moment `Q_+`.  In a
physical current refinement, `Q_+` must still be produced by the literal full
current/pair map, with all cross-child and mixed covariance content retained.
Likewise, this note does not identify a same-clock residual with a future bank,
`S^int`, ancestry resolution covariance, restart capacity, or a regularity
criterion.

---

## 1. Principal material-line directions give an exact local ledger

Let the physical line metric have the spectral representation

\[
\boxed{
M=V\,\mathrm{diag}(\sigma_1^2,\sigma_2^2,\sigma_3^2)V^T,
}
\]

where the columns `v_i` of `V` are orthonormal principal material-line
directions.  Let

\[
Q=\mathbb E(\chi\chi^T)
\]

for a fixed/conditioned frame.  Cyclicity of trace gives

\[
\boxed{
\operatorname{tr}(MQ)
=
\sum_{i=1}^3
\sigma_i^2\,v_i^TQv_i.
}
\]

This is not an estimate by the largest singular value.  Each physical line
direction has its own exact residual content.

If

\[
Q=C_\chi+m_\chi m_\chi^T,
\]

then direction `i` contributes

\[
\boxed{
\mathcal E_i
=
\sigma_i^2
\left[
(v_i\!\cdot m_\chi)^2
+v_i^TC_\chi v_i
\right].
}
\]

The two bracketed terms are again deterministic bias and stochastic spread, but
now resolved along an actual principal material-line direction rather than hidden
inside a scalar norm.

**Status: Exact spectral identity / physical directional typing.**

---

## 2. Literal repo refinement acts on the right

The line-frame convention already audited in the locality/lineage layer is

\[
\boxed{L_+=L_-R.}
\]

Material motion acts on the left; physical refinement/reselection acts on the
right.  Therefore

\[
\boxed{
M_+
=L_+^TL_+
=R^TM_-R.
}
\]

This is the geometry face of a finite refinement event.  It is not a rule for the
current-state second moment.  In particular, it does **not** say that an arbitrary
physical refinement must transform `Q` by inverse congruence.

**Status: Exact identity / literal refinement convention.**

---

## 3. Finite event: exact midpoint geometry/state polarization

First hold the random-frame correlation issue aside and consider deterministic
or conditioned tensors `M_-,Q_-` and `M_+,Q_+`.  Define

\[
\bar M=\frac{M_++M_-}{2},
\quad
\Delta M=M_+-M_-,
\]

and analogously for `Q`.  Since the physical energy is the bilinear pairing

\[
E=\operatorname{tr}(MQ),
\]

we have the exact finite identity

\[
\boxed{
\Delta E
=
\operatorname{tr}(\bar Q\,\Delta M)
+
\operatorname{tr}(\Delta Q\,\bar M).
}
\]

The two terms have different physical meanings:

- `tr(Qbar Delta M)`: **geometry / line-metric reweighting**;
- `tr(Delta Q Mbar)`: **current/residual second-moment revaluation**.

Both are signed finite revaluations.  Neither is a positive payment.  Midpoint
polarization is particularly useful because it does not impose an artificial
ordering such as "first change the geometry, then change the current".

Most importantly, this identity does not construct `Delta Q`.  For an actual
selected current refinement, `Delta Q` is inherited from the full tensor-square
pair refinement and therefore retains the cross-child sectors already audited in
the pair-current layer.

**Status: Exact finite-jump identity / physical two-face typing.**

---

## 4. Passive GL reparameterization: nonzero faces, zero physical event

A passive change of codeforming coordinates by an invertible `R` transforms

\[
M_+=R^TMR,
\qquad
Q_+=R^{-1}QR^{-T}.
\]

Then

\[
\boxed{
\operatorname{tr}(M_+Q_+)=\operatorname{tr}(MQ).
}
\]

Yet the midpoint geometry and state faces above can both be nonzero.  Exact
symbolic calibration gives

\[
\boxed{
G_{\rm face}+S_{\rm face}=0
}
\]

with `G_face != 0` and `S_face != 0` separately.

Thus a passive GL coordinate change can exhibit substantial signed traffic in the
split ledger while producing **zero physical revaluation**.  This must not be
confused with physical refinement/reselection, where the current itself and its
pair law may genuinely change.

**Status: Exact gauge identity / audited nontrivial cancellation.**

---

## 5. Random full state: a third finite-event face is mandatory

On the actual stochastic current-shape state, the line metric and residual second
moment need not be independent.  Write

\[
\mathcal E
=
\operatorname{tr}(\overline M\,\overline Q)
+C_{MQ},
\]

where

\[
C_{MQ}
=
\mathbb E\operatorname{tr}
[(M-\overline M)(Q-\overline Q)].
\]

Across a finite event, midpoint polarization of the factorized part gives

\[
\boxed{
\Delta\mathcal E
=
\operatorname{tr}(\overline Q_{\rm mid}\,\Delta\overline M)
+
\operatorname{tr}(\Delta\overline Q\,\overline M_{\rm mid})
+
\Delta C_{MQ}.
}
\]

The full event therefore has **three literal faces**:

1. geometry/metric reweighting;
2. current/residual second-moment revaluation;
3. metric--residual correlation revaluation.

An exact algebraic referee with

\[
M_- = I,
\quad Q_- = \mathrm{diag}(1,0,0),
\quad C_- = 0,
\]

and

\[
M_+ = \mathrm{diag}(4,1,1),
\quad Q_+ = \mathrm{diag}(2,0,0),
\quad C_+ = 3/4
\]

gives

\[
\boxed{
G_{\rm face}=\frac92,
\qquad
S_{\rm face}=\frac52,
\qquad
C_{\rm face}=\frac34,
}
\]

and their sum is exactly the total energy jump.

The third face is not selector covariance, not deformation covariance, and not a
future-bank source.  It is ordinary same-state correlation between physical
geometry and residual content.

**Status: Exact full-state finite-event identity / rigorous third-face necessity.**

---

## 6. Smooth segment: scale + anisotropy + current content

Factor the physical line metric as

\[
\boxed{M=\rho^2\mathcal A,}
\]

where `rho` is the coherent physical line scale and `A` carries anisotropy/shape.
For

\[
E=\operatorname{tr}(MQ),
\]

the literal product rule is

\[
\boxed{
\dot E
=
2\frac{\dot\rho}{\rho}E
+
\rho^2\operatorname{tr}(Q\dot{\mathcal A})
+
\operatorname{tr}(\dot Q M).
}
\]

The three smooth faces are:

- **physical scale dilation/refinement rate**;
- **anisotropy / line-metric work**;
- **residual/current-content evolution**.

For incompressible material transport, the previously audited coherent material
scale satisfies `rho_dot=0`; material motion changes anisotropy rather than
reference scale.  A physical refinement event may change `rho` separately.

**Status: Exact product-rule identity / scale--shape--content split.**

---

## 7. Reverse material segment: strain work + residual q.v.

For the reverse local line frame

\[
\dot L=-AL,
\]

the line metric obeys

\[
\boxed{
\dot M
=-L^T(A^T+A)L.
}
\]

For the codeforming residual martingale

\[
d\chi=\sqrt{2\nu}\,\widetilde Q\,dW,
\]

the second moment has q.v. source

\[
\dot Q_\chi
=2\nu\widetilde Q\widetilde Q^T
\]

at the pathwise/Itô second-moment level.  Substitution into the weighted energy
law gives exactly

\[
\boxed{
\dot E
=
-2\operatorname{tr}(S\,LQ_\chi L^T)
+
2\nu\operatorname{tr}
(\widetilde Q\widetilde Q^T M),
}
\]

where `S=(A+A^T)/2`.

Thus the codeforming q.v.-only law and the physical signed strain-work law are not
competing descriptions.  They are the same process viewed before and after the
physical line metric is restored.

**Status: Exact Itô/material-frame identity.**

---

## 8. Homogeneous isotropic physical refinement

For a homogeneous degree-`p` nonaffine jet, the weighted audit already found

\[
Q_\chi\sim\rho^{2p-4},
\qquad
M\sim\rho^2.
\]

Under an isotropic physical refinement factor `lambda`, this becomes

\[
M_+=\lambda^2M,
\qquad
Q_+=\lambda^{2p-4}Q,
\]

and therefore

\[
\boxed{
E_+=\lambda^{2p-2}E.
}
\]

At `p=2`, the raw codeforming residual content is scale-invariant and the entire
leading physical shrink is carried by the line metric.  For `p>2`, both geometry
and residual content shrink.  These are distinct physical mechanisms even though
their product has one compact exponent.

**Status: Exact homogeneous refinement identity.**

---

## 9. Exact quadratic NS: weighted residual descent does not imply support locality

Return to

\[
u=(y^2+2\nu t,0,0).
\]

Use the anisotropic line frame

\[
\boxed{L_\rho=\operatorname{diag}(1,\rho,\rho).}
\]

Take an `xy` rectangle with physical x-length `1` and y-length `rho`.  Exact Stokes
for the quadratic shear gives

\[
\boxed{
\varepsilon_z=-\rho^2.
}
\]

Since

\[
J=\det L_\rho=\rho^2,
\]

we have

\[
\boxed{
\chi=-e_z,
\qquad
r=L_\rho\chi=-\rho e_z,
\qquad
|r|^2=\rho^2\to0.
}
\]

But the physical x-line remains exactly length one:

\[
\boxed{|L_\rho e_x|=1.}
\]

The packet is therefore not support-local even though the weighted Kelvin residual
vanishes.

This is a rigorous seam separation:

\[
\boxed{
\text{weighted Kelvin residual collapse}
\not\Rightarrow
\text{support locality}.
}
\]

The converse has already failed in earlier anisotropic nonaffinity calibrations as
well.  The first-bad theorem must retain both physical geometry and physical
residual content.

**Status: Audited calibration (exact Navier--Stokes) / rigorous seam no-go.**

---

## 10. Placement relative to selector/refinement pair algebra

The energy identities above are downstream observers of the full selected-current
state.  They do not alter the already audited event semantics:

- a cycle-typed selector does not create an intrinsic physical boundary;
- moving support cuts have their own literal cut/boundary faces;
- finite first-bad entry/resolve changes are reset/reselection events;
- physical refinement lifts to the full pair tensor square;
- cross-child and cross-orientation covariance cannot be dropped;
- random-frame metric--residual correlation is an additional same-state mixed face,
  not a replacement for those pair sectors.

In particular, `Delta Q` in the midpoint identity is an **input from the exact full
current/pair event map**, not a closure hypothesis manufactured by this scalar
energy ledger.

**Status: Exact ledger placement / no new pair closure claim.**

---

## 11. Refined literal frontier

The surface complexity has now collapsed to a small exact local/event law without
throwing away its physical distinctions.  On a conditioned frame the residual
energy is resolved direction by direction:

\[
\boxed{
\mathcal E_i
=
\sigma_i^2
\left[(v_i\!\cdot m_\chi)^2+v_i^TC_\chi v_i\right].
}
\]

On the full random state, one must additionally retain metric--residual
correlation.  Across events, geometry, current content, and correlation each have
signed revaluation faces.  During smooth reverse material motion, the same energy
has strain-work and q.v. faces.

What remains genuinely open is not "find a norm that bounds everything."  It is:

1. prove actual first-bad **support locality/conditioning** in every relevant
   physical line direction;
2. prove the corresponding **directional weighted residual products** vanish in
   the correct full-state topology;
3. retain the metric--residual correlation rather than factorizing it away;
4. instantiate the physical selector/refinement/boundary/exit/reset laws on the
   same migrating state;
5. separately solve the unresolved clock/ancestry/future-bank identification if
   that bridge is needed for restart.

The exact quadratic long-support referee proves that item 2 cannot replace item 1.
There is **no restart/continuation/regularity theorem claimed** here; no first-bad threshold or restart capacity is proved either.

**Status: first-bad directional weighted products Open; support locality Open; no
restart/continuation/regularity theorem claimed.**
