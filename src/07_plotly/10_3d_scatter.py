#!/usr/bin/env python

"""Solution to exercise 10: 3-D scatter of three Gaussian clusters."""

import numpy as np
import pandas as pd
import plotly.express as px

rng = np.random.default_rng(0)
n = 100
df = pd.DataFrame({
    "x": np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n), rng.normal(-3, 1, n)]),
    "y": np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n), rng.normal(-3, 1, n)]),
    "z": np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n), rng.normal(-3, 1, n)]),
    "label": ["A"] * n + ["B"] * n + ["C"] * n,
})

fig = px.scatter_3d(df, x="x", y="y", z="z", color="label")
fig.write_html("/tmp/10_3d_scatter.html")
