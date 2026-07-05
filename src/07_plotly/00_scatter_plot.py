#!/usr/bin/env python

"""Solution to exercise 00: scatter plot from a DataFrame."""

import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5, 6, 7, 8],
    "y": [2, 3, 5, 4, 8, 7, 9, 11],
})

fig = px.scatter(df, x="x", y="y")
fig.write_html("/tmp/00_scatter_plot.html")
