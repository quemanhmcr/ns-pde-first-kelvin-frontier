# Orientation-complete Kelvin packet and material-flux restart audit

This note advances the restart frontier from a single selected Kelvin loop to the
smallest orientation-complete physical object capable of seeing the full vorticity
gradient: a packet of three closed Kelvin loops attached to one physical germ.

The purpose is not to introduce a continuation norm.  It is to let the actual
Navier--Stokes vorticity equation, Stokes theorem, shared-noise covariance, material
surface kinematics, and packet geometry determine which terms are physical and
which are only observer/frame bookkeeping.

No first-bad threshold is declared.  No continuation/restart theorem or 3D
Navier--Stokes regularity claim is made.

---

## 1. The restart selector must select a germ packet, not one orientation

The earlier first-bad selector acts on a germ coefficient space through a rank-one
support projector `M_fb`.  For the restart extension, one physical germ carries
three closed Kelvin loops.  The coefficient space is therefore

\[
G_{\rm restart}=G_{\rm germ}\otimes\mathbb R^3_{\rm orient}.
\]

The orientation-complete selector is

\[
\boxed{
M_{\rm fb}^{\rm mf}=M_{\rm fb}\otimes I_3.
}
\]

If the packet cycle library is

\[
K_{\rm mf}:G_{\rm restart}\to C_1^{\rm phys},
\qquad
B_xK_{\rm mf}=0,
\]

then the selected restart packet is

\[
P_{\rm fb}^{\rm mf}=K_{\rm mf}M_{\rm fb}^{\rm mf}.
\]

Hence

\[
\boxed{B_xP_{\rm fb}^{\rm mf}=0}
\]

and the full ordered pair packet is closed on both physical boundary faces.

The CI witness uses two germs with three independent closed cycles per germ.  A
single first-bad germ selection has rank `3`, not rank `1`, and both one-current and
full-pair boundaries vanish exactly.

This does **not** replace the older scalar selected-circulation observable.  It is a
restart-layer extension forced by the vorticity-gradient audit: one orientation can
be physically blind.

**Classification: Exact type lift and exact boundary identity.**

---

## 2. The real orientation object is a full shared-noise q.v. matrix

Let the three unit loop normals be the columns of

\[
N=(n_1,n_2,n_3).
\]

For a small loop with area `A`, the area-normalized Kelvin coefficient in a constant
orthonormal noise frame is

\[
b_{ij}
=
(\partial_i\omega)\cdot n_j.
\]

The three loop martingales are driven by the **same** Brownian noise directions.
Therefore their instantaneous cross-variation is not a diagonal list.  It is the
Gram matrix

\[
\boxed{
\Gamma_{\rm mf}
=2\nu N^T(\nabla\omega)(\nabla\omega)^TN.
}
\]

Thus

\[
(\Gamma_{\rm mf})_{jk}
=2\nu\sum_i
[(\partial_i\omega)\cdot n_j]
[(\partial_i\omega)\cdot n_k].
\]

The diagonal entries are the previously audited one-loop densities.  The
off-diagonal entries are physical shared-noise covariance between different loop
orientations.

For an orthonormal frame `N`,

\[
\boxed{
\frac12\operatorname{tr}\Gamma_{\rm mf}
=\nu|\nabla\omega|_F^2.
}
\]

**Classification: Exact shared-noise Gram identity.**

---

## 3. Cross-orientation covariance is not optional

Under an orientation change `Q in SO(3)`,

\[
N\mapsto NQ,
\qquad
\boxed{
\Gamma_{\rm mf}\mapsto Q^T\Gamma_{\rm mf}Q.
}
\]

The trace is invariant, but the individual diagonal channels are not.  Their
correct transformation uses the off-diagonal entries.

The exact periodic Navier--Stokes shear

\[
u=(e^{-\nu k^2t}\cos ky,0,0)
\]

has a canonical packet q.v. matrix with only the third orientation active.  Rotating
in the `e_1-e_3` plane produces nonzero cross-orientation q.v.  If those cross terms
are deleted and the packet is rotated back, the original directional q.v. matrix is
not recovered.

Therefore diagonal orientation bookkeeping is not functorial even when the scalar
trace happens to survive an orthogonal rotation.

**Classification: Rigorous consequence from an exact Navier--Stokes calibration.**

---

## 4. Genuine 3D ABC flow already has negative cross-orientation q.v.

For the exact ABC/Beltrami solution

\[
u=e^{-\nu t}U,
\qquad
U=(\sin z+\cos y,\ \sin x+\cos z,\ \sin y+\cos x),
\]

at the symmetric enstrophy maximum

\[
(x,y,z)=(\pi/4,\pi/4,\pi/4),
\]

CI computes

\[
\boxed{
\Gamma_{\rm mf}
=\nu e^{-2\nu t}
\begin{pmatrix}
2&-1&-1\\
-1&2&-1\\
-1&-1&2
\end{pmatrix}.
}
\]

The cross-orientation entries are negative in the ordinary coordinate frame.  No
observer rotation created them.

The matrix has a null direction

\[
n_\Delta=\frac1{\sqrt3}(1,1,1),
\]

so

\[
\boxed{
n_\Delta^T\Gamma_{\rm mf}n_\Delta=0
}
\]

while

\[
\frac12\operatorname{tr}\Gamma_{\rm mf}
=3\nu e^{-2\nu t}>0.
\]

Thus even a genuine 3D exact Navier--Stokes state can have a perfectly blind loop
orientation together with nonzero bulk viscous vorticity-gradient dissipation.

**Classification: Exact 3D Navier--Stokes calibration.**

---

## 5. Material loop packets are not preserved as orthonormal frames

A restart packet carried by the fluid should not be forced to remain an orthonormal
observer frame.  Let

\[
H=(h_1,h_2,h_3)
\]

be the three oriented material **area vectors** of the infinitesimal loop surfaces.
The columns include both orientation and area.

For an incompressible material deformation, Nanson/cofactor kinematics gives

\[
\boxed{
D_tH=-(\nabla u)^TH.
}
\]

For one column `h=A n`, with `|n|=1`,

\[
\boxed{
\frac{D_tA}{A}
=-n\cdot S n.
}
\]

The skew part of `grad u` rotates the surface but does not change its area.  The
symmetric strain changes area.

Different area vectors generally acquire different rates and cease to be mutually
orthogonal.  Therefore three independent scalar normalizations `1/A_j^2` are only
correct while the normal frame remains orthogonal.

**Classification: Exact material-surface kinematics.**

---

## 6. The correct non-orthogonal packet metric

For an arbitrary invertible area frame `H`, the raw small-loop q.v. matrix is

\[
\boxed{
\Gamma_H
=2\nu H^T(\nabla\omega)(\nabla\omega)^TH.
}
\]

Define the packet metric

\[
\boxed{
M_H=(H^TH)^{-1}.
}
\]

Then

\[
\boxed{
\frac12\operatorname{tr}(\Gamma_HM_H)
=\nu|\nabla\omega|_F^2.
}
\]

This identity holds for every invertible `H`: rotated, anisotropically scaled,
sheared, or non-orthogonal.

For `H=ND` with `N` orthogonal and `D=diag(A_1,A_2,A_3)`,

\[
M_H=D^{-2},
\]

and the metric contraction reduces to the previously obtained sum of
area-squared-normalized diagonal densities.

For a non-orthogonal material packet, `M_H` is not diagonal.  Consequently the
off-diagonal cross-orientation covariance contributes even to the scalar bulk
reconstruction.

**Classification: Exact GL(3) packet identity.**

---

## 7. A GL(3)-invariant normalized covariance capacity

For any raw packet covariance matrix `C_H`, define

\[
\boxed{
\mathcal B(C_H,H)
:=\frac12\operatorname{tr}(C_HM_H).
}
\]

Under an invertible packet reparameterization

\[
H\mapsto HL,
\qquad
C_H\mapsto L^TC_HL,
\]

one has

\[
M_H\mapsto L^{-1}M_HL^{-T}
\]

and therefore

\[
\boxed{
\mathcal B(L^TC_HL,HL)=\mathcal B(C_H,H).
}
\]

This includes rotation, anisotropic area rescaling, and packet shear in one law.

The earlier scalar dilation term

\[
-2\frac{\dot A}{A}\widehat V
\]

is the isotropic-coordinate form of this geometry.  It is not by itself a positive
physical production term.

**Classification: Exact identity.**

---

## 8. Continuous packet connection law

Let

\[
\dot C_H=-\Gamma_H+W_H,
\]

where `Gamma_H` is the physical q.v. payment and `W_H` collects the already typed
signed covariance work/physical transport terms.  Then

\[
\boxed{
\dot{\mathcal B}
=-\frac12\operatorname{tr}(\Gamma_HM_H)
+\frac12\operatorname{tr}(W_HM_H)
+\frac12\operatorname{tr}(C_H\dot M_H).
}
\]

The three slots are distinct:

1. martingale q.v./future-covariance depletion;
2. physical covariance transport/work;
3. packet metric work.

If the apparent packet motion is only a passive coordinate change `Hdot=HR`, then

\[
\dot C_H=R^TC_H+C_HR
\]

and the induced covariance and metric terms cancel exactly:

\[
\boxed{\dot{\mathcal B}_{\rm passive}=0.}
\]

So pure orientation/scale/shear reparameterization is connection bookkeeping, not a
reservoir.

**Classification: Exact identity.**

---

## 9. Finite packet jumps have two signed faces

At a finite jump `(C^-,H^-)->(C^+,H^+)`, write

\[
M^\pm=((H^\pm)^TH^\pm)^{-1}.
\]

Then

\[
\boxed{
\Delta\mathcal B
=
\frac12\operatorname{tr}[(C^+-C^-)M^+]
+
\frac12\operatorname{tr}[C^-(M^+-M^-)].
}
\]

The first term is covariance reset measured in the new packet metric.  The second
is metric revaluation.

For a passive GL(3) jump

\[
H^+=H^-L,
\qquad
C^+=L^TC^-L,
\]

CI finds both signed faces can be nonzero while

\[
\boxed{\Delta\mathcal B=0.}
\]

This is the packet analogue of the earlier odd-shear reset lesson: a positive
one-sided reset/zoom cost is not invariant physical content.

**Classification: Exact identity.**

---

## 10. Local tensorial covariance makes all packet geometry disappear

Suppose, at one physical germ, the raw covariance is induced by a local physical
symmetric tensor `mathcal C`:

\[
\boxed{
C_H=H^T\mathcal C H.
}
\]

Then

\[
\boxed{
\mathcal B(C_H,H)
=\frac12\operatorname{tr}\mathcal C
}
\]

for every invertible packet geometry `H`.

Even if `H` changes arbitrarily in time,

\[
\boxed{
\frac d{dt}\mathcal B
=\frac12\operatorname{tr}\dot{\mathcal C}.
}
\]

All rotation, dilation, and shear of the packet cancel from the scalar capacity.

This has an important consequence: a perfectly tensorial smooth covariance field
can be followed through arbitrarily many dyadic shrinking refinements without
paying a positive scale cost.  CI checks this exactly for seven dyadic scales.

**Classification: Exact algebra conditional on the local tensor representation.**

Whether the **future Kelvin covariance** admits such a local tensor limit uniformly
as a candidate singular time is approached is not established here.

**Classification: Conjectural bridge for the singular-time future-covariance tensor
limit.**

---

## 11. The true scale obstruction is the non-tensorial remainder

Write

\[
C_r
=H_r^T\mathcal C H_r+R_r.
\]

The tensorial part is killed exactly by metric normalization.  The surviving scale
capacity is

\[
\boxed{
\mathcal R_r^{\rm cap}
=\frac12\operatorname{tr}(R_rM_{H_r}).
}
\]

For an isotropically shrinking linear radius `r`, an area frame scales as

\[
H_r=r^2H_0,
\qquad
M_{H_r}=r^{-4}M_{H_0}.
\]

If

\[
R_r=r^pR_0,
\]

then exactly

\[
\boxed{
\mathcal R_r^{\rm cap}
=r^{p-4}\mathcal R_0^{\rm cap}.
}
\]

Thus the area-squared threshold becomes a precise remainder threshold:

\[
\begin{array}{c|c}
p>4 & \text{normalized remainder vanishes},\\
p=4 & \text{finite nonzero scale contribution may survive},\\
p<4 & \text{metric amplification can diverge unless signed cancellation occurs}.
\end{array}
\]

This is a structural scale law, not yet a regularity criterion.

**Classification: Exact scaling identity.**

---

## 12. Material vorticity flux removes stretching from the flux equation

Define the material packet flux coordinates

\[
\boxed{
\Phi=H^T\omega.
}
\]

Using

\[
D_tH=-(\nabla u)^TH
\]

and the exact Navier--Stokes vorticity equation

\[
D_t\omega=(\nabla u)\omega+\nu\Delta\omega,
\]

we obtain

\[
\begin{aligned}
D_t\Phi
&=(D_tH)^T\omega+H^TD_t\omega\\
&=-H^T(\nabla u)\omega
+H^T(\nabla u)\omega
+\nu H^T\Delta\omega.
\end{aligned}
\]

Therefore

\[
\boxed{
D_t\Phi=\nu H^T\Delta\omega.
}
\]

The nonlinear vortex-stretching term cancels exactly in material flux coordinates.
For Euler, `nu=0`, the infinitesimal vortex flux packet is frozen.

This is not saying stretching disappears physically.  It moves into the material
metric converting flux coordinates back to physical vorticity amplitude.

**Classification: Exact Navier--Stokes material-flux identity.**

---

## 13. Vortex stretching is packet metric work

Because

\[
\Phi=H^T\omega,
\]

one has

\[
\boxed{
\omega=H^{-T}\Phi
}
\]

and

\[
\boxed{
|\omega|^2=\Phi^TM_H\Phi.
}
\]

Under Nanson material evolution,

\[
\dot M_H
=2H^{-1}SH^{-T}.
\]

Hence

\[
\boxed{
\frac12\Phi^T\dot M_H\Phi
=\omega\cdot S\omega.
}
\]

So literal vortex stretching is the metric deformation work of a material Kelvin
flux packet.

For a material flux covariance matrix `C_Phi`, define the physical vorticity
covariance

\[
\Sigma_\omega
=H^{-T}C_\Phi H^{-1}.
\]

Then the same identity polarizes to

\[
\boxed{
\frac12\operatorname{tr}(C_\Phi\dot M_H)
=\operatorname{tr}(S\Sigma_\omega).
}
\]

The deterministic rank-one case `C_Phi=Phi Phi^T` is exactly
`omega dot S omega`.

**Classification: Exact metric-stretching identity.**

---

## 14. Incompressibility preserves metric determinant, not metric shape

For a material area frame,

\[
M_H=(H^TH)^{-1}.
\]

The exact logarithmic determinant rate is

\[
\boxed{
D_t\log\det M_H=2\nabla\cdot u.
}
\]

Thus incompressibility gives

\[
\boxed{
D_t\det M_H=0.
}
\]

The metric can nevertheless become highly anisotropic.  Stretching therefore does
not require material-volume collapse; it redistributes metric eigenvalues while
their product remains fixed.

This gives a physical geometric restatement of the nonlinear danger: large
vorticity can arise when flux coordinates align with an expanding direction of the
material packet metric.

**Classification: Exact incompressible kinematic identity.**

---

## 15. Instantaneous Kelvin bulk payment alone cannot dominate stretching

Consider the amplitude-scaled exact ABC family

\[
u=Ae^{-\nu t}U.
\]

It remains an exact 3D Navier--Stokes solution because the Beltrami nonlinearity is
a pressure gradient.

At `(0,0,0)`, CI finds

\[
\omega\cdot S\omega
=3A^3e^{-3\nu t},
\]

while the orientation-complete instantaneous Kelvin bulk payment is

\[
\frac12\operatorname{tr}\Gamma_{\rm mf}
=3\nu A^2e^{-2\nu t}.
\]

Therefore

\[
\boxed{
\frac{\omega\cdot S\omega}
{\frac12\operatorname{tr}\Gamma_{\rm mf}}
=
\frac{Ae^{-\nu t}}{\nu}.
}
\]

At `t=0` this ratio is unbounded as `A->infinity`.

So there is no universal amplitude-independent pointwise inequality making the
instantaneous Kelvin bulk q.v. payment alone a stretching reservoir.

This does not rule out a future-covariance capacity with material metric work,
spatial flux, scale remainder, and the full first-bad packet geometry.

**Classification: Rigorous no-go consequence from an exact 3D Navier--Stokes
family.**

---

## 16. Conditional local future-covariance tensor bridge

There is a natural next object, but it must not be assumed.

If the random terminal transported momentum/vorticity field used by the Kelvin
representation is conditionally mean-square continuous at a germ, small-loop
Stokes convergence would give a local conditional covariance tensor
`mathcal C_s(x)` such that

\[
C_H^{\rm future}
=H^T\mathcal C_s(x)H+o(|H|^2)
\]

in the appropriate area-squared sense.

Then the orientation-complete local future bank would be

\[
\boxed{
\mathcal B_{\rm loc}(s,x)
=\frac12\operatorname{tr}\mathcal C_s(x)
}
\]

plus the metric-amplified non-tensorial remainder.

This would be exactly the scale-invariant packet object needed by the restart
programme.  But the uniform existence, generator compatibility, and singular-time
control of this tensor limit have not been proved.

**Classification: Conjectural bridge.**

---

## 17. Complete shrinking-scale excursion skeleton

For a piecewise-smooth first-bad restart packet, the exact continuous law is

\[
\boxed{
\dot{\mathcal B}
=-\mathcal P_{\rm K}
+\mathcal W_{\rm phys}
+\mathcal W_{\rm metric},
}
\]

where

\[
\mathcal P_{\rm K}
=\frac12\operatorname{tr}(\Gamma_HM_H),
\]

\[
\mathcal W_{\rm phys}
=\frac12\operatorname{tr}(W_HM_H),
\]

and

\[
\mathcal W_{\rm metric}
=\frac12\operatorname{tr}(C_H\dot M_H).
\]

At each finite reset/refinement/scale jump,

\[
\boxed{
\Delta\mathcal B
=\mathcal R_{\rm cov}+\mathcal R_{\rm metric}
}
\]

with the two signed faces from Section 9.

Internal passive GL packet changes cancel.  Perfect local-tensor scale refinement
also cancels.  What can survive a complete shrinking-scale excursion is therefore
restricted to:

1. physical Kelvin q.v./future-covariance depletion;
2. physical transport, shell/quantile, boundary, exit, and reset terms already
   classified in the pair world-sheet;
3. material metric work, whose deterministic rank-one form is vortex stretching;
4. metric-amplified non-tensorial covariance remainder;
5. any failure of the local future-covariance tensor limit itself.

There is no autonomous positive orientation/dilation/refinement payment left after
full covariance and metric geometry are retained.

**Classification: Exact algebraic excursion skeleton; singular-time capacity bound
remains open.**

---

## 18. Restart frontier after the packet audit

The restart problem is no longer accurately stated as

> control one selected Kelvin variance while its loop shrinks.

The structurally correct question is now:

> Does the material, orientation-complete first-bad packet admit a local future
> covariance tensor with a metric-amplified remainder that remains controllable,
> while its physical covariance depletion, boundary/exit terms, and material metric
> stretching work are followed with their exact signs up to the candidate singular
> time?

The packet audit removes several false obstructions:

- rank-one orientation blindness;
- diagonal-only cross-orientation truncation;
- positive zoom/dilation cost;
- positive refinement count;
- passive frame rotation/shear production.

It also identifies a genuine exact obstruction that cannot be wished away:
material metric stretching is the vortex-stretching channel itself, and the
amplitude-scaled ABC family shows instantaneous viscous packet payment alone cannot
universally dominate it.

The next mathematical target is therefore the **local future-covariance tensor and
its non-tensorial remainder current**, not another norm estimate.

**Classification: Rigorous structural reduction plus Conjectural bridge for the
future-covariance tensor limit.**

No continuation/restart theorem and no regularity claim.
