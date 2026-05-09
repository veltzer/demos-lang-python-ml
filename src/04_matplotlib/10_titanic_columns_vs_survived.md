# Exercise 10: Titanic — Plot Each Column Against Survived

A standard EDA (exploratory data analysis) move on a classification problem: plot each
feature column against the target. If the two values of the target separate visibly
along a feature axis, that feature is likely predictive. If the two distributions
overlap completely, the feature probably won't help.

## Tasks

1. Load the Titanic CSV (`../../data/titanic.csv`).
2. Drop or skip columns that aren't useful to plot (`Name`, `Ticket`, `Cabin`,
   `PassengerId`).
3. For each remaining feature column produce a 2-D plot against `Survived`. Choose the
   plot type per column:
   - **Numeric columns** (`Age`, `Fare`, `SibSp`, `Parch`, `Pclass`): histogram of the
     column split by `Survived` (use `hist` with two stacked groups, or two overlaid
     translucent histograms).
   - **Categorical columns** (`Sex`, `Embarked`): grouped bar chart of the
     `Survived`-rate per category (compute with `groupby(col)["Survived"].mean()`).
4. Arrange them in a grid with `plt.subplots(rows, cols)` and save to
   `/tmp/10_titanic_columns_vs_survived.png`.

## Reflect

After looking at the plots:

- Which features separate the two classes well?
- Which features look like noise?
- Are there any surprises?

The clearest signal you should see on Titanic is `Sex` (women survived at much higher
rates) and `Pclass` (1st-class passengers survived more than 3rd). `Age` shows a small
"women and children first" bump for the youngest, but otherwise the two distributions
overlap heavily.
