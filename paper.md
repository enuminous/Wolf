# WOLF: Weighted Observation of Latent Failure

## Abstract

We introduce WOLF, an experimental sequential monitoring framework for detecting distributed weak-signal precursors to system failure. WOLF aggregates standardized directional deviations across multiple channels while preserving uncertainty, channel-level provenance, temporal persistence, and a measure of effective distributed contribution. The intended habitat is one in which no single sensor is strongly anomalous, but several weak signals jointly evolve toward a hazardous regime.

The framework is explicitly falsifiable. Its primary evaluation target is lead time at matched false-alarm rate relative to strong conventional baselines. WOLF is not claimed to be universally superior; rather, it predicts an interaction between performance advantage and structured complexity, including distributed precursors, partial observability, directional residuals, and temporal persistence.

## 1. Motivation

Catastrophic failures often emerge gradually. Conventional threshold monitors are effective when one observable becomes strongly abnormal. They may be less effective when precursor information is weakly distributed across several channels.

WOLF treats these sub-threshold deviations as a relational time-series problem.

## 2. Model

For channel i:

`z_i(t) = (y_i(t)-mu_i)/sigma_i`

Directional hazard projection:

`q_i(t) = d_i z_i(t)`

Trend:

`v_i(t) = d_i(z_i(t)-z_i(t-1))`

Local contribution:

`c_i(t)=max(0, alpha q_i + beta v_i - gamma u_i)`

Weighted aggregate:

`L_t=sum_i w_i c_i`

Recursive persistence:

`R_t=lambda R_{t-1}+(1-lambda)L_t`

Distributed-contribution statistic:

`N_eff = 1/sum_i p_i^2`

A candidate alarm requires both sufficient persistent score and sufficient number of effective contributors.

## 3. Evaluation

Primary endpoint:
- failure lead time

Constraint:
- matched false-alarm rate

Baselines:
- scalar thresholding
- EWMA
- CUSUM
- multivariate control chart
- Kalman/state-space residual monitoring
- change-point detection
- tuned ensemble

## 4. Ablations

- remove recursion
- remove directional information
- equalize all reliability weights
- remove uncertainty penalty
- remove distributed-contribution requirement
- shuffle channel labels
- replace WOLF with flat residual magnitude

## 5. Predicted habitat

WOLF should gain relative advantage as:
- precursor distribution increases,
- individual signal amplitude decreases,
- temporal depth increases,
- partial observability increases,
- relational structure increases.

Its advantage should fall under:
- single dominant precursor channels,
- completely unstructured noise,
- extremely high noise ceilings.

## 6. Claim boundaries

The implementation is a research candidate. Positive synthetic results are insufficient to establish real-world utility. Independent replication on held-out environments is required.
