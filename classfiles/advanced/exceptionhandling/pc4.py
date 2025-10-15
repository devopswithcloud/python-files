# using as to Access Exception object

try:
    x =int("abc")
except ValueError as e:
    print(e)


