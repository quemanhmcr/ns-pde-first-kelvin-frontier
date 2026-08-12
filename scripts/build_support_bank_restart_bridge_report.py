from __future__ import annotations

import json
from pathlib import Path
import sys
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from pde_audit.support_bank_restart_bridge import (
    causal_backward_kelvin_horizon,
    fixed_past_horizon_candidate_limit,
    future_candidate_remaining_horizon,
    horizon_matching_residual,
    moving_past_terminal_matching_future_horizon,
    one_mode_fixed_terminal_second_moment_residual,
    one_mode_moving_terminal_covariance_residual,
    one_mode_moving_terminal_second_moment_residual,
    parabolic_support_dynamics_residual,
    scalar_vorticity_rate_square_bound,
    scale_parametric_three_face_residual,
    support_bank_three_face_residual,
    time_integrated_vorticity_rate_bound,
)

p,q,nu,tau,eps=sp.symbols('p q nu tau eps', positive=True)
F=sp.Matrix([[2,1,0],[0,1,1],[1,0,1]])
eta=sp.Matrix(sp.symbols('e0:3'))
c=sp.symbols('c0:6')
C=sp.Matrix([[c[0],c[1],c[2]],[c[1],c[3],c[4]],[c[2],c[4],c[5]]])
A=sp.Matrix(3,3,sp.symbols('a0:9'))
Theta,t,t0=sp.symbols('Theta t t0')
y,k=sp.symbols('y k', positive=True)
ell2=sp.symbols('ell2')
scale_res=scale_parametric_three_face_residual(F,eta,C,p,q,ell2)

report={
  'classification':{
    'support_bank_factorization':'Exact scale-parametric tensor identity on the ideal coherent physical state; no clock identification required',
    'conditional_rate':'Rigorous conditional algebra once a shrinking physical scale and a total-second-moment family are paired on the same state/scale',
    'time_integrability':'Conditional two-clock bridge, not an already-established causal backward-Kelvin theorem for tau=Theta-t',
    'scale_covariance_horizon_identification':'Open-literal: fixed-past backward-Kelvin horizon h=t-t0 grows, whereas future remaining horizon tau=Theta-t shrinks',
    'programme_uniformity':'Open: no uniform first-bad/global p,q envelope or ancestry-to-physical state lift is proved',
    'continuation_restart':'Open; no regularity conclusion',
  },
  'factorization':{
    'three_face_residual_zero':bool(support_bank_three_face_residual(F,eta,C,p,q,nu,tau)==sp.zeros(3)),
    'scale_parametric_residual_zero':bool(scale_res==sp.zeros(3)),
    'physical_faces':['support headroom pI-P_nu','total-bank headroom qI-Q_tot','unresolved covariance Q_tot-eta eta^T'],
  },
  'rate':{
    'omega_square_bound':str(scalar_vorticity_rate_square_bound(p,q,nu,tau)),
    'integrated_bound_over_terminal_epsilon':str(time_integrated_vorticity_rate_bound(p*q,nu,eps)),
  },
  'support_dynamics':{
    'Pdot_residual_zero':bool(parabolic_support_dynamics_residual(A,F,nu,tau)==sp.zeros(3)),
    'law':'Pdot=A P+P A^T-P/tau for tau=Theta-t',
  },
  'clock_scope':{
    'causal_past_horizon':str(causal_backward_kelvin_horizon(t,t0)),
    'future_remaining_horizon':str(future_candidate_remaining_horizon(Theta,t)),
    'moving_past_terminal_to_match':str(moving_past_terminal_matching_future_horizon(Theta,t)),
    'moving_terminal_rate':str(sp.diff(moving_past_terminal_matching_future_horizon(Theta,t),t)),
    'matching_residual_zero':bool(horizon_matching_residual(Theta,t)==0),
    'fixed_past_candidate_limit':str(fixed_past_horizon_candidate_limit(Theta,t0)),
    'fixed_terminal_second_moment_residual_zero':bool(one_mode_fixed_terminal_second_moment_residual(y,t,t0,nu,k)==0),
    'moving_terminal_second_moment_residual_zero':bool(one_mode_moving_terminal_second_moment_residual(y,t,Theta,nu,k)==0),
    'moving_terminal_covariance_residual_zero':bool(one_mode_moving_terminal_covariance_residual(y,t,Theta,nu,k)==0),
    'moving_terminal_face':'t0dot * partial_t0 Q with t0dot=2 for h=Theta-t',
  },
  'frontier':{
    'resolved':'exact scale-parametric tensor route from coherent support geometry and total second moment to a conditional vorticity-rate envelope',
    'still_open':'identify the shrinking future first-bad scale with a causal/ancestry covariance family, then prove uniform/global envelopes, nonideal face control, state lift, and continuation',
  }
}
out=Path('audit-results/support_bank_restart_bridge_report.json')
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps(report,indent=2,sort_keys=True))
