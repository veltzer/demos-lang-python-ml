#!/usr/bin/env python

"""Solution to exercise 01: a basic line plot of y = x**2."""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = x ** 2

plt.plot(x, y)
plt.savefig("/tmp/01_line_plot.png")
