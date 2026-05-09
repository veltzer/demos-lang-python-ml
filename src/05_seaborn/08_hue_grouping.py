#!/usr/bin/env python

"""Solution to exercise 09: scatterplot with categorical hue mapping."""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 100
df = pd.DataFrame({
    "x": np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n)]),
    "y": np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n)]),
    "label": ["A"] * n + ["B"] * n,
})

sns.scatterplot(data=df, x="x", y="y", hue="label")
plt.title("Two clusters")
plt.savefig("/tmp/09_hue_grouping.png")
