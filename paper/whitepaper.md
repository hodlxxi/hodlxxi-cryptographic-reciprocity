# HODLXXI Whitepaper Draft

## Abstract
HODLXXI studies whether cryptographic capital constraints can extend cooperative stability in repeated strategic environments. The central **hypothesis** is that persistent public-key identity plus script-constrained Bitcoin capital (timelocks and conditional spend paths) increases the cost of defection relative to cooperation, thereby shifting equilibrium behavior in repeated interaction. This document separates implemented system elements from untested theoretical claims.

## 1. Introduction
Classical reciprocal altruism and repeated-game models explain cooperation when future interaction is expected. HODLXXI proposes an additional mechanism: ex ante capital locking that is publicly verifiable and identity-linked.

Research objective: evaluate whether verifiable lock commitments alter incentive geometry enough to improve long-horizon reciprocity.

## 2. Background
- **Reciprocal altruism (Trivers)**: cooperation can persist when actors condition future behavior on past conduct.
- **Repeated prisoner’s dilemma**: cooperative equilibria depend on discount factor and punishment credibility.
- **ESS framing**: strategy robustness requires resistance to invasion by defect-heavy mutants.
- **Bitcoin constraints**: timelocks (`CLTV`, `CSV`) and script paths can encode delayed access and contingency conditions.

## 3. System model
### 3.1 Existing components (today)
- Persistent public-key identity in a live Bitcoin-linked system.
- Script-aware handling of constrained spend structures.
- Verifiable historical traces tied to cryptographic keys.

### 3.2 Proposed research mechanism (untested)
- Agents post lock commitments with horizon `H`.
- Defection triggers economic penalties via inaccessible or delayed capital.
- Repeated interaction updates partner selection and trust weights from verifiable history.

## 4. Formalization
Let repeated stage game `G` have actions `{C, D}` and discount factor `δ ∈ (0,1)`. For agent `i`, define lock horizon `H_i ≥ 0` and lock ratio `λ_i ∈ [0,1]`.

Define effective defection payoff:

`u_i^D,eff = u_i^D - φ(H_i, λ_i, κ)`

where `φ` is a lock-imposed penalty function parameterized by settlement/liquidity cost `κ`.

**Hypothesis H1**: increasing `H` and/or `λ` increases `φ`, reducing profitable one-shot defection frequency.

## 5. Metrics
Primary indices (defined formally in `docs/03-metrics.md` and `paper/appendix-math.md`):
- `LDI`: Lock Duration Index.
- `DCR`: Defection Cost Ratio.
- `RCS`: Reciprocity Consistency Score.

## 6. Threat model summary
Adversarial scenarios include sybil identity inflation, collusive lock simulations, liquidity black swans, and exogenous bribery that dominates lock penalties. The mechanism is only credible when external payoff channels are bounded relative to cryptographic penalties.

## 7. Experiments and simulation plan
- Baseline repeated-game simulation over strategy sets `{ALLC, ALLD, TFT, GRIM}`.
- Parameter sweeps over `δ`, noise, `H`, and population composition.
- Hypothesis tests:
  - H1: lock severity lowers defection incidence.
  - H2: lock constraints increase persistence of reciprocal clusters.
  - H3: under high exogenous shocks, lock advantage can collapse.

## 8. Limitations
- Current model is stylized and may omit wallet behavior, legal constraints, and capital heterogeneity.
- Public verifiability does not imply truthful motive revelation.
- Simulation outcomes are not empirical proof.

## 9. Ethics
The framework is mechanism-design oriented, not moral ranking. Identity-linked financial constraints can create exclusion and surveillance risks; all empirical extensions should include privacy boundaries, minimization, and opt-in consent.

## 10. Conclusion
HODLXXI offers a testable framework: cryptographic commitments may alter repeated-game incentives by raising defections’ effective costs. This remains a hypothesis pending robust simulation and empirical validation.

## 11. References
See `paper/bibliography.md`.
