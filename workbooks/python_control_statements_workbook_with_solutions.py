
# 📘 Python Control Statements Workbook with Solutions

# 1. if-else Statement
age = 18
if age >= 18:
    print("1. You are eligible to vote.")
else:
    print("1. You are not eligible to vote.")

# 2. if-elif-else Ladder
marks = 85
if marks >= 90:
    print("2. Grade: A")
elif marks >= 75:
    print("2. Grade: B")
elif marks >= 60:
    print("2. Grade: C")
else:
    print("2. Grade: F")

# 3. Nested if
num = 10
if num >= 0:
    if num == 0:
        print("3. Zero")
    else:
        print("3. Positive number")
else:
    print("3. Negative number")

# 4. while Loop
print("4. while loop from 1 to 5:")
i = 1
while i <= 5:
    print(i)
    i += 1

# 5. for Loop
print("5. for loop over list:")
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# 6. range() in for Loop
print("6. for loop with range:")
for i in range(1, 6):
    print(i)

# 7. break Statement
print("7. break example:")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# 8. continue Statement
print("8. continue example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 9. pass Statement
print("9. pass example:")
for i in range(1, 4):
    if i == 2:
        pass  # placeholder for future code
    print(i)

# 10. else with Loop
print("10. else with for loop:")
for i in range(3):
    print(i)
else:
    print("Loop completed without break")
