#!/usr/bin/env python

"""Solution to exercise 20: walk through a polars basics workout end-to-end."""

import polars as pl

df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Dana", "Eve"],
    "dept": ["eng", "sales", "eng", "sales", "eng"],
    "age": [30, 25, 35, 28, 40],
    "salary": [70000, 50000, 90000, 65000, 120000],
})

df = df.with_columns((pl.col("salary") * 1.05).round(0).alias("raised"))
df = df.drop("raised")
df = df.rename({"salary": "income"})
df = df.filter(pl.col("name") != "Bob")

new_row = pl.DataFrame({
    "name": ["Frank"],
    "dept": ["hr"],
    "age": [33],
    "income": [80000],
})
df = pl.concat([df, new_row], how="vertical")

print(df.select(pl.col("age").cast(pl.Float64)).dtypes)

summary = df.group_by("dept").agg(
    pl.len().alias("headcount"),
    pl.col("income").mean().round(2).alias("avg_income"),
).sort("dept")

print(summary)
print(df.select(
    pl.col("income").mean().alias("mean"),
    pl.col("income").var().alias("variance"),
))
print(df.sort("income", descending=True))
