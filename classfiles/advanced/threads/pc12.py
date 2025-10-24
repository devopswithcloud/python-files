#dead lock scenerio
import threading
import time 

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread1():
    with lock_a:
        print("Thread 1 acquired lock_a")
        time.sleep(1)
        with lock_b:
            print("Thread 1 acquired lock b")

def thread2():
    with lock_b:
        print("Thread 2 acquired lock_b")
        time.sleep(1)
        with lock_a:
            print("Thread 2 acquired lock a")

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()
t1.join()
t2.join()