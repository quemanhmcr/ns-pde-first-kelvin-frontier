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

The restart frontier has now been tied back to the literal vorticity PDE.  In a constant orthonormal noise frame, three orthogonal infinitesimal closed Kelvin loops reconstruct the bulk viscous enstrophy dissipation exactly: `(1/2) sum_j gamma_dens(n_j) = nu |grad omega|^2`.  A single loop orientation can be exactly blind, and raw small-loop q.v. scales like area squared; therefore any restart bridge based on Kelvin q.v. needs orientation completion plus area-squared renormalization.  Continuous scale motion creates an exact signed dilation term `-2 (A_dot/A) V_hat`.  The remaining open capacity problem is to control vortex-stretching production against the orientation-complete normalized Kelvin bank together with signed spatial boundary and dilation work as scale tends to zero.

See `docs/vorticity_kelvin_restart_audit.md`, `docs/cycle_typed_first_bad_selector.md`, `docs/kelvin_ck_admissibility_audit.md`, and `docs/selected_kelvin_pair_localization_budget.md`.

## Current audited refinement result

The pair-localization audit has now isolated an exact refinement rule: a linear
physical refinement `Z_P=sum_i a_i Z_i` must be lifted by the **full tensor square**
`sum_ij a_i a_j Z_i tensor Z_j`.  Cross-child covariance is physical refinement
content, not a Pillar-II defect.  Exact odd-mode periodic Navier--Stokes shear
calibrations in GitHub Actions witness complete cancellation between positive child
diagonals and negative cross-child covariance for the parent `Z_0+Z_pi`.

See `docs/pair_localization_worldsheet_audit.md`.
