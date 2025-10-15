import array
arr = array.array('i',[10,20,30,40,50,60])

print(arr[1:4]) # prints element from 1 to 3  [20,30,40]
print(arr[:3]) #prints from start to index2 - [10,20,30]
print(arr[3:]) # from index 3 to end  - [40,50,60]
print(arr[::2]) # every 2nd element -[10,30,50]


print(arr[-3:]) #last 3 elements -[40,50,60]
print(arr[:-2]) # everyting except last2 [10,20,30,40]
print(arr[::-1]) # reverses the arry 


