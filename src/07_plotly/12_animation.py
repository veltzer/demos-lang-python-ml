#!/usr/bin/env python

"""Solution to exercise 12: animated scatter with year as the frame variable."""

import numpy as np
import pandas as pd
import plotly.express as px

rng = np.random.default_rng(0)
years = list(range(2010, 2021))
rows = []
for year in years:
    n = 50
    rows.append(pd.DataFrame({
        "year": year,
        "x": rng.normal(year - 2010, 2, n),
        "y": rng.normal(year - 2010, 2, n),
        "size": rng.uniform(5, 20, n),
    }))
df = pd.concat(rows, ignore_index=True)

fig = px.scatter(df, x="x", y="y", size="size", animation_frame="year",
                 range_x=[-5, 15], range_y=[-5, 15])
fig.write_html("/tmp/12_animation.html")
