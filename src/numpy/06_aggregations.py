#!/usr/bin/env python

"""Solution to exercise 06: aggregations with axis arguments."""

import numpy as np

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(m.sum())
print(m.sum(axis=0))
print(m.mean(axis=1))
print(int(m.argmax()))
