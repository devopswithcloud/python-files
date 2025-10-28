import threading
import time 
import random

# creating a semaphore with a maximum of 3 concurrent threads
semaphore = threading.Semaphore(2)

def worker(thread_id):
    print(f"Thread {thread_id} waiting for access...")
    with semaphore: # acquire the semaphore
        print(f"Thread {thread_id} acquired semaphore")
        #simulate some work 
        time.sleep(random.uniform(1,3))
        print(f" Thread {thread_id} releasing semaphore")

threads =[]

for i in range(10):
    t = threading.Thread(target=worker,args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All threds completed")