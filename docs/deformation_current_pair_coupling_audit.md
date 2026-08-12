# Stochastic Cauchy deformation -> physical Kelvin current/pair coupling audit

This note connects the causal reverse-age Cauchy deformation sector to the literal
physical-current/pair machinery without identifying objects that live in different
fibers.  The rule is: classify the physical action first, then derive its algebra.
No norm estimate, continuation theorem, or regularity conclusion is used.

## 1. The two factors are physically different

Let `P` be a current/selector map acting on chain or germ coefficients and let

\[
D_h
\]

be the reverse-age stochastic Cauchy deformation.  The corresponding forward
**tangent** deformation is

\[
\boxed{F_h=D_h^T.}
\]

These maps act on different factors:

- `P`: which physical chain/cycle coefficients are present;
- `D^T`: how the spatial tangent fiber is deformed.

Therefore the literal local current map is

\[
\boxed{T(P,D)=P\otimes D^T.}
\]

This tensor product is not a modeling convenience: it records that incidence and
spatial tangent geometry are different physical coordinates.

**Status: Exact identity / physical typing.**

## 2. Cauchy deformation cannot manufacture a physical boundary seam

If `B` is the physical chain boundary, its action on the spatial-fiber current is

\[
B_{\rm fib}=B\otimes I_3.
\]

Then

\[
\boxed{
(B\otimes I_3)(P\otimes D^T)=(BP)\otimes D^T.
}
\]

Hence if the selected Kelvin current is closed,

\[
BP=0,
\]

then every stochastic deformation replica remains closed:

\[
\boxed{B_{\rm fib}T(P,D)=0.}
\]

So deformation dispersion is not a boundary/interface producer.  Any physical
boundary defect must already be present in the chain/selector factor, or enter from
another literal operation.

**Status: Exact identity.**

## 3. The same statement survives on the full ordered pair current

Let `partial_pair` keep the two replica boundary faces in direct sum.  Writing

\[
C=(B_{\rm fib})T,
\]

the exact pair boundary is

\[
\boxed{
\partial_{\rm pair}(T\otimes T)
=
\begin{bmatrix}
C\otimes T\\
-T\otimes C
\end{bmatrix}.
}
\]

Thus for a closed selected cycle (`BP=0`) both pair faces vanish exactly.  There is
no third "deformation seam" hidden in the pair boundary.

This is the current-level counterpart of the earlier fact that pathwise `D` has
finite variation and no direct Brownian quadratic variation.

**Status: Exact identity.**

## 4. Full `Sigma_D` projects exactly to local material-tangent covariance

For a fixed reference tangent `e`,

\[
D^T e=(I\otimes e^T)\,\operatorname{vec}D.
\]

Define

\[
L_e:=I\otimes e^T.
\]

Then the covariance of the deformed tangent is not a new covariance sector:

\[
\boxed{
\operatorname{Cov}(D^Te,D^Tf)
=L_e\,\Sigma_D\,L_f^T.
}
\]

In particular,

\[
\operatorname{Cov}(D^Te)=L_e\Sigma_D L_e^T.
\]

This is an exact linear observation of the already-audited full vectorized
stochastic deformation covariance.

**Status: Exact identity.**

## 5. A fixed local cochain is another exact projection, not a new source

Let `alpha` be a fixed local spatial one-cochain.  Its readout on the deformed
reference tangent is

\[
Y_{e,\alpha}=\alpha^T D^T e.
\]

With column-major vectorization,

\[
\boxed{
Y_{e,\alpha}
=(\alpha\otimes e)^T\operatorname{vec}D.
}
\]

Hence for two tangent/cochain pairs,

\[
\boxed{
\operatorname{Cov}(Y_{e,\alpha},Y_{f,\beta})
=(\alpha\otimes e)^T\Sigma_D(\beta\otimes f).
}
\]

The same observation map projects the deformation carré-du-champ.  This means:

- the finite-horizon stochastic spread comes from Brownian **anchor sampling of
  spatially varying velocity gradient**;
- the deformed tangent and its fixed local cochain readout still have zero direct
  pathwise Brownian q.v. inherited from `D`;
- applying a fixed local current/cochain observation does not create a new physical
  covariance species.

**Status: Exact identity.**

## 6. The `2 nu / 3` cubic onset survives every fixed tangent/cochain projection

For locally smooth Navier--Stokes coefficients,

\[
\Sigma_D(h)
=
\frac{2\nu}{3}h^3
\sum_\mu
v_\mu v_\mu^T+O(h^4),
\qquad
v_\mu=\operatorname{vec}((\partial_\mu A)^T),
\quad A=\nabla u.
\]

Therefore

\[
\boxed{
\operatorname{Var}(\alpha^TD_h^Te)
=
\frac{2\nu}{3}h^3
\sum_\mu
\bigl[\alpha^T(\partial_\mu A)e\bigr]^2
+O(h^4).
}
\]

So the coefficient `2 nu / 3` is not an artifact of the row-Gram trace.  It survives
literal local current/cochain observation, with the spatial derivative and
orientation contractions dictated by the current and cochain themselves.

**Status: Rigorous consequence for locally smooth Navier--Stokes coefficients.**

## 7. Selected-support pair algebra: deformation, selector, and cross sector

For two replicas let

\[
T_i=T(P_i,D_i)=P_i\otimes D_i^T.
\]

The exact pathwise pair difference is

\[
\boxed{
T_1-T_2
=
T(P_1-P_2,D_1)
+
T(P_2,D_1-D_2).
}
\]

Call the first term `delta_sel` and the second `delta_D`.  The literal physical
pair functor is the tensor square, so before any expectation,

\[
\boxed{
\Delta T\otimes\Delta T
=
\delta_{\rm sel}\otimes\delta_{\rm sel}
+
\delta_D\otimes\delta_D
+
\delta_{\rm sel}\otimes\delta_D
+
\delta_D\otimes\delta_{\rm sel}.
}
\]

This Kronecker indexing is the actual ordered pair-current map.  An entrywise
`vec(Delta T) vec(Delta T)^T` contains permutation-equivalent products but is not
silently substituted for the physical pair functor here.

This gives a strict ledger rule.

### Shared/frozen first-bad selector

If both same-ancestor replicas start from the same frozen/hysteretic selected
current,

\[
P_1=P_2=P,
\]

then

\[
\delta_{\rm sel}=0
\]

and the selector/deformation cross pair terms are exactly zero.  The remaining pair spread
is the deformation sector transported through the fixed selected-current map.

### Replica-dependent selector

If the selector is reevaluated separately along the two replicas, `P_1 != P_2` in
general.  Then selector spread, deformation spread, and their cross pair terms are all
literal pair content.  Dropping the cross pair terms is not an identity.

Therefore `Sigma_D` must not be renamed selector covariance, resolution covariance,
or `S^int`.  Likewise selector reset covariance must not be renamed deformation
covariance.

**Status: Exact two-replica identity.**

## 8. The structural counterexample: `D` does not close the finite Kelvin-current state

The local tangent theorem above is exact, but it does **not** imply that a finite
Kelvin loop/surface is determined by `D`.

Use the exact smooth Navier--Stokes cubic heat shear

\[
u=(y^3+6\nu t y,0,0).
\]

At one anchor take two centered `yz` rectangles

\[
(b,c)=(1,1),
\qquad
(b,c)=(2,1/2).
\]

They have the same anchor, the same initial local deformation (`D=I` at zero
reverse age), and the same area vector

\[
\boxed{h=4e_x.}
\]

Nevertheless their exact finite-surface shape currents are

\[
\boxed{
E_{\rm shape}^{(1)}=-4e_y,
\qquad
E_{\rm shape}^{(2)}=-16e_y.
}
\]

Thus identical local `D` and identical local area data do not determine the finite
surface generator.  The obstruction is literal velocity-gradient variation across
the actual material shape.

The existing exact quintic/Legendre hierarchy is stronger: every finite even-moment
shape truncation can be defeated by a higher exact heat-shear Navier--Stokes
solution.  Hence there is no universal finite-moment closure to smuggle in as a
replacement for the full current shape.

**Status: Audited calibration (exact Navier--Stokes) and rigorous no-descent
consequence.**

## 9. Ledger placement after the coupling theorem

The current picture is now sharper.

1. `Sigma_D`: same-clock causal-past deformation covariance on the full `vec(D)`
   fiber.
2. `L Sigma_D L^T`: exact tangent/current/cochain projection of that same sector.
3. Frozen selected cycle: tensor-product transport of the deformation sector inside
   the closed-current pair space; no boundary seam is created.
4. Replica-dependent selector: a distinct selector pair sector plus mandatory cross
   pair terms.
5. Reduced hidden state: a distinct law-of-total-covariance resolution sector, as
   already audited.
6. Finite Kelvin current: requires the actual shape state `R(.)` (or an equivalent
   nontruncated representation); `D` alone is not a sufficient lift.
7. Future-remaining covariance bank: still a different clock until a literal state
   and time identification is proved.

No item above identifies `Sigma_D` with `S^int`, `Z_irr`, the future-remaining bank,
or the programme's unresolved restart quantity.

**Status: Exact ledger refinement; programme-specific full current/state lift remains
Open-literal.**

## 10. Full-state follow-through

The next theorem proposed here has now been derived in
`docs/full_current_shape_covariance_audit.md`.  On the literal reverse-age state
`(r,X,R(.),D)`, only `X` carries Brownian q.v.; NS makes the moving circulation drift
an exact pressure/Bernoulli gauge; Cartan turns anchor translation into the Kelvin
coefficient `<i_e Omega,Z>`; and the mixed deformation--Kelvin covariance is the
off-diagonal block of the joint connected covariance theorem.  Its short-age onset
is `O(h^2)`, between Kelvin variance `O(h)` and deformation covariance `O(h^3)`.

The remaining target has therefore moved: derive the exact finite-shape-to-local
current error and its joint deformation covariance on the migrating first-bad
support, then test whether genuine physical support collapse yields a descent.

**Status: Full-state source/cross law Exact; first-bad finite-shape descent remains
Open-literal.  No continuation/restart/regularity theorem claimed.**
