
# Raising an exception manually this is a built in exception
def divide(a,b):
    if b==0:
        raise ZeroDivisionError("You cannot divide by zero")
    return a/b

try:
    result =divide(10,0)
except ZeroDivisionError as e:
    print(f"Error :{e}")