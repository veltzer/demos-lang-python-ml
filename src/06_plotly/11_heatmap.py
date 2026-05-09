#!/usr/bin/env python

"""Solution to exercise 11: correlation heatmap with annotated cells."""

import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "age": [22, 38, 26, 35, 27, 54, 14, 4, 58, 20],
    "fare": [7.25, 71.28, 7.92, 53.10, 8.05, 51.86, 30.07, 16.7, 26.55, 8.05],
    "survived": [0, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    "pclass": [3, 1, 3, 1, 3, 1, 2, 3, 1, 3],
})

corr = df.corr()
fig = px.imshow(corr, text_auto=True, color_continuous_scale="RdBu", zmin=-1, zmax=1)
fig.update_layout(title="Correlation matrix")
fig.write_html("/tmp/11_heatmap.html")
