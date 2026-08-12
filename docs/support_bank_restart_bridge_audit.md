# Physical Kelvin support x total-bank restart-rate audit

This note asks the next literal PDE question after the first-bad event semantics and
naive-threshold exclusions:

> once the physical backward-Kelvin state is written in its coherent variables,
> what exact relation ties material support geometry and the resolved-plus-future
> second moment back to physical vorticity?

No new norm is chosen.  The only ordering used is positive-semidefinite tensor order,
which has direct physical meaning: principal support lengths and principal
second-moment amplitudes.

The result is a conditional **local rate theorem**, not a continuation theorem.  The
programme still lacks uniform first-bad/global coverage, the full ancestry lift, and
uniform control of nonideal localization/finite-shape faces.

---

## 1. Ideal full physical Kelvin core

On the full physical backward-Kelvin state, use the already audited co-deforming
variables

\[
\boxed{
\omega=F\eta,
}
\]

and write the co-deforming total terminal second moment as

\[
\boxed{
Q_{\rm tot}
=\eta\eta^T+\widetilde C,
\qquad
\widetilde C\succeq0.
}
\]

Here `eta eta^T` is the resolved mean-square sector and `Ctilde` is the future
conditional covariance sector.  Their physical pushforward is

\[
\boxed{
T_{\rm tot}
=FQ_{\rm tot}F^T
=\omega\omega^T+F\widetilde C F^T.
}
\]

Hence

\[
\boxed{
T_{\rm tot}-\omega\omega^T
=F\widetilde C F^T\succeq0.
}
\]

**Physical classification:** resolved physical vorticity dyad plus unresolved future
Kelvin covariance.

**Classification: Exact full-state tensor identity.**

---

## 2. Physical parabolic support tensor

Let

\[
\tau=\Theta-t>0
\]

be the remaining physical/Kelvin horizon and let the Brownian line scale be

\[
\rho_\nu=\sqrt{2\nu\tau}.
\]

The coherent Kelvin-scale material line frame is

\[
L_\nu=\rho_\nu F.
\]

Its spatial Cauchy--Green/support tensor is therefore

\[
\boxed{
P_\nu
:=L_\nu L_\nu^T
=2\nu\tau FF^T.
}
\]

Thus the eigenvalues of `P_nu` are literally squared physical lengths of the
principal Kelvin-scale material axes.

Under physical-time material deformation

\[
\dot F=(\nabla u)F,
\qquad
\dot\tau=-1,
\]

one obtains directly

\[
\boxed{
\dot P_\nu
=(\nabla u)P_\nu
+P_\nu(\nabla u)^T
-\frac1\tau P_\nu.
}
\]

The first two terms are real material strain/rotation.  The last term is the real
shrinking of the Kelvin diffusion horizon.  No artificial damping term has been
introduced.

**Classification: Exact material/parabolic support identity.**

---

## 3. Loewner envelopes have direct physical meaning

Suppose at a given physical Kelvin state there exist scalar principal envelopes
`p_*(t),q_*(t)` such that

\[
\boxed{
P_\nu\preceq p_* I,
}
\]

and

\[
\boxed{
Q_{\rm tot}\preceq q_* I.
}
\]

These are not arbitrary analysis norms:

- `p_*` is an upper bound for the **squared largest Kelvin-scale physical support
  axis**;
- `q_*` is an upper bound for the **largest co-deforming total second-moment
  principal value**.

The minimal such scalars are the corresponding largest principal values, but the
theorem does not require diagonalization or a particular coordinate frame.

**Classification: Physical tensor-order hypotheses, not a proved uniform bound.**

---

## 4. Exact three-face factorization

The key identity is

\[
\boxed{
\begin{aligned}
p_*q_*I-2\nu\tau\,\omega\omega^T
={}&q_*(p_*I-P_\nu)\\
&+2\nu\tau F(q_*I-Q_{\rm tot})F^T\\
&+2\nu\tau F(Q_{\rm tot}-\eta\eta^T)F^T.
\end{aligned}
}
\]

CI verifies this with a fully non-diagonal symbolic `F`, `eta`, and covariance.

Each term has an already identified physical type:

1. \(q_*(p_*I-P_\nu)\): **support headroom**;
2. \(2\nu\tau F(q_*I-Q_{\rm tot})F^T\): **total-bank principal headroom**;
3. \(2\nu\tau F(Q_{\rm tot}-\eta\eta^T)F^T\): **unresolved future covariance**.

If the stated tensor envelopes hold, all three terms are positive semidefinite.
Therefore

\[
\boxed{
2\nu\tau\,\omega\omega^T
\preceq
p_*q_* I.
}
\]

This is not an estimate guessed from the PDE.  It is the exact resolved/unresolved
and support decomposition followed by positivity of physical covariance.

**Classification: Exact factorization; rigorous conditional PSD consequence.**

---

## 5. Direction-free physical vorticity rate

Because the only nonzero eigenvalue of `omega omega^T` is `|omega|^2`, the tensor
order gives

\[
\boxed{
|\omega(t)|^2
\le
\frac{p_*(t)q_*(t)}{2\nu\tau}.
}
\]

Equivalently,

\[
\boxed{
\sqrt\tau\,|\omega(t)|
\le
\sqrt{\frac{p_*(t)q_*(t)}{2\nu}}.
}
\]

This relation keeps the two physical channels visible:

- vorticity can become large because Kelvin-scale support is stretched (`p_*`);
- or because the co-deforming resolved-plus-unresolved second moment is large
  (`q_*`);
- the covariance sector itself appears with the correct positive sign in the
  factorization rather than being discarded.

**Classification: Rigorous conditional local-rate consequence.**

---

## 6. Bounded support-bank product gives a time-integrable local rate

Assume only on a terminal interval

\[
0<\tau<\varepsilon
\]

that

\[
\boxed{
p_*(t)q_*(t)\le M<\infty.}
\]

Then

\[
|\omega(t)|
\le
\sqrt{\frac{M}{2\nu}}\,\tau^{-1/2}.
\]

The terminal-time integral is explicit:

\[
\boxed{
\int_{\Theta-\varepsilon}^{\Theta}|\omega(t)|\,dt
\le
\sqrt{\frac{2M\varepsilon}{\nu}}.
}
\]

Thus, **along any physical state/germ for which the ideal tensor identification and
the product envelope hold uniformly**, the vorticity rate is time-integrable near
the terminal time.

This statement is local/statewise.  It does not assert a spatially uniform bound and
therefore does not by itself invoke or close a global continuation criterion.

**Classification: Rigorous conditional local time-integrability theorem.**

---

## 7. Support locality plus bounded total bank is stronger

If the Kelvin-scale material packet becomes genuinely support-local in the tensor
sense

\[
\boxed{p_*(t)\to0}
\]

and the co-deforming total bank remains bounded,

\[
\boxed{q_*(t)\le Q_*<\infty,}
\]

then

\[
\boxed{
\tau|\omega(t)|^2
\le
\frac{p_*(t)Q_*}{2\nu}
\to0,
}
\]

so

\[
\boxed{
\sqrt\tau\,|\omega(t)|\to0.
}
\]

This is exactly the geometric meaning one would hope for from a local Kelvin
restart packet: if the physical Brownian-scale support truly collapses while the
co-deforming total second moment does not blow up, physical vorticity cannot outrun
the integrable `tau^-1/2` scale.

**Classification: Rigorous conditional local consequence.**

---

## 8. Why this is not yet a restart theorem

Several proof-critical bridges remain outside the identity:

1. **Programme ancestry state lift.**  The repository has not yet constructed the
   map/kernel from its abstract ancestry state to the full physical reverse-age
   Kelvin state on which `Q_tot` above lives.
2. **Uniform first-bad coverage.**  The first-bad `bad_flags` and `resolved`
   predicates are still undefined, so there is no theorem that the selected germ is
   the one whose loss would control the whole physical solution.
3. **Uniform envelopes.**  No proof gives a common terminal bound for `p_*q_*`
   over all physically relevant states/germs.
4. **Finite-shape/localization remainder.**  The ideal infinitesimal core omits the
   full finite-shape hierarchy, metric-whitened localization remainder, and moving
   quantile/shell faces whose uniform collapse is still open.
5. **Physical exit/boundary/reset work.**  These have exact types but no global
   terminal control theorem.
6. **Continuation theorem insertion.**  No global continuation criterion has been
   paired line by line with this local tensor rate.

Therefore the correct status is not

> vorticity is controlled.

It is

> **if** the physically named support and total-bank envelopes remain uniformly
> finite on the right state family, then the local terminal vorticity rate is
> integrable.

**Classification: Conditional bridge; continuation/restart remains open.**

---

## 9. Relation to the naive-threshold exclusion

The amplitude-scaled ABC audit showed that no finite universal raw threshold on
`|omega|`, stretching, q.v., or their instantaneous ratio can alone certify failure.

The present theorem is qualitatively different.  It does not say

\[
p_*q_*<\text{universal constant}.
\]

Instead it identifies the **asymptotic coupled resource** whose boundedness would
force an integrable terminal rate for a fixed solution/state family.

Thus this theorem does not contradict the ABC no-go and does not propose a new
finite first-bad threshold.

**Classification: Rigorous structural compatibility.**

---

## 10. A sharper obstruction ledger

Within the ideal full physical Kelvin core, a terminal vorticity blow-up fast enough
to evade the integrable `tau^-1/2` rate must be accompanied by failure of at least
one stated hypothesis, for example:

- parabolic material support envelope `p_*` becomes unbounded strongly enough;
- co-deforming total second-moment envelope `q_*` becomes unbounded strongly enough;
- the full physical state/covariance representation ceases to match the programme
  ancestry/reduced state;
- finite-shape/localization or boundary/exit faces fail to vanish/control uniformly.

This is an **obstruction ledger**, not yet a singularity theorem, because the
programme has not shown that these alternatives exhaust a globally selected
first-bad continuation failure.

**Classification: Rigorous conditional dichotomy inside the ideal core; global
exhaustiveness remains conjectural/open.**

---

## 11. Updated next target

The next PDE-first target is no longer to invent a scalar norm.  It is to ask whether
the actual first-bad construction can provide, from the NS/Kelvin dynamics itself,

\[
\boxed{
P_\nu\preceq p_*I,
\qquad
Q_{\rm tot}\preceq q_*I,
\qquad
p_*q_*\ \text{terminally controlled},
}
\]

**uniformly over the physically relevant selected state family**, while the named
finite-shape/localization/exit faces are retained.

No claim is made that this has been proved.

`S^int`, the literal badness/resolve functions, uniform singular-time collapse,
restart capacity, and continuation remain open.

Audit markers: `P_\nu`, `Q_{\rm tot}`, status **Open** for the uniform/global
first-bad envelope and continuation seams.

**Classification: Exact/conditional structural advance; no regularity conclusion.**
