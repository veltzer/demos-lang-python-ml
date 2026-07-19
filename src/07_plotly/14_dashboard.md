# Exercise 14: A Mini Dashboard

The capstone for this folder. Build a single HTML page that combines:

- a **scatter plot** (top-left) of `(x, y)` colored by `label`,
- a **bar chart** (top-right) of mean `y` per label,
- a **histogram** (bottom-left) of `y`,
- a **box plot** (bottom-right) of `y` per label.

All four panels should share the same source DataFrame. This is the kind of one-pager
analysts ship to non-technical stakeholders.

Build:

```text
import numpy as np

rng = np.random.default_rng(0)
n = 100
df = pd.DataFrame({
    "x":     np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n), rng.normal(-3, 1, n)]),
    "y":     np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n), rng.normal(-3, 1, n)]),
    "label": ["A"] * n + ["B"] * n + ["C"] * n,
})
```

Tasks:

1. `from plotly.subplots import make_subplots` and `import plotly.graph_objects as go`.
2. Build `fig = make_subplots(rows=2, cols=2, subplot_titles=("Scatter", "Mean y by
   label", "Histogram of y", "Box plot of y"))`.
3. Add a scatter trace per label (so colors stay distinct) at row 1, col 1.
4. Compute `df.groupby("label")["y"].mean()`. Add a `go.Bar` trace at row 1, col 2.
5. Add a `go.Histogram(x=df["y"])` at row 2, col 1.
6. Add a `go.Box` trace per label at row 2, col 2 (each with `name=<label>`,
   `y=<that-label's-y-values>`).
7. `fig.update_layout(height=800, title_text="Dashboard", showlegend=False)`.
8. Save to `/tmp/14_dashboard.html`.

The result is an interactive 4-panel page you can hand to anyone with a browser.
