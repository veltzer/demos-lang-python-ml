#!/usr/bin/env python

"""Solution to exercise 11: Euclidean distance and pairwise distance matrix."""

import numpy as np


def euclidean(p1: np.ndarray, p2: np.ndarray) -> float:
    return float(np.sqrt(np.sum((p1 - p2) ** 2)))


def pairwise(points: np.ndarray) -> np.ndarray:
    diff = points[:, None, :] - points[None, :, :]
    return np.sqrt((diff ** 2).sum(axis=-1))


def main() -> None:
    p1 = np.array([1.0, 2.0, 3.0])
    p2 = np.array([4.0, 6.0, 8.0])
    print(euclidean(p1, p2))

    points = np.array([[0.0, 0.0], [3.0, 4.0], [6.0, 8.0]])
    print(pairwise(points))


if __name__ == "__main__":
    main()
