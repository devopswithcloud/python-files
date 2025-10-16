with open("datanew.txt",'w') as f:
    f.write('Hello , this is an example file.')

with open('datanew.txt','rb') as f:
   # print(f.seek(7,0))
  #  print(f.read())
    #f.seek(7,0)
    f.seek(5,1)
    print(f.read())
    
with open("image.png","rb") as src,open("copy.png","wb") as dest:
    dest.write(src.read())


with open("C:/users/yourname/pictures/myphoto.jpg","rb") as file:
    data =file.read()

with open("destination_folder/copied_image.jpg","wb") as dest_file:
    dest_file.write(data)  
