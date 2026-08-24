# WOLF Theory

## 1. Problem definition

A monitored system emits observations:

`y_t = [y_1(t), ..., y_n(t)]`

Many conventional monitors alarm when one variable exceeds a threshold or a global residual becomes large. WOLF targets a different habitat: weakly expressed, distributed, directional precursors.

## 2. Standardization

For each channel:

`z_i(t) = (y_i(t) - mu_i) / sigma_i`

where `mu_i` and `sigma_i` are frozen baseline statistics.

Uncertainty may be represented as `u_i(t) >= 0`.

## 3. Directional precursor term

For a known hazardous direction `d_i in {-1, 0, +1}`:

`q_i(t) = d_i * z_i(t)`

A positive value means movement toward the hazardous regime.

Optionally include trend:

`v_i(t) = d_i * (z_i(t) - z_i(t-1))`

## 4. Local weak-signal contribution

One candidate contribution is:

`c_i(t) = reliability_i * max(0, alpha*q_i(t) + beta*v_i(t) - gamma*u_i(t))`

This does not require any single channel to be extreme.

## 5. Dynamic weighting

Weights may reflect reliability, historical precursor relevance, and current uncertainty:

`w_i(t) = r_i * h_i / (1 + u_i(t))`

normalized so:

`sum_i w_i(t) = 1`

## 6. Latent failure surface

`L_t = sum_i w_i(t) * c_i(t)`

A temporal state tracks persistence:

`R_t = lambda*R_{t-1} + (1-lambda)*L_t`

with `0 <= lambda < 1`.

## 7. Distributed contribution condition

To prevent one channel from dominating, define:

`N_eff(t) = 1 / sum_i p_i(t)^2`

where `p_i` is normalized positive contribution.

An alarm can require:

`R_t > theta_R AND N_eff(t) > theta_N`

This explicitly rewards distributed evidence.

## 8. Relational coherence

A further candidate term measures whether several channels are moving together in their hazardous directions:

`K_t = mean_{i<j}(sign(v_i) * sign(v_j))`

or a correlation-based equivalent over a sliding window.

WOLF may then use:

`S_t = a*R_t + b*K_t`

## 9. EFMW interpretation

The EFMW-inspired element is not a magical scalar. It is the recursive preservation of state, relation, direction, and weak cross-channel coherence over time.

WOLF should be tested as a candidate sequential monitor, not asserted as universally superior.

## 10. Falsifiable prediction

Pre-register a structured-complexity interaction:

WOLF's advantage should increase when:
- precursor information is distributed,
- individual channels remain sub-threshold,
- directionality matters,
- partial observability increases,
- temporal persistence matters,

and should disappear under unstructured noise or when a single-channel threshold already captures the failure.

If this interaction does not replicate, the claimed habitat is unsupported.
