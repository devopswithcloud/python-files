"""
Python Interfaces - Workbook with Exercises and Solutions
"""

from abc import ABC, abstractmethod

# ---------------------------
# Section 1: Basic Interface
# ---------------------------

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Exercise 1: Implement the Shape interface for a Rectangle

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Exercise 2: Implement the Shape interface for a Circle

import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# ---------------------------
# Section 2: Interface with Default Method
# ---------------------------

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def honk(self):
        print("Beep beep!")


class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")


# ---------------------------
# Section 3: Polymorphism using Interface
# ---------------------------

def vehicle_test(v: Vehicle):
    v.start_engine()
    v.honk()


# ---------------------------
# Section 4: Try it Yourself
# ---------------------------

# Exercise 3:
# Create an interface called 'Storage' with methods save(data) and load().
# Implement this interface in two classes: LocalStorage and CloudStorage.
# Provide different print statements for each method in both classes.

# Exercise 4:
# Use polymorphism to test both storage classes using a common function.

