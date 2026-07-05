#!/usr/bin/env python

"""Solution to exercise 01: a basic line plot of y = x**2."""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y = x ** 2

plt.plot(x, y)
plt.savefig("/tmp/01_line_plot.png")
