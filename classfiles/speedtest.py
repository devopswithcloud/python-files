import time
import numpy as np

#using Numpy
start = time.time()
a = np.arange(1000000)
b= a*2
end = time.time()
print("Numpy time", end-start)

# using normal python list
start = time.time()
a =list(range(1000000))
b =[x*2 for x in a]
end = time.time()
print("list time",end-start)
