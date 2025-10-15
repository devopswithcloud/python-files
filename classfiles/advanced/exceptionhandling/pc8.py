class NegativeNumberError(Exception):
    pass

def square_root(x):
    if(x <0):
        raise NegativeNumberError(" cannot use negative numbers")
    return x **0.5

try:
    result =square_root(-9)
except NegativeNumberError as e:
    print(f"custom error:{e}")