#!/usr/bin/env python

"""Solution to exercise 12: pairplot of three features colored by label."""

import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(0)
n = 80
df = pd.DataFrame({
    "x": np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n)]),
    "y": np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n)]),
    "z": np.concatenate([rng.normal(0, 1, n), rng.normal(0, 1, n)]),
    "label": ["A"] * n + ["B"] * n,
})

grid = sns.pairplot(df, hue="label")
grid.figure.savefig("/tmp/12_pair_plot.png")
