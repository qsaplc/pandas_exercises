import pandas as pd

series1 = pd.Series([2,4,6,8.10])
series2 = pd.Series([1,3.5,7,9])

print("Greater than")
print(series1>series2)

print("Lesser than")
print(series1<series2)

print("Equal")
print(series1==series2)
