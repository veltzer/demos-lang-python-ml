#!/usr/bin/env python

"""Solution to exercise 01: line plot with markers and a title."""

import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "sales": [120, 135, 150, 160, 180, 200, 210, 205, 190, 170, 150, 140],
})

fig = px.line(df, x="month", y="sales", markers=True)
fig.update_layout(title="Monthly sales")
fig.write_html("/tmp/01_line_plot.html")
