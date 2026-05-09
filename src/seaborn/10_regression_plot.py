#!/usr/bin/env python

"""Solution to exercise 10: regplot with linear fit and confidence band."""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
x = rng.uniform(0, 10, 100)
y = 2.5 * x + 1.0 + rng.normal(0, 3, 100)

df = pd.DataFrame({"x": x, "y": y})

sns.regplot(data=df, x="x", y="y")
plt.title("Regression fit")
plt.savefig("/tmp/10_regression_plot.png")
