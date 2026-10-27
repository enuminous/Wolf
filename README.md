# WOLF — EFMW Zoo #25

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Wolf) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#zoo-index-and-agents)

<details open>
<summary><strong>On this page</strong></summary>

- [Core idea](#core-idea)
- [Status](#status)
- [Repository contents](#repository-contents)
- [Minimal model](#minimal-model)
- [Scientific requirement](#scientific-requirement)
- [Quick start](#quick-start)
- [Zoo position](#zoo-position)


</details>

**Related repositories:** [Tortoise](https://github.com/enuminous/Tortoise) · [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Elephant](https://github.com/enuminous/Elephant) · [Magpie](https://github.com/enuminous/Magpie) · [Chameleon](https://github.com/enuminous/Chameleon) · [Turtle](https://github.com/enuminous/Turtle)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


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
