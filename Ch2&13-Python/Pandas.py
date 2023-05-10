import pandas as pd
import json
import numpy as np

# Series is like a column in the table, it is one dimentional array holding data of any type

a = ["series", "can", 4, "all", "data", 8.9]
my_var = pd.Series(a)
print(my_var)
print(my_var[5])
my_var = pd.Series(a, index=["a", "b", "c", "d", "e", "f"])
print(my_var)

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
my_var1 = pd.DataFrame(data, index=["a", "b", "c"])
print(my_var1)
print(my_var1.loc[["a", "b"]])

currency = pd.read_csv("currency.csv")
print(currency)
print(pd.options.display.max_rows)
print(currency.head(10))
print(currency.tail())  # last 5

# filename = 'sample.json'
#
# dict1 = json.loads("Users/yogashivamathivanan/PycharmProjects/Python20223/sample.json")

calories1 = [420, 380, 390]
duration1 = [50, 40, 45]
d = {"Cars": calories1, "Bikes": duration1}
s = set(duration1)
li = list(dict.fromkeys(
    duration1))  # This will remove the duplicate values as well like converting to set as Keys in dict need to be unique
print(type(li))
print(type(s))
df1 = pd.DataFrame()
df1["calories"] = calories1
df1["duration"] = duration1
df2 = pd.DataFrame(d)
print(df1)
print(df2)

arr = np.array([1, 5, 5, 100, 4, 48])
arr2 = np.array([3, 6, 8, 10, 30, 45])
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.vstack((arr, arr2)))

ab = "strNHGHUIJIHVUJBVksadnfiojn"
print(ab.capitalize())
print(ab.lower())

triple = lambda x: x * 3
print(triple(300))

#PICKLING - Converting Python Object into Byte Stream to store in Database, UNPICKLING is revese.

