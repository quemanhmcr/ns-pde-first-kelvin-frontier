# Critical-sheet transport / Nanson / moving-cut audit

This milestone asks a stricter question than the previous fixed-shape merger audit.
Instead of rebuilding the same box shape at each critical sheet, let the Navier--Stokes
velocity gradient and the literal Kelvin/material transport tell us what a transported
packet can and cannot be.

The conclusion is a structural no-go, but it is also a simplification of the frontier:

> **the Eulerian critical-sheet path, the Kelvin ancestry path, and the transported
> packet geometry are three distinct physical objects.**

For the exact merger calibration they cannot be identified literally.  The correct
sheet-attached object is a moving-cut/reanchored readout, and its singular branch rate
is exactly the moving-boundary circulation flux.  A Nanson-consistent local frame also
retains a finite branch-history shear at the merger, so endpoint anchor/vorticity
coalescence does not erase ancestry geometry.

No first-bad rule is inferred from this example.  No restart, continuation, blow-up
exclusion, or global regularity theorem is claimed.

## 1. Start from the exact Navier--Stokes field

Use the same periodic three-dimensional heat shear

\[
u=(U(y,t),0,0),\qquad
U=-e^{-\nu t}\sin y-\frac{e^3}{8}e^{-4\nu t}\sin2y.
\]

It is an exact smooth NSE solution because the nonlinear transport term vanishes and
`U_t=nu U_yy`.  Its vorticity is

\[
\omega=(0,0,q),\qquad
q=e^{-\nu t}\cos y+\frac{e^3}{4}e^{-4\nu t}\cos2y.
\]

Let

\[
r(t)=e^{3(\nu t-1)},\qquad T=\nu^{-1}.
\]

Before `T`, the two side enstrophy critical sheets are

\[
a_-(t)=\pi-d(t),\qquad a_+(t)=\pi+d(t),\qquad \cos d=r.
\]

They merge into the persistent central sheet `a_0=pi` at `T` while the PDE field
remains analytic.

**Classification: Exact identity / Audited calibration.**

## 2. The critical sheets are not material sheets

The exact fluid velocity has

\[
u_y\equiv0.
\]

Hence every deterministic material trajectory preserves its `y` coordinate.  But

\[
\dot a_- = \frac{3\nu r}{\sqrt{1-r^2}},\qquad
\dot a_+ =-\frac{3\nu r}{\sqrt{1-r^2}},
\]

which is nonzero for every `t<T` and diverges as the merger is approached.
Therefore a packet whose anchor is constrained to a side critical sheet is not a
material packet.  Its anchor must continuously move through material labels with
normal reanchoring velocity

\[
V_{\rm cut}^{\perp}=\dot a_\pm e_y.
\]

This is not a coordinate convention.  It follows directly from comparing the
PDE-generated critical-sheet speed with the exact material velocity.

**Classification: Exact identity / Rigorous consequence.**

## 3. A literal stochastic Kelvin anchor is also not the critical path

The full common-noise Kelvin state already audited in the repository has one uniform
Brownian translation for the whole packet.  In particular its anchor has

\[
\frac{d[X_y]}{d\sigma}=2\nu,
\]

while the deterministic critical-sheet coordinate has zero quadratic variation in
this calibration.  Thus

\[
\boxed{\text{critical-sheet path}\neq\text{literal Kelvin ancestry anchor}}
\]

for positive viscosity.  Conditioning or projecting a Kelvin state onto a critical
sheet would be a new state/lift construction; it is not the original Kelvin process.
This removes one tempting ancestry identification rather than replacing it by an
unsupported one.

**Classification: Exact q.v. mismatch / Rigorous no-go for literal path identity.**

The broader programme ancestry state/lift remains **Open-literal**.

## 4. The local Nanson connection remembers the branch history

Although the sheet anchor is not material, one can still ask for the most literal
local deformation connection along that reanchored path.  In forward physical time
let

\[
\dot L=A(a(t),t)L,\qquad A=\nabla u.
\]

For the shear,

\[
A=(\partial_y U)E_{xy}=-qE_{xy},\qquad E_{xy}^2=0.
\]

Starting all branches from the same line frame at a common pre-merger time gives

\[
L_b(t)=(I+\gamma_b(t)E_{xy})L_{\rm init},\qquad
\dot\gamma_b=-q_b.
\]

The exact critical vorticities are

\[
q_0=-e^{-\nu t}+\frac14e^{3-4\nu t},
\]

and on either side sheet

\[
q_s=-\frac12e^{2\nu t-3}-\frac14e^{3-4\nu t}.
\]

Their difference has the rigid square factor

\[
\boxed{
q_s-q_0=-e^{-\nu t}\frac{(1-r)^2}{2r}<0
}
\qquad(t<T).
\]

Consequently, if

\[
\Delta\gamma=\gamma_0-\gamma_s,
\]

then

\[
\dot{\Delta\gamma}=q_s-q_0<0.
\]

So for **any common initialization time strictly before the merger**, equal initial
frames become unequal at `T`.  This is not a special choice of `t=0`; the sign is
fixed throughout the entire pre-merger interval.

For the explicit common identity initialization at `t=0`,

\[
\gamma_0(t)=\frac{1-e^{-\nu t}}{\nu}
-\frac{e^3(1-e^{-4\nu t})}{16\nu},
\]

\[
\gamma_s(t)=\frac{e^{-3}(e^{2\nu t}-1)}{4\nu}
+\frac{e^3(1-e^{-4\nu t})}{16\nu}.
\]

At `T=1/nu`,

\[
\Delta\gamma_*
=\frac1\nu\left[
(1-e^{-1})-\frac{e^{-1}-e^{-3}}4-\frac{e^3-e^{-1}}8
\right]<0.
\]

Numerically `nu Delta gamma_* ~= -1.9121097196`.

The line-frame comparison between the central and either side history is therefore

\[
J_{0\leftarrow s}=L_0L_s^{-1}
=I+\Delta\gamma_*E_{xy}\neq I,
\]

with `det J=1`.  The Nanson area comparison is

\[
\operatorname{cof}J_{0\leftarrow s}
=I-\Delta\gamma_*E_{yx}\neq I.
\]

The two side branches have the same frame history by symmetry, but the central branch
has a different one.

Thus the same endpoint `(a,T,omega)` can carry different transported frame/support
histories.

**Classification: Exact identity / Rigorous consequence / exact NS no-go against
endpoint-only full-state ancestry collapse.**

## 5. Nanson consistency is exact, but it does not make the packet material

For

\[
L=(I+\gamma E_{xy})\operatorname{diag}(\ell,s,m),
\]

the exact area frame is `H=cof L`.  Because the flow is incompressible,

\[
\dot H=-A^TH
\]

whenever `dot L=AL`.  So the local line/area pair is exactly Nanson-consistent.

Now examine a finite support point with relative transverse displacement `r_y`.
Define the finite nonaffinity

\[
N_a(r_y)=U(a+r_y,t)-U(a,t)-U_y(a,t)r_y.
\]

If the packet grid is both reanchored with the critical sheet and locally deformed by
Nanson, then

\[
\boxed{
V_{\rm grid}-u(a+r_y,t)
=-N_a(r_y)e_x+\dot a\,e_y.
}
\]

The two defects live in orthogonal physical directions in this exact shear:

- finite-support nonaffinity is an `x`-slip;
- critical-sheet reanchoring is a `y`-slip.

They cannot cancel.  On a side branch, even the anchor point `r_y=0` has nonzero
`y` slip.  Away from the anchor, the nonlinear finite shear also produces the
independent nonaffinity face.

This gives an exact physical decomposition of why a sheet-attached affine/Nanson
packet is not a material finite Kelvin current.

**Classification: Exact identity / Rigorous consequence.**

## 6. The transported support remembers more than the Kelvin residual fiber

At the merger take the sheared packet frame

\[
L_b=
\begin{pmatrix}
\ell&\gamma_b s&0\\
0&s&0\\
0&0&m
\end{pmatrix}.
\]

Its three oriented area vectors are the columns of `H=cof L`.  The `xy` area vector
remains `(0,0,ell s)`, while the `yz` area vector records the accumulated shear.
Because the exact vorticity is purely `z`-directed, the `yz` and `zx` circulation
components vanish and

\[
K_z=\ell\int_\pi^{\pi+s}q(y,T)\,dy
\]

is independent of `gamma`.

Therefore central and side transported endpoint packets satisfy

\[
K_0=K_s,\qquad \omega_0=\omega_s,
\]

and, for the own-local reconstruction,

\[
\varepsilon_0=\varepsilon_s,\qquad
r_0=r_s,\qquad
\chi_0=\chi_s,
\]

while simultaneously

\[
L_0\neq L_s,\qquad H_0\neq H_s.
\]

This is an exact smooth-NS witness that the current/residual fiber can coalesce while
physical support/frame geometry does not.  A selector switch can therefore be
zero-jump in the residual readout yet require a nontrivial support replacement in the
full physical state.

The earlier fixed-shape merger result is not contradicted.  It describes an
**instantaneously rebuilt Eulerian packet functor**.  The present result describes a
**history-carrying Nanson packet**.  They are different physical semantics and must
not be identified.

**Classification: Exact identity / Audited calibration / rigorous semantic no-go.**

## 7. The singular packet derivative is exactly a moving-cut circulation flux

For the one-sided sheet-attached `xy` loop,

\[
K(a,t)=\ell\int_a^{a+s}q(y,t)\,dy.
\]

The vorticity satisfies the exact heat equation `q_t=nu q_yy`.  Therefore the chain
rule plus Reynolds transport gives the literal two-face law

\[
\boxed{
\dot K
=\ell\nu\,[q_y(a+s)-q_y(a)]
+\ell\dot a\,[q(a+s)-q(a)].
}
\]

The first term is viscous diffusion through the fixed endpoints.  The second is the
moving-cut/reanchoring flux.  No estimate has been used.

At the merger anchor `a=pi`,

\[
q(\pi+s,T)-q(\pi,T)
=\frac{e^{-1}}2(1-\cos s)^2.
\]

The viscous face is finite:

\[
K_{\rm diff}'
=\ell\nu e^{-1}\sin s(1-\cos s).
\]

The critical-sheet speed is singular, and since `d |dot a| -> 3nu`, the moving-cut
face has the exact distance-weighted limit

\[
\boxed{
 d\,|K_{\rm cut}'|
\to
\frac{3\nu\ell e^{-1}}2(1-\cos s)^2.
}
\]

Dividing by the physical `xy` area `ell s` gives

\[
\frac{3\nu e^{-1}}{2s}(1-\cos s)^2,
\]

which is **exactly** the residual cusp coefficient found in the previous milestone.
Hence the previously observed `1/d` packet-rate singularity is not an unexplained
Kelvin singularity:

\[
\boxed{
\text{critical packet cusp}
=
\text{area-normalized moving-cut circulation flux}.
}
\]

The Navier--Stokes field and the viscous circulation face remain smooth.

**Classification: Exact identity / Rigorous physical identification.**

## 8. The singular selector speed has finite total variation

Each side cut is monotone and travels only the remaining geometric distance `d(t)`.
Thus from any `t_0<T`,

\[
\int_{t_0}^{T}|\dot a_\pm(t)|\,dt=d(t_0)<\pi.
\]

So this exact endogenous critical-sheet moving cut has a divergent instantaneous
speed but finite path variation.  Its circulation state is continuous at the merger;
there is no finite jump atom and no need for a local-time correction in this specific
calibration.

This does **not** prove local finiteness or finite variation for a general first-bad
selector.  It does show exactly what the interface law is when the selector is the
PDE-generated critical sheet of this NS solution.

**Classification: Exact identity / Audited calibration.  General endogenous selector
interface accumulation remains Open-literal.**

## 9. What bottleneck this resolves

The question was whether replacing the externally fixed-shape construction by
NS-driven transport would produce a canonical full packet merger.  The exact answer
is **no**, for two independent physical reasons:

1. the critical sheet is not a Kelvin/material trajectory, so sheet attachment is a
   moving-cut/reanchoring operation;
2. a Nanson-consistent local frame retains branch-history shear, and central versus
   side histories do not coalesce even when their endpoint anchor and vorticity do.

Therefore the programme should not try to prove

\[
\text{critical-sheet path}=\text{Kelvin ancestry path}
\]

or

\[
\text{endpoint critical merger}\Rightarrow
\text{history-carrying full packet merger}.
\]

The correct architecture is two-layered:

- **Kelvin/material ancestry state:** transported with its own common-noise/material
  kinematics and full shape/frame history;
- **Eulerian critical selector/readout:** a moving cut through that physical state,
  with Reynolds/reanchoring faces generated by the critical-sheet speed.

This is a real reduction of the search space: the missing ancestry bridge must be a
nontrivial readout/lift or conditional relation, not literal path equality.

**Classification: Rigorous architecture consequence from exact identities.**

## 10. Frontier after the milestone

### Exact identity

- side critical-sheet normal speed and material `u_y=0` mismatch;
- Kelvin-anchor q.v. rate `2nu` versus deterministic critical-path q.v. zero;
- branch Nanson histories and the strict square gap
  `q_side-q_central=-e^{-nu t}(1-r)^2/(2r)`;
- nontrivial merger frame/area history comparison;
- finite packet grid-slip split into nonaffinity plus normal reanchoring;
- exact moving-cut circulation Reynolds law;
- exact identification of the old residual cusp with moving-cut flux;
- finite total variation of this isolated side-sheet cut.

### Rigorous consequence

- a side-sheet-attached packet is not a genuine material Kelvin packet;
- the deterministic critical branch cannot literally be the stochastic Kelvin anchor;
- common pre-merger Nanson initialization does not yield central/side frame
  coalescence at the merger;
- residual/readout coalescence is insufficient for full history-carrying physical
  packet coalescence;
- critical-sheet selection and Kelvin ancestry require separate state semantics.

### Audited calibration

- the exact two-mode periodic heat shear realizes the full transport/reanchoring/
  Nanson/moving-cut mechanism above while remaining analytic.

### Heuristic

None promoted.

### Conjectural bridge

None promoted.

### Open-literal

- the actual programme first-bad badness/resolve functional;
- whether actual first-bad localization is an enstrophy critical-sheet selector;
- the nontrivial Kelvin-ancestry-to-Eulerian-selector lift/readout in the full
  programme state;
- general endogenous selector accumulation/local-time behavior;
- future-bank/cross-clock identification.

### Open

- uniform first-bad support/finite-shape collapse;
- restart capacity;
- continuation/global regularity.

**No continuation/restart/regularity theorem claimed.**
