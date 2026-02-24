# Mathematical Appendix

## Symbols
- `N`: population size.
- `T`: number of repeated rounds.
- `δ`: discount factor.
- `H_i`: lock horizon for agent `i`.
- `λ_i`: capital lock ratio for agent `i`.
- `η`: execution/noise probability.
- `π_i`: cumulative payoff of agent `i`.
- `φ(H_i, λ_i, κ)`: lock-imposed expected penalty on opportunistic defection.

## Stage-game payoff template (Prisoner's Dilemma)
Let `T > R > P > S`.

| i \ j | C | D |
|---|---:|---:|
| C | (R, R) | (S, T) |
| D | (T, S) | (P, P) |

## Effective defection utility
`u_i^D,eff = u_i^D - φ(H_i, λ_i, κ)`

A simple baseline form used in simulation:
`φ = α * λ_i * log(1 + H_i)` where `α > 0`.

## Lock Duration Index (LDI)
For run `r` with horizon upper bound `H_max`:

`LDI_r = (1/N) * Σ_i (H_i / H_max)`

If heterogeneous lock schedules exist over time:

`LDI_r = (1/(N*T*H_max)) * Σ_t Σ_i H_i(t)`

## Defection Cost Ratio (DCR)
For observed defections `d ∈ D`:

`DCR_r = mean_d [ penalty_d / max(ε, gross_gain_d) ]`

where `gross_gain_d = u_d^D - u_d^C` and `ε` avoids division by zero.

## Reciprocity Consistency Score (RCS)
Given each pair `(i,j)` with interaction sequence length `L_ij`, define reciprocal alignment score `a_ij ∈ [0,1]` (fraction of rounds where behavior matches strategy-consistent reciprocity condition).

`RCS_r = mean_{(i,j)} a_ij`

## Stability horizon proxy
Define `δ*(H)` as the minimum discount factor where cooperative play frequency exceeds threshold `q` under fixed noise.

Hypothesis: `dδ*/dH < 0` over relevant parameter intervals.
