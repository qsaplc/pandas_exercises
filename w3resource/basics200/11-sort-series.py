import pandas as pd

serie = pd.Series(['100','200','python','300.12','400'])

print("Pre sorting:\n", serie)

serie = serie.sort_values()

print("Post sorting:\n",serie)
