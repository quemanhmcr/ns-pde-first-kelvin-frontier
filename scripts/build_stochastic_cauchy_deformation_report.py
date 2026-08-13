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
from pde_audit.cycle_selector import rank_one_selector, two_cycle_library  # noqa: E402
from pde_audit.codeforming_surface_moment_tower import (  # noqa: E402
    codeforming_homogeneous_scale_shape_residual,
    codeforming_anchor_one_form_derivative,
    codeforming_descent_error_drift,
    codeforming_nonaffinity_divergence,
    codeforming_nonaffinity_field,
    codeforming_nonaffinity_geometry_residual,
    codeforming_nonaffinity_one_form,
    codeforming_kelvin_curl_residual,
    pulledback_vorticity_defect,
    codeforming_oriented_moment,
    cofactor_map,
    curl3,
    coherent_refinement_codeforming_moment_residual,
    scalar_normalized_oriented_moments,
    scalar_normalized_refinement_residual,
    scale_shape_codeforming_residual,
)
from pde_audit.codeforming_whitened_kelvin_remainder import (  # noqa: E402
    coordinate_face_flux_vector,
    equal_two_state_covariance,
    equal_two_state_cross_covariance,
    face_error_qv_tensor,
    homogeneous_beta_scale_shape_residual,
    passive_orientation_reparameterization_residual,
    pointwise_orientation_density,
    pointwise_whitening_residual,
    whitened_covariance,
    whitened_covariance_trace_residual,
    whitened_energy_residual,
    whitened_face_error_qv_residual,
    whitened_face_reconstruction,
    whitened_full_covariance_from_blocks,
)
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
from pde_audit.full_current_shape_covariance import (  # noqa: E402
    anchor_cross_carre_du_champ,
    deformation_kelvin_cross_carre_du_champ,
    deformation_kelvin_cross_covariance_horizon_residual,
    deformation_kelvin_cross_covariance_leading_tensor,
    joint_deformation_kelvin_leading_gramian_residual,
    navier_stokes_kelvin_gauge_residual,
    one_mode_shear_deformation_kelvin_cross_covariance,
    one_mode_shear_deformation_kelvin_cross_leading_residual,
    one_mode_shear_kelvin_mean,
    one_mode_shear_kelvin_variance,
    reverse_age_current_shape_diffusion_covariance,
    translation_cartan_residual,
)
from pde_audit.directional_refinement_kelvin_residual import (  # noqa: E402
    directional_weighted_energy_residual,
    ensemble_event_three_face_residual,
    ensemble_event_three_faces,
    homogeneous_isotropic_refinement_residual,
    midpoint_revaluation_faces,
    midpoint_revaluation_residual,
    passive_reparameterization_energy_residual,
    quadratic_long_support_calibration,
    reverse_material_weighted_energy_rate_residual,
    right_refinement_metric_residual,
    scale_shape_smooth_rate_residual,
)
from pde_audit.dynamic_reconstructed_kelvin_residual import (  # noqa: E402
    full_dyad_block_decomposition_residual,
    full_qv_block_decomposition_residual,
    geometry_mismatch_flux_drift,
    inverse_transpose_connection_residual,
    local_error_noise_transfer_residual,
    local_frame_kelvin_error_noise,
    local_residual_cross_qv,
    local_vorticity_flux_drift_residual,
    reconstructed_kelvin_noise,
    reconstructed_residual_drift,
    reconstructed_residual_dyad_drift,
    reconstructed_residual_energy_drift,
    shape_drift_transfer_residual,
)
from pde_audit.finite_shape_kelvin_descent import (  # noqa: E402
    abc_origin_xy_kelvin_descent_error,
    abc_origin_xy_local_vorticity,
    abc_origin_xy_reverse_shape_residual,
    cauchy_metric_dual_area_frame_rate,
    deformation_descent_error_pathwise_cross_qv,
    joint_deformation_error_leading_covariance,
    joint_deformation_error_leading_gramian,
    one_mode_shear_deformation_rectangle_error_cross_covariance,
    one_mode_shear_deformation_rectangle_error_cross_leading_residual,
    one_mode_shear_rectangle_error_mean,
    one_mode_shear_rectangle_error_variance,
    reverse_age_kelvin_descent_error_drift,
    reverse_age_local_area_rate,
    xy_rectangle_shear_descent_error,
)
from pde_audit.first_bad_selected_residual_readout import (  # noqa: E402
    hidden_reset_faces_from_blocks,
    selected_physical_event_factorization_residual,
    selector_second_moment_jump_residual,
    selector_switch_factorization_on_subspace_residual,
    selector_switch_second_moment_counterexample,
    selector_switch_state_counterexample,
    selector_switch_unavoidable_new_block,
    selector_switch_universal_factorization_residual,
)
from pde_audit.future_covariance_tensor import (  # noqa: E402
    connected_covariance_horizon_residual,
    connected_mean_horizon_residual,
    connected_second_moment_horizon_residual,
    codeforming_mean_dyad_backward_source,
    product_pair_diagonal_defect,
    vector_carre_du_champ,
)
from pde_audit.kelvin_event_normal_form import (  # noqa: E402
    channel_only_composition_counterexample,
    codeforming_event_composition_residual,
    codeforming_raw_normal_form_residual,
    frame_aware_event_composition_residual,
    intermediate_degenerate_basis_telescope_residual,
    intermediate_projector_telescope_residual,
    pair_functor_event_composition_residual,
    physical_raw_normal_form_residual,
    second_moment_event_composition_residual,
    symmetric_event_probe_reconstruction_residual,
)
from pde_audit.kelvin_packet_locality import (  # noqa: E402
    affine_vortex_stretch_gradient,
    affine_vortex_stretch_ns_residual,
    exact_linear_strain_ns_residual,
    strained_refined_line_frame,
)
from pde_audit.kelvin_shape_generator import (  # noqa: E402
    cubic_shear_rectangle_shape_residual,
    oriented_rectangle_area_vector_yz,
    polynomial_heat_shear,
)
from pde_audit.surface_moment_hierarchy import (  # noqa: E402
    affine_reverse_age_oriented_moment_rate,
    homogeneous_moment_rate_degree,
    oriented_first_moment_recentering_residual,
    polynomial_error_noise_from_oriented_moments,
    polynomial_flux_error_from_oriented_moments,
    reverse_age_oriented_moment_rate_integrand,
)
from pde_audit.active_pair import interval_boundary, interval_refinement_map  # noqa: E402
from pde_audit.frame_aware_kelvin_residual_refinement import (  # noqa: E402
    block_synthesis_pair_expansion_residual,
    block_synthesis_pair_functor_residual,
    block_synthesis_spectral_channel_residual,
    codeforming_determinant_ratio_residual,
    codeforming_refinement_from_raw_error_residual,
    cofactor_physical_synthesis_residual,
    compatible_raw_error_refinement_residual,
    frame_aware_physical_synthesis_block,
    isotropic_frame_aware_scale_residuals,
    orientation_complete_chain_refinement_residual,
    orientation_preserving_scalar_refinement_blocks,
    physical_reconstruction_refinement_residual,
    physical_synthesis_gauge_residual,
    quadratic_isotropic_packet_refinement_calibration,
    scalar_refinement_pair_block_residual,
)
from pde_audit.principal_kelvin_residual_channels import (  # noqa: E402
    degenerate_basis_rotation_residual,
    degenerate_eigenspace_energy,
    principal_channel_rate_faces,
    principal_channel_rate_sum_residual,
    principal_metric_rate_reconstruction_residual,
    principal_mixing_offdiagonal_residual,
    projector_channel_decomposition_residual,
    reverse_linear_shear_metric_rate,
    simple_spectrum_connection,
    simple_spectrum_connection_skew_residual,
    two_replica_pathwise_channel_residual,
)
from pde_audit.selected_principal_kelvin_lineage import (  # noqa: E402
    coefficient_synthesis_map,
    first_bad_pair_spectral_commutator,
    first_bad_spectral_commutator,
    germ_extraction_map,
    one_mode_half_period_lineage_calibration,
    selected_library_spectral_decomposition_residual,
    selector_excursion_pair_face_sums,
    selector_reset_excursion_residual,
    selector_reset_weighted_faces,
    selector_reset_weighted_residual,
    spectral_synthesis_pair_expansion_residual,
    synthesis_pair_functor_residual,
)
from pde_audit.reverse_codeforming_kelvin_martingale import (  # noqa: E402
    codeforming_residual_energy_drift,
    constant_mean_bias_rate,
    cross_qv_tensor as reverse_codeforming_cross_qv_tensor,
    full_circulation_qv_decomposition_residual,
    incompressible_volume_rate_residual,
    joint_qv_block_residual as reverse_codeforming_joint_qv_block_residual,
    normalized_circulation_local_residual_identity_residual,
    orientation_error_to_codeforming_residual_residual,
    physical_pushforward_energy_drift_residual,
    qv_tensor as reverse_codeforming_qv_tensor,
    reverse_age_vs_backward_operator_source_residual,
    reverse_codeforming_noise_decomposition_residual,
    reverse_codeforming_residual_noise,
    reverse_codeforming_vorticity_drift_residual,
    reverse_codeforming_vorticity_noise,
    second_moment_minus_covariance_source_residual,
)
from pde_audit.weighted_codeforming_kelvin_residual import (  # noqa: E402
    homogeneous_weighted_exponent_residual,
    one_mode_asymmetric_codeforming_noise,
    one_mode_asymmetric_codeforming_residual,
    one_mode_shear as weighted_one_mode_shear,
    quadratic_asymmetric_square_exact_residual,
    quadratic_heat_shear_residual,
    two_state_mean_metric_mean_second_moment,
    two_state_metric_residual_correlation,
    two_state_metric_residual_decomposition_residual,
    two_state_weighted_energy,
    weighted_bias_spread_residual,
    weighted_qv_trace_residual,
)
from pde_audit.spectral_kelvin_event_transfer import (  # noqa: E402
    degenerate_block_internal_basis_residual,
    full_parent_spectral_energy_residual,
    projector_family_algebra_residuals,
    spectral_event_transfer_residual,
    spectral_event_transfer_term,
    transfer_sector_sums,
    two_child_opposite_residual_transfer_calibration,
)
from pde_audit.same_replica_residual_library_dynamics import (  # noqa: E402
    independent_vs_common_qv_difference,
    library_qv_block_residual,
    linear_event_qv_functor_residual,
    one_mode_two_packet_common_noise_calibration,
    qv_image_rank_bound,
    same_replica_library_qv,
    selected_qv_readout_residual,
    stacked_martingale_mean_rate,
)
from pde_audit.selected_residual_hybrid_semimartingale import (  # noqa: E402
    hybrid_optional_qv,
    one_mode_selector_excursion_calibration,
    selected_continuous_qv_factorization_residual,
    selector_closed_excursion,
    selector_jump_dyad_residual,
    selector_jump_optional_qv,
    selector_readout_jump,
)
from pde_audit.selected_residual_combined_event import (  # noqa: E402
    combined_jump_square,
    combined_second_moment_jump_faces,
    combined_second_moment_jump_residual,
    combined_selected_jump_operator,
    one_mode_hidden_germ_synthesis_calibration,
    same_space_event_interaction_faces,
    same_space_event_interaction_residual,
    same_space_sequential_product_rule_residuals,
)
from pde_audit.selected_residual_combined_qv_rate import (  # noqa: E402
    combined_continuous_qv_rate_revaluation_faces,
    combined_continuous_qv_rate_revaluation_residual,
    one_mode_hidden_synthesis_qv_rate_calibration,
    post_selected_noise_response,
    pre_selected_noise_response,
    selected_continuous_qv_rate_from_noise,
    source_revaluation_vs_jump_square_calibrations,
)
from pde_audit.random_selected_event_correlation import (  # noqa: E402
    adaptive_event_alignment_calibrations,
    event_dispersion_face_psd_quadratic_form,
    two_replica_congruence_faces,
    two_replica_congruence_residual,
    two_replica_mean_output_faces,
    two_replica_mean_output_residual,
)
from pde_audit.first_bad_rule_admissibility import (  # noqa: E402
    adaptive_event_joint_law_obstruction,
    first_bad_admissibility_ledger,
    full_coherence_event_obstruction,
    passive_event_gauge_calibration,
    passive_raw_ranking_flip_calibration,
    physical_residual_support_locality_no_go,
    physical_score_passive_gauge_residual,
    persistent_library_switch_obstruction,
    raw_score_passive_gauge_change,
)
from pde_audit.local_enstrophy_kelvin_growth_gate import (  # noqa: E402
    abc_beltrami_enstrophy_stretching_calibration,
    affine_vortex_local_growth_calibration,
    critical_point_growth_residual,
    enstrophy_balance_faces,
    growth_gate_margin,
    kelvin_bulk_packet_residual,
)
from pde_audit.moving_enstrophy_critical_point import (  # noqa: E402
    abc_fixed_critical_point_speed_calibration,
    affine_degenerate_critical_speed_calibration,
    critical_path_value_derivative_residual,
    nondegenerate_scalar_critical_velocity_at,
    scalar_critical_constraint_speed_residual_at,
)
from pde_audit.enstrophy_critical_hessian_evolution import (  # noqa: E402
    abc_hessian_logdet_calibration,
    critical_hessian_evolution_faces_at,
    determinant_jacobi_residual,
    hessian_connection_logdet_divergence_residual,
    hessian_connection_logdet_rate,
    hessian_connection_strain_rotation_faces,
    hessian_connection_strain_rotation_residual,
    hessian_logdet_face_rates,
    hessian_logdet_rate,
    hessian_strain_rotation_logdet_rates,
    nonzero_determinant_from_lograte,
)
from pde_audit.enstrophy_critical_branch_competition import (  # noqa: E402
    nondegenerate_value_crossing_geometry_calibration,
    three_mode_branch_crossing_calibration,
    transverse_crossing_orientation,
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

# Full moving current-shape state and deformation--Kelvin joint covariance.
full_state_diffusion = reverse_age_current_shape_diffusion_covariance(1, 2, 2, nu)
full_state_anchor_only = (
    full_state_diffusion[:2, :2] == 2 * nu * sp.eye(2)
    and full_state_diffusion[2:, :] == sp.zeros(6, 8)
    and full_state_diffusion[:, 2:] == sp.zeros(8, 6)
)
kelvin_gauge_zero = sp.trigsimp(sp.simplify(
    navier_stokes_kelvin_gauge_residual(sp.Matrix([U, 0]), sp.Integer(0), t, (x, y), nu)
)) == sp.zeros(2, 1)
cartan_x_zero = translation_cartan_residual(sp.Matrix([U, 0]), (x, y), 0) == sp.zeros(2, 1)
cartan_y_zero = translation_cartan_residual(sp.Matrix([U, 0]), (x, y), 1) == sp.zeros(2, 1)

Kbar = one_mode_shear_kelvin_mean(y, t, nu, k)
scalar_cross = one_mode_shear_deformation_kelvin_cross_covariance(y, t, h, nu, k)
C_DK = sp.simplify(scalar_cross * v21)
HC_DK = reverse_age_horizon_operator_matrix(C_DK, h, t, velocity, nu, (x, y))
dK = [sp.diff(Kbar, x), sp.diff(Kbar, y)]
cross_horizon_zero = deformation_kelvin_cross_covariance_horizon_residual(
    C_DK, HC_DK, A, dmean, dK, nu
) == sp.zeros(4, 1)
cross_leading_zero = one_mode_shear_deformation_kelvin_cross_leading_residual(
    y, t, h, nu, k
) == 0

V_K = one_mode_shear_kelvin_variance(y, t, h, nu, k)
mean_joint = mean_vec.col_join(sp.Matrix([Kbar]))
joint_cov = Sigma.row_join(C_DK).col_join(C_DK.T.row_join(sp.Matrix([[V_K]])))
joint_second = sp.simplify(joint_cov + mean_joint * mean_joint.T)
B_joint = sp.zeros(5)
B_joint[:4, :4] = -B_horizon.T
joint_connected_zero = sp.trigsimp(sp.simplify(connected_covariance_horizon_residual(
    mean_joint,
    joint_second,
    B_joint,
    h,
    sp.Matrix([-U, 0, -1]),
    sp.diag(2 * nu, 2 * nu, 0),
    (x, y, t),
))) == sp.zeros(5)

kg1, kg2 = sp.symbols("kg1 kg2")
joint_gram_zero = joint_deformation_kelvin_leading_gramian_residual(
    [dAx, dAy], [kg1, kg2], nu, h
) == sp.zeros(5)
generic_cross_leading = deformation_kelvin_cross_covariance_leading_tensor(
    [dAx, dAy], [kg1, kg2], nu, h
)
generic_cross_has_h2 = all(sp.simplify(entry / h**2).has(nu) for entry in generic_cross_leading if entry != 0)

# Literal finite-shape -> local Kelvin descent error.
ax, by, Y_anchor, Amp, bshape = sp.symbols("ax by Y_anchor Amp bshape", positive=True)
Aconn = sp.Matrix([[sp.Symbol("aa"), sp.Symbol("ab")], [sp.Symbol("ac"), sp.Symbol("ad")]])
hconn = sp.Matrix([sp.Symbol("hh1"), sp.Symbol("hh2")])
actual_reverse_area = reverse_age_local_area_rate(Aconn, hconn, sp.zeros(2, 1))
cauchy_metric_area = cauchy_metric_dual_area_frame_rate(Aconn, hconn)
area_connection_opposite = sp.simplify(actual_reverse_area + cauchy_metric_area) == sp.zeros(2, 1)
area_connection_not_identical = sp.simplify(actual_reverse_area - cauchy_metric_area) != sp.zeros(2, 1)

Ucubic = polynomial_heat_shear(3, y, t, nu)
cubic_bias = xy_rectangle_shear_descent_error(sp.diff(Ucubic, y), y, Y_anchor, ax, by)
cubic_bias_exact = sp.simplify(cubic_bias + 4 * ax * by**3) == 0
cubic_bias_anchor_independent = sp.simplify(sp.diff(cubic_bias, Y_anchor)) == 0
cubic_bias_time_independent = sp.simplify(sp.diff(cubic_bias, t)) == 0
cubic_error_qv_zero = cubic_bias_anchor_independent
cubic_D_error_cross_qv_zero = deformation_descent_error_pathwise_cross_qv(2) == sp.zeros(4, 1)

eps_bar = one_mode_shear_rectangle_error_mean(y, t, ax, by, nu, k)
eps_var = one_mode_shear_rectangle_error_variance(y, t, h, ax, by, nu, k)
eps_var_leading_zero = sp.trigsimp(sp.simplify(
    sp.series(eps_var, h, 0, 2).removeO() - 2 * nu * h * sp.diff(eps_bar, y)**2
)) == 0
eps_cross_scalar = one_mode_shear_deformation_rectangle_error_cross_covariance(
    y, t, h, ax, by, nu, k
)
eps_cross = sp.simplify(v21 * eps_cross_scalar)
Heps_cross = reverse_age_horizon_operator_matrix(eps_cross, h, t, velocity, nu, (x, y))
deps = [sp.diff(eps_bar, x), sp.diff(eps_bar, y)]
eps_cross_horizon_zero = deformation_kelvin_cross_covariance_horizon_residual(
    eps_cross, Heps_cross, A, dmean, deps, nu
) == sp.zeros(4, 1)
eps_cross_leading_zero = one_mode_shear_deformation_rectangle_error_cross_leading_residual(
    y, t, h, ax, by, nu, k
) == 0

eg1, eg2 = sp.symbols("eg1 eg2")
joint_error_gram_zero = sp.simplify(
    joint_deformation_error_leading_covariance([dAx, dAy], [eg1, eg2], nu, h)
    - joint_deformation_error_leading_gramian([dAx, dAy], [eg1, eg2], nu, h)
) == sp.zeros(5)

abc_R = abc_origin_xy_reverse_shape_residual(Amp, nu, t, bshape)
abc_omega0 = abc_origin_xy_local_vorticity(Amp, nu, t)
abc_error_drift = reverse_age_kelvin_descent_error_drift(abc_omega0, abc_R)
abc_error_drift_expected = sp.simplify(4 * Amp**2 * sp.exp(-2 * nu * t) * bshape * (bshape - sp.sin(bshape)))
abc_shape_drift_zero_residual = sp.simplify(abc_error_drift - abc_error_drift_expected) == 0
abc_bias = abc_origin_xy_kelvin_descent_error(Amp, nu, t, bshape)

# Exact reverse-age oriented material-surface moment hierarchy.
rx, ry, rz = sp.symbols("rx ry rz", real=True)
rvec3 = sp.Matrix([rx, ry, rz])
area_ex = sp.Matrix([1, 0, 0])
du_cubic_jet = sp.Matrix([ry**3, 0, 0])
A_cubic_jet = du_cubic_jet.jacobian((rx, ry, rz))
rate_m2_p3 = reverse_age_oriented_moment_rate_integrand(
    rvec3, area_ex, du_cubic_jet, A_cubic_jet, (0, 2, 0)
)
moment_degree_rule_ok = homogeneous_moment_rate_degree(rate_m2_p3, (rx, ry, rz)) == {4}
moment_degree_value_ok = sp.simplify(rate_m2_p3[1] - 3 * ry**4) == 0

A_aff_moment = sp.Matrix([[sp.Symbol("ma"), sp.Symbol("mb")], [sp.Symbol("mc"), sp.Symbol("md")]])
zero2 = sp.zeros(2, 1)
affine_first_zero = (
    affine_reverse_age_oriented_moment_rate({(1, 0): zero2, (0, 1): zero2}, (1, 0), A_aff_moment) == zero2
    and affine_reverse_age_oriented_moment_rate({(1, 0): zero2, (0, 1): zero2}, (0, 1), A_aff_moment) == zero2
)

qb, qc = sp.symbols("qb qc", positive=True)
Uquad = polynomial_heat_shear(2, ry, t, nu)
du_quad = sp.Matrix([sp.simplify(Uquad - Uquad.subs(ry, 0)), 0, 0])
Aquad = sp.Matrix([[0, sp.diff(Uquad, ry), 0], [0, 0, 0], [0, 0, 0]])
quad_M1_rate_integrand = reverse_age_oriented_moment_rate_integrand(
    rvec3, area_ex, du_quad, Aquad, (0, 1, 0)
)
quad_M1_rate = quad_M1_rate_integrand.applyfunc(
    lambda q: sp.simplify(sp.integrate(sp.integrate(q, (ry, -qb, qb)), (rz, -qc, qc)))
)
quad_centering_breaks = sp.simplify(
    quad_M1_rate - sp.Matrix([0, sp.Rational(8, 3) * qb**3 * qc, 0])
) == sp.zeros(3, 1)

F_recent = sp.eye(2)
recent_c1, recent_c2 = sp.symbols("recent_c1 recent_c2")
recent_res = oriented_first_moment_recentering_residual(
    F_recent, sp.Matrix([1, 0]), sp.Matrix([recent_c1, recent_c2])
)
recentering_generic_obstruction = recent_res != sp.zeros(2)

f_shear = sp.Function("f_shear")
du_tangent = sp.Matrix([f_shear(ry) - f_shear(0), 0, 0])
A_tangent = sp.Matrix([[0, sp.diff(f_shear(ry), ry), 0], [0, 0, 0], [0, 0, 0]])
area_ez = sp.Matrix([0, 0, 1])
shear_tower_zero = all(
    reverse_age_oriented_moment_rate_integrand(
        rvec3, area_ez, du_tangent, A_tangent, (0, m, 0)
    ) == sp.zeros(3, 1)
    for m in range(8)
)

Ucubic_moment = polynomial_heat_shear(3, ry, t, nu)
omega_cubic_moment = sp.Matrix([0, 0, -sp.diff(Ucubic_moment, ry)])
ma, mb = sp.symbols("moment_a moment_b", positive=True)
cubic_moments = {
    (0, 1, 0): sp.zeros(3, 1),
    (0, 2, 0): sp.Matrix([0, 0, sp.Rational(4, 3) * ma * mb**3]),
}
cubic_moment_bias = polynomial_flux_error_from_oriented_moments(
    omega_cubic_moment, (rx, ry, rz), cubic_moments
)
cubic_moment_bias_ok = sp.simplify(cubic_moment_bias + 4 * ma * mb**3) == 0
cubic_moment_noise_zero = polynomial_error_noise_from_oriented_moments(
    omega_cubic_moment, (rx, ry, rz), cubic_moments
) == [0, 0, 0]

# Full scale/shape and codeforming surface-moment reduction.
cx, cy, cz = sp.symbols("cx cy cz", real=True)
cr, ca, cb, cd = sp.symbols("code_r code_a code_b code_d", positive=True)
coords_phys = (rx, ry, rz)
coords_code = (cx, cy, cz)
M0 = sp.Matrix(sp.symbols("code_m0_0:3"))
zero_exp = (0, 0, 0)
base0 = {zero_exp: M0}
Rshape = sp.diag(ca, cb, cd**3 / (ca * cb))
scalar_refinement_zero = scalar_normalized_refinement_residual(
    base0, zero_exp, Rshape, rho, cd, coords_phys
) == sp.zeros(3, 1)
Sshape = sp.diag(ca, cb, 1 / (ca * cb))
Lshape = sp.simplify(rho * Sshape)
scale_shape_pullback_zero = scale_shape_codeforming_residual(
    base0, zero_exp, Lshape, rho, coords_phys
) == sp.zeros(3, 1)
Rcoh = sp.Matrix([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
Lcoh = sp.diag(2, 3, 1)
coherent_refinement_zero = coherent_refinement_codeforming_moment_residual(
    base0, zero_exp, Lcoh, Rcoh, coords_phys
) == sp.zeros(3, 1)

quad_residual_field = sp.Matrix([ry**2, 0, 0])
quad_grad_profile = quad_residual_field.jacobian(coords_phys)
Lquad = sp.diag(cr**3, cr, cr)
Nquad = codeforming_nonaffinity_field(
    quad_residual_field, sp.zeros(3), coords_phys, Lquad, coords_code
)
quad_nonaffinity_ratio_zero = sp.simplify(
    Nquad - sp.Matrix([cy**2 / cr, 0, 0])
) == sp.zeros(3, 1)
quad_nonaffinity_div_zero = codeforming_nonaffinity_divergence(Nquad, coords_code) == 0
quad_area_is_DN_transpose = codeforming_nonaffinity_geometry_residual(
    quad_residual_field, quad_grad_profile, sp.zeros(3), coords_phys, Lquad, coords_code
) == sp.zeros(3)
beta_quad = codeforming_nonaffinity_one_form(Nquad, Lquad)
beta_quad_expected = sp.Matrix([cr**5 * cy**2, 0, 0])
beta_quad_r5_zero = sp.simplify(beta_quad - beta_quad_expected) == sp.zeros(3, 1)
omega_quad_defect = sp.Matrix([0, 0, -2 * ry])
pulled_omega_quad = pulledback_vorticity_defect(
    omega_quad_defect, sp.zeros(3, 1), coords_phys, Lquad, coords_code
)
kelvin_curl_piola_zero = codeforming_kelvin_curl_residual(
    Nquad, Lquad, coords_code, pulled_omega_quad
) == sp.zeros(3, 1)

# Exact one-mode NS referee for beta_L anchor derivative = error martingale coefficient.
U_anchor = sp.exp(-alpha * t) * sp.cos(k * Y_anchor)
U_offset = sp.exp(-alpha * t) * sp.cos(k * (Y_anchor + ry))
one_mode_residual_velocity = sp.Matrix([
    sp.simplify(U_offset - U_anchor - sp.diff(U_anchor, Y_anchor) * ry), 0, 0
])
N_one = codeforming_nonaffinity_field(
    one_mode_residual_velocity, sp.zeros(3), coords_phys, sp.eye(3), coords_code
)
beta_one = codeforming_nonaffinity_one_form(N_one, sp.eye(3))
eps_beta_line = sp.simplify(2 * ax * (
    beta_one[0].subs(cy, -by) - beta_one[0].subs(cy, by)
))
eps_beta_expected = one_mode_shear_rectangle_error_mean(Y_anchor, t, ax, by, nu, k)
one_mode_beta_error_zero = sp.trigsimp(sp.simplify(eps_beta_line - eps_beta_expected)) == 0
beta_anchor_derivative = codeforming_anchor_one_form_derivative(beta_one, Y_anchor)
q_beta_line = sp.simplify(2 * ax * (
    beta_anchor_derivative[0].subs(cy, -by)
    - beta_anchor_derivative[0].subs(cy, by)
))
one_mode_beta_noise_zero = sp.trigsimp(
    sp.simplify(q_beta_line - sp.diff(eps_beta_expected, Y_anchor))
) == 0
eta_symbols = sp.Matrix(sp.symbols("eta_code_0:3"))
hdot_symbols = sp.Matrix(sp.symbols("hdot_code_0:3"))
codeforming_drift_identity = sp.simplify(
    codeforming_descent_error_drift(eta_symbols, hdot_symbols)
    + (eta_symbols.T * hdot_symbols)[0]
) == 0

cubic_homogeneous = sp.Matrix([ry**3, rz**3, rx**3])
homogeneous_scale_shape_zero = codeforming_homogeneous_scale_shape_residual(
    cubic_homogeneous, 3, coords_phys, rho, Sshape, coords_code
) == sp.zeros(3, 1)

# Critical exact linear-strain/refinement calibration.
linear_ns_res, _ = exact_linear_strain_ns_residual(a, (x, y, z), nu)
linear_ns_zero = sp.simplify(linear_ns_res) == sp.zeros(3, 1)
Lcritical = sp.diag(1, cr, cr**2)
critical_area = sp.Matrix([0, 0, cr])
critical_moments = {zero_exp: critical_area}
critical_scalar_area = scalar_normalized_oriented_moments(critical_moments, cr)[zero_exp]
critical_codeforming_area = codeforming_oriented_moment(
    critical_moments, zero_exp, Lcritical, coords_phys
)
critical_scalar_area_zero = sp.simplify(
    critical_scalar_area - sp.Matrix([0, 0, 1 / cr])
) == sp.zeros(3, 1)
critical_codeforming_area_zero = sp.simplify(
    critical_codeforming_area - sp.Matrix([0, 0, 1])
) == sp.zeros(3, 1)
critical_support_nonlocal = Lcritical[0, 0] == 1

# Supercritical exact strain geometry: all physical exponents are negative for k>s,
# while scalar-normalized xy area is exp(s t).  We record the exact symbolic faces.
kref = sp.symbols("k_ref", positive=True)
Lsuper = strained_refined_line_frame(a, kref, t)
rho_super = sp.exp(-kref * t)
super_area = sp.Matrix([0, 0, sp.exp((a - 2 * kref) * t)])
super_scalar_area = sp.simplify(
    scalar_normalized_oriented_moments({zero_exp: super_area}, rho_super)[zero_exp]
)
super_codeforming_area = codeforming_oriented_moment(
    {zero_exp: super_area}, zero_exp, Lsuper, coords_phys
)
super_scalar_factor_zero = sp.simplify(
    super_scalar_area - sp.Matrix([0, 0, sp.exp(a * t)])
) == sp.zeros(3, 1)
super_codeforming_area_zero = sp.simplify(
    super_codeforming_area - sp.Matrix([0, 0, 1])
) == sp.zeros(3, 1)

# Metric-whitened physical reconstruction of finite orientation residuals.
Hwhite = sp.Matrix([[2, 1, 0], [0, 3, 1], [1, 0, 2]])
delta_white = sp.Matrix(sp.symbols("delta_white_0:3"))
pointwise_white_zero = pointwise_whitening_residual(delta_white, Hwhite) == sp.zeros(3, 1)
pointwise_density = pointwise_orientation_density(delta_white, Hwhite)
pointwise_reconstruction_zero = sp.simplify(
    whitened_face_reconstruction(pointwise_density, Hwhite) - delta_white
) == sp.zeros(3, 1)
eps_white = sp.Matrix(sp.symbols("eps_white_0:3"))
white_energy_zero = whitened_energy_residual(eps_white, Hwhite) == 0
Cwhite = sp.Matrix(3, 3, sp.symbols("Cwhite_0:9"))
white_cov_trace_zero = whitened_covariance_trace_residual(Cwhite, Hwhite) == 0
Rwhite = sp.Matrix([[1, 1, 0], [0, 1, 1], [0, 0, 1]])
passive_white_zero = passive_orientation_reparameterization_residual(
    eps_white, Hwhite, Rwhite
) == sp.zeros(3, 1)
qwhite1 = sp.Matrix(sp.symbols("qwhite1_0:3"))
qwhite2 = sp.Matrix(sp.symbols("qwhite2_0:3"))
white_qv_zero = whitened_face_error_qv_residual(
    [qwhite1, qwhite2], Hwhite, nu
) == sp.zeros(3)

# Exact covariance cross-block calibration after whitening.
zwhite1 = sp.Matrix([1, 0])
zwhite2 = sp.Matrix([-1, 0])
rwhite1 = sp.Matrix([-sp.Rational(1, 2), 1])
rwhite2 = sp.Matrix([sp.Rational(1, 2), -1])
Cz_white = equal_two_state_covariance(zwhite1, zwhite2)
Cr_white = equal_two_state_covariance(rwhite1, rwhite2)
Czr_white = equal_two_state_cross_covariance(zwhite1, zwhite2, rwhite1, rwhite2)
Cfull_white = equal_two_state_covariance(zwhite1 + rwhite1, zwhite2 + rwhite2)
white_cross_decomposition_zero = sp.simplify(
    whitened_full_covariance_from_blocks(Cz_white, Cr_white, Czr_white) - Cfull_white
) == sp.zeros(2)
white_cross_mandatory = sp.simplify(Czr_white + Czr_white.T) != sp.zeros(2)
white_drop_cross_false = sp.simplify(Cfull_white - Cz_white - Cr_white) != sp.zeros(2)

# Homogeneous beta exponent law and exact cubic NS finite-face reconstruction.
beta_scale_shape_zero = homogeneous_beta_scale_shape_residual(
    cubic_homogeneous, 3, coords_phys, rho, Sshape, coords_code
) == sp.zeros(3, 1)
beta_cubic_unit = sp.Matrix([cy**3, 0, 0])
density_cubic_unit = curl3(beta_cubic_unit, coords_code)
eps_cubic_unit = coordinate_face_flux_vector(
    density_cubic_unit, coords_code, (sp.Rational(1, 2),) * 3
)
cubic_unit_reconstruction = whitened_face_reconstruction(eps_cubic_unit, sp.eye(3))
cubic_unit_expected = sp.Matrix([0, 0, -sp.Rational(1, 4)])
cubic_unit_reconstruction_zero = sp.simplify(
    cubic_unit_reconstruction - cubic_unit_expected
) == sp.zeros(3, 1)
cubic_center_defect_zero = sp.simplify(density_cubic_unit.subs({cx: 0, cy: 0, cz: 0})) == sp.zeros(3, 1)

Lwhite_iso = cr * sp.eye(3)
Hwhite_iso = cofactor_map(Lwhite_iso)
beta_cubic_iso = sp.Matrix([cr**4 * cy**3, 0, 0])
eps_cubic_iso = coordinate_face_flux_vector(
    curl3(beta_cubic_iso, coords_code), coords_code, (sp.Rational(1, 2),) * 3
)
recon_cubic_iso = whitened_face_reconstruction(eps_cubic_iso, Hwhite_iso)
cubic_raw_r4_zero = sp.simplify(
    eps_cubic_iso - sp.Matrix([0, 0, -cr**4 / 4])
) == sp.zeros(3, 1)
cubic_white_r2_zero = sp.simplify(
    recon_cubic_iso - sp.Matrix([0, 0, -cr**2 / 4])
) == sp.zeros(3, 1)

# Dynamic orientation-reconstructed Kelvin residual on the literal reverse-age state.
Adyn = sp.Matrix([[sp.Symbol("A00"), sp.Symbol("A01"), 0], [sp.Symbol("A10"), -sp.Symbol("A00"), 0], [0, 0, 0]])
Hdyn = sp.Matrix([[2, 1, 0], [0, 3, 1], [1, 0, 2]])
omega_dyn = sp.Matrix(sp.symbols("omega_dyn_0:3"))
hR_dyn = sp.Matrix(sp.symbols("hR_dyn_0:3"))
h_dyn = sp.Matrix(sp.symbols("h_dyn_0:3"))
RA_dyn = sp.Matrix(sp.symbols("RA_dyn_0:3"))
Gdyn = sp.Matrix(3, 3, sp.symbols("Gdyn_0:9"))
AKdyn = sp.Matrix(3, 3, sp.symbols("AKdyn_0:9"))
rdyn = sp.Matrix(sp.symbols("rdyn_0:3"))
invT_connection_zero = inverse_transpose_connection_residual(Adyn, Hdyn) == sp.zeros(3)
local_flux_drift_zero = local_vorticity_flux_drift_residual(Adyn, Hdyn, omega_dyn) == sp.zeros(3, 1)
shape_transfer_zero = shape_drift_transfer_residual(Adyn, omega_dyn, hR_dyn, h_dyn, RA_dyn) == 0
geometry_transfer_is_plus_shape = sp.simplify(
    geometry_mismatch_flux_drift(Adyn, omega_dyn, hR_dyn, h_dyn, RA_dyn)
    - (omega_dyn.T * RA_dyn)[0]
) == 0
AKrow_dyn = sp.Matrix(1, 3, sp.symbols("AKrow_dyn_0:3"))
noise_transfer_zero = local_error_noise_transfer_residual(
    AKrow_dyn, Gdyn, hR_dyn, h_dyn
) == sp.zeros(1, 3)
Qdyn = local_frame_kelvin_error_noise(AKdyn, Hdyn, Gdyn)
Qhat_dyn = reconstructed_kelvin_noise(Qdyn, Hdyn)
full_qv_blocks_zero = full_qv_block_decomposition_residual(AKdyn, Hdyn, Gdyn, nu) == sp.zeros(3)
full_dyad_blocks_zero = full_dyad_block_decomposition_residual(
    Adyn, omega_dyn, rdyn, Gdyn, Qhat_dyn, nu
) == sp.zeros(3)
dyad_dyn = reconstructed_residual_dyad_drift(Adyn, rdyn, Qhat_dyn, nu)
energy_dyn = reconstructed_residual_energy_drift(Adyn, rdyn, Qhat_dyn, nu)
dyad_energy_trace_zero = sp.simplify(sp.trace(dyad_dyn) / 2 - energy_dyn) == 0
cross_dyn = local_residual_cross_qv(Gdyn, Qhat_dyn, nu)
generic_dynamic_cross_nonzero = sp.simplify(cross_dyn) != sp.zeros(3)

# Exact cubic dynamic conserved-mode calibration.
A_cubic_dyn = sp.Matrix([[0, 6 * nu * t, 0], [0, 0, 0], [0, 0, 0]])
r_cubic_dyn = sp.Matrix([0, 0, -sp.Rational(1, 4)])
cubic_dynamic_drift_zero = reconstructed_residual_drift(A_cubic_dyn, r_cubic_dyn) == sp.zeros(3, 1)
cubic_dynamic_energy_zero = reconstructed_residual_energy_drift(
    A_cubic_dyn, r_cubic_dyn, sp.zeros(3), nu
) == 0

# Exact one-mode local/residual qv calibration.
ax_dyn, by_dyn = sp.symbols("ax_dyn by_dyn", positive=True)
eps_one_dyn = one_mode_shear_rectangle_error_mean(y, t, ax_dyn, by_dyn, nu, k)
G_one_dyn = sp.zeros(3)
G_one_dyn[2, 1] = -sp.diff(U, y, 2)
Q_one_dyn = sp.zeros(3)
Q_one_dyn[2, 1] = sp.diff(eps_one_dyn, y)
cross_one_dyn = local_residual_cross_qv(G_one_dyn, Q_one_dyn, nu)
one_mode_dynamic_cross_expected = sp.simplify(
    2 * nu * (-sp.diff(U, y, 2)) * sp.diff(eps_one_dyn, y)
)
one_mode_dynamic_cross_zero = sp.simplify(
    cross_one_dyn[2, 2] - one_mode_dynamic_cross_expected
) == 0
one_mode_dynamic_cross_nonzero = sp.simplify(one_mode_dynamic_cross_expected) != 0
V_one_dyn = one_mode_shear_rectangle_error_variance(y, t, h, ax_dyn, by_dyn, nu, k)
one_mode_dynamic_qv_onset_zero = sp.trigsimp(sp.simplify(
    sp.diff(V_one_dyn, h).subs(h, 0) - 2 * nu * sp.diff(eps_one_dyn, y) ** 2
)) == 0

# Reverse-age co-deforming Kelvin martingale core.
Acof = sp.Matrix([[sp.Symbol("Ac00"), sp.Symbol("Ac01"), 0], [sp.Symbol("Ac10"), -sp.Symbol("Ac00"), 0], [0, 0, 0]])
Lcof = sp.Matrix([[2, 1, 0], [0, 3, 1], [1, 0, 2]])
Jcof = sp.det(Lcof)
omega_cof = sp.Matrix(sp.symbols("omega_cof_0:3"))
Kcof = sp.Matrix(sp.symbols("Kcof_0:3"))
Hcof = cofactor_map(Lcof)
eps_cof = sp.simplify(Kcof - Hcof.T * omega_cof)
volume_freeze_zero = incompressible_volume_rate_residual(Acof, Lcof) == 0
residual_triangle_zero = orientation_error_to_codeforming_residual_residual(Lcof, eps_cof) == sp.zeros(3, 1)
normalized_split_zero = normalized_circulation_local_residual_identity_residual(
    Lcof, Kcof, omega_cof, eps_cof
) == sp.zeros(3, 1)
local_codeforming_drift_zero = reverse_codeforming_vorticity_drift_residual(
    Acof, Lcof, omega_cof
) == sp.zeros(3, 1)
Gcof = sp.Matrix(3, 3, sp.symbols("Gcof_0:9"))
AKcof = sp.Matrix(3, 3, sp.symbols("AKcof_0:9"))
Qeps_cof = sp.simplify(AKcof - Hcof.T * Gcof)
noise_split_zero = reverse_codeforming_noise_decomposition_residual(
    AKcof, Qeps_cof, Lcof, Gcof
) == sp.zeros(3)
Gtilde_cof = reverse_codeforming_vorticity_noise(Lcof, Gcof)
Qtilde_cof = reverse_codeforming_residual_noise(Qeps_cof, Lcof)
joint_gram_blocks_zero = reverse_codeforming_joint_qv_block_residual(
    Gtilde_cof, Qtilde_cof, nu
) == sp.zeros(6)
full_qv_split_zero = full_circulation_qv_decomposition_residual(
    Gtilde_cof, Qtilde_cof, nu
) == sp.zeros(3)
chi_cof = sp.Matrix(sp.symbols("chi_cof_0:3"))
metric_work_zero = physical_pushforward_energy_drift_residual(
    Acof, Lcof, chi_cof, Qtilde_cof, nu
) == 0
mean_bias_rate_zero = constant_mean_bias_rate() == 0
covariance_source_zero = second_moment_minus_covariance_source_residual(
    Qtilde_cof, nu
) == sp.zeros(3)
reverse_eta_source = reverse_codeforming_qv_tensor(Gtilde_cof, nu)
backward_eta_source = codeforming_mean_dyad_backward_source(Lcof, Gcof, nu)
clock_sign_zero = reverse_age_vs_backward_operator_source_residual(
    reverse_eta_source, backward_eta_source
) == sp.zeros(3)

# Exact cubic bias/no-qv calibration in unit coherent frame.
chi_cubic_cof = sp.Matrix([0, 0, -sp.Rational(1, 4)])
Q_cubic_cof = sp.zeros(3)
cubic_codeforming_bias_nonzero = chi_cubic_cof != sp.zeros(3, 1)
cubic_codeforming_qv_zero = reverse_codeforming_qv_tensor(Q_cubic_cof, nu) == sp.zeros(3)
cubic_codeforming_energy_zero = codeforming_residual_energy_drift(Q_cubic_cof, nu) == 0

# Exact periodic one-mode full-y-period mechanism calibration.
Ycof = sp.symbols("Ycof", real=True)
a_cof = sp.symbols("a_cof", positive=True)
b_cof = sp.pi / k
Ucof = lambda yy: sp.exp(-alpha * t) * sp.cos(k * yy)
Kz_full_period = sp.trigsimp(sp.simplify(-2 * a_cof * (Ucof(Ycof + b_cof) - Ucof(Ycof - b_cof))))
omega_z_cof = sp.simplify(-sp.diff(Ucof(Ycof), Ycof))
eta_z_cof = omega_z_cof  # choose coherent third line length one
chi_z_cof = sp.simplify(-eta_z_cof)  # Kz/J=0
geta_cof = sp.diff(eta_z_cof, Ycof)
qchi_cof = sp.diff(chi_z_cof, Ycof)
gamma_eta_cof = sp.simplify(2 * nu * geta_cof**2)
gamma_chi_cof = sp.simplify(2 * nu * qchi_cof**2)
gamma_cross_cof = sp.simplify(2 * nu * geta_cof * qchi_cof)
full_period_K_zero = Kz_full_period == 0
full_period_noise_opposite = sp.simplify(qchi_cof + geta_cof) == 0
full_period_cross_negative_equal = sp.simplify(gamma_cross_cof + gamma_eta_cof) == 0
full_period_diag_equal = sp.simplify(gamma_chi_cof - gamma_eta_cof) == 0
full_period_qv_cancellation_zero = sp.simplify(
    gamma_eta_cof + gamma_chi_cof + 2 * gamma_cross_cof
) == 0
full_period_local_qv_nonzero = sp.simplify(gamma_eta_cof) != 0
full_period_cross_qv_nonzero = sp.simplify(gamma_cross_cof) != 0

# Physical frame-weighted codeforming residual topology and exact NS target corrections.
Yw = sp.symbols("Yw", real=True)
rhow = sp.symbols("rhow", positive=True)
quad_weighted_ns_zero = quadratic_heat_shear_residual(Yw, t, nu) == 0
eps_quad_w, chi_quad_w, r_quad_w = quadratic_asymmetric_square_exact_residual(
    Yw, t, nu, rhow
)
quad_raw_bias_nonzero = sp.simplify(chi_quad_w) != 0
quad_raw_bias_constant = sp.simplify(chi_quad_w + 1) == 0
quad_physical_residual_limit_zero = sp.limit(r_quad_w, rhow, 0, dir="+") == 0
quad_weighted_bias_r2 = sp.simplify(r_quad_w**2 - rhow**2) == 0

chi_one_w = one_mode_asymmetric_codeforming_residual(Yw, t, rhow, nu, k)
qchi_one_w = one_mode_asymmetric_codeforming_noise(Yw, t, rhow, nu, k)
U_one_w = weighted_one_mode_shear(Yw, t, nu, k)
chi_one_limit_residual_zero = sp.simplify(
    sp.limit(chi_one_w, rhow, 0, dir="+") + sp.diff(U_one_w, Yw, 2) / 2
) == 0
qchi_one_limit_residual_zero = sp.simplify(
    sp.limit(qchi_one_w, rhow, 0, dir="+") + sp.diff(U_one_w, Yw, 3) / 2
) == 0
one_physical_bias_limit_zero = sp.simplify(
    sp.limit(rhow * chi_one_w, rhow, 0, dir="+")
) == 0
one_physical_noise_limit_zero = sp.simplify(
    sp.limit(rhow * qchi_one_w, rhow, 0, dir="+")
) == 0

Lw = sp.Matrix([[2, 1, 0], [0, 3, 1], [1, 0, 2]])
mw = sp.Matrix(sp.symbols("mw0:3"))
cw = sp.symbols("cw0:6")
Cw = sp.Matrix([[cw[0], cw[1], cw[2]], [cw[1], cw[3], cw[4]], [cw[2], cw[4], cw[5]]])
weighted_fixed_frame_split_zero = weighted_bias_spread_residual(mw, Cw, Lw) == 0
Qnoise_w = sp.Matrix(3, 2, sp.symbols("qnw0:6"))
weighted_qv_trace_zero = weighted_qv_trace_residual(Lw, Qnoise_w, nu) == 0

Lw1 = sp.diag(2, 1, 1)
Lw2 = sp.eye(3)
chw1 = sp.Matrix([1, 0, 0])
chw2 = sp.zeros(3, 1)
random_frame_energy = two_state_weighted_energy(Lw1, chw1, Lw2, chw2)
random_frame_factorized = two_state_mean_metric_mean_second_moment(Lw1, chw1, Lw2, chw2)
random_frame_mixed = two_state_metric_residual_correlation(Lw1, chw1, Lw2, chw2)
random_frame_decomposition_zero = two_state_metric_residual_decomposition_residual(
    Lw1, chw1, Lw2, chw2
) == 0
random_frame_factorization_false = sp.simplify(random_frame_energy-random_frame_factorized) != 0
random_frame_mixed_signed_positive = random_frame_mixed == sp.Rational(3, 4)
random_frame_mixed_signed_negative = two_state_metric_residual_correlation(
    Lw1, chw2, Lw2, chw1
) == -sp.Rational(3, 4)
homogeneous_weighted_exponents_zero = all(
    homogeneous_weighted_exponent_residual(rhow, p, a) == 0 for p in range(2, 8)
)

# Directional/refinement/event balance of the physical weighted Kelvin residual.
Vdir = sp.Matrix([[sp.Rational(3,5), -sp.Rational(4,5), 0], [sp.Rational(4,5), sp.Rational(3,5), 0], [0,0,1]])
s2dir = (sp.Integer(1), sp.Integer(4), sp.Integer(9))
Qdir = sp.Matrix([[2,1,0],[1,3,1],[0,1,5]])
directional_decomposition_zero = directional_weighted_energy_residual(Qdir, Vdir, s2dir) == 0

Lref = sp.Matrix([[2,1,0],[0,1,1],[1,0,1]])
Rref = sp.Matrix([[1,1,0],[0,1,0],[0,0,2]])
right_refinement_metric_zero = right_refinement_metric_residual(Lref, Rref) == sp.zeros(3)

Mm_evt = sp.Matrix([[2,1],[1,3]])
Qm_evt = sp.Matrix([[4,1],[1,2]])
Mp_evt = sp.Matrix([[5,2],[2,4]])
Qp_evt = sp.Matrix([[3,2],[2,6]])
midpoint_event_zero = midpoint_revaluation_residual(Mm_evt, Qm_evt, Mp_evt, Qp_evt) == 0
mid_geometry_evt, mid_state_evt = midpoint_revaluation_faces(Mm_evt, Qm_evt, Mp_evt, Qp_evt)

Mpass = sp.diag(2,3,5)
Qpass = sp.Matrix([[1,1,0],[1,2,0],[0,0,1]])
Rpass = sp.Matrix([[1,1,0],[0,1,0],[0,0,1]])
passive_gl_total_zero = passive_reparameterization_energy_residual(Mpass, Qpass, Rpass) == 0
Mpass_p = sp.simplify(Rpass.T*Mpass*Rpass)
Qpass_p = sp.simplify(Rpass.inv()*Qpass*Rpass.inv().T)
pass_geometry, pass_state = midpoint_revaluation_faces(Mpass, Qpass, Mpass_p, Qpass_p)
passive_gl_geometry_nonzero = sp.simplify(pass_geometry) != 0
passive_gl_state_nonzero = sp.simplify(pass_state) != 0
passive_gl_faces_cancel = sp.simplify(pass_geometry + pass_state) == 0

Me_m = sp.eye(3)
Qe_m = sp.diag(1,0,0)
Me_p = sp.diag(4,1,1)
Qe_p = sp.diag(2,0,0)
ce_m = sp.Integer(0)
ce_p = sp.Rational(3,4)
ensemble_three_face_zero = ensemble_event_three_face_residual(Me_m, Qe_m, ce_m, Me_p, Qe_p, ce_p) == 0
ensemble_geometry, ensemble_state, ensemble_corr = ensemble_event_three_faces(Me_m, Qe_m, ce_m, Me_p, Qe_p, ce_p)
ensemble_face_values_expected = (ensemble_geometry, ensemble_state, ensemble_corr) == (sp.Rational(9,2), sp.Rational(5,2), sp.Rational(3,4))

rho_evt, rhod_evt = sp.symbols("rho_evt rhod_evt", nonzero=True)
Qsmooth = sp.Matrix([[2,1],[1,3]])
Qsmooth_dot = sp.Matrix([[1,2],[2,-1]])
Asmooth = sp.Matrix([[3,1],[1,2]])
Asmooth_dot = sp.Matrix([[2,-1],[-1,1]])
smooth_scale_shape_content_zero = scale_shape_smooth_rate_residual(Qsmooth, Qsmooth_dot, rho_evt, rhod_evt, Asmooth, Asmooth_dot) == 0

A_mat = sp.Matrix([[1,2],[-1,-1]])
L_mat = sp.Matrix([[2,1],[0,1]])
Q_mat = sp.Matrix([[3,1],[1,2]])
B_mat = sp.Matrix([[1,2],[3,-1]])
reverse_material_weighted_zero = reverse_material_weighted_energy_rate_residual(A_mat, L_mat, Q_mat, B_mat, nu) == 0

homogeneous_refinement_p2_p7_zero = all(
    homogeneous_isotropic_refinement_residual(Mm_evt, Qm_evt, sp.Symbol("lambda_evt"), p) == 0
    for p in range(2,8)
)

rho_long = sp.symbols("rho_long", positive=True)
Ylong = sp.symbols("Ylong", real=True)
quad_long = quadratic_long_support_calibration(Ylong, t, nu, rho_long)
quad_long_epsilon_expected = sp.simplify(quad_long["epsilon_z"] + rho_long**2) == 0
quad_long_chi_expected = quad_long["chi"] == sp.Matrix([0,0,-1])
quad_long_residual_expected = quad_long["physical_residual"] == sp.Matrix([0,0,-rho_long])
quad_long_energy_expected = sp.simplify(quad_long["physical_energy"] - rho_long**2) == 0
quad_long_energy_limit_zero = sp.limit(quad_long["physical_energy"], rho_long, 0, dir="+") == 0
quad_long_support_not_local = quad_long["long_x_line_squared"] == 1 and quad_long["line_frame"][0,0] == 1

# Pathwise spectral Kelvin-residual channels and principal-axis traffic.
Ppc = [sp.diag(1,0,0), sp.diag(0,1,0), sp.diag(0,0,1)]
lampc = (sp.Integer(1), sp.Integer(4), sp.Integer(9))
Mpc = sp.diag(*lampc)
Qpc = sp.Matrix([[2,1,0],[1,3,1],[0,1,5]])
projector_channel_zero = projector_channel_decomposition_residual(Mpc,Qpc,Ppc,lampc) == 0

V1pc = sp.eye(3)
V2pc = sp.Matrix([[0,1,0],[1,0,0],[0,0,1]])
Q1pc = sp.diag(3,1,2)
Q2pc = sp.Matrix([[1,sp.Rational(1,2),0],[sp.Rational(1,2),4,0],[0,0,2]])
two_replica_channel_zero = two_replica_pathwise_channel_residual(
    V1pc,(1,4,9),Q1pc,V2pc,(2,5,7),Q2pc
) == 0

Bpc = sp.Matrix([[2,3,1],[3,-1,2],[1,2,4]])
Qrate_pc = sp.Matrix([[5,2,1],[2,3,sp.Rational(1,2)],[1,sp.Rational(1,2),4]])
Qdot_pc = sp.Matrix([[1,2,0],[2,3,1],[0,1,-2]])
connection_skew_zero = simple_spectrum_connection_skew_residual(Bpc,lampc) == sp.zeros(3)
metric_rate_reconstruction_zero = principal_metric_rate_reconstruction_residual(Bpc,lampc) == sp.zeros(3)
channel_rate_sum_zero = principal_channel_rate_sum_residual(Bpc,lampc,Qrate_pc,Qdot_pc) == 0
mixing_offdiag_zero = principal_mixing_offdiagonal_residual(Bpc,lampc,Qrate_pc) == 0

gamma_pc, qmix_pc = sp.symbols("gamma_pc qmix_pc", nonzero=True)
Lshear_pc = sp.diag(2,1,3)
Bshear_pc = reverse_linear_shear_metric_rate(gamma_pc,Lshear_pc)
Omegashear_pc = simple_spectrum_connection(Bshear_pc,(4,1,9))
Qshear_pc = sp.Matrix([[1,qmix_pc,0],[qmix_pc,2,0],[0,0,3]])
_,_,mixing_shear_pc = principal_channel_rate_faces(Bshear_pc,(4,1,9),Qshear_pc,sp.zeros(3))
linear_shear_B_expected = Bshear_pc == sp.Matrix([[0,-2*gamma_pc,0],[-2*gamma_pc,0,0],[0,0,0]])
linear_shear_connection_expected = sp.simplify(Omegashear_pc[0,1]-sp.Rational(2,3)*gamma_pc) == 0
linear_shear_mixing_expected = sp.simplify(sum(mixing_shear_pc)+4*gamma_pc*qmix_pc) == 0
linear_shear_mixing_active = mixing_shear_pc[0] != 0 and mixing_shear_pc[1] != 0

Wdeg_pc = sp.Matrix([[1,0],[0,1],[0,0]])
Rdeg_pc = sp.Matrix([[sp.Rational(3,5),-sp.Rational(4,5)],[sp.Rational(4,5),sp.Rational(3,5)]])
Qdeg_pc = sp.Matrix([[2,1,3],[1,5,2],[3,2,7]])
degenerate_basis_gauge_zero = degenerate_basis_rotation_residual(Wdeg_pc,Rdeg_pc,4,Qdeg_pc) == 0
degenerate_block_energy_expected = degenerate_eigenspace_energy(Wdeg_pc,4,Qdeg_pc) == 28
try:
    simple_spectrum_connection(sp.Matrix([[0,1,0],[1,0,0],[0,0,0]]),(1,1,4))
    degeneracy_rejected = False
except ValueError:
    degeneracy_rejected = True

# Literal first-bad selector / principal-channel lineage.
Slin = rank_one_selector(2,1)
P0lin = [sp.diag(1,0,0),sp.diag(0,1,0),sp.diag(0,0,1)]
clin = sp.sqrt(2)/2
v1lin=sp.Matrix([clin,clin,0]); v2lin=sp.Matrix([clin,-clin,0]); v3lin=sp.Matrix([0,0,1])
P1lin=[v1lin*v1lin.T,v2lin*v2lin.T,v3lin*v3lin.T]
lam0lin=(1,4,9); lam1lin=(2,5,7)
M0lin=sum((lam0lin[i]*P0lin[i] for i in range(3)),sp.zeros(3))
M1lin=sum((lam1lin[i]*P1lin[i] for i in range(3)),sp.zeros(3))
selector_spectral_zero = first_bad_spectral_commutator(Slin,[P0lin[0],P1lin[0]]) == sp.zeros(6)
selector_pair_spectral_zero = first_bad_pair_spectral_commutator(Slin,[P0lin[0],P1lin[0]]) == sp.zeros(36)
Smixlin=sp.Matrix([[0,1],[1,0]])
generic_germ_mixing_nonzero = first_bad_spectral_commutator(Smixlin,[P0lin[0],P1lin[1]]) != sp.zeros(6)
Qlin=sp.Matrix([
    [3,1,0, 1,0,1], [1,2,0, 0,1,0], [0,0,4, 1,0,2],
    [1,0,1, 5,2,0], [0,1,0, 2,6,1], [1,0,2, 0,1,7],
])
selected_endpoint_spectral_zero = selected_library_spectral_decomposition_residual(
    Qlin,Slin,[M0lin,M1lin],[P0lin,P1lin],[lam0lin,lam1lin]
) == 0
Alin=coefficient_synthesis_map([sp.Rational(2,3),-sp.Rational(1,2)])
synthesis_pair_zero=synthesis_pair_functor_residual(Qlin,Alin) == sp.zeros(9,1)
spectral_pair_expansion_zero=spectral_synthesis_pair_expansion_residual(
    Qlin,[sp.Rational(2,3),-sp.Rational(1,2)],sp.Integer(5),sp.diag(1,0,1)
) == 0
A0lin,A1lin=germ_extraction_map(2,0),germ_extraction_map(2,1)
selector_reset_zero=selector_reset_weighted_residual(Qlin,A0lin,A1lin,M0lin,M1lin) == 0
reset_faces_lin=selector_reset_weighted_faces(Qlin,A0lin,A1lin,M0lin,M1lin)
reset_four_face_zero=sp.simplify(reset_faces_lin.total_jump-reset_faces_lin.reconstructed) == 0

one_mode_lineage=one_mode_half_period_lineage_calibration(t,nu,k)
one_mode_lineage_opposite_zero=one_mode_lineage["opposite_residual_zero"] == 0
one_mode_lineage_parent_zero=one_mode_lineage["full_parent_channel"] == 0
one_mode_lineage_diag_nonzero=sp.simplify(one_mode_lineage["diagonal_parent_channel"]) != 0
one_mode_lineage_cross_cancels=sp.simplify(
    one_mode_lineage["cross_child_channel"]+one_mode_lineage["diagonal_parent_channel"]
) == 0
one_mode_lineage_reset_zero=one_mode_lineage["reset_total_jump"] == 0 and one_mode_lineage["reset_reconstruction_residual"] == 0
one_mode_lineage_reset_signed=sp.simplify(one_mode_lineage["reset_pair_left"]-one_mode_lineage["reset_pair_right"]) == 0 and sp.simplify(one_mode_lineage["reset_pair_quadratic"]+2*one_mode_lineage["reset_pair_left"]) == 0
Qoline=one_mode_lineage["library_second_moment"]
side_line=sp.pi/(2*k); Moline=sp.simplify(side_line**2*sp.eye(3))
closed_excursion_zero=selector_reset_excursion_residual(Qoline,[A0lin,A1lin,A0lin],[Moline,Moline,Moline]) == 0
geo_line,left_line,right_line,quad_line=selector_excursion_pair_face_sums(Qoline,[A0lin,A1lin,A0lin],[Moline,Moline,Moline])
closed_excursion_faces_cancel=geo_line == 0 and sp.simplify(left_line+right_line+quad_line) == 0
closed_excursion_quad_positive=bool(sp.N(quad_line.subs({t:1,nu:1,k:1})) > 0)
closed_excursion_signed_negative=bool(sp.N((left_line+right_line).subs({t:1,nu:1,k:1})) < 0)

Qaxis=sp.diag(3,1,2); e1axis,e2axis=sp.eye(3)[:,0],sp.eye(3)[:,1]
uaxis=sp.simplify((e1axis+e2axis)/sp.sqrt(2)); vaxis=sp.simplify((e1axis-e2axis)/sp.sqrt(2))
axis_before=((e1axis.T*Qaxis*e1axis)[0],(e2axis.T*Qaxis*e2axis)[0])
axis_after=(sp.simplify((uaxis.T*Qaxis*uaxis)[0]),sp.simplify((vaxis.T*Qaxis*vaxis)[0]))
cross_event_axis_values_change=axis_before != axis_after
cross_event_block_total_invariant=sp.simplify(sum(axis_before)-sum(axis_after)) == 0

# Frame-aware refinement forced by raw orientation-current packet synthesis.
Lpf=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
L1f=sp.Matrix([[1,1,0],[0,2,0],[0,1,3]])
L2f=sp.Matrix([[3,0,1],[1,2,0],[0,1,1]])
Hpf=cofactor_map(Lpf); H1f=cofactor_map(L1f); H2f=cofactor_map(L2f)
R1f=sp.Matrix([[1,1,0],[0,1,0],[0,0,2]])
R2f=sp.Matrix([[2,0,0],[1,1,1],[0,0,1]])
omegaf=sp.Matrix(sp.symbols("omega_frame0:3"))
K1f=sp.Matrix(sp.symbols("K1_frame0:3")); K2f=sp.Matrix(sp.symbols("K2_frame0:3"))
compatible_raw_error_zero=compatible_raw_error_refinement_residual(
    [K1f,K2f],[H1f,H2f],[R1f,R2f],omegaf
) == sp.zeros(3,1)
e1f=sp.Matrix(sp.symbols("eps1_frame0:3")); e2f=sp.Matrix(sp.symbols("eps2_frame0:3"))
physical_refinement_zero=physical_reconstruction_refinement_residual(
    [e1f,e2f],[H1f,H2f],[R1f,R2f],Hpf
) == sp.zeros(3,1)
Spf=sp.Matrix([[1,1,0],[0,1,0],[0,0,2]])
S1f=sp.Matrix([[2,0,0],[1,1,0],[0,0,1]])
physical_gauge_zero=physical_synthesis_gauge_residual(Hpf,H1f,R1f,Spf,S1f) == sp.zeros(3)
cofactor_synthesis_zero=cofactor_physical_synthesis_residual(Lpf,L1f,R1f) == sp.zeros(3)
codeforming_det_zero=codeforming_determinant_ratio_residual(Lpf,L1f,R1f) == sp.zeros(3)
c1f=sp.Matrix(sp.symbols("chi1_frame0:3")); c2f=sp.Matrix(sp.symbols("chi2_frame0:3"))
codeforming_parent_zero=codeforming_refinement_from_raw_error_residual(
    [c1f,c2f],Lpf,[L1f,L2f],[R1f,R2f]
) == sp.zeros(3,1)
A1f=frame_aware_physical_synthesis_block(Hpf,H1f,R1f)
A2f=frame_aware_physical_synthesis_block(Hpf,H2f,R2f)
Qframe=sp.Matrix(6,6,sp.symbols("Qframe0:36"))
frame_pair_functor_zero=block_synthesis_pair_functor_residual(Qframe,[A1f,A2f]) == sp.zeros(9,1)
frame_pair_expansion_zero=block_synthesis_pair_expansion_residual(Qframe,[A1f,A2f]) == sp.zeros(3)
frame_spectral_pair_zero=block_synthesis_spectral_channel_residual(
    Qframe,[A1f,A2f],sp.Symbol("lambda_frame"),sp.diag(1,0,1)
) == 0
rpf,rif,awf=sp.symbols("rho_parent_frame rho_child_frame a_frame", positive=True)
frame_iso_phys_zero,frame_iso_code_zero=isotropic_frame_aware_scale_residuals(rpf,rif,awf)
frame_iso_scale_zero=frame_iso_phys_zero == sp.zeros(3) and frame_iso_code_zero == sp.zeros(3)

rf1,rf2,af1,af2=sp.symbols("rho_frame1 rho_frame2 a_frame1 a_frame2", positive=True)
quad_frame=quadratic_isotropic_packet_refinement_calibration([rf1,rf2],[af1,af2],t,nu)
quad_frame_physical_zero=quad_frame["physical_prediction_residual"] == sp.zeros(3,1)
quad_frame_codeforming_zero=quad_frame["codeforming_prediction_residual"] == sp.zeros(3,1)
quad_frame_expected_r=sp.Matrix([0,0,-(af1*rf1**3+af2*rf2**3)/(af1*rf1**2+af2*rf2**2)])
quad_frame_expected_chi=sp.Matrix([0,0,-(af1*rf1**3+af2*rf2**3)/(af1*rf1**2+af2*rf2**2)**sp.Rational(3,2)])
quad_frame_r_expected=sp.simplify(quad_frame["parent_physical_residual"]-quad_frame_expected_r) == sp.zeros(3,1)
quad_frame_chi_expected=sp.simplify(quad_frame["parent_codeforming_residual"]-quad_frame_expected_chi) == sp.zeros(3,1)
quad_frame_naive_false=quad_frame["parent_physical_residual"].subs({rf1:1,rf2:2,af1:1,af2:1}) != quad_frame["naive_common_fiber_physical_sum"].subs({rf1:1,rf2:2,af1:1,af2:1})

scalar_weights=[sp.Rational(1,3),sp.Rational(2,3)]
scalar_packet_blocks=orientation_preserving_scalar_refinement_blocks(scalar_weights)
scalar_packet_blocks_expected=scalar_packet_blocks == [scalar_weights[0]*sp.eye(3),scalar_weights[1]*sp.eye(3)]
scalar_packet_pair_zero=all(X == sp.zeros(9) for X in scalar_refinement_pair_block_residual(scalar_weights))
Bfine_frame,R1chain_frame,R0chain_frame=interval_refinement_map(2,2)
Bcoarse_frame=interval_boundary(2)
orientation_chain_lift_zero=orientation_complete_chain_refinement_residual(
    Bfine_frame,Bcoarse_frame,R1chain_frame,R0chain_frame,3
) == sp.zeros(Bfine_frame.rows*3,R1chain_frame.cols*3)

# Spectral projector event transfer with a frame-converting finite map.
Lpe=sp.diag(2,3,4); L1e=sp.diag(1,2,5); L2e=sp.diag(3,1,2)
Hpe=cofactor_map(Lpe); H1e=cofactor_map(L1e); H2e=cofactor_map(L2e)
R1e=sp.Matrix([[0,1,0],[1,0,0],[0,0,1]]); R2e=sp.eye(3)
A1e=frame_aware_physical_synthesis_block(Hpe,H1e,R1e)
A2e=frame_aware_physical_synthesis_block(Hpe,H2e,R2e)
Pevent=[sp.diag(1,0,0),sp.diag(0,1,0),sp.diag(0,0,1)]
projector_family_zero=all(X == sp.zeros(3) for X in projector_family_algebra_residuals(Pevent))
Qevent=sp.Matrix(6,6,sp.symbols("Qevent0:36"))
event_transfer_all_zero=all(
    spectral_event_transfer_residual(Qevent,[A1e,A2e],lam,P,[Pevent,Pevent]) == 0
    for lam,P in zip((4,9,16),Pevent)
)
event_full_energy_zero=full_parent_spectral_energy_residual(
    Qevent,[A1e,A2e],(4,9,16),Pevent,sp.diag(4,9,16)
) == 0
Qcross_event=sp.zeros(6); Qcross_event[0,0]=1
event_cross_channel_term=spectral_event_transfer_term(
    Qcross_event,[A1e,A2e],1,Pevent[1],[Pevent,Pevent],0,0,0,0
)
event_cross_channel_nonzero=sp.simplify(event_cross_channel_term) != 0
event_cross_channel_residual_zero=spectral_event_transfer_residual(
    Qcross_event,[A1e,A2e],1,Pevent[1],[Pevent,Pevent]
) == 0

Pxy_event=sp.diag(1,1,0); Pz_event=sp.diag(0,0,1)
degenerate_parent_projector_family_zero=all(
    X == sp.zeros(3) for X in projector_family_algebra_residuals([Pxy_event,Pz_event])
)
degenerate_event_transfer_zero=spectral_event_transfer_residual(
    Qevent,[sp.eye(3),sp.eye(3)],4,Pxy_event,[Pevent,Pevent]
) == 0
e1ev,e2ev,e3ev=sp.eye(3)[:,0],sp.eye(3)[:,1],sp.eye(3)[:,2]
cev=sp.sqrt(2)/2; uev=cev*(e1ev+e2ev); vev=cev*(e1ev-e2ev)
fam_a_ev=[e1ev*e1ev.T,e2ev*e2ev.T,e3ev*e3ev.T]
fam_b_ev=[uev*uev.T,vev*vev.T,e3ev*e3ev.T]
degenerate_child_basis_transfer_zero=degenerate_block_internal_basis_residual(
    Qevent,[sp.eye(3),sp.eye(3)],4,Pxy_event,0,[fam_a_ev,Pevent],fam_a_ev,fam_b_ev
) == 0

one_mode_event_transfer=two_child_opposite_residual_transfer_calibration(one_mode_lineage["chi0"])
one_mode_event_transfer_zero=one_mode_event_transfer["transfer_residual"] == 0 and one_mode_event_transfer["parent_channel"] == 0
one_mode_event_same_positive=sp.simplify(one_mode_event_transfer["same_child_same_channel"]) != 0
one_mode_event_cross_negative=sp.simplify(
    one_mode_event_transfer["cross_child_same_channel"] + one_mode_event_transfer["same_child_same_channel"]
) == 0
one_mode_event_other_sectors_zero=one_mode_event_transfer["same_child_cross_channel"] == 0 and one_mode_event_transfer["cross_child_cross_channel"] == 0
sector_event=transfer_sector_sums(Qevent,[A1e,A2e],4,Pevent[0],[Pevent,Pevent])
sector_event_sum_zero=sp.simplify(sum(sector_event)-4*sp.trace(Pevent[0]*(sp.Matrix.hstack(A1e,A2e)*Qevent*sp.Matrix.hstack(A1e,A2e).T))) == 0

# Gauge-normal finite-event composition.
normal_physical_zero=physical_raw_normal_form_residual(Hpf,H1f,R1f) == sp.zeros(3)
normal_codeforming_zero=codeforming_raw_normal_form_residual(Lpf,L1f,R1f) == sp.zeros(3)
Lmid_nf=sp.Matrix([[1,1,0],[0,2,1],[1,0,3]]); Hmid_nf=cofactor_map(Lmid_nf)
normal_frame_comp_zero=frame_aware_event_composition_residual(
    Hpf,Hmid_nf,H1f,R1f,R2f
) == sp.zeros(3)
normal_code_comp_zero=codeforming_event_composition_residual(
    Lpf,Lmid_nf,L1f,R1f,R2f
) == sp.zeros(3)
Qnf=sp.Matrix(3,3,sp.symbols("Qnormal0:9"))
A1nf=sp.Matrix([[1,2,0],[0,1,1]])
A2nf=sp.Matrix([[1,0],[0,1],[1,1]])
normal_second_moment_zero=second_moment_event_composition_residual(Qnf,A1nf,A2nf) == sp.zeros(3)
normal_pair_functor_zero=pair_functor_event_composition_residual(A1nf,A2nf) == sp.zeros(9,9)
A1spec_nf=sp.Matrix([[1,1,0],[0,1,0],[0,0,1]])
A2spec_nf=sp.Matrix([[2,0,1],[0,1,0],[1,0,1]])
Pnf=Pevent
normal_projector_telescope_zero=intermediate_projector_telescope_residual(
    Qnf,A1spec_nf,A2spec_nf,5,Pnf[0],Pnf
) == 0
e1nf,e2nf,e3nf=sp.eye(3)[:,0],sp.eye(3)[:,1],sp.eye(3)[:,2]
cnf=sp.sqrt(2)/2; unf=cnf*(e1nf+e2nf); vnf=cnf*(e1nf-e2nf)
fam_a_nf=[e1nf*e1nf.T,e2nf*e2nf.T,e3nf*e3nf.T]
fam_b_nf=[unf*unf.T,vnf*vnf.T,e3nf*e3nf.T]
normal_degenerate_telescope_zero=intermediate_degenerate_basis_telescope_residual(
    Qnf,A1spec_nf,A2spec_nf,5,sp.diag(1,1,0),fam_a_nf,fam_b_nf
) == 0
channel_nf=channel_only_composition_counterexample()
channel_nf_same_inputs=channel_nf["input_channels_plus"] == channel_nf["input_channels_minus"]
channel_nf_parent_diff=channel_nf["parent_channel_difference"] == 2
channel_nf_coherence_opposite=sp.simplify(channel_nf["cross_coherence_plus"]+channel_nf["cross_coherence_minus"]) == 0 and channel_nf["cross_coherence_plus"] != 0
channel_nf_psd=all(
    all(ev >= 0 for ev in channel_nf[key].eigenvals()) for key in ("Q_plus","Q_minus")
)
qobs00,qobs11,qobs22,qobs01,qobs02,qobs12=sp.symbols(
    "qobs00 qobs11 qobs22 qobs01 qobs02 qobs12"
)
Qobs=sp.Matrix([
    [qobs00,qobs01,qobs02],
    [qobs01,qobs11,qobs12],
    [qobs02,qobs12,qobs22],
])
normal_probe_reconstruction_zero=symmetric_event_probe_reconstruction_residual(Qobs) == sp.zeros(3)

# Literal first-bad selected residual readout semantics.
Tsel=sp.Matrix(3,3,sp.symbols("Tsel0:9"))
selector_factorization_residual=selector_switch_universal_factorization_residual(2,0,1,Tsel)
selector_factorization_nonzero=selector_factorization_residual != sp.zeros(3,6)
selector_unavoidable_identity=selector_switch_unavoidable_new_block(2,0,1,Tsel) == sp.eye(3)
selector_state_counter=selector_switch_state_counterexample()
selector_state_old_same=selector_state_counter["old_readout_1"] == selector_state_counter["old_readout_2"]
selector_state_new_diff=selector_state_counter["new_readout_1"] != selector_state_counter["new_readout_2"]
Qsel=sp.Matrix(6,6,sp.symbols("Qselector0:36"))
selector_pair_jump_zero=selector_second_moment_jump_residual(Qsel,2,0,1) == sp.zeros(3)
selector_faces=hidden_reset_faces_from_blocks(Qsel)
selector_faces_expected=(
    selector_faces["left"] == sp.simplify(selector_faces["Q10"]-selector_faces["Q00"])
    and selector_faces["right"] == sp.simplify(selector_faces["Q01"]-selector_faces["Q00"])
    and selector_faces["quadratic"] == sp.simplify(selector_faces["Q11"]-selector_faces["Q10"]-selector_faces["Q01"]+selector_faces["Q00"])
)
selector_psd_counter=selector_switch_second_moment_counterexample()
selector_psd_old_same=selector_psd_counter["old_Q_1"] == selector_psd_counter["old_Q_2"]
selector_psd_new_diff=selector_psd_counter["new_Q_1"] != selector_psd_counter["new_Q_2"]
selector_psd_full=all(
    all(ev >= 0 for ev in selector_psd_counter[key].eigenvals())
    for key in ("Q_full_1","Q_full_2")
)
E0sel=germ_extraction_map(2,0); E1sel=germ_extraction_map(2,1)
Tad=sp.Matrix([[1,2,0],[0,1,0],[0,0,1]])
Sad=sp.Matrix.vstack(sp.eye(3),Tad)
selector_admissible_factor_zero=selector_switch_factorization_on_subspace_residual(
    E0sel,E1sel,Sad,Tad
) == sp.zeros(3)
selector_identity_event_factor_nonzero=selected_physical_event_factorization_residual(
    sp.eye(6),2,0,2,1,Tsel
) != sp.zeros(3,6)
B0sel=sp.diag(2,1,3); B1sel=sp.Matrix([[1,1,0],[0,1,0],[0,0,1]])
selector_same_germ_event_factor_zero=selected_physical_event_factorization_residual(
    sp.diag(B0sel,B1sel),2,0,2,0,B0sel
) == sp.zeros(3,6)

# Same-replica persistent residual-library dynamics.
Qlib1=sp.Matrix([[1,0,2],[0,1,0],[1,0,1]])
Qlib2=sp.Matrix([[0,1,0],[1,0,1],[0,1,1]])
Glib=same_replica_library_qv([Qlib1,Qlib2],nu)
library_cross_block_zero=library_qv_block_residual([Qlib1,Qlib2],0,1,nu) == sp.zeros(3)
library_cross_block_expected=Glib[:3,3:] == sp.simplify(2*nu*Qlib1*Qlib2.T)
library_selector_readout_zero=selected_qv_readout_residual([Qlib1,Qlib2],1,nu) == sp.zeros(3)
Alib=sp.Matrix([[1,0,0,1,0,0],[0,1,0,0,1,0],[0,0,1,0,0,1]])
library_event_qv_zero=linear_event_qv_functor_residual([Qlib1,Qlib2],Alib,nu) == sp.zeros(3)
library_independent_diff=independent_vs_common_qv_difference([Qlib1,Qlib2],nu)
library_independent_diff_nonzero=library_independent_diff != sp.zeros(6)
library_independent_diag_zero=library_independent_diff[:3,:3] == sp.zeros(3) and library_independent_diff[3:,3:] == sp.zeros(3)
library_mean_rate_zero=stacked_martingale_mean_rate(2) == sp.zeros(6,1)
library_rank,library_driver=qv_image_rank_bound([Qlib1,Qlib2],sp.Integer(1))
library_rank_bounded=library_rank <= library_driver and library_driver == 3

one_mode_library=one_mode_two_packet_common_noise_calibration(t,nu,k)
one_mode_library_noise_opposite=one_mode_library["opposite_noise_residual"] == 0 and one_mode_library["q1"] != 0
one_mode_library_cross_negative=one_mode_library["cross_qv"] == sp.simplify(-one_mode_library["diagonal_qv"])
one_mode_library_common_cancel=one_mode_library["synthesized_common_qv"] == sp.zeros(3)
one_mode_library_independent_positive=one_mode_library["synthesized_independent_qv"] != sp.zeros(3)
one_mode_library_event_functor_zero=one_mode_library["common_event_functor_residual"] == sp.zeros(3)

# Hybrid selected residual semimartingale: continuous common-noise branch plus finite selector jumps.
Qhy0=sp.Matrix([[1,0,1],[0,1,0],[1,0,2]])
Qhy1=sp.Matrix([[0,1,0],[1,0,1],[0,1,1]])
hybrid_continuous_qv_zero=selected_continuous_qv_factorization_residual([Qhy0,Qhy1],0,nu) == sp.zeros(3)
Xhy=sp.Matrix([1,2,3,4,5,6])
Jhy=selector_readout_jump(Xhy,2,0,1)
hybrid_jump_square_expected=selector_jump_optional_qv(Xhy,2,0,1) == sp.simplify(Jhy*Jhy.T)
hybrid_jump_dyad_zero=selector_jump_dyad_residual(Xhy,2,0,1) == sp.zeros(3)
Ghy=sp.diag(1,2,3)
hybrid_total_qv_expected=hybrid_optional_qv([Ghy],[Jhy]) == sp.simplify(Ghy+Jhy*Jhy.T)
closed_hybrid=selector_closed_excursion(Xhy,2,[0,1,0])
closed_hybrid_state_zero=closed_hybrid["state_change"] == sp.zeros(3,1)
closed_hybrid_jump_sum_zero=closed_hybrid["jump_sum"] == sp.zeros(3,1)
closed_hybrid_jump_qv_nonzero=closed_hybrid["jump_optional_qv"] != sp.zeros(3)

one_mode_hybrid=one_mode_selector_excursion_calibration(t,nu,k)
one_mode_hybrid_opposite=one_mode_hybrid["chi1"] == sp.simplify(-one_mode_hybrid["chi0"])
one_mode_hybrid_state_zero=one_mode_hybrid["state_change"] == sp.zeros(3,1) and one_mode_hybrid["jump_sum"] == sp.zeros(3,1)
one_mode_hybrid_jump_opposite=one_mode_hybrid["jump_10"] == sp.simplify(-one_mode_hybrid["jump_01"])
one_mode_hybrid_jump_qv_nonzero=one_mode_hybrid["jump_optional_qv"] != sp.zeros(3) and sp.simplify(one_mode_hybrid["jump_optional_qv_trace"]) != 0

# Simultaneous physical packet event plus selector switch.
Icomb=sp.eye(3); Zcomb=sp.zeros(3)
Acomb=sp.Matrix.vstack(
    sp.Matrix.hstack(Icomb,Zcomb),
    sp.Matrix.hstack(Icomb,Icomb),
)
combined_interaction_zero=same_space_event_interaction_residual(Acomb,2,0,1) == sp.zeros(3,6)
combined_seq_phys,combined_seq_sel=same_space_sequential_product_rule_residuals(Acomb,2,0,1)
combined_sequential_zero=combined_seq_phys == sp.zeros(3,6) and combined_seq_sel == sp.zeros(3,6)
combined_physical_face,combined_selector_face,combined_mixed_face=same_space_event_interaction_faces(Acomb,2,0,1)
combined_mixed_nonzero=combined_mixed_face != sp.zeros(3,6)
combined_naive_missing_mixed=sp.simplify(
    combined_selected_jump_operator(Acomb,2,0,2,1)-combined_physical_face-combined_selector_face
) == combined_mixed_face
Qcomb=sp.diag(1,2,3,4,5,6)
combined_second_moment_zero=combined_second_moment_jump_residual(Qcomb,Acomb,2,0,2,1) == sp.zeros(3)
Xcomb=sp.Matrix([1,2,3,4,5,6])
Qcomb_path=sp.simplify(Xcomb*Xcomb.T)
_,_,combined_quad_face=combined_second_moment_jump_faces(Qcomb_path,Acomb,2,0,2,1)
combined_jump_square_zero=sp.simplify(
    combined_quad_face-combined_jump_square(Xcomb,Acomb,2,0,2,1)
) == sp.zeros(3)

one_mode_combined=one_mode_hidden_germ_synthesis_calibration(t,nu,k)
one_mode_combined_opposite=one_mode_combined["chi1"] == sp.simplify(-one_mode_combined["chi0"])
one_mode_combined_physical_old_zero=one_mode_combined["physical_old_jump"] == sp.zeros(3,1)
one_mode_combined_mixed_nonzero=one_mode_combined["mixed_jump"] != sp.zeros(3,1)
one_mode_combined_post_zero=one_mode_combined["post_selected"] == sp.zeros(3,1)
one_mode_combined_naive_false=one_mode_combined["total_jump"] != one_mode_combined["selector_old_jump"]
one_mode_combined_mixed_closes=sp.simplify(
    one_mode_combined["total_jump"]-one_mode_combined["selector_old_jump"]-one_mode_combined["mixed_jump"]
) == sp.zeros(3,1)

# Continuous selected Brownian-source rate revaluation across the combined event.
Nrate=sp.Matrix(6,3,sp.symbols("nr0:18"))
combined_rate_revaluation_zero=combined_continuous_qv_rate_revaluation_residual(
    Nrate,Acomb,2,0,2,1,nu
) == sp.zeros(3)
Bpre_rate=pre_selected_noise_response(Nrate,2,0)
Bpost_rate=post_selected_noise_response(Nrate,Acomb,2,1)
combined_endpoint_rate_shapes=(Bpre_rate.shape,Bpost_rate.shape) == ((3,3),(3,3))
rate_left,rate_right,rate_quad=combined_continuous_qv_rate_revaluation_faces(
    Nrate,Acomb,2,0,2,1,nu
)
combined_rate_faces_nontrivial=rate_left != sp.zeros(3) and rate_quad != sp.zeros(3)
source_jump_separation=source_revaluation_vs_jump_square_calibrations()
source_nonzero_jump_zero=bool(source_jump_separation["rate_revaluation_nonzero_with_zero_state_jump_square"])
source_zero_jump_nonzero=bool(source_jump_separation["zero_rate_revaluation_with_nonzero_state_jump_square"])

one_mode_rate=one_mode_hidden_synthesis_qv_rate_calibration(t,nu,k)
one_mode_rate_opposite=one_mode_rate["opposite_noise_residual"] == 0
one_mode_rate_selector_only_same=one_mode_rate["selector_only_post_qv_rate"] == one_mode_rate["pre_qv_rate"]
one_mode_rate_post_zero=one_mode_rate["actual_post_qv_rate"] == sp.zeros(3)
one_mode_rate_actual_negative_pre=one_mode_rate["actual_rate_revaluation"] == sp.simplify(-one_mode_rate["pre_qv_rate"])
one_mode_rate_pair_faces_close=one_mode_rate["rate_revaluation_residual"] == sp.zeros(3)

# Random/adaptive selected event-map correlation.
Cr1=sp.Matrix([[1,2],[0,1]])
Cr2=sp.Matrix([[2,0],[1,1]])
xr1=sp.Matrix([3,1]); xr2=sp.Matrix([0,2])
random_mean_residual_zero=two_replica_mean_output_residual(Cr1,xr1,Cr2,xr2) == sp.zeros(2,1)
_,random_mean_corr=two_replica_mean_output_faces(Cr1,xr1,Cr2,xr2)
random_mean_corr_nonzero=random_mean_corr != sp.zeros(2,1)
Qr1=sp.Matrix([[3,1],[1,2]])
Qr2=sp.Matrix([[1,0],[0,4]])
random_congruence_zero=two_replica_congruence_residual(Cr1,Qr1,Cr2,Qr2) == sp.zeros(2)
_,random_disp,random_corr_l,random_corr_r=two_replica_congruence_faces(Cr1,Qr1,Cr2,Qr2)
random_disp_nonzero=random_disp != sp.zeros(2)
random_corr_nonzero=random_corr_l != sp.zeros(2) or random_corr_r != sp.zeros(2)
random_disp_probe=event_dispersion_face_psd_quadratic_form(
    sp.eye(2),sp.diag(2,5),sp.Matrix([[0,1],[1,0]]),sp.Matrix([3,-1])
)
random_disp_probe_nonnegative=bool(random_disp_probe >= 0)
random_alignment=adaptive_event_alignment_calibrations()
random_alignment_positive_expected=(
    random_alignment["positive_exact"],random_alignment["positive_naive"],
    random_alignment["positive_dispersion"],random_alignment["positive_corr_left"],
    random_alignment["positive_corr_right"]
) == (4,1,1,1,1)
random_alignment_negative_expected=(
    random_alignment["negative_exact"],random_alignment["negative_naive"],
    random_alignment["negative_dispersion"],random_alignment["negative_corr_left"],
    random_alignment["negative_corr_right"]
) == (0,1,1,-1,-1)
random_payloads_psd=bool(random_alignment["all_payloads_psd"])
Cq1=sp.Matrix([[1,0]]); Cq2=sp.Matrix([[0,1]])
Nq1=sp.Matrix([[1,0],[0,0]]); Nq2=sp.Matrix([[0,0],[0,2]])
Gq1=sp.simplify(Nq1*Nq1.T); Gq2=sp.simplify(Nq2*Nq2.T)
random_qv_congruence_zero=two_replica_congruence_residual(Cq1,Gq1,Cq2,Gq2) == sp.zeros(1)

# Necessary physical admissibility constraints for future first-bad rules.
eps_adm=sp.Matrix([2,-1,3])
H_adm=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
S_adm=sp.Matrix([[1,1,0],[0,2,0],[1,0,1]])
admiss_physical_gauge_zero=physical_score_passive_gauge_residual(eps_adm,H_adm,S_adm) == 0
admiss_raw_gauge_nonzero=raw_score_passive_gauge_change(sp.Matrix([1,0,0]),sp.eye(3),sp.diag(2,1,1)) != 0
admiss_ranking=passive_raw_ranking_flip_calibration()
admiss_raw_ranking_flips=admiss_ranking["raw_winner_before"] != admiss_ranking["raw_winner_after"]
admiss_physical_ranking_fixed=admiss_ranking["physical_winner_before"] == admiss_ranking["physical_winner_after"] and admiss_ranking["physical_before"] == admiss_ranking["physical_after"]
admiss_event_gauge=passive_event_gauge_calibration()
admiss_event_raw_changes=bool(admiss_event_gauge["raw_block_changes"])
admiss_event_physical_fixed=admiss_event_gauge["physical_event_gauge_residual"] == sp.zeros(3)
rho_adm=sp.symbols("rho_adm", positive=True)
Y_adm=sp.symbols("Y_adm", real=True)
admiss_support=physical_residual_support_locality_no_go(Y_adm,t,nu,rho_adm)
admiss_residual_collapse_support_nonlocal=admiss_support["physical_energy_limit"] == 0 and admiss_support["support_line_limit"] == 1
admiss_library=persistent_library_switch_obstruction()
admiss_library_all=all(admiss_library.values())
admiss_coherence=full_coherence_event_obstruction()
admiss_coherence_needed=admiss_coherence["input_channels_equal"] and admiss_coherence["parent_channels_different"] and admiss_coherence["parent_channel_difference"] == 2
admiss_adaptive=adaptive_event_joint_law_obstruction()
admiss_adaptive_needed=admiss_adaptive["aligned_mean_closure_false"] and admiss_adaptive["anti_aligned_mean_closure_false"]
admiss_ledger=first_bad_admissibility_ledger(Y_adm,t,nu,rho_adm)
admiss_necessary_flags=all(bool(admiss_ledger[k]) for k in [
    "raw_ranking_is_gauge_artifact","physical_ranking_gauge_invariant",
    "physical_event_map_gauge_invariant","residual_collapse_does_not_imply_support_locality",
    "persistent_library_needed_for_switch","full_coherence_needed_for_linear_events",
    "adaptive_joint_law_needed",
])
admiss_no_sufficiency=not bool(admiss_ledger["sufficient_first_bad_functional_defined"]) and not bool(admiss_ledger["restart_continuation_regularity_proved"])

# Literal local enstrophy growth gate and Kelvin bulk typing.
x_lg,y_lg,z_lg=sp.symbols("x_lg y_lg z_lg", real=True)
coords_lg=(x_lg,y_lg,z_lg)
u_lg=sp.Matrix([x_lg*y_lg,y_lg*z_lg,z_lg*x_lg])
omega_lg=sp.Matrix([x_lg+t,y_lg**2,z_lg+x_lg])
faces_lg=enstrophy_balance_faces(u_lg,omega_lg,coords_lg,t,nu)
local_balance_contraction_zero=faces_lg["balance_minus_vorticity_contraction"] == 0
G_lg=sp.Matrix([[1,2,0],[0,1,3],[2,0,1]])
H_lg=sp.Matrix([[2,1,0],[0,3,1],[1,0,2]])
local_kelvin_bulk_zero=kelvin_bulk_packet_residual(G_lg,H_lg,nu) == 0
s_lg,b_lg,ell_lg=sp.symbols("s_lg b_lg ell_lg")
local_critical_curvature_zero=critical_point_growth_residual(s_lg-b_lg-nu*ell_lg,s_lg,b_lg,-ell_lg,nu) == 0
local_margin_expected=growth_gate_margin(s_lg,b_lg) == s_lg-b_lg
A_lg=sp.symbols("A_lg", positive=True)
abc_lg=abc_beltrami_enstrophy_stretching_calibration(A_lg,nu,t,coords_lg)
abc_lg_beltrami_zero=abc_lg["beltrami_residual"] == sp.zeros(3,1)
abc_lg_transport_zero=abc_lg["stretching_minus_enstrophy_transport"] == 0
abc_lg_ns_zero=abc_lg["ns_residual"] == sp.zeros(3,1)
abc_point_lg={x_lg:sp.pi/4,y_lg:sp.pi/4,z_lg:sp.pi/4}
abc_lg_critical_zero=sp.simplify(abc_lg["enstrophy_gradient"].subs(abc_point_lg)) == sp.zeros(3,1)
abc_lg_critical_stretch_zero=sp.simplify(abc_lg["stretching"].subs(abc_point_lg)) == 0
a_lg,r0_lg=sp.symbols("a_lg r0_lg", positive=True)
aff_lg=affine_vortex_local_growth_calibration(a_lg,r0_lg,t,coords_lg,nu)
r_lg=sp.simplify(r0_lg*sp.exp(2*a_lg*t))
aff_lg_expected_growth=sp.simplify(8*a_lg*r_lg**2)
aff_lg_ns_zero=aff_lg["ns_residual"] == sp.zeros(3,1)
aff_lg_uniform=aff_lg["gradient"] == sp.zeros(3,1) and aff_lg["laplacian"] == 0
aff_lg_kelvin_zero=aff_lg["kelvin_bulk"] == 0
aff_lg_growth_expected=aff_lg["stretching"] == aff_lg_expected_growth and aff_lg["time"] == aff_lg_expected_growth
aff_lg_balance_zero=aff_lg["balance_residual"] == 0
aff_lg_nonperiodic=aff_lg["periodicity_defect_x_2pi"] != sp.zeros(3,1)

# Moving enstrophy critical-point geometry.
A_mc=sp.symbols("A_mc", positive=True)
abc_mc=abc_fixed_critical_point_speed_calibration(A_mc,nu,t,coords_lg)
abc_mc_grad_zero=abc_mc["gradient"] == sp.zeros(3,1)
abc_mc_hessian_invertible=abc_mc["hessian_det"] != 0
abc_mc_negative_sylvester=bool(abc_mc["hessian"][0,0] < 0 and sp.det(abc_mc["hessian"][:2,:2]) > 0 and abc_mc["hessian"].det() < 0)
abc_mc_fluid_nonzero=abc_mc["fluid_velocity"] != sp.zeros(3,1)
abc_mc_fixed=abc_mc["critical_velocity"] == sp.zeros(3,1) and abc_mc["predicted_critical_velocity"] == sp.zeros(3,1)
abc_mc_constraint_zero=abc_mc["constraint_speed_residual"] == sp.zeros(3,1) and abc_mc["pde_speed_residual"] == sp.zeros(3,1)
abc_mc_relative_minus_u=sp.simplify(abc_mc["relative_velocity"]+abc_mc["fluid_velocity"]) == sp.zeros(3,1)
a_mc,r0_mc=sp.symbols("a_mc r0_mc", positive=True)
aff_mc=affine_degenerate_critical_speed_calibration(a_mc,r0_mc,t,coords_lg,nu)
aff_mc_degenerate=aff_mc["gradient"] == sp.zeros(3,1) and aff_mc["hessian"] == sp.zeros(3) and aff_mc["growth_gradient"] == sp.zeros(3,1)
aff_mc_speed_nonunique=aff_mc["speed_residual_v1"] == sp.zeros(3,1) and aff_mc["speed_residual_v2"] == sp.zeros(3,1)
# Critical-path value derivative loses path velocity when grad e=0.
ft_mc=sp.symbols("ft_mc")
value_speed_independent=critical_path_value_derivative_residual(ft_mc,ft_mc,sp.zeros(3,1),sp.Matrix([3,-2,5])) == 0

# Critical-Hessian evolution and curvature-volume law.
a_he,b_he,c1_he,c2_he,c3_he=sp.symbols("a_he b_he c1_he c2_he c3_he")
e_he=-(x_lg-a_he*t)**2-2*(y_lg-b_he*t)**2-3*z_lg**2
u_he=sp.Matrix([c1_he,c2_he,c3_he])
grad_e_he=sp.Matrix([sp.diff(e_he,q) for q in coords_lg])
R_he=sp.simplify(sp.diff(e_he,t)+(grad_e_he.T*u_he)[0])
point_he={x_lg:a_he*t,y_lg:b_he*t,z_lg:0}
v_he=sp.Matrix([a_he,b_he,0])
faces_he=critical_hessian_evolution_faces_at(e_he,u_he,R_he,coords_lg,t,point_he,v_he)
hessian_evolution_zero=faces_he["residual"] == sp.zeros(3)

p_he,q_he=sp.symbols("p_he q_he")
Gu_he=sp.Matrix([[p_he,2,0],[0,q_he,1],[3,0,-p_he-q_he]])
H_he=sp.diag(-2,-3,-5)
strain_he,rotation_he=hessian_connection_strain_rotation_faces(Gu_he,H_he)
connection_split_zero=hessian_connection_strain_rotation_residual(Gu_he,H_he) == sp.zeros(3)
connection_nonzero=strain_he+rotation_he != sp.zeros(3)
connection_logdet_zero=hessian_connection_logdet_rate(Gu_he,H_he) == 0
connection_divergence_zero=hessian_connection_logdet_divergence_residual(Gu_he,H_he) == 0
strain_rate_he,rotation_rate_he=hessian_strain_rotation_logdet_rates(Gu_he,H_he)
strain_rotation_rates_expected=strain_rate_he == 0 and rotation_rate_he == 0

Hj_he=sp.diag(-sp.exp(t),-2*sp.exp(2*t),-3*sp.exp(-t))
Hjd_he=sp.diff(Hj_he,t)
detjd_he=sp.diff(Hj_he.det(),t)
jacobi_he_zero=determinant_jacobi_residual(Hj_he,Hjd_he,detjd_he) == 0
logdet_he_expected=hessian_logdet_rate(Hj_he,Hjd_he) == 2

Gface_he=sp.diag(1,2,3)
Cface_he=sp.Matrix([[0,1,0],[1,0,0],[0,0,0]])
Rface_he=sp.diag(-1,0,1)
face_rates_he=hessian_logdet_face_rates({
    "hessian":sp.diag(-2,-3,-4),
    "path_derivative":Gface_he+Cface_he+Rface_he,
    "growth_hessian":Gface_he,
    "connection":Cface_he,
    "relative_transport":Rface_he,
})
face_rates_sum_zero=sp.simplify(face_rates_he["total"]-face_rates_he["growth"]-face_rates_he["connection"]-face_rates_he["relative"]) == 0
finite_lograte_nonzero=nonzero_determinant_from_lograte(sp.Integer(2),sp.Integer(3)) != 0

abc_he=abc_hessian_logdet_calibration(A_mc,nu,t,coords_lg)
abc_he_hdot_expected=abc_he["hessian_dot_plus_2nu_hessian"] == sp.zeros(3)
abc_he_det_nonzero=abc_he["determinant"] != 0
abc_he_logdet_expected=abc_he["logdet_rate"] == -6*nu
abc_he_jacobi_zero=abc_he["jacobi_residual"] == 0
abc_he_div_zero=abc_he["divergence"] == 0
abc_he_connection_zero=abc_he["connection_logdet_rate"] == 0 and abc_he["connection_divergence_residual"] == 0

# Critical-branch competition and ranking crossing.
geom_bc=nondegenerate_value_crossing_geometry_calibration(t)
geom_bc_cross_zero=geom_bc["gap"].subs(t,0) == 0
geom_bc_transverse=geom_bc["gap_rate"] == 2
geom_bc_nondegenerate=geom_bc["det_hessian_1"] != 0 and geom_bc["det_hessian_2"] != 0

shear_bc=three_mode_branch_crossing_calibration(x_lg,y_lg,z_lg,t,nu)
shear_bc_ns_zero=shear_bc["ns_residual"] == sp.zeros(3,1)
shear_bc_critical=shear_bc["critical_y_derivative_0"] == 0 and shear_bc["critical_y_derivative_pi"] == 0
shear_bc_tie=shear_bc["value_0"] == shear_bc["value_pi"] == sp.Rational(9,2)*sp.exp(-2)
shear_bc_curvatures=shear_bc["hessian_yy_0"] == -12*sp.exp(-2) and shear_bc["hessian_yy_pi"] == -60*sp.exp(-2)
shear_bc_gap_rate=shear_bc["gap_rate_at_crossing"] == 48*nu*sp.exp(-2) and transverse_crossing_orientation(shear_bc["gap_rate_at_crossing"]) == 1
shear_bc_pure_curvature=shear_bc["stretching_0"] == 0 and shear_bc["stretching_pi"] == 0 and shear_bc["kelvin_bulk_0"] == 0 and shear_bc["kelvin_bulk_pi"] == 0 and shear_bc["gap_rate_face_residual"] == 0
shear_bc_rates_expected=shear_bc["time_rate_0"] == -12*nu*sp.exp(-2) and shear_bc["time_rate_pi"] == -60*nu*sp.exp(-2)
shear_bc_both_decrease=bool(shear_bc["time_rate_0"] < 0 and shear_bc["time_rate_pi"] < 0)
shear_bc_selector_value_continuous=shear_bc["selector_scalar_jump_at_tie"] == 0
shear_bc_envelope_switch=shear_bc["envelope"]["derivative_jump"] == 48*nu*sp.exp(-2)

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
        "full_current_shape_anchor_qv": "Exact identity",
        "moving_kelvin_gauge_cartan": "Exact identity",
        "deformation_kelvin_cross_covariance": "Exact identity",
        "joint_D_K_short_horizon": "Rigorous consequence for locally smooth Navier--Stokes coefficients",
        "exact_shear_D_K_cross": "Audited calibration",
        "reverse_current_area_vs_cauchy_frame": "Exact identity / theorem-type correction",
        "finite_shape_kelvin_descent_error_sde": "Exact identity",
        "finite_shape_error_pathwise_vs_horizon_covariance": "Exact identity",
        "centered_finite_shape_quadrupole_jet": "Rigorous consequence for centered locally smooth surfaces",
        "cubic_shape_bias_covariance_blindness": "Audited calibration / rigorous no-go consequence",
        "one_mode_finite_shape_error_covariance": "Audited calibration",
        "abc_finite_shape_error_drift": "Audited calibration",
        "finite_moment_covariance_blindness": "Audited calibration family / rigorous no-go consequence",
        "reverse_age_oriented_surface_moment_hierarchy": "Exact identity",
        "affine_surface_moment_order_closure": "Exact identity",
        "nonlinear_surface_moment_order_raising": "Exact homogeneous-polynomial identity / rigorous local-jet consequence",
        "material_surface_centering_preservation": "Audited calibration: false universally",
        "single_anchor_oriented_recentering": "Exact geometry / audited obstruction",
        "shear_hidden_oriented_moment_tower": "Exact shear identity",
        "finite_moment_dynamic_shape_closure": "Audited calibration family / rigorous no-go consequence",
        "first_bad_infinite_moment_jet_collapse": "Open-literal",
        "surface_moment_scalar_refinement_weight": "Exact identity",
        "codeforming_surface_moment_pullback": "Exact identity",
        "codeforming_nonaffinity_reduction": "Exact identity",
        "codeforming_generating_current_law": "Exact identity",
        "coherent_refinement_codeforming_gauge": "Exact identity",
        "codeforming_homogeneous_jet_scale_shape": "Exact identity",
        "codeforming_constancy_vs_support_locality": "Audited calibration / rigorous no-go consequence",
        "support_locality_vs_codeforming_affinity": "Audited calibration / rigorous no-go consequence",
        "first_bad_codeforming_nonaffinity_collapse": "Open-literal",
        "codeforming_kelvin_nonaffinity_one_form": "Exact identity / exact Stokes--Piola identity",
        "codeforming_nonaffinity_three_face_split": "Exact identity",
        "kinematic_vs_kelvin_nonaffinity_scaling": "Audited calibration / rigorous type-separation consequence",
        "first_bad_codeforming_kelvin_one_form_collapse": "Open-literal",
        "codeforming_kelvin_anchor_noise": "Exact identity / audited exact one-mode Navier--Stokes calibration",
        "codeforming_finite_shape_error_sde": "Exact identity",
        "metric_whitened_pointwise_orientation_inversion": "Exact identity",
        "metric_whitened_finite_face_reconstruction": "Exact physical typing",
        "metric_whitened_codeforming_stokes_bridge": "Exact Stokes--Piola / whitening identity",
        "metric_whitened_homogeneous_exponent_ladder": "Exact identity",
        "metric_whitened_reconstruction_covariance": "Exact identity",
        "metric_whitened_reconstruction_qv": "Exact identity",
        "metric_whitened_local_residual_cross_blocks": "Exact covariance identity / audited algebraic calibration",
        "cubic_finite_reconstruction_not_pointwise": "Audited calibration / rigorous finite-scale type separation",
        "cubic_whitened_r2": "Audited calibration",
        "fixed_state_whitened_topology_physical_typing": "Exact fixed-state topology identification",
        "codeforming_whitened_future_clock_identification": "Open-literal",
        "first_bad_reconstructed_kelvin_residual_collapse": "Open",
        "actual_area_vs_local_frame_kelvin_error": "Exact identity / physical typing",
        "finite_shape_drift_geometry_transfer": "Exact Navier--Stokes/Nanson transfer identity",
        "local_frame_kelvin_error_pure_martingale": "Exact identity",
        "dynamic_reconstructed_line_connection": "Exact identity",
        "dynamic_reconstructed_residual_qv": "Exact identity",
        "dynamic_local_residual_cross_qv": "Exact identity",
        "dynamic_reconstructed_dyad_energy": "Exact Itô identity",
        "dynamic_full_reconstructed_cross_blocks": "Exact identity",
        "cubic_dynamic_reconstructed_conserved_mode": "Audited calibration / rigorous no-go consequence",
        "one_mode_dynamic_reconstructed_cross_qv": "Audited calibration",
        "dynamic_reconstructed_reduced_covariance_closure": "Open-literal",
        "dynamic_reconstructed_future_clock_identification": "Open-literal",
        "reverse_codeforming_volume_freeze": "Exact identity",
        "reverse_codeforming_residual_triangle": "Exact identity",
        "reverse_codeforming_local_martingale": "Exact identity",
        "reverse_codeforming_residual_martingale": "Exact identity",
        "reverse_codeforming_joint_gram": "Exact identity",
        "reverse_codeforming_physical_metric_work": "Exact identity",
        "reverse_codeforming_bias_vs_spread": "Exact martingale consequence under square-integrability",
        "cubic_codeforming_bias_qv_blind": "Audited calibration / rigorous covariance-only no-go",
        "one_mode_full_period_cross_qv_cancellation": "Audited calibration / rigorous cross-block necessity",
        "reverse_codeforming_clock_sign": "Exact clock-orientation identity",
        "first_bad_codeforming_bias_collapse": "Audited calibration: false as a necessary physical-descent condition",
        "first_bad_codeforming_spread_collapse": "Audited calibration: false as a necessary physical-descent condition",
        "codeforming_physical_weighted_topology": "Exact identity",
        "codeforming_fixed_frame_bias_spread": "Exact fixed-frame / conditional identity",
        "codeforming_random_frame_residual_correlation": "Exact two-replica identity / rigorous cross-face necessity",
        "quadratic_raw_codeforming_bias_no_go": "Audited calibration / rigorous target correction",
        "one_mode_raw_codeforming_spread_no_go": "Audited calibration / rigorous spread-target correction",
        "homogeneous_weighted_residual_exponent": "Exact identity",
        "first_bad_weighted_physical_residual_collapse": "Open",
        "directional_weighted_residual_decomposition": "Exact identity",
        "right_refinement_weighted_metric_law": "Exact identity",
        "finite_weighted_residual_midpoint_revaluation": "Exact finite-jump identity",
        "random_frame_weighted_event_correlation_face": "Exact full-state finite-event identity",
        "passive_gl_weighted_residual_gauge": "Exact gauge identity",
        "smooth_weighted_scale_shape_content_law": "Exact product-rule identity",
        "reverse_material_weighted_strain_qv_law": "Exact Ito/material-frame identity",
        "homogeneous_weighted_refinement_exponent": "Exact identity",
        "weighted_residual_vs_support_locality": "Audited calibration / rigorous seam no-go",
        "first_bad_directional_weighted_products": "Open",
        "pathwise_spectral_weighted_residual_channels": "Exact spectral-projector identity",
        "weighted_collapse_spectral_channel_equivalence": "Rigorous nonnegative finite-channel consequence",
        "principal_simple_spectrum_connection": "Exact identity conditional on simple spectrum",
        "principal_channel_three_face_rate": "Exact simple-spectrum identity",
        "principal_mixing_offdiagonal_metric_work": "Exact simple-spectrum identity",
        "degenerate_eigenspace_projector_gauge": "Exact gauge identity / theorem-domain correction",
        "linear_shear_principal_mixing_calibration": "Audited calibration",
        "first_bad_principal_channel_collapse": "Open",
        "selected_first_bad_spectral_factor_commutation": "Exact identity",
        "generic_germ_mixing_spectral_scope": "Audited generic algebraic scope counterexample",
        "selected_endpoint_block_spectral_bank": "Exact identity",
        "physical_residual_linear_synthesis_pair_functor": "Exact identity",
        "spectral_refinement_cross_child_content": "Exact identity",
        "selected_weighted_reset_pair_resolution": "Exact fixed/conditioned finite-event identity",
        "one_mode_spectral_cross_child_cancellation": "Audited calibration / rigorous cross-child necessity",
        "one_mode_selected_reset_signed_revaluation": "Audited calibration",
        "selected_reset_positive_path_no_go": "Audited calibration / rigorous no-positive-path consequence",
        "cross_event_principal_axis_lineage": "Audited structural correction: individual-axis matching is noncanonical; projector transfer is exact",
        "first_bad_physical_residual_refinement_lift": "Audited-conditional structural lift given an orientation-complete current packet map",
        "selected_spectral_hybrid_same_clock_ledger": "Rigorous conditional composition of exact identities",
        "first_bad_selected_spectral_lineage": "Open-literal",
        "orientation_packet_current_error_refinement": "Exact current/cochain identity",
        "frame_aware_physical_residual_synthesis": "Exact identity / uniqueness consequence",
        "frame_aware_independent_orientation_gauge": "Exact gauge identity",
        "frame_aware_cofactor_line_conjugation": "Exact identity",
        "frame_aware_codeforming_determinant_synthesis": "Exact identity",
        "frame_aware_isotropic_area_volume_weights": "Exact identity",
        "quadratic_frame_aware_refinement_calibration": "Audited calibration / rigorous no-naive-weight consequence",
        "frame_aware_residual_pair_functor": "Exact pair-functor identity",
        "orientation_preserving_scalar_packet_refinement_lift": "Exact type lift of existing scalar current refinement",
        "orientation_complete_chain_refinement_lift": "Exact chain-map tensor lift",
        "first_bad_orientation_packet_refinement_instantiation": "Open-literal",
        "spectral_projector_event_transfer": "Exact identity",
        "spectral_event_transfer_sector_partition": "Exact identity",
        "spectral_event_frame_conversion_cross_channel": "Audited generic mechanism",
        "spectral_event_degenerate_projector_regularity": "Exact projector-gauge identity",
        "one_mode_spectral_event_signed_cross_child": "Audited calibration / rigorous signed-sector necessity",
        "positive_child_channel_event_kernel_no_go": "Audited calibration / exact signed-law no-go",
        "selected_spectral_hybrid_projector_event_ledger": "Rigorous conditional composition of exact same-clock identities",
        "first_bad_spectral_event_transfer_instantiation": "Open-literal",
        "physical_event_gauge_normal_form": "Exact gauge-normal-form identity / bijection",
        "codeforming_event_volume_normal_form": "Exact identity / bijection",
        "frame_aware_event_composition": "Exact identity",
        "codeforming_event_composition": "Exact identity",
        "event_second_moment_composition": "Exact identity",
        "event_pair_functor_composition": "Exact identity",
        "intermediate_projector_telescope": "Exact identity",
        "intermediate_degenerate_basis_telescope": "Exact projector-gauge identity",
        "scalar_channel_event_compositional_closure": "Audited PSD calibration: false universally",
        "full_second_moment_linear_event_observational_completeness": "Exact polarization identity / audited-conditional on unrestricted linear event probes",
        "specified_linear_packet_event_normal_form": "Exact normal-form/functoriality theorem",
        "first_bad_event_normal_form_instantiation": "Open-literal",
        "first_bad_selected_residual_readout": "Exact type/readout identity",
        "selector_switch_selected_state_factorization": "Audited exact obstruction: false universally for distinct germs",
        "selector_switch_state_nonclosure": "Audited exact counterexample",
        "selector_second_moment_full_pair_jump": "Exact identity",
        "selector_reset_hidden_germ_blocks": "Exact block identity",
        "selector_switch_selected_second_moment_nonclosure": "Audited PSD counterexample",
        "selector_switch_admissible_subspace_factorization": "Exact conditional factorization identity",
        "physical_event_plus_selector_factorization": "Exact generic factorization criterion / audited obstruction",
        "persistent_library_selected_observer_architecture": "Rigorous consequence of exact selector/event typing",
        "first_bad_persistent_library_dynamics": "Audited-conditional for a specified finite same-replica physical packet library",
        "same_replica_residual_library_common_noise": "Exact identity",
        "same_replica_residual_library_qv_gram": "Exact identity",
        "same_replica_residual_library_qv_rank": "Rigorous Gram-rank consequence",
        "same_replica_selector_qv_readout": "Exact identity",
        "same_replica_event_qv_functor": "Exact identity",
        "same_replica_library_bias_spread": "Exact martingale consequence under stated scope",
        "independent_per_germ_noise_model_distinction": "Exact physical model distinction",
        "one_mode_same_replica_cross_qv_cancellation": "Audited calibration / rigorous cross-block necessity",
        "first_bad_candidate_library_instantiation": "Open-literal",
        "first_bad_library_clock_replica_identification": "Open-literal",
        "selected_residual_frozen_interval_martingale": "Exact identity",
        "selector_readout_finite_jump": "Exact pathwise identity",
        "selector_fv_zero_continuous_qv_vs_jump_qv": "Exact semimartingale clarification",
        "selector_jump_dyad_three_face": "Exact identity",
        "selected_hybrid_semimartingale_law": "Audited-conditional on supplied same-replica library and selector path",
        "selector_jump_qv_bank_no_go": "Audited closed-excursion calibration / rigorous no-bank consequence",
        "one_mode_selector_optional_qv_closed_excursion": "Audited exact-NS calibration",
        "selector_jump_qv_vs_reset_covariance": "Exact identity / rigorous typing consequence",
        "first_bad_selected_hybrid_path_instantiation": "Open-literal",
        "combined_selected_post_event_readout": "Exact identity",
        "combined_selected_jump_operator": "Exact identity",
        "combined_event_discrete_product_rule": "Exact identity",
        "combined_event_physical_selector_mixed_face": "Exact identity / rigorous interaction necessity",
        "combined_event_second_moment_full_pair_jump": "Exact identity",
        "combined_event_jump_square_typing": "Exact semimartingale typing consequence",
        "one_mode_combined_event_mixed_face": "Audited exact-NS payload calibration",
        "naive_additive_physical_selector_event_no_go": "Audited calibration / rigorous no-naive-additivity consequence",
        "selected_hybrid_with_simultaneous_linear_events": "Rigorous conditional composition of exact same-clock identities",
        "first_bad_simultaneous_event_instantiation": "Open-literal",
        "combined_selected_continuous_noise_readout": "Exact identity",
        "combined_selected_continuous_qv_rate": "Exact identity",
        "combined_continuous_qv_rate_full_pair_revaluation": "Exact identity",
        "signed_qv_rate_revaluation_typing": "Exact physical typing consequence",
        "continuous_qv_rate_vs_jump_qv_independence": "Rigorous consequence of exact state/noise typing",
        "one_mode_hidden_event_continuous_qv_cancellation": "Audited exact-NS calibration",
        "selector_only_qv_rate_hidden_event_no_go": "Audited calibration / rigorous hidden-event necessity",
        "selected_hybrid_source_jump_ledger": "Rigorous conditional composition of exact same-clock identities",
        "first_bad_hybrid_source_event_instantiation": "Open-literal",
        "adaptive_selected_event_mean_correlation": "Exact two-replica identity",
        "adaptive_selected_event_congruence_four_face": "Exact identity",
        "adaptive_event_map_dispersion_face": "Rigorous PSD consequence",
        "adaptive_event_state_correlation_faces": "Exact signed correlation identity",
        "mean_event_map_mean_payload_closure": "Audited PSD calibration: false universally",
        "adaptive_event_alignment_correlation_sign": "Audited PSD calibration",
        "adaptive_event_qv_gram_congruence": "Exact identity",
        "selected_adaptive_event_expectation_ledger": "Rigorous conditional composition of exact replica identities",
        "first_bad_adaptive_event_joint_law": "Open-literal",
        "first_bad_physical_score_passive_gauge": "Exact physical gauge identity",
        "raw_first_bad_score_passive_gauge_no_go": "Audited calibration / rigorous observer-artifact no-go",
        "first_bad_event_map_passive_gauge_equivariance": "Exact event gauge identity",
        "first_bad_physical_residual_vs_support_locality": "Audited exact-NS calibration / rigorous insufficiency",
        "first_bad_persistent_library_memory_necessity": "Rigorous consequence of exact selector-switch obstruction",
        "first_bad_full_coherence_event_memory_necessity": "Audited PSD calibration / rigorous coherence necessity",
        "first_bad_adaptive_joint_law_necessity": "Rigorous consequence of exact adaptive-event algebra",
        "first_bad_rule_physical_admissibility_ledger": "Rigorous synthesis of necessary physical constraints; not sufficient",
        "first_bad_badness_resolve_functional_after_admissibility": "Open-literal",
        "local_enstrophy_balance_vorticity_contraction": "Exact identity",
        "kelvin_bulk_enstrophy_dissipation_identification": "Exact orientation-complete Kelvin identity",
        "local_enstrophy_critical_three_face_law": "Exact identity",
        "local_max_growth_gate_curvature_necessity": "Rigorous consequence",
        "abc_beltrami_critical_stretching_zero": "Exact Beltrami identity / rigorous scope correction",
        "affine_vortex_positive_local_growth_gate": "Audited exact-NS mechanism calibration",
        "affine_vortex_growth_gate_target_scope": "Exact theorem-domain correction",
        "first_bad_local_growth_to_continuation_bridge": "Open-literal",
        "moving_enstrophy_critical_constraint_speed": "Exact conditional critical-constraint identity",
        "moving_enstrophy_critical_pde_relative_speed": "Exact conditional Navier--Stokes identity",
        "moving_enstrophy_critical_three_gradient_faces": "Exact conditional physical split",
        "moving_enstrophy_critical_value_speed_independence": "Exact identity",
        "abc_fixed_enstrophy_maximum_vs_fluid_transport": "Audited exact periodic-NS calibration",
        "affine_degenerate_critical_speed_nonuniqueness": "Audited exact-NS degeneracy calibration",
        "critical_hessian_inversion_theorem_domain": "Exact theorem-domain correction",
        "first_bad_enstrophy_critical_path_identification": "Open-literal",
        "critical_hessian_evolution_three_face": "Exact conditional identity",
        "critical_hessian_connection_strain_rotation_split": "Exact identity / physical typing",
        "incompressible_critical_hessian_connection_logdet_cancellation": "Exact incompressible cancellation",
        "critical_hessian_strain_rotation_logdet_split": "Exact identity / theorem-type correction",
        "critical_hessian_incompressible_curvature_volume_law": "Rigorous consequence conditional on nondegeneracy",
        "critical_hessian_jacobi_logdet_law": "Exact conditional identity",
        "critical_branch_finite_lograte_nondegeneracy": "Rigorous conditional consequence",
        "abc_critical_hessian_logdet_calibration": "Audited exact periodic-NS calibration",
        "critical_hessian_logdet_degeneracy_domain": "Exact theorem-domain correction",
        "first_bad_critical_branch_degeneracy_identification": "Open-literal",
        "critical_branch_value_gap_rate": "Exact identity",
        "critical_branch_three_face_competition": "Exact conditional Navier--Stokes identity",
        "critical_value_crossing_vs_hessian_degeneracy": "Audited generic geometry separation",
        "three_mode_shear_critical_sheet_crossing": "Audited exact periodic-NS calibration",
        "three_mode_shear_pure_curvature_competition": "Audited exact-NS calibration",
        "critical_value_crossing_no_positive_growth": "Audited exact-NS calibration / rigorous no-growth-switch consequence",
        "selected_max_tie_continuity_derivative_switch": "Exact envelope consequence / audited NS calibration",
        "critical_event_taxonomy_ranking_degeneracy_packet": "Rigorous structural consequence",
        "first_bad_branch_competition_hysteresis_identification": "Open-literal",
        "reverse_codeforming_future_bank_identification": "Open-literal",
        "first_bad_full_shape_local_descent": "Open-literal",
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
    "finite_shape_kelvin_descent": {
        "corrected_local_readout": "epsilon_K=K_{Z(R)}-omega(X).h_R; actual reverse-current area h_R is not the Cauchy metric-dual H_C",
        "actual_reverse_area_connection": "+(grad u)^T",
        "cauchy_metric_dual_connection": "-(grad u)^T",
        "opposite_connection_residual_zero": bool(area_connection_opposite),
        "connections_not_identical_generically": bool(area_connection_not_identical),
        "exact_error_sde": "d epsilon_K=-omega.R_A dsigma+sqrt(2nu) sum_mu q_mu^err dW_mu",
        "pathwise_D_error_cross_qv_zero": bool(cubic_D_error_cross_qv_zero),
        "horizon_cross_source": "2nu sum_mu vec(partial_mu Dbar) partial_mu epsilon_bar",
        "joint_leading_gramian_residual_zero": bool(joint_error_gram_zero),
        "short_hierarchy": "Var(epsilon)=O(h), Cov(vec D,epsilon)=O(h^2), Sigma_D=O(h^3)",
        "centered_spatial_hierarchy": "epsilon and R_A start on oriented quadrupole O(r^4); q_mu^err uses one higher vorticity derivative; error qv rate O(r^8) at fixed smooth state",
        "cubic_heat_shear": {
            "bias": str(cubic_bias),
            "bias_equals_minus_4ab3": bool(cubic_bias_exact),
            "anchor_independent": bool(cubic_bias_anchor_independent),
            "time_independent": bool(cubic_bias_time_independent),
            "error_qv_zero": bool(cubic_error_qv_zero),
            "verdict": "nonzero deterministic finite-shape bias can be conserved while drift/qv/variance/D-error covariance vanish; covariance alone cannot prove descent",
        },
        "one_mode_shear": {
            "error_variance_leading_residual_zero": bool(eps_var_leading_zero),
            "D_error_cross_horizon_residual_zero": bool(eps_cross_horizon_zero),
            "D_error_cross_leading_residual_zero": bool(eps_cross_leading_zero),
            "typing": "same-anchor stochastic error spread and D/error finite-horizon covariance are active; pathwise [D,error] remains zero",
        },
        "abc": {
            "initial_bias": str(abc_bias),
            "shape_drift": str(abc_error_drift),
            "shape_drift_formula_residual_zero": bool(abc_shape_drift_zero_residual),
            "typing": "genuine 3D NS activates finite-variation strain-gradient shape drift -omega.R_A",
        },
        "finite_moment_hierarchy": "odd heat shears + Legendre P_2m expose every next deterministic even-moment flux mode while centered instantaneous qv coefficient can vanish",
        "first_bad_verdict": "Open-literal: must control deterministic bias, R_A, q_mu^err, support locality, and metric-whitened covariance remainder together",
    },
    "surface_moment_hierarchy": {
        "exact_law": "Mdot_alpha=-sum_i alpha_i int r^(alpha-e_i) Delta u_i n dA+int r^alpha A(X+r)^T n dA",
        "affine_order_preserving": bool(affine_first_zero),
        "nonlinear_p3_m2_degree_is_4": bool(moment_degree_rule_ok and moment_degree_value_ok),
        "order_rule": "degree-p velocity jet couples moment order m to m+p-1; p=1 affine is the exact order-preserving exception",
        "quadratic_heat_shear_centering_breaks": bool(quad_centering_breaks),
        "quadratic_centering_rate": str(quad_M1_rate),
        "single_anchor_recentering_generic_obstruction": bool(recentering_generic_obstruction),
        "recentering_law": "F' = F-c h^T",
        "tangential_xy_shear_y_moment_tower_zero_rate": bool(shear_tower_zero),
        "cubic_bias_from_Myy_residual_zero": bool(cubic_moment_bias_ok),
        "cubic_centered_error_noise_zero": bool(cubic_moment_noise_zero),
        "typing": "low oriented moments are observables of the full material surface; nonlinear NS calls omitted higher moments dynamically, while special shear geometry can conserve hidden moments exactly",
        "first_bad_verdict": "Open-literal: no uniform theorem controls the full normalized oriented moment tower on the migrating selected support",
    },
    "codeforming_surface_moment_tower": {
        "raw_isotropic_weight": "M_alpha -> lambda^(|alpha|+2) M_alpha",
        "scalar_refinement_shape_residual_zero": bool(scalar_refinement_zero),
        "scale_shape_full_pullback_residual_zero": bool(scale_shape_pullback_zero),
        "coherent_refinement_pullback_residual_zero": bool(coherent_refinement_zero),
        "nonaffinity_field": "N_L=L^-1[u(X+Lxi)-u(X)-A(X)Lxi]",
        "quadratic_heat_shear_nonaffinity": str(Nquad),
        "quadratic_nonaffinity_ratio_r_inverse": bool(quad_nonaffinity_ratio_zero),
        "nonaffinity_divergence_zero": bool(quad_nonaffinity_div_zero),
        "area_source_equals_DN_transpose": bool(quad_area_is_DN_transpose),
        "kelvin_one_form": "beta_L=(L^T L)N_L",
        "quadratic_kelvin_one_form": str(beta_quad),
        "quadratic_kelvin_one_form_r5": bool(beta_quad_r5_zero),
        "quadratic_pulled_vorticity_defect": str(pulled_omega_quad),
        "kelvin_curl_piola_residual_zero": bool(kelvin_curl_piola_zero),
        "kelvin_identity": "epsilon_K=oint beta_L.dxi; curl_xi beta_L=cof(L)^T[omega(X+Lxi)-omega(X)]",
        "one_mode_beta_recovers_error": bool(one_mode_beta_error_zero),
        "one_mode_anchor_beta_derivative_recovers_noise": bool(one_mode_beta_noise_zero),
        "codeforming_drift_contraction_residual_zero": bool(codeforming_drift_identity),
        "codeforming_error_sde": "d epsilon=-eta0.htilde_dot dsigma+sqrt(2nu) sum_mu (oint partial_Xmu beta_L.dxi)dW_mu",
        "three_faces": "shape velocity -N_L; area rate (D N_L)^T; Kelvin one-form (L^T L)N_L",
        "homogeneous_scale_shape_residual_zero": bool(homogeneous_scale_shape_zero),
        "homogeneous_law": "N_{rho S}^{(p)}=rho^(p-1) S^-1 U_p(Sxi)",
        "linear_strain_ns_residual_zero": bool(linear_ns_zero),
        "critical_long_thin": {
            "line_frame": str(Lcritical),
            "scalar_normalized_xy_area": str(critical_scalar_area),
            "scalar_area_is_r_inverse": bool(critical_scalar_area_zero),
            "codeforming_xy_area": str(critical_codeforming_area),
            "codeforming_area_is_reference": bool(critical_codeforming_area_zero),
            "physical_support_nonlocal": bool(critical_support_nonlocal),
            "verdict": "codeforming constancy does not imply physical support locality",
        },
        "supercritical_refinement": {
            "line_frame": str(Lsuper),
            "scalar_normalized_xy_area": str(super_scalar_area),
            "scalar_factor_is_exp_st": bool(super_scalar_factor_zero),
            "codeforming_xy_area": str(super_codeforming_area),
            "codeforming_area_is_reference": bool(super_codeforming_area_zero),
            "verdict": "support locality for k>s does not require bounded scalar-normalized area moments",
        },
        "anisotropic_quadratic_no_go": "L=diag(r^3,r,r) shrinks all physical lines but N_L=r^-1 xi_y^2 e_x",
        "first_bad_verdict": "Open-literal: instantaneous Kelvin descent requires beta_L/curl control, while dynamic current-shape descent separately requires N_L/DN_L plus actual support and selector/boundary/exit/reset faces",
    },
    "metric_whitened_kelvin_remainder": {
        "pointwise_density": "g_H=H^T delta_zeta",
        "pointwise_whitening_residual_zero": bool(pointwise_white_zero),
        "pointwise_reconstruction_residual_zero": bool(pointwise_reconstruction_zero),
        "finite_reconstruction": "r_H=H^-T epsilon_H",
        "finite_reconstruction_typing": "physical vector reconstructed from three different finite face residuals; not generally a pointwise field value",
        "energy_reconstruction_residual_zero": bool(white_energy_zero),
        "covariance_trace_reconstruction_residual_zero": bool(white_cov_trace_zero),
        "passive_orientation_reparameterization_residual_zero": bool(passive_white_zero),
        "qv_reconstruction_residual_zero": bool(white_qv_zero),
        "covariance_cross_decomposition_residual_zero": bool(white_cross_decomposition_zero),
        "covariance_cross_blocks_nonzero": bool(white_cross_mandatory),
        "dropping_cross_blocks_is_false": bool(white_drop_cross_false),
        "homogeneous_beta_scale_shape_residual_zero": bool(beta_scale_shape_zero),
        "homogeneous_beta_law": "beta_{rho S}^{(p)}=rho^(p+1) S^T U_p(Sxi)",
        "scale_ladder": "N_L: rho^(p-1); beta/raw Stokes: rho^(p+1); H^-T whitened defect: rho^(p-1)",
        "cubic_unit_cube_center_defect_zero": bool(cubic_center_defect_zero),
        "cubic_unit_cube_face_residual": str(eps_cubic_unit),
        "cubic_unit_cube_reconstructed_residual": str(cubic_unit_reconstruction),
        "cubic_unit_cube_reconstruction_expected": bool(cubic_unit_reconstruction_zero),
        "cubic_isotropic_raw_face_r4": bool(cubic_raw_r4_zero),
        "cubic_isotropic_whitened_r2": bool(cubic_white_r2_zero),
        "fixed_state_bridge": "for same-time NS, H^-T curl_xi beta_L=delta omega; for future random payoff the same whitening algebra applies only after its literal full state/clock is specified",
        "first_bad_verdict": "Open: must prove actual first-bad support locality and reconstructed residual collapse while retaining covariance cross blocks and selector/boundary/exit/reset faces; future-clock/ancestry identification remains Open-literal",
    },
    "dynamic_reconstructed_kelvin_residual": {
        "actual_area_error": "epsilon_area=K-omega.h_R; drift=-omega.R_A",
        "local_frame_error": "epsilon_lin=K-H^T omega; zero finite-variation drift",
        "geometry_mismatch_transfer": "epsilon_lin=epsilon_area+omega.(h_R-h_local)",
        "inverse_transpose_connection_residual_zero": bool(invT_connection_zero),
        "local_flux_drift_residual_zero": bool(local_flux_drift_zero),
        "shape_drift_transfer_residual_zero": bool(shape_transfer_zero),
        "geometry_mismatch_drift_is_plus_omega_RA": bool(geometry_transfer_is_plus_shape),
        "noise_transfer_residual_zero": bool(noise_transfer_zero),
        "reconstructed_sde": "dr=-A r dsigma+sqrt(2nu) Qhat dW; Qhat=H^-T(A_K-H^T grad omega)",
        "full_qv_block_decomposition_residual_zero": bool(full_qv_blocks_zero),
        "full_dyad_block_decomposition_residual_zero": bool(full_dyad_blocks_zero),
        "dyad_energy_trace_residual_zero": bool(dyad_energy_trace_zero),
        "generic_local_residual_cross_qv_nonzero": bool(generic_dynamic_cross_nonzero),
        "energy_law": "d|r|^2/2 drift=-r.S.r+nu||Qhat||_F^2",
        "cubic": {
            "residual": str(r_cubic_dyn),
            "drift_zero": bool(cubic_dynamic_drift_zero),
            "qv_zero": True,
            "energy_drift_zero": bool(cubic_dynamic_energy_zero),
            "verdict": "nonzero reconstructed residual can be exactly conserved while qv is zero",
        },
        "one_mode": {
            "cross_qv_zz": str(one_mode_dynamic_cross_expected),
            "cross_qv_formula_residual_zero": bool(one_mode_dynamic_cross_zero),
            "cross_qv_generically_nonzero": bool(one_mode_dynamic_cross_nonzero),
            "residual_variance_qv_onset_residual_zero": bool(one_mode_dynamic_qv_onset_zero),
            "typing": "residual e_z martingale has zero line-connection drift but nonzero shared-anchor cross qv with local vorticity",
        },
        "reduced_covariance": "Open-literal: pathwise dyad law does not factor full-state correlations into an autonomous reduced centered covariance PDE",
        "future_clock": "Open-literal: same-clock reverse-age dynamic residual is not identified with future-remaining or ancestry resolution bank",
    },
    "reverse_codeforming_kelvin_martingale": {
        "variables": "eta=L^-1 omega; chi=L^-1 r=epsilon/J; kappa=K/J=eta+chi; J=det L",
        "volume_freeze_residual_zero": bool(volume_freeze_zero),
        "orientation_error_codeforming_residual_triangle_zero": bool(residual_triangle_zero),
        "normalized_circulation_split_residual_zero": bool(normalized_split_zero),
        "local_codeforming_affine_drift_residual_zero": bool(local_codeforming_drift_zero),
        "noise_decomposition_residual_zero": bool(noise_split_zero),
        "joint_gram_block_residual_zero": bool(joint_gram_blocks_zero),
        "full_circulation_qv_split_residual_zero": bool(full_qv_split_zero),
        "physical_metric_work_residual_zero": bool(metric_work_zero),
        "mean_bias_rate_zero": bool(mean_bias_rate_zero),
        "centered_covariance_source_residual_zero": bool(covariance_source_zero),
        "reverse_age_backward_operator_clock_sign_residual_zero": bool(clock_sign_zero),
        "martingale_core": "d eta=sqrt(2nu)Gtilde dW; d chi=sqrt(2nu)Qtilde dW; d kappa=sqrt(2nu)(Gtilde+Qtilde)dW",
        "cubic": {
            "chi": str(chi_cubic_cof),
            "bias_nonzero": bool(cubic_codeforming_bias_nonzero),
            "qv_zero": bool(cubic_codeforming_qv_zero),
            "energy_drift_zero": bool(cubic_codeforming_energy_zero),
            "verdict": "nonzero co-deforming mean bias can persist with exactly zero stochastic spread",
        },
        "one_mode_full_period": {
            "actual_circulation_zero": bool(full_period_K_zero),
            "chi_equals_minus_eta": True,
            "noise_responses_opposite": bool(full_period_noise_opposite),
            "positive_diagonal_qv_equal": bool(full_period_diag_equal),
            "cross_qv_is_negative_diagonal": bool(full_period_cross_negative_equal),
            "local_qv_nonzero": bool(full_period_local_qv_nonzero),
            "cross_qv_nonzero": bool(full_period_cross_qv_nonzero),
            "full_qv_cancellation_residual_zero": bool(full_period_qv_cancellation_zero),
            "typing": "full-period finite face is a nonlocal mechanism calibration, not a local first-bad packet",
        },
        "bias_spread_typing": "E chi is constant; covariance grows by expected qv, so bias and stochastic spread are distinct",
        "physical_pushforward": "r=L chi restores signed strain as frame/metric work",
        "future_clock": "Open-literal: reverse-age co-deforming martingale covariance is not identified with the future conditional covariance bank",
        "first_bad": "Open: must force both mean-bias and spread collapse with actual support/conditioning and moving physical faces",
    },
    "weighted_codeforming_kelvin_residual": {
        "physical_topology": "r=L chi; |r|^2=chi^T L^T L chi",
        "fixed_frame_bias_spread_residual_zero": bool(weighted_fixed_frame_split_zero),
        "weighted_qv_trace_residual_zero": bool(weighted_qv_trace_zero),
        "quadratic": {
            "ns_residual_zero": bool(quad_weighted_ns_zero),
            "epsilon": str(eps_quad_w),
            "chi": str(chi_quad_w),
            "r": str(r_quad_w),
            "raw_bias_nonzero": bool(quad_raw_bias_nonzero),
            "raw_bias_exact_minus_one": bool(quad_raw_bias_constant),
            "physical_residual_limit_zero": bool(quad_physical_residual_limit_zero),
            "weighted_bias_exact_rho2": bool(quad_weighted_bias_r2),
        },
        "one_mode": {
            "chi_jet_limit_residual_zero": bool(chi_one_limit_residual_zero),
            "noise_jet_limit_residual_zero": bool(qchi_one_limit_residual_zero),
            "physical_bias_limit_zero": bool(one_physical_bias_limit_zero),
            "physical_noise_limit_zero": bool(one_physical_noise_limit_zero),
            "typing": "raw codeforming bias/noise can stay O(1) while physical L-weighted residual/noise vanish",
        },
        "random_frame": {
            "exact_energy": str(random_frame_energy),
            "mean_metric_times_mean_Q": str(random_frame_factorized),
            "mixed_face": str(random_frame_mixed),
            "decomposition_residual_zero": bool(random_frame_decomposition_zero),
            "factorization_without_mixed_face_false": bool(random_frame_factorization_false),
            "mixed_face_positive_example": bool(random_frame_mixed_signed_positive),
            "mixed_face_negative_example": bool(random_frame_mixed_signed_negative),
        },
        "homogeneous_exponent_p2_to_p7_residual_zero": bool(homogeneous_weighted_exponents_zero),
        "first_bad": "Open: control E[chi^T L^T L chi] on the actual migrating packet with random-frame correlation plus selector/refinement/boundary/exit/reset faces; support locality remains separate",
        "future_clock": "Open-literal: same-clock weighted physical residual is not the future conditional covariance bank",
    },
    "directional_refinement_kelvin_residual": {
        "directional_decomposition_residual_zero": bool(directional_decomposition_zero),
        "right_refinement_metric_residual_zero": bool(right_refinement_metric_zero),
        "midpoint_event_residual_zero": bool(midpoint_event_zero),
        "midpoint_geometry_face": str(mid_geometry_evt),
        "midpoint_state_face": str(mid_state_evt),
        "passive_gl_total_residual_zero": bool(passive_gl_total_zero),
        "passive_gl_geometry_face_nonzero": bool(passive_gl_geometry_nonzero),
        "passive_gl_state_face_nonzero": bool(passive_gl_state_nonzero),
        "passive_gl_faces_cancel": bool(passive_gl_faces_cancel),
        "random_frame_three_face_residual_zero": bool(ensemble_three_face_zero),
        "random_frame_face_values_expected": bool(ensemble_face_values_expected),
        "random_frame_geometry_face": str(ensemble_geometry),
        "random_frame_state_face": str(ensemble_state),
        "random_frame_correlation_face": str(ensemble_corr),
        "smooth_scale_shape_content_residual_zero": bool(smooth_scale_shape_content_zero),
        "reverse_material_strain_qv_residual_zero": bool(reverse_material_weighted_zero),
        "homogeneous_refinement_p2_to_p7_residual_zero": bool(homogeneous_refinement_p2_p7_zero),
        "quadratic_long_support": {
            "epsilon_expected": bool(quad_long_epsilon_expected),
            "chi_expected": bool(quad_long_chi_expected),
            "physical_residual_expected": bool(quad_long_residual_expected),
            "physical_energy_rho2": bool(quad_long_energy_expected),
            "physical_energy_limit_zero": bool(quad_long_energy_limit_zero),
            "support_not_local": bool(quad_long_support_not_local),
            "line_frame": str(quad_long["line_frame"]),
            "typing": "weighted physical Kelvin residual collapses while one support line remains exactly length one",
        },
        "event_typing": "conditioned event has geometry plus current/state faces; full random-frame event adds metric-residual correlation; Delta Q remains supplied by the full pair/current event map",
        "first_bad": "Open: control each directional sigma_i^2 v_i^T Q_chi v_i together with support locality, random-frame correlation, selector/refinement/boundary/exit/reset faces",
    },
    "principal_kelvin_residual_channels": {
        "projector_channel_decomposition_residual_zero": bool(projector_channel_zero),
        "two_replica_pathwise_channel_residual_zero": bool(two_replica_channel_zero),
        "simple_spectrum_connection_skew_residual_zero": bool(connection_skew_zero),
        "metric_rate_reconstruction_residual_zero": bool(metric_rate_reconstruction_zero),
        "principal_channel_rate_sum_residual_zero": bool(channel_rate_sum_zero),
        "principal_mixing_offdiagonal_residual_zero": bool(mixing_offdiag_zero),
        "linear_shear": {
            "metric_rate_expected": bool(linear_shear_B_expected),
            "connection_12_expected": bool(linear_shear_connection_expected),
            "mixing_total_expected": bool(linear_shear_mixing_expected),
            "mixing_channels_active": bool(linear_shear_mixing_active),
            "typing": "exact steady NS shear routes off-diagonal metric work through moving principal-axis residual channels",
        },
        "degeneracy": {
            "internal_basis_gauge_residual_zero": bool(degenerate_basis_gauge_zero),
            "block_energy_expected": bool(degenerate_block_energy_expected),
            "simple_spectrum_api_rejects_degeneracy": bool(degeneracy_rejected),
            "typing": "individual axes inside a repeated-eigenvalue block are gauge; the spectral projector block is canonical",
        },
        "random_frame_typing": "pathwise spectral products retain geometry-residual correlation without mean-metric factorization",
        "first_bad": "Open: weighted channel collapse is an exact reformulation of residual descent but does not prove support locality or close physical event/cross-clock faces",
    },
    "selected_residual_hybrid_semimartingale": {
        "frozen_selector_continuous_qv_factorization_residual_zero": bool(hybrid_continuous_qv_zero),
        "selector_jump_square_expected": bool(hybrid_jump_square_expected),
        "selector_jump_dyad_residual_zero": bool(hybrid_jump_dyad_zero),
        "hybrid_optional_qv_sum_expected": bool(hybrid_total_qv_expected),
        "closed_selector_excursion": {
            "state_change_zero": bool(closed_hybrid_state_zero),
            "jump_sum_zero": bool(closed_hybrid_jump_sum_zero),
            "jump_optional_qv_nonzero": bool(closed_hybrid_jump_qv_nonzero),
        },
        "one_mode_ns": {
            "opposite_endpoint_residuals": bool(one_mode_hybrid_opposite),
            "closed_excursion_state_zero": bool(one_mode_hybrid_state_zero),
            "jumps_opposite": bool(one_mode_hybrid_jump_opposite),
            "jump_optional_qv_nonzero": bool(one_mode_hybrid_jump_qv_nonzero),
            "jump_optional_qv_trace": str(one_mode_hybrid["jump_optional_qv_trace"]),
            "typing": "exact one-mode NS closed selector excursion accumulates positive cadlag jump qv while returning to the identical selected residual",
        },
        "typing": "continuous Brownian bracket and finite selector jump squares are distinct path-variation faces; jump square is not a continuous stochastic covariance producer",
        "first_bad": "Open-literal at NS-generated selector timing and any simultaneous physical packet event; hybrid algebra is exact once path data are supplied",
    },
    "selected_residual_combined_event": {
        "interaction_product_rule_residual_zero": bool(combined_interaction_zero),
        "sequential_product_rules_residual_zero": bool(combined_sequential_zero),
        "mixed_physical_selector_face_nonzero": bool(combined_mixed_nonzero),
        "naive_old_reference_faces_miss_exactly_mixed_face": bool(combined_naive_missing_mixed),
        "second_moment_full_pair_jump_residual_zero": bool(combined_second_moment_zero),
        "jump_square_equals_quadratic_pair_face": bool(combined_jump_square_zero),
        "event_law": "D=E_+ A-E_-=E_- DeltaA+DeltaE+DeltaE DeltaA",
        "one_mode_ns": {
            "opposite_pre_event_residuals": bool(one_mode_combined_opposite),
            "old_selector_physical_face_zero": bool(one_mode_combined_physical_old_zero),
            "mixed_face_nonzero": bool(one_mode_combined_mixed_nonzero),
            "post_selected_residual_zero": bool(one_mode_combined_post_zero),
            "naive_selector_only_jump_false": bool(one_mode_combined_naive_false),
            "mixed_face_closes_exact_jump": bool(one_mode_combined_mixed_closes),
            "selector_old_jump": str(one_mode_combined["selector_old_jump"]),
            "mixed_jump": str(one_mode_combined["mixed_jump"]),
            "total_jump": str(one_mode_combined["total_jump"]),
            "typing": "exact one-mode NS residual payload under specified hidden-germ current synthesis activates the finite physical-selector interaction",
        },
        "typing": "physical library event and selector readout are distinct; simultaneous event uses the discrete product rule and full pair jump",
        "first_bad": "Open-literal only at NS-generated badness/resolve timing and actual event-map/state instantiation",
    },
    "selected_residual_combined_qv_rate": {
        "continuous_qv_rate_revaluation_residual_zero": bool(combined_rate_revaluation_zero),
        "pre_post_selected_noise_response_shapes_expected": bool(combined_endpoint_rate_shapes),
        "rate_revaluation_faces_nontrivial": bool(combined_rate_faces_nontrivial),
        "source_rate_can_change_with_zero_state_jump_square": bool(source_nonzero_jump_zero),
        "state_jump_square_can_be_nonzero_with_zero_source_rate_change": bool(source_zero_jump_nonzero),
        "one_mode_ns": {
            "opposite_same_replica_noise_coefficients": bool(one_mode_rate_opposite),
            "selector_only_qv_rate_unchanged": bool(one_mode_rate_selector_only_same),
            "actual_post_event_qv_rate_zero": bool(one_mode_rate_post_zero),
            "actual_rate_revaluation_is_minus_pre_rate": bool(one_mode_rate_actual_negative_pre),
            "full_pair_rate_revaluation_residual_zero": bool(one_mode_rate_pair_faces_close),
            "q0": str(one_mode_rate["q0"]),
            "q1": str(one_mode_rate["q1"]),
            "pre_qv_rate": str(one_mode_rate["pre_qv_rate"]),
            "actual_rate_revaluation": str(one_mode_rate["actual_rate_revaluation"]),
            "typing": "selector-only source rate misses a hidden physical synthesis that cancels the actual post-event same-replica Brownian response",
        },
        "typing": "jump optional qv and adjacent-interval continuous Brownian source-rate revaluation are distinct exact tensors",
        "first_bad": "Open-literal at actual library/badness/timing/event/clock instantiation",
    },
    "random_selected_event_correlation": {
        "mean_output_correlation_residual_zero": bool(random_mean_residual_zero),
        "mean_output_correlation_face_nonzero": bool(random_mean_corr_nonzero),
        "second_order_four_face_residual_zero": bool(random_congruence_zero),
        "event_map_dispersion_nonzero": bool(random_disp_nonzero),
        "event_state_correlation_faces_nonzero": bool(random_corr_nonzero),
        "event_dispersion_probe_nonnegative": bool(random_disp_probe_nonnegative),
        "all_alignment_payloads_psd": bool(random_payloads_psd),
        "aligned_faces_expected_1_1_1_1_to_4": bool(random_alignment_positive_expected),
        "anti_aligned_faces_expected_1_1_minus1_minus1_to_0": bool(random_alignment_negative_expected),
        "qv_gram_congruence_residual_zero": bool(random_qv_congruence_zero),
        "aligned": {
            "exact": str(random_alignment["positive_exact"]),
            "naive": str(random_alignment["positive_naive"]),
            "dispersion": str(random_alignment["positive_dispersion"]),
            "corr_left": str(random_alignment["positive_corr_left"]),
            "corr_right": str(random_alignment["positive_corr_right"]),
        },
        "anti_aligned": {
            "exact": str(random_alignment["negative_exact"]),
            "naive": str(random_alignment["negative_naive"]),
            "dispersion": str(random_alignment["negative_dispersion"]),
            "corr_left": str(random_alignment["negative_corr_left"]),
            "corr_right": str(random_alignment["negative_corr_right"]),
        },
        "typing": "adaptive event-map dispersion and signed event-state correlation are mandatory expectation-level faces",
        "first_bad": "Open-literal at actual badness/resolve rule, adaptive event-map distribution, joint law, and outer clock",
    },
    "first_bad_rule_admissibility": {
        "physical_score_passive_gauge_residual_zero": bool(admiss_physical_gauge_zero),
        "raw_score_passive_gauge_change_nonzero": bool(admiss_raw_gauge_nonzero),
        "raw_ranking_flips_under_passive_basis": bool(admiss_raw_ranking_flips),
        "physical_ranking_unchanged_under_passive_basis": bool(admiss_physical_ranking_fixed),
        "raw_event_block_changes_under_passive_bases": bool(admiss_event_raw_changes),
        "physical_event_map_gauge_residual_zero": bool(admiss_event_physical_fixed),
        "physical_residual_collapse_with_nonlocal_support": bool(admiss_residual_collapse_support_nonlocal),
        "persistent_library_switch_obstruction_all_true": bool(admiss_library_all),
        "full_coherence_event_obstruction_expected": bool(admiss_coherence_needed),
        "adaptive_joint_law_obstruction_expected": bool(admiss_adaptive_needed),
        "all_necessary_admissibility_flags_true": bool(admiss_necessary_flags),
        "no_sufficient_functional_or_regularity_claim": bool(admiss_no_sufficiency),
        "ranking_calibration": {
            "raw_before": [str(x) for x in admiss_ranking["raw_before"]],
            "raw_after": [str(x) for x in admiss_ranking["raw_after"]],
            "physical_before": [str(x) for x in admiss_ranking["physical_before"]],
            "physical_after": [str(x) for x in admiss_ranking["physical_after"]],
            "raw_winner_before": int(admiss_ranking["raw_winner_before"]),
            "raw_winner_after": int(admiss_ranking["raw_winner_after"]),
            "physical_winner_before": int(admiss_ranking["physical_winner_before"]),
            "physical_winner_after": int(admiss_ranking["physical_winner_after"]),
        },
        "support_no_go": {
            "physical_energy": str(admiss_support["physical_energy"]),
            "physical_energy_limit_zero": bool(admiss_support["physical_energy_limit"] == 0),
            "long_support_line_squared": str(admiss_support["long_x_line_squared"]),
            "support_line_limit_one": bool(admiss_support["support_line_limit"] == 1),
        },
        "coherence_parent_channel_difference": str(admiss_coherence["parent_channel_difference"]),
        "adaptive_aligned_exact_vs_naive": [str(admiss_adaptive["aligned_exact"]),str(admiss_adaptive["aligned_naive"])],
        "adaptive_anti_aligned_exact_vs_naive": [str(admiss_adaptive["anti_aligned_exact"]),str(admiss_adaptive["anti_aligned_naive"])],
        "typing": "necessary physical admissibility only: gauge, support, persistent-library memory, full coherence, and adaptive joint-law constraints",
        "first_bad": "Open-literal: no sufficient Navier-Stokes badness/resolve functional is defined",
    },
    "local_enstrophy_kelvin_growth_gate": {
        "enstrophy_balance_equals_vorticity_residual_contraction": bool(local_balance_contraction_zero),
        "orientation_complete_kelvin_bulk_residual_zero": bool(local_kelvin_bulk_zero),
        "critical_point_three_face_residual_zero": bool(local_critical_curvature_zero),
        "growth_gate_margin_expected": bool(local_margin_expected),
        "abc": {
            "beltrami_residual_zero": bool(abc_lg_beltrami_zero),
            "stretching_equals_enstrophy_transport_globally": bool(abc_lg_transport_zero),
            "ns_residual_zero": bool(abc_lg_ns_zero),
            "symmetric_critical_gradient_zero": bool(abc_lg_critical_zero),
            "symmetric_critical_stretching_zero": bool(abc_lg_critical_stretch_zero),
            "typing": "global Beltrami identity forces zero stretching at every enstrophy critical point; ABC cannot referee a positive local-max gate",
        },
        "affine_vortex": {
            "ns_residual_zero": bool(aff_lg_ns_zero),
            "spatially_uniform_enstrophy": bool(aff_lg_uniform),
            "kelvin_bulk_zero": bool(aff_lg_kelvin_zero),
            "stretching_and_time_growth_expected": bool(aff_lg_growth_expected),
            "enstrophy_balance_residual_zero": bool(aff_lg_balance_zero),
            "nonperiodic_x_shift_defect": bool(aff_lg_nonperiodic),
            "exact_growth": str(aff_lg_expected_growth),
            "typing": "positive local growth gate is compatible with exact smooth affine NS, but the calibration is outside periodic/finite-energy target class",
        },
        "local_max_law": "at grad e=0: e_t=stretching-Kelvin_bulk+nu Delta e; at a max Delta e<=0, positive margin is necessary but not sufficient for growth",
        "first_bad": "Open-literal: no bridge from this local growth law plus packet/support/event structure to continuation failure",
    },
    "moving_enstrophy_critical_point": {
        "critical_path_value_speed_independence": bool(value_speed_independent),
        "abc": {
            "critical_gradient_zero": bool(abc_mc_grad_zero),
            "hessian_invertible": bool(abc_mc_hessian_invertible),
            "hessian_negative_definite_sylvester": bool(abc_mc_negative_sylvester),
            "fluid_velocity_nonzero": bool(abc_mc_fluid_nonzero),
            "critical_velocity_fixed_zero": bool(abc_mc_fixed),
            "constraint_and_pde_speed_residuals_zero": bool(abc_mc_constraint_zero),
            "relative_speed_equals_minus_fluid": bool(abc_mc_relative_minus_u),
            "hessian_det": str(abc_mc["hessian_det"]),
            "fluid_velocity": str(abc_mc["fluid_velocity"]),
            "typing": "exact periodic ABC strict enstrophy maximum is fixed in Eulerian space while nonzero fluid moves through it",
        },
        "affine_degeneracy": {
            "gradient_hessian_growth_gradient_zero": bool(aff_mc_degenerate),
            "two_distinct_speed_residuals_zero": bool(aff_mc_speed_nonunique),
            "typing": "uniform enstrophy has singular Hessian and no unique inverse-Hessian critical speed",
        },
        "speed_law": "H_e(xdot_*-u)+grad[stretching-Kelvin_bulk+nu Delta e]=0 on a differentiable critical branch; invert H_e only when nondegenerate",
        "first_bad": "Open-literal: the programme first-bad observable is not identified with a nondegenerate enstrophy critical branch",
    },
    "enstrophy_critical_hessian_evolution": {
        "generic_three_face_evolution_residual_zero": bool(hessian_evolution_zero),
        "connection_strain_rotation_split_residual_zero": bool(connection_split_zero),
        "incompressible_connection_tensor_nonzero": bool(connection_nonzero),
        "incompressible_connection_logdet_rate_zero": bool(connection_logdet_zero),
        "connection_logdet_minus_two_divergence_residual_zero": bool(connection_divergence_zero),
        "incompressible_strain_and_rotation_logdet_rates_zero": bool(strain_rotation_rates_expected),
        "jacobi_determinant_residual_zero": bool(jacobi_he_zero),
        "generic_logdet_rate_expected": bool(logdet_he_expected),
        "logdet_face_rates_sum_residual_zero": bool(face_rates_sum_zero),
        "finite_integrated_lograte_example_keeps_nonzero_determinant": bool(finite_lograte_nonzero),
        "abc": {
            "hessian_dot_equals_minus_2nu_hessian": bool(abc_he_hdot_expected),
            "determinant_nonzero_at_finite_time": bool(abc_he_det_nonzero),
            "logdet_rate_minus_6nu": bool(abc_he_logdet_expected),
            "jacobi_residual_zero": bool(abc_he_jacobi_zero),
            "divergence_zero": bool(abc_he_div_zero),
            "connection_logdet_face_zero": bool(abc_he_connection_zero),
            "determinant": str(abc_he["determinant"]),
            "typing": "exact periodic ABC critical Hessian decays isotropically in amplitude while local incompressible connection contributes zero curvature-volume rate",
        },
        "curvature_volume_law": "for incompressible flow on a nondegenerate critical branch, d log|det H|/dt retains only growth-Hessian and relative-critical-transport faces",
        "conditional_nondegeneracy": "finite limiting integrated lograte preserves nonzero det H on an already smooth nondegenerate branch; this is not Navier-Stokes continuation",
        "first_bad": "Open-literal: no identification of critical-Hessian degeneracy/branch loss with the programme first-bad event or continuation failure",
    },
    "enstrophy_critical_branch_competition": {
        "generic_geometry_crossing_at_equal_value": bool(geom_bc_cross_zero),
        "generic_geometry_crossing_transverse": bool(geom_bc_transverse),
        "generic_geometry_hessians_nondegenerate": bool(geom_bc_nondegenerate),
        "three_mode_shear": {
            "ns_residual_zero": bool(shear_bc_ns_zero),
            "two_persistent_critical_sheets": bool(shear_bc_critical),
            "crossing_value_expected": bool(shear_bc_tie),
            "transverse_curvatures_expected": bool(shear_bc_curvatures),
            "gap_rate_48nu_e_minus2": bool(shear_bc_gap_rate),
            "pure_curvature_competition": bool(shear_bc_pure_curvature),
            "branch_rates_expected": bool(shear_bc_rates_expected),
            "both_branch_values_decrease": bool(shear_bc_both_decrease),
            "selected_scalar_jump_zero_at_tie": bool(shear_bc_selector_value_continuous),
            "selected_envelope_derivative_switch_expected": bool(shear_bc_envelope_switch),
            "value": str(shear_bc["value_0"]),
            "curvature_y0": str(shear_bc["hessian_yy_0"]),
            "curvature_ypi": str(shear_bc["hessian_yy_pi"]),
            "rate_y0": str(shear_bc["time_rate_0"]),
            "rate_ypi": str(shear_bc["time_rate_pi"]),
            "typing": "exact periodic NS critical-sheet ranking switch driven purely by different curvature decay rates; both values decrease and no sheet is created/destroyed",
        },
        "event_typing": "value crossing, critical-geometry degeneracy/birth/death, and physical packet events are distinct mechanisms",
        "first_bad": "Open-literal: no mapping from programme badness/resolve hysteresis to enstrophy critical-value competition is defined",
    },
    "same_replica_residual_library_dynamics": {
        "cross_germ_qv_block_residual_zero": bool(library_cross_block_zero),
        "cross_germ_qv_block_expected": bool(library_cross_block_expected),
        "selector_qv_readout_residual_zero": bool(library_selector_readout_zero),
        "linear_event_qv_functor_residual_zero": bool(library_event_qv_zero),
        "independent_noise_model_differs": bool(library_independent_diff_nonzero),
        "independent_common_difference_has_zero_diagonal_blocks": bool(library_independent_diag_zero),
        "stacked_martingale_mean_rate_zero": bool(library_mean_rate_zero),
        "instantaneous_qv_rank": int(library_rank),
        "common_driver_dimension": int(library_driver),
        "rank_bounded_by_driver": bool(library_rank_bounded),
        "one_mode_ns": {
            "opposite_noise_coefficients": bool(one_mode_library_noise_opposite),
            "cross_qv_is_negative_diagonal": bool(one_mode_library_cross_negative),
            "synthesized_common_qv_zero": bool(one_mode_library_common_cancel),
            "synthesized_independent_qv_nonzero": bool(one_mode_library_independent_positive),
            "event_qv_functor_residual_zero": bool(one_mode_library_event_functor_zero),
            "q1": str(one_mode_library["q1"]),
            "q2": str(one_mode_library["q2"]),
            "typing": "exact one-mode NS same-replica packet noises require signed cross-germ qv; independent-per-germ noise gives the wrong synthesized source",
        },
        "library_law": "dChi=sqrt(2nu) Qstack dW; Gamma=2nu Qstack Qstack^T with one common three-dimensional W",
        "first_bad": "Open-literal at actual candidate-library and clock/replica instantiation; same-replica structural dynamics is exact once the physical library is specified",
    },
    "first_bad_selected_residual_readout": {
        "distinct_selector_universal_factorization_nonzero": bool(selector_factorization_nonzero),
        "unavoidable_new_germ_identity_block": bool(selector_unavoidable_identity),
        "state_counterexample": {
            "old_selected_equal": bool(selector_state_old_same),
            "new_selected_different": bool(selector_state_new_diff),
        },
        "second_moment_pair_jump_residual_zero": bool(selector_pair_jump_zero),
        "two_germ_reset_block_faces_expected": bool(selector_faces_expected),
        "second_moment_psd_counterexample": {
            "both_full_moments_psd": bool(selector_psd_full),
            "old_selected_blocks_equal": bool(selector_psd_old_same),
            "new_selected_blocks_different": bool(selector_psd_new_diff),
        },
        "admissible_subspace_factorization_residual_zero": bool(selector_admissible_factor_zero),
        "identity_event_plus_genuine_switch_not_factorable": bool(selector_identity_event_factor_nonzero),
        "same_germ_block_event_factorization_residual_zero": bool(selector_same_germ_event_factor_zero),
        "typing": "selector is an active readout on a persistent germ/fiber library, not a universal physical transition between selected endpoints",
        "first_bad": "Open-literal at NS-generated persistent library dynamics and programme-specific admissible inter-germ relations",
    },
    "kelvin_event_normal_form": {
        "physical_raw_bijection_residual_zero": bool(normal_physical_zero),
        "codeforming_raw_bijection_residual_zero": bool(normal_codeforming_zero),
        "frame_aware_event_composition_residual_zero": bool(normal_frame_comp_zero),
        "codeforming_event_composition_residual_zero": bool(normal_code_comp_zero),
        "second_moment_event_composition_residual_zero": bool(normal_second_moment_zero),
        "pair_functor_event_composition_residual_zero": bool(normal_pair_functor_zero),
        "intermediate_projector_telescope_residual_zero": bool(normal_projector_telescope_zero),
        "intermediate_degenerate_basis_telescope_residual_zero": bool(normal_degenerate_telescope_zero),
        "symmetric_second_moment_probe_reconstruction_residual_zero": bool(normal_probe_reconstruction_zero),
        "observational_completeness_typing": "unrestricted linear event-probe class reconstructs symmetric Q by polarization; no actual first-bad probe reachability/minimality claim",
        "channel_only_no_go": {
            "input_diagonal_channels_identical": bool(channel_nf_same_inputs),
            "cross_coherence_opposite": bool(channel_nf_coherence_opposite),
            "both_second_moments_psd": bool(channel_nf_psd),
            "parent_channel_difference_exact_2": bool(channel_nf_parent_diff),
            "input_channels": [str(x) for x in channel_nf["input_channels_plus"]],
            "parent_plus": str(channel_nf["parent_channel_plus"]),
            "parent_minus": str(channel_nf["parent_channel_minus"]),
            "typing": "diagonal spectral channel list loses cross-channel coherence and is not a compositional event state",
        },
        "normal_form": "raw packet gauge orbit <-> physical A; sequential A maps compose; pair functor and complete intermediate projector resolutions are functorial",
        "first_bad": "Open-literal at NS-generated event choice/map/state; normal-form algebra itself is exact",
    },
    "spectral_kelvin_event_transfer": {
        "parent_projector_family_algebra_residual_zero": bool(projector_family_zero),
        "all_parent_channel_transfer_residuals_zero": bool(event_transfer_all_zero),
        "full_parent_metric_energy_spectral_residual_zero": bool(event_full_energy_zero),
        "frame_conversion_cross_channel_term_nonzero": bool(event_cross_channel_nonzero),
        "frame_conversion_cross_channel_transfer_residual_zero": bool(event_cross_channel_residual_zero),
        "degenerate_parent_projector_family_residual_zero": bool(degenerate_parent_projector_family_zero),
        "degenerate_parent_transfer_residual_zero": bool(degenerate_event_transfer_zero),
        "degenerate_child_internal_basis_transfer_residual_zero": bool(degenerate_child_basis_transfer_zero),
        "sector_partition_residual_zero": bool(sector_event_sum_zero),
        "one_mode_ns": {
            "parent_channel_zero": bool(one_mode_event_transfer_zero),
            "same_child_sector_nonzero_positive_symbolically": bool(one_mode_event_same_positive),
            "cross_child_cancels_same_child": bool(one_mode_event_cross_negative),
            "other_sectors_zero": bool(one_mode_event_other_sectors_zero),
            "same_child": str(one_mode_event_transfer["same_child_same_channel"]),
            "cross_child": str(one_mode_event_transfer["cross_child_same_channel"]),
            "typing": "exact half-period one-mode NS activates positive same-child and equal negative cross-child projector traffic",
        },
        "event_law": "T_{alpha;i beta,j gamma}=lambda_P tr(P_P A_i P_i_beta Q_ij P_j_gamma A_j^T)",
        "degeneracy_typing": "spectral projector blocks are canonical; no eigenvector gap connection or cross-event axis matching is needed",
        "first_bad": "Open-literal only at actual event-map/state instantiation; projector transfer itself is exact once A_i and Q_ij are supplied",
    },
    "frame_aware_kelvin_residual_refinement": {
        "compatible_raw_error_refinement_residual_zero": bool(compatible_raw_error_zero),
        "physical_reconstruction_refinement_residual_zero": bool(physical_refinement_zero),
        "independent_orientation_gauge_residual_zero": bool(physical_gauge_zero),
        "cofactor_physical_synthesis_residual_zero": bool(cofactor_synthesis_zero),
        "codeforming_determinant_ratio_residual_zero": bool(codeforming_det_zero),
        "direct_codeforming_parent_refinement_residual_zero": bool(codeforming_parent_zero),
        "frame_aware_pair_functor_residual_zero": bool(frame_pair_functor_zero),
        "frame_aware_pair_expansion_residual_zero": bool(frame_pair_expansion_zero),
        "frame_aware_spectral_pair_expansion_residual_zero": bool(frame_spectral_pair_zero),
        "isotropic_area_volume_scale_residual_zero": bool(frame_iso_scale_zero),
        "quadratic_ns": {
            "physical_prediction_residual_zero": bool(quad_frame_physical_zero),
            "codeforming_prediction_residual_zero": bool(quad_frame_codeforming_zero),
            "physical_formula_expected": bool(quad_frame_r_expected),
            "codeforming_formula_expected": bool(quad_frame_chi_expected),
            "naive_unchanged_scalar_weights_false": bool(quad_frame_naive_false),
            "typing": "exact quadratic heat-shear current synthesis uses area-frame weights physically and determinant/volume weights codeformingly",
        },
        "scalar_packet_lift": {
            "blocks_equal_w_i_I3": bool(scalar_packet_blocks_expected),
            "pair_blocks_equal_w_i_w_j_I9": bool(scalar_packet_pair_zero),
            "interval_chain_orientation_lift_residual_zero": bool(orientation_chain_lift_zero),
            "typing": "the existing scalar current/chain refinement class canonically tensors with the independent orientation fiber",
        },
        "structural_lift": "A_i=H_P^-T R_i H_i^T=(J_i/J_P)L_P R_i L_i^-1; B_i=(J_i/J_P)R_i",
        "first_bad": "Open-literal only at actual event-map instantiation: scalar orientation-preserving refinement is already lifted, while genuine orientation mixing/reselection requires its physical R_i",
    },
    "selected_principal_kelvin_lineage": {
        "selector_spectral_commutator_zero": bool(selector_spectral_zero),
        "selector_pair_spectral_commutator_zero": bool(selector_pair_spectral_zero),
        "generic_germ_mixing_commutator_nonzero": bool(generic_germ_mixing_nonzero),
        "selected_endpoint_spectral_decomposition_residual_zero": bool(selected_endpoint_spectral_zero),
        "synthesis_pair_functor_residual_zero": bool(synthesis_pair_zero),
        "spectral_pair_expansion_residual_zero": bool(spectral_pair_expansion_zero),
        "selector_reset_residual_zero": bool(selector_reset_zero),
        "selector_reset_four_face_residual_zero": bool(reset_four_face_zero),
        "one_mode": {
            "opposite_half_period_residual_zero": bool(one_mode_lineage_opposite_zero),
            "full_parent_channel_zero": bool(one_mode_lineage_parent_zero),
            "diagonal_parent_channel_nonzero": bool(one_mode_lineage_diag_nonzero),
            "cross_child_cancels_diagonal": bool(one_mode_lineage_cross_cancels),
            "selector_reset_total_zero": bool(one_mode_lineage_reset_zero),
            "selector_reset_signed_face_identity": bool(one_mode_lineage_reset_signed),
            "typing": "exact one-mode NS half-period finite residuals force cross-child spectral cancellation and signed reset revaluation",
        },
        "closed_selector_excursion": {
            "telescope_residual_zero": bool(closed_excursion_zero),
            "signed_faces_cancel": bool(closed_excursion_faces_cancel),
            "quadratic_path_face_positive": bool(closed_excursion_quad_positive),
            "linear_pair_sum_negative": bool(closed_excursion_signed_negative),
            "typing": "positive quadratic selector path length is cancelled by signed pair faces and is not a physical bank",
        },
        "cross_event_axis_gauge": {
            "rank_one_channel_values_change": bool(cross_event_axis_values_change),
            "projector_block_total_invariant": bool(cross_event_block_total_invariant),
            "typing": "endpoint spectral blocks are canonical; individual axes are not canonically matched through a degenerate event without physical transport",
        },
        "hybrid_same_clock": "frozen selector: stretch+content+mixing; finite event: geometry+left+right+quadratic pair reset; degeneracy: projector blocks",
        "first_bad": "Open-literal: actual current-to-residual refinement lift, badness/resolve predicates, moving cut time faces, support locality, and cross-clock ancestry remain missing",
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
    "full_current_shape_state": {
        "state": "(r,X,R(.),D) on reverse age; only X carries Brownian q.v.",
        "anchor_only_diffusion_block": bool(full_state_anchor_only),
        "exact_shear_ns_kelvin_gauge_residual_zero": bool(kelvin_gauge_zero),
        "translation_cartan_x_residual_zero": bool(cartan_x_zero),
        "translation_cartan_y_residual_zero": bool(cartan_y_zero),
        "typing": "relative shape and D are finite variation; moving Kelvin drift is Bernoulli/pressure gauge; anchor translation gives the Kelvin martingale coefficient",
    },
    "deformation_kelvin_joint_covariance": {
        "mixed_law": "H C_DK=B_D C_DK+2nu sum_mu vec(partial_mu Dbar) partial_mu Kbar",
        "exact_shear_cross_horizon_residual_zero": bool(cross_horizon_zero),
        "exact_shear_cross_leading_residual_zero": bool(cross_leading_zero),
        "exact_shear_joint_connected_covariance_residual_zero": bool(joint_connected_zero),
        "general_leading_gramian_residual_zero": bool(joint_gram_zero),
        "generic_cross_block_has_h2_factor": bool(generic_cross_has_h2),
        "short_hierarchy": "V_K=O(h), C_DK=O(h^2), Sigma_D=O(h^3); leading coefficients 2nu, nu, 2nu/3 arise from one Gram integral",
        "exact_shear_cross_covariance": str(scalar_cross),
        "typing": "C_DK is the deformation-circulation off-diagonal block of one same-ancestor joint covariance; not S^int, not resolution covariance, not a new branching source",
    },
    "ledger_placement": {
        "same_clock_face": "Sigma_D is the existing connected vector covariance theorem specialized to reverse-age Cauchy deformation; C_D^Gram is its row-Gram projection",
        "future_remaining_horizon": "not identified: causal past h=t-s is distinct from future remaining tau=Theta-t",
        "resolution_covariance": "given a lift, reduction adds Cov_R(Dbar_vec) to averaged intrinsic Sigma_D; it does not retype intrinsic deformation covariance as resolution",
        "selected_current_projection": "for a shared frozen selector, Sigma_D transports inside the closed-current spatial fiber; replica-dependent selectors add separate selector and cross pair sectors",
        "finite_current_state": "local D/current projection and full current-shape source law are exact; the literal epsilon_K descent-error SDE is also exact, but uniform first-bad shape collapse remains Open-literal",
        "finite_shape_descent_error": "epsilon_K has a deterministic bias/shape-drift face plus anchor-qv spread; exact cubic NS proves zero covariance does not imply zero descent bias",
        "deformation_kelvin_cross": "C_DK is an exact same-clock off-diagonal joint covariance block; it is distinct from Sigma_D, Kelvin variance, S^int, and resolution covariance",
        "S_int": "no identification with S^int, Z_irr, or irreducible content",
    },
}

out = Path("audit-results/stochastic_cauchy_deformation_report.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(json.dumps(report, indent=2, sort_keys=True))
