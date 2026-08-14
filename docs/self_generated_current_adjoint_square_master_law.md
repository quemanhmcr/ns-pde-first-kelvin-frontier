# Self-generated current adjoint-square master law

## Purpose

The preceding material--vortex curvature theorem compressed many Navier--Stokes
mechanisms to the literal vorticity current

\[
\mathcal J_{\rm NS}=\iota_u\beta+\nu\delta\beta,
\qquad
\beta=d\alpha,
\qquad
\alpha=u^\flat.
\]

This note asks whether even `beta` and `J_NS` must remain primitive objects.  They do
not.  For positive viscosity, define the degree-raising operator forced by the
velocity one-form and the exterior derivative

\[
\boxed{
\mathcal R_\alpha:=\nu d+\alpha\wedge.
}
\]

Its `L^2` adjoint on the flat periodic domain is

\[
\boxed{
\mathcal C_\alpha:=\mathcal R_\alpha^*
=\nu\delta+\iota_u.
}
\]

The lowering operator is not postulated: it is exactly the literal NS current map,

\[
\boxed{
\mathcal C_\alpha\beta=\mathcal J_{\rm NS}.
}
\]

The pair has two exact state-generated square laws:

\[
\boxed{
\mathcal R_\alpha^2
=\nu\,\beta\wedge,
\qquad
\mathcal C_\alpha^2
=\nu\,\iota_{\beta^\sharp}.
}
\]

Thus vorticity is not merely an output of `curl`.  It is the exact failure of the
literal raising/lowering current operators to be nilpotent.  At Euler viscosity zero
the lowering operator becomes pure self-contraction `i_u` and squares to zero; at
positive viscosity its square is forced to be contraction by the actual vorticity
state.

More importantly, because `alpha wedge alpha=0`,

\[
\mathcal R_\alpha\alpha=\nu\beta.
\]

Therefore

\[
\frac1\nu
\mathcal R_\alpha^*\mathcal R_\alpha\alpha
=\mathcal J_{\rm NS},
\]

and the complete momentum equation is exactly

\[
\boxed{
\partial_t\alpha
+\frac1\nu
\mathcal R_\alpha^*\mathcal R_\alpha\alpha
=d\varphi,
\qquad
\delta\alpha=0,
}
\]

where

\[
\varphi=B-\alpha(u)
=-\left(p+\frac{|u|^2}{2}\right).
\]

After Hodge projection,

\[
\boxed{
\partial_t\alpha
=-\frac1\nu
P_\sigma\mathcal R_\alpha^*\mathcal R_\alpha\alpha.
}
\]

This is a whole-PDE identity, not a model.  The same operator that raises the current
state into its vorticity curvature is adjointed back to produce the exact physical
current which moves the state.

The positive frozen square does **not** imply that all stronger norms decrease.  The
operator itself depends on `alpha`; its state dependence contains the Euler Lamb
rotation.  Smooth divergence-free finite Fourier data can have positive instantaneous
enstrophy production after amplitude scaling.  Hence this theorem is a compression
of the literal mechanism, not a regularity proof.

---

## 1. The raising and lowering operators are forced by the literal current

Fix the flat periodic Hodge structure and positive viscosity `nu>0`.  Define

\[
\mathcal R_\alpha=\nu d+\alpha\wedge.
\]

For differential forms `eta,zeta`, periodic adjointness gives

\[
\langle d\eta,\zeta\rangle
=\langle\eta,\delta\zeta\rangle,
\]

while wedge by the velocity one-form has adjoint contraction by the velocity vector:

\[
\langle\alpha\wedge\eta,\zeta\rangle
=\langle\eta,\iota_u\zeta\rangle.
\]

Hence

\[
\boxed{
\mathcal R_\alpha^*
=\nu\delta+\iota_u
=: \mathcal C_\alpha.
}
\]

Applied to the actual exact vorticity two-form,

\[
\boxed{
\mathcal C_\alpha\beta
=\iota_u\beta+\nu\delta\beta
=\mathcal J_{\rm NS}.
}
\]

No current variable has been added.  `C_alpha` is simply the adjoint form of the two
operations already appearing in the literal current.

**Classification: Exact Hodge-adjoint identity.**

---

## 2. Vorticity is the square curvature of the raising operator

For any smooth form `eta`,

\[
\begin{aligned}
\mathcal R_\alpha^2\eta
&=(\nu d+\alpha\wedge)
  (\nu d\eta+\alpha\wedge\eta)\\
&=\nu d\alpha\wedge\eta,
\end{aligned}
\]

because `d^2=0`, `alpha wedge alpha=0`, and the two terms containing
`alpha wedge d eta` cancel by the graded Leibniz rule.  Since

\[
\beta=d\alpha,
\]

one has the whole exterior-algebra identity

\[
\boxed{
\mathcal R_\alpha^2
=\nu\,\beta\wedge.
}
\]

This statement is local and contains no spectral decomposition or norm.

In particular, for every scalar `f`,

\[
\boxed{
\mathcal R_\alpha^2 f
=\nu f\beta.
}
\]

All derivatives of `f` cancel.  The square of the first-order operator is a zero-order
curvature multiplication forced by the actual vorticity.

**Classification: Exact whole-form operator identity.**

---

## 3. The adjoint current operator squares to vorticity contraction

Taking the adjoint of the preceding identity yields

\[
\boxed{
\mathcal C_\alpha^2
=\nu\,\iota_{\beta^\sharp},
}
\]

where the bivector contraction convention is chosen so that, in an orthonormal
frame,

\[
\iota_{\beta^\sharp}\beta=|\beta|^2.
\]

Equivalently, the identity can be derived directly from

\[
\delta=-\sum_j\iota_{e_j}\partial_j.
\]

The derivative terms cancel because contractions anticommute, leaving

\[
\boxed{
\{\delta,\iota_u\}
=\iota_{(d\alpha)^\sharp}
=\iota_{\beta^\sharp}.
}
\]

Since `i_u^2=0` and `delta^2=0`, this is exactly the square formula above.

At `nu=0`, the literal lowering operation is just `i_u` and is nilpotent.  Positive
viscosity deforms that nilpotency by precisely the actual vorticity state:

\[
\boxed{
\mathcal C_\alpha^2=\nu\iota_{\beta^\sharp}.
}
\]

Nothing independent has been introduced to measure the failure.

**Classification: Exact whole-form anticommutator / square identity.**

---

## 4. The vorticity current descends to positive enstrophy pointwise

Apply the lowering square to the actual vorticity form:

\[
\mathcal C_\alpha\beta
=\mathcal J_{\rm NS}.
\]

A second application gives

\[
\boxed{
\mathcal C_\alpha\mathcal J_{\rm NS}
=\mathcal C_\alpha^2\beta
=\nu|\beta|^2
=\nu|\omega|^2.
}
\]

Thus the literal current has the finite descent

\[
\boxed{
\beta
\xrightarrow{\ \mathcal C_\alpha\ }
\mathcal J_{\rm NS}
\xrightarrow{\ \mathcal C_\alpha\ }
\nu|\omega|^2
\xrightarrow{\ \mathcal C_\alpha\ }
0.
}
\]

The positivity at the second descent is not imposed by a norm estimate.  It is the
pointwise square curvature of the same current-lowering operator.

For an arbitrary scalar cutoff `f`, the whole-operator identity gives the localized
version

\[
\boxed{
\mathcal C_\alpha^2(f\beta)
=\nu f|\omega|^2.
}
\]

Again, all cutoff derivatives cancel inside the operator square.

**Classification: Exact pointwise positive current-square identity.**

---

## 5. The dual raising chain generates velocity, vorticity and helicity

Start from the constant scalar `1`.  Since `d1=0`,

\[
\boxed{
\mathcal R_\alpha 1=\alpha.
}
\]

Apply the same operator again:

\[
\boxed{
\mathcal R_\alpha^2 1
=\nu\beta.
}
\]

Because `d beta=0`,

\[
\boxed{
\mathcal R_\alpha^3 1
=\nu\alpha\wedge\beta.
}
\]

In three spatial dimensions there is no next degree, and directly

\[
\boxed{
\mathcal R_\alpha^4 1=0.
}
\]

The three nontrivial outputs are the velocity one-form, viscous multiple of the
vorticity two-form, and viscous multiple of the local helicity three-form.

The adjoint chain from the volume form is

\[
\boxed{
\begin{aligned}
\mathcal C_\alpha\operatorname{vol}
&=\iota_u\operatorname{vol}=*\alpha,\\
\mathcal C_\alpha^2\operatorname{vol}
&=\nu\omega^\flat,\\
\mathcal C_\alpha^3\operatorname{vol}
&=\nu\,u\cdot\omega,\\
\mathcal C_\alpha^4\operatorname{vol}
&=0.
\end{aligned}
}
\]

The last scalar formula uses `div omega=0`, so `delta omega^flat=0`.

These chains do not define new conserved quantities.  They show that velocity,
vorticity and helicity are consecutive degree faces of the same state-generated
adjoint pair.

**Classification: Exact three-dimensional descent identities.**

---

## 6. The complete momentum equation is one self-generated adjoint square

Because

\[
\alpha\wedge\alpha=0,
\]

one has

\[
\boxed{
\mathcal R_\alpha\alpha
=\nu d\alpha
=\nu\beta.
}
\]

Apply the adjoint:

\[
\boxed{
\mathcal R_\alpha^*\mathcal R_\alpha\alpha
=\nu\mathcal C_\alpha\beta
=\nu\mathcal J_{\rm NS}.
}
\]

The one-form momentum equation was already

\[
\partial_t\alpha+\mathcal J_{\rm NS}=d\varphi,
\qquad
\varphi=B-\alpha(u).
\]

Therefore

\[
\boxed{
\partial_t\alpha
+\frac1\nu
\mathcal R_\alpha^*\mathcal R_\alpha\alpha
=d\varphi,
\qquad
\delta\alpha=0.
}
\]

Applying the Hodge projector onto co-closed one-forms gives

\[
\boxed{
\partial_t\alpha
=-\frac1\nu
P_\sigma\mathcal R_\alpha^*\mathcal R_\alpha\alpha.
}
\]

Thus the complete projected incompressible Navier--Stokes equation is the closed
feedback cycle

\[
\boxed{
\alpha
\xrightarrow{\ \mathcal R_\alpha\ }
\nu\beta
\xrightarrow{\ \mathcal R_\alpha^*\ }
\nu\mathcal J_{\rm NS}
\xrightarrow{\ -P_\sigma/\nu\ }
\partial_t\alpha.
}
\]

This is exact for `nu>0`.  The displayed factorization is singular as a representation
at `nu=0`; it should not be used as an inviscid limiting formula.

**Classification: Exact whole-PDE factorization.**

---

## 7. Energy loss is the norm square of the same raising step

On the co-closed state,

\[
\begin{aligned}
\frac12\frac d{dt}\|\alpha\|_2^2
&=-\frac1\nu
\langle\alpha,
P_\sigma\mathcal R_\alpha^*\mathcal R_\alpha\alpha\rangle\\
&=-\frac1\nu
\|\mathcal R_\alpha\alpha\|_2^2.
\end{aligned}
\]

Since `R_alpha alpha=nu beta`,

\[
\boxed{
\dot E
=-\nu\|\beta\|_2^2
=-\nu\|\omega\|_2^2.
}
\]

Equivalently, Section 4 gives the pointwise current-square density whose spatial
integral is the same energy loss:

\[
\boxed{
-\dot E
=\int_{\mathbb T^3}
\mathcal C_\alpha^2\beta\,dx.
}
\]

Hence the usual finite energy reservoir is literally the spacetime mass of the
second lowering descent of the physical current.

**Classification: Exact energy identity / exact current-square interpretation.**

---

## 8. Frozen mobility is positive, but the flow is not a fixed linear gradient system

Define, only as shorthand for the already factorized operator on the co-closed
subspace,

\[
\mathcal M_\alpha
:=\frac1\nu
P_\sigma\mathcal R_\alpha^*\mathcal R_\alpha P_\sigma.
\]

For every smooth one-form `v`,

\[
\boxed{
\langle v,\mathcal M_\alpha v\rangle
=\frac1\nu\|\mathcal R_\alpha P_\sigma v\|_2^2
\ge0.
}
\]

The NS equation is

\[
\alpha_t=-\mathcal M_\alpha\alpha.
\]

This positivity explains the kinetic-energy law, but it must not be misread.  The
operator `M_alpha` depends on the state `alpha`.  Its variation contains the full
Euler Lamb rotation.  In particular,

\[
\frac1{2\nu}\|\mathcal R_\alpha\alpha\|_2^2
=\frac\nu2\|d\alpha\|_2^2
\]

has ordinary `L^2` gradient only `nu delta beta`; varying this scalar square does not
produce the Euler term `i_u beta`.

So the factorization is an exact state-dependent positive mobility of kinetic energy,
not an assertion that NS is the ordinary fixed-metric gradient flow of enstrophy.

**Classification: Exact positivity; rigorous anti-overclaim.**

---

## 9. The same adjoint pair contains strain as its symmetric cross term

Expand the two positive operator squares:

\[
\mathcal R_\alpha^*\mathcal R_\alpha
+\mathcal R_\alpha\mathcal R_\alpha^*.
\]

Using

\[
\{d,\iota_u\}=\mathcal L_u,
\qquad
\{\delta,\alpha\wedge\}=\mathcal L_u^*,
\]

and

\[
\{\alpha\wedge,\iota_u\}=|u|^2,
\]

one obtains the whole-form identity

\[
\boxed{
\mathcal R_\alpha^*\mathcal R_\alpha
+\mathcal R_\alpha\mathcal R_\alpha^*
=\nu^2\Delta_H
+|u|^2
+\nu(\mathcal L_u+\mathcal L_u^*).
}
\]

Thus the symmetric deformation operator is not an independent primitive below the
current algebra.  It is the symmetric cross term of the same raising/lowering pair.

For incompressible flow on the flat torus:

- on one-forms, under vector identification,
  `L_u+L_u^*=2S`;
- on two-forms, under Hodge dual vector identification,
  `L_u+L_u^*=-2S`.

Since the left side is a sum of positive squares, both form degrees carry exact
operator positivity constraints generated by the same state.

**Classification: Exact whole-form adjoint-square identity.**

---

## 10. Vortex stretching is an interference face of the actual current

Apply Section 9 to the actual closed vorticity two-form.  Since

\[
\mathcal R_\alpha\beta
=\alpha\wedge\beta,
\qquad
\mathcal R_\alpha^*\beta
=\mathcal J_{\rm NS},
\]

one has

\[
\begin{aligned}
\|\alpha\wedge\beta\|_2^2
+\|\mathcal J_{\rm NS}\|_2^2
&=\nu^2\|\delta\beta\|_2^2
+\int |u|^2|\omega|^2\\
&\quad-2\nu\int\omega\cdot S\omega.
\end{aligned}
\]

Using

\[
|u|^2|\omega|^2
=|u\cdot\omega|^2+|u\times\omega|^2
\]

and `alpha wedge beta=(u dot omega) vol`, the helicity-density square cancels.  Hence

\[
\boxed{
2\nu\int\omega\cdot S\omega
=\nu^2\|\operatorname{curl}\omega\|_2^2
+\|u\times\omega\|_2^2
-\|\mathcal J_{\rm NS}\|_2^2.
}
\]

This is equivalently the polarization identity for the two literal legs

\[
\mathcal J_{\rm NS}^\sharp
=-u\times\omega
+\nu\operatorname{curl}\omega.
\]

Thus stretching is not a third producer.  It is the interference face between the
separate alternating/Hodge-adjoint legs and their actual combined current.

**Classification: Exact integrated current-square identity.**

---

## 11. Local kinetic energy and pressure are the two pieces of the second current descent

Section 4 gives

\[
\mathcal C_\alpha\mathcal J_{\rm NS}
=\iota_u\mathcal J_{\rm NS}
+\nu\delta\mathcal J_{\rm NS}
=\nu|\omega|^2.
\]

The two terms are individually forced.  In vector notation,

\[
\boxed{
\iota_u\mathcal J_{\rm NS}
=\nu\,u\cdot\operatorname{curl}\omega,
}
\]

and

\[
\boxed{
\delta\mathcal J_{\rm NS}
=|\omega|^2-u\cdot\operatorname{curl}\omega.
}
\]

But momentum gives

\[
\mathcal J_{\rm NS}
=-\alpha_t+d\varphi.
\]

Contracting with `u` therefore yields

\[
\boxed{
-\partial_t\frac{|u|^2}{2}
+u\cdot\nabla\varphi
=\nu u\cdot\operatorname{curl}\omega,
}
\]

which is the local kinetic-energy equation in Lamb/Hodge form.

Applying `delta` instead gives

\[
\boxed{
\Delta_H\varphi
=|\omega|^2-u\cdot\operatorname{curl}\omega.
}
\]

With

\[
\varphi=-\left(p+\frac{|u|^2}{2}\right),
\]

this is exactly the usual pressure/Bernoulli Poisson constraint after standard vector
identities.

Hence local energy and pressure are not separate primitive equations here.  They are
the contraction and codifferential components of the same positive second descent
`C_alpha J_NS=nu|omega|^2`.

**Classification: Exact local current-square projections.**

---

## 12. The current equation is a commutator consequence of the same algebra

The raising/lowering pair also gives

\[
\boxed{
\{d,\mathcal C_\alpha\}
=\mathcal L_u+\nu\Delta_H.
}
\]

Define the literal parabolic form operator

\[
\mathscr H_u
:=\partial_t+\mathcal L_u+\nu\Delta_H
=\partial_t+\{d,\mathcal C_\alpha\}.
\]

The vorticity equation is simply

\[
\mathscr H_u\beta=0.
\]

Because

\[
\partial_t\mathcal C_\alpha=\iota_{u_t}
\]

and

\[
\mathcal C_\alpha^2=\nu\iota_{\beta^\sharp},
\]

operator algebra gives

\[
\boxed{
[\mathscr H_u,\mathcal C_\alpha]
=\iota_{u_t}
+\nu[d,\iota_{\beta^\sharp}].
}
\]

Apply this to `beta`.  Since `d beta=0`,

\[
\boxed{
\mathscr H_u\mathcal J_{\rm NS}
=\iota_{u_t}\beta
+\nu d|\omega|^2.
}
\]

Projected momentum says

\[
u_t^\flat=-P_\sigma\mathcal J_{\rm NS},
\]

so equivalently

\[
\boxed{
\mathscr H_u\mathcal J_{\rm NS}
+\iota_{(P_\sigma\mathcal J_{\rm NS})^\sharp}\beta
=\nu d|\omega|^2.
}
\]

Thus the current does not require an independent evolution law.  Its equation is a
commutator consequence of the same two operator identities that evolve `beta`.

**Classification: Exact current-evolution consequence.**

---

## 13. No-go: positive frozen square does not prevent instantaneous higher-norm growth

The factorized equation

\[
\alpha_t
=-\nu^{-1}P_\sigma
\mathcal R_\alpha^*\mathcal R_\alpha\alpha
\]

has a positive frozen mobility, but this does not force enstrophy or other stronger
Hodge quantities to decrease.

The reason is structural.  Under amplitude scaling

\[
u\mapsto a u,
\]

the nonlinear stretching contribution to enstrophy scales like `a^3`, while the
viscous enstrophy loss scales like `a^2`.  Any smooth periodic divergence-free datum
with positive nonzero integrated stretching therefore has positive initial enstrophy
rate after sufficiently large amplitude scaling.

A finite Fourier referee on the torus gives one such smooth datum.  In the convention
`u(x)=sum_k u_k exp(i k dot x)` with `u_-k=conj(u_k)`, its nonzero positive-mode
coefficients are

\[
\begin{array}{c|c}
k&u_k\\ \hline
(1,0,0)&(0,\,2-i,\,2i)\\
(0,1,0)&(1+2i,\,0,\,-2+i)\\
(1,1,0)&((1+3i)/2,\,-(1+3i)/2,\,1+2i)\\
(1,0,1)&(3/2+i,\,1-i,\,-3/2-i)\\
(0,1,1)&(2+i,\,-1/2-2i,\,1/2+2i)\\
(1,1,1)&(-1-2i/3,\,-1-2i/3,\,2+4i/3).
\end{array}
\]

Each coefficient is exactly transverse to its wavevector.  Exact rational convolution
gives the normalized values

\[
\int\omega\cdot S\omega
=\frac{310}{3},
\qquad
\int|\nabla\omega|^2=450.
\]

At `nu=1`, amplitudes

\[
a>\frac{450}{310/3}
=\frac{135}{31}
\]

therefore give positive instantaneous enstrophy growth.  This is an algebra referee;
the no-go itself only needs the cubic/quadratic scaling and one nonzero-stretching
smooth datum.

Hence the adjoint-square representation must not be advertised as a monotonicity
theorem for all Hodge levels.

**Classification: Rigorous amplitude-scaling no-go; audited finite Fourier witness.**

---

## 14. What has actually been removed from the primitive list

Below this theorem the following are derived faces rather than independent
mechanisms:

- vorticity: the square curvature `R_alpha^2=nu beta wedge` and the first raising
  descent of `alpha`;
- the literal NS current: `C_alpha beta` or equivalently
  `R_alpha^* R_alpha alpha / nu`;
- positive enstrophy density: the second lowering descent
  `C_alpha^2 beta / nu`;
- helicity density: the third raising descent of `1`;
- kinetic-energy dissipation: the norm square of `R_alpha alpha`;
- pressure/Bernoulli Poisson and local kinetic energy: the two components of
  `C_alpha J_NS=nu|omega|^2`;
- strain/stretching: the symmetric cross term and current interference face of the
  same adjoint pair;
- the current evolution equation: the commutator of the same lowering operator with
  the literal parabolic form operator.

The complete positive-viscosity velocity equation is therefore generated by one
state and one state-generated adjoint pair:

\[
\boxed{
\begin{gathered}
\alpha=u^\flat,
\qquad
\mathcal R_\alpha=\nu d+\alpha\wedge,
\qquad
\mathcal R_\alpha^*=\nu\delta+\iota_u,\\
\mathcal R_\alpha^2=\nu(d\alpha)\wedge,
\qquad
(\mathcal R_\alpha^*)^2=\nu\iota_{(d\alpha)^\sharp},\\
\partial_t\alpha
=-\frac1\nu P_\sigma
\mathcal R_\alpha^*\mathcal R_\alpha\alpha.
\end{gathered}
}
\]

Everything in this box is forced by the original one-form NS equation, exterior
calculus and the fixed Hodge adjoint.

**Classification: Rigorous synthesis of exact identities.**

---

## 15. No-escape frontier after the adjoint-square compression

This theorem exposes a smaller self-generated loop than the previous
Poisson/ray/heat descriptions:

\[
\boxed{
\alpha
\longrightarrow
\mathcal R_\alpha
\longrightarrow
\mathcal R_\alpha^2=\nu\beta\wedge
\longrightarrow
\mathcal R_\alpha^*\mathcal R_\alpha\alpha
\longrightarrow
\alpha_t.
}
\]

The state creates the operator; the operator creates the vorticity curvature; the
adjoint reads that curvature as the literal NS current; that current moves the state
which creates the next operator.

The unresolved question is no longer whether Euler transfer can be bounded by a
separate viscous term.  They are already inside one adjoint-square feedback.

The actual no-escape question becomes:

\[
\boxed{
\begin{gathered}
\text{Can the curvature }d\alpha\text{ of this self-generated first-order operator}\\
\text{concentrate to a finite-time singular escape while the same operator adjoint}\\
\text{feeds that curvature back into }\alpha_t\text{ and its second lowering descent}\\
\text{is the positive energy-drain density }\nu|d\alpha|^2?
\end{gathered}
}
\]

A proof would have to use the **self-generated adjoint-square compatibility**, not
merely the positivity of one frozen square.  High-frequency Beltrami heat modes and
the amplitude-scaling no-go show that raw curvature size and snapshot higher-norm
monotonicity are insufficient.

No curvature nonconcentration theorem is proved here.

**Classification: Open.**

---

## 16. Classification summary

### Exact

- `R_alpha=nu d+alpha wedge`, `C_alpha=R_alpha^*=nu delta+i_u`;
- whole-form square laws
  `R_alpha^2=nu beta wedge` and `C_alpha^2=nu i_(beta sharp)`;
- anticommutator `delta i_u+i_u delta=i_(beta sharp)`;
- raising chain `1 -> alpha -> nu beta -> nu alpha wedge beta -> 0`;
- lowering chains `beta -> J_NS -> nu|omega|^2 ->0` and the volume-form adjoint
  chain;
- complete momentum factorization
  `alpha_t+R_alpha^*R_alpha alpha/nu=d varphi` and its projected version;
- kinetic-energy square law;
- positive frozen mobility form;
- whole-form symmetric adjoint-square identity;
- current-square local energy and pressure projections;
- current evolution as an operator-commutator consequence.

### Rigorous consequences

- vorticity is the exact square curvature of the state-generated raising operator;
- the literal NS current is the adjoint feedback of that same curvature;
- pressure, local energy, enstrophy, helicity and stretching are lower-degree or
  bilinear faces of the same adjoint pair rather than primitive mechanisms;
- the entire positive-viscosity projected velocity equation is one self-generated
  adjoint-square feedback law.

### Audited no-go

- exact periodic heat shear verifies the factorized momentum equation;
- generic polynomial differential-form referees verify the whole-form square laws;
- smooth finite Fourier data plus amplitude scaling show that positive frozen
  mobility does not imply monotonicity of enstrophy;
- high-frequency Beltrami heat modes from the preceding theorem remain a no-go
  against interpreting raw curvature/current-square size as badness.

### Open

- a curvature/current anti-concentration theorem using the self-generated
  adjoint-square feedback itself;
- exclusion of finite-time escape;
- continuation, restart, blow-up exclusion and global regularity.
