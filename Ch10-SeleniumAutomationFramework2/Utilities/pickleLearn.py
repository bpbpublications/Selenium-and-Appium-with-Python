import pickle

# Define a list of dictionaries
employee = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35}
]

# Serialize the list of dictionaries
with open('people.pickle', 'wb') as f:
    pickle.dump(employee, f)

selialized_data = pickle.dumps(employee)
print(selialized_data)


# Deserialize the list of dictionaries
with open('people.pickle', 'rb') as f:
    loaded_employee = pickle.load(f)

# Print the loaded people
print(loaded_employee)
