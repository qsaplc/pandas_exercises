import pandas as pd
import numpy as np

serie = pd.Series([1,2,3,4,5,6,7])

# My solution, using pandas functions
print(serie.quantile(q=0))
print(serie.quantile(q=0.25))
print(serie.quantile(q=0.5))
print(serie.quantile(q=0.75))
print(serie.median()) # same as quantile 0.5
print(serie.max()) # same as quantile 1

print(np.percentile(serie, q=[0,25,50,75,100]))
