#!/usr/bin/env python

"""Solution to exercise 18: write a DataFrame to CSV and read it back."""

import io

import polars as pl

df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [30, 25, 35],
})

buffer = io.StringIO()
df.write_csv(buffer)
csv_text = buffer.getvalue()
print(csv_text)

restored = pl.read_csv(io.StringIO(csv_text))
print(restored)
print(restored.equals(df))
