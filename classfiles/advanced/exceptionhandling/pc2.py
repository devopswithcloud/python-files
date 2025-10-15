try:
    num =int(input("enter a number"))
    result =10/num
except ZeroDivisionError:
    print("Youcannot divide by zero")
except ValueError:
    print("invalid input,Please enter a valid number")
else:
    print("Result",result)
finally:
    print("This block always run")