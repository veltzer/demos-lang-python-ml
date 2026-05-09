#!/usr/bin/env python

"""Solution to exercise 06: scatter colored by class with custom hover data."""

import numpy as np
import pandas as pd
import plotly.express as px

rng = np.random.default_rng(0)
n = 50
df = pd.DataFrame({
    "x": np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n)]),
    "y": np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n)]),
    "label": ["A"] * n + ["B"] * n,
    "weight": rng.uniform(1, 10, 2 * n),
})

fig = px.scatter(df, x="x", y="y", color="label", size="weight", hover_data=["weight"])
fig.write_html("/tmp/06_hover_and_color.html")
