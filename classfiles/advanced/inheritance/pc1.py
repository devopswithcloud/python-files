
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def honk(self):
        print("sound horn")

# The above is an interface vehicle defines required methods  but no logic
    
class Car(Vehicle):
    def start_engine(self):
        print("car engine started")
    
    def stop_engine(self):
        print("car engine stopped")
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")
    
    def stop_engine(self):
        print("Bike engine stopped")       


print(issubclass(Car,Vehicle))
