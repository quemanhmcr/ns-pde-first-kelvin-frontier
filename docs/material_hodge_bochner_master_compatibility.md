# Material Hodge--Bochner master compatibility reduction

This note reverses the direction of the recent case-by-case development.  It does
not introduce a new score, selector, packet bank, or continuation criterion.  The
question is whether the already-audited Kelvin, Cauchy/Nanson, metric-work,
viscous-Gram, covariance, and normalized-vorticity contact laws are genuinely
separate mechanisms, or whether they are natural representations of one smaller
Navier--Stokes operator structure.

The answer on every smooth interval is substantially smaller than the previous
ledger suggests.  After pulling the physical vorticity two-form back by the actual
Lagrangian flow, the Lie-transport term disappears exactly.  What remains is an
exact closed two-form Hodge heat equation on the pullback Euclidean metric.  That
metric is not an added model state: it is the flat, volume-preserving metric induced
by the same physical flow, and the velocity that moves it is Hodge-reconstructed
from the same vorticity state (up to the usual harmonic/Galilean mode).

Thus the local nonlinear core can be written as a feedback between

\[
\boxed{\text{closed/exact vorticity Hodge heat}}
\qquad\text{and}\qquad
\boxed{\text{self-generated volume-one material metric}}.
\]

The two visible defects of functoriality are then:

1. time variation of the metric/Hodge pairing, which is vortex stretching / metric
   work;
2. failure of the second-order diffusion operator to be a derivation, whose
   bilinear defect is the Bochner/carre-du-champ Gram.

The normalized-vorticity contact identity is the *untraced* version of the second
product defect.  It is therefore not a third primitive mechanism.

No first-bad identification, restart theorem, continuation theorem, blow-up
exclusion, or global-regularity conclusion is claimed.

Throughout this note, `Delta_g` denotes the **PDE-sign** Hodge Laplacian: in a flat
Euclidean frame its coefficient action is `sum_i partial_i^2`.  With this convention
Navier--Stokes uses `+ nu Delta_g` on the right-hand side.

---

## 1. Exact one-form and vorticity-form equations

Let the physical domain be the flat three-torus with Euclidean metric `g_0` and
volume form `vol_0`.  Write

\[
\alpha=u^\flat,
\qquad
\beta=d\alpha=\iota_\omega\,\mathrm{vol}_0.
\]

The incompressible Navier--Stokes momentum equation is exactly

\[
\boxed{
(\partial_t+\mathcal L_u-\nu\Delta_{g_0})\alpha
=dB,
\qquad
B=\frac{|u|^2}{2}-p.
}
\]

Applying `d` and using

\[
[d,\mathcal L_u]=0,
\qquad
[d,\Delta_{g_0}]=0,
\qquad
d^2=0,
\]

gives

\[
\boxed{
(\partial_t+\mathcal L_u-\nu\Delta_{g_0})\beta=0,
\qquad d\beta=0.
}
\]

The pressure/Bernoulli sector has disappeared because it was exact before any
estimate or current pairing was introduced.

**Classification: Exact identity.**

---

## 2. Pull back by the actual Lagrangian flow

Let `Phi_t` be the deterministic Lagrangian flow of the same Navier--Stokes
velocity:

\[
\partial_t\Phi_t(a)=u(\Phi_t(a),t),
\qquad
\Phi_0(a)=a.
\]

Define the material pullbacks

\[
\bar\alpha=\Phi_t^*\alpha,
\qquad
\bar\beta=\Phi_t^*\beta,
\qquad
G_t=\Phi_t^*g_0.
\]

For every time-dependent tensor `T`,

\[
\frac d{dt}\Phi_t^*T
=
\Phi_t^*(\partial_t+\mathcal L_u)T.
\]

The Hodge Laplacian is natural when the metric is pulled back together with the
form:

\[
\Phi_t^*(\Delta_{g_0}T)
=
\Delta_{G_t}(\Phi_t^*T).
\]

Therefore the momentum one-form becomes

\[
\boxed{
\partial_t\bar\alpha-
u\Delta_{G_t}\bar\alpha
=d\bar B,
\qquad
\bar B=\Phi_t^*B,
}
\]

while the vorticity two-form becomes the much smaller law

\[
\boxed{
\partial_t\bar\beta
=
u\Delta_{G_t}\bar\beta,
\qquad
\bar\beta=d\bar\alpha,
\qquad
d\bar\beta=0.
}
\]

All explicit Lie transport has disappeared.  For Euler (`nu=0`), the material
vorticity two-form is literally frozen.  For Navier--Stokes, the same exact form is
Hodge-diffused in the material metric.

**Classification: Exact material-pullback/Hodge identity.**

---

## 3. The material metric is physical, flat, and volume preserving

Let

\[
F=D\Phi_t,
\qquad
G=F^TF.
\]

This is not an independently chosen metric.  It is exactly the pullback of the
physical Euclidean metric.  Hence, at every smooth time,

\[
\boxed{\operatorname{Rm}(G)=0.}
\]

Incompressibility gives

\[
\det F=1,
\qquad
\boxed{\det G=1},
\qquad
\boxed{\mathrm{vol}_{G}=\mathrm{vol}_0}.
\]

Let

\[
U=\Phi_t^*u
=F^{-1}u\circ\Phi_t.
\]

Then `bar alpha` is exactly the `G`-metric dual of `U`:

\[
\boxed{
\bar\alpha=U^{\flat_G}.
}
\]

Naturality of the Lie derivative gives

\[
\boxed{
\partial_tG
=\Phi_t^*(\mathcal L_u g_0)
=\mathcal L_U G.
}
\]

Equivalently, in physical matrix notation,

\[
\dot G
=F^T[(\nabla u)^T+\nabla u]F
=2F^TSF.
\]

The metric evolution is therefore a pure diffeomorphism deformation of a flat
metric, but its relative motion against the diffusing vorticity form is physical.

Incompressibility also pulls back exactly:

\[
\boxed{\delta_G\bar\alpha=0.}
\]

After fixing the conserved harmonic/Galilean velocity mode, the Hodge system

\[
d\bar\alpha=\bar\beta,
\qquad
\delta_G\bar\alpha=0
\]

reconstructs `bar alpha`, hence `U`, from `(G,bar beta)`.  If the harmonic mode is
not fixed to zero it must be carried explicitly; it is not silently discarded.

**Classification: Exact Cauchy/Hodge geometry; rigorous Hodge-reconstruction
consequence after the harmonic gauge is fixed.**

---

## 4. The exact reduced feedback loop

The preceding identities show that every smooth incompressible Navier--Stokes
solution produces the coupled material system

\[
\boxed{
\begin{aligned}
&\partial_t\bar\beta=\nu\Delta_G\bar\beta,
&&d\bar\beta=0,
&&\bar\beta=d\bar\alpha,\\
&\delta_G\bar\alpha=0,
&&U=\bar\alpha^{\sharp_G},
&&\partial_tG=\mathcal L_U G,\\
&\operatorname{Rm}(G)=0,
&&\mathrm{vol}_{G}=\mathrm{vol}_0.
\end{aligned}
}
\]

Modulo the exact pressure gauge and the finite-dimensional harmonic velocity mode,
this is the smallest operator system presently visible in the repository.

It is important not to overread this statement.  `G` is not arbitrary and
`bar beta` is not an arbitrary heat solution.  The metric is generated by the
velocity Hodge-reconstructed from the same exact vorticity form whose diffusion it
then controls.  The nonlinearity has been compressed into this self-generated
metric/heat feedback.

**Classification: Exact reduction from smooth Navier--Stokes.**

A full converse equivalence for arbitrary abstract pairs `(G,bar beta)` is not
claimed here; such a converse would require the global integrability/relabeling
conditions that characterize actual pullback metrics and the harmonic sector.

---

## 5. Reciprocal metric lock: amplification uses `G`, diffusion uses `G^{-1}`

Because `vol_G=vol_0`, write the pulled-back vorticity two-form as

\[
\bar\beta=\iota_b\,\mathrm{vol}_0
\]

for a material vector `b`.  Pullback of `i_omega vol_0` gives the exact Cauchy
relation

\[
\boxed{
\omega\circ\Phi=Fb.
}
\]

Therefore physical vorticity amplitude is

\[
\boxed{
|\omega|^2\circ\Phi
=b^TG b
=|\bar\beta|_G^2.
}
\]

Now let

\[
H=\operatorname{cof}F.
\]

Since `det F=1`,

\[
H=F^{-T}.
\]

Hence the exact area-frame identities are

\[
\boxed{
H^TH=G^{-1},
\qquad
(H^TH)^{-1}=G.
}
\]

The packet metric used throughout the earlier orientation-complete Kelvin work was

\[
M_H=(H^TH)^{-1}.
\]

Thus

\[
\boxed{M_H=G.}
\]

The earlier packet metric is not another physical degree of freedom at differential
material scale.  It is exactly the material pullback metric.

On the other hand, the principal symbol of the material Hodge heat operator is

\[
\boxed{
\sigma_2(\Delta_G)(\xi)
=-\,\xi^TG^{-1}\xi
}
\]

with the usual Fourier-sign interpretation for the PDE Laplacian.

So the same deformation has a forced reciprocal appearance:

\[
\boxed{
\text{vorticity/packet amplitude metric }G
\quad\leftrightarrow\quad
\text{area/diffusion metric }G^{-1}.
}
\]

This is an exact compatibility, not an estimate.  Stretching geometry and viscous
geometry cannot be prescribed independently.

**Classification: Exact Cauchy--Nanson--diffusion metric identity.**

A lightweight symbolic check on a general determinant-one upper-triangular frame
with anisotropic dilation and shear gives exactly
`M_H-G=0`, `H^T H-G^{-1}=0`, and
`|F b|^2-b^T G b=0`.  This is an algebra check, not a calibration campaign.

---

## 6. Vortex stretching is only time variation of the material fiber metric

Hold the material vorticity coordinate `b` fixed momentarily.  Since

\[
\dot G=2F^TSF,
\]

one has

\[
\boxed{
\frac12 b^T\dot G b
=(Fb)^TS(Fb)
=(\omega\cdot S\omega)\circ\Phi.
}
\]

Thus the nonlinear vortex-stretching scalar is precisely the work done by the
moving material metric on the vorticity flux coordinate.

This is the global material version of the earlier local packet identity

\[
\frac12\Phi^T\dot M_H\Phi=\omega\cdot S\omega.
\]

Because `M_H=G`, they are literally the same law.

**Classification: Exact metric-work identity.**

The important conceptual consequence is that Lie transport and vortex stretching
are not two independent physical producers.  After the exact material pullback,
Lie transport has disappeared from the form equation and stretching survives only
as the changing metric used to read its physical norm.

**Classification: Rigorous structural consequence.**

### 6.1 Stretching is the time-Hodge commutator

The same compression can be written without choosing the material vector `b`.
Because pullback commutes with the Hodge star when the metric is pulled back,

\[
\bar\zeta:=*_G\bar\beta
=\Phi_t^*(*_{g_0}\beta)
=\Phi_t^*(\omega^\flat).
\]

At each fixed time `Delta_G` commutes with `*_G`.  Therefore, for the material heat
operator

\[
\mathcal H_G:=\partial_t-\nu\Delta_G,
\]

one has the exact commutator identity

\[
\boxed{
\mathcal H_G(*_GX)-*_G\mathcal H_GX
=(\partial_t*_G)X.
}
\]

Since `H_G bar beta=0`,

\[
\boxed{
\mathcal H_G\bar\zeta
=(\partial_t*_G)\bar\beta.
}
\]

Pulling the physical vorticity one-form equation back gives

\[
\boxed{
(\partial_t*_G)\bar\beta
=2\,\Phi_t^*[(S\omega)^\flat].
}
\]

Thus vortex stretching is literally the failure of the time-dependent Hodge
identification between vorticity flux and vorticity vector/one-form to commute with
the material heat evolution.  In scalar form,

\[
\boxed{
(\omega\cdot S\omega)\circ\Phi
=\frac12\langle *_G\bar\beta,
(\partial_t*_G)\bar\beta\rangle_G.
}
\]

This is the operator version of the packet metric-work identity.

**Classification: Exact Hodge-star/strain commutator identity.**

---

## 7. One master pairing defect: metric work minus Bochner/carre-du-champ Gram

At each fixed time `(T^3,G_t)` is flat.  On differential forms the Hodge Laplacian
therefore agrees with the induced connection Laplacian up to the fixed PDE sign; the
corresponding pulled-back Euclidean vector/tensor representations obey the same
covariant product rule.  Hence

\[
\Delta_G\langle X,Y\rangle_G
=
\langle\Delta_GX,Y\rangle_G
+
\langle X,\Delta_GY\rangle_G
+2\langle\nabla^GX,\nabla^GY\rangle_G.
\]

The most compact form keeps the time-dependent metric and diffusion together.  For
`H_G=partial_t-nu Delta_G`,

\[
\boxed{
\begin{aligned}
&\mathcal H_G\langle X,Y\rangle_G
-\langle\mathcal H_GX,Y\rangle_G
-\langle X,\mathcal H_GY\rangle_G\\
&\qquad=
(\partial_t\langle\cdot,\cdot\rangle_G)(X,Y)
-2\nu\langle\nabla^GX,\nabla^GY\rangle_G.
\end{aligned}
}
\]

This is the master bilinear compatibility identity.  Its right-hand side has only
two terms: metric/Hodge work and the complete second-order Gram defect.  There is no
third local producer.

For `X=Y` the second term is the carré-du-champ Gram.

Apply this to the exact material vorticity heat equation.  Writing

\[
\bar e=\frac12|\bar\beta|_G^2=e\circ\Phi,
\]

one obtains

\[
\boxed{
(\partial_t-\nu\Delta_G)\bar e
=
\mathcal W_G(\bar\beta)
-\nu|\nabla^G\bar\beta|_G^2,
}
\]

where `W_G` is only the time derivative of the `G`-fiber pairing at fixed form.
Section 6 identifies it exactly with pulled-back vortex stretching:

\[
\mathcal W_G(\bar\beta)
=(\omega\cdot S\omega)\circ\Phi.
\]

Pulling the identity forward gives the familiar Eulerian enstrophy law

\[
D_te
=
\omega\cdot S\omega
+\nu\Delta e
-\nu|\nabla\omega|^2.
\]

So the three-face Eulerian enstrophy balance is the image of only two material
operations:

\[
\boxed{
\text{metric work}
\quad+\quad
\text{Hodge heat product defect}.
}
\]

**Classification: Exact Hodge--Bochner/enstrophy identity.**

The same bilinear product defect, before taking a scalar trace, is the tensor Gram
that already appears in the vorticity-dyad law and in connected covariance.  Thus
vorticity-dyad viscous defect, Kelvin quadratic variation, pair diagonal defect, and
future-covariance source are representations of one second-order bilinear defect,
not independent producers.

**Classification: Rigorous operator-level identification of already exact tensor
laws.**

---

## 8. Kelvin quadratic variation is the stochastic representation of the same heat defect

The material Hodge heat operator has carré-du-champ

\[
\Gamma_G(f,h)
=2\nu\langle df,dh\rangle_{G^{-1}}
\]

for scalar observables, with the natural matrix/Gram extension for vector-valued
observables.

For a closed current, the momentum one-form equation has only an exact
pressure/Bernoulli gauge besides Hodge diffusion.  Exactness kills that gauge under
closed-current pairing.  Cartan identifies spatial/noise derivatives of circulation
with contraction of the vorticity two-form.  Therefore the stochastic Kelvin Gram
is precisely the carré-du-champ representation of the same material Hodge heat
operator.

After returning to Eulerian coordinates this is the already-audited tensor

\[
2\nu(\nabla\omega)(\nabla\omega)^T
\]

and its full cross-orientation/common-noise Gram structure.

No independent ``Kelvin stochastic producer'' is added by passing to the stochastic
representation.  The stochastic process realizes the same second-order operator.

**Classification: Exact generator/carre-du-champ consequence of the established
Kelvin/Cartan laws.**

This statement does **not** identify different programme clocks or reduced ancestry
states.  A stochastic representation of the same operator is not automatically the
same random state as every future-bank construction.

---

## 9. Normalized-vorticity contact is the untraced Bochner product identity

Let

\[
W(t)=\|\omega(\cdot,t)\|_\infty,
\qquad
V=\omega/W.
\]

Pull the vector field back naturally to the material tangent bundle:

\[
\bar V=F^{-1}(V\circ\Phi).
\]

Because `Phi_t:(T^3,G_t)->(T^3,g_0)` is an isometry,

\[
\boxed{
|\bar V|_G^2=|V|^2\circ\Phi\le1.
}
\]

At an active maximum define the covariant material scalar curvature

\[
Q_G=-\operatorname{Hess}_G|\bar V|_G^2
\]

and the inward contact form

\[
\mathscr H_G(X,Y)
=-\langle\bar V,\nabla_X^G\nabla_Y^G\bar V\rangle_G.
\]

Metric compatibility of the Levi-Civita connection gives the untraced product rule

\[
\operatorname{Hess}_G\frac12|\bar V|_G^2(X,Y)
=
\langle\nabla_X^G\bar V,\nabla_Y^G\bar V\rangle_G
+
\langle\bar V,\nabla_X^G\nabla_Y^G\bar V\rangle_G.
\]

Hence

\[
\boxed{
\mathscr H_G
=(\nabla^G\bar V)^*\nabla^G\bar V
+\frac12Q_G.
}
\]

Pulling this identity forward is exactly the previously audited Eulerian law

\[
\mathscr H=(\nabla V)^T\nabla V+Q/2.
\]

Therefore normalized-vorticity contact is not a new primitive below the scalar
curvature layer.  It is the directional, untraced Bochner product defect of the
same covariant derivative whose trace is the viscous/Kelvin carré-du-champ.

In particular,

\[
\boxed{
\ker\mathscr H_G
=\ker Q_G\cap\ker(\nabla^G\bar V),
}
\]

and the left/right Gram tensors are simply the target/domain contractions of the
same derivative tensor.

**Classification: Exact covariant contact identity / rigorous compression of the
previous contact grammar.**

A direct symbolic jet check gives zero residual in
`H_contact - Gram - Q/2`; it is only an algebra referee for the exact covariant
identity.

---

## 10. Cauchy, Nanson, deformation connection, and finite material shape are functorial images

For any deterministic material current

\[
Z_t=\Phi_{t*}Z_0,
\]

pullback freezes the current itself:

\[
\langle\alpha_t,Z_t\rangle
=
\langle\bar\alpha_t,Z_0\rangle.
\]

Thus the full material support/current is a fixed reference current observed through
the evolving metric and pulled-back form.  Cauchy line transport, Nanson area
transport, deformation congruence, and the local connection cancellations are the
induced tangent/cotangent/current representations of the same diffeomorphism.

The earlier infinite finite-shape tower is therefore not evidence for an infinite
family of independent Navier--Stokes mechanisms.  It is what appears when the full
nonlinear pushforward of a current is projected onto a finite local affine/moment
representation.  Keeping the full reference current removes that projection loss
exactly.

**Classification: Exact material-current functoriality / rigorous architecture
compression.**

This does **not** prove that a finite packet state closes.  The prior polynomial
no-go results remain valid: replacing the full current by finitely many moments or
by a local deformation matrix loses physical information.  The master reduction
explains *why* that hierarchy appeared; it does not make an invalid finite
truncation valid.

---

## 11. Intrinsic moving readouts are observations of the same two-object system

The intrinsic max-normalized enstrophy field becomes in material coordinates

\[
\bar g(a,t)
=
\frac{|\bar\beta(a,t)|_{G_t}^2}
{\max_b|\bar\beta(b,t)|_{G_t}^2}.
\]

Thus the filtration `{g>=theta}` is generated entirely from `(G,bar beta)`.  Its
moving-boundary law is the Reynolds/coarea readout of the same metric-work plus
Hodge-heat balance.  No selector force or extra Brownian source is created by this
observation.

What does *not* follow from the master operator is that this particular readout is
the continuation-critical one.  An actual first-bad rule, a hysteretic event map,
or a reduced ancestry lift is additional state/readout semantics and remains to be
derived from Navier--Stokes rather than assumed.

**Classification: Exact intrinsic-readout provenance; first-bad identification
Open-literal.**

---

## 12. What has actually been unified

On a smooth interval the following formerly separate-looking mechanisms have now
been compressed.

### Exact/gauge sector

- pressure/Bernoulli invisibility on closed currents;
- `d beta=0` and preservation of exactness;
- Stokes/Cartan current relations.

These are consequences of the de Rham complex and exact gauge.

### Transport/deformation sector

- Cauchy line deformation;
- Nanson area deformation;
- packet metric work;
- curvature/support connection cancellation;
- deterministic full material-current shape transport.

These are induced representations of the same physical diffeomorphism / pullback
metric.

### Second-order sector

- viscous enstrophy Gram loss;
- vorticity-dyad defect tensor;
- Kelvin common-noise quadratic variation;
- same-ancestor pair diagonal defect;
- future covariance source;
- normalized-vorticity right Gram/contact term.

These are traced, left-Gram, pair, covariance, or untraced-Hessian representations
of the same Hodge/Bochner second-order product defect.

**Classification: Rigorous operator-level synthesis of exact identities already
established separately.**

---

## 13. What is *not* yet a direct consequence

The reduction does not manufacture semantics that are absent from the PDE state.
The following remain separate open questions.

1. **Actual first-bad readout/event.**  The PDE has not yet supplied a theorem that
   identifies continuation failure with the max-normalized filtration, contact
   kernel, or any hysteretic packet event.
2. **Reduced ancestry/future-bank state.**  A quotient state still requires a
   literal generator-compatible lift; law-of-total-covariance resolution faces do
   not disappear by changing coordinates.
3. **Clock identification.**  Material Hodge heat, reverse-age stochastic Kelvin,
   and any future-remaining bank must be related by an explicit causal state/time
   map before their random variables are called identical.
4. **Finite-state closure.**  The full material current can be frozen by pullback,
   but no finite moment/deformation truncation universally represents that current.
5. **Singular-time uniformity.**  All identities here hold on smooth intervals.
   They do not provide the missing uniform control as a candidate singular time is
   approached.

**Classification: Open-literal/Open as indicated; no restart or regularity claim.**

---

## 14. The new no-escape frontier is a self-generated metric/heat compatibility problem

The operator compression changes the research question.

A hypothetical vorticity escape is

\[
\sup_a |\bar\beta(a,t)|_{G_t}
\longrightarrow\infty.
\]

But the two ingredients in this norm cannot be chosen independently:

- `bar beta` is an **exact closed two-form** solving Hodge heat in `G_t`;
- `G_t` is a **flat volume-one pullback metric** generated by
  `U=bar alpha^{sharp_G}`;
- `bar alpha` is Hodge-reconstructed from the **same** `bar beta` modulo the
  harmonic mode;
- the metric that amplifies vorticity is exactly the packet metric `G`, while the
  principal diffusion/area metric is its reciprocal `G^{-1}`.

Thus any genuine no-escape theorem should not try to dominate a separately defined
stretching score by a separately defined dissipation score.  It should prove that
an escape path for the coupled state

\[
\boxed{(G_t,\bar\beta_t)}
\]

is incompatible with the simultaneous constraints

\[
\boxed{
\partial_t\bar\beta=\nu\Delta_G\bar\beta,
\quad
\partial_tG=\mathcal L_{\mathcal B_G\bar\beta}G,
\quad
d\bar\beta=0,
\quad
\operatorname{Rm}(G)=0,
\quad
\mathrm{vol}_G=\mathrm{vol}_0,
}
\]

where `B_G bar beta := (bar alpha)^{sharp_G}=U` denotes the velocity obtained
from the co-closed Hodge/Biot--Savart reconstruction with the harmonic mode fixed.

This is now the smallest literal candidate for the hidden self-compatibility law
behind the existing programme.

**Classification: Conjectural bridge only for the claim that these exact
compatibilities suffice to exclude singular escape.**

No such exclusion is proved here.

---

## 15. Frontier correction

The previous frontier asked what higher vector/contact structure closes
`ker H_contact`.  That remains a valid local question, but it is no longer the
primitive next question.

The deeper frontier is:

\[
\boxed{
\text{What exact compatibility between the self-generated flat metric }G
\text{ and the exact Hodge-heated form }\bar\beta
\text{ forbids an escape configuration, if such a prohibition exists?}
}
\]

A successful next theorem should reduce the number of independent mechanisms
again.  It should not add a new packet score or another contact tensor unless that
object is forced as a natural projection of the coupled `(G,bar beta)` system.

**Current status:** master material pullback, reciprocal metric lock, metric-work
identity, Bochner/carre-du-champ synthesis, and contact-as-untraced-Bochner are
Exact/Rigorous.  Their sufficiency for no-escape, continuation, or global regularity
is Open.

---

## Follow-through: the two-object frontier compresses to a moving Hodge constraint

The next theorem is now recorded in
`docs/hodge_strain_null_lagrangian_compatibility.md`.  It sharpens the apparent
`(G,bar beta)` two-object feedback in three ways.

First,

\[
\nabla^G\bar\alpha=\frac12\partial_tG+\frac12\bar\beta,
\]

so material metric velocity/strain and vorticity are the symmetric and
antisymmetric faces of one trace-free integrable covariant gradient.  The induced
Hodge--strain map is a scaled `L^2` isometry, and the quadratic/cubic minor
compatibilities are exactly the pressure Poisson/equipartition and Betchov laws.

Second, if `P_G` is the Hodge projector onto co-closed one-forms, then the exact
Bernoulli/pressure term is

\[
\boxed{d\bar B=(\partial_tP_G)\bar\alpha},
\]

so the material momentum equation is

\[
\boxed{(\partial_t-\partial_tP_G)\bar\alpha=\nu\Delta_G\bar\alpha.}
\]

Pressure/Bernoulli is therefore the off-diagonal connection needed to keep the
velocity one-form in a Hodge subspace moved by the self-generated metric.

Third, at frozen flat `G`, the Hodge--strain map intertwines diffusion; its actual
failure to heat is exactly its time variation, whose Eulerian representation is the
full symmetric quadratic/rotation/pressure-Hessian strain feedback.

Thus the shorter frontier superseding Section 14 is not merely `metric + heat`, but

\[
\boxed{
\text{Hodge heat inside a Hodge geometry moved by the same heated state}.
}
\]

Whether this self-Hodge compatibility forbids singular escape remains Open.  No
restart, continuation, blow-up exclusion, or regularity theorem is claimed.
