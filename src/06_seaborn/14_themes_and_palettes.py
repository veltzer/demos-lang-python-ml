#!/usr/bin/env python

"""Solution to exercise 15: 2x2 grid demonstrating four theme+palette combos."""

from typing import Literal

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(0)
n = 60
df = pd.DataFrame({
    "x": np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n), rng.normal(-3, 1, n)]),
    "y": np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n), rng.normal(-3, 1, n)]),
    "label": ["A"] * n + ["B"] * n + ["C"] * n,
})

combos: list[tuple[Literal["dark", "darkgrid", "ticks", "white", "whitegrid"], str]] = [
    ("darkgrid", "deep"),
    ("whitegrid", "pastel"),
    ("ticks", "colorblind"),
    ("white", "muted"),
]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, (style, palette) in zip(axes.flat, combos, strict=True):
    sns.set_theme(style=style, palette=palette)
    sns.scatterplot(data=df, x="x", y="y", hue="label", ax=ax)
    ax.set_title(f"{style} + {palette}")

fig.tight_layout()
fig.savefig("/tmp/15_themes_and_palettes.png")
