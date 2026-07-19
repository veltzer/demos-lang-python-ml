# Distance Metrics

Many ML algorithms — KNN, K-Means, hierarchical clustering, t-SNE — depend on a notion of
"distance" between two points in feature space. There is no single canonical definition;
the right choice depends on what your features mean and what kind of similarity you care
about.

## Notation

Given two points in `n`-dimensional space:

```text
p = (p_1, p_2, ..., p_n)
q = (q_1, q_2, ..., q_n)
```

## The three classics

### Euclidean distance

The straight-line distance you'd measure with a ruler:

```text
d_euclidean(p, q) = sqrt( sum over i of (p_i - q_i)^2 )
```

The default for almost everything. Works well when your features are commensurable —
i.e. all numeric, all on similar scales (which is why standardization matters before
KNN).

### Manhattan distance (a.k.a. L1, taxicab, city-block)

The distance you'd walk on a grid of streets where you can't cut through buildings:

```text
d_manhattan(p, q) = sum over i of |p_i - q_i|
```

More forgiving of outliers along a single axis than Euclidean (because it doesn't square
the differences). Useful when one feature being far off shouldn't dominate the entire
distance.

### Chebyshev distance (a.k.a. L_infinity, max distance)

The largest single-axis disagreement:

```text
d_chebyshev(p, q) = max over i of |p_i - q_i|
```

Two points are "close" only if they're close on **every** axis. Useful when you want any
single big gap to disqualify a match — e.g. in chess, the king's move count is a
Chebyshev distance.

## Visualizing them: the unit circle

The set of points at distance 1 from the origin — the *unit ball* — looks different for
each metric:

```text
Euclidean (L2):           Manhattan (L1):           Chebyshev (L_inf):

      ****                       *                  ****************
   **      **                  *   *                *              *
  *          *                *     *               *              *
  *          *               *       *              *              *
  *          *              *         *             *              *
  *          *             *           *            *              *
   **      **               *         *             *              *
      ****                   *       *              *              *
                              *     *               *              *
                               *   *                *              *
                                 *                  ****************
   (a smooth circle)         (a diamond)           (a square aligned
                                                    with the axes)
```

Same "distance 1", three completely different shapes.

## Which one should you use?

- **Default to Euclidean** if features are continuous, comparable, and standardized.
- **Manhattan** when individual large differences should not be squared, or when you
  want a metric that's more robust to outliers.
- **Chebyshev** when you want "close on every axis" semantics, or when you're
  modelling a grid-based movement.
- For **categorical** features none of these are appropriate — use Hamming distance
  (count of differing positions) or a similarity measure built for the domain.

## In code

scikit-learn's distance-based estimators (`KNeighborsClassifier`, `KMeans`, etc.) take a
`metric=` parameter:

```text
KNeighborsClassifier(metric="euclidean")   # default
KNeighborsClassifier(metric="manhattan")
KNeighborsClassifier(metric="chebyshev")
```

`scipy.spatial.distance` has all three (`euclidean`, `cityblock`, `chebyshev`) plus
~20 others if you want to experiment.
