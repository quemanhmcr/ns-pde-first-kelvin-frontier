# Vorticity/Kelvin microframe audit for the restart frontier

This note moves from the pair-localization bookkeeping back into the actual local
3D incompressible Navier--Stokes PDE.  The goal is not to insert a continuation norm
at the beginning.  The goal is to identify, before any estimate, the physical
mechanisms that can increase a vorticity germ and the exact Kelvin object that
records viscous vorticity-gradient dissipation.

No continuation theorem or 3D Navier--Stokes regularity claim is made here.

---

## 1. Curl the real Navier--Stokes equation before estimating it

For

\[
\partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u,
\qquad \nabla\cdot u=0,
\]

write

\[
\omega=\nabla\times u,
\qquad
S=\frac12(\nabla u+\nabla u^T),
\qquad
A=\frac12(\nabla u-\nabla u^T).
\]

Curl removes pressure exactly.  The standard vector identity gives

\[
\partial_t\omega+(u\cdot\nabla)\omega
=(\omega\cdot\nabla)u+\nu\Delta\omega.
\]

The skew part of the velocity gradient has axial vector parallel to `omega`, hence

\[
A\omega=0.
\]

Therefore

\[
\boxed{
(\partial_t+u\cdot\nabla)\omega=S\omega+\nu\Delta\omega.
}
\]

Nothing has been bounded.  The nonlinear vorticity producer is now physically
identified: it is strain acting on vorticity.  Rigid rotation does not stretch its
own vorticity.

**Classification: Exact identity.**

---

## 2. Vortex stretching is literal material-line stretching

Let `ell` be an infinitesimal material line vector.  Its exact kinematic law is

\[
\dot\ell=(\nabla u)\ell.
\]

Hence

\[
\boxed{
\frac d{dt}|\ell|^2=2\ell\cdot S\ell.
}
\]

The skew part only rotates.  If `hat ell=ell/|ell|`,

\[
\frac d{dt}\log|\ell|=\hat\ell\cdot S\hat\ell.
\]

When the line is tangent to a vortex line, define, only where `omega != 0`,

\[
\xi_\omega=\frac\omega{|\omega|},
\qquad
\boxed{\alpha_{\rm vort}:=\xi_\omega\cdot S\xi_\omega.}
\]

Then

\[
\boxed{
\omega\cdot S\omega=|\omega|^2\alpha_{\rm vort}.
}
\]

Thus `alpha_vort` has an exact physical meaning: the instantaneous logarithmic
lengthening rate of a material line aligned with the vorticity direction.

The older repository phrase `alpha^2 tau` was never defined line by line.  This
note does **not** identify it with `alpha_vort`.

**Classification: Exact kinematic identity; no identification with the old
undefined placeholder.**

---

## 3. Vorticity amplitude and direction separate exactly

Write

\[
\omega=\rho\xi,
\qquad
\rho=|\omega|,
\qquad
|\xi|=1
\]

away from vorticity zeros.  The unit-vector identity

\[
\xi\cdot\Delta\xi=-|\nabla\xi|^2
\]

gives

\[
\omega\cdot\Delta\omega
=\rho\Delta\rho-\rho^2|\nabla\xi|^2.
\]

Dotting the vorticity equation with `xi` yields

\[
\boxed{
(\partial_t+u\cdot\nabla)\rho
=\rho\alpha_{\rm vort}
+\nu\bigl(\Delta\rho-\rho|\nabla\xi|^2\bigr).
}
\]

So the visible complexity separates into three concrete mechanisms:

1. vortex-line stretching `rho alpha_vort`;
2. scalar spatial diffusion `nu Delta rho`;
3. a non-positive directional-roughness penalty `-nu rho |grad xi|^2`.

This is not a norm inequality.  It is the local PDE itself.

**Classification: Exact identity away from vorticity zeros.**

---

## 4. Local enstrophy ledger

Set

\[
e=\frac12|\omega|^2.
\]

Dot the vorticity equation with `omega` and use

\[
\omega\cdot\Delta\omega
=\Delta e-|\nabla\omega|^2.
\]

Then

\[
\boxed{
(\partial_t+u\cdot\nabla)e
=\omega\cdot S\omega
+\nu\Delta e
-\nu|\nabla\omega|^2.
}
\]

The three terms on the right are, respectively,

- vortex-stretching production;
- signed spatial/Hodge flux after localization;
- bulk viscous vorticity-gradient dissipation.

**Classification: Exact identity.**

---

## 5. The Kelvin small-loop coefficient sees directional vorticity gradients

Return to the Kelvin noise coefficient used throughout the repository.  In the
constant orthonormal noise frame `e_i`,

\[
a_i(Z)=\langle\iota_{e_i}\Omega,Z\rangle,
\qquad
\gamma(Z)=2\nu\sum_i a_i(Z)^2,
\]

where the vorticity two-form is `Omega=du^flat`.

Take an oriented small disk `Sigma_r(x,n)` with unit normal `n`, area `A_r`, and
closed boundary current

\[
Z_r=\partial\Sigma_r.
\]

Stokes and Cartan give, exactly,

\[
\begin{aligned}
a_i(Z_r)
&=\int_{\partial\Sigma_r}\iota_{e_i}\Omega\\
&=\int_{\Sigma_r}d\iota_{e_i}\Omega\\
&=\int_{\Sigma_r}\mathcal L_{e_i}\Omega,
\end{aligned}
\]

because `d Omega=0`.  In a constant Euclidean frame,
`L_{e_i} Omega` is the two-form corresponding to `partial_i omega`.  Therefore,
for smooth vorticity,

\[
\boxed{
\frac{a_i(Z_r)}{A_r}
\longrightarrow
(\partial_i\omega(x))\cdot n
\qquad(r\downarrow0).
}
\]

Consequently the area-squared normalized Kelvin action has the exact local limit

\[
\boxed{
\gamma_{\rm dens}(x,n)
:=\lim_{r\downarrow0}\frac{\gamma(Z_r)}{A_r^2}
=2\nu\,|(\nabla\omega)^Tn|^2.
}
\]

For an affine directional vorticity gradient across the spanning disk, the finite
area formula is already exact.

**Classification: Exact Stokes identity plus exact smooth small-disk limit.**

Variable noise frames require the connection terms already audited elsewhere; this
section intentionally uses the constant uniform Navier--Stokes noise frame.

---

## 6. Three closed loops reconstruct the whole bulk viscous dissipation

Let `n_1,n_2,n_3` be any orthonormal frame of disk normals.  Then

\[
\sum_{j=1}^3 |(\nabla\omega)^Tn_j|^2
=|\nabla\omega|_F^2.
\]

Hence

\[
\boxed{
\frac12\sum_{j=1}^3\gamma_{\rm dens}(x,n_j)
=\nu|\nabla\omega(x)|^2.
}
\]

This identity is invariant under rotation of the loop-normal frame.

This is the first literal local bridge from the Kelvin future-variance/q.v. sector
to the deterministic vorticity PDE:

\[
\boxed{
\text{orientation-complete Kelvin microframe q.v.}
=
\text{bulk viscous enstrophy dissipation}.
}
\]

**Classification: Exact identity.**

---

## 7. A single selected loop can be physically blind

One loop normal only measures

\[
2\nu|(\nabla\omega)^Tn|^2.
\]

It does not reconstruct `nu |grad omega|^2`.  For example, with

\[
\nabla\omega=\operatorname{diag}(0,b,c),
\qquad n=e_1,
\]

one gets

\[
\gamma_{\rm dens}(e_1)=0,
\qquad
\nu|\nabla\omega|^2=\nu(b^2+c^2)>0.
\]

So if the restart bridge intends to read full viscous vorticity-gradient
information from Kelvin q.v., a rank-one orientation sample is insufficient.
It needs either

- an orientation-complete packet of three independent closed loops per physical
  germ, or
- a separately proved orientation-coverage mechanism that is exactly equivalent.

The full cross-covariance rule from the pair audit remains mandatory when such a
packet moves, refines, or resets.

**Classification: Rigorous structural consequence.**

---

## 8. Material-germ restart ledger

Let `D_t` be a material volume transported by the physical velocity `u`.
Incompressibility gives volume preservation, and Reynolds transport gives

\[
\frac d{dt}\int_{D_t} e
=\int_{D_t}(\partial_t+u\cdot\nabla)e.
\]

Using the local enstrophy equation and the microframe identity,

\[
\boxed{
\begin{aligned}
\frac d{dt}\int_{D_t}\frac12|\omega|^2
={}&\int_{D_t}\omega\cdot S\omega\\
&-\frac12\sum_{j=1}^3\int_{D_t}\gamma_{\rm dens}(n_j)\\
&+\nu\int_{\partial D_t}\nabla e\cdot n\,dS.
\end{aligned}
}
\]

This is the PDE-first restart ledger.  Nothing is hidden:

- advection disappeared because the observation region moves with the fluid, not
  because an estimate discarded it;
- pressure disappeared because curl made the exact gauge sector vanish;
- stretching is the actual producer;
- Kelvin microframe q.v. is the actual bulk viscous gradient payment;
- the remaining viscous contribution is the signed physical boundary flux.

**Classification: Exact Reynolds/Stokes consequence.**

---

## 9. A necessary local growth gate, not a continuation criterion

At a spatial local maximum of enstrophy,

\[
\Delta e\le0.
\]

Therefore the exact pointwise equation implies

\[
(\partial_t+u\cdot\nabla)e>0
\quad\Longrightarrow\quad
\boxed{
\omega\cdot S\omega>\nu|\nabla\omega|^2.
}
\]

Equivalently, using the microframe,

\[
\boxed{
\omega\cdot S\omega
>
\frac12\sum_j\gamma_{\rm dens}(n_j).
}
\]

Define only as diagnostic notation

\[
\mathfrak G
:=
\omega\cdot S\omega-\nu|\nabla\omega|^2.
\]

Positive material growth at a local enstrophy maximum requires `mathfrak G>0`.
The converse is false because the Laplacian flux can still be negative.

Thus this is a physically grounded **gate** for local peak growth, not a first-bad
threshold and not a continuation theorem.

**Classification: Rigorous necessary consequence of the exact PDE.**

---

## 10. Exact Navier--Stokes shear calibration

For

\[
u=(e^{-\nu k^2t}\cos ky,0,0),
\]

which is an exact smooth 3D periodic Navier--Stokes solution,

\[
\omega=(0,0,k e^{-\nu k^2t}\sin ky).
\]

The exact audit gives

\[
S\omega=0,
\qquad
\omega\cdot S\omega=0,
\]

and both the vorticity equation and local enstrophy residual vanish identically.

More revealingly, for the coordinate loop normals,

\[
\gamma_{\rm dens}(e_1)=0,
\qquad
\gamma_{\rm dens}(e_2)=0,
\]

while

\[
\gamma_{\rm dens}(e_3)
=2\nu k^4e^{-2\nu k^2t}\cos^2(ky).
\]

Thus two of three perfectly legitimate loop orientations are exactly blind even in
an exact Navier--Stokes solution.  The full microframe nevertheless reconstructs
`nu |grad omega|^2` exactly.

A second exact shear calibration prevents a subtler bookkeeping error.  Add a
constant Galilean velocity `U` in the `y` direction and translate the phase:

\[
u=(e^{-\nu k^2t}\cos(k(y-Ut)),U,0).
\]

This remains an exact Navier--Stokes solution with constant pressure.  Its
vorticity has nonzero physical advection,

\[
(u\cdot\nabla)\omega\ne0,
\]

while vortex stretching is still exactly zero,

\[
S\omega=0.
\]

The audit verifies the full vorticity and enstrophy equations exactly.  Thus
transport of vorticity and stretching of vorticity are distinct physical channels
and are tested as such.

**Classification: Exact Galilean Navier--Stokes calibration.**

**Classification: Exact Navier--Stokes calibration.**

---

## 11. Exact 3D ABC/Beltrami calibration

For

\[
u=e^{-\nu t}U,
\qquad
U=(\sin z+\cos y,\;\sin x+\cos z,\;\sin y+\cos x),
\]

one has the genuine 3D exact Navier--Stokes solution

\[
\omega=u,
\qquad
p=-\frac12|u|^2.
\]

The new audit verifies exactly:

- the vorticity equation residual is zero;
- the local enstrophy balance residual is zero;
- the microframe reconstruction residual is zero;
- at `(0,0,0)` the stretching power is nonzero:

\[
\omega\cdot S\omega=3e^{-3\nu t};
\]

- at the symmetric enstrophy maximum
  `(pi/4,pi/4,pi/4)`,

\[
\nabla e=0,
\qquad
\omega\cdot S\omega=0,
\]

while

\[
\nu|\nabla\omega|^2=3\nu e^{-2\nu t},
\]

\[
\nu\Delta e=-3\nu e^{-2\nu t},
\]

and therefore

\[
\partial_t e=-6\nu e^{-2\nu t}.
\]

This calibration prevents a false simplification: bulk Kelvin q.v. dissipation and
spatial/Hodge flux are distinct physical channels.  At the peak they contribute
equal negative amounts, while stretching vanishes.

**Classification: Exact 3D Navier--Stokes calibration.**

---

## 12. Shrinking loops force an area-squared renormalization

For a smooth small disk,

\[
a_i(Z_r)=A_r\bigl((\partial_i\omega)\cdot n\bigr)+o(A_r),
\]

so

\[
\boxed{
\gamma(Z_r)
=A_r^2\gamma_{\rm dens}(n)+o(A_r^2).
}
\]

If the linear scale is multiplied by `lambda`, area scales by `lambda^2` and raw
Kelvin action scales at leading order by

\[
\boxed{\lambda^4.}
\]

Therefore a finite raw loop bank does not by itself bound a local
vorticity-gradient density as the selector moves to smaller scales.
The restart-relevant object is the area-squared normalized density

\[
\widehat\gamma=\frac\gamma{A^2},
\qquad
\widehat V=\frac V{A^2}.
\]

**Classification: Exact affine law and exact smooth small-scale leading law.**

---

## 13. Moving scale creates exact dilation work

For the continuous selected-current covariance bank,

\[
\dot V=-\gamma+W_{\rm cov},
\]

where `W_cov` is the already audited signed covariance work of physical selector
motion.  If the selected germ area is itself changing, then

\[
\boxed{
\dot{\widehat V}
=-\widehat\gamma
+\frac{W_{\rm cov}}{A^2}
-2\frac{\dot A}{A}\widehat V.
}
\]

The last term is not stochastic production.  It is exact density amplification or
dilution caused by changing observational scale.  If `A` shrinks, the coefficient
`-2 A_dot/A` is positive.

This term belongs to shell/refinement/dilation geometry and must be tracked with
its sign.  It cannot be silently charged to `S^int`, and it cannot be removed by
saying the raw Kelvin bank is finite.

At a finite scale jump both the covariance reset identity and the change of
`A^{-2}` must be retained.

**Classification: Exact chain-rule identity.**

---

## 14. What this changes in the restart frontier

The previous frontier said only that repeated selector/localization work had no
uniform capacity bound near a candidate singular time.  The present audit now
identifies what a restart-capacity theorem would actually have to control.

For a shrinking first-bad germ it is not enough to control one raw selected Kelvin
variance.  One needs, at minimum,

1. **orientation completion**: a three-loop packet, or a proved equivalent coverage,
   so no vorticity-gradient direction is invisible;
2. **packet-metric normalization**: the full cross-orientation covariance contracted
   with `(H^T H)^(-1)`, not three independent diagonal normalizations once the
   material frame becomes non-orthogonal;
3. **connection typing**: the scalar `-2(A_dot/A)Vhat` law is retained as a coordinate
   identity, but the later GL(3) audit proves passive rotation/dilation/shear cancels
   when covariance and packet metric are transported together;
4. **signed physical boundary flux** from the material-germ enstrophy ledger;
5. **material metric work**: the later Nanson/flux audit identifies this exactly with
   vortex stretching rather than a separate positive zoom cost;
6. all previously audited covariance/reset/cross-shell/cross-child terms with their
   signs intact, plus the metric-amplified non-tensorial scale remainder.

The local gate

\[
\omega\cdot S\omega>\nu|\nabla\omega|^2
\]

is only a necessary condition for positive material growth at an enstrophy maximum.
It is **not** yet the first-bad threshold and is not sufficient for restart or
blow-up.

The next unresolved structural problem is therefore much sharper:

> Does the orientation-complete material packet admit a uniform local future-
> covariance tensor with controlled metric-amplified non-tensorial remainder, while
> its material metric-stretching work and physical boundary/exit terms are followed
> with their exact signs as the selected scale tends to zero?

That is the refined physical capacity question.  Only after this exact ledger is
closed is it appropriate to compress the result into a continuation norm or a
classical restart criterion.

**Classification: Rigorous reduction of the restart target; the capacity bound
itself remains a Conjectural bridge.**

No continuation/restart theorem and no regularity claim.


---

## 15. Orientation-complete material packet sharpens the restart geometry

The later packet audit replaces the orthonormal diagnostic microframe by a general
invertible material area frame `H=(h_1,h_2,h_3)`.  Its raw shared-noise q.v. matrix is

\[
\Gamma_H=2\nu H^T(\nabla\omega)(\nabla\omega)^TH,
\]

and the exact packet metric is

\[
M_H=(H^TH)^{-1}.
\]

Then

\[
\boxed{
\frac12\operatorname{tr}(\Gamma_HM_H)=\nu|\nabla\omega|^2
}
\]

for every invertible `H`, not only an orthonormal one.  This is essential because a
material packet obeys Nanson kinematics

\[
D_tH=-(\nabla u)^TH
\]

and generally becomes non-orthogonal.

For any raw packet covariance `C_H`, the metric-normalized scalar

\[
\mathcal B_H=\frac12\operatorname{tr}(C_HM_H)
\]

is invariant under passive `GL(3)` reparameterization.  Thus the earlier scalar
`-2(A_dot/A)V_hat` term is only a coordinate face of the full metric connection; a
passive zoom/rotation/shear does not create capacity when covariance and metric are
transported together.

If

\[
C_H=H^T\mathcal C H+R,
\]

the tensorial part gives exactly `tr(mathcal C)/2`; only

\[
\frac12\operatorname{tr}(R M_H)
\]

survives packet normalization.  Under isotropic linear scale `r`, `H_r=r^2H_0`, so
a raw remainder `r^pR_0` contributes exactly `r^(p-4)` after metric normalization.

Most importantly, material vorticity flux coordinates

\[
\Phi=H^T\omega
\]

obey the exact Navier--Stokes law

\[
\boxed{D_t\Phi=\nu H^T\Delta\omega.}
\]

Vortex stretching cancels from the flux equation and reappears as packet metric
work:

\[
\boxed{
\frac12\Phi^T\dot M_H\Phi=\omega\cdot S\omega.
}
\]

For flux covariance `C_Phi`, this polarizes to

\[
\frac12\operatorname{tr}(C_\Phi\dot M_H)
=\operatorname{tr}(S\Sigma_\omega),
\qquad
\Sigma_\omega=H^{-T}C_\Phi H^{-1}.
\]

Thus the restart obstruction is no longer accurately described as a positive
"dilation cost" plus a separate cubic stretching term.  Passive packet geometry
cancels; **material** metric deformation is the stretching channel itself.

**Classification: Exact packet/flux/metric identities.**

The remaining singular-time question is whether the future Kelvin covariance has a
uniform diagonal trace/remainder law for the now identified fixed-state local tensor,
whose signed physical transport, boundary, exit, material metric work, generator
descent, and causal time orientation remain controllable.

**Classification: Conjectural bridge.  No continuation/restart theorem and no
regularity claim.**

See `docs/orientation_complete_restart_packet.md` for the full packet audit.


---

## 16. Tensor enstrophy identity and future-covariance transfer

The scalar enstrophy equation is the trace of a stronger exact NS identity.  With
`E_omega=omega omega^T` and `A=grad u`,

\[
\boxed{
(\partial_t+u\cdot\nabla-\nu\Delta)E_\omega
=AE_\omega+E_\omega A^T
-\mathcal G_K,
\qquad
\mathcal G_K=2\nu(\nabla\omega)(\nabla\omega)^T.
}
\]

The tensor `mathcal G_K` is exactly the local orientation-complete Kelvin q.v.
tensor; pulling it back by an arbitrary area frame reproduces `Gamma_H`.

The full-state vector conditional-moment audit independently obtains the same tensor
as the carré-du-champ source of future covariance and as the diagonal defect of the
same-ancestor pair generator.  Double Stokes identifies its stored future tensor
with the diagonal density of `(d box d) mathbb K_s` when that trace is regular.

Conditional mean-square continuity of the random terminal vorticity field gives the
fixed-state local covariance tensor rigorously.  Centered conditional `C^2` packets
have raw remainder `O(r^6)` and normalized remainder `O(r^2)`.  These statements do
not provide uniform constants near a candidate singular time.

In the causal backward-Kelvin orientation, exact shear further verifies

\[
\mathfrak D_K C=+\mathcal G_K,
\qquad
\mathfrak D_K E_\omega=-\mathcal G_K,
\qquad
\mathfrak D_K(C+E_\omega)=0.
\]

Thus Kelvin q.v. is literally a tensor transfer between resolved mean-square and
conditional covariance.  The remaining obstruction is generator/time descent and
uniform singular-time control, not the existence of a fixed-state tensor.

**Classification: Exact NS tensor identity and exact backward-Kelvin calibration;
rigorous conditional fixed-state Stokes theorem.  No continuation/restart theorem.**

See `docs/future_covariance_tensor_audit.md`.


---

## Finite-loop generator correction: strain-gradient surface current

The infinitesimal Kelvin microframe is not the same object as a finite loop packet.
Under the uniform backward stochastic flow, relative loop shape has zero martingale
part, but a finite material spanning surface obeys

\[
\dot h_\Sigma=-(\nabla u(x))^T h_\Sigma
-\int_\Sigma[(\nabla u(y)-\nabla u(x))^Tn]\,dA.
\]

The second term is a physical finite-variation strain-gradient/surface-shape
current.  The exact NS shear `u=(y^3+6 nu t y,0,0)` gives equal-anchor equal-area
surfaces with different values of this current, so finite `(x,H)` generator descent
is false in general.  For centered scaled rectangles the residual is raw `r^4` and
relative-to-area `r^2`, matching the geometric order of the independently derived
centered future-covariance remainder without identifying the two physical terms.

**Classification: Exact material-surface identity and exact NS calibration.  Uniform
first-bad shape collapse remains open.**
