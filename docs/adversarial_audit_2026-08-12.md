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

Exact incompressible kinematic witness:

`F_r = diag(r^(-1), 1, r)`, `det F_r=1`.

A reference `r x r` material face can become a `1 x r^2` face. Its area is still `r^2 -> 0`, while its diameter stays order one. Thus `H -> 0` does not imply that the loop samples only an arbitrarily small neighborhood of the germ.

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

## Status

These findings do **not** provide a counterexample to the Kelvin programme or to any claimed regularity theorem (none is claimed here). They sharpen the restart bridge to require, simultaneously:

`uniform local covariance + support locality + metric-whitened remainder control + signed metric/boundary/exit accounting`.

---

## Draft PR #1 follow-up — clock, de Rham, covariance, and moving-cut findings

The open Draft PR #1 later extended this locality audit with four additional
compatibility findings.  They have now been independently checked against the
current theorem spine rather than accepted by provenance alone.

| Draft PR finding | Referee verdict on current main | Resolution |
|---|---|---|
| Physical time vs stochastic ancestry/backward clock | **Correct** | Same-clock conditional variance remains exact; physical first-bad lift is now explicitly two-clock and remains open-literal. |
| `d_pair V-gamma ds=d_spacetime V` | **Incorrect old main claim; PR objection correct** | Replaced by exact Dynkin/Fokker--Planck covariance current `partial_s(qV)+div(qjV+nu q K grad V)=-q gamma`. |
| Centered covariance carries deterministic stretching | **PR objection correct** | Current main already separates `mm^T`, `C`, `Q`, and `T_tot`; Kelvin q.v. is internal mean-square/covariance transfer. |
| Moving quantile/shell cut needs `Qdot` / boundary-speed face | **Correct** | Static spatial commutator retained, and distinct moving transport face `G_Q=Qdot+T_out Q-Q T_in` plus two-replica lift are now explicit; literal first-bad cut speed remains open. |
| Area shrinkage / metric-whitened locality | **Correct** | Already repaired by the support-local, metric-whitened packet theorem and coherent primal/dual geometry. |

The determinant caveat is also correct: the general 3D Nanson extension is
`D_t log det M_H=-4 div u`; the incompressible consequence used by the programme is
`D_t det M_H=0`.

See `docs/clock_cut_compatibility_audit.md` for the exact equations and regression
calibrations.

**Current status:** the Draft PR supplied valid adversarial pressure at several
proof-critical seams.  Its valid findings are now part of the main theorem spine;
the remaining two-clock and literal moving-cut constructions are deliberately left
open rather than patched by declaration.
