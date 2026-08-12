from __future__ import annotations

import json
from pathlib import Path
import sys
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from pde_audit.support_bank_restart_bridge import (
    parabolic_support_dynamics_residual,
    scalar_vorticity_rate_square_bound,
    support_bank_three_face_residual,
    time_integrated_vorticity_rate_bound,
)

p,q,nu,tau,eps=sp.symbols('p q nu tau eps', positive=True)
F=sp.Matrix([[2,1,0],[0,1,1],[1,0,1]])
eta=sp.Matrix(sp.symbols('e0:3'))
c=sp.symbols('c0:6')
C=sp.Matrix([[c[0],c[1],c[2]],[c[1],c[3],c[4]],[c[2],c[4],c[5]]])
A=sp.Matrix(3,3,sp.symbols('a0:9'))
report={
  'classification':{
    'support_bank_factorization':'Exact tensor identity on the ideal full physical Kelvin core',
    'conditional_rate':'Rigorous conditional consequence: Loewner envelopes P_nu<=pI and Q_tot<=qI imply |omega|^2<=pq/(2nu tau)',
    'time_integrability':'Rigorous conditional local consequence if the product envelope pq stays bounded near the candidate time',
    'programme_uniformity':'Open: no uniform first-bad/global p,q envelope or ancestry-to-physical state lift is proved',
    'continuation_restart':'Open; no regularity conclusion',
  },
  'factorization':{
    'three_face_residual_zero':bool(support_bank_three_face_residual(F,eta,C,p,q,nu,tau)==sp.zeros(3)),
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
  'frontier':{
    'resolved':'exact local tensor route from physical parabolic support and total Kelvin second moment to a vorticity-rate envelope',
    'still_open':'uniform/global first-bad envelopes, nonideal finite-shape/localization faces, state lift, and literal continuation theorem',
  }
}
out=Path('audit-results/support_bank_restart_bridge_report.json')
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps(report,indent=2,sort_keys=True))
