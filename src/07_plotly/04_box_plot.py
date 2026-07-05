#!/usr/bin/env python

"""Solution to exercise 04: box plot comparing three groups."""

import numpy as np
import pandas as pd
import plotly.express as px

n = 200
rng = np.random.default_rng(0)
df = pd.DataFrame({
    "group": ["A"] * n + ["B"] * n + ["C"] * n,
    "value": np.concatenate([
        rng.normal(0, 1, n),
        rng.normal(1, 2, n),
        rng.normal(-1, 0.5, n),
    ]),
})

fig = px.box(df, x="group", y="value")
fig.update_layout(title="Distribution by group")
fig.write_html("/tmp/04_box_plot.html")
