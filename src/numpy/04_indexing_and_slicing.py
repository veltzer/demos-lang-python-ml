#!/usr/bin/env python

"""Solution to exercise 04: element / row / column / submatrix indexing."""

import numpy as np

m = np.arange(16).reshape(4, 4)

print(m[2, 3])
print(m[1])
print(m[:, 2])
print(m[:2, :2])
print(m[2:, 2:])
