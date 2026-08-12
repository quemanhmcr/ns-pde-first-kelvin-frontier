# Adversarial audit — Kelvin restart/covariance frontier

Date: 2026-08-12. Scope intentionally narrow: proof-critical compatibility between the exact Kelvin/NS identities and the proposed restart bank.

## Priority finding P0 — physical time and stochastic ancestry time are being conflated

The local Kelvin noise coefficient is consistent with Navier--Stokes **when derived on the reverse-time stochastic flow**. For a closed loop, reverse drift `-u` and additive noise `sqrt(2 nu)` cancel the viscous drift modulo an exact pressure/gauge form; Cartan reduces the noise coefficient to

`sqrt(2 nu) <i_e Omega,Z>`.

So the local `gamma=2 nu sum_i <i_{e_i}Omega,Z>^2` normalization is not the problem.

The problem is the time orientation of the bank. `selected_kelvin_pair_localization_budget.md` calls `V_s` variance to a common **future physical terminal horizon** `Theta`, uses `D_s C=-Gamma`, and later combines the same `s` with the moving first-bad selector. The repository's own exact shear calibration has the opposite stochastic meaning.

For

`u(a,t)=exp(-nu k^2 t) cos(k a)`,

a forward Brownian anchor satisfies

`d u(a_t,t) = -2 nu k^2 u(a_t,t) dt + sqrt(2 nu) partial_a u dW`.

It has the advertised bracket rate `gamma`, but it is **not** a martingale. In reverse physical time the drift cancels exactly. Equivalently,

`u(a,t)=E[cos(k(a+sqrt(2 nu t) Z))]`

is ancestry to the time-zero field. For `s<Theta`, ordinary future Brownian conditioning gives instead

`E_s[u(X_Theta,Theta)] = exp(-nu k^2(2 Theta-s)) cos(k a) != u(a,s)`.

The multi-mode payoff `X_N` used by the repository has scale `sqrt(2 nu T_N)` and no terminal viscous prefactor, so it is exactly of this **past/ancestral** type.

This changes the sign of the distributed bank in the same calibration: with uniform anchor measure,

`d/dt <V(a,t)> = <gamma(a,t)> > 0`,

whereas the proposed future-physical bank has `d/ds int q V = - int q gamma`.

There is also a path mismatch. The true reverse-time Kelvin bracket for a fixed physical loop `Z_t` follows its random back-transport `Z_tau^back`, schematically

`int 2 nu sum_i <i_{e_i} Omega_{t-tau}, Z_tau^back>^2 d tau`.

The programme's target instead follows contemporaneous first-bad germs,

`int 2 nu sum_i <i_{xi_i} Omega_s, Z_{lambda_*(s)}>^2 ds`.

These are not the same stochastic process. Therefore the one-clock formula

`d(a_s^T C_s a_s)/ds = -Gamma_s(a_s,a_s) + 2 C_s(a_s,a_dot_s)`

is not yet a physical-time selected-Kelvin bank theorem.

**Required repair:** introduce separate physical and ancestry clocks (`t`,`tau`), the reverse stochastic flow/filtration, the random back-transported current, and the terminal variable. Then prove a two-time identity connecting the ancestry bracket to the contemporaneous first-bad action before using any physical-time telescope.

## Priority finding P1 — the Doob equation is parabolic, not an ordinary exact one-form

`pair_localization_worldsheet_audit.md` writes

`A_cov = d_pair V - gamma ds = d_spacetime V`

and applies ordinary Stokes. This is false when `D_s` contains the diffusion generator.

The exact one-mode calibration gives, in remaining-time `tau`,

`partial_tau V - nu partial_a^2 V = gamma`.

With `s=Theta-tau`,

`partial_s V = -gamma - nu partial_a^2 V`,

so the ordinary differential contains the extra diffusion term. At `a=0`, `gamma=0` but `nu partial_a^2 V>0` for every `tau>0`, giving a direct counterexample inside the repository's exact NS calibration.

**Required repair:** replace the de Rham/Stokes packaging by Dynkin--Itô/Markov duality or by the already-derived forward--backward covariance flux law. A second-order generator is not an exterior derivation.

## Priority finding P1 — centered future covariance is not the tensor carrying deterministic vortex stretching

Let terminal material flux be `Y` and write

`m=E_s Y`, `C=Cov_s(Y)`, `Q=E_s[YY^T]=C+m m^T`.

With `omega=H^(-T)m`, literal deterministic stretching is

`omega.S.omega = (1/2) m^T Mdot m`.

The centered covariance contributes a different metric term,

`(1/2) tr(C Mdot) = tr(S Sigma_cov)`.

They cannot be identified. At the terminal horizon `C=0`, while the repository's exact ABC calibration has

`omega.S.omega = 3 A^3 exp(-3 nu t) != 0`

at `(0,0,0)`. The one-mode calibration gives the same separation dynamically: `Q` obeys the homogeneous backward heat equation, whereas `C` carries the positive `gamma` source.

**Required repair:** track `m m^T` and `C` separately, or use `Q=C+m m^T` and derive its distinct evolution law.

## Priority finding P1 — moving quantile/shell cuts need the time-face flux, not only the spatial commutator

`active_first_bad_germ_pair_maps.md` defines a moving quantile restriction `Q_s` but the literal quantile stage records only

`C_quant = B Q_s - Q_{s,0} B`,

which is the spatial boundary commutator. A moving characteristic also has a distributional time derivative. In one space dimension, for a conservation law

`partial_t q + partial_x(q v)=0`

and moving chamber `D_t=(-infinity,a(t))`, Reynolds gives exactly

`d/dt int_{D_t} q dx = -q(a,t) (v(a,t)-a_dot(t))`.

The `a_dot q` face is not contained in the static spatial commutator. In operator language it is the `Qdot` term in the transport defect `G_Q=Qdot+T_out Q-Q T_in`. The repository has the abstract `G_F` product rule and mentions `Mdot`, but no literal `Qdot`/moving-shell map or test is inserted for the quantile stage; current CI uses static interval block projections.

**Required repair:** instantiate the moving cut as a spacetime current and retain its boundary-speed term (and the two replica faces at pair level) before declaring the completed quantile/shell seam exhaustive.

## Priority finding P1 — area-frame shrinkage needs an independent support-locality hypothesis

Small area vectors do not uniformly imply a spatially local packet near a candidate singular time. An exact periodic NS witness is

`u_r(y,t)=(r^(-1) exp(-nu k^2 t) cos(k y),0,0)`.

The nonlinearity vanishes. Its flow shears an initially `r x r` material face at `y0=pi/(2k)` while preserving its area exactly as `r^2`; nevertheless its diameter has a positive `r->0` limit. Thus no uniform implication `H->0 => support diameter->0` holds across smooth NS states without a deformation bound.

Consequently a local covariance expansion must assume actual support shrinkage. For anisotropic packets, raw `R_H=o(||H||^2)` is also insufficient because `M=(H^T H)^(-1)` amplifies weak directions. The invariant requirement is of the form

`tr(R_H M_H)->0`,

or, at payoff level, `H^(-T) epsilon_H -> 0` in conditional `L^2`.

## Minor domain caveat — determinant rate

The incompressible conclusion `D_t det M_H=0` is correct. The displayed extension `D_t log det M_H=2 div u` should not be read as general 3D Nanson: the general rate is `-4 div u`. This does not affect the present incompressible route.

## Independently re-derived backbone that survived this audit

The following exact identities were re-derived and no counterexample was found:

- `D_t(H^T omega)=nu H^T Delta omega` under incompressible Nanson transport;
- `(1/2) Phi^T Mdot Phi = omega.S.omega` for deterministic material flux `Phi=H^T omega`;
- `(1/2) tr(2 nu H^T (grad omega)(grad omega)^T H M)=nu |grad omega|_F^2` for invertible `H`;
- the same-ancestor diagonal branching difference leaves `2 nu sum_mu D_mu^(1)D_mu^(2)` and cancels first-order drift;
- covariance reset/full tensor-square algebra retains mandatory cross terms.

## Audit status

No counterexample to 3D Navier--Stokes regularity is claimed. The local Kelvin/Nanson backbone remains viable. The proof-critical restart route is **not yet certified** because the current covariance reservoir mixes physical time with stochastic ancestry time, and the subsequent world-sheet/metric ledger inherits that mismatch.
