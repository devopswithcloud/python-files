
# abstraction_workbook.py

from abc import ABC, abstractmethod

# Exercise 1: Abstract class for Animal
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Subclass Dog that implements make_sound
class Dog(Animal):
    def make_sound(self):
        return "Bark!"

# Subclass Cat that implements make_sound
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

def test_animals():
    dog = Dog()
    cat = Cat()
    print("Dog says:", dog.make_sound())
    print("Cat says:", cat.make_sound())

# Exercise 2: Abstract class Vehicle
class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start_engine(self):
        pass

    def description(self):
        return f"{self.name} is a type of vehicle."

# Subclass Car implementing start_engine
class Car(Vehicle):
    def start_engine(self):
        return f"{self.name}'s engine started with a key."

# Subclass Bike implementing start_engine
class Bike(Vehicle):
    def start_engine(self):
        return f"{self.name}'s engine started with a button."

def test_vehicles():
    car = Car("Honda")
    bike = Bike("Yamaha")
    print(car.description())
    print(car.start_engine())
    print(bike.description())
    print(bike.start_engine())

# Exercise 3: Payment system use case
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using Credit Card."

class UpiPayment(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using UPI."

def process_payment(payment: Payment, amount: float):
    print(payment.pay(amount))

def test_payments():
    cc = CreditCardPayment()
    upi = UpiPayment()
    process_payment(cc, 1000)
    process_payment(upi, 750)

if __name__ == "__main__":
    print("== Animal Sounds ==")
    test_animals()
    print("\n== Vehicle Tests ==")
    test_vehicles()
    print("\n== Payment System ==")
    test_payments()
