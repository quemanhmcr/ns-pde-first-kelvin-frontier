# Intrinsic normalized-vorticity unit-ball contact grammar

This audit follows the scalar curvature-kernel milestone and asks the next literal
question: if `Q=-Hess(e/M)` is flat in a direction, should one descend an infinite
scalar jet hierarchy, or is scalar enstrophy already a quotient of a smaller
physical object?

The answer is that the scalar hierarchy is incomplete even in exact smooth
periodic Navier--Stokes.  The smaller endogenous object is normalized vorticity
itself.

No first-bad identification, restart, continuation, or regularity theorem is
claimed.

## 1. Normalize the vector, not only its norm

Let

\[
e=\frac12|\omega|^2,\qquad
M(t)=\max_x e(x,t)>0,
\]

and define

\[
W(t)=\sqrt{2M(t)}=\|\omega(\cdot,t)\|_{L^\infty},
\qquad
V=\frac{\omega}{W}.
\]

Then

\[
\boxed{|V(x,t)|\le1}
\]

at every point, and the previous scalar intrinsic field is simply

\[
\boxed{g=\frac eM=|V|^2.}
\]

Thus `V` is a similarity-neutral map from physical space into the closed unit
ball in vorticity space.  The active max set is the preimage of the unit sphere.

Under Navier--Stokes scaling, both numerator and denominator have vorticity
weight two, so `V` is exactly invariant.

**Classification: Exact definition / NS-similarity consequence.**

## 2. Exact normalized-vorticity PDE

The literal vorticity equation is

\[
D_t\omega=(\nabla u)\omega+\nu\Delta\omega.
\]

At every time where the scalar max envelope `M` (equivalently `W`) is differentiable, `W` is time-only and

\[
\boxed{
D_tV=(\nabla u)V+\nu\Delta V-\mu V,
\qquad
\mu=\frac{\dot W}{W}=\frac{\dot M}{2M}.
}
\]

This is more primitive than the scalar normalized-enstrophy equation.  Taking the
squared norm recovers it:

\[
D_t|V|^2
 =2V\cdot S V
 +\nu\Delta|V|^2
 -2\nu|\nabla V|_F^2
 -2\mu|V|^2.
\]

The antisymmetric part of `grad u` disappears only after taking the norm.  The
vector law retains the orientation information discarded by `g`.

**Classification: Exact local Navier--Stokes identity at differentiability times of the max envelope.**

## 3. Geometry at the active unit sphere

At an active maximum, `|V|=1` and `g=|V|^2` has a spatial maximum.  Therefore

\[
(\nabla V)^T V=\frac12\nabla |V|^2=0.
\]

Every first spatial derivative of `V` is tangent to the unit sphere.

Introduce the domain-direction gradient Gram

\[
G_R=(\nabla V)^T\nabla V\succeq0,
\]

the old scalar curvature

\[
Q=-\nabla^2|V|^2\succeq0,
\]

and the inward radial second-contact form

\[
\mathscr H_{ij}=-V\cdot\partial_{ij}V.
\]

Differentiating `|V|^2` twice gives the exact identity

\[
\partial_{ij}|V|^2
 =2\partial_iV\cdot\partial_jV
  +2V\cdot\partial_{ij}V.
\]

Hence

\[
\boxed{
\mathscr H=G_R+\frac12Q.
}
\]

There is no free coefficient in this sum.  It is forced by the Euclidean unit-ball
constraint satisfied by the actual normalized vorticity.

**Classification: Exact geometric identity.**

## 4. Contact-kernel completeness

At an active maximum, both terms on the right are positive semidefinite.  Thus for
any physical direction `xi`,

\[
\xi^T\mathscr H\xi
 =|\nabla_\xi V|^2+\frac12\xi^TQ\xi.
\]

Consequently

\[
\boxed{
\ker\mathscr H
 =\ker Q\cap\ker(\nabla V).
}
\]

This is the crucial reduction.  A `Q`-flat direction has two genuinely different
physical meanings:

1. normalized vorticity is also first-order flat there; or
2. normalized vorticity moves tangentially along the unit sphere even though its
   scalar norm is flat.

The second possibility is completely invisible to every scalar jet of `g` when
`|V|` stays identically one along the direction.  It is not invisible to the
vector contact form.

**Classification: Rigorous consequence of the exact contact identity and the
active-maximum PSD geometry.**

## 5. Kelvin q.v. is already the same gradient sector

Let

\[
G_L=(\nabla V)(\nabla V)^T.
\]

Since `omega=W V` and `W^2=2M`,

\[
\nabla\omega=W\nabla V.
\]

For the canonical orientation-complete Kelvin frame, the exact local q.v. tensor is

\[
\Gamma_I=2\nu(\nabla\omega)(\nabla\omega)^T.
\]

Therefore

\[
\boxed{
\Gamma_I=4\nu M G_L.
}
\]

The left and right Gram tensors are the two Gram faces of the same local noise
coefficient `grad V`.  In particular

\[
\operatorname{tr}G_L=\operatorname{tr}G_R=|\nabla V|_F^2,
\]

so the Kelvin bulk payment is

\[
\boxed{
\nu|\nabla\omega|_F^2
 =2\nu M\operatorname{tr}G_R
 =2\nu M\operatorname{tr}G_L.
}
\]

Thus the tangential part added by the contact grammar is not an invented penalty.
It is the domain-direction Gram of the same normalized gradient whose left Gram is
measured by orientation-complete Kelvin quadratic variation.

**Classification: Exact Kelvin/q.v.--normalized-gradient identity.**

## 6. Exact NS polarization family

Consider the periodic heat shear

\[
u(x,y,z,t)=\frac{a e^{-\nu k^2t}}{k}
\bigl(-\beta\cos kz,-\sin kz,0\bigr),
\qquad 0\le\beta\le1.
\]

Because the field depends only on `z` and has zero `z` component,

\[
(u\cdot\nabla)u=0,
\]

and each component solves the heat equation.  Hence this is literal smooth
periodic incompressible Navier--Stokes with constant pressure.

Its vorticity is

\[
\omega=a e^{-\nu k^2t}
       (\cos kz,\beta\sin kz,0).
\]

The exact max vorticity scale is

\[
W=a e^{-\nu k^2t},
\]

and therefore

\[
\boxed{
V=(\cos kz,\beta\sin kz,0).
}
\]

The unit-ball certificate is immediate:

\[
\boxed{
1-|V|^2=(1-\beta^2)\sin^2(kz)\ge0.
}
\]

For `beta<1`, `z=0 mod pi/k` is an active maximum.  At `z=0`,

\[
G_{R,zz}=\beta^2k^2,
\]

\[
Q_{zz}=2(1-\beta^2)k^2,
\]

while

\[
\boxed{
\mathscr H_{zz}=k^2
}
\]

for every `beta`.

Thus

\[
\boxed{
\beta^2k^2+(1-\beta^2)k^2=k^2.
}
\]

The same intrinsic contact curvature continuously reallocates itself between
scalar amplitude localization and tangential orientation motion.

**Classification: Audited exact-NS calibration.**

## 7. Two endpoints expose the scalar-jet no-go

### Linear polarization: `beta=0`

At the active maximum,

\[
G_R=0,
\qquad
Q=2k^2 e_z\otimes e_z,
\qquad
\mathscr H=k^2e_z\otimes e_z.
\]

The contact is carried entirely by amplitude curvature.

### Circular/helical polarization: `beta=1`

Now

\[
V=(\cos kz,\sin kz,0),
\qquad
|V|^2\equiv1.
\]

Hence

\[
\boxed{g\equiv1,\qquad Q=0,}
\]

and every spatial scalar jet of `g` vanishes identically.  The normalized scalar
source is also identically zero.

But

\[
G_R=k^2e_z\otimes e_z,
\qquad
\mathscr H=k^2e_z\otimes e_z,
\]

and

\[
\boxed{
\nu|\nabla\omega|_F^2
 =\nu a^2k^2e^{-2\nu k^2t}>0.
}
\]

Thus exact smooth periodic Navier--Stokes gives

\[
\boxed{
\text{all scalar normalized-enstrophy jets flat}
\not\Rightarrow
\nabla V=0
}
\]

and

\[
\boxed{
Q=0
\not\Rightarrow
\text{Kelvin gradient/q.v. sector is zero}.
}
\]

This directly refutes a universal strategy that tries to exhaust a `Q`-flat
direction by descending only higher scalar jets of `g`.

**Classification: Audited exact-NS no-go / rigorous insufficiency consequence.**

## 8. What has actually become smaller

The previous scalar grammar saw only

\[
g=|V|^2
\]

and its boundary curvature `Q`.  The vector lift shows that the apparent two-sector
complexity is generated by one normalized map `V` subject to one hard geometric
constraint `|V|<=1`.

At the active sphere, the exact contact identity

\[
\boxed{
-\,V\cdot\nabla^2V
=(\nabla V)^T\nabla V+\frac12Q
}
\]

unifies amplitude localization and orientation twisting.  The latter is already
the same local gradient coefficient that generates Kelvin q.v.

So the correct intrinsic question is no longer "which higher scalar derivative is
first nonzero?".  It is:

\[
\boxed{
\text{what does the normalized-vorticity PDE force on }
\ker\mathscr H?
}
\]

Only directions simultaneously invisible to scalar curvature and to the first
normalized-vorticity gradient survive into the next layer.

## 9. Classification and frontier

**Exact identity:** normalized-vorticity unit-ball map; at max-envelope differentiability times, exact vector PDE; squared
radius recovery of `g`; boundary tangency identity; contact split
`H_c=G_R+Q/2`; Kelvin q.v./left-Gram identity; left/right Gram trace equality.

**Rigorous consequence:** at an active maximum, `H_c` is PSD and
`ker H_c=ker Q intersect ker(grad V)`; scalar-curvature flatness alone is not full
physical flatness.

**Audited calibration:** the exact periodic elliptic-polarization heat-shear family
transfers contact continuously between amplitude curvature and orientation twist
while keeping `H_c,zz=k^2`.

**Audited no-go:** the helical endpoint has `g identically 1`, zero scalar source,
and all scalar spatial jets zero while normalized-vorticity gradient, contact, and
Kelvin bulk remain nonzero.

**Heuristic:** none promoted.

**Conjectural bridge:** none promoted.

**Open-literal:** no theorem identifies an actual first-bad state with loss of
coercivity of the unit-ball contact form; no theorem yet determines whether a
direction in `ker H_c` must be closed by higher vector contact, a material
symmetry, or another exact NS compatibility face.

**Open:** uniform singular-time support/refinement control, restart capacity,
continuation, and global regularity.

**No restart/continuation/regularity theorem claimed.**
