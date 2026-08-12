"""Fail CI if a first-bad-germ seam has no explicit structural status."""
from __future__ import annotations

SEAMS = {
    "freeze": ("audited", "fixed-current Kelvin q.v./future-variance bank"),
    "quantile": ("audited-calibration", "one-particle conservation does not erase pair leakage"),
    "anchor-orientation": ("audited", "continuous covariance derivative + reset revaluation"),
    "shell": ("audited-calibration", "full product pair partition required"),
    "refinement": ("audited", "full tensor-square pair functor; cross-child covariance required"),
    "resolve-reset": ("audited", "observer jump has no q.v.; covariance revaluation is exact"),
    "physical-exit": ("audited-calibration", "two-face sub-Markov pair sink"),
    "variable-frame-connection": ("audited-generic", "Cartan/transport geometry audited; literal extra CK frame operator, if any, remains separate"),
    "active-pair-factorization": ("audited", "full pair boundary/transport residual is exact tensor lift of one-current commutator"),
    "cycle-typed-first-bad-boundary": ("audited", "closed Kelvin cycle library forces zero intrinsic selector physical boundary and pair boundary"),
    "cycle-typed-first-bad-transport": ("audited", "support transport is exact germ cut current; finite hysteresis switch is reset revaluation"),
    "hodge-cycle-projector": ("audited-generic", "idempotent closed-range projector has zero physical boundary and pure range/complement exchange motion"),
    "kelvin-ck-admissibility": ("audited", "arbitrary cycle-preserving linear/differentiable CK maps have zero intrinsic boundary; cycle breaking is gauge-visible physical boundary"),
    "stochastic-ck-carre-du-champ": ("audited-generic", "stochastic cycle motion contributes explicit martingale pair q.v.; finite-variation selector contribution is zero"),
    "vorticity-kelvin-microframe": ("audited", "three orthogonal infinitesimal closed-loop q.v. densities reconstruct nu|grad omega|^2 exactly"),
    "restart-scale-renormalization": ("audited", "raw small-loop q.v. scales like area^2; GL(3) packet metric gives the exact scale-normalized contraction and passive dilation cancels"),
    "orientation-complete-restart-packet": ("audited", "first-bad restart selector lifts as M_fb tensor I_3 and full cross-orientation covariance is retained"),
    "material-flux-metric-split": ("audited", "Nanson plus NS gives D_t(H^T omega)=nu H^T Delta omega while packet metric work is vortex stretching"),
    "future-covariance-full-state-tensor-law": ("audited", "vector conditional covariance gains the full mixed carre-du-champ while conditional mean-square loses it"),
    "future-covariance-double-stokes": ("audited", "closed-loop future covariance is the double-Stokes localization of the existing pair momentum covariance cochain"),
    "future-covariance-fixed-state-stokes-limit": ("audited-conditional", "conditional mean-square continuity gives the fixed-state area-squared local covariance tensor; centered C2 packets have r^2 normalized remainder"),
    "backward-kelvin-infinitesimal-generator": ("audited-calibration", "Nanson plus exact NS gives the backward-Ito packet mean operator; exact shear covariance transfers the Kelvin Gram tensor"),
    "future-covariance-generator-descent": ("open-literal", "the full stochastic Kelvin current/shape state generator has not been shown to intertwine with the reduced first-bad spatial/area-frame state"),
    "future-backward-time-identification": ("open-literal", "the abstract forward future-ancestry bank has not been line-by-line identified with the causal physical backward-Kelvin martingale bank"),
    "future-covariance-uniform-singular-limit": ("open", "fixed-state tensor existence is conditional-rigorous, but no uniform diagonal trace/remainder control is proved near a candidate singular time"),
    "restart-capacity": ("open", "uniform tensor remainder plus material metric-stretching and physical boundary/exit work remain uncontrolled"),
    "active-ck-pillar-ii": ("open-literal", "selector and deterministic/stochastic admissible CK operation classes are classified; S^int itself or any independently intended Z_irr is not defined line by line"),
    "continuation-restart": ("open", "no regularity bridge claimed"),
}

ALLOWED = {"audited", "audited-calibration", "audited-generic", "audited-conditional", "open-literal", "open"}
required = {
    "freeze", "quantile", "anchor-orientation", "shell", "refinement",
    "resolve-reset", "physical-exit", "variable-frame-connection",
    "active-pair-factorization", "cycle-typed-first-bad-boundary",
    "cycle-typed-first-bad-transport", "hodge-cycle-projector", "kelvin-ck-admissibility",
    "stochastic-ck-carre-du-champ", "vorticity-kelvin-microframe",
    "restart-scale-renormalization", "orientation-complete-restart-packet",
    "material-flux-metric-split", "future-covariance-full-state-tensor-law",
    "future-covariance-double-stokes", "future-covariance-fixed-state-stokes-limit",
    "backward-kelvin-infinitesimal-generator", "future-covariance-generator-descent",
    "future-backward-time-identification", "future-covariance-uniform-singular-limit",
    "restart-capacity", "active-ck-pillar-ii", "continuation-restart",
}

if set(SEAMS) != required:
    raise SystemExit(f"frontier seam registry mismatch: {set(SEAMS) ^ required}")
for seam, (status, meaning) in SEAMS.items():
    if status not in ALLOWED or not meaning.strip():
        raise SystemExit(f"invalid seam classification: {seam}: {status}: {meaning!r}")

for exact_seam in (
    "active-pair-factorization",
    "cycle-typed-first-bad-boundary",
    "cycle-typed-first-bad-transport",
    "kelvin-ck-admissibility",
    "vorticity-kelvin-microframe",
    "restart-scale-renormalization",
    "orientation-complete-restart-packet",
    "material-flux-metric-split",
    "future-covariance-full-state-tensor-law",
    "future-covariance-double-stokes",
):
    if SEAMS[exact_seam][0] != "audited":
        raise SystemExit(f"{exact_seam} must remain explicitly audited")
if SEAMS["future-covariance-fixed-state-stokes-limit"][0] != "audited-conditional":
    raise SystemExit("fixed-state future-covariance Stokes limit must remain explicitly conditional on mean-square continuity")
if SEAMS["backward-kelvin-infinitesimal-generator"][0] != "audited-calibration":
    raise SystemExit("backward-Kelvin infinitesimal generator must remain an exact/calibrated NS result")
for seam in ("future-covariance-generator-descent", "future-backward-time-identification"):
    if SEAMS[seam][0] != "open-literal":
        raise SystemExit(f"{seam} must remain open-literal until the full state/time map is written line by line")
if SEAMS["future-covariance-uniform-singular-limit"][0] != "open":
    raise SystemExit("uniform singular-time future-covariance trace/remainder control must remain open")
if SEAMS["active-ck-pillar-ii"][0] != "open-literal":
    raise SystemExit("global Pillar II must remain open-literal until S^int and any independently intended Z_irr are literally defined and audited")
if SEAMS["restart-capacity"][0] != "open":
    raise SystemExit("restart capacity must remain open until the metric-normalized future covariance remainder and material metric work are controlled")
if SEAMS["continuation-restart"][0] != "open":
    raise SystemExit("continuation/restart must remain open")

print("pair-localization frontier coverage: PASS")
for seam, (status, meaning) in SEAMS.items():
    print(f"{seam:40s} {status:20s} {meaning}")
