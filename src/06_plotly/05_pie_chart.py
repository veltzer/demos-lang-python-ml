#!/usr/bin/env python

"""Solution to exercise 05: pie chart of category shares."""

import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "browser": ["Chrome", "Safari", "Firefox", "Edge", "Other"],
    "share": [65, 18, 8, 5, 4],
})

fig = px.pie(df, names="browser", values="share")
fig.update_layout(title="Browser market share")
fig.write_html("/tmp/05_pie_chart.html")
