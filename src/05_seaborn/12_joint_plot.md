# Exercise 13: Joint Plot

`sns.jointplot` shows a scatter plot of two variables in the center and the marginal
distribution of each variable along its respective axis. With `kind="hex"` the center
becomes a hexbin density plot, useful when the scatter is so dense that points overlap.

Generate 1000 correlated samples:

```
import numpy as np

rng = np.random.default_rng(0)
mean = [0, 0]
cov  = [[1.0, 0.7], [0.7, 1.0]]
xy = rng.multivariate_normal(mean, cov, size=1000)

df = pd.DataFrame(xy, columns=["x", "y"])
```

1. Draw `sns.jointplot(data=df, x="x", y="y", kind="hex")`.
2. Save to `/tmp/13_joint_plot.png`. As with `pairplot`, `jointplot` returns a `JointGrid`
   — use `.figure.savefig`.
