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

## 5. Same-clock backward-drift matching (distinct from reversing a future bank)

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

This is not yet a proof that the state identification is correct.  More
importantly, it is a **same-clock** statement: it compares the backward drift of the
ancestry diffusion with the physical backward-Itô drift while retaining the same
clock orientation.  It is not the coefficient condition for converting the
repository's future conditional bank into a physical past-payoff bank.  That latter
operation reverses the future-bank clock and uses `b_+`; see
`docs/two_clock_kelvin_quantile_audit.md`.

**Classification: Exact same-clock algebra conditional on the physical state
identification.**

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

## 8. Consequence for the future-covariance bank: reverse the bank clock explicitly

The normalized diffusion time-reversal algebra remains exact:

\[
(b_+,b_-,j),
\qquad
j=\frac{b_++b_-}{2}.
\]

But a second operation must be kept distinct.  A future bank with ancestry clock
`s` and terminal `Theta` becomes a causal physical past-payoff bank by introducing
reverse age

\[
\boxed{\sigma=\Theta-s.}
\]

If

\[
(\partial_s+b_+\cdot\nabla+\nu K:\nabla^2)m=0,
\]

then

\[
\boxed{
(\partial_\sigma-b_+\cdot\nabla-\nu K:\nabla^2)\widehat m=0.
}
\]

Hence an identity-map flat anchor bridge to the physical backward-Kelvin operator
requires

\[
\boxed{b_+=-u,}
\]

not `b_-=u`.  The latter remains the distinct same-clock matching condition of
Section 5.  Demanding both identity-map interpretations against the same physical
drift forces `b_++b_-=2j=0`.

For a general clock-reversed state map `Pi(sigma,y)`, the exact equations are

\[
\boxed{K_K=D\Pi K D\Pi^T,}
\]

and

\[
\boxed{
B_K
=\partial_\sigma\Pi-D\Pi b_+-\nu(K:D^2\Pi).
}
\]

These are the equations relevant to the **future covariance bank**.  They are not
the same-clock `b_-` pushforward equations.

**Classification: Exact clock-reversal/state-map equations; programme-specific
future-bank state intertwining remains open-literal.**

---

## 9. Updated causal frontier

The causal bridge now has three typed arrows rather than one:

\[
\boxed{
\begin{aligned}
&\text{normalized ancestry diffusion}
\xrightarrow{\text{exact split}}
(b_+,b_-,j),\\
&\text{future bank}
\xrightarrow{\sigma=\Theta-s}
\text{reverse-age bank using }-b_+,\\
&\text{reverse-age ancestry state}
\xrightarrow{\text{open intertwining}}
\text{physical reverse-age Kelvin state}.
\end{aligned}
}
\]

The first two arrows are audited.  The third is the living state-semantics seam.
The full physical Kelvin side independently has

\[
\mathscr L_{\rm K,rev}^{(t)}(\sigma)
=-\mathscr K^-_{t-\sigma},
\]

so its causal clock is no longer ambiguous.

The same audit also shows that fixed-mass quantile motion is governed by
probability-current velocity, not by `b_+`, `b_-`, or `u` alone.  The remaining
first-bad cut problem is to define the actual scalar germ observable/threshold and
its outer physical-time lift.

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

## 10. A deterministic state map, when applicable, obeys an explicit backward-Itô system

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


---

## 11. `f`, `phi`, and `w` are reference-gauge data, not three physical coordinates

The decomposition

\[
q=f\phi
\]

has an exact reference gauge.  For any scalar `g`, define

\[
\boxed{
\phi'=e^g\phi,
\qquad
f'=e^{-g}f,
\qquad
w'=w-\nu K\nabla g.
}
\]

For symmetric `K`, direct substitution gives

\[
\boxed{
q'=q,
\qquad
j'=j,
\qquad
\mathscr L'=\mathscr L,
\qquad
b_+'=b_+,
\qquad
b_-'=b_-.
}
\]

Thus `phi`, `f`, and `w` separately are **reference representation data**.  They
must not be interpreted as independent physical hidden state variables.  The
state-map problem is defined by the underlying ancestry state manifold together
with the gauge-invariant diffusion data `(K,b_-)` and the Kelvin payoff.

The current repository uses a full ancestry kernel `P_{s,t}(y,dy')` but does not
supply a line-by-line construction of the state coordinate/manifold `y`.  This is a
literal definition seam, not an estimate.

**Classification: Exact reference-gauge identity; open-literal ancestry-state
manifold definition.**

---

## 12. Zero-q.v. Kelvin shape forces a degenerate ancestry noise sector

Factor the symmetric positive-semidefinite ancestry diffusion tensor as

\[
K=BB^T.
\]

For a proposed physical relative-shape coordinate `Pi_shape`, the pushed quadratic
variation is

\[
\boxed{
D\Pi_{\rm shape}K D\Pi_{\rm shape}^T
=
(D\Pi_{\rm shape}B)(D\Pi_{\rm shape}B)^T.
}
\]

Physical backward-Kelvin relative shape has zero q.v. after anchoring.  Therefore

\[
\boxed{D\Pi_{\rm shape}B=0.}
\]

So every physical shape coordinate must be constant along the ancestry noisy
distribution `Range(B)`.

If `K` is positive definite on an open connected ancestry state region, then `B` is
invertible and the condition forces

\[
D\Pi_{\rm shape}=0
\]

throughout that region.  Hence a nontrivial instantaneous finite-variation Kelvin
shape cannot be encoded as a smooth function of a purely full-rank diffusion state.
One needs either

1. deterministic/null directions of `K` carrying shape; or
2. a larger path/history state rather than a Markov function of the current
   full-rank diffusion coordinate.

This is a structural necessary condition for the state map, not a regularity
estimate.

**Classification: Exact diffusion-factorization identity and rigorous local no-go
for full-rank ancestry diffusion encoding nontrivial zero-q.v. shape.**


---

## 13. Deterministic `Pi` is only one branch of the state lift

A later full/reduced-state audit shows that the physical lift need not be a
deterministic map.  If ancestry state `y` is reduced, the general object is a
conditional kernel `kappa(y,dY_K)`.  The deterministic equations above remain exact
when `kappa` is Dirac, but a non-Dirac lift carries the separate resolution covariance
`Cov_kappa(m(Y_K))`.

**Classification: Rigorous structural correction; see
`docs/ancestry_resolution_kernel_audit.md`.**
