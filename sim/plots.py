"""Plot helpers for HODLXXI simulation outputs."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import matplotlib.pyplot as plt


def plot_payoffs(payoffs: List[float], output_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(range(len(payoffs)), payoffs)
    ax.set_xlabel("Agent index")
    ax.set_ylabel("Discounted payoff")
    ax.set_title("Payoff distribution")
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)


def plot_metrics(metrics: Dict[str, float], output_path: Path) -> None:
    keys = list(metrics.keys())
    values = [metrics[k] for k in keys]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(keys, values)
    ax.set_title("Run metrics")
    ax.set_ylabel("Value")
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
