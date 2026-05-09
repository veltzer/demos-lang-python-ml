#!/usr/bin/env python

"""Solution to exercise 09: sample from N(5, 2), check empirical stats."""

import numpy as np

rng = np.random.default_rng(42)
samples = rng.normal(loc=5.0, scale=2.0, size=10000)

print(samples.mean())
print(samples.std())
print(float(((samples >= 3) & (samples <= 7)).mean()))
