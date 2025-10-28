import threading
import queue
import time
import timeit

q = queue.Queue()

def producer():
    for i in range(5):
        print(f"Producter :putting {i}")
        q.put(i)
        time.sleep(0.5)
        q.put(None) # singles to consumer to stop 

def consumer():
    while True:
        item =q.get()
        if item is None: #stop signal
            break
        print(f"Consumer :got {item}")
        q.task_done()

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()
t1.join()
t2.join()