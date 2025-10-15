student ={
   "name":"r",
   "age":2,
   "grade":"a" 
}

# dict() constructor
car =dict(brand="Toyata",model="coralla",year=2020)

my_dict={
    1:"one",
    "two":2,
    (3,4):"tuple key"
}
#accessing values []
print(car["brand"])

# using get()
print(car.get("model"))
print(car.get("color","N/A"))
#Reassigning & adding a values
car["year"] =2025
print(car)
car["color"]="white"
print(car)

#deleting items
del car["model"]
print(car)
car.pop("year")
print(car)
#car.clear()
#print(car)

print("brand" not in car)

#keys
for key in car:
    print(key)

#values
for value in car.values():
    print(value)

#key-value pair

for key,value in car.items():
    print(key,value)

#creating a dictory where keys are numbers from 1 to 5 and valures are there squares
    
square ={x:x**2 for x in range(1,11) if x%2 ==0}
print(square)   

keys ={'a','b','c'}
values=[1,2,3]
combined ={k:v for k,v in zip(keys,values)}
print(combined)


my_dict ={'a':1,'b':2}
my_dict['hey'] =my_dict.pop('a') # renames  a to hey
print(my_dict)

inverted ={v:k for k,v in my_dict.items()}
print(inverted);















