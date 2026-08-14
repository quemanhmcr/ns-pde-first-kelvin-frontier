# Critical-spread heat continuity and transport-action law

## Purpose

The causal heat-ray theorem puts the normalized heat-resolved state

\[
q_h
=\frac{e^{-hA/2}u}{\|e^{-hA/2}u\|},
\qquad
A=C^2,
\]

on a projectively flat heat--time plane.  The polar theorem identifies the positive
critical Rayleigh center

\[
\kappa
=\langle q,\Lambda q\rangle,
\qquad
\Lambda=|C|,
\]

and its scalar transfer-relevant action.

The two statements compress further when `kappa` is lifted to heat age:

\[
\boxed{
\kappa(h,t)
:=\langle q_h,\Lambda q_h\rangle.
}
\]

Its heat derivative is automatically nonpositive.  Define the positive
critical-spread density

\[
\boxed{
\chi(h,t)
:=-\partial_h\kappa(h,t)
=\operatorname{Cov}_{q_h}(\Lambda,\Lambda^2)
\ge0.
}
\]

Define the causal critical flux

\[
\boxed{
\Theta(h,t)
:=\mathcal D_\nu\kappa(h,t),
\qquad
\mathcal D_\nu=\partial_t-2\nu\partial_h.
}
\]

Because the heat and causal derivatives commute,

\[
\boxed{
\mathcal D_\nu\chi
+\partial_h\Theta
=0.
}
\]

Equivalently, in physical time,

\[
\boxed{
\partial_t\chi
+\partial_h(\Theta-2\nu\chi)
=0.
}
\]

Thus the normalized critical spread is not a collection of moment balances.  It is
one positive continuity equation on the same canonical heat half-line already used
by the energy density.

At the physical boundary `h=0`,

\[
\boxed{
\Theta(0,t)=T_\kappa(t),
\qquad
4\chi(0,t)=V_\kappa(t),
}
\]

where `T_kappa` and `V_kappa` are exactly the Euler forcing and positive viscous
susceptibility in the polar critical-action theorem.  Therefore

\[
\boxed{
\mathscr A_{rel}(t)
=\frac{T_\kappa(t)^2}{V_\kappa(t)}
=\frac14\frac{\Theta(0,t)^2}{\chi(0,t)}.
}
\]

The previously derived scalar critical action is consequently one quarter of the
canonical kinetic transport action `flux^2/density` of this literal positive
continuity law.  It was not a human-chosen quotient.

The same identity explains the physical critical law:

\[
\boxed{
\partial_t\kappa(0,t)
=\Theta(0,t)-2\nu\chi(0,t).
}
\]

Euler supplies the boundary control flux; viscosity is the fixed drift toward the
zero-heat-age boundary.

No no-escape theorem follows yet.  The remaining question becomes a boundary-action
problem for a positive density which is itself generated from the same heat-resolved
state and coupled to the projectively flat ray connection.

---

## 1. Heat age turns the positive critical center into a monotone scalar potential

Let

\[
u_h=e^{-hA/2}u,
\qquad
q_h=u_h/\|u_h\|,
\]

and define

\[
\kappa_h:=\langle q_h,\Lambda q_h\rangle,
\qquad
\mu_h:=\langle q_h,Aq_h\rangle.
\]

The normalized heat equation is

\[
\partial_hq_h
=-\frac12(A-\mu_h)q_h.
\]

Therefore

\[
\begin{aligned}
\partial_h\kappa_h
&=2\langle\partial_hq_h,\Lambda q_h\rangle\\
&=-\langle(A-\mu_h)q_h,\Lambda q_h\rangle.
\end{aligned}
\]

Since `A=Lambda^2`, this is

\[
\boxed{
\partial_h\kappa_h
=-\left(
\langle q_h,\Lambda^3q_h\rangle
-\kappa_h\mu_h
\right).
}
\]

Define

\[
\boxed{
\chi_h
:=\langle q_h,\Lambda^3q_h\rangle
-\kappa_h\mu_h.
}
\]

Then

\[
\boxed{
\partial_h\kappa_h=-\chi_h.
}
\]

**Classification: Exact normalized heat-Rayleigh identity.**

---

## 2. The critical-spread density is positive by one spectral pair square

Let `pi_h` be the normalized positive `Lambda` spectral measure of `q_h`.  Then

\[
\chi_h
=\operatorname{Cov}_{\pi_h}(\ell,\ell^2).
\]

For two independent samples `ell,ell'`,

\[
\boxed{
\chi_h
=\frac12
\mathbb E_h\!\left[
(\ell-\ell')^2(\ell+\ell')
\right]
\ge0.
}
\]

Hence `kappa(h,t)` is decreasing in heat age and `chi` is a literal positive spread
density.

At a one-Laplacian-shell state, `ell=ell'` almost surely and

\[
\boxed{
\chi=0.
}
\]

Thus the earlier one-shell critical null set is exactly the zero set of the new
positive density.

**Classification: Exact positive pair representation.**

---

## 3. The same density is the mixed projective Hodge covariance

Let

\[
\mathsf P_h=q_h\otimes q_h,
\]

and define

\[
D_\Lambda=[\mathsf P_h,\Lambda],
\qquad
D_A=[\mathsf P_h,A].
\]

The projective covariance identity gives

\[
\operatorname{Cov}_{q_h}(\Lambda,A)
=\frac12\langle D_\Lambda,D_A\rangle_{HS}.
\]

Since

\[
A=\Lambda^2,
\]

one also has the Sylvester factorization

\[
\boxed{
D_A
=\Lambda D_\Lambda+D_\Lambda\Lambda.
}
\]

Therefore

\[
\boxed{
\chi_h
=\frac12
\left\langle
D_\Lambda,
\Lambda D_\Lambda+D_\Lambda\Lambda
\right\rangle_{HS}
\ge0.
}
\]

The critical-spread density is consequently the positive Sylvester metric energy of
the same projective positive-scale mismatch.

No new positive field has been introduced.

**Classification: Exact covariance/Sylvester identity.**

---

## 4. The causal critical flux is the horizontal derivative of the same potential

Use the causal characteristic derivative

\[
\mathcal D_\nu
=\partial_t-2\nu\partial_h.
\]

The heat-ray theorem gives

\[
\mathcal D_\nu q_h=a_h^E,
\]

where `a_h^E` is the heat-resolved Euler ray velocity, including the exact heat
renormalization anomaly.

Hence

\[
\boxed{
\Theta_h
:=\mathcal D_\nu\kappa_h
=2\langle(\Lambda-\kappa_h)q_h,a_h^E\rangle.
}
\]

In projective form,

\[
\boxed{
\Theta_h
=-\langle\Gamma_h^E,D_\Lambda\rangle_{HS},
}
\]

where `Gamma_h^E` is the canonical rank-two characteristic connection.

At `h=0`, the heat anomaly vanishes and

\[
\boxed{
\Theta(0,t)
=\langle\nabla_S\kappa,(q_t)_E\rangle
=T_\kappa(t).
}
\]

Thus the Euler forcing in the scalar critical square is exactly the boundary value
of one heat-age current.

**Classification: Exact causal critical-flux identity.**

---

## 5. Mixed derivatives generate one positive critical-spread continuity law

By definition,

\[
\chi=-\partial_h\kappa,
\qquad
\Theta=\mathcal D_\nu\kappa.
\]

Since

\[
[\mathcal D_\nu,\partial_h]=0,
\]

one obtains

\[
\boxed{
\mathcal D_\nu\chi
+\partial_h\Theta
=0.
}
\]

Because

\[
\partial_t
=\mathcal D_\nu+2\nu\partial_h,
\]

this is equivalently

\[
\boxed{
\partial_t\chi
+\partial_h(\Theta-2\nu\chi)
=0.
}
\]

The physical critical-spread current is therefore

\[
\boxed{
J_\kappa
:=\Theta-2\nu\chi.
}
\]

The two faces have exact meanings:

- `Theta` is the self-generated Euler transport current;
- `-2nu chi` is the universal viscous drift toward heat age zero.

**Classification: Exact positive continuity equation.**

---

## 6. The boundary current is exactly the normalized critical-center evolution

At `h=0`, physical time satisfies

\[
\partial_t\kappa
=\mathcal D_\nu\kappa+2\nu\partial_h\kappa.
\]

Therefore

\[
\boxed{
\partial_t\kappa(0,t)
=\Theta(0,t)-2\nu\chi(0,t).
}
\]

Now the polar theorem used

\[
\dot\kappa
=T_\kappa-\frac\nu2V_\kappa.
\]

Comparing the two formulas gives

\[
\boxed{
T_\kappa=\Theta(0,t),
\qquad
V_\kappa=4\chi(0,t).
}
\]

Thus the polar critical balance is literally the boundary flux law of the positive
critical-spread continuity equation.

This removes `T_kappa` and `V_kappa` from the primitive list below the heat lift:
they are boundary current and boundary density.

**Classification: Exact boundary identification.**

---

## 7. The transfer-relevant critical action is the boundary kinetic transport action

Off the shell-null set, the polar theorem defined

\[
\mathscr A_{rel}
=\frac{T_\kappa^2}{V_\kappa}.
\]

Section 6 gives

\[
\boxed{
\mathscr A_{rel}
=\frac14
\frac{\Theta(0,t)^2}{\chi(0,t)}.
}
\]

The quantity

\[
\boxed{
\mathscr B(h,t)
:=\frac{\Theta(h,t)^2}{\chi(h,t)}
}
\]

is the standard kinetic action density `flux^2/mass` of the positive continuity law,
where it is defined; set it to zero on the exact null set `chi=Theta=0`.

Hence

\[
\boxed{
\mathscr A_{rel}
=\frac14\mathscr B(0,t).
}
\]

The action needed in the critical no-escape theorem is therefore not an externally
chosen Riemannian cost.  It is the boundary kinetic action of an exact positive
transport law generated by Navier--Stokes itself.

The scalar square becomes

\[
\boxed{
\partial_t\kappa(0,t)
=-2\nu
\left(
\sqrt{\chi}
-\frac{\Theta}{4\nu\sqrt{\chi}}
\right)^2_{h=0}
+\frac1{8\nu}\mathscr B(0,t).
}
\]

**Classification: Exact boundary transport-action identity.**

---

## 8. The total critical-spread mass is the excess above the heat-selected shell

For each fixed nonzero smooth state on the torus, the discrete positive Hodge
spectrum has a lowest occupied magnitude.  Denote it by

\[
\ell_*(t).
\]

As `h` tends to infinity, normalized heat sorting selects the corresponding lowest
occupied Laplacian shell, so

\[
\lim_{h\to\infty}\kappa(h,t)=\ell_*(t).
\]

Therefore

\[
\boxed{
\int_0^\infty\chi(h,t)\,dh
=\kappa(0,t)-\ell_*(t).
}
\]

Thus `chi` carries exactly the positive critical-center excess above the shell which
heat would select from the current state.

On a time interval where the identity of the lowest occupied shell does not change,
its causal derivative is zero.  Integrating the continuity law then gives

\[
\mathcal D_\nu
\int_0^\infty\chi\,dh
=\Theta(0,t),
\]

assuming the large-heat flux vanishes, as it does after the one-shell limit is
reached.

A shell-switch event must be treated as a spectral support event rather than hidden
inside this formula; no monotonicity of `ell_*` under the full nonlinear PDE is
claimed.

**Classification: Exact fixed-state mass identity; piecewise-smooth support consequence.**

---

## 9. The critical-spread density is derived from the existing heat-energy profile

The new continuity law does not add an independent heat state.

Let

\[
\mathcal E(h,t)
=\frac12\|u_h\|_2^2
\]

and

\[
\rho(h,t)
=-\partial_h\mathcal E(h,t).
\]

The positive critical quadratic of the heat-resolved physical state is

\[
\mathcal K_h
:=\frac12\langle u_h,\Lambda u_h\rangle.
\]

By the same subordination formula used in the canonical critical theorem,

\[
\boxed{
\mathcal K_h
=\frac1{\sqrt\pi}
\int_0^\infty
s^{-1/2}\rho(h+s,t)\,ds.
}
\]

Hence

\[
\boxed{
\kappa(h,t)
=\frac{\mathcal K_h}{\mathcal E(h,t)}.
}
\]

The density

\[
\chi=-\partial_h\kappa
\]

is therefore a nonlinear fractional/conditional readout of the same positive heat
energy profile, not a separately postulated population.

What is genuinely additional to the scalar energy profile is the oriented Euler
flux `Theta`, and the projectively flat ray theorem has already identified its
heat-renormalization source.

**Classification: Exact subordination/derived-state identity.**

---

## 10. Two positive heat-half-line laws are now recognized as faces of one state

The energy heat density obeys

\[
\partial_t\rho
-\partial_h(2\nu\rho+\Pi_{\rm heat})
=0.
\]

The normalized critical-spread density obeys

\[
\partial_t\chi
+\partial_h(\Theta-2\nu\chi)
=0.
\]

These should not be promoted as two independent modeled cascades.

- `rho` is the radial heat derivative of the physical heat energy.
- `chi` is the heat derivative of the normalized positive critical Rayleigh center
  derived from that same energy profile.
- `Pi_heat` is the radial projection of the one vector heat-product anomaly.
- `Theta` is the corresponding characteristic derivative of the critical Rayleigh
  readout through the same projectively flat heat-resolved ray.

Thus energy cascade, critical transfer, viscous critical susceptibility and critical
action all live on one heat--time state.

**Classification: Rigorous synthesis.**

---

## 11. The no-escape frontier becomes a positive boundary-action trace problem

The previous theorem showed that critical escape requires

\[
\int_0^T\mathscr A_{rel}(t)\,dt
=+\infty.
\]

Section 7 turns this into

\[
\boxed{
\int_0^T
\frac{\Theta(0,t)^2}{\chi(0,t)}\,dt
=+\infty.
}
\]

So the remaining Zeno is exactly an infinite kinetic-action trace at the boundary of
a positive continuity equation.

At every positive heat age:

- `chi` is nonnegative;
- its current obeys exact conservation;
- the underlying heat ray obeys projective zero curvature;
- the scalar energy component has only the finite physical energy reservoir;
- the flux/current is generated by the same heat-renormalized Euler connection.

The open theorem can now be stated without inventing a badness score:

\[
\boxed{
\begin{gathered}
\text{Can the self-generated positive critical-spread continuity law develop an}\
\text{infinite boundary kinetic-action trace at }(T,0)\text{ while its full heat--time}\
\text{ray connection remains projectively flat and its radial energy face stays finite?}
\end{gathered}
}
\]

A successful no-escape theorem would be a boundary-action compactness theorem for
this exact positive transport, not an instantaneous domination estimate.

No such trace theorem is proved here.

**Classification: Open.**

---

## 12. Classification summary

### Exact

- heat-resolved critical center `kappa(h,t)`;
- positive density `chi=-partial_h kappa=Cov_h(Lambda,Lambda^2)`;
- pair-square positivity of `chi`;
- projective covariance/Sylvester representation of `chi`;
- causal flux `Theta=D_nu kappa`;
- continuity laws
  `D_nu chi+partial_h Theta=0` and
  `chi_t+partial_h(Theta-2nu chi)=0`;
- boundary identities `Theta(0)=T_kappa`, `4chi(0)=V_kappa`;
- `A_rel=(1/4)Theta(0)^2/chi(0)`;
- total heat-age mass `int chi dh=kappa-ell_*` for a fixed nonzero state;
- subordination of `kappa` and `chi` from the existing heat-energy profile.

### Rigorous consequences

- critical Euler transfer and viscous susceptibility are boundary current/density,
  not primitive scalar mechanisms;
- the transfer-relevant action is the kinetic action of a literal positive
  continuity law;
- the remaining critical Zeno is a boundary kinetic-action trace singularity;
- the energy and critical-spread heat equations are derived faces of one
  heat-resolved state rather than separate cascade models.

### Open

- finiteness of the boundary kinetic-action trace;
- a boundary compactness theorem coupling `chi,Theta` to the projectively flat ray;
- exclusion of the causal `(T,0)` Zeno corner;
- continuation, restart, blow-up exclusion and global regularity.
