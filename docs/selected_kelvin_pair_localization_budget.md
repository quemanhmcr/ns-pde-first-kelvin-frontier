# Selected Kelvin pair-localization budget: PDE-first frontier

This is the standalone research ledger for a PDE-first, structure-first programme
on 3D Navier--Stokes.  It is **uncertified research**, not a regularity theorem.
The rule throughout is structure first: identify every term as a physical current,
transfer, exact pressure/gauge sector, stochastic quadratic variation/future
variance, Hodge flux, localization covariance, physical exit, or observer artefact
before using inequalities.

The present question is deliberately narrow:

\[
\boxed{
[M^{\rm sel}]
=2\nu\int
\sum_\mu
\left\langle \iota_{\xi_\mu}\Omega,
Z_{\lambda_*(s)}\right\rangle^2ds
}
\]

and the goal is to identify a finite **physical** reservoir for it, or prove that
no such reservoir exists at the currently constructed one-/two-ancestry level.
No continuation or restart claim is made here.

---

## 1. Standing physical objects

The normalized ancestry law is

\[
q=f\phi,
\qquad
j=w-\nu K\nabla\log f,
\qquad
\partial_s q+\nabla\cdot(qj)=0,
\]

with an orthogonal split

\[
j=j_{\rm def}+j_{\rm circ}.
\]

For a closed physical current `Z`, define the Kelvin noise coefficient

\[
a_\mu(Z)
:=\left\langle\iota_{\xi_\mu}\Omega,Z\right\rangle
\]

and the instantaneous Kelvin action

\[
\boxed{
\gamma(Z)
:=2\nu\sum_\mu a_\mu(Z)^2.
}
\]

In the constant uniform-noise frame, a frozen physical circulation coordinate has
martingale part

\[
dM_Z
=\sqrt{2\nu}\sum_\mu a_\mu(Z)\,dW^\mu,
\]

hence

\[
\boxed{d[M_Z]_s=\gamma_s(Z)\,ds.}
\]

**Classification: Exact identity.**

Finite-variation motion of the observer-selected current does not itself create
quadratic variation.  It can change which physical observable is read, but it is
not a stochastic production channel.

---

## 2. Future Kelvin variance is the exact bank for a fixed current

For a common physical terminal horizon `Theta`, let `X_Z` be the terminal
compensated Kelvin payoff and

\[
K_s(Z)=\mathbb E_sX_Z,
\qquad
V_s(Z)=\operatorname{Var}_s(X_Z).
\]

Then

\[
\boxed{
V_s(Z)
=\mathbb E_s\big([M_Z]_\Theta-[M_Z]_s\big).
}
\]

Equivalently, after matching the physical ancestry generator,

\[
\boxed{
D_sV_s(Z)=-\gamma_s(Z)
}
\]

modulo already classified physical transport/exit terms.

For two currents define

\[
C_s(Z,Z')=\operatorname{Cov}_s(X_Z,X_{Z'}),
\]

and the polarized instantaneous action

\[
\Gamma_{\rm K}(Z,Z')
=2\nu\sum_\mu a_\mu(Z)a_\mu(Z').
\]

Then

\[
\boxed{D_sC_s(Z,Z')=-\Gamma_{{\rm K},s}(Z,Z').}
\]

**Classification: Exact identity** once the full Kelvin ancestry state and its
generator have been matched literally.

The covariance kernel is therefore not auxiliary Hilbert geometry: it is future
Kelvin cross-action.

---

## 3. Selector resets: exact recharge law

For a finite selector change

\[
Z^+=Z^-+\Delta Z,
\]

quadraticity gives

\[
\boxed{
V(Z^+)-V(Z^-)
=2C(Z^-,\Delta Z)+V(\Delta Z).
}
\]

At the instantaneous-action level,

\[
\boxed{
\gamma(Z^+)-\gamma(Z^-)
=2\Gamma_{\rm K}(Z^-,\Delta Z)+\gamma(\Delta Z).
}
\]

Thus a positive deformation diagonal can never be interpreted alone.  The signed
mixed term is required by exact quadratic geometry.

**Classification: Exact identity.**

A back-and-forth observer loop can accumulate arbitrarily many positive diagonal
pieces while the mixed pieces cancel them exactly and the physical endpoint is
unchanged.  Therefore a diagonal selector-deformation sum is not a physical
finite reservoir.

**Classification: Rigorous consequence.**

Likewise, subdivision of one increment into `n` equal refinement steps changes a
diagonal quadratic sum by a factor `1/n`; cross terms restore the invariant full
quadratic action.  Hence a nonzero quadratic diagonal functional cannot be both
additive under subdivision and refinement-invariant.

**Classification: Rigorous consequence.**

---

## 4. Canonical mixed Kelvin current

Let

\[
b_\mu:=\iota_{\xi_\mu}\Omega.
\]

The first variation of `gamma` under a physical current deformation
`Z -> Z + epsilon partial T` forces the normal form

\[
\boxed{
\Pi^{\rm mix}_{\mu,{\rm K}}(Z)
=4\nu\,\langle b_\mu,Z\rangle\,b_\mu
\quad\pmod{\text{closed cochains}}.
}
\]

Indeed

\[
D\gamma(Z)[\partial T]
=\sum_\mu
\left\langle
\Pi^{\rm mix}_{\mu,{\rm K}}(Z),\partial T
\right\rangle.
\]

Since `d Omega = 0`, Cartan gives

\[
db_\mu=\mathcal L_{\xi_\mu}\Omega=:\Xi_\mu,
\]

so the same mixed transfer is

\[
\boxed{
4\nu\sum_\mu
\langle\iota_{\xi_\mu}\Omega,Z\rangle
\langle\Xi_\mu,T\rangle.
}
\]

This is a signed Kelvin--Hodge transfer, not a positive producer.

**Classification: Exact identity.**

Any existing repository object named `Pi_mu^mix` can be identified with this
Kelvin mixed current only after a literal coefficient, orientation, current-degree,
and closed/gauge-sector audit.

**Classification: Conjectural bridge.**

---

## 5. Normalized ancestry generator and exact distributed variance current

From

\[
q=f\phi,
\qquad
j=w-\nu K\nabla\log f,
\]

we obtain

\[
\partial_sq
=-\nabla\cdot(qw)
+\nu\nabla\cdot\left(\phi K\nabla\frac q\phi\right).
\]

Thus the dual backward operator is

\[
\mathscr L\psi
=w\cdot\nabla\psi
+\nu\phi^{-1}\nabla\cdot(\phi K\nabla\psi).
\]

Its carré-du-champ is

\[
\boxed{
\Gamma_{\mathscr L}(\psi,\chi)
=2\nu\nabla\psi\cdot K\nabla\chi.
}
\]

When the full state is the same state used by the Kelvin martingale, the future
variance field satisfies

\[
(\partial_s+\mathscr L)V_Z=-\gamma_Z.
\]

Combining the forward and backward equations yields the exact local balance

\[
\boxed{
\partial_s(qV_Z)
+\nabla\cdot\big(qjV_Z+\nu qK\nabla V_Z\big)
=-q\gamma_Z.
}
\]

**Classification: Exact identity** after generator compatibility; compatibility
itself remains a literal bridge if the stored `q` state is reduced relative to
the full stochastic Kelvin state.

On a periodic domain,

\[
\boxed{
\frac d{ds}\int qV_Z
=-\int q\gamma_Z.
}
\]

Hence the distributed Kelvin action already has a finite future-variance bank.
The unresolved problem is not distributed payment but localization onto the
moving first-bad germ.

---

## 6. Fisher/osmotic bank is a different bank

Under the usual reference-measure invariance assumptions, the same ancestry law
has the relative-entropy depletion

\[
\frac d{ds}\int q\log f
=-\nu\int q\,\nabla\log f\cdot K\nabla\log f.
\]

The positive Fisher/osmotic bulk therefore has conjugate potential `log f`, while
Kelvin future variance has conjugate potential `V_Z`.

Their mixed physical transfer is

\[
\boxed{
-\nu q\,\nabla\log f\cdot K\nabla V_Z,
}
\]

a signed cross-carré-du-champ current.

An exact periodic shear calibration can have `f == 1`, hence zero Fisher bulk,
while Kelvin quadratic variation is nonzero.  Therefore Fisher/osmotic action is
not universally the Kelvin bank.

**Classification: Rigorous consequence.**

---

## 7. Strong Hodge split: what it would actually imply

A mere pointwise statement `j_def perp j_circ` is not enough.  A strong weighted
Hodge split would require orthogonality of `j_circ` against the full deformation
gradient sector, equivalently

\[
\boxed{
\nabla\cdot(qj_{\rm circ})=0
}
\]

on periodic/no-flux geometry.

Then

\[
\boxed{
\partial_sq+\nabla\cdot(qj_{\rm def})=0,
\qquad
\nabla\cdot(qj_{\rm circ})=0.
}
\]

Thus

\[
\mathbf C_{\rm circ}:=(0,qj_{\rm circ})
\]

is a closed occupation current in spacetime.

For a functorial localization map to germ space and a globally single-valued
future covariance potential,

\[
\boxed{
\langle d_{\rm g}V,\Lambda_\#(qj_{\rm circ})\rangle=0
}
\]

globally.  Localizing to a chamber turns this zero into a boundary-crossing
covariance flux.

Thus first-order circulation current transports covariance but cannot count
positive crossing multiplicity.

**Classification: Exact identity in the strong-Hodge/functorial case.**

If the active CK projection breaks boundary/push-forward commutation, the residual
appears precisely as the pair/current version of the unresolved
`S^int / Z_irr` sector.  It must not be set to zero before literal verification.

---

## 8. Why first-order circulation activity does not close the bank

A natural positive traffic action is

\[
qj_{\rm circ}\cdot K^{-1}j_{\rm circ}.
\]

This can be physically meaningful, but closedness of `q j_circ` supplies no time
evolution law for it.  A stationary or cyclic occupation current can carry
positive traffic indefinitely while its one-time density returns to the same
state.

Therefore a positive multiplicity cost cannot be an endpoint state function on
one-current space unless an additional physical evolution/depletion law exists.

**Classification: Rigorous consequence.**

A natural coexact Hodge Green reservoir can be defined when the harmonic sector
has been removed, but it becomes a true finite bank only if `q j_circ` obeys its
own diffusive/Hodge evolution equation.  The normalized one-ancestry continuity
law does not provide such an equation.

**Classification: Conjectural bridge.**

Harmonic/Galilean current must be quotiented as frame/connection geometry or
retained as a separate physical finite-dimensional sector; it cannot simply be
charged as Kelvin production.

---

## 9. Same-ancestor pair process: the canonical second-order object

For conditional variance, two replicas must start from the **same ancestor** and
use independent future noises after the branch time.  If `P_{s,t}` is the full
ancestry transition kernel, the two-replica law is

\[
\boxed{
P^{(2)}_{s,t}(y;dy_1,dy_2)
=P_{s,t}(y,dy_1)P_{s,t}(y,dy_2).
}
\]

Hence the replica generator is

\[
\boxed{
\mathscr L^{(1)}+\mathscr L^{(2)},
}
\]

with no common-noise cross term between the variance replicas.  The common-noise
spatial coupling belongs inside each replica's full stochastic flow.

For terminal payoff `F_Z`,

\[
\boxed{
V_Z(s,y)
=\frac12\mathbb E_{s,y}
\big(F_Z^{(1)}-F_Z^{(2)}\big)^2.
}
\]

Weighting the common ancestor by `q_s` gives the canonical same-ancestor pair
occupation measure

\[
\widehat Q_s(dy,dy_1,dy_2)
=q_s(dy)P_{s,\Theta}(y,dy_1)P_{s,\Theta}(y,dy_2).
\]

**Classification: Exact probabilistic identity.**

---

## 10. The actual pair source is diagonal viscous branching, not drift traffic

Write the full diffusion generator abstractly as

\[
\mathscr L
=\mathscr B+\nu\sum_\mu\mathscr D_\mu^2.
\]

If `U(y1,y2)` is a pair test and `U^Delta(y)=U(y,y)`, then

\[
\boxed{
\mathscr L(U^\Delta)
-(\mathscr L^{(1)}+\mathscr L^{(2)})U\big|_\Delta
=2\nu\sum_\mu
\mathscr D_\mu^{(1)}\mathscr D_\mu^{(2)}U\big|_\Delta.
}
\]

All first-order drift terms cancel from this branch-time difference.  The
canonical branching tensor is therefore

\[
\boxed{
\mathbb T^{\rm br}
=2\nu qK\,\delta_\Delta
}
\]

in flat diffusion coordinates, with the appropriate covariant replacement in a
variable frame.

This tensor is positive-semidefinite; its double divergence is the signed pair
probability-current source.  Pairing it with the squared-difference future Kelvin
observable yields precisely the positive Kelvin carré-du-champ.

**Classification: Exact identity.**

Consequently

\[
qj_{\rm circ}\otimes j_{\rm circ}
\]

is a deterministic traffic tensor, **not** the canonical Kelvin branching source.

**Classification: Rigorous consequence.**

---

## 11. Conductance is not stored covariance

The total mass of the physical branching conductance `2 nu q K` may remain fixed,
while a selected Kelvin observable has arbitrarily concentrated derivative in
noise directions.  The payment is the contraction

\[
q\gamma_Z
=2\nu q\sum_\mu(\mathscr D_\mu m_Z)^2,
\]

not the mass of `2 nu q K` alone.

Thus

\[
\boxed{
\text{branching tensor} = \text{conductance},
\qquad
V_Z = \text{stored future covariance},
\qquad
q\gamma_Z = \text{instantaneous power/payment}.
}
\]

**Classification: Rigorous consequence.**

---

## 12. Exact smooth periodic calibration excluding several false reservoirs

Consider the exact periodic Navier--Stokes shear family

\[
u_N(y,t)
=\left(
\frac1{\sqrt N}\sum_{m=1}^N
 e^{-\nu k_m^2t}\cos(k_my),0,0
\right),
\qquad k_m=2m-1.
\]

Because the field depends only on `y` and has only an `x` component,

\[
(u_N\cdot\nabla)u_N=0,
\]

so this is an exact smooth 3D periodic Navier--Stokes solution with constant
pressure.

Take uniform ancestry density and the time scale

\[
T_N=\frac c{\nu N^2}.
\]

For a suitable fixed rectangular physical circulation `Z_0`, the terminal Kelvin
payoff has the exact Gaussian-translation form

\[
X_N
=\frac{2L}{\sqrt N}
\sum_{m=1}^N
\cos\left(k_m\frac{\sqrt{2c}}N Z\right),
\qquad Z\sim N(0,1).
\]

The associated Riemann sum converges to a nonconstant limiting function, hence

\[
\boxed{
\operatorname{Var}(X_N)=\Theta(N).
}
\]

By the Kelvin--Doob identity,

\[
\boxed{
\mathbb E[M_{Z_0}]_{T_N}=\Theta(N).
}
\]

Meanwhile, for the strong-Hodge flat calibration `j_circ = u_N`, the integrated
drift-square circulation traffic satisfies

\[
\int_0^{T_N}\int q|j_{\rm circ}|^2=O(N^{-2}),
\]

and the natural coexact Hodge Green bank is `O(N^{-1})`; the total branching-tensor
mass and normalized distributed ancestry mass remain `O(1)`.

Therefore none of the following, taken alone, is a universal selected-Kelvin
reservoir:

- one-time ancestry mass `q`;
- first-order closed occupation current `q j_circ`;
- drift-square traffic `q j_circ tensor j_circ`;
- the natural coexact Hodge filling bank;
- total mass of the viscous branching tensor `2 nu q K`;
- a normalized distributed Kelvin-variance average.

**Classification: Rigorous consequence from an exact NS calibration.**

This is an elimination result, not a claim excluding every possible new physical
structure.

---

## 13. The remaining obstruction is pair localization, not pair existence

The canonical pair covariance cochain already exists:

\[
\mathbb K_s
=\mathbb E_s
[(\beta-\bar\beta_s)\boxtimes(\beta-\bar\beta_s)],
\]

where `beta` is the random transported momentum cochain modulo exact forms.
For every closed physical current,

\[
V_s(Z)=\langle\mathbb K_s,Z\boxtimes Z\rangle.
\]

A physical distributed germ measure `eta_s` defines

\[
\Pi_s^{\rm dist}
=\int Z_\lambda\boxtimes Z_\lambda\,\eta_s(d\lambda),
\]

while the first-bad selector reads

\[
\Pi_s^{\rm sel}
=Z_{\lambda_*(s)}\boxtimes Z_{\lambda_*(s)}.
\]

The unresolved object is therefore exactly

\[
\boxed{
\Pi_s^{\rm sel}-\Pi_s^{\rm dist}.
}
\]

The same-ancestor pair stochastic process does not make this difference disappear.
It only supplies the correct physical meaning of the covariance cochain being
localized.

**Classification: Rigorous consequence.**

---

## 14. Required pair-localization current identity

The surviving route is a literal pair-current decomposition of the form

\[
\boxed{
\Pi^{\rm sel}-\Pi^{\rm dist}
=\partial_{\rm pair}\mathscr W_{\rm loc}^{(2)}
+\Pi_{\rm quant}^{(2)}
+\Pi_{\rm shell}^{(2)}
+\Pi_{\rm ref}^{(2)}
+\Pi_{\rm exit}^{(2)}
+\Pi_{\rm irr}^{(2)}.
}
\]

Pairing with `mathbb K` gives an exact selector-bank decomposition if this chain
identity is literally true:

\[
\begin{aligned}
V(\lambda_*)-R_{\rm dist}
={}&
\langle d_{\rm pair}\mathbb K,
\mathscr W_{\rm loc}^{(2)}\rangle
\\
&+\langle\mathbb K,
\Pi_{\rm quant}^{(2)}+
\Pi_{\rm shell}^{(2)}+
\Pi_{\rm ref}^{(2)}+
\Pi_{\rm exit}^{(2)}\rangle
\\
&+\langle\mathbb K,\Pi_{\rm irr}^{(2)}\rangle.
\end{aligned}
\]

**Classification: Conjectural bridge until the literal active chain is built and
checked line by line.**

The target is not an inequality.  It is a physical pair-current Stokes theorem in
which internal seams/refinements cancel, quantile/shell terms are tracked physical
covariance transfers, physical exit remains explicit, and only the irreducible
non-functorial sector can obstruct closure.

---

## 15. Pillar-II dependence

No statement in this note assumes

\[
S^{\rm int}=0
\quad\Longleftrightarrow\quad
Z_{\rm irr}=0
\]

has been literally verified.

At pair level, a non-functorial active CK/refinement block produces

\[
\Pi_{\rm irr}^{(2)}
=(R\otimes R)_*\Pi-\Pi_{\rm allowed}^{(2)},
\]

and the future-covariance budget sees it directly through

\[
\langle\mathbb K,\Pi_{\rm irr}^{(2)}\rangle.
\]

This is the correct slot for an unresolved content defect.  It is not a physical
producer and must not be silently discarded.

---

## 16. Current no-go ledger

At the present structural level, do **not** infer a finite selected-Kelvin budget
from any of the following alone:

1. positivity of `A_def`, `A_circ`, or `alpha^2 tau`;
2. Fisher/osmotic entropy depletion;
3. a first-order closed Hodge current;
4. drift-square circulation traffic;
5. a natural Hodge Green filling bank;
6. total mass of the same-ancestor branching tensor;
7. normalized `q`-averaged Kelvin variance;
8. homology equivalence of selector loops;
9. observer hysteresis by itself;
10. a diagonal refinement sum without cross-covariances.

Each item is physically meaningful, but none is the missing universal selector
bank at this level.

**Classification: Rigorous consequence of the exact identities/calibrations above.**

---

## 17. Present frontier

The distributed problem is solved structurally:

\[
\boxed{
\text{future covariance bank}
\longrightarrow
\text{positive distributed Kelvin payment}.
}
\]

The remaining problem is strictly localization:

\[
\boxed{
\text{distributed pair covariance}
\longrightarrow
\text{migrating first-bad selector atom}.
}
\]

The next literal calculation must lift the actual first-bad-germ chain through one
complete hysteresis excursion to pair-current level, including

- entry/first trigger;
- frozen coordinate interval;
- anchor/orientation motion;
- quantile motion;
- shell change;
- refinement;
- resolve/reset;
- physical exit;
- all active CK seams.

For every face/seam, classify it as exactly one of

\[
\boxed{
\text{pair-boundary cancellation},
\quad
\text{physical covariance transfer},
\quad
\text{physical exit},
\quad
S^{\rm int}/Z_{\rm irr}\text{ defect}.
}
\]

If the pair world-sheet closes after the literal Pillar-II audit, then selected
Kelvin q.v. inherits a finite physical pair bank.  If a non-boundary selector
component remains, the present exact NS calibrations show that no averaged
one-/two-ancestry reservoir already on the table can absorb it merely by stronger
estimates.

**Classification: Conjectural bridge.**

---

## 18. Regularity status

There is no continuation theorem or 3D Navier--Stokes regularity proof at this
stage.  The safe restart target remains separate.  The present result is a
structural localization audit: the missing resource, if any, has been narrowed to
a **physical pair-localization capacity/current** for the migrating first-bad germ,
plus the unresolved literal Pillar-II defect sector.
