import random
from statistics import mean
from wolf import ChannelSpec, WolfConfig, WolfMonitor

def generate(seed=23, n=5, steps=160, precursor_start=70, fail_time=130):
    rng = random.Random(seed)
    names = [f"c{i}" for i in range(n)]
    data = []
    for t in range(steps):
        row = {}
        for i, name in enumerate(names):
            noise = rng.gauss(0, 0.35)
            ramp = 0.0
            if t >= precursor_start:
                ramp = (t - precursor_start) * (0.012 + 0.002*i)
            row[name] = noise + ramp
        data.append(row)
    return names, data, fail_time

def run(seed=23):
    names, data, fail_time = generate(seed=seed)
    specs = {n: ChannelSpec(hazard_direction=1, reliability=1) for n in names}
    cfg = WolfConfig(alarm_threshold=0.55, min_effective_channels=2.5, coherence_threshold=-0.2)
    wolf = WolfMonitor(specs, cfg)
    alarm_t = None
    scores = []
    for t, row in enumerate(data):
        out = wolf.update(row)
        scores.append(out["latent_score"])
        if out["alarm"] and alarm_t is None:
            alarm_t = t
    return {"seed": seed, "alarm_time": alarm_t, "fail_time": fail_time,
            "lead_time": None if alarm_t is None else fail_time-alarm_t,
            "max_score": max(scores)}

if __name__ == "__main__":
    results = [run(s) for s in [11,23,37,46,59]]
    for r in results:
        print(r)
    leads = [r["lead_time"] for r in results if r["lead_time"] is not None]
    print("mean lead time:", mean(leads) if leads else None)
