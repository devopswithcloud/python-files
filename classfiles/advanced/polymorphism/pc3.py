#method overloading python doesnt support it directly 
#It is possible by using default arguments

class Greet:
    def hello(self,name=None):
        if name:
            print("Hello",name)
        else:
            print("Hello!")
        
    
g = Greet()
g.hello()
g.hello("Pythonpyt")
