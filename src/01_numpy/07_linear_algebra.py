#!/usr/bin/env python

"""Solution to exercise 08: solve a 2x2 linear system, verify, det + inv."""

import numpy as np

A = np.array([[3.0, 1.0], [1.0, 2.0]])
b = np.array([9.0, 8.0])

x = np.linalg.solve(A, b)
print(x)
print(A @ x)
print(np.linalg.det(A))
print(np.linalg.inv(A))
