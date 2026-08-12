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

with full cross-shell and cross-child content retained inside the physical maps.  The literal global `S^int / Z_irr` equivalence remains open because the repository still contains no line-by-line definition of `S^int` or of any additional ambient CK/Hodge operator beyond the closed-cycle realization.

See `docs/cycle_typed_first_bad_selector.md` and `docs/selected_kelvin_pair_localization_budget.md`.

## Current audited refinement result

The pair-localization audit has now isolated an exact refinement rule: a linear
physical refinement `Z_P=sum_i a_i Z_i` must be lifted by the **full tensor square**
`sum_ij a_i a_j Z_i tensor Z_j`.  Cross-child covariance is physical refinement
content, not a Pillar-II defect.  Exact odd-mode periodic Navier--Stokes shear
calibrations in GitHub Actions witness complete cancellation between positive child
diagonals and negative cross-child covariance for the parent `Z_0+Z_pi`.

See `docs/pair_localization_worldsheet_audit.md`.
