# Exercise 06: Subplot Grid

Use `plt.subplots(2, 2)` to create a 2x2 grid of axes (4 subplots in one figure).
On `x = np.linspace(0, 2*pi, 100)`, draw:

- top-left: `sin(x)`, title `"sin"`
- top-right: `cos(x)`, title `"cos"`
- bottom-left: `tan(x)` clipped to `[-5, 5]` (set `ylim`), title `"tan (clipped)"`
- bottom-right: `sin(x) * cos(x)`, title `"sin*cos"`

Call `fig.tight_layout()` so titles and axes don't overlap, and save the figure to
`/tmp/06_subplots.png`.
