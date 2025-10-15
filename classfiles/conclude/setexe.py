my_set ={1,2,3}
print(my_set)
fruits =set(["apple",'banana'])  # set constructor 

empty_set =set()
empty_set.add("orange")  # adding a single element

empty_set.update(["grape","orange"])  # adding multiples

print(empty_set)

empty_set.remove("apple")
print(empty_set)

a ={1,2,3}
b ={3,4,5}
print(a.union(b))     #a|b 
print(a.intersection(b))  # a&&b
print(a.difference(b)) #a-b
print(a.symmetric_difference(b))  #a^b

print("apple" not in empty_set)

fs = frozenset([1,2,3])

