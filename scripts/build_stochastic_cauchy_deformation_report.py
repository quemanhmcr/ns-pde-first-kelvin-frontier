from __future__ import annotations
import json,sys
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'src'))
from pde_audit.stochastic_cauchy_deformation import (
    affine_vortex_cauchy_z_residual, affine_vortex_total_bank_envelope_residual,
    cauchy_packet_metric_duality_residual,
    one_mode_shear_second_moment, one_mode_shear_terminal_headroom,
    one_mode_shear_terminal_supremum,
)
a,r0,s,t,nu,k,y=sp.symbols('a r0 s t nu k y', positive=True)
W=one_mode_shear_terminal_supremum(s,nu,k)
D=sp.Matrix([[2,1],[1,1]]); rho=sp.symbols('rho', positive=True)
Q=one_mode_shear_second_moment(y,t,s,nu,k)
H=one_mode_shear_terminal_headroom(y,t,s,nu,k)
report={
 'classification':{
   'fixed_past_cauchy_payoff':'Exact physical representation type Y=D omega(A_s^t,s); mean is current vorticity',
   'total_bank_envelope':'Rigorous Loewner consequence Q<=W_s R with R=E[D D^T] and W_s=sup|omega(s)|^2',
   'two_face_gap':'Exact W_s R-omega omega^T=(W_s R-Q)+(Q-omega omega^T): terminal directional headroom plus stochastic covariance',
   'deformation_moment':'Exact reverse-age law R_sigma=2 E[D S D^T], generally not closed on R alone',
   'fixed_past_uniform_bound':'Open: smooth past vorticity alone does not bound R; stochastic deformation moment remains physical obstruction',
   'continuation_restart':'Open; no regularity conclusion',
 },
 'affine_vortex':{
   'cauchy_z_residual_zero':bool(affine_vortex_cauchy_z_residual(a,r0,s,t)==0),
   'terminal_envelope_residual_zero':bool(affine_vortex_total_bank_envelope_residual(a,r0,s,t)==0),
   'centered_covariance':'zero: spatially uniform vorticity and affine deformation are deterministic relative to anchor noise',
   'interpretation':'all vorticity growth is carried by deformation, not centered covariance',
 },
 'one_mode_shear':{
   'terminal_supremum':str(W),
   'second_moment':str(Q),
   'terminal_headroom':str(H),
   'vorticity_direction_deformation':'1',
   'interpretation':'sampling/covariance sector is active while vorticity-direction deformation is absent',
 },
 'packet_metric_duality':{
   'residual_zero':bool(cauchy_packet_metric_duality_residual(D,rho)==sp.zeros(2)),
   'identity':'D D^T = rho^4 M_H on the same stochastic replica deformation',
   'interpretation':'stochastic Cauchy deformation Gram is the unscaled coherent Kelvin packet metric, not a new geometry',
 },
 'frontier':{
   'resolved':'fixed-past total-bank amplitude decomposes into terminal vorticity size times stochastic Cauchy deformation moment plus exact covariance/headroom faces',
   'still_open':'uniform control and the programme-specific alignment of deterministic first-bad selected support with the same stochastic replica deformation whose packet metric equals D D^T',
 }
}
out=Path('audit-results/stochastic_cauchy_deformation_report.json'); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n'); print(json.dumps(report,indent=2,sort_keys=True))
