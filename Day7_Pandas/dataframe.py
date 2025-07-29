import pandas as pd
import numpy as np


df = pd.DataFrame()
print(df)

print("______________________________")

lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']


df = pd.DataFrame(lst)

print(df)

print("______________________________")


data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df)

print("______________________________")

dict = {'customers': ['Aditya','Raghav','Naveen','Jahnvi'],
        'orders' : ['Mango','Apple','Banana','Orange'],
        'quantity': [1,2,3,4]}

df = pd.DataFrame(dict)
print(df)

print("______________________________")
