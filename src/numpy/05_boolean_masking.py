#!/usr/bin/env python

"""Solution to exercise 05: boolean masking — filter, replace, count."""

import numpy as np

a = np.array([3, -1, 4, -1, 5, 9, -2, 6, 5, 3, 5])

print(a[a > 0])

clipped = a.copy()
clipped[clipped < 0] = 0
print(clipped)

print(int((a > 4).sum()))
