#!/usr/bin/env python

"""Solution to exercise 18: Pearson correlations and per-column data summary."""

import pandas as pd

df = pd.read_csv("data.csv")

numeric = df.select_dtypes(include="number")
print(numeric.corr())
correlations = numeric.corr()["Survived"].drop("Survived").sort_values(ascending=False)
print("Pearson correlation with Survived:")
print(correlations)
print()

print("Per-column summary:")
for col in df.columns:
    series = df[col]
    print(f"\n=== {col} (dtype={series.dtype}) ===")
    if pd.api.types.is_numeric_dtype(series):
        print(f"mean:    {series.mean():.4f}")
        print(f"std:     {series.std():.4f}")
        print(f"unique:  {series.nunique()}")
        print(f"median:  {series.median():.4f}")
        print(f"q25:     {series.quantile(0.25):.4f}")
        print(f"q75:     {series.quantile(0.75):.4f}")
        print(f"min/max: {series.min()} / {series.max()}")
    else:
        print(series.value_counts().head(10))
