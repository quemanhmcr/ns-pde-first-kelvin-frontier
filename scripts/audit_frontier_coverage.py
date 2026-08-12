"""Fail CI if a first-bad-germ seam has no explicit structural status."""
from __future__ import annotations

SEAMS = {
    "freeze": ("audited", "fixed-current Kelvin q.v./future-variance bank"),
    "quantile": ("audited-calibration", "one-particle conservation does not erase pair leakage"),
    "anchor-orientation": ("audited", "continuous covariance derivative + reset revaluation"),
    "shell": ("audited-calibration", "full product pair partition required"),
    "refinement": ("audited", "full tensor-square pair functor; cross-child covariance required"),
    "resolve-reset": ("audited", "observer jump has no q.v.; covariance revaluation is exact"),
    "physical-exit": ("audited-calibration", "two-face sub-Markov pair sink"),
    "variable-frame-connection": ("audited-generic", "Cartan/transport geometry audited; literal extra CK frame operator, if any, remains separate"),
    "active-pair-factorization": ("audited", "full pair boundary/transport residual is exact tensor lift of one-current commutator"),
    "parabolic-covariance-current": ("audited", "second-order Kelvin covariance is carried by the exact Dynkin/Fokker-Planck divergence current, not an ordinary de Rham one-form"),
    "moving-cut-time-face": ("audited-generic", "a moving restriction has G_Q=Qdot+T_out Q-Q T_in and one boundary-speed face per replica"),
    "reverse-age-kelvin-generator": ("audited", "for physical reverse age sigma with r=t-sigma, the full Kelvin forward Markov generator is exactly L_K,rev=-K^-_{t-sigma}"),
    "future-bank-clock-reversal": ("audited", "reversing a future-bank clock uses -b_+ and flips the covariance source sign; it is distinct from same-clock b_- diffusion reversal"),
    "future-bank-clock-reversed-state-map": ("audited-generic", "a clock-reversed state map satisfies K_K=DPi K DPi^T and B_K=Pi_sigma-DPi b_+-nu K:D2Pi"),
    "quantile-current-speed-law": ("audited-generic", "fixed-mass level sets move by the exact Reynolds/coarea weighted rate of g_t+j.grad g; in one dimension g=x gives adot=j"),
    "affine-reverse-quantile-support-gramian": ("audited-calibration", "exact linear-strain NS reverse-age Gaussian covariance is the time integral of reverse support Cauchy-Green geometry and Mahalanobis quantile shells are pointwise material for probability current"),
    "outer-time-cut-speed-underdetermination": ("audited-generic", "one-clock ancestry continuity does not determine arbitrary outer physical-time quantile motion"),
    "hysteretic-first-bad-event-structure": ("audited", "the literal M_fb selector is coordinate-piecewise-constant on unresolved intervals and changes by finite entry/resolve events with exact pair jump algebra"),
    "selector-vs-localization-cut-distinction": ("audited", "the rank-one hysteretic M_fb event selector and moving Q_s/H_s localization maps are distinct typed operations"),
    "first-bad-badness-functional-definition": ("open-literal", "bad_flags are Boolean oracle inputs; no Navier-Stokes badness score/threshold functional generates them"),
    "first-bad-resolve-predicate-definition": ("open-literal", "resolved is an independent Boolean oracle input; no Navier-Stokes resolve condition generates it"),
    "first-bad-quantile-observable-definition": ("open-literal", "the separate scalar/state observable whose level sets define the moving first-bad quantile/shell localization map is not written line by line"),
    "first-bad-moving-cut-speed-law": ("open-literal", "the generic current/coarea speed law is exact, but the first-bad observable and outer physical-time lift needed to instantiate Qdot/Hdot_shell are missing"),
    "two-clock-first-bad-kelvin-lift": ("open-literal", "the physical reverse-age Kelvin clock is exact, but the programme ancestry state and first-bad outer time have not been intertwined with that state family"),
    "cycle-typed-first-bad-boundary": ("audited", "closed Kelvin cycle library forces zero intrinsic selector physical boundary and pair boundary"),
    "cycle-typed-first-bad-transport": ("audited", "support transport is exact germ cut current; finite hysteresis switch is reset revaluation"),
    "hodge-cycle-projector": ("audited-generic", "idempotent closed-range projector has zero physical boundary and pure range/complement exchange motion"),
    "kelvin-ck-admissibility": ("audited", "arbitrary cycle-preserving linear/differentiable CK maps have zero intrinsic boundary; cycle breaking is gauge-visible physical boundary"),
    "stochastic-ck-carre-du-champ": ("audited-generic", "stochastic cycle motion contributes explicit martingale pair q.v.; finite-variation selector contribution is zero"),
    "vorticity-kelvin-microframe": ("audited", "three orthogonal infinitesimal closed-loop q.v. densities reconstruct nu|grad omega|^2 exactly"),
    "restart-scale-renormalization": ("audited", "raw small-loop q.v. scales like area^2; GL(3) packet metric gives the exact scale-normalized contraction and passive dilation cancels"),
    "orientation-complete-restart-packet": ("audited", "first-bad restart selector lifts as M_fb tensor I_3 and full cross-orientation covariance is retained"),
    "material-flux-metric-split": ("audited", "Nanson plus NS gives D_t(H^T omega)=nu H^T Delta omega while packet metric work is vortex stretching"),
    "future-covariance-full-state-tensor-law": ("audited", "vector conditional covariance gains the full mixed carre-du-champ while conditional mean-square loses it"),
    "codeforming-kelvin-tensor-transfer": ("audited", "eta=F^-1 omega has zero backward-Kelvin mean residual; eta eta^T loses and future covariance gains the same pulled-back Kelvin Gram tensor"),
    "resolved-future-total-second-moment": ("audited", "T_tot=omega omega^T+Sigma_fut has no net Kelvin-Gram source; viscosity/qv transfers internally and only total tensor strain remains locally"),
    "codeforming-support-normalized-total-bank": ("audited", "I_cof=(1/2)tr((F F^T)^-1 T_tot)=(1/2)tr Q_tot; common stretch cancels exactly after Kelvin qv already cancels internally"),
    "future-covariance-double-stokes": ("audited", "closed-loop future covariance is the double-Stokes localization of the existing pair momentum covariance cochain"),
    "future-covariance-fixed-state-stokes-limit": ("audited-conditional", "support locality plus metric-whitened conditional L2 control gives the fixed-state covariance tensor; centered local uniformly conditioned C2 packets have r^2 normalized remainder"),
    "kelvin-packet-support-locality": ("audited", "small area frame does not imply local support; isotropic incompressible material packets have exact line-scale diagnostic sqrt(det H)/sigma_min(H)"),
    "metric-whitened-local-tensor-topology": ("audited", "the invariant local remainder is H^-T epsilon in conditional L2 / tr(R(H^T H)^-1), not raw Frobenius smallness"),
    "joint-shape-flux-locality-factor": ("audited-conditional", "chi_H=sqrt(sum A_j^2)/sigma_min(H) controls both E_shape H^-1 and H^-T epsilon_flux against their physical local moduli"),
    "coherent-microcell-primal-dual-geometry": ("audited", "for coherent material microcells L=sqrt(det H)H^-T and L^T L=(det H)M_H, so support line geometry and packet metric are the same dual geometry"),
    "coherent-microcell-scale-anisotropy": ("audited", "G_line=rho^2 A and M_H=rho^-4 A; incompressible transport freezes rho while physical refinement changes scale and possibly anisotropy"),
    "centered-surface-quadrupole-carrier": ("audited", "the same centered surface second moment Q_Sigma is the first finite-size carrier for material shape drift and local Stokes flux error"),
    "material-refinement-two-sided-lineage": ("audited", "L_N=F_material L_0 R_refinement; incompressible material flow has det F=1, so scale determinant loss is carried only by physical refinement/reselection"),
    "exact-ns-refinement-strain-locality": ("audited-calibration", "exact linear NS strain u=(sx,0,-sz) plus isotropic refinement rho=e^-kappa t gives stretched line e^(s-kappa)t and realizes the critical long-thin packet at kappa=s"),
    "exact-ns-vortex-support-stretch-calibration": ("audited-calibration", "exact affine NS flow has positive vortex stretching with grad omega=0; vorticity dyad and support tensor stretch in the same direction and support-normalized contraction is constant"),
    "kelvin-parabolic-support-scale": ("audited-calibration", "remaining horizon tau supplies rho_nu=sqrt(2nu tau); exact singular affine NS strain a/tau gives parabolic support exponent 1/2-a"),
    "first-bad-parabolic-scale-identification": ("open", "no theorem or selector definition yet identifies the first-bad germ scale with the Kelvin diffusion length sqrt(2nu tau)"),
    "orientation-complete-quadrupole-closure": ("audited", "for a coherent three-face microcell sum_i Q_i/A_i=(2/3)LL^T, reconstructing full spatial support Cauchy-Green geometry"),
    "support-vorticity-common-stretch-operator": ("audited", "material support LL^T and vorticity dyad share A T+T A^T; co-deforming pullback cancels this stretch exactly and leaves only nonstretch sources"),
    "minimal-coherent-restart-core": ("audited", "ideal coherent packet factorizes as L=rho F, H=rho^2F^-T, Q_flux_raw=rho^4Q_tot, T_tot=FQ_totF^T; scale, deformation and total second moment have separate physical roles"),
    "packet-support-uniform-locality": ("open", "no proof that the first-bad material packet remains support-local and sufficiently conditioned as scale collapses near a candidate singular time"),
    "backward-kelvin-infinitesimal-generator": ("audited-calibration", "Nanson plus exact NS gives the backward-Ito packet mean operator; exact shear covariance transfers the Kelvin Gram tensor"),
    "backward-kelvin-full-shape-kinematics": ("audited", "uniform common Wiener motion acts only on the material anchor; relative current shape has finite-variation velocity-difference drift"),
    "finite-surface-xH-descent": ("audited-calibration", "exact smooth NS cubic heat shear gives identical anchor/area-vector states with different finite-surface H drift"),
    "finite-shape-quadrupole-descent": ("audited-calibration", "exact quintic NS heat shear gives positive surfaces with identical area and quadrupole but different finite-surface H drift"),
    "finite-shape-moment-hierarchy": ("audited", "Legendre P_2m plus exact heat shear U_2m+1 rules out every finite even surface-moment closure universally"),
    "infinitesimal-xH-descent": ("audited", "differential material area frames close exactly on anchor plus H by Nanson under uniform common noise"),
    "finite-shape-uniform-collapse": ("open", "centered finite-surface shape residual is r^2 relative at fixed smooth scale in calibration, but no uniform first-bad singular-time collapse is proved"),
    "ancestry-time-reversal-operator": ("audited", "weighted ancestry operator determines forward and backward Ito drifts exactly and j is their midpoint current velocity"),
    "ancestry-reference-gauge": ("audited", "phi,f,w are reference-gauge data; q,j,L,b_+,b_- are invariant under phi->e^g phi, f->e^-g f, w->w-nu K grad g"),
    "ancestry-noisy-shape-distribution": ("audited-generic", "zero-qv physical Kelvin shape must annihilate the ancestry noisy distribution; full-rank diffusion cannot encode nontrivial smooth shape on an open region"),
    "ancestry-state-manifold-definition": ("open-literal", "the full ancestry state coordinate/manifold y underlying P_{s,t} is not defined line by line in the repository"),
    "ancestry-deterministic-state-map-conditions": ("audited-generic", "a deterministic lift Pi must satisfy DPi K DPi^T=K_K and the backward-Ito drift pushforward equation"),
    "ancestry-resolution-kernel-covariance": ("audited", "a reduced ancestry lift kappa carries exact law-of-total-covariance resolution pair content, including cross-orientation terms"),
    "ancestry-resolution-dynamic-transfer": ("audited", "under horizon intertwining, H_red C_res=Gamma_red[Rm]-R Gamma_full[m] and C_red=R C_full+C_res keeps the reduced future-bank law exact"),
    "physical-anchor-conditional-shape-kernel": ("audited-generic", "for flat common-noise Kelvin state mu=q kappa, joint-minus-marginal Fokker-Planck gives conditional shape transport with exact backward anchor drift b_-=b_+-2nu grad log q"),
    "ancestry-anchor-identification": ("open-literal", "the repository has not identified its generic ancestry state y and density q with the physical Kelvin anchor marginal"),
    "ancestry-fullstate-density-singularity": ("audited-calibration", "exact affine NS shear with fixed shape gives rank-3 joint (X,R) law in dimension 6, so smooth full-state volume density is not universal"),
    "ancestry-state-semantics": ("open-literal", "the repository has not declared whether y is full physical Kelvin state or a reduced state with conditional lift kernel"),
    "ancestry-physical-kelvin-state-lift": ("open-literal", "after state semantics are declared, no programme-specific deterministic map or conditional kernel lift to the physical Kelvin state/payoff has been constructed"),
    "future-covariance-uniform-singular-limit": ("open", "fixed-state support-local whitened tensor existence is conditional-rigorous, but no uniform support/conditioning/whitened remainder control is proved near a candidate singular time"),
    "restart-capacity": ("open", "uniform tensor remainder plus material metric-stretching and physical boundary/exit work remain uncontrolled"),
    "active-ck-pillar-ii": ("open-literal", "selector and deterministic/stochastic admissible CK operation classes are classified; S^int itself or any independently intended Z_irr is not defined line by line"),
    "continuation-restart": ("open", "no regularity bridge claimed"),
}

ALLOWED = {"audited", "audited-calibration", "audited-generic", "audited-conditional", "open-literal", "open"}
required = {
    "freeze", "quantile", "anchor-orientation", "shell", "refinement",
    "resolve-reset", "physical-exit", "variable-frame-connection",
    "active-pair-factorization", "parabolic-covariance-current", "moving-cut-time-face", "reverse-age-kelvin-generator", "future-bank-clock-reversal", "future-bank-clock-reversed-state-map", "quantile-current-speed-law", "affine-reverse-quantile-support-gramian", "outer-time-cut-speed-underdetermination", "hysteretic-first-bad-event-structure", "selector-vs-localization-cut-distinction", "first-bad-badness-functional-definition", "first-bad-resolve-predicate-definition", "first-bad-quantile-observable-definition", "first-bad-moving-cut-speed-law", "two-clock-first-bad-kelvin-lift", "cycle-typed-first-bad-boundary",
    "cycle-typed-first-bad-transport", "hodge-cycle-projector", "kelvin-ck-admissibility",
    "stochastic-ck-carre-du-champ", "vorticity-kelvin-microframe",
    "restart-scale-renormalization", "orientation-complete-restart-packet",
    "material-flux-metric-split", "future-covariance-full-state-tensor-law", "codeforming-kelvin-tensor-transfer", "resolved-future-total-second-moment", "codeforming-support-normalized-total-bank",
    "future-covariance-double-stokes", "future-covariance-fixed-state-stokes-limit",
    "kelvin-packet-support-locality", "metric-whitened-local-tensor-topology", "joint-shape-flux-locality-factor", "coherent-microcell-primal-dual-geometry", "coherent-microcell-scale-anisotropy", "centered-surface-quadrupole-carrier", "material-refinement-two-sided-lineage", "exact-ns-refinement-strain-locality", "exact-ns-vortex-support-stretch-calibration", "kelvin-parabolic-support-scale", "first-bad-parabolic-scale-identification", "orientation-complete-quadrupole-closure", "support-vorticity-common-stretch-operator", "minimal-coherent-restart-core", "packet-support-uniform-locality",
    "backward-kelvin-infinitesimal-generator", "backward-kelvin-full-shape-kinematics",
    "finite-surface-xH-descent", "finite-shape-quadrupole-descent", "finite-shape-moment-hierarchy", "infinitesimal-xH-descent", "finite-shape-uniform-collapse",
    "ancestry-time-reversal-operator", "ancestry-reference-gauge", "ancestry-noisy-shape-distribution",
    "ancestry-state-manifold-definition", "ancestry-deterministic-state-map-conditions",
    "ancestry-resolution-kernel-covariance", "ancestry-resolution-dynamic-transfer", "physical-anchor-conditional-shape-kernel", "ancestry-anchor-identification", "ancestry-fullstate-density-singularity",
    "ancestry-state-semantics", "ancestry-physical-kelvin-state-lift", "future-covariance-uniform-singular-limit",
    "restart-capacity", "active-ck-pillar-ii", "continuation-restart",
}

if set(SEAMS) != required:
    raise SystemExit(f"frontier seam registry mismatch: {set(SEAMS) ^ required}")
for seam, (status, meaning) in SEAMS.items():
    if status not in ALLOWED or not meaning.strip():
        raise SystemExit(f"invalid seam classification: {seam}: {status}: {meaning!r}")

for exact_seam in (
    "active-pair-factorization",
    "parabolic-covariance-current",
    "reverse-age-kelvin-generator",
    "future-bank-clock-reversal",
    "hysteretic-first-bad-event-structure",
    "selector-vs-localization-cut-distinction",
    "cycle-typed-first-bad-boundary",
    "cycle-typed-first-bad-transport",
    "kelvin-ck-admissibility",
    "vorticity-kelvin-microframe",
    "restart-scale-renormalization",
    "orientation-complete-restart-packet",
    "material-flux-metric-split",
    "future-covariance-full-state-tensor-law",
    "codeforming-kelvin-tensor-transfer",
    "resolved-future-total-second-moment",
    "codeforming-support-normalized-total-bank",
    "future-covariance-double-stokes",
    "kelvin-packet-support-locality",
    "metric-whitened-local-tensor-topology",
    "coherent-microcell-primal-dual-geometry",
    "coherent-microcell-scale-anisotropy",
    "centered-surface-quadrupole-carrier",
    "material-refinement-two-sided-lineage",
    "orientation-complete-quadrupole-closure",
    "support-vorticity-common-stretch-operator",
    "minimal-coherent-restart-core",
    "backward-kelvin-full-shape-kinematics",
    "finite-shape-moment-hierarchy",
    "infinitesimal-xH-descent",
    "ancestry-time-reversal-operator",
    "ancestry-reference-gauge",
    "ancestry-resolution-kernel-covariance",
    "ancestry-resolution-dynamic-transfer",
):
    if SEAMS[exact_seam][0] != "audited":
        raise SystemExit(f"{exact_seam} must remain explicitly audited")
if SEAMS["moving-cut-time-face"][0] != "audited-generic":
    raise SystemExit("moving-cut time face must remain generic/audited until the literal first-bad cut is instantiated")
if SEAMS["future-bank-clock-reversed-state-map"][0] != "audited-generic":
    raise SystemExit("clock-reversed state-map equations are generic exact algebra, not a programme-specific state identification")
if SEAMS["quantile-current-speed-law"][0] != "audited-generic":
    raise SystemExit("quantile current/coarea speed law must remain generic/audited until the first-bad scalar observable is defined")
if SEAMS["affine-reverse-quantile-support-gramian"][0] != "audited-calibration":
    raise SystemExit("affine reverse quantile/support Gramian must remain an exact NS calibration, not a general first-bad shell theorem")
if SEAMS["outer-time-cut-speed-underdetermination"][0] != "audited-generic":
    raise SystemExit("outer-time cut-speed underdetermination must remain explicitly audited")
if SEAMS["first-bad-badness-functional-definition"][0] != "open-literal":
    raise SystemExit("first-bad badness score/threshold must remain open-literal until derived from NS")
if SEAMS["first-bad-resolve-predicate-definition"][0] != "open-literal":
    raise SystemExit("first-bad resolve predicate must remain open-literal until derived from NS")
if SEAMS["first-bad-quantile-observable-definition"][0] != "open-literal":
    raise SystemExit("first-bad quantile scalar observable/threshold geometry must remain open-literal")
if SEAMS["first-bad-moving-cut-speed-law"][0] != "open-literal":
    raise SystemExit("literal first-bad moving-cut speed law must remain open-literal")
if SEAMS["two-clock-first-bad-kelvin-lift"][0] != "open-literal":
    raise SystemExit("two-clock physical first-bad/Kelvin lift must remain open-literal")
if SEAMS["future-covariance-fixed-state-stokes-limit"][0] != "audited-conditional":
    raise SystemExit("fixed-state future-covariance Stokes limit must remain conditional on support locality and metric-whitened L2 control")
if SEAMS["joint-shape-flux-locality-factor"][0] != "audited-conditional":
    raise SystemExit("joint-shape-flux-locality-factor must remain a conditional rigorous estimate, not a closed singular-time theorem")
if SEAMS["backward-kelvin-infinitesimal-generator"][0] != "audited-calibration":
    raise SystemExit("backward-Kelvin infinitesimal generator must remain an exact/calibrated NS result")
if SEAMS["finite-surface-xH-descent"][0] != "audited-calibration":
    raise SystemExit("finite-surface (x,H) descent must remain recorded as false by exact NS calibration")
if SEAMS["finite-shape-uniform-collapse"][0] != "open":
    raise SystemExit("finite-shape singular-time collapse must remain open until the strain-gradient hierarchy is controlled")
if SEAMS["packet-support-uniform-locality"][0] != "open":
    raise SystemExit("first-bad packet support locality/conditioning must remain open until uniformly controlled")
if SEAMS["ancestry-noisy-shape-distribution"][0] != "audited-generic":
    raise SystemExit("ancestry noisy-shape distribution theorem must remain generic/audited")
if SEAMS["physical-anchor-conditional-shape-kernel"][0] != "audited-generic":
    raise SystemExit("physical-anchor-conditional-shape-kernel must remain a generic exact physical construction")
if SEAMS["ancestry-anchor-identification"][0] != "open-literal":
    raise SystemExit("ancestry-anchor-identification must remain open-literal until y=q state semantics are declared")
if SEAMS["ancestry-state-manifold-definition"][0] != "open-literal":
    raise SystemExit("ancestry state manifold must remain open-literal until y and its geometry are defined line by line")
if SEAMS["ancestry-deterministic-state-map-conditions"][0] != "audited-generic":
    raise SystemExit("deterministic ancestry state-map pushforward conditions must remain generic/audited")
if SEAMS["ancestry-fullstate-density-singularity"][0] != "audited-calibration":
    raise SystemExit("full-state smooth-density nonuniversality must remain an exact NS calibration result")
for seam in ("ancestry-state-semantics", "ancestry-physical-kelvin-state-lift"):
    if SEAMS[seam][0] != "open-literal":
        raise SystemExit(f"{seam} must remain open-literal until full-vs-reduced ancestry semantics and lift are defined")
if SEAMS["future-covariance-uniform-singular-limit"][0] != "open":
    raise SystemExit("uniform singular-time future-covariance trace/remainder control must remain open")
if SEAMS["active-ck-pillar-ii"][0] != "open-literal":
    raise SystemExit("global Pillar II must remain open-literal until S^int and any independently intended Z_irr are literally defined and audited")
if SEAMS["restart-capacity"][0] != "open":
    raise SystemExit("restart capacity must remain open until the metric-normalized future covariance remainder and material metric work are controlled")
if SEAMS["continuation-restart"][0] != "open":
    raise SystemExit("continuation/restart must remain open")

print("pair-localization frontier coverage: PASS")
for seam, (status, meaning) in SEAMS.items():
    print(f"{seam:40s} {status:20s} {meaning}")
