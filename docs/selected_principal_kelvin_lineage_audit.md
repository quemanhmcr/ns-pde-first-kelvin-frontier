# Selected principal Kelvin lineage audit

This note connects the physical weighted Kelvin residual channels to the literal
cycle-typed first-bad selector and to the already-audited full pair refinement/reset
algebra.  The order is deliberately physical:

1. type the germ selector and the physical fiber separately;
2. prove which operators commute before assigning any channel meaning;
3. keep the full pair state under selector changes/refinement;
4. use exact Navier--Stokes finite-face calibrations before any collapse claim;
5. only then state the surviving first-bad frontier.

No norm estimate is used in the identities below.

---

## 1. Joint state: germ factor versus physical residual fiber

Let `G` be the finite candidate-germ coefficient space.  For each germ `g`, keep a
three-component residual fiber.  The joint residual library therefore lives in

\[
G\otimes \mathbb R^3.
\]

The literal first-bad selector is the already-defined diagonal rank-one germ
projector

\[
M_{\rm fb}:G\to G,
\]

and its orientation/fiber-complete lift is

\[
\boxed{\widehat M_{\rm fb}=M_{\rm fb}\otimes I_3.}
\]

Each germ may have its own primal line metric and its own spectral projectors.  Thus
one must not pretend that a single common principal basis exists across the entire
germ library.  A physical spectral operator on the library is block diagonal:

\[
\mathbb P=\operatorname{diag}(P_1,\ldots,P_N).
\]

**Status: Exact type definition inherited from the cycle selector and
orientation-complete packet.**

---

## 2. First-bad selection creates no spectral commutator source

Because `M_fb` is diagonal in the germ basis while `mathbb P` is block diagonal on
the physical fiber,

\[
\boxed{
[\widehat M_{\rm fb},\mathbb P]=0.
}
\]

The same is true on the full ordered pair state:

\[
\boxed{
[\widehat M_{\rm fb}^{\otimes2},\mathbb P^{\otimes2}]=0.
}
\]

Therefore, on a frozen hysteretic first-bad branch, there is **no intrinsic selector--spectral commutator source**.  Principal-axis motion that occurs because
the physical line metric evolves remains the eigenframe-mixing/metric-work face
already audited in `principal_kelvin_residual_channels_audit.md`; it is not selector
production.

This statement is special to the literal rank-one/diagonal first-bad support map.  A
generic germ-mixing matrix need not commute with per-germ spectral blocks.  CI keeps
an explicit two-germ counterexample.

**Status: Exact identity for the literal first-bad selector / audited scope
counterexample for generic germ mixing.**

---

## 3. The selected endpoint bank is an exact block-spectral bank

Let

\[
\mathbb Q=\mathbb E[\boldsymbol\chi\boldsymbol\chi^T]
\]

be the full joint germ/fiber residual second moment, including all off-diagonal germ
blocks.  Let

\[
\mathbb M=\operatorname{diag}(M_1,\ldots,M_N).
\]

The selected weighted residual energy is exactly

\[
\boxed{
\mathcal E_{\rm fb}
=\operatorname{tr}
\left(
\widehat M_{\rm fb}\,\mathbb M\,\widehat M_{\rm fb}\,\mathbb Q
\right).
}
\]

If the selected germ is `g_*` and

\[
M_{g_*}=\sum_\alpha\lambda_{g_*\alpha}P_{g_*\alpha},
\]

then

\[
\boxed{
\mathcal E_{\rm fb}
=\sum_\alpha
\lambda_{g_*\alpha}
\operatorname{tr}(P_{g_*\alpha}Q_{g_*g_*}).
}
\]

This does **not** mean the off-diagonal germ pair blocks have been discarded.  A
rank-one endpoint observable simply does not pair with them at that endpoint.  They
become active immediately when the selector changes, as the finite reset law below
shows.

**Status: Exact identity.**

---

## 4. Linear physical-fiber synthesis forces the full pair functor

Whenever a physical residual observable is genuinely synthesized linearly from a
fiber library, write

\[
A=[a_1I_3\;\cdots\;a_NI_3],
\qquad
r_A=A\mathbf r.
\]

Then its second moment is

\[
\boxed{Q_A=A\mathbb Q A^T.}
\]

After column vectorization,

\[
\boxed{
\operatorname{vec}(Q_A)
=(A\otimes A)\operatorname{vec}(\mathbb Q).
}
\]

Thus the pair map is not optional bookkeeping: it is exactly the tensor-square
functor forced by linear physical synthesis.

Writing `Q_ij` for the ordered child/germ pair blocks,

\[
\boxed{
Q_A=\sum_{i,j}a_i a_j Q_{ij}.
}
\]

For an endpoint spectral projector `P_alpha`,

\[
\boxed{
E_{\alpha,A}
=\lambda_\alpha
\sum_{i,j}a_i a_j\operatorname{tr}(P_\alpha Q_{ij}).
}
\]

Every `i != j` term is literal cross-child/cross-germ physical second-moment
content.  A diagonal-only spectral descendant is non-functorial for exactly the
same reason as the previously audited Kelvin covariance refinement.

**Status: Exact identity.**

Important scope boundary: the formula applies once the actual physical residual
observable is supplied as a linear synthesis map `A`.  The repository does **not**
yet derive a programme-specific map showing that every moving first-bad current
refinement induces such a common-fiber synthesis on the reconstructed Kelvin
residual.  That actual refinement lift remains Open-literal.

---

## 5. Exact one-mode Navier--Stokes cross-child channel cancellation

Use the exact smooth periodic shear

\[
u(y,t)=e^{-\nu k^2t}\cos(ky)e_x.
\]

Take two equal isotropic asymmetric square packets of side

\[
\rho=\frac{\pi}{2k}
\]

with anchors separated by half a period:

\[
Y_0=0,
\qquad
Y_1=\frac{\pi}{k}.
\]

The exact finite codeforming residuals satisfy

\[
\boxed{\chi_1=-\chi_0\neq0.}
\]

Therefore a physical linear parent with coefficients `(1,1)` has

\[
\chi_P=\chi_0+\chi_1=0.
\]

For the `z` principal channel,

\[
\boxed{E_{z,P}^{\rm full}=0,}
\]

while the diagonal-only child channel is strictly positive.  Hence the cross-child
channel is exactly the negative of the positive diagonal sum.

This is the weighted finite-residual analogue of the earlier odd-mode Kelvin
covariance witness: positive child diagonals are not a refinable physical payment.

**Status: Audited calibration using an exact Navier--Stokes solution / rigorous
cross-child necessity.**

---

## 6. Finite first-bad selector reset: geometry plus the full pair jump

Consider a frozen joint residual library `mathbb Q` and a finite selector/synthesis
change

\[
A_+=A_-+\Delta A.
\]

Let the endpoint line metrics be `M_-` and `M_+`, and define midpoint objects

\[
\bar M=\frac{M_++M_-}{2},
\qquad
\bar Q=\frac{Q_++Q_-}{2}.
\]

The exact weighted event jump is

\[
\Delta\mathcal E
=\operatorname{tr}(\bar Q\,\Delta M)
+\operatorname{tr}(\bar M\,\Delta Q).
\]

But the state face itself has the exact tensor-square reset decomposition

\[
\boxed{
\Delta Q
=\Delta A\,\mathbb Q A_-^T
+A_-\mathbb Q\,\Delta A^T
+\Delta A\,\mathbb Q\,\Delta A^T.
}
\]

Therefore the literal finite first-bad reset has four signed faces:

\[
\boxed{
\begin{aligned}
\Delta\mathcal E
={}&\underbrace{\operatorname{tr}(\bar Q\,\Delta M)}_{\rm geometry}\\
&+\underbrace{\operatorname{tr}(\bar M\,\Delta A\mathbb Q A_-^T)}_{\rm pair\ left}\\
&+\underbrace{\operatorname{tr}(\bar M\,A_-\mathbb Q\Delta A^T)}_{\rm pair\ right}\\
&+\underbrace{\operatorname{tr}(\bar M\,\Delta A\mathbb Q\Delta A^T)}_{\rm pair\ quadratic}.
\end{aligned}
}
\]

For a pure selector reset with fixed physical metric, the geometry face is exactly
zero.  The remaining three faces are the physical residual counterpart of the
cycle-selector pair jump

\[
\Delta P\otimes P_-+P_-\otimes\Delta P+\Delta P\otimes\Delta P.
\]

**Status: Exact fixed/conditioned finite-event identity.**

For a random metric/full stochastic state, the previously audited
metric--residual correlation face must still be retained if one factorizes at the
mean level.  The present identity does not erase that requirement.

---

## 7. Exact one-mode reset: positive quadratic face is not a reset cost

Use the same half-period exact NS pair.  Reset the selected germ from `g_0` to
`g_1`.  The endpoint weighted energies are equal because the two residuals are
opposite:

\[
\boxed{\Delta\mathcal E=0.}
\]

However the finite reset faces obey

\[
\mathcal R_L<0,
\qquad
\mathcal R_R<0,
\qquad
\mathcal R_Q>0,
\]

and

\[
\boxed{
\mathcal R_L+\mathcal R_R+\mathcal R_Q=0.
}
\]

Thus the positive quadratic selector increment is not a physical reset payment by
itself.

**Status: Audited calibration using exact Navier--Stokes.**

---

## 8. Closed hysteresis excursion: no positive selector path-length bank

Run the exact finite selector excursion

\[
g_0\longrightarrow g_1\longrightarrow g_0
\]

on the frozen one-mode residual library.  The endpoint energy returns to itself.
The accumulated quadratic reset face is strictly positive, while the accumulated
signed linear pair faces are negative and cancel it exactly:

\[
\boxed{
\sum_{\rm events}\Delta\mathcal E=0,
\qquad
\sum\mathcal R_Q>0,
\qquad
\sum(\mathcal R_L+\mathcal R_R)<0.
}
\]

Therefore even at the physically weighted residual level there is no legitimate
bank obtained by summing positive selector-jump squares.

**Status: Audited exact-NS closed-excursion calibration / rigorous no-positive-path
consequence.**

---

## 9. Endpoint spectral channels do not canonically match across an event

The spectral decomposition at each endpoint is canonical only at the level of
spectral projector blocks.  Across a finite selector/reset/refinement event, the
repository has not supplied a physical transport map identifying individual
principal axes from one endpoint with those at the other.

The obstruction is literal at eigenvalue degeneracy.  Inside a repeated-eigenvalue
plane, rotating the rank-one eigenbasis changes individual rank-one channel values
while preserving

\[
\boxed{\lambda\operatorname{tr}(P_{\rm block}Q).}
\]

Consequently, a statement such as “channel 1 before becomes channel 1 after” is not
coordinate-free unless a physical inter-event transport is supplied.  The correct
finite event law is the pair/metric revaluation above; endpoint channel sums may be
computed separately on each side.

**Status: Exact projector-gauge obstruction / Open-literal for any programme-specific
cross-event principal-channel transport map.**

---

## 10. Hybrid selected-lineage law on one compatible clock

On an unresolved hysteretic branch, `M_fb` is frozen.  For the selected germ the
already-audited principal-channel law applies without an extra selector source.
On a simple-spectrum interval,

\[
\boxed{
\frac{d}{ds}\mathcal E_{\rm fb}
=\sum_\alpha
\left(
\mathcal S_\alpha
+\mathcal C_\alpha
+\mathcal M_\alpha
\right),
}
\]

where the three literal smooth faces are:

- principal line eigenvalue stretch/compression `S_alpha`;
- residual/current content `C_alpha`;
- eigenframe mixing `M_alpha`, whose sum is the off-diagonal metric work.

At a finite entry/resolve/reselection event,

\[
\boxed{
\Delta\mathcal E_{\rm fb}
=\mathcal G_{\rm event}
+\mathcal R_L
+\mathcal R_R
+\mathcal R_Q.
}
\]

At a spectral degeneracy, replace individual-axis channels by the canonical
spectral-projector block law.  No singular eigenvector connection is introduced.

Thus a piecewise-smooth same-clock first-bad excursion has an exact hybrid ledger:

\[
\boxed{
\mathcal E(T)-\mathcal E(0)
=\sum_{I}\int_I
(\text{stretch}+\text{content}+\text{mixing})\,ds
+\sum_{e}
(\text{geometry}+\text{full pair reset})_e,
}
\]

provided the listed smooth intervals and finite selector events are the actual
physical ones being followed.

**Status: Rigorous composition of exact same-clock smooth and finite-event
identities; not a completed first-bad theorem.**

---

## 11. Physical faces that remain separate

The hybrid law above must not absorb other first-bad world-sheet faces:

1. moving quantile/shell **spatial** cut flux;
2. moving quantile/shell **time/boundary-speed** faces;
3. genuine physical exit/open-current faces;
4. connection/holonomy geometry not already represented by the local line metric;
5. actual physical refinement/reselection maps;
6. random metric--residual correlation when working after ensemble factorization.

In particular, the generic exact synthesis law `A tensor A` does **not** prove that
the programme's actual moving first-bad current refinement has already been lifted
to the reconstructed residual fiber.  That map must be written from the actual
current geometry and then audited for functoriality.

**Status: Exact physical typing / actual first-bad residual-refinement lift
Open-literal.**

---

## 12. Refined frontier

The exact selected spectral algebra now removes several false seams:

- no intrinsic first-bad selector--spectral commutator source;
- no diagonal-only spectral refinement payment;
- no positive selector-reset path-length bank;
- no canonical individual-axis matching through degeneracy;
- no need to factor random metric and residual before pathwise channelization.

What remains genuinely open is narrower:

\[
\boxed{
\begin{array}{l}
\text{actual first-bad badness/resolve predicates},\\
\text{actual moving quantile/shell outer-time law},\\
\text{actual current-to-physical-residual refinement lift},\\
\text{support locality/conditioning of the selected packet},\\
\text{uniform collapse of the selected nonnegative projector channels},\\
\text{cross-clock future-bank/ancestry identification}.
\end{array}
}
\]

The present work does not establish the first-bad physical support theorem, does not
identify a future-remaining covariance bank, and does not prove restart,
continuation, or regularity.

**Status: first-bad selected spectral lineage remains Open-literal/Open at precisely
the listed physical bridges.  No restart/continuation/regularity theorem claimed.**
