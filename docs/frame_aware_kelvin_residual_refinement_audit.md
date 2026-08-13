# Frame-aware Kelvin residual refinement audit

This note attacks the remaining refinement seam left by the selected principal
lineage audit.  The physical question is not whether one can invent a convenient
linear map on reconstructed residuals.  It is:

> if the orientation-complete **raw Kelvin packet** refines as an actual linear
> current packet, what map does Navier--Stokes/Kelvin geometry force after physical
> reconstruction and after codeforming pullback?

The answer is exact.  Whitening does not destroy refinement functoriality, but it
changes the child weights by the literal parent/child area frames.  Cofactor geometry
then removes all anisotropic frame conjugation from the codeforming residual and
leaves only determinant ratios and the raw orientation-current map.

No estimate is used below.

**Scope guard.** The linear residual synthesis derived in this note uses the same local vorticity target for parent and children.  Packet-specific own-local anchors require the affine target face derived in `own_local_kelvin_affine_event_audit.md`; the current/cochain theorem here is not revoked.

---

## 1. Raw orientation error is a current/cochain difference

For one orientation-complete packet write

\[
\varepsilon=K-H^T\omega,
\]

where `K in R^3` is the vector of the three closed-loop circulations and the columns
of `H` are the three oriented area vectors.

For a closed current `Z`, its oriented area vector can be written intrinsically as

\[
\boxed{
h(Z)=\frac12\oint_Z x\times dx.
}
\]

Hence both

\[
Z\mapsto \oint_Z u^\flat
\qquad\hbox{and}\qquad
Z\mapsto h(Z)
\]

are linear current readouts.  No spanning-surface ambiguity remains in the oriented
area vector: two surfaces with the same closed boundary give the same flux against
every constant divergence-free field.

Suppose an orientation-complete parent packet is an actual linear current synthesis
of child packets,

\[
Z_{P,a}
=\sum_{i,b}(R_i)_{ab}Z_{i,b}.
\]

Then linearity forces

\[
\boxed{
K_P=\sum_iR_iK_i,
\qquad
H_P^T=\sum_iR_iH_i^T.
}
\]

Therefore, for the **same local field** `omega`,

\[
\boxed{
\varepsilon_P
=K_P-H_P^T\omega
=\sum_iR_i\varepsilon_i.
}
\]

This is not an imposed residual rule.  It is the exact consequence of using the
same physical current synthesis on circulation and on its local oriented-area
readout.

**Status: Exact current/cochain identity for an orientation-complete linear current
packet refinement.**

The programme-specific question of which matrices `R_i` are realized by the actual
moving first-bad packet is separate and remains Open-literal.

---

## 2. Whitening forces the unique physical residual synthesis

For each child and parent define the reconstructed physical finite-face residual

\[
r_i=H_i^{-T}\varepsilon_i,
\qquad
r_P=H_P^{-T}\varepsilon_P.
\]

Insert the exact raw refinement law:

\[
\begin{aligned}
r_P
&=H_P^{-T}\sum_iR_i\varepsilon_i\\
&=\sum_iH_P^{-T}R_iH_i^T r_i.
\end{aligned}
\]

Thus

\[
\boxed{
r_P=\sum_iA_i r_i,
\qquad
A_i:=H_P^{-T}R_iH_i^T.
}
\]

The block `A_i` is **unique** if the identity is to hold for every child physical
residual: evaluating on a basis of `R^3` determines every column.

The important physical point is that unequal child/parent frames do not generally
permit the naive replacement `A_i=R_i`.  The area-frame conversion is part of the
actual observable.

**Status: Exact identity / exact uniqueness consequence.**

---

## 3. Independent orientation-basis changes leave `A_i` invariant

Let parent and child packet coordinates be passively reparameterized independently,

\[
H_P\mapsto H_PS_P,
\qquad
H_i\mapsto H_iS_i,
\]

with raw residual coordinates transforming as

\[
\varepsilon_P\mapsto S_P^T\varepsilon_P,
\qquad
\varepsilon_i\mapsto S_i^T\varepsilon_i.
\]

For the raw refinement relation to represent the same physical current map, its
block changes as

\[
\boxed{
R_i'
=S_P^TR_iS_i^{-T}.
}
\]

Then

\[
\boxed{
(H_PS_P)^{-T}R_i'(H_iS_i)^T
=H_P^{-T}R_iH_i^T
=A_i.
}
\]

So the frame-aware physical synthesis block is invariant under independent passive
parent/child orientation coordinates.

**Status: Exact gauge identity.**

---

## 4. Cofactor geometry turns frame conversion into a line-frame conjugation

For coherent invertible line frames,

\[
H_P=\operatorname{cof}L_P,
\qquad
H_i=\operatorname{cof}L_i,
\qquad
J_P=\det L_P,
\quad
J_i=\det L_i.
\]

Using

\[
H^T=J L^{-1},
\qquad
H^{-T}=J^{-1}L,
\]

one gets

\[
\boxed{
A_i
=\frac{J_i}{J_P}
L_PR_iL_i^{-1}.
}
\]

This is the literal physical conversion from child reconstructed residual vector to
parent reconstructed residual vector.

**Status: Exact cofactor identity.**

---

## 5. Codeforming coordinates cancel all anisotropic line-frame conjugation

Now write

\[
r_i=L_i\chi_i,
\qquad
r_P=L_P\chi_P.
\]

Then

\[
\begin{aligned}
\chi_P
&=L_P^{-1}\sum_iA_iL_i\chi_i\\
&=\sum_i\frac{J_i}{J_P}R_i\chi_i.
\end{aligned}
\]

Therefore the exact codeforming synthesis block is

\[
\boxed{
B_i:=L_P^{-1}A_iL_i
=\frac{J_i}{J_P}R_i,
}
\]

and the parent residual obeys the small rigid law

\[
\boxed{
\chi_P
=\sum_i\frac{J_i}{J_P}R_i\chi_i.
}
\]

This cancellation is stronger than a norm estimate.  The apparently complicated
parent/child anisotropic line-frame conversion is real in physical coordinates, but
it is pure frame geometry and disappears exactly after both sides are expressed in
their own codeforming coordinates.

**Status: Exact identity.**

---

## 6. Isotropic refinement exposes area weights versus volume weights

Let

\[
L_P=\rho_PI,
\qquad
L_i=\rho_iI,
\qquad
R_i=a_iI.
\]

Then

\[
\boxed{
A_i
=a_i\left(\frac{\rho_i}{\rho_P}\right)^2I,
}
\]

while

\[
\boxed{
B_i
=a_i\left(\frac{\rho_i}{\rho_P}\right)^3I.
}
\]

The physical reconstructed residual carries an **area ratio** because it descends
from orientation flux coefficients.  The codeforming residual carries a **volume ratio** because `epsilon=J chi`; this exact area ratio / volume ratio split is physical, not a normalization convention.

**Status: Exact scale identity.**

---

## 7. Exact quadratic Navier--Stokes calibration: naive scalar child weights fail

Use the exact heat shear

\[
u=(y^2+2\nu t,0,0)
\]

at anchor `y=0`.  For an isotropic asymmetric square packet of line scale `rho`, the
already-audited exact finite error is

\[
\varepsilon_z=-\rho^3,
\qquad
\chi_z=-1,
\qquad
r_z=-\rho.
\]

Take two child packets of scales `rho_1,rho_2` and form the literal orientation
current sum with scalar blocks `a_1I,a_2I`.  Current/area linearity gives

\[
H_P
=(a_1\rho_1^2+a_2\rho_2^2)I.
\]

Hence

\[
\boxed{
r_{P,z}
=-\frac{a_1\rho_1^3+a_2\rho_2^3}
        {a_1\rho_1^2+a_2\rho_2^2},
}
\]

not

\[
-a_1\rho_1-a_2\rho_2
\]

generically.

If `rho_P^2=a_1rho_1^2+a_2rho_2^2`, then

\[
\boxed{
\chi_{P,z}
=-\frac{a_1\rho_1^3+a_2\rho_2^3}
        {(a_1\rho_1^2+a_2\rho_2^2)^{3/2}}.
}
\]

The symbolic audit derives the same expressions from the frame-aware and determinant
weighted synthesis maps.

**Status: Audited calibration using an exact Navier--Stokes solution / rigorous
no-naive-weight consequence.**

---

## 8. Full pair functor survives frame-aware reconstruction

Stack the child physical residuals into one library vector and set

\[
A=[A_1\;\cdots\;A_N].
\]

For the full child second-moment matrix `mathbb Q_r`,

\[
\boxed{
Q_{r,P}=A\mathbb Q_rA^T.
}
\]

Therefore

\[
\boxed{
\operatorname{vec}Q_{r,P}
=(A\otimes A)\operatorname{vec}\mathbb Q_r.
}
\]

Equivalently,

\[
\boxed{
Q_{r,P}
=\sum_{i,j}A_iQ_{ij}A_j^T.
}
\]

The corresponding parent spectral channel is

\[
\boxed{
E_{\alpha,P}
=\lambda_{P,\alpha}
\sum_{i,j}
\operatorname{tr}
(P_{P,\alpha}A_iQ_{ij}A_j^T).
}
\]

Thus frame conversion does not create a new covariance defect and does not license a
diagonal-child projection.  Cross-child content is still mandatory; only the
physical contraction blocks have changed.

In codeforming coordinates the same theorem uses

\[
B=[(J_1/J_P)R_1\;\cdots\;(J_N/J_P)R_N]
\]

and `B tensor B`.

**Status: Exact pair-functor consequence.**

---

## 9. Canonical lift of the repository's scalar current refinement

The existing pair-worldsheet refinement already contains the literal scalar current
identity

\[
Z_P=\sum_i w_i Z_i
\]

and its full ordered pair coefficients `w_i w_j`.

If the three orientation channels are refined without rotating/mixing the orientation
fiber, there is no additional choice: the orientation-complete blocks are

\[
\boxed{R_i=w_i I_3.}
\]

Consequently

\[
\boxed{
R_i\otimes R_j=w_iw_j I_9,
}
\]

which is exactly the orientation-complete lift of the previously audited scalar
refinement pair coefficients.

The same statement holds for the literal chain subdivision map.  If

\[
B_fR_1=R_0B_c,
\]

then tensoring with the independent orientation fiber gives

\[
\boxed{
(B_f\otimes I_3)(R_1\otimes I_3)
=(R_0\otimes I_3)(B_c\otimes I_3).
}
\]

Thus scalar orientation-preserving current refinement is already an exact
orientation-complete packet refinement class in the repository.  For this class,
the codeforming child block is explicitly

\[
\boxed{
B_i=w_i\frac{J_i}{J_P}I_3.
}
\]

**Status: Exact type lift of the existing scalar current/chain refinement and exact
pair-functor compatibility.**

This does not prove that every moving first-bad event is orientation preserving.  A
physical reselection may rotate or mix the three packet currents; such an event needs
its actual matrix `R_i`, not an invented scalar surrogate.

---

## 10. What has actually been closed, and what has not

The previous frontier phrase “physical residual refinement lift” was too broad.  It
contained two logically different questions.

### 10.1 Closed structural lift

Once an orientation-complete linear current packet refinement is supplied **and the residuals are referenced to one common local target (or have already been reanchored to one)**, the
chain/current readouts force

\[
K_P=\sum_iR_iK_i,
\qquad
H_P^T=\sum_iR_iH_i^T,
\]

and the physical/codeforming residual refinement follows uniquely:

\[
\boxed{
A_i=H_P^{-T}R_iH_i^T,
\qquad
B_i=(J_i/J_P)R_i.
}
\]

No further residual-refinement ansatz is needed.

**Status: Rigorous consequence of the exact current/cochain and whitening/cofactor
identities.**

### 10.2 Remaining literal first-bad instantiation

The repository still has not written, for the actual migrating first-bad packet,
which orientation-complete parent/child closed-current triples occur at each physical
refinement/reselection event and therefore which matrices `R_i` the current map
induces there.

That is now the surviving refinement seam:

\[
\boxed{
\text{first-bad orientation-complete packet refinement-map instantiation}.
}
\]

It is a current-geometry question, not a missing whitening theorem.

**Status: Open-literal.**

---

## 11. Refined selected-lineage law

If a first-bad event supplies the actual orientation packet blocks `R_i` **and a common target/reanchoring has been established**, then the linear residual state map is no longer free:

\[
\boxed{
\chi_P=B\boldsymbol\chi,
\qquad
B=[(J_i/J_P)R_i]_i,
}
\]

and

\[
\boxed{
Q_{\chi,P}=B\mathbb Q_\chi B^T.
}
\]

The finite event ledger from the previous audit can therefore use the full
`B tensor B` state revaluation, while the endpoint line metric and spectral
projectors determine geometry and principal-channel readout.  Moving cut, physical
exit, and clock faces remain separate.

This is a substantial narrowing, but it is **not** a first-bad collapse theorem.
Nothing here proves that selected support shrinks, that the nonnegative projector
channels vanish uniformly, or that a future covariance/ancestry bank has been
identified.

**Status: Exact/rigorous conditional refinement law; first-bad packet-map
instantiation Open-literal.  No restart/continuation/regularity theorem claimed.**

---

## 12. Own-local anchor correction

For packet-specific targets `omega_i` and parent target `omega_P`, current/area linearity gives instead

\[
\varepsilon_P=\sum_iR_i\varepsilon_i+\sum_iR_iH_i^T(\omega_i-\omega_P).
\]

Thus the physical/codeforming event is affine.  The exact target coboundary, its selector interaction, continuous-source gradient face, and exact cubic heat-shear Navier--Stokes referee are derived in `own_local_kelvin_affine_event_audit.md`.

**Status: Exact scope correction.  The common-target linear theorem survives; own-local first-bad target/event instantiation remains Open-literal.**
