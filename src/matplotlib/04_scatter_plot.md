# Exercise 04: Scatter Plot

Generate 200 random `(x, y)` points where `x ~ N(0, 1)` and `y = 2*x + noise` with
`noise ~ N(0, 1)`. Use `np.random.default_rng(0)` for reproducibility.

1. Draw a scatter plot with `plt.scatter`.
2. Color each point by its `x` value (pass `c=x`).
3. Set marker size to 20 (`s=20`).
4. Add a colorbar with `plt.colorbar()`.
5. Label the axes `"x"` and `"y"`, give the plot the title `"Linear relationship with noise"`.
6. Save to `/tmp/04_scatter_plot.png`.
