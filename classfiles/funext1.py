
def greet(name):  #name is a parameter
    print("function greeting",name)


greet("Python") # python is an argument

def student(name="class",grade=10):
    print(name,"is in grade",grade)

student()
student("ravi")
student(name="chandu",grade=12) # keyword argument they are passed using the parameter name

def square(x):
    return x*x

result =square(5)
print(result)

def add_all(*args):
    print(sum(args))

add_all(2,3,4)

def show_details(**kwargs):
    for k,v in kwargs.items():
        print(k,"->",v)
show_details(name ="hh",age =30)


def add(a,b):
    return a+b

result =add(5,3)
print(result)







    


