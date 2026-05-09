# Exercise 16: Complete the Series (Visual Puzzle)

You are given a scatter of points on a 2-D axis. Your task: come up with a function that
*could* have produced these points, and demonstrate that any number of functions could
generate the same finite scatter.

The original puzzle (drawn as ASCII):

```
	|
	|
	|
	|				*
	|
	|					*
	|			*		    *
	|					    *
	|						*
	|		*
	|	*
	|
	|
	---------------------------------------------x---------------------------------
```

There are roughly 7 visible points. Reading off approximate `(x, y)` coordinates by eye
(each tab counts as one column unit, every blank line counts as one row unit going down),
you can see the points trend upward roughly linearly with some noise.

Tasks:

1. Read the points off the diagram above and store them in two lists `xs` and `ys`.
   Approximations are fine — six to eight points is enough.
2. Fit a polynomial of degree 1 (a line) through the points using `numpy.polyfit` and
   print the slope and intercept.
3. Fit a polynomial of degree `len(xs) - 1` through the same points (an exact fit) and
   print its coefficients.
4. Print both predictions at `x = 100` to see how wildly extrapolation differs between a
   simple model and a perfect-fit model.

Lesson: any finite scatter has infinitely many functions that produce it. A simple model
extrapolates predictably; a high-degree exact-fit model does not. This is the classic
overfitting trap.
