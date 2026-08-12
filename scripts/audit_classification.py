from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
note = ROOT / "docs" / "selected_kelvin_pair_localization_budget.md"
active_note = ROOT / "docs" / "active_first_bad_germ_pair_maps.md"
cycle_note = ROOT / "docs" / "cycle_typed_first_bad_selector.md"
hodge_note = ROOT / "docs" / "hodge_cycle_projector_audit.md"
ck_note = ROOT / "docs" / "kelvin_ck_admissibility_audit.md"
stochastic_note = ROOT / "docs" / "stochastic_cycle_map_audit.md"
vorticity_note = ROOT / "docs" / "vorticity_kelvin_restart_audit.md"
packet_note = ROOT / "docs" / "orientation_complete_restart_packet.md"
future_tensor_note = ROOT / "docs" / "future_covariance_tensor_audit.md"
shape_note = ROOT / "docs" / "kelvin_shape_generator_audit.md"
time_note = ROOT / "docs" / "ancestry_time_reversal_audit.md"
locality_note = ROOT / "docs" / "kelvin_packet_locality_audit.md"
resolution_note = ROOT / "docs" / "ancestry_resolution_kernel_audit.md"
clock_cut_note = ROOT / "docs" / "clock_cut_compatibility_audit.md"
two_clock_note = ROOT / "docs" / "two_clock_kelvin_quantile_audit.md"
event_note = ROOT / "docs" / "first_bad_event_semantics_audit.md"
candidate_note = ROOT / "docs" / "first_bad_candidate_exclusions_audit.md"
support_bank_note = ROOT / "docs" / "support_bank_restart_bridge_audit.md"
cauchy_note = ROOT / "docs" / "stochastic_cauchy_deformation_audit.md"
coupling_note = ROOT / "docs" / "deformation_current_pair_coupling_audit.md"
full_shape_cov_note = ROOT / "docs" / "full_current_shape_covariance_audit.md"
descent_note = ROOT / "docs" / "finite_shape_kelvin_descent_audit.md"
moment_note = ROOT / "docs" / "surface_moment_hierarchy_audit.md"
codeforming_note = ROOT / "docs" / "codeforming_surface_moment_tower_audit.md"
whitened_codeforming_note = ROOT / "docs" / "codeforming_whitened_kelvin_remainder_audit.md"
text = note.read_text()
active_text = active_note.read_text()
cycle_text = cycle_note.read_text()
hodge_text = hodge_note.read_text()
ck_text = ck_note.read_text()
stochastic_text = stochastic_note.read_text()
vorticity_text = vorticity_note.read_text()
packet_text = packet_note.read_text()
future_tensor_text = future_tensor_note.read_text()
shape_text = shape_note.read_text()
time_text = time_note.read_text()
locality_text = locality_note.read_text()
resolution_text = resolution_note.read_text()
clock_cut_text = clock_cut_note.read_text()
two_clock_text = two_clock_note.read_text()
event_text = event_note.read_text()
candidate_text = candidate_note.read_text()
support_bank_text = support_bank_note.read_text()
cauchy_text = cauchy_note.read_text()
coupling_text = coupling_note.read_text()
full_shape_cov_text = full_shape_cov_note.read_text()
descent_text = descent_note.read_text()
moment_text = moment_note.read_text()
codeforming_text = codeforming_note.read_text()
whitened_codeforming_text = whitened_codeforming_note.read_text()
required = [
    "Exact identity",
    "Rigorous consequence",
    "Conjectural bridge",
    "No continuation",
    "Z_irr",
    "pair localization",
]
missing = [token for token in required if token not in text]
if missing:
    print("missing required structural markers:", missing)
    sys.exit(1)
active_required = [
    "P_active",
    "There is no autonomous pair-only residual",
    "Conjectural bridge",
    "No continuation/restart conclusion",
    "Cycle-typed correction",
]
active_missing = [token for token in active_required if token not in active_text]
if active_missing:
    print("missing active-map structural markers:", active_missing)
    sys.exit(1)
cycle_required = [
    "B_xK_s=0",
    "C_{\\rm irr}^{\\rm selector}=0",
    "G_{\\rm irr}^{\\rm selector}=0",
    "off-cycle",
    "Exact identity",
    "Rigorous consequence",
    "Conjectural bridge",
    "S^int",
    "no continuation/restart",
]
cycle_missing = [token for token in cycle_required if token not in cycle_text]
if cycle_missing:
    print("missing cycle-typed selector structural markers:", cycle_missing)
    sys.exit(1)
hodge_required = [
    "H_W^2=H_W",
    "P G P=0",
    "Q G Q=0",
    "Conjectural bridge",
    "S^int",
    "No continuation/restart",
]
hodge_missing = [token for token in hodge_required if token not in hodge_text]
if hodge_missing:
    print("missing Hodge projector structural markers:", hodge_missing)
    sys.exit(1)

ck_required = [
    "BHK=0",
    "H^2 != H",
    "pressure/gauge",
    "non-idempotent",
    "differentiable nonlinear",
    "original pair-content-defect",
    "S^int",
    "Conjectural bridge",
    "No continuation/restart",
]
ck_missing = [token for token in ck_required if token not in ck_text]
if ck_missing:
    print("missing Kelvin CK admissibility structural markers:", ck_missing)
    sys.exit(1)

stochastic_required = [
    "quadratic-variation/carré-du-champ",
    "finite-variation",
    "S^int",
    "Exact identity",
    "Conjectural bridge",
    "No continuation/restart",
]
stochastic_missing = [token for token in stochastic_required if token not in stochastic_text]
if stochastic_missing:
    print("missing stochastic cycle-map structural markers:", stochastic_missing)
    sys.exit(1)

vorticity_required = [
    "Kelvin microframe",
    "orientation-complete",
    "area-squared",
    "dilation",
    "Material-germ restart ledger",
    "Exact identity",
    "Rigorous structural consequence",
    "Conjectural bridge",
    "No continuation/restart theorem",
]
vorticity_missing = [token for token in vorticity_required if token not in vorticity_text]
if vorticity_missing:
    print("missing vorticity/Kelvin restart structural markers:", vorticity_missing)
    sys.exit(1)

packet_required = [
    "orientation-complete",
    "cross-orientation",
    "GL(3)",
    "Material vorticity flux removes stretching from the flux equation",
    "Vortex stretching is packet metric work",
    "p-4",
    "future-covariance tensor",
    "Exact identity",
    "Conjectural bridge",
    "No continuation/restart theorem",
]
packet_missing = [token for token in packet_required if token not in packet_text]
if packet_missing:
    print("missing orientation-complete restart packet structural markers:", packet_missing)
    sys.exit(1)

future_tensor_required = [
    "Full-state vector conditional moments",
    "double-Stokes",
    "metric-whitened",
    "support locality",
    "vorticity dyad",
    "backward-Kelvin",
    "Generator descent",
    "open-literal physical state",
    "No continuation/restart theorem",
]
future_tensor_missing = [token for token in future_tensor_required if token not in future_tensor_text]
if future_tensor_missing:
    print("missing future-covariance tensor structural markers:", future_tensor_missing)
    sys.exit(1)

shape_required = [
    "common Wiener",
    "zero martingale part",
    "E_{\\rm shape}",
    "cubic heat shear",
    "same anchor",
    "r^4",
    "r^2",
    "No regularity conclusion",
]
shape_missing = [token for token in shape_required if token not in shape_text]
if shape_missing:
    print("missing Kelvin current-shape structural markers:", shape_missing)
    sys.exit(1)

time_required = [
    "Fokker--Planck",
    "b_+",
    "b_-",
    "midpoint",
    "w_{\\rm required}",
    "w=u",
    "reference gauge",
    "Open-literal state-identification bridge",
    "No regularity conclusion",
]
time_missing = [token for token in time_required if token not in time_text]
if time_missing:
    print("missing ancestry time-reversal structural markers:", time_missing)
    sys.exit(1)

locality_required = [
    "Small area is not spatial locality",
    "metric-whitened",
    "sigma_{\\min}",
    "long-thin",
    "Rigorous conditional fixed-state theorem",
    "Open singular-time bridge",
]
locality_missing = [token for token in locality_required if token not in locality_text]
if locality_missing:
    print("missing Kelvin packet locality structural markers:", locality_missing)
    sys.exit(1)

resolution_required = [
    "law of total covariance",
    "resolution covariance",
    "same ancestor",
    "affine shear",
    "rank `3`",
    "Full-state ancestry",
    "reduced ancestry",
    "S^int",
    "Open-literal ancestry-state semantics",
]
resolution_missing = [token for token in resolution_required if token not in resolution_text]
if resolution_missing:
    print("missing ancestry resolution-kernel structural markers:", resolution_missing)
    sys.exit(1)

clock_cut_required = [
    "Two clocks must not be silently identified",
    "parabolic, not an ordinary exact one-form",
    "Moving quantile/shell cuts have a time face",
    "boundary-speed",
    "Exact two-clock chain rule",
    "open-literal",
    "No continuation, restart, or regularity theorem",
]
clock_cut_missing = [token for token in clock_cut_required if token not in clock_cut_text]
if clock_cut_missing:
    print("missing clock/cut compatibility structural markers:", clock_cut_missing)
    sys.exit(1)

two_clock_required = [
    "reverse age",
    "b_+=-u",
    "b_-=u",
    "K_{\\rm K}=D\\Pi",
    "probability-current velocity",
    "dot a_p",
    "open-literal",
    "No continuation",
]
two_clock_missing = [token for token in two_clock_required if token not in two_clock_text]
if two_clock_missing:
    print("missing two-clock Kelvin/quantile structural markers:", two_clock_missing)
    sys.exit(1)

event_required = [
    "bad_flags",
    "resolved",
    "piecewise constant",
    "finite events",
    "first-bad event selector",
    "moving quantile/shell cut",
    "open-literal",
    "No restart",
]
event_missing = [token for token in event_required if token not in event_text]
if event_missing:
    print("missing first-bad event-semantics structural markers:", event_missing)
    sys.exit(1)

candidate_required = [
    "amplitude-scaled ABC",
    "smooth periodic",
    "continuation-failure",
    "diagnostic",
    "local enstrophy",
    "not an enstrophy critical point",
    "Open-literal",
    "No replacement threshold",
]
candidate_missing = [token for token in candidate_required if token not in candidate_text]
if candidate_missing:
    print("missing first-bad candidate-exclusion structural markers:", candidate_missing)
    sys.exit(1)

support_bank_required = [
    "P_nu",
    "Q_tot",
    "scale-parametric",
    "causal past horizon",
    "moving terminal",
    "support headroom",
    "total-bank principal headroom",
    "unresolved future covariance",
    "time-integrable",
    "not yet a restart theorem",
    "Open-literal",
]
support_bank_missing = [token for token in support_bank_required if token not in support_bank_text]
if support_bank_missing:
    print("missing support-bank restart-bridge structural markers:", support_bank_missing)
    sys.exit(1)

cauchy_required = [
    "stochastic Cauchy deformation",
    "terminal directional headroom",
    "centered covariance",
    "R_s",
    "finite variation",
    "affine-vortex",
    "one-mode",
    "D D^T",
    "packet metric",
    "same stochastic replica",
    "full vectorized deformation covariance",
    "row-Gram projection",
    "anchor carré-du-champ",
    "causal past horizon",
    "connected vector covariance theorem",
    "vector law of total covariance",
    "additional resolution covariance",
    "Sigma_D",
    "C_D^Gram",
    "two-replica",
    "h^3",
    "naive equality",
    "Open-literal",
    "Open",
    "No continuation",
]
cauchy_missing = [token for token in cauchy_required if token not in cauchy_text]
if cauchy_missing:
    print("missing stochastic Cauchy deformation structural markers:", cauchy_missing)
    sys.exit(1)

coupling_required = [
    "spatial tangent fiber",
    "cannot manufacture a physical boundary seam",
    "full ordered pair current",
    "fixed local cochain",
    "2 nu / 3",
    "Dropping the cross pair terms is not an identity",
    "Shared/frozen first-bad selector",
    "Replica-dependent selector",
    "finite Kelvin-current state",
    "cubic heat shear",
    "Open-literal",
    "No continuation/restart/regularity theorem claimed",
]
coupling_missing = [token for token in coupling_required if token not in coupling_text]
if coupling_missing:
    print("missing deformation/current coupling structural markers:", coupling_missing)
    sys.exit(1)

full_shape_cov_required = [
    "only martingale/q.v. channel",
    "pressure/Bernoulli gauge",
    "anchor carré-du-champ",
    "deformation--circulation cross covariance",
    "off-diagonal block",
    "h^2",
    "Gram-integral",
    "Literal reverse-age full state",
    "Open-literal",
    "No restart/continuation/regularity theorem claimed",
]
full_shape_cov_missing = [token for token in full_shape_cov_required if token not in full_shape_cov_text]
if full_shape_cov_missing:
    print("missing full current-shape covariance structural markers:", full_shape_cov_missing)
    sys.exit(1)

finite_shape_descent_required = [
    "opposite local connection signs",
    "finite-support vorticity-inhomogeneity flux",
    "finite-variation shape drift",
    "vorticity-gradient residual",
    "Pathwise q.v. versus finite-horizon covariance",
    "connected-covariance",
    "oriented quadrupole",
    "zero q.v.",
    "covariance-only",
    "ABC",
    "Legendre",
    "Open-literal",
    "No restart/continuation/regularity theorem claimed",
]
finite_shape_descent_missing = [token for token in finite_shape_descent_required if token not in descent_text]
if finite_shape_descent_missing:
    print("missing finite-shape Kelvin descent structural markers:", finite_shape_descent_missing)
    sys.exit(1)

surface_moment_required = [
    "oriented material-surface moment hierarchy",
    "Affine velocity is the exact order-preserving case",
    "upward-coupled hierarchy",
    "quadratic heat-shear",
    "material-anchor centering is not dynamically preserved",
    "F'=F-c h^T",
    "conserves an entire hidden moment tower",
    "not stored",
    "physically zero",
    "finite low-moment state",
    "Open-literal",
    "No restart/continuation/regularity theorem claimed",
]
surface_moment_missing = [token for token in surface_moment_required if token not in moment_text]
if surface_moment_missing:
    print("missing surface-moment hierarchy structural markers:", surface_moment_missing)
    sys.exit(1)

codeforming_required = [
    "m+2",
    "unit-determinant shape action",
    "Full codeforming pullback",
    "single codeforming nonaffinity field",
    "residual incompressible velocity",
    "generating current",
    "rho^(p-1)",
    "Coherent linear refinement is a gauge",
    "codeforming tower constancy does not imply physical support collapse",
    "bounded scalar-normalized moments are **not necessary**",
    "support diameter collapse alone does not imply codeforming affine collapse",
    "Open-literal",
    "No restart/continuation/regularity theorem claimed",
    "metric-weighted nonaffinity one-form",
    "exact Stokes--Piola identity",
    "three distinct physical faces",
    "does **not** imply a large Kelvin descent error",
    "Instantaneous Kelvin readout descent",
    "Dynamic current-shape descent",
    "anchor derivative of the Kelvin one-form",
    "entire exact finite-shape error SDE",
    "no new bank",
]
codeforming_missing = [token for token in codeforming_required if token not in codeforming_text]
if codeforming_missing:
    print("missing codeforming surface-moment structural markers:", codeforming_missing)
    sys.exit(1)

whitened_codeforming_required = [
    "whitening is exact physical inversion",
    "reconstructed physical residual vector",
    "not a pointwise field value",
    "Exact cubic NS referee",
    "r^2",
    "Homogeneous jet exponent ladder",
    "ordinary energy of the reconstructed residual",
    "Passive orientation coordinates are gauge",
    "stochastic q.v. also reconstructs exactly",
    "mandatory local--residual cross blocks",
    "cross-clock identification",
    "Open-literal",
    "No restart/continuation/regularity theorem claimed",
]
whitened_codeforming_missing = [token for token in whitened_codeforming_required if token not in whitened_codeforming_text]
if whitened_codeforming_missing:
    print("missing codeforming whitened-Kelvin structural markers:", whitened_codeforming_missing)
    sys.exit(1)

for forbidden in [
    "therefore 3D Navier--Stokes is regular",
    "global regularity is proved",
    "S^int = 0 is established",
    "S^int=0 iff Z_irr=0 is proved",
    "restart capacity is bounded",
    "first-bad threshold is established",
    "uniform singular-time covariance tensor is controlled",
    "spatial future-covariance generator descent is proved",
    "forward future bank equals backward Kelvin bank",
    "future covariance tensor closes restart",
    "finite-scale (x,H) generator descent is exact",
    "finite shape hierarchy is uniformly controlled",
    "shape residual is S^int",
    "ancestry state is proved identical to physical Kelvin state",
    "w=u is established generally",
    "H->0 implies packet locality",
    "small area frame proves support locality",
    "raw Frobenius remainder is sufficient",
    "ancestry full-rank diffusion carries Kelvin shape",
    "reduced same ancestor has only viscous branching",
    "resolution covariance is viscous q.v.",
    "resolution covariance is S^int",
    "finite quadrupole closes the full shape state",
    "finite moment hierarchy closes exactly",
    "Kelvin parabolic scale is the first-bad threshold",
    "parabolic support coefficient 1/2 proves regularity",
    "co-deforming total bank proves restart",
    "one-clock selected Kelvin bank is a physical-time theorem",
    "static quantile commutator exhausts moving cut",
    "moving shell needs no time face",
    "second-order covariance generator is an ordinary exterior derivative",
    "b_-=u closes the future bank",
    "b_-=u proves the future-bank bridge",
    "quantile boundary moves with u alone",
    "quantile boundary moves with b_+ alone",
    "one-clock ancestry continuity determines physical first-bad cut speed",
    "reverse-age Kelvin clock proves ancestry state identification",
    "bad_flags are derived from Navier-Stokes",
    "resolved is derived from Navier-Stokes",
    "first-bad projector is the moving quantile cut",
    "M_fb dot is the quantile boundary speed",
    "local enstrophy growth gate is the first-bad threshold",
    "ABC disproves the local-maximum growth gate",
    "raw vorticity threshold certifies singularity",
    "instantaneous stretching threshold certifies continuation failure",
    "stretching/Kelvin ratio threshold proves blowup",
    "support-bank rate proves continuation",
    "support-bank rate proves regularity",
    "bounded p q is proved uniformly",
    "P_nu is uniformly bounded at first bad time",
    "Q_tot is uniformly bounded at first bad time",
    "tau=Theta-t is the causal backward-Kelvin horizon",
    "fixed-past Kelvin horizon shrinks to zero at Theta",
    "support-bank rate is already a physical backward-Kelvin continuation theorem",
    "moving past terminal has no extra face",
    "support-bank scale and covariance horizon are identified",
    "smooth past vorticity proves Q_tot bounded",
    "fixed-past bank removes deformation growth",
    "R_s is centered covariance",
    "stochastic deformation is martingale q.v.",
    "selected material F equals stochastic Cauchy D",
    "stochastic Cauchy deformation is uniformly controlled",
    "same-replica packet metric proves first-bad alignment",
    "deterministic selected support equals stochastic replica support",
    "deterministic selected metric equals expected stochastic packet metric",
    "deformation dispersion is martingale q.v.",
    "h^3 deformation dispersion is S^int",
    "Sigma_D is S^int",
    "deformation covariance is the future remaining bank",
    "deformation covariance is the resolution covariance",
    "resolution covariance equals Sigma_D",
    "connected covariance theorem identifies the future clock",
    "pathwise D has Brownian q.v.",
    "shear dispersion closes first-bad alignment",
    "D alone closes finite Kelvin current",
    "deformation covariance is selector covariance",
    "deformation creates physical boundary seam",
    "selector-deformation cross pair terms can be dropped",
    "shape drift is quadratic variation",
    "D-K cross covariance is S^int",
    "joint covariance proves restart",
    "full current-shape state equals the programme ancestry state",
    "mixed covariance is the future remaining bank",
    "actual reverse-current area equals H_C",
    "descent error covariance proves local descent",
    "zero error covariance implies zero descent bias",
    "finite-shape error is S^int",
    "q.v. controls deterministic shape bias",
    "finite quadrupole closes descent",
    "first-bad shape collapse is proved",
    "finite moments close nonlinear material shape",
    "material centering is preserved by Navier-Stokes",
    "one anchor shift always centers oriented moments",
    "moment hierarchy proves first-bad support collapse",
    "scalar moment normalization proves locality",
    "codeforming tower constancy proves support locality",
    "support locality proves codeforming affine collapse",
    "rho^(p-1) alone controls nonaffinity",
    "codeforming nonaffinity proves restart",
    "large codeforming N implies large Kelvin descent error",
    "small Kelvin one-form controls full shape dynamics",
    "kinematic affine collapse is equivalent to Kelvin descent",
    "beta_L is S^int",
    "anchor derivative one-form is a new covariance bank",
    "codeforming error SDE proves restart",
    "finite reconstructed residual is pointwise vorticity defect",
    "whitened covariance defect equals residual covariance",
    "cross terms can be dropped after whitening",
    "metric whitening proves locality",
    "metric whitening proves restart",
    "same-time beta_L equals future epsilon_H",
    "beta_L is the future-bank remainder",
    "r_H is S^int",
    "r^2 whitened calibration proves first-bad collapse",
]:
    if forbidden in text or forbidden in active_text or forbidden in cycle_text or forbidden in hodge_text or forbidden in ck_text or forbidden in stochastic_text or forbidden in vorticity_text or forbidden in packet_text or forbidden in future_tensor_text or forbidden in shape_text or forbidden in time_text or forbidden in locality_text or forbidden in resolution_text or forbidden in clock_cut_text or forbidden in two_clock_text or forbidden in event_text or forbidden in candidate_text or forbidden in support_bank_text or forbidden in cauchy_text or forbidden in coupling_text or forbidden in full_shape_cov_text or forbidden in descent_text or forbidden in moment_text or forbidden in codeforming_text or forbidden in whitened_codeforming_text:
        print("forbidden overclaim found:", forbidden)
        sys.exit(1)
print("classification/anti-overclaim audit: PASS")
