import pandas as pd

serie1 = pd.Series([1,2,3,4,5])
serie2 = pd.Series([2,4,6,8,10])

print("Serie1:\n",serie1)
print("Serie2:\n",serie2)

print("Items of serie1 not in serie2")
seriediff = serie1[~serie1.isin(serie2)]

print(seriediff)
