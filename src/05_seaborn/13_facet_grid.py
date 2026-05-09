#!/usr/bin/env python

"""Solution to exercise 14: FacetGrid mapping scatterplot per (day, group)."""

import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(0)
n = 60
df = pd.DataFrame({
    "x": np.tile(np.arange(n), 4),
    "y": np.concatenate([
        rng.normal(0, 1, n),
        rng.normal(2, 1, n),
        rng.normal(0, 1, n) + 5,
        rng.normal(2, 1, n) + 5,
    ]),
    "day": ["Mon"] * (2 * n) + ["Tue"] * (2 * n),
    "group": (["A"] * n + ["B"] * n) * 2,
})

g = sns.FacetGrid(df, col="day", row="group")
g.map_dataframe(sns.scatterplot, x="x", y="y")
g.figure.savefig("/tmp/14_facet_grid.png")
