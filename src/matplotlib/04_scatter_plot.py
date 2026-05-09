#!/usr/bin/env python

"""Solution to exercise 04: scatter plot with per-point color and a colorbar."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
x = rng.normal(size=200)
y = 2 * x + rng.normal(size=200)

plt.scatter(x, y, c=x, s=20)
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear relationship with noise")
plt.savefig("/tmp/04_scatter_plot.png")
