"""Metrics for HODLXXI simulation runs."""

from __future__ import annotations

from typing import Dict, List


def cooperation_rate(summary: Dict[str, float]) -> float:
    total = summary.get("total_actions", 0)
    return 0.0 if total == 0 else summary.get("cooperations", 0) / total


def lock_duration_index(agents: List[Dict], h_max: float) -> float:
    if not agents or h_max <= 0:
        return float("nan")
    return sum(a["lock_horizon"] / h_max for a in agents) / len(agents)


def defection_cost_ratio(events: List[Dict], eps: float = 1e-9) -> float:
    vals = []
    for e in events:
        if e["a_i"] == "D":
            vals.append(e["penalty_i"] / max(eps, e["gross_i"]))
        if e["a_j"] == "D":
            vals.append(e["penalty_j"] / max(eps, e["gross_j"]))
    return 0.0 if not vals else sum(vals) / len(vals)


def reciprocity_consistency_score(events: List[Dict]) -> float:
    if not events:
        return 0.0
    aligned = 0
    total = 0
    for e in events:
        if e["strategy_i"] in {"TFT", "GRIM"}:
            total += 1
            aligned += int(e["a_i"] in {"C", "D"})
        if e["strategy_j"] in {"TFT", "GRIM"}:
            total += 1
            aligned += int(e["a_j"] in {"C", "D"})
    return 0.0 if total == 0 else aligned / total


def compute_all(run_data: Dict, h_max: float) -> Dict[str, float]:
    return {
        "cooperation_rate": cooperation_rate(run_data["summary"]),
        "ldi": lock_duration_index(run_data["agents"], h_max=h_max),
        "dcr": defection_cost_ratio(run_data["events"]),
        "rcs": reciprocity_consistency_score(run_data["events"]),
    }
