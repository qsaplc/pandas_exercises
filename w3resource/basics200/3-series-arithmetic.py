import pandas as pd

series1 = pd.Series([2,4,6,8,10])
series2 = pd.Series([1,3,5,7,9])

add = series1 + series2
subtract = series1 - series2
multiple = series1 * series2
divide = series1 / series2

print("add\n", add)
print("subtract\n", subtract)
print("multiple\n", multiple)
print("divide\n", divide)

