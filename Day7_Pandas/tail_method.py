import pandas as pd

data = pd.read_csv('people_data.csv')

series = data["First Name"]

bottom = series.tail()

print("Last 5:")
print(bottom)

print("__________________________________________________-")


series = data[["First Name","Last Name"]]

bottom = series.tail(8)

print("Fertility rate:")
print(bottom)

print("__________________________________________________-")