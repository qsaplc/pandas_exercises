import pandas as pd

serie = pd.Series({'A':1,'B':2,'C':3,'D':4,'E':5})

print("Pre reorder of series")
print(serie)

serie_reordered = serie.reindex(['B','A','C','D','E'])

print("Series reordered")
print(serie_reordered)
