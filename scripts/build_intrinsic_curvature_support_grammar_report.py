from __future__ import annotations
import json, sys
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from pde_audit.intrinsic_curvature_support_grammar import (
    curvature_support_connection_cancellation_residual,
    curvature_support_tensor,
    one_mode_persistent_flat_kernel_calibration,
)
from pde_audit.intrinsic_curvature_support_calibrations import (
    three_mode_kernel_birth_calibration,
    three_mode_kernel_birth_global_certificate,
)
from pde_audit.intrinsic_normalized_vorticity_ball import elliptic_polarization_contact_calibration
OUT=ROOT/'audit-results'/'intrinsic_curvature_support_grammar_report.json'
x,y,z,t=sp.symbols('x y z t', real=True)
nu=sp.symbols('nu', positive=True)
A,n=sp.symbols('A n', positive=True)
c=sp.symbols('c', real=True)
beta=sp.symbols('beta', nonnegative=True)
one=one_mode_persistent_flat_kernel_calibration(A,n,(x,y,z),t,nu)
birth=three_mode_kernel_birth_calibration((x,y,z),t,nu)
cert=three_mode_kernel_birth_global_certificate(c)
ball=elliptic_polarization_contact_calibration(A,beta,n,(x,y,z),t,nu)
G=sp.Matrix([[1,2,0],[0,-3,1],[4,0,2]])
Q=sp.Matrix([[2,1,0],[1,3,1],[0,1,5]])
K=sp.Matrix([[5,0,1],[0,6,2],[1,2,7]])
L=sp.Matrix([[1,1,0],[0,2,1],[1,0,1]])
report={
  'classification':{
    'covariant_curvature_law':'Exact local Navier-Stokes identity',
    'curvature_support_duality':'Exact Cauchy/Nanson compatibility identity',
    'psd_kernel_viability':'Rigorous consequence conditional on differentiable persistent maximum branch',
    'three_mode_kernel_birth':'Audited exact-NS global calibration',
    'first_bad_identification':'Open-literal',
    'restart_continuation_regularity':'Open',
  },
  'grammar':{
    'generic_connection_cancellation_residual':str(curvature_support_connection_cancellation_residual(G,Q,K,L)),
    'singular_safe_example':str(curvature_support_tensor(sp.diag(0,2,0),sp.diag(3,4,5))),
  },
  'persistent_flat_referee':{
    'curvature':str(one['curvature']),
    'source_curvature':str(one['source_curvature']),
    'x_flat_opening':str(one['x_flat_opening']),
    'z_flat_opening':str(one['z_flat_opening']),
    'covariant_residual':str(one['covariant_residual']),
  },
  'diffusive_kernel_birth':{
    'global_upper_factor':str(cert['upper_factor']),
    'global_derivative_factor':str(cert['derivative_factor']),
    'q_at_one':str(cert['value_at_one']),
    'q_at_minus_one':str(cert['value_at_minus_one']),
    'q_at_internal_critical':str(cert['value_at_internal_critical']),
    'lower_margin':str(cert['lower_margin_at_internal_critical']),
    'ns_residual':str(birth['ns_residual']),
    'enstrophy_balance_residual':str(birth['enstrophy_balance_residual']),
    'max_enstrophy':str(birth['max_enstrophy']),
    'max_rate':str(birth['max_rate']),
    'curvature':str(birth['curvature']),
    'source_curvature':str(birth['source_curvature']),
    'stretch_source_curvature':str(birth['stretch_source_curvature']),
    'kelvin_bulk_source_curvature':str(birth['kelvin_bulk_source_curvature']),
    'curvature_diffusion_source_curvature':str(birth['curvature_diffusion_source_curvature']),
    'source_face_residual':str(birth['source_face_residual']),
    'quartic_enstrophy_derivative':str(birth['quartic_enstrophy_derivative']),
    'z_curvature_opening_rate':str(birth['z_curvature_opening_rate']),
    'z_kernel_opening':str(birth['z_kernel_opening']),
    'kernel_normalization_residual':str(birth['kernel_normalization_residual']),
    'covariant_residual':str(birth['covariant_residual']),
  },
  'normalized_vorticity_unit_ball':{
    'ns_residual':str(ball['ns_residual']),
    'vector_pde_residual':str(ball['normalized_vorticity_pde_residual']),
    'unit_ball_gap_factor_residual':str(ball['unit_ball_gap_factor_residual']),
    'contact_identity_residual':str(ball['contact_identity_residual']),
    'right_gram_at_active_point':str(ball['right_gram']),
    'scalar_curvature_at_active_point':str(ball['scalar_curvature']),
    'contact_form_at_active_point':str(ball['contact_form']),
    'contact_frequency_residual':str(ball['contact_frequency_residual']),
    'kelvin_left_gram_residual':str(ball['kelvin_left_gram_residual']),
    'kelvin_bulk_trace_residual':str(ball['kelvin_bulk_trace_residual']),
    'helical_scalar_germ':str(sp.trigsimp(ball['normalized_enstrophy'].subs(beta,1))),
    'helical_scalar_curvature':str(sp.simplify(ball['scalar_curvature'].subs(beta,1))),
    'helical_right_gram':str(sp.simplify(ball['right_gram'].subs(beta,1))),
    'helical_contact':str(sp.simplify(ball['contact_form'].subs(beta,1))),
    'helical_kelvin_bulk':str(sp.simplify(ball['kelvin_bulk'].subs(beta,1))),
  },
  'frontier':{
    'resolved':'deformation connection cannot change curvature rank; kernel opening/branch viability is controlled by source curvature plus literal reanchoring',
    'open_literal':'actual first-bad identification and closure of higher-order flat directions when first-order kernel compression vanishes',
    'open':'uniform singular-time support/refinement control, restart, continuation, regularity',
  },
}
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(OUT)
