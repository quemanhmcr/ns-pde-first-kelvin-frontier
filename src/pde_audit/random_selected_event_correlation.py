"""Exact two-replica algebra for random/adaptive selected event maps.

Pathwise a finite selected event is already reduced to a physical map C=E_+ A from
the pre-event persistent library to the post-event selected residual.  If C depends
on the state/replica, expectation cannot be replaced by a mean event map acting on a
mean payload.

For two equal-weight replicas define

    Cbar=(C1+C2)/2, dC=C1-C2,
    Qbar=(Q1+Q2)/2, dQ=Q1-Q2.

Then exactly

  1/2(C1 Q1 C1^T + C2 Q2 C2^T)
   = Cbar Qbar Cbar^T
     + 1/4 dC Qbar dC^T
     + 1/4 Cbar dQ dC^T
     + 1/4 dC dQ Cbar^T.

The second face is event-map dispersion; the last two are signed event-state
correlation faces.  The identity applies to any symmetric second-order payload,
including a state second moment or a same-replica continuous q.v. Gram.
"""
from __future__ import annotations

import sympy as sp

Matrix = sp.MatrixBase


def two_replica_mean_output_faces(
    event_map_1: Matrix,
    state_1: Matrix,
    event_map_2: Matrix,
    state_2: Matrix,
) -> tuple[Matrix,Matrix]:
    """Return naive mean-map face and exact map/state correlation face."""
    if state_1.shape != state_2.shape or state_1.cols != 1:
        raise ValueError("replica states must be equal-size columns")
    if event_map_1.shape != event_map_2.shape or event_map_1.cols != state_1.rows:
        raise ValueError("event map/state dimensions mismatch")
    Cbar=sp.simplify((event_map_1+event_map_2)/2)
    dC=sp.simplify(event_map_1-event_map_2)
    xbar=sp.simplify((state_1+state_2)/2)
    dx=sp.simplify(state_1-state_2)
    naive=sp.simplify(Cbar*xbar)
    correlation=sp.simplify(dC*dx/4)
    return naive,correlation


def two_replica_mean_output_residual(
    event_map_1: Matrix,
    state_1: Matrix,
    event_map_2: Matrix,
    state_2: Matrix,
) -> Matrix:
    exact=sp.simplify((event_map_1*state_1+event_map_2*state_2)/2)
    naive,corr=two_replica_mean_output_faces(event_map_1,state_1,event_map_2,state_2)
    return sp.simplify(exact-naive-corr)


def two_replica_congruence_faces(
    event_map_1: Matrix,
    payload_1: Matrix,
    event_map_2: Matrix,
    payload_2: Matrix,
) -> tuple[Matrix,Matrix,Matrix,Matrix]:
    """Return naive, event-dispersion, left-correlation, right-correlation faces."""
    if event_map_1.shape != event_map_2.shape:
        raise ValueError("event maps must have equal shape")
    n=event_map_1.cols
    if payload_1.shape != (n,n) or payload_2.shape != (n,n):
        raise ValueError("payload dimensions must match event-map input")
    Cbar=sp.simplify((event_map_1+event_map_2)/2)
    dC=sp.simplify(event_map_1-event_map_2)
    Qbar=sp.simplify((payload_1+payload_2)/2)
    dQ=sp.simplify(payload_1-payload_2)
    naive=sp.simplify(Cbar*Qbar*Cbar.T)
    dispersion=sp.simplify(dC*Qbar*dC.T/4)
    corr_left=sp.simplify(Cbar*dQ*dC.T/4)
    corr_right=sp.simplify(dC*dQ*Cbar.T/4)
    return naive,dispersion,corr_left,corr_right


def two_replica_congruence_residual(
    event_map_1: Matrix,
    payload_1: Matrix,
    event_map_2: Matrix,
    payload_2: Matrix,
) -> Matrix:
    exact=sp.simplify((event_map_1*payload_1*event_map_1.T+event_map_2*payload_2*event_map_2.T)/2)
    faces=two_replica_congruence_faces(event_map_1,payload_1,event_map_2,payload_2)
    return sp.simplify(exact-sum(faces,sp.zeros(exact.rows)))


def event_dispersion_face_psd_quadratic_form(
    event_map_1: Matrix,
    payload_bar: Matrix,
    event_map_2: Matrix,
    probe: Matrix,
) -> sp.Expr:
    """probe^T [1/4 dC Qbar dC^T] probe, nonnegative when Qbar is PSD."""
    if probe.cols != 1 or probe.rows != event_map_1.rows:
        raise ValueError("probe output dimension mismatch")
    dC=sp.simplify(event_map_1-event_map_2)
    return sp.simplify((probe.T*dC*payload_bar*dC.T*probe)[0]/4)


def adaptive_event_alignment_calibrations() -> dict[str,sp.Expr|Matrix|bool]:
    """Two PSD two-replica witnesses with positive and negative correlation alignment.

    The event maps are coordinate readouts C1=[1,0], C2=[0,1].  In the aligned case
    each event reads the energetic coordinate of its own replica; in the anti-aligned
    case it reads the zero coordinate.  Both use the same mean map and mean payload.
    """
    C1=sp.Matrix([[1,0]])
    C2=sp.Matrix([[0,1]])
    Q1_plus=sp.diag(4,0)
    Q2_plus=sp.diag(0,4)
    Q1_minus=sp.diag(0,4)
    Q2_minus=sp.diag(4,0)

    def values(Q1: Matrix,Q2: Matrix) -> tuple[sp.Expr,sp.Expr,sp.Expr,sp.Expr,sp.Expr]:
        exact=sp.simplify(((C1*Q1*C1.T)[0]+(C2*Q2*C2.T)[0])/2)
        n,d,l,r=two_replica_congruence_faces(C1,Q1,C2,Q2)
        return exact,n[0],d[0],l[0],r[0]

    ep,np,dp,lp,rp=values(Q1_plus,Q2_plus)
    em,nm,dm,lm,rm=values(Q1_minus,Q2_minus)
    return {
        "maps":sp.Matrix.vstack(C1,C2),
        "positive_exact":ep,
        "positive_naive":np,
        "positive_dispersion":dp,
        "positive_corr_left":lp,
        "positive_corr_right":rp,
        "negative_exact":em,
        "negative_naive":nm,
        "negative_dispersion":dm,
        "negative_corr_left":lm,
        "negative_corr_right":rm,
        "all_payloads_psd":all(Q.is_positive_semidefinite for Q in (Q1_plus,Q2_plus,Q1_minus,Q2_minus)),
    }
