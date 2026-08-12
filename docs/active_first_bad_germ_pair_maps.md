# Active first-bad-germ maps on the full pair world-sheet

This note is an **uncertified PDE-first frontier calculation**.  It does not claim
continuation, restart, or regularity.  Its purpose is to remove one ambiguity from
Pillar II: after full pair content is retained, can a genuinely new pair-only
non-functorial residual appear, or is every pair residual already the two-replica
lift of a one-current active-map defect?

The answer at the algebraic level is rigid: for a tensor-square pair lift, every
boundary or transport defect factorizes exactly through the corresponding
one-current commutator.  Therefore cross-child/cross-shell covariance cannot be
relabelled as `S^int / Z_irr`, and no pair-only producer is created by the lift.
What remains open is narrower and literal: the repository still does not contain
the chain-level incidence and transport data of the actual active CK projection.
Until that datum is inserted, the one-current active commutators cannot be audited
to zero.

---

## 1. Chain data and the full ordered pair boundary

At stage `k`, let

\[
B_k:C^{(k)}_1\to C^{(k)}_0
\]

be the literal current boundary map.  A one-current stage map is a pair

\[
F_k=(F_{k,1},F_{k,0}),
\qquad
F_{k,1}:C^{(k)}_1\to C^{(k+1)}_1,
\qquad
F_{k,0}:C^{(k)}_0\to C^{(k+1)}_0.
\]

Its one-current boundary defect is

\[
\boxed{
C_k
:=B_{k+1}F_{k,1}-F_{k,0}B_k.
}
\]

The full ordered pair lift is

\[
\boxed{F_k^{(2)}=F_{k,1}\otimes F_{k,1}.}
\]

For degree-one factors, retain the two ordered physical faces separately:

\[
\partial_{\rm pair,k}
=
\begin{bmatrix}
B_k\otimes I\\
-I\otimes B_k
\end{bmatrix}.
\]

The stage map induced on those two boundary faces is

\[
F_{\partial,k}^{(2)}
=
\operatorname{diag}
\bigl(F_{k,0}\otimes F_{k,1},\;F_{k,1}\otimes F_{k,0}\bigr).
\]

Direct expansion gives

\[
\boxed{
\partial_{\rm pair,k+1}F_k^{(2)}
-F_{\partial,k}^{(2)}\partial_{\rm pair,k}
=
\begin{bmatrix}
C_k\otimes F_{k,1}\\
-F_{k,1}\otimes C_k
\end{bmatrix}.
}
\]

**Classification: Exact identity.**

This is the first decisive reduction.  With full pair content there is no new
pair-only boundary defect.  The pair defect is exactly the one-current defect on
replica face 1 plus the same defect on replica face 2, with the product-boundary
orientation sign.

In particular, if `C_k=0`, then the full pair lift commutes with boundary exactly.
If `C_k` is a known quantile/shell/exit interface current, the pair defect is the
genuine two-face physical lift of that interface current.  Only an unexplained
remainder in `C_k` can enter the literal `S^int / Z_irr` slot.

**Classification: Rigorous consequence.**

---

## 2. Transport analogue: no pair-only transport producer

Let the one-current covariant transport on the two sides of a stage be

\[
D_{\rm in}=\partial_s+T_{\rm in},
\qquad
D_{\rm out}=\partial_s+T_{\rm out}.
\]

For a possibly moving stage map `F(s)`, define

\[
\boxed{
G_F
:=\dot F+T_{\rm out}F-FT_{\rm in}.
}
\]

The ordered-pair generator is

\[
T^{(2)}=T\otimes I+I\otimes T.
\]

Differentiating `F tensor F` and expanding gives

\[
\boxed{
G_F^{(2)}
=G_F\otimes F+F\otimes G_F.
}
\]

**Classification: Exact identity.**

Thus a variable frame can create a connection commutator, but it cannot create a
new stochastic pair producer.  If the active frame is transported covariantly so
that

\[
\dot F+T_{\rm out}F-FT_{\rm in}=0,
\]

then the pair transport residual also vanishes exactly.  If the same geometry is
written in a fixed frame, the nonzero term is connection/holonomy geometry and
must remain classified as such.

**Classification: Rigorous consequence.**

---

## 3. The actual first-bad-germ maps to be used

The first-bad excursion is now represented by the following literal map types.
The notation is deliberately at current level before any inequality.

### 3.1 Entry/freeze

On a frozen selector interval,

\[
F_{\rm freeze,1}=I,
\qquad
F_{\rm freeze,0}=I.
\]

Hence `C_freeze=0`.  The stochastic payment on this interval is the already-audited
fixed-current Kelvin quadratic variation with its exact future-variance bank.

**Classification: Exact identity.**

### 3.2 Quantile localization

Let `Q_s` be the physical restriction to the moving quantile chamber used by the
selector.  On currents this is the restriction/push-forward map associated with
that chamber; on boundary data it has the induced restriction `Q_{s,0}`.  Define

\[
C_{\rm quant}
:=B Q_{s,1}-Q_{s,0}B.
\]

Distributionally this is supported on the moving quantile interface.  Its pair
lift is not zero merely because one-particle quantile mass is conserved:

\[
C_{\rm quant}^{(2)}
=
\begin{bmatrix}
C_{\rm quant}\otimes Q_{s,1}\\
-Q_{s,1}\otimes C_{\rm quant}
\end{bmatrix}.
\]

The exact same-ancestor Gaussian arcsine calibration already shows that this pair
interface current can be nonzero while each marginal mass stays fixed.

**Classification: Exact pair-commutator identity; rigorous physical
interpretation from the existing exact Gaussian calibration.**

### 3.3 Anchor/orientation motion

Let

\[
U_g=(\Phi_g)_\#
\]

be the push-forward generated by the physical anchor/orientation motion.  Push-
forward commutes with current boundary:

\[
B_{g_1}U_{g_1\leftarrow g_0,1}
=U_{g_1\leftarrow g_0,0}B_{g_0}.
\]

Hence the boundary commutator vanishes.  Continuous motion contributes instead
through

\[
G_U=\dot U+T_{g_1}U-UT_{g_0},
\]

which is connection geometry.  In a co-moving connection `G_U=0`; in a fixed
frame it is the already-audited Lie/connection term.  Pair transport contains
exactly `G_U tensor U + U tensor G_U` and nothing else.

**Classification: Exact identity for push-forward/boundary naturality and the
pair transport factorization.  Identification of the literal CK frame with this
push-forward remains a Conjectural bridge until its frame data are inserted.**

### 3.4 Shell map

For a physical shell partition

\[
D=\bigsqcup_i A_i,
\]

define the one-current partition map

\[
H_1 Z=(\mathbf 1_{A_i}Z)_i.
\]

The full pair map is not the diagonal shell list.  It is

\[
\boxed{
H^{(2)}(Z\boxtimes Z)
=
\bigl((\mathbf 1_{A_i}Z)\boxtimes
      (\mathbf 1_{A_j}Z)\bigr)_{i,j}.
}
\]

Individual shell restrictions have interface commutators

\[
C_{{\rm shell},i}=B H_{i,1}-H_{i,0}B.
\]

These are physical shell-boundary currents.  Reassembly of the complete physical
partition cancels internal shell interfaces in the parent current, while the pair
reassembly requires every ordered block `A_i x A_j`; the cross-shell blocks are
physical covariance transport.

**Classification: Exact identity for the full product partition and exact
commutator factorization; physical nontriviality is already a rigorous consequence
of the same-ancestor calibration.**

### 3.5 Refinement

For the literal linear refinement

\[
R_1:Z_P\mapsto \sum_i a_i Z_i,
\]

use its boundary map `R_0` and require the physical subdivision identity

\[
B_{\rm fine}R_1=R_0B_{\rm coarse}.
\]

Then

\[
C_{\rm ref}=0,
\qquad
R^{(2)}=R_1\otimes R_1,
\qquad
C_{\rm ref}^{(2)}=0.
\]

Every cross-child term is present automatically.  A diagonal-only pair map is not
this functor and is an analysis defect.

**Classification: Exact identity.**

### 3.6 Resolve/reset

At a selector reset, let `J` denote the finite map from the old closed selected
current to the new closed selected current.  On closed-current space the pair map
is exactly

\[
J^{(2)}=J\otimes J.
\]

There is no stochastic quadratic variation produced by the finite-variation
observer jump.  The future covariance changes by the exact reset identity

\[
V(Z^+)-V(Z^-)
=2C(Z^-,\Delta Z)+V(\Delta Z).
\]

For a chain-level boundary audit, a literal extension `(J_1,J_0)` is required.  If
that extension is a chain map, its boundary residual vanishes; if not, its
commutator must be retained and classified rather than silently assigned to
Pillar II.

**Classification: Exact covariance identity on closed currents; chain-level
functoriality of the actual reset extension is a Conjectural bridge until that
extension is supplied.**

### 3.7 Physical exit

Let `E_D` be killing/restriction to the physical domain.  Its one-current boundary
commutator is the physical exit face.  The full pair lift is

\[
E_D^{(2)}=E_D\otimes E_D
\]

and therefore its pair boundary residual is exactly

\[
\boxed{
\begin{bmatrix}
C_{\rm exit}\otimes E_D\\
-E_D\otimes C_{\rm exit}
\end{bmatrix},
}
\]

the two physical faces `(partial D x D)` and `(D x partial D)`.  The killed
Brownian calibration already verifies the corresponding two-face loss law.

**Classification: Exact current identity; rigorous calibration of the physical
sink.**

### 3.8 Active CK projection

Write the actual active projection, once its literal incidence data are supplied,
as

\[
P_{\rm act}=(P_{{\rm act},1},P_{{\rm act},0}).
\]

The two quantities that must be audited are exactly

\[
\boxed{
C_{\rm act}
=B P_{{\rm act},1}-P_{{\rm act},0}B,
}
\]

and

\[
\boxed{
G_{\rm act}
=\dot P_{{\rm act},1}
+T_{\rm out}P_{{\rm act},1}
-P_{{\rm act},1}T_{\rm in}.
}
\]

The repository currently contains neither the chain-level matrices/incidence maps
for `P_act` nor its literal transport generator.  Therefore `C_act=0` and
`G_act=0` are **not** established here.

**Classification: Conjectural bridge / literal missing datum.**

---

## 4. Completed hysteresis excursion: exact seam composition

Let the chronological one-current stages be

\[
F_1=F_{\rm freeze},\;
F_2=Q,\;
F_3=U,\;
F_4=H,\;
F_5=R,\;
F_6=J,\;
F_7=E_D,
\]

with active CK projection inserted at the literal places where the construction
actually applies it.  For the moment suppress those still-unspecified active
insertions and define

\[
F_{\rm phys}=F_7F_6\cdots F_1.
\]

For variable chain spaces, the exact product rule is

\[
\boxed{
C(GF)=C(G)F_1+G_0C(F).
}
\]

Iterating gives the completed one-current boundary residual line by line:

\[
\boxed{
C(F_{\rm phys})
=
\sum_k
F_{0,>k}\,C_k\,F_{1,<k}.
}
\]

Here `F_{1,<k}` transports the incoming current to stage `k`, and `F_{0,>k}`
transports the resulting boundary current to the final boundary space.

Thus:

- freeze contributes zero;
- quantile contributes transported quantile-interface current;
- anchor/orientation contributes zero boundary defect and, separately, connection
  transport geometry;
- shell contributes transported shell-interface current, with internal cancellation
  only after full physical reassembly;
- refinement contributes zero when the literal full chain map is used;
- resolve/reset contributes exact covariance revaluation and zero boundary defect
  if its chain extension is natural;
- physical exit contributes transported physical exit current.

The pair completed-excursion residual is obtained by the same product rule with
`F_k^(2)` and the two-face pair boundary maps.  Equivalently, after composing the
one-current physical map first, it is exactly the two-face lift of
`C(F_phys)`.

**Classification: Exact identity.**

This is stronger than abstract rung cancellation: it says exactly where every
longitudinal seam comes from and proves that a full tensor-square lift cannot
manufacture a second-order seam that did not already exist at one-current level.

---

## 5. Literal residual decomposition

Before any term can be called `S^int / Z_irr`, decompose the one-current active
commutators as

\[
C_{\rm act}
=
C_{\rm quant}
+C_{\rm shell}
+C_{\rm exit}
+C_{\rm conn,bdy}
+C_{\rm irr},
\]

and

\[
G_{\rm act}
=
G_{\rm quant}
+G_{\rm shell}
+G_{\rm anchor/conn}
+G_{\rm ref}
+G_{\rm reset}
+G_{\rm exit}
+G_{\rm irr}.
\]

Cross-child and cross-shell covariance are not terms in `C_irr` or `G_irr`; they
are already contained in the full pair maps.  The only pair residual eligible for
Pillar II is therefore

\[
\boxed{
C_{\rm irr}^{(2)}
=
\begin{bmatrix}
C_{\rm irr}\otimes P_{{\rm act},1}\\
-P_{{\rm act},1}\otimes C_{\rm irr}
\end{bmatrix}
}
\]

and

\[
\boxed{
G_{\rm irr}^{(2)}
=G_{\rm irr}\otimes P_{{\rm act},1}
+P_{{\rm act},1}\otimes G_{\rm irr}.
}
\]

**Classification: Exact identity once the decomposition of the one-current active
commutators has been made literally.**

So the pair problem has now been reduced to a one-current naturality audit.  There
is no independent pair-only `Z_irr` generated by full tensor-square lifting.

**Classification: Rigorous consequence.**

---

## 6. Counterexample pressure: why `P_active` cannot be assumed natural

A projection onto an arbitrary set of active cells need not define a subcomplex.
On a two-edge interval, retain only the first edge and its two incident vertices.
The deleted second edge still has the shared interface vertex in its boundary, so

\[
BP_1-P_0B\ne0.
\]

The exact symbolic audit in
`tests/test_active_first_bad_pair_maps.py` verifies that its pair residual is then
nonzero on both ordered replica faces.

This is a counterexample to the generic statement

> “projection onto active cells automatically commutes with boundary.”

It is **not** evidence that the actual CK projection has this defect; the actual CK
incidence map is not yet present in the repository.

**Classification: Exact finite-chain counterexample to an unjustified generic
cancellation; active-CK conclusion remains open.**

---

## 7. Exact Navier--Stokes calibration of active pair content

For the exact odd-mode periodic Navier--Stokes shear, the terminal Kelvin payoffs at
anchors `0` and `pi` satisfy pathwise

\[
X_\pi=-X_0.
\]

Consider an active interpolation

\[
Z_h=hZ_0+(1-h)Z_\pi.
\]

Then pathwise

\[
X_h=(2h-1)X_0,
\]

so the exact future variance is

\[
\boxed{
V_h=(2h-1)^2V_0.
}
\]

At `h=1/2` the physical current and its future variance vanish.  A diagonal-only
pair projection instead gives

\[
\bigl(h^2+(1-h)^2\bigr)V_0>0.
\]

The new CI test checks this over the closed-form exact NS calibration.  Therefore
an active map that mixes/refines physical currents must retain the full tensor
square; otherwise it manufactures a false positive bank exactly where the true
physical Kelvin current is zero.

**Classification: Rigorous consequence from an exact Navier--Stokes calibration.**

---

## 8. Answer to the present frontier question

After keeping full pair content and every already identified physical
boundary/connection term, the current audit supports the following precise answer:

\[
\boxed{
\text{There is no autonomous pair-only residual.}
}
\]

Every full-pair boundary/transport residual is generated exactly by the
corresponding one-current active-map commutator.  Quantile, shell, physical exit,
connection geometry, cross-shell covariance, and cross-child covariance are all
already classified and cannot be renamed `S^int / Z_irr`.

What is **not yet known** is whether the actual CK first-bad projection has a
nonzero one-current irreducible commutator after those physical terms are removed.
That question cannot be answered from the present repository because the literal
chain-level `P_act` incidence and transport data have not yet been written down.

Therefore the strongest current statement is:

\[
\boxed{
\Pi_{\rm irr}^{(2)}=0
\quad\text{if}\quad
C_{\rm irr}=0\ \text{and}\ G_{\rm irr}=0,
}
\]

and if either one-current remainder is nonzero, its full pair obstruction is the
explicit tensor formula in Section 5.  No estimate is needed or permitted to hide
it.

**Classification: Exact conditional identity plus an open literal CK incidence
audit.**

If the forthcoming literal `P_act` data make `C_irr=G_irr=0`, the next selected
Kelvin pair-bank identity is obtained from the world-sheet Stokes law with only
endpoint covariance, quantile/shell transfer, connection geometry, exact reset
revaluation, and physical exit.  If not, the nonzero `C_irr/G_irr` pairing with the
future covariance cochain is the genuine obstruction; no finite universal bank for
that irreducible term has yet been established.

No continuation/restart conclusion follows here.

---

## 9. Conditional exact selected-Kelvin pair-bank identity

The commutator reduction makes the next identity explicit.  Suppose the literal CK
incidence/transport audit eventually gives

\[
C_{\rm irr}=0,
\qquad
G_{\rm irr}=0.
\]

Then the irreducible pair term vanishes exactly, not by estimate:

\[
\Pi_{\rm irr}^{(2)}=0.
\]

After internal refinement and full-shell reassembly, the pair-current localization
identity reduces to

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

Here `Pi_conn^(2)` denotes the covariant connection/holonomy work when a fixed
frame rather than the co-moving frame is used, and `Pi_reset^(2)` denotes the exact
finite covariance revaluation at selector resets.  Neither is a stochastic
quadratic-variation producer.

Pairing with the future Kelvin covariance cochain `mathbb K` gives the next exact
selected-versus-distributed bank identity

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

The signs of the face terms are fixed by the oriented pair boundary convention of
Section 1.  Combined with the fixed-current Doob identity on each frozen segment,
this converts selected Kelvin quadratic variation into finite covariance endpoints
plus explicitly tracked physical transfer/exit and signed connection/reset work.
No diagonal refinement or diagonal shell payment appears.

**Classification: Exact conditional identity, conditional only on the still-open
literal equalities `C_irr=G_irr=0`.**

If the literal audit instead gives a nonzero irreducible remainder, the obstruction
is not mysterious.  It enters exactly as

\[
\boxed{
\mathcal O_{\rm irr}
=
\langle\mathbb K,C_{\rm irr}^{(2)}\rangle
+\langle\mathbb K,G_{\rm irr}^{(2)}\rangle\,ds
}
\]

with the two tensor factorizations from Section 5.  Before calling this a new
physical resource one must ask whether it is still an unrecognized physical
interface, connection term, exit face, or finite reset revaluation.  If all those
possibilities have been literally excluded, no finite universal physical bank for
`O_irr` is currently known; it is then a genuine obstruction to this
localization route rather than a quantity to hide with an inequality.

**Classification: Exact obstruction formula; existence of a finite bank for a
nonzero irreducible remainder is open.**
