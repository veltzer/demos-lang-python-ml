#!/usr/bin/env python

"""Solution to exercise 08: countplot of category frequencies."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "color": [
        "red", "blue", "red", "green", "blue", "blue",
        "red", "red", "green", "blue", "red", "blue",
    ],
})

sns.countplot(data=df, x="color")
plt.title("Color frequencies")
plt.savefig("/tmp/08_count_plot.png")
