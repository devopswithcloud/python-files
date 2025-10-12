
# 📘 Python Tuple Workbook with Solutions

# 1. Tuple Packing and Unpacking
print("Exercise 1: Packing and Unpacking")
t = ("apple", "banana", "cherry")
a, b, c = t
print("Unpacked:", a, b, c)

# 2. Single Item Tuple
print("\nExercise 2: Single Item Tuple")
single = ("apple",)
print("Type:", type(single))

# 3. Accessing Tuple Items
print("\nExercise 3: Accessing Tuple Items")
fruits = ("apple", "banana", "cherry")
print("First:", fruits[0])
print("Last:", fruits[-1])

# 4. Slicing
print("\nExercise 4: Slicing")
print("Slice 0:2 ->", fruits[0:2])
print("Slice -2: ->", fruits[-2:])

# 5. Tuple Length
print("\nExercise 5: Length")
print("Length of tuple:", len(fruits))

# 6. Tuple Functions
print("\nExercise 6: Tuple Functions")
t = (1, 2, 2, 3, 4)
print("Max:", max(t))
print("Min:", min(t))
print("Count of 2:", t.count(2))
print("Index of 3:", t.index(3))

# 7. Deleting Tuple
print("\nExercise 7: Deleting a Tuple")
sample = (1, 2, 3)
print("Before deletion:", sample)
del sample
# print(sample)  # Uncomment to test NameError

# 8. Tuple Reassignment
print("\nExercise 8: Tuple Reassignment")
my_tuple = (5, 6)
print("Original:", my_tuple)
my_tuple = (7, 8)
print("Reassigned:", my_tuple)

# 9. Extended Unpacking
print("\nExercise 9: Extended Unpacking")
x, *y = (10, 20, 30, 40)
print("x:", x, "y:", y)

# 10. Membership Test
print("\nExercise 10: Membership Test")
numbers = (1, 2, 3, 4, 5)
print("3 in numbers?", 3 in numbers)
print("6 in numbers?", 6 in numbers)
