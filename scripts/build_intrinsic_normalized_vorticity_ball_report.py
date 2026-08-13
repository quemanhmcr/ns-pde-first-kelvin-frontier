from __future__ import annotations
import json, sys
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from pde_audit.intrinsic_normalized_vorticity_ball import elliptic_polarization_contact_calibration

OUT=ROOT/'audit-results'/'intrinsic_normalized_vorticity_ball_report.json'
x,y,z,t=sp.symbols('x y z t', real=True)
nu,a,k=sp.symbols('nu a k', positive=True)
beta=sp.symbols('beta', nonnegative=True)
c=elliptic_polarization_contact_calibration(a,beta,k,(x,y,z),t,nu)
helical={key: sp.simplify(value.subs(beta,1)) if hasattr(value,'subs') else value for key,value in c.items()}
linear={key: sp.simplify(value.subs(beta,0)) if hasattr(value,'subs') else value for key,value in c.items()}
report={
  'classification':{
    'normalized_vorticity_pde':'Exact local Navier-Stokes identity at max-envelope differentiability times',
    'unit_ball_contact_split':'Exact geometric identity',
    'contact_kernel_completeness':'Rigorous consequence at active maxima',
    'kelvin_gram_duality':'Exact Kelvin/q.v.-normalized-gradient identity',
    'elliptic_polarization_transfer':'Audited exact-NS calibration',
    'scalar_jet_exhaustion':'Audited exact-NS no-go',
    'first_bad_contact_identification':'Open-literal',
    'restart_continuation_regularity':'Open',
  },
  'family':{
    'ns_residual':str(c['ns_residual']),
    'normalized_vorticity_pde_residual':str(c['normalized_vorticity_pde_residual']),
    'unit_ball_gap':str(c['unit_ball_gap']),
    'unit_ball_gap_factor_residual':str(c['unit_ball_gap_factor_residual']),
    'scalar_source':str(c['scalar_source']),
    'tangency_identity_residual':str(c['tangency_identity_residual']),
    'contact_identity_residual':str(c['contact_identity_residual']),
    'right_gram_at_active_point':str(c['right_gram']),
    'left_gram_at_active_point':str(c['left_gram']),
    'scalar_curvature_at_active_point':str(c['scalar_curvature']),
    'contact_form_at_active_point':str(c['contact_form']),
    'polarization_transfer_residual':str(c['polarization_transfer_residual']),
    'contact_frequency_residual':str(c['contact_frequency_residual']),
    'kelvin_left_gram_residual':str(c['kelvin_left_gram_residual']),
    'kelvin_bulk_trace_residual':str(c['kelvin_bulk_trace_residual']),
    'gram_trace_residual':str(c['gram_trace_residual']),
  },
  'linear_endpoint':{
    'right_gram':str(linear['right_gram']),
    'scalar_curvature':str(linear['scalar_curvature']),
    'contact_form':str(linear['contact_form']),
  },
  'helical_endpoint':{
    'normalized_enstrophy':str(sp.trigsimp(helical['normalized_enstrophy'])),
    'scalar_source':str(helical['scalar_source']),
    'scalar_curvature':str(helical['scalar_curvature']),
    'right_gram':str(helical['right_gram']),
    'contact_form':str(helical['contact_form']),
    'kelvin_bulk':str(helical['kelvin_bulk']),
  },
  'frontier':{
    'resolved':'scalar curvature plus normalized-vorticity tangent motion are the two forced faces of one unit-ball contact form; scalar higher-jet exhaustion is not universal',
    'open_literal':'actual first-bad contact coercivity and closure of directions in ker(contact) by higher vector contact/material symmetry',
    'open':'uniform singular-time support/refinement control, restart, continuation, regularity',
  },
}
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(OUT)
