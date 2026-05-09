#!/usr/bin/env python

"""Solution to exercise 13: hexbin jointplot of correlated samples."""

import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(0)
mean = [0, 0]
cov = [[1.0, 0.7], [0.7, 1.0]]
xy = rng.multivariate_normal(mean, cov, size=1000)

df = pd.DataFrame(xy, columns=["x", "y"])

grid = sns.jointplot(data=df, x="x", y="y", kind="hex")
grid.figure.savefig("/tmp/13_joint_plot.png")
