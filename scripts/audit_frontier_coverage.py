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
    "variable-frame-connection": ("audited-generic", "Cartan/transport geometry audited; literal CK frame data belongs to active projection audit"),
    "active-pair-factorization": ("audited", "full pair boundary/transport residual is exact tensor lift of one-current commutator"),
    "active-ck-pillar-ii": ("open-literal", "one-current P_active incidence/transport data absent; S^int / Z_irr not declared zero"),
    "continuation-restart": ("open", "no regularity bridge claimed"),
}

ALLOWED = {"audited", "audited-calibration", "audited-generic", "open-literal", "open"}
required = {
    "freeze", "quantile", "anchor-orientation", "shell", "refinement",
    "resolve-reset", "physical-exit", "variable-frame-connection",
    "active-pair-factorization", "active-ck-pillar-ii", "continuation-restart",
}

if set(SEAMS) != required:
    raise SystemExit(f"frontier seam registry mismatch: {set(SEAMS) ^ required}")
for seam, (status, meaning) in SEAMS.items():
    if status not in ALLOWED or not meaning.strip():
        raise SystemExit(f"invalid seam classification: {seam}: {status}: {meaning!r}")

if SEAMS["active-pair-factorization"][0] != "audited":
    raise SystemExit("full-pair commutator factorization must remain explicitly audited")
if SEAMS["active-ck-pillar-ii"][0] != "open-literal":
    raise SystemExit("Pillar II must remain open-literal until literal P_active incidence/transport verification")
if SEAMS["continuation-restart"][0] != "open":
    raise SystemExit("continuation/restart must remain open")

print("pair-localization frontier coverage: PASS")
for seam, (status, meaning) in SEAMS.items():
    print(f"{seam:28s} {status:20s} {meaning}")
