# WOLF — EFMW Zoo #25

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Wolf) · This repository is linked through its source; GitHub Pages is not enabled.
<!-- ENUMINOUS-NETWORK:END -->

**Weighted Observation of Latent Failure**

WOLF is a candidate EFMW-inspired monitoring framework for detecting weak, distributed, individually non-alarming signals that collectively indicate an emerging system failure.

## Core idea

Many serious failures are preceded by small deviations across several channels. None may cross a conventional threshold on its own. WOLF aggregates these weak observations while preserving channel provenance, temporal direction, uncertainty, and matched-false-alarm evaluation.

The canonical WOLF question is:

> Are multiple weak signals beginning to move coherently toward failure even though no single sensor has clearly failed?

## Status

This repository is an experimental research package. The mathematical forms here are candidate operationalizations, not validated physical laws. A WOLF advantage must be demonstrated against strong baselines under matched information access, compute, and false-alarm rates.

## Repository contents

- `theory.md` — conceptual and mathematical specification
- `architecture.md` — system architecture and data flow
- `latent_failure_model.md` — state-space formulation
- `limitations.md` — falsification criteria and claim boundaries
- `wolf.py` — reference implementation
- `benchmark.py` — synthetic benchmark harness
- `ablations.py` — ablation experiments
- `test_wolf.py` — unit tests
- `example.py` — worked example
- `paper.md` — paper-style technical draft
- `CITATION.cff`
- `LICENSE`

## Minimal model

For channels `i = 1..n`, WOLF computes standardized deviations `z_i(t)` and combines them:

`L_t = sum_i w_i(t) * g_i(z_i(t), dz_i/dt, uncertainty_i)`

The weighted latent-failure score is then temporally accumulated:

`R_t = lambda * R_{t-1} + (1-lambda) * L_t`

A candidate alarm occurs when the aggregate exceeds a preregistered threshold while enough independent channels contribute.

## Scientific requirement

WOLF is useful only if it detects structured precursor states earlier than tuned baselines such as CUSUM, EWMA, multivariate control charts, Kalman residual monitoring, change-point detection, or matched ensembles.

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_wolf.py
```

## Zoo position

MAGPIE #24 asks whether claims remain grounded.

**WOLF #25 asks whether failure is beginning to emerge before any single component makes it obvious.**
