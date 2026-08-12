from __future__ import annotations

import json
from pathlib import Path
import sys
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.kelvin_shape_generator import (  # noqa: E402
    anchor_relative_common_noise_covariance,
    common_wiener_covariance,
    cubic_heat_shear_ns_residual,
    cubic_shear_rectangle_shape_residual,
    cubic_shear_residual_from_second_moment,
    oriented_rectangle_area_vector_yz,
    width_surface_shear_area_rate,
    width_surface_even_moment,
    width_surface_area,
    polynomial_heat_shear_residual,
    polynomial_heat_shear,
    moment_hierarchy_shear_rate_difference,
    legendre_width_density,
    packet_shape_residual_matrix,
    rectangle_oriented_second_moment_yy,
    scaled_cubic_shape_residual,
)

OUT = ROOT / "audit-results" / "kelvin_shape_generator_report.json"
OUT.parent.mkdir(exist_ok=True)

nu, t, r, b0, c0 = sp.symbols("nu t r b0 c0", positive=True)
A = common_wiener_covariance(5, 3, nu)
Ar = anchor_relative_common_noise_covariance(4, 3, nu)
expected_Ar = sp.zeros(15)
expected_Ar[:3, :3] = 2 * nu * sp.eye(3)

h1 = oriented_rectangle_area_vector_yz(1, 1)
h2 = oriented_rectangle_area_vector_yz(2, sp.Rational(1, 2))
e1 = cubic_shear_rectangle_shape_residual(1, 1, t, nu)
e2 = cubic_shear_rectangle_shape_residual(2, sp.Rational(1, 2), t, nu)
raw = scaled_cubic_shape_residual(r, b0, c0)
ref = cubic_shear_residual_from_second_moment(b0, c0)
h_scaled = oriented_rectangle_area_vector_yz(r * b0, r * c0)

y = sp.Symbol("y", real=True)
eps = sp.Rational(1, 2)
w0 = sp.Integer(1)
w1 = legendre_width_density(4, y, eps)
U5 = polynomial_heat_shear(5, y, t, nu)
U5y = sp.diff(U5, y)
rate5_0 = width_surface_shear_area_rate(U5y, w0, y)
rate5_1 = width_surface_shear_area_rate(U5y, w1, y)
hierarchy = []
for m in range(1, 5):
    degree = 2 * m + 1
    wm = legendre_width_density(2 * m, y, eps)
    lower_equal = all(
        sp.simplify(width_surface_even_moment(wm, y, 2*j)-width_surface_even_moment(w0, y, 2*j)) == 0
        for j in range(m)
    )
    Uy = sp.diff(polynomial_heat_shear(degree, y, t, nu), y)
    diff = sp.simplify(width_surface_shear_area_rate(Uy, wm, y)[1]-width_surface_shear_area_rate(Uy, w0, y)[1])
    hierarchy.append({
        "m": m,
        "degree": degree,
        "heat_residual_zero": polynomial_heat_shear_residual(degree, y, t, nu) == 0,
        "lower_even_moments_equal": lower_equal,
        "generator_difference": str(diff),
        "formula_matches": sp.simplify(diff-moment_hierarchy_shear_rate_difference(m, eps)) == 0,
    })


def smat(M: sp.MatrixBase) -> list[list[str]]:
    return [[str(sp.simplify(M[i, j])) for j in range(M.cols)] for i in range(M.rows)]


def svec(v: sp.MatrixBase) -> list[str]:
    return [str(sp.simplify(v[i])) for i in range(v.rows)]

report = {
    "classification": {
        "common_noise_current_shape_state": "Exact backward-Ito cylinder/current-shape kinematics under one uniform Wiener motion",
        "relative_shape_quadratic_variation": "Exact zero; shape is finite variation after anchoring",
        "finite_surface_area_frame_law": "Exact incompressible material-surface identity Hdot=-(grad u(X))^T H+E_shape",
        "finite_scale_xH_descent": "False in general; exact NS cubic-shear counterexample at identical anchor and area vector",
        "finite_scale_xHQ_descent": "False in general; exact quintic heat-shear counterexample at identical area and quadrupole",
        "finite_moment_closure": "False universally; Legendre P_2m perturbations plus exact heat shears U_2m+1 expose every next unresolved even moment",
        "shape_residual_type": "Physical finite-variation strain-gradient/surface-shape deformation current; not q.v., pressure, or S^int",
        "infinitesimal_xH_limit": "Exact differential-area Nanson law; centered cubic-shear residual is raw r^4 and relative-to-area r^2",
        "uniform_singular_shape_collapse": "Open; no uniform first-bad r->0 control near a candidate singular time",
        "continuation_restart": "Open; no regularity conclusion",
    },
    "common_noise": {
        "five_point_covariance_rank": A.rank(),
        "point_space_dimension": A.rows,
        "common_block_0_3": smat(A[:3, 9:12]),
        "anchor_relative_only_anchor_noise": sp.simplify(Ar - expected_Ar) == sp.zeros(15),
        "anchor_covariance": smat(Ar[:3, :3]),
        "all_relative_covariance_zero": Ar[3:, 3:] == sp.zeros(12),
        "anchor_relative_cross_zero": Ar[:3, 3:] == sp.zeros(3, 12),
    },
    "exact_ns_cubic_shear": {
        "profile": "u=(y^3+6 nu t y,0,0)",
        "ns_residual": str(cubic_heat_shear_ns_residual(sp.Symbol("y"), t, nu)),
        "pressure": "constant",
        "physical_type": "exact heat shear; nonlinearity vanishes identically",
    },
    "finite_surface_counterexample": {
        "same_anchor": True,
        "same_area_vector": h1 == h2,
        "area_vector": svec(h1),
        "rectangle_halfwidths": [["1", "1"], ["2", "1/2"]],
        "shape_residual_1": svec(e1),
        "shape_residual_2": svec(e2),
        "generator_difference": svec(sp.simplify(e2 - e1)),
        "same_x_h_different_hdot": e1 != e2,
        "second_moment_yy_1": str(rectangle_oriented_second_moment_yy(1, 1)),
        "second_moment_yy_2": str(rectangle_oriented_second_moment_yy(2, sp.Rational(1, 2))),
        "residual_equals_minus3_second_moment": sp.simplify(e1 - cubic_shear_residual_from_second_moment(1, 1)) == sp.zeros(3, 1),
    },
    "quintic_same_area_quadrupole": {
        "profile": str(U5),
        "heat_residual_zero": polynomial_heat_shear_residual(5, y, t, nu) == 0,
        "same_area": width_surface_area(w1, y) == width_surface_area(w0, y),
        "same_second_moment": width_surface_even_moment(w1, y, 2) == width_surface_even_moment(w0, y, 2),
        "fourth_moment_difference": str(sp.simplify(width_surface_even_moment(w1, y, 4)-width_surface_even_moment(w0, y, 4))),
        "generator_difference": svec(sp.simplify(rate5_1-rate5_0)),
    },
    "moment_hierarchy": hierarchy,
    "scale_collapse": {
        "raw_residual": svec(raw),
        "raw_r4_residual_zero": sp.simplify(raw - r**4 * ref) == sp.zeros(3, 1),
        "area_vector": svec(h_scaled),
        "relative_nonzero_component": str(sp.simplify(raw[1] / h_scaled[0])),
        "relative_order": "r^2",
        "interpretation": "centered finite-surface strain-gradient correction vanishes at fixed smooth state but is not uniformly controlled near singular time",
    },
    "orientation_complete_packet": {
        "same_H_possible": "4 I_3 in the calibration",
        "residual_packet_1": smat(packet_shape_residual_matrix(e1)),
        "residual_packet_2": smat(packet_shape_residual_matrix(e2)),
        "same_H_different_packet_drift": packet_shape_residual_matrix(e1) != packet_shape_residual_matrix(e2),
        "difference": smat(packet_shape_residual_matrix(sp.simplify(e2 - e1))),
    },
    "frontier": {
        "resolved_generator_question": "the literal smooth-current state is anchor plus relative embedding; common noise acts only on the anchor and shape is finite variation",
        "finite_scale_reduction_answer": "(x,H) is not an exact finite-scale Markov quotient; E_shape depends on higher surface geometry",
        "infinitesimal_answer": "differential area elements do close on (x,H) with Nanson drift",
        "first_missing_shape_state": "oriented surface second moment/quadrupole in the centered cubic-shear calibration, but no finite moment hierarchy closes universally",
        "remaining_shape_problem": "control the strain-gradient shape hierarchy uniformly as first-bad packet scale collapses",
    },
}

OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(OUT)
print("common noise rank / anchor-only:", report["common_noise"]["five_point_covariance_rank"], report["common_noise"]["anchor_relative_only_anchor_noise"])
print("cubic NS residual:", report["exact_ns_cubic_shear"]["ns_residual"])
print("same h / different hdot:", report["finite_surface_counterexample"]["same_area_vector"], report["finite_surface_counterexample"]["same_x_h_different_hdot"])
print("shape residuals:", report["finite_surface_counterexample"]["shape_residual_1"], report["finite_surface_counterexample"]["shape_residual_2"])
print("quintic same area/Q, dH:", report["quintic_same_area_quadrupole"]["same_area"], report["quintic_same_area_quadrupole"]["same_second_moment"], report["quintic_same_area_quadrupole"]["generator_difference"])
print("moment hierarchy all exact:", all(x["heat_residual_zero"] and x["lower_even_moments_equal"] and x["formula_matches"] for x in report["moment_hierarchy"]))
print("scale raw r4 / relative:", report["scale_collapse"]["raw_r4_residual_zero"], report["scale_collapse"]["relative_nonzero_component"])
