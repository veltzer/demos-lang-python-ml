#!/usr/bin/env python

"""Solution to exercise 10: render a 2-D function as an image with a colorbar."""

import numpy as np
import matplotlib.pyplot as plt

i = np.arange(100)[:, None]
j = np.arange(100)[None, :]
z = np.sin(i / 10.0) * np.cos(j / 10.0)

plt.imshow(z, cmap="viridis")
plt.colorbar()
plt.title("sin(i/10) * cos(j/10)")
plt.savefig("/tmp/10_image_and_colormap.png")
