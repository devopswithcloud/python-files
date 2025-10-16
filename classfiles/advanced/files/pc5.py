from pathlib import Path

file_path = Path("images")/"my_photo.jpg"
with open(file_path,"rb") as file:
    data = file.read()