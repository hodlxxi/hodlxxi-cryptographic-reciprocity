# Simulation Scaffold

This directory provides a minimal, extendable repeated-game simulation for testing HODLXXI hypotheses.

## Install
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r sim/requirements.txt
```

## Run
```bash
python sim/run.py --help
python sim/run.py --config sim/examples/baseline_tft_vs_defect.json
```

## Example direct CLI
```bash
python sim/run.py \
  --population-size 60 \
  --rounds 150 \
  --strategy-set TFT ALLD GRIM \
  --noise 0.03 \
  --discount 0.97 \
  --lock-horizon 8 \
  --lock-ratio 0.45 \
  --seed 42
```

## Outputs
Generated in `sim/output/`:
- `run_data.json`
- `metrics.json`
- `payoffs.png`
- `run_metrics.png`

## How to reproduce
1. Use a committed config JSON file from `sim/examples/`.
2. Record Python version and package versions.
3. Run with fixed `--seed`.
4. Commit only configuration and code changes, not generated outputs.
