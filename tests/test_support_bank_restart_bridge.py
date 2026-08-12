from __future__ import annotations

from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pde_audit.support_bank_restart_bridge import (  # noqa: E402
    codeforming_total_second_moment,
    parabolic_support_dynamics_residual,
    parabolic_support_tensor,
    physical_total_second_moment,
    physical_vorticity_from_codeforming,
    resolved_unresolved_factorization_residual,
    scalar_vorticity_rate_square_bound,
    support_bank_three_face_residual,
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

    def test_rate_theorem_is_not_a_first_bad_threshold_by_itself(self) -> None:
        p,q,nu,tau=sp.symbols('p q nu tau', positive=True)
        # The theorem returns a conditional rate envelope; no Boolean event is encoded.
        bound=scalar_vorticity_rate_square_bound(p,q,nu,tau)
        self.assertTrue(bound.has(p,q,tau))


if __name__=='__main__':
    unittest.main()
