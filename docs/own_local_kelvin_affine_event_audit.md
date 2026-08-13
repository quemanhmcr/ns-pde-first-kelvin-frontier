# Own-local Kelvin affine event audit

The previous frame-aware refinement theorem is exact for residuals compared against a
single local vorticity target.  The persistent same-replica library, however, permits
packet-specific anchors.  This note derives the missing own-local event face directly
from the literal current/cochain identities before any norm or estimate.

## 1. Current and area still refine linearly

For child packet `i`,

\[
\varepsilon_i=K_i-H_i^T\omega_i,
\]

and for the parent,

\[
\varepsilon_P=K_P-H_P^T\omega_P.
\]

The physical current synthesis remains

\[
K_P=\sum_iR_iK_i,
\qquad
H_P^T=\sum_iR_iH_i^T.
\]

Substitution gives

\[
\boxed{
\varepsilon_P
=\sum_iR_i\varepsilon_i
+\Delta_\omega,
\qquad
\Delta_\omega
=\sum_iR_iH_i^T(\omega_i-\omega_P).
}
\]

The old linear error law is recovered exactly when all targets coincide, or when an
equivalent cancellation of `Delta_omega` is proved.

**Classification: Exact identity.**

## 2. Physical and codeforming events are affine

With

\[
r_i=H_i^{-T}\varepsilon_i,
\qquad
r_P=H_P^{-T}\varepsilon_P,
\]

and

\[
A_i=H_P^{-T}R_iH_i^T,
\]

one obtains

\[
\boxed{
r_P=\sum_iA_i r_i+d,
\qquad
d=H_P^{-T}\Delta_\omega.
}
\]

For coherent `H=cof L`,

\[
B_i=L_P^{-1}A_iL_i=\frac{J_i}{J_P}R_i,
\]

so

\[
\boxed{
\chi_P=B\boldsymbol\chi+d_\chi,
\qquad
d_\chi=\frac{1}{J_P}\Delta_\omega.
}
\]

Thus `A` and `B` remain the exact linear current/frame blocks, but they are not the
whole own-local residual event.

**Classification: Exact identity / exact scope correction.**

## 3. Reanchoring offset is a coboundary

Define the unreanchored reconstructed current/frame readout

\[
z=x+\Omega.
\]

A supplied physical current event acts linearly,

\[
z_+=Az_-.
\]

Therefore

\[
\boxed{x_+=Ax_-+d,
\qquad d=A\Omega_- - \Omega_+.}
\]

For two sequential events,

\[
d_1=A_1\Omega_0-\Omega_1,
\qquad
d_2=A_2\Omega_1-\Omega_2,
\]

and

\[
\boxed{A_2d_1+d_2=A_2A_1\Omega_0-\Omega_2.}
\]

The intermediate target cancels exactly.  The target face is therefore a physical
coboundary, not an arbitrary penalty or new source.

**Classification: Exact identity / rigorous functorial consequence.**

## 4. Second moment and selector jump retain affine faces

Pathwise,

\[
\boxed{
(Ax+d)(Ax+d)^T
=Axx^TA^T+Axd^T+dx^TA^T+dd^T.
}
\]

If a selector simultaneously changes from `E_-` to `E_+`, then

\[
\boxed{
\Delta Y=(E_+A-E_-)X+E_+d.
}
\]

Hence the optional jump-q.v. atom is the square of the full jump and contains the
linear/target cross faces plus the target dyad.  `A tensor A` remains the correct pair
functor of the linear block but is not the complete own-local affine moment event.

**Classification: Exact pathwise identity.**

## 5. Brownian response has the target-gradient coboundary

Let `N` denote the own-local residual response before the common factor
`sqrt(2 nu)`, and let `G` denote the corresponding local vorticity-gradient target
state.  The exact event law is

\[
\boxed{
N_+=AN_-+N_{\rm target},
\qquad
N_{\rm target}=AG_- - G_+.
}
\]

Therefore

\[
\begin{aligned}
N_+N_+^T={}&AN_-N_-^TA^T
+AN_-N_{\rm target}^T\\
&+N_{\rm target}N_-^TA^T
+N_{\rm target}N_{\rm target}^T.
\end{aligned}
\]

The two cross faces are signed.  The final face is PSD.  Their presence is forced by
the own-local target change, not by an estimate.

**Classification: Exact identity.**

## 6. Exact cubic heat-shear Navier--Stokes referee

Take

\[
u=(U,0,0),
\qquad
U(y,t)=y^3+6\nu ty.
\]

Then `u dot grad u=0`, constant pressure works, and

\[
U_t-\nu U_{yy}=0.
\]

The vorticity is

\[
\omega_z=-(3y^2+6\nu t).
\]

For a rectangular `xy` loop centered at `y=a`, with y half-width `b` and x-length
`ell`,

\[
K=2b\ell(-3a^2-b^2-6\nu t),
\qquad
H=2b\ell.
\]

Against target anchor `p`,

\[
\boxed{
\varepsilon_p=2b\ell(-3a^2-b^2+3p^2),
\qquad
Q_p=12b\ell(p-a).
}
\]

At the packet's own anchor `p=a`, `Q_a=0`.  Reanchoring the same current and frame to
`p=0` gives

\[
Q_0=-12ab\ell\neq0.
\]

Thus a pure target change with linear map `A=I` can change the continuous q.v. source.

For two symmetric children centered at `+a` and `-a`, each using its own target, but a
parent using target zero,

\[
\boxed{
\varepsilon_P-(\varepsilon_++\varepsilon_-)
=-12a^2b\ell\neq0.
}
\]

This is an exact smooth 3D Navier--Stokes no-go for extending the common-target linear
residual law to an own-local packet library.

**Classification: Audited exact-NS calibration / rigorous no-go consequence.**

## 7. What is closed and what remains open

Closed conditionally on supplied packet/current/frame/target event data:

- the linear block `A`/`B`;
- the own-local affine target offset;
- its exact composition law;
- its full pathwise second-moment faces;
- its selector interaction;
- its target-gradient Brownian response and Gram faces.

Still Open-literal:

- which NS-generated first-bad packet library and anchors are used;
- which physical event maps occur;
- the badness and resolve predicates;
- support locality/conditioning;
- endogenous event local finiteness versus interface/local-time calculus;
- the same-replica clock versus future-bank/restart clock identification.

No restart/continuation/global-regularity theorem is claimed.
