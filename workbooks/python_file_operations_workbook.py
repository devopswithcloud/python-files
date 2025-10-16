"""
Python File Operations & Directory Handling Workbook
Includes: Explanations, Examples, and Practice Exercises with Solutions
"""

import os
from pathlib import Path

# ==============================
# SECTION 1: FILE OBJECT METHODS
# ==============================

# Example file to work with
file_path = "sample.txt"

# Writing to a file
with open(file_path, "w") as f:
    f.write("Hello, Python!\n")
    f.write("This is a file handling example.\n")
    f.writelines(["Line 3\n", "Line 4\n"])

# Reading the whole file
with open(file_path, "r") as f:
    content = f.read()
print("Read entire file:\n", content)

# Reading line by line
with open(file_path, "r") as f:
    first_line = f.readline()
    second_line = f.readline()
print("First line:", first_line.strip())
print("Second line:", second_line.strip())

# Reading all lines into a list
with open(file_path, "r") as f:
    lines = f.readlines()
print("List of lines:", lines)

# Demonstrating seek() and tell()
with open(file_path, "r") as f:
    print("Initial position:", f.tell())
    f.seek(7)  # Move to position 7
    print("Position after seek:", f.tell())
    print("Data from position 7:", f.read())

# ==============================
# SECTION 2: DIRECTORY HANDLING
# ==============================

# Current working directory
print("Current working directory:", os.getcwd())

# Creating a new directory
dir_name = "test_dir"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Directory '{dir_name}' created.")

# Listing directory contents
print("Contents of current directory:", os.listdir())

# Renaming a directory
new_dir_name = "renamed_dir"
if os.path.exists(dir_name):
    os.rename(dir_name, new_dir_name)
    print(f"Directory renamed to '{new_dir_name}'.")

# Removing a directory
if os.path.exists(new_dir_name):
    os.rmdir(new_dir_name)
    print(f"Directory '{new_dir_name}' removed.")

# Using pathlib for directory handling
p = Path("pathlib_dir")
p.mkdir(exist_ok=True)
print("Pathlib created directory:", p)

# ==============================
# SECTION 3: EXERCISES
# ==============================

# Exercise 1: Create a file and write your name and age into it.
def exercise_1():
    with open("exercise1.txt", "w") as f:
        f.write("Name: John Doe\n")
        f.write("Age: 25\n")
    print("Exercise 1 completed: File created with name and age.")

# Exercise 2: Read the contents of 'exercise1.txt' and print them.
def exercise_2():
    with open("exercise1.txt", "r") as f:
        print("Exercise 2 file content:\n", f.read())

# Exercise 3: Create a directory named 'my_data' and inside it create a file 'data.txt'.
def exercise_3():
    os.makedirs("my_data", exist_ok=True)
    with open("my_data/data.txt", "w") as f:
        f.write("Sample data inside my_data/data.txt")
    print("Exercise 3 completed: Directory and file created.")

# Exercise 4: List all files in the current directory.
def exercise_4():
    print("Files in current directory:", [f for f in os.listdir() if os.path.isfile(f)])

# Exercise 5: Delete the file 'exercise1.txt'.
def exercise_5():
    if os.path.exists("exercise1.txt"):
        os.remove("exercise1.txt")
        print("Exercise 5 completed: 'exercise1.txt' deleted.")

# Run solutions
if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
