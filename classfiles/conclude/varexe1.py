count =0 # global vriable

def increment():
    global count
    count +=1 #  mofifying the global variable
    print("inside function",count)

increment()
increment()

print("fincal function",count)