#!/usr/bin/env python

"""Solution to exercise 03: histogram of normal samples."""

import numpy as np
import pandas as pd
import plotly.express as px

rng = np.random.default_rng(0)
df = pd.DataFrame({"value": rng.normal(size=1000)})

fig = px.histogram(df, x="value", nbins=30)
fig.update_layout(title="Standard normal samples")
fig.write_html("/tmp/03_histogram.html")
