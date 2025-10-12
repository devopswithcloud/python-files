"""
Python Lambda, Map, Filter, and Reduce - Workbook with Solutions
"""

# 1. Write a lambda function to add 10 to a given number.
add_10 = lambda x: x + 10
print("1. Add 10 to 5:", add_10(5))  # Output: 15

# 2. Use lambda to multiply two numbers.
multiply = lambda a, b: a * b
print("2. Multiply 3 and 4:", multiply(3, 4))  # Output: 12

# 3. Use filter() to get only even numbers from the list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("3. Even numbers:", even_numbers)  # Output: [2, 4, 6, 8, 10]

# 4. Use map() to square all numbers in the list.
squared = list(map(lambda x: x ** 2, numbers))
print("4. Squared numbers:", squared)

# 5. Use reduce() to multiply all numbers in a list.
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("5. Product of all numbers:", product)

# 6. Sort a list of tuples using lambda based on second item.
students = [("Alice", 87), ("Bob", 95), ("Carol", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("6. Students sorted by score:", sorted_students)

# 7. Use map() with lambda to convert a list of strings to uppercase.
words = ["apple", "banana", "cherry"]
uppercase_words = list(map(lambda x: x.upper(), words))
print("7. Uppercase words:", uppercase_words)

# 8. Use filter() with lambda to find names longer than 4 characters.
names = ["John", "Ali", "Alexander", "Bob", "Catherine"]
long_names = list(filter(lambda x: len(x) > 4, names))
print("8. Long names:", long_names)

# 9. Use lambda to return the maximum of two numbers.
maximum = lambda a, b: a if a > b else b
print("9. Max of 10 and 15:", maximum(10, 15))

# 10. Use reduce() to concatenate a list of strings.
words = ["Python", "is", "awesome"]
sentence = reduce(lambda x, y: x + " " + y, words)
print("10. Concatenated sentence:", sentence)
