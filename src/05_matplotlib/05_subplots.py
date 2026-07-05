#!/usr/bin/env python

"""Solution to exercise 06: 2x2 subplot grid with per-axes titles."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title("sin")

axes[0, 1].plot(x, np.cos(x))
axes[0, 1].set_title("cos")

axes[1, 0].plot(x, np.tan(x))
axes[1, 0].set_ylim(-5, 5)
axes[1, 0].set_title("tan (clipped)")

axes[1, 1].plot(x, np.sin(x) * np.cos(x))
axes[1, 1].set_title("sin*cos")

fig.tight_layout()
fig.savefig("/tmp/06_subplots.png")
