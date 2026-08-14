# Hodge--strain / null-Lagrangian compatibility of the material NS gradient

This note continues the compression begun in the material Hodge--Bochner theorem.
It does **not** add a badness score, packet mechanism, auxiliary metric model, or
continuation criterion.  The question is whether the two objects in the current
frontier,

\[
(G_t,\bar\beta_t),
\]

are really independent even instantaneously.

They are not.  Once the harmonic/Galilean velocity mode is fixed, the same exact
vorticity two-form `bar beta` Hodge-reconstructs the material velocity one-form
`bar alpha`.  The covariant gradient of that one-form has the exact pointwise split

\[
\boxed{
\nabla^G\bar\alpha
=E+\frac12\bar\beta,
\qquad
E=\operatorname{Sym}\nabla^G\bar\alpha=\frac12\partial_tG.
}
\]

Thus material metric velocity and material vorticity are the symmetric and
antisymmetric faces of **one actual covariant gradient**.  Because that gradient is
trace-free, integrable, and lives on a flat volume-preserving material geometry,
its quadratic and cubic minors are not free.  Their null-Lagrangian identities are
exactly the familiar strain--vorticity equipartition, pressure Poisson law, and
Betchov stretching relation.

The new compression is therefore:

\[
\boxed{
\text{metric rate / strain}
\quad+\quad
\text{vorticity form}
\quad=\quad
\text{one incompressible integrable velocity gradient}.
}
\]

No no-escape, restart, continuation, or global-regularity theorem is claimed.

---

## 1. Material gradient split

Use the notation of `material_hodge_bochner_master_compatibility.md`.  On the
material torus,

\[
\bar\alpha=U^{\flat_G},
\qquad
\bar\beta=d\bar\alpha,
\qquad
\delta_G\bar\alpha=0,
\qquad
\partial_tG=\mathcal L_U G.
\]

Metric compatibility and torsion-freeness give

\[
(d\bar\alpha)_{ij}
=\nabla_i^G\bar\alpha_j-\nabla_j^G\bar\alpha_i,
\]

while

\[
(\mathcal L_U G)_{ij}
=\nabla_i^G\bar\alpha_j+\nabla_j^G\bar\alpha_i.
\]

Hence, as a covariant two-tensor,

\[
\boxed{
\nabla^G\bar\alpha
=\frac12\partial_tG+\frac12\bar\beta.
}
\]

Define

\[
E:=\frac12\partial_tG
=\operatorname{Sym}\nabla^G\bar\alpha.
\]

Then incompressibility gives

\[
\boxed{\operatorname{tr}_GE=0.}
\]

If `A=\nabla^G U` is read as a `(1,1)` endomorphism and

\[
K:=G^{-1}E=\operatorname{Sym}_G A,
\]

then the skew part of `A` is the metric endomorphism corresponding to
`bar beta/2`.  In three dimensions let

\[
b=(\,*_G\bar\beta\,)^{\sharp_G}.
\]

The skew part is the cross-product operator with axial vector `b/2`.

This is not a modeled decomposition: it is the symmetric/antisymmetric split of the
literal NS velocity gradient after the exact material pullback.

**Classification: Exact identity.**

---

## 2. Local integrability is stronger than the split

Because

\[
A_{ij}=\nabla_i^G\bar\alpha_j
\]

is an actual covariant gradient and `G` is flat,

\[
\boxed{
\nabla_k^G A_{ij}-\nabla_i^G A_{kj}=0.
}
\]

Therefore `E` and `bar beta` cannot be varied independently even at first spatial
order:

\[
\boxed{
\nabla_k^G E_{ij}-\nabla_i^G E_{kj}
=-\frac12
\left(
\nabla_k^G\bar\beta_{ij}-\nabla_i^G\bar\beta_{kj}
\right).
}
\]

Together with `tr_G E=0`, this is the local flat gradient-integrability/Hodge compatibility of the
material strain and vorticity faces.  It is the local differential reason that the
strain is an order-zero Hodge transform of vorticity rather than an independent
symmetric tensor.

Equivalently, define the intrinsic Hodge--strain map

\[
\mathfrak S_G:\bar\beta\mapsto
E=\operatorname{Sym}\nabla^G(\mathcal B_G\bar\beta)^{\flat_G},
\]

where `mathcal B_G` is any co-closed Hodge/Biot--Savart primitive of `bar beta`.  Two such primitives differ by a harmonic one-form; on a flat torus harmonic one-forms are parallel, so their symmetric gradients vanish.  Thus `mathfrak S_G` is well-defined even before fixing the harmonic/Galilean velocity mode.  Then

\[
\boxed{\partial_tG=2\mathfrak S_G\bar\beta.}
\]

No new state has been introduced: `mathfrak S_G` is simply the symmetric-gradient
readout of the same reconstructed NS velocity.

**Classification: Exact local compatibility / rigorous Hodge reconstruction.**

---

## 3. The Hodge--strain map is a scaled `L^2` isometry

At each fixed time `(T^3,G)` is flat and isometric to the physical Euclidean torus.
For a co-closed one-form `bar alpha`, the flat Weitzenbock identity gives

\[
\int |\nabla^G\bar\alpha|_G^2\,dV_G
=
\int |d\bar\alpha|_G^2\,dV_G.
\]

The symmetric and antisymmetric parts of `nabla bar alpha` are orthogonal, and

\[
\left|\operatorname{Skew}\nabla^G\bar\alpha\right|_G^2
=\frac12|\bar\beta|_G^2.
\]

Therefore

\[
\boxed{
\int |E|_G^2\,dV_G
=\frac12\int|\bar\beta|_G^2\,dV_G.
}
\]

Since `partial_t G=2E`,

\[
\boxed{
\|\partial_tG\|_{L^2(G)}^2
=2\|\bar\beta\|_{L^2(G)}^2.
}
\]

Polarization gives, for two exact vorticity forms,

\[
\boxed{
\langle\mathfrak S_G\beta_1,\mathfrak S_G\beta_2\rangle_{L^2(G)}
=\frac12\langle\beta_1,\beta_2\rangle_{L^2(G)}.
}
\]

Thus the metric-rate/strain representation and the vorticity representation carry
exactly the same instantaneous `L^2` information up to the forced factor `1/2`.

Because `G` is flat, the same statement holds after any fixed number of covariant
derivatives.  For every integer `m>=0`,

\[
\boxed{
\|\nabla_G^m E\|_{L^2(G)}^2
=\frac12\|\nabla_G^m\bar\beta\|_{L^2(G)}^2,
}
\]

or equivalently

\[
\boxed{
\|\nabla_G^m\partial_tG\|_{L^2(G)}^2
=2\|\nabla_G^m\bar\beta\|_{L^2(G)}^2.
}
\]

This derivative tower is not a new estimate.  It is the Fourier/Hodge isometry
transported by the actual isometry `Phi_t:(T^3,G)->(T^3,g_0)`.

A lightweight Fourier-mode algebra referee verifies the forced factor
`2|S|^2=|omega|^2` for a generic transverse Fourier amplitude.  The theorem itself
is the exact Hodge identity above, not the computation.

**Classification: Exact global Hodge identity / rigorous derivative consequence.**

---

## 4. Total enstrophy is exactly material metric-speed energy

Let

\[
\mathcal E_\omega(t)
:=\frac12\int|\omega|^2\,dx
=\frac12\int|\bar\beta|_G^2\,dV_G.
\]

Section 3 gives

\[
\boxed{
\mathcal E_\omega
=\int|E|_G^2\,dV_G
=\frac14\|\partial_tG\|_{L^2(G)}^2.
}
\]

The ordinary kinetic-energy identity therefore becomes

\[
\boxed{
\frac d{dt}\frac12\int|U|_G^2\,dV_G
=-\frac\nu2\|\partial_tG\|_{L^2(G)}^2.
}
\]

So viscosity dissipates kinetic energy at exactly the squared speed of the
self-generated material metric path.  This is the standard NS energy law expressed
in the intrinsic geometry already forced by the PDE; no metric action has been
invented.

Likewise the bulk enstrophy dissipation is

\[
\boxed{
\nu\|\nabla^G\bar\beta\|_{L^2(G)}^2
=\frac\nu2
\|\nabla^G\partial_tG\|_{L^2(G)}^2.
}
\]

**Classification: Exact consequence of the NS energy law plus the Hodge--strain
isometry.**

---

## 5. Quadratic minor compatibility is exactly the pressure Poisson law

Return momentarily to physical Euclidean coordinates and write

\[
A=\nabla u=S+\Omega,
\qquad \operatorname{tr}A=0.
\]

The skew matrix `Omega` has axial vector `omega/2`; hence

\[
\operatorname{tr}(A^2)
=|S|^2-\frac12|\omega|^2.
\]

Because `A` is the gradient of a periodic divergence-free velocity,

\[
\operatorname{tr}(A^2)
=\nabla\cdot((u\cdot\nabla)u).
\]

Taking divergence of Navier--Stokes gives

\[
\boxed{
-\Delta p
=\operatorname{tr}(A^2)
=|S|^2-\frac12|\omega|^2.
}
\]

Pulling this identity back by `Phi_t` gives the intrinsic material law

\[
\boxed{
-\Delta_G\bar p
=|E|_G^2-\frac12|\bar\beta|_G^2.
}
\]

Thus pressure is not an independent producer and is not physically absent merely
because closed Kelvin currents kill its exact one-form.  Its scalar Poisson source
is exactly the **local defect from the global Hodge strain--vorticity
 equipartition**.

The source has zero spatial mean precisely because Section 3 forces

\[
\int|E|^2=\frac12\int|\bar\beta|^2.
\]

So pressure solvability, strain--vorticity equipartition, and the degree-two
null-Lagrangian identity are the same compatibility viewed three ways.

**Classification: Exact pressure/Hodge/null-Lagrangian identity.**

The pressure Hessian remains active in the symmetric velocity-gradient evolution.
Calling pressure a `gauge` is correct only for closed-current circulation.  It must
not be generalized into a claim that pressure is absent from the metric/strain
constraint sector.

**Classification: Rigorous architecture correction.**

---

## 6. Cubic minor compatibility is the Betchov stretching law

For any trace-free three-by-three matrix

\[
A=S+\Omega,
\]

with `S` symmetric and `Omega` skew with axial vector `omega/2`, direct algebra gives

\[
\boxed{
\operatorname{tr}(A^3)
=\operatorname{tr}(S^3)
+\frac34\,\omega\cdot S\omega.
}
\]

Since `tr S=0`,

\[
\operatorname{tr}(S^3)=3\det S,
\]

and since `tr A=0`,

\[
\operatorname{tr}(A^3)=3\det A.
\]

But `A=grad u` is an actual periodic Jacobian.  Its determinant is a null
Lagrangian: by the Piola identity,

\[
\int_{\mathbb T^3}\det(\nabla u)\,dx=0.
\]

Therefore

\[
\boxed{
\int\omega\cdot S\omega\,dx
=-4\int\det S\,dx.
}
\]

This is the exact Betchov relation, but its role here is structural: vortex
stretching and cubic strain self-amplification are not independent global channels.
They are the antisymmetric/symmetric projections of the degree-three
null-Lagrangian compatibility of the **same velocity gradient**.

In material coordinates `K=G^{-1}E` is `G`-selfadjoint and is similar to the physical
strain `S`.  With

\[
b=(*_G\bar\beta)^{\sharp_G},
\]

the same identity is

\[
\boxed{
\int\langle b,Kb\rangle_G\,dV_G
=-4\int\det K\,dV_G.
}
\]

A lightweight symbolic algebra referee verifies

\[
\operatorname{tr}(A^3)-\operatorname{tr}(S^3)
-\frac34\omega\cdot S\omega=0
\]

and `tr(S^3)=3 det S` for a generic trace-free symmetric `S`.  The zero integral of
`det grad u` is the exact Piola/null-Lagrangian theorem, not a calibration.

**Classification: Exact null-Lagrangian/Betchov consequence.**

---

## 7. Enstrophy evolution can be written entirely in metric-tangent variables

The material strain endomorphism

\[
K=\frac12G^{-1}\partial_tG
\]

satisfies

\[
\mathcal E_\omega
=\int|K|_G^2\,dV_G.
\]

The Betchov identity converts the integrated vortex-stretching production into
`-4 int det K`, while the derivative Hodge--strain identity converts the viscous
term into metric-rate roughness.  Hence the exact total enstrophy law becomes

\[
\boxed{
\frac d{dt}\int|K|_G^2\,dV_G
=-4\int\det K\,dV_G
-2\nu\int|\nabla^GK|_G^2\,dV_G.
}
\]

Equivalently, because `partial_t G=2 G K`,

\[
\boxed{
\frac14\frac d{dt}\|\partial_tG\|_{L^2(G)}^2
=-4\int\det K\,dV_G
-\frac\nu2\|\nabla^G\partial_tG\|_{L^2(G)}^2.
}
\]

This is not a new estimate and does not close regularity.  It shows that the
usual integrated `stretching minus dissipation` balance is already a pure law of the
velocity of the flat volume-one metric path.

**Classification: Exact integrated material-metric reformulation.**

---

## 8. The three-dimensional minor ladder is one compatibility grammar

The previous sections are best read together, not as separate mechanisms.
For the actual incompressible gradient `A=grad u`:

1. **Degree one:**
   \[
   \operatorname{tr}A=0
   \]
   is incompressibility.
2. **Degree two:** the quadratic minor/null-Lagrangian compatibility gives
   \[
   -\Delta p=|S|^2-\tfrac12|\omega|^2,
   \qquad
   \int|S|^2=\tfrac12\int|\omega|^2.
   \]
3. **Degree three:** the determinant/Piola compatibility gives
   \[
   \int\omega\cdot S\omega=-4\int\det S.
   \]

These are not three independently selected balances.  They are the first three
invariant consequences available in dimension three from the fact that

\[
\boxed{
\nabla^G\bar\alpha
=E+\frac12\bar\beta
}
\]

is one trace-free **integrable gradient**, not a freely prescribed strain plus a
freely prescribed vorticity.

The Hodge--strain scaled isometry is the quadratic Hilbert-space face of this same
compatibility.  The pressure Poisson field is its local quadratic potential.  The
Betchov law is its cubic global face.

**Classification: Rigorous operator-level synthesis of exact identities.**

---

## 9. Pressure is the symmetric constraint sector hidden by the vorticity quotient

The one-form equation

\[
(\partial_t+\mathcal L_u-\nu\Delta)u^\flat=dB
\]

shows why pressure disappears after applying `d`: exterior differentiation quotients
out exact gradient forces.  But the full velocity gradient has both antisymmetric
and symmetric sectors.  The antisymmetric sector is `beta`; the symmetric sector is
metric velocity `E`.

The vorticity quotient therefore hides exactly the sector in which the pressure
Hessian acts.  The pressure Poisson identity of Section 5 shows that this hidden
sector is still determined by the same strain/vorticity gradient compatibility.
Pressure is not a new independent physical resource; it is the nonlocal constraint
potential required by incompressibility of the reconstructed velocity.

This is the precise correction to an over-literal reading of `pressure is gauge`:

\[
\boxed{
\text{pressure is gauge for closed circulation, but constraint geometry for strain.}
}
\]

**Classification: Rigorous structural consequence of exact NS identities.**

No claim is made here that the pressure Hessian by itself prevents blow-up.

---

## 10. The reduced self-generated system becomes still smaller

The preceding theorem allows the material system to be written as

\[
\boxed{
\partial_t\bar\beta=\nu\Delta_G\bar\beta,
\qquad
\partial_tG=2\mathfrak S_G\bar\beta,
}
\]

subject to

\[
\boxed{
d\bar\beta=0,
\quad
\operatorname{Rm}(G)=0,
\quad
\mathrm{vol}_G=\mathrm{vol}_0,
}
\]

where `mathfrak S_G` is not arbitrary: it is the Hodge--strain transform generated
by the unique co-closed velocity reconstruction modulo the fixed harmonic mode, and
it obeys

\[
\boxed{
\mathfrak S_G^*\mathfrak S_G=\frac12 I
}
\]

on the exact vorticity sector, in the `L^2(G)` pairing.

Moreover `E=mathfrak S_G beta` and `beta/2` must recombine into the actual covariant
gradient `nabla bar alpha`, hence obey the local integrability relation of Section 2
and the quadratic/cubic null-Lagrangian constraints of Sections 5--6.

So even the apparent two-object `(G,bar beta)` feedback is more rigid than the
previous master theorem stated: **the velocity of `G` is an exact Hodge-isometric
representation of `bar beta` constrained to the tangent space of the flat
volume-preserving metric orbit.**

**Classification: Exact/Rigorous reduction from smooth Navier--Stokes.**

---

## 11. The Bernoulli/pressure gauge is exactly motion of the Hodge projector

There is one further compression at the one-form level.  Let

\[
P_G:\Omega^1\to\ker\delta_G
\]

be the orthogonal Hodge projector onto co-closed one-forms, including the harmonic
sector.  The material velocity one-form satisfies

\[
P_G\bar\alpha=\bar\alpha.
\]

At each fixed metric, the Hodge Laplacian preserves the Hodge decomposition, so

\[
P_G\Delta_G\bar\alpha=\Delta_G\bar\alpha.
\]

The exact material momentum law is

\[
\partial_t\bar\alpha-\nu\Delta_G\bar\alpha=d\bar B,
\qquad
\bar B=\Phi_t^*\left(\frac{|u|^2}{2}-p\right).
\]

Because `d bar B` is exact, it lies in the orthogonal complement of the co-closed
range and therefore `P_G d bar B=0`.  Differentiate the identity
`P_G bar alpha=bar alpha`:

\[
\dot P_G\bar\alpha+P_G\partial_t\bar\alpha
=\partial_t\bar\alpha.
\]

Hence

\[
(I-P_G)\partial_t\bar\alpha
=\dot P_G\bar\alpha.
\]

But the momentum equation shows that the left-hand side is exactly `d bar B`.
Therefore

\[
\boxed{
d\bar B=\dot P_G\bar\alpha.
}
\]

Equivalently, the full material momentum equation is

\[
\boxed{
(\partial_t-\dot P_G)\bar\alpha
=\nu\Delta_G\bar\alpha,
\qquad
P_G\bar\alpha=\bar\alpha.
}
\]

This is an exact **moving-Hodge heat equation**.  At a frozen metric the heat
operator preserves the co-closed subspace; the only exact correction needed in the
real Navier--Stokes evolution is the connection term generated because the Hodge
subspace itself moves with the self-generated metric.

The differentiated-projector identity gives

\[
P_G\dot P_G P_G=0,
\]

so `dot P_G bar alpha` is pure range-to-complement exchange.  In the present Hodge
decomposition that complement is the exact one-form sector.  Thus the
Bernoulli/pressure force is not an additional internal producer: it is exactly the
off-diagonal connection required to keep the velocity one-form on the moving
co-closed constraint manifold.

Differentiating `delta_G bar alpha=0` gives the equivalent scalar constraint

\[
\boxed{
\delta_G d\bar B
=-(\partial_t\delta_G)\bar\alpha.
}
\]

So the Bernoulli potential is fixed, up to the usual additive constant, by the
variation of the codifferential itself.

**Classification: Exact moving-Hodge-projector identity.**

This supplies a literal PDE Hodge projector on the material momentum-one-form
bundle.  It should not be silently identified with any older programme-specific
chain/CK projector that had no line-by-line definition; the common projector tangent
algebra is exact, but the state spaces are different.

**Classification: Rigorous architecture typing.**

---

## 12. Pressure, stretching, and strain are three derivatives of one moving Hodge structure

The material Hodge--Bochner theorem already gave

\[
(\partial_t *_G)\bar\beta
=2\Phi_t^*[(S\omega)^\flat],
\]

so vortex stretching is the variation of the Hodge-star identification between
vorticity flux and the vorticity vector/one-form.  Section 11 now gives

\[
d\bar B=\dot P_G\bar\alpha,
\]

so the Bernoulli/pressure exact force is the variation of the co-closed Hodge
projector.  Finally

\[
\partial_tG=2\mathfrak S_G\bar\beta
\]

shows that the metric motion driving both Hodge variations is itself the
Hodge--strain representation of the same vorticity form.

Therefore the formerly distinct nonlinear faces

\[
\text{vortex stretching},
\qquad
\text{pressure constraint},
\qquad
\text{strain/metric deformation}
\]

are all functorial derivatives of **one self-generated moving Hodge geometry**.
Diffusion remains the Hodge heat operator, whose only product defect is the
Bochner/carre-du-champ Gram already identified in the previous master theorem.

This yields the shortest operator grammar presently visible:

\[
\boxed{
\text{Navier--Stokes in material coordinates}
=
\text{Hodge heat inside a Hodge geometry moved by the same heated state}.
}
\]

More explicitly,

\[
\boxed{
\begin{aligned}
&P_G\bar\alpha=\bar\alpha,\\
&(\partial_t-\dot P_G)\bar\alpha=\nu\Delta_G\bar\alpha,\\
&\partial_tG=\mathcal L_{\bar\alpha^{\sharp_G}}G,\\
&\bar\beta=d\bar\alpha,
\qquad
\partial_t\bar\beta=\nu\Delta_G\bar\beta,\\
&\operatorname{Rm}(G)=0,
\qquad
\mathrm{vol}_G=\mathrm{vol}_0.
\end{aligned}
}
\]

The pressure/Bernoulli connection disappears after `d` because `d^2=0`; stretching
appears when the evolving Hodge star is used to read the same two-form as a vector;
metric strain appears when the same one-form is read through the symmetric-gradient
functor.  None is an independently prescribed mechanism.

**Classification: Rigorous operator-level synthesis of exact identities.**

---

## 13. Frozen-geometry intertwining isolates where the nonlinearity lives

For a fixed flat metric `G`, the Hodge--strain transform and the Laplacian
intertwine:

\[
\boxed{
\mathfrak S_G\Delta_G^{(2)}\beta
=
\Delta_G^{\nabla}\mathfrak S_G\beta,
}
\]

where `Delta_G^(2)` is the Hodge Laplacian on two-forms and
`Delta_G^nabla` is the induced component/connection Laplacian on symmetric
covariant two-tensors.  Flatness removes a curvature Weitzenbock remainder.

Along the actual self-generated metric path, `E=mathfrak S_G bar beta` and
`partial_t bar beta=nu Delta_G bar beta`, so

\[
\boxed{
(\partial_t-\nu\Delta_G^{\nabla})E
=(\partial_t\mathfrak S_G)\bar\beta.
}
\]

Thus if the Hodge geometry were frozen, the compatible strain representation would
heat with exactly the same generator as vorticity.  The entire nonlinear symmetric
feedback is the time variation of the Hodge--strain transform itself.

In physical Euclidean coordinates the exact strain equation is

\[
D_tS+S^2+\Omega^2+\nabla^2p=\nu\Delta S.
\]

Pulling the covariant strain tensor back by `Phi_t` identifies the abstract operator
variation above with

\[
\boxed{
(\partial_t\mathfrak S_G)\bar\beta
=
\Phi_t^*\!\left[
S^2-\Omega^2+[S,\Omega]-\nabla^2p
\right]^{\flat\flat}.
}
\]

Here `[S,Omega]=S Omega-Omega S` is symmetric.  Consequently strain
self-interaction, rotation coupling, and the pressure Hessian are not separate
sources below the master material description: together they are the coordinate
expression of the single commutator produced by changing the Hodge--strain
reconstruction while the state evolves.

**Classification: Exact strain equation / rigorous identification with the moving
Hodge--strain commutator.**

This does not assert a favorable sign or a regularity estimate for that commutator.

---

## 14. New no-escape frontier

A hypothetical singular escape still corresponds to

\[
\sup_a|\bar\beta|_G\to\infty,
\]

but the candidate escape geometry must now satisfy simultaneously:

\[
\boxed{
\begin{gathered}
\partial_t\bar\beta=\nu\Delta_G\bar\beta,\\
\partial_tG=2\mathfrak S_G\bar\beta,\\
\nabla^G\bar\alpha=\mathfrak S_G\bar\beta+\frac12\bar\beta,\\
\operatorname{tr}_G\mathfrak S_G\bar\beta=0,\\
\nabla_k(\nabla_i\bar\alpha_j)-\nabla_i(\nabla_k\bar\alpha_j)=0,\\
\operatorname{Rm}(G)=0,
\qquad
\mathrm{vol}_G=\mathrm{vol}_0,
\end{gathered}
}
\]

plus the exact quadratic and cubic null-Lagrangian compatibility forced by the same
gradient.

The next research question is therefore **not** to invent a scalar combining
stretching, pressure, and diffusion.  It is:

\[
\boxed{
\begin{gathered}
\text{Does parabolic evolution of the antisymmetric face of an incompressible}\\
\text{integrable gradient remain compatible with an escaping symmetric metric face?}
\end{gathered}
}
\]

Equivalently: can a flat volume-one metric path whose velocity is the Hodge-strain
mate of the exact form it is simultaneously diffusing develop an escape geometry
without violating the gradient/minor compatibility above?

That is the smallest literal no-escape target currently visible.  Its sufficiency
for blow-up exclusion is **Conjectural/Open**.  No continuation or regularity claim
is made.
