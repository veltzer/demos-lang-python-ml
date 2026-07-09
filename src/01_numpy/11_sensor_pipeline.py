#!/usr/bin/env python

"""Solution to exercise 12: large-scale sensor pipeline — masking, filtering, fast expressions."""

import time

import numpy as np


def generate(n: int, s: int) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(42)
    sensor = rng.integers(0, s, size=n)
    base = rng.uniform(10.0, 50.0, size=s)
    sigma = rng.uniform(0.5, 2.0, size=s)
    values = base[sensor] + rng.normal(0.0, 1.0, size=n) * sigma[sensor]
    values[rng.random(n) < 0.01] = np.nan
    spikes = rng.random(n) < 0.005
    values[spikes] += rng.choice([-100.0, 100.0], size=int(spikes.sum()))
    return sensor, values


def sensor_stats(sensor: np.ndarray, values: np.ndarray, s: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Per-sensor count/mean/std in two bincount passes — no loop over sensors."""
    cnt = np.bincount(sensor, minlength=s)
    sums = np.bincount(sensor, weights=values, minlength=s)
    sumsq = np.bincount(sensor, weights=values * values, minlength=s)
    mean = sums / cnt
    var = sumsq / cnt - mean * mean  # var = E[x^2] - E[x]^2
    return cnt, mean, np.sqrt(var)


def score_naive(clean: np.ndarray, clean_sensor: np.ndarray, mean: np.ndarray, std: np.ndarray) -> np.ndarray:
    return np.exp(-(((clean - mean[clean_sensor]) / std[clean_sensor]) ** 2) / 2.0)


def score_fast(clean: np.ndarray, clean_sensor: np.ndarray, mean: np.ndarray, std: np.ndarray) -> np.ndarray:
    inv_std = 1.0 / std
    shift = mean * inv_std
    z = clean * inv_std[clean_sensor]
    z -= shift[clean_sensor]
    z *= z
    z *= -0.5
    return np.exp(z, out=z)


def main() -> None:
    n, s = 10_000_000, 1_000
    sensor, values = generate(n, s)

    start = time.perf_counter()

    # 1. mask the dead (NaN) readings
    valid = ~np.isnan(values)
    dead = n - int(np.count_nonzero(valid))
    print(f"dead readings: {dead} ({100.0 * dead / n:.2f}%)")

    # 2. per-sensor stats over valid readings only
    cnt, mean, std = sensor_stats(sensor[valid], values[valid], s)
    print(f"sensor counts: min={cnt.min()} max={cnt.max()}")
    print(f"sensor means:  min={mean.min():.2f} max={mean.max():.2f}")

    # 3. filter outliers: > 4 sigma from their own sensor's mean
    deviation = np.abs(values - mean[sensor])
    outlier = valid & (deviation > 4.0 * std[sensor])
    print(f"outliers caught: {int(outlier.sum())} ({100.0 * outlier.sum() / n:.2f}%)")

    keep = valid & ~outlier
    clean = values[keep]
    clean_sensor = sensor[keep]
    print(f"clean readings: {clean.size}")

    # 4. health score: naive vs massaged expression
    t0 = time.perf_counter()
    naive = score_naive(clean, clean_sensor, mean, std)
    t1 = time.perf_counter()
    fast = score_fast(clean, clean_sensor, mean, std)
    t2 = time.perf_counter()

    assert np.allclose(naive, fast)
    print(f"score_naive: {t1 - t0:.3f}s  score_fast: {t2 - t1:.3f}s  speedup: {(t1 - t0) / (t2 - t1):.2f}x")
    print(f"mean health score: {fast.mean():.4f}")

    # 5. total budget
    print(f"pipeline total: {time.perf_counter() - start:.3f}s")


if __name__ == "__main__":
    main()
