# Adversarial audit note — Kelvin packet locality

Date: 2026-08-12

Scope: independent re-derivation of the material Kelvin packet identities and an adversarial check of the local future-covariance restart bridge. This note is intentionally narrow.

## Confirmed backbone

The following identities re-derive directly from incompressible Navier--Stokes/Nanson algebra:

- `D_t(H^T omega) = nu H^T Delta omega` for the material area frame `D_t H = -(grad u)^T H`;
- with `M=(H^T H)^(-1)` and `Phi=H^T omega`, `(1/2) Phi^T (D_t M) Phi = omega.S.omega`;
- `(1/2) tr(2 nu H^T (grad omega)(grad omega)^T H M) = nu |grad omega|_F^2` for every invertible `H`;
- the same-ancestor pair branching difference leaves exactly the cross term `2 nu sum_mu D_mu^(1) D_mu^(2)`; first-order drift cancels.

No counterexample was found to these exact identities.

## Finding 1 — determinant-rate formula is domain-sensitive

`docs/orientation_complete_restart_packet.md` works throughout in the incompressible specialization and writes

`D_t log det M_H = 2 div u`.

Within that theorem domain this reduces to `0=0` and the used conclusion `D_t det M_H=0` is correct. It should not, however, be read as the general compressible Nanson formula. For a general 3D area frame,

`D_t H = [(div u) I - (grad u)^T] H`,

so

`D_t log det H = 2 div u`

and, since `M_H=(H^T H)^(-1)`,

`D_t log det M_H = -4 div u`.

**Downstream status:** no defect in the present incompressible route. Minimal wording repair: state only `div u=0 => D_t det M_H=0`, or explicitly label `-4 div u` as the general-Nanson extension.

## Finding 2 — shrinking area frame does not by itself imply a local packet

The conditional local future-covariance bridge needs spatial support shrinkage in addition to small area vectors.

Exact periodic Navier--Stokes witness: take the shear

`u_r(y,t)=(A_r e^(-nu k^2 t) cos(k y),0,0)`, `A_r=1/r`.

Its nonlinearity vanishes identically. The flow is

`X_t(x,y,z)=(x+B_r(t) cos(k y),y,z)`,
`B_r=A_r(1-e^(-nu k^2 t))/(nu k^2)`.

Start with an `r x r` material face in the `x-y` plane at `y_0=pi/(2k)`. Its image has tangent vectors `(1,0,0)` and `(-B_r k sin(k y),1,0)`, so its area remains exactly `r^2`, but its diameter is at least

`B_r sin(k r) -> (1-e^(-nu k^2 t))/(nu k) > 0`.

Thus there is no **uniform** implication over smooth periodic NS states from `H -> 0` to support locality. For one fixed pre-singular smooth solution the flow is locally Lipschitz and small supports remain small; the missing issue is precisely uniform control as a candidate singular time is approached.

A concrete smooth covariance witness is `W(x)=X cos(x_1) e_2`, with centered scalar `X`, `E X^2=1`. For the long-thin face

`Sigma_r=[-1/2,1/2] x {0} x [-r^2/2,r^2/2]`,

its area vector is `h_r=r^2 e_2 -> 0`, but

`int_{Sigma_r} W.n dA = 2 r^2 sin(1/2) X`,

whereas the local-center approximation gives `r^2 X`. Hence the covariance defect remains order `r^4` rather than `o(r^4)`.

**Minimal repair:** make locality explicit, e.g. require packet support diameter `->0` (or an equivalent material deformation bound) before invoking the small-loop covariance tensor expansion.

For an isotropic reference packet transported by an incompressible deformation, one useful diagnostic is

`sqrt(det H) / sigma_min(H) -> 0`,

which equals the largest transported line scale up to the fixed reference geometry.

## Remainder normalization

The scalar bank is

`2 B_H = tr(C_H (H^T H)^(-1)) = E |H^(-T) X_H|^2`.

Therefore a raw Frobenius condition such as `R_H=o(||H||^2)` is not sufficient for a highly anisotropic packet. The invariant smallness condition should control the metric-amplified remainder, for example

`tr(R_H (H^T H)^(-1)) -> 0`,

or at the payoff level `H^(-T) epsilon_H -> 0` in conditional `L^2`.

This is consistent with the repository's stated concern about a metric-amplified non-tensorial remainder; the point here is to make the required topology/norm explicit.

## Finding 3 — Doob evolution is parabolic, not an ordinary exact one-form

`docs/pair_localization_worldsheet_audit.md` writes

`A_cov = d_pair V - gamma ds = d_spacetime V`

from `D_s V=-gamma`, and then applies ordinary Stokes on a pair strip. This identification is not valid when `D_s` contains the diffusion generator.

The repository's own one-mode exact NS shear calibration gives, in remaining-time `tau`,

`partial_tau V - nu partial_a^2 V = gamma`.

With forward physical time `s=Theta-tau`,

`partial_s V = -gamma - nu partial_a^2 V`.

Hence the ordinary spacetime differential is

`d_spacetime V = d_a V - (gamma + nu partial_a^2 V) ds`,

not `d_a V-gamma ds`. At `a=0`, `gamma=0` while for every `tau>0`

`nu partial_a^2 V = 2 nu k^2 (e^(2 nu k^2 tau)-1)e^(-4 nu k^2 tau) > 0`.

So the claimed one-form equality already fails inside an exact calibration used by the repository. The same distinction also affects any use of `dot C=-Gamma` as an ordinary fixed-anchor time derivative: the exact identity is generator/covariant (`D_s C=-Gamma`), and the fixed-anchor derivative carries the diffusion term.

**Downstream status:** the fixed-current Doob/Itô bank and the distributed forward--backward balance remain valid. What is not justified is the de Rham-Stokes packaging of the second-order generator. Minimal repair: use Dynkin--Itô/Markov duality (or the already derived distributed covariance flux law) and derive the localization boundary terms there. A second-order generator cannot be treated as an exterior derivation without its carré-du-champ correction.

## Finding 4 — future covariance is not the deterministic rank-one flux tensor

The metric algebra is correct, but two different tensors are being placed next to each other. If `Y` is the terminal material flux vector, write

`m=E_s Y`, `C=Cov_s(Y)`, `Q=E_s[YY^T]=C+m m^T`.

Under the Kelvin representation the current deterministic flux is the conditional mean `m`, so with `omega=H^(-T)m`, literal vortex stretching is

`omega.S.omega = (1/2) m^T Mdot m`.

By contrast, the future-covariance bank carries metric work

`(1/2) tr(C Mdot) = tr(S Sigma_cov)`.

These are different terms. In particular at the terminal horizon `C=0` identically, while the repository's exact ABC calibration has `omega.S.omega=3 A^3 e^(-3 nu t) != 0` at `(0,0,0)`. Thus future-covariance metric work cannot itself be identified with literal deterministic vortex stretching.

**Minimal repair:** track the mean rank-one tensor `m m^T` separately, or pass to the full second moment `Q=C+m m^T` and derive its own evolution. The latter does not satisfy the same covariance-depletion law `D_s C=-Gamma`, so the two ledgers cannot be merged by notation alone.

## Status

These findings do **not** provide a counterexample to the Kelvin programme or to any claimed regularity theorem (none is claimed here). They sharpen the restart bridge to require, simultaneously:

`parabolic covariance transport + mean/covariance separation + support locality + metric-whitened remainder control + signed metric/boundary/exit accounting`.
