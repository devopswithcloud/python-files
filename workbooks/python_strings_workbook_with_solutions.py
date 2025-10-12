"""
📘 Python Strings Workbook with Solutions
-----------------------------------------
Covers:
- String declaration and operations
- Indexing and slicing
- String methods
- Escape characters
- String formatting
"""

# 1️⃣ String Declaration

# Q1. Declare a string variable with your name and print it
name = "Shashank"
print(name)


# 2️⃣ Indexing and Slicing

text = "PythonProgramming"

# Q2. Print the first character
print(text[0])  # Output: P

# Q3. Print the last character
print(text[-1])  # Output: g

# Q4. Print characters from index 2 to 6
print(text[2:7])  # Output: thonP

# Q5. Print the string in reverse
print(text[::-1])  # Output: gnimmargorPnohtyP


# 3️⃣ String Methods

sample = "  Hello, Python!  "

# Q6. Use strip() to remove spaces
print(sample.strip())  # Output: Hello, Python!

# Q7. Use lower() and upper()
print(sample.lower())  # Output:   hello, python!
print(sample.upper())  # Output:   HELLO, PYTHON!

# Q8. Use replace() to change 'Python' to 'World'
print(sample.replace("Python", "World"))  # Output:   Hello, World!

# Q9. Find the index of 'o'
print(sample.find("o"))  # Output: 7

# Q10. Split the string by ','
print(sample.split(","))  # Output: ['  Hello', ' Python!  ']


# 4️⃣ Escape Characters

# Q11. Print the string: He said, "Hello!"
print("He said, \"Hello!\"")  # Output: He said, "Hello!"

# Q12. Print the following on two lines:
# Line1
# Line2
print("Line1\nLine2")  # Output:
# Line1
# Line2


# 5️⃣ String Formatting

name = "Alice"
age = 25

# Q13. Use f-string to print: My name is Alice and I am 25 years old.
print(f"My name is {name} and I am {age} years old.")

# Q14. Use format() to print the same string
print("My name is {} and I am {} years old.".format(name, age))
