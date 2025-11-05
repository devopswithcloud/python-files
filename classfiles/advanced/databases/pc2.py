#iterator
my_list =[1,2,3]
my_iter =iter(my_list)  #get iterator object
print(next(my_iter))  #1
print(next(my_iter))  #2
print(next(my_iter)) #3
print(next(my_iter)) #Raises stop iteratortion