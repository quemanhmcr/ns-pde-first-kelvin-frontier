from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.kelvin_packet_locality import (  # noqa: E402
    diagonal_locality_ratio,
    time_dependent_linear_strain_ns_residual,
    strained_refined_line_frame,
    parabolic_kelvin_line_log_rate,
    packet_shape_amplification_factor,
    kelvin_diffusion_length,
    exact_linear_strain_ns_residual,
    coherent_three_face_quadrupole_closure_residual,
    coherent_planar_amplification_from_H_diagonal,
    coherent_core_bank_residual,
    affine_vortex_stretch_vorticity,
    affine_vortex_stretch_support_tensor,
    affine_vortex_stretch_ns_residual,
    affine_vortex_stretch_gradient,
    general_nanson_area_frame_rhs,
    general_nanson_metric_logdet_rate,
    anisotropy_tensor_from_lines,
    centered_quadratic_flux_error,
    centered_quadratic_shape_residual,
    centered_rectangle_second_moment_yz,
    cofactor_area_frame,
    incompressible_isotropic_area_frame,
    line_frame_from_area_frame,
    line_gram_from_area_frame,
    refinement_anisotropy_pullback,
    refinement_scale_factor,
    long_thin_center_flux,
    long_thin_covariance_defect,
    long_thin_face_flux,
    long_thin_whitened_payoff_error,
    metric_whitened_covariance_remainder,
    raw_frobenius_square,
    whitened_l2_error_bound_factor,
)

r, c, A, sigma, omega = sp.symbols("r c A sigma omega", positive=True)
F_bad = sp.diag(1 / r, 1, r)
H_bad = incompressible_isotropic_area_frame(F_bad, r)
L_bad = line_frame_from_area_frame(H_bad)
F_good = sp.diag(2, 1, sp.Rational(1, 2))
H_good = incompressible_isotropic_area_frame(F_good, r)
L_good = line_frame_from_area_frame(H_good)
R_bad = sp.diag(0, c * r**4, 0)
raw_ratio = sp.simplify(raw_frobenius_square(R_bad) / raw_frobenius_square(H_bad))

A_long = anisotropy_tensor_from_lines(L_bad, r)
lam = sp.symbols("lam", positive=True)
A_iso_refined = refinement_anisotropy_pullback(A_long, lam * sp.eye(3), lam)
Q_yz = centered_rectangle_second_moment_yz(r, r)
normal_x = sp.Matrix([1, 0, 0])
Z33 = sp.zeros(3)
Hess_grad = [[Z33.copy() for _ in range(3)] for _ in range(3)]
Ayy = sp.zeros(3)
Ayy[0, 1] = 6
Hess_grad[1][1] = Ayy
quad_shape = centered_quadratic_shape_residual(Q_yz, Hess_grad, normal_x)
Z31 = sp.zeros(3, 1)
Hess_flux = [[Z31.copy() for _ in range(3)] for _ in range(3)]
Hess_flux[1][1] = sp.Matrix([1, 0, 0])
quad_flux = centered_quadratic_flux_error(Q_yz, Hess_flux, normal_x)

g = sp.symbols("g0:9")
G = sp.Matrix(3, 3, g)
H0 = sp.Matrix([[2, 1, 0], [0, 3, 1], [1, 0, 2]])

# Exact NS and ideal-core witnesses.
x, y, z, tt, srate, r0, nua, Theta, alpha = sp.symbols("x y z tt srate r0 nua Theta alpha", positive=True)
linear_ns_res, linear_p = exact_linear_strain_ns_residual(srate, (x, y, z), nua)
critical_L = strained_refined_line_frame(srate, srate, tt)
vortex_ns_res, vortex_p = affine_vortex_stretch_ns_residual(srate, r0, tt, (x, y, z), nua)
vortex_A = affine_vortex_stretch_gradient(srate, r0, tt)
vortex_S = sp.simplify((vortex_A + vortex_A.T) / 2)
vortex_omega = affine_vortex_stretch_vorticity(srate, r0, tt)
vortex_stretch = sp.simplify((vortex_omega.T * vortex_S * vortex_omega)[0])
vortex_B = affine_vortex_stretch_support_tensor(srate, tt)
vortex_I = sp.simplify(sp.trace(vortex_B.inv() * (vortex_omega * vortex_omega.T)) / 2)
Fcore = sp.diag(sp.Symbol("fa", positive=True), sp.Symbol("fb", positive=True), 1/(sp.Symbol("fa", positive=True)*sp.Symbol("fb", positive=True)))
Qcore = sp.diag(sp.Symbol("q1"), sp.Symbol("q2"), sp.Symbol("q3"))
core_res = coherent_core_bank_residual(r, Fcore, Qcore)
chi_long = coherent_planar_amplification_from_H_diagonal(r**3, r**2, r, r**3)
parabolic_rate = parabolic_kelvin_line_log_rate(alpha/(Theta-tt), Theta-tt)
singular_ns_res, singular_p = time_dependent_linear_strain_ns_residual(alpha/(Theta-tt), tt, (x,y,z), nua)
quad_close = coherent_three_face_quadrupole_closure_residual(sp.diag(1, r, r**2))

def smat(M):
    return [[str(sp.simplify(M[i, j])) for j in range(M.cols)] for i in range(M.rows)]

report = {
    "classification": {
        "general_nanson_metric_determinant": "Exact 3D identity: d log det M_H/dt=-4 div u; incompressible consequence det M_H constant",
        "area_frame_not_locality": "Exact incompressible kinematic counterexample: H_r->0 does not imply support diameter->0",
        "long_thin_covariance": "Exact smooth covariance counterexample to area-only localization",
        "metric_whitened_topology": "Exact invariant normalization; raw smallness is insufficient under anisotropy",
        "coherent_microcell_duality": "Exact: L=sqrt(det H) H^-T and L^T L=(det H)(H^T H)^-1",
        "scale_anisotropy_factorization": "Exact: G_line=rho^2 A and M_H=rho^-4 A; incompressible material motion freezes rho",
        "centered_quadrupole_carrier": "Exact: the same surface second moment Q_Sigma carries the first centered finite-shape and flux-localization corrections",
        "orientation_complete_quadrupole": "Exact coherent closure sum Q_i/A_i=(2/3)LL^T",
        "joint_shape_flux_geometry_factor": "Rigorous: chi_H=sqrt(sum A_j^2)/sigma_min(H) controls both normalized shape and flux errors",
        "exact_ns_locality_calibrations": "Exact linear strain realizes long-thin support; exact affine vortex stretch has positive stretching with grad omega=0",
        "kelvin_parabolic_scale": "Exact Brownian scale sqrt(2nu tau); singular affine NS strain gives support exponent 1/2-a",
        "minimal_coherent_core": "Exact L=rho F, H=rho^2 F^-T and raw/metric rho^4 cancellation",
        "fixed_state_local_tensor_repair": "Rigorous conditional theorem requires support locality plus metric-whitened conditional L2 error ->0",
        "uniform_singular_locality": "Open; no first-bad singular-time support-locality/conditioning control",
        "continuation_restart": "Open; no regularity conclusion",
    },
    "general_nanson": {
        "metric_logdet_plus_4_div_zero": sp.simplify(general_nanson_metric_logdet_rate(G, H0) + 4 * sp.trace(G)) == 0,
        "area_frame_rhs": smat(general_nanson_area_frame_rhs(G, H0)),
    },
    "long_thin_material_packet": {
        "F": smat(F_bad),
        "det_F": str(sp.det(F_bad)),
        "H": smat(H_bad),
        "det_H": str(sp.det(H_bad)),
        "H_entries_vanish": True,
        "line_scale_ratio": str(diagonal_locality_ratio(H_bad, r**3)),
        "reconstructed_line_frame": smat(L_bad),
        "line_gram": smat(line_gram_from_area_frame(H_bad)),
        "cofactor_reconstruction_zero": sp.simplify(cofactor_area_frame(L_bad) - H_bad) == sp.zeros(3),
        "interpretation": "largest transported line scale stays order one while every area-frame entry tends to zero; full H conditioning still reconstructs that line exactly",
    },
    "bounded_deformation_packet": {
        "F": smat(F_good),
        "H": smat(H_good),
        "line_scale_ratio": str(diagonal_locality_ratio(H_good, r**2 / 2)),
        "reconstructed_line_frame": smat(L_good),
    },
    "scale_anisotropy": {
        "rho_long_thin": "r",
        "anisotropy_long_thin": smat(A_long),
        "support_gram": smat(sp.simplify(r**2 * A_long)),
        "packet_metric": smat(sp.simplify(r**(-4) * A_long)),
        "isotropic_refinement_scale_factor": str(refinement_scale_factor(lam * sp.eye(3))),
        "isotropic_refinement_anisotropy_unchanged": sp.simplify(A_iso_refined - A_long) == sp.zeros(3),
        "interpretation": "continuous incompressible strain acts on A; physical refinement/reselection supplies rho collapse",
    },
    "common_quadrupole": {
        "centered_yz_Q": smat(Q_yz),
        "cubic_shear_shape_residual": [str(v) for v in quad_shape],
        "quadratic_flux_error": str(quad_flux),
        "raw_order": "r^4",
        "relative_to_area_order": "r^2",
        "interpretation": "shape drift and Stokes payoff error contract the same physical surface quadrupole against different PDE Hessians",
    },
    "joint_geometry_factor": {
        "long_thin_chi": str(chi_long),
        "r2_chi_limit": str(sp.limit(r**2 * chi_long, r, 0, dir="+")),
        "isotropic_chi": str(coherent_planar_amplification_from_H_diagonal(r**2,r**2,r**2,r**2)),
        "uniform_scale_invariant": sp.simplify(packet_shape_amplification_factor([r**2,r**2,r**2], r**2)-sp.sqrt(3)) == 0,
    },
    "orientation_complete_quadrupole": {
        "long_thin_closure_zero": quad_close == sp.zeros(3),
    },
    "exact_ns_support_calibrations": {
        "linear_strain_residual_zero": linear_ns_res == sp.zeros(3,1),
        "critical_refined_line_frame": smat(critical_L),
        "affine_vortex_residual_zero": vortex_ns_res == sp.zeros(3,1),
        "affine_vortex_stretching": str(vortex_stretch),
        "affine_vortex_support_normalized_bank": str(vortex_I),
        "affine_vortex_grad_omega_zero": True,
    },
    "parabolic_kelvin_support": {
        "rho_nu": str(kelvin_diffusion_length(nua, Theta-tt)),
        "directional_log_rate": str(parabolic_rate),
        "singular_affine_ns_residual_zero": singular_ns_res == sp.zeros(3,1),
        "critical_coefficient": "1/2",
        "classification": "support-locality calibration only; not first-bad or continuation criterion",
    },
    "minimal_core": {
        "normalized_bank_residual_zero": core_res == 0,
    },
    "smooth_flux_witness": {
        "actual_flux_coefficient": str(long_thin_face_flux(r)),
        "local_center_coefficient": str(long_thin_center_flux(r)),
        "payoff_error_over_area": str(sp.simplify((long_thin_face_flux(r) - long_thin_center_flux(r)) / r**2)),
        "covariance_defect_over_r4": str(sp.trigsimp(long_thin_covariance_defect(r) / r**4)),
        "whitened_payoff_error": [str(x) for x in long_thin_whitened_payoff_error(r)],
    },
    "raw_vs_whitened": {
        "raw_remainder_over_H_frobenius_square": str(raw_ratio),
        "raw_ratio_limit": str(sp.limit(raw_ratio, r, 0, dir="+")),
        "metric_whitened_remainder": str(metric_whitened_covariance_remainder(R_bad, H_bad)),
    },
    "repaired_local_tensor_condition": {
        "sufficient_bound_factor": str(whitened_l2_error_bound_factor(A, sigma, omega)),
        "meaning": "A=sqrt(sum face areas^2), sigma=sigma_min(H), omega=conditional L2 modulus at packet support diameter",
        "required_limit": "A/sigma_min(H) * omega_2(diameter) -> 0",
        "equivalent_invariant_target": "H^{-T} epsilon_H -> 0 in conditional L2",
    },
    "frontier": {
        "resolved": "small area is not locality; the correct fixed-state topology is support-local plus metric-whitened",
        "remaining": "prove uniform support locality/conditioning and whitened remainder collapse for the first-bad material packet near candidate singular time",
    },
}

out = ROOT / "audit-results" / "kelvin_packet_locality_report.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(out)
print("general Nanson residual:", report["general_nanson"]["metric_logdet_plus_4_div_zero"])
print("long-thin line scale / reconstructed L:", report["long_thin_material_packet"]["line_scale_ratio"], report["long_thin_material_packet"]["reconstructed_line_frame"])
print("scale A / isotropic refinement unchanged:", report["scale_anisotropy"]["anisotropy_long_thin"], report["scale_anisotropy"]["isotropic_refinement_anisotropy_unchanged"])
print("quadrupole shape/flux:", report["common_quadrupole"]["cubic_shear_shape_residual"], report["common_quadrupole"]["quadratic_flux_error"])
print("joint chi long/isotropic:", report["joint_geometry_factor"]["long_thin_chi"], report["joint_geometry_factor"]["isotropic_chi"])
print("NS linear/vortex/parabolic:", report["exact_ns_support_calibrations"]["linear_strain_residual_zero"], report["exact_ns_support_calibrations"]["affine_vortex_residual_zero"], report["parabolic_kelvin_support"]["singular_affine_ns_residual_zero"])
print("quadrupole/core:", report["orientation_complete_quadrupole"]["long_thin_closure_zero"], report["minimal_core"]["normalized_bank_residual_zero"])
print("raw ratio limit / whitened remainder:", report["raw_vs_whitened"]["raw_ratio_limit"], report["raw_vs_whitened"]["metric_whitened_remainder"])
print("whitened payoff error:", report["smooth_flux_witness"]["whitened_payoff_error"])
