#approach2  using try-lock pattern with acquire(timeout)
#This lets the thread giveup if it cant get a lock with in the given time

import threading
import time 

lock = threading.Lock()

def worker(name,wait_before_try):
    time.sleep(wait_before_try)
    print(f"{name} trying to acquire lock ")

    #try to acquire lock with a timeout of 2 seconds

    acquired = lock.acquire(timeout=2)
    if acquired:
        try:
            print(f"{name} acquired lock  ")
            time.sleep(10)
        finally:
            print(f"{name} releasing lock  ")
            lock.release()
    else:
       print(f"{name} could not acuqire the  lock  ")
         
t1 = threading.Thread(target=worker,args=("Thread-1",0))
t2 = threading.Thread(target=worker,args=("Thread-2",1))

t1.start()
t2.start()
t1.join()
t2.join()

    