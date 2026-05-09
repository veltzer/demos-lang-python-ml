#!/usr/bin/env python

"""Solution to exercise 03: histplot of normal samples."""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
samples = rng.normal(size=1000)

sns.histplot(samples, bins=30)
plt.title("Standard normal samples")
plt.savefig("/tmp/03_histogram.png")
