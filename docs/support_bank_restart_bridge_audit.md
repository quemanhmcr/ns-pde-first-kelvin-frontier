# Scale-parametric support x total-bank restart-rate audit

This note isolates an exact tensor relation between coherent material support,
resolved vorticity, and an unresolved covariance sector.  A causal correction is
essential: the algebra is **scale-parametric** and does not by itself identify the
shrinking first-bad scale with the horizon of the causal backward-Kelvin covariance
bank.

Three objects must remain distinct:

1. a positive physical packet scale `ell` and its support geometry;
2. a causal backward-Kelvin covariance bank with a past terminal `t0<t`;
3. the future candidate/first-bad remaining time `tau=Theta-t`.

The first gives exact algebra.  The second gives a physical positive covariance.
Connecting both to the third is a separate two-clock/terminal/state problem.

No restart or regularity conclusion is claimed.

---

## 1. Exact coherent state algebra does not need a clock

Let `F` be an invertible material deformation tensor and let

\[
\boxed{\omega=F\eta.}
\]

Let a co-deforming total second moment be

\[
\boxed{
Q_{\rm tot}=\eta\eta^T+\widetilde C,
\qquad
\widetilde C\succeq0.
}
\]

Here `eta eta^T` is the resolved mean dyad and `Ctilde` is any physically valid
unresolved covariance sector on the **same state and coordinate frame**.  Its
physical pushforward is

\[
\boxed{
T_{\rm tot}=FQ_{\rm tot}F^T
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

This identity is purely tensorial.  No stochastic horizon has entered.

**Physical classification:** resolved physical vorticity dyad plus pushed
unresolved covariance.

**Classification: Exact full-state tensor identity.**

---

## 2. Pure material support at an arbitrary positive scale

Let `ell>0` be a physical linear scale attached to a coherent isotropic reference
microcell.  The material line frame at that scale is

\[
L_\ell=\ell F.
\]

Define the spatial support Cauchy--Green tensor

\[
\boxed{
P_\ell:=L_\ell L_\ell^T
=\ell^2FF^T.
}
\]

The eigenvalues of `P_ell` are squared principal line lengths of this material
microcell.  This is ordinary continuum geometry; it is not automatically the
covariance matrix of a Brownian cloud.

The exact affine reverse-diffusion audit is a useful warning.  Actual Gaussian
anchor covariance is a time integral

\[
2\nu\int F_rF_r^T\,dr,
\]

whereas `ell^2 F F^T` is an endpoint material support tensor.  They coincide only in
special/infinitesimal circumstances, not by definition.

**Classification: Exact material support identity and exact type distinction.**

---

## 3. Exact three-face factorization is scale-parametric

Suppose scalar principal envelopes `p_*`, `q_*` satisfy

\[
P_\ell\preceq p_*I,
\qquad
Q_{\rm tot}\preceq q_*I.
\]

Then the exact algebraic identity is

\[
\boxed{
\begin{aligned}
p_*q_*I-\ell^2\omega\omega^T
={}&q_*(p_*I-P_\ell)\\
&+\ell^2F(q_*I-Q_{\rm tot})F^T\\
&+\ell^2F(Q_{\rm tot}-\eta\eta^T)F^T.
\end{aligned}
}
\]

CI audits this with a fully non-diagonal symbolic `F`, `eta`, and covariance.

The three terms have literal physical types:

1. **support headroom** `q_*(p_*I-P_ell)`;
2. **total-bank principal headroom** `ell^2 F(q_*I-Q_tot)F^T`;
3. **unresolved future covariance** or other physically supplied covariance
   `ell^2 F(Q_tot-eta eta^T)F^T`.

If the stated Loewner envelopes and covariance positivity hold, all three terms are
positive semidefinite, hence

\[
\boxed{
\ell^2\omega\omega^T\preceq p_*q_*I.
}
\]

and therefore

\[
\boxed{
|\omega|^2\le\frac{p_*q_*}{\ell^2}.
}
\]

No estimate was guessed from Navier--Stokes; the inequality is the positivity
consequence of an exact resolved/unresolved/support factorization.

**Classification: Exact scale-parametric factorization; rigorous conditional PSD
consequence.**

---

## 4. Candidate parabolic material scale is a separate specialization

A natural **candidate** scale supplied by a future remaining time is

\[
\boxed{
\ell_\nu^2=2\nu\tau,
\qquad
\tau=\Theta-t.
}
\]

If a physical packet is actually refined/reselected at this scale, its material
support tensor is

\[
\boxed{
P_\nu^{\rm cand}
=2\nu\tau FF^T.
}
\]

For physical-time material deformation `Fdot=A F` and `taudot=-1`, this chosen
support tensor obeys

\[
\boxed{
\dot P_\nu^{\rm cand}
=A P_\nu^{\rm cand}
+P_\nu^{\rm cand}A^T
-\frac1\tau P_\nu^{\rm cand}.
}
\]

The first two terms are real material deformation.  The last comes from the chosen
shrinking reference scale `sqrt(2nu tau)`.

This is **not** yet a theorem that the actual first-bad germ uses this scale.  That
seam already exists as `first-bad-parabolic-scale-identification`.

It is also not yet a statement about the causal backward-Kelvin covariance horizon.

**Classification: Exact candidate-scale kinematics; first-bad scale identification
Open.**

---

## 5. Causal backward-Kelvin bank has a past horizon, not `Theta-t`

The physical backward-Kelvin covariance theorem uses a past terminal

\[
t_0<t.
\]

Its causal past horizon is

\[
\boxed{h=t-t_0.}
\]

For fixed `t0`,

\[
\boxed{\dot h=+1.}
\]

If `t` approaches a future candidate time `Theta`, then

\[
\boxed{h\to\Theta-t_0,}
\]

which is generally positive.  It does **not** shrink to zero.

By contrast,

\[
\tau=\Theta-t,
\qquad
\boxed{\dot\tau=-1.}
\]

Therefore

\[
\boxed{
\text{causal past horizon }h=t-t_0
\ne
\text{future remaining horizon }\tau=\Theta-t
}
\]

for a fixed past terminal.

This is the causal correction to the first version of this audit.

**Classification: Exact clock identity and exact incompatibility for fixed `t0`.**

---

## 6. A moving past terminal can match the shrinking horizon pointwise

For each `t<Theta`, one may define

\[
\boxed{t_0(t)=2t-\Theta.}
\]

Then

\[
t_0(t)<t,
\]

and

\[
\boxed{
t-t_0(t)=\Theta-t=\tau.
}
\]

Thus a genuine causal past-payoff Kelvin bank **can** be evaluated over a past
interval whose length equals the shrinking future remaining time.

However,

\[
\boxed{\dot t_0=2.}
\]

The terminal itself moves.  Consequently this family is not the fixed-terminal
martingale bank used by the standard backward-Kelvin PDE without modification.

Pointwise positivity and the decomposition

\[
Q_{\rm tot}(t,t_0(t))
=\eta(t)\eta(t)^T+\widetilde C(t,t_0(t))
\]

remain legitimate whenever the physical backward representation is defined.  But
its time derivative has a new physical terminal-motion face.

**Classification: Exact causal moving-terminal construction; fixed-terminal PDE
cannot be reused without its extra face.**

---

## 7. Moving-terminal face is exact

For any two-time quantity `Q(t,t0)`, along `t0=t0(t)`,

\[
\boxed{
\frac d{dt}Q(t,t_0(t))
=\partial_tQ+\dot t_0\,\partial_{t_0}Q.
}
\]

For the matching choice `t0(t)=2t-Theta`,

\[
\boxed{
\frac d{dt}Q
=\partial_tQ+2\partial_{t_0}Q.
}
\]

The one-mode exact NS shear audits this literally.  At fixed past terminal its
second moment satisfies the homogeneous backward-Kelvin equation.  Along the moving
terminal, the same operator leaves exactly

\[
\boxed{2\partial_{t_0}Q}
\]

as the terminal-motion face.

For centered covariance the corresponding moving-terminal law is

\[
\boxed{
\mathfrak D_K C
=\mathcal G_K
+2\partial_{t_0}C
}
\]

in the one-mode calibration.  The first term is physical Kelvin q.v.; the second is
terminal reselection/motion.  It is not `S^int` and must not be discarded.

This is directly analogous to the `Qdot` face of a moving quantile chamber: moving
the object being conditioned/localized on changes the balance.

**Classification: Exact chain rule and exact one-mode Navier--Stokes calibration.**

---

## 8. What remains exact if a shrinking scale is paired with a covariance family

The scale-parametric factorization of Section 3 needs only:

- the same deformation `F` in the support and second-moment coordinates;
- a positive covariance sector `Ctilde`;
- one chosen physical scale `ell`.

Therefore, if one constructs a **same-state/same-scale** family with

\[
\ell^2=2\nu(\Theta-t)
\]

and a total second moment `Q_tot(t)` satisfying the stated positivity, then

\[
\boxed{
|\omega(t)|^2
\le
\frac{p_*(t)q_*(t)}{2\nu(\Theta-t)}.
}
\]

If

\[
\boxed{p_*(t)q_*(t)\le M}
\]

on a terminal interval, then

\[
|\omega(t)|
\le
\sqrt{\frac{M}{2\nu}}(\Theta-t)^{-1/2}
\]

and the **statewise** rate is time-integrable:

\[
\boxed{
\int_{\Theta-\varepsilon}^{\Theta}|\omega(t)|\,dt
\le
\sqrt{\frac{2M\varepsilon}{\nu}}.
}
\]

This implication is rigorous **conditional on the same-scale covariance pairing and
the Loewner envelopes**.

What is not yet proved is that the programme's abstract future bank, a causal
moving-past Kelvin bank, or the first-bad selected packet supplies exactly this
same-state family with uniform `p_*q_*` control.

**Classification: Rigorous conditional scale-parametric/two-clock local-rate
consequence.**

---

## 9. Support collapse plus bounded total bank

Under the same conditional pairing, if

\[
p_*(t)\to0
\]

and

\[
q_*(t)\le Q_*<\infty,
\]

then

\[
\boxed{
(\Theta-t)|\omega(t)|^2
\le
\frac{p_*(t)Q_*}{2\nu}
\to0,
}
\]

hence

\[
\boxed{
\sqrt{\Theta-t}\,|\omega(t)|\to0.
}
\]

Again, this is a conditional statement on a physically aligned shrinking packet
and second-moment family.  It is not a theorem that the actual first-bad packet has
those properties.

**Classification: Rigorous conditional local consequence.**

---

## 10. Why this is not yet a restart theorem

The remaining seams are now more precise.

### A. First-bad scale identification

No theorem identifies the actual selected germ scale with

\[
\sqrt{2\nu(\Theta-t)}.
\]

### B. Scale--covariance horizon/state identification

A fixed-past causal bank has horizon `h=t-t0`, not `Theta-t`.  The moving-terminal
construction can match the lengths, but introduces the explicit terminal-motion
face and still requires the covariance state/deformation to be the same state used
by the selected packet.

A separate fixed-past audit now identifies the total-bank envelope more literally:
`Q_s<=W_s R_s`, where `R_s=E[D D^T]` is the stochastic Cauchy deformation second
moment, with an exact terminal-directional-headroom plus centered-covariance split.
This improves physical typing but does not identify the selected coherent `F` with
the random Cauchy deformation `D`.

See `docs/stochastic_cauchy_deformation_audit.md`.

This seam is **Open-literal**.

### C. Uniform support-bank envelopes

No theorem supplies a common terminal bound on `p_*q_*` over all physically
relevant selected states/germs.

### D. Finite-shape/localization hierarchy

The ideal coherent identity omits the finite shape hierarchy, metric-whitened
localization remainder, moving quantile/shell faces, and state-resolution covariance
that must be controlled uniformly.

### E. Physical boundary/exit/reset work

These terms are typed exactly but have no global terminal control theorem.

### F. Badness/resolve semantics

`bad_flags` and `resolved` remain Boolean oracle inputs.  No Navier--Stokes event
functional proves that the selected germ exhausts continuation failure.

### G. Continuation insertion

No literal global continuation criterion has yet been paired line by line with this
statewise rate.

Therefore the theorem is **not yet a restart theorem**.

**Classification: Exact obstruction ledger; restart/continuation Open.**

---

## 11. Relation to the causal future-bank audit

The future ancestry bank can be reversed in its own clock, and the physical
backward-Kelvin process can be parameterized by reverse age.  Those operator facts
are exact.  But they do not automatically identify

\[
\tau=\Theta-t
\]

with the past horizon of the covariance tensor used here.

The moving-terminal construction above is one literal physical way to create a
past horizon equal to `tau`; its extra terminal face shows exactly what must be paid
when doing so.

Thus the living bridge is no longer a vague sign problem.  It is:

\[
\boxed{
\text{selected shrinking scale}
+\text{same-state covariance family}
+\text{moving-terminal/clock faces}
+\text{uniform Loewner envelopes}.
}
\]

**Classification: Rigorous structural reduction; programme-specific identification
Open-literal.**

---

## 12. Updated next target

The exact support×bank algebra has done its job: it tells us what a successful
terminal mechanism would have to control without pretending that control already
exists.

The next PDE-first question is whether the actual NS/Kelvin first-bad construction
can produce a physical family for which

\[
P_\ell\preceq p_*I,
\qquad
Q_{\rm tot}\preceq q_*I,
\qquad
p_*q_*\ \text{is terminally controlled},
\]

with `ell` tied to the actual selected physical scale and all clock/terminal faces
retained.

Audit markers: `P_nu`, `Q_tot`, **scale-parametric**, **causal past horizon**,
**moving terminal**, status **Open-literal** for scale--covariance horizon/state
identification, and status **Open** for uniform/global first-bad control.

`S^int`, uniform finite-shape/localization collapse, restart capacity, and
continuation remain open.

**Classification: Exact/conditional structural advance; no regularity conclusion.**
