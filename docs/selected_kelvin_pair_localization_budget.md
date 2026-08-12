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
quantile/shell interfaces and physical exit remain explicit two-face currents;
anchor/frame terms are connection geometry; reset is exact covariance revaluation.
Only a one-current active-map remainder left after these terms are subtracted can
feed the literal `S^int / Z_irr` sector.

**Classification: Rigorous consequence.**

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

and the first-bad support projector in germ space as `M_fb(s)`.  Then

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
quantile/shell localization, connection geometry, refinement, physical exit, and
finite reset are kept literally, the first-bad selector itself has no remaining
irreducible sector:

\[
\boxed{
C_{\rm irr}^{\rm selector}=0,
\qquad
G_{\rm irr}^{\rm selector}=0.
}
\]

**Classification: Rigorous consequence of exact cycle typing, cut-current algebra,
and finite reset algebra.**

Accordingly, for the cycle-typed selector sector the pair-localization identity is

\[
\boxed{
\Pi^{\rm sel}-\Pi^{\rm dist}
=
\partial_{\rm pair}\mathscr W_{\rm loc}^{(2)}
+\Pi_{\rm quant}^{(2)}
+\Pi_{\rm shell}^{(2)}
+\Pi_{\rm exit}^{(2)}
+\Pi_{\rm conn}^{(2)}
+\Pi_{\rm reset}^{(2)}.
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
  \Pi_{\rm quant}^{(2)}
 +\Pi_{\rm shell}^{(2)}
 +\Pi_{\rm exit}^{(2)}\rangle\\
&+\mathcal H_{\rm conn}+\mathcal R_{\rm reset}.
\end{aligned}
}
\]

**Classification: Exact current/covariance identity for the cycle-typed selector
sector, with the same full-state generator-compatibility caveat already stated for
the Kelvin future-variance PDE.**

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

The canonical ancestry source `2 nu q K delta_Delta` has the same diagonal
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

The existence of a singular-time-uniform local **future** covariance tensor and a
suitable remainder current is not established.

**Classification: Conjectural bridge.**

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
