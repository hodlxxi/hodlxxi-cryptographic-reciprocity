# Contributing to HODLXXI Research

Thank you for contributing. This repository welcomes academic, engineering, and mixed-method contributions.

## Contribution types
- **Theory**: formal models, assumptions, proofs/sketches, critiques.
- **Simulation**: strategy models, metrics implementations, reproducibility improvements.
- **Empirical**: data schema, measurement plans, falsification attempts.
- **Documentation**: clarifications, definitions, references, writing quality.

## Ground rules
1. Separate observations from hypotheses.
2. Include citations for claims about prior literature.
3. Document assumptions explicitly.
4. Keep contributions reproducible.

## Workflow
1. Open an issue using a template in `.github/ISSUE_TEMPLATE/`.
2. Propose scope and acceptance criteria.
3. Submit PR with:
   - Rationale and expected impact.
   - Any equations or metric changes.
   - Reproduction steps for simulation changes.
   - References added to `paper/bibliography.md` if relevant.

## Simulation contributions
- Use Python 3.10+.
- Keep new behavior configurable via CLI flags or JSON config.
- Include at least one runnable example command.
- Preserve deterministic runs through `--seed` whenever possible.

## Citation format
Use a simple, consistent format in `paper/bibliography.md`:
`Author, Year, Title, Venue/Publisher, Link (if available)`.

## Quality checks before PR
- `python sim/run.py --help`
- `python sim/run.py --config sim/examples/baseline_tft_vs_defect.json`
- Ensure generated outputs are not committed from `sim/output/` (except `.gitkeep`).

## Style
- English only.
- Avoid hype and marketing language.
- Prefer concise technical writing.
