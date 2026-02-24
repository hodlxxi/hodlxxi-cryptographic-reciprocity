"""Core repeated-game simulation primitives for HODLXXI."""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Dict, List, Tuple

Action = str
Strategy = str


@dataclass
class Agent:
    idx: int
    strategy: Strategy
    lock_horizon: float
    lock_ratio: float


PD_PAYOFFS: Dict[Tuple[Action, Action], Tuple[float, float]] = {
    ("C", "C"): (3.0, 3.0),
    ("C", "D"): (0.0, 5.0),
    ("D", "C"): (5.0, 0.0),
    ("D", "D"): (1.0, 1.0),
}


def choose_action(strategy: Strategy, my_hist: List[Action], opp_hist: List[Action]) -> Action:
    if strategy == "ALLC":
        return "C"
    if strategy == "ALLD":
        return "D"
    if strategy == "TFT":
        return "C" if not opp_hist else opp_hist[-1]
    if strategy == "GRIM":
        return "D" if "D" in opp_hist else "C"
    raise ValueError(f"Unknown strategy: {strategy}")


def lock_penalty(lock_horizon: float, lock_ratio: float, alpha: float = 0.8) -> float:
    return alpha * lock_ratio * (lock_horizon + 1.0) ** 0.5


def simulate(
    population_size: int,
    rounds: int,
    strategy_set: List[Strategy],
    noise: float,
    discount: float,
    lock_horizon: float,
    lock_ratio: float,
    seed: int,
) -> dict:
    rng = random.Random(seed)
    agents = [
        Agent(i, strategy_set[i % len(strategy_set)], lock_horizon, lock_ratio)
        for i in range(population_size)
    ]

    histories: Dict[Tuple[int, int], Tuple[List[Action], List[Action]]] = {}
    payoffs = [0.0 for _ in agents]
    defections = 0
    cooperations = 0
    events = []

    for t in range(rounds):
        order = list(range(population_size))
        rng.shuffle(order)
        for k in range(0, population_size - 1, 2):
            i, j = order[k], order[k + 1]
            key = (min(i, j), max(i, j))
            h_i, h_j = histories.get(key, ([], []))
            ai = choose_action(agents[i].strategy, h_i, h_j)
            aj = choose_action(agents[j].strategy, h_j, h_i)

            if rng.random() < noise:
                ai = "D" if ai == "C" else "C"
            if rng.random() < noise:
                aj = "D" if aj == "C" else "C"

            pi, pj = PD_PAYOFFS[(ai, aj)]
            gross_i = 2.0 if ai == "D" and aj == "C" else 0.0
            gross_j = 2.0 if aj == "D" and ai == "C" else 0.0

            pen_i = lock_penalty(lock_horizon, lock_ratio) if ai == "D" else 0.0
            pen_j = lock_penalty(lock_horizon, lock_ratio) if aj == "D" else 0.0

            pi_eff = pi - pen_i
            pj_eff = pj - pen_j

            weight = discount**t
            payoffs[i] += weight * pi_eff
            payoffs[j] += weight * pj_eff

            defections += int(ai == "D") + int(aj == "D")
            cooperations += int(ai == "C") + int(aj == "C")

            events.append(
                {
                    "round": t,
                    "i": i,
                    "j": j,
                    "a_i": ai,
                    "a_j": aj,
                    "penalty_i": pen_i,
                    "penalty_j": pen_j,
                    "gross_i": gross_i,
                    "gross_j": gross_j,
                    "strategy_i": agents[i].strategy,
                    "strategy_j": agents[j].strategy,
                }
            )

            h_i.append(ai)
            h_j.append(aj)
            histories[key] = (h_i, h_j)

    return {
        "agents": [a.__dict__ for a in agents],
        "payoffs": payoffs,
        "events": events,
        "summary": {
            "defections": defections,
            "cooperations": cooperations,
            "total_actions": defections + cooperations,
        },
    }
