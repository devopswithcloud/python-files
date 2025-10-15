from abc import ABC , abstractmethod
import math

#interface
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

#circle class implementing shape
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius= radius

    def area(self):
        return  math.pi *self.radius **2
    
    def perimeter(self):
        return  2* math.pi* self.radius


class Rectange(Shape):
     def __init__(self,width,height):
        self.width= width
        self.height =height

     def area(self):
        return self.width * self.height
    
     def perimeter(self):
        return  2* (self.width +self.height)


#polymorphic function 
     
def print_shape_info(shape:Shape):
    print(f"shape type",{type(shape).__name__})
    print(f"Area:{shape.area():.2f}")

#main porgram

if __name__ =="__main__":
    shapes=[
        Circle(5),
        Rectange(4,6)
    ]    

    for shape in shapes:
        print_shape_info(shape)

