"""Exact reduced/full ancestry resolution-kernel identities.

If an ancestry state is coarser than the physical Kelvin current-shape state, the
correct lift is generally a Markov/conditional kernel R rather than a deterministic
state map.  The resulting hidden-state covariance is ordinary conditional variance,
not viscous quadratic variation.
"""
from __future__ import annotations

import sympy as sp

Matrix = sp.MatrixBase


def kernel_mean(kernel: Matrix, payoff: Matrix) -> sp.Matrix:
    """Conditional mean R F; rows of R are reduced-state conditional laws."""
    if kernel.cols != payoff.rows:
        raise ValueError("kernel physical-state dimension must match payoff rows")
    return sp.simplify(kernel * payoff)


def kernel_covariances(kernel: Matrix, payoff: Matrix) -> list[sp.Matrix]:
    """Full output covariance matrix under each row of a conditional kernel."""
    if kernel.cols != payoff.rows:
        raise ValueError("kernel physical-state dimension must match payoff rows")
    out: list[sp.Matrix] = []
    for a in range(kernel.rows):
        weights = [kernel[a, i] for i in range(kernel.cols)]
        mean = sp.Matrix([
            sp.simplify(sum(weights[i] * payoff[i, j] for i in range(kernel.cols)))
            for j in range(payoff.cols)
        ])
        second = sp.zeros(payoff.cols)
        for i in range(kernel.cols):
            fi = sp.Matrix([payoff[i, j] for j in range(payoff.cols)])
            second += weights[i] * fi * fi.T
        out.append(sp.simplify(second - mean * mean.T))
    return out


def scalar_resolution_variance(kernel: Matrix, payoff: Matrix) -> sp.Matrix:
    """Var_R(F)=R(F^2)-(RF)^2 for a scalar physical payoff."""
    if payoff.cols != 1:
        raise ValueError("scalar payoff must have one column")
    mean = kernel_mean(kernel, payoff)
    second = sp.simplify(kernel * payoff.applyfunc(lambda x: x**2))
    return sp.Matrix([
        sp.simplify(second[a] - mean[a] ** 2) for a in range(kernel.rows)
    ])


def scalar_pair_resolution_variance(kernel: Matrix, payoff: Matrix) -> sp.Matrix:
    """1/2 E_RxR[(F1-F2)^2], exactly equal to conditional variance."""
    if payoff.cols != 1 or kernel.cols != payoff.rows:
        raise ValueError("kernel/payoff dimensions do not match scalar pair identity")
    vals = []
    for a in range(kernel.rows):
        total = sp.Integer(0)
        for i in range(kernel.cols):
            for j in range(kernel.cols):
                total += (
                    sp.Rational(1, 2)
                    * kernel[a, i]
                    * kernel[a, j]
                    * (payoff[i, 0] - payoff[j, 0]) ** 2
                )
        vals.append(sp.simplify(total))
    return sp.Matrix(vals)


def total_variance_decomposition(
    kernel: Matrix,
    physical_means: Matrix,
    physical_future_variances: Matrix,
) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    """E_R[V_full] + Var_R(m_full) for scalar terminal payoffs."""
    if physical_means.cols != 1 or physical_future_variances.cols != 1:
        raise ValueError("this helper is scalar-output")
    averaged_full = sp.simplify(kernel * physical_future_variances)
    resolution = scalar_resolution_variance(kernel, physical_means)
    return averaged_full, resolution, sp.simplify(averaged_full + resolution)


def kernel_intertwining_residual(
    reduced_generator: Matrix,
    lift_kernel: Matrix,
    physical_generator: Matrix,
    lift_kernel_dot: Matrix | None = None,
) -> sp.Matrix:
    """Rdot + L_red R - R L_phys for backward-observable generators."""
    if lift_kernel_dot is None:
        lift_kernel_dot = sp.zeros(*lift_kernel.shape)
    return sp.simplify(
        lift_kernel_dot + reduced_generator * lift_kernel - lift_kernel * physical_generator
    )


def affine_shear_ns_residual(
    shear_rate: sp.Expr,
    coords: tuple[sp.Symbol, sp.Symbol, sp.Symbol],
    t: sp.Symbol,
    nu: sp.Expr,
) -> sp.Matrix:
    """NS residual for u=(a y,0,0), an exact steady affine shear."""
    x, y, z = coords
    u = sp.Matrix([shear_rate * y, 0, 0])
    adv = sp.Matrix([
        sum(u[j] * sp.diff(u[i], coords[j]) for j in range(3))
        for i in range(3)
    ])
    lap = sp.Matrix([
        sum(sp.diff(u[i], q, 2) for q in coords) for i in range(3)
    ])
    return sp.simplify(sp.diff(u, t) + adv - nu * lap)


def affine_shear_relative_shape(
    shear_rate: sp.Expr,
    initial_shape: Matrix,
    elapsed: sp.Expr,
) -> sp.Matrix:
    """Exact relative-shape solution R=(rx+a t ry, ry, rz)."""
    if initial_shape.shape != (3, 1):
        raise ValueError("shape must be a 3-vector")
    rx, ry, rz = initial_shape
    return sp.Matrix([sp.simplify(rx + shear_rate * elapsed * ry), ry, rz])


def affine_shear_joint_state_covariance(anchor_covariance: Matrix) -> sp.Matrix:
    """Joint covariance of (anchor,shape) when initial shape is fixed in affine shear."""
    if anchor_covariance.shape != (3, 3):
        raise ValueError("anchor covariance must be 3x3")
    return sp.diag(anchor_covariance, sp.zeros(3))


def generator_carre_du_champ_scalar(generator: Matrix, values: Matrix) -> Matrix:
    """Finite-state Gamma_L(f)=L(f^2)-2 f (L f), componentwise."""
    if values.cols != 1 or generator.rows != generator.cols or generator.cols != values.rows:
        raise ValueError("generator/value dimensions do not match")
    Lv = sp.simplify(generator * values)
    v2 = values.applyfunc(lambda x: x**2)
    return sp.Matrix([
        sp.simplify((generator * v2)[i] - 2 * values[i] * Lv[i])
        for i in range(values.rows)
    ])


def generator_carre_du_champ_matrix(generator: Matrix, values: Matrix) -> list[Matrix]:
    """Finite-state vector Gamma matrices at each state."""
    if generator.rows != generator.cols or generator.cols != values.rows:
        raise ValueError("generator/value dimensions do not match")
    out: list[Matrix] = []
    Lv = sp.simplify(generator * values)
    for i in range(values.rows):
        G = sp.zeros(values.cols)
        for j in range(generator.cols):
            diff = sp.Matrix([values[j, a] - values[i, a] for a in range(values.cols)])
            G += generator[i, j] * diff * diff.T
        out.append(sp.simplify(G))
    return out


def kernel_average_statewise_matrices(kernel: Matrix, matrices: list[Matrix]) -> list[Matrix]:
    """Average a full-state matrix field through each row of a reduction kernel."""
    if kernel.cols != len(matrices):
        raise ValueError("kernel full-state dimension must match matrix field")
    if not matrices:
        return []
    n = matrices[0].rows
    out: list[Matrix] = []
    for a in range(kernel.rows):
        M = sp.zeros(n)
        for i in range(kernel.cols):
            M += kernel[a, i] * matrices[i]
        out.append(sp.simplify(M))
    return out


def resolution_horizon_source_scalar(
    reduced_generator: Matrix,
    kernel: Matrix,
    full_generator: Matrix,
    full_mean: Matrix,
) -> Matrix:
    """Gamma_red(Rm)-R Gamma_full(m) for a horizon-compatible static lift."""
    reduced_mean = kernel_mean(kernel, full_mean)
    gamma_red = generator_carre_du_champ_scalar(reduced_generator, reduced_mean)
    gamma_full = generator_carre_du_champ_scalar(full_generator, full_mean)
    return sp.simplify(gamma_red - kernel * gamma_full)


def hidden_two_state_mean(amplitude: sp.Expr, rate: sp.Expr, tau: sp.Expr) -> Matrix:
    """Mean semigroup for symmetric hidden switching from terminal values (+a,-a)."""
    decay = sp.exp(-2 * rate * tau)
    return sp.Matrix([amplitude * decay, -amplitude * decay])


def hidden_two_state_resolution_variance(amplitude: sp.Expr, rate: sp.Expr, tau: sp.Expr) -> sp.Expr:
    """Resolution variance under the stationary 1/2,1/2 reduction kernel."""
    return sp.simplify(amplitude**2 * sp.exp(-4 * rate * tau))


def flat_joint_fp_operator_1d(
    density: sp.Expr,
    anchor_drift: sp.Expr,
    shape_drift: sp.Expr,
    x: sp.Symbol,
    r: sp.Symbol,
    t: sp.Symbol,
    nu: sp.Expr,
) -> sp.Expr:
    """J mu=mu_t+d_x(b_+ mu)+d_r(v_R mu)-nu mu_xx."""
    return sp.simplify(
        sp.diff(density, t)
        + sp.diff(anchor_drift * density, x)
        + sp.diff(shape_drift * density, r)
        - nu * sp.diff(density, x, 2)
    )


def flat_anchor_marginal_fp_operator_1d(
    q: sp.Expr,
    anchor_drift: sp.Expr,
    x: sp.Symbol,
    t: sp.Symbol,
    nu: sp.Expr,
) -> sp.Expr:
    return sp.simplify(
        sp.diff(q, t)
        + sp.diff(anchor_drift * q, x)
        - nu * sp.diff(q, x, 2)
    )


def flat_conditional_shape_operator_1d(
    kappa: sp.Expr,
    q: sp.Expr,
    anchor_drift: sp.Expr,
    shape_drift: sp.Expr,
    x: sp.Symbol,
    r: sp.Symbol,
    t: sp.Symbol,
    nu: sp.Expr,
) -> sp.Expr:
    """C kappa with b_-=b_+-2nu d_x log q."""
    b_minus = sp.simplify(anchor_drift - 2 * nu * sp.diff(q, x) / q)
    return sp.simplify(
        sp.diff(kappa, t)
        + b_minus * sp.diff(kappa, x)
        + sp.diff(shape_drift * kappa, r)
        - nu * sp.diff(kappa, x, 2)
    )


def flat_joint_marginal_conditional_factorization_residual_1d(
    q: sp.Expr,
    kappa: sp.Expr,
    anchor_drift: sp.Expr,
    shape_drift: sp.Expr,
    x: sp.Symbol,
    r: sp.Symbol,
    t: sp.Symbol,
    nu: sp.Expr,
) -> sp.Expr:
    """J(q kappa)-kappa M(q)-q C(kappa), identically zero."""
    joint = flat_joint_fp_operator_1d(q * kappa, anchor_drift, shape_drift, x, r, t, nu)
    marginal = flat_anchor_marginal_fp_operator_1d(q, anchor_drift, x, t, nu)
    conditional = flat_conditional_shape_operator_1d(kappa, q, anchor_drift, shape_drift, x, r, t, nu)
    return sp.simplify(joint - kappa * marginal - q * conditional)
