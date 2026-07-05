#!/usr/bin/env python

"""Solution to exercise 07: violinplot comparing three groups."""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

n = 200
rng = np.random.default_rng(0)
df = pd.DataFrame({
    "group": ["A"] * n + ["B"] * n + ["C"] * n,
    "value": np.concatenate([
        rng.normal(0, 1, n),
        rng.normal(1, 2, n),
        rng.normal(-1, 0.5, n),
    ]),
})

sns.violinplot(data=df, x="group", y="value")
plt.title("Violin plot of value by group")
plt.savefig("/tmp/07_violin_plot.png")
