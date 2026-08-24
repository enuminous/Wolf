# Latent Failure Model

## Hidden-state interpretation

Let `x_t` be an unobserved degradation state.

Observed channels follow:

`y_t = H x_t + epsilon_t`

WOLF does not require explicit recovery of `x_t`. Instead it estimates a precursor surface from weak directional deviations.

## Candidate state vector

`W_t = (R_t, L_t, K_t, N_eff(t), U_t, A_t)`

where:
- `R_t` = persistent latent-failure score
- `L_t` = instantaneous weighted weak-signal score
- `K_t` = relational/directional coherence
- `N_eff` = effective number of contributing channels
- `U_t` = aggregate uncertainty
- `A_t` = alarm state

## Alarm logic

A conservative alarm rule:

`A_t = 1[R_t > theta_R and N_eff > theta_N and K_t > theta_K]`

Thresholds must be chosen only from calibration data.

## Lead-time metric

If physical failure begins at time `T_fail` and monitor first alarms at `T_alarm`:

`LeadTime = T_fail - T_alarm`

Comparison must be made at matched false-alarm rates.

## False-alarm matching

No claim of superiority is valid unless:
- same observation history,
- same precursor horizon,
- equivalent preprocessing access,
- matched false-positive rate,
- comparable compute budget.

## Failure habitat generator

Synthetic precursor:

`y_i(t) = noise_i(t) + a_i * ramp(t - T0)`

with small `a_i` such that no individual channel crosses a conventional threshold until late.

This is the canonical WOLF test condition.
