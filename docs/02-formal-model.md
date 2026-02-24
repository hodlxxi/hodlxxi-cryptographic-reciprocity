# Formal Model

## Assumptions
1. Agents interact in repeated pairings over horizon `T`.
2. Each agent has persistent identifier key `k_i`.
3. Agent `i` optionally commits lock tuple `(H_i, λ_i, script_i)`.
4. Defection events produce expected lock-related opportunity cost `φ_i`.
5. Observation is imperfect under noise `η`.

## State
At round `t`, state includes:
- strategy profile `s(t)`;
- lock profile `L(t) = {(H_i, λ_i)}_i`;
- history tensor `h(t)` with action observations;
- matching graph `M(t)`.

## Utility
Per-round utility:

`u_i(t) = g_i(a_i(t), a_j(t)) - c_i(lock maintenance) - ψ_i(shocks)`

If defection occurs and enforcement conditions trigger:

`u_i(t) <- u_i(t) - φ(H_i, λ_i, κ, t)`

## Population update (optional extension)
Replicator-style update for strategy fraction `x_m`:

`x_m(t+1) = x_m(t) * (1 + β(\bar{π}_m - \bar{π}))`

with normalization over strategy set.

## Testable outputs
- Cooperation rate over time.
- Mean payoff under varying `H`.
- `DCR` and `RCS` response surfaces.
