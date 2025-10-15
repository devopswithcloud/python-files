from functools import reduce

add =lambda x,y:x+y
print(add(3,5))

square =lambda x:x *x
print(square(4))


numbers =[1,2,3,4,5,6]
even =list(filter(lambda x:x%2==0,numbers))
print(even)

numbers =[1,2,3,4]
squared =list(map(lambda x:x**2,numbers))
print(squared)

product = reduce(lambda x,y:x*y,numbers)
print(product)

students = [("Alice", 87), ("Bob", 95), ("Carol", 78)]

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)

students = [("Alice", 87), ("Bob", 95), ("Carol", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("6. Students sorted by score:", sorted_students)




