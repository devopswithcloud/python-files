def outer():
    x =10 # enclosing non local variable

    def inner():
        nonlocal x
        x +=5
        print("insid inser",x)
    
    inner()
    print("inside outer",x)

outer()