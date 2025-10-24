import threading

def print_numbers():
    for i in range(5):
        print(f"Number:{i}")

#creating a thread 
t1 = threading.Thread(target=print_numbers)

   #start the thread
t1.start()

#wait for the thread to finish 
t1.join()
print("Main thread finsished")