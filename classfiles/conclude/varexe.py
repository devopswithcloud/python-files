x=10 # global variable

def func():
    x=5 # local variable
    print("localx",x)

func()
print("global x",x)

y= 10

def modify():
    global y
    y=20

modify()
print(y)