import pandas as pd

print("PANDAS SERIES")
x = [3, 12, 36]
y = {"Fruit1": "apple", "Fruit2": "banana", "Fruit3":"Orange"}
index = ['a', 'b', 'c']
var_x = pd.Series(x, index)
var_y = pd.Series(y)
print(var_y)


print("PANDAS DATAFRAMES")
animal_data = {
    'animals': ['dogs', 'cats', 'rats', 'camels'],
    'name': ['Alice', 'Bob', 'Charlie', 'Adam'],
    'age': [2, 4, 7, 9],
    'city': ['New York', 'Paris', 'London', 'Tokyo']
}
index = ['a', 'b', 'c', 'd']
var_animal = pd.DataFrame(animal_data, index)
print(var_animal)