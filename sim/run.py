"""CLI entrypoint for HODLXXI repeated-game simulation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from metrics import compute_all
from model import simulate


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run HODLXXI repeated-game simulation")
    parser.add_argument("--config", type=str, help="Path to JSON config", default=None)
    parser.add_argument("--population-size", type=int, default=40)
    parser.add_argument("--rounds", type=int, default=100)
    parser.add_argument("--strategy-set", nargs="+", default=["TFT", "ALLD", "ALLC", "GRIM"])
    parser.add_argument("--noise", type=float, default=0.02)
    parser.add_argument("--discount", type=float, default=0.98)
    parser.add_argument("--lock-horizon", type=float, default=5.0)
    parser.add_argument("--lock-ratio", type=float, default=0.4)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--h-max", type=float, default=10.0)
    parser.add_argument("--output-dir", type=str, default="sim/output")
    return parser.parse_args()


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    args = parse_args()
    params = vars(args).copy()

    if args.config:
        cfg = load_config(args.config)
        params.update(cfg)

    data = simulate(
        population_size=int(params["population_size"]),
        rounds=int(params["rounds"]),
        strategy_set=list(params["strategy_set"]),
        noise=float(params["noise"]),
        discount=float(params["discount"]),
        lock_horizon=float(params["lock_horizon"]),
        lock_ratio=float(params["lock_ratio"]),
        seed=int(params["seed"]),
    )
    metrics = compute_all(data, h_max=float(params["h_max"]))

    output_dir = Path(params["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)

    data_path = output_dir / "run_data.json"
    metrics_path = output_dir / "metrics.json"
    payoffs_path = output_dir / "payoffs.png"
    run_metrics_path = output_dir / "run_metrics.png"

    data_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    metrics_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    print(f"Saved: {data_path}")
    print(f"Saved: {metrics_path}")

    try:
        from plots import plot_metrics, plot_payoffs

        plot_payoffs(data["payoffs"], payoffs_path)
        plot_metrics(metrics, run_metrics_path)
        print(f"Saved: {payoffs_path}")
        print(f"Saved: {run_metrics_path}")
    except ModuleNotFoundError as exc:
        print(f"Plot generation skipped (missing dependency): {exc}")


if __name__ == "__main__":
    main()
