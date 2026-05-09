#!/usr/bin/env python

"""Solution to exercise 02: lineplot with auto-aggregated confidence band."""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
xs = np.repeat(np.arange(10), 5)
ys = 2 * xs + rng.normal(scale=2.0, size=xs.shape)

df = pd.DataFrame({"x": xs, "y": ys})

sns.lineplot(data=df, x="x", y="y")
plt.savefig("/tmp/02_line_plot.png")
