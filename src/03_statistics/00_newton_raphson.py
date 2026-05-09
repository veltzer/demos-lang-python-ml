#!/usr/bin/env python

"""Solution: Newton-Raphson for roots and for minima (via derivative)."""

from typing import Callable


def newton_raphson_root(
    f: Callable[[float], float],
    initial_guess: float = 1.0,
    max_iterations: int = 1000,
    dx: float = 0.001,
    precision: float = 0.001,
) -> float | None:
    x = initial_guess
    for _ in range(max_iterations):
        y = f(x)
        if abs(y) < precision:
            return x
        derivative = (f(x + dx) - f(x - dx)) / (2 * dx)
        if derivative == 0:
            return None
        x -= y / derivative
    return None


def newton_raphson_min(
    f: Callable[[float], float],
    initial_guess: float = 1.0,
    max_iterations: int = 1000,
    dx: float = 0.001,
    precision: float = 0.001,
) -> float | None:
    x = initial_guess
    for _ in range(max_iterations):
        first = (f(x + dx) - f(x - dx)) / (2 * dx)
        if abs(first) < precision:
            return x
        second = (f(x + dx) - 2 * f(x) + f(x - dx)) / (dx * dx)
        if second == 0:
            return None
        x -= first / second
    return None


def cube_minus_8(x: float) -> float:
    return x * x * x - 8


def square(x: float) -> float:
    return x * x


def quartic(x: float) -> float:
    return (x - 3) ** 4 + 5


print(f"root of x^3 - 8: {newton_raphson_root(cube_minus_8)}")
print(f"min of x^2:       {newton_raphson_min(square)}")
print(f"min of (x-3)^4+5: {newton_raphson_min(quartic, initial_guess=0.0)}")
