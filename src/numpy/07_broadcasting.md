# Exercise 07: Broadcasting

Center the columns of a matrix: subtract each column's mean from every entry in that column,
so each resulting column has mean `0`.

Starting from `m = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])`,
produce the centered matrix and print:

1. the centered matrix
2. the mean of each column of the centered matrix (should be all zeros)

Do it in one expression using broadcasting — no loops.
