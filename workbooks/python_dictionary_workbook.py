
# Python Dictionary Workbook with Solutions

# 1. Creating a Dictionary
student = {"name": "Alice", "age": 21, "course": "Python"}
print("1. Dictionary:", student)

# 2. Dictionary with mixed keys
mixed = {1: "One", "Two": 2, (3, 4): "Tuple key"}
print("2. Mixed Keys:", mixed)

# 3. Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print("3. Dictionary Comprehension:", squares)

# 4. Accessing elements
print("4. Access name:", student["name"])

# 5. Reassigning values
student["age"] = 22
print("5. Reassigned age:", student)

# 6. Deleting an item
del student["course"]
print("6. After Deletion:", student)

# 7. Built-in functions
print("7. Keys:", student.keys())
print("   Values:", student.values())
print("   Items:", student.items())
print("   Length:", len(student))

# 8. Membership test
print("8. Is 'age' in student?", 'age' in student)
print("   Is 'grade' in student?", 'grade' in student)

# 9. Iterating over dictionary
print("9. Iterating over items:")
for key, value in student.items():
    print(f"   {key}: {value}")

# 10. Merging dictionaries
extra_info = {"grade": "A", "pass": True}
student.update(extra_info)
print("10. After Merging:", student)
