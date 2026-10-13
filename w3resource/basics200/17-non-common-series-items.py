import pandas as pd
import numpy as np

serie1 = pd.Series([1,2,3,4,5])
serie2 = pd.Series([2,4,6,8,10])

#Using concat
serie1diff = serie1[~serie1.isin(serie2)]
serie2diff = serie2[~serie2.isin(serie1)]

print(pd.concat([serie1diff,serie2diff], ignore_index=True))

#Using union and intersect/w3resource solution
seriesunion = pd.Series(np.union1d(serie1,serie2))
seriesintersect = pd.Series(np.intersect1d(serie1,serie2))

result = seriesunion[~seriesunion.isin(seriesintersect)]
print(result)
