from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
note = ROOT / "docs" / "selected_kelvin_pair_localization_budget.md"
text = note.read_text()
required = [
    "Exact identity",
    "Rigorous consequence",
    "Conjectural bridge",
    "No continuation",
    "Z_irr",
    "pair localization",
]
missing = [token for token in required if token not in text]
if missing:
    print("missing required structural markers:", missing)
    sys.exit(1)
for forbidden in [
    "therefore 3D Navier--Stokes is regular",
    "global regularity is proved",
    "S^int = 0 is established",
]:
    if forbidden in text:
        print("forbidden overclaim found:", forbidden)
        sys.exit(1)
print("classification/anti-overclaim audit: PASS")
