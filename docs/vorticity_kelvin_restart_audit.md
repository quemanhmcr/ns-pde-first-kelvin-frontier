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

1. **orientation completion**: three-loop microframe content, or a proved equivalent
   orientation coverage, so no vorticity-gradient direction is invisible;
2. **area-squared normalization**: the local density rather than the vanishing raw
   small-loop action;
3. **dilation work**: the exact `-2(A_dot/A) Vhat` term during shell migration;
4. **signed physical boundary flux** from the material-germ enstrophy ledger;
5. **vortex-stretching production** `omega·S omega`, the actual nonlinear source;
6. all previously audited covariance/reset/cross-shell/cross-child terms with their
   signs intact.

The local gate

\[
\omega\cdot S\omega>\nu|\nabla\omega|^2
\]

is only a necessary condition for positive material growth at an enstrophy maximum.
It is **not** yet the first-bad threshold and is not sufficient for restart or
blow-up.

The next unresolved structural problem is therefore much sharper:

> Can the orientation-complete, area-normalized Kelvin pair bank plus signed
> material-germ boundary flux control the cumulative time spent in the
> stretch-dominant gate as the selected scale tends to zero?

That is a physical capacity question.  Only after this exact ledger is closed is it
appropriate to compress the result into a continuation norm or a classical restart
criterion.

**Classification: Rigorous reduction of the restart target; the capacity bound
itself remains a Conjectural bridge.**

No continuation/restart theorem and no regularity claim.
