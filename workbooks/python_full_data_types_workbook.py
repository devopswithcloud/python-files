
# 📘 Python Data Types Workbook

# ▶️ Exercise 1: Static vs Dynamic Typing
# Python is dynamically typed. Prove it by assigning different data types to the same variable.

x = 10
print(f"x = {x}, type = {type(x)}")
x = "hello"
print(f"x = {x}, type = {type(x)}")

# ▶️ Exercise 2: Type Conversions
# Convert and print the types of the following:
a = "123"
b = 45.67
c = int(float("89.9"))
d = str(100)
e = float("456.78")
print(type(a), type(b), type(c), type(d), type(e))

# ▶️ Exercise 3: Constants by Convention
# Python doesn't have built-in constants, but we use uppercase for constants by convention.
PI = 3.14159
GRAVITY = 9.8
radius = 5
area = PI * radius * radius
print(f"Area of circle = {area}")

# ▶️ Exercise 4: None Type
nothing = None
print(nothing)
print(type(nothing))
if nothing is None:
    print("Yes, it's None!")

# ▶️ Exercise 5: Numbers
int_num = 100
float_num = 123.45
complex_num = 2 + 3j
print(type(int_num), type(float_num), type(complex_num))

# ▶️ Exercise 6: Sequences - Strings and Lists
my_str = "Python"
my_list = ["apple", "banana", "cherry"]
print(my_str[0], my_str[-1])
my_list.append("orange")
print(my_list)

# ▶️ Exercise 7: Tuples and Ranges
my_tuple = (10, 20, 30)
print(my_tuple[1])
for i in range(1, 6):
    print(i)

# ▶️ Exercise 8: Sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# ▶️ Exercise 9: Dictionaries (Maps)
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print(student["name"])
print(student.get("age"))

# ▶️ Exercise 10: Challenge
# Create a dictionary with your favorite 3 movies as keys and their release years as values.
# Print the dictionary and use a loop to display each key-value pair.
