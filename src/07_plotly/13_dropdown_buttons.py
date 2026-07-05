#!/usr/bin/env python

"""Solution to exercise 13: dropdown that toggles trace visibility."""

import numpy as np
import plotly.graph_objects as go

x = np.linspace(0, 2 * np.pi, 100)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=np.sin(x), name="sin"))
fig.add_trace(go.Scatter(x=x, y=np.cos(x), name="cos"))
fig.add_trace(go.Scatter(x=x, y=np.clip(np.tan(x), -5, 5), name="tan"))

fig.update_layout(updatemenus=[{
    "buttons": [
        {"label": "All", "method": "update", "args": [{"visible": [True, True, True]}]},
        {"label": "sin", "method": "update", "args": [{"visible": [True, False, False]}]},
        {"label": "cos", "method": "update", "args": [{"visible": [False, True, False]}]},
        {"label": "tan", "method": "update", "args": [{"visible": [False, False, True]}]},
    ],
    "direction": "down",
    "showactive": True,
}])

fig.write_html("/tmp/13_dropdown_buttons.html")
