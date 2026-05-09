#!/usr/bin/env python

"""Solution to exercise 07: facet grid using facet_row and facet_col."""

import numpy as np
import pandas as pd
import plotly.express as px

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

fig = px.scatter(df, x="x", y="y", facet_row="group", facet_col="day")
fig.write_html("/tmp/07_facets.html")
