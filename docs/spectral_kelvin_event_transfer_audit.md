# Spectral Kelvin event-transfer audit

The earlier principal-channel audit deliberately refused to identify individual
eigenvector labels across a finite refinement/reset event.  The frame-aware residual
refinement audit now supplies the missing physical map

\[
r_P=\sum_i A_i r_i.
\]

This note asks the literal next question:

> what is the exact event law for parent spectral residual channels, without inventing
> an axis-to-axis ancestry map?

The answer is a signed projector-to-projector transfer law on the full ordered child
pair state.  It is regular at spectral degeneracy, retains cross-child and
cross-channel content, and makes individual principal-axis matching unnecessary.

---

## 1. Endpoint spectral projectors, not eigenvector labels

For each child `i`, let its physical line metric have spectral resolution

\[
M_i=\sum_\beta\lambda_{i\beta}P_{i\beta},
\qquad
\sum_\beta P_{i\beta}=I.
\]

The `P_{i beta}` are orthogonal spectral **projector blocks**.  Their ranks may be
larger than one at eigenvalue degeneracy.

Similarly,

\[
M_P=\sum_\alpha\lambda_{P\alpha}P_{P\alpha}.
\]

The exact parent residual channel is

\[
\boxed{
E_{P\alpha}
=\lambda_{P\alpha}\operatorname{tr}(P_{P\alpha}Q_P).
}
\]

No statement here labels a child eigenvector as the ancestor of a parent
eigenvector.

**Status: Exact spectral-projector typing.**

---

## 2. Frame-aware event synthesis acts before spectral readout

Let the exact physical event map from the frame-aware audit be

\[
r_P=\sum_i A_i r_i,
\qquad
A=[A_1\;\cdots\;A_N].
\]

For the full child residual second-moment library

\[
\mathbb Q=(Q_{ij})_{i,j},
\qquad
Q_{ij}=\mathbb E[r_i r_j^T],
\]

one has

\[
\boxed{
Q_P
=A\mathbb QA^T
=\sum_{i,j}A_iQ_{ij}A_j^T.
}
\]

This physical synthesis occurs before choosing any parent principal readout.

**Status: Exact identity inherited from frame-aware refinement.**

---

## 3. Exact projector event-transfer law

Insert the child projector resolutions on both sides of every pair block:

\[
Q_{ij}
=\sum_{\beta,\gamma}
P_{i\beta}Q_{ij}P_{j\gamma}.
\]

Therefore

\[
\boxed{
E_{P\alpha}
=\sum_{i,j,\beta,\gamma}
T_{\alpha;i\beta,j\gamma},
}
\]

where

\[
\boxed{
T_{\alpha;i\beta,j\gamma}
:=
\lambda_{P\alpha}
\operatorname{tr}
\left(
P_{P\alpha}
A_iP_{i\beta}
Q_{ij}
P_{j\gamma}A_j^T
\right).
}
\]

This is the literal finite-event **signed ordered child-pair traffic**.  Its indices have distinct physical meanings:

- `alpha`: parent spectral projector block;
- `i,j`: ordered child-current pair;
- `beta,gamma`: child spectral projector blocks inside that ordered pair.

The transfer is generally **signed**.  There is no positivity theorem for an
individual off-diagonal sector.

**Status: Exact identity.**

---

## 4. Four bookkeeping sectors, none disposable a priori

For auditing only, one may group the exact terms into four sectors:

1. same child / same channel index;
2. same child / different channel index;
3. different child / same channel index;
4. different child / different channel index.

Their sum is exactly `E_{P alpha}`.

The phrase “same channel index” is only bookkeeping.  It does **not** assert that
channel `beta` of two different children has the same physical axis.  The projector
formula itself carries the geometry.

Dropping sectors 2--4 is not justified by positivity, covariance centering, or
spectral diagonalization of the endpoint metrics.

**Status: Exact partition of the event-transfer identity.**

---

## 5. Parent total weighted energy is recovered exactly

Since

\[
M_P=\sum_\alpha\lambda_{P\alpha}P_{P\alpha},
\]

summing the parent channels gives

\[
\boxed{
\sum_\alpha E_{P\alpha}
=\operatorname{tr}(M_PQ_P).
}
\]

Thus projector event transfer is not a new bank.  It is the exact resolution of the
already-audited physical weighted residual energy into the parent spectral blocks.

**Status: Exact identity.**

---

## 6. Frame conversion activates genuine cross-channel traffic

Even if a child second moment is supported in one child principal direction, a
nontrivial frame-aware synthesis block `A_i` can feed a different parent projector.
For diagonal parent/child line metrics and an orientation permutation in the raw
packet map, the symbolic audit gives a nonzero transfer from the child `x` projector
to the parent `y` projector.

This is not eigenframe motion along a smooth material interval.  It is finite-event
physical frame conversion carried by `A_i`.

Therefore “channel content” is not transported by keeping the same spectral index.
The correct event object is the projector contraction above.

**Status: Audited exact algebraic calibration.**

---

## 7. Degeneracy is regular in projector variables

Suppose the parent metric has a repeated eigenvalue with canonical projector block

\[
P_{P,*}=P_{P,1}+P_{P,2}.
\]

The event-transfer formula uses only `P_{P,*}` and contains no spectral-gap
denominator.  It remains exact at the repeated eigenvalue.

Likewise, inside a degenerate child block one may choose two different orthonormal
rank-one resolutions.  The individual subterms change, but after summing all
subchannels in that block the transfer is invariant because both resolutions sum to
the same projector.

Hence

\[
\boxed{
\text{degenerate projector-block transfer is canonical},
}
\]

while individual eigenvector ancestry is gauge.

**Status: Exact projector-gauge identity / theorem-domain correction.**

---

## 8. Exact one-mode Navier--Stokes referee: signed cross-child traffic is active

Use the exact periodic one-mode Navier--Stokes shear from the selected-lineage audit
and the two half-period packets with opposite finite residuals

\[
\chi_1=-\chi_0\neq0.
\]

For a common `z` projector and parent synthesis `(I,I)`, the parent residual is zero.
The exact projector transfer resolves this as

\[
\boxed{
T_{\rm same\ child}=2|\chi_0|^2>0,
}
\]

and

\[
\boxed{
T_{\rm cross\ child}=-2|\chi_0|^2<0.
}
\]

The total parent channel is therefore

\[
\boxed{E_{P,z}=0.}
\]

The negative cross-child sector is not a technical covariance correction: it is the
literal physical cancellation produced by the exact NS current pair.

**Status: Audited calibration using an exact Navier--Stokes solution / rigorous
signed-sector necessity.**

---

## 9. No exact positive child-channel replacement

The previous calibration has strictly positive same-child diagonal contribution and
zero exact parent channel only because a negative cross-child term is retained.
Therefore the exact pair-resolved event law cannot be replaced by the diagonal
positive child-channel sum.

More generally, `T_{alpha;i beta,j gamma}` is a signed bilinear pair transfer, not a
Markov probability kernel.  A separate positive surrogate could be introduced for
some estimate, but it would be an additional mathematical object and would not be
the exact physical event lineage derived here.

**Status: Rigorous consequence of the exact signed transfer law; exact NS calibration
shows the obstruction is active.**

---

## 10. Correction to the cross-event principal-axis frontier

The earlier seam “cross-event principal-axis lineage” asked for something stronger
than the physics provides: a canonical matching of individual axes across an event.
That target is neither necessary nor invariant at degeneracy.

The exact replacement is now known:

\[
\boxed{
\text{endpoint spectral projector blocks}
+\text{ physical synthesis }A_i
+\text{ full pair state }Q_{ij}
\Longrightarrow
T_{\alpha;i\beta,j\gamma}.
}
\]

Thus the structural cross-event spectral transfer is closed once the physical event
map is supplied.  What remains Open-literal is the programme-specific event
instantiation (`R_i`, hence `A_i`) and the actual first-bad support/current state, not
an axis-matching theorem.

**Status: Rigorous structural correction; individual-axis ancestry is an audited noncanonical target, projector event transfer is exact.**

---

## 11. Updated hybrid first-bad channel law

A same-clock selected lineage can now be written without any fictitious axis matching:

- on smooth simple-spectrum intervals: stretch + content + eigenframe mixing;
- at smooth degeneracy: spectral projector blocks;
- at finite selector/refinement/reselection events: frame-aware `A_i` synthesis plus
  signed full projector-pair transfer;
- at pure selector reset: the previously audited geometry + left + right + quadratic
  pair faces;
- moving cut, physical exit, boundary-speed, and cross-clock ancestry faces remain
  separate.

The exact event transfer says how an already specified event acts on residual
channels.  It does not supply the actual first-bad event weights/maps, nor prove
support locality or channel collapse.

**Status: Rigorous conditional composition of exact same-clock identities.  Actual first-bad event-map instantiation remains Open-literal; selected-channel collapse and support locality remain Open.  No restart/continuation/regularity theorem claimed.**
