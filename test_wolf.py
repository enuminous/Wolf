import unittest
from wolf import ChannelSpec, WolfConfig, WolfMonitor

class TestWolf(unittest.TestCase):
    def test_rising_distributed_signal_increases_score(self):
        specs = {k: ChannelSpec() for k in ["a","b","c"]}
        m = WolfMonitor(specs, WolfConfig(persistence=0.5, alarm_threshold=10))
        scores = []
        for x in [0.0, 0.1, 0.2, 0.4, 0.8]:
            out = m.update({"a":x, "b":x*0.9, "c":x*0.8})
            scores.append(out["latent_score"])
        self.assertGreater(scores[-1], scores[0])

    def test_effective_channel_count(self):
        specs = {k: ChannelSpec() for k in ["a","b","c"]}
        m = WolfMonitor(specs, WolfConfig(persistence=0.0, alarm_threshold=10))
        m.update({"a":0,"b":0,"c":0})
        out = m.update({"a":1,"b":1,"c":1})
        self.assertGreater(out["effective_channels"], 2.5)

    def test_single_channel_not_distributed(self):
        specs = {k: ChannelSpec() for k in ["a","b","c"]}
        m = WolfMonitor(specs, WolfConfig(persistence=0.0, alarm_threshold=0.1, min_effective_channels=2))
        m.update({"a":0,"b":0,"c":0})
        out = m.update({"a":2,"b":0,"c":0})
        self.assertFalse(out["alarm"])

if __name__ == "__main__":
    unittest.main()
