from string import Template
name ="Python"
version= 3
print(f"My system ,{name} will be {version} on it")

print(" My system is{} and will be on {}".format(version,name))

#positional or named placeholder

print(" My system is{1} and will be on {0}".format(version,name))

print(" My system is{name} and will be on {age}".format(name="xyz",age=25))

print(" My system is %s and will be on %d"%(name,version))

t =Template(" My name is $name and i am $age years")
print(t.substitute(name="Ravi",age=22))
print(t.substitute(name="Charan",age=40))

