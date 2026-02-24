# Metrics Specification

This document defines primary metrics for HODLXXI simulations and future empirical studies.

## 1) Lock Duration Index (LDI)

### Definition
For static lock horizon `H_i` and global normalization `H_max > 0`:

`LDI = (1/N) * Σ_i (H_i / H_max)`

Range: `[0, 1]` if `H_i <= H_max`.

### Interpretation
Higher `LDI` indicates stronger aggregate time commitment.

### Edge cases
- If `H_max = 0`, return undefined (`NaN`) and flag configuration error.
- If `N = 0`, metric undefined.

## 2) Defection Cost Ratio (DCR)

### Definition
For each observed defection event `d`:

`dcr_d = penalty_d / max(ε, gross_gain_d)`

Aggregate:

`DCR = mean_d dcr_d`

where `gross_gain_d` is gain from defecting over cooperating in equivalent context.

### Interpretation
- `DCR < 1`: penalty smaller than gain.
- `DCR ≈ 1`: parity.
- `DCR > 1`: defection economically dominated under modeled assumptions.

### Edge cases
- No defections: return `0` with note `no_defections=True`.
- Non-positive gain scenarios: use `ε` denominator and emit warning.

## 3) Reciprocity Consistency Score (RCS)

### Definition
For each interacting pair `(i,j)`, compute fraction of rounds where observed action aligns with declared strategy-conditioned reciprocity rule. Let score `a_ij ∈ [0,1]`.

`RCS = mean_{(i,j)} a_ij`

### Interpretation
Higher `RCS` means behavior is more consistent with reciprocal strategies (e.g., TFT-like behavior under low noise).

### Edge cases
- Sparse interactions: require minimum round count threshold.
- High noise: report `RCS` with noise parameter for contextualization.

## 4) Auxiliary metrics
- Cooperation rate `CR = cooperative_actions / total_actions`.
- Payoff variance for inequality tracking.
- Strategy survival share by class.
