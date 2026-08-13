# Kelvin finite-event normal-form audit

The preceding audits progressively removed coordinate artifacts from finite Kelvin
residual refinement:

- raw orientation-current blocks `R_i`;
- physical reconstructed residual blocks `A_i`;
- codeforming blocks `B_i`;
- spectral projector event traffic.

This note asks whether these are independent layers of complexity or different
representations of one much smaller event law.

They are largely one law.  For invertible endpoint frames, the physical synthesis
block is a complete gauge-normal representative of the **linear raw current block**; sequential
events compose functorially on one-current state and on the full pair state; and any
intermediate spectral projector resolution telescopes out.  What does **not**
compose is a reduced list of diagonal scalar channel energies, because that list has
forgotten cross-channel coherence.

---

## 1. `A` is the complete physical normal form of a raw packet block

The exact frame-aware map is

\[
A=H_P^{-T}R H_C^T.
\]

Because the parent and child area frames are invertible,

\[
\boxed{
R=H_P^T A H_C^{-T}.
}
\]

Thus, once the physical endpoint frames are fixed, the correspondence

\[
\boxed{
R\longleftrightarrow A
}
\]

is bijective.

Under passive parent/child orientation coordinates,

\[
H_P\mapsto H_PS_P,
\qquad
H_C\mapsto H_CS_C,
\qquad
R\mapsto S_P^TRS_C^{-T},
\]

while `A` is unchanged.  Therefore `A` is precisely the physical representative of
the raw orientation-map gauge orbit.

**Status: Exact gauge-normal-form identity / exact bijection given invertible
endpoint frames.**

---

## 2. The codeforming block is an equivalent volume-normal form

For coherent line frames,

\[
B=L_P^{-1}AL_C
=\frac{J_C}{J_P}R.
\]

Since `J_P,J_C` are nonzero,

\[
\boxed{
R=\frac{J_P}{J_C}B.
}
\]

Hence `B` also determines the raw packet block once the endpoint volume factors are
known.

The physical and codeforming normal forms answer different questions:

- `A` acts on actual physical reconstructed vectors;
- `B` acts on each packet's own co-deforming residual coordinates.

Neither introduces additional physics inside that linear current block.  An own-local residual event can still carry an affine target/reanchoring coboundary not encoded by `A` or `B` alone.

**Status: Exact identity / exact bijection given invertible coherent frames.**

---

## 3. Sequential frame-aware events compose and the intermediate frame cancels

Let one event map child `C` to an intermediate packet `M`, and a second map `M` to
parent `P`:

\[
R_{MC},\qquad R_{PM}.
\]

The raw current map composes as

\[
R_{PC}=R_{PM}R_{MC}.
\]

The corresponding physical blocks are

\[
A_{MC}=H_M^{-T}R_{MC}H_C^T,
\]

\[
A_{PM}=H_P^{-T}R_{PM}H_M^T.
\]

Multiplying them gives

\[
\boxed{
A_{PM}A_{MC}
=H_P^{-T}R_{PM}R_{MC}H_C^T
=A_{PC}.
}
\]

The intermediate area frame cancels exactly.  There is no additional
“frame-transition residual”.

**Status: Exact composition identity.**

---

## 4. Codeforming event composition cancels the intermediate volume as well

The two codeforming blocks are

\[
B_{MC}=\frac{J_C}{J_M}R_{MC},
\qquad
B_{PM}=\frac{J_M}{J_P}R_{PM}.
\]

Therefore

\[
\boxed{
B_{PM}B_{MC}
=\frac{J_C}{J_P}R_{PM}R_{MC}
=B_{PC}.
}
\]

The intermediate determinant `J_M` cancels exactly.

Thus the codeforming event law is not merely local in each event: it is functorial
under sequential composition.

**Status: Exact identity.**

---

## 5. Full second moments compose with the one-current map

Let a first event be a possibly rectangular linear map `A_1` and a second event
`A_2`.  For a child second moment `Q`,

\[
Q_1=A_1QA_1^T,
\]

and then

\[
Q_2=A_2Q_1A_2^T.
\]

Associativity gives

\[
\boxed{
Q_2
=(A_2A_1)Q(A_2A_1)^T.
}
\]

No autonomous pair correction appears under event composition.

**Status: Exact identity.**

---

## 6. The pair functor itself composes exactly

After vectorization, one event acts by

\[
A\otimes A.
\]

For two events,

\[
\boxed{
(A_2\otimes A_2)(A_1\otimes A_1)
=(A_2A_1)\otimes(A_2A_1).
}
\]

Thus

\[
\boxed{
A\mapsto A\otimes A
}
\]

is an exact event functor.  The full ordered-pair state is not an extra layer that
must be repaired at every event; it is the tensor-square image of the actual
one-current map.

This does not allow diagonal-only reduction: tensor-square functoriality is exactly
what keeps cross-child and cross-channel sectors.

**Status: Exact identity.**

---

## 7. Intermediate spectral projectors telescope

Suppose the intermediate physical residual state has a complete spectral projector
resolution

\[
I=\sum_\beta P_{M\beta}.
\]

For a final parent projector `P_P` and eigenvalue `lambda_P`, the direct composite
channel is

\[
E_P
=\lambda_P\operatorname{tr}
\left[
P_P(A_2A_1)Q(A_2A_1)^T
\right].
\]

Insert the intermediate resolution on both sides of the intermediate second moment:

\[
\boxed{
E_P
=\sum_{\beta,\gamma}
\lambda_P\operatorname{tr}
\left(
P_PA_2P_{M\beta}A_1Q
A_1^TP_{M\gamma}A_2^T
\right).
}
\]

Summing every intermediate projector pair returns the direct composite channel
exactly.

Therefore an intermediate spectral decomposition is a valid exact resolution of
traffic, but it is **not additional ancestry data** that survives after all sectors
are summed.

**Status: Exact identity.**

---

## 8. Degenerate intermediate bases also telescope

If an intermediate eigenvalue is repeated, choose any orthonormal rank-one basis
inside that degenerate block.  Two such bases give different individual subterms,
but both resolutions sum to the same block projector.

Consequently their fully summed composite event transfer is identical:

\[
\boxed{
E_P^{(\text{basis A})}
=E_P^{(\text{basis B})}.
}
\]

So even inside a multi-event lineage there is no hidden need to transport
eigenvector labels through degeneracy.

**Status: Exact projector-gauge identity.**

---

## 9. A scalar channel list is not a compositional state

The exact projector traffic suggests a tempting reduction: keep only the diagonal
channel energies

\[
q_\alpha=\operatorname{tr}(P_\alpha Q)
\]

at each event.

That reduction is false universally.

Consider the two positive semidefinite intermediate second moments

\[
Q_+
=\begin{pmatrix}
1&1/2&0\\
1/2&1&0\\
0&0&0
\end{pmatrix},
\qquad
Q_-
=\begin{pmatrix}
1&-1/2&0\\
-1/2&1&0\\
0&0&0
\end{pmatrix}.
\]

They have identical diagonal projector channels:

\[
\boxed{(1,1,0).}
\]

But their cross-channel coherence has opposite sign.  Apply the same event map

\[
A=\begin{pmatrix}
1&1&0\\
0&1&0\\
0&0&1
\end{pmatrix}
\]

and read the parent `x` channel.  The symbolic audit gives two different parent
values, differing by exactly `2`.

Hence

\[
\boxed{
\text{same scalar channel list}
\not\Rightarrow
\text{same future event response}.
}
\]

The missing physical content is the signed cross-channel block of `Q`.

**Status: Audited algebraic counterexample / rigorous no reduced scalar-channel
closure consequence.**

---

## 10. Full symmetric second moment is complete for unrestricted linear event probes

The diagonal-channel counterexample shows what is lost by keeping only
`tr(P_alpha Q)`.  There is also an exact converse statement for the full symmetric
second moment.

Consider the unrestricted class of one-row linear event probes.  The coordinate
probe `e_i^T` reads

\[
q_i=e_i^TQe_i=Q_{ii}.
\]

The pair-sum probe `(e_i+e_j)^T` reads

\[
q_{ij}^{+}
=(e_i+e_j)^TQ(e_i+e_j).
\]

For a symmetric second moment, polarization gives

\[
\boxed{
Q_{ij}=\frac12\left(q_{ij}^{+}-q_i-q_j
ight).
}
\]

Therefore the coordinate probes and pair-sum probes reconstruct every entry of
`Q` exactly.  Equivalently, if two symmetric second moments give the same quadratic
response to all such linear event probes, they are identical.

This establishes a precise second-order completeness statement:

\[
\boxed{
	ext{full symmetric }Q
	ext{ is observationally complete for the unrestricted linear event-probe class}.
}
\]

It is not a claim that the actual first-bad packet family realizes every coordinate
or pair-sum probe.  The physically realized first-bad event class may be much
smaller, and no minimal-state theorem for that programme-specific class is proved.

**Status: Exact polarization identity / rigorous observational-completeness consequence conditional on the unrestricted linear event-probe class.  No actual first-bad probe-reachability or minimality claim.**

---

## 11. Event normal form modulo packet gauge

The structural finite-event lineage can now be compressed without losing physics:

\[
\boxed{
\begin{array}{c}
\text{raw orientation packet map }R\\
\text{mod passive parent/child packet bases}
\end{array}
\quad\longleftrightarrow\quad
\text{physical residual map }A.
}
\]

Sequential events compose by ordinary matrix multiplication,

\[
A_{n:0}=A_{n:n-1}\cdots A_{1:0},
\]

and the full pair state follows functorially via

\[
A_{n:0}\otimes A_{n:0}.
\]

Spectral projector decompositions may be inserted at any intermediate stage and
summed out exactly.  What cannot be discarded is the full second-moment coherence
needed by the next physical map.

This is the small rigid event law underneath selector/refinement frame complexity.

**Status: Exact normal-form/functoriality theorem for specified same-clock finite
linear packet events.**

---

## 12. What remains first-bad literal

The normal form does not choose the event.  The open physical questions are now
sharply separated from the event algebra:

1. which first-bad badness and resolve predicates are generated by Navier--Stokes;
2. which parent/child current packets and event maps `R` actually occur;
3. whether the event is scalar orientation-preserving, passive gauge, or a genuine
   packet-subspace/reselection change;
4. the moving quantile/shell spatial and time faces;
5. support locality/conditioning of the selected packet;
6. uniform control/collapse of the full selected projector-pair state, not merely
   its diagonal channel list;
7. the cross-clock future-bank/ancestry lift.

No item on this list is solved by the event normal-form identity itself.

**Status: first-bad event choice/state remains Open-literal/Open.  No restart/continuation/regularity theorem claimed.**


---

## 13. Affine own-local normal form

The gauge-normal theorem above is exact for the current/frame block.  If the packet residual uses packet-specific local vorticity targets, define the unreanchored readout `z=x+Omega`.  A supplied current event acts linearly on `z`, while the residual obeys

\[
\boxed{x_+=Ax_-+d,\qquad d=A\Omega_- - \Omega_+.}
\]

The homogeneous affine matrix `[[A,d],[0,1]]` composes exactly, and the intermediate target cancels.  Therefore the repaired physical event normal form is `(A,d)` on an own-local library, not `A` alone.  Because `d` is generally state-dependent/adapted, this pathwise lift is not an unconditional moment closure.

**Status: Exact affine extension; actual first-bad own-local event data remain Open-literal.**
