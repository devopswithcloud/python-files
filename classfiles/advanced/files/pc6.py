import os

file_path = os.path.join("images","my_photo.jpg")
with open(file_path,"rb") as file:
    data = file.read()