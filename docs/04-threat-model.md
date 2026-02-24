# Threat Model and Attack Surface

## Scope
Threats to validity and mechanism integrity in cryptographic reciprocity systems.

## Adversaries
1. Rational opportunists maximizing short-term payoff.
2. Coordinated colluding groups.
3. Sybil operators creating low-cost pseudo-identities.
4. External attackers offering out-of-band bribes.
5. Macro shocks (black swans) forcing liquidity exits.

## Attack categories

### A. Sybil amplification
- **Vector**: create many identities to harvest cooperation then defect.
- **Impact**: degrades trust calibration and inflates apparent reciprocity.
- **Mitigations (hypothesized)**: identity-aging weights, minimum lock thresholds, graph-based anomaly detection.

### B. Collusive lock theater
- **Vector**: allied agents simulate credible locks but coordinate private side channels.
- **Impact**: false positive commitment signals.
- **Mitigations**: counterparty diversity requirements, random audit games, anti-concentration heuristics.

### C. Liquidity black swan
- **Vector**: sudden market/liability shock raises immediate cash preference.
- **Impact**: cooperative agents involuntarily defect.
- **Mitigations**: emergency unwind paths, staggered maturities, adaptive lock ratios.

### D. External payoff attacks
- **Vector**: bribes or coercion larger than modeled lock penalties.
- **Impact**: mechanism loses deterrence.
- **Mitigations**: increase bond size, multi-party attestation, reputational slashing layers.

### E. Script and implementation risk
- **Vector**: malformed scripts, policy incompatibility, wallet UX failures.
- **Impact**: unspendable funds or unenforceable constraints.
- **Mitigations**: formal descriptor validation, test vectors, staged deployment.

## Black swan analysis checklist
- Parameter regime where `DCR < 1`.
- Correlated defaults due to shared exposure.
- Temporary chain congestion raising execution cost.
- Regulatory constraints blocking expected spend path.

## Residual risk statement
No lock mechanism guarantees cooperation under all external incentives. Claims should remain conditional on adversary budget, enforcement reliability, and liquidity environment.
