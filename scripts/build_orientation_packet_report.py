from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.active_pair import pair_boundary, pair_lift  # noqa: E402
from pde_audit.orientation_packet import (  # noqa: E402
    area_frame_metric,
    area_frame_qv_matrix,
    deterministic_flux_stretching_residual,
    flux_metric_stretching_residual,
    isotropic_scale_remainder_law,
    local_tensor_bank_derivative_residual,
    local_tensor_bank_residual,
    local_tensor_packet_covariance,
    material_flux_transport_residual,
    material_metric_logdet_rate,
    metric_bulk_reconstruction_residual,
    metric_normalized_packet_bank,
    metric_packet_jump_decomposition,
    orientation_diagonal_projection,
    orientation_qv_matrix,
    packet_basis_change_invariance_residual,
    packet_bulk_payment,
    packet_covariance_pullback,
    packet_selector,
    parallel_cycle_packet_library,
    pure_frame_bank_derivative_residual,
)
from pde_audit.vorticity_restart import curl3, gradient, stretching_power  # noqa: E402


def zmat(M: sp.MatrixBase) -> bool:
    return all(sp.simplify(x) == 0 for x in M)


def main() -> None:
    nu = sp.symbols("nu", positive=True)

    # Generic GL(3) packet geometry.
    G = sp.Matrix([[1, 2, -1], [0, 3, 1], [2, -2, 4]])
    H = sp.Matrix([[2, 1, 0], [0, 2, 1], [1, 0, 1]])
    C = sp.Matrix([[5, -2, 1], [-2, 4, 3], [1, 3, 7]])
    T = sp.Matrix([[4, -1, 2], [-1, 5, 3], [2, 3, 6]])
    Tdot = sp.Matrix([[1, 2, 0], [2, -3, 1], [0, 1, 4]])
    Hdot = sp.Matrix([[3, -2, 1], [1, 4, -1], [2, 0, -3]])
    L = sp.Matrix([[1, 2, 0], [0, 1, 1], [1, 0, 1]])
    R = sp.Matrix([[2, -3, 1], [3, -1, 4], [0, 2, -1]])
    Gamma_H = area_frame_qv_matrix(G, H, nu)

    # First-bad germ packet: select a whole 3-loop block.
    B, K = parallel_cycle_packet_library(2, 3)
    Mfb = sp.diag(0, 1)
    Smf = packet_selector(Mfb, 3)
    Pmf = K * Smf
    pair_closed = zmat(sp.simplify(pair_boundary(B) * pair_lift(Pmf)))

    # Exact shear: a rotation creates cross-orientation q.v.
    x, y, z, t, k = sp.symbols("x y z t k", positive=True)
    shear = sp.Matrix([sp.exp(-nu * k**2 * t) * sp.cos(k * y), 0, 0])
    shear_w = curl3(shear, (x, y, z))
    shear_G = gradient(shear_w, (x, y, z))
    Gamma_shear = sp.simplify(orientation_qv_matrix(shear_G, sp.eye(3), nu))
    q = sp.sqrt(2) / 2
    Q = sp.Matrix([[q, 0, q], [0, 1, 0], [-q, 0, q]])
    Gamma_rot = sp.simplify(Q.T * Gamma_shear * Q)
    Gamma_diag = orientation_diagonal_projection(Gamma_rot)
    shear_recovered_diag_only = sp.simplify(Q * Gamma_diag * Q.T)

    # Exact ABC: canonical coordinate packet already has negative cross orientation.
    amp = sp.exp(-nu * t)
    abc = amp * sp.Matrix([
        sp.sin(z) + sp.cos(y),
        sp.sin(x) + sp.cos(z),
        sp.sin(y) + sp.cos(x),
    ])
    abc_w = curl3(abc, (x, y, z))
    abc_G = gradient(abc_w, (x, y, z))
    pmax = {x: sp.pi / 4, y: sp.pi / 4, z: sp.pi / 4}
    Gamma_abc_peak = sp.simplify(orientation_qv_matrix(abc_G, sp.eye(3), nu).subs(pmax))
    ndiag = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    abc_blind = sp.simplify((ndiag.T * Gamma_abc_peak * ndiag)[0])

    # Amplitude-scaled exact ABC no-go for instantaneous payment as universal bank.
    A = sp.symbols("A", positive=True)
    abcA = A * abc
    abcA_w = curl3(abcA, (x, y, z))
    abcA_G = gradient(abcA_w, (x, y, z))
    p0 = {x: 0, y: 0, z: 0}
    stretchA = sp.simplify(stretching_power(abcA, (x, y, z)).subs(p0))
    GammaA = sp.simplify(area_frame_qv_matrix(abcA_G, sp.eye(3), nu).subs(p0))
    bulkA = sp.simplify(metric_normalized_packet_bank(GammaA, sp.eye(3)))
    ratioA = sp.simplify(stretchA / bulkA)

    # p-4 scale threshold.
    r, p = sp.symbols("r p", positive=True)
    R0 = sp.Matrix([[2, -1, 0], [-1, 3, 1], [0, 1, 4]])
    H0 = sp.Matrix([[1, 1, 0], [0, 2, 0], [0, 1, 1]])
    scale_law = sp.simplify(isotropic_scale_remainder_law(R0, H0, r, p))
    scale_reference = sp.simplify(metric_normalized_packet_bank(R0, H0))

    # Passive finite GL jump: signed pieces cancel exactly.
    Lj = sp.Matrix([[sp.Rational(1, 2), 1, 0], [0, sp.Rational(1, 3), 1], [0, 0, 2]])
    jump = metric_packet_jump_decomposition(C, sp.simplify(Lj.T * C * Lj), H, sp.simplify(H * Lj))

    # Material flux/metric algebra.
    g = sp.symbols("g0:9")
    Gu = sp.Matrix(3, 3, g)
    omega_syms = sp.Matrix(sp.symbols("w1:4"))
    lap_syms = sp.Matrix(sp.symbols("l1:4"))
    flux_res = material_flux_transport_residual(Gu, omega_syms, lap_syms, H, nu)
    det_rate_divfree = material_metric_logdet_rate(
        sp.Matrix([[g[0], g[1], g[2]], [g[3], g[4], g[5]], [g[6], g[7], -g[0] - g[4]]]),
        H,
    )
    det_stretch_res = deterministic_flux_stretching_residual(omega_syms, Gu, H)
    Cflux = sp.Matrix([[5, -2, 1], [-2, 4, 3], [1, 3, 6]])
    cov_stretch_res = flux_metric_stretching_residual(Cflux, Gu, H)

    report = {
        "classification": {
            "orientation_qv_matrix": "Exact shared-noise Gram identity; off-diagonal cross-orientation covariance is physical",
            "orientation_complete_first_bad_packet": "Exact block selector M_fb tensor I_3 on closed Kelvin cycles",
            "GL3_metric_capacity": "Exact invariant scalar contraction 1/2 tr(C (H^T H)^-1)",
            "local_tensor_packet_reduction": "Exact algebra conditional on a local tensor representation C_H=H^T C_local H",
            "future_covariance_local_tensor_limit": "Conjectural bridge; no uniform singular-time tensor limit is proved",
            "material_flux_law": "Exact NS identity D_t(H^T omega)=nu H^T Delta omega",
            "material_metric_stretching": "Exact identity; rank-one metric work is omega.S.omega and covariance work is tr(S Sigma_omega)",
            "scale_remainder_threshold": "Exact r^(p-4) metric amplification for raw remainder r^p when area frame scales as r^2",
            "passive_GL3_jump": "Exact signed reset/metric revaluation cancellation",
            "abc_instantaneous_payment_no_go": "Rigorous consequence from exact amplitude-scaled 3D Navier-Stokes ABC family",
            "restart_capacity": "Open; metric-amplified non-tensorial covariance remainder and physical metric-stretching work remain uncontrolled",
            "continuation_restart": "Open; no regularity conclusion",
        },
        "generic_GL3_packet": {
            "metric_bulk_reconstruction_residual": str(metric_bulk_reconstruction_residual(G, H, nu)),
            "basis_change_invariance_residual": str(packet_basis_change_invariance_residual(C, H, L)),
            "pure_frame_bank_derivative_residual": str(pure_frame_bank_derivative_residual(C, H, R)),
            "local_tensor_bank_residual": str(local_tensor_bank_residual(T, H)),
            "local_tensor_bank_derivative_residual": str(local_tensor_bank_derivative_residual(T, Tdot, H, Hdot)),
            "area_frame_metric": [[str(v) for v in row] for row in area_frame_metric(H).tolist()],
            "raw_qv_metric_bank": str(metric_normalized_packet_bank(Gamma_H, H)),
        },
        "first_bad_restart_packet": {
            "selector_rank": Smf.rank(),
            "one_current_closed": zmat(sp.simplify(B * Pmf)),
            "pair_closed": pair_closed,
            "orientation_block_dimension": 3,
            "full_selected_pair_orientation_slots": 9,
        },
        "exact_ns_shear": {
            "canonical_qv_matrix": [[str(v) for v in row] for row in Gamma_shear.tolist()],
            "rotated_qv_matrix": [[str(v) for v in row] for row in Gamma_rot.tolist()],
            "rotated_cross_02_nonzero": sp.simplify(Gamma_rot[0, 2]) != 0,
            "trace_rotation_invariant": sp.simplify(sp.trace(Gamma_rot) - sp.trace(Gamma_shear)) == 0,
            "diagonal_only_fails_to_recover_original": not zmat(sp.simplify(shear_recovered_diag_only - Gamma_shear)),
        },
        "exact_ns_abc_peak": {
            "qv_matrix": [[str(v) for v in row] for row in Gamma_abc_peak.tolist()],
            "negative_cross_01": str(Gamma_abc_peak[0, 1]),
            "diagonal_normal_blind_qv": str(abc_blind),
            "bulk_payment": str(packet_bulk_payment(Gamma_abc_peak)),
            "determinant": str(sp.simplify(Gamma_abc_peak.det())),
        },
        "exact_ns_abc_amplitude_no_go": {
            "stretching_at_000": str(stretchA),
            "instantaneous_kelvin_bulk_at_000": str(bulkA),
            "ratio": str(ratioA),
            "ratio_at_t0_A_to_infinity": str(sp.limit(ratioA.subs(t, 0), A, sp.oo)),
        },
        "scale_capacity": {
            "raw_remainder_metric_law": str(scale_law),
            "reference_contraction": str(scale_reference),
            "law_over_reference": str(sp.simplify(scale_law / scale_reference)),
            "p_gt_4_limit_example_p5": str(sp.limit(scale_law.subs(p, 5), r, 0, dir='+')),
            "p_eq_4": str(sp.simplify(scale_law.subs(p, 4))),
            "p_lt_4_limit_example_p3": str(sp.limit(scale_law.subs(p, 3), r, 0, dir='+')),
        },
        "passive_GL3_jump": {
            "total": str(jump.total),
            "covariance_reset_at_new_metric": str(jump.covariance_reset_at_new_metric),
            "metric_revaluation": str(jump.metric_revaluation),
            "reconstructs": sp.simplify(jump.total - jump.reconstructed) == 0,
            "signed_faces_cancel": sp.simplify(jump.covariance_reset_at_new_metric + jump.metric_revaluation) == 0,
        },
        "material_flux_metric": {
            "flux_transport_residual_zero": zmat(flux_res),
            "incompressible_metric_logdet_rate": str(det_rate_divfree),
            "rank_one_metric_stretching_residual": str(det_stretch_res),
            "covariance_metric_stretching_residual": str(cov_stretch_res),
        },
        "frontier": {
            "old_rank_one_restart_issue": "resolved structurally by selecting a 3-loop packet per first-bad germ; threshold itself remains undefined",
            "frame_geometry": "passive GL(3) orientation/scale/shear cancels in metric-normalized scalar capacity",
            "material_geometry": "physical Nanson metric motion is vortex-stretching work when flux coordinates are held by the NS flux law",
            "scale_obstruction": "only metric-amplified departure from area^2 local tensorial covariance survives pure packet normalization",
            "remaining_restart_problem": "prove a uniform local future-covariance tensor/remainder law and control its material metric-stretching/boundary terms up to a candidate singular time",
        },
    }

    out = ROOT / "audit-results" / "orientation_complete_restart_packet_report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(out)
    print("packet selector rank / closed / pair closed:", report["first_bad_restart_packet"]["selector_rank"], report["first_bad_restart_packet"]["one_current_closed"], report["first_bad_restart_packet"]["pair_closed"])
    print("GL3 bulk / basis / frame residuals:", report["generic_GL3_packet"]["metric_bulk_reconstruction_residual"], report["generic_GL3_packet"]["basis_change_invariance_residual"], report["generic_GL3_packet"]["pure_frame_bank_derivative_residual"])
    print("ABC peak qv matrix:", report["exact_ns_abc_peak"]["qv_matrix"])
    print("ABC amplitude stretching/payment ratio:", report["exact_ns_abc_amplitude_no_go"]["ratio"])
    print("scale law/reference:", report["scale_capacity"]["law_over_reference"])
    print("material flux / rank-one stretch residuals:", report["material_flux_metric"]["flux_transport_residual_zero"], report["material_flux_metric"]["rank_one_metric_stretching_residual"])
    print("passive jump signed cancellation:", report["passive_GL3_jump"]["signed_faces_cancel"])


if __name__ == "__main__":
    main()
