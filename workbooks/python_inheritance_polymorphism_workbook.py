"""
Python Inheritance and Polymorphism Workbook with Solutions
"""

# 1. Single Inheritance Example
class Animal:
    def speak(self):
        return "Animal Sound"

class Dog(Animal):
    def bark(self):
        return "Woof!"

# Test Single Inheritance
dog = Dog()
print(dog.speak())  # Inherited
print(dog.bark())   # Own method


# 2. Constructor in Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

# Test Constructor
student = Student("Alice", "A")
print(student.name)
print(student.grade)


# 3. Method Overriding and super()
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()
        print("Child method")

child = Child()
child.show()


# 4. Types of Inheritance: Multiple
class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def skills(self):
        print("Art, Cooking")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Dance")

child = Child()
child.skills()


# 5. Method Resolution Order (MRO)
class A:
    def whoami(self):
        print("A")

class B(A):
    def whoami(self):
        print("B")

class C(A):
    def whoami(self):
        print("C")

class D(B, C):
    pass

d = D()
d.whoami()  # Output will be from B due to MRO


# 6. Duck Typing
class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Grammar Check")
        print("Running")

class Laptop:
    def code(self, ide):
        ide.execute()

laptop = Laptop()
laptop.code(Pycharm())  # Can be replaced with MyEditor()


# 7. Polymorphism - Method Overloading (achieved with default args)
class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5, 10))
print(calc.add(5, 10, 20))


# 8. Polymorphism - Method Overriding (already shown above)


# 9. Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Uses __add__
