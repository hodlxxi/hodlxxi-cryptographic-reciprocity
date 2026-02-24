# Experiments Plan

## 1. Simulated experiments

### E1: Baseline strategy competition
- Vary strategy composition across `{ALLC, ALLD, TFT, GRIM}`.
- Sweep `δ`, noise `η`, lock horizon `H`, lock ratio `λ`.
- Outputs: cooperation rate, payoff distributions, `LDI`, `DCR`, `RCS`.

### E2: Shock robustness
- Inject exogenous shock rounds where liquidity penalty increases.
- Evaluate collapse thresholds of cooperation clusters.

### E3: Adversarial population
- Add sybil cluster and colluding subgroup.
- Measure metric degradation and false reciprocity inflation.

## 2. On-chain derived experiments (future)
- Define lock-like proxy events from script descriptors/timelock usage.
- Track longitudinal behavior of identity-linked entities.
- Correlate commitment proxies with repeated interaction proxies.

## 3. Hybrid experiments
- Use observed on-chain distributions to parameterize simulation priors.
- Compare simulated trend envelopes with observed summary statistics.

## Reproducibility requirements
- Versioned config files.
- Fixed random seeds.
- Saved metrics JSON and plots.
- Explicit software environment in `sim/requirements.txt`.
