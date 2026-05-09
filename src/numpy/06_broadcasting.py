#!/usr/bin/env python

"""Solution to exercise 07: column-mean centering via broadcasting."""

import numpy as np

m = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])

centered = m - m.mean(axis=0)
print(centered)
print(centered.mean(axis=0))
