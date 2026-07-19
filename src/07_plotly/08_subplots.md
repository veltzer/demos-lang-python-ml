# Exercise 08: Manual Subplots with `make_subplots`

Faceting works when the subplots share a common plot type. When you want *different*
plot types in one figure (a bar chart on the left, a line chart on the right), drop down
to `plotly.graph_objects` and use `make_subplots`.

Build:

```text
import numpy as np

rng = np.random.default_rng(0)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 135, 150, 160, 180, 200]
samples = rng.normal(loc=10, scale=2, size=300)
```

Tasks:

1. `from plotly.subplots import make_subplots` and `import plotly.graph_objects as go`.
2. Build a 1-row, 2-column figure: `fig = make_subplots(rows=1, cols=2,
   subplot_titles=("Monthly sales", "Sample distribution"))`.
3. Add a `go.Bar(x=months, y=sales)` to row 1, col 1 with `fig.add_trace(..., row=1, col=1)`.
4. Add a `go.Histogram(x=samples)` to row 1, col 2.
5. Save to `/tmp/08_subplots.html`.
