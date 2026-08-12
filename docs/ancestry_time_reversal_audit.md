# Normalized ancestry time reversal and the physical backward-Kelvin state seam

This note attacks the causal-identification seam without renaming variables by
analogy.  The normalized ancestry law already contains enough PDE structure to
derive its forward Itô drift, backward/time-reversed drift, and probability-current
velocity exactly.  The result separates a solved operator-level time-orientation
problem from the still-open state-identification problem.

No continuation or regularity claim is made.

---

## 1. Start from the actual normalized ancestry operator

The repository uses

\[
q=f\phi,
\qquad
j=w-\nu K\nabla\log f,
\]

and the dual operator

\[
\boxed{
\mathscr L\psi
=
w\cdot\nabla\psi
+
\nu\phi^{-1}\nabla\cdot(\phi K\nabla\psi),
}
\]

with symmetric diffusion tensor `K`.

Before assigning `w` a physical name, expand the divergence term.  Define

\[
\boxed{
(c_\phi)_j
=
\phi^{-1}\sum_i\partial_i(\phi K_{ij}).
}
\]

Then

\[
\mathscr L\psi
=
\boxed{b_+\cdot\nabla\psi}
+
\nu K:\nabla^2\psi,
\qquad
\boxed{b_+=w+\nu c_\phi.}
\]

Thus `w` itself is not the forward Itô drift when the reference geometry or `K`
varies.

**Classification: Exact operator expansion.**

---

## 2. The repository current is exactly the Fokker--Planck current

For diffusion matrix `a=2 nu K`, the forward probability current is

\[
J_j
=
q(b_+)_j
-
\nu\sum_i\partial_i(K_{ij}q).
\]

Substitute `q=f phi` and the formula for `b_+`.  The derivatives of `K` and `phi`
cancel exactly, leaving

\[
\boxed{
J
=
q\left(w-\nu K\nabla\log f\right)
=qj.
}
\]

So the stored vector `j` already has a precise physical meaning: it is the
probability-current velocity of the normalized ancestry diffusion.

**Classification: Exact Fokker--Planck identity.**

---

## 3. Exact time reversal

For the same diffusion and one-time density `q`, the backward/time-reversed Itô drift
is

\[
(b_-)_j
=
(b_+)_j
-
2\nu q^{-1}\sum_i\partial_i(K_{ij}q).
\]

Using `q=f phi` again gives

\[
\boxed{
 b_-
=
 w
-
\nu c_\phi
-
2\nu K\nabla\log f.
}
\]

Therefore

\[
\boxed{
\frac{b_++b_-}{2}
=
w-\nu K\nabla\log f
=j.
}
\]

The normalized ancestry current is the exact midpoint of the forward and backward
Itô drifts.

This is the weighted/generalized form of the familiar current/osmotic drift split;
no stochastic-mechanics interpretation is needed beyond the Fokker--Planck algebra.

**Classification: Exact time-reversal identity.**

---

## 4. Flat uniform sector

If

\[
K=I,
\qquad
\phi=1,
\]

then `c_phi=0` and the identities reduce to

\[
\boxed{
 b_+=w,
\qquad
 b_-=w-2\nu\nabla\log f,
\qquad
 j=w-\nu\nabla\log f.
}
\]

Thus even in the simplest sector, silently calling `w` the physical backward drift
is wrong unless the density correction vanishes or `w` has already been chosen to
include it.

**Classification: Exact specialization.**

---

## 5. What is required to match the physical backward Kelvin drift?

The physical backward stochastic Kelvin flow has backward Itô drift `u` in the
spatial anchor coordinate.  Suppose, as a proposed state identification, that the
ancestry backward drift is that same physical drift:

\[
\boxed{b_-=u.}
\]

Then the ancestry symbol `w` is not free.  Solving the exact formula above gives

\[
\boxed{
 w_{\rm required}
=
 u
+
\nu c_\phi
+
2\nu K\nabla\log f.
}
\]

With this choice, symbolic CI verifies

\[
\boxed{b_--u=0.}
\]

This is not yet a proof that the state identification is correct.  It is the exact
coefficient condition that any correct identification must satisfy.

**Classification: Exact algebra conditional on the physical state identification.**

---

## 6. Why `w=u` cannot be inserted silently

If one instead writes `w=u` by notation alone, then

\[
\boxed{
 b_--u
=
-\nu c_\phi
-2\nu K\nabla\log f.
}
\]

The discrepancy has a completely named physical origin:

- reference/diffusion geometry through `c_phi`;
- time-reversal/osmotic density drift through `K grad log f`.

It is not a mysterious pair source.  It is not `S^int`.

Only in a flat uniform constant-density sector does this mismatch vanish exactly.

**Classification: Rigorous consequence of the exact drift formulas.**

---

## 7. Relation to the backward-Kelvin current-shape audit

The current-shape audit independently gives a literal physical backward state

\[
Y_{\rm K}=(X,R(\cdot)),
\]

with common Brownian translation in `X` and finite-variation relative shape.

The ancestry law has its own state variables, density `q=f phi`, diffusion tensor
`K`, and drift data `w`.  At the operator level the forward/backward split is now
fully determined.  What is **not** yet written is a state map

\[
\boxed{
\Pi:Y_{\rm ancestry}\longrightarrow Y_{\rm K}
}
\]

such that the ancestry backward generator/pushforward becomes the physical
backward-Kelvin current-shape generator.

Because the physical common-noise shape state is degenerate in the shape directions
(zero shape q.v.), this state map is not a cosmetic renaming of a nondegenerate
finite-dimensional diffusion tensor.

**Classification: Open-literal state-identification bridge.**

---

## 8. Consequence for the future-covariance bank

The earlier phrase "forward-future versus backward-Kelvin time orientation" mixed
two issues.

The **time-reversal algebra of the normalized ancestry diffusion is now exact**:
`b_+`, `b_-`, and `j` are explicitly related.

What remains open is narrower:

> is the ancestry backward state/process that supports the future covariance bank
> literally the physical backward Kelvin current-shape process, after the correct
> state projection/reference-density identification?

If yes, the conditional future covariance and the physical backward martingale bank
can be placed on the same state with their causal orientations explicit.  If not,
the residual must be retained as a named state/projection current.

**Classification: Rigorous structural reduction; physical state identification
remains open.**

---

## 9. Updated causal frontier

The causal bridge is no longer one opaque step.  It is

\[
\boxed{
\text{normalized ancestry operator}
\xrightarrow{\text{exact time reversal}}
(b_+,b_-,j)
\xrightarrow{\text{open state map}}
\text{physical backward Kelvin state}.
}
\]

The first arrow is audited.  The second is the living seam.

The next PDE-first task should therefore inspect the actual ancestry state variables
`f, phi, K, w` and determine whether they are defined on the same anchor/current
state as the Kelvin representation.  One must not solve this by declaring `w=u`.

`S^int`, restart capacity, and continuation remain open.

No regularity conclusion.

---

## Primary representation context

The causal backward stochastic Kelvin orientation used for the physical side is the
Constantin--Iyer stochastic Lagrangian representation and its backward stochastic
formulation emphasized by Eyink.  In that formulation the stochastic flow is driven
by a spatially uniform Wiener motion and the backward Itô chain rule produces the
`-nu Delta` physical-time operator used in the preceding audits.


---

## 10. The open state map is an explicit backward-Itô system

Let `Y` denote ancestry coordinates and let

\[
\Pi(Y)=Y_{\rm K}=(X,R(\cdot))
\]

be a proposed map to the physical backward-Kelvin current-shape state.  The map is
not free.  Backward Itô calculus imposes two exact equations.

If the ancestry backward covariance is `2 nu K`, then the physical diffusion tensor
must be

\[
\boxed{
K_{\rm K}
=D\Pi\,K\,D\Pi^T.
}
\]

For the physical common-noise current-shape state, `K_K` has only the rank-three
anchor block; all relative-shape diffusion blocks are zero.

The backward drift must simultaneously satisfy

\[
\boxed{
B_{\rm K}
=D\Pi\,b_-
-\nu K:D^2\Pi.
}
\]

The minus sign in the Hessian correction is the same backward-Itô sign that produces
`-nu Delta` in the physical Kelvin generator.

Therefore an ancestry noise direction may be hidden only if `D Pi` kills it.  If a
noisy hidden coordinate is mixed into a physical relative-shape coordinate, the
pushed diffusion gives nonzero shape q.v. and cannot equal the uniform-common-noise
Kelvin state.

The audit contains both cases exactly:

- a projection that ignores a hidden noisy coordinate gives zero drift and diffusion
  residuals against the physical `(anchor, finite-variation shape)` target;
- a map that adds that noisy coordinate into shape produces a nonzero shape diffusion
  block and is rejected.

The remaining state-map problem is thus a concrete system of drift/diffusion
pushforward equations plus terminal-payoff compatibility, not an unspecified
identification.

**Classification: Exact backward-Itô state-map conditions and exact obstruction
witness.  Existence of the actual programme-specific map remains open-literal.**
