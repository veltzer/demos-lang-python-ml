# Exercise 12: Animation Frames

Pass `animation_frame=` to any `plotly.express` function and the resulting figure gets
play/pause buttons and a slider — each frame is the subset of the data corresponding to
one value of the animation column.

Build a per-year scatter dataset:

```
import numpy as np

rng = np.random.default_rng(0)
years = list(range(2010, 2021))
rows = []
for year in years:
    n = 50
    rows.append(pd.DataFrame({
        "year": year,
        "x":    rng.normal(year - 2010, 2, n),
        "y":    rng.normal(year - 2010, 2, n),
        "size": rng.uniform(5, 20, n),
    }))
df = pd.concat(rows, ignore_index=True)
```

Tasks:

1. Draw `px.scatter(df, x="x", y="y", size="size", animation_frame="year",
   range_x=[-5, 15], range_y=[-5, 15])`. The `range_x` and `range_y` keep the axes
   stable across frames so motion is meaningful.
2. Save to `/tmp/12_animation.html`. Open it and use the play button to watch the
   distribution drift outward over time.
