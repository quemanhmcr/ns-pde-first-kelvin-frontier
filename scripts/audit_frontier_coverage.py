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
    "naive-instantaneous-badness-threshold-no-go": ("audited-calibration", "arbitrary-amplitude smooth periodic ABC flow makes raw vorticity, enstrophy, stretching, Kelvin bulk qv, growth margin, and stretch/bulk ratio exceed every finite threshold, so none alone certifies continuation failure"),
    "abc-local-growth-gate-scope-check": ("audited", "for the full Beltrami ABC family omega.S.omega=u.grad e, so every enstrophy critical point has zero stretching; ABC cannot falsify the local-maximum necessary growth gate"),
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
    "support-bank-three-face-factorization": ("audited", "for arbitrary coherent scale ell, p q I-ell^2 omega omega^T splits exactly into support headroom, total-bank headroom, and pushed unresolved covariance"),
    "support-bank-causal-horizon-dichotomy": ("audited", "fixed-past backward-Kelvin horizon h=t-t0 grows while future candidate horizon tau=Theta-t shrinks; they are not the same clock for fixed t0"),
    "support-bank-moving-terminal-face": ("audited-calibration", "matching h=tau with t0(t)=2t-Theta is causal pointwise but adds the exact terminal-motion face 2 partial_t0; one-mode NS shear audits second moment and covariance laws"),
    "support-bank-terminal-local-rate": ("audited-conditional", "aligned same-state envelopes P_ell<=pI and Q_tot<=qI imply |omega|^2<=pq/ell^2; ell^2=2nu(Theta-t) gives a statewise integrable tau^-1/2 rate only conditionally"),
    "support-bank-scale-covariance-horizon-identification": ("open-literal", "the shrinking first-bad/future scale is not yet identified with a same-state causal or ancestry covariance family; moving-past matching has an explicit terminal face"),
    "support-bank-uniform-first-bad-envelope": ("open", "no theorem supplies uniform/global first-bad Loewner envelopes p,q or controls all nonideal finite-shape/localization/exit faces near a candidate singular time"),
    "stochastic-cauchy-fixed-past-envelope": ("audited", "for the fixed-past Cauchy payoff Y=D omega(A_s^t,s), omega omega^T<=Q_s<=W_s R_s and W_s R_s-omega omega^T splits into terminal directional headroom plus centered covariance"),
    "stochastic-cauchy-deformation-moment-law": ("audited", "reverse-age deformation satisfies D_sigma=D(grad u)^T and R_sigma=2 E[D S D^T]; incompressibility preserves pathwise det D but not deformation second moment"),
    "stochastic-cauchy-packet-metric-duality": ("audited", "on the same stochastic replica F_C=D^T and H_C=rho^2 F_C^-T give D D^T=rho^4 (H_C^T H_C)^-1, so Cauchy deformation Gram is the unscaled coherent packet metric"),
    "stochastic-cauchy-deformation-dispersion": ("audited", "full Sigma_D=Cov(vec D) has an exact two-replica form; C_D^Gram=E[D D^T]-Dbar Dbar^T is its column partial trace and rho^4 E[M_H]=Dbar Dbar^T+C_D^Gram"),
    "stochastic-cauchy-deformation-horizon-law": ("audited", "causal reverse-age conditioning gives H_h Dbar=A^T Dbar and H_h Sigma_D=(I tensor A^T)Sigma_D+Sigma_D(I tensor A)+Gamma_D^vec, distinct from pathwise D_sigma=D A^T"),
    "stochastic-cauchy-vectorized-short-horizon": ("audited-conditional", "for locally smooth NS, Sigma_D=(2nu/3)h^3 sum vec((partial_mu grad u)^T) outer itself+O(h^4), whose row-Gram projection is (2nu/3)h^3 sum (partial_mu grad u)^T(partial_mu grad u)+O(h^4)"),
    "stochastic-cauchy-shear-dispersion-calibration": ("audited-calibration", "exact one-mode NS shear solves mean, second-moment, full-vectorized and projected covariance horizon laws; Var(c_h) starts at (2nu/3)|partial_y U_y|^2 h^3"),
    "stochastic-cauchy-covariance-ledger-placement": ("audited", "reverse-age Sigma_D is an exact specialization of the existing connected vector covariance/pair-defect theorem; C_D^Gram is its projection, while an explicit reduced lift adds a separate Cov_R(Dbar_vec) resolution face"),
    "stochastic-cauchy-mechanism-calibration": ("audited-calibration", "genuine affine-vortex NS carries vorticity growth through deformation with zero centered covariance, while one-mode shear activates covariance with no vorticity-direction deformation"),
    "deterministic-selected-vs-stochastic-metric-naive-equality": ("audited-calibration", "false universally: exact one-mode NS shear at y=0 has deterministic selected metric I while the expected stochastic replica metric has a positive deformation-dispersion face"),
    "stochastic-cauchy-current-fiber-coupling": ("audited", "on a fixed selected current, Cauchy deformation acts on the spatial tangent fiber as P tensor D^T; chain boundary acts on the independent incidence factor, so closed cycles remain closed replica by replica and on the full pair boundary"),
    "stochastic-cauchy-local-cochain-projection": ("audited-conditional", "for fixed local tangent/cochain data, current and cochain deformation covariance is an exact linear projection L Sigma_D L^T; the short-horizon source retains coefficient 2nu/3 with literal orientation contractions"),
    "stochastic-cauchy-selected-pair-sector-split": ("audited", "two replica selected maps split pathwise into selector difference plus deformation difference; if both vary, their squared pair difference has mandatory selector-deformation cross pair terms; a shared frozen selector removes selector and cross sectors exactly"),
    "stochastic-cauchy-finite-current-D-descent": ("audited-calibration", "false universally: exact cubic NS heat shear has the same anchor, initial D, and area vector for two finite surfaces but different literal shape currents; D is exact local tangent transport, not a complete finite-current state"),
    "physical-current-shape-anchor-qv": ("audited", "on the literal reverse-age state (r,X,R,D), only the anchor X has Brownian covariance 2nu I; relative shape and Cauchy deformation are finite-variation coordinates"),
    "kelvin-moving-current-gauge-cartan": ("audited", "Navier-Stokes makes the moving momentum-one-form drift an exact Bernoulli/pressure gauge on closed currents, while constant-frame Cartan turns anchor translation into the literal Kelvin coefficient <i_e Omega,Z>"),
    "deformation-kelvin-cross-covariance": ("audited", "Cov(vec D,K_Z) is the exact off-diagonal block of the joint same-ancestor connected covariance theorem with source 2nu sum vec(partial_mu Dbar) partial_mu Kbar; it is not S^int or a new branching producer"),
    "deformation-kelvin-joint-short-horizon": ("audited-conditional", "for locally smooth NS the joint block has Kelvin variance O(h), deformation-Kelvin cross covariance O(h^2), deformation covariance O(h^3), with an exact leading Gram-integral representation"),
    "reverse-current-area-vs-cauchy-frame": ("audited", "actual reverse-current tangent/area have local connections -A and +A^T, while the Cauchy metric-dual frame H_C=rho^2 D^-1 has -A^T; the geometries are not directly identified"),
    "finite-shape-kelvin-descent-error-sde": ("audited", "epsilon_K=K_Z-omega(X).h_R is finite-support vorticity-inhomogeneity flux and obeys d epsilon=-omega.R_A dsigma+sqrt(2nu) sum q_mu^err dW_mu on the full reverse-age current-shape state"),
    "finite-shape-error-pathwise-vs-horizon-covariance": ("audited", "pathwise [vec D,epsilon_K]=0 because D is finite variation, while finite-horizon Cov(vec D,epsilon_K) is an ordinary anchor-carre-du-champ connected-covariance block"),
    "finite-shape-centered-quadrupole-jet": ("audited-conditional", "for a centered locally smooth surface, epsilon_K and R_A start on the oriented quadrupole M_kl=O(r^4), q_mu^err uses one higher vorticity derivative and the error qv rate is O(r^8)"),
    "finite-shape-cubic-covariance-blind-no-go": ("audited-calibration", "exact cubic heat-shear NS has epsilon_K=-4ab^3 nonzero and conserved while drift, qv, variance, and Cov(vec D,epsilon_K) vanish exactly, so covariance alone cannot force descent"),
    "finite-shape-one-mode-error-covariance": ("audited-calibration", "exact periodic one-mode NS activates the finite-shape error qv and D/error mixed horizon law with O(h), O(h^2), O(h^3) joint response hierarchy"),
    "finite-shape-abc-shape-drift": ("audited-calibration", "exact 3D ABC/Beltrami NS has nonzero -omega.R_A on a centered finite square, proving the finite-variation strain-shape drift face is physically active"),
    "finite-shape-moment-covariance-blindness": ("audited-calibration", "odd polynomial heat shears plus Legendre P_2m surfaces expose every next unresolved deterministic even-moment flux mode while the centered instantaneous error-qv coefficient can vanish"),
    "reverse-age-oriented-surface-moment-hierarchy": ("audited", "M_alpha=int r^alpha n dA obeys the exact reverse-age velocity-difference plus oriented-area transport law; relative shape carries no martingale source"),
    "affine-surface-moment-order-closure": ("audited", "for Delta u=A r, every order-m oriented moment evolves only through order-m moments; affine flow is exactly order preserving"),
    "nonlinear-surface-moment-order-raising": ("audited", "a homogeneous spatial velocity jet of degree p couples moment order m to m+p-1, so nonlinear material-surface transport is upward coupled"),
    "material-surface-centering-preservation": ("audited-calibration", "false universally: exact quadratic NS heat shear generates a transverse oriented first moment from a centered quadrupole"),
    "single-anchor-oriented-recentering": ("audited", "anchor shift gives F->F-c h^T, so generic vector-valued first moments cannot all be centered unless the rank-one compatibility F=c h^T holds"),
    "shear-hidden-oriented-moment-tower": ("audited", "for any x-shear and an xy surface normal e_z, every oriented y-moment is exactly conserved, providing a persistent hidden-shape channel"),
    "finite-moment-dynamic-shape-closure": ("audited-calibration", "false universally: exact polynomial NS heat shears realize arbitrarily high order-raising jets, complementing the static Legendre finite-moment no-go"),
    "first-bad-infinite-moment-jet-collapse": ("open-literal", "no theorem shows the actual migrating first-bad support controls the full normalized oriented moment tower uniformly enough to justify asymptotic local-jet descent"),
    "surface-moment-scalar-refinement-weight": ("audited", "order-m oriented surface moments carry the exact isotropic refinement weight m+2; scalar normalization removes scale but leaves unit-det shape action"),
    "codeforming-surface-moment-pullback": ("audited", "xi=L^-1 r and a_tilde=cof(L)^-1 a remove scalar scale and coherent affine anisotropy from the full oriented moment tower"),
    "codeforming-nonaffinity-reduction": ("audited", "with reverse local frame Ldot=-A0 L, the pulled-back surface is transported by the single divergence-free residual field N_L=L^-1[Delta u-A0 Lxi] and area source (Dxi N_L)^T"),
    "codeforming-generating-current-law": ("audited", "G_L(theta)=int exp(theta.xi)a_tilde packages every pulled-back oriented moment and obeys one exact N_L-driven current law"),
    "coherent-refinement-codeforming-gauge": ("audited", "when current and local frame undergo the same coherent linear refinement, every codeforming moment is exactly unchanged; noncoherent reset/reselection remains a separate physical face"),
    "codeforming-homogeneous-jet-scale-shape": ("audited", "a homogeneous degree-p nonaffine jet obeys N_{rho S}=rho^(p-1) S^-1 U_p(Sxi), so scalar scale and anisotropy conjugation are distinct exact faces"),
    "codeforming-constancy-vs-support-locality": ("audited-calibration", "exact critical linear-strain NS has a frozen codeforming tower while one physical line remains order one; codeforming constancy does not imply locality"),
    "support-locality-vs-codeforming-affinity": ("audited-calibration", "exact quadratic heat-shear NS on shrinking L=diag(r^3,r,r) has N_L=r^-1 xi_y^2 e_x, so support locality alone does not force codeforming affine collapse"),
    "first-bad-codeforming-nonaffinity-collapse": ("open-literal", "no theorem controls the dynamic current-shape residual N_L and D N_L together with actual support, selector, boundary, exit, and reset faces on the migrating first-bad current"),
    "codeforming-kelvin-nonaffinity-one-form": ("audited", "beta_L=(L^T L)N_L is the pulled-back physical residual momentum one-form; epsilon_K=oint beta_L.dxi and curl_xi beta_L=cof(L)^T delta omega exactly"),
    "codeforming-nonaffinity-three-face-split": ("audited", "one underlying N_L has distinct kinematic, area, and Kelvin faces: -N_L, (D N_L)^T, and (L^T L)N_L; they are related but not interchangeable"),
    "kinematic-vs-kelvin-nonaffinity-scaling": ("audited-calibration", "exact quadratic heat-shear with L=diag(r^3,r,r) has N_L=r^-1 xi_y^2 e_x while beta_L=r^5 xi_y^2 e_x, so divergent shape nonaffinity need not obstruct instantaneous Kelvin descent"),
    "first-bad-codeforming-kelvin-one-form-collapse": ("open-literal", "no theorem controls beta_L or cof(L)^T delta omega uniformly on the actual migrating first-bad current while retaining physical selector/boundary/exit/reset faces"),
    "codeforming-kelvin-anchor-noise": ("audited", "because anchor X is the only martingale coordinate, q_mu^err is exactly the closed-loop integral of partial_Xmu beta_L at fixed codeforming frame/shape"),
    "codeforming-finite-shape-error-sde": ("audited", "the physical descent-error SDE rewrites exactly as -eta0.htilde_dot dsigma plus sqrt(2nu) times anchor derivatives of beta_L; this is a representation, not a new bank"),
    "metric-whitened-pointwise-orientation-inversion": ("audited", "for common orientation density g=H^T delta zeta, H^-T g=delta zeta exactly; whitening is the inverse orientation map"),
    "metric-whitened-finite-face-reconstruction": ("audited", "r_H=H^-T epsilon_H is the physical vector reconstructed from three finite face residuals; because the components sample different faces it is not generally a pointwise defect"),
    "metric-whitened-codeforming-stokes-bridge": ("audited", "for the same-time NS current with H=cof(L), H^-T curl_xi beta_L=omega(X+Lxi)-omega(X) exactly"),
    "metric-whitened-homogeneous-exponent-ladder": ("audited", "degree-p nonaffinity has N~rho^(p-1), beta~rho^(p+1), and whitening removes the area rho^2 to recover the physical rho^(p-1) defect scale"),
    "metric-whitened-reconstruction-covariance": ("audited", "|r_H|^2 and Cov(r_H) are exactly the packet-metric energy and congruence H^-T C_epsilon H^-1"),
    "metric-whitened-reconstruction-qv": ("audited", "the whitened error qv is exactly the qv tensor of reconstructed anchor-noise coefficients H^-T q_mu"),
    "metric-whitened-local-residual-cross-blocks": ("audited", "Cov(zeta+r_H) contains residual covariance plus both mandatory local/residual cross blocks"),
    "cubic-finite-reconstruction-not-pointwise": ("audited-calibration", "exact cubic heat-shear NS on the unit cube has zero center vorticity defect but reconstructed finite residual -e_z/4"),
    "cubic-whitened-r2-calibration": ("audited-calibration", "under isotropic scale r the same exact cubic NS residual has raw face error -r^4 e_z/4 and reconstructed whitened residual -r^2 e_z/4"),
    "fixed-state-whitened-topology-physical-typing": ("audited", "the existing H^-T epsilon_H topology is now physically typed as finite orientation reconstruction on a fixed coherent state"),
    "codeforming-whitened-future-clock-identification": ("open-literal", "same-time beta_L gives the physical current remainder, but no theorem identifies it across clocks with the future-bank random remainder or programme ancestry lift"),
    "first-bad-reconstructed-kelvin-residual-collapse": ("open", "no uniform theorem makes the actual first-bad reconstructed residual H^-T epsilon_H vanish together with support locality and all selector/boundary/exit/reset faces"),
    "actual-area-vs-local-frame-kelvin-error": ("audited", "K-omega.h_R isolates actual-area vorticity inhomogeneity, while K-omega.h_local includes geometry mismatch; they are distinct exact observables"),
    "finite-shape-drift-geometry-transfer": ("audited", "the drift -omega.R_A of the actual-area error transfers exactly to +omega.R_A in omega.(h_R-h_local), and the Brownian coefficients transfer analogously"),
    "local-frame-kelvin-error-pure-martingale": ("audited", "closed-current Kelvin gauge and local Nanson/vorticity stretching cancellation give d epsilon=sqrt(2nu)(A_K-H^T grad omega)dW with zero finite-variation drift"),
    "dynamic-reconstructed-line-connection": ("audited", "Hdot=A^T H implies (H^-T)dot=-A H^-T, so W=H^-T K, omega, and r=W-omega share the reverse material-line connection -A"),
    "dynamic-reconstructed-residual-qv": ("audited", "r obeys dr=-A r dsigma+sqrt(2nu) Qhat dW and Gamma_r=2nu Qhat Qhat^T"),
    "dynamic-local-residual-cross-qv": ("audited", "the common anchor creates Gamma_omega,r=2nu grad(omega) Qhat^T, a signed mixed qv block"),
    "dynamic-reconstructed-dyad-energy": ("audited", "rr^T has drift -A rr^T-rr^T A^T+Gamma_r and |r|^2/2 has signed strain work -r.S.r plus positive qv injection"),
    "dynamic-full-reconstructed-cross-blocks": ("audited", "the qv and dyad laws of W=omega+r require local, residual, and both mixed local/residual blocks exactly"),
    "cubic-dynamic-reconstructed-conserved-mode": ("audited-calibration", "exact cubic heat-shear NS has r=-e_z/4 with A r=0 and Qhat=0 at the symmetry point, giving a nonzero conserved reconstructed residual"),
    "one-mode-dynamic-reconstructed-cross-qv": ("audited-calibration", "exact periodic one-mode shear has a pure e_z residual martingale and generically nonzero Gamma_omega,r"),
    "dynamic-reconstructed-reduced-covariance-closure": ("open-literal", "the full-state pathwise dyad law contains state correlations and finite-current noise; no autonomous centered covariance PDE on a reduced x/H or first-bad state is proved"),
    "dynamic-reconstructed-future-clock-identification": ("open-literal", "the dynamic residual law is same-clock reverse-age Kelvin and is not identified with a future-remaining bank or ancestry resolution residual"),
    "reverse-codeforming-volume-freeze": ("audited", "for Ldot=-A L, incompressibility gives det(L) constant; material deformation changes shape but not reference volume"),
    "reverse-codeforming-residual-triangle": ("audited", "with H=cof(L), chi=L^-1 r=epsilon/det(L), eta=L^-1 omega, and kappa=K/det(L)=eta+chi exactly"),
    "reverse-codeforming-local-martingale": ("audited", "eta=L^-1 omega has zero affine drift and noise L^-1 grad omega on the literal reverse-age state"),
    "reverse-codeforming-residual-martingale": ("audited", "chi=epsilon/J is driftless with noise Q/J because J is material-constant and local-frame epsilon is a pure Kelvin martingale"),
    "reverse-codeforming-joint-gram": ("audited", "the stacked eta/chi qv is one full Gram tensor with mandatory signed mixed block 2nu Gtilde Qtilde^T"),
    "reverse-codeforming-physical-metric-work": ("audited", "co-deforming chi energy has qv-only drift while pushforward r=L chi recovers signed physical strain exactly as frame/metric work"),
    "reverse-codeforming-bias-vs-spread": ("audited", "E chi is constant while centered covariance grows by expected residual qv under square-integrability; deterministic bias and stochastic spread are distinct"),
    "cubic-codeforming-bias-qv-blind": ("audited-calibration", "exact cubic heat shear has chi=-e_z/4 nonzero and constant with zero qv/covariance at the symmetry point"),
    "one-mode-full-period-cross-qv-cancellation": ("audited-calibration", "an exact one-mode face spanning a full y period has K_z=0 and chi_z=-eta_z, so negative cross qv cancels both positive diagonal qv terms exactly"),
    "reverse-codeforming-clock-sign": ("audited", "the reverse-age eta-dyad qv source is the opposite sign of the existing backward physical-time mean-dyad source for the same pulled-back Gram"),
    "first-bad-codeforming-bias-collapse": ("audited-calibration", "false as a necessary condition: exact quadratic NS has raw chi=-1 while the physical residual L chi tends to zero"),
    "first-bad-codeforming-spread-collapse": ("audited-calibration", "false as a necessary condition: exact one-mode NS can keep raw chi noise order one while the physical reconstructed noise L q_chi tends to zero"),
    "codeforming-physical-weighted-topology": ("audited", "the literal physical residual is r=L chi and |r|^2=chi^T L^T L chi"),
    "codeforming-fixed-frame-bias-spread": ("audited-conditional", "at fixed/conditioned line frame, E|r|^2=m_chi^T M_L m_chi+tr(C_chi M_L) exactly"),
    "codeforming-random-frame-residual-correlation": ("audited", "the full stochastic state has a mandatory signed metric-residual correlation; two replicas contribute one quarter tr(Delta M Delta Q)"),
    "quadratic-raw-codeforming-bias-no-go": ("audited-calibration", "exact quadratic heat shear has epsilon=-rho^3, chi=-1, but physical residual r=-rho e_z tends to zero"),
    "one-mode-raw-codeforming-spread-no-go": ("audited-calibration", "exact one-mode asymmetric face has q_chi -> -U_yyy/2 generically nonzero while rho q_chi ->0"),
    "first-bad-weighted-physical-residual-collapse": ("open", "no theorem proves E[chi^T L^T L chi] vanishes on the actual migrating first-bad packet with random-frame correlation and moving physical faces retained"),
    "directional-weighted-residual-decomposition": ("audited", "the weighted physical residual energy is the exact sum sigma_i^2 v_i^T Q_chi v_i over principal material-line directions"),
    "right-refinement-weighted-metric-law": ("audited", "literal repo refinement L_+=L_-R gives M_+=R^T M_- R; this is geometry and does not define Q_+"),
    "finite-weighted-residual-midpoint-revaluation": ("audited", "finite conditioned events split exactly into signed geometry tr(Qbar Delta M) plus current/residual tr(Delta Q Mbar) faces"),
    "random-frame-weighted-event-correlation-face": ("audited", "the full stochastic event adds the signed Delta C_MQ metric-residual correlation face"),
    "passive-gl-weighted-residual-gauge": ("audited", "passive GL inverse-congruence of Q cancels its nonzero geometry/state midpoint faces and leaves total physical energy unchanged"),
    "smooth-weighted-scale-shape-content-law": ("audited", "M=rho^2 A gives exact scale, anisotropy/metric, and residual/current-content product-rule faces"),
    "reverse-material-weighted-strain-qv-law": ("audited", "reverse material Ldot=-A L converts the weighted law exactly into signed physical strain work plus residual qv content"),
    "homogeneous-weighted-refinement-exponent": ("audited", "degree-p isotropic physical refinement gives M->lambda^2 M, Q->lambda^(2p-4)Q, E->lambda^(2p-2)E"),
    "weighted-residual-vs-support-locality": ("audited-calibration", "exact quadratic NS with L=diag(1,rho,rho) has weighted residual rho^2->0 while one physical support line stays length one"),
    "first-bad-directional-weighted-products": ("open", "no theorem controls every directional sigma_i^2 v_i^T Q_chi v_i together with support locality, random-frame correlation, and moving selected-current faces"),
    "pathwise-spectral-weighted-residual-channels": ("audited", "the random full-state weighted energy is exactly the expectation of pathwise spectral-block products lambda_alpha tr(P_alpha Q_chi)"),
    "weighted-collapse-spectral-channel-equivalence": ("audited", "nonnegative finite spectral channels imply weighted residual collapse iff every expected spectral-block channel collapses, with support locality separate"),
    "principal-simple-spectrum-connection": ("audited-conditional", "for distinct metric eigenvalues B=V^T Mdot V gives lambda_i_dot=B_ii and Omega_ij=B_ij/(lambda_j-lambda_i)"),
    "principal-channel-three-face-rate": ("audited-conditional", "each simple-spectrum channel rate is eigenvalue stretch plus residual/current content plus eigenframe mixing"),
    "principal-mixing-offdiagonal-metric-work": ("audited-conditional", "sum of eigenframe-mixing faces equals exactly 2 sum_{i<j} B_ij Qtilde_ij, the off-diagonal metric work"),
    "degenerate-eigenspace-projector-gauge": ("audited", "at repeated eigenvalues individual axes are gauge while lambda tr(PQ) is invariant under internal orthogonal basis rotations"),
    "linear-shear-principal-mixing-calibration": ("audited-calibration", "exact linear NS shear with anisotropic line frame activates nonzero eigenframe mixing equal to off-diagonal metric work"),
    "first-bad-principal-channel-collapse": ("open", "the spectral reformulation is exact but no theorem controls its nonnegative channel products on the actual first-bad packet together with support and event faces"),
    "selected-first-bad-spectral-factor-commutation": ("audited", "the diagonal rank-one M_fb tensor I_3 commutes with per-germ block-diagonal spectral fiber operators, including the full pair lift"),
    "generic-germ-mixing-spectral-scope": ("audited-generic", "a non-diagonal germ-mixing map need not commute with different per-germ spectral blocks; the first-bad commutation theorem is domain-specific"),
    "selected-endpoint-block-spectral-bank": ("audited", "the rank-one selected weighted energy is exactly the sum of spectral-projector channels of the selected germ block"),
    "physical-residual-linear-synthesis-pair-functor": ("audited", "once a common-fiber physical residual synthesis A is specified, Q_A=A Q_library A^T and vec(Q_A)=(A tensor A)vec(Q_library)"),
    "spectral-refinement-cross-child-content": ("audited", "every synthesized parent spectral channel contains the full ordered i,j child-pair sum; diagonal-only descendants drop physical cross-child content"),
    "selected-weighted-reset-pair-resolution": ("audited-conditional", "for a frozen/conditioned residual library, a finite selector reset is metric geometry plus left, right, and quadratic full-pair synthesis faces"),
    "one-mode-spectral-cross-child-cancellation": ("audited-calibration", "exact half-period one-mode NS finite residuals are opposite, so the full parent spectral channel vanishes while positive child diagonals are cancelled by cross-child content"),
    "one-mode-selected-reset-signed-revaluation": ("audited-calibration", "the same exact NS pair has zero endpoint reset energy while two negative linear pair faces cancel a positive quadratic reset face"),
    "selected-reset-positive-path-no-go": ("audited-calibration", "the exact NS closed selector excursion has positive accumulated quadratic reset path length but zero net energy revaluation after signed pair faces"),
    "cross-event-principal-axis-lineage": ("audited", "individual axis matching is noncanonical and unnecessary; the exact invariant replacement is signed projector-pair event transfer through the physical synthesis blocks"),
    "first-bad-physical-residual-refinement-lift": ("audited-conditional", "given an orientation-complete linear current packet map R_i, whitening/cofactor geometry uniquely forces A_i=H_P^-T R_i H_i^T and codeforming B_i=(J_i/J_P)R_i"),
    "selected-spectral-hybrid-same-clock-ledger": ("audited-conditional", "on frozen-selector simple-spectrum intervals the stretch/content/mixing law composes with exact finite reset faces; degeneracy uses projector blocks"),
    "first-bad-selected-spectral-lineage": ("open-literal", "badness/resolve predicates, moving cut time faces, actual orientation-packet refinement-map instantiation, support locality, and cross-clock ancestry remain missing from the literal selected lineage"),
    "orientation-packet-current-error-refinement": ("audited", "the same orientation-complete linear current blocks R_i act on circulation and oriented-area readouts, hence epsilon_P=sum_i R_i epsilon_i exactly"),
    "frame-aware-physical-residual-synthesis": ("audited", "whitening uniquely forces A_i=H_P^-T R_i H_i^T on reconstructed physical residuals"),
    "frame-aware-independent-orientation-gauge": ("audited", "under independent parent/child passive packet bases R_i transforms as S_P^T R_i S_i^-T and A_i is invariant"),
    "frame-aware-cofactor-line-conjugation": ("audited", "for H=cof L, A_i=(J_i/J_P)L_P R_i L_i^-1 exactly"),
    "frame-aware-codeforming-determinant-synthesis": ("audited", "the codeforming refinement block is B_i=L_P^-1 A_i L_i=(J_i/J_P)R_i, cancelling anisotropic line-frame conjugation"),
    "frame-aware-isotropic-area-volume-weights": ("audited", "isotropic physical reconstructed weights carry squared scale ratios while codeforming weights carry cubed/determinant ratios"),
    "quadratic-frame-aware-refinement-calibration": ("audited-calibration", "exact quadratic heat-shear packet synthesis gives area-weighted physical residual and volume-weighted codeforming residual, disproving naive unchanged scalar child weights"),
    "frame-aware-residual-pair-functor": ("audited", "frame-converted parent second moments and spectral channels retain the full ordered child-pair A tensor A or B tensor B content"),
    "first-bad-orientation-packet-refinement-instantiation": ("open-literal", "orientation-preserving scalar current refinement already lifts canonically, but the actual migrating first-bad event weights and any genuine orientation mixing/reselection blocks R_i are not yet specified"),
    "orientation-preserving-scalar-packet-refinement-lift": ("audited", "the existing scalar current refinement Z_P=sum_i w_i Z_i canonically lifts to packet blocks R_i=w_i I_3 and pair blocks w_i w_j I_9"),
    "orientation-complete-chain-refinement-lift": ("audited", "the exact scalar chain-map refinement B_f R1=R0 B_c remains exact after tensoring every chain space and map with I_3"),
    "spectral-projector-event-transfer": ("audited", "each parent spectral channel is exactly the signed sum lambda_P tr(P_P A_i P_i Q_ij P_j A_j^T) over all ordered child pairs and child projector blocks"),
    "spectral-event-transfer-sector-partition": ("audited", "same-child/same-channel, same-child/cross-channel, cross-child/same-index, and cross-child/cross-index sectors form an exact partition; none is dropped by the identity"),
    "spectral-event-frame-conversion-cross-channel": ("audited-generic", "a frame-aware finite synthesis block can route one child principal projector into a different parent projector, so equal spectral indices are not event ancestry"),
    "spectral-event-degenerate-projector-regularity": ("audited", "projector transfer contains no spectral-gap denominator and is invariant under internal basis changes of a degenerate projector block"),
    "one-mode-spectral-event-signed-cross-child": ("audited-calibration", "exact half-period one-mode NS has positive same-child channel traffic cancelled exactly by negative cross-child projector traffic"),
    "positive-child-channel-event-kernel-no-go": ("audited-calibration", "the exact signed event law cannot be replaced by the positive diagonal child-channel sum; exact one-mode NS activates the missing negative sector"),
    "selected-spectral-hybrid-projector-event-ledger": ("audited-conditional", "smooth stretch/content/mixing and degenerate projector blocks compose with frame-aware signed projector transfer at finite same-clock events"),
    "first-bad-spectral-event-transfer-instantiation": ("open-literal", "the projector transfer is exact once A_i and Q_ij are supplied, but the actual first-bad event map/state is not instantiated line by line"),
    "physical-event-gauge-normal-form": ("audited", "for invertible endpoint area frames the raw packet block R and physical residual block A=H_P^-T R H_C^T determine each other exactly; A is invariant under passive packet bases"),
    "codeforming-event-volume-normal-form": ("audited", "with coherent invertible line frames B=(J_C/J_P)R and R=(J_P/J_C)B exactly"),
    "frame-aware-event-composition": ("audited", "sequential physical residual maps compose as A_PC=A_PM A_MC and the intermediate area frame cancels exactly"),
    "codeforming-event-composition": ("audited", "sequential codeforming maps compose and the intermediate determinant cancels exactly"),
    "event-second-moment-composition": ("audited", "Q maps functorially under sequential rectangular event maps: A2(A1 Q A1^T)A2^T=(A2A1)Q(A2A1)^T"),
    "event-pair-functor-composition": ("audited", "tensor-square event maps compose exactly: (A2 tensor A2)(A1 tensor A1)=(A2A1) tensor (A2A1)"),
    "intermediate-projector-telescope": ("audited", "a complete intermediate spectral projector resolution can be inserted and summed out exactly in a composite event channel"),
    "intermediate-degenerate-basis-telescope": ("audited", "internal rank-one bases of an intermediate repeated-eigenvalue block give the same fully summed composite transfer"),
    "scalar-channel-event-compositional-closure": ("audited-calibration", "false universally: two PSD second moments with identical diagonal projector channels but opposite cross coherence give different parent channels under the same event map"),
    "full-second-moment-linear-event-observational-completeness": ("audited-conditional", "for the unrestricted linear event-probe class, coordinate and pair-sum quadratic probes reconstruct every symmetric second-moment entry exactly by polarization; actual first-bad probe reachability is not claimed"),
    "specified-linear-packet-event-normal-form": ("audited", "specified same-clock finite linear packet events reduce modulo passive orientation gauge to physical A maps whose pair lifts and intermediate projector resolutions are functorial"),
    "first-bad-event-normal-form-instantiation": ("open-literal", "the event algebra is closed once maps/states are supplied, but Navier-Stokes first-bad predicates and the actual event map/state sequence are not instantiated"),
    "first-bad-selected-residual-readout": ("audited", "the active residual is the germ extraction E_g X from a persistent germ/fiber library"),
    "selector-switch-selected-state-factorization": ("audited-calibration", "false universally for distinct germs: no T satisfies E_h=T E_g on the full library; the new-germ identity block is an unavoidable obstruction"),
    "selector-switch-state-nonclosure": ("audited-calibration", "two full library states can share the old selected residual and differ after a genuine selector switch"),
    "selector-second-moment-full-pair-jump": ("audited", "Q_h-Q_g equals DeltaE Q E_g^T + E_g Q DeltaE^T + DeltaE Q DeltaE^T exactly"),
    "selector-reset-hidden-germ-blocks": ("audited", "for a two-germ switch the left/right/quadratic faces expose Q10-Q00, Q01-Q00, and Q11-Q10-Q01+Q00"),
    "selector-switch-selected-second-moment-nonclosure": ("audited-calibration", "two PSD full-library second moments can share Q_gg and have different switched Q_hh"),
    "selector-switch-admissible-subspace-factorization": ("audited-conditional", "a selected-to-selected transition exists on an explicitly supplied admissible subspace S only when E_h S=T E_g S"),
    "physical-event-plus-selector-factorization": ("audited-generic", "the literal post-event readout is E_post A_full; factorization through the old selected residual requires E_post A_full=T E_pre and fails generically under genuine selector switches"),
    "persistent-library-selected-observer-architecture": ("audited", "arbitrary hysteretic selector switches require a persistent candidate library/full pair state plus an active readout; selected endpoint state alone is not universally compositional"),
    "first-bad-persistent-library-dynamics": ("audited-conditional", "for any specified finite physical packet library carried in one stochastic-flow replica, the stacked codeforming residual dynamics and full common-noise Gram are exact; actual first-bad library instantiation remains separate"),
    "same-replica-residual-library-common-noise": ("audited", "stacking finite codeforming packet residuals in one stochastic-flow replica gives dChi=sqrt(2nu) Qstack dW with the same three-dimensional W for every germ"),
    "same-replica-residual-library-qv-gram": ("audited", "the full library qv is one Gram 2nu Qstack Qstack^T with ordered cross-germ block 2nu Q_g Q_h^T"),
    "same-replica-residual-library-qv-rank": ("audited", "the instantaneous same-replica library qv image has rank at most the three-dimensional common Wiener driver"),
    "same-replica-selector-qv-readout": ("audited", "a frozen germ selector reads the corresponding diagonal block E_g Gamma E_g^T=2nu Q_g Q_g^T without creating a new Brownian source"),
    "same-replica-event-qv-functor": ("audited", "a specified linear physical event A sends Qstack to A Qstack and Gamma to A Gamma A^T exactly"),
    "same-replica-library-bias-spread": ("audited-conditional", "under square-integrability the stacked martingale mean is constant and centered covariance grows by the expected full same-replica qv Gram"),
    "independent-per-germ-noise-model-distinction": ("audited", "assigning independent Brownian drivers per germ deletes the physical same-replica cross-germ qv blocks and is a different stochastic model"),
    "one-mode-same-replica-cross-qv-cancellation": ("audited-calibration", "exact one-mode NS packets in one replica have opposite residual noise coefficients, negative cross-germ qv, and zero synthesized common-noise qv while the independent-noise model is positive"),
    "first-bad-candidate-library-instantiation": ("open-literal", "the actual first-bad candidate packet library, anchors/shapes/frames, and whether its members share the required physical stochastic replica are not instantiated line by line"),
    "first-bad-library-clock-replica-identification": ("open-literal", "no theorem identifies the conditional same-replica residual library law with the programme's intended first-bad outer clock or future-bank/ancestry state"),
    "selected-residual-frozen-interval-martingale": ("audited", "on a frozen selector branch Y=E_g Chi obeys dY=sqrt(2nu) E_g Qstack dW and its continuous qv is E_g Gamma_lib E_g^T"),
    "selector-readout-finite-jump": ("audited", "at a selector-only event with continuous library state DeltaY=(E_+-E_-)Chi exactly"),
    "selector-fv-zero-continuous-qv-vs-jump-qv": ("audited", "finite-variation selector motion creates no continuous Brownian carre-du-champ source, while the cadlag selected path has jump square DeltaY DeltaY^T in optional quadratic variation"),
    "selector-jump-dyad-three-face": ("audited", "the selected dyad jump is DeltaY Y_-^T + Y_- DeltaY^T + DeltaY DeltaY^T, matching left/right/quadratic reset faces"),
    "selected-hybrid-semimartingale-law": ("audited-conditional", "given a same-replica library and specified piecewise-constant selector path, selected optional qv is the active continuous Gram integral plus finite selector jump squares"),
    "selector-jump-qv-bank-no-go": ("audited-calibration", "a closed selector excursion can have zero net selected-state change but strictly positive accumulated jump-square, so jump qv is not a monotone physical state bank"),
    "one-mode-selector-optional-qv-closed-excursion": ("audited-calibration", "exact half-period one-mode NS realizes a closed 0->1->0 selector excursion with positive jump optional qv and zero net residual change"),
    "selector-jump-qv-vs-reset-covariance": ("audited", "the jump square is only the quadratic reset face; signed left/right and mean revaluation prevent replacing the full reset covariance ledger by jump qv alone"),
    "first-bad-selected-hybrid-path-instantiation": ("open-literal", "the hybrid law including specified simultaneous linear packet/selector events is exact, but NS badness/resolve timing and the actual event map/state are not instantiated"),
    "combined-selected-post-event-readout": ("audited", "a simultaneous finite event reads the post-event library as C=E_+ A, distinct from both physical transport A and selector extraction E_+"),
    "combined-selected-jump-operator": ("audited", "the exact selected jump operator is D=E_+ A-E_- on the pre-event persistent library"),
    "combined-event-discrete-product-rule": ("audited", "on a common library D=E_- DeltaA+DeltaE+DeltaE DeltaA=E_- DeltaA+DeltaE A=DeltaE+E_+ DeltaA"),
    "combined-event-physical-selector-mixed-face": ("audited", "DeltaE DeltaA is the mandatory finite interaction between physical library change and selector readout change; it is not Brownian qv"),
    "combined-event-second-moment-full-pair-jump": ("audited", "the selected second-moment jump is D Q E_-^T+E_- Q D^T+D Q D^T with the combined event operator D"),
    "combined-event-jump-square-typing": ("audited", "pathwise jump optional qv is only D X X^T D^T, the quadratic face, not the full signed second-moment revaluation"),
    "one-mode-combined-event-mixed-face": ("audited-calibration", "exact one-mode NS residuals under a specified hidden-germ current synthesis activate a nonzero physical-selector mixed face"),
    "naive-additive-physical-selector-event-no-go": ("audited-calibration", "exact one-mode NS payload shows physical-old plus selector-old faces alone give the wrong simultaneous selected jump"),
    "selected-hybrid-with-simultaneous-linear-events": ("audited-conditional", "for supplied same-replica library, selector path, and specified finite linear packet events, continuous and combined finite selected path algebra is exact"),
    "first-bad-simultaneous-event-instantiation": ("open-literal", "Navier-Stokes badness/resolve timing and the actual first-bad physical packet event map/state remain unspecified"),
    "combined-selected-continuous-noise-readout": ("audited", "pre/post selected Brownian responses are B_-=E_- N and B_+=E_+ A N on the common same-replica noise response"),
    "combined-selected-continuous-qv-rate": ("audited", "adjacent frozen-interval continuous qv rates are the PSD Grams 2nu B_-B_-^T and 2nu B_+B_+^T"),
    "combined-continuous-qv-rate-full-pair-revaluation": ("audited", "with dB=(E_+A-E_-)N, the signed rate change is 2nu[dB B_-^T+B_- dB^T+dB dB^T] and retains full cross-germ pair content"),
    "signed-qv-rate-revaluation-typing": ("audited", "the difference of two PSD continuous qv rates is a signed event revaluation, not negative Brownian carre-du-champ production"),
    "continuous-qv-rate-vs-jump-qv-independence": ("audited", "continuous source-rate revaluation depends on the noise response while jump optional qv depends on the state jump; exact witnesses show either may vanish without the other"),
    "one-mode-hidden-event-continuous-qv-cancellation": ("audited-calibration", "exact one-mode NS opposite same-replica noises plus hidden-germ synthesis cancel the actual post-event selected Brownian response to zero"),
    "selector-only-qv-rate-hidden-event-no-go": ("audited-calibration", "for the same exact NS payload selector-only qv rate is unchanged, while the actual combined event removes the continuous source entirely"),
    "selected-hybrid-source-jump-ledger": ("audited-conditional", "for supplied same-clock library/event/selector data, continuous source, state jump, jump qv atom, source-rate revaluation, and second-moment revaluation are separately exact"),
    "first-bad-hybrid-source-event-instantiation": ("open-literal", "actual first-bad library, badness/resolve timing, physical event maps, and clock/replica identification remain unspecified"),
    "adaptive-selected-event-mean-correlation": ("audited", "two-replica mean selected output is Cbar xbar+(1/4)DeltaC Deltax, so state-dependent event choice has an exact mean correlation face"),
    "adaptive-selected-event-congruence-four-face": ("audited", "two-replica E[C Q C^T] splits exactly into mean-map/mean-payload, event-map dispersion, and two signed event-state correlation faces"),
    "adaptive-event-map-dispersion-face": ("audited", "for PSD mean payload the event-map dispersion (1/4)DeltaC Qbar DeltaC^T is PSD"),
    "adaptive-event-state-correlation-faces": ("audited", "the left/right DeltaQ-DeltaC faces are signed and can reinforce or cancel both naive and dispersion contributions"),
    "mean-event-map-mean-payload-closure": ("audited-calibration", "false universally: PSD adaptive-event replicas with the same mean map/payload give exact values 4 or 0 while the naive mean-map face is 1"),
    "adaptive-event-alignment-correlation-sign": ("audited-calibration", "PSD aligned calibration gives 1+1+1+1=4 while anti-aligned gives 1+1-1-1=0"),
    "adaptive-event-qv-gram-congruence": ("audited", "the same random congruence law applies to same-replica continuous qv Gram payloads"),
    "selected-adaptive-event-expectation-ledger": ("audited-conditional", "once replica-wise physical event maps and payloads are supplied, expectation-level event dispersion/correlation algebra is exact"),
    "first-bad-adaptive-event-joint-law": ("open-literal", "the actual first-bad badness/resolve rule, adaptive map distribution, event-state joint law, and outer clock remain unspecified"),
    "first-bad-physical-score-passive-gauge": ("audited", "physical reconstructed residual r=H^-T epsilon and |r|^2 are invariant under passive packet GL(3) basis changes"),
    "raw-first-bad-score-passive-gauge-no-go": ("audited-calibration", "raw residual norm and ranking are observer-coordinate dependent; a passive basis change flips the raw worst-germ index with no physical change"),
    "first-bad-event-map-passive-gauge-equivariance": ("audited", "raw packet event blocks must transform equivariantly so the physical event map A=H_p^-T R H_c^T remains invariant"),
    "first-bad-physical-residual-vs-support-locality": ("audited-calibration", "exact quadratic NS has gauge-correct physical residual energy rho^2->0 while one support line remains length one"),
    "first-bad-persistent-library-memory-necessity": ("audited", "genuine hysteretic switches are not universally compositional from the old selected endpoint or selected second moment alone"),
    "first-bad-full-coherence-event-memory-necessity": ("audited-calibration", "identical diagonal spectral channels with opposite cross coherence give different later linear-event response"),
    "first-bad-adaptive-joint-law-necessity": ("audited", "state-dependent event choice requires event-map/state joint correlation faces; mean event map times mean payload is not an identity"),
    "first-bad-rule-physical-admissibility-ledger": ("audited", "packet gauge, event gauge, support separation, persistent-library memory, full coherence, and adaptive joint law are necessary typing constraints only"),
    "first-bad-badness-resolve-functional-after-admissibility": ("open-literal", "no Navier-Stokes badness/resolve functional satisfying the necessary physical constraints has been defined or proved sufficient"),
    "local-enstrophy-balance-vorticity-contraction": ("audited", "the local enstrophy balance residual is exactly omega contracted with the vorticity-equation residual"),
    "kelvin-bulk-enstrophy-dissipation-identification": ("audited", "metric-normalized orientation-complete Kelvin loop qv equals nu|grad omega|_F^2 exactly"),
    "local-enstrophy-critical-three-face-law": ("audited", "at grad e=0 the time rate splits exactly into vortex stretching minus Kelvin qv bulk plus nu Delta e curvature diffusion"),
    "local-max-growth-gate-curvature-necessity": ("audited", "at a local maximum positive stretching-minus-Kelvin-bulk is necessary but not sufficient; it must also exceed -nu Delta e"),
    "abc-beltrami-critical-stretching-zero": ("audited", "global ABC Beltrami identity omega.S.omega=u.grad e forces zero stretching at every enstrophy critical point"),
    "affine-vortex-positive-local-growth-gate": ("audited-calibration", "exact affine NS has uniform enstrophy, zero Kelvin bulk, positive stretching 8 a r(t)^2, and exact positive time growth"),
    "affine-vortex-growth-gate-target-scope": ("audited-calibration", "the affine mechanism is nonperiodic/non-finite-energy, so it calibrates local growth but does not refute a target-class global criterion"),
    "first-bad-local-growth-to-continuation-bridge": ("open-literal", "no theorem turns the exact local growth three-face law plus packet/support/event structure into continuation failure"),
    "moving-enstrophy-critical-constraint-speed": ("audited-conditional", "on a differentiable nondegenerate critical branch, H_e xdot_*+partial_t grad e=0 and xdot_*=-H_e^-1 partial_t grad e"),
    "moving-enstrophy-critical-pde-relative-speed": ("audited-conditional", "at grad e=0, H_e(xdot_*-u)+grad[stretching-Kelvin_bulk+nu Delta e]=0"),
    "moving-enstrophy-critical-three-gradient-faces": ("audited-conditional", "relative critical speed splits through H_e^-1 into stretching-gradient, Kelvin-bulk-gradient, and curvature-gradient faces"),
    "moving-enstrophy-critical-value-speed-independence": ("audited", "along any critical path the first value derivative is partial_t e because grad e=0"),
    "abc-fixed-enstrophy-maximum-vs-fluid-transport": ("audited-calibration", "exact periodic ABC has a strict nondegenerate maximum fixed in space while the local fluid velocity is nonzero"),
    "affine-degenerate-critical-speed-nonuniqueness": ("audited-calibration", "exact affine uniform enstrophy has H_e=0 and distinct critical-path velocities satisfying the same speed constraint"),
    "critical-hessian-inversion-theorem-domain": ("audited", "inverse-Hessian critical speed is canonical only off Hessian degeneracy; singular Hessian is explicitly rejected"),
    "first-bad-enstrophy-critical-path-identification": ("open-literal", "the programme first-bad observable is not identified with a differentiable nondegenerate enstrophy-max branch or its creation/loss events"),
    "critical-hessian-evolution-three-face": ("audited-conditional", "on a differentiable critical branch Hdot=Hess(R)-(grad u)^T H-H grad u+((xdot_*-u).grad)H"),
    "critical-hessian-connection-strain-rotation-split": ("audited", "the local connection splits exactly into strain reshaping -(S H+H S) and rotation commutator W H-H W"),
    "incompressible-critical-hessian-connection-logdet-cancellation": ("audited", "connection logdet rate is -2 div u; incompressibility erases curvature-volume rate but not Hessian reshaping"),
    "critical-hessian-strain-rotation-logdet-split": ("audited", "rotation commutator has zero logdet rate and strain has -2 tr S, hence both curvature-volume rates vanish in incompressible flow"),
    "critical-hessian-incompressible-curvature-volume-law": ("audited-conditional", "on a nondegenerate incompressible critical branch only growth-Hessian and relative-transport faces remain in d log|det H|/dt"),
    "critical-hessian-jacobi-logdet-law": ("audited-conditional", "for invertible H, detdot=det(H) tr(H^-1 Hdot) and det H follows the exact exponential integrated lograte law"),
    "critical-branch-finite-lograte-nondegeneracy": ("audited-conditional", "on a smooth nondegenerate branch a finite limiting integrated lograte prevents continuous determinant collapse; det H->0 requires lograte integral -> -infinity"),
    "abc-critical-hessian-logdet-calibration": ("audited-calibration", "exact periodic ABC strict maximum has Hdot=-2nu H, logdet rate -6nu, nonzero determinant at finite time, and zero connection logdet face"),
    "critical-hessian-logdet-degeneracy-domain": ("audited", "inverse-Hessian/logdet formulas stop at det H=0; branch creation/loss/merger is a separate geometry event seam"),
    "first-bad-critical-branch-degeneracy-identification": ("open-literal", "no theorem identifies critical-Hessian degeneracy or branch loss with the programme first-bad selector/event or continuation failure"),
    "reverse-codeforming-future-bank-identification": ("open-literal", "the same-clock co-deforming martingale core is not identified with the future conditional covariance bank or ancestry state"),
    "first-bad-full-shape-local-descent": ("open-literal", "the exact descent-error SDE is now known, but no theorem controls deterministic bias, strain-shape drift, vorticity-gradient residual, metric-whitened covariance remainder, and actual support locality uniformly on the migrating first-bad current"),
    "selected-support-cauchy-deformation-alignment": ("open-literal", "the full physical current-shape source and deformation-Kelvin cross law are now exact, but programme-specific ancestry identification and first-bad finite-shape-to-local descent remain unresolved"),
    "stochastic-cauchy-uniform-deformation-control": ("open", "no uniform first-bad/global bound controls the stochastic Cauchy deformation second moment or the sharper directional headroom near a candidate singular time"),
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
    "ancestry-resolution-kernel-covariance": ("audited", "a reduced ancestry lift kappa carries exact vector law-of-total-covariance resolution pair content, including cross-orientation terms, additional to averaged intrinsic full-state covariance"),
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
    "active-pair-factorization", "parabolic-covariance-current", "moving-cut-time-face", "reverse-age-kelvin-generator", "future-bank-clock-reversal", "future-bank-clock-reversed-state-map", "quantile-current-speed-law", "affine-reverse-quantile-support-gramian", "outer-time-cut-speed-underdetermination", "hysteretic-first-bad-event-structure", "selector-vs-localization-cut-distinction", "first-bad-badness-functional-definition", "first-bad-resolve-predicate-definition", "naive-instantaneous-badness-threshold-no-go", "abc-local-growth-gate-scope-check", "first-bad-quantile-observable-definition", "first-bad-moving-cut-speed-law", "two-clock-first-bad-kelvin-lift", "cycle-typed-first-bad-boundary",
    "cycle-typed-first-bad-transport", "hodge-cycle-projector", "kelvin-ck-admissibility",
    "stochastic-ck-carre-du-champ", "vorticity-kelvin-microframe",
    "restart-scale-renormalization", "orientation-complete-restart-packet",
    "material-flux-metric-split", "future-covariance-full-state-tensor-law", "codeforming-kelvin-tensor-transfer", "resolved-future-total-second-moment", "codeforming-support-normalized-total-bank",
    "future-covariance-double-stokes", "future-covariance-fixed-state-stokes-limit",
    "kelvin-packet-support-locality", "metric-whitened-local-tensor-topology", "joint-shape-flux-locality-factor", "coherent-microcell-primal-dual-geometry", "coherent-microcell-scale-anisotropy", "centered-surface-quadrupole-carrier", "material-refinement-two-sided-lineage", "exact-ns-refinement-strain-locality", "exact-ns-vortex-support-stretch-calibration", "kelvin-parabolic-support-scale", "first-bad-parabolic-scale-identification", "orientation-complete-quadrupole-closure", "support-vorticity-common-stretch-operator", "minimal-coherent-restart-core", "support-bank-three-face-factorization", "support-bank-causal-horizon-dichotomy", "support-bank-moving-terminal-face", "support-bank-terminal-local-rate", "support-bank-scale-covariance-horizon-identification", "support-bank-uniform-first-bad-envelope", "stochastic-cauchy-fixed-past-envelope", "stochastic-cauchy-deformation-moment-law", "stochastic-cauchy-packet-metric-duality", "stochastic-cauchy-deformation-dispersion", "stochastic-cauchy-deformation-horizon-law", "stochastic-cauchy-vectorized-short-horizon", "stochastic-cauchy-shear-dispersion-calibration", "stochastic-cauchy-covariance-ledger-placement", "stochastic-cauchy-mechanism-calibration", "deterministic-selected-vs-stochastic-metric-naive-equality", "stochastic-cauchy-current-fiber-coupling", "stochastic-cauchy-local-cochain-projection", "stochastic-cauchy-selected-pair-sector-split", "stochastic-cauchy-finite-current-D-descent", "physical-current-shape-anchor-qv", "kelvin-moving-current-gauge-cartan", "deformation-kelvin-cross-covariance", "deformation-kelvin-joint-short-horizon", "reverse-current-area-vs-cauchy-frame", "finite-shape-kelvin-descent-error-sde", "finite-shape-error-pathwise-vs-horizon-covariance", "finite-shape-centered-quadrupole-jet", "finite-shape-cubic-covariance-blind-no-go", "finite-shape-one-mode-error-covariance", "finite-shape-abc-shape-drift", "finite-shape-moment-covariance-blindness", "reverse-age-oriented-surface-moment-hierarchy", "affine-surface-moment-order-closure", "nonlinear-surface-moment-order-raising", "material-surface-centering-preservation", "single-anchor-oriented-recentering", "shear-hidden-oriented-moment-tower", "finite-moment-dynamic-shape-closure", "first-bad-infinite-moment-jet-collapse", "surface-moment-scalar-refinement-weight", "codeforming-surface-moment-pullback", "codeforming-nonaffinity-reduction", "codeforming-generating-current-law", "coherent-refinement-codeforming-gauge", "codeforming-homogeneous-jet-scale-shape", "codeforming-constancy-vs-support-locality", "support-locality-vs-codeforming-affinity", "first-bad-codeforming-nonaffinity-collapse", "codeforming-kelvin-nonaffinity-one-form", "codeforming-nonaffinity-three-face-split", "kinematic-vs-kelvin-nonaffinity-scaling", "first-bad-codeforming-kelvin-one-form-collapse", "codeforming-kelvin-anchor-noise", "codeforming-finite-shape-error-sde", "metric-whitened-pointwise-orientation-inversion", "metric-whitened-finite-face-reconstruction", "metric-whitened-codeforming-stokes-bridge", "metric-whitened-homogeneous-exponent-ladder", "metric-whitened-reconstruction-covariance", "metric-whitened-reconstruction-qv", "metric-whitened-local-residual-cross-blocks", "cubic-finite-reconstruction-not-pointwise", "cubic-whitened-r2-calibration", "fixed-state-whitened-topology-physical-typing", "codeforming-whitened-future-clock-identification", "first-bad-reconstructed-kelvin-residual-collapse", "actual-area-vs-local-frame-kelvin-error", "finite-shape-drift-geometry-transfer", "local-frame-kelvin-error-pure-martingale", "dynamic-reconstructed-line-connection", "dynamic-reconstructed-residual-qv", "dynamic-local-residual-cross-qv", "dynamic-reconstructed-dyad-energy", "dynamic-full-reconstructed-cross-blocks", "cubic-dynamic-reconstructed-conserved-mode", "one-mode-dynamic-reconstructed-cross-qv", "dynamic-reconstructed-reduced-covariance-closure", "dynamic-reconstructed-future-clock-identification", "reverse-codeforming-volume-freeze", "reverse-codeforming-residual-triangle", "reverse-codeforming-local-martingale", "reverse-codeforming-residual-martingale", "reverse-codeforming-joint-gram", "reverse-codeforming-physical-metric-work", "reverse-codeforming-bias-vs-spread", "cubic-codeforming-bias-qv-blind", "one-mode-full-period-cross-qv-cancellation", "reverse-codeforming-clock-sign", "first-bad-codeforming-bias-collapse", "first-bad-codeforming-spread-collapse", "codeforming-physical-weighted-topology", "codeforming-fixed-frame-bias-spread", "codeforming-random-frame-residual-correlation", "quadratic-raw-codeforming-bias-no-go", "one-mode-raw-codeforming-spread-no-go", "first-bad-weighted-physical-residual-collapse", "directional-weighted-residual-decomposition", "right-refinement-weighted-metric-law", "finite-weighted-residual-midpoint-revaluation", "random-frame-weighted-event-correlation-face", "passive-gl-weighted-residual-gauge", "smooth-weighted-scale-shape-content-law", "reverse-material-weighted-strain-qv-law", "homogeneous-weighted-refinement-exponent", "weighted-residual-vs-support-locality", "first-bad-directional-weighted-products", "pathwise-spectral-weighted-residual-channels", "weighted-collapse-spectral-channel-equivalence", "principal-simple-spectrum-connection", "principal-channel-three-face-rate", "principal-mixing-offdiagonal-metric-work", "degenerate-eigenspace-projector-gauge", "linear-shear-principal-mixing-calibration", "first-bad-principal-channel-collapse", "selected-first-bad-spectral-factor-commutation", "generic-germ-mixing-spectral-scope", "selected-endpoint-block-spectral-bank", "physical-residual-linear-synthesis-pair-functor", "spectral-refinement-cross-child-content", "selected-weighted-reset-pair-resolution", "one-mode-spectral-cross-child-cancellation", "one-mode-selected-reset-signed-revaluation", "selected-reset-positive-path-no-go", "cross-event-principal-axis-lineage", "first-bad-physical-residual-refinement-lift", "selected-spectral-hybrid-same-clock-ledger", "first-bad-selected-spectral-lineage", "orientation-packet-current-error-refinement", "frame-aware-physical-residual-synthesis", "frame-aware-independent-orientation-gauge", "frame-aware-cofactor-line-conjugation", "frame-aware-codeforming-determinant-synthesis", "frame-aware-isotropic-area-volume-weights", "quadratic-frame-aware-refinement-calibration", "frame-aware-residual-pair-functor", "first-bad-orientation-packet-refinement-instantiation", "orientation-preserving-scalar-packet-refinement-lift", "orientation-complete-chain-refinement-lift", "spectral-projector-event-transfer", "spectral-event-transfer-sector-partition", "spectral-event-frame-conversion-cross-channel", "spectral-event-degenerate-projector-regularity", "one-mode-spectral-event-signed-cross-child", "positive-child-channel-event-kernel-no-go", "selected-spectral-hybrid-projector-event-ledger", "first-bad-spectral-event-transfer-instantiation", "physical-event-gauge-normal-form", "codeforming-event-volume-normal-form", "frame-aware-event-composition", "codeforming-event-composition", "event-second-moment-composition", "event-pair-functor-composition", "intermediate-projector-telescope", "intermediate-degenerate-basis-telescope", "scalar-channel-event-compositional-closure", "full-second-moment-linear-event-observational-completeness", "specified-linear-packet-event-normal-form", "first-bad-event-normal-form-instantiation", "first-bad-selected-residual-readout", "selector-switch-selected-state-factorization", "selector-switch-state-nonclosure", "selector-second-moment-full-pair-jump", "selector-reset-hidden-germ-blocks", "selector-switch-selected-second-moment-nonclosure", "selector-switch-admissible-subspace-factorization", "physical-event-plus-selector-factorization", "persistent-library-selected-observer-architecture", "first-bad-persistent-library-dynamics", "same-replica-residual-library-common-noise", "same-replica-residual-library-qv-gram", "same-replica-residual-library-qv-rank", "same-replica-selector-qv-readout", "same-replica-event-qv-functor", "same-replica-library-bias-spread", "independent-per-germ-noise-model-distinction", "one-mode-same-replica-cross-qv-cancellation", "first-bad-candidate-library-instantiation", "first-bad-library-clock-replica-identification", "selected-residual-frozen-interval-martingale", "selector-readout-finite-jump", "selector-fv-zero-continuous-qv-vs-jump-qv", "selector-jump-dyad-three-face", "selected-hybrid-semimartingale-law", "selector-jump-qv-bank-no-go", "one-mode-selector-optional-qv-closed-excursion", "selector-jump-qv-vs-reset-covariance", "first-bad-selected-hybrid-path-instantiation", "combined-selected-post-event-readout", "combined-selected-jump-operator", "combined-event-discrete-product-rule", "combined-event-physical-selector-mixed-face", "combined-event-second-moment-full-pair-jump", "combined-event-jump-square-typing", "one-mode-combined-event-mixed-face", "naive-additive-physical-selector-event-no-go", "selected-hybrid-with-simultaneous-linear-events", "first-bad-simultaneous-event-instantiation", "combined-selected-continuous-noise-readout", "combined-selected-continuous-qv-rate", "combined-continuous-qv-rate-full-pair-revaluation", "signed-qv-rate-revaluation-typing", "continuous-qv-rate-vs-jump-qv-independence", "one-mode-hidden-event-continuous-qv-cancellation", "selector-only-qv-rate-hidden-event-no-go", "selected-hybrid-source-jump-ledger", "first-bad-hybrid-source-event-instantiation", "adaptive-selected-event-mean-correlation", "adaptive-selected-event-congruence-four-face", "adaptive-event-map-dispersion-face", "adaptive-event-state-correlation-faces", "mean-event-map-mean-payload-closure", "adaptive-event-alignment-correlation-sign", "adaptive-event-qv-gram-congruence", "selected-adaptive-event-expectation-ledger", "first-bad-adaptive-event-joint-law", "first-bad-physical-score-passive-gauge", "raw-first-bad-score-passive-gauge-no-go", "first-bad-event-map-passive-gauge-equivariance", "first-bad-physical-residual-vs-support-locality", "first-bad-persistent-library-memory-necessity", "first-bad-full-coherence-event-memory-necessity", "first-bad-adaptive-joint-law-necessity", "first-bad-rule-physical-admissibility-ledger", "first-bad-badness-resolve-functional-after-admissibility", "local-enstrophy-balance-vorticity-contraction", "kelvin-bulk-enstrophy-dissipation-identification", "local-enstrophy-critical-three-face-law", "local-max-growth-gate-curvature-necessity", "abc-beltrami-critical-stretching-zero", "affine-vortex-positive-local-growth-gate", "affine-vortex-growth-gate-target-scope", "first-bad-local-growth-to-continuation-bridge", "moving-enstrophy-critical-constraint-speed", "moving-enstrophy-critical-pde-relative-speed", "moving-enstrophy-critical-three-gradient-faces", "moving-enstrophy-critical-value-speed-independence", "abc-fixed-enstrophy-maximum-vs-fluid-transport", "affine-degenerate-critical-speed-nonuniqueness", "critical-hessian-inversion-theorem-domain", "first-bad-enstrophy-critical-path-identification", "critical-hessian-evolution-three-face", "critical-hessian-connection-strain-rotation-split", "incompressible-critical-hessian-connection-logdet-cancellation", "critical-hessian-strain-rotation-logdet-split", "critical-hessian-incompressible-curvature-volume-law", "critical-hessian-jacobi-logdet-law", "critical-branch-finite-lograte-nondegeneracy", "abc-critical-hessian-logdet-calibration", "critical-hessian-logdet-degeneracy-domain", "first-bad-critical-branch-degeneracy-identification", "reverse-codeforming-future-bank-identification", "first-bad-full-shape-local-descent", "selected-support-cauchy-deformation-alignment", "stochastic-cauchy-uniform-deformation-control", "packet-support-uniform-locality",
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
    "support-bank-three-face-factorization",
    "support-bank-causal-horizon-dichotomy",
    "stochastic-cauchy-fixed-past-envelope",
    "stochastic-cauchy-deformation-moment-law",
    "stochastic-cauchy-packet-metric-duality",
    "stochastic-cauchy-deformation-dispersion",
    "stochastic-cauchy-deformation-horizon-law",
    "stochastic-cauchy-covariance-ledger-placement",
    "physical-current-shape-anchor-qv",
    "kelvin-moving-current-gauge-cartan",
    "deformation-kelvin-cross-covariance",
    "reverse-current-area-vs-cauchy-frame",
    "finite-shape-kelvin-descent-error-sde",
    "finite-shape-error-pathwise-vs-horizon-covariance",
    "reverse-age-oriented-surface-moment-hierarchy",
    "affine-surface-moment-order-closure",
    "nonlinear-surface-moment-order-raising",
    "single-anchor-oriented-recentering",
    "shear-hidden-oriented-moment-tower",
    "backward-kelvin-full-shape-kinematics",
    "finite-shape-moment-hierarchy",
    "surface-moment-scalar-refinement-weight",
    "codeforming-surface-moment-pullback",
    "codeforming-nonaffinity-reduction",
    "codeforming-generating-current-law",
    "coherent-refinement-codeforming-gauge",
    "codeforming-homogeneous-jet-scale-shape",
    "codeforming-kelvin-nonaffinity-one-form",
    "codeforming-nonaffinity-three-face-split",
    "codeforming-kelvin-anchor-noise",
    "codeforming-finite-shape-error-sde",
    "metric-whitened-pointwise-orientation-inversion",
    "metric-whitened-finite-face-reconstruction",
    "metric-whitened-codeforming-stokes-bridge",
    "metric-whitened-homogeneous-exponent-ladder",
    "metric-whitened-reconstruction-covariance",
    "metric-whitened-reconstruction-qv",
    "metric-whitened-local-residual-cross-blocks",
    "fixed-state-whitened-topology-physical-typing",
    "actual-area-vs-local-frame-kelvin-error",
    "finite-shape-drift-geometry-transfer",
    "local-frame-kelvin-error-pure-martingale",
    "dynamic-reconstructed-line-connection",
    "dynamic-reconstructed-residual-qv",
    "dynamic-local-residual-cross-qv",
    "dynamic-reconstructed-dyad-energy",
    "dynamic-full-reconstructed-cross-blocks",
    "reverse-codeforming-volume-freeze",
    "reverse-codeforming-residual-triangle",
    "reverse-codeforming-local-martingale",
    "reverse-codeforming-residual-martingale",
    "reverse-codeforming-joint-gram",
    "reverse-codeforming-physical-metric-work",
    "reverse-codeforming-bias-vs-spread",
    "reverse-codeforming-clock-sign",
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
if SEAMS["naive-instantaneous-badness-threshold-no-go"][0] != "audited-calibration":
    raise SystemExit("naive instantaneous badness threshold no-go must remain an exact NS calibration")
if SEAMS["abc-local-growth-gate-scope-check"][0] != "audited":
    raise SystemExit("ABC local-growth gate scope check must remain an exact Beltrami theorem-domain statement and must not falsify the local-max gate")
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
if SEAMS["support-bank-moving-terminal-face"][0] != "audited-calibration":
    raise SystemExit("moving-terminal support-bank face must remain an exact NS calibration, not a free horizon identification")
if SEAMS["support-bank-terminal-local-rate"][0] != "audited-conditional":
    raise SystemExit("support-bank terminal rate must remain conditional on same-scale/state Loewner envelopes")
if SEAMS["support-bank-scale-covariance-horizon-identification"][0] != "open-literal":
    raise SystemExit("support-bank shrinking-scale/covariance horizon identification must remain open-literal")
if SEAMS["support-bank-uniform-first-bad-envelope"][0] != "open":
    raise SystemExit("uniform/global support-bank first-bad envelope must remain open")
if SEAMS["stochastic-cauchy-vectorized-short-horizon"][0] != "audited-conditional":
    raise SystemExit("general h^3 deformation covariance asymptotic must remain local-smooth conditional, not a singular-frontier theorem")
if SEAMS["stochastic-cauchy-shear-dispersion-calibration"][0] != "audited-calibration":
    raise SystemExit("stochastic Cauchy shear deformation-dispersion must remain an exact NS calibration")
if SEAMS["deterministic-selected-vs-stochastic-metric-naive-equality"][0] != "audited-calibration":
    raise SystemExit("naive deterministic selected = expected stochastic metric must remain recorded as false by exact NS calibration")
if SEAMS["stochastic-cauchy-mechanism-calibration"][0] != "audited-calibration":
    raise SystemExit("stochastic Cauchy mechanism split must remain an exact NS calibration pair")
if SEAMS["stochastic-cauchy-current-fiber-coupling"][0] != "audited":
    raise SystemExit("Cauchy/current spatial-fiber boundary coupling must remain an exact audited identity")
if SEAMS["stochastic-cauchy-local-cochain-projection"][0] != "audited-conditional":
    raise SystemExit("local cochain h^3 projection must remain conditional on locally smooth NS coefficients")
if SEAMS["stochastic-cauchy-selected-pair-sector-split"][0] != "audited":
    raise SystemExit("selected/deformation pair-sector split and its cross tensor-lift terms must remain exact audited algebra")
if SEAMS["stochastic-cauchy-finite-current-D-descent"][0] != "audited-calibration":
    raise SystemExit("D-only finite-current descent must remain recorded as false by exact NS calibration")
if SEAMS["deformation-kelvin-joint-short-horizon"][0] != "audited-conditional":
    raise SystemExit("joint h/h^2/h^3 deformation-Kelvin law must remain conditional on locally smooth NS coefficients")
if SEAMS["material-surface-centering-preservation"][0] != "audited-calibration":
    raise SystemExit("material centering failure must remain an exact NS calibration, not a universal geometry assertion")
if SEAMS["finite-moment-dynamic-shape-closure"][0] != "audited-calibration":
    raise SystemExit("finite-moment dynamic closure no-go must remain tied to exact NS polynomial calibrations")
if SEAMS["first-bad-infinite-moment-jet-collapse"][0] != "open-literal":
    raise SystemExit("full first-bad moment-tower collapse must remain open-literal")
if SEAMS["codeforming-constancy-vs-support-locality"][0] != "audited-calibration":
    raise SystemExit("codeforming constancy/locality separation must remain an exact-NS calibration")
if SEAMS["support-locality-vs-codeforming-affinity"][0] != "audited-calibration":
    raise SystemExit("support-locality/codeforming-affinity separation must remain an exact-NS calibration")
if SEAMS["first-bad-codeforming-nonaffinity-collapse"][0] != "open-literal":
    raise SystemExit("first-bad codeforming nonaffinity collapse must remain open-literal")
if SEAMS["kinematic-vs-kelvin-nonaffinity-scaling"][0] != "audited-calibration":
    raise SystemExit("kinematic/Kelvin nonaffinity scaling separation must remain an exact-NS calibration")
if SEAMS["first-bad-codeforming-kelvin-one-form-collapse"][0] != "open-literal":
    raise SystemExit("first-bad codeforming Kelvin one-form collapse must remain open-literal")
if SEAMS["cubic-finite-reconstruction-not-pointwise"][0] != "audited-calibration":
    raise SystemExit("finite reconstructed residual / pointwise defect separation must remain exact-NS calibrated")
if SEAMS["cubic-whitened-r2-calibration"][0] != "audited-calibration":
    raise SystemExit("cubic whitened r2 onset must remain an exact-NS calibration")
if SEAMS["codeforming-whitened-future-clock-identification"][0] != "open-literal":
    raise SystemExit("same-time codeforming remainder / future-clock identification must remain open-literal")
if SEAMS["first-bad-reconstructed-kelvin-residual-collapse"][0] != "open":
    raise SystemExit("uniform first-bad reconstructed Kelvin residual collapse must remain open")
if SEAMS["cubic-dynamic-reconstructed-conserved-mode"][0] != "audited-calibration":
    raise SystemExit("cubic dynamic reconstructed conserved mode must remain an exact-NS calibration")
if SEAMS["one-mode-dynamic-reconstructed-cross-qv"][0] != "audited-calibration":
    raise SystemExit("one-mode dynamic local/residual cross qv must remain an exact-NS calibration")
if SEAMS["dynamic-reconstructed-reduced-covariance-closure"][0] != "open-literal":
    raise SystemExit("reduced dynamic reconstructed covariance closure must remain open-literal")
if SEAMS["dynamic-reconstructed-future-clock-identification"][0] != "open-literal":
    raise SystemExit("dynamic reconstructed future-clock identification must remain open-literal")
if SEAMS["cubic-codeforming-bias-qv-blind"][0] != "audited-calibration":
    raise SystemExit("cubic co-deforming bias/qv blindness must remain exact-NS calibrated")
if SEAMS["one-mode-full-period-cross-qv-cancellation"][0] != "audited-calibration":
    raise SystemExit("one-mode full-period cross-qv cancellation must remain exact-NS calibrated")
if SEAMS["first-bad-codeforming-bias-collapse"][0] != "audited-calibration":
    raise SystemExit("raw co-deforming mean-bias collapse must remain recorded as unnecessary by exact quadratic NS calibration")
if SEAMS["first-bad-codeforming-spread-collapse"][0] != "audited-calibration":
    raise SystemExit("raw co-deforming spread collapse must remain recorded as unnecessary by exact one-mode NS calibration")
if SEAMS["codeforming-physical-weighted-topology"][0] != "audited":
    raise SystemExit("physical r=L chi weighted topology must remain an exact audited identity")
if SEAMS["codeforming-fixed-frame-bias-spread"][0] != "audited-conditional":
    raise SystemExit("weighted bias/spread split must remain fixed-frame/conditional, not a random-frame factorization")
if SEAMS["codeforming-random-frame-residual-correlation"][0] != "audited":
    raise SystemExit("random-frame metric/residual correlation must remain an exact full-state pair face")
if SEAMS["quadratic-raw-codeforming-bias-no-go"][0] != "audited-calibration":
    raise SystemExit("quadratic raw-bias target correction must remain exact-NS calibrated")
if SEAMS["one-mode-raw-codeforming-spread-no-go"][0] != "audited-calibration":
    raise SystemExit("one-mode raw-spread target correction must remain exact-NS calibrated")
if SEAMS["first-bad-weighted-physical-residual-collapse"][0] != "open":
    raise SystemExit("first-bad weighted physical residual collapse must remain open")
if SEAMS["directional-weighted-residual-decomposition"][0] != "audited":
    raise SystemExit("directional weighted residual decomposition must remain exact audited algebra")
if SEAMS["right-refinement-weighted-metric-law"][0] != "audited":
    raise SystemExit("right-refinement weighted metric congruence must remain exact audited geometry")
if SEAMS["finite-weighted-residual-midpoint-revaluation"][0] != "audited":
    raise SystemExit("finite weighted midpoint revaluation must remain exact audited algebra")
if SEAMS["random-frame-weighted-event-correlation-face"][0] != "audited":
    raise SystemExit("random-frame weighted event correlation must remain an exact third face")
if SEAMS["passive-gl-weighted-residual-gauge"][0] != "audited":
    raise SystemExit("passive GL weighted residual law must remain an exact gauge identity")
if SEAMS["smooth-weighted-scale-shape-content-law"][0] != "audited":
    raise SystemExit("smooth weighted scale/shape/content law must remain exact")
if SEAMS["reverse-material-weighted-strain-qv-law"][0] != "audited":
    raise SystemExit("reverse material weighted strain/qv law must remain exact")
if SEAMS["homogeneous-weighted-refinement-exponent"][0] != "audited":
    raise SystemExit("homogeneous weighted refinement exponent must remain exact")
if SEAMS["weighted-residual-vs-support-locality"][0] != "audited-calibration":
    raise SystemExit("weighted residual/support locality separation must remain exact-NS calibrated")
if SEAMS["first-bad-directional-weighted-products"][0] != "open":
    raise SystemExit("first-bad directional weighted products must remain open")
if SEAMS["pathwise-spectral-weighted-residual-channels"][0] != "audited":
    raise SystemExit("pathwise spectral weighted residual channels must remain exact audited algebra")
if SEAMS["weighted-collapse-spectral-channel-equivalence"][0] != "audited":
    raise SystemExit("spectral-channel collapse equivalence must remain an exact nonnegative finite-sum consequence")
if SEAMS["principal-simple-spectrum-connection"][0] != "audited-conditional":
    raise SystemExit("principal connection must remain explicitly conditional on simple spectrum")
if SEAMS["principal-channel-three-face-rate"][0] != "audited-conditional":
    raise SystemExit("principal channel rate law must remain simple-spectrum conditional")
if SEAMS["principal-mixing-offdiagonal-metric-work"][0] != "audited-conditional":
    raise SystemExit("principal mixing/off-diagonal work identity must remain simple-spectrum conditional")
if SEAMS["degenerate-eigenspace-projector-gauge"][0] != "audited":
    raise SystemExit("degenerate eigenspace projector gauge law must remain exact audited algebra")
if SEAMS["linear-shear-principal-mixing-calibration"][0] != "audited-calibration":
    raise SystemExit("linear-shear principal mixing must remain exact-NS calibrated")
if SEAMS["first-bad-principal-channel-collapse"][0] != "open":
    raise SystemExit("first-bad principal channel collapse must remain open")
if SEAMS["selected-first-bad-spectral-factor-commutation"][0] != "audited":
    raise SystemExit("literal first-bad selector/spectral factor commutation must remain exact audited algebra")
if SEAMS["generic-germ-mixing-spectral-scope"][0] != "audited-generic":
    raise SystemExit("generic germ mixing must remain outside the first-bad spectral commutation theorem")
for seam in ("selected-endpoint-block-spectral-bank", "physical-residual-linear-synthesis-pair-functor", "spectral-refinement-cross-child-content"):
    if SEAMS[seam][0] != "audited":
        raise SystemExit(f"{seam} must remain exact audited algebra")
if SEAMS["selected-weighted-reset-pair-resolution"][0] != "audited-conditional":
    raise SystemExit("weighted selector reset resolution must remain conditional on the specified frozen/conditioned library state")
for seam in ("one-mode-spectral-cross-child-cancellation", "one-mode-selected-reset-signed-revaluation", "selected-reset-positive-path-no-go"):
    if SEAMS[seam][0] != "audited-calibration":
        raise SystemExit(f"{seam} must remain an exact NS calibration/no-go")
if SEAMS["selected-spectral-hybrid-same-clock-ledger"][0] != "audited-conditional":
    raise SystemExit("selected spectral hybrid ledger must remain a same-clock conditional composition, not a completed first-bad theorem")
if SEAMS["first-bad-physical-residual-refinement-lift"][0] != "audited-conditional":
    raise SystemExit("frame-aware physical residual lift must remain conditional on an explicitly supplied orientation-complete current packet map")
for seam in ("orientation-packet-current-error-refinement", "frame-aware-physical-residual-synthesis", "frame-aware-independent-orientation-gauge", "frame-aware-cofactor-line-conjugation", "frame-aware-codeforming-determinant-synthesis", "frame-aware-isotropic-area-volume-weights", "frame-aware-residual-pair-functor"):
    if SEAMS[seam][0] != "audited":
        raise SystemExit(f"{seam} must remain exact audited algebra")
for seam in ("orientation-preserving-scalar-packet-refinement-lift", "orientation-complete-chain-refinement-lift"):
    if SEAMS[seam][0] != "audited":
        raise SystemExit(f"{seam} must remain the exact packet lift of the existing scalar refinement class")
if SEAMS["quadratic-frame-aware-refinement-calibration"][0] != "audited-calibration":
    raise SystemExit("quadratic frame-aware packet refinement must remain an exact NS calibration")
if SEAMS["cross-event-principal-axis-lineage"][0] != "audited":
    raise SystemExit("individual cross-event principal-axis matching must remain recorded as a noncanonical target replaced by exact projector transfer")
for seam in ("spectral-projector-event-transfer", "spectral-event-transfer-sector-partition", "spectral-event-degenerate-projector-regularity"):
    if SEAMS[seam][0] != "audited":
        raise SystemExit(f"{seam} must remain exact audited projector algebra")
if SEAMS["spectral-event-frame-conversion-cross-channel"][0] != "audited-generic":
    raise SystemExit("finite frame-conversion cross-channel traffic must remain an audited generic mechanism")
for seam in ("one-mode-spectral-event-signed-cross-child", "positive-child-channel-event-kernel-no-go"):
    if SEAMS[seam][0] != "audited-calibration":
        raise SystemExit(f"{seam} must remain tied to the exact one-mode NS calibration")
for seam in ("physical-event-gauge-normal-form", "codeforming-event-volume-normal-form", "frame-aware-event-composition", "codeforming-event-composition", "event-second-moment-composition", "event-pair-functor-composition", "intermediate-projector-telescope", "intermediate-degenerate-basis-telescope", "specified-linear-packet-event-normal-form"):
    if SEAMS[seam][0] != "audited":
        raise SystemExit(f"{seam} must remain exact audited event normal-form algebra")
if SEAMS["scalar-channel-event-compositional-closure"][0] != "audited-calibration":
    raise SystemExit("scalar diagonal channel state non-closure must remain an audited PSD counterexample")
if SEAMS["full-second-moment-linear-event-observational-completeness"][0] != "audited-conditional":
    raise SystemExit("full-Q observational completeness must remain conditional on the unrestricted linear event-probe class")
if SEAMS["first-bad-event-normal-form-instantiation"][0] != "open-literal":
    raise SystemExit("first-bad event normal-form instantiation must remain open-literal until actual NS event choices/maps are supplied")
for seam in ("first-bad-selected-residual-readout", "selector-second-moment-full-pair-jump", "selector-reset-hidden-germ-blocks", "persistent-library-selected-observer-architecture"):
    if SEAMS[seam][0] != "audited":
        raise SystemExit(f"{seam} must remain exact audited selector/readout algebra")
for seam in ("selector-switch-selected-state-factorization", "selector-switch-state-nonclosure", "selector-switch-selected-second-moment-nonclosure"):
    if SEAMS[seam][0] != "audited-calibration":
        raise SystemExit(f"{seam} must remain an exact selector nonclosure calibration")
if SEAMS["selector-switch-admissible-subspace-factorization"][0] != "audited-conditional":
    raise SystemExit("selector selected-to-selected factorization must remain conditional on an explicit admissible-state relation")
if SEAMS["physical-event-plus-selector-factorization"][0] != "audited-generic":
    raise SystemExit("physical-event plus selector factorization must remain a generic exact criterion, not a universal reduced transition")
if SEAMS["first-bad-persistent-library-dynamics"][0] != "audited-conditional":
    raise SystemExit("persistent library dynamics must remain conditional on an explicitly specified finite same-replica physical packet library")
for seam in ("same-replica-residual-library-common-noise", "same-replica-residual-library-qv-gram", "same-replica-residual-library-qv-rank", "same-replica-selector-qv-readout", "same-replica-event-qv-functor", "independent-per-germ-noise-model-distinction"):
    if SEAMS[seam][0] != "audited":
        raise SystemExit(f"{seam} must remain exact audited same-replica stochastic algebra")
if SEAMS["same-replica-library-bias-spread"][0] != "audited-conditional":
    raise SystemExit("same-replica library bias/spread law must remain conditional on the stated martingale integrability/adapted-coefficient scope")
if SEAMS["one-mode-same-replica-cross-qv-cancellation"][0] != "audited-calibration":
    raise SystemExit("same-replica cross-germ qv cancellation must remain tied to the exact one-mode NS calibration")
for seam in ("first-bad-candidate-library-instantiation", "first-bad-library-clock-replica-identification"):
    if SEAMS[seam][0] != "open-literal":
        raise SystemExit(f"{seam} must remain open-literal until the programme-specific physical library/clock is instantiated")
for seam in ("selected-residual-frozen-interval-martingale", "selector-readout-finite-jump", "selector-fv-zero-continuous-qv-vs-jump-qv", "selector-jump-dyad-three-face", "selector-jump-qv-vs-reset-covariance"):
    if SEAMS[seam][0] != "audited":
        raise SystemExit(f"{seam} must remain exact audited hybrid selector algebra")
if SEAMS["selected-hybrid-semimartingale-law"][0] != "audited-conditional":
    raise SystemExit("hybrid selected semimartingale law must remain conditional on a supplied same-replica library and selector path")
for seam in ("selector-jump-qv-bank-no-go", "one-mode-selector-optional-qv-closed-excursion"):
    if SEAMS[seam][0] != "audited-calibration":
        raise SystemExit(f"{seam} must remain an exact closed-excursion/NS calibration")
if SEAMS["first-bad-selected-hybrid-path-instantiation"][0] != "open-literal":
    raise SystemExit("first-bad hybrid path timing/event instantiation must remain open-literal")
for seam in ("combined-selected-post-event-readout", "combined-selected-jump-operator", "combined-event-discrete-product-rule", "combined-event-physical-selector-mixed-face", "combined-event-second-moment-full-pair-jump", "combined-event-jump-square-typing"):
    if SEAMS[seam][0] != "audited":
        raise SystemExit(f"{seam} must remain exact audited simultaneous-event algebra")
for seam in ("one-mode-combined-event-mixed-face", "naive-additive-physical-selector-event-no-go"):
    if SEAMS[seam][0] != "audited-calibration":
        raise SystemExit(f"{seam} must remain an exact-NS calibrated no-go/mechanism statement")
if SEAMS["selected-hybrid-with-simultaneous-linear-events"][0] != "audited-conditional":
    raise SystemExit("combined hybrid selected path law must remain conditional on supplied physical event/path data")
if SEAMS["first-bad-simultaneous-event-instantiation"][0] != "open-literal":
    raise SystemExit("actual first-bad simultaneous event timing/map/state must remain open-literal")
for seam in ("combined-selected-continuous-noise-readout", "combined-selected-continuous-qv-rate", "combined-continuous-qv-rate-full-pair-revaluation", "signed-qv-rate-revaluation-typing", "continuous-qv-rate-vs-jump-qv-independence"):
    if SEAMS[seam][0] != "audited":
        raise SystemExit(f"{seam} must remain exact audited continuous-source/event typing")
for seam in ("one-mode-hidden-event-continuous-qv-cancellation", "selector-only-qv-rate-hidden-event-no-go"):
    if SEAMS[seam][0] != "audited-calibration":
        raise SystemExit(f"{seam} must remain an exact-NS calibration")
if SEAMS["selected-hybrid-source-jump-ledger"][0] != "audited-conditional":
    raise SystemExit("hybrid source/jump ledger must remain conditional on supplied same-clock path data")
if SEAMS["first-bad-hybrid-source-event-instantiation"][0] != "open-literal":
    raise SystemExit("actual first-bad source/event/clock instantiation must remain open-literal")
for seam in ("adaptive-selected-event-mean-correlation", "adaptive-selected-event-congruence-four-face", "adaptive-event-map-dispersion-face", "adaptive-event-state-correlation-faces", "adaptive-event-qv-gram-congruence"):
    if SEAMS[seam][0] != "audited":
        raise SystemExit(f"{seam} must remain exact audited adaptive-event algebra")
for seam in ("mean-event-map-mean-payload-closure", "adaptive-event-alignment-correlation-sign"):
    if SEAMS[seam][0] != "audited-calibration":
        raise SystemExit(f"{seam} must remain an exact PSD calibration/no-go")
if SEAMS["selected-adaptive-event-expectation-ledger"][0] != "audited-conditional":
    raise SystemExit("adaptive event expectation ledger must remain conditional on supplied replica event/state data")
if SEAMS["first-bad-adaptive-event-joint-law"][0] != "open-literal":
    raise SystemExit("actual first-bad adaptive event joint law must remain open-literal")
for seam in ("first-bad-physical-score-passive-gauge", "first-bad-event-map-passive-gauge-equivariance", "first-bad-persistent-library-memory-necessity", "first-bad-adaptive-joint-law-necessity"):
    if SEAMS[seam][0] != "audited":
        raise SystemExit(f"{seam} must remain exact audited necessary physical typing")
for seam in ("raw-first-bad-score-passive-gauge-no-go", "first-bad-physical-residual-vs-support-locality", "first-bad-full-coherence-event-memory-necessity"):
    if SEAMS[seam][0] != "audited-calibration":
        raise SystemExit(f"{seam} must remain an audited exact calibration/no-go")
if SEAMS["first-bad-rule-physical-admissibility-ledger"][0] != "audited":
    raise SystemExit("first-bad admissibility ledger must remain exact/audited necessary-only typing, not sufficient")
if SEAMS["first-bad-badness-resolve-functional-after-admissibility"][0] != "open-literal":
    raise SystemExit("actual admissible first-bad badness/resolve functional must remain open-literal")
for seam in ("local-enstrophy-balance-vorticity-contraction", "kelvin-bulk-enstrophy-dissipation-identification", "local-enstrophy-critical-three-face-law", "local-max-growth-gate-curvature-necessity", "abc-beltrami-critical-stretching-zero"):
    if SEAMS[seam][0] != "audited":
        raise SystemExit(f"{seam} must remain exact audited PDE/Kelvin structure")
for seam in ("affine-vortex-positive-local-growth-gate", "affine-vortex-growth-gate-target-scope"):
    if SEAMS[seam][0] != "audited-calibration":
        raise SystemExit(f"{seam} must remain an exact affine calibration with target-class scope")
if SEAMS["first-bad-local-growth-to-continuation-bridge"][0] != "open-literal":
    raise SystemExit("local growth to continuation bridge must remain open-literal")
for seam in ("moving-enstrophy-critical-constraint-speed", "moving-enstrophy-critical-pde-relative-speed", "moving-enstrophy-critical-three-gradient-faces"):
    if SEAMS[seam][0] != "audited-conditional":
        raise SystemExit(f"{seam} must remain conditional on a differentiable nondegenerate critical branch")
for seam in ("moving-enstrophy-critical-value-speed-independence", "critical-hessian-inversion-theorem-domain"):
    if SEAMS[seam][0] != "audited":
        raise SystemExit(f"{seam} must remain exact audited critical-point geometry")
for seam in ("abc-fixed-enstrophy-maximum-vs-fluid-transport", "affine-degenerate-critical-speed-nonuniqueness"):
    if SEAMS[seam][0] != "audited-calibration":
        raise SystemExit(f"{seam} must remain an exact NS calibration")
if SEAMS["first-bad-enstrophy-critical-path-identification"][0] != "open-literal":
    raise SystemExit("first-bad enstrophy critical-path identification must remain open-literal")
if SEAMS["critical-hessian-evolution-three-face"][0] != "audited-conditional":
    raise SystemExit("critical-Hessian evolution must remain conditional on a differentiable critical branch")
for seam in ("critical-hessian-connection-strain-rotation-split", "incompressible-critical-hessian-connection-logdet-cancellation", "critical-hessian-strain-rotation-logdet-split", "critical-hessian-logdet-degeneracy-domain"):
    if SEAMS[seam][0] != "audited":
        raise SystemExit(f"{seam} must remain exact audited Hessian geometry")
for seam in ("critical-hessian-incompressible-curvature-volume-law", "critical-hessian-jacobi-logdet-law", "critical-branch-finite-lograte-nondegeneracy"):
    if SEAMS[seam][0] != "audited-conditional":
        raise SystemExit(f"{seam} must remain conditional on Hessian nondegeneracy/branch regularity")
if SEAMS["abc-critical-hessian-logdet-calibration"][0] != "audited-calibration":
    raise SystemExit("ABC critical-Hessian logdet statement must remain an exact periodic calibration")
if SEAMS["first-bad-critical-branch-degeneracy-identification"][0] != "open-literal":
    raise SystemExit("critical-branch degeneracy to first-bad identification must remain open-literal")
if SEAMS["selected-spectral-hybrid-projector-event-ledger"][0] != "audited-conditional":
    raise SystemExit("hybrid projector event ledger must remain a same-clock conditional composition")
for seam in ("first-bad-orientation-packet-refinement-instantiation", "first-bad-spectral-event-transfer-instantiation", "first-bad-selected-spectral-lineage"):
    if SEAMS[seam][0] != "open-literal":
        raise SystemExit(f"{seam} must remain open-literal until the programme-specific physical event is supplied")
if SEAMS["reverse-codeforming-future-bank-identification"][0] != "open-literal":
    raise SystemExit("reverse codeforming / future-bank identification must remain open-literal")
if SEAMS["finite-shape-centered-quadrupole-jet"][0] != "audited-conditional":
    raise SystemExit("centered finite-shape quadrupole/qv jet law must remain local-smooth conditional")
for seam in ("finite-shape-cubic-covariance-blind-no-go", "finite-shape-one-mode-error-covariance", "finite-shape-abc-shape-drift", "finite-shape-moment-covariance-blindness"):
    if SEAMS[seam][0] != "audited-calibration":
        raise SystemExit(f"{seam} must remain an exact NS calibration/no-go, not a first-bad theorem")
if SEAMS["first-bad-full-shape-local-descent"][0] != "open-literal":
    raise SystemExit("first-bad finite-shape/local-current descent must remain open-literal")
if SEAMS["selected-support-cauchy-deformation-alignment"][0] != "open-literal":
    raise SystemExit("selected support / stochastic Cauchy deformation alignment must remain open-literal")
if SEAMS["stochastic-cauchy-uniform-deformation-control"][0] != "open":
    raise SystemExit("uniform stochastic Cauchy deformation control must remain open")
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
