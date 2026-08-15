#!/usr/bin/env python

"""Solution to exercise 12: manipulate text columns with the str namespace."""

import polars as pl

df = pl.DataFrame({
    "email": ["Alice@Example.com", "BOB@example.COM", "charlie@example.com"],
})

df = df.with_columns(
    pl.col("email").str.to_lowercase().alias("normalized"),
    pl.col("email").str.split("@").list.first().alias("user"),
    pl.col("email").str.len_chars().alias("length"),
    pl.col("email").str.contains("(?i)example").alias("is_example"),
)

print(df)
