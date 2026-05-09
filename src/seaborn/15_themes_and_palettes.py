#!/usr/bin/env python

"""Solution to exercise 15: 2x2 grid demonstrating four theme+palette combos."""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 60
df = pd.DataFrame({
    "x": np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n), rng.normal(-3, 1, n)]),
    "y": np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n), rng.normal(-3, 1, n)]),
    "label": ["A"] * n + ["B"] * n + ["C"] * n,
})

combos = [
    ("darkgrid", "deep"),
    ("whitegrid", "pastel"),
    ("ticks", "colorblind"),
    ("white", "muted"),
]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, (style, palette) in zip(axes.flat, combos):
    sns.set_theme(style=style, palette=palette)
    sns.scatterplot(data=df, x="x", y="y", hue="label", ax=ax)
    ax.set_title(f"{style} + {palette}")

fig.tight_layout()
fig.savefig("/tmp/15_themes_and_palettes.png")
