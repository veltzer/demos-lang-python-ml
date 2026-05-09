# Exercise 10: 2-D Image with Colormap

`plt.imshow` displays a 2-D array as an image — each cell is colored by its value
according to a colormap.

1. Build a 100x100 array `z` with `z[i, j] = sin(i / 10.0) * cos(j / 10.0)`.
   Use a single broadcasting expression (no Python loops):
   `i = np.arange(100)[:, None]`, `j = np.arange(100)[None, :]`.
2. Display it with `plt.imshow(z, cmap="viridis")`.
3. Add a colorbar with `plt.colorbar()`.
4. Set the title to `"sin(i/10) * cos(j/10)"`.
5. Save to `/tmp/10_image_and_colormap.png`.
