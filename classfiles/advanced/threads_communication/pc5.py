import threading

shared_data =None
lock = threading.Lock()

def writer():
    global shared_data
    with lock:
        shared_data ="Hello for writer"

def reader():
    with lock:
        print(shared_data)

t1 = threading.Thread(target=writer)
t2 = threading.Thread(target=reader)
t1.start()
t2.start()
t1.join()
t2.join()