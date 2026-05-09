# Exercise 11: Euclidean Distance

Given two points in n-dimensional space:

```
p1 = (x1, x2, x3, ..., xn)
p2 = (y1, y2, y3, ..., yn)
```

The Euclidean distance between `p1` and `p2` is:

```
d = sqrt((x1 - y1)^2 + (x2 - y2)^2 + ... + (xn - yn)^2)
```

Tasks:

1. Implement a function `euclidean(p1, p2)` that takes two 1-D NumPy arrays and returns
   the distance. Do it as a single vectorized expression — no Python loop.
2. Test it on `p1 = [1, 2, 3]` and `p2 = [4, 6, 8]`. The expected answer is
   `sqrt(9 + 16 + 25) = sqrt(50) ≈ 7.0711`.
3. Bonus: implement `pairwise(points)` that takes a 2-D array of shape `(N, D)` and
   returns the `(N, N)` matrix of pairwise distances. Use broadcasting:
   `points[:, None, :] - points[None, :, :]`.
