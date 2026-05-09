#!/usr/bin/env python

"""Solution to exercise 03: arange + reshape + transpose."""

import numpy as np

m = np.arange(12).reshape(3, 4)
print(m)
print(m.T)
