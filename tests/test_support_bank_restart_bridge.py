from __future__ import annotations

from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.support_bank_restart_bridge import (  # noqa: E402
    causal_backward_kelvin_horizon,
    codeforming_total_second_moment,
    fixed_past_horizon_candidate_limit,
    future_candidate_remaining_horizon,
    horizon_matching_residual,
    moving_past_terminal_matching_future_horizon,
    moving_terminal_chain_derivative,
    one_mode_fixed_terminal_second_moment_residual,
    one_mode_moving_terminal_covariance_residual,
    one_mode_moving_terminal_second_moment_residual,
    parabolic_support_dynamics_residual,
    parabolic_support_tensor,
    physical_total_second_moment,
    physical_vorticity_from_codeforming,
    resolved_unresolved_factorization_residual,
    scalar_vorticity_rate_square_bound,
    scale_parametric_three_face_residual,
    support_bank_three_face_residual,
    support_tensor_from_scale_squared,
    time_integrated_vorticity_rate_bound,
    total_bank_support_factorization_residual,
)


class SupportBankRestartBridgeAudit(unittest.TestCase):
    def test_total_second_moment_is_mean_dyad_plus_covariance(self) -> None:
        e1,e2,c11,c12,c22=sp.symbols('e1 e2 c11 c12 c22')
        eta=sp.Matrix([e1,e2])
        C=sp.Matrix([[c11,c12],[c12,c22]])
        self.assertEqual(codeforming_total_second_moment(eta,C), eta*eta.T+C)

    def test_physical_resolved_plus_unresolved_factorization_is_exact(self) -> None:
        F=sp.Matrix([[2,1],[1,1]])
        e1,e2,c11,c12,c22=sp.symbols('e1 e2 c11 c12 c22')
        eta=sp.Matrix([e1,e2])
        C=sp.Matrix([[c11,c12],[c12,c22]])
        self.assertEqual(resolved_unresolved_factorization_residual(F,eta,C),sp.zeros(2))

    def test_three_face_support_bank_factorization_is_exact_for_full_matrices(self) -> None:
        F=sp.Matrix([[2,1,0],[0,1,1],[1,0,1]])
        e=sp.Matrix(sp.symbols('e0:3'))
        c=sp.symbols('c0:6')
        C=sp.Matrix([[c[0],c[1],c[2]],[c[1],c[3],c[4]],[c[2],c[4],c[5]]])
        p,q,nu,tau=sp.symbols('p q nu tau')
        residual=support_bank_three_face_residual(F,e,C,p,q,nu,tau)
        self.assertEqual(residual,sp.zeros(3))

    def test_total_bank_support_factorization_is_exact(self) -> None:
        F=sp.Matrix([[2,1],[1,1]])
        q,nu,tau=sp.symbols('q nu tau')
        Q=sp.Matrix([[3,1],[1,2]])
        self.assertEqual(total_bank_support_factorization_residual(F,Q,q,nu,tau),sp.zeros(2))

    def test_tensor_envelope_reduces_to_scalar_vorticity_rate(self) -> None:
        p,q,nu,tau=sp.symbols('p q nu tau', positive=True)
        self.assertEqual(scalar_vorticity_rate_square_bound(p,q,nu,tau),p*q/(2*nu*tau))

    def test_bounded_support_bank_product_has_integrable_tau_minus_half_rate(self) -> None:
        M,nu,eps,tau=sp.symbols('M nu eps tau', positive=True)
        rate=sp.sqrt(M/(2*nu*tau))
        direct=sp.integrate(rate,(tau,0,eps))
        expected=time_integrated_vorticity_rate_bound(M,nu,eps)
        self.assertEqual(sp.simplify(direct-expected),0)

    def test_parabolic_support_tensor_has_exact_physical_time_dynamics(self) -> None:
        a=sp.symbols('a0:9')
        A=sp.Matrix(3,3,a)
        F=sp.Matrix([[2,1,0],[0,2,1],[1,0,1]])
        nu,tau=sp.symbols('nu tau', nonzero=True)
        self.assertEqual(parabolic_support_dynamics_residual(A,F,nu,tau),sp.zeros(3))

    def test_support_tensor_is_squared_kelvin_scale_line_geometry(self) -> None:
        nu,tau=sp.symbols('nu tau', positive=True)
        f1,f2,f3=sp.symbols('f1 f2 f3', positive=True)
        F=sp.diag(f1,f2,f3)
        P=parabolic_support_tensor(F,nu,tau)
        rho=sp.sqrt(2*nu*tau)
        self.assertEqual(P,sp.diag((rho*f1)**2,(rho*f2)**2,(rho*f3)**2))

    def test_diagonal_positive_sector_witness_gives_nonnegative_gap_components(self) -> None:
        # Explicit positive numbers satisfying P<=pI, Q<=qI, eta eta^T<=Q.
        nu=tau=sp.Integer(1)
        F=sp.diag(1,2)
        eta=sp.Matrix([1,1])
        C=sp.diag(3,4)
        Q=codeforming_total_second_moment(eta,C)
        P=parabolic_support_tensor(F,nu,tau)
        # Use conservative scalar envelopes p=8, q=7.
        pstar,qstar=sp.Integer(8),sp.Integer(7)
        gap=sp.simplify(pstar*qstar*sp.eye(2)-2*nu*tau*(F*eta)*(F*eta).T)
        self.assertTrue(gap.is_positive_semidefinite)
        self.assertTrue(sp.simplify(pstar*sp.eye(2)-P).is_positive_semidefinite)
        self.assertTrue(sp.simplify(qstar*sp.eye(2)-Q).is_positive_semidefinite)
        self.assertTrue(C.is_positive_semidefinite)


    def test_three_face_factorization_is_really_scale_parametric_not_clock_specific(self) -> None:
        ell2,p,q=sp.symbols('ell2 p q')
        F=sp.Matrix([[2,1],[1,1]])
        eta=sp.Matrix(sp.symbols('e0:2'))
        c11,c12,c22=sp.symbols('c11 c12 c22')
        C=sp.Matrix([[c11,c12],[c12,c22]])
        self.assertEqual(scale_parametric_three_face_residual(F,eta,C,p,q,ell2),sp.zeros(2))
        self.assertEqual(support_tensor_from_scale_squared(F,ell2),ell2*F*F.T)

    def test_fixed_past_terminal_horizon_does_not_shrink_at_future_candidate_time(self) -> None:
        Theta,t,t0=sp.symbols('Theta t t0')
        h=causal_backward_kelvin_horizon(t,t0)
        self.assertEqual(h,t-t0)
        self.assertEqual(fixed_past_horizon_candidate_limit(Theta,t0),Theta-t0)

    def test_matching_causal_past_horizon_to_future_remaining_horizon_requires_moving_terminal(self) -> None:
        Theta,t=sp.symbols('Theta t')
        t0=moving_past_terminal_matching_future_horizon(Theta,t)
        self.assertEqual(t0,2*t-Theta)
        self.assertEqual(sp.diff(t0,t),2)
        self.assertEqual(horizon_matching_residual(Theta,t),0)

    def test_future_remaining_horizon_and_fixed_past_horizon_have_opposite_time_rates(self) -> None:
        Theta,t,t0=sp.symbols('Theta t t0')
        h=causal_backward_kelvin_horizon(t,t0)
        tau=future_candidate_remaining_horizon(Theta,t)
        self.assertEqual(sp.diff(h,t),1)
        self.assertEqual(sp.diff(tau,t),-1)


    def test_generic_moving_terminal_chain_rule_has_explicit_terminal_face(self) -> None:
        Qt,Qt0,v=sp.symbols('Qt Qt0 v')
        self.assertEqual(moving_terminal_chain_derivative(Qt,Qt0,v),Qt+v*Qt0)

    def test_one_mode_fixed_past_terminal_second_moment_has_homogeneous_backward_kelvin_law(self) -> None:
        y,t,t0,nu,k=sp.symbols('y t t0 nu k', positive=True)
        self.assertEqual(one_mode_fixed_terminal_second_moment_residual(y,t,t0,nu,k),0)

    def test_one_mode_moving_past_terminal_second_moment_has_exact_terminal_motion_face(self) -> None:
        y,t,Theta,nu,k=sp.symbols('y t Theta nu k', positive=True)
        self.assertEqual(one_mode_moving_terminal_second_moment_residual(y,t,Theta,nu,k),0)

    def test_one_mode_moving_past_terminal_covariance_has_qv_plus_terminal_motion_face(self) -> None:
        y,t,Theta,nu,k=sp.symbols('y t Theta nu k', positive=True)
        self.assertEqual(one_mode_moving_terminal_covariance_residual(y,t,Theta,nu,k),0)

    def test_rate_theorem_is_not_a_first_bad_threshold_by_itself(self) -> None:
        p,q,nu,tau=sp.symbols('p q nu tau', positive=True)
        # The theorem returns a conditional rate envelope; no Boolean event is encoded.
        bound=scalar_vorticity_rate_square_bound(p,q,nu,tau)
        self.assertTrue(bound.has(p,q,tau))


if __name__=='__main__':
    unittest.main()
