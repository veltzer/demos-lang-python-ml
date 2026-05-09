#!/usr/bin/env python

"""Solution to exercise 01: scatterplot from a DataFrame."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5, 6, 7, 8],
    "y": [2, 3, 5, 4, 8, 7, 9, 11],
})

sns.scatterplot(data=df, x="x", y="y")
plt.savefig("/tmp/01_scatter_plot.png")
