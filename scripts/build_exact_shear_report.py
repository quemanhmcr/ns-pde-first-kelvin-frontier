from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.exact_shear import (  # noqa: E402
    circulation_traffic_integral,
    hodge_green_bank_initial,
    horizon,
    kelvin_terminal_moments,
)

nu = c = L = 1.0
rows = []
for N in [8, 16, 32, 64, 128, 256]:
    mean, second, var = kelvin_terminal_moments(N, c, L)
    traffic = circulation_traffic_integral(N, nu, c)
    hodge = hodge_green_bank_initial(N)
    rows.append({
        "N": N,
        "T_N": horizon(N, nu, c),
        "E_X": mean,
        "E_X2": second,
        "Var_X": var,
        "Var_X_over_N": var / N,
        "traffic_integral": traffic,
        "N2_times_traffic": N * N * traffic,
        "hodge_bank_initial": hodge,
        "N_times_hodge_bank": N * hodge,
        "Var_over_traffic": var / traffic,
        "Var_over_hodge_bank": var / hodge,
    })

report = {
    "calibration": "exact periodic 3D Navier-Stokes multimode shear",
    "parameters": {"nu": nu, "c": c, "L": L},
    "method": "closed-form Gaussian expectations; no Monte Carlo; exact NS solution family",
    "interpretation": {
        "Var_X": "Kelvin future-variance bank / expected martingale quadratic variation for fixed circulation",
        "traffic_integral": "time-integrated drift-square circulation traffic on T_N",
        "hodge_bank_initial": "natural coexact Green/Hodge bank at t=0",
    },
    "rows": rows,
}
out = ROOT / "audit-results" / "exact_shear_report.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(report, indent=2) + "\n")
print(out)
for row in rows:
    print(
        f"N={row['N']:3d} Var={row['Var_X']:.8g} Var/N={row['Var_X_over_N']:.8g} "
        f"traffic={row['traffic_integral']:.8g} N^2*traffic={row['N2_times_traffic']:.8g} "
        f"H={row['hodge_bank_initial']:.8g} N*H={row['N_times_hodge_bank']:.8g} "
        f"Var/traffic={row['Var_over_traffic']:.8g}"
    )
