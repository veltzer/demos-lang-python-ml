#!/usr/bin/env python

"""Solution to exercise 14: a 4-panel mini dashboard combining trace types."""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

rng = np.random.default_rng(0)
n = 100
df = pd.DataFrame({
    "x": np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n), rng.normal(-3, 1, n)]),
    "y": np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n), rng.normal(-3, 1, n)]),
    "label": ["A"] * n + ["B"] * n + ["C"] * n,
})

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Scatter", "Mean y by label", "Histogram of y", "Box plot of y"),
)

for label in ["A", "B", "C"]:
    sub = df[df["label"] == label]
    fig.add_trace(go.Scatter(x=sub["x"], y=sub["y"], mode="markers", name=label),
                  row=1, col=1)

means = df.groupby("label")["y"].mean()
fig.add_trace(go.Bar(x=means.index, y=means.values), row=1, col=2)

fig.add_trace(go.Histogram(x=df["y"]), row=2, col=1)

for label in ["A", "B", "C"]:
    fig.add_trace(go.Box(y=df[df["label"] == label]["y"], name=label), row=2, col=2)

fig.update_layout(height=800, title_text="Dashboard", showlegend=False)
fig.write_html("/tmp/14_dashboard.html")
