#!/usr/bin/env python

"""Solution to exercise 09: two series on independent y-axes via twinx."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
temperature = 20 + 5 * np.sin(x)
pressure = 1000 + 50 * np.cos(x)

fig, ax1 = plt.subplots()

ax1.plot(x, temperature, color="red")
ax1.set_xlabel("x")
ax1.set_ylabel("temperature (C)", color="red")

ax2 = ax1.twinx()
ax2.plot(x, pressure, color="blue")
ax2.set_ylabel("pressure (hPa)", color="blue")

fig.suptitle("Temperature and pressure")
fig.savefig("/tmp/09_dual_axis.png")
