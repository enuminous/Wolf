from dataclasses import dataclass, field
from typing import Dict, List, Optional
import math

@dataclass
class ChannelSpec:
    mean: float = 0.0
    std: float = 1.0
    hazard_direction: float = 1.0
    reliability: float = 1.0

@dataclass
class WolfConfig:
    alpha: float = 1.0
    beta: float = 0.5
    gamma: float = 0.25
    persistence: float = 0.85
    alarm_threshold: float = 0.8
    min_effective_channels: float = 2.0
    coherence_threshold: float = 0.0

@dataclass
class WolfState:
    persistent_score: float = 0.0
    previous_z: Dict[str, float] = field(default_factory=dict)

class WolfMonitor:
    def __init__(self, specs: Dict[str, ChannelSpec], config: Optional[WolfConfig] = None):
        self.specs = specs
        self.config = config or WolfConfig()
        self.state = WolfState()

    def update(self, observations: Dict[str, float], uncertainty: Optional[Dict[str, float]] = None):
        uncertainty = uncertainty or {}
        contributions = {}
        velocities = {}
        raw_weights = {}

        for name, value in observations.items():
            spec = self.specs[name]
            std = spec.std if abs(spec.std) > 1e-12 else 1.0
            z = (value - spec.mean) / std
            prev = self.state.previous_z.get(name, z)
            v = spec.hazard_direction * (z - prev)
            q = spec.hazard_direction * z
            u = max(0.0, uncertainty.get(name, 0.0))

            local = max(
                0.0,
                self.config.alpha * q
                + self.config.beta * v
                - self.config.gamma * u
            )

            weight = max(0.0, spec.reliability) / (1.0 + u)
            raw_weights[name] = weight
            contributions[name] = local
            velocities[name] = v
            self.state.previous_z[name] = z

        total_w = sum(raw_weights.values()) or 1.0
        weighted = {
            k: (raw_weights[k] / total_w) * contributions[k]
            for k in contributions
        }
        instantaneous = sum(weighted.values())

        self.state.persistent_score = (
            self.config.persistence * self.state.persistent_score
            + (1.0 - self.config.persistence) * instantaneous
        )

        positive = {k: max(0.0, v) for k, v in weighted.items()}
        pos_sum = sum(positive.values())
        if pos_sum > 0:
            p = [v / pos_sum for v in positive.values() if v > 0]
            effective = 1.0 / sum(x*x for x in p)
        else:
            effective = 0.0

        signed = [1 if velocities[k] > 0 else (-1 if velocities[k] < 0 else 0) for k in velocities]
        pairs = []
        for i in range(len(signed)):
            for j in range(i+1, len(signed)):
                pairs.append(signed[i] * signed[j])
        coherence = sum(pairs) / len(pairs) if pairs else 0.0

        alarm = (
            self.state.persistent_score > self.config.alarm_threshold
            and effective >= self.config.min_effective_channels
            and coherence >= self.config.coherence_threshold
        )

        return {
            "latent_score": self.state.persistent_score,
            "instantaneous_score": instantaneous,
            "coherence": coherence,
            "effective_channels": effective,
            "alarm": alarm,
            "contributors": weighted,
            "velocities": velocities,
        }
