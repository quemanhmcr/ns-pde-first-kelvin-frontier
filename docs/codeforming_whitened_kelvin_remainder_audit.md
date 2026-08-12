# Codeforming Kelvin remainder and metric-whitened Stokes topology

## Scope

The repository already identified

\[
H^{-T}\varepsilon_H
\]

as the invariant remainder topology for an orientation-complete three-face Kelvin
packet.  This note asks what that object is **physically**, before estimating it.

The answer is exact.  For a coherent line frame `L` with area frame

\[
H=\operatorname{cof}(L),
\]

metric whitening reconstructs a physical vorticity-like residual vector from the
orientation flux coordinates.  At pointwise density level the reconstruction is
literally the physical field defect.  At finite scale the three components are
integrals over three different faces, so the reconstructed vector is a finite-face
object and must not be retyped as a pointwise field value.

No future-clock identification, restart theorem, continuation theorem, or regularity
claim is made.

---

## 1. Pointwise orientation density: whitening is exact physical inversion

Let `delta zeta` be a physical vector-field defect at a common point and let the
orientation-complete area frame be `H`.  The three flux-density coefficients are

\[
\boxed{
g_H=H^T\delta\zeta.
}
\]

Therefore

\[
\boxed{
H^{-T}g_H=\delta\zeta.
}
\]

At this level metric whitening is not a chosen norm.  It is the exact inverse of the
orientation-coordinate map.

**Status: Exact identity / physical typing.**

---

## 2. The codeforming Kelvin one-form lands exactly in this topology

For the actual same-time Navier--Stokes vorticity field, the previous audit derived

\[
\beta_L=(L^TL)\mathcal N_L
\]

and

\[
\operatorname{curl}_\xi\beta_L
=H^T[\omega(X+L\xi)-\omega(X)].
\]

Whitening gives

\[
\boxed{
H^{-T}\operatorname{curl}_\xi\beta_L
=\omega(X+L\xi)-\omega(X).
}
\]

Thus the Stokes--Piola density of the finite Kelvin descent error and the existing
metric-whitened local topology are the same physical map at fixed coherent state.

This is a fixed-state/current identity.  It does not identify a future-bank clock or
the programme ancestry state.

**Status: Exact Stokes--Piola / whitening identity.**

---

## 3. Finite three-face residual: reconstruction, not a pointwise value

Let

\[
\varepsilon_H
=\begin{bmatrix}
\varepsilon_1\\
\varepsilon_2\\
\varepsilon_3
\end{bmatrix}
\]

be the three finite face circulation/flux residuals.  Define

\[
\boxed{
r_H:=H^{-T}\varepsilon_H.
}
\]

`r_H` has physical vector units and is the vector reconstructed from the full
orientation packet.  At finite scale it is **not a pointwise field value**.

But each `epsilon_j` is integrated over a **different face**.  In general there is no
single point `y` such that

\[
r_H=\zeta(y)-\zeta(x).
\]

The pointwise identity of Section 1 applies to a common orientation density, not to
three unrelated finite face integrals.

### Exact cubic NS referee

For the exact cubic heat shear

\[
u=(y^3+6\nu ty,0,0)
\]

at `y=0`, subtract the value and affine Taylor part.  On the unit reference cube
`L=I`,

\[
\beta=(\xi_y^3,0,0),
\qquad
\operatorname{curl}_\xi\beta=(0,0,-3\xi_y^2).
\]

The center vorticity defect is zero, but the `xy` face integral is

\[
\boxed{
\varepsilon_H=(0,0,-1/4)^T.
}
\]

Since `H=I`,

\[
\boxed{
r_H=(0,0,-1/4)^T\neq0.}
\]

So a finite reconstructed residual is not a pointwise center defect even in an exact
smooth Navier--Stokes solution.

**Status: Exact definition / audited exact-NS finite-scale calibration.**

---

## 4. Isotropic cubic scaling explains the old `r^2` whitened remainder

For `L=rI`,

\[
H=r^2I.
\]

The cubic residual gives

\[
\beta_r=r^4\xi_y^3e_x,
\]

hence

\[
\varepsilon_{H,r}
=-\frac{r^4}{4}e_z.
\]

Whitening removes precisely the area factor:

\[
\boxed{
r_{H,r}=H^{-T}\varepsilon_{H,r}
=-\frac{r^2}{4}e_z.}
\]

This is the literal exact-NS face behind the previously audited statement that a
centered smooth finite Stokes remainder is `O(r^2)` after metric normalization.

No estimate was used to obtain this calibration.

**Status: Audited calibration (exact Navier--Stokes).**

---

## 5. Homogeneous jet exponent ladder

For a homogeneous nonaffine velocity jet of degree `p>=2`, the previous codeforming
law is

\[
\mathcal N_{\rho S}^{(p)}
=\rho^{p-1}S^{-1}U_p(S\xi),
\qquad \det S=1.
\]

The line metric is

\[
G_{\rho S}=\rho^2S^TS.
\]

Therefore the Kelvin one-form is

\[
\boxed{
\beta_{\rho S}^{(p)}
=\rho^{p+1}S^TU_p(S\xi).
}
\]

Meanwhile

\[
H=\operatorname{cof}(\rho S)=\rho^2S^{-T},
\qquad
H^{-T}=\rho^{-2}S.
\]

Hence the exact hierarchy of scalar powers is

\[
\boxed{
\begin{array}{ccl}
\text{kinematic nonaffinity }\mathcal N_L &:& \rho^{p-1},\\
\text{Kelvin one-form / raw flux density} &:& \rho^{p+1},\\
\text{whitened Stokes defect} &:& \rho^{p-1}.
\end{array}
}
\]

The two extra powers in the Kelvin face are exactly the oriented-area powers removed
by `H^{-T}`.

Anisotropy remains a tensorial action and is not summarized by these scalar powers.

**Status: Exact homogeneous scale--shape identity.**

---

## 6. Metric-whitened energy is ordinary energy of the reconstructed residual

For any finite face residual vector,

\[
\boxed{
|r_H|^2
=\varepsilon_H^T(H^TH)^{-1}\varepsilon_H.
}
\]

So the packet metric is exactly the Euclidean physical-vector energy after
orientation reconstruction.

For centered covariance `C_epsilon` at fixed `H`,

\[
\boxed{
C_r
=H^{-T}C_\varepsilon H^{-1},
}
\]

and

\[
\boxed{
\operatorname{tr}C_r
=\operatorname{tr}[C_\varepsilon(H^TH)^{-1}].
}
\]

This supplies a physical interpretation for the repository's metric-whitened
covariance contraction.

**Status: Exact linear covariance identity.**

---

## 7. Passive orientation coordinates are gauge

Under an invertible passive orientation-coordinate change

\[
H_+=HR,
\qquad
\varepsilon_+=R^T\varepsilon,
\]

one has

\[
\boxed{
H_+^{-T}\varepsilon_+
=H^{-T}\varepsilon.
}
\]

Thus the reconstructed residual is independent of the chosen orientation basis.
This is a passive `GL(3)` coordinate statement, not a claim that changing the
physical finite surfaces leaves their residuals unchanged.

**Status: Exact identity.**

---

## 8. The stochastic q.v. also reconstructs exactly

Let the orientation-complete finite-error martingale coefficients be

\[
q_\mu\in\mathbb R^3,
\]

so

\[
\Gamma_\varepsilon
=2\nu\sum_\mu q_\mu q_\mu^T.
\]

Because `H` is finite variation in the instantaneous martingale direction, the
reconstructed coefficients are

\[
\widehat q_\mu=H^{-T}q_\mu.
\]

Therefore

\[
\boxed{
H^{-T}\Gamma_\varepsilon H^{-1}
=2\nu\sum_\mu
\widehat q_\mu\widehat q_\mu^T.
}
\]

The metric-whitened q.v. is exactly the q.v. tensor of the reconstructed physical
residual process.  It is not a new branching source.

**Status: Exact identity.**

---

## 9. Full payoff covariance has mandatory local--residual cross blocks

The existing fixed-state decomposition is

\[
X_H=H^T\zeta(x)+\varepsilon_H.
\]

Whitening gives

\[
\boxed{
W_H:=H^{-T}X_H
=\zeta(x)+r_H.
}
\]

Take covariance **before** discarding anything:

\[
\boxed{
\operatorname{Cov}(W_H)
=C_\zeta+C_r+C_{\zeta r}+C_{\zeta r}^T.
}
\]

The two cross blocks are mandatory.  Therefore

\[
H^{-T}C_HH^{-1}-C_\zeta
\]

is not generally equal to `Cov(r_H)` at finite scale.

A two-state exact algebraic calibration with anti-correlated local and residual
vectors gives nonzero signed cross blocks and a full covariance different from
`C_zeta+C_r`.

The existing conditional `L^2` theorem remains valid because small `r_H` controls
both its covariance and the cross blocks.  That is an **estimate after** this exact
algebra, not a license to delete the cross terms beforehand.

**Status: Exact covariance identity / audited algebraic cross-block calibration.**

---

## 10. Placement relative to the future-covariance tensor theorem

This audit closes a **fixed-state physical typing seam**:

- `H^{-T} epsilon_H` is a reconstructed physical residual vector;
- at pointwise orientation-density level it is exactly the physical field defect;
- for the actual same-time NS vorticity/current it is generated by the codeforming
  Kelvin one-form `beta_L` through Stokes;
- its covariance and q.v. are the ordinary covariance/q.v. of that reconstructed
  vector.

It does **not** close these separate seams:

1. the future-bank clock versus the causal past/reverse-age clock;
2. the programme ancestry state/lift;
3. uniform first-bad support locality;
4. uniform first-bad metric-whitened residual control;
5. dynamic finite-current shape control by `N_L,D N_L`;
6. restart/continuation/regularity.

In particular, the same algebra applies to a random future payoff once a literal
same-state packet `X_H` is specified, but the present theorem does not identify that
future random payoff with the same-time deterministic `beta_L` process across
clocks.

**Status: Exact fixed-state topology identification; cross-clock identification
Open-literal.**

---

## 11. Refined first-bad target

The fixed-state local tensor condition

\[
H^{-T}\varepsilon_H\to0
\]

can now be read literally as

\[
\boxed{
r_H\to0,}
\]

where `r_H` is the physical residual reconstructed from the three actual finite face
circulations.

For a same-time NS current, those face circulations are Stokes integrals of
`curl_xi beta_L`.  For a future conditional packet, they are the corresponding
future payoff residuals on that specified full state.

The surviving hard theorem is therefore not to justify the topology; its physical
meaning is now exact.  The hard theorem is to prove that the actual migrating
first-bad packet is support-local **and** that its reconstructed residual tends to
zero uniformly on the correct state/clock, while retaining selector, boundary,
exit, reset, and covariance cross faces.

**Status: Open-literal.  No restart/continuation/regularity theorem claimed.**

---

## 12. Dynamic reconstruction: the physical residual carries the reverse line connection

The fixed-state reconstruction `r_H=H^-T epsilon_H` has now been differentiated on
the literal reverse-age Kelvin state.  When `H` is the local reverse cofactor frame,
`Hdot=A^T H`, so `(H^-T)dot=-A H^-T`.

For the local-frame error `epsilon=K-H^T omega`, both the actual closed-current
Kelvin drift and the local Nanson/vorticity-flux drift vanish exactly.  Thus
`epsilon` is a pure orientation-coordinate martingale.  Its physical reconstruction
satisfies

\[
\boxed{
dr=-A r\,d\sigma+\sqrt{2\nu}\,H^{-T}(A_K-H^T\nabla\omega)\,dW.
}
\]

Changing from the earlier actual-area error `K-omega.h_R` to `K-omega.h` does not
discard finite shape drift: `-omega.R_A` is transferred exactly into the geometry
mismatch `omega.(h_R-h)` with opposite sign.

The reconstructed residual q.v. and the local-vorticity/residual cross q.v. are both
literal.  The full reconstructed payoff `W=omega+r` requires both cross blocks in its
q.v. and dyad dynamics.  Exact cubic heat shear gives a nonzero conserved residual
with zero q.v.; exact one-mode shear activates a generically nonzero local/residual
cross q.v.

**Status: Exact same-clock dynamic identity / audited exact-NS calibrations.  Reduced
covariance closure, future-clock identification, and first-bad uniform control remain
Open-literal/Open.  No restart/continuation/regularity theorem claimed.**

See `docs/dynamic_reconstructed_kelvin_residual_audit.md`.
