# Exercise 14: Print and Visualize a Trained Decision Tree

A decision tree classifier is unusual among ML models in that you can read the entire
trained model out — every split condition, every leaf class. There are two complementary
ways to inspect it:

- **Text export** with `sklearn.tree.export_text(clf)` — fast, copy-pasteable,
  terminal-friendly. Good for a small tree or a quick check.
- **Graphical render** with `sklearn.tree.plot_tree(clf)` (uses matplotlib) — much easier
  to read for non-trivial trees, shows the data distribution at each node, exports to
  PNG.

The text output looks like:

```
|--- feature_6 <= 0.50
|   |--- feature_5 <= 26.27
|   |   |--- feature_4 <= 0.50
...
```

`|---` is a node; the indent shows depth.

## Tasks

1. Load `data.csv` (Titanic) and prepare features:
   - drop `Name`, `Embarked`, `Cabin`, `Ticket`,
   - separate `Survived` as the target,
   - fill NaNs with `0`,
   - one-hot encode the remaining categorical columns with `pd.get_dummies`.
2. Print `X.columns` so you can map `feature_0`, `feature_1`, …, back to real column
   names later.
3. Train a `DecisionTreeClassifier` on the full data with a fixed `random_state`. Limit
   `max_depth=4` so the visualization stays readable; without a limit the tree explodes
   to 15+ levels of depth on Titanic.
4. **Text view.** Print the tree using `export_text(clf, feature_names=list(X.columns))`.
5. **Graphical view.** Use `plot_tree(clf, feature_names=list(X.columns),
   class_names=["died", "survived"], filled=True, fontsize=8)` to render the tree as a
   matplotlib figure, then save the figure to `/tmp/14_decision_tree.png` via
   `plt.savefig(..., dpi=150, bbox_inches="tight")`.

## Reflect

After looking at the visualization:

- Which feature is the root split? (Hint: it's almost always `Sex_male` on Titanic.)
- How deep does the tree decide women's survival vs men's?
- Does anything in the tree surprise you? Are there any nodes that look like noise — a
  split on a feature you don't believe should matter?

Other visualization options worth knowing about (referenced in the original exercise):
[mljar's blog post](https://mljar.com/blog/visualize-decision-tree/) covers
`graphviz`-based and `dtreeviz`-based renders that are prettier than `plot_tree` for
publication, at the cost of an extra dependency.
