from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
       pass

    def description(self):
        print("This is a shape")

class Circle(Shape):
    def __init__(self,radius):
        self.radius =radius

    def area(self):
        return 3.14 * self.radius* self.radius

c =Circle(5)
print("Area",c.area())
c.description()
 