"""Exact packet-locality and Nanson geometry for Kelvin restart germs.

This module separates three notions that must not be conflated:

1. small oriented area vectors;
2. small spatial support diameter;
3. small metric-whitened covariance/payoff remainder.

For incompressible material deformation an isotropic reference packet has
H_r = r^2 F^{-T}.  Hence H_r -> 0 does not by itself force the transported
packet diameter to zero when F becomes anisotropic.
"""
from __future__ import annotations

import sympy as sp

Matrix = sp.MatrixBase


def general_nanson_area_frame_rhs(grad_u: Matrix, area_frame: Matrix) -> sp.Matrix:
    """General 3D Nanson evolution Hdot=((div u)I-(grad u)^T)H."""
    if grad_u.shape != (3, 3) or area_frame.shape != (3, 3):
        raise ValueError("general Nanson area-frame law is 3D")
    div_u = sp.trace(grad_u)
    return sp.simplify((div_u * sp.eye(3) - grad_u.T) * area_frame)


def metric_from_area_frame(area_frame: Matrix) -> sp.Matrix:
    if area_frame.shape != (3, 3):
        raise ValueError("area frame must be 3x3")
    return sp.simplify((area_frame.T * area_frame).inv())


def metric_logdet_rate(area_frame: Matrix, area_frame_dot: Matrix) -> sp.Expr:
    """Exact d/dt log det((H^T H)^-1) for any invertible H."""
    M = metric_from_area_frame(area_frame)
    J = sp.simplify(area_frame.T * area_frame)
    Jdot = sp.simplify(area_frame_dot.T * area_frame + area_frame.T * area_frame_dot)
    Mdot = sp.simplify(-M * Jdot * M)
    return sp.simplify(sp.trace(M.inv() * Mdot))


def general_nanson_metric_logdet_rate(grad_u: Matrix, area_frame: Matrix) -> sp.Expr:
    """General 3D Nanson value; equals -4 div u."""
    return sp.simplify(
        metric_logdet_rate(area_frame, general_nanson_area_frame_rhs(grad_u, area_frame))
    )


def incompressible_isotropic_area_frame(deformation_gradient: Matrix, radius: sp.Expr) -> sp.Matrix:
    """H_r=r^2 F^{-T} for an isotropic reference packet when det F=1."""
    if deformation_gradient.shape != (3, 3):
        raise ValueError("deformation gradient must be 3x3")
    return sp.simplify(radius**2 * deformation_gradient.inv().T)


def diagonal_locality_ratio(area_frame: Matrix, sigma_min: sp.Expr) -> sp.Expr:
    """sqrt(det H)/sigma_min(H), valid as a line-scale diagnostic for isotropic material packets."""
    return sp.simplify(sp.sqrt(sp.det(area_frame)) / sigma_min)


def long_thin_face_flux(radius: sp.Expr) -> sp.Expr:
    """Flux coefficient for W=X cos(x1)e2 through [-1/2,1/2] x [-r^2/2,r^2/2]."""
    return sp.simplify(2 * radius**2 * sp.sin(sp.Rational(1, 2)))


def long_thin_center_flux(radius: sp.Expr) -> sp.Expr:
    """Local-center flux coefficient area*W(0).n for the same face."""
    return sp.simplify(radius**2)


def long_thin_covariance_defect(radius: sp.Expr) -> sp.Expr:
    """Variance defect for centered scalar amplitude X with E[X^2]=1."""
    actual = long_thin_face_flux(radius)
    local = long_thin_center_flux(radius)
    return sp.simplify(actual**2 - local**2)


def long_thin_whitened_payoff_error(radius: sp.Expr) -> sp.Matrix:
    """H^{-T} epsilon for H=diag(r^3,r^2,r); it stays O(1), not o(1)."""
    H = sp.diag(radius**3, radius**2, radius)
    eps = sp.Matrix([
        0,
        sp.simplify(long_thin_face_flux(radius) - long_thin_center_flux(radius)),
        0,
    ])
    return sp.simplify(H.inv().T * eps)


def metric_whitened_covariance_remainder(remainder: Matrix, area_frame: Matrix) -> sp.Expr:
    """Invariant scalar remainder tr(R(H^T H)^-1)."""
    if remainder.shape != (3, 3) or area_frame.shape != (3, 3):
        raise ValueError("remainder and area frame must be 3x3")
    return sp.simplify(sp.trace(remainder * metric_from_area_frame(area_frame)))


def raw_frobenius_square(matrix: Matrix) -> sp.Expr:
    return sp.simplify(sum(matrix[i, j] ** 2 for i in range(matrix.rows) for j in range(matrix.cols)))


def whitened_l2_error_bound_factor(
    area_l2: sp.Expr,
    sigma_min: sp.Expr,
    l2_modulus: sp.Expr,
) -> sp.Expr:
    """Sufficient bound factor ||H^-T epsilon||_L2 <= A_l2/sigma_min * omega_2(delta)."""
    return sp.simplify(area_l2 * l2_modulus / sigma_min)


def cofactor_area_frame(line_frame: Matrix) -> sp.Matrix:
    """Cofactor/dual area frame H=det(L)L^{-T}."""
    if line_frame.shape != (3, 3):
        raise ValueError("line frame must be 3x3")
    return sp.simplify(sp.det(line_frame) * line_frame.inv().T)


def line_frame_from_area_frame(area_frame: Matrix) -> sp.Matrix:
    """Positive-orientation inverse cofactor: L=sqrt(det H) H^{-T}."""
    if area_frame.shape != (3, 3):
        raise ValueError("area frame must be 3x3")
    return sp.simplify(sp.sqrt(sp.det(area_frame)) * area_frame.inv().T)


def line_gram_from_area_frame(area_frame: Matrix) -> sp.Matrix:
    """Primal material-line Gram L^T L = det(H)(H^T H)^-1."""
    return sp.simplify(sp.det(area_frame) * metric_from_area_frame(area_frame))


def material_line_frame_rhs(grad_u: Matrix, line_frame: Matrix) -> sp.Matrix:
    """Material line kinematics Ldot=(grad u)L."""
    if grad_u.shape != (3, 3) or line_frame.shape != (3, 3):
        raise ValueError("material line-frame law is 3D")
    return sp.simplify(grad_u * line_frame)


def material_line_gram_rhs(grad_u: Matrix, line_frame: Matrix) -> sp.Matrix:
    """Gdot=L^T(A^T+A)L=2 L^T S L."""
    A = grad_u
    return sp.simplify(line_frame.T * (A.T + A) * line_frame)


def coherent_linear_scale(line_frame: Matrix) -> sp.Expr:
    """rho=(det L)^(1/3), the physical volume-equivalent linear scale."""
    if line_frame.shape != (3, 3):
        raise ValueError("line frame must be 3x3")
    return sp.real_root(sp.det(line_frame), 3)


def normalized_line_shape(line_frame: Matrix, rho: sp.Expr) -> sp.Matrix:
    """Unit-determinant line frame L/rho; caller supplies positive rho^3=det L."""
    return sp.simplify(line_frame / rho)


def anisotropy_tensor_from_lines(line_frame: Matrix, rho: sp.Expr) -> sp.Matrix:
    """A=(L/rho)^T(L/rho), det A=1 for rho^3=det L."""
    Lhat = normalized_line_shape(line_frame, rho)
    return sp.simplify(Lhat.T * Lhat)


def scale_shape_line_gram_residual(line_frame: Matrix, rho: sp.Expr) -> sp.Matrix:
    """Residual G_line-rho^2 A."""
    A = anisotropy_tensor_from_lines(line_frame, rho)
    return sp.simplify(line_frame.T * line_frame - rho**2 * A)


def scale_shape_packet_metric_residual(line_frame: Matrix, rho: sp.Expr) -> sp.Matrix:
    """Residual M_H-rho^-4 A for H=cof L and rho^3=det L."""
    H = cofactor_area_frame(line_frame)
    M = metric_from_area_frame(H)
    A = anisotropy_tensor_from_lines(line_frame, rho)
    return sp.simplify(M - rho**(-4) * A)


def incompressible_scale_rate(grad_u: Matrix, line_frame: Matrix) -> sp.Expr:
    """d log rho/dt=(1/3)div u for material Ldot=A L."""
    Ldot = material_line_frame_rhs(grad_u, line_frame)
    return sp.simplify(sp.trace(line_frame.inv() * Ldot) / 3)


def anisotropy_tensor_material_rhs(
    grad_u: Matrix,
    line_frame: Matrix,
    rho: sp.Expr,
    rho_log_rate: sp.Expr,
) -> sp.Matrix:
    """Exact A-dot after separating L=rho Lhat."""
    A = anisotropy_tensor_from_lines(line_frame, rho)
    Gdot = material_line_gram_rhs(grad_u, line_frame)
    return sp.simplify(Gdot / rho**2 - 2 * rho_log_rate * A)


def refinement_scale_shape(
    line_frame: Matrix,
    refinement: Matrix,
    rho_old: sp.Expr,
    rho_new: sp.Expr,
) -> tuple[sp.Matrix, sp.Matrix]:
    """Physical linear refinement L+ = L- R split into new scale and unit-det shape."""
    Lplus = sp.simplify(line_frame * refinement)
    Aplus = anisotropy_tensor_from_lines(Lplus, rho_new)
    return Lplus, Aplus


def centered_quadratic_shape_residual(
    second_moment: Matrix,
    grad_u_hessians: list[list[Matrix]],
    normal: Matrix,
) -> Matrix:
    """Exact centered-face residual for a velocity-gradient field quadratic in offset.

    grad_u_hessians[k][l] is the 3x3 coefficient partial_{kl}(grad u).
    Centering kills the linear offset term, leaving -1/2 Q_kl A_kl^T n.
    """
    if second_moment.shape != (3, 3) or normal.shape != (3, 1):
        raise ValueError("second moment must be 3x3 and normal a 3-vector")
    out = sp.zeros(3, 1)
    for k in range(3):
        for l in range(3):
            Hkl = grad_u_hessians[k][l]
            if Hkl.shape != (3, 3):
                raise ValueError("velocity-gradient Hessian slices must be 3x3")
            out -= sp.Rational(1, 2) * second_moment[k, l] * Hkl.T * normal
    return sp.simplify(out)


def centered_quadratic_flux_error(
    second_moment: Matrix,
    field_hessians: list[list[Matrix]],
    normal: Matrix,
) -> sp.Expr:
    """Exact centered-face flux error 1/2 Q_kl (partial_kl zeta).n for quadratic zeta."""
    if second_moment.shape != (3, 3) or normal.shape != (3, 1):
        raise ValueError("second moment must be 3x3 and normal a 3-vector")
    out = sp.Integer(0)
    for k in range(3):
        for l in range(3):
            hkl = field_hessians[k][l]
            if hkl.shape != (3, 1):
                raise ValueError("field Hessian slices must be 3-vectors")
            out += sp.Rational(1, 2) * second_moment[k, l] * (hkl.T * normal)[0]
    return sp.simplify(out)


def centered_rectangle_second_moment_yz(half_y: sp.Expr, half_z: sp.Expr) -> sp.Matrix:
    """Q=int xi xi^T dA for centered yz rectangle [-b,b]x[-c,c]."""
    b, c = half_y, half_z
    return sp.diag(
        0,
        sp.Rational(4, 3) * b**3 * c,
        sp.Rational(4, 3) * b * c**3,
    )


def refinement_scale_factor(refinement: Matrix) -> sp.Expr:
    """Positive real cube-root of det R; physical rho+ / rho- for L+ = L- R."""
    if refinement.shape != (3, 3):
        raise ValueError("refinement must be 3x3")
    return sp.real_root(sp.det(refinement), 3)


def refinement_anisotropy_pullback(
    anisotropy: Matrix,
    refinement: Matrix,
    scale_factor: sp.Expr,
) -> sp.Matrix:
    """A+ = d^(-2/3) R^T A- R = scale_factor^-2 R^T A R."""
    if anisotropy.shape != (3, 3) or refinement.shape != (3, 3):
        raise ValueError("anisotropy/refinement must be 3x3")
    return sp.simplify(scale_factor**(-2) * refinement.T * anisotropy * refinement)


def incompressible_material_scale_residual(grad_u: Matrix, line_frame: Matrix) -> sp.Expr:
    """Residual of d log rho/dt-(1/3)div u; zero generally for Ldot=A L."""
    return sp.simplify(incompressible_scale_rate(grad_u, line_frame) - sp.trace(grad_u) / 3)


def two_sided_lineage_frame(
    material_deformation: Matrix,
    initial_line_frame: Matrix,
    refinement_product: Matrix,
) -> sp.Matrix:
    """Exact lineage frame F L0 R: material flow left, physical refinement right."""
    if material_deformation.shape != (3, 3) or initial_line_frame.shape != (3, 3) or refinement_product.shape != (3, 3):
        raise ValueError("all lineage factors must be 3x3")
    return sp.simplify(material_deformation * initial_line_frame * refinement_product)


def right_cauchy_green(material_deformation: Matrix) -> sp.Matrix:
    """Physical right Cauchy--Green deformation tensor F^T F."""
    return sp.simplify(material_deformation.T * material_deformation)


def isotropic_lineage_support_metric(
    material_deformation: Matrix,
    scale: sp.Expr,
) -> sp.Matrix:
    """For L0=I,R=scale I: G_line=scale^2 F^T F."""
    return sp.simplify(scale**2 * right_cauchy_green(material_deformation))


def isotropic_lineage_packet_metric(
    material_deformation: Matrix,
    scale: sp.Expr,
) -> sp.Matrix:
    """For L0=I,R=scale I: M_H=scale^-4 F^T F when det F=1."""
    return sp.simplify(scale**(-4) * right_cauchy_green(material_deformation))


def cauchy_green_material_rhs(grad_u: Matrix, deformation: Matrix) -> sp.Matrix:
    """Cdot=F^T(A^T+A)F for Fdot=A F."""
    return sp.simplify(deformation.T * (grad_u.T + grad_u) * deformation)


def centered_parallelogram_normalized_second_moment(
    half_edge_a: Matrix,
    half_edge_b: Matrix,
) -> Matrix:
    """Q/A=(aa^T+bb^T)/3 for xi=s a+t b, s,t in [-1,1]."""
    if half_edge_a.shape != (3, 1) or half_edge_b.shape != (3, 1):
        raise ValueError("parallelogram half-edges must be 3-vectors")
    return sp.simplify(
        (half_edge_a * half_edge_a.T + half_edge_b * half_edge_b.T) / 3
    )


def coherent_three_face_normalized_quadrupoles(line_frame: Matrix) -> list[Matrix]:
    """Normalized Q_i/A_i for the three faces dual to columns of a coherent line frame."""
    if line_frame.shape != (3, 3):
        raise ValueError("line frame must be 3x3")
    cols = [line_frame[:, i] for i in range(3)]
    return [
        centered_parallelogram_normalized_second_moment(cols[1], cols[2]),
        centered_parallelogram_normalized_second_moment(cols[2], cols[0]),
        centered_parallelogram_normalized_second_moment(cols[0], cols[1]),
    ]


def coherent_three_face_quadrupole_closure_residual(line_frame: Matrix) -> Matrix:
    """Residual sum_i Q_i/A_i - (2/3) L L^T."""
    faces = coherent_three_face_normalized_quadrupoles(line_frame)
    return sp.simplify(sum(faces, sp.zeros(3)) - sp.Rational(2, 3) * line_frame * line_frame.T)


def two_sided_stretch_action(grad_u: Matrix, tensor: Matrix) -> sp.Matrix:
    """A T + T A^T, the common material/vorticity stretch operator."""
    if grad_u.shape != (3, 3) or tensor.shape != (3, 3):
        raise ValueError("stretch action is 3x3")
    return sp.simplify(grad_u * tensor + tensor * grad_u.T)


def material_support_tensor_residual(grad_u: Matrix, line_frame: Matrix) -> sp.Matrix:
    """Residual d(LL^T)/dt-[A LL^T+LL^T A^T] under Ldot=A L."""
    Ldot = material_line_frame_rhs(grad_u, line_frame)
    B = sp.simplify(line_frame * line_frame.T)
    direct = sp.simplify(Ldot * line_frame.T + line_frame * Ldot.T)
    return sp.simplify(direct - two_sided_stretch_action(grad_u, B))


def codeforming_pullback_residual(
    grad_u: Matrix,
    deformation: Matrix,
    tensor: Matrix,
    nonstretch_source: Matrix,
) -> sp.Matrix:
    """Residual for d(F^-1 T F^-T)=F^-1 D F^-T if Fdot=A F, Tdot=AT+TA^T+D."""
    if any(M.shape != (3, 3) for M in (grad_u, deformation, tensor, nonstretch_source)):
        raise ValueError("all co-deforming pullback tensors must be 3x3")
    Finv = sp.simplify(deformation.inv())
    Finv_dot = sp.simplify(-Finv * grad_u)
    Tdot = sp.simplify(two_sided_stretch_action(grad_u, tensor) + nonstretch_source)
    direct = sp.simplify(
        Finv_dot * tensor * Finv.T
        + Finv * Tdot * Finv.T
        + Finv * tensor * Finv_dot.T
    )
    target = sp.simplify(Finv * nonstretch_source * Finv.T)
    return sp.simplify(direct - target)


def exact_linear_strain_ns_residual(
    strain_rate: sp.Expr,
    coords: tuple[sp.Symbol, sp.Symbol, sp.Symbol],
    nu: sp.Expr,
) -> tuple[sp.Matrix, sp.Expr]:
    """Residual and pressure for u=(s x,0,-s z), p=-s^2(x^2+z^2)/2."""
    x, y, z = coords
    s = strain_rate
    u = sp.Matrix([s * x, 0, -s * z])
    p = -sp.Rational(1, 2) * s**2 * (x**2 + z**2)
    grad_p = sp.Matrix([sp.diff(p, q) for q in coords])
    adv = sp.Matrix([
        sum(u[j] * sp.diff(u[i], coords[j]) for j in range(3))
        for i in range(3)
    ])
    lap = sp.Matrix([sum(sp.diff(u[i], q, 2) for q in coords) for i in range(3)])
    return sp.simplify(adv + grad_p - nu * lap), p


def exact_linear_strain_deformation(strain_rate: sp.Expr, time: sp.Expr) -> sp.Matrix:
    s, t = strain_rate, time
    return sp.diag(sp.exp(s * t), 1, sp.exp(-s * t))


def strained_refined_line_frame(
    strain_rate: sp.Expr,
    refinement_rate: sp.Expr,
    time: sp.Expr,
) -> sp.Matrix:
    """L=rho F with rho=exp(-kappa t)."""
    s, k, t = strain_rate, refinement_rate, time
    rho = sp.exp(-k * t)
    return sp.simplify(rho * exact_linear_strain_deformation(s, t))


def directional_material_log_length_rate(grad_u: Matrix, line: Matrix) -> sp.Expr:
    """d log|ell|/dt = n.S.n = ell^T S ell / ell^T ell."""
    if grad_u.shape != (3, 3) or line.shape != (3, 1):
        raise ValueError("directional material line rate is 3D")
    S = sp.simplify((grad_u + grad_u.T) / 2)
    return sp.simplify((line.T * S * line)[0] / (line.T * line)[0])


def affine_vortex_stretch_rate(a: sp.Expr, r0: sp.Expr, t: sp.Expr) -> sp.Expr:
    return sp.simplify(r0 * sp.exp(2 * a * t))


def affine_vortex_stretch_gradient(a: sp.Expr, r0: sp.Expr, t: sp.Expr) -> sp.Matrix:
    r = affine_vortex_stretch_rate(a, r0, t)
    return sp.Matrix([[-a, -r, 0], [r, -a, 0], [0, 0, 2 * a]])


def affine_vortex_stretch_pressure_hessian(a: sp.Expr, r0: sp.Expr, t: sp.Expr) -> sp.Matrix:
    """P=-(A_dot+A^2), symmetric for the exact affine vortex-stretch flow."""
    A = affine_vortex_stretch_gradient(a, r0, t)
    Adot = sp.diff(A, t)
    return sp.simplify(-(Adot + A * A))


def affine_vortex_stretch_ns_residual(
    a: sp.Expr,
    r0: sp.Expr,
    t: sp.Expr,
    coords: tuple[sp.Symbol, sp.Symbol, sp.Symbol],
    nu: sp.Expr,
) -> tuple[sp.Matrix, sp.Expr]:
    """Exact affine NS residual for u=A(t)x with quadratic pressure."""
    xvec = sp.Matrix(coords)
    A = affine_vortex_stretch_gradient(a, r0, t)
    u = sp.simplify(A * xvec)
    P = affine_vortex_stretch_pressure_hessian(a, r0, t)
    p = sp.simplify(sp.Rational(1, 2) * (xvec.T * P * xvec)[0])
    grad_p = sp.simplify(P * xvec)
    adv = sp.simplify(A * u)
    lap = sp.zeros(3, 1)
    return sp.simplify(sp.diff(u, t) + adv + grad_p - nu * lap), p


def affine_vortex_stretch_vorticity(a: sp.Expr, r0: sp.Expr, t: sp.Expr) -> sp.Matrix:
    r = affine_vortex_stretch_rate(a, r0, t)
    return sp.Matrix([0, 0, 2 * r])


def affine_vortex_stretch_support_tensor(a: sp.Expr, t: sp.Expr) -> sp.Matrix:
    """B_F=F F^T; xy rotation cancels, leaving pure stretch eigenvalues."""
    return sp.diag(sp.exp(-2 * a * t), sp.exp(-2 * a * t), sp.exp(4 * a * t))


def coherent_core_line_frame(rho: sp.Expr, deformation: Matrix) -> sp.Matrix:
    return sp.simplify(rho * deformation)


def coherent_core_area_frame(rho: sp.Expr, deformation: Matrix) -> sp.Matrix:
    """For det F=1, H=cof(rho F)=rho^2 F^-T."""
    return sp.simplify(rho**2 * deformation.inv().T)


def coherent_core_raw_flux_second_moment(rho: sp.Expr, codeforming_total: Matrix) -> sp.Matrix:
    return sp.simplify(rho**4 * codeforming_total)


def coherent_core_physical_second_moment(deformation: Matrix, codeforming_total: Matrix) -> sp.Matrix:
    return sp.simplify(deformation * codeforming_total * deformation.T)


def coherent_core_packet_metric(rho: sp.Expr, deformation: Matrix) -> sp.Matrix:
    return sp.simplify(rho**(-4) * deformation.T * deformation)


def coherent_core_bank_residual(
    rho: sp.Expr,
    deformation: Matrix,
    codeforming_total: Matrix,
) -> sp.Expr:
    """Residual 1/2 tr(Qraw M)-1/2 tr(F Q F^T)."""
    Qraw = coherent_core_raw_flux_second_moment(rho, codeforming_total)
    M = coherent_core_packet_metric(rho, deformation)
    T = coherent_core_physical_second_moment(deformation, codeforming_total)
    return sp.simplify(sp.trace(Qraw * M) / 2 - sp.trace(T) / 2)


def kelvin_diffusion_length(nu: sp.Expr, remaining_horizon: sp.Expr) -> sp.Expr:
    """One-coordinate Brownian standard-deviation scale sqrt(2 nu tau)."""
    return sp.sqrt(2 * nu * remaining_horizon)


def kelvin_diffusion_log_rate(remaining_horizon: sp.Expr) -> sp.Expr:
    """d/dt log sqrt(2nu(Theta-t))=-1/(2 tau)."""
    return sp.simplify(-sp.Rational(1, 2) / remaining_horizon)


def parabolic_kelvin_line_log_rate(
    directional_strain_rate: sp.Expr,
    remaining_horizon: sp.Expr,
) -> sp.Expr:
    return sp.simplify(directional_strain_rate + kelvin_diffusion_log_rate(remaining_horizon))


def time_dependent_linear_strain_ns_residual(
    strain_rate: sp.Expr,
    t: sp.Symbol,
    coords: tuple[sp.Symbol, sp.Symbol, sp.Symbol],
    nu: sp.Expr,
) -> tuple[sp.Matrix, sp.Expr]:
    """Exact NS for A(t)=diag(s(t),0,-s(t)), pressure Hessian -(A'+A^2)."""
    xvec = sp.Matrix(coords)
    A = sp.diag(strain_rate, 0, -strain_rate)
    u = sp.simplify(A * xvec)
    P = sp.simplify(-(sp.diff(A, t) + A * A))
    p = sp.simplify(sp.Rational(1, 2) * (xvec.T * P * xvec)[0])
    return sp.simplify(sp.diff(u, t) + A * u + P * xvec), p


def singular_strain_deformation_factor(
    coefficient: sp.Expr,
    terminal_time: sp.Expr,
    start_time: sp.Expr,
    t: sp.Expr,
) -> sp.Expr:
    """exp int_{t0}^t a/(Theta-s) ds = ((Theta-t0)/(Theta-t))^a."""
    return sp.simplify(((terminal_time - start_time) / (terminal_time - t)) ** coefficient)


def parabolic_strained_line_length(
    coefficient: sp.Expr,
    terminal_time: sp.Expr,
    start_time: sp.Expr,
    t: sp.Expr,
    nu: sp.Expr,
) -> sp.Expr:
    tau = terminal_time - t
    return sp.simplify(
        kelvin_diffusion_length(nu, tau)
        * singular_strain_deformation_factor(coefficient, terminal_time, start_time, t)
    )


def packet_shape_amplification_factor(
    face_areas: list[sp.Expr],
    sigma_min_area_frame: sp.Expr,
) -> sp.Expr:
    """Dimensionless geometry factor sqrt(sum A_j^2)/sigma_min(H)."""
    return sp.simplify(
        sp.sqrt(sum(A**2 for A in face_areas)) / sigma_min_area_frame
    )


def finite_shape_connection_bound_factor(
    face_areas: list[sp.Expr],
    sigma_min_area_frame: sp.Expr,
    grad_u_modulus: sp.Expr,
) -> sp.Expr:
    """Sufficient bound for ||E_shape H^-1||_F."""
    return sp.simplify(
        packet_shape_amplification_factor(face_areas, sigma_min_area_frame)
        * grad_u_modulus
    )


def finite_flux_whitened_bound_factor(
    face_areas: list[sp.Expr],
    sigma_min_area_frame: sp.Expr,
    flux_l2_modulus: sp.Expr,
) -> sp.Expr:
    """Sufficient bound for ||H^-T epsilon_flux||_{L2}."""
    return sp.simplify(
        packet_shape_amplification_factor(face_areas, sigma_min_area_frame)
        * flux_l2_modulus
    )


def coherent_planar_amplification_from_H_diagonal(
    h1: sp.Expr,
    h2: sp.Expr,
    h3: sp.Expr,
    sigma_min: sp.Expr,
) -> sp.Expr:
    """Orthogonal planar-face witness with A_j=|h_j|, positive diagonal inputs."""
    return sp.simplify(sp.sqrt(h1**2 + h2**2 + h3**2) / sigma_min)
