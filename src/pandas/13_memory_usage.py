#!/usr/bin/env python

"""Solution to exercise 13: measure DataFrame memory usage and process RSS."""

import os
import random
import psutil
import pandas as pd

process = psutil.Process(os.getpid())
print(process.memory_info().rss)

rows = [[random.random() for _ in range(12)] for _ in range(890)]
df = pd.DataFrame(rows)

print(df.dtypes)
print(df.memory_usage())
print(int(df.memory_usage().sum()))

print(process.memory_info().rss)
