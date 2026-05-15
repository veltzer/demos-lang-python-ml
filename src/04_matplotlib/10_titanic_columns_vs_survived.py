#!/usr/bin/env python

"""Solution to exercise 10: per-column plots vs Survived on Titanic data."""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/titanic.csv")

numeric_cols = ["Age", "Fare", "SibSp", "Parch", "Pclass"]
categorical_cols = ["Sex", "Embarked"]

fig, axes = plt.subplots(2, 4, figsize=(18, 8))
axes_flat = axes.flatten()

for ax, col in zip(axes_flat, numeric_cols):
    df[df["Survived"] == 0][col].plot.hist(ax=ax, alpha=0.5, label="died", bins=20)
    df[df["Survived"] == 1][col].plot.hist(ax=ax, alpha=0.5, label="survived", bins=20)
    ax.set_title(col)
    ax.legend()

for ax, col in zip(axes_flat[len(numeric_cols):], categorical_cols):
    rates = df.groupby(col)["Survived"].mean()
    rates.plot.bar(ax=ax)
    ax.set_title(f"survival rate by {col}")
    ax.set_ylabel("P(Survived)")

axes_flat[-1].axis("off")

fig.tight_layout()
fig.savefig("/tmp/10_titanic_columns_vs_survived.png")
