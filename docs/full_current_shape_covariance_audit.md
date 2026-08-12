# Full current-shape Kelvin covariance and deformation--circulation cross audit

This note moves one layer below the fixed-local-current projection.  The state is now
the literal common-noise backward-Kelvin current-shape cylinder, augmented by the
stochastic Cauchy deformation when that local tangent datum is also retained.

The rule remains physical typing first.  In particular:

- the anchor is the only Brownian coordinate;
- relative current shape is finite variation;
- the Cauchy deformation is finite variation;
- the Navier--Stokes one-form drift is a pressure/Bernoulli gauge on closed currents;
- the Kelvin martingale source is produced by anchor translation through vorticity;
- deformation covariance, Kelvin variance, and their cross covariance are different
  blocks of one joint same-ancestor covariance, not interchangeable banks.

No norm estimate, first-bad restart theorem, continuation theorem, or regularity
conclusion is used.

---

## 1. Literal reverse-age full state

Fix current physical time `t`, write reverse age

\[
r=t-\sigma,
\]

and choose an anchor `X` on a material current with relative shape points

\[
R_p=X_p-X.
\]

For the physical backward common-noise Kelvin flow, reverse age gives

\[
\boxed{
\begin{aligned}
dr_\sigma&=-d\sigma,\\
dX_\sigma&=-u(X_\sigma,r_\sigma)d\sigma
+\sqrt{2\nu}\,dW_\sigma,\\
dR_{p,\sigma}
&=-\bigl[u(X_\sigma+R_{p,\sigma},r_\sigma)-u(X_\sigma,r_\sigma)\bigr]d\sigma.
\end{aligned}}
\]

If the local stochastic Cauchy deformation is carried as an additional state
coordinate in the convention already audited in
`stochastic_cauchy_deformation_audit.md`,

\[
\boxed{
\partial_\sigma D_\sigma
=D_\sigma(\nabla u(X_\sigma,r_\sigma))^T.
}
\]

Therefore, in coordinates `(X,R_1,...,R_N,vec D)`, the diffusion covariance is

\[
\boxed{
a_{\rm full}
=\operatorname{diag}(2\nu I_X,0_R,0_D).
}
\]

The physical-time coordinate `r` also has zero q.v.

So there are three distinct mechanisms:

1. **anchor Brownian translation** -- the only martingale/q.v. channel;
2. **relative-shape velocity differences** -- finite-variation nonlocal shape
   transport;
3. **Cauchy strain/rotation transport** -- finite-variation local deformation.

**Status: Exact identity / physical typing.**

---

## 2. Full-state carré-du-champ is anchor-only

Let `F` and `G` be vector observables on the full state and let `m_F,m_G` be their
conditional means.  Since `a_full` has only the anchor block,

\[
\boxed{
\Gamma_{\rm full}(m_F,m_G)
=2\nu\sum_{\mu=1}^3
(\partial_{X_\mu}m_F)(\partial_{X_\mu}m_G)^T.
}
\]

Derivatives with respect to `R` or `D` can be large and physically active, but they
do not enter direct q.v. because those coordinates have no Brownian differential.
They enter the first-order generator and hence change the conditional means that
appear in the anchor derivatives at later reverse age.

This is the exact place where the distinction

> finite-variation random deformation dispersion versus pathwise quadratic variation

matters.  The former is generated indirectly because the anchor samples different
velocity gradients; it is not a hidden `dD dD` term.

**Status: Exact identity.**

---

## 3. Navier--Stokes makes the moving circulation drift a pure gauge

Write the momentum one-form as

\[
\beta=u^\flat.
\]

For a one-form, the material Lie derivative is

\[
(\mathcal L_u\beta)_i
=u^j\partial_j\beta_i+\beta_j\partial_i u^j.
\]

Because

\[
\beta_j\partial_i u^j
=\partial_i\frac{|u|^2}{2},
\]

the literal incompressible Navier--Stokes equation gives

\[
\boxed{
(\partial_t+\mathcal L_u-\nu\Delta)u^\flat
=d\!\left(\frac{|u|^2}{2}-p\right).
}
\]

Let `Z` be a closed material current.  Then

\[
\left\langle
 d\!\left(\frac{|u|^2}{2}-p\right),Z
\right\rangle
=
\left\langle
\frac{|u|^2}{2}-p,\partial Z
\right\rangle
=0.
\]

Thus the finite-variation drift of the actual moving Kelvin circulation is not an
untyped cancellation: it is an exact pressure/Bernoulli gauge killed by physical
closedness.

The audit checks this directly on the exact one-mode Navier--Stokes shear.

**Status: Exact Navier--Stokes / Cartan identity.**

---

## 4. Brownian translation of the actual cochain gives the Kelvin noise coefficient

For a constant Euclidean noise direction `e_mu`, Cartan gives

\[
\mathcal L_{e_\mu}\beta
=\iota_{e_\mu}d\beta+d(\iota_{e_\mu}\beta).
\]

Since

\[
\Omega=d\beta,
\]

and `Z` is closed,

\[
\boxed{
\partial_{X_\mu}\langle\beta,Z\rangle
=
\langle\mathcal L_{e_\mu}\beta,Z\rangle
=
\langle\iota_{e_\mu}\Omega,Z\rangle
=:a_\mu(Z).
}
\]

The exact term `d(u_mu)` vanishes by the same boundary-squared-zero mechanism as
pressure gauge.  Therefore the full-state anchor carré-du-champ becomes

\[
\boxed{
\Gamma_K(Z,Z')
=2\nu\sum_\mu a_\mu(Z)a_\mu(Z').
}
\]

This is exactly the Kelvin pair source already used elsewhere in the repository,
now derived on the literal moving current-shape state rather than inserted as a
frozen-current coefficient.

Relative-shape motion changes `Z` by first-order transport and hence changes the
values of `a_mu(Z)` along the path.  It does **not** add a direct shape q.v. source.

**Status: Exact Cartan + closed-current identity.**

---

## 5. This instantiates the existing connected covariance theorem on the physical state

For any stacked terminal observable on the full current-shape Markov state, the
repository's existing connected vector covariance theorem applies with the full
reverse-age generator.  The diagonal pair defect is precisely

\[
\Gamma_{\rm full}=J_X(2\nu I)J_X^T.
\]

For a Kelvin circulation block, Section 4 identifies that block with the literal
Kelvin action.  For the deformation block, the earlier audit identifies it with the
anchor sampling source

\[
2\nu\sum_\mu
\operatorname{vec}(\partial_\mu\bar D)
\operatorname{vec}(\partial_\mu\bar D)^T.
\]

Thus no new branching producer is created by putting the current shape and `D` in
the same state.  The new content is the **mixed block that the joint covariance
forces**.

**Status: Exact specialization of the existing connected covariance/pair theorem.**

---

## 6. Exact deformation--Kelvin cross-covariance law

Let

\[
z=\operatorname{vec}D,
\qquad
K=\text{scalar Kelvin terminal payoff},
\]

and define

\[
\bar z=E[z],
\qquad
\bar K=E[K],
\qquad
C_{DK}=E[zK]-\bar z\,\bar K.
\]

With the current-end reverse-age horizon operator

\[
\mathcal H_h
=\partial_h+\partial_t+u\cdot\nabla-\nu\Delta
\]

and the deformation horizon connection

\[
B_D=I\otimes(\nabla u)^T,
\]

the exact mixed law is

\[
\boxed{
\mathcal H_h C_{DK}
=B_D C_{DK}+\Gamma_{DK},
}
\]

where

\[
\boxed{
\Gamma_{DK}
=2\nu\sum_\mu
\operatorname{vec}(\partial_\mu\bar D)\,
\partial_\mu\bar K.
}
\]

This follows from the diffusion product rule applied to `bar z * bar K`.  It is also
exactly the off-diagonal block of the joint connected-covariance theorem for

\[
\boxed{
Y_{\rm joint}=
\begin{bmatrix}
\operatorname{vec}D\\
K
\end{bmatrix}.
}
\]

Physical typing:

- `Sigma_D` is deformation--deformation covariance;
- `V_K` is Kelvin--Kelvin variance;
- `C_DK` is deformation--circulation cross covariance;
- all three are generated by the same noisy anchor but are different observable
  blocks and must not be renamed into one another.

**Status: Exact identity.**

---

## 7. Short-horizon hierarchy: `h`, `h^2`, `h^3`

At a smooth current point, set

\[
A=\nabla u,
\qquad
v_\mu=\operatorname{vec}((\partial_\mu A)^T),
\qquad
g_\mu=\partial_{X_\mu}K_0.
\]

For an actual closed Kelvin current, Section 4 gives

\[
\boxed{g_\mu=a_\mu(Z).}
\]

The three joint covariance blocks have different leading ages:

\[
\boxed{
V_K(h)
=2\nu h\sum_\mu g_\mu^2+O(h^2),
}
\]

\[
\boxed{
C_{DK}(h)
=\nu h^2\sum_\mu v_\mu g_\mu+O(h^3),
}
\]

\[
\boxed{
\Sigma_D(h)
=\frac{2\nu}{3}h^3
\sum_\mu v_\mu v_\mu^T+O(h^4).
}
\]

The powers have a direct physical origin:

- Kelvin circulation responds immediately to anchor translation: response `O(1)`;
- deformation must first integrate one sampled velocity gradient: response `O(h)`;
- covariance integrates the product of those response profiles over age.

No norm estimate is involved.

**Status: Rigorous consequence for locally smooth Navier--Stokes coefficients.**

---

## 8. The leading joint block has an exact Gram-integral representation

The leading covariance of `(vec D,K)` is

\[
\boxed{
\Sigma_{\rm joint}^{(0)}(h)
=
\begin{bmatrix}
\frac{2\nu}{3}h^3\sum_\mu v_\mu v_\mu^T
&
\nu h^2\sum_\mu v_\mu g_\mu\\
\nu h^2\sum_\mu g_\mu v_\mu^T
&
2\nu h\sum_\mu g_\mu^2
\end{bmatrix}.
}
\]

More rigidly,

\[
\boxed{
\Sigma_{\rm joint}^{(0)}(h)
=
2\nu\sum_\mu
\int_0^h
\begin{bmatrix}s v_\mu\\g_\mu\end{bmatrix}
\begin{bmatrix}s v_\mu\\g_\mu\end{bmatrix}^{T}\,ds.
}
\]

Hence the coefficients `2/3`, `1`, and `2` are one integrated response geometry:

\[
2\nu\int_0^h s^2ds=\frac{2\nu}{3}h^3,
\quad
2\nu\int_0^h s\,ds=\nu h^2,
\quad
2\nu\int_0^h1\,ds=2\nu h.
\]

The leading block is PSD because it is literally a sum of Gram integrals.  This is
not a post hoc Cauchy--Schwarz estimate.

**Status: Exact algebraic representation of the rigorous short-horizon leading tensor.**

---

## 9. Exact one-mode Navier--Stokes referee for the mixed block

Take

\[
u=(U(y,t),0,0),
\qquad
U=e^{-\alpha t}\cos(ky),
\qquad
\alpha=\nu k^2.
\]

Use the same reverse Brownian anchor

\[
Y_\sigma=y+\sqrt{2\nu}W_\sigma.
\]

The active deformation coefficient is

\[
c_h=\int_0^h U_y(Y_\sigma,t-\sigma)d\sigma,
\]

while the normalized closed `x`-cycle Kelvin terminal payoff is

\[
K_h=e^{-\alpha(t-h)}\cos(kY_h).
\]

Its conditional mean is exactly

\[
E[K_h]=U(y,t),
\]

independent of `h`, as required by the backward Kelvin/heat martingale.

Direct Gaussian integration gives

\[
\boxed{
\operatorname{Cov}(c_h,K_h)
=
\frac{k e^{-2\alpha t}\sin(2ky)}{4\alpha}
\left(2\alpha h-1+e^{-2\alpha h}\right).
}
\]

The audit verifies exactly that this satisfies the mixed horizon PDE of Section 6.
Its short-age expansion is

\[
\boxed{
\operatorname{Cov}(c_h,K_h)
=\nu h^2 U_{yy}(y,t)U_y(y,t)+O(h^3).
}
\]

Thus the exact shear referees:

- the positive `2 nu` anchor cross-carré-du-champ source;
- the deformation connection ordering;
- the `nu h^2` coefficient;
- the orientation/sign in `U_yy U_y`;
- the fact that the mixed block can be signed even though the full joint covariance
  is PSD.

The same exact shear also verifies that the full `5 x 5` joint covariance of
`(vec D,K)` is the existing connected vector covariance theorem with block
connection `diag(B_D,0)` after converting to the repository's connection convention.

**Status: Audited calibration (exact periodic Navier--Stokes).**

---

## 10. Three locations in the same shear separate the mechanisms

The exact shear makes the physical distinction visible without estimates.

- At `y=0`, `U_y=0` but `U_yy != 0`: the leading Kelvin q.v. and mixed block vanish,
  while deformation dispersion has the already-audited positive cubic onset.
- At `ky=pi/2`, `U_y != 0` but `U_yy=0`: Kelvin q.v. is active, while the leading
  deformation dispersion and mixed block vanish.
- At a generic point such as `ky=pi/4`, both are active and the mixed `h^2` block is
  nonzero.

So no one of the three blocks can be substituted for another.

**Status: Audited calibration / rigorous mechanism separation.**

---

## 11. What this closes in the ledger

The physical current-shape side is now more explicit.

1. **Full physical state:** `(r,X,R(.),D)` has a literal reverse-age generator with
   Brownian covariance only in `X`.
2. **Actual moving Kelvin circulation:** NS drift is exact gauge on closed currents;
   Brownian translation gives the Cartan/vorticity coefficient `a_mu(Z)`.
3. **Same-ancestor pair source:** exactly the anchor carré-du-champ on the full
   current-shape state.
4. **Deformation/Kelvin coupling:** `C_DK` is the mixed block of the existing joint
   connected covariance theorem, not `S^int`, not resolution covariance, and not a
   new branching producer.
5. **Finite shape:** `R(.)` remains essential for finite currents.  The cubic and
   polynomial heat-shear counterexamples still forbid universal descent to `D`, an
   area frame, or any finite shape-moment truncation.
6. **Reduced ancestry state:** identifying the programme's stored ancestry variable
   with the physical anchor marginal and its conditional shape kernel remains
   unproved.
7. **First-bad selected support:** a theorem that shrinking/hysteretic selected
   support makes the full `R(.)` dependence descend to the local joint block remains
   unproved.
8. **Future-remaining bank:** still a different clock unless the state/time lift is
   explicitly constructed.

**Status: Exact physical full-state covariance law; programme-specific reduced-state
and first-bad descent remain Open-literal.**

---

## 12. Next literal target

The next structural question is no longer "where does the pair source come from?".
That source is now explicit.  The remaining hard question is the finite-shape
**descent at the migrating first-bad support**.

Before any norm estimate, derive the exact evolution of the difference

\[
K_{Z(R)}-K_{Z_{\rm local}(D,H)}
\]

and of its joint covariance with `vec D` under the same reverse-age generator.
The cubic/Legendre examples say this error cannot vanish by algebra alone at finite
scale.  The only plausible route is a genuinely shrinking physical support theorem
that makes the full shape current collapse to its local jet while retaining the
metric-whitened pair covariance topology.

That is still a state/descent theorem or a counterexample problem first; only after
its exact current equation is visible should an estimate be attempted.

**Status: Open-literal.  No restart/continuation/regularity theorem claimed.**
