#!/usr/bin/env python

"""Solution to exercise 04: overlay two filled KDE plots."""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
a = rng.normal(loc=0.0, scale=1.0, size=1000)
b = rng.normal(loc=2.0, scale=1.5, size=1000)

sns.kdeplot(a, label="a", fill=True)
sns.kdeplot(b, label="b", fill=True)
plt.legend()
plt.savefig("/tmp/04_kde_plot.png")
