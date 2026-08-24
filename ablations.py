from wolf import ChannelSpec, WolfConfig, WolfMonitor
from benchmark import generate

def evaluate(config, disable_direction=False, disable_persistence=False):
    names, data, fail_time = generate(seed=23)
    specs = {
        n: ChannelSpec(hazard_direction=(0 if disable_direction else 1))
        for n in names
    }
    if disable_persistence:
        config = WolfConfig(
            alpha=config.alpha,
            beta=config.beta,
            gamma=config.gamma,
            persistence=0.0,
            alarm_threshold=config.alarm_threshold,
            min_effective_channels=config.min_effective_channels,
            coherence_threshold=config.coherence_threshold,
        )
    m = WolfMonitor(specs, config)
    alarm_t = None
    for t,row in enumerate(data):
        out = m.update(row)
        if out["alarm"] and alarm_t is None:
            alarm_t = t
    return alarm_t

if __name__ == "__main__":
    cfg = WolfConfig(alarm_threshold=0.55, min_effective_channels=2.5, coherence_threshold=-0.2)
    print("full:", evaluate(cfg))
    print("no direction:", evaluate(cfg, disable_direction=True))
    print("no persistence:", evaluate(cfg, disable_persistence=True))
