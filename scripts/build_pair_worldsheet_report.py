from __future__ import annotations

import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.exact_shear import kelvin_anchor_covariance, kelvin_anchor_moments
from pde_audit.pair_worldsheet import make_stage, worldsheet_boundary


def main() -> None:
    labels = ["freeze", "quantile", "anchor", "shell", "refinement", "resolve", "exit"]
    stages = [make_stage(label, k) for k, label in enumerate(labels)]
    boundary = worldsheet_boundary(stages)

    rows = []
    for N in [8, 16, 32, 64, 128]:
        v0 = kelvin_anchor_moments(N, 1.0, 0.0)[2]
        vpi = kelvin_anchor_moments(N, 1.0, math.pi)[2]
        cov = kelvin_anchor_covariance(N, 1.0, 0.0, math.pi)
        rows.append(
            {
                "N": N,
                "V0": v0,
                "Vpi": vpi,
                "Cov0pi": cov,
                "diagonal_only_parent_variance": v0 + vpi,
                "full_parent_variance": v0 + vpi + 2.0 * cov,
            }
        )

    report = {
        "classification": {
            "worldsheet_internal_seam_cancellation": "Exact identity",
            "odd_shear_cross_child_cancellation": "Rigorous consequence from exact NS calibration",
            "pair_localization_closure": "Conjectural bridge pending literal active-chain/Pillar-II audit",
        },
        "worldsheet_boundary": boundary.as_dict(),
        "odd_shear_refinement_rows": rows,
        "interpretation": (
            "Internal localization rungs telescope. A linear physical refinement must be lifted by the full "
            "tensor square; cross-child pair currents are physical covariance content, not an irreducible defect."
        ),
    }
    out = ROOT / "audit-results" / "pair_worldsheet_report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(out)
    for row in rows:
        print(
            f"N={row['N']:3d} V0={row['V0']:.8g} Cov(0,pi)={row['Cov0pi']:.8g} "
            f"diag={row['diagonal_only_parent_variance']:.8g} full={row['full_parent_variance']:.3e}"
        )


if __name__ == "__main__":
    main()
