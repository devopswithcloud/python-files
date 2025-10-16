with open("output.txt","w") as f:
    f.write("Hello world \n")
    f.write("Python is awesome")


#writelines() - writes list of strings

lines =["First line\n","second line\n"]
with open("output.txt","w") as f:
    f.writelines(lines)    

with open("output.txt","a") as f:
    f.write("\n new line to be added")  
