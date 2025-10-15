# catching multiple exceptions 
#try:
 # some code
#except(ValueError,TypeError):
 # print("Caught either valueError or TypeError")


try:
    num =int(input("enter a number"))
    result =10/num
except(ValueError,ZeroDivisionError):
    print("caught either value error or zero division error")