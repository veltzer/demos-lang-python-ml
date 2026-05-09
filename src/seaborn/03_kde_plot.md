# Exercise 04: Kernel Density Plot

A KDE (kernel density estimate) is a smoothed version of a histogram — useful when you
want to compare the *shape* of two distributions rather than their bin counts.

1. Generate two samples of size 1000 from `np.random.default_rng(0)`:
   - `a` from `N(0, 1)`
   - `b` from `N(2, 1.5)`
2. Plot both KDEs on the same axes:
   - `sns.kdeplot(a, label="a", fill=True)`
   - `sns.kdeplot(b, label="b", fill=True)`
3. Add a legend.
4. Save to `/tmp/04_kde_plot.png`.
