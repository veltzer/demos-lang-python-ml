#!/usr/bin/env python

"""Solution to exercise 11: annotated correlation heatmap."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "age": [22, 38, 26, 35, 27, 54, 14, 4, 58, 20],
    "fare": [7.25, 71.28, 7.92, 53.10, 8.05, 51.86, 30.07, 16.7, 26.55, 8.05],
    "survived": [0, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    "pclass": [3, 1, 3, 1, 3, 1, 2, 3, 1, 3],
})

sns.heatmap(df.corr(), annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation matrix")
plt.savefig("/tmp/11_heatmap.png")
