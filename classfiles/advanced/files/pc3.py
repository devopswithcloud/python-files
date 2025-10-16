with open("example.txt","r") as f:
    print(f.tell()) #0 at start
    f.read(5) # reads 5 chars
    print(f.tell()) # 5 char
    print(f.seek(3)) # move back to start

#seek(offset,whence) -> moves coursor
    #0  from start (default)
    #1   from current position 
    #2 - from end 

#flush() : forces writing data from buffer to disk
    
ff = open("data.txt","w")
ff.write("important data")   
ff.flush()
f.close()
    
