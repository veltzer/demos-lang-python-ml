#!/usr/bin/env python

"""Solution to exercise 07: histogram of Age split by Survived."""

import pandas as pd

df = pd.DataFrame({
    "Age": [22, 38, 26, 35, 27, 54, 14, 4, 58, 20, 39, 14, 55, 2, 31, 35],
    "Survived": [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0],
})

axes = df.hist(column="Age", by="Survived")
fig = axes[0].get_figure()
fig.savefig("/tmp/07_histogram.png")
