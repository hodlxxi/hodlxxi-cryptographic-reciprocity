# HODLXXI Research Hub

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Reproducibility: Simulation Scaffold](https://img.shields.io/badge/reproducibility-simulation%20scaffold-blue)](sim/README.md)

HODLXXI is a Bitcoin-native research program on long-horizon cooperation under cryptographic capital constraints. This repository is an academic-friendly workspace that separates:

- **What exists today**: a live Bitcoin-based system using persistent public-key identity and script-constrained capital primitives.
- **What is hypothesized**: claims that such constraints can improve cooperation stability over longer horizons.

## Research question
Can script-constrained capital locking (timelocks + conditional spend paths) function as a measurable commitment device that increases the stability horizon of reciprocal cooperation in repeated strategic interaction?

## What is inside
- `paper/`: whitepaper draft, bibliography, and mathematical appendix.
- `docs/`: technical research notes (formal model, metrics, threats, experiments, data sources, FAQ).
- `glossary/`: canonical terminology.
- `sim/`: reproducible Python simulation scaffold for repeated games under lock constraints.
- `.github/`: issue and pull request templates for research and engineering collaboration.

## How to cite
Use `CITATION.cff` for machine-readable citation metadata. A suggested citation entry is included there.

## License note
This repository uses the **MIT License** to maximize academic and engineering reuse while preserving attribution and warranty disclaimers.

## Contributing
See `CONTRIBUTING.md` for research proposals, simulation contribution standards, and citation expectations.

## Current status summary
This initial commit provides:
1. A structured research documentation hub.
2. A draft whitepaper with explicit hypotheses and limitations.
3. A minimal, extendable simulation scaffold with JSON-configurable experiments.
4. Threat-model and metric definitions for empirical follow-on work.
