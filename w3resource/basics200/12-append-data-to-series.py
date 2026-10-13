import pandas as pd

serie = pd.Series(['100','200','python','300.12','400'])

print("Pre append\n", serie)

serie = pd.concat([serie,pd.Series(['500','php'])], ignore_index=True)

print("Post append\n", serie)
