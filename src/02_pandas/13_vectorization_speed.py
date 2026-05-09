#!/usr/bin/env python

"""Solution to exercise 14: compare vectorized vs apply vs Python-loop timings."""

import time
import numpy as np
import pandas as pd


def time_it(label: str, func) -> None:
    t0 = time.perf_counter()
    func()
    t1 = time.perf_counter()
    print(f"{label}: {t1 - t0:.4f} s")


def main() -> None:
    n = 1_000_000
    df = pd.DataFrame({0: pd.Series(np.random.randn(n))})

    df1 = df.copy()
    time_it("vectorized .abs()", df1[0].abs)

    df2 = df.copy()
    time_it("apply(abs)", lambda: df2[0].apply(abs))

    df3 = df.copy()

    def loop() -> None:
        for i in range(df3.shape[0]):
            df3.iat[i, 0] = abs(float(df3.iat[i, 0]))

    time_it("python for-loop", loop)


if __name__ == "__main__":
    main()
