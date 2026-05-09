# Exercise 09: Random Sampling and Statistics

Using a seeded random generator (`np.random.default_rng(42)`):

1. Draw 10000 samples from a normal distribution with mean `5` and standard deviation `2`.
2. Print the empirical mean and standard deviation — they should be close to `5` and `2`.
3. Print the fraction of samples that fall within one standard deviation of the mean
   (i.e. in the interval `[3, 7]`) — for a normal distribution this should be ~0.68.
