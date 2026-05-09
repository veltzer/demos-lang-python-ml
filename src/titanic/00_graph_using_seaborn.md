# Stage 00: Visual Exploration with Seaborn

This is the first step of a multi-stage Titanic pipeline. Before cleaning anything,
*look* at the data — a few well-chosen plots will tell you which features are likely to
matter and which are mostly noise.

## Setup

1. Set `random.seed(0)` and `numpy.random.seed(0)` so plots are reproducible.
2. Load the raw Titanic dataset from `../data/titanic.csv`.

## Tasks

Try each of these plots (the solution leaves the first three commented out as
alternatives, with the fourth as the final choice):

1. **Regression plot of Age vs Survived** — `seaborn.regplot(x=df['Age'],
   y=df['Survived'])`. Useful as a sanity check, but Survived is binary, so the line is
   only mildly informative.
2. **Histogram of Age** — `seaborn.histplot(df['Age'], bins=16)`. Shows the age
   distribution overall.
3. **Histogram of Age split by Sex** — `seaborn.histplot(df, x='Age', hue='Sex',
   multiple='dodge')`. Useful but doesn't show survival.
4. **Histogram of Age split by Survived × Sex** — combine the two categorical columns
   into one (`df['Survived_Sex'] = df['Survived'].astype(str) + '_' + df['Sex']`) and
   plot a dodged histogram with `hue='Survived_Sex'`.

Call `plt.show()` to display each plot.

## What you should see

The Survived × Sex split is the punchline: **female passengers survived at much higher
rates than males at every age**. That single plot motivates "Sex" as the most important
feature in everything that follows.

## Pipeline note

This stage produces no output file — it is purely exploratory. The real cleaning starts
at stage 01.
