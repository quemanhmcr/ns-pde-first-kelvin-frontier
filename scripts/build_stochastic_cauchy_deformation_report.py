from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.ancestry_resolution_kernel import (  # noqa: E402
    vector_total_covariance_decomposition,
)
from pde_audit.cycle_selector import two_cycle_library  # noqa: E402
from pde_audit.deformation_current_pair_coupling import (  # noqa: E402
    selected_deformation_pair_decomposition,
    selected_deformation_pair_dyad_residual,
    spatial_fiber_boundary,
    spatial_fiber_boundary_factorization_residual,
    spatial_fiber_current_map,
    spatial_fiber_pair_boundary_factorization_residual,
    tangent_cochain_covariance,
    tangent_projection_residual,
)
from pde_audit.future_covariance_tensor import (  # noqa: E402
    connected_covariance_horizon_residual,
    connected_mean_horizon_residual,
    connected_second_moment_horizon_residual,
    product_pair_diagonal_defect,
    vector_carre_du_champ,
)
from pde_audit.kelvin_packet_locality import (  # noqa: E402
    affine_vortex_stretch_gradient,
    affine_vortex_stretch_ns_residual,
)
from pde_audit.kelvin_shape_generator import (  # noqa: E402
    cubic_shear_rectangle_shape_residual,
    oriented_rectangle_area_vector_yz,
)
from pde_audit.stochastic_cauchy_deformation import (  # noqa: E402
    affine_vortex_cauchy_z_residual,
    affine_vortex_total_bank_envelope_residual,
    cauchy_packet_metric_duality_residual,
    column_vectorize,
    column_partial_trace_vectorized_covariance,
    deformation_covariance_leading_projection_residual,
    deformation_mean_horizon_residual,
    deformation_second_moment_horizon_residual,
    one_mode_shear_deformation_mean_coefficient,
    one_mode_shear_deformation_second_coefficient,
    one_mode_shear_deformation_variance,
    one_mode_shear_deformation_variance_at_symmetry,
    one_mode_shear_second_moment,
    one_mode_shear_terminal_headroom,
    one_mode_shear_terminal_supremum,
    projected_deformation_covariance_horizon_residual,
    projected_deformation_covariance_leading_tensor,
    reverse_age_horizon_operator_matrix,
    vectorized_deformation_covariance_horizon_residual,
    vectorized_deformation_covariance_leading_tensor,
    vectorized_horizon_connection,
)

x, y, z, t, s, h, nu, k, a, r0 = sp.symbols(
    "x y z t s h nu k a r0", positive=True
)
rho = sp.symbols("rho", positive=True)
alpha = nu * k**2

# Fixed-past bank quantities.
W = one_mode_shear_terminal_supremum(s, nu, k)
Q = one_mode_shear_second_moment(y, t, s, nu, k)
headroom = one_mode_shear_terminal_headroom(y, t, s, nu, k)

# Same-replica metric duality calibration.
D_generic = sp.Matrix([[2, 1], [1, 1]])

# Exact one-mode shear deformation covariance calibration.
U = sp.exp(-alpha * t) * sp.cos(k * y)
Uy = sp.diff(U, y)
velocity = sp.Matrix([U, 0])
A = sp.Matrix([[0, Uy], [0, 0]])
mean_c = one_mode_shear_deformation_mean_coefficient(y, t, h, nu, k)
second_c = one_mode_shear_deformation_second_coefficient(y, t, h, nu, k)
variance = one_mode_shear_deformation_variance(y, t, h, nu, k)
mean_D = sp.Matrix([[1, 0], [mean_c, 1]])
R = sp.Matrix([[1, mean_c], [mean_c, 1 + second_c]])
C_gram = sp.simplify(R - mean_D * mean_D.T)
Hmean = reverse_age_horizon_operator_matrix(mean_D, h, t, velocity, nu, (x, y))
HR = reverse_age_horizon_operator_matrix(R, h, t, velocity, nu, (x, y))
HC = reverse_age_horizon_operator_matrix(C_gram, h, t, velocity, nu, (x, y))
dmean = [sp.diff(mean_D, x), sp.diff(mean_D, y)]

E21 = sp.Matrix([[0, 0], [1, 0]])
v21 = column_vectorize(E21)
Sigma = sp.simplify(variance * v21 * v21.T)
HSigma = reverse_age_horizon_operator_matrix(Sigma, h, t, velocity, nu, (x, y))

# Cross-module specialization to the repo's existing connected vector covariance theorem.
mean_vec = column_vectorize(mean_D)
second_vec = sp.simplify(Sigma + mean_vec * mean_vec.T)
B_horizon = vectorized_horizon_connection(A)
B_connected = -B_horizon.T
reverse_drift = sp.Matrix([-1, -U, 0])
reverse_diffusion = sp.diag(0, 2 * nu, 2 * nu)
reverse_coords = (t, x, y)
connected_mean_zero = connected_mean_horizon_residual(
    mean_vec, B_connected, h, reverse_drift, reverse_diffusion, reverse_coords
) == sp.zeros(4, 1)
connected_second_zero = connected_second_moment_horizon_residual(
    second_vec, B_connected, h, reverse_drift, reverse_diffusion, reverse_coords
) == sp.zeros(4)
connected_covariance_zero = connected_covariance_horizon_residual(
    mean_vec, second_vec, B_connected, h, reverse_drift, reverse_diffusion, reverse_coords
) == sp.zeros(4)
t1, x1, y1, t2, x2, y2 = sp.symbols("t1 x1 y1 t2 x2 y2")
pair_defect = product_pair_diagonal_defect(
    mean_vec,
    reverse_coords,
    (t1, x1, y1),
    (t2, x2, y2),
    reverse_drift,
    reverse_diffusion,
)
reverse_gamma = vector_carre_du_champ(mean_vec, reverse_diffusion, reverse_coords)
pair_defect_zero = sp.simplify(pair_defect - reverse_gamma) == sp.zeros(4)

# Exact vector law-of-total-covariance split for an explicit reduced/full lift.
p_red = sp.symbols("p_red", real=True)
Dbar_hidden_1 = sp.Matrix([[1, sp.Symbol("a_red")], [0, 1]])
Dbar_hidden_2 = sp.Matrix([[1, sp.Symbol("c_red")], [sp.Symbol("d_red"), 1]])
hidden_means = sp.Matrix([
    list(column_vectorize(Dbar_hidden_1)),
    list(column_vectorize(Dbar_hidden_2)),
])
S1 = sp.diag(sp.Symbol("s1_red"), 0, sp.Symbol("q1_red"), 0)
S2 = sp.diag(sp.Symbol("s2_red"), 0, sp.Symbol("q2_red"), 0)
reduction_kernel = sp.Matrix([[p_red, 1 - p_red]])
averaged_intrinsic, resolution_cov, reduced_total = vector_total_covariance_decomposition(
    reduction_kernel, hidden_means, [S1, S2]
)
resolution_split_zero = sp.simplify(
    reduced_total[0] - averaged_intrinsic[0] - resolution_cov[0]
) == sp.zeros(4)
projected_resolution_split_zero = sp.simplify(
    column_partial_trace_vectorized_covariance(reduced_total[0], 2)
    - column_partial_trace_vectorized_covariance(averaged_intrinsic[0], 2)
    - column_partial_trace_vectorized_covariance(resolution_cov[0], 2)
) == sp.zeros(2)

# General short-horizon tensor/projection audit with symbolic spatial derivatives.
g11, g12, g21, g22, q11, q12, q21, q22 = sp.symbols(
    "g11 g12 g21 g22 q11 q12 q21 q22"
)
dAx = sp.Matrix([[g11, g12], [g21, g22]])
dAy = sp.Matrix([[q11, q12], [q21, q22]])
full_leading = vectorized_deformation_covariance_leading_tensor([dAx, dAy], nu, h)
projected_leading = projected_deformation_covariance_leading_tensor([dAx, dAy], nu, h)

# Exact affine-vortex NS calibration: spatially uniform gradient means zero source.
A_aff = affine_vortex_stretch_gradient(a, r0, t)
ns_aff, _ = affine_vortex_stretch_ns_residual(a, r0, t, (x, y, z), nu)
aff_derivatives = [sp.diff(A_aff, q) for q in (x, y, z)]
aff_leading = vectorized_deformation_covariance_leading_tensor(aff_derivatives, nu, h)

shear_mean0 = one_mode_shear_deformation_mean_coefficient(0, t, h, nu, k)
shear_second0 = one_mode_shear_deformation_second_coefficient(0, t, h, nu, k)
shear_var0 = one_mode_shear_deformation_variance_at_symmetry(t, h, nu, k)

# Literal current-fiber / selected-pair coupling audit.
B_cycle, K_cycle = two_cycle_library()
P_cycle = K_cycle * sp.diag(1, 0)
D_coupling = sp.Matrix([[1, 2], [0, 1]])
fiber_boundary_res = spatial_fiber_boundary_factorization_residual(B_cycle, P_cycle, D_coupling)
pair_boundary_res = spatial_fiber_pair_boundary_factorization_residual(B_cycle, P_cycle, D_coupling)
Bfiber = spatial_fiber_boundary(B_cycle, 2)
Tfiber = spatial_fiber_current_map(P_cycle, D_coupling)
closed_current_boundary_zero = sp.simplify(Bfiber * Tfiber) == sp.zeros(Bfiber.rows, Tfiber.cols)

e1, e2, a1, a2 = sp.symbols("e1 e2 a1 a2")
e_ref = sp.Matrix([e1, e2])
alpha_ref = sp.Matrix([a1, a2])
local_projection_zero = tangent_projection_residual(D_coupling, e_ref) == sp.zeros(2, 1)
local_cochain_leading = tangent_cochain_covariance(full_leading, e_ref, alpha_ref)
local_cochain_expected = sp.simplify(
    sp.Rational(2, 3) * nu * h**3 * (
        (alpha_ref.T * dAx * e_ref)[0] ** 2
        + (alpha_ref.T * dAy * e_ref)[0] ** 2
    )
)
local_cochain_leading_zero = sp.simplify(local_cochain_leading - local_cochain_expected) == 0

P1 = sp.Matrix([[1, 0], [0, 0]])
P2 = sp.Matrix([[0, 0], [0, 1]])
D1 = sp.Matrix([[1, 1], [0, 1]])
D2 = sp.Matrix([[1, 0], [2, 1]])
pair_sector = selected_deformation_pair_decomposition(P1, D1, P2, D2)
_, pair_selector_lift, pair_deformation_lift, pair_cross_lift = pair_sector.pair_lift_parts()
pair_sector_residual_zero = selected_deformation_pair_dyad_residual(P1, D1, P2, D2) == sp.zeros(16)
shared_sector = selected_deformation_pair_decomposition(P1, D1, P1, D2)
_, shared_selector_lift, shared_deformation_lift, shared_cross_lift = shared_sector.pair_lift_parts()

h_surface_1 = oriented_rectangle_area_vector_yz(1, 1)
h_surface_2 = oriented_rectangle_area_vector_yz(2, sp.Rational(1, 2))
shape_current_1 = cubic_shear_rectangle_shape_residual(1, 1, t, nu)
shape_current_2 = cubic_shear_rectangle_shape_residual(2, sp.Rational(1, 2), t, nu)

report = {
    "status": {
        "reverse_age_state": "Exact identity",
        "mean_second_moment_covariance_laws": "Exact identity",
        "pair_and_projection_identities": "Exact identity",
        "connected_covariance_theorem_specialization": "Exact identity",
        "vector_total_covariance_given_lift": "Exact identity",
        "current_fiber_boundary_and_pair_coupling": "Exact identity",
        "fixed_local_current_cochain_projection": "Exact identity",
        "selected_deformation_pair_sector_split": "Exact identity",
        "finite_current_D_only_descent": "Audited calibration / rigorous no-descent consequence",
        "short_horizon_asymptotic": "Rigorous consequence for locally smooth Navier--Stokes coefficients",
        "one_mode_shear": "Audited calibration",
        "affine_vortex": "Audited calibration",
        "future_remaining_bank_identification": "Open-literal",
        "actual_reduced_ancestry_lift_identification": "Open-literal",
        "selected_support_alignment": "Conjectural bridge / Open-literal",
        "restart_continuation_regularity": "Open; no theorem claimed",
    },
    "reverse_age_geometry": {
        "pathwise_state": "dX=-u(X,t-sigma) dsigma+sqrt(2nu)dW; D_sigma=D(grad u)^T; [D,D]=0 pathwise",
        "pathwise_vectorized_connection": "K_path=(grad u) tensor I",
        "horizon_operator": "H_h=partial_h+partial_t+u.grad-nu Delta",
        "horizon_mean_law": "H_h Dbar=(grad u)^T Dbar",
        "horizon_vectorized_connection": "B=I tensor (grad u)^T",
        "physical_typing": "finite-variation deformation dispersion generated by Brownian anchor sampling; not direct pathwise deformation q.v.",
    },
    "covariance_law": {
        "full": "Sigma_D=Cov(vec D); H_h Sigma_D=B Sigma_D+Sigma_D B^T+Gamma_D^vec",
        "carre_du_champ": "Gamma_D^vec=2nu sum_mu vec(partial_mu Dbar) vec(partial_mu Dbar)^T",
        "projection": "C_D^Gram=ptr_col Sigma_D=E[D D^T]-Dbar Dbar^T",
        "projected_law": "H_h C_D^Gram=A^T C_D^Gram+C_D^Gram A+2nu sum_mu (partial_mu Dbar)(partial_mu Dbar)^T",
        "pair": "Sigma_D=(1/2)E[(vec D1-vec D2)(vec D1-vec D2)^T]; C_D^Gram is its row-Gram projection",
        "packet_metric": "rho^4 E[M_H]=Dbar Dbar^T+C_D^Gram on the stochastic replica ensemble",
    },
    "existing_theorem_specialization": {
        "reverse_generator": "L_rev=-partial_t-u.grad+nu Delta",
        "connection_identification": "B_conn=-(I tensor (grad u)^T)^T",
        "connected_mean_residual_zero": bool(connected_mean_zero),
        "connected_second_moment_residual_zero": bool(connected_second_zero),
        "connected_covariance_residual_zero": bool(connected_covariance_zero),
        "pair_diagonal_defect_minus_gamma_zero": bool(pair_defect_zero),
        "typing": "same covariance algebra/pair source already exists; Cauchy deformation payload, connection ordering, and causal-past clock are the physical specialization",
    },
    "reduced_state_covariance_split": {
        "identity": "Sigma_D^red=R Sigma_D+Cov_R(Dbar_vec)",
        "full_split_residual_zero": bool(resolution_split_zero),
        "row_gram_partial_trace_split_residual_zero": bool(projected_resolution_split_zero),
        "intrinsic_sector": "R Sigma_D: averaged full-state same-clock deformation covariance",
        "resolution_sector": "Cov_R(Dbar_vec): additional covariance created by hiding full-state deformation means",
        "actual_lift": "Open-literal: the programme-specific ancestry kernel/state semantics are not constructed here",
    },
    "short_horizon": {
        "full_vectorized": "Sigma_D=(2nu/3)h^3 sum_mu vec((partial_mu grad u)^T) outer vec((partial_mu grad u)^T)+O(h^4)",
        "row_gram_projection": "C_D^Gram=(2nu/3)h^3 sum_mu (partial_mu grad u)^T(partial_mu grad u)+O(h^4)",
        "candidate_verdict": "the proposed 3x3 expression is correct for C_D^Gram, not for full 9x9 Sigma_D in 3D",
        "symbolic_projection_residual_zero": bool(
            deformation_covariance_leading_projection_residual([dAx, dAy], nu, h)
            == sp.zeros(2)
        ),
        "full_leading_shape": list(full_leading.shape),
        "projected_leading_shape": list(projected_leading.shape),
    },
    "one_mode_shear": {
        "mean_horizon_residual_zero": bool(
            deformation_mean_horizon_residual(mean_D, Hmean, A) == sp.zeros(2)
        ),
        "second_moment_horizon_residual_zero": bool(
            deformation_second_moment_horizon_residual(R, HR, A) == sp.zeros(2)
        ),
        "projected_covariance_horizon_residual_zero": bool(
            projected_deformation_covariance_horizon_residual(C_gram, HC, A, dmean, nu)
            == sp.zeros(2)
        ),
        "vectorized_covariance_horizon_residual_zero": bool(
            vectorized_deformation_covariance_horizon_residual(Sigma, HSigma, A, dmean, nu)
            == sp.zeros(4)
        ),
        "symmetry_anchor_mean_coefficient": str(shear_mean0),
        "symmetry_anchor_second_coefficient": str(shear_second0),
        "symmetry_anchor_variance": str(shear_var0),
        "small_h_onset": "Var(c_h)=(2nu/3)|partial_y U_y|^2 h^3+O(h^4)",
        "referees": "positive source sign, horizon transpose/order, and coefficient 2nu/3",
        "selected_vs_replica": "at y=0 deterministic material deformation is I while stochastic replica metric has positive C_D^Gram",
    },
    "affine_vortex": {
        "ns_residual_zero": bool(sp.simplify(ns_aff) == sp.zeros(3, 1)),
        "cauchy_z_residual_zero": bool(affine_vortex_cauchy_z_residual(a, r0, s, t) == 0),
        "terminal_envelope_residual_zero": bool(
            affine_vortex_total_bank_envelope_residual(a, r0, s, t) == 0
        ),
        "spatial_gradient_covariance_source_zero": bool(aff_leading == sp.zeros(9)),
        "interpretation": "spatially uniform grad u permits deformation/stretching but no anchor-induced deformation-dispersion source",
    },
    "fixed_past_bank": {
        "terminal_supremum": str(W),
        "second_moment": str(Q),
        "terminal_directional_headroom": str(headroom),
        "metric_duality_residual_zero": bool(
            cauchy_packet_metric_duality_residual(D_generic, rho) == sp.zeros(2)
        ),
    },
    "physical_current_pair_coupling": {
        "local_map": "T(P,D)=P tensor D^T: selector/current coefficients and spatial tangent deformation are distinct factors",
        "boundary_factorization_residual_zero": bool(fiber_boundary_res == sp.zeros(*fiber_boundary_res.shape)),
        "closed_selected_current_boundary_zero": bool(closed_current_boundary_zero),
        "pair_boundary_factorization_residual_zero": bool(pair_boundary_res == sp.zeros(*pair_boundary_res.shape)),
        "local_tangent_projection_residual_zero": bool(local_projection_zero),
        "short_h_local_cochain_projection_residual_zero": bool(local_cochain_leading_zero),
        "short_h_local_cochain_law": "Var(alpha^T D_h^T e)=(2nu/3)h^3 sum_mu [alpha^T(partial_mu grad u)e]^2+O(h^4)",
        "typing": "deformation transports the spatial fiber of a closed current; it is not a boundary/interface seam and has no direct pathwise Brownian q.v.",
    },
    "selected_pair_sector_split": {
        "identity": "T(P1,D1)-T(P2,D2)=T(P1-P2,D1)+T(P2,D1-D2)",
        "pair_lift_residual_zero": bool(pair_sector_residual_zero),
        "replica_dependent_selector_pair_lift_nonzero": bool(pair_selector_lift != sp.zeros(16)),
        "replica_dependent_deformation_pair_lift_nonzero": bool(pair_deformation_lift != sp.zeros(16)),
        "replica_dependent_cross_pair_lift_nonzero": bool(pair_cross_lift != sp.zeros(16)),
        "shared_selector_lift_zero": bool(shared_selector_lift == sp.zeros(16)),
        "shared_deformation_lift_nonzero": bool(shared_deformation_lift != sp.zeros(16)),
        "shared_cross_lift_zero": bool(shared_cross_lift == sp.zeros(16)),
        "typing": "selector, deformation, and cross tensor-lift terms are distinct literal pair-current content",
    },
    "finite_current_no_descent": {
        "exact_ns_calibration": "u=(y^3+6nu t y,0,0)",
        "same_area_vector": bool(h_surface_1 == h_surface_2),
        "same_initial_local_deformation": "D=I at zero reverse age for both surfaces at the same anchor",
        "shape_current_1": str(shape_current_1),
        "shape_current_2": str(shape_current_2),
        "shape_current_difference": str(sp.simplify(shape_current_2 - shape_current_1)),
        "verdict": "D is exact local tangent transport but does not close the finite Kelvin-current state; full shape R(.) or an equivalent nontruncated state is required",
    },
    "ledger_placement": {
        "same_clock_face": "Sigma_D is the existing connected vector covariance theorem specialized to reverse-age Cauchy deformation; C_D^Gram is its row-Gram projection",
        "future_remaining_horizon": "not identified: causal past h=t-s is distinct from future remaining tau=Theta-t",
        "resolution_covariance": "given a lift, reduction adds Cov_R(Dbar_vec) to averaged intrinsic Sigma_D; it does not retype intrinsic deformation covariance as resolution",
        "selected_current_projection": "for a shared frozen selector, Sigma_D transports inside the closed-current spatial fiber; replica-dependent selectors add separate selector and cross pair sectors",
        "finite_current_state": "local D/current projection is exact but D-only finite-current descent is false in exact NS; actual stochastic shape/cochain lift remains Open-literal",
        "S_int": "no identification with S^int, Z_irr, or irreducible content",
    },
}

out = Path("audit-results/stochastic_cauchy_deformation_report.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(json.dumps(report, indent=2, sort_keys=True))
