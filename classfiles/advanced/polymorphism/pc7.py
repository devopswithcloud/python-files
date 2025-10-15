#example wit out duck typing 
class Duck:
    def quack(self):
        print("Quack")

class Person:
    def quack(self):
        print("I am quacking like a duck")

def make_it_quack(entity):
        entity.quack()
  
        
d= Duck()
p = Person()

make_it_quack(d)  #quack 
make_it_quack(p)   # nota duckt

# hear person has a quack() method but it isnt a duck
