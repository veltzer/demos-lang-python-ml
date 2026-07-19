# Exercise 10: Regression Plot

`sns.regplot` draws a scatter plot **and** fits an ordinary least-squares regression line
through it, with a translucent confidence band around the line. It is the fastest way to
eyeball whether a linear relationship is plausible.

Generate 100 noisy points from a linear model:

```text
import numpy as np

rng = np.random.default_rng(0)
x = rng.uniform(0, 10, 100)
y = 2.5 * x + 1.0 + rng.normal(0, 3, 100)

df = pd.DataFrame({"x": x, "y": y})
```

1. Draw `sns.regplot(data=df, x="x", y="y")`.
2. Title `"Regression fit"`.
3. Save to `/tmp/10_regression_plot.png`.
