#Avoid deadlock 
# 1. Always acquire locks in the same order

import threading
import time 

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread1():
    with lock_a:
        time.sleep(1)
        with lock_b:
            print("Thread 1 acquired both locks")

def thread2():
    with lock_a: # same order as thread1
        time.sleep(1)
        with lock_b:
            print("Thread 2 acquired both the locks")

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()
t1.join()
t2.join()