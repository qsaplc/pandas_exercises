import pandas as pd

serie = pd.Series([100,200,'python',300.12,400])

print("Serie pre data change \n", serie)

serie = pd.to_numeric(serie, errors='coerce')

print("Serie post data change \n",serie)
