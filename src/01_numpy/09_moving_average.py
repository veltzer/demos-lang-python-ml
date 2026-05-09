#!/usr/bin/env python

"""Solution to exercise 10: vectorized moving average via cumsum."""

import numpy as np


def moving_average(a: np.ndarray, window: int) -> np.ndarray:
    csum = np.cumsum(np.insert(a.astype(float), 0, 0.0))
    return (csum[window:] - csum[:-window]) / window


def main() -> None:
    a = np.arange(1, 11)
    print(moving_average(a, 3))


if __name__ == "__main__":
    main()
