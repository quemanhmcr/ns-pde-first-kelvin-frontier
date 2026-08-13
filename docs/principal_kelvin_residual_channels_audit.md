# Pathwise principal channels of the physical Kelvin residual

## Scope

The physical finite-to-local residual energy is

\[
\mathcal E
=\mathbb E[\chi^TM\chi],
\qquad
M=L^TL.
\]

The previous random-frame audit expressed this as a mean-metric/mean-second-moment
pairing plus a mandatory metric--residual correlation.  That decomposition is
exact, but it is not the only exact representation.  A more literal alternative
is to keep the physical metric **inside each realization** and resolve it by its
own spectral geometry before taking expectation.

This note derives that pathwise channel law and then differentiates it on a
simple-spectrum smooth segment.  No norm bound is introduced.  No first-bad
support theorem, future-bank identification, restart, continuation, or regularity
claim is made.

---

## 1. General spectral-projector law

For each realization, let the symmetric positive line metric have spectral
resolution

\[
\boxed{
M=\sum_\alpha \lambda_\alpha P_\alpha,
}
\]

where `P_alpha` are the orthogonal spectral projectors.  The index `alpha` runs
over distinct eigenspaces, not necessarily individual vectors.

For the residual second moment `Q`, pathwise

\[
\boxed{
\operatorname{tr}(MQ)
=
\sum_\alpha
\lambda_\alpha\operatorname{tr}(P_\alpha Q).
}
\]

Therefore the full random-state energy is

\[
\boxed{
\mathcal E
=
\mathbb E\sum_\alpha
\lambda_\alpha\operatorname{tr}(P_\alpha Q).
}
\]

This representation does **not remove geometry--residual correlation**.  It keeps
that correlation pathwise inside each product
`lambda_alpha tr(P_alpha Q)` rather than factorizing the ensemble into separate
mean geometry and mean residual tensors.

For positive semidefinite `Q`, every channel is nonnegative.  Because there are at
most three spectral blocks in 3D, the rigorous finite-sum consequence is

\[
\mathcal E_n\to0
\quad\Longleftrightarrow\quad
\mathbb E[\lambda_{\alpha,n}\operatorname{tr}(P_{\alpha,n}Q_n)]\to0
\text{ for every spectral block }\alpha,
\]

provided the blocks are followed in a well-defined measurable labeling/grouping.
The statement is about residual descent, not support locality.

**Status: Exact spectral-projector identity / rigorous nonnegative-channel consequence.**

---

## 2. Simple spectrum: three principal directional channels

When the spectrum is simple, write

\[
M=V\Lambda V^T,
\qquad
\Lambda=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3),
\]

with orthonormal principal vectors `v_i`.  Then

\[
\boxed{
E_i
=
\lambda_i v_i^TQv_i,
\qquad
\operatorname{tr}(MQ)=\sum_iE_i.
}
\]

For a random ensemble this formula is applied **replica by replica before
averaging**.  An exact two-replica referee confirms that the equal-weight sum of
pathwise channels equals the equal-weight physical energy even when the two
replicas have different eigenframes, eigenvalues, and residual tensors.

Thus one can carry the full geometry--residual correlation without introducing a
mean-metric closure.

**Status: Exact identity / random-frame physical typing.**

---

## 3. Moving simple-spectrum frame: exact connection

Let

\[
B=V^T\dot M V,
\qquad
\Omega=V^T\dot V.
\]

Orthogonality gives `Omega^T=-Omega`.  Differentiating
`M=V Lambda V^T` yields

\[
B
=
\dot\Lambda+\Omega\Lambda-\Lambda\Omega.
\]

Hence

\[
\boxed{
\dot\lambda_i=B_{ii},
}
\]

and, for `i != j`,

\[
\boxed{
\Omega_{ij}
=
\frac{B_{ij}}{\lambda_j-\lambda_i}.
}
\]

This is an **exact simple-spectrum identity**.  The denominator is physical: at a
repeated eigenvalue the individual principal vectors cease to be canonical.  The
implementation therefore rejects zero spectral gaps instead of silently emitting
a singular connection.

**Status: Exact identity conditional on simple spectrum.**

---

## 4. Residual tensor in the moving eigenframe

Let

\[
\widetilde Q=V^TQV.
\]

If `Qdot_0=V^T dot Q V` denotes the physical tensor rate expressed in the current
principal frame before differentiating the basis itself, then

\[
\boxed{
\dot{\widetilde Q}
=
\dot Q_0
+\widetilde Q\Omega-\Omega\widetilde Q.
}
\]

The commutator is not a new stochastic source.  It is the redistribution created
because the physical principal axes themselves rotate.

**Status: Exact moving-frame identity.**

---

## 5. Three traffic faces for every principal channel

For

\[
E_i=\lambda_i\widetilde Q_{ii},
\]

the exact derivative is

\[
\boxed{
\dot E_i
=
\underbrace{B_{ii}\widetilde Q_{ii}}_{\text{eigenvalue stretch/compression}}
+
\underbrace{\lambda_i(\dot Q_0)_{ii}}_{\text{residual/current content}}
+
\underbrace{\lambda_i[\widetilde Q,\Omega]_{ii}}_{\text{eigenframe mixing}}.
}
\]

These are three physically distinct local traffic faces:

1. the length-scale/eigenvalue of the principal material line changes;
2. the residual second moment itself receives q.v./current content;
3. the principal axes rotate, moving off-diagonal residual content through the
   directional ledger.

Summing all channels reproduces exactly

\[
\boxed{
\frac d{d\sigma}\operatorname{tr}(MQ)
=
\operatorname{tr}(\dot M Q)
+
\operatorname{tr}(M\dot Q).
}
\]

**Status: Exact simple-spectrum channel-rate identity.**

---

## 6. Eigenframe mixing is exactly off-diagonal metric work

In the principal frame,

\[
\boxed{
\sum_i
\lambda_i[\widetilde Q,\Omega]_{ii}
=
2\sum_{i<j}B_{ij}\widetilde Q_{ij}.
}
\]

The right-hand side is precisely the off-diagonal part of
`tr(B Qtilde)`.

Therefore eigenframe mixing is **not an additional physical source** sitting on
top of metric work.  It is the same off-diagonal metric work expressed as traffic
through moving principal axes.

This is an exact example of the project's guiding rule: keeping the complicated
moving geometry long enough reveals a smaller law rather than requiring a coarse
norm estimate.

**Status: Exact identity / physical source typing.**

---

## 7. Exact linear Navier--Stokes shear activates principal-axis mixing

Take the exact steady shear

\[
\boxed{u=(\gamma y,0,0).}
\]

Its nonlinear advection vanishes, its Laplacian vanishes, and constant pressure
solves Navier--Stokes exactly.

At an instant choose the coherent reverse line frame

\[
L=\operatorname{diag}(2,1,3),
\qquad
M=\operatorname{diag}(4,1,9).
\]

For

\[
A=
\begin{pmatrix}
0&\gamma&0\\
0&0&0\\
0&0&0
\end{pmatrix},
\]

the reverse material metric law gives

\[
\boxed{
B=\dot M
=
\begin{pmatrix}
0&-2\gamma&0\\
-2\gamma&0&0\\
0&0&0
\end{pmatrix}.
}
\]

The simple-spectrum connection is therefore

\[
\boxed{
\Omega_{12}=\frac{2\gamma}{3},
\qquad
\Omega_{21}=-\frac{2\gamma}{3}.
}
\]

If the residual second moment has `Qtilde_12=q`, then all diagonal eigenvalue
stretch faces vanish at this instant, but the two eigenframe-mixing channel faces
are nonzero and their sum is

\[
\boxed{-4\gamma q.}
\]

Direct off-diagonal metric work gives exactly

\[
2B_{12}\widetilde Q_{12}=-4\gamma q.
\]

Thus exact Navier--Stokes shear physically activates the axis-mixing traffic face;
it is not merely a coordinate artifact invented by the spectral calculation.

**Status: Audited calibration (exact Navier--Stokes).**

---

## 8. Degenerate spectrum: projectors are physical, individual axes are gauge

If two eigenvalues coincide, the formula

\[
\Omega_{ij}=B_{ij}/(\lambda_j-\lambda_i)
\]

must not be used.  The individual basis vectors inside that eigenspace are not
physically distinguished by `M`.

For a degenerate eigenspace with orthonormal basis matrix `W` and eigenvalue
`lambda`, the canonical channel is

\[
\boxed{
E_{\rm block}
=
\lambda\operatorname{tr}(W^TQW)
=
\lambda\operatorname{tr}(P Q),
\qquad P=WW^T.
}
\]

Under any orthogonal internal rotation `W -> W R`,

\[
\boxed{E_{\rm block}\text{ is unchanged}.}
\]

A rational `3-4-5` rotation referee gives zero residual exactly.  Thus the
spectral-projector representation remains regular at degeneracy even though the
simple-eigenvector connection does not.

**Status: Exact gauge identity / theorem-type domain correction.**

---

## 9. Placement relative to first-bad support

Pathwise spectral channels sharpen the weighted residual target:

\[
\boxed{
\mathcal E
=
\mathbb E\sum_\alpha
\lambda_\alpha\operatorname{tr}(P_\alpha Q).
}
\]

They do not replace physical support locality.  The earlier exact quadratic
long-support calibration already has one eigenvalue equal to `1` while the only
active residual channel is carried by an eigenvalue `rho^2`; weighted energy
vanishes but the packet is not local.

Therefore the literal first-bad problem still has two different questions:

- do all physical support directions localize/condition appropriately?
- do all nonnegative residual channel products vanish on that same random packet?

The channel representation does, however, remove one artificial bookkeeping
burden: one need not factor random geometry from random residual content in order
to state the physical descent target.  Their correlation remains inside each
pathwise channel automatically.

**Status: Rigorous reformulation of the open weighted-residual seam; support locality remains Open.**

---

## 10. Refined frontier

The local law under the finite-surface complexity is now especially small:

\[
\boxed{
E_\alpha
=\lambda_\alpha\operatorname{tr}(P_\alpha Q).
}
\]

On a simple-spectrum smooth segment each directional channel has only

\[
\boxed{
\text{eigenvalue stretch}
+
\text{residual content}
+
\text{eigenframe mixing}.
}
\]

The mixing sum is exactly off-diagonal metric work.  At degeneracy the individual
axes disappear and the eigenspace projector remains.  Across finite physical
events, the separate refinement/event ledger from the previous audit still
applies; these smooth spectral equations do not define event `Q_+`.

What remains open is to control these pathwise spectral channel products together
with actual support locality and all selected-current event faces near the
migrating first-bad state.  The same-clock channel energy is not a future-remaining
covariance bank and is not `S^int`.

There is **no restart/continuation/regularity theorem claimed** here.

**Status: first-bad principal-channel collapse Open; cross-clock/restart bridge
Open-literal/Open.**
