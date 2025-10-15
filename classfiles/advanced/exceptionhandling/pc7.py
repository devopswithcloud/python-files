# nested try exception 

try:
    try:
        x =int(input("Enter a number"))
        y =10/x
    except ZeroDivisionError:
        print("Cant divide by zero")
except ValueError:
    print("Invalid number")