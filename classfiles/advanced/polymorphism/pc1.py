#Operator overloading 
 # python allows us to change the behaviour of operators like + ,-,== etc
# example to see overloading of + in custom class

class Point:
    def __init__(self,x,y):
        self.x =x
        self.y=y
    
    def __mul__(self,other): #overload '+ (a+b)
        return Point(self.x*other.x,self.y*other.y)
    
    def __str__(self): # makes our custom object more readable and user friendly when printing
        return f"({self.x},{self.y})"

p1 = Point(2,3)
p2 = Point(4,5)
result =p1*p2
print(result)  #(6,8)