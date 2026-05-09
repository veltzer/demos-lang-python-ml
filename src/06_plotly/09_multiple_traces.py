#!/usr/bin/env python

"""Solution to exercise 09: three trig curves on one figure with custom styles."""

import numpy as np
import plotly.graph_objects as go

x = np.linspace(0, 2 * np.pi, 100)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=np.sin(x), mode="lines", name="sin",
                         line={"color": "blue"}))
fig.add_trace(go.Scatter(x=x, y=np.cos(x), mode="lines", name="cos",
                         line={"color": "red"}))
fig.add_trace(go.Scatter(x=x, y=np.sin(x) * np.cos(x), mode="lines", name="sin*cos",
                         line={"color": "green", "dash": "dash"}))

fig.update_layout(title="Trig functions", xaxis_title="x", yaxis_title="value")
fig.write_html("/tmp/09_multiple_traces.html")
