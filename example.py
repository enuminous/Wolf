from wolf import ChannelSpec, WolfConfig, WolfMonitor

specs = {
    "temperature": ChannelSpec(hazard_direction=1, reliability=0.95),
    "vibration": ChannelSpec(hazard_direction=1, reliability=0.90),
    "pressure_noise": ChannelSpec(hazard_direction=1, reliability=0.92),
}

monitor = WolfMonitor(
    specs,
    WolfConfig(alarm_threshold=0.35, min_effective_channels=2.0, coherence_threshold=-0.5)
)

stream = [
    {"temperature": 0.05, "vibration": -0.02, "pressure_noise": 0.01},
    {"temperature": 0.20, "vibration": 0.10, "pressure_noise": 0.08},
    {"temperature": 0.40, "vibration": 0.28, "pressure_noise": 0.21},
    {"temperature": 0.65, "vibration": 0.52, "pressure_noise": 0.44},
    {"temperature": 0.85, "vibration": 0.74, "pressure_noise": 0.61},
]

for t, obs in enumerate(stream):
    out = monitor.update(obs)
    print(t, out)
