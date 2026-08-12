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
    "active-ck-pillar-ii": ("open-literal", "selector residual closed; projector kinematics classified; S^int or any non-projector CK content is not defined line by line"),
    "continuation-restart": ("open", "no regularity bridge claimed"),
}

ALLOWED = {"audited", "audited-calibration", "audited-generic", "open-literal", "open"}
required = {
    "freeze", "quantile", "anchor-orientation", "shell", "refinement",
    "resolve-reset", "physical-exit", "variable-frame-connection",
    "active-pair-factorization", "cycle-typed-first-bad-boundary",
    "cycle-typed-first-bad-transport", "hodge-cycle-projector", "active-ck-pillar-ii", "continuation-restart",
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
):
    if SEAMS[exact_seam][0] != "audited":
        raise SystemExit(f"{exact_seam} must remain explicitly audited")
if SEAMS["active-ck-pillar-ii"][0] != "open-literal":
    raise SystemExit("global Pillar II must remain open-literal until S^int and any extra CK/Hodge operator are defined and audited")
if SEAMS["continuation-restart"][0] != "open":
    raise SystemExit("continuation/restart must remain open")

print("pair-localization frontier coverage: PASS")
for seam, (status, meaning) in SEAMS.items():
    print(f"{seam:34s} {status:20s} {meaning}")
