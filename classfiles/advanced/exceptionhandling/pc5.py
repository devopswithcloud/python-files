try:
    f =open("file.txt","r")
    #File operation
except FileNotFoundError:
    print("File not found")
finally:
    print("cleaning up")
    f.close()