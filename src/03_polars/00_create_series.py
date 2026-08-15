#!/usr/bin/env python

"""Solution to exercise 01: build a polars Series and inspect it."""

import polars as pl

s = pl.Series("nums", [10, 20, 30, 40, 50])

print(s)
print(s.dtype)
print(s.name)
print(s.to_list())
