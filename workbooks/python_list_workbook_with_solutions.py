
# 📘 Python List Workbook with Solutions

# 1. Accessing list elements
fruits = ["apple", "banana", "cherry"]
print("1. First fruit:", fruits[0])

# 2. Slicing
print("2. Slice fruits[1:3]:", fruits[1:3])

# 3. Negative indexing
print("3. Last fruit using negative index:", fruits[-1])

# 4. Reassigning an element
fruits[1] = "blueberry"
print("4. Modified fruits list:", fruits)

# 5. Deleting an element
del fruits[2]
print("5. After deleting third fruit:", fruits)

# 6. Multidimensional list
matrix = [[1, 2, 3], [4, 5, 6]]
print("6. Element at matrix[1][2]:", matrix[1][2])

# 7. Concatenation
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2
print("7. Concatenated list:", combined)

# 8. Membership test
print("8. Is 3 in combined list?", 3 in combined)

# 9. Iteration over list
print("9. Iterating over combined list:")
for item in combined:
    print(item)

# 10. Built-in functions
numbers = [10, 20, 30, 40]
print("10. Max:", max(numbers))
print("10. Min:", min(numbers))
print("10. Sum:", sum(numbers))
print("10. Length:", len(numbers))
