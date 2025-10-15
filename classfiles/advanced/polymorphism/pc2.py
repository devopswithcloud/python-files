#method overloading python doesnt support it directly 
#The below will not work

class Greet:
    def hello(self,name):
        print("Hello",name)
    
    def hello(self):
        print("Hello")
    
g = Greet()
g.hello("Pythonpyt")
