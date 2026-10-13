import pandas as pd

df = pd.DataFrame({"col1":[1,2,3,4,7,11],"col2":[4,5,6,9,5,0],"col3":[7,5,8,12,1,11]})

print("DataFrame:\n",df.head(5))

# Calling Series function from pandas
#serie = pd.Series(df["col1"])

# Using iloc
serie = df.iloc[:,0]

#Reference by column name
#serie = df.['col1']

print("First column of DataFrame to Series \n",serie)
