from __future__ import annotations

import json
from pathlib import Path
import sys
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from pde_audit.first_bad_candidate_exclusions import (
    abc_enstrophy_gradient_at, abc_origin_quantities, abc_stretching_at,
    amplitude_limits,
)

A,nu,t=sp.symbols('A nu t', positive=True)
q=abc_origin_quantities(A,nu,t)
limits=amplitude_limits(A,abc_origin_quantities(A,nu,sp.Integer(0)))
p0=(0,0,0)
pc=(sp.pi/4,sp.pi/4,sp.pi/4)
report={
  'classification':{
    'raw_instantaneous_thresholds':'Excluded as universal continuation-failure predicates by exact globally smooth periodic amplitude-scaled ABC family',
    'diagnostic_use':'Still allowed; exclusion concerns sufficiency for continuation failure, not localization utility',
    'local_max_growth_gate':'Not excluded by the ABC origin witness because origin is not an enstrophy critical point; gate remains only a necessary local-growth condition, not a first-bad theorem',
    'badness_functional':'Open-literal; no replacement first-bad score is proposed',
    'continuation_restart':'Open; no regularity conclusion',
  },
  'abc_origin':{
    'omega_sq':str(q.omega_sq),
    'enstrophy':str(q.enstrophy),
    'stretching':str(q.stretching),
    'kelvin_bulk':str(q.kelvin_bulk),
    'stretch_bulk_ratio':str(q.stretch_bulk_ratio),
    'growth_gate_margin':str(q.growth_gate_margin),
  },
  'amplitude_limits_at_t0':{k:str(v) for k,v in limits.items()},
  'gate_scope_check':{
    'origin_enstrophy_gradient':str(abc_enstrophy_gradient_at(A,nu,t,p0)),
    'symmetric_critical_gradient':str(abc_enstrophy_gradient_at(A,nu,t,pc)),
    'symmetric_critical_stretching':str(abc_stretching_at(A,nu,t,pc)),
  },
  'frontier':{
    'resolved':'raw amplitude/stretching/qv/instantaneous-ratio thresholds cannot alone certify continuation failure',
    'still_open':'derive a physical NS badness/resolve event tied to the actual restart obstruction rather than raw instantaneous size',
  }
}
out=Path('audit-results/first_bad_candidate_exclusions_report.json')
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps(report,indent=2,sort_keys=True))
