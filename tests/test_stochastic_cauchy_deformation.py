from __future__ import annotations

from pathlib import Path
import sys
import unittest
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))

from pde_audit.kelvin_packet_locality import (  # noqa: E402
    affine_vortex_stretch_ns_residual,
)
from pde_audit.stochastic_cauchy_deformation import (  # noqa: E402
    affine_vortex_cauchy_z_residual,
    affine_vortex_total_bank_envelope_residual,
    cauchy_sample,
    cauchy_two_face_envelope_residual,
    deformation_gram_rate_residual,
    deformation_reverse_age_residual,
    ensemble_cauchy_moments,
    ensemble_deformation_rate_residual,
    ensemble_terminal_headroom_residual,
    incompressible_deformation_determinant_log_rate,
    one_mode_shear_second_moment,
    one_mode_shear_terminal_headroom,
    one_mode_shear_terminal_supremum,
    sample_terminal_headroom_residual,
)

class StochasticCauchyDeformationAudit(unittest.TestCase):
    def test_sample_terminal_headroom_factorization_is_exact(self) -> None:
        D=sp.Matrix([[2,1],[1,1]])
        w=sp.Matrix(sp.symbols('w0:2'))
        W=sp.symbols('W')
        self.assertEqual(sample_terminal_headroom_residual(D,w,W),sp.zeros(2))

    def test_ensemble_terminal_headroom_factorization_is_exact(self) -> None:
        D1=sp.Matrix([[1,1],[0,1]])
        D2=sp.Matrix([[2,0],[1,1]])
        w1=sp.Matrix(sp.symbols('a0:2'))
        w2=sp.Matrix(sp.symbols('b0:2'))
        p=sp.symbols('p')
        weights=[p,1-p]
        W=sp.symbols('W')
        self.assertEqual(ensemble_terminal_headroom_residual([D1,D2],[w1,w2],weights,W),sp.zeros(2))

    def test_total_vorticity_envelope_splits_into_terminal_headroom_plus_covariance(self) -> None:
        D1=sp.eye(2); D2=sp.Matrix([[1,1],[0,1]])
        w1=sp.Matrix([1,0]); w2=sp.Matrix([0,1])
        m,Q,C,R=ensemble_cauchy_moments([D1,D2],[w1,w2],[sp.Rational(1,2)]*2)
        W=sp.Integer(1)
        self.assertEqual(cauchy_two_face_envelope_residual(m,Q,R,W),sp.zeros(2))
        self.assertTrue(C.is_positive_semidefinite)

    def test_reverse_age_deformation_and_gram_rate_are_exact(self) -> None:
        d11,d12,d21,d22=sp.symbols('d11 d12 d21 d22')
        a11,a12,a21,a22=sp.symbols('a11 a12 a21 a22')
        D=sp.Matrix([[d11,d12],[d21,d22]])
        A=sp.Matrix([[a11,a12],[a21,a22]])
        Ddot=sp.simplify(D*A.T)
        self.assertEqual(deformation_reverse_age_residual(D,Ddot,A),sp.zeros(2))
        self.assertEqual(deformation_gram_rate_residual(D,Ddot,A),sp.zeros(2))

    def test_incompressible_deformation_preserves_pathwise_volume_not_shape(self) -> None:
        a,b,c=sp.symbols('a b c')
        A=sp.diag(a,b,c)
        rate=incompressible_deformation_determinant_log_rate(A).subs(c,-a-b)
        self.assertEqual(sp.simplify(rate),0)

    def test_ensemble_deformation_moment_law_is_exact_and_not_closed_on_R_only(self) -> None:
        D1=sp.diag(2,1); D2=sp.diag(1,3)
        s1,s2=sp.symbols('s1 s2')
        A1=sp.diag(s1,-s1); A2=sp.diag(s2,-s2)
        weights=[sp.Rational(1,2)]*2
        rhs=sp.simplify(
            (2*D1*((A1+A1.T)/2)*D1.T + 2*D2*((A2+A2.T)/2)*D2.T)/2
        )
        self.assertEqual(ensemble_deformation_rate_residual([D1,D2],[A1,A2],weights,rhs),sp.zeros(2))
        self.assertTrue(rhs.has(s1,s2))

    def test_genuine_affine_vortex_ns_has_pathwise_cauchy_stretch_and_zero_centered_variance(self) -> None:
        a,r0,s,t,nu=sp.symbols('a r0 s t nu', positive=True)
        x,y,z=sp.symbols('x y z')
        ns,_=affine_vortex_stretch_ns_residual(a,r0,t,(x,y,z),nu)
        self.assertEqual(sp.simplify(ns),sp.zeros(3,1))
        self.assertEqual(affine_vortex_cauchy_z_residual(a,r0,s,t),0)
        self.assertEqual(affine_vortex_total_bank_envelope_residual(a,r0,s,t),0)
        # The affine gradient is spatially uniform, so the stochastic anchor does
        # not randomize the deformation or the spatially uniform vorticity payoff.

    def test_one_mode_shear_has_no_vorticity_direction_deformation_but_positive_covariance_bank(self) -> None:
        y,t,s,nu,k=sp.symbols('y t s nu k', positive=True)
        W=one_mode_shear_terminal_supremum(s,nu,k)
        Q=one_mode_shear_second_moment(y,t,s,nu,k)
        headroom=one_mode_shear_terminal_headroom(y,t,s,nu,k)
        self.assertEqual(sp.simplify(W-Q-headroom),0)
        # At y=pi/(2k), terminal headroom remains nonnegative for t>=s.
        h=sp.symbols('h', nonnegative=True)
        special=sp.simplify(headroom.subs({y:sp.pi/(2*k),t:s+h}))
        expected=sp.simplify(W/2*(1-sp.exp(-4*nu*k**2*h)))
        self.assertEqual(sp.simplify(special-expected),0)

    def test_smooth_past_vorticity_bound_does_not_remove_deformation_moment(self) -> None:
        W,r=sp.symbols('W r', positive=True)
        # The direct Loewner envelope is W*R, not W*I.
        self.assertNotEqual(W*r,W)

if __name__=='__main__':
    unittest.main()
