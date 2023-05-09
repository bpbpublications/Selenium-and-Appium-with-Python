
mySet = {1, 2, 3, 4, 5}

mySet2 = {"apple", "banana", "cherry"}

print(type(mySet))
print(type(mySet2))

# Creating a set from a list of integers
myList = [1, 2, 3, 4, 5,  5]
mySet = set(myList)
print(mySet)

# Creating a set from a tuple of strings
myTuple = ("apple", "banana", "cherry", "apple")
mySet2 = set(myTuple)
print(mySet2)

# Creating a set from a string
myString = "hello"
mySet3 = set(myString)
print(mySet3)



# Union operation
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)

# Intersection operation
set3 = {3, 4, 5}
intersection_set = set2.intersection(set3)
print(intersection_set)

# Difference operation
set4 = {1, 2, 3, 4, 5}
set5 = {4, 5, 6, 7, 8}
difference_set = set4.difference(set5)
print(difference_set)

# Symmetric difference operation
symmetric_difference_set = set4.symmetric_difference(set5)
print(symmetric_difference_set)

