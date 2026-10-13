import pandas as pd

serie = pd.Series(['1','2','3','4','5','6','7','8','9','5','3'])

serie = serie.astype(float)

avg = serie.mean()

std = serie.std()


print("Mean of series values")
print(avg)
print("Standard deviation of series values")
print(std)
