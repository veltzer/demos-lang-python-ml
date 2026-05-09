#!/usr/bin/env python

"""Solution to exercise 03: three trig curves on one axes with a legend."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)

plt.plot(x, np.sin(x), label="sin")
plt.plot(x, np.cos(x), label="cos")
plt.plot(x, np.sin(x) * np.cos(x), label="sin*cos")

plt.xlabel("x")
plt.ylabel("value")
plt.legend()
plt.savefig("/tmp/03_multiple_lines.png")
