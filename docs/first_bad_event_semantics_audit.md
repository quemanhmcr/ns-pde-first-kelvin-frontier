# Hysteretic first-bad event semantics versus moving localization cuts

This note audits a type distinction that became visible only after the clock/cut
repair.  The current repository contains two different kinds of state-dependent
operations:

1. the intrinsic rank-one **first-bad selector** `M_fb`, which consumes Boolean
   `bad_flags` and a Boolean `resolved` input;
2. moving **quantile/shell localization maps** `Q_s`, `H_s`, whose boundaries have
   continuous Reynolds/coarea time faces when their defining geometry moves.

They are not the same map and need not move on the same clock.  Conflating them
would hide two missing physical definitions behind one symbol.

No restart or regularity claim is made.

---

## 1. Literal implementation semantics of `M_fb`

The code implements

```text
hysteretic_first_bad_projection(bad_flags, previous_index, resolved)
```

with the following rule:

- if `previous_index` is active and `resolved=False`, keep that same index;
- otherwise recompute the first `True` bad flag in the prescribed priority order.

Hence on an unresolved hysteresis interval,

\[
\boxed{M_{\rm fb}(t)=M_*\quad\Longrightarrow\quad \dot M_{\rm fb}=0}
\]

in the literal selector coordinates, regardless of how the Boolean badness pattern
of unselected germs changes.

CI exhausts every Boolean flag pattern for selectors of sizes `1,2,3,4` and verifies
that the unresolved output is always the same rank-one projector.

**Classification: Exact implementation identity.**

---

## 2. Entry and resolve are finite events, not a smooth selector payment

If no germ is active and a bad flag appears, the selector changes from zero to a
rank-one projector.  If an active germ resolves, priority is recomputed and the
selector may jump to another rank-one projector.

Thus the coordinate-level selector path is naturally piecewise constant:

\[
\boxed{
dM_{\rm fb}
=\sum_k \Delta M_k\,\delta_{t_k}
}
\]

in distributional/event-measure notation.  There is no reason to replace these
finite events by a positive smooth density.

For every event, the pair selector obeys the already audited exact jump law

\[
\boxed{
M_+\otimes M_+-M_-\otimes M_-
=
\Delta M\otimes M_-
+M_-\otimes\Delta M
+\Delta M\otimes\Delta M.
}
\]

The same identity is the current-level source of the signed covariance reset law.

**Classification: Exact finite-event and pair-jump identities.**

---

## 3. `bad_flags` are currently a Boolean oracle

The selector receives

```text
bad_flags: Sequence[bool]
```

directly.  The repository contains no function

\[
\boxed{
\mathcal B_i[
 u,\omega,F,Q_{\rm tot},\rho,\ldots](t)
}
\]

and no threshold `theta_i(t)` such that

\[
\boxed{
\texttt{bad\_flags}_i(t)
=\mathbf 1_{\{\mathcal B_i(t)\ge\theta_i(t)\}}.
}
\]

A generic constructor `score_i >= theta_i` is trivial algebra, but it does not
choose a Navier--Stokes quantity.  The PDE must supply that physical meaning.

This matters because the first-bad event times themselves are undefined until the
score and threshold are defined.  Priority semantics alone does not produce a
physical first-bad time.

**Classification: Open-literal programme definition; exact code-level diagnosis.**

---

## 4. `resolved` is a second independent Boolean oracle

Even if `bad_flags` were physically defined, the current API still takes

```text
resolved: bool
```

as an independent input.

Exact witness: with the same badness pattern

\[
(\text{True},\text{False},\text{True})
\]

and previous active index `2`,

- `resolved=False` keeps index `2`;
- `resolved=True` reselects index `0`.

Therefore badness flags alone do not determine selector evolution.

A physical construction still needs a resolve predicate

\[
\boxed{
\mathcal R_i[u,\omega,F,Q_{\rm tot},\rho,\ldots](t)
\in\{0,1\}
}
\]

or an equivalent event rule.

**Classification: Exact independence witness; programme-specific resolve predicate
open-literal.**

---

## 5. The first-bad selector and moving quantile/shell cuts are different objects

The clock/cut audit derived for a moving localization map

\[
G_Q=\dot Q+T_{\rm out}Q-QT_{\rm in}
\]

and the exact level-set quantile speed law.  Those formulas concern a **geometric
restriction map** whose boundary moves continuously through state space.

By contrast, on an unresolved hysteresis branch the literal `M_fb` has

\[
\dot M_{\rm fb}=0.
\]

A finite-matrix type witness makes the independence explicit:

\[
M_{\rm fb}=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
Q(a)=\begin{pmatrix}a&0\\0&1-a\end{pmatrix}.
\]

Then

\[
\partial_aM_{\rm fb}=0,
\qquad
\partial_aQ\ne0.
\]

Conversely, `M_fb` can jump at a resolve event while the same `Q(a)` is unchanged.

Thus

\[
\boxed{
\text{first-bad event selector}
\ne
\text{moving quantile/shell cut}.
}
\]

**Classification: Exact type-separation witness.**

---

## 6. What remains of the covariant support term `G_M`

The cycle-selector factorization remains exact:

\[
G_{KM}=G_KM+KG_M,
\qquad
G_M=\dot M+A_gM-MA_g.
\]

For the literal frozen first-bad projector,

\[
\boxed{
\dot M_{\rm fb}=0
}
\]

between events.  A nonzero continuous `G_M` can therefore still arise from the
**germ-frame transport commutator**

\[
A_gM-MA_g,
\]

which is the already audited interface/cut current in a non-co-moving germ frame.
It is not a derivative of the unspecified badness threshold.

If the germ frame is co-moving with the frozen support, this commutator also
vanishes and all selector change is concentrated at finite entry/resolve events.

Moving quantile/shell maps retain their own `Qdot/Hdot_shell` faces separately.

**Classification: Exact decomposition and rigorous physical typing.**

---

## 7. Transversal score crossing, if later defined, determines event time but not a
continuous `Mdot`

Suppose a future programme definition supplies a smooth physical score

\[
h_i(t)=\mathcal B_i(t)-\theta_i(t).
\]

At a transversal crossing `h_i(t_*)=0`, `h_i'(t_*)!=0`, the Boolean flag changes at
an isolated event time.  Under the current hysteresis semantics:

- if another germ is active and unresolved, the crossing changes no selector state;
- if no germ is active, it can create a finite entry jump;
- after resolve, it can affect the finite re-selection jump.

So even after badness scores are supplied, threshold crossing determines **event
timing**, not a continuous first-bad support velocity.

**Classification: Rigorous consequence of the literal hysteresis rule, conditional
on a smooth transversal future badness definition.**

---

## 8. Updated physical data ledger

The selector/localization construction now requires three distinct missing data
objects:

### A. First-bad entry/badness data

\[
\boxed{
\mathcal B_i(t),\;\theta_i(t)
}
\]

which generate `bad_flags` and physical entry/reselection event times.

### B. Resolve data

\[
\boxed{
\mathcal R_i(t)
}
\]

which decide when the hysteresis freeze is released.

### C. Moving localization geometry

A scalar/state observable `g_Q` (and shell analogue) whose level sets define
`Q_s/H_s`; once supplied, its speed is already fixed by the exact probability-current
Reynolds/coarea law.

These three roles must not be assigned to one symbol merely because all are called
"first-bad localization" in prose.

**Classification: Exact type ledger; all three programme-specific PDE definitions
remain to be supplied where indicated.**

---

## 9. Consequence for the restart frontier

The immediate missing theorem is no longer

> find an estimate for selector motion.

It is the more primitive PDE-definition problem:

\[
\boxed{
\text{Which literal Navier--Stokes event declares a germ bad, and which event
resolves it?}
}
\]

Only after those are defined can one ask whether their event sequence couples to
the reverse-age Kelvin scale/support/covariance laws strongly enough to close a
restart argument.

The local positive enstrophy-growth gate already audited in the repository is not
silently promoted to this role; it is only a necessary local growth condition.
A separate amplitude-scaled ABC audit further excludes raw finite thresholds on
vorticity/enstrophy/stretching/Kelvin q.v. and their instantaneous ratio as standalone
continuation-failure predicates, while carefully preserving the local-maximum
hypothesis of the growth gate.

See `docs/first_bad_candidate_exclusions_audit.md`.

`S^int`, uniform collapse, restart capacity, and continuation remain open.

**Classification: Structural refinement; no continuation/restart conclusion.**
