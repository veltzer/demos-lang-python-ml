#!/usr/bin/env python

"""Solution to exercise 16: linear vs exact-fit polynomial through scatter points."""

import numpy as np

xs = np.array([2.0, 3.0, 5.0, 8.0, 8.5, 9.0, 10.0])
ys = np.array([1.5, 2.0, 4.0, 4.5, 6.0, 7.0, 7.5])

slope, intercept = np.polyfit(xs, ys, 1)
print(slope, intercept)

exact = np.polyfit(xs, ys, len(xs) - 1)
print(exact)

linear_at_100 = slope * 100 + intercept
exact_at_100 = float(np.polyval(exact, 100))
print(linear_at_100)
print(exact_at_100)
