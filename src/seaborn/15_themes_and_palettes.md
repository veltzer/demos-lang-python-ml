# Exercise 15: Themes and Color Palettes

Seaborn ships with several built-in *themes* (axes background, gridlines, fonts) and
*palettes* (sequences of colors for categorical hues). Switch them globally with
`sns.set_theme` and `sns.set_palette`.

Plot the same scatter four times in a 2x2 grid, each subplot using a different
combination of theme and palette. Use this dataset:

```
import numpy as np

rng = np.random.default_rng(0)
n = 60
df = pd.DataFrame({
    "x":     np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n), rng.normal(-3, 1, n)]),
    "y":     np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n), rng.normal(-3, 1, n)]),
    "label": ["A"] * n + ["B"] * n + ["C"] * n,
})
```

For each combination below, set the theme + palette, then draw a scatter on the
corresponding axes:

| subplot       | theme         | palette       |
| ------------- | ------------- | ------------- |
| top-left      | `"darkgrid"`  | `"deep"`      |
| top-right     | `"whitegrid"` | `"pastel"`    |
| bottom-left   | `"ticks"`     | `"colorblind"`|
| bottom-right  | `"white"`     | `"muted"`     |

Hint: `sns.set_theme(style=...)` resets matplotlib's rcParams globally — call it before
each `sns.scatterplot(..., ax=axes[i, j])`.

Title each subplot `"<style> + <palette>"`. Call `fig.tight_layout()` and save to
`/tmp/15_themes_and_palettes.png`.
