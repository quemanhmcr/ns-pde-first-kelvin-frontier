# Full-state versus reduced ancestry: resolution-kernel covariance audit

This note resolves a hidden ambiguity in the phrase **same ancestor**.  The canonical
viscous pair-branching tensor is exact only after the ancestor state has been fixed.
If the stored ancestry state is a reduction of the physical Kelvin current-shape
state, there is an additional exact conditional-resolution covariance at the
reduction face.

This term is not identified with the repository's still-undefined `S^int` or
`Z_irr`.  No continuation theorem is claimed.

---

## 1. A deterministic state map is not the general bridge

Let `Y` denote the full physical Kelvin state and `y` a possibly coarser ancestry
state.  The general lift from reduced to full observables is a conditional Markov
kernel

\[
\kappa_s(y,dY).
\]

For a physical observable `F(Y)`, define

\[
(R_sF)(y)=\int F(Y)\,\kappa_s(y,dY).
\]

A deterministic map is only the special case in which `kappa_y` is a Dirac mass.

If `L_y` and `L_Y` are the reduced and full backward-observable generators, exact
Markov compatibility is

\[
\boxed{
\partial_sR_s+L_yR_s-R_sL_Y=0.
}
\]

The CI witness has a nontrivial two-hidden-shape kernel that satisfies this
intertwining exactly.

**Classification: Exact kernel-intertwining identity.**

---

## 2. Law of total covariance produces a physical resolution bank

Let the terminal Kelvin payoff have full-state conditional mean `m(Y)` and
full-state future covariance `C(Y)`.  Conditioning only on the reduced ancestry
state gives

\[
\bar m(y)=\int m(Y)\,\kappa_y(dY).
\]

The full matrix law of total covariance is

\[
\boxed{
\bar C(y)
=
\int C(Y)\,\kappa_y(dY)
+
C_{\rm res}(y),
}
\]

where

\[
\boxed{
C_{\rm res}(y)
=
\int
(m(Y)-\bar m)(m(Y)-\bar m)^T
\,\kappa_y(dY).
}
\]

Equivalently,

\[
\boxed{
C_{\rm res}(y)
=
\frac12\iint
[m(Y_1)-m(Y_2)]
[m(Y_1)-m(Y_2)]^T
\,\kappa_y(dY_1)\kappa_y(dY_2).
}
\]

Thus the extra reduced-state pair content is itself an exact squared-difference
pair covariance.  It retains all cross-orientation entries.

**Classification: Exact conditional-covariance / pair identity.**

---

## 3. It is not viscous quadratic variation

Take two hidden physical shapes under one reduced ancestry label with means

\[
m_1=a,
\qquad
m_2=-a,
\]

and equal conditional weights.  Suppose each full physical state has zero remaining
future variance.  Then

\[
\int C(Y)\,d\kappa=0,
\]

but

\[
\boxed{C_{\rm res}=a^2.}
\]

This remains true even when the hidden physical generator is zero.  Therefore the
resolution covariance can exist with no viscous q.v. production at all.

Its physical type is:

> covariance caused by conditioning on a state that does not resolve the physical
> current shape.

It is not pressure, not observer q.v., and not the canonical viscous branching
tensor.

**Classification: Exact no-go against identifying resolution covariance with
viscous q.v.**

---

## 4. Full-pair meaning of `same ancestor`

There are now two distinct branch-time constructions.

### Full physical ancestor

If `Y` is known, both replicas start from the same full current shape.  The
branch-time resolution covariance is zero.  The continuous diffusion branch source
is the already audited viscous diagonal cross-derivation.

### Reduced ancestor

If only `y` is known, the full states are drawn from `kappa_y`.  Two independent
future replicas use

\[
\kappa_y(dY_1)\kappa_y(dY_2).
\]

The corresponding squared-difference at the reduction face is exactly
`C_res(y)`.

Hence

\[
\boxed{
\text{reduced same ancestor}
\neq
\text{full physical same ancestor}
}
\]

unless the conditional kernel is Dirac or the payoff is constant on each reduction
fiber.

**Classification: Exact state-resolution dichotomy.**

---

## 5. Exact Navier--Stokes calibration: full current-shape law can be singular

Consider the exact affine shear

\[
\boxed{u=(ay,0,0).}
\]

Its advection and Laplacian vanish, so it is an exact incompressible Navier--Stokes
solution with constant pressure.

For anchored relative shape

\[
R=(r_x,r_y,r_z),
\]

the common-noise Kelvin kinematics gives

\[
\boxed{
R(t)
=
(r_x+a t r_y,\,r_y,\,r_z).
}
\]

Thus a fixed initial shape remains deterministic; only the anchor carries Brownian
q.v.  For a nondegenerate three-dimensional anchor covariance `C_X`, the joint
`(X,R)` covariance is

\[
\boxed{
\operatorname{diag}(C_X,0_{3\times3}),
}
\]

which has rank `3` in state dimension `6` and determinant zero.

Therefore a smooth positive density with respect to ordinary six-dimensional
volume is **not a universal representation of the full Kelvin current-shape law**.
One would need either a degenerate/submanifold reference measure, a hypoelliptic
measure formulation, or a reduced ancestry state with a conditional shape kernel.

**Classification: Exact Navier--Stokes calibration and rigorous structural
consequence.**

---

## 6. The ancestry-state dichotomy

The existing normalized ancestry law must eventually choose one of two physical
semantics.

### A. Full-state ancestry

The state `y` is the full Kelvin current-shape state.  Then:

- there is no reduction covariance `C_res`;
- the canonical continuous pair source is the viscous full-state branching source;
- but the ancestry measure calculus must allow the degenerate/singular shape support
  seen in exact affine shear.

### B. Reduced ancestry

The state `y` omits physical current-shape information.  Then:

- a conditional lift kernel `kappa(y,dY)` is mandatory;
- `C_res` is mandatory full pair content;
- the phrase `same ancestor` means same reduced label, not automatically same full
  physical current;
- localization/refinement/exit laws must carry this resolution face with full cross
  covariance.

The invalid third option is to use a reduced smooth ancestry density while silently
pretending its state is already the full physical current and dropping `C_res`.

**Classification: Rigorous structural dichotomy.**

---

## 7. Relation to the canonical `2 nu q K delta_Delta` source

The earlier pair audit remains exact on the **full diffusion state**:

\[
\boxed{
\mathbb T^{\rm br}_{\rm visc}
=2\nu qK\,\delta_\Delta.
}
\]

The new result does not modify its coefficient.  It sharpens its scope.

If an additional state-reduction map is inserted before the pair process, the
reduction has its own pair face `C_res`.  This term can survive at `nu=0`; therefore
it cannot be absorbed into the viscous branching tensor.

No identification with `S^int` is made.  If a future literal definition of `S^int`
contains a state-resolution term, it must be compared line by line with `C_res`.

**Classification: Exact type separation; Pillar II identification remains
open-literal.**

---

## 8. New literal frontier

Before a global restart-capacity law can use the normalized ancestry density, the
repository must state explicitly:

1. what the ancestry state `y` is;
2. whether it is full physical Kelvin state or reduced;
3. if full, what reference-measure calculus handles degenerate/singular shape
   support;
4. if reduced, what conditional lift kernel `kappa` is used and where its
   resolution covariance enters the pair world-sheet.

This is a definition/geometry bridge before it is an estimate problem.

**Classification: Open-literal ancestry-state semantics.  No continuation/restart
conclusion.**


---

## 9. Resolution covariance has its own exact carré-du-champ transfer law

Let `H_full=partial_tau-L_full` and `H_red=partial_tau-L_red`.  Suppose the
(time-dependent, if needed) lift operator `R_tau` intertwines horizon operators,

\[
\boxed{\mathfrak H_{\rm red}R=R\mathfrak H_{\rm full}.}
\]

If the full conditional mean satisfies `H_full m=0`, set

\[
\bar m=Rm,
\qquad
C_{\rm res}=R(mm^T)-\bar m\bar m^T.
\]

The product rule gives exactly

\[
\boxed{
\mathfrak H_{\rm red}C_{\rm res}
=
\Gamma_{\rm red}[\bar m]
-
R\Gamma_{\rm full}[m].
}
\]

Meanwhile full future covariance satisfies

\[
\mathfrak H_{\rm full}C_{\rm full}=\Gamma_{\rm full}[m].
\]

Hence

\[
\boxed{
C_{\rm red}=RC_{\rm full}+C_{\rm res}
}
\]

obeys

\[
\boxed{
\mathfrak H_{\rm red}C_{\rm red}
=\Gamma_{\rm red}[\bar m].
}
\]

So state reduction does not destroy the future-bank law.  It transfers covariance
between the resolved full-state bank and unresolved fiber covariance.

An exact two-hidden-state switching witness has one reduced stationary state,
`m=(a,-a)e^{-2 lambda tau}`, and

\[
C_{\rm res}=a^2e^{-4\lambda\tau}.
\]

The reduced carré-du-champ is zero, while the averaged full hidden-state
carré-du-champ is

\[
4\lambda a^2e^{-4\lambda\tau}.
\]

Thus

\[
\boxed{
\partial_\tau C_{\rm res}
=-4\lambda a^2e^{-4\lambda\tau},
}
\]

exactly: full hidden-state stochastic activity depletes unresolved resolution
covariance even when the reduced generator sees no local q.v.

**Classification: Exact horizon-transfer identity and exact finite-state
calibration.**

---

## 10. Physical anchor marginalization produces the backward conditional-shape drift

There is a canonical **physical** reduced-state construction for the common-noise
Kelvin cylinder, independent of whether the repository's stored ancestry state is
ultimately identified with it.

Let `(X,R)` have a joint probability density `mu=q kappa`, where

- `X` carries forward drift `b_+(X)` and covariance `2 nu I`;
- relative shape `R` has deterministic drift `v_R(X,R)` and zero direct q.v.

The joint Fokker--Planck equation is

\[
\partial_t\mu
+\nabla_X\cdot(b_+\mu)
+\nabla_R\cdot(v_R\mu)
-\nu\Delta_X\mu=0.
\]

Its anchor marginal satisfies

\[
\partial_tq
+\nabla_X\cdot(b_+q)
-\nu\Delta_Xq=0.
\]

Substitute `mu=q kappa` and subtract `kappa` times the marginal equation.  The exact
product identity gives

\[
\boxed{
\partial_t\kappa
+b_-\cdot\nabla_X\kappa
+\nabla_R\cdot(v_R\kappa)
-\nu\Delta_X\kappa=0,
}
\]

where

\[
\boxed{b_-=b_+-2\nu\nabla\log q.}
\]

Thus the time-reversed anchor drift is not appended by hand.  It is forced by the
conditionalization of the full common-noise state onto the anchor marginal.

This gives a natural exact **candidate semantics** for a reduced ancestry state:

\[
y=X,
\qquad
\kappa_t(X,dR)=\text{conditional physical current-shape law}.
\]

If the normalized ancestry density `q` in the programme is eventually identified
with this anchor marginal, then its missing shape sector and its resolution
covariance are supplied canonically by `kappa`.  The repository does not yet define
its ancestry state `y` as this anchor, so that final identification is not asserted.

**Classification: Exact physical joint/marginal/conditional Fokker--Planck identity;
programme-specific ancestry-anchor identification is a Conjectural/open-literal
bridge.**
