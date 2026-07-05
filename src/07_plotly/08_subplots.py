#!/usr/bin/env python

"""Solution to exercise 08: 1x2 subplots mixing bar and histogram traces."""

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

rng = np.random.default_rng(0)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 135, 150, 160, 180, 200]
samples = rng.normal(loc=10, scale=2, size=300)

fig = make_subplots(rows=1, cols=2, subplot_titles=("Monthly sales", "Sample distribution"))
fig.add_trace(go.Bar(x=months, y=sales), row=1, col=1)
fig.add_trace(go.Histogram(x=samples), row=1, col=2)
fig.write_html("/tmp/08_subplots.html")
