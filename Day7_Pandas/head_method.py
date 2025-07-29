import pandas as pd

data = pd.read_csv('people_data.csv')

series = data["First Name"]

top = series.head()

print("People:")
print(top)

print("__________________________________________________-")


series = data[["First Name","Last Name"]]

top = series.head(8)

print("People:")
print(top)

print("__________________________________________________-")