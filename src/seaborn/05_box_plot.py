#!/usr/bin/env python

"""Solution to exercise 06: boxplot comparing three groups."""

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

sns.boxplot(data=df, x="group", y="value")
plt.title("Distribution of value by group")
plt.savefig("/tmp/06_box_plot.png")
