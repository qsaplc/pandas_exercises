import pandas as pd

dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

series = pd.Series(dict)

print(series)

print(series['a'])
