# NS PDE-first Kelvin Frontier

Standalone local Git repository for the PDE-first, structure-first 3D Navier--Stokes regularity research programme developed in this conversation.

## Research rule

Let the Navier--Stokes PDE and its physical/stochastic current structure act first. Before estimates, classify every term as one of: physical current/transfer, exact pressure or gauge form, connection/holonomy geometry, martingale quadratic variation/future variance, Hodge/spatial flux, ancestry deformation, quantile/localization covariance, physical exit, or observer artifact.

Every result must be labeled as **Exact identity**, **Rigorous consequence**, **Heuristic**, or **Conjectural bridge**. No regularity claim is allowed before the continuation/restart bridge is actually closed.

## Current frontier

The selected Kelvin quadratic variation has an exact fixed-current future-variance bank, but no selector-independent finite bank has been found at the present one-/two-ancestry level. The canonical same-ancestor pair branching tensor is the viscous diagonal tensor `2 nu q K delta_Delta`; drift traffic `q j_circ tensor j_circ` is a different physical object.

The surviving target is an exact **pair-localization current/capacity law** for the migrating first-bad germ.  The active selector has now been type-corrected: it acts on a library of closed Kelvin cycles, not on arbitrary ambient physical chains.  On this intrinsic domain its physical boundary residual and full-pair physical boundary residual vanish exactly; germ support transport is an exact cut-interface current, and finite hysteresis jumps are exact covariance revaluations.

For the cycle-typed selector sector the current identity has no intrinsic active-selector defect:

`Pi_sel - Pi_dist = boundary(pair localization world-sheet) + quantile + shell + physical exit + connection + reset`,

with full cross-shell and cross-child content retained inside the physical maps.  A further admissibility audit now shows that idempotency is not needed: any linear or differentiable CK operation that genuinely acts on Kelvin currents must preserve closed cycles, in which case it produces no intrinsic physical-boundary or pair-content defect when full pair content is retained.  If it breaks closedness, exact pressure gauge exposes a physical open boundary/interface/exit instead.  The literal global `S^int / Z_irr` equivalence remains open because `S^int` itself has never been defined line by line.

The restart frontier has now been tied back to the literal vorticity PDE and upgraded from one loop to an **orientation-complete three-loop packet**.  The full shared-noise packet q.v. is the `3 x 3` Gram matrix `Gamma_mf=2 nu N^T (grad omega)(grad omega)^T N`; exact ABC flow already has negative cross-orientation entries, so diagonal orientation bookkeeping is physically incomplete.  For a general invertible material area frame `H`, the scalar packet capacity `B=(1/2) tr(C (H^T H)^(-1))` is exactly GL(3)-invariant: passive rotation, anisotropic dilation, and shear cancel when full covariance is retained.  If raw covariance has local tensor form `C_H=H^T C_local H`, all packet geometry cancels and only `tr(C_local)/2` remains; a raw non-tensorial remainder `r^p R` at linear scale `r` is amplified exactly as `r^(p-4)`.  Material geometry is different from passive frame motion: Nanson kinematics and the NS vorticity equation give `D_t(H^T omega)=nu H^T Delta omega`, while material packet metric work recovers literal vortex stretching.  The exact amplitude-scaled ABC family also rules out instantaneous Kelvin bulk payment alone as a universal stretching bank.  The remaining open capacity problem is the uniform local future-covariance tensor/remainder law together with its signed material metric-stretching and physical boundary/exit terms near a candidate singular time.

See `docs/orientation_complete_restart_packet.md`, `docs/vorticity_kelvin_restart_audit.md`, `docs/cycle_typed_first_bad_selector.md`, `docs/kelvin_ck_admissibility_audit.md`, and `docs/selected_kelvin_pair_localization_budget.md`.

## Current audited refinement result

The pair-localization audit has now isolated an exact refinement rule: a linear
physical refinement `Z_P=sum_i a_i Z_i` must be lifted by the **full tensor square**
`sum_ij a_i a_j Z_i tensor Z_j`.  Cross-child covariance is physical refinement
content, not a Pillar-II defect.  Exact odd-mode periodic Navier--Stokes shear
calibrations in GitHub Actions witness complete cancellation between positive child
diagonals and negative cross-child covariance for the parent `Z_0+Z_pi`.

See `docs/pair_localization_worldsheet_audit.md`.
