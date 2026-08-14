# Causal heat-ray projective zero-curvature master law

## Purpose

The repository had already reduced two large parts of Navier--Stokes to canonical
heat geometry:

1. the positive heat-scale energy density obeys one scalar continuity law;
2. the normalized energy ray obeys one Lax/double-bracket law.

The energy-ray theorem explicitly left open whether these two Lax structures satisfy
a stronger zero-curvature compatibility.  This note closes that structural question
on every smooth interval.

Let

\[
A=C^2=-\Delta,
\qquad
S_h:=e^{-hA/2},
\qquad h\ge0,
\]

and heat-resolve the actual velocity by

\[
\boxed{
u_h(t):=S_hu(t).}
\]

Write

\[
\boxed{
r_h:=\|u_h\|_2,
\qquad
q_h:=\frac{u_h}{r_h},
\qquad
\mathsf P_h:=q_h\otimes q_h.
}
\]

The heat-age derivative is the normalized Brockett/double-bracket flow

\[
\boxed{
\partial_h\mathsf P_h
=\left[\frac12[\mathsf P_h,A],\mathsf P_h\right].
}
\]

Introduce the causal parabolic characteristic derivative

\[
\boxed{
\mathcal D_\nu
:=\partial_t-2\nu\partial_h.
}
\]

Then the viscous square cancels exactly:

\[
\boxed{
\mathcal D_\nu u_h
=S_hX_E(u),
\qquad
X_E(u)=P_\sigma(u\times Cu).
}
\]

After normalization,

\[
\boxed{
\mathcal D_\nu\mathsf P_h
=[\Gamma_h^E,\mathsf P_h],
}
\]

where `Gamma_h^E` is the canonical rank-two connection of the heat-resolved Euler
ray velocity.

The two flows commute projectively.  If

\[
B_h:=\frac12[\mathsf P_h,A],
\]

then

\[
\boxed{
\left[
\partial_h\Gamma_h^E
-\mathcal D_\nu B_h
+[\Gamma_h^E,B_h],
\mathsf P_h
\right]=0.
}
\]

This is the exact projective zero-curvature law which the earlier energy-ray theorem
left open.

There is a stronger physical compression.  Define the one heat-renormalization
defect

\[
\boxed{
\mathfrak N_h(u)
:=P_\sigma\!\left[
S_h(u\times Cu)
-(S_hu)\times(S_hCu)
\right].
}
\]

Because `S_h`, `C` and the Leray projector commute,

\[
\boxed{
S_hX_E(u)
=X_E(u_h)+\mathfrak N_h(u).
}
\]

The same `mathfrak N_h` has two forced projections:

- its radial component is exactly the canonical heat-scale nonlinear energy flux;
- its tangent component is exactly the anomaly between the Euler ray connection of
  the heat-smoothed state and the heat-smoothed Euler connection of the actual state.

Explicitly, if `Pi_heat(h,t)` is the existing canonical nonlinear scale flux, then

\[
\boxed{
\langle q_h,\mathfrak N_h\rangle
=-\frac{\Pi_{\rm heat}(h,t)}{r_h},
}
\]

while

\[
\boxed{
(\mathcal D_\nu q_h)
=\frac{X_E(u_h)}{r_h}
+\frac1{r_h}(I-\mathsf P_h)\mathfrak N_h.
}
\]

Moreover `mathfrak N_h` is exactly the cross-product heat
carré-du-champ/product defect already proved earlier.  Thus scalar cascade and
directional ray renormalization are not two heat mechanisms.  They are the radial
and tangent faces of one canonical vector defect.

Finally, the old scalar heat continuity equation is itself the radial curvature-zero
condition of this lifted system.  With

\[
\mathcal E(h,t)=\frac12r_h^2,
\qquad
\rho=-\partial_h\mathcal E,
\]

one has

\[
\boxed{
\partial_h\mathcal E=-\rho,
\qquad
\mathcal D_\nu\mathcal E=-\Pi_{\rm heat}.
}
\]

Commutation of `partial_h` and `D_nu` gives exactly

\[
\boxed{
\partial_t\rho
-\partial_h(2\nu\rho+\Pi_{\rm heat})=0.
}
\]

Hence the scalar heat continuity law and the projective ray zero-curvature law are
two components of one flat heat--time lift of Navier--Stokes.

No no-escape, continuation, restart, blow-up exclusion or global-regularity theorem
is claimed.  The remaining escape can live only as a singular boundary
concentration of this projectively flat self-generated connection at the parabolic
corner `h=0`.

---

## 1. The unnormalized heat lift absorbs the viscous square into heat-age translation

The physical velocity equation is

\[
\partial_tu
=X_E(u)-\nu Au.
\]

Since

\[
\partial_hS_h=-\frac12AS_h,
\]

one has

\[
\begin{aligned}
\mathcal D_\nu u_h
&=(\partial_t-2\nu\partial_h)S_hu\\
&=S_h(X_E-\nu Au)+\nu AS_hu\\
&=S_hX_E.
\end{aligned}
\]

Therefore

\[
\boxed{
(\partial_t-2\nu\partial_h)u_h
=S_hX_E(u).
}
\]

This is not a mild approximation.  It is an exact two-variable rewrite of the
literal smooth PDE.

Along a characteristic

\[
\dot h=-2\nu,
\]

the explicit viscous generator disappears.  In the lifted plane, viscosity is
translation toward the heat-age boundary while the remaining characteristic forcing
is exactly the heat image of the Euler vector.

**Classification: Exact heat-lift identity.**

---

## 2. The heat-age ray is a canonical double-bracket gradient flow

At fixed physical time, differentiate

\[
u_h=S_hu,
\qquad
r_h=\|u_h\|,
\qquad
q_h=u_h/r_h.
\]

Define

\[
\mu_h:=\langle q_h,Aq_h\rangle.
\]

Then

\[
\boxed{
\partial_hr_h
=-\frac12r_h\mu_h,
}
\]

and

\[
\boxed{
\partial_hq_h
=-\frac12(A-\mu_h)q_h.
}
\]

Let

\[
\mathsf P_h=q_h\otimes q_h.
\]

The skew rank-two heat connection is

\[
\boxed{
B_h
:=\frac12[\mathsf P_h,A].
}
\]

Indeed

\[
B_hq_h
=-\frac12(A-\mu_h)q_h
=\partial_hq_h.
\]

Therefore

\[
\boxed{
\partial_h\mathsf P_h
=[B_h,\mathsf P_h]
=-\frac12[\mathsf P_h,[\mathsf P_h,A]].
}
\]

Thus heat age is exactly the Brockett/double-bracket sorting flow of the energy ray
relative to the fixed positive Hodge square.

No spectral coordinate or cascade model has been added.

**Classification: Exact normalized heat/double-bracket identity.**

---

## 3. Along the causal heat characteristic the normalized ray has no explicit viscous leg

Let

\[
X_E(u)=P_\sigma(u\times Cu).
\]

From Section 1,

\[
\mathcal D_\nu u_h=S_hX_E(u).
\]

The radius derivative is

\[
\boxed{
\mathcal D_\nu r_h
=\langle q_h,S_hX_E(u)\rangle.
}
\]

Hence the normalized ray satisfies

\[
\boxed{
a_h^E
:=\mathcal D_\nu q_h
=\frac1{r_h}(I-\mathsf P_h)S_hX_E(u).
}
\]

Define its canonical rank-two skew connection

\[
\boxed{
\Gamma_h^E
:=a_h^E\otimes q_h-q_h\otimes a_h^E.
}
\]

Then

\[
\boxed{
\mathcal D_\nu\mathsf P_h
=[\Gamma_h^E,\mathsf P_h].
}
\]

The normalized lifted dynamics therefore separate exactly into

\[
\boxed{
\begin{array}{rcl}
\partial_h\mathsf P_h
&=&[B_h,\mathsf P_h]
\quad\text{(pure positive Hodge sorting)},\\[1mm]
\mathcal D_\nu\mathsf P_h
&=&[\Gamma_h^E,\mathsf P_h]
\quad\text{(pure heat-resolved Euler ray rotation)}.
\end{array}
}
\]

The word `pure` here means only that the explicit `-nu A` leg has been absorbed into
the characteristic.  The Euler connection itself still contains the heat
renormalization anomaly derived below.

**Classification: Exact causal normalized-ray law.**

---

## 4. One heat-product anomaly generates both scalar cascade and directional connection defect

Because `S_h` commutes with the Leray projector and with `C`,

\[
\begin{aligned}
S_hX_E(u)
&=P_\sigma S_h(u\times Cu),\\
X_E(u_h)
&=P_\sigma\bigl((S_hu)\times(S_hCu)\bigr).
\end{aligned}
\]

Define

\[
\boxed{
\mathfrak N_h
:=S_hX_E(u)-X_E(u_h).
}
\]

Equivalently,

\[
\boxed{
\mathfrak N_h
=P_\sigma\!\left[
S_h(u\times Cu)
-(S_hu)\times(S_hCu)
\right].
}
\]

Then

\[
\boxed{
\mathcal D_\nu u_h
=X_E(u_h)+\mathfrak N_h.
}
\]

The intrinsic Euler vector of `u_h` is energy-skew:

\[
\langle u_h,X_E(u_h)\rangle=0.
\]

Therefore the radial component of the single defect is

\[
\boxed{
\mathcal D_\nu r_h
=\langle q_h,\mathfrak N_h\rangle.
}
\]

The tangent component is

\[
\boxed{
\mathcal D_\nu q_h
=\frac{X_E(u_h)}{r_h}
+\frac1{r_h}(I-\mathsf P_h)\mathfrak N_h.
}
\]

Thus the same vector `mathfrak N_h` splits exactly into

\[
\boxed{
\text{radial heat-scale energy transfer}
+\text{tangent Euler-connection renormalization}.
}
\]

This is the key physical compression of the heat lift.

**Classification: Exact radial/tangent decomposition of one heat-renormalization defect.**

---

## 5. The renormalization defect is exactly the existing heat carré-du-champ anomaly

Let

\[
P_s=e^{-sA}.
\]

Since

\[
S_h=P_{h/2},
\]

the cross-product heat defect from the earlier heat-null theorem gives

\[
\boxed{
\begin{aligned}
\mathfrak N_h
&=2P_\sigma\int_0^{h/2}
P_{h/2-r}
\sum_{k=1}^3
\bigl(
\partial_kP_ru\times\partial_kP_rCu
\bigr)\,dr.
\end{aligned}
}
\]

Hence `mathfrak N_h` is generated entirely by the failure of the Hodge heat square to
be a derivation of the alternating product.

At the heat boundary,

\[
\boxed{
\mathfrak N_0=0.
}
\]

Therefore the heat-resolved Euler connection agrees with the literal Euler
connection at `h=0`; all nontrivial coarse-scale difference is accumulated by the
same carré-du-champ defect already responsible for the canonical scale flux and the
critical heat-null transfer.

No new nonlinear source has appeared.

**Classification: Exact descent to the established heat-product/carré-du-champ identity.**

---

## 6. The canonical scale flux is the radial projection of the same defect

The heat-resolved energy is

\[
\boxed{
\mathcal E(h,t)
:=\frac12\|u_h\|_2^2
=\frac12r_h^2.
}
\]

The existing nonlinear heat-scale flux is

\[
\Pi_{\rm heat}(h,t)
:=-\langle u\times Cu,e^{-hA}u\rangle.
\]

By self-adjointness of `S_h`,

\[
\Pi_{\rm heat}
=-\langle S_h(u\times Cu),u_h\rangle.
\]

The pointwise null relation

\[
u_h\cdot(u_h\times Cu_h)=0
\]

removes the intrinsic Euler part.  Hence

\[
\boxed{
\Pi_{\rm heat}(h,t)
=-\langle u_h,\mathfrak N_h\rangle.
}
\]

Equivalently,

\[
\boxed{
\langle q_h,\mathfrak N_h\rangle
=-\frac{\Pi_{\rm heat}}{r_h}.
}
\]

Together with Section 4 this proves that the scalar cascade flux and the tangent
connection anomaly are orthogonal projections of one literal vector defect.

A theory which retains only `Pi_heat` therefore keeps only the radial shadow of the
full heat renormalization event.

**Classification: Exact heat-flux/radial-defect identity.**

---

## 7. The scalar heat continuity law is the radial flatness condition

Differentiate the heat energy in `h`:

\[
\boxed{
\partial_h\mathcal E
=-\rho,
}
\]

where

\[
\rho(h,t)
=\frac12\langle u_h,Au_h\rangle
\]

is the existing positive heat-scale density.

Section 6 and the characteristic velocity give

\[
\boxed{
\mathcal D_\nu\mathcal E
=-\Pi_{\rm heat}.
}
\]

Since

\[
[\mathcal D_\nu,\partial_h]=0,
\]

one has

\[
\mathcal D_\nu(-\rho)
=\partial_h(-\Pi_{\rm heat}).
\]

Therefore

\[
\boxed{
(\partial_t-2\nu\partial_h)\rho
=\partial_h\Pi_{\rm heat},
}
\]

or

\[
\boxed{
\partial_t\rho
-\partial_h(2\nu\rho+\Pi_{\rm heat})
=0.
}
\]

Thus the canonical heat-scale continuity theorem is not an independent scalar
mechanism below the lift.  It is the radial mixed-derivative compatibility of one
heat-resolved state.

**Classification: Exact equivalence with the established heat continuity law.**

---

## 8. The directional mixed-derivative compatibility is projective zero curvature

The ray equations are

\[
\partial_h\mathsf P_h
=[B_h,\mathsf P_h],
\]

and

\[
\mathcal D_\nu\mathsf P_h
=[\Gamma_h^E,\mathsf P_h].
\]

Apply `partial_h` to the second and `D_nu` to the first.  Since the differential
operators commute,

\[
0
=\partial_h\mathcal D_\nu\mathsf P_h
-\mathcal D_\nu\partial_h\mathsf P_h.
\]

Expand and use Jacobi.  One obtains

\[
\boxed{
[\mathcal F_{th},\mathsf P_h]=0,
}
\]

where

\[
\boxed{
\mathcal F_{th}
:=\partial_h\Gamma_h^E
-\mathcal D_\nu B_h
+[\Gamma_h^E,B_h].
}
\]

Equivalently, the off-diagonal/projectively active curvature vanishes:

\[
\boxed{
[\mathsf P_h,[\mathsf P_h,\mathcal F_{th}]]=0.
}
\]

The remaining value of `F_th`, if nonzero in the canonical rank-two gauge, commutes
with the ray and is therefore pure tangent-frame curvature.  It cannot move the
physical energy line.

This is the precise zero-curvature theorem requested by the previous energy-ray
frontier.

**Classification: Exact projective zero-curvature identity.**

---

## 9. Scalar continuity and projective zero curvature are one heat--time flatness law

Sections 7 and 8 should not be read as two parallel observations.

The heat-resolved physical state has a radial/directional decomposition

\[
u_h=r_hq_h.
\]

The same two commuting differential directions

\[
\partial_h,
\qquad
\mathcal D_\nu=\partial_t-2\nu\partial_h
\]

act on both pieces.

- On the radius/energy, mixed-derivative compatibility is exactly
  `rho_t-partial_h(2nu rho+Pi_heat)=0`.
- On the ray, mixed-derivative compatibility is exactly
  `[F_th,P_h]=0`.
- The nonlinear coupling in both equations is the same vector heat-product anomaly
  `mathfrak N_h`: its radial projection is `Pi_heat`, while its tangent projection
  corrects the Euler connection.

Hence the whole lifted grammar is

\[
\boxed{
\begin{gathered}
u_h=S_hu,
\qquad
\mathcal D_\nu u_h=X_E(u_h)+\mathfrak N_h,\\
\partial_hu_h=-\frac12Au_h,\\
\mathfrak N_h
=P_\sigma\bigl[S_h(u\times Cu)-S_hu\times S_hCu\bigr],\\
\text{radial flatness}=\text{heat continuity},\\
\text{directional flatness}=\text{projective zero curvature}.
\end{gathered}
}
\]

This is smaller than treating heat cascade, critical heat anomaly, viscous sorting,
Euler ray motion and causal time evolution as separate mechanisms.

**Classification: Rigorous synthesis of exact identities.**

---

## 10. Interior projective holonomy is zero; the remaining escape is a boundary problem

On every smooth rectangle contained in

\[
\{(t,h):h>0\},
\]

the actual heat-resolved ray `P_h(t)` is a single-valued smooth field.  The
projective curvature law says that transporting this ray infinitesimally in the two
orders

\[
\text{heat age then causal physical time}
\]

or

\[
\text{causal physical time then heat age}
\]

produces no off-diagonal discrepancy.

Thus there is no independent interior projective source capable of creating a new
ray mechanism.  The only nonlinear defect is `mathfrak N_h`, and it is already the
connection correction required for the two flows to be compatible.

A candidate finite-time escape must therefore be a failure of uniform control as the
smooth rectangles approach the parabolic corner

\[
\boxed{(t,h)\to(T,0).}
\]

This gives a stricter meaning to the previous phrase "zero-heat-age Zeno": it is a
possible singular boundary concentration of a connection which is projectively flat
at every positive heat age.

Projective flatness alone does not bound the size of the connection near that
boundary.  Therefore this is not yet a no-escape theorem.

**Classification: Rigorous interior-flatness consequence / Open boundary control.**

---

## 11. Why a snapshot action-to-energy bound cannot replace heat--time compatibility

The polar critical-action theorem reduced critical feeding to the transfer-relevant
scalar action

\[
\mathscr A_{\rm rel}
:=
\frac{T_\kappa^2}{V_\kappa},
\]

where

\[
T_\kappa
=\langle\nabla_S\kappa,(q_t)_E\rangle,
\qquad
V_\kappa
=\langle\nabla_S\kappa,M_q\nabla_S\kappa\rangle,
\]

with the value zero on the one-shell null set.  The exact scalar square gives

\[
\dot\kappa
=-\frac\nu2
\left(
\sqrt{V_\kappa}
-\frac{T_\kappa}{\nu\sqrt{V_\kappa}}
\right)^2
+\frac1{2\nu}\mathscr A_{\rm rel}.
\]

Hence critical escape requires

\[
\int\mathscr A_{\rm rel}\,dt=\infty.
\]

A tempting route would be a universal instantaneous estimate

\[
\mathscr A_{\rm rel}
\lesssim r^2\mu,
\]

because `r^2 mu` is the literal energy-drain density up to viscosity.  The route is
not scale-compatible with intermittent concentration.

On Euclidean localization, an `L^2`-normalized packet at spatial scale `epsilon`
with nonzero critical transfer has the formal exact Hodge scaling

\[
\mu\sim\epsilon^{-2},
\qquad
V_\kappa\sim\epsilon^{-3},
\qquad
T_\kappa\sim\epsilon^{-7/2},
\]

so

\[
\boxed{
\frac{\mathscr A_{\rm rel}}{\mu}
=\frac{T_\kappa^2}{\mu V_\kappa}
\sim\epsilon^{-2}.
}
\]

A torus mixed-helical wavepacket referee realizes the predicted onset.  The family is
constructed by taking a nonzero-transfer mixed-helical carrier triad at wavevectors
`N k_j`, multiplying its vector potential by a real Dirichlet envelope of bandwidth
`N`, and taking curl; divergence-free structure is exact.  The audited carrier uses

\[
(k_1,k_2,k_3)=((1,0,0),(1,1,0),(-2,-1,0)),
\]

helical signs `(-,+,-)` and complex amplitudes approximately

\[
(-0.199764+0.030998i,
 -0.077298-0.198051i,
 -0.084570-0.051050i).
\]

For the `N`th packet, the carrier vector-potential modes are placed at `Nk_j` with
the exact inverse-curl factor `1/(s_j N|k_j|)`, multiplied by

\[
\phi_N(x)=\sum_{m\in[-N,N]^3\cap\mathbb Z^3}e^{im\cdot x},
\]

and the velocity is the curl of that product before `L^2` normalization.  This makes
the calibration reproducible without declaring the numerically optimized amplitudes
canonical.  After normalization the measured values are

\[
\begin{array}{c|ccccc}
N&1&2&3&4&5\\ \hline
T_\kappa^2/(\mu V_\kappa)
&8.30\!\times10^{-4}
&1.66\!\times10^{-3}
&3.31\!\times10^{-3}
&5.69\!\times10^{-3}
&8.80\!\times10^{-3},\\
N^{-2}T_\kappa^2/(\mu V_\kappa)
&8.30\!\times10^{-4}
&4.15\!\times10^{-4}
&3.67\!\times10^{-4}
&3.56\!\times10^{-4}
&3.52\!\times10^{-4}.
\end{array}
\]

Over `N=2,...,5`, log slopes are approximately

\[
T_\kappa:N^{3.29},
\qquad
\mu:N^{1.87},
\qquad
V_\kappa:N^{2.89},
\qquad
\mathscr A_{\rm rel}/\mu:N^{1.82},
\]

converging toward the localization exponents `7/2,2,3,2`.

This referee is an adversarial scaling calibration, not a proof of an asymptotic
torus theorem.  Its role is methodological: a no-escape proof should not be built on
an instantaneous action-versus-energy estimate whose natural localization scaling
is wrong.  The missing compensator must involve the parabolic time/heat scale, which
is exactly what the flat lift retains.

**Classification: Exact scalar action identity; rigorous Euclidean scaling grammar;
audited torus intermittent calibration; no universal torus inequality claimed.**

---

## 12. The no-escape frontier after heat--time projective flatness

The previous descriptions of a candidate escape were:

- a zero-heat-age concentration of the canonical heat density/flux;
- a finite weak ray path with infinite critical action;
- an `L^1` but non-`L^2` active radial-loss spike;
- a sequence of positive-scale spread creation events.

They now sit on one lifted object.

At every positive heat age the actual state obeys a projectively flat pair of
connections.  The one vector defect `mathfrak N_h` simultaneously supplies the
radial scale flux and the tangent Euler renormalization anomaly, and that defect is
itself the Hodge heat carré-du-champ of the literal Lamb product.

The next question is therefore not another snapshot estimate.  It is

\[
\boxed{
\begin{gathered}
\text{Can the self-generated heat-product defect }\mathfrak N_h
\text{ concentrate at }(T,0)\\
\text{strongly enough to produce infinite critical ray action and an infinite}
\text{ negative-half heat moment,}\\
\text{while the heat--time connection remains projectively flat at every }h>0\\
\text{and its radial component has only the finite physical energy reservoir?}
\end{gathered}
}
\]

A true no-escape theorem at this stage must be a **boundary compactness or boundary
holonomy theorem for the projectively flat heat--time connection**.  Interior
curvature cannot be invoked because its ray-active part is exactly zero.

No such boundary theorem is proved here.

**Classification: Open.**

---

## 13. Classification summary

### Exact

- heat lift `u_h=S_hu` and characteristic law
  `(partial_t-2nu partial_h)u_h=S_hX_E(u)`;
- heat-age radius/ray laws;
- heat-age double-bracket projector flow;
- causal characteristic ray Lax law;
- one vector renormalization defect
  `N_h=S_hX_E(u)-X_E(S_hu)`;
- radial/tangent decomposition of `N_h`;
- `N_h` as the established heat cross-product/carré-du-champ defect;
- scale flux `Pi_heat=-<u_h,N_h>`;
- radial mixed-derivative compatibility equals the canonical heat continuity law;
- directional mixed-derivative compatibility gives
  `[F_th,P_h]=0`, exact projective zero curvature.

### Rigorous consequences

- scalar cascade and tangent ray renormalization are two projections of one vector
  heat defect;
- there is no independent ray-active interior curvature at positive heat age;
- the previous physical-time and heat-age Zeno descriptions are boundary faces of
  one projectively flat lifted connection;
- a snapshot action-to-energy route has the wrong localization scaling and is not a
  viable replacement for the time--scale compatibility.

### Audited calibration

- mixed-helical vector-potential/Dirichlet wavepackets through `N=5` show the
  predicted intermittent onset of
  `T_kappa^2/(mu V_kappa) ~ const * N^2`.

### Open

- a boundary compactness/holonomy theorem at `(T,0)`;
- exclusion of concentration of the tangent component of `N_h` relative to its
  finite radial energy face;
- finiteness of the critical quotient action;
- continuation, restart, blow-up exclusion and global regularity.

---

## Follow-through: projective flatness is an interior compatibility, not an abstract no-escape principle

A later shell-ladder adversary shows that a fixed Hodge square, finite radial
reservoir, skew/Casimir-null ray motion and projectively flat heat lift can coexist
with finite-time Hodge escape if the conservative ray plane is allowed to be chosen
abstractly from shell to shell.

Therefore the boundary problem identified here cannot be solved by flatness alone.
The genuinely Navier--Stokes-specific ingredient is the fixed Lamb/self-Lie
realization of the horizontal connection and its heat anomaly:

\[
X_E(u)=P_\sigma(u\times Cu),
\qquad
\mathfrak N_h
=S_hX_E(u)-X_E(S_hu).
\]

Any successful boundary theorem must exploit that specific nonlinear realization,
not merely the fact that the resulting heat--time connection is projectively flat.
See `docs/abstract_shell_ladder_escape_self_lie_stop_theorem.md`.

**Classification: Rigorous later architecture correction.**
