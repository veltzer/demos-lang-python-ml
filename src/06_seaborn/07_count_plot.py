#!/usr/bin/env python

"""Solution to exercise 08: countplot of category frequencies."""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.DataFrame({
    "color": [
        "red", "blue", "red", "green", "blue", "blue",
        "red", "red", "green", "blue", "red", "blue",
    ],
})

sns.countplot(data=df, x="color")
plt.title("Color frequencies")
plt.savefig("/tmp/08_count_plot.png")
