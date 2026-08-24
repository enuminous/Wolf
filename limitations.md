# Limitations and Falsification

WOLF is a research monitor, not a validated safety system.

## Known limitations

- Strongly correlated channels can create apparent distributed evidence.
- Hazard directions may be misspecified.
- Dynamic weights can overfit.
- Baseline drift can masquerade as degradation.
- Nonstationary systems require careful recalibration.
- A tuned multivariate baseline may fully match or exceed WOLF.

## Falsification criteria

The central WOLF hypothesis is weakened or falsified if:

1. Tuned conventional monitors achieve equivalent or better lead time at matched false-alarm rates.
2. Removing recursion causes no meaningful loss.
3. Removing directional information causes no meaningful loss in directional precursor tasks.
4. Removing distributed-contribution constraints improves generalization.
5. Performance gains disappear on held-out environments.
6. Gains require privileged information unavailable to baselines.

## Claim boundary

Internal coherence is not external truth.

A high WOLF score means only that the configured monitor has detected a pattern matching its precursor model. It does not prove that failure will occur.
