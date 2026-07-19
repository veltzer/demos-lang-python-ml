# Exercise 12: Sensor Data Pipeline — Masking, Filtering and Fast Expressions

You receive a large batch of raw readings from a fleet of sensors. The data is big
enough (10 million readings, 1000 sensors) that sloppy NumPy code is visibly slow,
so every step must be fully vectorized — no Python loop over readings or sensors.

## The data

Generate it with a fixed seed so results are reproducible:

```python
rng = np.random.default_rng(42)
N, S = 10_000_000, 1_000

sensor = rng.integers(0, S, size=N)          # which sensor produced each reading
base   = rng.uniform(10.0, 50.0, size=S)     # per-sensor baseline
sigma  = rng.uniform(0.5, 2.0, size=S)       # per-sensor noise level
values = base[sensor] + rng.normal(0.0, 1.0, size=N) * sigma[sensor]

# corrupt the data:
values[rng.random(N) < 0.01] = np.nan        # ~1% dead readings
spikes = rng.random(N) < 0.005               # ~0.5% spikes
values[spikes] += rng.choice([-100.0, 100.0], size=int(spikes.sum()))
```

## Tasks

1. **Masking.** Build a boolean mask of the valid (non-NaN) readings. Print how many
   readings are dead and what percentage of the batch that is.

2. **Per-sensor statistics without a loop.** Compute each sensor's `count`, `mean`
   and `std` over its *valid* readings only — in a constant number of passes over the
   data, with no loop over the 1000 sensors. Hint: `np.bincount(sensor, weights=...)`
   gives you per-sensor sums; get the variance from the algebraic identity
   `var = E[x^2] - E[x]^2` so a second `bincount` over `values**2` is all you need.

3. **Outlier filtering.** A reading is an outlier if it is more than 4 standard
   deviations away from *its own sensor's* mean. Broadcast the per-sensor stats back
   onto the readings with fancy indexing (`mean[sensor]`, `std[sensor]`), build the
   outlier mask, and print how many outliers were caught (it should be close to the
   ~0.5% of spikes that were injected). Produce a `clean` array holding only the
   valid, non-outlier readings and its matching `sensor` ids.

4. **Expression massaging.** For every clean reading compute the health score

   ```text
   score = exp(-((v - mean[sensor]) / std[sensor])^2 / 2)
   ```

   Implement it twice:

   * `score_naive` — the formula written directly, as one expression. Count the
     temporary arrays it allocates.
   * `score_fast` — the same math massaged for speed: pre-divide so the inner loop
     does `v * inv_std[sensor] - shift[sensor]` (one multiply and one subtract
     instead of a subtract and a divide), then square, halve and negate **in place**
     (`*=`, `-=`), and finish with `np.exp(..., out=...)` so no new temporaries are
     created.

   Time both with `time.perf_counter()`, verify they agree with `np.allclose`, and
   print the speedup.

5. **Budget.** Print the total wall-clock time of the whole pipeline (excluding data
   generation). On a modern machine everything should finish in well under 2 seconds;
   if it takes tens of seconds, something is looping in Python.
