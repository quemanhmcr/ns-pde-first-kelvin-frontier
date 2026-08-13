"""Same-replica dynamics of a finite library of codeforming Kelvin residual packets.

For physical packets carried by one stochastic flow replica, every packet is driven
by the same three-dimensional spatial Wiener motion.  Stacking the exact driftless
codeforming residual martingales therefore produces one tall noise matrix and one
full Gram quadratic-variation tensor with mandatory signed cross-germ blocks.
"""
from __future__ import annotations

from collections.abc import Sequence
import sympy as sp

from .selected_principal_kelvin_lineage import germ_extraction_map
from .weighted_codeforming_kelvin_residual import one_mode_asymmetric_codeforming_noise

Matrix = sp.MatrixBase


def stacked_common_noise(noise_blocks: Sequence[Matrix]) -> Matrix:
    if not noise_blocks:
        raise ValueError("nonempty packet-noise library required")
    driver_dim=noise_blocks[0].cols
    fiber_dim=noise_blocks[0].rows
    if any(Q.shape != (fiber_dim,driver_dim) for Q in noise_blocks):
        raise ValueError("all packet noise blocks must share fiber and driver dimensions")
    return sp.Matrix.vstack(*noise_blocks)


def same_replica_library_qv(noise_blocks: Sequence[Matrix], nu: sp.Expr) -> Matrix:
    S=stacked_common_noise(noise_blocks)
    return sp.simplify(2*nu*S*S.T)


def same_replica_qv_block(
    noise_blocks: Sequence[Matrix],
    left: int,
    right: int,
    nu: sp.Expr,
) -> Matrix:
    if not (0 <= left < len(noise_blocks) and 0 <= right < len(noise_blocks)):
        raise ValueError("packet index out of range")
    return sp.simplify(2*nu*noise_blocks[left]*noise_blocks[right].T)


def library_qv_block_residual(
    noise_blocks: Sequence[Matrix],
    left: int,
    right: int,
    nu: sp.Expr,
) -> Matrix:
    G=same_replica_library_qv(noise_blocks,nu)
    d=noise_blocks[0].rows
    block=G[left*d:(left+1)*d,right*d:(right+1)*d]
    return sp.simplify(block-same_replica_qv_block(noise_blocks,left,right,nu))


def selected_qv_readout_residual(
    noise_blocks: Sequence[Matrix],
    index: int,
    nu: sp.Expr,
) -> Matrix:
    d=noise_blocks[0].rows
    E=germ_extraction_map(len(noise_blocks),index,d)
    G=same_replica_library_qv(noise_blocks,nu)
    return sp.simplify(E*G*E.T-2*nu*noise_blocks[index]*noise_blocks[index].T)


def linear_event_noise(noise_blocks: Sequence[Matrix], event_map: Matrix) -> Matrix:
    S=stacked_common_noise(noise_blocks)
    if event_map.cols != S.rows:
        raise ValueError("event map/library noise dimensions do not compose")
    return sp.simplify(event_map*S)


def linear_event_qv_functor_residual(
    noise_blocks: Sequence[Matrix],
    event_map: Matrix,
    nu: sp.Expr,
) -> Matrix:
    Splus=linear_event_noise(noise_blocks,event_map)
    lhs=sp.simplify(2*nu*Splus*Splus.T)
    G=same_replica_library_qv(noise_blocks,nu)
    rhs=sp.simplify(event_map*G*event_map.T)
    return sp.simplify(lhs-rhs)


def independent_noise_diagonal_qv(noise_blocks: Sequence[Matrix], nu: sp.Expr) -> Matrix:
    """Counterfactual model with independent Brownian drivers per packet."""
    return sp.diag(*[sp.simplify(2*nu*Q*Q.T) for Q in noise_blocks])


def independent_vs_common_qv_difference(noise_blocks: Sequence[Matrix], nu: sp.Expr) -> Matrix:
    return sp.simplify(independent_noise_diagonal_qv(noise_blocks,nu)-same_replica_library_qv(noise_blocks,nu))


def stacked_martingale_mean_rate(packet_count: int, fiber_dim: int = 3) -> Matrix:
    if packet_count <= 0 or fiber_dim <= 0:
        raise ValueError("positive packet/fiber dimensions required")
    return sp.zeros(packet_count*fiber_dim,1)


def fixed_noise_centered_covariance_rate(noise_blocks: Sequence[Matrix], nu: sp.Expr) -> Matrix:
    """For fixed deterministic noise blocks, centered covariance grows by the q.v. Gram."""
    return same_replica_library_qv(noise_blocks,nu)


def qv_image_rank_bound(noise_blocks: Sequence[Matrix], nu: sp.Expr) -> tuple[int,int]:
    """Return (rank Gamma, driver dimension); factorization forces the first <= second."""
    S=stacked_common_noise(noise_blocks)
    G=same_replica_library_qv(noise_blocks,nu)
    return G.rank(),S.cols


def one_mode_two_packet_common_noise_calibration(
    t: sp.Expr,
    nu: sp.Expr,
    k: sp.Expr,
) -> dict[str,sp.Expr|Matrix]:
    """Exact NS two-packet same-replica q.v. cancellation.

    Packets have side pi/(2k), anchors pi/(2k) and 3pi/(2k), and only the
    z-residual/y-Brownian coefficient is active in this calibration.
    """
    Y=sp.symbols("Y_library", real=True)
    side=sp.pi/(2*k)
    q=one_mode_asymmetric_codeforming_noise(Y,t,side,nu,k)
    q1=sp.trigsimp(sp.simplify(q.subs(Y,sp.pi/(2*k))))
    q2=sp.trigsimp(sp.simplify(q.subs(Y,3*sp.pi/(2*k))))
    Q1=sp.zeros(3); Q2=sp.zeros(3)
    Q1[2,1]=q1; Q2[2,1]=q2
    noises=[Q1,Q2]
    G=same_replica_library_qv(noises,nu)
    Gind=independent_noise_diagonal_qv(noises,nu)
    A=sp.Matrix.hstack(sp.eye(3),sp.eye(3))
    synth_common=sp.simplify(A*G*A.T)
    synth_independent=sp.simplify(A*Gind*A.T)
    return {
        "q1":q1,
        "q2":q2,
        "opposite_noise_residual":sp.simplify(q1+q2),
        "common_qv":G,
        "independent_qv":Gind,
        "cross_qv":same_replica_qv_block(noises,0,1,nu),
        "diagonal_qv":same_replica_qv_block(noises,0,0,nu),
        "synthesized_common_qv":synth_common,
        "synthesized_independent_qv":synth_independent,
        "common_event_functor_residual":linear_event_qv_functor_residual(noises,A,nu),
    }
