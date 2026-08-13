# Kelvin ancestry -> Eulerian moving-readout audit

This milestone follows the exact physical distinction exposed by the critical-sheet
transport audit.  A Kelvin ancestry trajectory is material/stochastic; an Eulerian
critical sheet is a moving observation surface.  They are **not** identified.  The
question is instead:

> If a full physical Kelvin ancestry state is observed through a moving Eulerian
> localization, what mean/covariance/event law is forced by the Navier--Stokes,
> Reynolds/coarea, and conditional-probability structure already present?

The answer is rigid.  There is no fourth ``selector covariance source`` to invent.
Conditioning and localization produce exactly three covariance layers, and the
moving cut acts on them by one signed Reynolds boundary-revaluation law.

No first-bad badness functional, restart, continuation, or global-regularity claim is
made.

## 1. Keep the two physical layers separate

Let `Y` denote the full physical Kelvin current-shape state.  A reduced ancestry
coordinate `y` may retain only the physical anchor or another coarse state.  If it is
reduced, the correct lift is a conditional kernel

\[
\kappa(y,dY),
\]

not an implicit equality of states.  Let the full-state payoff have conditional mean
`m(Y)` and intrinsic covariance `C_full(Y)`.

Now let an Eulerian localization select a moving region `Omega(t)` in the reduced
ancestry state.  The selector is therefore a **readout/restriction of an ancestry
population**, not another stochastic ancestry trajectory.

This is the state semantics forced by the previous exact no-go:

\[
\boxed{
\text{Kelvin/material ancestry}
\;\neq\;
\text{Eulerian moving observation}.
}
\]

**Classification: Rigorous consequence of the previous exact transport/q.v. no-go.**

## 2. Exact three-layer covariance law

At each reduced ancestry state define

\[
\bar m(y)=\mathbb E_\kappa[m(Y)\mid y],
\]

\[
C_{\rm int}(y)=\mathbb E_\kappa[C_{\rm full}(Y)\mid y],
\]

and

\[
C_{\rm res}(y)=\operatorname{Cov}_\kappa(m(Y)\mid y).
\]

Normalize the selected reduced ancestry measure on `Omega(t)`.  Applying the law of
total covariance twice gives

\[
\boxed{
C_{\rm sel}
=
\underbrace{\mathbb E_{\rm sel}C_{\rm int}}_{\text{intrinsic Kelvin/future covariance}}
+
\underbrace{\mathbb E_{\rm sel}C_{\rm res}}_{\text{hidden-state resolution covariance}}
+
\underbrace{\operatorname{Cov}_{\rm sel}(\bar m)}_{\text{Eulerian localization covariance}}.
}
\]

These terms are different physical objects.

- `C_int` already exists on the full Kelvin state and may contain the Brownian
  carré-du-champ/future-bank covariance.
- `C_res` is ordinary conditional variance caused by hiding full-state information.
  It is not Brownian q.v.
- the final term is dispersion between different reduced ancestry states retained by
  the Eulerian localization.

A direct finite-state reconstruction in the symbolic audit recovers the same total
second moment exactly, including vector cross components.

**Classification: Exact identity.**

## 3. Moving boundary law: signed revaluation, not a new stochastic producer

Let the selected mass be `M`, selected mean be `m_bar`, and let a moving boundary
piece carry signed ancestry-mass flux `lambda_b`, positive into the selected region.
For any normalized matrix-valued selected average `A_bar`, Reynolds normalization
forces

\[
\boxed{
\dot A_{\partial}
=
\frac1M\sum_b\lambda_b(A_b-A_{\rm bar}).
}
\]

For the selected mean,

\[
\boxed{
\dot{\bar m}_{\partial}
=
\frac1M\sum_b\lambda_b(m_b-\bar m).
}
\]

For the total selected covariance,

\[
\boxed{
\dot C_{\partial}
=
\frac1M\sum_b\lambda_b
\left[
C_b+(m_b-\bar m)(m_b-\bar m)^T-C_{\rm sel}
\right].
}
\]

The sign is inherited from physical mass crossing.  This term can raise or lower a
covariance component.  It is therefore a **finite-variation population
revaluation**, not a positive Brownian source.

Applying the first formula separately to the intrinsic and resolution layers, and
the covariance formula to the localization layer, telescopes **exactly** to the total
covariance boundary law.  Thus

\[
\boxed{
\text{intrinsic} + \text{resolution} + \text{localization}
}
\]

is closed under moving Eulerian readout; there is no missing fourth selector term.

**Classification: Exact Reynolds/conditional-covariance identity.**

## 4. Exact Navier--Stokes calibration: a stationary Kelvin ancestry population

Return to the exact periodic two-mode heat shear

\[
u=(U(y,t),0,0).
\]

On the physical reverse-age Kelvin anchor, the `y` drift is zero and the diffusion
coefficient is `nu`.  The one-dimensional Fokker--Planck equation is

\[
\partial_\sigma\rho
=-\partial_y(b_y\rho)+\nu\partial_{yy}\rho.
\]

Because `b_y=0`, the uniform torus marginal

\[
\rho_y=\frac1{2\pi}
\]

is an exact stationary Kelvin-ancestry measure.

This is important physically: the critical sheet moves through a perfectly regular
ancestry population.  Any singular readout rate comes from the moving observation
geometry, not from a singular Kelvin anchor density.

**Classification: Exact identity / Audited exact-NS calibration.**

## 5. The critical chamber is a literal sub-Markov readout

Let the minus side critical sheet be

\[
a_-(t)=\pi-d(t),
\qquad
\cos d=e^{3(\nu t-1)},
\]

and select the chamber

\[
\Omega(t)=[\pi-d(t),\pi].
\]

Its uniform Kelvin-anchor mass is exactly

\[
\boxed{M(t)=\frac{d(t)}{2\pi}}.
\]

The half-width obeys

\[
\boxed{\dot d=-3\nu\cot d},
\]

so

\[
\dot M=\frac{\dot d}{2\pi}
\sim -\frac{3\nu}{2\pi d}.
\]

The instantaneous mass-loss rate diverges, but the entire mass excursion from
`d=d_0` to the merger is

\[
\boxed{\operatorname{TV}M=\frac{d_0}{2\pi}<\infty}.
\]

The readout is therefore a finite-variation sub-Markov restriction even though its
boundary speed diverges.

**Classification: Exact identity / Audited calibration.**

## 6. Exact vorticity payoff: criticality regularizes the normalized mean

Write `x=pi-y`, so the selected chamber is `0<=x<=d`.  On the exact critical relation,

\[
\alpha(d)=e^{-1}\cos(d)^{-1/3},
\]

and the actual vorticity is

\[
q(x,d)
=
\alpha(d)
\left[-\cos x+\frac{\cos2x}{4\cos d}\right].
\]

Its selected uniform mean has the closed form

\[
\boxed{
\bar q(d)
=-\frac{3\alpha(d)}4\frac{\sin d}{d}.
}
\]

Both endpoints are vorticity-critical.  Hence integrating the literal heat equation

\[
q_t=\nu q_{yy}
\]

across the chamber gives zero endpoint diffusive flux in the **first moment**.  The
whole normalized mean motion is therefore the Reynolds moving-cut revaluation:

\[
\boxed{
\dot{\bar q}
=
\frac{\dot d}{d}\bigl(q_{\rm side}-\bar q\bigr).
}
\]

Now the merger geometry supplies a second rigid cancellation.  Direct expansion of
the exact NS expressions gives

\[
q_{\rm side}-\bar q
=-\frac{e^{-1}}{15}d^4+O(d^6),
\]

while

\[
\frac{\dot d}{d}\sim -\frac{3\nu}{d^2}.
\]

Therefore the apparently singular moving observation produces

\[
\boxed{
\dot{\bar q}
=
\frac{\nu e^{-1}}5d^2+O(d^4)\longrightarrow0.
}
\]

The normalized readout reaches the common merger value

\[
\boxed{\bar q\to-\frac{3}{4e}}.
\]

The singular boundary speed is real, but the PDE forces the physical contrast to
collapse faster.  No ad hoc smoothing has been introduced.

**Classification: Exact identity / Rigorous consequence within the exact NS
calibration.**

## 7. Selected covariance: Kelvin bulk plus moving-cut revaluation

Let

\[
V(d)=\operatorname{Var}_{\Omega(d)}q.
\]

The exact elementary trigonometric second moment gives

\[
\boxed{
V(d)=\frac{e^{-2}}{525}d^8+O(d^{10}).
}
\]

Differentiating the actual selected variance and using
`q_t=nu q_yy` gives a two-face law:

\[
\boxed{
\dot V
=
\underbrace{-2\nu\left\langle |q_y|^2\right\rangle_{\Omega}}_{\text{intrinsic NS/Kelvin bulk}}
+
\underbrace{\frac{\dot d}{d}
\left[(q_{\rm side}-\bar q)^2-V\right]}_{\text{moving-cut covariance revaluation}}.
}
\]

The two faces are physically distinct and have different forced coefficients:

\[
-2\nu\langle|q_y|^2\rangle
=
-\frac{4\nu e^{-2}}{105}d^6+O(d^8),
\]

\[
\frac{\dot d}{d}
\left[(q_{\rm side}-\bar q)^2-V\right]
=
-\frac{4\nu e^{-2}}{525}d^6+O(d^8).
\]

Hence

\[
\boxed{
\dot V
=-\frac{8\nu e^{-2}}{175}d^6+O(d^8)\longrightarrow0.
}
\]

This is a literal example of the programme's desired discipline: do not call every
negative term ``dissipation`` and do not call every covariance change ``q.v.``.  One
face is the local viscous/Kelvin gradient bulk; the other is signed population
revaluation caused by ancestry crossing a moving Eulerian boundary.

**Classification: Exact identity / Audited exact-NS calibration.**

## 8. What bottleneck this resolves

Before this milestone, the repository knew separately that

1. a reduced ancestry state may require a conditional full-state lift kernel;
2. moving cuts have Reynolds/coarea boundary-speed faces;
3. a critical sheet is not a Kelvin ancestry path.

The missing composition is now literal:

\[
\boxed{
\text{physical Kelvin ancestry}
\xrightarrow{\;\kappa\;}
\text{conditional full-state payload}
\xrightarrow{\;\Omega(t)\;}
\text{Eulerian moving readout}.
}
\]

At second order the complete state seen by that readout is

\[
\boxed{
C_{\rm int}+C_{\rm res}+C_{\rm loc},
}
\]

and a moving selector acts by signed boundary revaluation of these same objects.  It
does **not** supply an independent stochastic covariance producer.

For the exact critical merger, the previously singular selector speed is further
shown to be harmless at normalized vorticity mean/covariance level because exact NS
criticality forces quartic/eighth-order state collapse.

This resolves the **semantics and second-order transport law of an ancestry-to-moving-
Eulerian-readout lift once the physical localization is supplied**.

It does **not** define which localization is the programme's first-bad localization.
That remaining choice must itself come from an NS observable/obstruction, not from an
external threshold oracle.

**Classification: Rigorous structural consequence; first-bad instantiation remains
Open-literal.**

## 9. Frontier after this milestone

Established:

- exact three-layer covariance decomposition under a reduced/full ancestry lift plus
  Eulerian localization;
- exact signed Reynolds boundary law for selected mean and covariance;
- exact telescope showing no independent fourth ``selector covariance source``;
- exact stationary uniform Kelvin-anchor marginal in the periodic shear calibration;
- exact critical-chamber ancestry mass and finite total variation;
- exact vorticity mean law whose moving-cut singularity is cancelled by quartic
  critical contrast;
- exact variance law = Kelvin bulk + moving-cut covariance revaluation;
- exact eighth-order variance collapse and sixth-order vanishing rate.

Still **Open-literal**:

- the programme-specific first-bad scalar/state observable defining `Omega(t)`;
- the global ancestry-state manifold and its programme-specific physical lift outside
  the instantiated physical anchor semantics;
- the two-clock first-bad/future-bank identification;
- endogenous general selector accumulation/local-time beyond supplied smooth moving
  cuts;
- uniform first-bad support/finite-shape collapse.

Still **Open**: restart capacity, continuation, and 3D Navier--Stokes regularity.

**No continuation/restart/regularity theorem claimed.**
