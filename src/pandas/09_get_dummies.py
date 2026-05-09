#!/usr/bin/env python

"""Solution to exercise 09: one-hot encode a categorical column with get_dummies."""

import pandas as pd

df = pd.DataFrame({
    "car": ["ferrari", "honda", "mazda", "honda"],
    "weight": [4, 5, 6, 5],
})

print(df)
print(pd.get_dummies(df))
