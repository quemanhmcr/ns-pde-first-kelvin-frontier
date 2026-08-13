# Adversarial audit — 2026-08-13 hybrid/event frontier

Initial pass audited `ad8cd25` (`Separate continuous source revaluation from selected jump qv`);
this note was extended through `eba4aa9` (`Derive adaptive selected-event correlation faces`)
and is now rebased/audited through `884956e` (`Derive enstrophy critical-Hessian
curvature-volume law`), including `9bc8fb0`, `37c635f`, and `c27d1f1`.  The previous
clock/cut/covariance/locality findings have been incorporated upstream; this note does not
reopen them.
Full regression on the rebased audit branch through `884956e`: **610 passed in 121.97s**.
Targeted affine/event/enstrophy/Hessian suite: **103 passed in 28.45s**.

## P0 — frame-aware residual refinement silently drops the local-target change

The frame-aware refinement note proves its raw error identity under an explicit
hypothesis: parent and children are compared against the **same local field**
`omega`.  That hypothesis is essential.

For own-local packet states write

\[
\varepsilon_i=K_i-H_i^T\omega_i,
\qquad
\varepsilon_P=K_P-H_P^T\omega_P,
\]

and retain the exact current/cochain identities

\[
K_P=\sum_i R_iK_i,
\qquad
H_P^T=\sum_iR_iH_i^T.
\]

Then the exact event law is

\[
\boxed{
\varepsilon_P
=\sum_iR_i\varepsilon_i
+\Delta_\omega,
\qquad
\Delta_\omega:=\sum_iR_iH_i^T(\omega_i-\omega_P).
}
\]

Therefore `epsilon_P=sum R_i epsilon_i` holds only when the common-target condition
(or an equivalent cancellation of `Delta_omega`) is actually proved.

This matters downstream because the persistent same-replica library explicitly
allows different anchors for different packets, while the event-normal-form note says
`B` acts on each packet's own co-deforming residual coordinates.  Supplying only the
raw current blocks `R_i` is therefore not enough to determine the own-local residual
event map.

With coherent frames,

\[
A_i=H_P^{-T}R_iH_i^T,
\qquad
B_i=(J_i/J_P)R_i,
\]

but the exact own-local laws are affine:

\[
\boxed{
r_P=\sum_iA_ir_i+H_P^{-T}\Delta_\omega,
}
\]

and

\[
\boxed{
\chi_P
=\sum_i\frac{J_i}{J_P}R_i\chi_i
+\frac1{J_P}\Delta_\omega.
}
\]

Hence `A`/`B` alone are not a complete physical event normal form on an own-anchor
library.  The full second-moment event law also acquires the mean/cross/offset faces
of an affine map; `A tensor A` alone is not the whole revaluation unless
`Delta_omega=0`.

This reaches the latest simultaneous-event theorem directly.  If the physical
library event is actually `chi_+=A chi_-+d_omega`, then with a selector change
`E_- -> E_+` the selected jump is

\[
\boxed{
\Delta Y=(E_+A-E_-)\boldsymbol\chi_-+E_+d_\omega,
}
\]

not only `D boldsymbol chi` with `D=E_+A-E_-`.  The new discrete product-rule algebra
remains exact conditional on a genuinely linear `A`; it does not pay this affine
local-target face.

The same issue reaches the newest continuous-source theorem.  Write each own-local
orientation-noise response as

\[
Q_i=A_{K,i}-H_i^T\nabla\omega_i,
\qquad
Q_P=A_{K,P}-H_P^T\nabla\omega_P.
\]

Current linearity gives `A_{K,P}=sum R_i A_{K,i}`, so

\[
\boxed{
Q_P=\sum_iR_iQ_i+\Delta_{\nabla\omega},
\qquad
\Delta_{\nabla\omega}
:=\sum_iR_iH_i^T(\nabla\omega_i-\nabla\omega_P).
}
\]

Thus the post-event Brownian response is not generically just `A N`.  The latest
`B_+=E_+ A N` and its q.v.-rate revaluation are exact for a genuinely linear
common-target noise event, but an own-local packet event additionally requires the
target-gradient/reanchoring response (and its cross terms in the Gram rate).

### Exact Navier--Stokes witness

Use the exact heat shear

\[
u=(y^3+6\nu ty,0,0),
\qquad
\omega_z=-(3y^2+6\nu t).
\]

Take two equal closed rectangular `xy` loops with `x`-length `l`, `y` half-width
`b`, centered at `y=+a` and `y=-a`, and form the literal parent current as their sum.
For either child, Stokes gives exactly

\[
K_i=2bl(-3a^2-b^2-6\nu t),
\qquad
H_i^T\omega_i=-6bl(a^2+2\nu t),
\]

so

\[
\varepsilon_i=-2b^3l.
\]

Use the natural symmetric parent anchor `y=0`.  The parent current/area identities
remain exact, but

\[
\varepsilon_P
=-12a^2bl-4b^3l,
\qquad
\varepsilon_1+\varepsilon_2=-4b^3l.
\]

Thus

\[
\boxed{
\varepsilon_P-(\varepsilon_1+\varepsilon_2)
=-12a^2bl
=\sum_iH_i^T(\omega_i-\omega_P)\ne0.
}
\]

This scalar `z` channel can be embedded in an invertible orientation-complete packet
by adjoining two auxiliary orthogonal loops whose vorticity flux is identically zero;
the mismatch remains entirely in the `z` block.  Thus this is an exact smooth NSE
counterexample to extending the common-target linear residual refinement law to
own-local child states.  It does **not** contradict the common-target theorem proved
in Section 1 of the frame-aware audit.

**Impact.**  The claims that the surviving refinement seam is only the physical
`R_i` instantiation, that `A`/`B` are complete event normal forms, and that a supplied
`R_i` automatically gives `chi_P=B boldsymbol chi` need one more target-compatibility
hypothesis or one more physical event face.

**Minimal repair.**  Type a packet event on `(current, frame, local target)` rather
than current/frame alone.  Either:

1. prove every event is a common-target refinement and explicitly reanchor the child
   library before applying `A/B`; or
2. retain `Delta_omega` as a signed affine target/reanchoring face, including its
   mean/cross/second-moment terms and its interaction with selector resets.

A regression should use separated anchors in the exact cubic heat shear; the current
frame-aware tests all use one common `omega` (and the quadratic calibration evaluates
all children at the same anchor).

**Classification: P0 proof-support/interface gap.  The common-target current/cochain
identity survives; its downstream promotion to an own-local first-bad event law does
not.**

## P1 — finite-event hybrid calculus does not automatically survive endogenous Zeno switching

The newest hybrid theorem is correct as stated for a supplied selector path with
finitely many jumps.  The actual first-bad event sequence is still undefined, and no
local-finiteness / bounded-variation theorem for that sequence is present.

That missing hypothesis is mathematically active.  In one scalar component of a
same-noise two-germ library, take

\[
d\chi_1=dW,
\qquad
d\chi_2=-dW.
\]

If an endogenous selector chooses germ 1 for `W>=0` and germ 2 for `W<0`, then the
selected path is

\[
Y=|W|.
\]

Each frozen branch is driftless, but Brownian zero crossings accumulate.  Tanaka's
formula gives

\[
\boxed{
|W_t|
=\int_0^t\operatorname{sgn}(W_s)\,dW_s+L_t^0(W),
}
\]

where `L^0` is positive continuous local time.  At every zero crossing the selected
value itself is continuous (`Delta Y=0`), so the formal jump-square payment is zero;
nonetheless the switching limit creates the positive singular-continuous
finite-variation term `L^0`.  It is therefore not represented by a finite sum of
selector jump squares.

This is **not** a counterexample to the current finite-event theorem.  It is a
counterexample to extending that theorem to an endogenous threshold selector without
first proving event local finiteness / genuine hysteresis separation, or adding the
corresponding local-time/interface measure.  The current `bad_flags` and `resolved`
inputs are Boolean oracles, so neither protection is presently available.

**Minimal repair.**  When the physical badness/resolve predicates are finally
specified, prove one of:

- locally finite selector events on every pre-restart interval (for example from a
  nonzero hysteresis band plus sufficient path regularity);
- summable finite-event variation strong enough to pass to the limit; or
- a generalized switching formula retaining the local-time/interface contribution.

**Classification: P1 first-bad closure seam / anti-extension guardrail; no defect in
the explicitly finite-event hybrid identity.**

## P0 propagation on `eba4aa9` — adaptive map faces still need the own-local affine target face

The new `eba4aa9` adaptive-event audit is algebraically correct on its stated pathwise
linear domain: it begins from

\[
C=E_+A,
\qquad
Y_+=C X_-.
\]

But the P0 target mismatch above changes the own-local physical event before any
random-event averaging is done.  In own-local coordinates the event is instead

\[
\chi_+=A\boldsymbol\chi_-+d_\omega,
\qquad
Y_+=E_+A\boldsymbol\chi_-+E_+d_\omega.
\]

Thus, with `C=E_+A` and `b=E_+d_omega`, the literal selected jump is

\[
\boxed{
\Delta Y=(C-E_-)\boldsymbol\chi_-+b.
}
\]

The affine face is not recoverable from event-map dispersion or event/state
correlation of `C` alone.  The same issue appears in the continuous source: if the
own-local residual-noise response changes by `N_target` because the target gradient
changes, then

\[
\boxed{
B_+=E_+(A\mathcal N+N_{\rm target}),
}
\]

not merely `E_+A\mathcal N`.  Its q.v. Gram therefore contains the two signed cross
terms with `N_target` and the `N_target N_target^T` face.

### Exact one-loop reanchoring calibration

The cubic heat shear already used above gives a particularly sharp referee because
one can keep the **same physical current and frame** and change only the local target.
For

\[
u=(y^3+6\nu t\,y,0,0),
\qquad
\omega_z=-(3y^2+6\nu t),
\]

take one closed rectangular `xy` loop of `x`-length `l`, `y` half-width `b`, centered
at `y=a`.  Its exact circulation and scalar oriented-area readout are

\[
K=2bl(-3a^2-b^2-6\nu t),
\qquad
H=2bl.
\]

Against its own target `omega(a)`,

\[
\varepsilon_a=K-H\omega(a)=-2b^3l.
\]

Reanchor the **same current/frame** against `omega(0)`.  The raw current map is still
`A=I`, but

\[
\boxed{
\varepsilon_0
=K-H\omega(0)
=-6a^2bl-2b^3l,
\qquad
\varepsilon_0-\varepsilon_a=-6a^2bl\ne0.
}
\]

The Brownian `y`-translation coefficient is equally decisive.  Since

\[
A_K=\partial_aK=-12abl,
\qquad
H\,\partial_y\omega_z(a)=-12abl,
\qquad
H\,\partial_y\omega_z(0)=0,
\]

we get

\[
\boxed{
Q_a=0,
\qquad
Q_0=-12abl.
}
\]

So a pure reanchoring event with `A=I` changes the scalar continuous q.v. rate from
zero to

\[
2\nu(12abl)^2>0.
\]

This is exactly the type of own-local target-gradient response that cannot be seen by
randomness of `C` alone.  The scalar channel can again be embedded in an
orientation-complete packet without changing the mismatch.

**Classification: propagation of the existing P0 into `eba4aa9`, not a new
independent defect.  The new two-replica correlation algebra survives on the
common-target / genuinely linear event domain.**

## Affine/reanchoring composition audit — the physical coboundary is functorial, the reduced stochastic moment state is not

The P0 repair has more structure than an arbitrary additive correction.  It is useful
to separate the **unreanchored physical current/frame readout** from the own-local
choice of vorticity origin.  Write, on a stacked packet library,

\[
z:=x+\Omega,
\]

where `x` is the reconstructed residual state and `Omega` stacks the local vorticity
targets.  A specified current/frame event acts linearly on `z`:

\[
z_+=A z_-.
\]

Therefore the exact own-local residual event is

\[
\boxed{
x_+=A x_-+d,
\qquad
d=A\Omega_- - \Omega_+.
}
\]

For one parent synthesized from children this is exactly the earlier P0 face

\[
d=\sum_i A_i\omega_i-\omega_P
  =H_P^{-T}\Delta_\omega,
\]

because area compatibility gives `sum_i A_i=I`.  Thus the affine term is a physical
target **coboundary**, not an arbitrary extra forcing.  In coherent Nanson/cofactor
coordinates, `H^T=J L^{-1}` and `B_i=(J_i/J_P)R_i`, so the same statement is

\[
\chi_+=B\chi_-+d_\chi,
\qquad
d_\chi=B\Omega_{\chi,-}-\Omega_{\chi,+},
\qquad
\Omega_{\chi,g}=L_g^{-1}\omega_g.
\]

Thus the affine repair is compatible with the repo's Nanson/cofactor geometry; it is
not a separate coordinate artifact.

### Hypotheses of the affine composition statement

The theorem below is conditional on the same finite-event domain as the surviving
linear normal form, with the target data added explicitly:

- endpoint orientation-complete area frames are invertible and satisfy the exact
  current/area compatibility used to define `A` (or coherent `L,H=cof(L)` data for `B`);
- the raw/current event is a **supplied finite event** and sequential raw maps really
  compose to the same direct current map;
- `Omega_-`, `Omega_+` are the actual own-local vorticity targets at the event, not
  observer-chosen surrogates;
- the adjacent continuous intervals use the same physical Wiener driver, while the
  shape/frame variables and supplied event map have no continuous martingale part
  (the repo's finite-variation frame hypothesis); and
- selector readouts are frozen on the two adjacent intervals.  Endogenous switching
  accumulation is still the separate P1 seam.

No support-locality, first-bad admissibility, or regularity conclusion follows from
these hypotheses.

### Sequential affine events compose exactly

For two supplied events,

\[
x_1=A_1x_0+d_1,
\qquad
d_1=A_1\Omega_0-\Omega_1,
\]

and

\[
x_2=A_2x_1+d_2,
\qquad
d_2=A_2\Omega_1-\Omega_2,
\]

ordinary affine composition gives

\[
\boxed{
x_2=A_2A_1x_0+A_2d_1+d_2.}
\]

The intermediate target cancels:

\[
\boxed{
A_2d_1+d_2
=A_2A_1\Omega_0-\Omega_2.
}
\]

Hence, whenever the underlying current/frame maps themselves compose,

\[
A_{20}=A_{21}A_{10},
\]

the **direct own-local reanchor and the sequential own-local reanchor agree exactly**.
For a pure target change with the current/frame fixed, `A=I` and

\[
d_{a\to b}=\omega(a)-\omega(b),
\]

so `d_{a->b}+d_{b->c}=d_{a->c}` pathwise.  There is no new path-dependence defect in
the physical reanchoring itself.

Equivalently, for supplied event data the homogeneous matrix

\[
\widetilde A=
\begin{pmatrix}
A&d\\
0&1
\end{pmatrix}
\]

composes exactly.  This is a valid **pathwise/conditional** affine normal form.

The qualification is stochastic and important.  In the actual own-local library,

\[
\Omega_g=\omega(X_g,t),
\]

so the targets are adapted random state variables, and the frame-derived `A` may also
be random finite variation.  Thus `d=A Omega_- - Omega_+` is generally random and
correlated with `x`.  The homogeneous lift does **not** turn the unconditional
first-bad law into a fixed linear moment closure: one needs the joint law of the
realized event data and the state.

### Exact second-moment and covariance faces

Pathwise, with `Q=xx^T`,

\[
\boxed{
Q_+
=AQA^T+Axd^T+dx^TA^T+dd^T.
}
\]

If `A,d` are deterministic and `mu=E x`, `M=E[xx^T]`, then

\[
\boxed{
\mu_+=A\mu+d,
}
\]

and

\[
\boxed{
M_+=AMA^T+A\mu d^T+d\mu^TA^T+dd^T.
}
\]

The centered covariance is then simply `A Cov(x) A^T`; the offset cancels only
because it is deterministic.  Equivalently, for deterministic supplied event data,

\[
\widetilde M=
E\!\left[
\begin{pmatrix}x\\1\end{pmatrix}
\begin{pmatrix}x\\1\end{pmatrix}^{T}
\right]
=
\begin{pmatrix}M&\mu\\\mu^T&1\end{pmatrix}
\]

obeys

\[
\widetilde M_+=\widetilde A\widetilde M_-\widetilde A^T.
\]

Thus direct and sequential **state, mean, raw second moment, and centered covariance**
are path-independent when the full fixed affine event data are carried.  The reduced
raw second moment `M` alone is not closed because it has forgotten `mu` and the
offset faces.  If `A` is fixed but `d` is random,

\[
\boxed{
E[x_+x_+^T]
=AMA^T
+A E[xd^T]
+E[dx^T]A^T
+E[dd^T],
}
\]

and

\[
\boxed{
\operatorname{Cov}(x_+)
=A\operatorname{Cov}(x)A^T
+A\operatorname{Cov}(x,d)
+\operatorname{Cov}(d,x)A^T
+\operatorname{Cov}(d).
}
\]

When `A` is also adaptive/random, the exact object is the full joint expectation

\[
E\!\left[
Axx^TA^T+Axd^T+dx^TA^T+dd^T
\right],
\]

with the corresponding mean subtraction for covariance.  Therefore `A tensor A`
is still the correct pair functor for a **fixed linear event**, but it is not the
complete own-local affine second-moment event.

### Simultaneous selector plus affine physical event

Let

\[
C=E_+A,
\qquad F=E_-,
\qquad D=C-F,
\qquad b=E_+d.
\]

Then

\[
Y_-=FX,
\qquad
Y_+=CX+b,
\]

and the literal selected jump is

\[
\boxed{
\Delta Y=DX+b.
}
\]

The pathwise dyad reset is

\[
\boxed{
\begin{aligned}
\Delta(YY^T)
={}&DQF^T+FQD^T+DQD^T\\
&+FXb^T+bX^TF^T\\
&+DXb^T+bX^TD^T+bb^T,
\end{aligned}
}
\]

where `Q=XX^T`.  The first line is the existing linear combined-event law.  The
remaining lines are the affine target faces.  In particular the optional jump q.v.
atom is

\[
\boxed{
(\Delta Y)(\Delta Y)^T
=DQD^T+DXb^T+bX^TD^T+bb^T.
}
\]

Thus the linear jump square `DQD^T` alone misses the cross terms between the linear
jump and the reanchoring face, as well as the offset dyad.

### Continuous q.v. response also has an exact target coboundary

Let `G` stack the target vorticity-gradient matrices and let `N` denote the own-local
Brownian response before the common factor `sqrt(2 nu)`.  The same current linearity
gives

\[
\boxed{
N_+=A N_-+N_{\rm target},
\qquad
N_{\rm target}=A G_- - G_+.
}
\]

This is the gradient analogue of `d=A Omega_- - Omega_+`.  It is also functorial:
for two sequential events,

\[
N_2=A_2A_1N_0+A_2N_{{\rm target},1}+N_{{\rm target},2},
\]

and the intermediate target gradient cancels exactly against the direct endpoint
formula.

Without selector notation, the post-event continuous Gram is

\[
\boxed{
\begin{aligned}
2\nu N_+N_+^T
=2\nu\bigl[{}
&A N_-N_-^TA^T
+A N_-N_{\rm target}^T\\
&+N_{\rm target}N_-^TA^T
+N_{\rm target}N_{\rm target}^T
\bigr].
\end{aligned}
}
\]

With a selector, set `b_N=E_+N_target`.  Then

\[
B_-=F N,
\qquad
B_+=C N+b_N,
\]

so the rate revaluation has the same left/right/quadratic product rule with
`delta B=DN+b_N`.  The existing `DN` faces survive, but there are additional signed
cross terms with `b_N` and the positive `b_N b_N^T` endpoint face.  Because
`G_g=grad omega(X_g,t)` is random/adapted, expectation-level source bookkeeping again
requires the event/state/target-gradient joint law.

### Exact Navier--Stokes path-independence referees

The cubic heat shear used in P0 is already enough.  For

\[
U_3(y,t)=y^3+6\nu t y,
\qquad
u_3=(U_3,0,0),
\qquad
\omega_{3,z}=-(3y^2+6\nu t),
\]

`U_{3,t}-nu U_{3,yy}=0`, the nonlinear term vanishes identically, and constant
pressure gives an exact smooth 3D Navier--Stokes solution.  Its vorticity equation is
also literal: `u dot grad omega=0`, `omega dot grad u=0`, and
`omega_t-nu Delta omega=-partial_y(U_t-nu U_yy)=0`.  Keep one rectangular
`xy` loop centered at `y=a`, with `x`-length `l`, `y` half-width `b`, and reanchor only
the local target to `y=p`.  Then

\[
K=-2bl(3a^2+b^2+6\nu t),
\qquad H=2bl,
\]

\[
\boxed{
\varepsilon_p=2bl(-3a^2-b^2+3p^2),
}
\]

and the `y`-Brownian residual response is

\[
\boxed{
Q_p=12bl(p-a).
}
\]

For arbitrary targets `p,q,r`, direct calculation gives

\[
\varepsilon_q-\varepsilon_p-H(\omega(p)-\omega(q))=0,
\]

\[
H(\omega(p)-\omega(q))+H(\omega(q)-\omega(r))
-H(\omega(p)-\omega(r))=0,
\]

and exactly the same two identities with `omega` replaced by `partial_y omega` for
`Q`.  Thus state and noise reanchoring are path-independent on this exact NSE witness.

An independent nonlinear-gradient calibration uses the quartic heat shear

\[
U_4(y,t)=y^4+12\nu t y^2+12\nu^2t^2,
\qquad
\omega_{4,z}=-(4y^3+24\nu t y),
\]

which again satisfies `U_{4,t}-nu U_{4,yy}=0`.  For the same fixed loop,

\[
K=-8abl(a^2+b^2+6\nu t),
\]

\[
\boxed{
\varepsilon_p
=8bl(-a^3-ab^2-6a\nu t+p^3+6\nu pt),
}
\]

and

\[
\boxed{
Q_p=8bl(-3a^2-b^2+3p^2).
}
\]

Here `partial_y omega` is genuinely nonlinear in the target anchor, yet the direct
and sequential target/noise offsets still telescope exactly.  Symbolic checks were
used only as a referee for these hand-derived identities.

### Dimensional check

In physical reconstructed coordinates,

- `K` and raw `epsilon` have units `L^2/T`;
- `H` has units `L^2`;
- `x=r=H^{-T}epsilon` and `d` have units `1/T`;
- `A`, `E_+`, `E_-`, `C`, and `D` are dimensionless;
- `N` and `N_target`, before multiplication by `sqrt(2 nu)`, have units `1/(L T)`;
- therefore `2 nu N N^T` has units `1/T^3`, the correct rate for a `1/T^2`
  residual dyad.

Every affine cross term above has the same dimensions as the object it corrects.  The polynomial
heat-shear witnesses are calibration formulas in nondimensionalized coordinates; restoring
physical units only inserts the corresponding amplitude/length scales and does not change the
reanchoring identities.

### Classification

This deeper composition audit finds **no independent new P-level defect**.

- The exact physical reanchoring offset is a target coboundary and sequential
  reanchoring is functorial/path-independent when the underlying specified
  current/frame events compose.
- The existing P0 nevertheless propagates through the repo's linear event normal
  form, second-moment functor, selected jump/dyad law, and continuous q.v. push unless
  the theorem is explicitly restricted to common-target/genuinely linear events or
  the affine target state is retained.
- The simple homogeneous coordinate is an exact pathwise representation for supplied
  `(A,d)`, but it is **not** an unconditional stochastic moment closure when `A,d`
  depend on own-local anchors, `omega`, or other state.
- `9bc8fb0`'s passive-gauge identity for the linear block `A` survives.  Its wording
  `physical event map A` must be read in the common-target/linear-component scope;
  treating `A` as the complete own-local event would be the already identified P0,
  not a new issue in the admissibility theorem.
- P1 (endogenous Zeno/local time) and P2 (two-replica versus population closure)
  are unchanged guardrails.

**Classification: exact affine composition theorem plus downstream propagation of P0;
no new independent P-level finding.**

## P2 guardrail — the two-replica four-face identity is not a population four-face closure

The `eba4aa9` four-face identity is exact for **two equal-weight replicas** as stated.
A separate guardrail is needed before it is promoted to a general expectation law by
replacing pair bars with population means.

Let

\[
\mu_C=\mathbb E C,
\qquad
\mu_Q=\mathbb E Q,
\qquad
\delta C=C-\mu_C,
\qquad
\delta Q=Q-\mu_Q.
\]

For a general random event/payload pair,

\[
\boxed{
\begin{aligned}
\mathbb E[CQC^T]
={}&\mu_C\mu_Q\mu_C^T
+\mathbb E[\delta C\,\mu_Q\,\delta C^T]\\
&+\mu_C\,\mathbb E[\delta Q\,\delta C^T]
+\mathbb E[\delta C\,\delta Q]\,\mu_C^T\\
&+\mathbb E[\delta C\,\delta Q\,\delta C^T].
\end{aligned}
}
\]

The last centered triple face vanishes automatically in the symmetric two-point
representation used by the current audit, but it need not vanish for a general
adaptive event law.

A scalar PSD three-state witness is enough.  Give equal probability to

\[
(C,Q)=(0,1),(1,0),(2,1).
\]

Then

\[
\mu_C=1,
\qquad
\mu_Q=\frac23,
\qquad
\mathbb E[C^2Q]=\frac43.
\]

The population mean-map face is `2/3`, the dispersion face is `4/9`, and both linear
correlation faces vanish.  They sum only to `10/9`.  The missing amount is exactly

\[
\boxed{
\mathbb E[(C-1)^2(Q-2/3)]=\frac29.
}
\]

This does **not** refute the repo's exact two-replica identity.  If one averages that
whole pair identity without factorizing its random pair-bars, it remains exact.  It
only forbids the later shortcut “pair four faces = four population-mean faces” for a
general first-bad distribution.

**Minimal guardrail.**  At actual first-bad expectation level, either retain
`E[C Q C^T]` as a joint-law object, use an explicitly conditioned decomposition, or
include the centered triple face above.  Do not silently identify the pair averages
with population means.

**Classification: P2 anti-extension guardrail; no defect in the explicitly scoped
two-replica theorem.**

## Upstream delta through `c27d1f1` — enstrophy/Kelvin growth and critical-point motion survive in their stated domains

Two commits landed while the affine audit was running:

- `37c635f` — `Type local enstrophy growth through Kelvin bulk and curvature`;
- `c27d1f1` — `Derive nondegenerate enstrophy critical-point speed law`.

They were audited as PDE statements before rebasing the audit branch.

### Local enstrophy three-face law

For

\[
e=\frac12|\omega|^2,
\qquad S=\frac12(\nabla u+\nabla u^T),
\]

the vorticity equation gives exactly

\[
\boxed{
(\partial_t+u\cdot\nabla-\nu\Delta)e
=\omega\cdot S\omega-\nu|\nabla\omega|_F^2.
}
\]

At a spatial critical point `grad e=0`,

\[
\boxed{
\partial_t e
=\omega\cdot S\omega
-\nu|\nabla\omega|_F^2
+\nu\Delta e.
}
\]

For an invertible orientation-complete area frame `H`, the infinitesimal Kelvin
Brownian packet Gram

\[
\Gamma_H=2\nu H^T(\nabla\omega)(\nabla\omega)^T H
\]

and packet metric `M_H=(H^TH)^{-1}` satisfy

\[
\boxed{
\frac12\operatorname{tr}(\Gamma_HM_H)
=\nu|\nabla\omega|_F^2.
}
\]

This follows by cyclicity of trace and invertibility of `H`; no estimate or isotropy
assumption is used.  Thus the repo's Kelvin-bulk typing has the right factor and
orientation content.

At a local maximum `Delta e<=0`, if

\[
G=\omega\cdot S\omega-\nu|\nabla\omega|_F^2,
\]

then

\[
\partial_t e=G+\nu\Delta e\le G.
\]

Consequently `G>0` is necessary for positive instantaneous growth but is not
sufficient unless the curvature face is retained.  The commit states exactly this
scope and does not promote the gate to a first-bad or regularity criterion.

The exact affine-vortex calibration also survives direct PDE checking.  With

\[
A(t)=
\begin{pmatrix}
-a&-r(t)&0\\
r(t)&-a&0\\
0&0&2a
\end{pmatrix},
\qquad r(t)=r_0e^{2at},
\qquad u=A(t)x,
\]

`tr A=0` and `-(\dot A+A^2)` is symmetric, so a quadratic pressure exists and

\[
\partial_tu+(u\cdot\nabla)u+\nabla p-\nu\Delta u=0
\]

exactly.  Its uniform vorticity is `(0,0,2r)`, hence `grad omega=0`, while

\[
\partial_t e=\omega\cdot S\omega=8ar(t)^2.
\]

This is a smooth local growth mechanism, but the velocity is affine in space and the
repo correctly excludes it from the periodic/finite-energy target class.

**Classification: exact PDE/Kelvin identities and an exact smooth-NS calibration;
no new P-level gap.**

### Nondegenerate enstrophy critical-point speed

Suppose a differentiable critical branch satisfies

\[
\nabla e(x_*(t),t)=0
\]

and its Hessian `H_e=grad^2 e` is invertible.  Differentiating the constraint gives

\[
H_e\dot x_*+\partial_t\nabla e=0.
\]

Writing the exact critical-value source as

\[
R=\omega\cdot S\omega-\nu|\nabla\omega|_F^2+\nu\Delta e,
\]

the spatial gradient of the enstrophy PDE gives, at `grad e=0`,

\[
\partial_t\nabla e=-H_eu+\nabla R.
\]

Therefore

\[
\boxed{
H_e(\dot x_*-u)+\nabla R=0,
\qquad
\dot x_*-u=-H_e^{-1}\nabla R.
}
\]

The three relative-speed faces in `c27d1f1` have the correct signs:

\[
-H_e^{-1}\nabla(\omega\cdot S\omega)
+H_e^{-1}\nabla(\nu|\nabla\omega|_F^2)
-\nu H_e^{-1}\nabla\Delta e.
\]

The dimensions also close: `H_e` has units `1/(L^2T^2)`, `grad R` has units
`1/(LT^3)`, and `H_e^{-1}grad R` has velocity units `L/T`.

The exact periodic ABC referee survives independently: at
`(pi/4,pi/4,pi/4)` the enstrophy gradient vanishes, the Hessian is negative definite
with determinant `-A^6 exp(-6 nu t)/2`, the critical point is fixed, and the formula
reconstructs `dot x_*=0` while the fluid velocity is nonzero.  The affine-vortex
uniform-enstrophy calibration correctly lands outside the inverse-Hessian theorem
because `H_e=0` and the critical-lineage speed is nonunique.

There is one theorem-domain hypothesis worth keeping explicit: the differentiated
PDE formula requires enough classical spatial regularity to make `grad Delta e` and
the other source gradients meaningful, in addition to a differentiable
nondegenerate critical branch.  In the smooth exact-NS domain used by these audits
this is satisfied; it is not a new continuation theorem and does not extend through
Hessian degeneracy without additional branch/event calculus.

The repo also correctly keeps this critical-point velocity distinct from the moving
quantile/shell law and from the hysteretic first-bad selector.  In particular it does
not repair or invalidate P1: branch creation/loss, Hessian degeneracy, and endogenous
selector accumulation remain separate event questions.

**Classification: exact conditional smooth-NS identity with a regularity/nondegeneracy
guardrail; no independent new P-level finding.**

## Upstream delta `884956e` — critical-Hessian curvature-volume law also survives, with a stronger smoothness/event guardrail

The next upstream commit derives the Hessian evolution along the same conditional
enstrophy critical branch.  For a scalar equation

\[
\partial_t e+u\cdot\nabla e=R,
\qquad
\nabla e(x_*(t),t)=0,
\qquad
H=\nabla^2e,
\]

taking two spatial derivatives and then differentiating along the moving critical
path gives exactly

\[
\boxed{
\frac{d_*H}{dt}
=\nabla^2R
-(\nabla u)^TH-H\nabla u
+((\dot x_*-u)\cdot\nabla)H.
}
\]

The term involving `Hess u` contracts with `grad e` and therefore vanishes only on
the critical branch.  The remaining connection matrix is

\[
C_{\rm conn}=-(\nabla u)^TH-H\nabla u.
\]

For invertible `H`, cyclicity of trace gives the exact log-determinant contribution

\[
\boxed{
\operatorname{tr}(H^{-1}C_{\rm conn})
=-2\operatorname{tr}(\nabla u)
=-2\nabla\cdot u.
}
\]

Thus incompressibility removes the **direct connection contribution to the scalar
curvature-volume rate**, not the connection matrix itself.  With
`grad u=S+W`,

\[
C_{\rm conn}=-(SH+HS)+(WH-HW),
\]

and separately

\[
\operatorname{tr}\!\left[H^{-1}(-(SH+HS))\right]=-2\operatorname{tr}S,
\qquad
\operatorname{tr}\!\left[H^{-1}(WH-HW)\right]=0.
\]

So strain and rotation may still reshape or rotate the Hessian while their
log-determinant contribution vanishes in incompressible flow.

Jacobi's formula then gives, on an already smooth nondegenerate incompressible branch,

\[
\boxed{
\frac d{dt}\log|\det H|
=\operatorname{tr}(H^{-1}\nabla^2R)
+\operatorname{tr}\!\left[
H^{-1}((\dot x_*-u)\cdot\nabla)H
\right].
}
\]

The determinant representation

\[
\det H(t)=\det H(t_0)
\exp\!\left(\int_{t_0}^t
\operatorname{tr}(H^{-1}\dot H)\,ds\right)
\]

is exact on the nondegenerate interval.  Therefore a finite real limit of the
integrated log-rate prevents `det H` from tending continuously to zero from a nonzero
initial value.  Conversely, continuous degeneration forces that integral to tend to
`-infinity`.  This is a taut but useful critical-geometry criterion; it is **not** a
Navier--Stokes continuation estimate because no uniform control of that log-rate is
proved.

An independent cubic-scalar/incompressible-affine-flow referee gives zero residual in
the full moving-Hessian identity while the connection matrix is nonzero and its
logdet contribution is exactly zero.  The periodic ABC calibration is also
consistent: `Hdot=-2 nu H`, hence

\[
\frac d{dt}\log|\det H|=-6\nu,
\qquad
\det H=-\frac12A^6e^{-6\nu t},
\]

which stays nonzero at every finite time.

The dimensional typing closes:

- `H` has units `L^{-2}T^{-2}`;
- every Hessian-evolution face has units `L^{-2}T^{-3}`;
- each contracted log-determinant rate has units `T^{-1}`.

The theorem-domain guardrail is stronger than at the speed layer.  The enstrophy
specialization contains `Hess R` with `R` itself containing `nu Delta e`, and the
relative face contains `grad H`; the identity therefore presupposes enough classical
spatial regularity for these higher derivatives, in addition to a differentiable
critical branch and `det H != 0` wherever `H^{-1}` or `log|det H|` is used.

Finally, a loss of Hessian nondegeneracy is a genuine boundary of this coordinate
chart, but it does **not** by itself supply a locally finite selector event.  Branch
creation/annihilation/merging or repeated degeneracy may still require separate event
calculus, and no theorem here rules out accumulation.  This is the existing P1/open
first-bad seam, not a new defect in the conditional Hessian identity.

**Classification: exact conditional critical-Hessian/Jacobi theorem plus smoothness,
nondegeneracy, and P1 event guardrails; no independent new P-level finding.**

## Status

The reverse-age Kelvin martingale core, common-noise library Gram law, signed
cross-germ content, finite-event optional-q.v. decomposition, exact two-replica adaptive-event
identity, and the target-coboundary affine composition law were independently stress-tested.
No new local algebra defect was found inside their stated theorem domains.  The affine event
itself is path-independent/functorial; the unresolved P0 issue is completeness of the own-local
state/noise/moment interface when the target data are random and state-dependent.

The new decisive interface is now:

\[
\boxed{
\text{own-local packet library}
\to
\text{target-compatible affine state + noise event}
\to
\text{adaptive joint-law bookkeeping}
\to
\text{endogenous locally-finite first-bad selector}
\to
\text{hybrid bank/restart calculus}.
}
\]

No restart/continuation/regularity theorem is claimed or refuted here.
