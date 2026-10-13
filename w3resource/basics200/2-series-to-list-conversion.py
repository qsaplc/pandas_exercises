import pandas as pd

serie = pd.Series([2,3,4,5,6])

print(serie, type(serie))
print("Convert serie to list")

print(serie.to_list(), type(serie.to_list()))
