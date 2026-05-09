#!/usr/bin/env python

"""Solution to exercise 08: three curves with distinct colors, linestyles, markers."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)

plt.plot(x, x, color="red", linestyle="-", label="x")
plt.plot(x, x ** 1.5, color="green", linestyle="--", marker="o", label="x^1.5")
plt.plot(x, x ** 2, color="blue", linestyle=":", marker="^", linewidth=2, label="x^2")

plt.legend()
plt.grid(True)
plt.title("Power-law growth")
plt.savefig("/tmp/08_styling.png")
