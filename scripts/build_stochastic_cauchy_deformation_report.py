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
