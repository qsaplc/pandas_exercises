import pandas as pd

serie = pd.Series(
        [['Red','Green','White'],
         ['Red','Black'],
         ['Yellow']
            ]
        )

#Using explode
#flatten_serie = serie.explode().reset_index(drop=True)

#Using .apply().stack()
flatten_serie = serie.apply(pd.Series).stack().dropna().reset_index(drop=True)

print("Pre flattened\n",serie)

print("Post flattened\n",flatten_serie)
