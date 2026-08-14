# Poisson--Casimir / metric-gradient master law for incompressible Navier--Stokes

## Purpose

The preceding milestones compressed the Navier--Stokes mechanism list in stages:

\[
\text{de Rham skew-square current}
\to
\text{heat-null / carré-du-champ transfer}
\to
\text{canonical heat-scale continuity}
\to
\text{signed-curl alternating three-current}.
\]

The signed-curl theorem exhausted the entire quadratic Hodge functional calculus, but
it was still written in spectral coordinates.  This note asks the more intrinsic
question:

\[
\boxed{
\text{Is the alternating three-current itself only a coordinate shadow of one
phase-space operator law acting on every observable?}
}
\]

For every smooth incompressible Navier--Stokes solution on the mean-zero flat
three-torus, the answer is yes.

There is a constant alternating phase-space three-form

\[
\Omega(a,b,c)=\int_{\mathbb T^3}a\cdot(b\times c)\,dx,
\]

two canonical quadratic functionals

\[
E(u)=\frac12\|u\|_2^2,
\qquad
H(u)=\frac12\langle u,Cu\rangle,
\qquad C=\operatorname{curl},
\]

and the full nonlinear Euler operator is the Lie--Poisson Hamiltonian flow generated
by `E`, with `H` a Casimir.  Viscosity is the ordinary `L^2` gradient descent of

\[
Z(u)=\frac12\|Cu\|_2^2
=\frac12\|\nabla H(u)\|_2^2.
\]

Thus for every sufficiently smooth real functional `F[u]`, literal Navier--Stokes
obeys the single functional identity

\[
\boxed{
\frac d{dt}\mathcal F(u(t))
=
\Omega\bigl(\nabla\mathcal F,\nabla E,\nabla H\bigr)
-
\nu\left\langle\nabla\mathcal F,
\nabla\frac12\|\nabla H\|_2^2
\right\rangle.
}
\]

Equivalently,

\[
\boxed{
\dot{\mathcal F}
=
\{\mathcal F,E\}_{LP}
-
\nu\,(\mathcal F,Z)_{L^2}.
}
\]

This is a whole-functional, not merely quadratic, law.  The earlier spectral
three-current is exactly the signed-curl coordinate representation of `Omega`, and
the determinant theorem is the quadratic spectral specialization of this one
phase-space identity.

No claim is made that the displayed alternating tribracket by itself defines an
independent Nambu--Poisson structure.  What is used rigorously is that the induced
two-bracket below is exactly the standard Lie--Poisson bracket of divergence-free
vector fields and therefore satisfies Jacobi on the usual smooth functional domain.

No no-escape, blow-up exclusion, restart, continuation, or global-regularity theorem
is claimed.

---

## 1. Phase space and the constant alternating three-form

Let

\[
\mathcal H
=
\left\{
 u\in L^2(\mathbb T^3;\mathbb R^3):
 \nabla\cdot u=0,
 \ \int_{\mathbb T^3}u=0
\right\}.
\]

On smooth elements of this phase space define

\[
\boxed{
\Omega(a,b,c)
:=
\int_{\mathbb T^3}a\cdot(b\times c)\,dx.
}
\]

`Omega` is constant on the linear phase space and fully alternating:

\[
\boxed{
\Omega(a,b,c)
=
\operatorname{sgn}(\sigma)
\Omega(\sigma(a,b,c)).
}
\]

Let

\[
C:=\operatorname{curl}
\]

on the mean-zero divergence-free sector.  Then `C` is self-adjoint and

\[
\boxed{C^2=-\Delta=:A.}
\]

Define

\[
E(u)=\frac12\langle u,u\rangle,
\qquad
H(u)=\frac12\langle u,Cu\rangle,
\qquad
Z(u)=\frac12\langle Cu,Cu\rangle.
\]

Their `L^2` gradients are

\[
\boxed{
\nabla E=u,
\qquad
\nabla H=Cu=\omega,
\qquad
\nabla Z=C^2u=Au.
}
\]

Moreover

\[
\boxed{
Z=\frac12\|\nabla H\|_2^2.
}
\]

Thus kinetic energy, helicity and enstrophy are one Hodge-gradient ladder rather
than three unrelated scalar quantities:

\[
\boxed{
\nabla E
\xrightarrow{\ C\ }
\nabla H
\xrightarrow{\ C\ }
\nabla Z.
}
\]

**Classification: Exact Hodge/variational identities.**

---

## 2. The state-generated Poisson operator is contraction of `Omega` with `grad H`

For each smooth state `u` define the operator

\[
\boxed{
\mathbb J(u)v
:=
P(v\times\omega),
\qquad
\omega=Cu,
}
\]

where `P` is the Leray--Hodge projector.

For divergence-free test fields `a,b`, projection may be removed inside the pairing,
and therefore

\[
\begin{aligned}
\langle a,\mathbb J(u)b\rangle
&=\int a\cdot(b\times\omega)\,dx\\
&=\Omega(a,b,\nabla H).
\end{aligned}
\]

Hence

\[
\boxed{
\langle a,\mathbb J(u)b\rangle
=
(\iota_{\nabla H}\Omega)(a,b).
}
\]

In other words, the Euler Poisson tensor is obtained by contracting one constant
phase-space alternating three-form with the gradient of helicity.

Full alternation immediately gives

\[
\boxed{\mathbb J(u)^*=-\mathbb J(u)}
\]

and, because two arguments then coincide,

\[
\boxed{
\mathbb J(u)\nabla H
=
\mathbb J(u)(Cu)
=0.
}
\]

The latter is the phase-space operator version of

\[
\iota_\omega\iota_\omega\mathrm{vol}=0.
\]

**Classification: Exact alternating-operator identity.**

---

## 3. The induced two-bracket is exactly Lie--Poisson

For a sufficiently smooth real functional `F[u]`, let `grad F` denote its `L^2`
gradient in the divergence-free phase space.  Define

\[
\boxed{
\{\mathcal F,\mathcal G\}_{LP}(u)
:=
\Omega(\nabla\mathcal F,\nabla\mathcal G,Cu).
}
\]

Equivalently,

\[
\{\mathcal F,\mathcal G\}_{LP}
=
\langle\nabla\mathcal F,
\mathbb J(u)\nabla\mathcal G\rangle.
\]

Let the divergence-free vector-field Lie bracket be

\[
[a,b]_{\rm Lie}
:=
(a\cdot\nabla)b-(b\cdot\nabla)a.
\]

Since

\[
[a,b]_{\rm Lie}
=-\nabla\times(a\times b)
\]

for divergence-free fields, periodic integration by parts and self-adjointness of
curl give

\[
\boxed{
\Omega(a,b,Cu)
=-\langle u,[a,b]_{\rm Lie}\rangle.
}
\]

Therefore

\[
\boxed{
\{\mathcal F,\mathcal G\}_{LP}(u)
=
-\left\langle
u,
[\nabla\mathcal F,\nabla\mathcal G]_{\rm Lie}
\right\rangle.
}
\]

This is the Lie--Poisson bracket on the dual of the divergence-free vector-field Lie
algebra, after the `L^2` identification used throughout the repository.  Hence on
the standard smooth/cylinder functional domain it is antisymmetric, obeys the
Leibniz rule, and satisfies Jacobi.

A lightweight symbolic periodic referee independently verifies both

\[
\int u\cdot[a,b]_{\rm Lie}
+
\int(Cu)\cdot(a\times b)
=0
\]

and the vector-field Jacobi identity for explicit smooth divergence-free trigonometric
fields.  This is only a sign/Jacobi referee; the theorem is the exact Lie-algebra
identity above.

**Classification: Exact Lie--Poisson identification; audited sign/Jacobi referee.**

---

## 4. Energy is the Hamiltonian and helicity is a Casimir

The projected Euler velocity field is

\[
X_E(u)
:=
\mathbb J(u)\nabla E
=
P(u\times\omega).
\]

Therefore for every smooth functional `F`,

\[
\boxed{
\left(\frac d{dt}\mathcal F\right)_{Euler}
=
\{\mathcal F,E\}_{LP}
=
\Omega(\nabla\mathcal F,\nabla E,\nabla H).
}
\]

This is the functional version of the de Rham/Lamb law.  The Euler nonlinearity is
not merely energy-skew for one quadratic observable: it is a Hamiltonian vector
field on the entire functional algebra.

Because

\[
\mathbb J(u)\nabla H=0,
\]

one has for **every** smooth functional `F`

\[
\boxed{
\{\mathcal F,H\}_{LP}=0.
}
\]

Thus helicity is a Casimir of this Poisson structure.  Energy and helicity
conservation are now two different structural statements generated by one operator:

- `E` is the Hamiltonian whose Poisson vector field moves the state;
- `H` is a Casimir whose gradient is the null direction used to build that same
  Poisson tensor.

In particular,

\[
\boxed{
\langle X_E,\nabla E\rangle=0,
\qquad
\langle X_E,\nabla H\rangle=0.
}
\]

The inviscid velocity is tangent simultaneously to the kinetic-energy and helicity
level sets wherever these gradients are regular.

**Classification: Exact Hamiltonian/Casimir identities.**

---

## 5. Viscosity is metric gradient descent of the squared Casimir gradient

The viscous velocity is

\[
-\nu C^2u.
\]

But Section 1 gives

\[
\nabla Z=C^2u,
\qquad
Z=\frac12\|\nabla H\|_2^2.
\]

Hence

\[
\boxed{
-\nu C^2u
=
-\nu\nabla Z
=
-\nu\nabla\frac12\|\nabla H\|_2^2.
}
\]

This is ordinary `L^2` metric gradient descent.  Introduce the positive symmetric
functional pairing

\[
\boxed{
(\mathcal F,\mathcal G)_{L^2}
:=
\langle\nabla\mathcal F,\nabla\mathcal G\rangle.
}
\]

Then viscosity contributes

\[
\boxed{
\left(\frac d{dt}\mathcal F\right)_{visc}
=-\nu(\mathcal F,Z)_{L^2}.
}
\]

The same helicity functional therefore plays two linked roles:

1. `grad H=omega` is a null direction of the conservative Poisson operator;
2. the squared norm of that same null direction is exactly the viscous potential
   `2Z=||omega||_2^2`.

This yields the particularly compact energy law

\[
\boxed{
\dot E
=-\nu\|\nabla H\|_2^2
=-2\nu Z.
}
\]

Thus the field direction annihilated by the nonlinear Poisson tensor is exactly the
field whose squared norm measures the energy drain by viscosity.

**Classification: Exact metric-gradient/Casimir-gradient identity.**

---

## 6. Whole-PDE functional master law

Combining Sections 4 and 5, every smooth incompressible Navier--Stokes solution obeys

\[
\boxed{
\partial_tu
=
\mathbb J(u)\nabla E
-
\nu\nabla Z.
}
\]

Since `Z=||grad H||^2/2`, this is equivalently

\[
\boxed{
\partial_tu
=
(\iota_{\nabla H}\Omega)^\sharp\nabla E
-
\nu\nabla\frac12\|\nabla H\|_2^2.
}
\]

Because `H` is quadratic, its phase-space Hessian is the constant self-adjoint Hodge
operator

\[
\boxed{\nabla^2H=C.}
\]

Therefore the viscous gradient is itself generated by `H`:

\[
\boxed{
\nabla\frac12\|\nabla H\|_2^2
=\nabla^2H\,\nabla H.
}
\]

The full PDE can consequently be written with **only the two canonical functionals**
`E` and `H` plus the fixed `L^2` geometry and the constant alternating `Omega`:

\[
\boxed{
\partial_tu
=
\Omega^\sharp(\nabla E,\nabla H)
-\nu\,\nabla^2H\,\nabla H,
}
\]

where `Omega^sharp(b,c)` is defined by
`<a,Omega^sharp(b,c)>=Omega(a,b,c)`.  The first term uses `grad H` through an
alternating contraction; the second uses the same `grad H` through the symmetric
Hessian of `H`.  `Z` is therefore a derived metric potential, not a third generator.

For every sufficiently smooth real functional `F[u]`, chain rule gives the universal
observable law

\[
\boxed{
\frac d{dt}\mathcal F(u(t))
=
\{\mathcal F,E\}_{LP}
-
\nu(\mathcal F,Z)_{L^2}.
}
\]

Or, with no bracket notation,

\[
\boxed{
\frac d{dt}\mathcal F
=
\Omega(\nabla\mathcal F,\nabla E,\nabla H)
-
\nu\left\langle
\nabla\mathcal F,
\nabla\frac12\|\nabla H\|_2^2
\right\rangle.
}
\]

This is the current smallest **whole-functional operator law** in the repository.
It contains the full PDE rather than one selected norm or spectral family.

Only three geometric ingredients appear:

\[
\boxed{
\text{constant alternating }\Omega,
\qquad
\text{kinetic }E,
\qquad
\text{helicity }H,
}
\]

with viscosity obtained from the metric norm of `grad H`.  `Z` is therefore derived,
not a third primitive generator.

**Classification: Exact whole-functional Navier--Stokes identity.**

---

## 7. The signed-curl three-current is only coordinates of `Omega`

Let

\[
Cu_c=c\,u_c
\]

be the signed curl decomposition from the preceding milestone.  Its alternating
three-current was

\[
\mathscr T_{cdr}
=
\int u_c\cdot(u_d\times u_r)\,dx.
\]

But by definition

\[
\boxed{
\mathscr T_{cdr}
=
\Omega(u_c,u_d,u_r).
}
\]

Hence `T` is not a new nonlinear state and not even a new primitive operator.  It is
simply the matrix/tensor of the **same constant phase-space three-form `Omega`** in
the signed-curl spectral decomposition of the actual velocity.

Similarly,

\[
\mathscr J_{cd}
=\sum_r r\mathscr T_{cdr}
\]

is the spectral matrix of the contracted two-form

\[
\iota_{\nabla H}\Omega.
\]

Thus the entire preceding spectral-current architecture is the coordinate image

\[
\boxed{
\Omega
\xrightarrow{\ \iota_{\nabla H}\ }
\mathbb J(u)
\xrightarrow{\ \nabla E\ }
X_E(u).
}
\]

**Classification: Exact representation reduction.**

---

## 8. The determinant theorem is the quadratic shadow of the phase-space law

Let `f` be a real signed-curl spectral multiplier and define

\[
Q_f(u)
=
\frac12\langle u,f(C)u\rangle.
\]

Then

\[
\nabla Q_f=f(C)u.
\]

The full Euler rate is therefore simply

\[
\boxed{
(\dot Q_f)_{Euler}
=
\Omega(f(C)u,u,Cu).
}
\]

Expanding all three arguments in signed-curl blocks gives

\[
\sum_{c,d,r}f(c)r\,\mathscr T_{cdr}.
\]

Full alternation of `Omega`, equivalently of `T`, antisymmetrizes the coefficient and
produces exactly the preceding determinant

\[
\mathfrak D_f(c,d,r)
=
\det
\begin{pmatrix}
1&1&1\\
c&d&r\\
f(c)&f(d)&f(r)
\end{pmatrix}.
\]

Hence

\[
\boxed{
(\dot Q_f)_{Euler}
=
\frac16\sum_{c,d,r}
\mathfrak D_f(c,d,r)\mathscr T_{cdr}.
}
\]

The determinant theorem therefore does not add a spectral mechanism.  It is the
coordinate formula for evaluating one constant alternating three-form on

\[
\nabla Q_f,
\quad
\nabla E,
\quad
\nabla H.
\]

In particular, affine `f=a+bc` gives

\[
Q_f=aE+bH,
\]

so its nonlinear rate vanishes because `E` is the Hamiltonian and `H` is a Casimir.
The previous "affine kernel" is exactly the span of these two phase-space generators.

**Classification: Exact descent of the spectral determinant theorem.**

---

## 9. Stretching, critical chirality and heat flux are one functional law

### 9.1 Vortex stretching

For

\[
Z=\frac12\langle u,C^2u\rangle,
\]

the Euler production is

\[
\boxed{
(\dot Z)_{Euler}
=
\{Z,E\}_{LP}
=
\Omega(C^2u,u,Cu)
=
\int\omega\cdot S\omega\,dx.
}
\]

Thus stretching is the Hamiltonian derivative of the viscous potential `Z`.

The complete enstrophy law is

\[
\boxed{
\dot Z
=
\{Z,E\}_{LP}
-
\nu\|\nabla Z\|_2^2.
}
\]

This is the exact tangent-Hamiltonian versus metric-gradient-square form of the
familiar stretching/dissipation balance.

### 9.2 Positive critical quantity

Let

\[
\mathcal K
=
\frac12\langle u,|C|u\rangle.
\]

Then

\[
\boxed{
(\dot{\mathcal K})_{Euler}
=
\{\mathcal K,E\}_{LP}.
}
\]

On a purely positive-curl sector,

\[
\mathcal K=H,
\]

while on a purely negative-curl sector,

\[
\mathcal K=-H.
\]

Since `H` is a Casimir,

\[
\boxed{
(\dot{\mathcal K})_{Euler}=0
\quad\text{on every one-sign curl sector}.
}
\]

The preceding heterochiral theorem is therefore the phase-space statement that the
positive critical functional ceases to be a Casimir only when the state straddles
the kink of `|C|` across the two curl signs.

### 9.3 Canonical heat-scale flux

For fixed heat age `h`, define

\[
\mathcal E_h(u)
=
\frac12\langle u,e^{-hC^2}u\rangle.
\]

Then

\[
\nabla\mathcal E_h=e^{-hC^2}u
\]

and the nonlinear heat flux from the previous milestone is exactly

\[
\boxed{
\Pi(h)
=-\{\mathcal E_h,E\}_{LP}.
}
\]

Thus stretching, critical chirality transfer, spectral determinants and the entire
heat-scale flux are all functional evaluations of one Lie--Poisson vector field.

**Classification: Exact whole-family functional synthesis.**

---

## 10. Beltrami states are rank-collapse equilibria of the alternating generator plane

Suppose

\[
Cu=c\,u
\]

for one nonzero signed curl eigenvalue.  Then

\[
\boxed{
\nabla H=c\,\nabla E.
}
\]

The two generator directions entering `Omega` are linearly dependent.  Therefore

\[
\boxed{
X_E
=(\iota_{\nabla H}\Omega)^\sharp\nabla E
=0.
}
\]

This recovers the exact Beltrami fact

\[
u\times\omega=0
\]

without introducing a separate calibration mechanism.  The Navier--Stokes solution
then follows only the metric-gradient leg:

\[
\boxed{
u(t)=e^{-\nu c^2t}u_0.}
\]

Hence the earlier no-go against "thin heat layer = badness" has a direct phase-space
explanation: arbitrarily high curl frequency can be completely benign when the
Hamiltonian/Casimir generator plane collapses to one dimension.

**Classification: Exact Beltrami/phase-space rank-collapse identity.**

---

## 11. The nonlinear null direction is exactly viscosity's energy-drain field

The operator law contains a particularly rigid self-compatibility:

\[
\boxed{
\mathbb J(u)\nabla H=0,
\qquad
-\dot E/\nu=\|\nabla H\|_2^2.
}
\]

Thus the same physical field

\[
\nabla H=Cu=\omega
\]

appears in two apparently opposite roles:

1. it is invisible as an input direction to the conservative Poisson tensor;
2. its squared norm is exactly the rate at which viscosity drains kinetic energy.

Moreover the viscous vector itself is one further action of the same Hodge operator:

\[
\boxed{
-\nu\nabla Z
=-\nu C\nabla H.
}
\]

So below all previous representations the first and second curl derivatives have a
minimal division of labor:

\[
\boxed{
\begin{array}{c}
C\nabla E=\nabla H
\quad\text{creates the alternating conservative Poisson tensor},\\[1mm]
C\nabla H=\nabla Z
\quad\text{creates the metric dissipative direction}.
\end{array}
}
\]

This is the variational form of the earlier "first derivative rotates, its square
dissipates" theorem.

**Classification: Exact operator-level synthesis.**

---

## 12. What the whole-functional law removes from the primitive list

The following are no longer independent mechanisms beneath this theorem:

- pressure projection: part of the divergence-free phase-space/Lie--Poisson
  identification;
- energy conservation: antisymmetry of the Hamiltonian bracket;
- Euler helicity conservation: Casimir nullity;
- vortex stretching: Hamiltonian derivative `{Z,E}`;
- signed-curl alternating three-current: spectral coordinates of `Omega`;
- determinant/divided-difference law: quadratic spectral coordinates of
  `Omega(grad Q_f,grad E,grad H)`;
- homochiral critical cancellation: `K=+/-H` on one-sign sectors;
- canonical heat-scale nonlinear flux: `-{E_h,E}`;
- Beltrami nonlinear collapse: `grad H` parallel to `grad E`;
- viscosity: metric gradient descent of `||grad H||^2/2`.

Thus the current primitive grammar is

\[
\boxed{
\text{one constant alternating phase-space 3-form}
+
\text{energy Hamiltonian}
+
\text{helicity Casimir}
+
\text{metric descent of the Casimir-gradient norm}.
}
\]

Even `Z` is derived from `H` rather than primitive.

**Classification: Rigorous synthesis of exact identities.**

---

## 13. Euler sees only the tangent quotient modulo `dE` and `dH`

At a fixed smooth state define the closed phase-space normal subspace

\[
\mathcal N_u
:=
\operatorname{span}\{\nabla E,\nabla H\}
=
\operatorname{span}\{u,Cu\},
\]

with dimension one in the degenerate Beltrami case and dimension two otherwise.  Let

\[
\mathcal T_u:=\mathcal N_u^\perp
\]

and let `P_T`, `P_N` be the corresponding orthogonal projections.

Section 4 gives

\[
X_E\perp\nabla E,
\qquad
X_E\perp\nabla H,
\]

so

\[
\boxed{X_E\in\mathcal T_u.}
\]

Consequently every functional Euler derivative factors through the tangent quotient:

\[
\boxed{
\{\mathcal F,E\}_{LP}
=
\langle X_E,P_T\nabla\mathcal F\rangle.
}
\]

Any normal addition to the functional gradient is invisible to Euler.  In
particular, for every smooth scalar function `Phi(E,H)`,

\[
\boxed{
\{\mathcal F+\Phi(E,H),E\}_{LP}
=
\{\mathcal F,E\}_{LP}.
}
\]

Thus the Euler operator acts on observables only modulo the two canonical directions
`dE,dH`.  The affine null family `f(c)=a+bc` in the preceding signed-curl determinant
theorem is exactly the quadratic spectral coordinate shadow of this whole-functional
quotient.

Now apply the quotient to the viscous potential `Z`.  Define the leaf-tangent and
normal pieces

\[
\boxed{
R_Z:=P_T\nabla Z,
\qquad
N_Z:=P_N\nabla Z,
\qquad
\nabla Z=R_Z+N_Z.
}
\]

Then

\[
\boxed{
\{Z,E\}_{LP}
=
\langle X_E,R_Z\rangle.
}
\]

The complete Navier--Stokes vector has the exact instantaneous orthogonal split

\[
\boxed{
\begin{aligned}
P_T\partial_tu
&=X_E-\nu R_Z,\\
P_N\partial_tu
&=-\nu N_Z.
\end{aligned}
}
\]

Therefore the enstrophy law sharpens to

\[
\boxed{
\dot Z
=
\langle X_E,R_Z\rangle
-
\nu\|R_Z\|_2^2
-
\nu\|N_Z\|_2^2.
}
\]

This is not an estimate.  It is an exact geometric decomposition of the literal PDE.
Only the leaf-tangent gradient residual `R_Z` can participate in nonlinear enstrophy
production, while viscosity pays for that same tangent residual **and** the entire
normal component `N_Z`.

For a quadratic spectral observable

\[
Q_f=\frac12\langle u,f(C)u\rangle,
\]

the relevant Euler gradient is therefore

\[
P_T f(C)u.
\]

In signed-curl coordinates this is precisely the residual after removing the best
`L^2` component in the affine span of `u` and `Cu`; equivalently it is the
phase-space form of the second-spectral-curvature information detected by the
three-point determinant.  No new spectral residual is introduced as a primitive:
`P_T` is fixed canonically by the two generators `E,H`.

Two immediate exact null cases become transparent:

1. on a one-sign curl sector, `grad K=+/- grad H`, hence `P_T grad K=0` and critical
   Euler transfer vanishes;
2. on a pure Beltrami state, `grad H` is parallel to `grad E`, the alternating
   Hamiltonian plane collapses and `X_E=0`.

The no-escape obstruction is therefore narrower than the raw competition
`stretching versus viscosity`: a candidate growth episode must keep the
self-generated Hamiltonian tangent vector aligned with the **leaf-tangent gradient
of Hodge complexity**, while viscosity acts against exactly that tangent gradient
and additionally drains the normal gradient component.

**Classification: Exact tangent-quotient / orthogonal Poisson--gradient decomposition.**

---

## 14. Canonical transverse Casimir defect: the entire Euler engine lives off Beltrami alignment

The tangent quotient of Section 13 admits a particularly rigid canonical
representative.  Assume `E>0` and define the signed global curl barycenter

\[
\boxed{
\alpha(u):=\frac{H(u)}{E(u)}.
}
\]

Define the transverse Casimir-gradient defect

\[
\boxed{
B
:=
\nabla H-\alpha\nabla E
=
(C-\alpha)u
=
\omega-\alpha u.
}
\]

By construction,

\[
\boxed{\langle u,B\rangle=0.}
\]

This is not an externally chosen alignment score.  It is the canonical orthogonal
projection of the Casimir gradient `grad H` away from the Hamiltonian gradient
`grad E`.

Its positive squared norm is

\[
\begin{aligned}
\frac12\|B\|_2^2
&=
Z-\frac{H^2}{E}.
\end{aligned}
\]

Thus define only as shorthand

\[
\boxed{
D_B
:=
Z-\frac{H^2}{E}
=
\frac12\|B\|_2^2
\ge0.
}
\]

Spectrally, if `e_c/E` is the normalized signed-curl energy measure, then

\[
\boxed{
\alpha=\mathbb E(c),
\qquad
\frac{D_B}{E}=\operatorname{Var}(c).
}
\]

So `B` is the physical vector representative of the canonical signed-curl variance,
not a new modeled state.

### 14.1 Euler ignores the Beltrami-aligned component exactly

Since

\[
\omega=\alpha u+B,
\]

pointwise alternation gives

\[
\boxed{
 u\times\omega
=u\times B.
}
\]

Therefore

\[
\boxed{
X_E=P(u\times B).
}
\]

The full Hamiltonian evolution sees only the transverse defect `B`.  The component
`alpha u` of vorticity can be arbitrarily large without entering the Lamb current at
all.

At the level of every observable,

\[
\boxed{
\{\mathcal F,E\}_{LP}
=
\Omega(\nabla\mathcal F,u,B).
}
\]

Thus the actual Euler vector depends on the Casimir gradient only modulo its
projection onto `grad E`.

### 14.2 The defect functional has an exact closed energy law

The functional gradient of `D_B` is

\[
\boxed{
\nabla D_B
=
C^2u-2\alpha Cu+\alpha^2u
=
(C-\alpha)^2u
=
(C-\alpha)B.
}
\]

Because `E` and `H` have zero Euler derivative,

\[
\{D_B,E\}_{LP}=\{Z,E\}_{LP}.
\]

Using `X_E=P(u\times B)`, `B\perp u`, and self-adjointness of `C`,

\[
\boxed{
\{D_B,E\}_{LP}
=
\langle u\times B,CB\rangle.
}
\]

The metric term collapses just as rigidly.  Since

\[
\nabla Z=C^2u
\]

and

\[
\nabla D_B=(C-\alpha)B,
\]

direct expansion using `B\perp u` and

\[
\langle u,CB\rangle
=
\langle Cu,B\rangle
=
\|B\|_2^2
\]

gives

\[
\boxed{
\langle\nabla D_B,\nabla Z\rangle
=
\|CB\|_2^2.
}
\]

Therefore the literal Navier--Stokes evolution of the canonical non-Beltrami defect
is

\[
\boxed{
\dot D_B
=
\langle u\times B,CB\rangle
-
\nu\|CB\|_2^2.
}
\]

Equivalently,

\[
\boxed{
\frac12\frac d{dt}\|B\|_2^2
=
\int (u\times B)\cdot CB\,dx
-
\nu\|CB\|_2^2.
}
\]

No `alpha_dot` remainder survives.  The modulation by `alpha=H/E` is exactly the
one that makes the defect energy law close at this quadratic level.

This has the same skew-square grammar as the original enstrophy law, but with raw
vorticity replaced by the **only part of the Casimir gradient that can actually drive
Euler motion**.

### 14.3 Exact defect PDE and modulation law

Since

\[
B=(C-\alpha)u,
\]

differentiation of the full Navier--Stokes equation gives

\[
\boxed{
\partial_tB
=
(C-\alpha)X_E
-
\nu C^2B
-
\dot\alpha\,u,
\qquad
X_E=P(u\times B).
}
\]

The last term is an orthogonality/modulation term; it performs no direct work in the
`B` energy because `<B,u>=0`.

Euler alone keeps both `E` and `H` fixed, so `alpha=H/E` has no Euler drift.  Under
full Navier--Stokes its exact evolution is

\[
\boxed{
\dot\alpha
=-\frac{\nu}{E}
\langle B,(C+\alpha)B\rangle.
}
\]

Thus even the global Beltrami center `alpha` can move only through the transverse
defect.  If `B=0`, then

\[
X_E=0,
\qquad
\dot\alpha=0,
\]

and one recovers pure Beltrami heat decay.

### 14.4 Nonlinearity sees defect; viscosity pays for both coherent and defective curl

The enstrophy itself decomposes as

\[
\boxed{
Z
=
\alpha^2E+D_B.
}
\]

Hence the kinetic-energy law becomes

\[
\boxed{
\dot E
=-2\nu(\alpha^2E+D_B).
}
\]

The asymmetry is exact:

\[
\boxed{
\begin{gathered}
\text{Euler nonlinearity uses only }B,\\
\text{viscosity drains the full }\omega=\alpha u+B.
\end{gathered}
}
\]

A large Beltrami-aligned curl component `alpha u` therefore strengthens viscous
energy loss but contributes nothing directly to the Euler Lamb current.  The only
nonlinear engine is transverse Casimir-gradient defect.

### 14.5 Critical excess above signed helicity is defect-controlled

The positive critical quadratic has signed-curl representation

\[
\mathcal K=\sum_c |c|e_c,
\qquad
H=\sum_c c\,e_c,
\qquad
E=\sum_c e_c.
\]

Since `alpha=H/E`, the elementary pointwise spectral inequality

\[
|c|\le |\alpha|+|c-\alpha|
\]

and Cauchy--Schwarz give

\[
\begin{aligned}
\mathcal K
&\le
|\alpha|E
+
\sum_c|c-\alpha|e_c\\
&\le
|H|+\sqrt{E D_B}.
\end{aligned}
\]

Together with `|H|<=K`, this yields the exact intrinsic estimate

\[
\boxed{
0\le\mathcal K-|H|
\le
\sqrt{E D_B}.
}
\]

The inequality is not promoted as a regularity criterion.  Its structural meaning is
that the part of the positive critical size not already accounted for by the signed
Casimir is controlled by the canonical transverse Casimir defect.  Conversely, a
large Beltrami-aligned critical contribution may make `K` large without directly
feeding Euler nonlinearity; its center `alpha=H/E` can itself move only through `B`
by Section 14.3.

**Classification: Rigorous consequence of the exact signed-curl/defect decomposition.**

An exact rational signed-curl referee verifies simultaneously
`D_B=||B||^2/2`, the defect energy law, and the `alpha_dot` formula with zero
residual.  This is only a factor/cancellation referee; the identities follow from
the whole-functional Poisson--gradient law.

**Classification: Exact canonical Beltrami-defect / transverse-Casimir-gradient law.**

---

## 15. No-escape frontier after the whole-PDE compression

The previous frontier was an infinite heterochiral signed-curl triangle cascade.
That remains a correct spectral description, but it is now recognized as a
coordinate shadow of a smaller phase-space question.

Write

\[
X_E(u)
:=
\mathbb J(u)\nabla E.
\]

Then

\[
\boxed{
\langle X_E,\nabla E\rangle=0,
\qquad
\langle X_E,\nabla H\rangle=0,
}
\]

while

\[
\boxed{
\partial_tu
=X_E-\nu\nabla Z,
\qquad
Z=\frac12\|\nabla H\|_2^2.
}
\]

A candidate singular escape must therefore be generated by a Hamiltonian tangent
motion that preserves `E` and `H` instantaneously but continually drives higher
Hodge complexity, while the metric leg descends the squared norm of the very Casimir
gradient used to build the Poisson tensor.

Section 14 sharpens this further.  With

\[
lpha=H/E,
\qquad
B=\omega-lpha u,
\]

one has the exact active/benign split

\[
oxed{
X_E=P(u	imes B),
\qquad
\dot E=-2
u(lpha^2E+D_B),
\qquad
D_B=rac12\|B\|_2^2,
}
\]

and

\[
oxed{
\dot D_B
=\langle u	imes B,CB
angle-
u\|CB\|_2^2.
}
\]

Thus arbitrarily large Beltrami-aligned vorticity is not itself an Euler engine.
Any genuinely nonlinear escape must maintain transverse Casimir defect and its Hodge
derivative; meanwhile viscosity drains both that defect and the aligned curl
component that is nonlinearly invisible.

At enstrophy level the exact unresolved competition is

\[
\boxed{
\dot Z
=
\underbrace{\Omega(\nabla Z,\nabla E,\nabla H)}_{\text{Hamiltonian tangent ascent/descent of }Z}
-
\underbrace{\nu\|\nabla Z\|_2^2}_{\text{metric gradient-square loss}}.
}
\]

The amplitude-scaling no-go from earlier milestones still rules out a universal
instantaneous domination of the first term by the second.  Therefore a true
no-escape theorem, if one exists, must be a **dynamic compatibility theorem** for
this self-generated Poisson--gradient pair, not another snapshot inequality.

In the present variables the literal question is

\[
\boxed{
\begin{gathered}
\text{Can the Hamiltonian flow generated by }E\text{ on the Casimir geometry of }H\\
\text{drive }\|\nabla H\|\text{ and higher Hodge moments through a finite-time escape,}\\
\text{while the same }H\text{ generates the metric potential }\frac12\|\nabla H\|^2\\
\text{whose gradient is being descended by viscosity?}
\end{gathered}
}
\]

No theorem here proves that it cannot.

The spectral heterochiral-chain frontier, the heat-age Zeno frontier, and the
material-Hodge distortion frontier are now three representations of this same
functional problem.  Any future theorem that treats them as independent mechanisms
would be below the compression already proved here.

**Classification: Conjectural bridge / Open.**

No no-escape, blow-up exclusion, restart, continuation, or global-regularity theorem
is claimed.

---

## 16. Classification

**Exact identity**

- constant alternating phase-space three-form
  `Omega(a,b,c)=int a.(b cross c)`;
- Hodge gradient ladder `grad E=u`, `grad H=Cu`, `grad Z=C^2u`;
- `Z=||grad H||^2/2`;
- Poisson operator `J(u)v=P(v cross Cu)=i_(grad H) Omega` in pairing form;
- skewness `J(u)^*=-J(u)` and Casimir nullity `J(u) grad H=0`;
- Lie--Poisson bracket
  `{F,G}=Omega(grad F,grad G,grad H)=-<u,[grad F,grad G]_Lie>`;
- whole-functional NS law `Fdot={F,E}-nu(F,Z)_(L2)`;
- viscosity `-nu grad Z=-nu grad ||grad H||^2/2`;
- spectral three-current `T_cdr=Omega(u_c,u_d,u_r)`;
- determinant theorem as the quadratic spectral coordinate form of the phase-space
  law;
- stretching `{Z,E}`, homochiral critical Casimir reduction, heat flux
  `Pi=-{E_h,E}`;
- Beltrami rank collapse `grad H=c grad E => X_E=0`;
- tangent quotient `X_E in span{grad E,grad H}^perp` and the orthogonal split
  `P_T u_t=X_E-nu R_Z`, `P_N u_t=-nu N_Z`;
- canonical transverse defect `alpha=H/E`, `B=(C-alpha)u`,
  `D_B=Z-H^2/E=||B||^2/2`;
- active-defect law `X_E=P(u cross B)` and
  `D_Bdot=<u cross B,C B>-nu||C B||^2`;
- defect PDE `B_t=(C-alpha)X_E-nu C^2B-alpha_dot u` and modulation law
  `alpha_dot=-(nu/E)<B,(C+alpha)B>`;
- enstrophy decomposition `Z=alpha^2 E+D_B`.

**Rigorous consequence**

- the preceding whole quadratic/spectral family is subsumed by one functional law;
- energy is Hamiltonian while helicity is a Casimir of the same Poisson operator;
- the nonlinear vector field is tangent to both energy and helicity levels;
- the same helicity gradient annihilated by the Poisson tensor supplies the exact
  viscous energy-drain norm;
- the signed-curl triangle, heat-scale and material-Hodge frontiers are
  representations of one Poisson--gradient compatibility problem;
- Euler sees observables only through their cotangent class modulo `dE,dH`;
- only the transverse Casimir defect can drive the actual Euler vector, whereas
  viscosity dissipates the full Casimir gradient.

**Audited algebra referee**

- explicit smooth divergence-free periodic trigonometric fields verify
  `Omega(a,b,Cu)=-<u,[a,b]_Lie>` and the vector-field Jacobi identity symbolically;
- previous exact rational signed-curl referees then become coordinate checks of the
  same constant `Omega`;
- an exact rational three-label referee verifies with zero residual
  `D_B=||B||^2/2`, the defect energy law, and the `alpha_dot` modulation identity.

**Conjectural bridge / Open**

- a dynamic obstruction preventing Hamiltonian tangent transfer from producing a
  finite-time escape against metric descent of `||grad H||^2/2`;
- exclusion of the equivalent infinite heterochiral spectral chain / zero-heat-age
  Zeno concentration / unbounded material-conjugacy distortion;
- no-escape/blow-up exclusion;
- restart/continuation/global regularity.
