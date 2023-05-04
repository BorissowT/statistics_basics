import pandas as pd
import functools


sample = pd.Series(
    [7.1, 6.3, 6.2, 5.8, 7.7, 6.8, 6.7, 5.9, 5.7, 5.1])

dispersion = functools.reduce(lambda a, b: a+b,
                              map(lambda x: (x-sample.mean())**2, sample)
                              )/(sample.size-1)


print(dispersion)
