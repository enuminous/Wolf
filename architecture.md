# WOLF Architecture

## Pipeline

1. Observation Adapter
2. Baseline Standardizer
3. Directional Residual Engine
4. Reliability/Uncertainty Weighting
5. Distributed Contribution Analyzer
6. Temporal Accumulator
7. Relational Coherence Monitor
8. Alarm Controller
9. Provenance Logger

## Inputs

Each observation can include:

```json
{
  "timestamp": 120,
  "channel": "temperature_gradient",
  "value": 0.82,
  "baseline_mean": 0.0,
  "baseline_std": 1.0,
  "hazard_direction": 1,
  "reliability": 0.96,
  "uncertainty": 0.08
}
```

## Outputs

```json
{
  "latent_score": 0.61,
  "instantaneous_score": 0.55,
  "coherence": 0.44,
  "effective_channels": 4.2,
  "alarm": false,
  "contributors": {
    "temperature_gradient": 0.16,
    "pressure_variance": 0.13
  }
}
```

## Design principle

WOLF must preserve explainability at the channel level.

Every aggregate alarm should answer:
- which channels contributed,
- how strongly,
- in what direction,
- over what time interval,
- with what uncertainty.

## Integration

MAGPIE may audit the provenance of WOLF's evidence and claims.

Downstream Zoo animals can consume WOLF's state vector without losing the original channel contribution map.
