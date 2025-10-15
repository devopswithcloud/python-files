
from abc import ABC,abstractmethod

class Vechile(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vechile):
    def start(self):
        print("Cart started")

    def stop(self):
        print("Car stopped")

car = Car()
car.start()
car.stop()