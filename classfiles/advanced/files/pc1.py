f =open("example.txt","r")
content =f.read()
#print(content)
f.close()

#using with (preferred)

with open("example.txt") as f:
    content =f.read(5)
    line1 =f.readline()
    line2 =f.readline()
    
    #File auto closed here


with open("example.txt") as f:
    lines =f.readlines()
    for line in lines:
        print(line.strip())

 
   
    
