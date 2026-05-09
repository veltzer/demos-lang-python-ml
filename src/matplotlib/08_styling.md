# Exercise 08: Styling Lines

Plot three curves over `x = np.linspace(0, 10, 50)`, each with a distinct visual style:

1. `y1 = x` — solid red line, no markers
2. `y2 = x**1.5` — dashed green line, circle markers (`marker="o"`)
3. `y3 = x**2` — dotted blue line, triangle markers (`marker="^"`), thicker line
   (`linewidth=2`)

Add:

- a legend identifying each curve
- a grid (`plt.grid(True)`)
- title `"Power-law growth"`

Save to `/tmp/08_styling.png`.
