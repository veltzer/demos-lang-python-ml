# Exercise 09: Two Y-Axes (twinx)

When two series share the same x-axis but live on very different scales, plotting them on
the same y-axis squashes the smaller one. The fix is `Axes.twinx()`, which gives you a
second y-axis on the right that shares the x-axis with the first.

Plot, over `x = np.linspace(0, 10, 100)`:

- `temperature = 20 + 5 * sin(x)` (range: ~15..25), in red, on the **left** y-axis
- `pressure    = 1000 + 50 * cos(x)` (range: ~950..1050), in blue, on the **right** y-axis

1. Create the figure with `fig, ax1 = plt.subplots()`.
2. Plot temperature on `ax1`. Label its y-axis `"temperature (C)"` and color the label
   red.
3. Create `ax2 = ax1.twinx()`. Plot pressure on `ax2`. Label its y-axis
   `"pressure (hPa)"` and color the label blue.
4. Title the figure `"Temperature and pressure"`.
5. Save to `/tmp/09_dual_axis.png`.
