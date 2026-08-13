# Necessary physical admissibility constraints for any first-bad rule

This note deliberately does **not** propose a first-bad badness functional.  It asks
a prior question:

> What must any future first-bad rule respect before it can even be interpreted as a
> physical Navier--Stokes rule rather than an observer-coordinate artifact?

The answer comes from exact packet gauge, support geometry, selector memory, pair
coherence, and adaptive-event algebra already derived in the repository.

Passing the tests below is **necessary typing only**.  It is not a sufficient
regularity mechanism.

## 1. Passive packet coordinates are not physical badness

For an orientation-complete finite packet let

\[
H=(h_1,h_2,h_3)
\]

be its invertible oriented area frame and let

\[
\varepsilon\in\mathbb R^3
\]

be the three raw finite face residual coefficients.

A passive orientation-coordinate change is

\[
H\mapsto H'=HS,
\qquad
\varepsilon\mapsto\varepsilon'=S^T\varepsilon,
\qquad S\in GL(3).
\]

The physical reconstructed residual is

\[
\boxed{r=H^{-T}\varepsilon.}
\]

Therefore

\[
(H')^{-T}\varepsilon'
=(HS)^{-T}S^T\varepsilon
=H^{-T}\varepsilon
=r.
\]

Hence the physical energy

\[
\boxed{
|r|^2
=\varepsilon^T(H^TH)^{-1}\varepsilon
}
\]

is exactly passive-gauge invariant.

By contrast, the raw Euclidean coordinate square

\[
|\varepsilon|^2
\]

is not invariant under non-orthogonal `S`.

**Classification: Exact identity / exact physical typing.**

## 2. Exact passive-gauge ranking flip: raw first-bad score is observer artifact

Take two physically fixed packet residuals:

\[
H_0=H_1=I,
\qquad
\varepsilon_0=e_1,
\qquad
\varepsilon_1=\frac32e_1.
\]

Before any reparameterization,

\[
(|\varepsilon_0|^2,|\varepsilon_1|^2)
=\left(1,\frac94\right).
\]

Thus a rule that ranks larger raw residual norm as "worse" selects germ `1`.

Now perform only a passive basis change on packet `0`:

\[
S_0=\operatorname{diag}(2,1,1),
\quad
H_0'=H_0S_0,
\quad
\varepsilon_0'=S_0^T\varepsilon_0=2e_1.
\]

No physical packet has changed.  But the raw coordinate energies become

\[
\left(4,\frac94\right),
\]

so the raw-norm ranking flips from germ `1` to germ `0`.

The physical whitened energies remain exactly

\[
\left(1,\frac94\right)
\]

before and after, so the physical ranking does not change.

Therefore a first-bad predicate/ranking built from raw packet-coordinate residual
norm can change solely because the observer changed coordinates.

**Classification: Audited calibration / rigorous observer-artifact no-go.**

## 3. Physical event rules must also be passive-gauge equivariant

Suppose a raw orientation packet refinement block is `R` from child frame `H_c` to
parent frame `H_p`.  The physical residual synthesis block is

\[
\boxed{
A=H_p^{-T}R H_c^T.
}
\]

Under independent passive bases

\[
H_p\mapsto H_pS_p,
\qquad
H_c\mapsto H_cS_c,
\]

the raw block must transform as

\[
R\mapsto R'
=S_p^T R S_c^{-T}.
\]

Then

\[
(H_pS_p)^{-T}R'(H_cS_c)^T
=A
\]

exactly.

The symbolic calibration changes `R` nontrivially while the physical `A` remains
identical.  Thus a future first-bad event rule stated in raw packet coordinates must
transform equivariantly; otherwise the physical event changes when only the observer
basis changes.

**Classification: Exact gauge identity / necessary event typing.**

## 4. Gauge-invariant residual smallness is still not support locality

Removing observer artifact does not solve the physical first-bad problem.

Use the exact quadratic Navier--Stokes heat shear with anisotropic line frame

\[
L_\rho=\operatorname{diag}(1,\rho,\rho).
\]

The audited finite packet has

\[
\varepsilon_z=-\rho^2,
\qquad
\chi_z=-1,
\qquad
r_z=-\rho,
\]

so the literal physical reconstructed energy is

\[
\boxed{|r|^2=\rho^2\to0.}
\]

But the physical `x` support line remains exactly length `1`:

\[
\boxed{|L_\rho e_x|^2=1.}
\]

Therefore

\[
\boxed{
\text{physical residual collapse}
\not\Rightarrow
\text{support locality}.
}
\]

A first-bad rule cannot use a correct gauge-invariant residual score as a substitute
for the actual support geometry/locality/conditioning face.

**Classification: Audited exact-Navier--Stokes calibration / rigorous insufficiency.**

## 5. Genuine hysteretic switches require persistent-library state

For a selector switch `g -> h`, the active residual is a readout

\[
Y_g=E_g X
\]

of a persistent candidate library `X`.

The existing exact counterexample gives two full library states `X_1,X_2` with

\[
E_gX_1=E_gX_2
\]

but

\[
E_hX_1\ne E_hX_2.
\]

The same obstruction exists at second order: two PSD full-library second moments can
have the same old selected block but different new selected blocks after the switch.

Therefore an arbitrary hysteretic first-bad rule cannot use the previously selected
endpoint state alone as a universally compositional physical state.

**Classification: Rigorous consequence of exact selector-readout no-go.**

## 6. Diagonal spectral channels do not retain event coherence

Even after preserving the persistent library, an event state cannot generically be
reduced to diagonal nonnegative spectral channel values alone.

The exact PSD calibration uses

\[
Q_+=
\begin{pmatrix}
1&1/2&0\\
1/2&1&0\\
0&0&0
\end{pmatrix},
\qquad
Q_-=
\begin{pmatrix}
1&-1/2&0\\
-1/2&1&0\\
0&0&0
\end{pmatrix}.
\]

They have identical diagonal spectral channel list

\[
(1,1,0),
\]

but opposite cross-channel coherence.  Under the same later linear event map, the
parent channel values differ by exactly

\[
\boxed{2.}
\]

Thus full signed second-moment coherence is physical event memory; diagonal channel
scores are not a universal event state.

**Classification: Audited PSD calibration / rigorous coherence necessity.**

## 7. Adaptive first-bad events require the event--state joint law

A first-bad selector/event map is intended to depend on the state.  The exact
adaptive two-replica law shows

\[
\mathbb E_2[CQC^T]
\]

contains mean-map, positive event-map dispersion, and signed event--state correlation
faces.

The PSD aligned calibration gives

\[
1+1+1+1=4,
\]

while the PSD anti-aligned calibration gives

\[
1+1-1-1=0.
\]

In both cases the naive mean-map/mean-payload face is `1`.

Therefore an adaptive first-bad rule cannot close its expectation-level physical
state using only the mean event map and mean payload.  The joint event-map/library
law is required.

**Classification: Rigorous consequence of exact adaptive-event algebra.**

## 8. Necessary physical admissibility ledger

Any future first-bad rule must at least survive the following tests:

1. **packet gauge invariance** — passive `GL(3)` orientation coordinates cannot alter
   the physical badness decision;
2. **event gauge equivariance** — raw packet event coordinates must represent the
   same physical event map under passive reparameterization;
3. **support separation** — residual smallness cannot stand in for actual support
   locality/conditioning;
4. **persistent-library memory** — genuine hysteretic selector switches cannot be
   propagated from the old selected endpoint alone;
5. **full second-order coherence** — diagonal spectral channels alone do not close
   later linear event response;
6. **adaptive joint-law memory** — state-dependent event selection requires the
   event-map/state correlation faces.

These are **necessary physical admissibility constraints**.  They do not specify how
Navier--Stokes decides that a packet is bad, when a packet resolves, or when an event
must occur.

**Classification: Rigorous synthesis of exact necessary conditions.**

## 9. What is explicitly not proved

This audit does not define a sufficient first-bad functional.  It does not identify a
singularity threshold, does not prove that any admissible score is monotone, and does
not show that the actual migrating packet remains local.

The programme still needs the physical Navier--Stokes mechanism that generates the
candidate library and its badness/resolve/event rule while satisfying all the
constraints above.

**Status: first-bad badness/resolve functional remains Open-literal.**

**Status: support-locality and uniform physical channel control remain Open.**

No restart/continuation/regularity theorem claimed.
