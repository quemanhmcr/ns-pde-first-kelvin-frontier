from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.future_covariance_tensor import (  # noqa: E402
    backward_kelvin_flux_mean_residual,
    backward_local_tensor_operator,
    conditional_covariance,
    connected_covariance_horizon_residual,
    connected_mean_horizon_residual,
    connected_mean_square_horizon_residual,
    connected_second_moment_horizon_residual,
    double_stokes_pair_covariance,
    exact_gauge_cycle_projection,
    generator_descends,
    generator_intertwining_residual,
    metric_amplified_symmetric_remainder,
    packet_tensor_pullback,
    product_pair_diagonal_defect,
    quotient_generator,
    symmetric_loop_covariance_expansion,
    vector_carre_du_champ,
    vorticity_dyad_residual,
)
from pde_audit.orientation_packet import area_frame_qv_matrix  # noqa: E402
from pde_audit.vorticity_restart import curl3, gradient  # noqa: E402


def zmat(M: sp.MatrixBase) -> bool:
    return all(sp.simplify(x) == 0 for x in M)


def smat(M: sp.MatrixBase) -> list[list[str]]:
    return [[str(sp.simplify(M[i, j])) for j in range(M.cols)] for i in range(M.rows)]


def main() -> None:
    a, tau, nu, k = sp.symbols("a tau nu k", positive=True)
    b1, b2 = sp.symbols("b1 b2")
    heat = sp.exp(-nu * k**2 * tau)
    mean = sp.Matrix([
        sp.exp(-b1 * tau) * heat * sp.cos(k * a),
        sp.exp(-b2 * tau) * heat * sp.sin(k * a),
    ])
    e4 = sp.exp(-4 * nu * k**2 * tau)
    Q0 = sp.Matrix([
        [sp.Rational(1, 2) * (1 + e4 * sp.cos(2 * k * a)), sp.Rational(1, 2) * e4 * sp.sin(2 * k * a)],
        [sp.Rational(1, 2) * e4 * sp.sin(2 * k * a), sp.Rational(1, 2) * (1 - e4 * sp.cos(2 * k * a))],
    ])
    D = sp.diag(sp.exp(-b1 * tau), sp.exp(-b2 * tau))
    second = sp.simplify(D * Q0 * D)
    B = sp.diag(b1, b2)
    drift = sp.Matrix([0])
    diffusion = sp.Matrix([[2 * nu]])
    C = conditional_covariance(mean, second)
    Gamma = vector_carre_du_champ(mean, diffusion, [a])

    x, x1, x2 = sp.symbols("x x1 x2")
    poly_mean = sp.Matrix([x**2 + x, x**3 - 2 * x])
    poly_drift = sp.Matrix([x + 1])
    poly_diff = sp.Matrix([[2 * nu]])
    pair_defect = product_pair_diagonal_defect(poly_mean, [x], [x1], [x2], poly_drift, poly_diff)
    pair_gamma = vector_carre_du_champ(poly_mean, poly_diff, [x])

    B1 = sp.Matrix([
        [-1, 0, 1],
        [1, -1, 0],
        [0, 1, -1],
    ])
    D2 = sp.Matrix([1, 1, 1])
    k11, k12, k13, k22, k23, k33 = sp.symbols("k11 k12 k13 k22 k23 k33")
    Kpair = sp.Matrix([
        [k11, k12, k13],
        [k12, k22, k23],
        [k13, k23, k33],
    ])
    face_cov = double_stokes_pair_covariance(Kpair, D2)
    p0, p1, p2 = sp.symbols("p0 p1 p2")
    gauge = exact_gauge_cycle_projection(B1, D2, sp.Matrix([p0, p1, p2]))

    L_bad = sp.Matrix([
        [-1, 0, 1, 0],
        [0, -2, 0, 2],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ])
    L_good = sp.Matrix([
        [-1, 0, 1, 0],
        [0, -1, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ])
    labels = [0, 0, 1, 1]

    r = sp.symbols("r", positive=True)
    c11, c12, c22 = sp.symbols("c11 c12 c22")
    d11, d12, d22 = sp.symbols("d11 d12 d22")
    e11, e12, e22 = sp.symbols("e11 e12 e22")
    C0 = sp.Matrix([[c11, c12], [c12, c22]])
    C1 = sp.Matrix([[d11, d12], [d12, d22]])
    C2 = sp.Matrix([[e11, e12], [e12, e22]])
    raw = symmetric_loop_covariance_expansion(C0, C1, C2, r)
    amplified = metric_amplified_symmetric_remainder(raw, C0, r)

    # Exact NS shear and ABC tensor-enstrophy calibrations.
    X, Y, Z, t = sp.symbols("X Y Z t", positive=True)
    coords = (X, Y, Z)
    shear = sp.Matrix([sp.exp(-nu * k**2 * t) * sp.cos(k * Y), 0, 0])
    shear_omega = curl3(shear, coords)
    shear_dyad_res = vorticity_dyad_residual(shear_omega, gradient(shear, coords), shear, nu, t, coords)

    amp = sp.exp(-nu * t)
    abc = amp * sp.Matrix([
        sp.sin(Z) + sp.cos(Y),
        sp.sin(X) + sp.cos(Z),
        sp.sin(Y) + sp.cos(X),
    ])
    abc_omega = curl3(abc, coords)
    abc_dyad_res = vorticity_dyad_residual(abc_omega, gradient(abc, coords), abc, nu, t, coords)

    # Exact causal backward-Kelvin shear covariance tensor with past terminal t0.
    t0 = sp.symbols("t0", positive=True)
    Qzz_back = sp.Rational(1, 2) * k**2 * sp.exp(-2 * nu * k**2 * t0) * (
        1 - sp.exp(-4 * nu * k**2 * (t - t0)) * sp.cos(2 * k * Y)
    )
    Czz_back = sp.simplify(Qzz_back - shear_omega[2] ** 2)
    rho_back = sp.exp(-2 * nu * k**2 * (t - t0))
    Czz_manifest = sp.Rational(1, 2) * k**2 * sp.exp(-2 * nu * k**2 * t0) * (1 - rho_back) * (1 + rho_back * sp.cos(2 * k * Y))
    Cback = sp.diag(0, 0, Czz_back)
    Qback = sp.diag(0, 0, Qzz_back)
    shear_G = gradient(shear_omega, coords)
    shear_Gamma = sp.simplify(2 * nu * shear_G * shear_G.T)
    backward_cov_res = sp.simplify(backward_local_tensor_operator(Cback, gradient(shear, coords), shear, nu, t, coords) - shear_Gamma)
    backward_Q_res = sp.simplify(backward_local_tensor_operator(Qback, gradient(shear, coords), shear, nu, t, coords))
    Hback = sp.Matrix([[1, 2, 0], [0, 1, 1], [1, 0, 1]])
    backward_mean_res = backward_kelvin_flux_mean_residual(shear_omega, gradient(shear, coords), shear, Hback, nu, t, coords)

    g = sp.Matrix(3, 3, sp.symbols("g0:9"))
    H = sp.Matrix([[1, 2, 0], [0, 1, 1], [1, 0, 1]])
    local_source = sp.simplify(2 * nu * g * g.T)
    packet_pullback_res = sp.simplify(packet_tensor_pullback(local_source, H) - area_frame_qv_matrix(g, H, nu))

    orient = sp.Matrix([1, 0, -1])
    scalar_mean = sp.exp(-nu * k**2 * tau) * sp.cos(k * a)
    orient_mean = orient * scalar_mean
    orient_gamma = sp.simplify(vector_carre_du_champ(orient_mean, diffusion, [a]))

    report = {
        "classification": {
            "full_state_vector_moment_law": "Exact conditional-moment identity on the full Markov/Kelvin state",
            "vector_future_covariance_pde": "Exact horizon law H C + connection = full vector carre-du-champ",
            "mean_square_to_covariance_transfer": "Exact: the same carre-du-champ is lost by conditional mean-square and gained by future covariance",
            "same_ancestor_pair_diagonal_defect": "Exact matrix cross-derivation equal to vector carre-du-champ",
            "double_stokes_pair_covariance": "Exact current/cochain identity; closed-loop future covariance is double exterior derivative of pair momentum covariance",
            "fixed_state_local_tensor": "Rigorous conditional Stokes theorem under conditional mean-square continuity of the random vorticity two-form",
            "centered_C2_remainder": "Exact symmetric-loop scaling model; raw remainder starts at r^6 and metric-normalized remainder at r^2",
            "vorticity_dyad_tensor": "Exact 3D Navier-Stokes tensor identity; Kelvin Gram tensor is the viscous defect tensor of omega tensor omega",
            "backward_kelvin_infinitesimal_generator": "Exact NS cancellation for the backward-Ito packet operator on H^T omega",
            "backward_kelvin_covariance_transfer": "Exact one-mode NS shear calibration: backward covariance gains Gamma while omega omega^T loses Gamma",
            "forward_future_vs_backward_kelvin_identification": "Open-literal; causal time orientation/full-state identification must be written before equating the two banks",
            "generator_descent_criterion": "Exact lumpability/intertwining criterion L R = R Lbar",
            "actual_spatial_generator_descent": "Open-literal until the full stochastic Kelvin state/current-shape generator is written and shown to descend",
            "uniform_singular_tensor_remainder": "Open; no uniform approach-to-singularity control",
            "continuation_restart": "Open; no regularity conclusion",
        },
        "connected_one_mode_vector_bank": {
            "mean_residual_zero": zmat(connected_mean_horizon_residual(mean, B, tau, drift, diffusion, [a])),
            "second_moment_residual_zero": zmat(connected_second_moment_horizon_residual(second, B, tau, drift, diffusion, [a])),
            "covariance_residual_zero": zmat(connected_covariance_horizon_residual(mean, second, B, tau, drift, diffusion, [a])),
            "mean_square_transfer_residual_zero": zmat(connected_mean_square_horizon_residual(mean, B, tau, drift, diffusion, [a])),
            "cross_gamma": str(sp.simplify(Gamma[0, 1])),
            "covariance_matrix": smat(C),
            "gamma_matrix": smat(Gamma),
        },
        "pair_diagonal_branching": {
            "defect_equals_gamma": zmat(sp.simplify(pair_defect - pair_gamma)),
            "gamma_matrix": smat(pair_gamma),
        },
        "double_stokes": {
            "boundary_squared_zero": zmat(B1 * D2),
            "face_covariance": str(face_cov[0, 0]),
            "exact_gauge_projection_zero": zmat(gauge),
            "interpretation": "local future flux tensor is a diagonal density of (d box d) pair momentum covariance when the trace exists",
        },
        "generator_descent": {
            "hidden_shape_bad_descends": generator_descends(L_bad, labels),
            "hidden_shape_bad_obstruction": smat(generator_intertwining_residual(L_bad, labels)),
            "lumpable_good_descends": generator_descends(L_good, labels),
            "quotient_generator": smat(quotient_generator(L_good, labels)),
            "good_intertwining_residual_zero": zmat(generator_intertwining_residual(L_good, labels)),
        },
        "fixed_state_small_loop": {
            "raw_covariance": smat(raw),
            "metric_amplified_remainder": smat(amplified),
            "leading_normalized_remainder_order": "r^2 for centered C^2 loop packets",
            "analytic_condition": "conditional L2 continuity gives the area-squared tensor limit; C2 centered symmetry improves the raw remainder to r^6",
        },
        "ns_tensor_enstrophy": {
            "shear_dyad_residual_zero": zmat(shear_dyad_res),
            "abc_dyad_residual_zero": zmat(abc_dyad_res),
            "tensor_identity": "(dt+u.grad-nu Delta)(omega omega^T)=A omega omega^T + omega omega^T A^T - 2nu grad(omega) grad(omega)^T",
            "trace_identity": "one-half trace recovers the local enstrophy balance",
        },
        "exact_ns_backward_kelvin_shear": {
            "packet_mean_residual_zero": zmat(backward_mean_res),
            "covariance_tensor_residual_zero": zmat(backward_cov_res),
            "total_second_moment_residual_zero": zmat(backward_Q_res),
            "past_terminal_covariance_zero": sp.simplify(Czz_back.subs(t, t0)) == 0,
            "manifest_positive_factorization_residual_zero": sp.trigsimp(sp.simplify(Czz_back - Czz_manifest)) == 0,
            "manifest_factorization": "(k^2 exp(-2 nu k^2 t0)/2) (1-rho) (1+rho cos(2ky)), rho=exp(-2 nu k^2(t-t0))",
            "local_gamma_tensor": smat(shear_Gamma),
            "causal_orientation": "past terminal t0 < t for the backward Kelvin martingale; forcing T>t into the anti-diffusive operator is not a positive conditional-variance semigroup",
        },
        "packet_source_consistency": {
            "local_source_pullback_residual_zero": zmat(packet_pullback_res),
            "orientation_rank_one_cross_negative": sp.simplify(orient_gamma[0, 2]) != 0 and sp.simplify(orient_gamma[0, 2] / (2 * nu * sp.diff(scalar_mean, a) ** 2)) == -1,
            "orientation_gamma": smat(orient_gamma),
        },
        "frontier": {
            "new_exact_object": "full-state vector future covariance tensor with complete mixed carre-du-champ source",
            "localization_object": "diagonal density of double-Stokes pair covariance (d box d) K_s",
            "fixed_state_limit": "available conditionally from mean-square Stokes continuity",
            "true_generator_obstruction": "full stochastic Kelvin state must intertwine with the proposed reduced spatial/current-frame state; hidden shape/history cannot be dropped by declaration",
            "time_orientation_obstruction": "backward physical Kelvin martingale and forward abstract future-ancestry bank need a literal causal/time-reversal identification",
            "true_singular_obstruction": "uniform diagonal trace/remainder control and material metric/boundary/exit work up to candidate singular time",
        },
    }

    out = ROOT / "audit-results" / "future_covariance_tensor_report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(out)
    print("connected mean/second/cov/meansq residuals:", report["connected_one_mode_vector_bank"]["mean_residual_zero"], report["connected_one_mode_vector_bank"]["second_moment_residual_zero"], report["connected_one_mode_vector_bank"]["covariance_residual_zero"], report["connected_one_mode_vector_bank"]["mean_square_transfer_residual_zero"])
    print("pair diagonal defect equals Gamma:", report["pair_diagonal_branching"]["defect_equals_gamma"])
    print("double Stokes boundary2 / gauge:", report["double_stokes"]["boundary_squared_zero"], report["double_stokes"]["exact_gauge_projection_zero"])
    print("generator descent bad/good:", report["generator_descent"]["hidden_shape_bad_descends"], report["generator_descent"]["lumpable_good_descends"])
    print("NS dyad shear/ABC residuals:", report["ns_tensor_enstrophy"]["shear_dyad_residual_zero"], report["ns_tensor_enstrophy"]["abc_dyad_residual_zero"])
    print("backward shear mean/cov/Q/positivity:", report["exact_ns_backward_kelvin_shear"]["packet_mean_residual_zero"], report["exact_ns_backward_kelvin_shear"]["covariance_tensor_residual_zero"], report["exact_ns_backward_kelvin_shear"]["total_second_moment_residual_zero"], report["exact_ns_backward_kelvin_shear"]["manifest_positive_factorization_residual_zero"])
    print("packet source pullback residual:", report["packet_source_consistency"]["local_source_pullback_residual_zero"])
    print("fixed-state normalized remainder order:", report["fixed_state_small_loop"]["leading_normalized_remainder_order"])


if __name__ == "__main__":
    main()
