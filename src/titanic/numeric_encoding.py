#!/usr/bin/env python

"""
This example shows how to convert all the columns of data frame to numeric
values in preparation to doing ML with an algorithm that only works with
numeric data (e.g. KNN).
"""

import pandas

df = pandas.read_csv("../../data/titanic_clean.csv")
