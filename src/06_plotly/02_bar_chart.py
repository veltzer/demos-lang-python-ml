#!/usr/bin/env python

"""Solution to exercise 02: vertical bar chart."""

import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "fruit": ["apples", "oranges", "bananas", "pears", "grapes"],
    "quantity": [23, 17, 35, 12, 28],
})

fig = px.bar(df, x="fruit", y="quantity")
fig.update_layout(title="Fruit inventory")
fig.write_html("/tmp/02_bar_chart.html")
