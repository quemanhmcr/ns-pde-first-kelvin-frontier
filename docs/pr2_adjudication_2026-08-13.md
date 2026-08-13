# Draft PR #2 adjudication — own-local Kelvin event compatibility

This is the repository-side adjudication of draft PR #2.  The rule is PDE-first:
current, frame, local target, stochastic source, selector, and expectation are typed
as distinct physical objects before any norm or estimate is introduced.

## Verdict table

| PR #2 finding | Verdict | Action |
|---|---|---|
| P0 own-local target mismatch | **Correct** | Repair the event interface: keep the old `A/B` law only for common-target/already-reanchored residuals and add the exact affine target face. |
| Affine reanchoring composition | **Correct** | Promote the target face as an exact coboundary/functoriality theorem for supplied finite events. |
| Affine moment/selector/noise propagation | **Correct** | Retain offset, cross, selector, and target-gradient Gram faces. |
| P1 Zeno/local-time | **Correct guardrail, not a defect in the finite-event theorem** | Add an Open-literal local-finiteness/interface-local-time seam. |
| P2 two-replica versus population closure | **Correct guardrail, not a defect in the two-replica theorem** | Add the general centered triple face and exact three-state PSD witness. |
| `37c635f` enstrophy audit | **Correct in stated smooth domain** | No algebra repair. |
| `c27d1f1` critical-point speed audit | **Correct conditionally** | Keep differentiable nondegenerate branch and classical regularity explicit. |
| `884956e` Hessian/Jacobi audit | **Correct conditionally** | Keep higher smoothness and nondegeneracy explicit; degeneracy is a chart boundary, not a continuation failure. |

No principal mathematical finding in PR #2 is rejected.  The key adjudication is the
**type** of finding: P0 is a genuine interface correction; P1 and P2 are anti-extension
guardrails for theorems that remain correct in their stated finite-event and
two-replica domains.

## 1. Exact own-local event

For packet-specific targets

\[
\varepsilon_i=K_i-H_i^T\omega_i,
\qquad
\varepsilon_P=K_P-H_P^T\omega_P,
\]

and literal current/area identities

\[
K_P=\sum_iR_iK_i,
\qquad
H_P^T=\sum_iR_iH_i^T,
\]

the exact relation is

\[
\boxed{
\varepsilon_P=\sum_iR_i\varepsilon_i+\Delta_\omega,
\qquad
\Delta_\omega=\sum_iR_iH_i^T(\omega_i-\omega_P).
}
\]

Hence the common-target theorem survives exactly, while an own-local physical event is

\[
\boxed{r_P=A\mathbf r+d,\qquad d=H_P^{-T}\Delta_\omega.}
\]

In coherent codeforming coordinates,

\[
\boxed{\chi_P=B\boldsymbol\chi+d_\chi,\qquad d_\chi=J_P^{-1}\Delta_\omega.}
\]

**Classification: Exact identity.**

## 2. Target change is a coboundary, not an arbitrary forcing

Let `z=x+Omega` be the unreanchored current/frame readout.  If `z_+=A z_-`, then

\[
\boxed{x_+=Ax_-+d,\qquad d=A\Omega_- - \Omega_+.}
\]

For two supplied events,

\[
A_2d_1+d_2=A_2A_1\Omega_0-\Omega_2.
\]

Thus direct and sequential reanchoring agree whenever the underlying current maps
compose.  The affine term is physical but path-independent at this algebraic level.

**Classification: Exact identity / rigorous functorial consequence.**

## 3. Second moment, selector jump, and continuous source

Pathwise,

\[
(Ax+d)(Ax+d)^T
=Axx^TA^T+Axd^T+dx^TA^T+dd^T.
\]

For a simultaneous selector change,

\[
\boxed{\Delta Y=(E_+A-E_-)X+E_+d.}
\]

The optional jump-q.v. atom is the square of that full jump, so the linear/target
cross faces and target dyad are mandatory.

The Brownian response has the exact gradient analogue

\[
\boxed{
N_+=AN_-+N_{\rm target},
\qquad
N_{\rm target}=AG_- - G_+.
}
\]

Thus the post-event Gram contains the base `A N_-` face, two signed cross faces, and
`N_target N_target^T`.  A pure reanchor can change continuous q.v. even when `A=I`.

**Classification: Exact pathwise identities.**

## 4. Exact Navier--Stokes witness

For

\[
u=(y^3+6\nu ty,0,0),
\qquad
\omega_z=-(3y^2+6\nu t),
\]

the nonlinear term vanishes and the scalar profile obeys `U_t-nu U_yy=0`.  For a
rectangular `xy` loop centered at `a`, half-width `b`, x-length `ell`, reanchored to
`p`,

\[
\varepsilon_p=2b\ell(-3a^2-b^2+3p^2),
\qquad
Q_p=12b\ell(p-a).
\]

The own anchor `p=a` has `Q_a=0`, while reanchoring the same current/frame to `p=0`
gives `Q_0=-12ab\ell`.  For symmetric children at `+a` and `-a` with parent target
zero,

\[
\varepsilon_P-(\varepsilon_++\varepsilon_-)=-12a^2b\ell\neq0.
\]

**Classification: Audited exact-NS calibration / rigorous no-linear-own-local-extension consequence.**

## 5. P1 finite-event boundary

The finite-jump hybrid identity is retained for a supplied selector path with locally
finite, or otherwise summably controlled, events.  A Brownian-sign threshold selector
can instead produce `Y=|W|`; Tanaka local time is not represented by a finite sum of
jump squares.

This does not refute the finite-event theorem.  It forbids silently extending it to an
endogenous first-bad selector before local finiteness/hysteresis separation is proved,
or before an interface/local-time term is retained.

**Classification: Rigorous anti-extension guardrail; endogenous first-bad event local finiteness/interface law remains Open-literal.**

## 6. P2 population expectation boundary

The exact two-replica four-face identity remains unchanged.  For a general population,
with `delta C=C-E C`, `delta Q=Q-E Q`, one has

\[
\begin{aligned}
E[CQC^T]={}&\mu_C\mu_Q\mu_C^T
+E[\delta C\,\mu_Q\,\delta C^T]\\
&+\mu_CE[\delta Q\,\delta C^T]
+E[\delta C\,\delta Q]\mu_C^T\\
&+\boxed{E[\delta C\,\delta Q\,\delta C^T]}.
\end{aligned}
\]

For equal weights on `(C,Q)=(0,1),(1,0),(2,1)`, all payloads are PSD and

\[
E[C^2Q]=\frac43,
\qquad
\text{first four population faces}=\frac{10}{9},
\qquad
\text{triple face}=\frac29.
\]

**Classification: Exact population identity / rigorous anti-factorization consequence.**

## 7. Repaired frontier

The literal chain is now

\[
\boxed{
\text{own-local packet library}
\to
\text{target-compatible affine state/noise event}
\to
\text{adaptive joint law}
\to
\text{locally-finite or interface-corrected endogenous selector}
\to
\text{hybrid bank/restart calculus}.
}
\]

Open-literal items remain the actual NS-generated packet/anchor event, the physical
badness/resolve rule, support locality, event local finiteness versus interface local
time, and the bridge from the same-replica clock to the future-bank/restart clock.

No restart/continuation/global-regularity theorem is claimed.
