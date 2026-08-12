from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.vorticity_restart import (  # noqa: E402
    canonical_microframe_bulk_dissipation,
    curl3,
    enstrophy_density,
    frobenius_square,
    gradient,
    kelvin_microframe_bulk_dissipation,
    kelvin_microframe_density,
    kelvin_small_disk_action_from_local_gradient,
    laplacian_scalar,
    local_enstrophy_balance_residual,
    material_line_length_residual,
    microframe_reconstruction_residual,
    normalized_small_disk_action,
    renormalized_bank_chain_residual,
    skew_annihilates_vorticity_residual,
    strain_tensor,
    stretching_gate_margin,
    stretching_power,
    vorticity_equation_residual,
)


def zmat(M: sp.MatrixBase) -> bool:
    return all(sp.trigsimp(sp.simplify(c)) == 0 for c in M)


def main() -> None:
    nu = sp.symbols("nu", positive=True)
    a = sp.symbols("a0:9")
    Gomega = sp.Matrix(3, 3, a)
    I = sp.eye(3)
    rotated = [
        sp.Matrix([1, 1, 0]) / sp.sqrt(2),
        sp.Matrix([1, -1, 0]) / sp.sqrt(2),
        sp.Matrix([0, 0, 1]),
    ]
    canonical_bulk = canonical_microframe_bulk_dissipation(Gomega, nu)
    rotated_bulk = kelvin_microframe_bulk_dissipation(Gomega, rotated, nu)

    b, c = sp.symbols("b c", positive=True)
    blind_G = sp.diag(0, b, c)
    blind_gamma = kelvin_microframe_density(blind_G, sp.Matrix([1, 0, 0]), nu)
    blind_bulk = sp.simplify(nu * frobenius_square(blind_G))

    A, lam = sp.symbols("A lam", positive=True)
    scale_G = sp.diag(*sp.symbols("g1:4", positive=True))
    scale_n = sp.Matrix([0, 0, 1])
    raw = kelvin_small_disk_action_from_local_gradient(scale_G, scale_n, A, nu)
    raw_scaled = kelvin_small_disk_action_from_local_gradient(scale_G, scale_n, lam**2 * A, nu)
    normalized = normalized_small_disk_action(raw, A)
    normalized_scaled = normalized_small_disk_action(raw_scaled, lam**2 * A)

    V, gamma, work, area, area_dot = sp.symbols("V gamma work area area_dot", nonzero=True)
    bank_residual = renormalized_bank_chain_residual(V, gamma, work, area, area_dot)

    g = sp.symbols("m0:9")
    G = sp.Matrix(3, 3, g)
    ell = sp.Matrix(sp.symbols("l1:4"))

    x, y, z, t, k = sp.symbols("x y z t k", positive=True)
    coords = (x, y, z)

    shear_amp = sp.exp(-nu * k**2 * t)
    shear = sp.Matrix([shear_amp * sp.cos(k * y), 0, 0])
    shear_omega = curl3(shear, coords)
    shear_Gomega = gradient(shear_omega, coords)
    shear_gammas = [sp.simplify(kelvin_microframe_density(shear_Gomega, I[:, j], nu)) for j in range(3)]

    Uadv = sp.symbols("Uadv", positive=True)
    adv_phase = k * (y - Uadv * t)
    adv_shear = sp.Matrix([shear_amp * sp.cos(adv_phase), Uadv, 0])
    adv_omega = curl3(adv_shear, coords)
    adv_vorticity_transport = sp.Matrix([sp.trigsimp(sp.simplify(c)) for c in gradient(adv_omega, coords) * adv_shear])
    adv_stretching = sp.Matrix([sp.trigsimp(sp.simplify(c)) for c in strain_tensor(adv_shear, coords) * adv_omega])

    abc_amp = sp.exp(-nu * t)
    abc = abc_amp * sp.Matrix([
        sp.sin(z) + sp.cos(y),
        sp.sin(x) + sp.cos(z),
        sp.sin(y) + sp.cos(x),
    ])
    abc_omega = curl3(abc, coords)
    abc_Gomega = gradient(abc_omega, coords)
    abc_e = enstrophy_density(abc_omega)
    p0 = {x: 0, y: 0, z: 0}
    pmax = {x: sp.pi / 4, y: sp.pi / 4, z: sp.pi / 4}
    abc_peak_bulk = sp.simplify(canonical_microframe_bulk_dissipation(abc_Gomega, nu).subs(pmax))
    abc_peak_lap_flux = sp.simplify(nu * laplacian_scalar(abc_e, coords).subs(pmax))
    abc_peak_dt = sp.simplify(sp.diff(abc_e, t).subs(pmax))
    abc_peak_grad_e = [sp.simplify(sp.diff(abc_e, q).subs(pmax)) for q in coords]

    report = {
        "classification": {
            "vorticity_strain_equation": "Exact identity after curl removes pressure gauge",
            "material_line_stretching": "Exact kinematic identity; strain is the line-length deformation channel",
            "amplitude_direction_split": "Exact identity away from vorticity zeros",
            "kelvin_microframe_density": "Exact small-disk Stokes limit in constant orthonormal noise frame",
            "microframe_bulk_reconstruction": "Exact identity: one-half of three orthogonal loop q.v. densities equals nu|grad omega|^2",
            "material_germ_enstrophy_ledger": "Exact Reynolds/Stokes consequence for a material volume",
            "local_growth_gate": "Rigorous necessary condition only; not a restart criterion",
            "orientation_completion": "Rigorous structural requirement if Kelvin q.v. is used to reconstruct full bulk vorticity-gradient dissipation",
            "area_squared_scaling": "Exact affine/small-disk leading law; raw q.v. scales like area^2",
            "renormalized_bank_dilation": "Exact chain-rule term under changing germ area",
            "continuation_restart": "Open; no regularity conclusion",
        },
        "generic_algebra": {
            "skew_annihilates_vorticity": zmat(skew_annihilates_vorticity_residual(G)),
            "material_line_length_residual": str(material_line_length_residual(G, ell)),
            "microframe_reconstruction_residual": str(microframe_reconstruction_residual(Gomega, nu)),
            "rotated_frame_same_bulk": sp.simplify(canonical_bulk - rotated_bulk) == 0,
            "canonical_bulk": str(canonical_bulk),
        },
        "orientation_blindness": {
            "single_normal_gamma": str(blind_gamma),
            "full_bulk_dissipation": str(blind_bulk),
            "single_normal_blind": sp.simplify(blind_gamma) == 0,
            "bulk_nonzero_symbolically": blind_bulk != 0,
        },
        "small_disk_scaling": {
            "raw_action": str(raw),
            "raw_scaled_minus_lambda4_raw": str(sp.simplify(raw_scaled - lam**4 * raw)),
            "normalized_density": str(normalized),
            "normalized_scale_residual": str(sp.simplify(normalized_scaled - normalized)),
        },
        "renormalized_bank": {
            "chain_rule_residual": str(bank_residual),
            "dilation_term": "-2*(area_dot/area)*(V/area^2)",
        },
        "exact_ns_galilean_advected_shear": {
            "vorticity_transport": [str(c) for c in adv_vorticity_transport],
            "vorticity_transport_nonzero": not zmat(adv_vorticity_transport),
            "stretching_zero": zmat(adv_stretching),
            "vorticity_equation_zero": zmat(vorticity_equation_residual(adv_shear, coords, t, nu)),
            "enstrophy_balance_residual": str(local_enstrophy_balance_residual(adv_shear, coords, t, nu)),
        },
        "exact_ns_shear": {
            "vorticity": [str(c) for c in shear_omega],
            "vorticity_equation_zero": zmat(vorticity_equation_residual(shear, coords, t, nu)),
            "stretching_power": str(stretching_power(shear, coords)),
            "enstrophy_balance_residual": str(local_enstrophy_balance_residual(shear, coords, t, nu)),
            "microframe_gammas": [str(gm) for gm in shear_gammas],
            "two_normals_blind": shear_gammas[0] == 0 and shear_gammas[1] == 0,
            "microframe_bulk_residual": str(microframe_reconstruction_residual(shear_Gomega, nu)),
        },
        "exact_ns_abc": {
            "beltrami_vorticity_equals_velocity": zmat(sp.Matrix([sp.trigsimp(sp.simplify(c)) for c in abc_omega - abc])),
            "vorticity_equation_zero": zmat(vorticity_equation_residual(abc, coords, t, nu)),
            "enstrophy_balance_residual": str(local_enstrophy_balance_residual(abc, coords, t, nu)),
            "stretching_power_at_000": str(sp.simplify(stretching_power(abc, coords).subs(p0))),
            "peak_grad_enstrophy": [str(v) for v in abc_peak_grad_e],
            "peak_stretching_power": str(sp.simplify(stretching_power(abc, coords).subs(pmax))),
            "peak_kelvin_bulk_dissipation": str(abc_peak_bulk),
            "peak_spatial_laplacian_flux": str(abc_peak_lap_flux),
            "peak_time_derivative_enstrophy": str(abc_peak_dt),
            "peak_gate_margin": str(sp.simplify(stretching_gate_margin(abc, coords, nu).subs(pmax))),
        },
        "restart_frontier": {
            "new_exact_ledger": "stretching production + spatial/Hodge boundary flux - Kelvin microframe bulk q.v. dissipation",
            "rank_one_issue": "one loop orientation can be blind; an orientation-complete packet or proved orientation coverage is required",
            "scale_issue": "raw Kelvin bank scales like area^2; local-gradient restart requires area^2-renormalized capacity across shrinking shells",
            "dilation_issue": "scalar isotropic dilation is an exact coordinate term; the later GL(3) packet metric audit shows passive scale/frame motion cancels when full covariance and metric co-transform",
            "first_bad_threshold": "still not defined; local stretch-over-Kelvin gate is only a necessary local-growth gate",
            "remaining_restart_problem": "establish the local future-covariance tensor/remainder law and control metric-amplified remainder, material metric-stretching, and physical boundary/exit work up to a candidate singular time",
        },
    }

    out = ROOT / "audit-results" / "vorticity_restart_geometry_report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(out)
    print("microframe reconstruction residual:", report["generic_algebra"]["microframe_reconstruction_residual"])
    print("rotated frame same bulk:", report["generic_algebra"]["rotated_frame_same_bulk"])
    print("single normal blind:", report["orientation_blindness"]["single_normal_blind"])
    print("raw lambda^4 scaling residual:", report["small_disk_scaling"]["raw_scaled_minus_lambda4_raw"])
    print("renormalized bank chain residual:", report["renormalized_bank"]["chain_rule_residual"])
    print("advected shear transport nonzero / stretching zero:", report["exact_ns_galilean_advected_shear"]["vorticity_transport_nonzero"], report["exact_ns_galilean_advected_shear"]["stretching_zero"])
    print("shear microframe gammas:", report["exact_ns_shear"]["microframe_gammas"])
    print("ABC peak bulk / flux / dt:", report["exact_ns_abc"]["peak_kelvin_bulk_dissipation"], report["exact_ns_abc"]["peak_spatial_laplacian_flux"], report["exact_ns_abc"]["peak_time_derivative_enstrophy"])


if __name__ == "__main__":
    main()
