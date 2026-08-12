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
]:
    if forbidden in text or forbidden in active_text or forbidden in cycle_text or forbidden in hodge_text or forbidden in ck_text or forbidden in stochastic_text or forbidden in vorticity_text or forbidden in packet_text or forbidden in future_tensor_text or forbidden in shape_text or forbidden in time_text or forbidden in locality_text or forbidden in resolution_text:
        print("forbidden overclaim found:", forbidden)
        sys.exit(1)
print("classification/anti-overclaim audit: PASS")
