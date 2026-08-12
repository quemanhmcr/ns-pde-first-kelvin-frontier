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

## 2. Conditional Kelvin variance is an exact bank on one compatible Markov clock

Let `sigma` denote the clock of a **single specified Markov state/filtration**, and
let `Theta_sigma` be a terminal horizon in that same clock.  For a fixed current
observable `Z`, let `X_Z` be the terminal compensated payoff and

\[
K_\sigma(Z)=\mathbb E_\sigma X_Z,
\qquad
V_\sigma(Z)=\operatorname{Var}_\sigma(X_Z).
\]

For the martingale `M_Z=E[X_Z|F_sigma]`,

\[
\boxed{
V_\sigma(Z)
=\mathbb E_\sigma\big([M_Z]_{\Theta_\sigma}-[M_Z]_\sigma\big).
}
\]

and, on that same compatible state/clock,

\[
\boxed{
D_\sigma V_\sigma(Z)=-\gamma_\sigma(Z)
}
\]

modulo already classified physical transport/exit terms.

This is an exact conditional-variance theorem; it is **not yet** a theorem saying
that `sigma` is contemporaneous physical first-bad time.  The one-mode NS shear
separates the clocks exactly: `(partial_t+nu partial_a^2)u` is nonzero for forward
Brownian physical-time conditioning, while `(partial_t-nu partial_a^2)u=0` in the
causal backward-Kelvin orientation.  Therefore a physical first-bad telescope needs
an explicit two-clock/state lift before this bank can be differentiated along the
physical selector path.

For two currents on the same Markov clock define

\[
C_\sigma(Z,Z')=\operatorname{Cov}_\sigma(X_Z,X_{Z'}),
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

## 10. The full-state continuous pair source is diagonal viscous branching, not drift traffic

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

is a deterministic traffic tensor, **not** the canonical full-state viscous Kelvin branching source.

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

Here the historical symbols `Pi_quant^(2)` and `Pi_shell^(2)` are only aggregate
placeholders.  The later clock/cut audit splits each into separate spatial and
moving-time faces.  No completed physical identity may use the aggregate symbol
unless both pieces have been instantiated.

**Classification: Conjectural bridge at this historical stage; later algebraic
factorization is exact but literal moving-cut realization remains open-literal.**

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

In the initial repository state, the pair-level placeholder was written

\[
\Pi_{\rm irr}^{(2)}
=(R\otimes R)_*\Pi-\Pi_{\rm allowed}^{(2)}.
\]

The subsequent literal audits now classify this **content-defect realization**.
Full physical refinement and every linear cycle-preserving CK map use the full
tensor-square image, so this difference is exactly zero.  If
`Pi_allowed^(2)` deletes cross-child, cross-shell, or cross-cycle blocks, the
remainder is omitted physical covariance and therefore an observer/analysis
projection defect.  If the underlying one-current operation breaks closedness,
exact pressure gauge detects a physical boundary/interface/exit.

Thus this original pair-content placeholder is no longer an unclassified physical
producer.  It remains illegitimate to identify that conclusion with the global
statement `S^int=0 iff Z_irr=0`, because `S^int` and any independently intended
`Z_irr` have no separate line-by-line definition in the repository.

**Classification: Rigorous consequence for the original pair-content-defect
realization; global Pillar-II equivalence remains a Conjectural bridge.**

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

The distributed problem remains solved structurally:

\[
\boxed{
\text{future covariance bank}
\longrightarrow
\text{positive distributed Kelvin payment}.
}
\]

The pair-localization frontier has now narrowed one level further.  For any literal
one-current active stage `(F_1,F_0)`, define

\[
C_F=B_{\rm out}F_1-F_0B_{\rm in},
\qquad
G_F=\dot F+T_{\rm out}F-FT_{\rm in}.
\]

With the full tensor-square pair lift, CI now audits the exact identities

\[
\boxed{
C_F^{(2)}=
\begin{bmatrix}
C_F\otimes F_1\\
-F_1\otimes C_F
\end{bmatrix},
\qquad
G_F^{(2)}=G_F\otimes F+F\otimes G_F.
}
\]

**Classification: Exact identities.**

Thus there is no autonomous pair-only non-functorial producer once full pair
content is retained.  Cross-child and cross-shell covariance are physical content;
quantile/shell **spatial** interfaces and physical exit remain explicit two-face
currents; anchor/frame terms are connection geometry; reset is exact covariance
revaluation.  For moving quantile/shell maps, the `dot Q` / `dot H_shell`
boundary-speed faces are separate physical transport terms through the exact
`G_F` defect.  Only a one-current remainder left after **all spatial and moving-time
faces** are subtracted can feed any literal `S^int / Z_irr` sector.

**Classification: Rigorous consequence of exact pair factorization; literal
first-bad moving-cut speed laws remain open-literal.**

The completed hysteresis composition also has an exact seam product rule:

\[
\boxed{
C(F_n\cdots F_1)
=
\sum_k F_{0,>k}\,C(F_k)\,F_{1,<k}.
}
\]

A finite-cell current audit now instantiates the chronological stages
freeze/quantile/anchor-orientation/shell/refinement/resolve-reset/physical-exit and
checks this identity exactly.  The new exact NS active-mixture calibration also
forces full pair covariance: in the odd shear, `Z_h=h Z_0+(1-h)Z_pi` has
`V(Z_h)=(2h-1)^2V(Z_0)`, so the true bank vanishes at `h=1/2` while a diagonal-only
active projection remains positive.

**Classification: Exact current algebra plus rigorous consequence from an exact
Navier--Stokes calibration.**

The later cycle-typing audit removes the need to postulate an arbitrary ambient
active-chain map.  The intrinsic selector is `P_fb=K M_fb` with `BK=0`, and its
boundary/transport remainder closes after named interface/connection/reset terms.
The subsequent CK admissibility audit goes further: any additional linear or
differentiable operation that is genuinely internal to Kelvin circulation must map
closed currents to closed currents.  Such an operation has zero intrinsic physical
boundary; linear maps factor as cycle-coordinate transformations and use the full
tensor-square pair image, while differentiable nonlinear maps have cycle-valued
tangents and the ordinary two-factor pair Leibniz derivative.

If an operation instead sends a closed Kelvin cycle to an open current, Stokes makes
exact pressure observable through its boundary, so that term must be exposed as a
physical interface/open-current/exit contribution rather than placed in an
irreducible internal slot.

What remains open is therefore a literal-definition problem: `S^int` itself has
never been written line by line, nor has any separate object been supplied whose
physical type escapes the above classification.  No zero statement about the
global `S^int / Z_irr` equivalence is inferred from absence of such a definition.

**Classification: Rigorous consequence for the specified Kelvin operation classes;
Conjectural bridge only for the still-undefined global Pillar-II objects.**

---

## 18. Regularity status

There is no continuation theorem or 3D Navier--Stokes regularity proof at this
stage.  The safe restart target remains open and is sharpened below by the
vorticity/Kelvin microframe audit.  The present result is a
structural localization audit: the missing resource, if any, has been narrowed to
a **physical pair-localization capacity/current** for the migrating first-bad germ,
plus the unresolved literal Pillar-II defect sector.


---

## 19. Cycle-typed first-bad selector removes the intrinsic active residual

A type audit of the actual selected Kelvin observable changes the active-map
question.  The observable is evaluated on closed physical currents.  Write the
closed germ library as

\[
K_s:G\to C_1^{\rm phys},
\qquad B_xK_s=0,
\]

and the first-bad support projector in germ space as `M_fb(s)`.  Literal code
semantics are hysteretic: `bad_flags` and `resolved` are Boolean inputs, the active
index is frozen while unresolved, and re-selection is a finite event.  Hence `M_fb`
is distinct from the continuously moving quantile/shell maps `Q_s/H_s`.  The
Navier--Stokes badness functional and resolve predicate generating those Boolean
events are not yet defined line by line.  Then

\[
\boxed{P_{\rm fb}=K_sM_{\rm fb}}
\]

and therefore

\[
\boxed{B_xP_{\rm fb}=0,
\qquad
\partial_{x,\rm pair}(P_{\rm fb}\otimes P_{\rm fb})=0.}
\]

**Classification: Exact identity.**

This shows that the global ambient expression `B P_active,1-P_active,0 B` is not an
intrinsic selector observable unless the active selector has first been extended
off the physical cycle library.  Such extensions are nonunique.  CI gives an exact
finite-chain witness with a nonzero global ambient commutator whose restriction to
the physical cycle and pair cycle is nevertheless zero.

**Classification: Rigorous consequence: an off-cycle ambient commutator cannot by
itself be charged to `Z_irr`.**

The transport side also factorizes exactly.  For physical transport `T_x`, germ
connection `A_g`, and `P_fb=KM`,

\[
G_{P_{\rm fb}}
=G_KM+KG_M,
\]

where

\[
G_K=\dot K+T_xK-KA_g,
\qquad
G_M=\dot M+A_gM-MA_g.
\]

For a diagonal support mask,

\[
\boxed{(A_gM-MA_g)_{ij}=A_{ij}(\chi_j-\chi_i),}
\]

so the support term is exactly germ-interface transport.  On hysteresis jumps the
finite tensor-square jump is the exact reset covariance identity.  Thus, after
quantile/shell localization is interpreted as the **full spacetime operation** --
including fixed-time cut currents and moving boundary-speed faces -- together with
connection geometry, refinement, physical exit, and finite reset, the intrinsic
cycle-typed selector has no additional irreducible sector:

\[
\boxed{
C_{\rm irr}^{\rm selector}=0,
\qquad
G_{\rm irr}^{\rm selector}=0
\quad\text{after all named spatial/time faces are retained}.
}
\]

The algebraic statement is exact, but the actual first-bad `dot Q_s` and moving-shell
speed data are not yet defined line by line.  Therefore a completed physical
first-bad excursion is not certified until those time faces are instantiated.

**Classification: Rigorous conditional structural consequence of exact cycle typing,
cut-current/transport algebra, and finite reset algebra; moving-cut realization
open-literal.**

Accordingly, for the cycle-typed selector sector the **full spacetime** pair-localization
ledger must be

\[
\boxed{
\begin{aligned}
\Pi^{\rm sel}-\Pi^{\rm dist}
={}&\partial_{\rm pair}\mathscr W_{\rm loc}^{(2)}
+\Pi_{\rm quant,space}^{(2)}+\Pi_{\rm quant,time}^{(2)}\\
&+\Pi_{\rm shell,space}^{(2)}+\Pi_{\rm shell,time}^{(2)}
+\Pi_{\rm exit}^{(2)}
+\Pi_{\rm conn}^{(2)}
+\Pi_{\rm reset}^{(2)}.
\end{aligned}
}
\]

Pairing with the future Kelvin covariance cochain gives

\[
\boxed{
\begin{aligned}
V(\lambda_*)-R_{\rm dist}
={}&
\langle d_{\rm pair}\mathbb K,
        \mathscr W_{\rm loc}^{(2)}\rangle\\
&+\langle\mathbb K,
  \Pi_{\rm quant,space}^{(2)}+\Pi_{\rm quant,time}^{(2)}
 +\Pi_{\rm shell,space}^{(2)}+\Pi_{\rm shell,time}^{(2)}
 +\Pi_{\rm exit}^{(2)}\rangle\\
&+\mathcal H_{\rm conn}+\mathcal R_{\rm reset}.
\end{aligned}
}
\]

**Classification: Exact algebraic spacetime-ledger template for the cycle-typed
selector sector.  Generator compatibility and the literal moving quantile/shell
time-face realization remain open-literal before this becomes a completed physical
first-bad identity.**

This does not silently set the programme-wide `S^int / Z_irr` sector to zero.  The
repository still has no literal line-by-line definition of `S^int`, and it has no
additional ambient CK/Hodge operator beyond the closed-cycle realization `K` whose
commutator could be audited.  If such an extra operator is intended, it must be
written explicitly; any residual then belongs to that operator, not to first-bad
support selection and not to pair lifting.

**Classification: Conjectural bridge for any additional CK/Hodge operator and for
the global Pillar-II equivalence.**

---

## 20. If the extra CK/Hodge map is a closed-range projector, its motion is pure exchange

Suppose a future literal CK/Hodge operator is an idempotent projector `H`,
`H^2=H`, with `Ran H subset ker B_x`.  Then `B_xH=0` exactly.  For its covariant
derivative `G=D_sH`, differentiated idempotency gives

\[
G H+H G=G,\qquad H G H=0,\qquad (I-H)G(I-H)=0.
\]

Thus `G=H G(I-H)+(I-H)G H`: projector motion is signed range/complement exchange,
not an internal production channel.  At pair level

\[
D_s(H\otimes H)=G\otimes H+H\otimes G,
\]

with zero active-pair internal sandwich.  Pure frame motion is removable by the
co-moving connection.

**Classification: Exact identity under the stated projector hypotheses.**

This does not identify the programme's still-undefined `S^int` with projector
motion and therefore does not prove the global Pillar-II equivalence.  A literal
non-projector CK operation, if intended, remains to be written and audited.

**Classification: Conjectural bridge for the identification with any actual extra
CK/Hodge operator and with `S^int`.**


---

## 21. Kelvin admissibility dichotomy removes the non-projector loophole

The projector audit used `H^2=H`, but the physical Kelvin type gives a stronger
criterion.  Let `K` be the admissible closed-cycle library, `BK=0`, and let an
additional operation `H` be visible only through `Y=HK`.  An internal Kelvin
operation must obey

\[
\boxed{BHK=0.}
\]

Idempotency is unnecessary.  If `HK=KL` for a cycle-coordinate map `L`, then

\[
\boxed{
(HK)^{(2)}=(KL)^{(2)}=K^{(2)}L^{(2)},
}
\]

so the original pair content defect vanishes when the full physical pair image is
kept.  CI audits an explicit `H` with `H^2 != H` but `BHK=0` and zero pair
boundary.

For any differentiable nonlinear cycle-valued map `Phi`,

\[
B\Phi(a)=0
\quad\Longrightarrow\quad
\boxed{B D\Phi_a=0},
\]

and along a path

\[
\boxed{
\frac d{ds}(Z\otimes Z)=\dot Z\otimes Z+Z\otimes\dot Z,
\qquad
\partial_{\rm pair}\frac d{ds}(Z\otimes Z)=0.
}
\]

Conversely, if an operation breaks closedness, Stokes gives

\[
\langle dp,HZ\rangle=\langle p,BHZ\rangle.
\]

Thus exact pressure/gauge becomes sensitive to the new boundary.  In the exact
3D ABC/Beltrami solution the pressure work around the closed `x` cycle is zero,
while on the open half-cycle `y=pi/2,z=0`, `0<=x<=pi`, it is exactly

\[
\boxed{2e^{-2\nu t}}.
\]

A cycle-breaking CK operation is therefore a physical cut/interface/exit (or a
change away from the Kelvin observable), not an internal producer.

**Classification: Exact identities plus rigorous consequence from an exact 3D
Navier--Stokes pressure calibration.**

The current construction has therefore exhausted the original `Pi_irr^(2)`
content-defect mechanism: full admissible pair content gives zero; truncation is an
observer projection; cycle breaking is a physical boundary; continuous
cycle-preserving motion is covariance/connection work; finite discontinuity is
reset revaluation.  This does not define `S^int` and hence does not prove the
global Pillar-II equivalence.

**Classification: Rigorous consequence for the original content-defect mechanism;
Conjectural bridge for any independently intended, still-undefined `S^int` or
`Z_irr`.**

No continuation/restart conclusion follows here.

---

## 22. If a CK coordinate is stochastic, the extra pair term is carré-du-champ

The present first-bad observer is finite variation between resets, so it creates no
continuous observer q.v.  For completeness, let a future CK coordinate be
`Z=Phi(S)` with `dS=b ds+sigma dW` and assume it remains a closed Kelvin current,
`B Phi=0`.  Then differentiated closedness and Itô give closed drift/diffusion
currents and

\[
\boxed{
\mathcal Q_\Phi^{(2)}
=\sum_\mu \Psi_\mu\otimes\Psi_\mu,
\qquad
\Psi_\mu=D\Phi\,\sigma_\mu.
}
\]

This is the exact second-order term in `d(Z tensor Z)`, with

\[
\boxed{\partial_{\rm pair}\mathcal Q_\Phi^{(2)}=0.}
\]

It is martingale quadratic variation/carré-du-champ and therefore already has a
physical category and future-variance conjugate bank.  It is not an internal chain
seam.  When `sigma=0`, as in the current finite-variation selector, this extra pair
source vanishes exactly.

The one-mode Kelvin calibration verifies symbolically that Brownian anchor
covariance `2 nu` gives q.v. density `2 nu (partial_a m)^2`, exactly the Kelvin
carré-du-champ.

**Classification: Exact identities; exact Kelvin stochastic calibration.**

The full-state continuous ancestry source `2 nu q K delta_Delta` has the same diagonal
carré-du-champ form, but a coefficient-level identification with a future stochastic
CK coordinate requires its literal state map and is therefore a Conjectural bridge.

No `S^int` conclusion is inferred without a line-by-line definition.


---

## 23. Vorticity/Kelvin microframe identifies the restart-relevant density

The restart question can now be tied directly to the local Navier--Stokes
vorticity equation.  In a constant orthonormal noise frame, for a small disk loop
`Z_r=partial Sigma_r(x,n)`, Stokes gives

\[
\frac{\gamma(Z_r)}{A_r^2}
\longrightarrow
2\nu |(\nabla\omega)^Tn|^2.
\]

For any orthonormal triple of normals,

\[
\boxed{
\frac12\sum_{j=1}^3\gamma_{\rm dens}(n_j)
=\nu|\nabla\omega|^2.
}
\]

Thus an orientation-complete Kelvin microframe is exactly the bulk viscous
enstrophy-dissipation channel.  A single loop may be blind; the exact periodic
shear calibration has two coordinate normals with zero Kelvin density even though
`grad omega` is nonzero.

The local enstrophy equation is

\[
(\partial_t+u\cdot\nabla)e
=\omega\cdot S\omega+\nu\Delta e-\nu|\nabla\omega|^2,
\qquad e=|\omega|^2/2.
\]

For a material germ volume `D_t`, incompressibility and Reynolds transport give

\[
\boxed{
\frac d{dt}\int_{D_t}e
=\int_{D_t}\omega\cdot S\omega
-\frac12\sum_j\int_{D_t}\gamma_{\rm dens}(n_j)
+\nu\int_{\partial D_t}\nabla e\cdot n.
}
\]

This separates the restart ledger into literal vortex-stretching production,
Kelvin microframe bulk dissipation, and signed spatial/Hodge boundary flux.
Pressure is absent by curl; advection is absent only because the germ is material.

Raw small-loop action scales as `A_r^2`.  Therefore the local restart density is
`gamma_hat=gamma/A^2`, with covariance bank `V_hat=V/A^2`.  If area moves
continuously, the exact bank chain rule is

\[
\boxed{
\dot{\widehat V}
=-\widehat\gamma
+\frac{W_{\rm cov}}{A^2}
-2\frac{\dot A}{A}\widehat V.
}
\]

The last term is signed dilation/zoom work and belongs to shell/refinement geometry.
It is not stochastic production.

At a spatial local maximum of enstrophy, positive material growth requires

\[
\boxed{\omega\cdot S\omega>\nu|\nabla\omega|^2,}
\]

but this is only a necessary local gate, not a first-bad threshold or continuation
criterion.

**Classification: Exact identities and rigorous structural consequences.**

This section identifies the correct local density but not yet the invariant packet
capacity.  The subsequent orientation-complete packet audit shows that passive
rotation/dilation/shear cancel exactly in the GL(3)-normalized contraction, while
material metric deformation is the vortex-stretching channel itself.  The living
restart-capacity problem is therefore the local future-covariance tensor/remainder
law plus signed material metric and physical boundary/exit work.

**Classification: Conjectural bridge for restart capacity.  No continuation or
regularity conclusion.**

See `docs/vorticity_kelvin_restart_audit.md` and
`docs/orientation_complete_restart_packet.md`.



---

## 24. Orientation-complete first-bad packet and GL(3)-normalized capacity

The restart extension of one selected germ carries three closed loop orientations.
The first-bad support selector therefore lifts as

\[
\boxed{M_{\rm fb}^{\rm mf}=M_{\rm fb}\otimes I_3.}
\]

With a closed packet library `B_x K_mf=0`, both the selected one-current packet and
its full pair lift remain physically closed.  The packet q.v. is the full matrix

\[
\boxed{
\Gamma_{\rm mf}=2\nu N^T(\nabla\omega)(\nabla\omega)^TN,
}
\]

not a diagonal list.  Exact ABC flow at `(pi/4,pi/4,pi/4)` has negative
cross-orientation entries, so these terms are physical even in the ordinary
coordinate frame.

For a general material area frame `H`, define

\[
M_H=(H^TH)^{-1},
\qquad
\boxed{\mathcal B(C_H,H)=\frac12\operatorname{tr}(C_HM_H).}
\]

Then `B` is exactly invariant under any invertible packet reparameterization
`H->HL`, `C_H->L^T C_H L`.  Rotation, anisotropic dilation and packet shear are one
connection geometry; they do not create a scalar capacity when full covariance and
the packet metric are retained.

If a local covariance tensor exists so that

\[
C_H=H^T\mathcal C H,
\]

then

\[
\boxed{\mathcal B=\frac12\operatorname{tr}\mathcal C}
\]

independently of packet geometry.  Under `H_r=r^2H_0`, a non-tensorial raw remainder
`R_r=r^pR_0` contributes exactly `r^(p-4)` after metric normalization.  Thus the
scale obstruction is the metric-amplified **failure of local area-squared
tensoriality**, not the number of refinements or a positive zoom cost.

The continuous exact packet bank law is

\[
\boxed{
\dot{\mathcal B}
=-\frac12\operatorname{tr}(\Gamma_HM_H)
+\frac12\operatorname{tr}(W_HM_H)
+\frac12\operatorname{tr}(C_H\dot M_H).
}
\]

Finite jumps split into signed covariance-reset and metric-revaluation faces.  A
passive `GL(3)` jump can make both faces nonzero while their sum is exactly zero.

**Classification: Exact identities.**

A subsequent double-Stokes audit proves a fixed-state local **future** covariance
tensor under conditional mean-square continuity of the random terminal vorticity
two-form.  What is not established is a **singular-time-uniform** diagonal
trace/remainder law, nor the programme-specific descent of the full stochastic
Kelvin generator to the reduced first-bad `(x,H)` state.

**Classification: Rigorous conditional fixed-state theorem; Conjectural/open-literal
bridge for uniform singular-time control and generator descent.**

---

## 25. Material flux coordinates move vortex stretching into the packet metric

For a material area frame, Nanson gives

\[
D_tH=-(\nabla u)^TH.
\]

Define the infinitesimal vorticity-flux coordinates

\[
\Phi=H^T\omega.
\]

Combining Nanson with the exact NS vorticity equation gives

\[
\boxed{D_t\Phi=\nu H^T\Delta\omega.}
\]

The nonlinear stretching term cancels exactly from the material flux equation.  It
reappears in the metric converting flux coordinates to physical vorticity:

\[
|\omega|^2=\Phi^TM_H\Phi,
\qquad
\boxed{
\frac12\Phi^T\dot M_H\Phi=\omega\cdot S\omega.
}
\]

For a flux covariance `C_Phi`,

\[
\boxed{
\frac12\operatorname{tr}(C_\Phi\dot M_H)
=\operatorname{tr}(S\Sigma_\omega),
\qquad
\Sigma_\omega=H^{-T}C_\Phi H^{-1}.
}
\]

Incompressibility preserves `det M_H` exactly, so material stretching changes
packet anisotropy rather than collapsing material volume.

The exact amplitude-scaled ABC family gives another no-go.  At `(0,0,0)`,

\[
\omega\cdot S\omega=3A^3e^{-3\nu t},
\qquad
\frac12\operatorname{tr}\Gamma_{\rm mf}=3\nu A^2e^{-2\nu t},
\]

hence their ratio is `A exp(-nu t)/nu`, unbounded with amplitude at fixed `nu`.
Instantaneous Kelvin bulk payment alone is therefore not a universal stretching
bank.

The restart-capacity target is now the coupled **future flux covariance + material
packet metric + non-tensorial scale remainder + physical boundary/exit** ledger.
No continuation theorem follows until that coupled object is controlled up to a
candidate singular time.

**Classification: Exact identities, exact 3D NS no-go calibration, and
Conjectural bridge for the remaining future-covariance capacity.**

See `docs/orientation_complete_restart_packet.md`.


---

## 26. Full-state future-covariance tensor, double Stokes, and the true descent seam

Let the full stochastic Kelvin state have generator

\[
\mathscr L=b\cdot\nabla+\frac12a:\nabla^2,
\]

and let a vector terminal Kelvin payoff have conditional mean `m`, second moment `Q`
and covariance `C=Q-mm^T`.  Before any localization,

\[
\boxed{
(\partial_\tau-\mathscr L)C
=\Gamma_{\mathscr L}[m]
=(\nabla m)a(\nabla m)^T,
}
\]

while

\[
(\partial_\tau-\mathscr L)(mm^T)=-\Gamma_{\mathscr L}[m],
\qquad
(\partial_\tau-\mathscr L)Q=0.
\]

Thus quadratic variation is an exact transfer from conditional mean-square to
future covariance, with all mixed orientation entries retained.

The same matrix source is the diagonal defect of the same-ancestor pair generator:

\[
\boxed{
\mathscr L(U^\Delta)
-(\mathscr L^{(1)}+\mathscr L^{(2)})U|_\Delta
=\Gamma_{\mathscr L}[m],
\qquad
U(y_1,y_2)=m(y_1)m(y_2)^T.
}
\]

At the current/cochain level, the already existing pair momentum covariance
`mathbb K_s` localizes by double Stokes:

\[
\boxed{
C_s(\partial\Sigma_i,\partial\Sigma_j)
=\langle(d\boxtimes d)\mathbb K_s,\Sigma_i\boxtimes\Sigma_j\rangle.
}
\]

Exact gauge cochains vanish by boundary-squared-zero before any small-loop limit.
The independent locality audit shows that conditional mean-square continuity alone
is not enough for an arbitrary anisotropic material packet: its support must also
shrink and its error must be small in the packet metric.  Writing

\[
X_r=H_r^T\zeta_s(x)+\varepsilon_r,
\]

the invariant fixed-state condition is

\[
\boxed{H_r^{-T}\varepsilon_r\to0\quad\text{in conditional }L^2.}
\]

A sufficient criterion is support diameter `delta_r -> 0` together with

\[
\boxed{
\frac{(\sum_j A_{r,j}^2)^{1/2}}{\sigma_{\min}(H_r)}
\omega_2(\delta_r)\to0.
}
\]

Then

\[
\boxed{
H_r^{-T}C_{H_r}^{\rm future}H_r^{-1}
\to
\mathcal C_s(x)=\operatorname{Cov}_s(\zeta_s(x)).
}
\]

For centered, genuinely local and uniformly conditioned conditionally `C^2`
packets, the raw remainder begins at `r^6`, hence is only `r^2` after the packet
metric normalization.

Navier--Stokes supplies an independent tensor identity.  With
`E_omega=omega omega^T`, `A=grad u`,

\[
\boxed{
(\partial_t+u\cdot\nabla-\nu\Delta)E_\omega
=AE_\omega+E_\omega A^T
-2\nu(\nabla\omega)(\nabla\omega)^T.
}
\]

Thus the full Kelvin Gram tensor, not merely its trace, is the viscous defect tensor
of the vorticity dyad.  Its pullback by any area frame `H` is exactly the previously
audited packet q.v. matrix.

For the physical backward stochastic Kelvin orientation, Nanson plus NS further
gives the infinitesimal packet mean law

\[
\boxed{
[\partial_t+u\cdot\nabla-\nu\Delta-A^TH:\nabla_H](H^T\omega)=0.
}
\]

The exact one-mode shear has a causal past-payoff covariance tensor `C` satisfying

\[
\boxed{\mathfrak D_K C=+\mathcal G_K,
\qquad
\mathfrak D_K(\omega\omega^T)=-\mathcal G_K,
\qquad
\mathfrak D_K(C+\omega\omega^T)=0.}
\]

This causal check matters: the anti-diffusive physical-time operator cannot be
silently used with a future terminal `T>t`.  The repository's abstract forward
future-ancestry bank and the physical backward-Kelvin martingale therefore require a
literal time/state identification before they are declared the same object.

Finally, a reduced autonomous generator exists only when the full generator
intertwines with the reduction lift,

\[
\boxed{\mathscr L R=R\bar{\mathscr L}.}
\]

A finite-state audit contains both an exactly lumpable hidden-shape model and a
non-lumpable model in which two hidden current shapes at the same spatial point have
different physical exit rates.  In the latter case no spatial quotient generator
exists: the residual is hidden-state physical flux.

**Classification: Exact full-state tensor identities; exact NS and pair-current
calibrations; rigorous conditional fixed-state Stokes limit.  Programme-specific
generator descent, forward-future/backward-Kelvin identification, uniform
singular-time diagonal remainder control, restart, and regularity remain open.**

See `docs/future_covariance_tensor_audit.md`.


---

## 27. Literal backward-Kelvin current-shape state and the finite-shape current

The generator-descent seam can now be typed more sharply.  For a smooth material
current under the uniform backward Wiener flow, choose one material anchor `X` and
relative embedding `R`.  Then

\[
\widehat d_tX=u(X,t)dt+\sqrt{2\nu}\widehat dW_t,
\qquad
\boxed{
\widehat d_tR(\sigma)
=[u(X+R(\sigma),t)-u(X,t)]dt.
}
\]

Thus relative shape has zero stochastic quadratic variation.  On cylinder
observables the exact backward generator is

\[
\boxed{
\mathscr K^-
=u(X)\cdot\nabla_X-\nu\Delta_X
+\sum_p[u(X+R_p)-u(X)]\cdot\nabla_{R_p}.
}
\]

A differential area frame closes exactly:

\[
D_tH=-(\nabla u(X))^TH.
\]

A finite surface does not.  Its exact drift is

\[
\boxed{
\dot H=-(\nabla u(X))^TH+E_{\rm shape},
\qquad
E_{\rm shape}
=-\int_\Sigma[(\nabla u(y)-\nabla u(X))^Tn]dA.
}
\]

The exact smooth NS shear `u=(y^3+6 nu t y,0,0)` supplies two centered surfaces with
the same anchor and area vector `4e_x` but shape residuals `-4e_y` and `-16e_y`.
Therefore finite `(x,H)` is not an exact quotient state.  For centered scale `r`, the
calibration gives `E_shape=O(r^4)` raw and `E_shape/H=O(r^2)` exactly.

**Physical classification:** `E_shape` is finite-variation strain-gradient/material
shape deformation.  It is not martingale q.v., not pressure/gauge, and not `S^int`.

**Classification: Exact current-shape generator identity and exact NS no-descent
calibration.  Uniform singular-time collapse of the shape hierarchy remains open.**

See `docs/kelvin_shape_generator_audit.md`.


---

## 28. Same-clock drift split versus clock-reversed future-bank bridge

The causal seam can be read directly from the existing normalized ancestry operator

\[
\mathscr L\psi
=w\cdot\nabla\psi
+\nu\phi^{-1}\nabla\cdot(\phi K\nabla\psi),
\qquad q=f\phi.
\]

For symmetric `K`, define

\[
(c_\phi)_j=\phi^{-1}\partial_i(\phi K_{ij}).
\]

Then the expanded forward Itô drift is

\[
\boxed{b_+=w+\nu c_\phi.}
\]

The exact time-reversed drift at density `q` is

\[
\boxed{
b_-=w-\nu c_\phi-2\nu K\nabla\log f.
}
\]

The repository current velocity therefore satisfies

\[
\boxed{
j=w-\nu K\nabla\log f
=\frac{b_++b_-}{2},
}
\]

and the Fokker--Planck current is exactly `J=qj`.

For a **same-clock** identification of the ancestry backward drift with the
physical backward Kelvin drift `u`, the symbol must obey

\[
\boxed{
w_{\rm same}=u+\nu c_\phi+2\nu K\nabla\log f.
}
\]

Silently setting `w=u` instead leaves the explicit mismatch
`-nu c_phi-2nu K grad log f`, which is time-reversal/osmotic plus reference-geometry
drift, not an internal pair source.

However the repository's **future covariance bank** requires a different causal
operation.  Reverse its clock by `sigma=Theta-s`.  Then the future mean operator
uses `-b_+` with second-order sign `-nu K:Hess`.  Therefore a flat identity-map
anchor bridge to the physical backward-Kelvin operator requires

\[
\boxed{b_+=-u,}
\]

or, from `b_+=w+nu c_phi`,

\[
\boxed{w_{\rm future}=-u-\nu c_\phi.}
\]

The conditions `b_-=u` and `b_+=-u` are distinct.  If both were imposed on one
identity-map process, `2j=b_++b_-` would have to vanish.  The future-bank bridge must
therefore use the clock-reversed `b_+` state-map equations, not borrow the
same-clock `b_-` condition.

**Classification: Exact weighted time-reversal/Fokker--Planck identities and exact
future-bank clock reversal.  Programme-specific reverse-age ancestry-to-Kelvin
state intertwining remains open-literal.**

See `docs/ancestry_time_reversal_audit.md` and
`docs/two_clock_kelvin_quantile_audit.md`.


---

## 29. Packet locality is a separate physical seam from small area

The independent locality audit gives the exact incompressible witness

\[
F_r=\operatorname{diag}(r^{-1},1,r),
\qquad
H_r=r^2F_r^{-T}=\operatorname{diag}(r^3,r^2,r)\to0,
\]

while the largest transported line scale remains

\[
\boxed{
\sqrt{\det H_r}/\sigma_{\min}(H_r)=1.
}
\]

Thus a shrinking area-frame bank can remain spatially nonlocal.  The local future
covariance theorem must instead use the whitened error

\[
\boxed{H_r^{-T}\varepsilon_r\to0\quad\text{in conditional }L^2,}
\]

with explicit support locality.  A sufficient condition is

\[
\frac{(\sum_jA_{r,j}^2)^{1/2}}{\sigma_{\min}(H_r)}
\omega_2(\operatorname{diam}\Sigma_r)\to0.
\]

**Classification: Exact kinematic/covariance counterexample plus rigorous
conditional repaired Stokes criterion.  Uniform first-bad support locality remains
open.**

---

## 30. The ancestry reference gauge and the real state-map data

The ancestry representation has the exact gauge

\[
\phi'=e^g\phi,
\qquad
f'=e^{-g}f,
\qquad
w'=w-\nu K\nabla g,
\]

under which

\[
\boxed{q,j,\mathscr L,b_+,b_-\text{ are unchanged}.}
\]

Therefore `f`, `phi`, and `w` are not independent physical state coordinates.  The
state-map domain must be the as-yet-unspecified ancestry state `y` together with its
gauge-invariant diffusion data `(K,b_-)`.

If `K=BB^T`, zero-q.v. physical relative shape requires

\[
\boxed{D\Pi_{\rm shape}B=0.}
\]

A full-rank `K` therefore cannot encode a nontrivial smooth current shape on an open
region; the ancestry state must contain deterministic/null directions or be enlarged
by path/history information.

**Classification: Exact reference-gauge and diffusion-factorization identities;
open-literal ancestry-state construction.**

---

## 31. Reduced ancestry introduces an exact resolution-covariance pair face

If the stored ancestry state `y` is coarser than the physical Kelvin current-shape
state `Y`, let `kappa_y(dY)` be the conditional lift kernel.  For full-state terminal
mean `m(Y)` and covariance `C(Y)`, the reduced covariance is exactly

\[
\boxed{
\bar C(y)
=
\int C(Y)\,\kappa_y(dY)
+
\operatorname{Cov}_{\kappa_y}(m(Y)).
}
\]

The second term has the pair form

\[
\boxed{
C_{\rm res}(y)
=
\frac12\iint
[m(Y_1)-m(Y_2)]^{\otimes2}
\,\kappa_y(dY_1)\kappa_y(dY_2).
}
\]

It is full cross-orientation pair content and can be nonzero even when `nu=0` and
the full-state future variance vanishes.  Thus it is a **state-resolution covariance
face**, not the viscous branching tensor.

The canonical `2 nu q K delta_Delta` source remains exact when `q` is on the full
diffusion state.  If `q` is reduced, `C_res` must be added at the reduction face or
the phrase “same ancestor” loses physical state information.

**Classification: Exact law-of-total-covariance identity and rigorous state-resolution
dichotomy.  No identification with undefined `S^int / Z_irr`.**


---

## 32. One anisotropy tensor controls support and Kelvin metric amplification

For a coherent microcell,

\[
\boxed{
G_{\rm line}=\rho^2\mathcal A,
\qquad
M_H=\rho^{-4}\mathcal A,
\qquad
\det\mathcal A=1.
}
\]

Incompressible material evolution leaves `rho` fixed and lets strain act on
`mathcal A`; physical refinement/reselection supplies the scale jumps.  Therefore
uniform packet support locality and metric-whitened covariance control are not two
unrelated geometries.  They are two contractions of the same material anisotropy
against opposite scale powers.

For centered planar faces the first finite-size shape and flux errors also share one
physical carrier,

\[
Q_\Sigma=\int_\Sigma\xi\xi^T\,dA.
\]

For quadratic Taylor fields,

\[
E_{\rm shape}
=-\frac12 Q_\Sigma:\partial^2(\nabla u)^Tn,
\qquad
\varepsilon_{\rm flux}
=\frac12 Q_\Sigma:\partial^2\zeta\,\cdot n.
\]

Thus the two previously separate fixed-state `r^2` remainders are manifestations of
the same centered quadrupole geometry, with different PDE fields attached.

**Classification: Exact cofactor/scale algebra and exact centered quadratic Taylor
identities.  Uniform singular-time control remains open.**

---

## 33. Viscosity is internal transfer in the resolved-plus-future second-moment bank

In co-deforming Kelvin coordinates, let `C_tilde` be the future covariance and
`Sigma_fut=F C_tilde F^T`.  Then

\[
\boxed{
T_{\rm tot}=\omega\omega^T+\Sigma_{\rm fut}
}
\]

has exact backward-Kelvin tensor law

\[
\boxed{
\mathfrak D_K^-T_{\rm tot}
=(\nabla u)T_{\rm tot}+T_{\rm tot}(\nabla u)^T.
}
\]

The Kelvin Gram tensor is lost by the resolved mean dyad and gained by future
covariance with equal magnitude.  Consequently

\[
\boxed{
\mathfrak D_K^-
\left(\frac12|\omega|^2+\mathcal B_{\rm fut}\right)
=\operatorname{tr}(S T_{\rm tot}),
}
\]

where `B_fut=(1/2)tr(C_tilde F^T F)` for the coherent isotropic packet lineage.
The hard local channel is therefore total second-moment strain work, not a proposed
pointwise domination of stretching by instantaneous viscous payment.

**Classification: Exact full-state identity.  Localized singular-time capacity and
restart remain open.**

---

## 34. A co-deforming total bank cancels both q.v. transfer and common strain

After combining resolved vorticity dyad with future covariance into `T_tot`, use the
shape-only support tensor `B_F=F F^T`.  Then

\[
\boxed{
\mathcal I_{\rm cof}
=\frac12\operatorname{tr}(B_F^{-1}T_{\rm tot})
=\frac12\operatorname{tr}Q_{\rm tot}.
}
\]

The Kelvin Gram source has already canceled between mean and covariance, and the
common two-sided strain cancels exactly against the evolution of `B_F^{-1}`.  Thus
`I_cof` is homogeneous on the full physical backward-Kelvin state.

This does not prove physical vorticity remains bounded: recovering physical
coordinates requires the actual support/refinement geometry.  The result instead
isolates the remaining obstruction to that geometry and to the already named
localization/state-resolution faces.

**Classification: Exact identity; restart/continuation remains open.**

---

## 35. Shape and covariance remainders share one support-amplification factor

Define

\[
\chi_H
=
\frac{(\sum_jA_j^2)^{1/2}}{\sigma_{\min}(H)}.
\]

The exact finite-shape connection and metric-whitened flux errors satisfy

\[
\|E_{\rm shape}H^{-1}\|_F
\le\chi_H\omega_{\nabla u}(\delta),
\qquad
\|H^{-T}\varepsilon_{\rm flux}\|_{L^2_s}
\le\chi_H\omega_{\zeta,2}(\delta).
\]

Thus finite-shape collapse and local future-covariance collapse are not separate
geometric problems.  Their common geometry is support diameter plus packet
anisotropy/conditioning; the PDE fields differ.

**Classification: Rigorous joint sufficient criterion.  Uniform first-bad control
remains open.**

---

## 36. Literal finite-shape Kelvin descent error: covariance is not the bias

The full-current descent seam can now be written without an abstract remainder.
For the actual finite material spanning surface `Sigma_R`, set

\[
h_R=\int_{\Sigma_R}n\,dA,
\qquad
\varepsilon_K
=K_{\partial\Sigma_R}-\omega(X)\cdot h_R.
\]

Stokes gives exactly

\[
\boxed{
\varepsilon_K
=\int_{\Sigma_R}[\omega(X+r)-\omega(X)]\cdot n\,dA.
}
\]

This is finite-support vorticity-inhomogeneity flux.  It is not a norm defect or a
covariance by definition.

A type correction is essential.  The actual current marched backward in reverse age
has local area connection `+A^T`; the same-replica Cauchy metric-dual packet frame
`H_C=rho^2D^-1` has `-A^T`.  They are different physical geometries and the old
shorthand `Z_local(D,H)` must not identify them.

For the actual finite surface define

\[
\mathcal R_A
=\int_{\Sigma_R}[A(X+r)-A(X)]^Tn\,dA
\]

and

\[
q_\mu^{\rm err}
=\int_{\Sigma_R}
[\partial_\mu\omega(X+r)-\partial_\mu\omega(X)]\cdot n\,dA.
\]

The genuine reverse-age Navier--Stokes/Nanson/Itô law is

\[
\boxed{
d\varepsilon_K
=-\omega(X)\cdot\mathcal R_A\,d\sigma
+\sqrt{2\nu}\sum_\mu q_\mu^{\rm err}dW^\mu.
}
\]

Thus the finite-shape seam has a deterministic/finite-variation bias-drift face and
an anchor-translation stochastic-spread face.  Relative shape itself still has zero
q.v.

Pathwise,

\[
[\operatorname{vec}D,\varepsilon_K]=0,
\]

but finite-horizon `Cov(vec D,epsilon_K)` can be nonzero through the same anchor
carré-du-champ as every other full-state connected covariance.  This covariance is
not the value or mean of `epsilon_K`.

Exact cubic heat-shear Navier--Stokes makes that distinction decisive.  For a
centered `xy` rectangle of half-widths `a,b`,

\[
\boxed{\varepsilon_K=-4ab^3\neq0}
\]

for every reverse age and every Brownian anchor, while

\[
\dot\varepsilon_K=0,
\qquad
[\varepsilon_K]=0,
\qquad
\operatorname{Var}(\varepsilon_K)=0,
\qquad
\operatorname{Cov}(\operatorname{vec}D,\varepsilon_K)=0.
\]

Therefore a covariance bank can be exactly blind to a nonzero conserved finite-shape
mode.  Exact ABC flow independently activates the finite-variation
`-omega dot R_A` face, while exact one-mode shear activates error q.v. and the
`D`/error covariance block.

For centered smooth surfaces the first deterministic carrier is the oriented
quadrupole `M_kl=int r_k r_l n dA`.  Both `epsilon_K` and `R_A` start at raw order
`r^4`; `q_mu^err` uses one additional vorticity derivative and is also raw `r^4`, so
its q.v. rate is raw `r^8`.  Odd polynomial heat shears with Legendre `P_2m`
surfaces show that every finite even-moment truncation misses a higher deterministic
flux mode, and at the centered symmetry point the exposing mode can have zero
instantaneous error-q.v. coefficient.

**Classification: Exact Stokes/Navier--Stokes/Nanson/Itô identities; exact NS
calibrations and rigorous covariance-only / finite-moment no-go consequences.**

The first-bad target is therefore sharper: a real descent theorem must control the
actual deterministic bias `epsilon_K`, the finite-variation shape current `R_A`, the
stochastic residual `q_mu^err`, support locality, and the metric-whitened pair
covariance remainder on one compatible selected physical state/clock.  Covariance
alone cannot substitute for that state theorem.

**Classification: Open-literal.  No restart/continuation/regularity theorem
claimed.**

See `docs/finite_shape_kelvin_descent_audit.md`.

---

## 37. The finite-shape seam is an upward-coupled material moment hierarchy

For the actual reverse-age spanning surface define oriented moments

\[
M_\alpha=\int r^\alpha n\,dA.
\]

Their exact transport is

\[
\dot M_\alpha
=-\sum_i\alpha_i\int r^{\alpha-e_i}\Delta u_i(r)n\,dA
+\int r^\alpha A(X+r)^Tn\,dA.
\]

Affine velocity closes each order exactly.  A spatial velocity jet of degree `p`
forces order `m` to couple to order `m+p-1`.  Hence nonlinear Navier--Stokes does
not preserve a generic finite low-moment quotient.

Exact quadratic heat shear makes a centered `yz` surface acquire a nonzero oriented
first moment directly from its quadrupole; the new component is transverse to the
area vector, so one anchor shift cannot remove it.  In the complementary `xy` shear
geometry, the entire oriented `y`-moment tower is conserved exactly.  Thus omitted
shape content can be either dynamically injected into lower-order observables or
carried as a persistent hidden mode.

This dynamic hierarchy and the static Legendre no-go say the same thing from two
sides: adding any fixed finite list of moments cannot be the universal exact
first-bad state.  What remains open is whether genuine shrinking selected support
makes the infinite tower asymptotically subordinate to one local scale/shape law.

**Classification: Exact material hierarchy / audited exact-NS calibrations;
first-bad uniform jet collapse Open-literal.  No continuation/restart theorem.**

See `docs/surface_moment_hierarchy_audit.md`.

---

## 36. The infinite finite-shape tower reduces to one codeforming nonaffinity field

The literal finite-surface hierarchy can be reorganized without truncation.  On a
smooth reverse-age material segment choose the actual local line frame

\[
\dot L=-\nabla u(X)L,
\]

and pull the surface back by

\[
\xi=L^{-1}r,
\qquad
\widetilde a=\operatorname{cof}(L)^{-1}a.
\]

Then all affine deformation cancels.  Define

\[
\boxed{
\mathcal N_L(\xi)
=L^{-1}[u(X+L\xi)-u(X)-\nabla u(X)L\xi].
}
\]

Incompressibility gives the exact residual material-surface system

\[
\boxed{
\dot\xi=-\mathcal N_L,
\qquad
\dot{\widetilde a}=(D_\xi\mathcal N_L)^T\widetilde a,
\qquad
\nabla_\xi\cdot\mathcal N_L=0.
}
\]

Thus every pulled-back oriented moment, and equivalently the generating current
`int exp(theta.xi) a_tilde`, is driven by this one nonaffinity field.  Affine flow
freezes the entire tower exactly.  Coherent linear refinement of current and frame is
also exact gauge.

For `L=rho S`, a homogeneous degree-`p` NS jet appears as

\[
\mathcal N_{\rho S}^{(p)}
=\rho^{p-1}S^{-1}U_p(S\xi),
\]

so scalar scale and anisotropy are distinct physical faces.  Exact linear-strain NS
shows codeforming constancy without physical locality at critical refinement.  Exact
quadratic heat-shear NS with shrinking `L_r=diag(r^3,r,r)` gives
`mathcal N_L=r^-1 xi_y^2 e_x`, so physical support shrink alone does not imply
codeforming affine collapse.

The remaining first-bad descent seam is therefore not "choose more moments".  It is
simultaneous control of actual support/current faces and tensorial NS nonaffinity
relative to the actual selected frame.  Selector switches, noncoherent refinements,
physical boundary/exit, and reset remain separate pair-current faces.

**Classification: Exact identities and audited exact-NS no-go calibrations.
First-bad anisotropic jet-frame collapse is Open-literal.  No restart, continuation,
or regularity theorem is claimed.**

---

## 37. Kelvin reads the metric-weighted codeforming nonaffinity one-form

The codeforming residual vector field has a second exact face.  With
`G_L=L^T L`, define

\[
\boxed{\beta_L=G_L\mathcal N_L.}
\]

Because the physical residual velocity is `L mathcal N_L` and `dr=L dxi`,

\[
\boxed{
\varepsilon_K
=\oint_{\widetilde Z}\beta_L\cdot d\xi,
\qquad
\operatorname{curl}_\xi\beta_L
=\operatorname{cof}(L)^T[\omega(X+L\xi)-\omega(X)].
}
\]

Thus the same nonaffinity drives three differently typed objects: residual shape
velocity `N_L`, oriented-area rate `(D N_L)^T`, and Kelvin one-form `G_L N_L`.
Exact quadratic heat-shear with `L=diag(r^3,r,r)` gives
`N_L=r^-1 xi_y^2 e_x` but `beta_L=r^5 xi_y^2 e_x`.  A divergent normalized shape
velocity therefore does not imply failure of instantaneous Kelvin descent.

The first-bad frontier must keep two seams separate: instantaneous circulation/local
Stokes descent is a `beta_L`/vorticity-defect question, while dynamic finite-current
shape descent is an `N_L,D N_L` plus selector/boundary/exit/reset question.

**Classification: Exact identity / audited exact-NS type separation.  Both first-bad
uniform controls remain Open-literal.  No restart, continuation, or regularity theorem
is claimed.**

---

## 38. Codeforming form of the exact finite-shape error SDE

Because only the anchor is Brownian on the full current-shape state, the codeforming
Kelvin one-form gives the martingale coefficient directly:

\[
q_\mu^{\rm err}
=\oint_{\widetilde Z}\partial_{X_\mu}\beta_L\cdot d\xi.
\]

With `eta_0=cof(L)^T omega(X)` and
`htilde_dot=int(D_xi N_L)^T a_tilde`, the already audited physical SDE becomes

\[
\boxed{
d\varepsilon_K
=-\eta_0\cdot\dot{\widetilde h}\,d\sigma
+\sqrt{2\nu}\sum_\mu
\left(\oint\partial_{X_\mu}\beta_L\cdot d\xi\right)dW^\mu.
}
\]

Thus deterministic shape drift and stochastic finite-support spread are both faces of
the same codeforming nonaffinity geometry, but remain physically distinct: the first
uses `D N_L`, the second uses anchor derivatives of `G_L N_L`.

**Classification: Exact identity / exact one-mode NS calibration.  No new bank and no
restart/continuation/regularity conclusion.**

---

## 39. Metric-whitened remainder is a reconstructed physical residual

For a coherent orientation packet `H=cof(L)`, pointwise flux-density coordinates
satisfy

\[
g_H=H^T\delta\omega,
\qquad
H^{-T}g_H=\delta\omega.
\]

For the same-time finite Kelvin current this is exactly

\[
H^{-T}\operatorname{curl}_\xi\beta_L
=\omega(X+L\xi)-\omega(X).
\]

At finite scale define `r_H=H^-T epsilon_H`.  It is the physical vector reconstructed
from the three finite face residuals.  It is generally not a pointwise defect because
each component samples a different face.  Exact cubic heat-shear NS witnesses this:
on the unit cube the center defect vanishes while `r_H=-e_z/4`; isotropic refinement
gives exactly `r_H=-r^2 e_z/4`.

The packet metric has the literal reconstruction meaning

\[
|r_H|^2=\varepsilon_H^T(H^TH)^{-1}\varepsilon_H,
\]

with the same congruence identity for covariance and q.v.  For a random full payoff
`H^-T X_H=zeta+r_H`, the exact covariance contains residual covariance **and both
local--residual cross blocks**.  Those cross terms cannot be dropped before the
conditional `L^2` local-limit argument.

This closes the fixed-state physical typing of the metric-whitened topology, not its
uniform first-bad control and not the cross-clock future-bank/ancestry bridge.

**Classification: Exact fixed-state reconstruction/covariance identities; audited
exact-NS finite-scale calibration.  First-bad uniform collapse and cross-clock
identification remain Open-literal.  No restart/continuation/regularity theorem.**
