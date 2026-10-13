import pandas as pd
import numpy as np

serie = pd.Series([100,200,'python',300.12,400])

print("Pre transformation \n", type(serie))
print(serie)

#Using numpy array
#arr = np.array(serie)

#Using pandas
arr = serie.values

print("Post transformation \n", type(arr))
print(arr)
