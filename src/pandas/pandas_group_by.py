#!/usr/bin/env python
import pandas

tbl = pandas.read_csv("data.csv")
tbl.fillna(0, inplace=True)
print(tbl.groupby(["Survived", "Sex"]).count())
print(tbl)
