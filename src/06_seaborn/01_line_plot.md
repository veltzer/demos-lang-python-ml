# Exercise 02: Line Plot with Confidence Band

When the same `x` value appears multiple times in your data, `sns.lineplot` aggregates
the `y` values and draws a translucent confidence band around the mean.

Build a DataFrame where each `x` in `0..9` appears 5 times, with `y = 2*x + noise`:

```text
import numpy as np

rng = np.random.default_rng(0)
xs = np.repeat(np.arange(10), 5)
ys = 2 * xs + rng.normal(scale=2.0, size=xs.shape)

df = pd.DataFrame({"x": xs, "y": ys})
```

1. Draw `sns.lineplot(data=df, x="x", y="y")`. Note that seaborn automatically draws the
   95% confidence band around the mean.
2. Save to `/tmp/02_line_plot.png`.
