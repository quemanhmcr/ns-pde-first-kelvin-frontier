# Exact NS critical-sheet merger -> physical Kelvin packet event audit

This milestone starts from the literal 3D Navier--Stokes field and only then asks what
packet/event algebra the PDE actually supplies.  It does **not** assume that a
critical-sheet merger is already a packet refinement, selector jump, restart, or
continuation event.

## 1. Exact smooth Navier--Stokes merger mechanism

On the periodic three-torus take

\[
u=(U(y,t),0,0),\qquad
U=-e^{-\nu t}\sin y-\frac{e^3}{8}e^{-4\nu t}\sin 2y.
\]

The nonlinear term is identically zero because `u` has only an `x` component and is
`x`-independent.  Each Fourier mode satisfies the heat equation, so with constant
pressure this is an **exact smooth 3D Navier--Stokes solution**.

Its vorticity is

\[
\omega=(0,0,q),\qquad
q=e^{-\nu t}\cos y+\frac{e^3}{4}e^{-4\nu t}\cos 2y.
\]

Write

\[
r(t)=e^{3(\nu t-1)},\qquad t_*=\nu^{-1}.
\]

For `t<t_*`, in addition to the persistent `sin y=0` sheets, `q_y=0` has two side
sheets

\[
 y_\pm=\pi\pm d(t),\qquad \cos d=r(t).
\]

They merge into the persistent sheet `y=pi` at `t=t_*`.  On either side sheet, with
`alpha=e^{-nu t}`,

\[
q_{\rm side}=-\alpha\frac{2r^2+1}{4r},\qquad
\partial_{yy}e_{\rm side}
=-\alpha^2\frac{(2r^2+1)(1-r^2)}{4r^2}<0,
\]

and the transverse curvature tends to zero.  At the merger

\[
q_*=-\frac{3}{4e},\qquad
\partial_y e=\partial_{yy}e=\partial_{yyy}e=0,\qquad
\partial_{yyyy}e=-\frac{9}{4e^2}.
\]

The coordinate speed diverges, but `d |d_dot| -> 3 nu`; the velocity/vorticity field
itself remains an analytic finite Fourier polynomial.

**Classification: Exact identity / Audited calibration.**

## 2. A physical orientation-complete Kelvin packet library

A critical sheet fixes an anchor `a` in the `y` coordinate.  Attach a physical box
packet with line frame

\[
L=\operatorname{diag}(\ell,s,m),\qquad
H=\operatorname{cof}L
=\operatorname{diag}(sm,\ell m,\ell s).
\]

The `yz` and `zx` Kelvin loops have zero vorticity flux.  The `xy` loop is the
one-sided physical rectangle `y in [a,a+s]`, of `x`-length `ell`, so

\[
K_z=\ell\int_a^{a+s}q(y,t)\,dy.
\]

The packet target is its own local vorticity `omega(a,t)`.  Therefore

\[
\varepsilon=K-H^T\omega(a,t),\qquad
r=H^{-T}\varepsilon,\qquad
\chi=\varepsilon/\det L
\]

are literal finite-current quantities, not estimates.  The one-sided support is
intentional: at the merger the finite-current anchor-noise response is nonzero, so
the same-replica cross-block question is not vacuous.

At `a=pi,t=t_*`,

\[
r_z(s)=\frac{e^{-1}}{8s}\bigl(6s-8\sin s+\sin2s\bigr),
\]

and, because the critical target has `grad omega=0`, the target/local Brownian face
vanishes while the finite-current residual face is

\[
N_{zy}(s,m)=\frac{e^{-1}(1-\cos s)^2}{2sm}.
\]

**Classification: Exact identity.**

## 3. Fixed-shape translated packets really do coalesce

Choose one common `(ell,s,m)` and attach the same box construction to the central and
both side critical sheets.  Every packet component above is an analytic function of
`(a,t)` near `(pi,t_*)`.  Since

\[
(a_-(t),t),(a_+(t),t)\to(\pi,t_*),
\]

both side packet states converge to the central packet in

- support placement;
- line frame and area frame;
- all three Kelvin circulations;
- own-local target vorticity;
- raw, physical, and codeforming residual;
- target-gradient face;
- residual and full codeforming Brownian response.

Thus a **specified translation-covariant fixed-shape packet functor** has full
instantaneous physical packet-state coalescence at this exact NS merger.

The branch labels/ancestries do not become the same datum: the central branch
persists while the two side branches terminate.  Instantaneous state equality is not
an ancestry theorem.

**Classification: Rigorous consequence of the exact packet formulas and smooth NS limit.**

## 4. Scalar/critical coalescence does not force full packet coalescence

The PDE merger fixes `a=pi` and the local scalar/vorticity value.  It does **not** fix
`(ell,s,m)`.  Two perfectly admissible physical packet shapes at the same merged
sheet therefore give a direct counterexample.

Take `ell=m=1`, but `s_1=pi/2` and `s_2=pi/3`.  Their area frames already differ.  More
strongly,

\[
r_z(s_1)-r_z(s_2)
=\frac{e^{-1}}{16\pi}\bigl(-32+21\sqrt3\bigr)\ne0,
\]

and their nonzero anchor-noise coefficients also differ.

Hence

\[
\boxed{\text{critical position/enstrophy merger}
\not\Rightarrow\text{full Kelvin packet-state merger}.}
\]

Full coalescence is true only after a physical packet-library construction supplies
compatible support/frame/shape data.  This is a no-go against promoting the merger
geometry itself into a canonical library quotient.

**Classification: Rigorous consequence / exact NS counterexample.**

## 5. The physical event map for the instantiated branch-resolved library

Now impose the concrete rule **one fixed-shape packet per critical sheet**.  Before
the event the library has central/minus/plus blocks; after the event only the
persistent central critical sheet remains.  Branch geometry therefore supplies the
literal dimension-dropping event map

\[
A=E_0=[I\;0\;0].
\]

On the collision subspace `X_-=Sx`, `S=1_3 tensor I`,

\[
AS=I.
\]

All three local targets equal the merged target `omega_*`, and every critical anchor
has `grad omega=0`.  Therefore the already-audited own-local affine faces instantiate
as

\[
\boxed{d=A\Omega_- -\Omega_+=0},\qquad
\boxed{N_{\rm target}=A G_- -G_+=0}.
\]

The surviving finite-current noise is not zero for the one-sided packet; it is the
common physical packet noise `N_*` above.  Thus the event is not made linear by
ignoring reanchoring: the reanchoring and target-gradient coboundaries vanish here
for an exact physical reason, namely common collision target plus criticality.

**Classification: Exact identity on the instantiated physical library.**

## 6. Same-replica cross blocks at the collision

For the fixed-shape construction all three packet noise blocks converge to the same
nonzero `N_*`.  The common-Wiener library q.v. is therefore

\[
\Gamma_-=2\nu(SN_*)(SN_*)^T,
\]

so every diagonal **and cross-label** block equals `2 nu N_* N_*^T`.

For any normalized quotient

\[
C_w=[w_0I\;w_1I\;w_2I],\qquad \sum_iw_i=1,
\]

one has `C_w S=I` and exactly

\[
C_w\Gamma_-C_w^T=2\nu N_*N_*^T.
\]

Deleting the cross blocks gives instead the spurious factor `sum_i w_i^2`; for equal
weights it loses `2/3` of the true q.v. block.  Thus the earlier abstract collision
quotient algebra is now instantiated by a nonzero-noise exact NS packet library.

This does **not** mean the weights are physical merger dynamics.  They are gauge only
on the already-proved collision subspace.  The branch-resolved physical event above
selects the persistent central branch.

**Classification: Exact identity / Audited physical calibration.**

## 7. Endogenous selector/interface behavior in this exact merger

A label selector can switch from a side label to the central label at `t_*`.  The
projection matrix jumps, but on the collision subspace

\[
(E_0-E_\pm)Sx=0.
\]

So the selected **physical packet state has no finite jump** at the merger even if
the branch label changes.  This is a continuous interface, not a reset payment.

The interface is nevertheless not differentiably harmless.  For the one-sided
packet

\[
\partial_a r_z\big|_*
=\frac{e^{-1}(1-\cos s)^2}{2s}\ne0,
\]

while the side-sheet speed behaves like `3 nu/d`.  Hence the side packet approaches
the common state continuously but its branch derivative has a `1/d` singular face,
with

\[
d\,|\dot r_z|\to
3\nu\,\frac{e^{-1}(1-\cos s)^2}{2s}.
\]

The analytic NS field does not blow up; the singularity is in the critical-coordinate
parameterization of the packet branch.

This example has one isolated merger, so its supplied branch selector is locally
finite.  It does **not** settle general endogenous first-bad local finiteness or rule
out interface accumulation/local-time in another selector.

**Classification: Exact zero-jump interface identity / Audited calibration; general selector local finiteness remains Open-literal.**

## 8. Frontier after this milestone

Established:

- exact smooth periodic NS critical-sheet merger;
- exact physical finite Kelvin packet formulas at the merger;
- full instantaneous coalescence for a specified fixed-shape translated library;
- rigorous no-go: critical scalar/position coalescence alone does not force full
  packet-state coalescence;
- exact branch-resolved event map `A=E_0`, with `d=0` and `N_target=0` for physical
  collision/criticality reasons;
- exact nonzero same-replica cross-block quotient law;
- exact selector zero-jump at collision plus singular one-sided packet-branch rate.

Still **Open-literal**: identifying branch ancestry labels with the programme's
future/backward ancestry state; deriving the actual first-bad badness/resolve rule
from this critical-sheet mechanism; proving general endogenous selector local
finiteness.  Still **Open**: any restart/continuation/regularity consequence.

The geometric merger scale has not been identified with Kelvin diffusion scale here;
a shared square-root exponent, if later used, must be derived with its physical
coefficient and mechanism rather than promoted by analogy.

**No restart/continuation/regularity theorem claimed.**
