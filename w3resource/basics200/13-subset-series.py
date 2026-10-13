import pandas as pd

serie = pd.Series([0,1,2,3,4,5,6,7,8,9,10])

print("Full series:\n",serie)

subset = serie[serie  <= 5]

print("Subset made with condition:\n", subset)
