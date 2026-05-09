#!/usr/bin/env python

"""Solution to exercise 02: line plot with labels, title, and legend."""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y = x ** 2

plt.plot(x, y, label="x^2")
plt.xlabel("x")
plt.ylabel("y = x^2")
plt.title("Square function")
plt.legend()
plt.savefig("/tmp/02_axis_labels_and_title.png")
