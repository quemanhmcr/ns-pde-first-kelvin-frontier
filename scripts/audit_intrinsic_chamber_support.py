from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "intrinsic_chamber_kelvin_support_audit.md"
text = DOC.read_text()

required = [
    "Literal periodic Navier--Stokes first",
    "Intrinsic chamber geometry",
    "Orientation-complete packet lift",
    "Kelvin current collapses while one physical face stays large",
    "Orientation-complete quadrupoles expose what circulation misses",
    "Exact nested-chamber no-go",
    "Architecture consequence",
    "Open-literal",
    "No restart/continuation/regularity theorem claimed",
]
missing = [x for x in required if x not in text]
if missing:
    raise SystemExit(f"missing intrinsic chamber support markers: {missing}")

prohibited_claims = [
    "tangential support tensor proves continuation",
    "intrinsic chamber proves support locality",
    "zero compatibility proves support locality",
    "Kelvin residual collapse proves support locality",
    "first-bad support collapse is proved",
    "global regularity is proved",
]
hits = [x for x in prohibited_claims if x in text]
if hits:
    raise SystemExit(f"intrinsic chamber support overclaim markers found: {hits}")

print("intrinsic chamber support anti-overclaim audit: PASS")
